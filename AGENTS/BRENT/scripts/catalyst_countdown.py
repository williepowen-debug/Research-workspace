#!/usr/bin/env python3
"""
BRENT Catalyst Countdown
Reads docket/CATALYSTS.tsv and shows weekday countdown to each event.
Flags anything within 5 weekdays. Highlights 🔴 priority events within horizon.

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/catalyst_countdown.py
  .venv/bin/python3 AGENTS/BRENT/scripts/catalyst_countdown.py --days 60
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

BRENT_DIR = Path(__file__).resolve().parent.parent
CATALYSTS_TSV = BRENT_DIR / "docket" / "CATALYSTS.tsv"

DEFAULT_HORIZON = 60  # days to look ahead (broader for oil — OPEC+ meetings etc.)


def load_catalysts():
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


def weekdays_between(start_date, end_date):
    if end_date <= start_date:
        return 0
    # Weekdays only; holidays are not excluded. This is not an exchange calendar.
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

    print(f"\n{'='*72}")
    print(f"  BRENT Catalyst Countdown — {now}  ({horizon}-day horizon)")
    print("  Weekday count excludes weekends only; holidays are included.")
    print(f"  {'~'} prefix = modeled/projected date (not source-confirmed; may revise)")
    print(f"{'='*72}")

    catalysts = load_catalysts()
    if not catalysts:
        print(f"\n  ERROR: Could not load {CATALYSTS_TSV}")
        return 1

    upcoming = []
    past = []
    horizon_cutoff = today + timedelta(days=horizon)

    for c in catalysts:
        try:
            edate = datetime.strptime(c["date"].lstrip("~"), "%Y-%m-%d").date()
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

    imminent = []
    later = []
    for edate, c in upcoming:
        trd = weekdays_between(today, edate)
        if trd <= 5:
            imminent.append((edate, c, trd))
        else:
            later.append((edate, c, trd))

    if imminent:
        print(f"\n  🔴 IMMINENT (≤5 weekdays)")
        print(f"  {'-'*68}")
        for edate, c, trd in imminent:
            pri = c.get("priority", "").strip() or "  "
            cal_days = (edate - today).days
            day_of_week = edate.strftime("%a")
            marker = "~" if c.get("date_class", "").strip() == "modeled" else " "
            print(f"  {pri} {marker}{edate.strftime('%Y-%m-%d')} ({day_of_week})  {cal_days:>2}d cal / {trd:>2}d weekday  {c.get('event', '')}")
            check = c.get("what_to_check", "")
            if check:
                print(f"       ↳ check: {check}")
            sig = c.get("threshold_signal", "")
            if sig and sig.lower() != "routine":
                print(f"       ↳ signal: {sig}")
            who = c.get("who_cares", "")
            if who and who != "-":
                print(f"       ↳ send to: {who}")

    if later:
        print(f"\n  📅 UPCOMING (within {horizon} days)")
        print(f"  {'-'*68}")
        for edate, c, trd in later:
            pri = c.get("priority", "").strip() or "  "
            cal_days = (edate - today).days
            day_of_week = edate.strftime("%a")
            event = c.get("event", "")
            if len(event) > 48:
                event = event[:45] + "..."
            marker = "~" if c.get("date_class", "").strip() == "modeled" else " "
            print(f"  {pri} {marker}{edate.strftime('%Y-%m-%d')} ({day_of_week})  {cal_days:>3}d cal / {trd:>3}d weekday  {event}")

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
