#!/usr/bin/env python3
"""argus_scope.py — the GIT WATERMARK that defines what ARGUS audits (WQ-226, Will-ruled 2026-09-11).

PROME cannot choose what ARGUS reads: the scope is every path touched by a PROME-authored commit since the
PREVIOUS CLOSEOUT COMMIT. A closeout commit is one whose subject starts `PROME: [<TIER> ]closeout` (case-
insensitive; "STANDARD closeout", "LIGHT closeout", "closeout 9/10 evening" all match; a subject that merely
MENTIONS closeout later in the line — "WQ-227 registered (exempt-desk closeout …)" — does not). PROME-authored = subject starts with `PROME` (the fleet convention: `<DESK>: …` /
`<DESK> -> <RECIPIENT>: …`) OR every path it touched lies inside PROME's ownership perimeter (the durable
fallback: PROME-owned work committed under a `FORGE:`/`HEARTBEAT:` subject is still PROME's — audit 2026-09-11 F1).

🔴 PENDING WORK IS IN SCOPE (audit 2026-09-11 F1, P1). CLOSEOUT 1f runs ARGUS **before** the closeout commit,
so the session's own HANDOFF/SCRATCH/STATUS/BRIEF writes are UNCOMMITTED at audit time. A scope built only from
`watermark..HEAD` cannot see the very writes the verdict is meant to approve — the witness could not see what it
certified. Pending PROME-OWNED paths (tracked modifications + new untracked files) are therefore included and
LABELLED, so ARGUS knows which diff to run. Scoped to PROME's perimeter, never the whole shared dirty tree:
another desk's uncommitted work is not PROME's to audit.

Usage (from the repo root):
    python3 PROME/tools/argus_scope.py            # human list + the skip verdict
    python3 PROME/tools/argus_scope.py --json     # machine form for the spawn prompt
Exit: 0 = scope has >= MIN_PATHS paths (spawn ARGUS) · 3 = under the floor (skip, say so in the closeout report) ·
2 = no closeout commit found in the last MAX_LOOKBACK commits (do not guess — audit everything since HEAD~50 and say so).
"""
import argparse
import json
import re
import subprocess
import sys

MIN_PATHS = 3          # WQ-226: skipped when PROME's commit set is < 3 paths
MAX_LOOKBACK = 600     # commits to search for the previous closeout
CLOSEOUT_RE = re.compile(r"^PROME:\s+(?:\w+\s+)?closeout\b", re.I)
PROME_RE = re.compile(r"^PROME\b")

# TWO perimeters, deliberately different — conflating them was a self-caught false positive on the first
# attempt at this fix (it attributed `CARL -> PROME:` and `VIOLET -> PROME:` inbound packets to PROME):
#
#   AUTHORSHIP — paths only PROME writes. Used for the durable attribution fallback (the `FORGE:`-subject case).
#     EXCLUDES PROME/inbox/: inbound mail is other desks' output sitting in PROME's tree, never PROME's work
#     (`finding_path_scoped_git_log_measures_inbound_traffic` — a path-scoped log measures INBOUND traffic).
#     EXCLUDES memory/auto/: fleet-shared authorship, any desk commits there under carve-out (3).
#   PENDING — paths whose UNCOMMITTED state ARGUS may be shown at a pre-commit run. Authorship plus the fleet
#     surfaces PROME itself must self-commit at closeout. Never the whole shared dirty tree.
AUTHORSHIP_PREFIXES = ("PROME/", "FORGE/", "HEARTBEAT.md", ".claude/agents/argus.md")
AUTHORSHIP_EXCLUDE = ("PROME/inbox/",)
PENDING_EXTRA = ("memory/auto/",)
# Carve-out (1): a packet PROME authored into another desk's inbox is PROME's to commit, so it is PROME's to audit.
PROME_PACKET_RE = re.compile(r"^AGENTS/[A-Z0-9_]+/inbox/.*from-PROME", re.I)


def is_prome_authored(path):
    """Strict: only paths PROME itself writes. Drives the attribution fallback."""
    if path.startswith(AUTHORSHIP_EXCLUDE):
        return False
    return path.startswith(AUTHORSHIP_PREFIXES) or bool(PROME_PACKET_RE.match(path))


def is_prome_owned(path):
    """Wider: what ARGUS may be shown UNCOMMITTED. Authorship + surfaces PROME self-commits at closeout."""
    return is_prome_authored(path) or path.startswith(PENDING_EXTRA)


def pending_paths():
    """PROME-owned paths with UNCOMMITTED changes — tracked modifications and new untracked files.

    Why this exists: ARGUS runs pre-commit, so the closeout's own writes are not in any commit yet. Without this
    the audit verdict covers a scope that excludes the work being approved (audit 2026-09-11 F1).
    Deliberately perimeter-scoped: another desk's dirty paths are never handed to ARGUS.
    """
    out = set()
    for line in git("status", "--porcelain").splitlines():
        if len(line) < 4:
            continue
        path = line[3:].strip().strip('"')
        if " -> " in path:              # rename/copy: audit the destination
            path = path.split(" -> ")[-1].strip().strip('"')
        if is_prome_owned(path):
            out.add(path)
    return out


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def find_watermark(exclude_head=True):
    """Return (sha, subject) of the most recent closeout commit — HEAD itself excluded when exclude_head, so a
    run AFTER the closeout commit still scopes the session that just closed."""
    lines = git("log", f"-{MAX_LOOKBACK}", "--format=%H\t%s").splitlines()
    for i, line in enumerate(lines):
        sha, _, subj = line.partition("\t")
        if i == 0 and exclude_head:
            continue
        if CLOSEOUT_RE.match(subj):
            return sha, subj
    return None, None


def commit_paths(sha):
    return set(p for p in git("show", "--name-only", "--format=", sha).splitlines() if p.strip())


def scope(watermark, include_pending=True):
    """Return (commits, committed_paths, pending_paths). The audit scope is the UNION of the last two."""
    commits, paths = [], set()
    for line in git("log", "--format=%H\t%s", f"{watermark}..HEAD").splitlines():
        sha, _, subj = line.partition("\t")
        touched = commit_paths(sha)
        # Durable attribution: the subject convention, OR an all-PROME-owned path set (the `FORGE:` case).
        owned = bool(touched) and all(is_prome_authored(p) for p in touched)
        if PROME_RE.match(subj) or owned:
            commits.append({"sha": sha[:9], "subject": subj,
                            "attribution": "subject" if PROME_RE.match(subj) else "paths"})
            paths |= touched
    pend = pending_paths() if include_pending else set()
    return commits, sorted(paths), sorted(pend - paths)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--include-head", action="store_true", help="let HEAD itself be the watermark (pre-commit run)")
    ap.add_argument("--no-pending", action="store_true", help="committed paths only (diagnostic; NOT the closeout form)")
    args = ap.parse_args(argv)
    wm, subj = find_watermark(exclude_head=not args.include_head)
    if not wm:
        print(f"ARGUS-SCOPE 2 — no closeout commit in the last {MAX_LOOKBACK} commits; scope undefined", file=sys.stderr)
        return 2
    commits, paths, pend = scope(wm, include_pending=not args.no_pending)
    total = len(paths) + len(pend)
    verdict = "SPAWN" if total >= MIN_PATHS else f"SKIP (<{MIN_PATHS} paths)"
    if args.json:
        print(json.dumps({"watermark": wm[:9], "watermark_subject": subj, "prome_commits": commits,
                          "paths": paths, "pending_paths": pend, "path_count": total,
                          "read": {"committed": "git diff <watermark>..HEAD -- <path>",
                                   "pending_tracked": "git diff HEAD -- <path>",
                                   "pending_new": "read the file (it has no committed side)"},
                          "verdict": verdict}, indent=1))
    else:
        print(f"ARGUS-SCOPE · watermark {wm[:9]} — {subj}")
        print(f"  PROME commits since: {len(commits)} · committed paths: {len(paths)} · "
              f"pending paths: {len(pend)} · total: {total} · verdict: {verdict}")
        for c in commits:
            print(f"    {c['sha']}  [{c['attribution']}]  {c['subject'][:92]}")
        for p in paths:
            print(f"    - [committed] {p}")
        for p in pend:
            print(f"    - [PENDING]   {p}   (git diff HEAD -- {p}; read whole if new)")
    return 0 if total >= MIN_PATHS else 3


if __name__ == "__main__":
    sys.exit(main())
