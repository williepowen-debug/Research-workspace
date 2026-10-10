#!/usr/bin/env python3
"""
REGINALD Earnings Countdown
Counts trading days to each bank's earnings date, read from the canonical table in
AGENTS/REGINALD/CALENDAR.md (§ Q3-2026 BANK EARNINGS DATES). No dates live in this script.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/earnings_countdown.py
  .venv/bin/python3 AGENTS/REGINALD/scripts/earnings_countdown.py --selftest   # fixtures, no file

Exit: 0 = table read · 2 = table missing, duplicated or malformed (a Day that is not its Date's
weekday, a bad date, an unknown Status) — the countdown is then NOT printed, never "no dates".

Repair 2026-10-09 (Will's bounded pass): this script carried a hand-typed April-2026 list and
printed "No upcoming earnings dates" in Q3 print week.
"""

import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

CALENDAR = Path(__file__).resolve().parents[1] / "CALENDAR.md"
BEGIN = "<!-- reginald:earnings-dates:begin -->"
END = "<!-- reginald:earnings-dates:end -->"
STATUSES = ("CONFIRMED", "NOT-ANNOUNCED")
COLUMNS = ["Ticker", "Date", "Day", "Timing", "Status", "Question", "Source"]


def parse_table(text):
    """CALENDAR text -> (rows, errors). Pure; any error voids the table."""
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        return [], [f"expected exactly one begin and one end marker, found {text.count(BEGIN)}/{text.count(END)}"]
    body = text.split(BEGIN, 1)[1].split(END, 1)[0]
    lines = [ln.strip() for ln in body.strip().splitlines() if ln.strip()]
    if len(lines) < 3:
        return [], ["table has no data rows"]
    header = [c.strip() for c in lines[0].strip("|").split("|")]
    if header != COLUMNS:
        return [], [f"header {header} != {COLUMNS}"]
    rows, errors = [], []
    for n, ln in enumerate(lines[2:], start=1):
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) != len(COLUMNS):
            errors.append(f"row {n}: {len(cells)} cells, expected {len(COLUMNS)}")
            continue
        r = dict(zip(COLUMNS, cells))
        try:
            d = datetime.strptime(r["Date"], "%Y-%m-%d").date()
        except ValueError:
            errors.append(f"row {n} {r['Ticker']}: bad date '{r['Date']}'")
            continue
        if d.strftime("%a") != r["Day"]:
            errors.append(f"row {n} {r['Ticker']}: Day '{r['Day']}' but {r['Date']} is a {d:%a}")
        if r["Status"] not in STATUSES:
            errors.append(f"row {n} {r['Ticker']}: Status '{r['Status']}' not in {STATUSES}")
        if not re.fullmatch(r"[A-Z]{1,5}", r["Ticker"]):
            errors.append(f"row {n}: bad ticker '{r['Ticker']}'")
        r["date"] = d
        rows.append(r)
    return rows, errors


def trading_days_between(start, end):
    """Weekdays after start up to and including end (NYSE holidays not modelled)."""
    days, cur = 0, start
    while cur < end:
        cur += timedelta(days=1)
        days += cur.weekday() < 5
    return days


def selftest():
    def table(*rows, begin=BEGIN, end=END):
        head = "| " + " | ".join(COLUMNS) + " |\n|" + "---|" * len(COLUMNS) + "\n"
        return f"x\n{begin}\n{head}" + "".join("| " + " | ".join(r) + " |\n" for r in rows) + f"{end}\n"
    ok_row = ("CFG", "2026-10-16", "Fri", "pre-open", "CONFIRMED", "Q1", "IR")
    cases = [
        ("valid table -> 1 row, no errors", parse_table(table(ok_row)), (1, 0)),
        ("missing markers -> error", parse_table("no table here"), (0, 1)),
        ("duplicated begin marker -> error", parse_table(table(ok_row) + BEGIN), (0, 1)),
        ("Day/Date mismatch -> error", parse_table(table(("CFG", "2026-10-16", "Thu", "x", "CONFIRMED", "Q1", "IR"))), (1, 1)),
        ("bad date -> error", parse_table(table(("CFG", "2026-13-16", "Fri", "x", "CONFIRMED", "Q1", "IR"))), (0, 1)),
        ("unknown status -> error", parse_table(table(("CFG", "2026-10-16", "Fri", "x", "MAYBE", "Q1", "IR"))), (1, 1)),
        ("short row -> error", parse_table(table(("CFG", "2026-10-16", "Fri"))), (0, 1)),
    ]
    fails = 0
    for name, (rows, errs), (want_rows, want_err) in cases:
        ok = len(rows) == want_rows and (len(errs) > 0) == bool(want_err)
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  rows={len(rows)} errors={len(errs)}  {name}")
    td = trading_days_between(date(2026, 10, 9), date(2026, 10, 16))
    ok = td == 5
    fails += not ok
    print(f"  {'PASS' if ok else 'FAIL'}  Fri 10/9 -> Fri 10/16 = {td} trading days (want 5)")
    print(f"COUNTDOWN SELFTEST {'PASS' if not fails else 'FAIL'}: {len(cases) + 1 - fails}/{len(cases) + 1}")
    return 1 if fails else 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    today = datetime.now().date()
    print(f"\n{'='*70}")
    print(f"  REGINALD Earnings Countdown — {datetime.now():%Y-%m-%d %H:%M}  (source: {CALENDAR.name})")
    print(f"{'='*70}")
    try:
        text = CALENDAR.read_text(encoding="utf-8")
    except OSError as e:
        print(f"\n  ⚠️  INCOMPLETE: cannot read {CALENDAR} ({e}) — no countdown")
        return 2
    rows, errors = parse_table(text)
    if errors:
        print("\n  ⚠️  INCOMPLETE: the CALENDAR earnings table is malformed — no countdown printed:")
        for e in errors:
            print(f"     {e}")
        return 2

    upcoming = sorted((r for r in rows if r["date"] >= today), key=lambda r: (r["date"], r["Ticker"]))
    past = [r["Ticker"] for r in rows if r["date"] < today]
    if not upcoming:
        print("\n  No upcoming dates in the CALENDAR table — add the next quarter's dates there.")
        return 0

    print(f"\n  {'Ticker':<6} {'Date':>11} {'Trd':>4}  {'Status':<15} {'Q':<6} Timing")
    print(f"  {'-'*68}")
    for r in upcoming:
        td = trading_days_between(today, r["date"])
        flag = ("🔴 TODAY" if td == 0 else "🔴 ≤2d" if td <= 2 else "⚠️  ≤5d" if td <= 5
                else "🟡 ≤10d" if td <= 10 else "")
        status = "✓ confirmed" if r["Status"] == "CONFIRMED" else "~ESTIMATE"
        print(f"  {r['Ticker']:<6} {r['date']:%a %b %d} {td:>4}  {status:<15} {r['Question']:<6} {r['Timing']}  {flag}")
    est = [r["Ticker"] for r in upcoming if r["Status"] != "CONFIRMED"]
    if est:
        print(f"\n  ⚠️  NOT ANNOUNCED (dates above are estimates): {', '.join(est)}")
    if past:
        print(f"  Reported: {', '.join(past)}")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
