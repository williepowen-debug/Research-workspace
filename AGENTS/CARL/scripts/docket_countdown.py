#!/usr/bin/env python3
"""
CARL Docket Countdown
Reads docket/CATALYSTS.tsv and shows a calendar-day countdown to upcoming
catalysts, and — the load-bearing part — flags any PAST-dated row still in the
file as "released but not yet integrated" (a row should be pruned once its data
is folded into STATUS/ROADMAP, so a lingering past row = a missed integration).

Calendar days (not trading days) — CARL tracks monthly macro releases / court
dates / earnings, which are calendar-dated, so trading-day precision is overkill.

Usage:
  .venv/bin/python3 AGENTS/CARL/scripts/docket_countdown.py
  .venv/bin/python3 AGENTS/CARL/scripts/docket_countdown.py --days 30   # horizon override
"""

import sys
from datetime import date
from pathlib import Path

CARL_DIR = Path(__file__).resolve().parent.parent
CATALYSTS_TSV = CARL_DIR / "docket" / "CATALYSTS.tsv"
DEFAULT_HORIZON = 21  # days to look ahead


def load_catalysts():
    if not CATALYSTS_TSV.exists():
        return []
    rows = []
    with open(CATALYSTS_TSV) as f:
        header = f.readline().rstrip("\n").split("\t")
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2 or not parts[0].strip():
                continue
            rows.append(dict(zip(header, parts + [""] * (len(header) - len(parts)))))
    return rows


def parse_iso(s):
    try:
        y, m, d = (int(x) for x in s.strip().split("-"))
        return date(y, m, d)
    except (ValueError, AttributeError):
        return None


def main():
    horizon = DEFAULT_HORIZON
    if "--days" in sys.argv:
        try:
            horizon = int(sys.argv[sys.argv.index("--days") + 1])
        except (IndexError, ValueError):
            pass

    today = date.today()
    cats = load_catalysts()
    if not cats:
        print("docket/CATALYSTS.tsv empty or missing.")
        return

    overdue, upcoming, beyond = [], [], []
    for c in cats:
        d = parse_iso(c.get("date", ""))
        if d is None:
            continue
        delta = (d - today).days
        if delta < 0:
            overdue.append((delta, d, c))
        elif delta <= horizon:
            upcoming.append((delta, d, c))
        else:
            beyond.append((delta, d, c))

    print(f"=== CARL DOCKET — {today.isoformat()} (horizon {horizon}d) ===\n")

    by_date = lambda t: (t[0], t[1])  # sort by delta then date — never touches the dict

    if overdue:
        print("⚠️  RELEASED / PAST-DUE — integrate & prune (these should not linger):")
        for delta, d, c in sorted(overdue, key=by_date):
            print(f"  [{-delta:>3}d ago] {d.isoformat()}  {c['priority']} {c['event']}")
            print(f"            -> {c.get('threshold_signal','')}")
        print()

    if upcoming:
        print(f"NEXT {horizon} DAYS:")
        for delta, d, c in sorted(upcoming, key=by_date):
            tag = "TODAY" if delta == 0 else f"in {delta:>2}d"
            print(f"  [{tag:>7}] {d.isoformat()}  {c['priority']} {c['event']}  ({c.get('who_cares','')})")
        print()

    if beyond:
        nxt = sorted(beyond, key=by_date)[0]
        print(f"BEYOND {horizon}D: {len(beyond)} more catalyst(s) on the docket "
              f"(next: {nxt[1].isoformat()} {nxt[2]['event']}).")


if __name__ == "__main__":
    main()
