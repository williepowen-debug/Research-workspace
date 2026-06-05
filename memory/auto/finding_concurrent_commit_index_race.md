---
name: finding_concurrent_commit_index_race
description: "In the shared-tree multi-agent repo, the gap between `git add` and `git commit` is a race — a concurrent agent's commit can grab YOUR staged index under THEIR message; stage+commit atomically in one shell call"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 74d0128b-dae1-471e-b482-6e12cc68944c
---

The fleet shares ONE working tree + ONE `.git` index. With 4+ agents (SAM/BRENT/BROCK/HENRY) committing concurrently, the index is global mutable state. If you `git add` your files in one shell call and `git commit` in a later call, another agent's `git commit` can land in between and **commit YOUR staged files under THEIR message** (observed 2026-06-03: HENRY's KB Pass-0 files were committed by `8ac5bf71 "SAM: session closeout"`, then pushed — permanent mislabel, content intact).

**Why:** staging writes to the shared index; any agent's `commit` flushes whatever is currently staged, regardless of who staged it. Splitting add↔commit across tool-call turns widens the window; a verification step in between (valuable — it caught a stray staged `SAM/MEMORY.md`) widens it further.

**How to apply:**
- In a known-concurrent session, run stage→verify→commit as ONE shell invocation: `git reset HEAD && git add AGENTS/<ME>/ && git diff --cached --stat && git commit -m "..."` chained with `&&` so nothing interleaves.
- Still always `git diff --cached --stat` (or fold a grep-guard that aborts if a non-`AGENTS/<ME>/` path is staged) — concurrent staging by others is real.
- If you lose the race: check `git show --stat <other-commit>` + `git status AGENTS/<ME>/`. If your content is in HEAD and pushed, it's SAFE — do NOT rewrite pushed history to fix the message. Note the mislabel and move on.
- Builds on [[feedback_agent_git_isolation]] + [[feedback_check_staged_before_commit]] + [[finding_push_train_pattern]].
