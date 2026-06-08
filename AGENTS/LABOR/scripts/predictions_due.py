#!/usr/bin/env python3
"""
LABOR Predictions-Due Scanner

Parses workbook/PREDICTIONS.tsv and flags OPEN rows whose Timeframe has
arrived (due-by ≤ today) or is imminent (≤ 14 days). Best-effort fuzzy
parsing of the Timeframe column — FLAGS for resolution, never resolves.
Unparseable timeframes are surfaced for manual check rather than silently
dropped.

Supports the SPAWN PROTOCOL step 1.5 predictions sweep (automation of an
otherwise-manual scan; SAM/BRENT eyeball this).

Usage:
  .venv/bin/python3 AGENTS/LABOR/scripts/predictions_due.py
  .venv/bin/python3 AGENTS/LABOR/scripts/predictions_due.py --soon 30   # widen imminent window

Exit code: 0 normally, 2 if any OPEN prediction is past-due (so boot.py surfaces).
"""

import re
import sys
from datetime import datetime, date, timedelta
from pathlib import Path

LABOR_DIR = Path(__file__).resolve().parent.parent
PREDICTIONS_TSV = LABOR_DIR / "workbook" / "PREDICTIONS.tsv"

QUARTER_END = {1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}
MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
    "january": 1, "february": 2, "march": 3, "april": 4, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10,
    "november": 11, "december": 12,
}


def month_end(year, month):
    if month == 12:
        return date(year, 12, 31)
    return date(year, month + 1, 1) - timedelta(days=1)


def parse_timeframe(tf):
    """Return (due_by_date, basis_str) or (None, reason) if unparseable.

    due_by = the LAST date by which the prediction must have resolved.
    """
    if not tf:
        return None, "empty timeframe"
    s = tf.strip()
    low = s.lower()

    year_m = re.search(r"(20\d{2})", s)
    year = int(year_m.group(1)) if year_m else None

    # "Mon D YYYY"  e.g. "Jun 6 2026"
    m = re.search(r"([A-Za-z]{3,9})\.?\s+(\d{1,2})[,]?\s+(20\d{2})", s)
    if m and m.group(1).lower()[:3] in MONTHS:
        mon = MONTHS[m.group(1).lower()[:3]]
        return date(int(m.group(3)), mon, int(m.group(2))), "exact date"

    # "Through YYYY" / "Through 2026" → year end (ongoing — only due at year end)
    if low.startswith("through") and year:
        return date(year, 12, 31), "through-year (ongoing)"

    # Quarter range "Qa-Qb YYYY" → end of last quarter
    qr = re.search(r"q([1-4])\s*[-–]\s*q([1-4])", low)
    if qr and year:
        mo, dy = QUARTER_END[int(qr.group(2))]
        return date(year, mo, dy), f"end Q{qr.group(2)} {year}"

    # Single quarter "Qn YYYY"
    q = re.search(r"q([1-4])", low)
    if q and year:
        mo, dy = QUARTER_END[int(q.group(1))]
        return date(year, mo, dy), f"end Q{q.group(1)} {year}"

    # Month range "Mon-Mon YYYY" → end of 2nd month
    mr = re.search(r"([A-Za-z]{3,9})\s*[-–]\s*([A-Za-z]{3,9})", s)
    if mr and year and mr.group(2).lower()[:3] in MONTHS:
        mon = MONTHS[mr.group(2).lower()[:3]]
        return month_end(year, mon), f"end {mr.group(2)} {year}"

    # Single "Mon YYYY"
    msingle = re.search(r"([A-Za-z]{3,9})\s+(20\d{2})", s)
    if msingle and msingle.group(1).lower()[:3] in MONTHS:
        mon = MONTHS[msingle.group(1).lower()[:3]]
        return month_end(int(msingle.group(2)), mon), f"end {msingle.group(1)} {msingle.group(2)}"

    # Bare year
    if year and re.fullmatch(r"20\d{2}", s):
        return date(year, 12, 31), f"year end {year}"

    return None, f"unparseable: '{s}'"


def load_predictions():
    if not PREDICTIONS_TSV.exists():
        return None, None
    rows = []
    with open(PREDICTIONS_TSV) as f:
        header = f.readline().rstrip("\n").split("\t")
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            rows.append(dict(zip(header, parts + [""] * (len(header) - len(parts)))))
    return header, rows


def main():
    soon_days = 14
    if "--soon" in sys.argv:
        i = sys.argv.index("--soon")
        if i + 1 < len(sys.argv):
            soon_days = int(sys.argv[i + 1])

    today = datetime.now().date()
    header, rows = load_predictions()

    print(f"\n{'='*72}")
    print(f"  LABOR Predictions-Due Scan — {today.isoformat()}")
    print(f"  source: workbook/PREDICTIONS.tsv  (flags OPEN rows; never resolves)")
    print(f"{'='*72}")

    if rows is None:
        print(f"\n  ERROR: {PREDICTIONS_TSV} not found")
        return 1

    open_rows = [r for r in rows if r.get("Status", "").strip().upper() == "OPEN"]

    overdue, imminent, future, unparsed = [], [], [], []
    for r in open_rows:
        due, basis = parse_timeframe(r.get("Timeframe", ""))
        if due is None:
            unparsed.append((r, basis))
            continue
        days = (due - today).days
        if days < 0:
            overdue.append((r, due, basis, days))
        elif days <= soon_days:
            imminent.append((r, due, basis, days))
        else:
            future.append((r, due, basis, days))

    def line(r, due, basis, days):
        pid = r.get("Pred_ID", "?")
        pred = r.get("Prediction", "")[:54]
        conf = r.get("Confidence", "")
        return f"  {pid:<7} due {due.isoformat()} ({basis}) {days:+}d  [{conf}]  {pred}"

    if overdue:
        print(f"\n  🔴 OVERDUE — resolve this session ({len(overdue)}):")
        for r, due, basis, days in sorted(overdue, key=lambda x: x[1]):
            print(line(r, due, basis, days))

    if imminent:
        print(f"\n  🟠 DUE SOON (≤{soon_days}d) ({len(imminent)}):")
        for r, due, basis, days in sorted(imminent, key=lambda x: x[1]):
            print(line(r, due, basis, days))

    if unparsed:
        print(f"\n  ⚠️  UNPARSEABLE timeframe — check manually ({len(unparsed)}):")
        for r, reason in unparsed:
            print(f"     {r.get('Pred_ID','?'):<7} {reason}  | {r.get('Prediction','')[:50]}")

    if future:
        print(f"\n  📅 OPEN, not yet due ({len(future)}): "
              + ", ".join(f"{r.get('Pred_ID')}→{due.isoformat()}" for r, due, _, _ in sorted(future, key=lambda x: x[1])))

    if not (overdue or imminent or unparsed):
        print(f"\n  ✅ No OPEN predictions overdue or due within {soon_days}d.")

    print()
    return 2 if overdue else 0


if __name__ == "__main__":
    sys.exit(main())
