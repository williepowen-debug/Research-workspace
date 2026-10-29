#!/usr/bin/env python3
"""warn_monthly.py — monthly WARN employees-affected series for T-07 (BD-36, built 2026-10-28).

Source: LayoffAlert.org home page, chart "Mass Layoffs by State – Last 24 Months". The
series lives in the page's embedded `chartConfig` JSON, NOT in the page text. That is why
the 2026-09-29 read (fetch-tool summaries of the text) concluded no monthly figure existed.
Basis: employees affected per month keyed by layoff EFFECTIVE date, ~46 jurisdictions.
SECONDARY aggregator of state WARN notices — tag every figure `[2ND]`.

T-07 (TRADE.md §1, re-specced 2026-10-28): a COMPLETED month with >50,000 employees affected
fires T-07 (→ CARL, REGINALD). Grade month M in month M+1, once late notices have landed.

USAGE
  warn_monthly.py [--months 6] [--state Florida] [--save DIR]

EXIT  0 = read OK, last completed month ≤ 50,000 · 1 = last completed month > 50,000 (T-07)
      2 = UNKNOWN (page not fetched, chart JSON missing or reshaped) — never guess a figure.
"""
import argparse
import datetime as dt
import hashlib
import json
import pathlib
import re
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
import fetch_primary as FP  # noqa: E402

URL = "https://www.layoffalert.org/"
BAR = 50_000
MON = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def label_to_ym(lab):
    """"Sep '26" -> (2026, 9)."""
    m = re.fullmatch(r"([A-Z][a-z]{2}) '(\d\d)", lab.strip())
    if not m:
        raise ValueError(f"unrecognized month label {lab!r}")
    return 2000 + int(m.group(2)), MON[m.group(1)]


def parse(raw):
    t = raw.decode("utf-8", "ignore")
    m = re.search(r"const chartConfig = (\{.*?\});", t, re.S)
    if not m:
        raise ValueError("chartConfig JSON not found — page reshaped")
    cfg = json.loads(m.group(1))
    labs, ds = cfg["labels"], cfg["datasets"]
    if not ds or any(len(d["data"]) != len(labs) for d in ds):
        raise ValueError("datasets do not align with labels")
    upd = re.search(r"Updated ([A-Z][a-z]+ \d{1,2}, 20\d\d)", t)
    rows = []
    for i, lab in enumerate(labs):
        by_state = {d["label"]: (d["data"][i] or 0) for d in ds}
        rows.append((label_to_ym(lab), lab, sum(by_state.values()), by_state))
    return rows, (upd.group(1) if upd else None), len(ds)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--months", type=int, default=6)
    ap.add_argument("--state")
    ap.add_argument("--save", type=pathlib.Path)
    a = ap.parse_args(argv)

    out = a.save or pathlib.Path(tempfile.mkdtemp())
    out.mkdir(parents=True, exist_ok=True)
    path, tries = FP.fetch(URL, out)
    if not path:
        for t in tries:
            print(f"  try  {t}")
        print("UNKNOWN: page not fetched — T-07 ungraded this month, do not estimate")
        return 2
    raw = path.read_bytes()
    try:
        rows, upd, nstates = parse(raw)
    except (ValueError, KeyError, json.JSONDecodeError) as e:
        print(f"UNKNOWN: {e}")
        return 2

    today = dt.date.today()
    completed = [r for r in rows if r[0] < (today.year, today.month)]
    print(f"LayoffAlert monthly [2ND] — page updated {upd or '?'} · {nstates} jurisdictions · "
          f"sha256 {hashlib.sha256(raw).hexdigest()[:16]} · saved {path}")
    print(f"basis: employees affected by layoff EFFECTIVE month; T-07 bar >{BAR:,} on a COMPLETED month")
    for (ym, lab, tot, by) in completed[-a.months:]:
        extra = f"   {a.state}: {by.get(a.state, 'n/a')}" if a.state else ""
        print(f"  {lab}  {tot:>8,}{'  ⚠️ >50K' if tot > BAR else ''}{extra}")
    if not completed:
        print("UNKNOWN: no completed month in the series")
        return 2
    ym, lab, tot, _ = completed[-1]
    verdict = "T-07 FIRES" if tot > BAR else "T-07 not fired"
    print(f"LAST COMPLETED {lab}: {tot:,} → {verdict} (`{BAR:,} − {tot:,} = {BAR - tot:,}`)"
          if tot <= BAR else f"LAST COMPLETED {lab}: {tot:,} → {verdict}")
    return 1 if tot > BAR else 0


if __name__ == "__main__":
    sys.exit(main())
