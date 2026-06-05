---
name: pathspec-commit-race-safety
description: "Use `git commit <pathspec>` for modified files and atomic `git add <files> && git commit <same files>` for new files; never `git reset HEAD`. Required when multiple agents share a `.git/index`."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 110e9b3c-07c3-4222-87b9-57e8595e4580
---

When multiple agents share one working directory and one `.git/index`, the staging area is a global shared resource. Operations that touch the index — especially `git reset HEAD` — can clobber another agent's pending stages between their `git add` and their `git commit`. This was the mechanism behind mis-attributed commit `8ac5bf71` (Jun 4 2026): SAM ran the standard `git reset HEAD` + `git add AGENTS/SAM/MEMORY.md`, verified with `git diff --cached --stat`, then committed — but HENRY's concurrent process ran its own `git reset HEAD` + `git add AGENTS/HENRY/...` in the window between SAM's verify and SAM's commit. SAM's commit then captured HENRY's staged files under SAM's commit message.

**Why:** the shared `.git/index` is one file. Any agent's `git reset HEAD` un-stages every agent's pending stages. The standard protocol (reset → add → verify → commit) has a window between verify and commit where another agent can clobber. The protocol is correct under the assumption of single-agent operation; it fails as soon as agents are concurrent.

**How to apply:**

- **For already-tracked files you've modified:** use `git commit AGENTS/<NAME>/<file> -m "..."` directly. Pathspec commit captures working-tree content, bypasses the staging area entirely — race-safe regardless of what other agents do to the index.

- **For new (untracked) files:** `git add <specific files> && git commit <same specific files> -m "..."`. The atomic chain minimizes the staging-area window; the pathspec on commit means even if another agent stages something in the microsecond between `add` and `commit`, your commit only takes the named files. Use explicit file paths, never directory wildcards (`git add AGENTS/<NAME>/` can race-collide; `git add AGENTS/<NAME>/specific_file.md` cannot).

- **Never use `git reset HEAD`** in a shared-index environment. If you have stuff staged from a previous operation and want to start over, either commit the staged stuff (pathspec or otherwise) or leave it alone. Reset is the race trigger.

- **Verification step is optional** under pathspec discipline. `git diff --cached --stat` between add and commit is the canonical sanity check, but pathspec commits are race-safe with or without it.

**When this stops mattering:** the architectural fix is separate clones per agent (each with its own `.git/index`). Under that model, `git reset HEAD` is local-only and can't clobber anyone. See [[SAM proposals 2026-06-04 separate clones]] (review-not-apply drafts in `AGENTS/SAM/proposals/`). Until that migration lands, pathspec is the interim discipline.

**Pre-existing protocol that this refines:** [[feedback_agent_git_isolation]] ("never stash/commit other agents' files") and [[feedback_check_staged_before_commit]] ("run git diff --cached before committing"). Both rules are still valid but insufficient on their own — the `8ac5bf71` race happened despite both being honored, because the discipline assumed a non-concurrent model. Pathspec discipline closes the gap.

**Validated:** Jun 4 2026 — caught and corrected `8ac5bf71` race within minutes; SAM session-closeout MEMORY.md re-committed cleanly via `git commit AGENTS/SAM/MEMORY.md -m "..."` as `6c7d840b`. Subsequent commit `afc12c40` (proposal-file additions) used the atomic add+commit pattern for new files with explicit paths — clean, no collision despite BROCK being concurrently active.

Cross-agent transferable: applies to ANY agent operating in the shared-folder environment (SAM, HENRY, BROCK, BRENT, CARL, REGINALD, OZK, RED, LIQUID, HENRY, HAWK, BRENT, NEXUS, and any future agents). Should propagate via auto-memory + root CLAUDE.md update.
