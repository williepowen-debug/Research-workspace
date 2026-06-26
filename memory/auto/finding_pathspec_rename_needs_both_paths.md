---
name: finding_pathspec_rename_needs_both_paths
description: "a pathspec commit of a git-mv rename must list BOTH source+dest paths or it splits the atomic move, leaving a dangling source deletion"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 2f3024fd-7864-49b7-9956-726f4d2a90ff
---

When you `git mv A B` then commit with an explicit pathspec listing only the **destination** (`git commit B -m ...`), git commits the add of B but NOT the delete of A — splitting what `git mv` had staged atomically. The source path is left as a dangling unstaged deletion; if the dest copy is pushed without it, origin ends up with a duplicate file.

**Why:** the shared-tree pathspec-commit discipline ([[finding_pathspec_commit_race_safety]], [[feedback_git_mv_for_inbox_processing]]) tells agents to scope commits to explicit paths — but for a *rename* that scoping silently drops half the change if you only name the new path. Hit by both SHADE and BROCK on 2026-06-26 during inbox→processed and research→archive moves; surfaced by Prome's pre-push `git status` check.

**How to apply:** moving a file with a path-scoped commit? List **both** old+new paths in the pathspec (or don't over-narrow it). Backstop: the now-canonical pre-commit `git status -- AGENTS/<NAME>/` check (root CLAUDE.md, ratified 2026-06-26) — a dangling ` D` on the source path is the tell. Links to [[finding_concurrent_commit_index_race]].
