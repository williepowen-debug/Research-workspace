#!/usr/bin/env python3
"""
CARL Housing Pulse — FRED Housing Series Monitor
Pulls housing-related FRED series, flags direction changes and threshold breaches.
Checks Fannie Mae website for MF DQ update.

Writes to: AGENTS/CARL/scripts/data/HOUSING_PULSE.tsv

Usage:
  .venv/bin/python3 AGENTS/CARL/scripts/housing_pulse.py
"""

import json
import os
import re
import sys
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPTS_DIR / "data"
HSG_TSV = DATA_DIR / "HOUSING_PULSE.tsv"

def _fred_key():
    """Env first, else the gitignored FORGE market-data .env (single per-machine home).
    Hardcoded copies scrubbed 2026-07-01 (public-prep) — never hardcode this key."""
    import pathlib, sys
    k = os.environ.get("FRED_API_KEY", "")
    if k:
        return k
    p = pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/.env"
    if p.exists():
        for line in p.read_text().splitlines():
            if line.startswith("FRED_API_KEY="):
                return line.split("=", 1)[1].strip()
    print("WARN: FRED_API_KEY not found (env or FORGE/tools/market-data/.env) — FRED pulls will fail", file=sys.stderr)
    return ""

FRED_API_KEY = _fred_key()
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

# Housing FRED series: (series_id, label, direction_bad, thresholds)
SERIES = [
    ("MORTGAGE30US", "30yr Mortgage (%)",          "rising",  (5.5, 6.0, 6.5, 7.0)),
    ("HOUST",        "Housing Starts (K, SAAR)",   "falling", (1400, 1200, 1000, 800)),
    ("PERMIT",       "Building Permits (K, SAAR)", "falling", (1400, 1200, 1000, 800)),
    ("EXHOSLUSM495S","Existing Home Sales (M SAAR)","falling", (5000, 4500, 4000, 3500)),
    ("HSN1F",        "New Home Sales (K, SAAR)",   "falling", (700, 600, 500, 400)),
    ("MSPUS",        "Median Home Price ($K)",     "rising",  None),
    ("CSUSHPINSA",   "Case-Shiller National",      "rising",  None),
    ("MSACSR",       "Months Supply (New Homes)",   "rising",  (5.0, 7.0, 9.0, 11.0)),
]

TSV_HEADER = "Run_Date\tSeries\tLabel\tDate\tValue\tPrior\tChange\tPct_Chg\tStatus"


def fred_fetch(series_id, limit=5):
    """Fetch latest FRED observations."""
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": limit,
    }
    url = f"{FRED_BASE}?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CARL-Monitor/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        obs = data.get("observations", [])
        return [{"date": o["date"], "value": o["value"]} for o in obs if o["value"] != "."]
    except Exception as e:
        return [{"error": str(e)}]


def check_fannie_mf():
    r"""RETIRED 2026-09-01. Do not re-enable without reading this comment.

    TWO independent reasons, either of which is sufficient:

    1. DOMAIN. Fannie multifamily serious-DQ was promoted to HOMER on 2026-07-12.
       CARL is not the owner and must not publish a competing figure. Reconcile
       MF numbers with AGENTS/HOMER/, not here.
    2. DEAD URL. The scraped page 404s on every User-Agent (BRENT measured it
       2026-08-21: 404 in 0.2s and 0.6s, browser UA and CARL-Monitor/1.0 alike).
       Not a tarpit, not a UA problem -- the page is gone.

    It also carried the trap BRENT warned about: a bare `(\d+\.\d+)%` grep over
    raw HTML, which on his Baker Hughes page returned his own frozen threshold
    value out of Drupal CSS. A digit-regex over undifferentiated markup can
    fabricate a threshold breach.

    Returns the retirement reason so the caller fails LOUD rather than printing
    a stale literal -- the previous fallback printed "0.74% (Feb 2026)" and
    "Mar data expected late April", both of which were still on screen in
    September against a STATUS that had read 0.58% since July.
    """
    return None, "RETIRED 2026-09-01 - Fannie MF belongs to HOMER (promoted 7/12); scraped URL 404s on every UA (BRENT 8/21)"

def status_for(value, thresholds, direction_bad):
    """Determine status color."""
    if thresholds is None:
        return "TRACK"
    g, y, o, r = thresholds
    if direction_bad == "rising":
        if value >= r:
            return "RED"
        if value >= o:
            return "ORANGE"
        if value >= y:
            return "YELLOW"
        return "GREEN"
    else:
        if value <= r:
            return "RED"
        if value <= o:
            return "ORANGE"
        if value <= y:
            return "YELLOW"
        return "GREEN"


def fmt_val(val, series_id):
    """Format value based on series type."""
    if series_id == "MSPUS":
        return f"${val/1000:.1f}K"
    if series_id in ("HOUST", "PERMIT", "HSN1F"):
        return f"{val:.0f}K"
    if series_id == "EXHOSLUSM495S":
        return f"{val/1000:.2f}M"
    if series_id == "CSUSHPINSA":
        return f"{val:.2f}"
    if series_id == "MSACSR":
        return f"{val:.1f}mo"
    return f"{val:.2f}"


def main():
    now = datetime.now()
    run_date = now.strftime("%Y-%m-%d")
    run_time = now.strftime("%Y-%m-%d %H:%M")

    print(f"\n{'='*72}")
    print(f"  CARL Housing Pulse \u2014 {run_time}")
    print(f"{'='*72}")

    tsv_rows = []

    print(f"\n  FRED HOUSING SERIES")
    print(f"  {'-'*68}")
    print(f"  {'Series':<30} {'Value':>12} {'Change':>10} {'%':>8} {'Status':>8}")
    print(f"  {'-'*68}")

    for series_id, label, direction_bad, thresholds in SERIES:
        obs = fred_fetch(series_id, limit=5)
        if not obs or "error" in obs[0]:
            err = obs[0].get("error", "no data")[:40] if obs else "no data"
            print(f"  {label:<30} {'ERROR':>12}  {err}")
            continue

        try:
            val = float(obs[0]["value"])
            date = obs[0]["date"]
        except (ValueError, KeyError):
            print(f"  {label:<30} {'BAD DATA':>12}")
            continue

        # Prior
        prior = None
        change = None
        pct_chg = None
        if len(obs) > 1:
            try:
                prior = float(obs[1]["value"])
                change = val - prior
                if prior != 0:
                    pct_chg = (change / prior) * 100
            except (ValueError, KeyError):
                pass

        status = status_for(val, thresholds, direction_bad)

        # Direction arrow
        if change is not None:
            if direction_bad == "rising":
                arrow = "\U0001f534" if change > 0 else "\U0001f7e2"
            else:
                arrow = "\U0001f7e2" if change > 0 else "\U0001f534"
        else:
            arrow = "\u26aa"

        val_str = fmt_val(val, series_id)
        chg_str = f"{change:+.1f}" if change is not None else ""
        pct_str = f"{pct_chg:+.1f}%" if pct_chg is not None else ""
        status_str = f"[{status}]" if status != "TRACK" else ""

        print(f"  {arrow} {label:<28} {val_str:>12} {chg_str:>10} {pct_str:>8} {status_str:>8}  ({date})")

        tsv_rows.append("\t".join([
            run_date, series_id, label, date,
            str(val),
            str(prior) if prior is not None else "",
            f"{change:.4f}" if change is not None else "",
            f"{pct_chg:.2f}" if pct_chg is not None else "",
            status,
        ]))

    # Fannie MF DQ check
    print(f"\n  FANNIE MAE MF DELINQUENCY CHECK")
    print(f"  {'-'*68}")
    mf_rate, mf_source = check_fannie_mf()
    if mf_rate:
        mf_status = "RED" if mf_rate >= 0.80 else "ORANGE" if mf_rate >= 0.70 else "YELLOW"
        gap = 0.80 - mf_rate
        print(f"  MF Serious DQ: {mf_rate:.2f}%  [{mf_status}]  (GFC peak 0.80%, gap {gap:+.2f}pp)")
    else:
        print(f"  Fannie MF DQ: NOT PULLED HERE — {mf_source}")
        print(f"  → owner is HOMER (AGENTS/HOMER/); do not cite a CARL figure for MF")

    # Key housing signals summary
    # ⛔ 2026-09-01: the hardcoded block that stood here was DELETED. It printed four
    # literals under a live heading and every one had rotted: "Fannie MF DQ 0.74%"
    # (STATUS had read 0.58% since July), "CMBS MF DQ 7.15% (Trepp Mar)" (June was
    # 7.23%), and "Existing Home Sales: 3.98M SAAR" printed directly BENEATH this
    # script's own live FRED pull of 4.06M -- the hardcode contradicted the fetch on
    # the same screen. Flagged by DAEDALUS (SFG sweep 8/17, housing_pulse.py:226) and
    # confirmed still live at CARL's 9/1 boot.
    # Numbers do not go here. STATUS.md is canonical; this script pulls live series
    # above and says nothing it has not fetched.
    print(f"\n  KEY HOUSING SIGNALS")
    print(f"  {'-'*68}")
    print(f"  (no stored figures — live pulls are above; STATUS.md is canonical)")

    # Write TSV
    DATA_DIR.mkdir(exist_ok=True)
    write_header = not HSG_TSV.exists()
    with open(HSG_TSV, "a") as f:
        if write_header:
            f.write(TSV_HEADER + "\n")
        for row in tsv_rows:
            f.write(row + "\n")
    print(f"\n  Wrote {len(tsv_rows)} rows to {HSG_TSV.relative_to(SCRIPTS_DIR.parent)}")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
