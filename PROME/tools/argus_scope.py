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
#   AUTHORSHIP — paths only PROME writes. Drives the durable attribution fallback (the `FORGE:`-subject case)
#     AND the pending perimeter. EXCLUDES PROME/inbox/: inbound mail is other desks' output sitting in PROME's
#     tree (`finding_path_scoped_git_log_measures_inbound_traffic`).
#   SHARED-LOCATION — memory/auto/ is FLEET-shared: any desk commits there under carve-out (3). Repair review
#     2026-09-11: "avoid treating directory membership as authorship." A pending file there is attributed by its
#     COMMIT LINEAGE, never by its directory; an untracked one has no lineage, so it is reported as
#     UNATTRIBUTED rather than silently claimed or silently dropped.
AUTHORSHIP_PREFIXES = ("PROME/", "FORGE/", "HEARTBEAT.md", ".claude/agents/argus.md")
AUTHORSHIP_EXCLUDE = ("PROME/inbox/",)
SHARED_PREFIXES = ("memory/auto/",)
# PROME's daily session log — CLOSEOUT.md Chunk 2 writes it and Chunk 4 commits it (repair review 2026-09-11).
DAILY_LOG_RE = re.compile(r"^memory/\d{4}-\d{2}-\d{2}\.md$")
# Carve-out (1): a packet PROME authored into another desk's inbox is PROME's to commit, so it is PROME's to audit.
PROME_PACKET_RE = re.compile(r"^AGENTS/[A-Z0-9_]+/inbox/.*from-PROME", re.I)


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def find_watermark(exclude_head=True):
    """Return (sha, subject) of the most recent closeout commit — HEAD itself excluded when exclude_head, so a
    run AFTER the closeout commit still scopes the session that just closed.

    KNOWN LIMIT (external audit 2026-09-11 F1, completeness leg — OPEN, not fixed here): only a LITERAL HEAD is
    excluded, so a domain commit landing immediately after a closeout makes that just-finished closeout the
    watermark and the scope comes back empty. Tracked as an open item rather than silently patched.
    """
    lines = git("log", f"-{MAX_LOOKBACK}", "--format=%H\t%s").splitlines()
    for i, line in enumerate(lines):
        sha, _, subj = line.partition("\t")
        if i == 0 and exclude_head:
            continue
        if CLOSEOUT_RE.match(subj):
            return sha, subj
    return None, None


def is_prome_authored(path):
    """Strict: only paths PROME itself writes. Drives attribution AND the pending perimeter."""
    if path.startswith(AUTHORSHIP_EXCLUDE):
        return False
    return (path.startswith(AUTHORSHIP_PREFIXES)
            or bool(DAILY_LOG_RE.match(path))
            or bool(PROME_PACKET_RE.match(path)))


def is_shared_location(path):
    return path.startswith(SHARED_PREFIXES)


def last_commit_subject(path):
    try:
        out = git("log", "-1", "--format=%s", "--", path).strip()
    except subprocess.CalledProcessError:
        return ""
    return out


def porcelain_entries():
    """(status, path) from `git status --porcelain -z -uall`.

    -uall so a new DIRECTORY is listed as its individual FILES (default collapses it to `dir/`, which both
    undercounts the threshold and hands ARGUS a directory to read). -z so paths with spaces survive.
    """
    raw = git("status", "--porcelain", "-z", "-uall")
    toks = [t for t in raw.split("\0") if t]
    out, i = [], 0
    while i < len(toks):
        tok = toks[i]
        if len(tok) < 4:
            i += 1
            continue
        st, path = tok[:2], tok[3:]
        if st[0] in "RC" and i + 1 < len(toks):
            i += 1                       # rename/copy: next token is the ORIGIN; audit the destination
        out.append((st, path))
        i += 1
    return out


def pending_paths():
    """(owned, unattributed) PROME-relevant paths with UNCOMMITTED changes.

    Why this exists: ARGUS runs pre-commit, so the closeout's own writes are in no commit yet. Without this the
    verdict covers a scope that excludes the work being approved (audit 2026-09-11 F1).
    Perimeter-scoped: another desk's dirty paths are never handed to ARGUS.
    """
    owned, unattributed = set(), set()
    for st, path in porcelain_entries():
        if is_prome_authored(path):
            owned.add(path)
        elif is_shared_location(path):
            subj = last_commit_subject(path)
            if PROME_RE.match(subj):
                owned.add(path)          # PROME's own lineage in a shared directory
            elif subj:
                continue                 # another desk's file — not PROME's to audit
            else:
                unattributed.add(path)   # untracked in a shared dir: no lineage, fail LOUD
    return owned, unattributed


def commit_paths(sha):
    return set(p for p in git("show", "--name-only", "--format=", sha).splitlines() if p.strip())


def scope(watermark, include_pending=True):
    """Return (commits, committed_paths, pending_paths, unattributed_pending).

    🔴 committed_paths and pending_paths DELIBERATELY OVERLAP. A file committed earlier in the session and
    edited again before closeout belongs to BOTH, and needs BOTH reads — the committed diff does not contain
    the later edit. Subtracting one from the other dropped exactly that case, which is the commonest closeout
    shape (STATUS.md written, committed, then corrected). Repair review 2026-09-11, blocking finding #1.
    The size threshold counts UNIQUE paths; the read instructions do not deduplicate."""
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
    if include_pending:
        pend, unattr = pending_paths()
    else:
        pend, unattr = set(), set()
    return commits, sorted(paths), sorted(pend), sorted(unattr)


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
    commits, paths, pend, unattr = scope(wm, include_pending=not args.no_pending)
    total = len(set(paths) | set(pend))          # unique paths for the threshold
    both = sorted(set(paths) & set(pend))
    verdict = "SPAWN" if total >= MIN_PATHS else f"SKIP (<{MIN_PATHS} paths)"
    if args.json:
        print(json.dumps({"watermark": wm[:9], "watermark_subject": subj, "prome_commits": commits,
                          "paths": paths, "pending_paths": pend, "both": both,
                          "unattributed_pending": unattr, "path_count": total,
                          "read": {"committed": "git diff <watermark>..HEAD -- <path>",
                                   "pending_tracked": "git diff HEAD -- <path>",
                                   "pending_new": "read the file (it has no committed side)",
                                   "both": "run BOTH reads — the committed diff omits the later edit"},
                          "verdict": verdict}, indent=1))
    else:
        print(f"ARGUS-SCOPE · watermark {wm[:9]} — {subj}")
        print(f"  PROME commits since: {len(commits)} · committed: {len(paths)} · pending: {len(pend)} · "
              f"both: {len(both)} · unique: {total} · verdict: {verdict}")
        for c in commits:
            print(f"    {c['sha']}  [{c['attribution']}]  {c['subject'][:92]}")
        for p in paths:
            tag = "[committed+PENDING]" if p in set(pend) else "[committed]"
            extra = "   ⚠️ BOTH reads required" if p in set(pend) else ""
            print(f"    - {tag} {p}{extra}")
        for p in pend:
            if p not in set(paths):
                print(f"    - [PENDING]   {p}   (git diff HEAD -- {p}; read whole if new)")
        for p in unattr:
            print(f"    - [UNATTRIBUTED PENDING] {p}   (shared dir, no commit lineage — ask PROME whose it is)")
    return 0 if total >= MIN_PATHS else 3


if __name__ == "__main__":
    sys.exit(main())
