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

# ── SCHEDULED-PUBLICATION CANARIES (KB-VIO-226 · v3, 2026-09-04) ────────────────
# A fixed calendar-age threshold is wrong for a series with a publication lag: CFTC
# TFF reports are dated Tuesday and released ~Friday 15:30 ET, so a PERFECTLY
# CURRENT ledger reads 10d old every Friday morning and a >9d rule false-DARKs
# weekly. That was v1's bug and it was real.
#
# ⚠️⚠️ I THEN GOT THE REPLACEMENT WRONG TWICE, THE SAME WAY BOTH TIMES.
#   v2 asserted a fixed Tue-report / Fri+3d-release lag, "zero free parameters".
#       FALSE: federal holidays can delay a release.
#   v3 asserted that a MONDAY federal holiday slips the REPORT DATE Tue -> Wed.
#       ALSO FALSE, and falsified by DATA I ALREADY HAD: `COT_VIX.tsv` contains
#       2026-05-26 (Tuesday) directly after Memorial Day Mon 2026-05-25. CFTC's
#       own history shows Tue 2024-09-03 and Tue 2023-09-05, both immediately
#       after Labor Day. The report date does NOT move to Wednesday — ever. The
#       only non-Tuesday report dates in this desk's whole ledger are two MONDAYS
#       (2023-07-03, 2025-11-10), i.e. the opposite direction.
#
# 🔑 BOTH WRONG VERSIONS PASSED THEIR OWN SELFTESTS, because I wrote the tests
# from the same synthesized model as the code. A selftest cannot falsify the
# premise it was derived from. The second time, the falsifying evidence was
# sitting in the ledger this very module reads.
#
# ⇒ v3 STOPS SYNTHESIZING THE CALENDAR ALTOGETHER. There is no holiday table and
# no release-date arithmetic here any more, because every version of that I have
# written has been wrong and each was wrong in the direction of a false alarm.
# The rule is now derived ONLY from the ledger's own observed dates:
#
#     weekly cadence + a GRACE window wide enough to absorb any documented
#     holiday slippage, and DARK asserted only when the ledger is far enough
#     behind that no single delayed release can explain it.
#
# This trades a few days of detection latency on a WEEKLY instrument for the
# elimination of a whole class of false alarm — the right trade, since the
# failure this guard exists to catch (a ledger quietly stopping) persists and
# gets LOUDER with time, while a false DARK is read once and dismissed.
# ⚠️ It is deliberately NOT precise about WHEN a report is due. It cannot be:
# that requires CFTC's published release calendar, which is the honest remedy if
# precision is ever needed, and which this desk does not currently ingest.
SCHEDULED = {
    "COT_VIX.tsv": {
        "cadence_days": 7,       # observed in the ledger, not assumed
        "nominal_lag_days": 3,   # report Tue -> release ~Fri; ANNOTATION ONLY
        "grace_days": 4,         # absorbs a holiday-delayed release (documented max ~2)
        "label": "CFTC TFF weekly, Tue report date, released ~Fri 15:30 ET "
                 "(releases can slip on federal holidays — grace applied, "
                 "no holiday table is used)",
    },
}


def reports_behind(spec: dict, last: date, today: date) -> int:
    """Count the scheduled reports after `last` that are provably overdue.

    SEMANTIC, stated first so neither the code nor the tests can quietly drift
    to match the other (which is how the last two versions of this guard went
    wrong): report k after `last` is dated ``last + cadence*k``, released about
    ``+nominal_lag`` after that, and is OVERDUE once ``+grace`` beyond THAT has
    also passed. `behind` is how many such reports are overdue right now.

      0  nothing is provably owed — covers the normal Friday-morning 10d read
         AND any holiday-delayed release inside the grace window
      1  one cycle overdue: a delayed release and a missed pull are
         INDISTINGUISHABLE here, so this is PENDING, never DARK
      2+ no single delayed release explains it — DARK

    Counted explicitly rather than by closed form: this is not hot code, and the
    off-by-one at the grace boundary is exactly the kind of error that has
    already cost this guard two rewrites.
    """
    n = 0
    k = 1
    while True:
        overdue_after = last + timedelta(
            days=spec["cadence_days"] * k + spec["nominal_lag_days"] + spec["grace_days"])
        if overdue_after < today:
            n += 1
            k += 1
            if k > 500:          # bounded; a decade of silence is already DARK
                break
        else:
            break
    return n


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
    # ⚠️ WAS `return []` on both branches — a MISSING OR UNREADABLE MAP READ AS
    # CLEAN (DAEDALUS 🔴#3). Deleting the file this contract exists to police was
    # the cheapest way to satisfy it. Absent is an UNKNOWN, not a pass.
    if not m.exists():
        return [f"CANARY_MAP.md IS MISSING from {VIOLET_DIR} — the staleness "
                f"contract cannot be evaluated at all. CANNOT CERTIFY."]
    try:
        text = m.read_text()
    except OSError as e:
        return [f"CANARY_MAP.md unreadable ({e}) — CANNOT CERTIFY."]
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
    # ⚠️ WIDENED 2026-09-04 (DAEDALUS 🔴#3). The bracket was digits-and-slash ONLY,
    # so every basis-qualified cell this desk actually writes was INVISIBLE:
    # "[8/4 SETTLE]", "[7/28 report]", "[HENRY 7/28]". The matcher saw 2 of 6 live
    # CURRENT cells and reported clean while six were 31-38 days stale — a checker
    # whose blind spot is the desk's own house style. Now: an optional prefix word
    # inside the bracket, and an optional basis word after the date.
    DATE_IN_BRACKET = r"\[(?:[A-Za-z]+\s+)?(\d{1,2})/(\d{1,2})(?:\s+[A-Za-z]+)?\]"
    for mo in re.finditer(rf"(Current\s*{DATE_IN_BRACKET})"
                          rf"|({DATE_IN_BRACKET}\s*\*{{0,2}}(?:{STATE}))",
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
        # Pick the year that minimises |age| — a "[12/24]" cell read in January is
        # 11 months old under today.year and 7 days old under the previous one.
        # v1 assumed today.year and could hand back a NEGATIVE age (a future date),
        # which silently passed the `age > 4` test.
        cands = []
        for yr in (today.year - 1, today.year, today.year + 1):
            try:
                cands.append(date(yr, mon, day))
            except ValueError:
                pass
        if not cands:
            continue
        d = min(cands, key=lambda x: abs((today - x).days))
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
            behind = reports_behind(spec, d, today)
            if behind == 0:
                rows.append((name, ledger, str(d), f"{age}d", "🟢 fresh"))
                if not a.quiet:
                    sched_notes.append(
                        f"  ℹ️  {name}: {age}d old and within contract — {spec['label']}. "
                        f"Nothing is provably owed until "
                        f"{d + timedelta(days=spec['cadence_days'] + spec['nominal_lag_days'] + spec['grace_days'])} "
                        f"(cadence {spec['cadence_days']}d + lag {spec['nominal_lag_days']}d + "
                        f"grace {spec['grace_days']}d). A fixed >9d age rule called this DARK "
                        f"every Friday morning; KB-VIO-226.")
            elif behind == 1:
                # One cycle late is EXACTLY what a holiday-delayed release looks
                # like, and this module no longer claims to know which weeks have
                # holidays. Report it; do not assert failure.
                rows.append((name, ledger, str(d), f"{age}d", "🟡 PENDING"))
                sched_notes.append(
                    f"  🟡 {name}: newest report {d} is {age}d old — ONE cycle past its grace "
                    f"window. This is what a holiday-delayed release looks like AND what a "
                    f"missed pull looks like; they are indistinguishable from here. "
                    f"⚠️ Run `cftc_cot.py --boot`. If it is still behind next week, it is real.")
            else:
                rows.append((name, ledger, str(d), f"{age}d", "🔴 DARK"))
                dark.append(
                    f"{name}: {ledger} newest report {d} = {age}d old, {behind} publication "
                    f"cycles behind ({spec['label']}). No single delayed release explains "
                    f"{behind} cycles.")
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
    """Falsify the cadence rule in BOTH directions.

    ⚠️ AND A STANDING WARNING ABOUT THIS FUNCTION, EARNED THE HARD WAY: the two
    previous versions of this guard ALSO passed their own selftests, because the
    tests were written from the same synthesized calendar model as the code. A
    selftest cannot falsify the premise it was derived from. These checks are
    therefore keyed ONLY to observed cadence and to the ledger's real dates —
    there is no calendar model left here to be wrong about.
    """
    spec = SCHEDULED["COT_VIX.tsv"]
    fails = []

    def ck(label, got, want):
        if got != want:
            fails.append(f"  x {label}\n      got  {got!r}\n      want {want!r}")
        else:
            print(f"  ok {label}")

    due = spec["cadence_days"] + spec["nominal_lag_days"] + spec["grace_days"]  # 14
    ck("grace window is cadence+lag+grace", due, 14)

    # ── the weekly false-DARK this guard exists to kill ──────────────────────
    ck("Fri morning, 10d old, report is current -> not behind",
       reports_behind(spec, date(2026, 8, 25), date(2026, 9, 4)), 0)
    ck("Thu, 9d old -> not behind",
       reports_behind(spec, date(2026, 9, 1), date(2026, 9, 10)), 0)
    ck("13d old, still inside grace -> not behind",
       reports_behind(spec, date(2026, 8, 25), date(2026, 9, 7)), 0)

    # ── the REAL-WORLD dates that falsified v2 and v3, as regressions ────────
    # Memorial Day Mon 2026-05-25 -> the ledger's own next report is TUE 05-26.
    # A guard that expected a Wednesday would have mis-stated the schedule; this
    # one makes no weekday claim at all, so it is simply unaffected.
    ck("post-Memorial-Day Tue report, 10d later -> not behind",
       reports_behind(spec, date(2026, 5, 26), date(2026, 6, 5)), 0)
    ck("post-Labor-Day Tue report (CFTC 2024-09-03 shape) -> not behind",
       reports_behind(spec, date(2024, 9, 3), date(2024, 9, 13)), 0)
    ck("a Monday report date (2025-11-10, real) is handled, not special-cased",
       reports_behind(spec, date(2025, 11, 10), date(2025, 11, 20)), 0)

    # ── and it must still FIRE on a genuinely stalled ledger ─────────────────
    ck("15d old -> ONE cycle late (PENDING band)",
       reports_behind(spec, date(2026, 8, 25), date(2026, 9, 9)), 1)
    # 8/25 + 21d = 9/15. The 9/8 report's release+grace lands ON 9/15, so at that
    # instant it is not YET overdue — 1, not 2. Derived from the semantic above,
    # not read off the implementation.
    ck("21d old -> ONE cycle overdue (grace boundary)",
       reports_behind(spec, date(2026, 8, 25), date(2026, 9, 15)), 1)
    ck("22d old -> TWO cycles behind = DARK",
       reports_behind(spec, date(2026, 8, 25), date(2026, 9, 16)), 2)
    # 8/25 + 35d = 9/29. Overdue reports are 9/1, 9/8, 9/15 (the 9/22 report's
    # grace lands ON 9/29) => THREE. I first wrote 4 here by counting cycles
    # instead of applying the semantic; the semantic is what governs.
    ck("35d old -> THREE cycles behind = DARK",
       reports_behind(spec, date(2026, 8, 25), date(2026, 9, 29)), 3)
    ck("14d = exactly the grace boundary -> still 0",
       reports_behind(spec, date(2026, 8, 25), date(2026, 9, 8)), 0)
    ck("DARK band is monotonic in age",
       [reports_behind(spec, date(2026, 8, 25), date(2026, 8, 25) + timedelta(days=n))
        for n in (10, 14, 15, 22, 29)], [0, 0, 1, 2, 3])

    print()
    if fails:
        print("\n".join(fails))
        print(f"FAILED {len(fails)} check(s)")
        return 1
    print("all cadence-rule selftests pass")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        raise SystemExit(selftest())
    raise SystemExit(main())
