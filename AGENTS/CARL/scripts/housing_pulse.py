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

FRED_API_KEY = os.environ.get("FRED_API_KEY", "8ce3f08db56f151f54221a0dd12b63de")
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
    """Check Fannie Mae website for latest MF DQ rate. Returns (rate, date) or (None, None)."""
    # Fannie publishes monthly summary at a known URL pattern
    try:
        url = "https://www.fanniemae.com/research-and-insights/multifamily-market-commentary"
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode()
        # Look for delinquency rate patterns
        # Common format: "serious delinquency rate" or "60+ day delinquency"
        m = re.search(r'(?:serious\s+)?delinquency\s+rate[^0-9]*?(\d+\.\d+)%', html, re.IGNORECASE)
        if m:
            return float(m.group(1)), "fanniemae.com"
        return None, None
    except Exception as e:
        return None, f"error: {e}"


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
        print(f"  Could not scrape Fannie MF DQ rate ({mf_source})")
        print(f"  Last known: 0.74% (Feb 2026) \u2014 6bps from GFC peak")
        print(f"  Mar data expected late April \u2014 CRITICAL WATCH")

    # Key housing signals summary
    print(f"\n  KEY HOUSING SIGNALS")
    print(f"  {'-'*68}")
    print(f"  Fannie MF DQ: 0.74% (last known) \u2014 6bps from 0.80% GFC peak")
    print(f"  CMBS MF DQ: 7.15% ATH (Trepp Mar) \u2014 shadow rate 9.07%")
    print(f"  FL Condo: 13.2mo inventory, prices -6.1% YoY")
    print(f"  Existing Home Sales: 3.98M SAAR (approaching <4.0M RED)")
    print(f"  (These are STATUS.md values \u2014 check freshness)")

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
