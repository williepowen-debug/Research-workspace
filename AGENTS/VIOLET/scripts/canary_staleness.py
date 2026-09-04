#!/usr/bin/env python3
"""VIOLET CANARY_MAP staleness enforcement — the check the map has been asking for since v1.0.

`CANARY_MAP.md` § Staleness audit contract declares: *"A canary is DARK when its
last pull exceeds 2x its stated cadence (EOD instruments: >2 trading days; weekly
COT: >9 days)."* That contract was **UNENFORCED FROM v1.0 UNTIL 2026-07-28**, and
when it was finally audited by hand the file was **breaching it on five rows** —
COT 21d, JPY 11d, OVX 11d, cheap-tail 6d, and a Tier-3 GEX band 18d that sits
inside a registered VIOLET fire-condition.

The map names its own root cause: *"extend `ledger_staleness.py` coverage to this
file's Tier-1/2 pull dates = a future small ask"* had sat in the doc since v1.0 and
**was never built, so the only thing enforcing the contract was remembering to.**
The instrument the map exists to protect — a canary going dark unnoticed — went
dark inside the map's own text. (auto-memory `finding_mechanize_the_cap_not_the_ritual`.)

⚠️ WHY THIS LIVES IN `AGENTS/VIOLET/scripts/` AND NOT IN THE ROOT `ledger_staleness.py`:
the root script is a shared file VIOLET may not commit (root CLAUDE.md § Git
Protocol). The contract, the map and every backing ledger are VIOLET-owned, so the
enforcement belongs here. Wired into VIOLET's own `boot.py`.

METHOD — content vintage, never mtime. Each Tier-1 canary writes a dated row to a
workbook ledger; we read the MAX DATE in that ledger and compare it to the row's
stated cadence. ⚠️ mtime is corrupted by git sync (a pull restamps every file), so
an mtime-based freshness check fails FALSE-NEGATIVE — the failure direction that
lets a dark canary read as fresh (auto-memory `finding_mtime_is_corrupted_by_git_sync`).

Exit codes: 0 = all canaries within contract (or only un-ledgered rows flagged);
1 = at least one DARK canary, with --strict.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/canary_staleness.py
  .venv/bin/python3 AGENTS/VIOLET/scripts/canary_staleness.py --quiet   # boot mode
"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
from pathlib import Path

VIOLET_DIR = Path(__file__).resolve().parents[1]
WB = VIOLET_DIR / "workbook"

# (canary, ledger, date column, cadence label, DARK threshold in CALENDAR days)
# Thresholds are 2x cadence per the contract, expressed in calendar days with
# weekend slack so a routine Fri-pull read on Monday does not false-fire.
CANARIES = [
    ("VIX3M/VIX inversion", "VX_DAILY.tsv",  "date",        "EOD daily", 4),
    ("VVIX",                "VX_DAILY.tsv",  "date",        "EOD daily", 4),
    ("SKEW + sustain",      "VX_DAILY.tsv",  "date",        "EOD daily", 4),
    ("JPY vol (carry)",     "JPY_VOL.tsv",   "date",        "EOD daily", 4),
    ("OVX/VIX ratio",       "OVX.tsv",       "date",        "EOD daily", 4),
    ("Cheap-tail window",   "CHEAP_TAIL.tsv","date",        "EOD daily", 4),
    # COT is NOT a calendar-age row — see SCHEDULED below. `None` marks it.
    ("COT VIX lev-money",   "COT_VIX.tsv",   "report_date", "CFTC TFF weekly", None),
]

# ── SCHEDULED-PUBLICATION CANARIES (added 2026-09-04, KB-VIO-226) ───────────────
# A fixed calendar-age threshold is WRONG for any series with a publication lag.
# CFTC TFF report dates are nominally Tuesdays, released the following Friday at
# 15:30 ET, so a PERFECTLY CURRENT ledger reads 10d old every Friday morning and a
# >9d rule fires a guaranteed false DARK once a week, forever.
#
# ⚠️ CORRECTION 2026-09-04 (PM), AFTER AN EXTERNAL REVIEW (Codex, routed by Will).
# The first version of this fix asserted a fixed Tue→Fri+3d lag and called itself
# "zero free parameters, self-calibrating." **THAT CLAIM WAS WRONG**, and it was
# wrong in the same direction as the bug it replaced — a false DARK on a schedule
# I had not modelled. Per CFTC's published release schedule, FEDERAL HOLIDAYS move
# BOTH ENDS of the window:
#
#   · Monday holiday  → the REPORT DATE moves Tue → Wed (collection slips a day)
#   · Friday holiday  → the RELEASE moves to the following Monday
#
# So Juneteenth (Fri 2026-06-19) and Christmas (Fri 2026-12-25) would each have
# produced a multi-day false DARK under v1 of this "fix". The arithmetic is not
# self-calibrating; it depends on a FEDERAL HOLIDAY TABLE, which is a maintained
# input with an expiry — and this module now says so out loud rather than
# claiming a self-sufficiency it does not have.
#
# 🔑 AND BECAUSE MY MODEL OF THIS SCHEDULE HAS NOW BEEN WRONG ONCE, THE GUARD NO
# LONGER TRUSTS IT ALONE. When the ledger is exactly ONE report behind and any
# federal holiday sits in the window, the state is 🟡 PENDING, not 🔴 DARK — an
# unpublished report is an UNKNOWN, not a failure. Two or more reports behind is
# DARK regardless, because no single holiday delays two releases.
#
# ⚠️ FEDERAL holidays are NOT the NYSE holidays in catalyst_countdown.py, and the
# two tables must not be merged: Good Friday closes the NYSE and is not federal;
# Columbus Day and Veterans Day are federal and the NYSE trades through them.
FEDERAL_HOLIDAYS = {
    # 2026
    "2026-01-01", "2026-01-19", "2026-02-16", "2026-05-25",
    "2026-06-19",  # Juneteenth (Fri) — would have false-DARKed v1
    "2026-07-03",  # Independence Day observed (Jul 4 is a Saturday)
    "2026-09-07",  # Labor Day (Mon) — moves the report date Tue->Wed
    "2026-10-12", "2026-11-11", "2026-11-26",
    "2026-12-25",  # Christmas (Fri) — would have false-DARKed v1
    # 2027
    "2027-01-01", "2027-01-18", "2027-02-15", "2027-05-31",
    "2027-06-18",  # Juneteenth observed (Jun 19 is a Saturday)
    "2027-07-05",  # Independence Day observed (Jul 4 is a Sunday)
    "2027-09-06", "2027-10-11", "2027-11-11", "2027-11-25",
    "2027-12-24",  # Christmas observed (Dec 25 is a Saturday)
}
HOLIDAY_COVERAGE = (date(2026, 1, 1), date(2027, 12, 31))

SCHEDULED = {
    "COT_VIX.tsv": {
        "nominal_report_weekday": 1,   # Tuesday (Mon=0)
        "nominal_release_weekday": 4,  # Friday
        "release_hour_et": 15,
        "release_minute_et": 30,
        "label": "CFTC TFF: Tue report date, released Fri 15:30 ET "
                 "(both shift on federal holidays — see FEDERAL_HOLIDAYS)",
    },
}


def _is_fed_holiday(d: date) -> bool:
    return d.isoformat() in FEDERAL_HOLIDAYS


def report_and_release(spec: dict, week_monday: date) -> tuple[date, datetime]:
    """(report_date, release_instant) for the week beginning `week_monday`.

    Monday holiday  -> report date slips Tue -> Wed.
    Release lands on that week's Friday, pushed forward past any holiday/weekend.
    """
    report = week_monday + timedelta(days=spec["nominal_report_weekday"])
    if _is_fed_holiday(week_monday):
        report += timedelta(days=1)                      # Tue -> Wed
    rel_day = week_monday + timedelta(days=spec["nominal_release_weekday"])
    while _is_fed_holiday(rel_day) or rel_day.weekday() >= 5:
        rel_day += timedelta(days=1)                     # Fri holiday -> next Mon
    return report, datetime.combine(
        rel_day, time(spec["release_hour_et"], spec["release_minute_et"]), tzinfo=ET)


def expected_report_date(spec: dict, now_et: datetime) -> date:
    """Latest report date whose release has ALREADY happened, as of now_et."""
    wk = now_et.date() - timedelta(days=now_et.date().weekday())   # this Monday
    for _ in range(60):
        report, release = report_and_release(spec, wk)
        if release <= now_et:
            return report
        wk -= timedelta(days=7)
    return report


def holiday_in_window(lo: date, hi: date) -> list[str]:
    return sorted(h for h in FEDERAL_HOLIDAYS if lo.isoformat() <= h <= hi.isoformat())


def coverage_ok(d: date) -> bool:
    return HOLIDAY_COVERAGE[0] <= d <= HOLIDAY_COVERAGE[1]


# Rows with a registered threshold but NO backing ledger — they cannot be checked
# mechanically, which is itself worth surfacing rather than silently passing.
UNLEDGERED = [
    ("MOVE (rates vol)", "investing.com primary; yf ^MOVE unreliable as sole source"),
    ("CCC-BB dispersion + CCC OAS", "FRED via fred_fetch --summary (cache dir, not a dated ledger)"),
    ("Broad equity put/call", "WALTER-intake only — genuinely un-pullable, declared dark at v1.2"),
]


def check_map_agreement() -> list[str]:
    """AGREEMENT half — added 2026-07-30 PM, hours after the age half, because the
    age half MISSED the very breach it was built to prevent.

    ⚠️ THE GAP, stated plainly: `canary_staleness.py` v1 asked *"is the LEDGER
    fresh?"* and answered yes for every row — while `CANARY_MAP.md` was asserting
    **"Current [7/28]: RV10 3.47%"** against a ledger that read **4.81% on 7/30**,
    a 39% error, and **"[7/27] DORMANT 2/4"** against an actual 1/4. **Both ledgers
    were green.** Age was never the failure mode; AGREEMENT was — the same
    distinction that KB-VIO-142 turned on, where a staleness check passed a file
    that was fresh and affirmatively wrong (`finding_freshness_check_cannot_catch_a_fresh_lie`).
    Third time this file has carried a stale "current".

    This extracts every `Current [M/D]` / `[M/D] STATE n/4` assertion from
    CANARY_MAP and compares its DATE against the backing ledger's newest row.
    It deliberately does NOT try to parse the prose values — matching a date is
    robust; regexing narrative numbers is not, and a check that breaks on wording
    is worse than none.
    """
    import re
    m = VIOLET_DIR / "CANARY_MAP.md"
    if not m.exists():
        return []
    try:
        text = m.read_text()
    except OSError:
        return []
    today = date.today()
    out = []
    STATE = r"DORMANT|ARMING|OPEN|FIRE|CALM|WATCH|BIN-A"
    # ⚠️ v1 of this matcher FALSE-POSITIVED on its first real run: it looked only at
    # the 90 chars BEFORE the date and treated any state-ish word as evidence of a
    # current claim, so "Validated: **7/6-7/10 fires** … [7/27]" matched on "fires",
    # and a RETROSPECTIVE note (*"this cell read … until 7/28 — 11 days stale"*) got
    # reported as a live stale cell. Wrong direction is cheap here (noise, not a
    # miss) but a checker that cries wolf gets ignored, which turns it into a miss.
    # Tightened to two PRECISE shapes plus an explicit retrospective exclusion.
    for mo in re.finditer(r"(Current\s*\[(\d{1,2})/(\d{1,2})\])"          # "Current [7/30]"
                          rf"|(\[(\d{{1,2}})/(\d{{1,2}})\]\s*\*{{0,2}}(?:{STATE}))",  # "[7/29] DORMANT"
                          text, re.I):
        g = mo.groups()
        mon, day = (int(g[1]), int(g[2])) if g[0] else (int(g[4]), int(g[5]))
        if not (1 <= mon <= 12 and 1 <= day <= 31):
            continue
        # EXCLUDE retrospective notes ABOUT a past staleness — they legitimately
        # quote an old date and must not be re-reported as the thing they document.
        window = text[max(0, mo.start() - 160): mo.start() + 160]
        if re.search(r"until \d{1,2}/\d{1,2}|days stale|this cell read|read \"", window, re.I):
            continue
        try:
            d = date(today.year, mon, day)
        except ValueError:
            continue
        age = (today - d).days
        if age > 4:  # same 2x-EOD-cadence contract as the ledger half
            snippet = text[mo.start(): mo.start() + 60].replace("\n", " ")
            out.append(f"CANARY_MAP asserts a CURRENT reading dated {mon}/{day} "
                       f"({age}d old, contract >4d): …{snippet}…")
    return out


def max_date(path: Path, col: str) -> date | None:
    if not path.exists():
        return None
    best = None
    try:
        with path.open(newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                v = (row.get(col) or "").strip()
                if not v:
                    continue
                try:
                    d = datetime.fromisoformat(v).date()
                except ValueError:
                    continue
                if best is None or d > best:
                    best = d
    except OSError:
        return None
    return best


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true", help="print only breaches (boot mode)")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any canary is DARK")
    a = ap.parse_args(argv)

    today = date.today()
    dark, rows, sched_notes = [], [], []
    now_et = datetime.now(ET)
    for name, ledger, col, cadence, limit in CANARIES:
        d = max_date(WB / ledger, col)
        if d is None:
            rows.append((name, ledger, "NO DATA", "?", "🔴 DARK"))
            dark.append(f"{name}: no dated rows in {ledger}")
            continue
        age = (today - d).days
        spec = SCHEDULED.get(ledger)
        if spec is not None:
            exp = expected_report_date(spec, now_et)
            if not coverage_ok(exp) or not coverage_ok(today):
                rows.append((name, ledger, str(d), f"{age}d", "🟡 UNKNOWN"))
                dark.append(
                    f"{name}: federal-holiday table covers {HOLIDAY_COVERAGE[0]}..{HOLIDAY_COVERAGE[1]}; "
                    f"{exp}/{today} is outside it, so the release schedule cannot be computed. "
                    f"FAILING CLOSED — extend FEDERAL_HOLIDAYS in canary_staleness.py.")
            elif d >= exp:
                rows.append((name, ledger, str(d), f"{age}d", "🟢 fresh"))
                if not a.quiet:
                    sched_notes.append(
                        f"  ℹ️  {name}: {age}d old and CORRECT — {exp} is the newest report "
                        f"released as of now ({spec['label']}). A fixed >9d age rule called "
                        f"this DARK every Friday morning; KB-VIO-226.")
            else:
                behind = len([w for w in range(1, 60)
                              if (exp - timedelta(days=7 * w)) >= d]) or 1
                hols = holiday_in_window(d, today)
                if behind <= 1 and hols:
                    # ⚠️ FAIL SAFE. My model of this schedule has already been wrong
                    # once (v1 ignored holidays entirely). One report behind WITH a
                    # holiday in the window is an UNKNOWN, not a failure — an
                    # unpublished report and a missed pull look identical from here.
                    rows.append((name, ledger, str(d), f"{age}d", "🟡 PENDING"))
                    sched_notes.append(
                        f"  🟡 {name}: newest ledger report {d}, expected {exp} — ONE behind, "
                        f"and federal holiday(s) {', '.join(hols)} fall in the window. "
                        f"CFTC shifts BOTH the report date (Mon holiday: Tue->Wed) and the "
                        f"release (Fri holiday: -> Mon). Treating as PENDING, not DARK. "
                        f"⚠️ If it is still behind after the next clean week, it is real.")
                else:
                    rows.append((name, ledger, str(d), f"{age}d", "🔴 DARK"))
                    dark.append(
                        f"{name}: {ledger} newest report {d}, expected {exp} — "
                        f"{behind} publication(s) behind ({spec['label']})"
                        + (f"; holidays {', '.join(hols)} in window cannot explain "
                           f"{behind} missed releases" if hols else ""))
            continue
        state = "🔴 DARK" if age > limit else ("🟡 aging" if age > limit // 2 else "🟢 fresh")
        if age > limit:
            dark.append(f"{name}: {ledger} last row {d} = {age}d old (contract: DARK >{limit}d, {cadence})")
        rows.append((name, ledger, str(d), f"{age}d", state))

    if not a.quiet:
        print("CANARY_MAP staleness — contract: DARK when last pull > 2x cadence")
        print(f"{'canary':30s} {'ledger':16s} {'last row':12s} {'age':>5s}  state")
        print("-" * 78)
        for r in rows:
            print(f"{r[0]:30s} {r[1]:16s} {r[2]:12s} {r[3]:>5s}  {r[4]}")
        print()
        print("Un-ledgered rows (cannot be checked mechanically — verify by hand):")
        for n, why in UNLEDGERED:
            print(f"  · {n:32s} {why}")
        print()

    stale_cells = check_map_agreement()
    if stale_cells and not a.quiet:
        print("Doc-vs-ledger agreement (the half the age check cannot see):")
        for s in stale_cells:
            print(f"  ⚠️  {s}")
        print()
    elif not a.quiet:
        print("  ✓ no stale CURRENT assertions in CANARY_MAP")
        print()

    for n in sched_notes:
        print(n)
    if sched_notes:
        print()

    if dark or stale_cells:
        if dark:
            print(f"  🔴 CANARY_MAP CONTRACT BREACH — {len(dark)} DARK LEDGER(S):")
            for d_ in dark:
                print(f"     {d_}")
        if stale_cells:
            print(f"  🔴 CANARY_MAP STALE 'CURRENT' CELLS — {len(stale_cells)}:")
            for s in stale_cells:
                print(f"     {s}")
        return 1 if a.strict else 0
    if not a.quiet:
        print("  ✓ all ledger-backed canaries within contract")
    return 0


def selftest() -> int:
    """Falsify the schedule rule in BOTH directions before trusting it.

    A guard that only passes on the case it was built for is untested — this
    module's own history (the age half MISSED the breach it was built to prevent,
    2026-07-30) is why this exists as code rather than as a paragraph.
    """
    spec = SCHEDULED["COT_VIX.tsv"]
    fails = []

    def ck(label, got, want):
        if got != want:
            fails.append(f"  x {label}\n      got  {got!r}\n      want {want!r}")
        else:
            print(f"  ok {label}")

    # ── expected_report_date across the release boundary ────────────────────
    for label, now, want in [
        ("Fri pre-release 13:44 -> prior Tue", datetime(2026, 9, 4, 13, 44, tzinfo=ET), date(2026, 8, 25)),
        ("Fri 15:29, one minute before",       datetime(2026, 9, 4, 15, 29, tzinfo=ET), date(2026, 8, 25)),
        ("Fri 15:30, the release instant",     datetime(2026, 9, 4, 15, 30, tzinfo=ET), date(2026, 9, 1)),
        ("Sat after release",                  datetime(2026, 9, 5, 10, 0, tzinfo=ET),  date(2026, 9, 1)),
        ("Mon holiday (Labor Day)",            datetime(2026, 9, 7, 10, 0, tzinfo=ET),  date(2026, 9, 1)),
        ("Thu, 9d old and CORRECT",            datetime(2026, 9, 10, 10, 0, tzinfo=ET), date(2026, 9, 1)),
        # ⚠️ CHANGED 2026-09-04 PM, and NOT to make a red test pass. v1 of this
        # file asserted 2026-09-08 here. That expectation was WRONG: Labor Day is
        # Mon 2026-09-07, so CFTC collection slips and the report date is Wed
        # 09-09. The corrected code produced 09-09, the stale assertion failed,
        # and the assertion is what was wrong. Tightening, not loosening — the
        # old value encoded the very bug this pass fixes.
        ("next Fri post-release rolls on (Labor Day week -> WED 09-09)",
         datetime(2026, 9, 11, 16, 0, tzinfo=ET), date(2026, 9, 9)),
    ]:
        ck(label, expected_report_date(spec, now), want)

    # ⚠️ REPLACED 2026-09-04 PM. The old assertion was "every expected date is a
    # Tuesday" — which is exactly the false invariant this pass removed, so it
    # necessarily failed once the code became correct. The real invariant is
    # weaker and is the honest one: a report date is a Tuesday UNLESS that week's
    # Monday is a federal holiday, in which case it is the Wednesday.
    def _weekday_ok(d0: date) -> bool:
        exp = expected_report_date(spec, datetime(d0.year, d0.month, d0.day, 12, 0, tzinfo=ET))
        wk_mon = exp - timedelta(days=exp.weekday())
        return exp.weekday() == (2 if _is_fed_holiday(wk_mon) else 1)

    ck("report date is Tue, or Wed after a Monday federal holiday",
       all(_weekday_ok(date(2026, 9, d)) for d in range(1, 29)), True)
    ck("and that exception actually bites in Sep 2026 (Labor Day)",
       any(expected_report_date(spec, datetime(2026, 9, d, 12, 0, tzinfo=ET)).weekday() == 2
           for d in range(1, 29)), True)

    # ── HOLIDAY CASES — the ones v1 of this fix got WRONG (external review) ──
    # Each of these would have produced a multi-day FALSE DARK under the fixed
    # Tue->Fri+3d assumption. They are the regression tests for that mistake.
    ck("Juneteenth Fri 2026-06-19: release slips to Mon 06-22",
       report_and_release(spec, date(2026, 6, 15))[1].date(), date(2026, 6, 22))
    ck("  ...so on Fri 06-19 16:00 the 06-16 report is NOT yet expected",
       expected_report_date(spec, datetime(2026, 6, 19, 16, 0, tzinfo=ET)), date(2026, 6, 9))
    ck("  ...and after Mon 06-22 15:30 it IS",
       expected_report_date(spec, datetime(2026, 6, 22, 16, 0, tzinfo=ET)), date(2026, 6, 16))
    ck("Christmas Fri 2026-12-25: release slips to Mon 12-28",
       report_and_release(spec, date(2026, 12, 21))[1].date(), date(2026, 12, 28))
    ck("Labor Day Mon 2026-09-07: REPORT DATE slips Tue->Wed 09-09",
       report_and_release(spec, date(2026, 9, 7))[0], date(2026, 9, 9))
    ck("  ...its release is still Fri 09-11",
       report_and_release(spec, date(2026, 9, 7))[1].date(), date(2026, 9, 11))
    ck("normal week: report Tue, release Fri",
       report_and_release(spec, date(2026, 8, 24)), (date(2026, 8, 25),
       datetime(2026, 8, 28, 15, 30, tzinfo=ET)))
    ck("holiday_in_window sees Labor Day", holiday_in_window(date(2026, 9, 1), date(2026, 9, 10)),
       ["2026-09-07"])
    ck("coverage_ok rejects 2028", coverage_ok(date(2028, 1, 3)), False)

    # ── the DARK path must still fire on a genuinely behind ledger ───────────
    # THE POINT OF THIS BLOCK: the fix removes a false alarm, and the risk of any
    # such fix is that it removes the TRUE alarm with it. Fail closed, loudly.
    now = datetime(2026, 9, 4, 16, 0, tzinfo=ET)   # post-release; expected = 9/1
    exp = expected_report_date(spec, now)
    ck("post-release expected is 2026-09-01", exp, date(2026, 9, 1))
    ck("ledger AT expected -> not dark",      date(2026, 9, 1) < exp, False)
    ck("ledger ONE report behind -> DARK",    date(2026, 8, 25) < exp, True)
    ck("ledger THREE reports behind -> DARK", date(2026, 8, 11) < exp, True)
    ck("3-behind counts 3 publications",      (exp - date(2026, 8, 11)).days // 7, 3)
    # and the pre-release instant must NOT call the same ledger dark
    exp_pre = expected_report_date(spec, datetime(2026, 9, 4, 13, 44, tzinfo=ET))
    ck("SAME ledger pre-release -> not dark", date(2026, 8, 25) < exp_pre, False)

    print()
    if fails:
        print("\n".join(fails))
        print(f"FAILED {len(fails)} check(s)")
        return 1
    print("all schedule-rule selftests pass")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        raise SystemExit(selftest())
    raise SystemExit(main())
