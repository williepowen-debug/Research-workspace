#!/usr/bin/env python3
"""MARCO Google Trends puller — feeds VX-MARCO-GTR-01 (Tourism Intent).

Why this exists: GTR-01 sat 157 days stale (Feb → Jul 2026) not because the data
was unavailable — Google Trends is free and live — but because the only path was a
MANUAL CSV export from the web UI. A metric whose refresh depends on someone
remembering to click is a metric that rots. This automates it.

No pytrends dependency (not installed, and adding to the shared .venv is a
cross-agent change). Uses the same two-step the UI does:
  1. /trends/api/explore  -> returns widgets, one of which carries a TIMESERIES token
  2. /trends/api/widgetdata/multiline -> the weekly index, given that token

Both responses are prefixed with `)]}'` which must be stripped before JSON parsing.

Index caveat that governs every reading: Google Trends is **relative, 0-100 scaled
within the requested window**. It is NOT a volume count, and two separately-pulled
series are NOT comparable to each other. Only compare points inside one pull.

Usage:
  .venv/bin/python3 AGENTS/MARCO/tools/google_trends_pull.py
  .venv/bin/python3 AGENTS/MARCO/tools/google_trends_pull.py --geo CA --out baselines/
"""
import json
import sys
import time
import urllib.parse
from datetime import datetime
from pathlib import Path

import requests

BASE = "https://trends.google.com/trends/api"
OUT_DIR = Path(__file__).resolve().parents[1] / "baselines"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# The two intents GTR-01 has tracked since founding, WITH their category filters.
# Both must match the Feb-2026 baseline exports byte-for-byte in definition:
#   baselines/google_trends_flights_to_florida_canada_5yr.csv -> "Category: All categories"
#   baselines/google_trends_florida_travel_canada_5yr.csv     -> "Category: Travel"
# ⚠️ Keep keyword AND category stable. Changing either silently REBASES the index
# and makes the new reading non-comparable to the carried one — which is exactly
# the trap caught on 2026-07-31 (a first pass used bare "florida vacation"/all-cats
# and produced a number that looked like a continuation of the series but wasn't).
TERMS = [("flights to florida", 0), ("florida", 67)]      # 67 = Travel category
DEFAULT_GEO = "CA"          # Canada — the snowbird-origin market Channel 2 cares about
WINDOW = "today 5-y"


def _strip(txt):
    """Google prefixes JSON with )]}' — strip to the first brace."""
    i = txt.find("{")
    if i < 0:
        raise RuntimeError(f"no JSON in response: {txt[:120]!r}")
    return json.loads(txt[i:])


def session():
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    try:
        s.get("https://trends.google.com/trends/", timeout=45)   # cookie warmup
    except requests.RequestException:
        pass
    return s


def fetch_series(s, keyword, cat=0, geo=DEFAULT_GEO, window=WINDOW):
    """-> list of (date_str, index_int). Raises on any failure — no silent empties."""
    req = {"comparisonItem": [{"keyword": keyword, "geo": geo, "time": window}],
           "category": cat, "property": ""}
    url = f"{BASE}/explore?hl=en-US&tz=0&req=" + urllib.parse.quote(json.dumps(req))
    r = s.get(url, timeout=90)
    r.raise_for_status()
    widgets = _strip(r.text)["widgets"]
    w = next((x for x in widgets if x.get("id") == "TIMESERIES"), None)
    if w is None:
        raise RuntimeError(f"no TIMESERIES widget for {keyword!r} (ids: "
                           f"{[x.get('id') for x in widgets]})")
    murl = (f"{BASE}/widgetdata/multiline?hl=en-US&tz=0"
            f"&req={urllib.parse.quote(json.dumps(w['request']))}"
            f"&token={urllib.parse.quote(w['token'])}")
    # Trends rate-limits hard (429) on back-to-back terms. Back off rather than
    # let a throttle read as "no data" — a 429 swallowed is a silent gap.
    last = None
    for attempt, wait in enumerate((2, 15, 45, 90)):
        time.sleep(wait)
        r2 = s.get(murl, timeout=90)
        if r2.status_code == 200:
            break
        last = r2.status_code
        print(f"     · {keyword!r} HTTP {last}, retry {attempt + 1}/4")
    else:
        raise RuntimeError(f"rate-limited after 4 attempts (last HTTP {last})")
    pts = _strip(r2.text)["default"]["timelineData"]
    out = [(p["formattedAxisTime"], p["value"][0]) for p in pts if p.get("value")]
    if not out:
        raise RuntimeError(f"empty timeline for {keyword!r} — treat as FAILURE, not zero")
    return out


def month_mean(series, year, month):
    """Mean weekly index for a calendar month. Trends' formattedAxisTime is like
    'Jul 27, 2026'; parse rather than string-match so this survives locale drift."""
    vals = []
    for label, v in series:
        try:
            d = datetime.strptime(label, "%b %d, %Y")
        except ValueError:
            continue
        if d.year == year and d.month == month:
            vals.append(v)
    return (sum(vals) / len(vals)) if vals else None


def main():
    geo = DEFAULT_GEO
    if "--geo" in sys.argv:
        geo = sys.argv[sys.argv.index("--geo") + 1]
    s = session()
    now = datetime.now()
    # Last COMPLETE month — the current month is partial and would read artificially low.
    y, m = (now.year, now.month - 1) if now.month > 1 else (now.year - 1, 12)

    print(f"Google Trends — geo={geo}, window={WINDOW}, reference month={y}-{m:02d}")
    print("(index is RELATIVE 0-100 within each pull; never compare across pulls)\n")
    results = {}
    for kw, cat in TERMS:
        try:
            ser = fetch_series(s, kw, cat, geo)
        except Exception as e:
            print(f"  ❌ {kw!r}: {type(e).__name__}: {str(e)[:90]}")
            results[kw] = None
            continue
        cur = month_mean(ser, y, m)
        base24 = month_mean(ser, 2024, m)
        base25 = month_mean(ser, 2025, m)
        results[kw] = {"series": ser, "cur": cur, "b24": base24, "b25": base25}
        def pct(a, b):
            return f"{(a/b-1)*100:+.1f}%" if (a and b) else "n/a"
        print(f"  {kw!r} [cat={cat}]  ({len(ser)} weekly points, {ser[0][0]} → {ser[-1][0]})")
        print(f"     {y}-{m:02d} mean index {cur:.1f}" if cur else "     current: n/a")
        print(f"     vs {m:02d}/2024 ({base24:.1f}): {pct(cur, base24)}   "
              f"vs {m:02d}/2025 ({base25:.1f}): {pct(cur, base25)}"
              if base24 and base25 else "     baselines incomplete")
        time.sleep(2)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = f"{now:%Y-%m-%d}"
    for kw, d in results.items():
        if not d:
            continue
        slug = kw.replace(" ", "_")
        f = OUT_DIR / f"google_trends_{slug}_{geo}_{stamp}.csv"
        with open(f, "w") as fh:
            fh.write(f"# MARCO Google Trends | term={kw} | geo={geo} | cat={dict(TERMS)[kw]} | window={WINDOW} "
                     f"| pulled={stamp} | RELATIVE index 0-100, not volume\n")
            fh.write("week,index\n")
            for label, v in d["series"]:
                fh.write(f"{label},{v}\n")
        print(f"\n  wrote {f.name} ({len(d['series'])} rows)")
    return 0 if any(results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
