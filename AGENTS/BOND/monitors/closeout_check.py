#!/usr/bin/env python3
"""BOND — ONE closeout pass: numeric drift + stale assertions, one fetch, one verdict.

WHY THIS EXISTS
---------------
As of 2026-08-20 this desk had two complementary checkers and no single way to
run them:

  * `boot_recompute.py`  -- stale NUMBERS on the boot-unread surfaces
                            (TRADE.md, monitors/*.md, NEXUS_BRIEF.md)
  * `assertion_check.py` -- stale ASSERTIONS, which contain no number at all
                            ("PREDICTIONS.tsv IS EMPTY" with two rows OPEN)

Two commands is one command too many at closeout. The 8/20 core-file sweep's
lesson was not that the checks were missing -- it was that **conditional,
self-assessed steps get skipped**. A pass that takes two invocations is a pass
that gets half-run on a busy session, and the half that gets skipped is the one
whose failure mode is silent.

This runs both against a SINGLE cache-busted fetch and returns ONE exit code.

    rc 0  both clean
    rc 1  at least one finding -- NOT a pass
    rc 2  fetch failure -- NOT a pass either (an unrun check is a GAP, not a
          green light; the numeric and DIRECTIONAL checks both go blind here
          and the pass says so out loud rather than reporting 0 findings)

USAGE
    python3 monitors/closeout_check.py
    python3 monitors/closeout_check.py --selftest   # verify the checkers themselves
"""
from __future__ import annotations

import datetime as dt
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "FORGE" / "tools" / "market-data"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    br = _load("boot_recompute")
    ac = _load("assertion_check")

    if "--selftest" in sys.argv:
        print("=" * 74)
        print("  CLOSEOUT SELFTEST — verifying the checkers, not the files")
        print("=" * 74)
        # BOTH halves. Until 2026-08-21 this line was `return ac.selftest()`:
        # it delegated entirely to the ASSERTION checker while CLAUDE.md said
        # the pass "verifies the CHECKERS", plural. The numeric half had zero
        # coverage and the doc asserted otherwise -- a check certifying its
        # SCOPE, read as certifying the whole thing.
        rc_num = br.drift_selftest()
        print()
        rc_lint = _load("kb_lint").selftest()
        print()
        rc_ass = ac.selftest()
        print("\n" + "=" * 74)
        # counts read from the modules, never hardcoded -- a literal here goes
        # stale the moment a fixture is added, which is the same class of defect
        # the fixtures exist to catch. The "6" that used to sit here was already
        # wrong by 8 within an hour of kb_lint gaining VX/FLOW coverage.
        nlint = len(_load("kb_lint").FIXTURES_ALL())
        total = len(br.DRIFT_FIXTURES) + nlint + len(ac.FIXTURES)
        print(f"  COMBINED: {len(br.DRIFT_FIXTURES)} numeric + {nlint} workbook-lint + "
              f"{len(ac.FIXTURES)} assertion = {total} fixtures")
        bad = rc_num or rc_ass or rc_lint
        print(f"  {'ALL PASS' if not bad else 'FAILURES PRESENT'}")
        print("=" * 74)
        return 1 if bad else 0

    print("=" * 74)
    print(f"  BOND CLOSEOUT PASS · {dt.datetime.now():%Y-%m-%d %H:%M} local")
    print("  workbook conformance + numeric drift + stale assertions · one fetch · one verdict")
    print("=" * 74)

    # ---- ONE cache-busted fetch, shared by both checkers -------------------
    print("\n" + "-" * 74)
    print("  0/3  WORKBOOK CONFORMANCE  (enums · vocabulary · dates · IDs)")
    print("-" * 74)
    rc_lint = _load("kb_lint").main()

    print(f"\n[fetch] cache entries busted: {br.bust_cache()}")
    series = {}
    try:
        import fetch  # noqa: E402  (path injected above)
        for sid in br.H15_SET + br.CREDIT:
            raw = fetch.fred_fetch(sid, limit=20000)
            obs = sorted((o["date"], float(o["value"])) for o in raw if "error" not in o)
            if not obs:
                raise RuntimeError(f"{sid} returned no observations")
            series[sid] = obs
        newest = max(o[-1][0] for o in series.values())
        print(f"[fetch] {len(series)} series, newest observation {newest}")
    except Exception as e:                                    # noqa: BLE001
        print(f"\n[closeout_check] FETCH FAILURE: {e}", file=sys.stderr)
        print("[closeout_check] rc=2 — NOT a pass. The numeric drift check and the",
              file=sys.stderr)
        print("                 DIRECTIONAL assertion check both went UNRUN; an unrun",
              file=sys.stderr)
        print("                 check is a GAP, never zero findings.", file=sys.stderr)
        return 2

    findings = 0

    # ---- 1. NUMERIC drift on the boot-unread surfaces ---------------------
    print("\n" + "-" * 74)
    print("  1/3  NUMERIC DRIFT  (gate table + boot-unread surfaces)")
    print("-" * 74)
    findings += br.check_unread_surfaces(series)

    # ---- 2. STALE ASSERTIONS ---------------------------------------------
    print("\n" + "-" * 74)
    print("  2/3  STALE ASSERTIONS  (directional · file-state · expired · capability)")
    print("-" * 74)
    a = 0
    a += ac.check_directional(series)
    a += ac.check_file_state()
    a += ac.check_expired()
    a += ac.check_capability()
    if a == 0:
        print("\n   ✅ no stale assertion of a CHECKED SHAPE fired")
    findings += a

    # ---- verdict ----------------------------------------------------------
    print("\n" + "=" * 74)
    if findings == 0:
        print("  ✅ CLOSEOUT PASS CLEAN — 0 findings across all three checks.")
        print()
        print("  Scope of that statement, so it is not over-read:")
        print("   · workbook conformance covers KB/PREDICTIONS enums, vocab, dates, IDs")
        print("   · numeric drift is checked on TRADE.md / monitors/ / NEXUS_BRIEF + FR2004 vintage")
        print("   · assertions are checked for FOUR shapes only")
        print("   · neither check can judge whether ANALYSIS is still true, and")
        print("     assertions phrased in unknown words are outside scope entirely")
        print("  A clean pass means 'nothing of these shapes fired', never 'the files")
        print("  are true'. Run --selftest to verify the checkers themselves.")
    else:
        print(f"  🔴 {findings} FINDING(S) — rc=1, NOT a pass.")
        print("     Fix by PATTERN across the tree, never by the line list above:")
        print("     on 2026-08-20 a line-targeted sweep left the same defect standing")
        print("     on four other surfaces, four separate times in one session.")
        print("     Each finding is a prompt to LOOK — a correctly-labelled QUOTE of a")
        print("     corrected error is a legitimate hit and should be left alone.")
    print("=" * 74)
    # rc_lint folds in: a workbook conformance failure is a closeout finding.
    return 1 if (findings or rc_lint) else 0


if __name__ == "__main__":
    sys.exit(main())
