#!/usr/bin/env python3
"""
memory_index_paths.py — ONE definition of "the cold auto-memory index file set".

Built 2026-09-06 (DAEDALUS, `scripts/` lane; PROME Tier-1 task packet, inside the
Will-approved auto-memory three-tier workstream 2026-07-28/31 and the ceiling +
pre-registered SHARD form approved 2026-08-23/28).

WHY THIS FILE EXISTS
--------------------
`memory/auto/INDEX_COLD.md` carries a HARD 51,200 B ceiling (Will-approved
2026-08-23). It truncated silently once at 58,825 B, stranding 26 slugs while the
hot index kept advertising them. Its own header pre-registers the next legal move
once trimming and rotation are exhausted: **SHARD by theme** into sibling files.

Two fleet readers resolve "the cold index":
    scripts/memory_index_check.py     (the closeout gate: --strict --slug)
    scripts/memory_citation_census.py (the flow-pass demotion/promotion census)

Both hardcoded the single path. After a shard, a slug living in a shard would read
as UNINDEXED and `memory_index_check.py --strict --slug <it>` would BLOCK its
owner's closeout on a condition carve-out ③ forbids them to fix — the exact
"gate fails on something the runner cannot fix" failure the --strict docstring
already records once. So the file set is defined ONCE, here, and both read it.

This is the `scripts/harness_caps.env` shape one layer up (PAT-069): "the cold
index" is a CONCEPT; two tools resolving it to two different instruments is how
guards silently disagree. The concept now has one instrument.

THE RULE (deliberately dumb, so it cannot drift)
------------------------------------------------
    cold set = memory/auto/INDEX_COLD.md          (the base, if it exists)
             + memory/auto/INDEX_COLD_*.md        (every shard, sorted by name)

Base first, then shards in sorted order — a stable, reproducible read order, so
two runs on one tree print the same thing. A slug present in ANY member is
INDEXED. Slugs de-dup across members (first appearance wins its position).

An unreadable member is a LOUD FAILURE, never a silent skip: a shard that cannot
be read is indistinguishable, to a naive reader, from a shard that contains
nothing — and "contains nothing" is the answer that un-indexes every slug inside
it. Fail closed `[[finding_fail_loud_on_incomplete_data]]`.

WHAT A CLEAN RESULT PROVES (PAT-074): that every member of the set was OPENED and
READ. It proves nothing about whether the sharding is sensible, whether a slug is
in the RIGHT member, or whether the rows are current.

NOT IN SCOPE: the per-file byte ceiling. `read_cap_check.py <FILE>` stays
per-file — each shard carries its own ceiling; the set is NEVER summed. Summing
would let two 40 KB shards read as one 80 KB breach that no single file has, and
would license "the set is fine" while a member sat past the truncation line.
"""

import os
from typing import List, Tuple

COLD_BASENAME = "INDEX_COLD.md"
COLD_STEM = "INDEX_COLD"
COLD_SUFFIX = ".md"


def cold_index_files(mem_dir: str) -> List[str]:
    """Every cold-index file in `mem_dir`, base first then shards sorted by name.

    Returns [] when none exists — which is the NORMAL pre-migration state and is
    the caller's business to interpret, not an error here.

    Directory unreadable/absent → [] (the callers already handle "no cold index").
    A member that exists but cannot be READ is NOT filtered out here; it is
    returned, so read_cold_indexes() can fail loudly on it. Filtering it here
    would be the silent skip this module exists to prevent.
    """
    base = os.path.join(mem_dir, COLD_BASENAME)
    out = [base] if os.path.exists(base) else []
    try:
        names = os.listdir(mem_dir)
    except OSError:
        return out
    shards = sorted(
        n for n in names
        if n.startswith(COLD_STEM + "_") and n.endswith(COLD_SUFFIX)
    )
    out.extend(os.path.join(mem_dir, n) for n in shards)
    return out


def read_cold_indexes(paths) -> Tuple[List[str], List[Tuple[str, str]]]:
    """Read each path. Returns (texts, unreadable).

    `unreadable` is a list of (path, reason) — non-empty means the caller MUST
    fail; it may not proceed on the partial read. Every caller in the fleet
    surfaces the PATH, because "a shard is broken" without the name is not
    actionable.

    Note `errors="replace"` is used for CONTENT (a mojibake byte must not hide a
    slug), but an OSError — permissions, a directory wearing a shard's name, a
    dangling symlink — is a real perimeter failure and is reported.
    """
    texts, unreadable = [], []
    for p in paths:
        try:
            with open(p, encoding="utf-8", errors="replace") as f:
                texts.append(f.read())
        except OSError as e:
            unreadable.append((p, f"{e.__class__.__name__}: {e}"))
    return texts, unreadable


def describe(n_slugs: int, paths) -> str:
    """One-line human description of the resolved set, for a report header.

    ⚠️ The absent and single-file wordings are BYTE-IDENTICAL to what
    memory_index_check.py printed before sharding existed, so a pre-shard tree
    renders exactly as it always did (PAT-035: the no-op case must be PROVABLY a
    no-op, not asserted to be one). Only a tree that ACTUALLY has shards prints
    the new wording — and then it names every member, because a reader who
    cannot see which files were read cannot audit the count beside them.
    """
    if not paths:
        return f"{COLD_BASENAME} absent (normal pre-migration)"
    if len(paths) == 1 and os.path.basename(paths[0]) == COLD_BASENAME:
        return f"{n_slugs} in {COLD_BASENAME}"
    return (f"{n_slugs} across {len(paths)} cold index file(s): "
            + ", ".join(os.path.basename(p) for p in paths))
