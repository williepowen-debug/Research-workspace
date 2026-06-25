---
name: finding_curated_worktree_branch_landing
description: "reconcile a stale/divergent branch safely via isolated worktree — salvage net-new, drop superseded-vs-authoritative, merge the clean canonical branch, guardrail-verify, then FF-land"
metadata: 
  node_type: memory
  type: project
  originSessionId: cf89e4b7-9687-42dc-a7c2-560f84d1d85d
---

When an unmerged branch is far behind master (e.g. 111 commits) and `git merge-tree` shows conflicts, do NOT raw-merge. Instead run a **curated landing in an isolated git worktree** so the shared main tree never leaves master until a verified fast-forward:

1. `git worktree add -b <staging> <tmp-path> origin/master` (main tree stays on master, untouched — no race with sibling agents).
2. Triage the branch into buckets by comparing against master: **net-new files** (salvage via `git checkout <branch> -- <paths>`), **conflicting-but-superseded** (drop — keep master's, which is usually newer/fuller), and **a separate clean canonical branch** that supersedes part of the stale one (merge that instead).
3. Decide conflicts by *timestamp + completeness*, not by which branch you started from. Check `git rev-list --count <base>..origin/master -- <file>` — **0 commits since base means master never diverged**, so the branch's edit is safe to apply faithfully (the "N behind" only ever touched *other* files).
4. Guardrail-verify before landing: (a) master's authoritative files literally unchanged (`git diff --quiet`), (b) staging diff stays inside an allowlist (no leak into other agents' dirs), (c) no dangling refs (a doc on branch X referencing a file that lives only on branch Y → land the prereq first).
5. FF-land from the main tree only after a clean-tree gate: `git merge --ff-only <staging>`. Then `git worktree remove` + `git branch -D` (use `-D`: `-d` refuses because it compares to origin, but the commits already live on local master).

**Why:** the shared working tree means a stray checkout disrupts concurrent agents, and a raw merge of a stale branch clobbers master's newer same-day work + replays a huge conflict diff. The worktree isolates the build; bucketed triage recovers value without regressing master.

**How to apply:** use for any branch reconciliation where merge-tree shows conflicts or the branch is many commits behind. Pairs with [[finding_two_machine_partition_clean_merge]] and the pathspec-commit discipline in [[finding_pathspec_commit_race_safety]]. Validated 2026-06-25 landing two `prome/*` branches (pending-flush + reconcile-yeyou) onto master at 2ee22af4.
