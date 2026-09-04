#!/usr/bin/env python3
"""VIOLET write-back ordering contract — the three handoff surfaces may not lag STATUS.

WHY THIS EXISTS (2026-09-04, a session crash)
---------------------------------------------
The 2026-09-04 ~10:0x session graded the post-NFP vol reaction, committed
`STATUS.md` (10:06) and `SIGNAL_INTAKE.md` (10:08) — and then died before the
write-back tail. It left:

    STATUS.md          committed 10:06   <- current
    SCRATCH.md         committed 08:47   <- describes a SUPERSEDED state
    LAST_COMPLETION.md committed 08:47   <- PROME reads this
    NEXUS_BRIEF.md     committed 08:47   <- NEXUS reads this IN PLACE OF STATUS

Nothing detected it. Not `boot.py`, not `closeout_guard.py`, not
`ledger_staleness.py` — all four ran clean at the next boot.

🔑 **The failure is not that the rule was missing. The rule exists and is already
written in CHECKABLE form.** VIOLET's `CLAUDE.md` write-back step 12 states NEXUS
Amendment 10 as: *"the brief's commit timestamp >= the session's last STATUS
commit timestamp."* That is an arithmetic comparison of two integers. **It had
been sitting there as a sentence for 31 days and nothing computed it.**

That is this desk's own named failure class — a ritual is not a mechanism — and
it is the same diagnosis as KB-VIO-165 (enums "validated" by remembering) and
KB-VIO-226/190 (a registered mechanical line inherited as a fresh judgement call).
A rule a human must remember at the end of a session is a rule that fails exactly
when the session ends badly.

⚠️ **WHAT THIS CANNOT SEE — stated so nobody reads a PASS as more than it is.**
It compares VINTAGE, never CONTENT. A brief re-stamped with a fresh `As of:` line
and a stale body passes green: that is `[[finding_header_edit_is_the_edit_most_
mistaken_for_maintenance]]`, and this check is blind to it by construction. It
catches the surface LEFT BEHIND, not the surface REFRESHED BADLY.

HOW A DIRTY FILE IS TREATED, AND WHY
------------------------------------
`closeout_guard.py` runs BEFORE the session's commit, so at that moment the files
being written are dirty and have no new commit timestamp yet. Comparing raw commit
timestamps there would flag every honest closeout — a guard that cries wolf on the
correct path is one you learn to bypass, which is the explicit design warning
already written into `closeout_guard.py`'s docstring about the thesis check.

So the effective vintage of a surface is:

    dirty in the working tree  ->  now   (it is being written this session)
    clean                      ->  its last commit timestamp

This makes the check correct at BOTH ends: at closeout it passes once you have
actually touched the lagging surface, and at boot it fires on a crash that left
one behind.

Exit codes: 0 = ordering holds; 1 = at least one surface lags STATUS.
"""
from __future__ import annotations
import argparse, subprocess, sys, time
from pathlib import Path

AGENT_DIR = Path(__file__).resolve().parent.parent
REPO = AGENT_DIR.parent.parent
REF = "STATUS.md"
# surface -> why it lagging matters (the CONSUMER, which is the whole point)
TRACKED = {
    "NEXUS_BRIEF.md": "NEXUS reads this IN PLACE OF raw STATUS (Amendment 10 ordering rule)",
    "SCRATCH.md": "my own next boot reads this as the canonical 'where are we'",
    "LAST_COMPLETION.md": "PROME reads this to update its STATUS/SCRATCH/ACTIVE_DECISIONS",
}


def _git(*args: str) -> str:
    r = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True)
    return r.stdout.strip()


def _rel(name: str) -> str:
    return str((AGENT_DIR / name).relative_to(REPO))


def effective_ts(name: str) -> tuple[int, str]:
    """(unix ts, basis) — dirty files count as NOW; see module docstring."""
    rel = _rel(name)
    if not (AGENT_DIR / name).exists():
        return 0, "MISSING"
    if _git("status", "--porcelain", "--", rel):
        return int(time.time()), "dirty (being written now)"
    out = _git("log", "-1", "--format=%ct|%h|%ad", "--date=format:%m-%d %H:%M", "--", rel)
    if not out:
        return 0, "never committed"
    ct, sha, when = out.split("|", 2)
    return int(ct), f"committed {when} ({sha})"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    ref_ts, ref_basis = effective_ts(REF)
    if ref_ts == 0:
        print(f"  ⚠️  {REF} {ref_basis} — cannot evaluate ordering, failing closed.")
        return 1

    lagging = []
    lines = [f"  reference  {REF:<20} {ref_basis}"]
    for name, consumer in TRACKED.items():
        ts, basis = effective_ts(name)
        lag_min = (ref_ts - ts) / 60.0
        if ts < ref_ts:
            lagging.append((name, lag_min, basis, consumer))
            lines.append(f"  🔴 LAGS    {name:<20} {basis}  — {lag_min:,.0f} min behind {REF}")
        else:
            lines.append(f"  ✓          {name:<20} {basis}")

    if lagging or not a.quiet:
        print("\n".join(lines))

    if lagging:
        print(f"\n  🔴 WRITE-BACK ORDERING BREACH — {len(lagging)} surface(s) lag {REF}.")
        print("     Each of these is read by someone who is NOT me:")
        for name, lag_min, _, consumer in lagging:
            print(f"       · {name} — {consumer}")
        print("     Fix: finish the write-back tail (CLAUDE.md steps 11, 11a, 12) before committing.")
        print("     ⚠️  A PASS here means FRESH, never CORRECT — this check cannot read content.")
        return 1
    if not a.quiet:
        print(f"\n  ✓ Write-back ordering holds — no surface lags {REF}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
