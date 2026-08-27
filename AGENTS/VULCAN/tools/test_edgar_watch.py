#!/usr/bin/env python3
"""
test_edgar_watch.py — falsify every guard in edgar_watch.py, rather than trusting it.

WHY THIS FILE EXISTS: `finding_test_the_guard_not_just_the_guarded` — a guard's own v1 fails
on first RUN, and this desk has bought that lesson twice at real cost (`mag7.py` v1's breadth
leg was untrippable by construction; `tsmc_watch.py` v1 was blind to every declining month
and still wrote 8 clean-looking rows [L-20]). Both were CORRECT-LOOKING. The only thing that
separates a working guard from a decorative one is showing it FIRE.

⚠️ Also `finding_guard_correctness_and_wiring_are_independent` + L-22's third axis (TIMING):
   each test below asks not just "is it right?" but "can it fire, and can it fire in time?"

Run: python3 AGENTS/VULCAN/tools/test_edgar_watch.py     (offline — no network, no writes)
"""
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import edgar_watch as E  # noqa: E402

PASS, FAIL = [], []


def check(name, got, want, why):
    (PASS if got == want else FAIL).append(f"{name}: got {got!r} want {want!r} — {why}")


def mk(rd, fd):
    return (date.fromisoformat(rd), date.fromisoformat(fd),
            (date.fromisoformat(fd) - date.fromisoformat(rd)).days)


# ── 1. THE BACKTEST MUST BE ABLE TO FAIL ─────────────────────────────────────
# The whole predictor rests on this. If backtest() can only ever say PASS it is a
# decoration, exactly like mag7 v1's breadth leg.
tight = [mk("2025-01-31", "2025-03-03"), mk("2025-04-30", "2025-05-31"),
         mk("2025-07-31", "2025-08-31"), mk("2025-10-31", "2025-12-01")]
check("backtest PASS on consistent history", E.backtest(tight)[0], "PASS",
      "held-out lag >= earliest bound derived from the rest")

# held-out filing lands FAR EARLIER than anything in history -> must FAIL
early = tight[:-1] + [mk("2025-10-31", "2025-11-02")]
check("backtest FAILS on an impossibly-early held-out filing", E.backtest(early)[0], "FAIL",
      "THE key test: a predictor whose window opens after the event must say so")

check("backtest UNGRADEABLE on thin history", E.backtest(tight[:2])[0], "UNGRADEABLE",
      "reported, NOT silently downgraded to PASS [the mag7 breadth-leg rule]")

# ── 2. THE EARLIEST BOUND MUST BE min(), NOT median() ────────────────────────
# This is L-22 encoded. If the window opened at the typical lag it would, by construction,
# open AFTER roughly half of all filings — the guard-dated-on-the-event defect rebuilt.
spread = [mk("2025-01-31", "2025-02-20"), mk("2025-04-30", "2025-05-31"),
          mk("2025-07-31", "2025-08-31"), mk("2025-10-31", "2025-12-01")]
w = E.window(spread)
check("window opens at the MINIMUM historical lag", w["min"], 20,
      "L-22: earliest plausible occurrence, never the expected one")
check("window's minimum is strictly below its median", w["min"] < w["med"], True,
      "if min==med the leg cannot be distinguished from a typical-date guard")

# ── 3. THE FY-QUARTER GUARD MUST SKIP, NOT SUPPRESS ──────────────────────────
# v1 of this guard SUPPRESSED the window, which silenced the 10-K rows too and threw away
# a real ORCL Q1 prediction. Both behaviours are tested so the regression cannot return.
q = [mk("2025-08-31", "2025-09-21"), mk("2025-11-30", "2025-12-21"),
     mk("2026-02-28", "2026-03-21")]
fy = [date(2025, 5, 31), date(2026, 5, 31)]
nw = E.next_window(q, date(2026, 4, 1), fy, "10-Q")
check("10-Q projection SKIPS the fiscal-year quarter", nw is not None and nw["skipped_fy_quarter"],
      True, "must step PAST the FY quarter and still return a usable window")
check("10-Q projection lands after the FY end", nw is not None and nw["period_end"] > date(2026, 5, 31),
      True, "the skip must advance the period, not merely flag it")

ann = [mk("2023-05-31", "2023-06-21"), mk("2024-05-31", "2024-06-21"),
       mk("2025-05-31", "2025-06-21")]
nwa = E.next_window(ann, date(2026, 1, 1), fy, "10-K")
check("ANNUAL forms are NOT suppressed by the FY guard", nwa is not None, True,
      "the 10-K is exactly the form that covers the FY end — v1 silenced it")

# ── 4. STALE-SERIES ROLL-FORWARD ─────────────────────────────────────────────
# A quiet leg must mean "nothing due", never "the series stopped and I stopped with it".
old = [mk("2023-01-31", "2023-03-03"), mk("2023-04-30", "2023-05-31"),
       mk("2023-07-31", "2023-08-31")]
nwo = E.next_window(old, date(2026, 8, 27), None, "10-Q")
# ⚠️ SPEC CORRECTED 2026-08-27: this test originally asserted "rolls forward past today" and
# it FAILED — which exposed that the SPEC was wrong, not just the loop bound. Rolling a
# 3-years-dead series forward ~11 periods fabricates a confident window out of an ended
# regime: a worse and quieter failure than the None it replaced. The requirement that
# actually matters is unchanged and still tested here — a stale series must not read as a
# calm one — it is now satisfied by REPORTING staleness instead of projecting through it.
check("stale series is REPORTED stale, not projected", bool(nwo and nwo.get("stale")), True,
      "the staleness IS the finding; a dead series must not yield a confident window")
check("stale result carries how far behind it is", bool(nwo and nwo.get("behind_days", 0) > 300),
      True, "a stale flag with no magnitude cannot be triaged")
check("a HEALTHY series is not flagged stale", E.next_window(q, date(2026, 4, 1), fy, "10-Q").get("stale"),
      False, "the stale guard must not fire on a live series [guard must be specific]")

# ── 5. TIERING MUST FAIL TOWARD VISIBILITY ───────────────────────────────────
check("8-K is tier 1", E.tier("8-K"), 1, "material-agreement disclosures must surface")
check("10-Q is tier 1", E.tier("10-Q"), 1, "")
check("Form 4 is tier 3", E.tier("4"), 3, "insider noise, logged not surfaced")
check("UNKNOWN form defaults to SURFACED", E.tier("SOMETHING-NEW-2027"), 2,
      "an unrecognised form must never be silently suppressed — fail toward visibility")

# ── 6. RAGGED-FEED DETECTION ─────────────────────────────────────────────────
# A ragged parallel-array feed mis-pairs a form with another filing's date and every row
# still looks well-formed. `finding_partial_record_written_as_final_never_heals`.
import json as _json  # noqa: E402
_real = E._get
try:
    E._get = lambda u: _json.dumps({"filings": {"recent": {
        "form": ["8-K", "10-Q"], "filingDate": ["2026-01-01"],   # <- short by one
        "accessionNumber": ["a", "b"], "primaryDocument": ["x", "y"],
        "reportDate": ["2026-01-01", "2026-01-02"]}}}).encode()
    try:
        E.fetch(1)
        check("ragged feed raises", False, True, "must refuse to pair mismatched arrays")
    except ValueError as e:
        check("ragged feed raises ValueError", "ragged" in str(e), True, str(e)[:60])
    E._get = lambda u: _json.dumps({"filings": {"recent": {"form": ["8-K"]}}}).encode()
    try:
        E.fetch(1)
        check("missing-field feed raises", False, True, "schema change must be loud")
    except ValueError as e:
        check("missing-field feed raises ValueError", "missing" in str(e), True, str(e)[:60])
finally:
    E._get = _real

# ── report ───────────────────────────────────────────────────────────────────
print("=" * 74)
print("  edgar_watch guard falsification")
print("=" * 74)
for p in PASS:
    print(f"  ✓ {p.split(':')[0]}")
if FAIL:
    print(f"\n  🔴 {len(FAIL)} GUARD(S) DID NOT BEHAVE AS SPECIFIED:")
    for f in FAIL:
        print(f"     {f}")
print(f"\n  {len(PASS)} passed, {len(FAIL)} failed")
sys.exit(1 if FAIL else 0)
