#!/usr/bin/env python3
"""
CARL Consumer Pulse — FRED Economic Series Monitor
Pulls key consumer health series from FRED, compares to prior period,
flags direction changes, and checks against VX thresholds.

Writes to: AGENTS/CARL/scripts/data/CONSUMER_PULSE.tsv (append row per series per run)

Usage:
  .venv/bin/python3 AGENTS/CARL/scripts/consumer_pulse.py
"""

import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPTS_DIR / "data"
PULSE_TSV = DATA_DIR / "CONSUMER_PULSE.tsv"

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

# Series to track: (series_id, label, frequency, direction_bad, thresholds)
# direction_bad: "rising" means higher is worse, "falling" means lower is worse
# thresholds: (green, yellow, orange, red) — values at which status changes
SERIES = [
    # Credit / Delinquency (quarterly)
    ("DRCCLACBS",  "CC DQ Rate (%)",           "quarterly", "rising",  (3.0, 4.0, 5.0, 6.0)),
    ("DRCLACBS",   "Consumer Loan DQ (%)",      "quarterly", "rising",  (2.0, 3.0, 4.0, 5.0)),
    # Savings / Income (monthly)
    ("PSAVERT",    "Personal Savings Rate (%)", "monthly",   "falling", (6.0, 4.0, 3.0, 2.0)),
    ("DSPIC96",    "Real DPI (B$, 2017)",       "monthly",   "falling", None),  # direction only
    # Spending (monthly)
    ("RSXFS",      "Retail Sales ex Food (M$)", "monthly",   "falling", None),  # direction only
    # Sentiment (monthly)
    ("UMCSENT",    "UMich Sentiment",           "monthly",   "falling", (80.0, 65.0, 55.0, 45.0)),
    # Inflation (monthly)
    ("PCEPILFE",   "Core PCE (index)",          "monthly",   "rising",  None),  # direction only, YoY matters
    ("CPIUFDNS",   "CPI Food (index)",          "monthly",   "rising",  None),
    ("CPIENGNS",   "CPI Energy (index)",        "monthly",   "rising",  None),
    # Credit growth (monthly)
    ("TOTALNS",    "Total Consumer Credit (B$)","monthly",   "rising",  None),
    # Labor (weekly / monthly)
    ("ICSA",       "Initial Claims (wkly)",     "weekly",    "rising",  (200000, 250000, 300000, 350000)),
    ("CCSA",       "Continuing Claims",         "weekly",    "rising",  (1700000, 1900000, 2000000, 2200000)),
    # Housing-adjacent
    ("MORTGAGE30US","30yr Mortgage (%)",        "weekly",    "rising",  (5.5, 6.0, 6.5, 7.0)),
    # Spreads
    ("BAMLH0A0HYM2","HY OAS (% spread)",       "daily",     "rising",  (2.5, 3.0, 3.5, 4.5)),
]

TSV_HEADER = "Run_Date\tSeries\tLabel\tDate\tValue\tPrior\tChange\tPct_Chg\tYoY_Value\tYoY_Pct\tStatus"


def fred_fetch(series_id, limit=15):
    """Fetch latest observations from FRED."""
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


def compute_yoy(observations):
    """Find year-ago value from observations for YoY comparison."""
    if len(observations) < 2:
        return None, None
    latest_date = observations[0]["date"]
    try:
        latest_dt = datetime.strptime(latest_date, "%Y-%m-%d")
        target_year = latest_dt.year - 1
        target_date = latest_dt.replace(year=target_year)
    except ValueError:
        return None, None

    # Find closest observation to target date
    best = None
    best_diff = float("inf")
    for obs in observations[1:]:
        try:
            obs_dt = datetime.strptime(obs["date"], "%Y-%m-%d")
            diff = abs((obs_dt - target_date).days)
            if diff < best_diff:
                best_diff = diff
                best = obs
        except ValueError:
            continue

    if best and best_diff < 45:  # within ~6 weeks
        return best["date"], best["value"]
    return None, None


def status_for(value, thresholds, direction_bad):
    """Determine status color based on thresholds."""
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
    else:  # falling
        if value <= r:
            return "RED"
        if value <= o:
            return "ORANGE"
        if value <= y:
            return "YELLOW"
        return "GREEN"


def fmt_val(val, series_id):
    """Format value based on series type."""
    if series_id in ("ICSA", "CCSA"):
        return f"{val:,.0f}"
    if series_id in ("TOTALNS", "RSXFS", "DSPIC96"):
        return f"{val:,.1f}"
    return f"{val:.2f}"


def main():
    now = datetime.now()
    run_date = now.strftime("%Y-%m-%d")
    run_time = now.strftime("%Y-%m-%d %H:%M")

    print(f"\n{'='*72}")
    print(f"  CARL Consumer Pulse \u2014 {run_time}")
    print(f"{'='*72}")

    tsv_rows = []
    display_rows = []

    for series_id, label, freq, direction_bad, thresholds in SERIES:
        obs = fred_fetch(series_id, limit=15)
        if not obs or "error" in obs[0]:
            err = obs[0].get("error", "no data") if obs else "no data"
            display_rows.append((label, series_id, "ERROR", err[:40], "", "", "", ""))
            continue

        try:
            latest_val = float(obs[0]["value"])
            latest_date = obs[0]["date"]
        except (ValueError, KeyError):
            display_rows.append((label, series_id, "ERROR", "bad value", "", "", "", ""))
            continue

        # Prior period
        prior_val = None
        change = None
        pct_chg = None
        if len(obs) > 1:
            try:
                prior_val = float(obs[1]["value"])
                change = latest_val - prior_val
                if prior_val != 0:
                    pct_chg = (change / prior_val) * 100
            except (ValueError, KeyError):
                pass

        # YoY
        yoy_date, yoy_raw = compute_yoy(obs)
        yoy_val = None
        yoy_pct = None
        if yoy_raw:
            try:
                yoy_val = float(yoy_raw)
                if yoy_val != 0:
                    yoy_pct = ((latest_val - yoy_val) / yoy_val) * 100
            except ValueError:
                pass

        status = status_for(latest_val, thresholds, direction_bad)

        # Direction arrow
        if change is not None:
            if direction_bad == "rising":
                arrow = "\U0001f534" if change > 0 else "\U0001f7e2"
            else:
                arrow = "\U0001f7e2" if change > 0 else "\U0001f534"
        else:
            arrow = "\u26aa"

        display_rows.append((
            label, series_id, latest_date,
            fmt_val(latest_val, series_id),
            f"{change:+.2f}" if change is not None and series_id not in ("ICSA", "CCSA") else (f"{change:+,.0f}" if change is not None else ""),
            f"{pct_chg:+.1f}%" if pct_chg is not None else "",
            f"{yoy_pct:+.1f}% YoY" if yoy_pct is not None else "",
            status, arrow,
        ))

        # TSV row
        tsv_rows.append("\t".join([
            run_date, series_id, label, latest_date,
            str(latest_val),
            str(prior_val) if prior_val is not None else "",
            f"{change:.4f}" if change is not None else "",
            f"{pct_chg:.2f}" if pct_chg is not None else "",
            str(yoy_val) if yoy_val is not None else "",
            f"{yoy_pct:.2f}" if yoy_pct is not None else "",
            status,
        ]))

    # Display
    # Group by category
    categories = [
        ("CREDIT / DELINQUENCY", ["DRCCLACBS", "DRCLACBS"]),
        ("SAVINGS / INCOME", ["PSAVERT", "DSPIC96"]),
        ("SPENDING", ["RSXFS"]),
        ("SENTIMENT", ["UMCSENT"]),
        ("INFLATION", ["PCEPILFE", "CPIUFDNS", "CPIENGNS"]),
        ("CREDIT GROWTH", ["TOTALNS"]),
        ("LABOR", ["ICSA", "CCSA"]),
        ("HOUSING / RATES", ["MORTGAGE30US"]),
        ("SPREADS", ["BAMLH0A0HYM2"]),
    ]

    series_to_row = {r[1]: r for r in display_rows}

    for cat_name, series_list in categories:
        cat_rows = [series_to_row[s] for s in series_list if s in series_to_row]
        if not cat_rows:
            continue

        print(f"\n  {cat_name}")
        print(f"  {'-'*68}")

        for row in cat_rows:
            if len(row) >= 9:
                label, sid, date, val, chg, pct, yoy, status, arrow = row
                status_str = f"[{status}]" if status not in ("TRACK", "") else ""
                print(f"  {arrow} {label:<28} {val:>14}  {chg:>10}  {pct:>8}  {yoy:>12}  {status_str}")
                print(f"    {'':28} as of {date}")
            else:
                label, sid, status, err = row[0], row[1], row[2], row[3]
                print(f"  \u26a0\ufe0f  {label:<28} {status}: {err}")

    # Summary
    statuses = [r[7] for r in display_rows if len(r) >= 9]
    red = sum(1 for s in statuses if s == "RED")
    orange = sum(1 for s in statuses if s == "ORANGE")
    yellow = sum(1 for s in statuses if s == "YELLOW")
    green = sum(1 for s in statuses if s == "GREEN")
    track = sum(1 for s in statuses if s == "TRACK")

    print(f"\n  {'='*68}")
    print(f"  SUMMARY: {red} RED | {orange} ORANGE | {yellow} YELLOW | {green} GREEN | {track} track-only")

    # Write TSV
    DATA_DIR.mkdir(exist_ok=True)
    write_header = not PULSE_TSV.exists()
    with open(PULSE_TSV, "a") as f:
        if write_header:
            f.write(TSV_HEADER + "\n")
        for row in tsv_rows:
            f.write(row + "\n")
    print(f"  Wrote {len(tsv_rows)} rows to {PULSE_TSV.relative_to(SCRIPTS_DIR.parent)}")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
