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
        return ac.selftest()

    print("=" * 74)
    print(f"  BOND CLOSEOUT PASS · {dt.datetime.now():%Y-%m-%d %H:%M} local")
    print("  numeric drift + stale assertions · one fetch · one verdict")
    print("=" * 74)

    # ---- ONE cache-busted fetch, shared by both checkers -------------------
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
    print("  1/2  NUMERIC DRIFT  (gate table + boot-unread surfaces)")
    print("-" * 74)
    findings += br.check_unread_surfaces(series)

    # ---- 2. STALE ASSERTIONS ---------------------------------------------
    print("\n" + "-" * 74)
    print("  2/2  STALE ASSERTIONS  (directional · file-state · expired · capability)")
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
        print("  ✅ CLOSEOUT PASS CLEAN — 0 findings across both checks.")
        print()
        print("  Scope of that statement, so it is not over-read:")
        print("   · numeric drift is checked on TRADE.md / monitors/ / NEXUS_BRIEF")
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
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
