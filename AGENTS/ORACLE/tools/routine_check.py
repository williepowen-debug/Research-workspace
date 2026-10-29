#!/usr/bin/env python3
"""ORACLE routine ran-check (WQ-527 C, DOCKET L847) — run at boot.

For each US weekday (ET) from the routine's install date through today, says plainly whether a
read exists (any ODDS_LOG row stamped on that ET date, routine or live session) and whether the
routine itself ran (a ROUTINE_RUNS.tsv row). A weekday with no read prints `NOT READ` — the usual
cause is a machine switch or a powered-off/idle box (cron runs only while WSL is up).

rc 0 = every weekday read · rc 1 = at least one weekday NOT READ · rc 2 = cannot evaluate.
Market holidays are listed like any weekday; O3 treats a holiday pull as context, not a read.
"""
import csv, datetime as dt, os, socket, sys
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
HERE = os.path.dirname(os.path.abspath(__file__))
WB = os.path.join(HERE, "..", "workbook")
ODDS = os.path.join(WB, "ODDS_LOG.tsv")
RUNS = os.path.join(WB, "ROUTINE_RUNS.tsv")
INSTALLED = dt.date(2026, 10, 29)  # first weekday the routine could run


def et_date(stamp):
    t = dt.datetime.strptime(stamp, "%Y-%m-%dT%H:%MZ").replace(tzinfo=dt.timezone.utc)
    return t.astimezone(ET).date()


def main():
    if not os.path.exists(ODDS):
        print("ROUTINE-CHECK CANNOT-EVALUATE: no ODDS_LOG"); return 2
    read_days = set()
    with open(ODDS) as fh:
        for line in fh:
            if line[:2] == "20":
                read_days.add(et_date(line.split("\t", 1)[0]))
    runs = {}
    if os.path.exists(RUNS):
        with open(RUNS, newline="") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                runs[dt.date.fromisoformat(r["et_date"])] = r
    today = dt.datetime.now(ET).date()
    day, missed = INSTALLED, []
    print(f"ORACLE routine ran-check — today {today} ET, this box {socket.gethostname()}")
    while day <= today:
        if day.weekday() < 5:
            r = runs.get(day)
            src = f"routine {r['status']} on {r['host']}" if r else "live session (no routine row)"
            if day in read_days:
                print(f"  {day} {day:%a}  READ      {src}")
            elif day == today:
                print(f"  {day} {day:%a}  PENDING   no read yet today")
            else:
                print(f"  {day} {day:%a}  NOT READ  routine did not run and no session pulled")
                missed.append(day)
        day += dt.timedelta(days=1)
    if missed:
        print(f"ROUTINE-CHECK MISSED {len(missed)}: " + ", ".join(map(str, missed))
              + " — check the box was on and `crontab -l` holds the ORACLE line (SCHEDULED_RUNS.md)")
        return 1
    print("ROUTINE-CHECK OK"); return 0


if __name__ == "__main__":
    sys.exit(main())
