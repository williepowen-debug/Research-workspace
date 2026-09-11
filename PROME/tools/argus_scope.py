#!/usr/bin/env python3
"""argus_scope.py — the GIT WATERMARK that defines what ARGUS audits (WQ-226, Will-ruled 2026-09-11).

PROME cannot choose what ARGUS reads: the scope is every path touched by a PROME-authored commit since the
PREVIOUS CLOSEOUT COMMIT. A closeout commit is one whose subject starts `PROME: [<TIER> ]closeout` (case-
insensitive; "STANDARD closeout", "LIGHT closeout", "closeout 9/10 evening" all match; a subject that merely
MENTIONS closeout later in the line — "WQ-227 registered (exempt-desk closeout …)" — does not). PROME-authored =
subject starts with `PROME` (the fleet convention: `<DESK>: …` or `<DESK> -> <RECIPIENT>: …`).

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


def scope(watermark):
    commits = []
    for line in git("log", "--format=%H\t%s", f"{watermark}..HEAD").splitlines():
        sha, _, subj = line.partition("\t")
        if PROME_RE.match(subj):
            commits.append({"sha": sha[:9], "subject": subj})
    paths = set()
    for c in commits:
        paths |= set(p for p in git("show", "--name-only", "--format=", c["sha"]).splitlines() if p.strip())
    return commits, sorted(paths)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--include-head", action="store_true", help="let HEAD itself be the watermark (pre-commit run)")
    args = ap.parse_args(argv)
    wm, subj = find_watermark(exclude_head=not args.include_head)
    if not wm:
        print(f"ARGUS-SCOPE 2 — no closeout commit in the last {MAX_LOOKBACK} commits; scope undefined", file=sys.stderr)
        return 2
    commits, paths = scope(wm)
    verdict = "SPAWN" if len(paths) >= MIN_PATHS else f"SKIP (<{MIN_PATHS} paths)"
    if args.json:
        print(json.dumps({"watermark": wm[:9], "watermark_subject": subj, "prome_commits": commits,
                          "paths": paths, "verdict": verdict}, indent=1))
    else:
        print(f"ARGUS-SCOPE · watermark {wm[:9]} — {subj}")
        print(f"  PROME commits since: {len(commits)} · paths: {len(paths)} · verdict: {verdict}")
        for c in commits:
            print(f"    {c['sha']}  {c['subject'][:100]}")
        for p in paths:
            print(f"    - {p}")
    return 0 if len(paths) >= MIN_PATHS else 3


if __name__ == "__main__":
    sys.exit(main())
