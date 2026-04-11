#!/usr/bin/env python3
"""
SAM Catalyst Countdown
Reads workbook/CATALYSTS.tsv and shows trading-day countdown to each event.
Flags anything within 5 trading days. Highlights 🔴 priority events within 30 days.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/catalyst_countdown.py
  .venv/bin/python3 AGENTS/SAM/scripts/catalyst_countdown.py --days 14    # horizon override
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
CATALYSTS_TSV = SAM_DIR / "workbook" / "CATALYSTS.tsv"

DEFAULT_HORIZON = 45  # days to look ahead


def load_catalysts():
    """Read CATALYSTS.tsv and return list of dicts."""
    if not CATALYSTS_TSV.exists():
        return []

    catalysts = []
    with open(CATALYSTS_TSV) as f:
        header = f.readline().strip().split("\t")
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            d = dict(zip(header, parts + [""] * (len(header) - len(parts))))
            catalysts.append(d)
    return catalysts


def trading_days_between(start_date, end_date):
    """Count weekdays between two dates, exclusive of start, inclusive of end."""
    if end_date <= start_date:
        return 0
    days = 0
    current = start_date + timedelta(days=1)
    while current <= end_date:
        if current.weekday() < 5:
            days += 1
        current += timedelta(days=1)
    return days


def main():
    horizon = DEFAULT_HORIZON
    if "--days" in sys.argv:
        idx = sys.argv.index("--days")
        if idx + 1 < len(sys.argv):
            horizon = int(sys.argv[idx + 1])

    today = datetime.now().date()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"\n{'='*70}")
    print(f"  SAM Catalyst Countdown — {now}  ({horizon}-day horizon)")
    print(f"{'='*70}")

    catalysts = load_catalysts()
    if not catalysts:
        print(f"\n  ERROR: Could not load {CATALYSTS_TSV}")
        return 1

    # Parse and filter
    upcoming = []
    past = []
    horizon_cutoff = today + timedelta(days=horizon)

    for c in catalysts:
        try:
            edate = datetime.strptime(c["date"], "%Y-%m-%d").date()
        except (ValueError, KeyError):
            continue

        if edate < today:
            past.append((edate, c))
        elif edate <= horizon_cutoff:
            upcoming.append((edate, c))

    upcoming.sort(key=lambda x: x[0])

    if not upcoming:
        print(f"\n  No catalysts within {horizon} days.")
        if past:
            last = past[-1]
            print(f"  Most recent past: {last[0].strftime('%Y-%m-%d')} — {last[1].get('event', '')}")
        return 0

    # Imminent (≤5 trading days)
    imminent = []
    this_month = []
    for edate, c in upcoming:
        trd = trading_days_between(today, edate)
        if trd <= 5:
            imminent.append((edate, c, trd))
        else:
            this_month.append((edate, c, trd))

    # 🔴 IMMINENT section
    if imminent:
        print(f"\n  🔴 IMMINENT (≤5 trading days)")
        print(f"  {'-'*66}")
        for edate, c, trd in imminent:
            pri = c.get("priority", "").strip() or "  "
            cal_days = (edate - today).days
            day_of_week = edate.strftime("%a")
            print(f"  {pri} {edate.strftime('%Y-%m-%d')} ({day_of_week})  {cal_days:>2}d cal / {trd:>2}d trd  {c.get('event', '')}")
            check = c.get("what_to_check", "")
            if check:
                print(f"       ↳ check: {check}")
            sig = c.get("threshold_signal", "")
            if sig and sig.lower() != "routine":
                print(f"       ↳ signal: {sig}")
            who = c.get("who_cares", "")
            if who and who != "-":
                print(f"       ↳ send to: {who}")

    # Within-horizon section
    if this_month:
        print(f"\n  📅 UPCOMING (within {horizon} days)")
        print(f"  {'-'*66}")
        for edate, c, trd in this_month:
            pri = c.get("priority", "").strip() or "  "
            cal_days = (edate - today).days
            day_of_week = edate.strftime("%a")
            event = c.get("event", "")
            # Truncate long events
            if len(event) > 45:
                event = event[:42] + "..."
            print(f"  {pri} {edate.strftime('%Y-%m-%d')} ({day_of_week})  {cal_days:>3}d cal / {trd:>3}d trd  {event}")

    # Summary of 🔴 priority in horizon
    high_pri = [x for x in upcoming if "🔴" in x[1].get("priority", "")]
    if high_pri:
        print(f"\n  🔴 HIGH PRIORITY in horizon: {len(high_pri)}")
        for edate, c in high_pri:
            cal_days = (edate - today).days
            print(f"     • {edate.strftime('%a %b %d')} ({cal_days}d) — {c.get('event', '')}")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
