#!/usr/bin/env python3
"""
SAM JGB Yield Monitor
Fetches daily JGB yield curve from MOF's authoritative CSV.

Source: https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv
Format: Date, 1Y, 2Y, 3Y, ..., 10Y, 15Y, 20Y, 25Y, 30Y, 40Y (all in %)
Update cadence: MOF publishes with ~1 business day lag. Friday data posts Monday.

Checks thresholds:
  🔴 10Y ≥ 2.40% (stress crossover)
  🔴 30Y ≥ 4.00% (severe insurer stress)
  🔴 40Y ≥ 4.00% (extreme long-end stress)

Appends to workbook/JGB_YIELDS.tsv (one row per date).

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/jgb_yields.py
  .venv/bin/python3 AGENTS/SAM/scripts/jgb_yields.py --history 10   # show last 10 days
"""

import sys
import urllib.request
from datetime import datetime
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
JGB_TSV = WORKBOOK / "JGB_YIELDS.tsv"

MOF_CSV_URL = "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv"

HEADERS = {"User-Agent": "Mozilla/5.0 (SAM-Research)"}

# Tenors SAM cares about (CSV has 1Y-40Y; we track these)
TRACKED_TENORS = ["2Y", "5Y", "10Y", "20Y", "30Y", "40Y"]

# Threshold levels (from THESIS.md KEY THRESHOLDS table)
THRESHOLDS = {
    "10Y": (2.40, "Stress crossover"),
    "30Y": (4.00, "Severe insurer stress"),
    "40Y": (4.00, "Extreme long-end stress"),
}

TSV_HEADER = "Date\t2Y\t5Y\t10Y\t20Y\t30Y\t40Y\tSource\n"


def fetch_mof_csv():
    """Fetch MOF JGB yield CSV. Returns raw text or None on failure."""
    try:
        req = urllib.request.Request(MOF_CSV_URL, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ERROR fetching MOF CSV: {e}")
        return None


def parse_mof_csv(text):
    """
    Parse MOF CSV. Returns list of dicts ordered by date ascending.
    Structure:
      Line 1: "Interest Rate (Month Year),..."
      Line 2: "Date,1Y,2Y,3Y,4Y,5Y,6Y,7Y,8Y,9Y,10Y,15Y,20Y,25Y,30Y,40Y"
      Lines 3+: "YYYY/M/D,1.xxx,1.xxx,..."
      Trailer: empty lines + encoding warning
    """
    lines = text.splitlines()
    if len(lines) < 3:
        return []

    # Header is line 2 (index 1)
    header = [h.strip() for h in lines[1].split(",")]
    if header[0] != "Date":
        # Shouldn't happen, but bail cleanly
        return []

    # Map tenor name to column index
    tenor_idx = {name: i for i, name in enumerate(header)}

    rows = []
    for line in lines[2:]:
        parts = [p.strip() for p in line.split(",")]
        if not parts[0] or "/" not in parts[0]:
            continue
        try:
            # MOF format: 2026/4/9
            d = datetime.strptime(parts[0], "%Y/%m/%d").date()
        except ValueError:
            continue

        row = {"date": d.strftime("%Y-%m-%d")}
        for tenor in TRACKED_TENORS:
            idx = tenor_idx.get(tenor)
            if idx is not None and idx < len(parts):
                val = parts[idx]
                try:
                    row[tenor] = float(val) if val else None
                except ValueError:
                    row[tenor] = None
            else:
                row[tenor] = None
        rows.append(row)

    return rows


def append_tsv(rows):
    """Append rows to TSV, idempotent on date."""
    existing_dates = set()
    if JGB_TSV.exists():
        with open(JGB_TSV) as f:
            next(f, None)  # skip header
            for line in f:
                parts = line.strip().split("\t")
                if parts:
                    existing_dates.add(parts[0])
    else:
        with open(JGB_TSV, "w") as f:
            f.write(TSV_HEADER)

    appended = 0
    with open(JGB_TSV, "a") as f:
        for r in rows:
            if r["date"] in existing_dates:
                continue
            values = [r["date"]]
            for tenor in TRACKED_TENORS:
                v = r.get(tenor)
                values.append(f"{v:.3f}" if v is not None else "")
            values.append("MOF")
            f.write("\t".join(values) + "\n")
            appended += 1
    return appended


def check_thresholds(row):
    """Return list of threshold breaches for the given row."""
    breaches = []
    for tenor, (level, label) in THRESHOLDS.items():
        v = row.get(tenor)
        if v is not None and v >= level:
            dist = ((v - level) / level) * 100
            breaches.append((tenor, v, level, label, dist))
    return breaches


def main():
    history = 5
    if "--history" in sys.argv:
        idx = sys.argv.index("--history")
        if idx + 1 < len(sys.argv):
            history = int(sys.argv[idx + 1])

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  SAM JGB Yield Monitor — {now}")
    print(f"{'='*70}")

    text = fetch_mof_csv()
    if not text:
        print("\n  ERROR: MOF CSV fetch failed. Try again later.")
        return 1

    rows = parse_mof_csv(text)
    if not rows:
        print("\n  ERROR: MOF CSV parsed empty. Format may have changed.")
        return 1

    latest = rows[-1]
    print(f"\n  Source: MOF (authoritative)")
    print(f"  Latest publication: {latest['date']}")

    # Print latest snapshot
    print(f"\n  LATEST CURVE ({latest['date']})")
    print(f"  {'-'*60}")
    for tenor in TRACKED_TENORS:
        v = latest.get(tenor)
        if v is None:
            print(f"  {tenor:<4}  — no data")
            continue
        mark = ""
        if tenor in THRESHOLDS:
            level, _ = THRESHOLDS[tenor]
            if v >= level:
                mark = "  🔴 BREACHED"
            elif v >= level * 0.95:
                mark = "  ⚠️  near breach"
        print(f"  {tenor:<4}  {v:>6.3f}%{mark}")

    # Threshold breaches
    breaches = check_thresholds(latest)
    if breaches:
        print(f"\n  🔴 ACTIVE BREACHES")
        print(f"  {'-'*60}")
        for tenor, v, level, label, dist in breaches:
            print(f"  🔴 {tenor} at {v:.3f}%  (threshold {level:.2f}%, +{dist:.1f}%)  {label}")

    # History
    if len(rows) >= 2:
        print(f"\n  RECENT HISTORY (last {min(history, len(rows))} days)")
        print(f"  {'-'*60}")
        print(f"  {'Date':<12}  " + "  ".join(f"{t:>6}" for t in TRACKED_TENORS))
        for r in rows[-history:]:
            vals = "  ".join(
                f"{r[t]:>6.3f}" if r.get(t) is not None else "     —"
                for t in TRACKED_TENORS
            )
            print(f"  {r['date']:<12}  {vals}")

        # Week-over-week change (latest vs 5 business days ago if available)
        if len(rows) >= 6:
            prior = rows[-6]
            print(f"\n  5-DAY CHANGE ({prior['date']} → {latest['date']})")
            print(f"  {'-'*60}")
            for tenor in TRACKED_TENORS:
                cur = latest.get(tenor)
                old = prior.get(tenor)
                if cur is not None and old is not None:
                    delta_bp = (cur - old) * 100
                    arrow = "↑" if delta_bp > 0 else "↓" if delta_bp < 0 else "·"
                    print(f"  {tenor:<4}  {old:.3f}% → {cur:.3f}%  ({arrow}{abs(delta_bp):.1f}bp)")

    # Append to TSV
    appended = append_tsv(rows)
    if appended > 0:
        print(f"\n  Appended {appended} row(s) to JGB_YIELDS.tsv")
    else:
        print(f"\n  TSV already current (no new rows)")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
