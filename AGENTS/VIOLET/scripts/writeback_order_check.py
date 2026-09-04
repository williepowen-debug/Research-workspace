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
import argparse, re, subprocess, sys, time
from datetime import datetime
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


def brief_provenance() -> list[str]:
    """Check the two provenance stamps the ORDERING rule cannot see.

    Added 2026-09-04 PM after an external review (Codex, routed by Will) found
    both wrong on a brief this very check had just passed green:

      · it cited `ef3e0be9c` as its STATUS commit while the latest STATUS commit
        was `ec5d05b69` — the hash pointed two commits and four hours back
      · it was stamped "~14:3x ET" and committed at 13:56 ET — a stamp from the
        FUTURE relative to its own commit

    The ordering rule compares vintages and is blind to both, exactly as this
    module's docstring warned. That warning was correct and it was not enough:
    a limitation you have written down is still a limitation. These two stamps
    are the part of "content" that IS mechanically checkable, so they are checked.
    """
    out: list[str] = []
    rel = _rel("NEXUS_BRIEF.md")
    if not (AGENT_DIR / "NEXUS_BRIEF.md").exists():
        return out
    if _git("status", "--porcelain", "--", rel):
        return out                       # being written now; nothing committed to judge
    text = (AGENT_DIR / "NEXUS_BRIEF.md").read_text(encoding="utf-8")

    # ① cited STATUS hash must be the current STATUS head, or the brief's own commit
    # `same-commit` is a legitimate, VERIFIABLE answer to the chicken-and-egg:
    # when the brief and STATUS land in one commit the sha cannot be known while
    # writing. The marker is not a free pass — it asserts something checkable
    # after the fact (that they really did land together) and is RED if they did not.
    m = re.search(r"STATUS commit:\*{0,2}\s*`(same-commit|[0-9a-f]{7,40})`", text)
    latest = _git("log", "-1", "--format=%h", "--", _rel("STATUS.md"))
    brief_commit = _git("log", "-1", "--format=%h", "--", rel)
    if not m:
        out.append("  🔴 NEXUS_BRIEF has no `STATUS commit:` hash — NEXUS cannot tell which "
                   "STATUS this brief stands on.")
    elif m.group(1) == "same-commit":
        if latest and brief_commit and latest != brief_commit:
            out.append(f"  🔴 NEXUS_BRIEF claims `same-commit` but STATUS's latest commit is "
                       f"`{latest}` while the brief was committed in `{brief_commit}`.\n"
                       f"     They did NOT land together — the marker is false.")
    else:
        cited = m.group(1)
        if latest and not (latest.startswith(cited) or cited.startswith(latest)
                           or brief_commit.startswith(cited) or cited.startswith(brief_commit)):
            out.append(f"  🔴 NEXUS_BRIEF cites STATUS commit `{cited}`, but the latest STATUS "
                       f"commit is `{latest}` (brief committed in `{brief_commit}`).\n"
                       f"     A stale hash sends NEXUS to the wrong STATUS while every vintage "
                       f"check passes green.")

    # ② the As-of stamp cannot be later than the commit that published it
    ms = re.search(r"\*\*As of:\*\*\s*(\d{4}-\d{2}-\d{2})\s*\*{0,2}~?(\d{1,2}):(\d{2}|\dx|xx)", text)
    ct = _git("log", "-1", "--format=%ct", "--", rel)
    if ms and ct:
        # "~14:3x" means 14:30-14:39, so the FLOOR is 30, not 0. The first version
        # fell back to 0 on any non-digit, which made this check untrippable on
        # exactly the fuzzy stamps VIOLET actually writes — a guard that cannot
        # fire [[finding_banded_threshold_with_no_metric_surface_is_untrippable]].
        # Floor is the charitable reading: it under-reports drift, never invents it.
        mins = ms.group(3)
        if mins.isdigit():
            mn = int(mins)
        elif len(mins) == 2 and mins[0].isdigit():           # "3x" -> 30
            mn = int(mins[0]) * 10
        else:                                                 # "xx" -> unknown, floor 0
            mn = 0
        try:
            stamped = datetime.strptime(f"{ms.group(1)} {int(ms.group(2)):02d}:{mn:02d}",
                                        "%Y-%m-%d %H:%M")
        except ValueError:
            stamped = None
        if stamped is not None:
            committed = datetime.fromtimestamp(int(ct))
            drift = (stamped - committed).total_seconds() / 60.0
            if drift > 5:
                out.append(f"  🔴 NEXUS_BRIEF is stamped {stamped:%H:%M} but was committed at "
                           f"{committed:%H:%M} — a stamp {drift:.0f} min in its own FUTURE.\n"
                           f"     Write timestamps from the clock, not from the narrative "
                           f"[[finding_write_timestamps_from_the_clock_not_the_narrative]].")
    return out


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

    prov = brief_provenance()
    if prov:
        print("\n  🔴 BRIEF PROVENANCE:")
        for line in prov:
            print(line)

    if lagging or prov:
        if not lagging:
            print(f"\n  🔴 {len(prov)} brief-provenance problem(s) — the ordering half is fine, "
                  f"the stamps are not.")
            return 1
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
