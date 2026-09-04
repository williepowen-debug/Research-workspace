#!/usr/bin/env python3
"""VIOLET closeout guard — refuses a clean exit while a staleness contract is RED.

WHY THIS EXISTS (n=4 on one file, 2026-08-04)
---------------------------------------------
On the morning of 2026-08-04 `boot.py` printed:

    🔴 CANARY_MAP STALE 'CURRENT' CELLS — 2

**The session read it and did not act.** By that evening five `CURRENT` cells were
5–11 days stale — MOVE carried **no current value at all** while the instrument
made an episode high, and COT carried `+3,098/p92.9` after the sign had flipped to
`−12,289/p76.9`.

🔑 **And every one of those cells already carried a parenthetical confessing a
PRIOR staleness incident** (*"this cell read X until 7/28 — 11 days stale"*). So
this is the fourth occurrence on one file, and it forces the diagnosis to change:

    DETECTION WAS NEVER THE GAP. ACTING ON DETECTION IS.

The >4-day contract works and fires on time. **A boot warning that is read and not
actioned is indistinguishable, at the file, from no warning at all.** The honest
fix is not a better alert — it is a step that will not complete while a contract is
red. Same family as the three "labelled gap ≠ filled gap" instances of the same
day (MOVE five sessions · FRED retracted within the hour · SKEW missed at the
settle): in each, the defect was correctly DETECTED and correctly WRITTEN DOWN,
and nothing converted that into an action.

⚠️ **BOOT WARNS; CLOSEOUT BLOCKS. That asymmetry is deliberate.** At boot a red
contract is information you need in order to work. At closeout it is work you did
not do. Warning at both ends produced exactly this failure — the same message
twice a day for four incidents, actioned on none of them.

WHAT IT AGGREGATES
------------------
  · `canary_staleness.py`  — CANARY_MAP `CURRENT` cells past their cadence
  · `grading_note_check.py`— catalyst notes citing retracted KB rows
  · `validate_workbook.py` — KB schema conformance (errors only, not the
                             ACTIVE-past-Stale_By WARN, which is by design)
  · `surface_agreement.py`  — the SAME figure must read the same on STATUS,
                             NEXUS_BRIEF, SCRATCH and LAST_COMPLETION. Added
                             2026-09-04 after the convergence score was live as
                             29/50 and 26/55 simultaneously across four surfaces
                             while every other contract passed. A summary block
                             is rewritten from memory while the body is rewritten
                             from data, so the summary is where a corrected
                             number goes to die.
  · `twin_check.py`         — CALENDAR.md vs CATALYSTS.tsv. Added 2026-09-04
                             (KB-VIO-235). It reports divergence and REFUSES to
                             name a winner: the 9/4 incident was a twin "fix"
                             that made the accurate surface match the wrong one.
                             A red here is an OPERATOR decision, not an edit.
  · `writeback_order_check.py` — the three handoff surfaces (SCRATCH,
                             LAST_COMPLETION, NEXUS_BRIEF) must not lag STATUS.
                             Added 2026-09-04 after a session crashed between the
                             STATUS commit and the write-back tail and NOTHING
                             detected it at the next boot. Vintage only — it
                             cannot see a fresh stamp over a stale body.
  · `thesis_bump_check.py` — ADVISORY ONLY; never blocks (see below)

⚠️ **The thesis check is deliberately non-blocking.** It is a judgement prompt, not
a contract — blocking on a counter that cannot see a semantic contradiction would
train the operator to bypass the guard, which destroys the value of every other
check in it. **A guard you learn to skip is worse than no guard.**

Exit codes: 0 = clear to close out; 1 = at least one contract RED.
"""
from __future__ import annotations
import argparse, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = sys.executable

BLOCKING = [
    ("CANARY_MAP staleness contract", "canary_staleness.py", ["--strict"]),
    ("Grading-note citations", "grading_note_check.py", ["--strict"]),
    ("KB schema conformance", "validate_workbook.py", []),
    ("Write-back ordering (handoff surfaces vs STATUS)", "writeback_order_check.py", ["--quiet"]),
    ("CALENDAR/CATALYSTS twin consistency", "twin_check.py", ["--quiet"]),
    ("Convergence matrix arithmetic", "convergence_score.py", []),
    ("Cross-surface figure agreement", "surface_agreement.py", ["--quiet"]),
]
ADVISORY = [
    ("Thesis currency", "thesis_bump_check.py", []),
]


def run(script: str, args: list[str]) -> tuple[int, str]:
    p = HERE / script
    if not p.exists():
        # ⚠️ WAS `return 0` — a MISSING CHECK CERTIFIED THE CLOSEOUT (DAEDALUS 🔴#5a).
        # Deleting or renaming a guard script was the cheapest way to make this
        # guard green, and the "(skipped)" line read like an ordinary note. A
        # check that is absent is an UNKNOWN, and an unknown is not a pass.
        return 2, (f"  🔴 CANNOT CERTIFY — {script} IS MISSING from {HERE}.\n"
                   f"     An absent check is an UNKNOWN, not a pass. Restore it or "
                   f"remove its row from BLOCKING deliberately.")
    try:
        r = subprocess.run([PY, str(p), *args], capture_output=True, text=True, timeout=120)
        return r.returncode, (r.stdout + r.stderr).rstrip()
    except subprocess.TimeoutExpired:
        return 1, f"  🔴 {script} timed out"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true", help="only show RED contracts")
    a = ap.parse_args()

    print("═" * 62)
    print("  VIOLET CLOSEOUT GUARD")
    print("═" * 62)

    red = []
    for label, script, args in BLOCKING:
        rc, out = run(script, args)
        if rc != 0:
            red.append(label)
            print(f"\n  🔴 {label}")
            print(out)
        elif not a.quiet:
            print(f"  ✓ {label}")

    for label, script, args in ADVISORY:
        rc, out = run(script, args)
        if not a.quiet or rc != 0:
            print(f"\n  ℹ️  {label} (advisory — never blocks)")
            print(out)

    print("\n" + "─" * 62)
    if red:
        print(f"  🔴 CLOSEOUT BLOCKED — {len(red)} contract(s) RED: {', '.join(red)}")
        print("  Fix them, or write on the surface WHY the red state is correct and intended.")
        print("  ⚠️  Do not close out on a red contract just because boot also warned about it —")
        print("      that is the exact n=4 failure this guard was built to end.")
        return 1
    print("  ✓ All blocking contracts green — clear to close out.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
