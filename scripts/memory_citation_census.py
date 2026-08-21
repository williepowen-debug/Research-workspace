#!/usr/bin/env python3
"""memory_citation_census.py — census of auto-memory citations; advisory demotion/promotion queues.

Built 2026-08-21 (DAEDALUS scripts/ lane; Will-commissioned memory-retrieval design,
disposition ③ of answer packet 1e1067253, spec committed pre-8/28).

WHAT A PASS PROVES (PAT-074): a run that exits 0 proves the two index tiers parsed to a
non-zero slug set, the git-log window was scanned, and the printed queues reflect that scan.
It does NOT prove any memory is valuable or dead — queues are ADVISORY input to PROME's
flow-pass judgment (overrides expected). It cannot see the agent who never knew a slug
existed; a zero-citation row is "uncited in window", never "useless".

METHOD (reproduces PROME's 8/21 census command from ask packet 5c66ea63b; SCRATCH
baseline 515 cites / 227 slugs / 30d, "reproduce don't trust"): a slug is CITED by a
commit when it appears in the commit MESSAGE (subject+body) — conscious invocation in the
desk's own words. Diff-text scanning was tried first and rejected (see scan_git_window
docstring): it counts rotations, regens, and quoting files as consumption.

QUEUES:
  (a) DEMOTION queue  — HOT index rows uncited >= --days (default 30), minus rows carrying
      the HELD-HOT marker (a held row is a decision, not an oversight — ZHAO's
      declared-asymmetry form; it prints in its own section, never in the queue).
  (b) PROMOTION queue — COLD index rows cited >= --min-promote (default 2) in-window.
  (c) counts summary (hot/cold totals, cite totals, coverage).

RC CONTRACT (§9): 0 = census ran and printed (queues may be non-empty — advisory, not a
gate; deliberate non-zero-on-findings would make it a gate the spec forbids).
2 = CANNOT-CERTIFY: an index parsed to zero slugs, git failed, or the window scanned zero
commits — no queue printed, because an empty scan must never read as an empty queue
(finding_fail_loud_on_incomplete_data / PAT-074).

INVOKED BY: PROME flow passes (MEMORY.md >=75% demotion passes) + DAEDALUS Production
Review question ④ (canon-graduation candidates = rows citing a PAT/§ that now exists).
Not boot-wired anywhere by design.

Usage:
  python3 scripts/memory_citation_census.py                # default 30d window
  python3 scripts/memory_citation_census.py --days 60 --min-promote 3
  python3 scripts/memory_citation_census.py --hot-index F --cold-index F  # fixture legs (§3/§8)
"""

import argparse
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HOT_INDEX = REPO / "memory" / "auto" / "MEMORY.md"
COLD_INDEX = REPO / "memory" / "auto" / "INDEX_COLD.md"
MEMORY_DIR_PREFIX = "memory/auto/"

SLUG_RE = re.compile(r"\b((?:finding|feedback|project|reference|user)_[a-z0-9_]+)")


def parse_hot_index(path: Path):
    """MEMORY.md: thematic bullets, each packing many 'slug — hook' entries split on '·'.
    Returns {slug: held_hot_bool}. Split on '·' within a bullet, never assume one slug/line."""
    slugs = {}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"CANNOT-CERTIFY: hot index unreadable: {e}")
        sys.exit(2)
    for line in text.splitlines():
        if not line.lstrip().startswith("-"):
            continue
        for segment in line.split("·"):
            m = SLUG_RE.search(segment)
            if m:
                # last slug in segment wins the HELD-HOT attribution only if marker present
                for slug in SLUG_RE.findall(segment):
                    slugs[slug] = slugs.get(slug, False) or ("HELD-HOT" in segment)
    return slugs


def _annotation_of(text: str):
    if "embed-pending" in text:
        return "embed-pending" + (" " + text.split("embed-pending", 1)[1].strip(" →`—-")[:60] if True else "")
    if "embedded" in text:
        tail = text.split("embedded", 1)[1].strip(" →`—-").replace("`", "")
        return "embedded → " + tail[:60]
    return None


def parse_cold_index(path: Path):
    """INDEX_COLD.md: one '- slug — hook' row per line under theme headings.
    Returns {slug: annotation} — per-row embedded/embed-pending marker wins, else the
    section heading's, else 'plain' (census-v2 input ③: a heavily-cited EMBEDDED row may
    be cited BECAUSE it lives where needed — promotion would be duplication, not recall;
    the flow pass decides with this context printed)."""
    slugs = {}
    section_ann = None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"CANNOT-CERTIFY: cold index unreadable: {e}")
        sys.exit(2)
    for line in text.splitlines():
        if line.startswith("##"):
            section_ann = _annotation_of(line)
        elif line.lstrip().startswith("-"):
            m = SLUG_RE.search(line)
            if m:
                slugs[m.group(1)] = _annotation_of(line) or section_ann or "plain"
    return slugs


def scan_git_window(days: int, slugs):
    """Reproduces PROME's census command (ask packet 5c66ea63b):
        git log --since=<window> --pretty="%s %b" | grep -oE "(finding|feedback|project)_[a-z0-9_]+"
    A citation = a slug named in a COMMIT MESSAGE (subject+body) — the desk consciously
    invoking the memory in its own words. NOT diff text: the first live run (2026-08-21)
    used diffs and read 3,278 cites / 80% cold coverage vs the 515 / 37% baseline —
    rotations, index regens, and files QUOTING a slug all counted as consumption.
    Documented deviation from the baseline command: SLUG_RE also covers reference_/user_
    prefixes (the baseline grep missed those two classes; superset, direction stated).
    Returns ({slug: set(commit)}, n_commits)."""
    try:
        out = subprocess.run(
            ["git", "log", f"--since={days} days ago", "--format=@@COMMIT@@ %H%n%s%n%b"],
            cwd=REPO, capture_output=True, text=True, errors="replace", check=True,
        ).stdout
    except (subprocess.CalledProcessError, OSError) as e:
        print(f"CANNOT-CERTIFY: git log failed: {e}")
        sys.exit(2)

    cited = defaultdict(set)   # slug -> set of commits whose MESSAGE names it
    commit, n_commits = None, 0
    slugset = set(slugs)
    for line in out.splitlines():
        if line.startswith("@@COMMIT@@ "):
            commit = line.split()[1]
            n_commits += 1
        elif commit:
            for slug in SLUG_RE.findall(line):
                if slug in slugset:
                    cited[slug].add(commit)
    return cited, n_commits


def scan_artifact_window(days: int, slugs):
    """SECOND SOURCE (census-v2 input ①, PROME reframe of the v1 'defect'): slugs WRITTEN
    into artifacts (packets/KBs/links) in-window — added diff lines only, memory/auto/
    self-refs excluded. Not the calibrated primary (its 80%-vs-37% cold gap vs the
    baseline is the size of its extra reach), but the v1 all-lines diff scan measured
    something real that commit messages miss: day one's false-cold (resolver_anchored)
    was load-bearing in an artifact the same afternoon, invisible to messages.
    Returns {slug: set(commit)}."""
    try:
        out = subprocess.run(
            ["git", "log", "-p", f"--since={days} days ago", "--format=@@COMMIT@@ %H"],
            cwd=REPO, capture_output=True, text=True, errors="replace", check=True,
        ).stdout
    except (subprocess.CalledProcessError, OSError) as e:
        print(f"CANNOT-CERTIFY: git log -p failed: {e}")
        sys.exit(2)
    cited = defaultdict(set)
    commit, path = None, None
    slugset = set(slugs)
    for line in out.splitlines():
        if line.startswith("@@COMMIT@@ "):
            commit = line.split()[1]
            path = None
        elif line.startswith("+++ b/"):
            path = line[6:]
        elif (commit and line.startswith("+") and not line.startswith("+++")
              and not (path and path.startswith(MEMORY_DIR_PREFIX))
              and ("finding_" in line or "feedback_" in line or "project_" in line
                   or "reference_" in line or "user_" in line)):
            for slug in SLUG_RE.findall(line):
                if slug in slugset:
                    cited[slug].add(commit)
    return cited


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--days", type=int, default=30, help="citation window (default 30, the census's validated window)")
    ap.add_argument("--min-promote", type=int, default=2, help="cold-row citations to enter promotion queue (default 2)")
    ap.add_argument("--hot-index", type=Path, default=HOT_INDEX, help="override for fixture testing")
    ap.add_argument("--cold-index", type=Path, default=COLD_INDEX, help="override for fixture testing")
    ap.add_argument("--head", type=int, default=40, help="max promotion rows printed (count always printed in full)")
    args = ap.parse_args()

    hot = parse_hot_index(args.hot_index)      # {slug: held_hot}
    cold = parse_cold_index(args.cold_index)   # set

    if not hot:
        print(f"CANNOT-CERTIFY: hot index parsed to ZERO slugs ({args.hot_index}) — parse failure, not an empty tier")
        sys.exit(2)
    if not cold:
        print(f"CANNOT-CERTIFY: cold index parsed to ZERO slugs ({args.cold_index}) — parse failure, not an empty tier")
        sys.exit(2)

    all_slugs = set(hot) | set(cold)
    cited, n_commits = scan_git_window(args.days, all_slugs)
    if n_commits == 0:
        print(f"CANNOT-CERTIFY: git window scanned ZERO commits ({args.days}d) — no basis for any queue")
        sys.exit(2)
    art_cited = scan_artifact_window(args.days, all_slugs)

    total_cites = sum(len(v) for v in cited.values())
    hot_cited = {s for s in hot if s in cited}
    cold_cited = {s for s in cold if s in cited}
    hot_art_only = {s for s in hot if s not in cited and s in art_cited}

    print(f"memory_citation_census v2 — window {args.days}d, {n_commits} commits · primary = commit-message grep (calibrated vs PROME 5c66ea63b baseline) · second source = artifact writes (added diff lines, self-refs excluded)")
    print(f"COUNTS: hot {len(hot)} rows ({len(hot_cited)} msg-cited, {len(hot)-len(hot_cited)} msg-uncited, of those {len(hot_art_only)} artifact-rescued) · cold {len(cold)} rows ({len(cold_cited)} msg-cited) · {total_cites} msg-citations across {len(cited)} slugs · both-tier overlap {len(set(hot)&set(cold))}")

    held = sorted(s for s, h in hot.items() if h and s not in cited and s not in art_cited)
    demote = sorted(s for s, h in hot.items()
                    if not h and s not in cited and s not in art_cited)
    promote = sorted((s for s in cold if len(cited.get(s, ())) >= args.min_promote),
                     key=lambda s: -len(cited[s]))

    if demote:
        print(f"\nDEMOTION QUEUE (advisory — hot, uncited on BOTH sources {args.days}d, no HELD-HOT marker): {len(demote)} rows")
        for s in demote:
            print(f"  DEMOTE-CANDIDATE {s}")
    else:
        print(f"\nDEMOTION QUEUE: empty — every unheld hot row cited (either source) within {args.days}d")
    if hot_art_only:
        print(f"  (artifact-rescued, NOT queued — msg-uncited but written into artifacts in-window: {len(hot_art_only)} rows: {', '.join(sorted(hot_art_only)[:10])}{'…' if len(hot_art_only)>10 else ''})")

    if held:
        print(f"HELD-HOT (uncited both sources but held by declared decision — not queued): {len(held)}")
        for s in held:
            print(f"  HELD-HOT {s}")
    denom = len(demote) + len(held)
    if denom:
        print(f"FALSE-COLD RATE proxy: {len(held)}/{denom} = {len(held)/denom:.0%} of the would-be queue is held by declared decision (day-one floor 7%; a CLIMBING number means the citation proxy is degrading — census-v2 input ②)")

    if promote:
        print(f"\nPROMOTION QUEUE (advisory — cold, cited >={args.min_promote}x in {args.days}d): {len(promote)} rows")
        for s in promote[:args.head]:
            print(f"  PROMOTE-CANDIDATE {s} ({len(cited[s])} commits) [{cold[s]}]")
        if len(promote) > args.head:
            print(f"  … and {len(promote)-args.head} more above threshold (ranked head capped at --head {args.head}; the count above is the population, this list is not)")
    else:
        print(f"\nPROMOTION QUEUE: empty — no cold row cited >={args.min_promote}x in {args.days}d")

    print("\nAdvisory only: PROME flow-pass judgment unchanged; a hot row surviving this queue says HELD-HOT: <why> on its row. This census cannot see the agent who never knew the slug existed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
