#!/usr/bin/env python3
"""
LABOR Catalyst Countdown
Reads docket/CATALYSTS.tsv and shows trading-day countdown to each event.
Flags anything within 5 trading days. Highlights 🔴 priority events within horizon.

Ported from BRENT's catalyst_countdown.py (path + default horizon differ).

Usage:
  .venv/bin/python3 AGENTS/LABOR/scripts/catalyst_countdown.py
  .venv/bin/python3 AGENTS/LABOR/scripts/catalyst_countdown.py --days 90
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

LABOR_DIR = Path(__file__).resolve().parent.parent
CATALYSTS_TSV = LABOR_DIR / "docket" / "CATALYSTS.tsv"

DEFAULT_HORIZON = 45  # days to look ahead (labor releases cluster monthly)


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


def trading_days_between(start_date, end_date):
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

    print(f"\n{'='*72}")
    print(f"  LABOR Catalyst Countdown — {now}  ({horizon}-day horizon)")
    print(f"  '~' prefix = modeled/projected date (not source-confirmed; may revise)")
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
            edate = datetime.strptime(c["date"], "%Y-%m-%d").date()
        except (ValueError, KeyError):
            continue
        if edate < today:
            past.append((edate, c))
        elif edate <= horizon_cutoff:
            upcoming.append((edate, c))

    upcoming.sort(key=lambda x: x[0])
    past.sort(key=lambda x: x[0])

    # PAST-DUE block — printed UNCONDITIONALLY and FIRST.
    # Boot step B5 requires verifying every catalyst dated <= today that is not yet
    # resolved. Because fired rows are PRUNED at closeout (C2), a row still present
    # past its date reads as "not yet graded" -- which is exactly the class B5 exists
    # to catch. This block used to print only when `upcoming` was empty, so on every
    # normal boot (upcoming non-empty) past-due rows were silently dropped and B5 ran
    # against a surface that could not show its own target class. Two HIGH rows sat
    # past-due and unflagged until PROME's external summons check found them.
    # Fixed 2026-08-23. Second defect fixed same edit: `past` was never sorted, so the
    # old `past[-1]` reported the last row in FILE order, not the most recent date.
    if past:
        print(f"\n  {'='*68}")
        print(f"  \u26d4 PAST DUE — {len(past)} row(s) dated <= today and NOT pruned")
        print(f"  A present past-due row reads as UNGRADED (fired rows are pruned at C2).")
        print(f"  {'='*68}")
        for edate, c in past:
            overdue = (today - edate).days
            pri = c.get("priority", "").strip() or "-"
            print(f"  [{pri:<4}] {edate.strftime('%Y-%m-%d')} ({overdue}d overdue)  {c.get('event','')}")
            note = (c.get("notes", "") or "").strip()
            if note:
                print(f"         \u21b3 notes: {note[:150]}")
        print(f"\n  \u2192 Grade, re-date, or prune each row above before new analysis (B5/C2).")

    if not upcoming:
        print(f"\n  No catalysts within {horizon} days.")
        return 0

    imminent = []
    later = []
    for edate, c in upcoming:
        trd = trading_days_between(today, edate)
        if trd <= 5:
            imminent.append((edate, c, trd))
        else:
            later.append((edate, c, trd))

    if imminent:
        print(f"\n  🔴 IMMINENT (≤5 trading days)")
        print(f"  {'-'*68}")
        for edate, c, trd in imminent:
            pri = c.get("priority", "").strip() or "  "
            cal_days = (edate - today).days
            day_of_week = edate.strftime("%a")
            marker = "~" if c.get("date_class", "").strip() == "modeled" else " "
            print(f"  {pri} {marker}{edate.strftime('%Y-%m-%d')} ({day_of_week})  {cal_days:>2}d cal / {trd:>2}d trd  {c.get('event', '')}")
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
            print(f"  {pri} {marker}{edate.strftime('%Y-%m-%d')} ({day_of_week})  {cal_days:>3}d cal / {trd:>3}d trd  {event}")

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
