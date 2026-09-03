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

import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))
from tsvutil import read_tsv  # noqa: E402

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
    # Banner-tolerant (PAT-044). Not currently bannered, but the naive readline()
    # form fails SILENTLY the day it is — see scripts/tsvutil.py.
    header, data = read_tsv(CATALYSTS_TSV)
    for parts in data:
        if len(parts) < 2:
            continue
        d = dict(zip(header, parts + [""] * (len(header) - len(parts))))
        rows.append(d)
    return rows


def check_integrity(rows):
    """Docket self-checks. Returns a list of warning strings (empty = clean).

    Added 2026-07-31 after the docket accumulated three DUPLICATE event pairs:
    seven rows were appended on 7/25 without a merge pass against the nine already
    there, so the countdown printed 11 due-events for 8 real ones and each of the
    two highest-priority August catalysts rendered twice. The duplicates were also
    written in a SECOND priority vocabulary (HIGH/MEDIUM/LOW), which prio_rank()
    silently buckets to rank 9 — so the off-schema rows sorted to the bottom
    instead of announcing themselves. Both are one-line checks; the failure was
    that nobody ran one. Mechanize the check, don't remember the ritual.
    """
    warns = []

    # Same-date rows whose event names share a leading token run. Prefix matching
    # alone is not enough: two of the 7/25 duplicates differed only in trailing
    # qualifiers (catchable by prefix), but the third was the SAME release under
    # two framings — "BLS July NFP + UR" vs "BLS July NFP + state CES wages" —
    # which no prefix rule catches. Token overlap does, and it stays quiet about
    # genuinely distinct events that merely share a date (Aug 1 legitimately holds
    # both Banxico remittances and the OFLC H-2A disclosure: 0 shared tokens).
    def toks(s):
        return [t for t in re.sub(r"[^a-z0-9 ]", " ", s.lower()).split() if t]

    for i, a in enumerate(rows):
        for b in rows[i + 1:]:
            if a.get("date", "").strip() != b.get("date", "").strip():
                continue
            ta, tb = toks(a.get("event", "")), toks(b.get("event", ""))
            shared = 0
            for x, y in zip(ta, tb):
                if x != y:
                    break
                shared += 1
            if shared >= 2:
                warns.append(f"LIKELY DUPLICATE ({shared} shared leading tokens): "
                             f"{a.get('date','?')} · {a.get('event','?')[:34]} "
                             f"|| {b.get('event','?')[:34]}")

    for r in rows:
        p = r.get("priority", "")
        if prio_rank(p) == 9:
            warns.append(f"OFF-VOCABULARY priority {p.strip()!r} on {r.get('date','?')} · "
                         f"{r.get('event','?')[:40]} (docket uses 🔴/🟠/🟡/🟢)")

    dates = [parse_date(r.get("date", "")) for r in rows]
    if [d for d in dates if d] != sorted(d for d in dates if d):
        warns.append("ROWS NOT DATE-SORTED (harmless to the countdown, but the file "
                     "is read by eye too)")
    return warns


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

    integrity = check_integrity(cats)
    if integrity:
        print(f"\n  ⚠️  DOCKET INTEGRITY — {len(integrity)} issue(s):")
        for w in integrity:
            print(f"      · {w}")
        print("      (fix in docket/CATALYSTS.tsv; reconcile docket/CALENDAR.md to match)")

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
    #
    # FIRED-ROW RULE (DAEDALUS ⑫(a) flag 2026-08-28, answered 2026-09-02): OTTO's 7/25 rule
    # keeps recently-FIRED rows visible for a look-back so they get swept. This fork does NOT
    # need it, and porting it would be a no-op: `passed` is unconditional on `delta < 0`, with
    # NO look-back window and NO expiry, so a fired or resolved row CANNOT age out of the print.
    # It stays in PASSED, every boot, until a human prunes it at closeout step 9 (docket refresh).
    # That is strictly more conservative than a windowed look-back. DECLINED-AS-NO-OP, not skipped;
    # re-verify this comment against the `delta < 0` branch above before assuming it still holds.
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
