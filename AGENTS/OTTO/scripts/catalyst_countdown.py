#!/usr/bin/env python3
"""
OTTO Catalyst Countdown
Reads docket/CATALYSTS.tsv and shows calendar/trading-day countdown to each event.
Flags anything within 5 trading days. Highlights 🔴 priority events within horizon.
Also surfaces past-but-recent rows (last 10 days) so the boot past-due-catch never
misses a fired catalyst that hasn't been swept.

OTTO's docket is sparse and long-dated (fraud hearings, bank earnings, trial dates,
prediction-resolve milestones), so the default look-ahead is wider than the oil/JGB
agents (150 days vs 60).

Usage:
  .venv/bin/python3 AGENTS/OTTO/scripts/catalyst_countdown.py
  .venv/bin/python3 AGENTS/OTTO/scripts/catalyst_countdown.py --days 200
"""

import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

OTTO_DIR = Path(__file__).resolve().parent.parent
REPO = OTTO_DIR.parent.parent
CATALYSTS_TSV = OTTO_DIR / "docket" / "CATALYSTS.tsv"
STATUS_MD = OTTO_DIR / "STATUS.md"

DEFAULT_HORIZON = 150      # days to look ahead (sparse, long-dated docket)
PAST_RETENTION_MIN = 10    # floor — daily-cadence operation
PAST_RETENTION_MAX = 120   # ceiling — past this, the docket is the record, not the boot


def past_retention_days():
    """Look-back window for the fired-catalyst sweep, sized to how long OTTO has been dark.

    A FIXED window is wrong for this agent. OTTO is Tier-2 / spawn-gated and routinely
    goes dark longer than 10 days (21 days, 2026-07-04 -> 2026-07-25), which silently
    ages fired catalysts out of the past-due-catch before they were ever swept — the
    Jul 14 Q2-bank row, an OTTO-30 input, aged out exactly this way.

    The window tracks "everything that fired since I last wrote back." Deliberately
    asymmetric: re-showing an already-swept row costs one line of noise; hiding an
    unswept one costs a catalyst.

    ⚠ 2026-08-27 — BASIS CORRECTED, and the original was defective in the silent
    direction. This sized the window off `STATUS.md`'s **mtime**, which root
    Data-Hygiene canon forbids because **git sync restamps it**
    (`finding_mtime_is_corrupted_by_git_sync`). On any desk that pulls at session
    start, `dark_days` reads ≈0, the window collapses to the 10-day floor, and fired
    rows older than the floor age out BEFORE being swept — which is precisely the miss
    this function exists to prevent. It fails as a clean "nothing fired" line, so
    nothing about the output would reveal it. Found by ZHAO while porting this
    function as a donor, routed by DAEDALUS 2026-08-21; verified against this file
    2026-08-27 before back-porting.

    Basis order is now git commit time → content vintage → mtime (last resort), and
    the basis that answered is RETURNED so the caller can print it — a corrected
    mechanism whose basis is invisible is one restamp away from being wrong again.
    """
    lc, basis = _last_closeout()
    dark_days = (date.today() - lc).days + 3  # +3 grace
    return max(PAST_RETENTION_MIN, min(dark_days, PAST_RETENTION_MAX)), basis


def _git_commit_date(path):
    """Canon-preferred vintage: git commit time, NOT mtime (git sync restamps mtime)."""
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO), "log", "-1", "--format=%cI", "--", str(path)],
            capture_output=True, text=True, timeout=10)
        stamp = out.stdout.strip()[:10]
        return datetime.strptime(stamp, "%Y-%m-%d").date() if stamp else None
    except Exception:
        return None


def _last_closeout():
    """When did OTTO last write back? git commit → content vintage → mtime → floor."""
    d = _git_commit_date(STATUS_MD)
    if d:
        return d, "git-commit"
    try:  # content vintage: the newest dated row the docket itself carries
        best = date.min
        for row in (load_catalysts() or []):
            try:
                best = max(best, datetime.strptime(row["date"].strip(), "%Y-%m-%d").date())
            except (ValueError, KeyError, AttributeError):
                continue
        if best != date.min:
            return best, "content"
    except Exception:
        pass
    try:
        return datetime.fromtimestamp(STATUS_MD.stat().st_mtime).date(), "mtime⚠️"
    except OSError:
        return date.today() - timedelta(days=PAST_RETENTION_MIN), "floor"


def load_catalysts():
    if not CATALYSTS_TSV.exists():
        return None
    catalysts = []
    with open(CATALYSTS_TSV) as f:
        header = f.readline().rstrip("\n").split("\t")
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
    print(f"  OTTO Catalyst Countdown — {now}  ({horizon}-day horizon)")
    print(f"  '~' prefix = modeled/projected date (not source-confirmed; may revise)")
    print(f"{'='*72}")

    catalysts = load_catalysts()
    if catalysts is None:
        print(f"\n  ERROR: {CATALYSTS_TSV} not found.")
        return 1
    if not catalysts:
        print(f"\n  (No catalyst rows in docket.)")
        return 0

    upcoming = []
    recent_past = []
    horizon_cutoff = today + timedelta(days=horizon)
    past_retention, retention_basis = past_retention_days()
    past_cutoff = today - timedelta(days=past_retention)

    for c in catalysts:
        try:
            edate = datetime.strptime(c["date"], "%Y-%m-%d").date()
        except (ValueError, KeyError):
            continue
        if edate < today:
            if edate >= past_cutoff:
                recent_past.append((edate, c))
        elif edate <= horizon_cutoff:
            upcoming.append((edate, c))

    # Past-due-catch: recently fired, surface for sweep
    if recent_past:
        recent_past.sort(key=lambda x: x[0])
        print(f"\n  ⚠️  RECENTLY FIRED (last {past_retention} days = since last closeout, basis={retention_basis} — sweep now)")
        print(f"  {'-'*68}")
        for edate, c in recent_past:
            days_since = (today - edate).days
            print(f"  {c.get('priority','').strip() or '  '} {edate.strftime('%Y-%m-%d')} ({edate.strftime('%a')})  {days_since}d ago  {c.get('event','')}")

    upcoming.sort(key=lambda x: x[0])
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
            marker = "~" if c.get("date_class", "").strip() == "modeled" else " "
            print(f"  {pri} {marker}{edate.strftime('%Y-%m-%d')} ({edate.strftime('%a')})  {cal_days:>2}d cal / {trd:>2}d trd  {c.get('event','')}")
            check = c.get("what_to_check", "")
            if check:
                print(f"       ↳ check: {check}")
            sig = c.get("threshold_signal", "")
            if sig and sig.lower() not in ("routine", ""):
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
            event = c.get("event", "")
            if len(event) > 50:
                event = event[:47] + "..."
            marker = "~" if c.get("date_class", "").strip() == "modeled" else " "
            print(f"  {pri} {marker}{edate.strftime('%Y-%m-%d')} ({edate.strftime('%a')})  {cal_days:>3}d cal / {trd:>3}d trd  {event}")

    high_pri = [x for x in upcoming if "🔴" in x[1].get("priority", "")]
    if high_pri:
        print(f"\n  🔴 HIGH PRIORITY in horizon: {len(high_pri)}")
        for edate, c in high_pri:
            cal_days = (edate - today).days
            print(f"     • {edate.strftime('%a %b %d')} ({cal_days}d) — {c.get('event','')}")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
