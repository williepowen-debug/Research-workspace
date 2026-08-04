#!/usr/bin/env python3
"""canon_check — find documents that PRESCRIBE a command root canon FORBIDS.

WHY THIS EXISTS (2026-08-03, DAEDALUS, Will-approved). The fleet's git canon is stated
in root `CLAUDE.md` § Git Protocol. Nothing checked whether the fleet's *other* prose —
auto-memories, agent CLAUDE.md files, coordination docs — agrees with it. It did not:

  `memory/auto/finding_concurrent_commit_index_race.md`'s "How to apply" block
  prescribed `git reset HEAD && git add AGENTS/<ME>/ && ... && git commit -m "..."` —
  THREE things root canon explicitly forbids — while its sibling memory
  `finding_pathspec_commit_race_safety` said the opposite on all three. WALTER followed
  the first one, improved on it, and still published half of MARCO's `git mv` into HEAD.
  The class then recurred two days later (`418b5f142`, 8/03: five packets duplicated in
  HEAD, five deletions stranded in the shared index).

Neither document was STALE, so no staleness mechanism could see it. That is the gap this
closes: "find contradictions between two docs" is unbuildable in general, but **"find a
doc that prescribes what canon forbids" is a grep.**

★ THE HARD PART IS NOT THE GREP — IT IS NOT FLAGGING CANON ITSELF. Root `CLAUDE.md`
contains the string `git reset HEAD` precisely because it forbids it, and a naive grep
flags the prohibition alongside the violation. So every hit is tested for a SAME-LINE
NEGATION (never / don't / forbidden / avoid / ⚠ ...). A command wrapped in a prohibition
is canon working; the same command with no negation on its line is a prescription. This
is the 2026-07-30 compound-gate lesson applied at build time: read the surrounding text
before flagging, or the screen punishes the documents that state the rule most carefully.
**Same-line, not a window** — see the NEGATION comment below for why a window failed the
one case this check exists for.

Advisory. Flags, never edits. Exit 0 = clean, 1 = flags found, 2 = usage error.

USAGE
    python3 scripts/canon_check.py                    # default doc surfaces
    python3 scripts/canon_check.py PATH [PATH...]     # explicit files/dirs
    python3 scripts/canon_check.py --quiet             # flags only
"""
import argparse
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(
    subprocess.run(["git", "rev-parse", "--show-toplevel"],
                   capture_output=True, text=True).stdout.strip() or ".")

# Doc surfaces that carry procedure. Deliberately NOT the whole tree: prescriptions live
# in canon, memories, agent instructions and coordination docs.
DEFAULT_TARGETS = ["CLAUDE.md", "AGENTS.md", "memory/auto", "docs", "PROME", "AGENTS"]
DOC_EXTS = {".md"}
# Historical by design — a superseded recipe SHOULD survive in these.
EXCLUDE_PARTS = {".git", "_archive", "archive", "archived", "processed", "delivered",
                 "node_modules", ".venv", "__pycache__", "sources", "raw"}

# ⚠️ RESTATEMENT, and the risk is named rather than hidden: root canon states these
# prohibitions in PROSE, so there is no machine-readable source to read instead. This
# table is therefore a copy, and a copy can drift from its original (the same
# script-restates-the-registry class this fleet has hit twice — REGINALD's thresholds.py,
# BRENT's thresholds.py). Consequence: IF ROOT CANON ADDS A PROHIBITION, THIS TABLE DOES
# NOT KNOW. Re-verify it against root `CLAUDE.md` § Git Protocol at each Production
# Review; the `canon` field is the citation a reader checks it against.
PROHIBITIONS = [
    dict(id="reset-head",
         rx=re.compile(r"git\s+reset\s+HEAD"),
         canon="root CLAUDE.md § Before committing 4: 'Never `git reset HEAD` — shared "
               ".git/index makes it a global unstage that races against other agents'",
         why="un-stages EVERY agent's pending work, not just yours"),
    dict(id="add-all",
         rx=re.compile(r"git\s+add\s+(-A\b|--all\b|\.\s*(?:$|&|;|\|))"),
         canon="root CLAUDE.md § Git Protocol: 'Never `git add .` or `git add -A`'",
         why="sweeps in every other agent's uncommitted work"),
    dict(id="add-directory",
         rx=re.compile(r"git\s+add\s+(?:\"|')?AGENTS/[A-Z_<][A-Za-z_<>]*/(?:\"|')?\s*(?:$|&|;|\||\))"),
         canon="root CLAUDE.md § Before committing 2: 'never `git add AGENTS/<YOUR_NAME>/` "
               "as a directory (sweeps in unintended files)'",
         why="a directory pathspec picks up files you did not mean to commit"),
    dict(id="computed-pathspec",
         rx=re.compile(r"\$\(\s*git\s+(diff|status|ls-files)"),
         canon="DAEDALUS ruling 2026-08-03 (RAV-QC-20260801-002), design/"
               "2026-08-03_RAV_QC_002_SHARED_INDEX_RECIPE_REVIEW.md",
         why="reads the SHARED index, so the list is the FLEET's pending work, not yours "
             "— this is the mechanism that published half of MARCO's git mv"),
    dict(id="force-push",
         rx=re.compile(r"git\s+push\s+(?:\S+\s+)*(-f\b|--force(?!-with-lease))"),
         canon="root CLAUDE.md § Git Protocol: 'Never: force push'",
         why="rewrites shared history other agents have already built on"),
]

# A command inside a prohibition is canon WORKING — but the negation must be on the SAME
# LINE. ⚠️ A window was tried first (±2 lines, "canon often states the rule above the
# example") and it FAILED THE CAPABLE CASE: in a bullet list every bullet is a separate
# instruction, so a negation two bullets down governs ITS command, not yours. Measured —
# `finding_concurrent_commit_index_race.md:16` prescribes `git reset HEAD` and line 18
# says "do NOT rewrite pushed history" about something else entirely; the window
# swallowed the one flag this check was built to raise. Same-line scoping catches both
# directions because root canon states each prohibition inline with its command
# ("**Never `git reset HEAD`** — shared .git/index makes it a global unstage").
# If a doc puts its negation on a lead-in line instead, it will flag; the fix is to put
# the negation on the line, which is better writing anyway.
NEGATION = re.compile(
    r"\b(never|never\b.*again|no|not|don'?t|do not|avoid|forbidden|forbid|prohibit|"
    r"no longer|must not|cannot|can'?t|instead of|rather than|wrong|bad|anti-pattern|"
    r"deprecated|violat|banned|disallow|excluded|do NOT|signs? of|flag|detect|catch)\b"
    r"|⚠|❌|🚫", re.I)


# Surface class decides whether a hit is ACTIONABLE. A prescription only misleads someone
# if they READ it as instruction. Mail and dated records are point-in-time — the 6/08
# BROCK/CARL packets that argued the fleet toward pathspec discipline necessarily QUOTE the
# old recipe, and "correcting" them would erase the argument that fixed canon. Same
# discriminator consumer_check.py uses (surface_of: inbox/outbox = MAIL).
HISTORICAL_PARTS = {"inbox", "outbox", "reports", "proposals", "design", "upgrades",
                    "builds", "audits", "runs", "cluster", "postmortems", "grades",
                    "handoff", "output", "outputs", "research", "setups"}


def dormant_agents():
    """DORMANT agent names from the GENERATED FLEET_DIRECTORY — read at runtime, never
    restated here. A dormant agent's docs are inert: nobody boots it, so a recipe inside
    it cannot mislead a live session. Fails OPEN (empty set) rather than crashing, because
    a missing directory should not stop a canon check from running."""
    d = ROOT / "AGENTS" / "DAEDALUS" / "FLEET_DIRECTORY.md"
    if not d.exists():
        return set()
    out, cur = set(), None
    for line in d.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("## "):
            cur = "DORMANT" if "DORMANT" in line else None
            continue
        if cur and line.startswith("| "):
            name = line.strip("|").split("|")[0].strip()
            if re.fullmatch(r"[A-Z][A-Z0-9]+", name):
                out.add(name)
    return out


DORMANT = dormant_agents()


def surface_of(path):
    parts = [q for q in path.parts]
    lower = {q.lower() for q in parts}
    if HISTORICAL_PARTS & lower:
        return "HISTORICAL"
    if "AGENTS" in parts:
        i = parts.index("AGENTS")
        if i + 1 < len(parts) and parts[i + 1] in DORMANT:
            return "HISTORICAL"        # dormant agent: nobody boots it
    return "LIVE"


def targets(paths):
    out = []
    for raw in paths:
        p = (ROOT / raw) if not pathlib.Path(raw).is_absolute() else pathlib.Path(raw)
        if p.is_file():
            out.append(p)
        elif p.is_dir():
            out += [q for q in p.rglob("*")
                    if q.is_file() and q.suffix.lower() in DOC_EXTS
                    and not (EXCLUDE_PARTS & {x.lower() for x in q.parts})]
    return sorted(set(out))


def check(path):
    """Hits are per (line, prohibition), minus two suppressions.

    ★ DOC-LEVEL STANCE is the second one and it matters more than the first. A document
    that FORBIDS a command somewhere in it has taken a position, so its other mentions are
    explanation, not instruction — `finding_pathspec_commit_race_safety.md` says "Never use
    `git reset HEAD` … Reset is the race trigger" and then explains the mechanism twice in
    prose, which same-line scoping alone flagged three times. Meanwhile
    `finding_concurrent_commit_index_race.md` never forbids it anywhere — it PRESCRIBES it —
    so it still flags. That asymmetry is exactly the signal wanted: not "is this command
    mentioned?" but "has this document taken a position against it?"
    """
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return []
    # Per prohibition: does ANY line in this doc pair the command WITH a negation?
    stance = {pro["id"] for pro in PROHIBITIONS
              if any(pro["rx"].search(l) and NEGATION.search(l) for l in lines)}
    rel = str(path.relative_to(ROOT)) if ROOT in path.parents or path.parent == ROOT else str(path)
    hits = []
    for i, line in enumerate(lines):
        for pro in PROHIBITIONS:
            if not pro["rx"].search(line):
                continue
            if NEGATION.search(line):
                continue          # wrapped in a prohibition -> canon working, not a violation
            if pro["id"] in stance:
                continue          # this doc forbids the command elsewhere -> discussion
            hits.append((rel, i + 1, pro, line.strip()[:150]))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    files = targets(a.paths or DEFAULT_TARGETS)
    if not files:
        print("canon_check: FAIL — 0 documents matched; the target list is wrong "
              f"(searched: {', '.join(a.paths or DEFAULT_TARGETS)})", file=sys.stderr)
        return 2

    live, hist = [], []
    for f in files:
        for hit in check(f):
            (hist if surface_of(pathlib.Path(hit[0])) == "HISTORICAL" else live).append(hit)
    flags = live

    if not flags:
        if not a.quiet:
            # Say what was searched — a bare tick is indistinguishable from not looking.
            print(f"CANON-CHECK ✓ {len(files)} doc(s) searched for "
                  f"{len(PROHIBITIONS)} prohibited command patterns; none PRESCRIBED on a "
                  "LIVE instruction surface. (Same-line prohibitions skipped by design; "
                  f"{len(hist)} hit(s) on historical/mail surfaces not counted — those "
                  "quote old recipes to argue against them.)")
        return 0

    print(f"CANON-CHECK ⚠️  {len(flags)} prescription(s) of a forbidden command on a LIVE "
          f"instruction surface ({len(files)} doc(s) searched; {len(hist)} further hit(s) on "
          f"historical/mail surfaces NOT listed — point-in-time, and the 6/08 packets that "
          f"argued canon toward pathspec discipline necessarily quote the old recipe)\n")
    for rel, n, pro, text in flags:
        print(f"  [{pro['id']}] {rel}:{n}")
        print(f"      {text}")
        print(f"      why: {pro['why']}")
        print(f"      canon: {pro['canon']}\n")
    print("Advisory. A hit means the doc TELLS someone to run a command canon forbids — "
          "fix the doc, not the agent who followed it. If the command is being quoted in "
          "order to forbid it, add the negation to the line so this stops flagging it.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
