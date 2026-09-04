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
    # ⚠️ THIRD FAIL-OPEN HOLE, CLOSED 2026-09-04 (external review, second pass).
    # v1 returned early whenever the brief was dirty. This guard is wired into
    # `closeout_guard.py`, and AT CLOSEOUT THE BRIEF IS ALWAYS DIRTY — you have
    # just written it. So the check ran green at boot and was INERT at exactly
    # the moment it was supposed to block. Correct and wired are independent
    # properties [[finding_guard_correctness_and_wiring_are_independent]], and I
    # had tested only the first.
    # Dirty now means: check everything that does not require the commit to
    # exist, and say plainly which single assertion is deferred.
    dirty = bool(_git("status", "--porcelain", "--", rel))
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
        if dirty:
            # ⚠️ v1 passed unconditionally while dirty. A BRIEF-ONLY commit could
            # then claim `same-commit` and clear closeout on a false marker, caught
            # only on a later run. If the brief is being written, STATUS must be
            # too — otherwise they are provably NOT landing together.
            if not _git("status", "--porcelain", "--", _rel("STATUS.md")):
                out.append("  🔴 NEXUS_BRIEF claims `same-commit` and is dirty, but STATUS.md "
                           "is CLEAN — they cannot land in the same commit.\n"
                           "     Either this is a brief-only commit (the marker is false) or "
                           "STATUS has not been written yet.")
        elif latest and brief_commit and latest != brief_commit:
            out.append(f"  🔴 NEXUS_BRIEF claims `same-commit` but STATUS's latest commit is "
                       f"`{latest}` while the brief was committed in `{brief_commit}`.\n"
                       f"     They did NOT land together — the marker is false.")
    else:
        cited = m.group(1)
        # ⚠️ HOLE CLOSED 2026-09-04 (external review, second pass): v1 accepted any
        # sha matching the BRIEF's own commit, even a commit that never touched
        # STATUS.md — so a brief could cite a commit unrelated to STATUS and pass.
        # The citation must name a commit that ACTUALLY TOUCHED STATUS.
        touching = _git("log", "-30", "--format=%h", "--", _rel("STATUS.md")).split()
        is_status_commit = any(h.startswith(cited) or cited.startswith(h) for h in touching)
        is_latest = bool(latest) and (latest.startswith(cited) or cited.startswith(latest))
        if not is_status_commit:
            out.append(f"  🔴 NEXUS_BRIEF cites `{cited}`, which is NOT among the last 30 commits "
                       f"that touched STATUS.md.\n"
                       f"     A hash that names no STATUS revision points NEXUS at nothing.")
        elif not is_latest and not dirty:
            out.append(f"  🔴 NEXUS_BRIEF cites STATUS commit `{cited}`, but the latest STATUS "
                       f"commit is `{latest}` (brief committed in `{brief_commit}`).\n"
                       f"     A stale hash sends NEXUS to the wrong STATUS while every vintage "
                       f"check passes green.")

    # ② the As-of stamp cannot be later than the commit that published it
    ms = re.search(r"\*\*As of:\*\*\s*(\d{4}-\d{2}-\d{2})\s*\*{0,2}~?(\d{1,2}):(\d{2}|\dx|xx)", text)
    ct = _git("log", "-1", "--format=%ct", "--", rel)
    # ⚠️ HOLE CLOSED 2026-09-04 (external review, second pass): v1 SILENTLY SKIPPED
    # validation when the stamp was missing or malformed — fail-OPEN, so deleting
    # the stamp was the cheapest way to pass this check. A stamp that cannot be
    # parsed is not a stamp. [[finding_silent_blank_evades_review]]
    if not ms:
        out.append("  🔴 NEXUS_BRIEF has no parseable `**As of:** YYYY-MM-DD HH:MM` stamp — "
                   "the freshness claim NEXUS reads cannot be checked at all.\n"
                   "     Absent is not the same as fine; this check fails closed.")
    if ms:
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
            # Reference is the COMMIT when one exists, otherwise NOW — a stamp in
            # the future is wrong either way, and the dirty case is the one that
            # actually matters at closeout.
            ref = datetime.fromtimestamp(int(ct)) if (ct and not dirty) else datetime.now()
            what = "committed at" if (ct and not dirty) else "checked at"
            drift = (stamped - ref).total_seconds() / 60.0
            if drift > 5:
                out.append(f"  🔴 NEXUS_BRIEF is stamped {stamped:%H:%M} but was {what} "
                           f"{ref:%H:%M} — a stamp {drift:.0f} min in its own FUTURE.\n"
                           f"     Write timestamps from the clock, not from the narrative "
                           f"[[finding_write_timestamps_from_the_clock_not_the_narrative]].")
    return out


# ⚠️ #4 (external review): the stamp check covered NEXUS_BRIEF only, so a future
# timestamp reappeared on STATUS and CANARY_MAP within one commit of the last fix.
# A check scoped to one surface teaches the defect to move to the others.
STAMPED = {
    "STATUS.md": re.compile(r"Last write-back:\s*(\d{4}-\d{2}-\d{2})\s*~?(\d{1,2}):(\d{2}|\dx|xx)"),
    "CANARY_MAP.md": re.compile(r"Last refreshed:\s*\*{0,2}(\d{4}-\d{2}-\d{2})\*{0,2}\s*~?(\d{1,2}):(\d{2}|\dx|xx)"),
}


def _floor_minute(mins: str) -> int:
    if mins.isdigit():
        return int(mins)
    if len(mins) == 2 and mins[0].isdigit():
        return int(mins[0]) * 10
    return 0


def stamp_futures() -> list[str]:
    """No surface may carry an as-of stamp later than the clock that reads it."""
    out = []
    now = datetime.now()
    for name, rx in STAMPED.items():
        f = AGENT_DIR / name
        if not f.exists():
            continue
        mo = rx.search(f.read_text(encoding="utf-8"))
        if not mo:
            continue
        try:
            stamped = datetime.strptime(
                f"{mo.group(1)} {int(mo.group(2)):02d}:{_floor_minute(mo.group(3)):02d}",
                "%Y-%m-%d %H:%M")
        except ValueError:
            continue
        drift = (stamped - now).total_seconds() / 60.0
        if drift > 5:
            out.append(f"  🔴 {name} is stamped {stamped:%H:%M} but it is {now:%H:%M} — "
                       f"a stamp {drift:.0f} min in the FUTURE.\n"
                       f"     Run `date` before every stamp; do not write the hour you "
                       f"expect to finish in.")
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

    prov = brief_provenance() + stamp_futures()
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
