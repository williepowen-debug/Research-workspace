#!/usr/bin/env python3
"""
MARCO Catalyst Countdown
Reads docket/CATALYSTS.tsv and shows a calendar-day countdown to each forward event.
Flags anything PASSED-but-still-listed (needs pruning/resolution) and anything DUE
within the horizon. Highlights 🔴/🟠 priority events.

MARCO's domain is monthly government data releases (BLS, Banxico, StatCan, FL
Realtors), not tradeable ticks — so the countdown is calendar-day-primary (a CPI
print lands on a calendar date), with a business-day note for context.

Usage:
  .venv/bin/python3 AGENTS/MARCO/scripts/catalyst_countdown.py
  .venv/bin/python3 AGENTS/MARCO/scripts/catalyst_countdown.py --days 14   # horizon override
  .venv/bin/python3 AGENTS/MARCO/scripts/catalyst_countdown.py --all       # show beyond horizon too
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

MARCO_DIR = Path(__file__).resolve().parent.parent
CATALYSTS_TSV = MARCO_DIR / "docket" / "CATALYSTS.tsv"

DEFAULT_HORIZON = 30  # days to look ahead for the "DUE SOON" cut

# US market / federal holidays 2026 (for the business-day note only).
HOLIDAYS = frozenset({
    "2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25",
    "2026-06-19", "2026-07-03", "2026-09-07", "2026-11-26", "2026-12-25",
})


def load_catalysts():
    """Read CATALYSTS.tsv → list of dicts. Schema: date, event, what_to_check,
    threshold_signal, priority, who_cares, notes."""
    if not CATALYSTS_TSV.exists():
        return None
    rows = []
    with open(CATALYSTS_TSV) as f:
        header = f.readline().rstrip("\n").split("\t")
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2 or not parts[0].strip():
                continue
            d = dict(zip(header, parts + [""] * (len(header) - len(parts))))
            rows.append(d)
    return rows


def parse_date(s):
    """Parse an ISO date from the date column; tolerate a leading ~ or whitespace."""
    s = s.strip().lstrip("~").strip()
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def business_days_between(start, end):
    """Weekdays excluding US holidays, exclusive of start, inclusive of end."""
    if end <= start:
        return 0
    days, cur = 0, start + timedelta(days=1)
    while cur <= end:
        if cur.weekday() < 5 and cur.isoformat() not in HOLIDAYS:
            days += 1
        cur += timedelta(days=1)
    return days


def prio_rank(p):
    """Sort/severity rank from the priority emoji."""
    for i, e in enumerate(("🔴", "🟠", "🟡", "🟢")):
        if e in p:
            return i
    return 9


def main():
    horizon = DEFAULT_HORIZON
    if "--days" in sys.argv:
        i = sys.argv.index("--days")
        if i + 1 < len(sys.argv):
            horizon = int(sys.argv[i + 1])
    show_all = "--all" in sys.argv

    today = datetime.now().date()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"\n{'='*72}")
    print(f"  MARCO Catalyst Countdown — {now}  ({horizon}-day horizon)")
    print(f"{'='*72}")

    cats = load_catalysts()
    if cats is None:
        print(f"\n  ❌ ERROR: {CATALYSTS_TSV} not found")
        return 1
    if not cats:
        print("\n  (no catalysts listed)")
        return 0

    passed, due, later, unparsed = [], [], [], []
    for c in cats:
        dt = parse_date(c.get("date", ""))
        if dt is None:
            unparsed.append(c)
            continue
        delta = (dt - today).days
        rec = (dt, delta, c)
        if delta < 0:
            passed.append(rec)
        elif delta <= horizon:
            due.append(rec)
        else:
            later.append(rec)

    # PASSED-but-still-listed: the NFP-gap catcher. Most urgent — needs action.
    if passed:
        print(f"\n  ⚠️  PASSED — still in docket, needs resolve/prune ({len(passed)}):")
        for dt, delta, c in sorted(passed, key=lambda r: r[0]):
            print(f"    🔴 {dt}  ({-delta:>3}d ago)  {c.get('event','')[:60]}")
            note = c.get("notes", "").strip()
            if note:
                print(f"         ↳ {note[:90]}")

    # DUE within horizon
    print(f"\n  📅 DUE within {horizon}d ({len(due)}):")
    if due:
        for dt, delta, c in sorted(due, key=lambda r: (r[0], prio_rank(r[2].get('priority','')))):
            bd = business_days_between(today, dt)
            pr = c.get("priority", "").strip() or "  "
            dayname = dt.strftime("%a %b %d")
            print(f"    {pr} {dayname}  in {delta:>2}d ({bd} bd)  {c.get('event','')[:55]}")
            sig = c.get("threshold_signal", "").strip()
            if sig:
                print(f"         ↳ {sig[:100]}")
    else:
        print("    (none)")

    # Beyond horizon (compact unless --all)
    if later:
        print(f"\n  · Beyond {horizon}d: {len(later)} more catalyst(s)" + ("" if show_all else " (use --all)"))
        if show_all:
            for dt, delta, c in sorted(later, key=lambda r: r[0]):
                pr = c.get("priority", "").strip() or "  "
                print(f"    {pr} {dt}  in {delta:>3}d  {c.get('event','')[:55]}")

    if unparsed:
        print(f"\n  ⚠️  {len(unparsed)} row(s) with UNPARSEABLE date (check CATALYSTS.tsv):")
        for c in unparsed:
            print(f"      date='{c.get('date','')}'  {c.get('event','')[:50]}")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
