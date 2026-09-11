#!/usr/bin/env python3
"""Regression test for `surface_agreement.py`'s memo-set bound.

WHY THIS EXISTS
---------------
`resolve()` globbed `PROME/inbox/` and `processed/` and read EVERY
`*_from-VIOLET_*` memo together. That is right within one closeout — a same-day
addendum contradicting the memo it amends is a genuine disagreement — and wrong
across closeouts, where a figure that legitimately MOVED between deliveries reads
as a permanent cross-surface disagreement. Seven 2026-09-06 memos carrying 28/50
and "2 of 4", both true at their vintage, held this BLOCKING check red against a
STATUS correctly at 33/50 and 0, and the red grew by one surface per memo sent.

🔑 The printed remedy — "fix the non-canonical surfaces by RE-DERIVING" — could
not be followed honestly, because a delivered memo is an immutable record and
re-deriving one means editing history. **A guard whose remedy is impossible
trains its reader to wave the red through**, which is the n=4 CANARY_MAP
behaviour this guard exists to end.

⚠️ THE RISK THIS TEST EXISTS TO BOUND
--------------------------------------
The fix makes a noisy blocking check quiet, and "quieter" is exactly how a guard
gets loosened into uselessness — trading loud-and-safe for silent-and-certifying.
So the property under test is NOT "it stopped complaining." It is that the check
still FAILS on a real same-session disagreement (A) and still fails CLOSED when
the memo surface is absent (C), while dropping only the cross-session comparison
that was never a defect (B).

FROZEN AND OFFLINE: every surface, memo and figure here is a fixture in a temp
dir. Nothing reads the live STATUS/SCRATCH/NEXUS_BRIEF or the real PROME/inbox,
so this cannot rot when those files change and cannot touch another agent's dir.

Run: .venv/bin/python3 AGENTS/VIOLET/scripts/tests/test_surface_agreement_bound.py
"""
from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import surface_agreement as sa  # noqa: E402

DAY, PRIOR = "2026-09-11", "2026-09-06"
AGREE = "Convergence score is 33/50 this cycle. FT-10 sustain count 0 of 4.\n"
ADDENDUM_DRIFT = "Convergence score is 30/50 in this addendum. FT-10 sustain count 0 of 4.\n"
PRIOR_VINTAGE = "Convergence score is 28/50. FT-10 sustain count 2 of 4.\n"


class R:
    def __init__(self) -> None:
        self.ok, self.n = True, 0

    def check(self, label: str, got, want) -> None:
        self.n += 1
        good = got == want
        print(("  ✅ " if good else "  ❌ ") + f"{label}  [got {got}, want {want}]")
        self.ok = self.ok and good


def main() -> int:
    r = R()
    tmp = Path(tempfile.mkdtemp(prefix="violet_sa_"))
    (tmp / "memos").mkdir()
    # Redirect BOTH roots: agent surfaces and the memo dirs are fixtures.
    sa.AGENT_DIR, sa.REPO, sa.MEMO_DIRS = tmp, tmp, ("memos",)
    for name in ("STATUS.md", "NEXUS_BRIEF.md", "SCRATCH.md"):
        (tmp / name).write_text(AGREE, encoding="utf-8")

    def memo(name: str, body: str) -> None:
        (tmp / "memos" / name).write_text(body, encoding="utf-8")

    def clear() -> None:
        for f in (tmp / "memos").iterdir():
            f.unlink()

    print("\n--- A. same-session addendum contradicts its memo -> must FAIL ---")
    clear()
    memo(f"{DAY}_from-VIOLET_memo.md", AGREE)
    memo(f"{DAY}_from-VIOLET_addendum.md", ADDENDUM_DRIFT)
    r.check("still catches same-day drift", sa.main(["--quiet", "--date", DAY]), 1)

    print("\n--- B. prior-session memo carrying a superseded figure -> must PASS ---")
    clear()
    memo(f"{PRIOR}_from-VIOLET_old.md", PRIOR_VINTAGE)
    memo(f"{DAY}_from-VIOLET_memo.md", AGREE)
    r.check("ignores prior-session vintage", sa.main(["--quiet", "--date", DAY]), 0)

    print("\n--- C. no memo for the session date -> must FAIL CLOSED ---")
    clear()
    memo(f"{PRIOR}_from-VIOLET_old.md", PRIOR_VINTAGE)
    r.check("absence is not agreement", sa.main(["--quiet", "--date", DAY]), 1)

    print("\n--- D. contrast: the UNBOUNDED resolve is what produced the false red ---")
    clear()
    memo(f"{PRIOR}_from-VIOLET_old.md", PRIOR_VINTAGE)
    memo(f"{DAY}_from-VIOLET_memo.md", AGREE)
    spec = "PROME/inbox/*_from-VIOLET_*.md"
    r.check("unbounded resolve pulls BOTH sessions", len(sa.resolve(spec, None)), 2)
    r.check("bounded resolve pulls ONE session", len(sa.resolve(spec, DAY)), 1)

    shutil.rmtree(tmp, ignore_errors=True)
    print(f"\n{'ALL ' + str(r.n) + ' CHECKS PASSED' if r.ok else 'FAILED'}")
    return 0 if r.ok else 1


if __name__ == "__main__":
    sys.exit(main())
