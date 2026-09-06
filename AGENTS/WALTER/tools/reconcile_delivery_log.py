#!/usr/bin/env python3
"""
reconcile_delivery_log.py — sweep `delivery_log.tsv` written_state against git ground truth.

WHY THIS EXISTS
---------------
`written_state` distinguishes a handoff that is written-but-not-yet-pushed from one
that is genuinely delivered. That distinction is real and load-bearing *within* a
session, and `walter_doctor`'s `delivery_claim_vs_git` (check #23) consumes it — so
the column must NOT be dropped.

But it was only ever reconciled by hand, for the current session's rows, at closeout.
Historical rows were never swept. On 2026-07-27 that had accumulated to **774 rows
reading `written_not_delivered_pending_push` while all 774 paths were in git** — i.e.
the column systematically UNDERSTATED delivery and had become decorative.

A deferrable manual step wants a mechanism, not a remembered ritual
(auto-memory: `finding_mechanize_the_cap_not_the_ritual`).

DEFINITION OF `delivered` (BOARD_CONSUMPTION_SPEC): committed AND on origin.
Two ways a path satisfies that:
  (a) it is present in the `origin/master` tree right now; or
  (b) it is ABSENT from the tree but git has seen it before — consumed-by-delete,
      or a retired inbox dir. A file gone from disk is usually SUCCESS; only a path
      git has NEVER seen is a real orphan. (Same `_ever_in_git` logic that stopped
      `delivery_claim_vs_git` v1 from firing 17 false HIGHs.)

SAFETY
------
- DRY-RUN BY DEFAULT. `--apply` is required to write.
- Refuses to write if the field count is not uniform before AND after.
- Only ever flips `written_not_delivered_pending_push` -> `delivered`. It never
  flips the other way, never touches any other column, and never reorders rows.
- Matching is by ROW INDEX + the path COLUMN, never by substring search over the
  line — a loose substring matcher flipped 2 unrelated rows on 2026-07-27 because
  the word appeared in a free-text notes field, and happened to be right by luck.

USAGE
  python3 AGENTS/WALTER/tools/reconcile_delivery_log.py            # dry run
  python3 AGENTS/WALTER/tools/reconcile_delivery_log.py --apply    # write
"""
import subprocess
import sys
from pathlib import Path

LOG = "AGENTS/WALTER/routed/delivery_log.tsv"
PENDING = "written_not_delivered_pending_push"
DELIVERED = "delivered"
REF = "origin/master"
EXPECTED_FIELDS = 9
PATH_COL = 6      # handoff_path
STATE_COL = 7     # written_state


def sh(args):
    return subprocess.run(args, capture_output=True, text=True)


def repo_root():
    r = sh(["git", "rev-parse", "--show-toplevel"])
    if r.returncode != 0:
        sys.exit("not a git repo")
    return Path(r.stdout.strip())


def tree_paths(ref):
    """Every path present in `ref` right now."""
    r = sh(["git", "ls-tree", "-r", "--name-only", ref])
    if r.returncode != 0:
        sys.exit(f"cannot read {ref} — fetch first? ({r.stderr.strip()})")
    return set(r.stdout.splitlines())


def ever_in_git(path):
    """Was this path EVER in history REACHABLE FROM `REF` (= origin/master)?

    Returns True (was on origin, now gone -> consumed-by-delete / retired dir),
    False (origin has never seen it -> real orphan), or None (git could not
    answer -> UNKNOWN, which is NOT delivered).

    🔴 FIXED 2026-09-05 (Codex finding 1). This was `git log --all`, which
    includes UNPUSHED LOCAL COMMITS. A handoff committed locally but never
    pushed therefore flipped to `delivered` — the exact inverse of this log's
    own definition (`delivered` = committed AND on origin). The window is not
    hypothetical: after a non-ff push abort (root CLAUDE.md §Git Protocol step 3)
    HEAD routinely carries commits origin does not have, and this script's whole
    contract is that it runs AFTER the push. Scope the history to the ref whose
    tree the primary check already uses, and never let an unusable answer read
    as delivery. `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`
    """
    r = sh(["git", "log", REF, "--oneline", "-1", "--", path])
    if r.returncode != 0:
        return None
    return bool(r.stdout.strip())


def main():
    apply = "--apply" in sys.argv
    root = repo_root()
    log = root / LOG
    if not log.exists():
        sys.exit(f"missing {LOG}")

    raw = log.read_text(encoding="utf-8")
    lines = raw.split("\n")
    trailing_nl = lines and lines[-1] == ""
    body = lines[:-1] if trailing_nl else lines

    # integrity BEFORE
    widths = {len(l.split("\t")) for l in body if l.strip()}
    if widths != {EXPECTED_FIELDS}:
        sys.exit(f"REFUSING: field count not uniform before edit: {sorted(widths)}")

    on_origin = tree_paths(REF)

    flips, orphans, unknowns, unresolved = [], [], [], 0
    cache = {}
    for i, line in enumerate(body):
        if not line.strip() or i == 0:      # header
            continue
        f = line.split("\t")
        if f[STATE_COL] != PENDING:
            continue
        p = f[PATH_COL]
        if p in on_origin:
            flips.append(i)
            continue
        if p not in cache:
            cache[p] = ever_in_git(p)
        if cache[p] is True:
            flips.append(i)                 # was on origin, now gone: consumed-by-delete / retired dir
        elif cache[p] is False:
            orphans.append((i, p))
            unresolved += 1
        else:                               # None -> git could not answer
            unknowns.append((i, p))
            unresolved += 1

    print(f"delivery_log rows: {len(body) - 1}")
    print(f"  pending -> delivered (in {REF} tree, or in {REF} HISTORY): {len(flips)}")
    print(f"  REAL ORPHANS ({REF} has NEVER seen the path, left untouched): {len(orphans)}")
    for i, p in orphans[:20]:
        print(f"    row {i + 1}: {p}")
    if len(orphans) > 20:
        print(f"    … and {len(orphans) - 20} more")
    if unknowns:
        print(f"  UNKNOWN (git could not answer — NOT flipped, NOT an orphan): {len(unknowns)}")
        for i, p in unknowns[:20]:
            print(f"    row {i + 1}: {p}")

    if not apply:
        print("\nDRY RUN — nothing written. Re-run with --apply to write.")
        return 0 if unresolved == 0 else 1

    if not flips:
        print("\nnothing to do.")
        return 0

    for i in flips:
        f = body[i].split("\t")
        f[STATE_COL] = DELIVERED
        body[i] = "\t".join(f)

    # integrity AFTER
    widths = {len(l.split("\t")) for l in body if l.strip()}
    if widths != {EXPECTED_FIELDS}:
        sys.exit(f"REFUSING TO WRITE: field count broke during edit: {sorted(widths)}")

    out = "\n".join(body) + ("\n" if trailing_nl else "")
    log.write_text(out, encoding="utf-8")
    print(f"\nWROTE {len(flips)} rows -> {DELIVERED}. Field count uniform at {EXPECTED_FIELDS}.")
    if orphans:
        print(f"⚠️  {len(orphans)} real orphan(s) LEFT AS-IS — investigate, do not sweep.")
    if unknowns:
        print(f"⚠️  {len(unknowns)} UNKNOWN row(s) LEFT AS-IS — unavailable evidence is not delivery.")
    return 0 if unresolved == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
