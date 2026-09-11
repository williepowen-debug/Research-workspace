#!/usr/bin/env python3
"""VIOLET offline regression suites — discover, run, aggregate.

WHY THIS EXISTS (D#14, 2026-09-11)
-----------------------------------
`scripts/tests/` was created on 2026-09-11 holding 18 frozen checks, and SCRATCH
recorded the problem in its own next-session list: **"18 checks nobody runs is
the D#14 class."** A suite that no step invokes is indistinguishable, at the
file, from a suite that does not exist — the same shape as the n=4 CANARY_MAP
failure `closeout_guard.py` was built to end: detection written down, never
converted into an action.

These suites exist because guards shipped broken. `vx_daily_gapcheck.py`,
`backfill.py` and `surface_agreement.py` all shipped with wrong REFERENCES on
2026-09-11, and `thresholds.py`'s stale-column witness shipped with one that had
been silently suppressing real ^SKEW closes (KB-VIO-283). The suites are the
only thing standing between a future edit and a fifth instance.

⚠️ FAIL-CLOSED ON AN EMPTY DISCOVERY
-------------------------------------
Discovery makes wiring automatic for suites added later — the failure this file
exists to prevent, applied to itself. But discovery has the mirror-image defect:
if the directory is renamed, emptied or moved, a naive runner finds nothing,
reports success and CERTIFIES the closeout. That is the DAEDALUS 🔴#5a defect
(`run()` in closeout_guard.py used to `return 0` for a missing script) in a new
place. So: zero discovered suites is a FAILURE, and MIN_SUITES is a floor that
only a deliberate edit may lower.

Run: .venv/bin/python3 AGENTS/VIOLET/scripts/run_tests.py [--quiet]
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TESTS = HERE / "tests"
PY = sys.executable

# Floor, not a target. Retiring a suite is a deliberate act and must edit this
# number in the same commit — otherwise a deleted suite is invisible to
# discovery. It only ever moves DOWN on purpose.
MIN_SUITES = 3


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Run VIOLET's frozen offline suites.")
    ap.add_argument("--quiet", action="store_true", help="only show failures")
    a = ap.parse_args(argv)

    if not TESTS.is_dir():
        print(f"  🔴 CANNOT CERTIFY — {TESTS} does not exist. An absent suite set "
              f"is an UNKNOWN, not a pass.")
        return 2
    suites = sorted(TESTS.glob("test_*.py"))
    if len(suites) < MIN_SUITES:
        print(f"  🔴 CANNOT CERTIFY — discovered {len(suites)} suite(s), floor is "
              f"{MIN_SUITES}. A suite was deleted, renamed or moved; restore it, or "
              f"lower MIN_SUITES deliberately in the same commit.")
        for s in suites:
            print(f"       found: {s.name}")
        return 2

    failed, total_checks = [], 0
    for s in suites:
        try:
            r = subprocess.run([PY, str(s)], capture_output=True, text=True, timeout=180)
        except subprocess.TimeoutExpired:
            failed.append(s.name)
            print(f"  🔴 {s.name} TIMED OUT")
            continue
        out = (r.stdout + r.stderr).rstrip()
        # Suites end with "ALL <n> CHECKS PASSED"; harvest n so the inventory is
        # visible — a suite silently shrinking to one check would otherwise pass.
        n = 0
        for line in out.splitlines():
            if line.startswith("ALL ") and "CHECKS PASSED" in line:
                try:
                    n = int(line.split()[1])
                except (IndexError, ValueError):
                    n = 0
        total_checks += n
        if r.returncode != 0:
            failed.append(s.name)
            print(f"\n  🔴 {s.name}")
            print(out)
        elif not a.quiet:
            print(f"  ✓ {s.name}  ({n} checks)")

    if failed:
        print(f"\n  🔴 {len(failed)} suite(s) FAILED: {', '.join(failed)}")
        return 1
    if not a.quiet:
        print(f"  ✓ {len(suites)} suite(s), {total_checks} checks, all green.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
