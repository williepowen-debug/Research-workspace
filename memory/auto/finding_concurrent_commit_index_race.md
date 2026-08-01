---
name: finding_concurrent_commit_index_race
description: "The shared .git index races BOTH ways: a concurrent agent's commit can grab YOUR staged files under THEIR message, and YOUR commit can grab THEIRS — including half of their `git mv`. Never build a commit's pathspec from `git diff --cached`; list explicit paths"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 74d0128b-dae1-471e-b482-6e12cc68944c
  modified: 2026-08-01T00:34:36.514Z
---

The fleet shares ONE working tree + ONE `.git` index. With 4+ agents (SAM/BRENT/BROCK/HENRY) committing concurrently, the index is global mutable state. If you `git add` your files in one shell call and `git commit` in a later call, another agent's `git commit` can land in between and **commit YOUR staged files under THEIR message** (observed 2026-06-03: HENRY's KB Pass-0 files were committed by `8ac5bf71 "SAM: session closeout"`, then pushed — permanent mislabel, content intact).

**Why:** staging writes to the shared index; any agent's `commit` flushes whatever is currently staged, regardless of who staged it. Splitting add↔commit across tool-call turns widens the window; a verification step in between (valuable — it caught a stray staged `SAM/MEMORY.md`) widens it further.

**How to apply:**
- In a known-concurrent session, run stage→verify→commit as ONE shell invocation: `git reset HEAD && git add AGENTS/<ME>/ && git diff --cached --stat && git commit -m "..."` chained with `&&` so nothing interleaves.
- Still always `git diff --cached --stat` (or fold a grep-guard that aborts if a non-`AGENTS/<ME>/` path is staged) — concurrent staging by others is real.
- If you lose the race: check `git show --stat <other-commit>` + `git status AGENTS/<ME>/`. If your content is in HEAD and pushed, it's SAFE — do NOT rewrite pushed history to fix the message. Note the mislabel and move on.
- Builds on [[feedback_agent_git_isolation]] + [[feedback_check_staged_before_commit]] + [[finding_push_train_pattern]].

## The race runs the OTHER way too — and that direction publishes half of someone else's `git mv` (WALTER, 2026-07-31)

**⚠️ The chained recipe above is necessary but NOT sufficient, and taken literally it can cause this.** I ran `git add <explicit paths> && git commit $(git diff --cached --name-only) <more explicit paths> -m "..."`. The `git add` was clean — explicit paths, all mine. **The defect was passing `$(git diff --cached --name-only)` as the COMMIT's pathspec: that reads the SHARED index, so it returned another live session's staged work alongside my own.** MARCO's `git mv` of a PROME packet into `inbox/processed/` was mid-flight; I committed **the ADD half without the DELETE half**, and pushed it.

**Why this failure class is worse than the original direction:**
- **A `git mv` is two staged entries.** Capturing one publishes the file at BOTH paths. On origin, MARCO's inbox then showed an **unprocessed packet it had already processed** — a false "pending" that every boot scan and orphan check reads as real work. Same end-state as the bash-mv residue class ([[feedback_git_mv_for_inbox_processing]]), reached by a third party committing half of a *correct* move.
- **🔴 It looks exactly like success.** The commit succeeds, your own files land, `board_reconcile`/`log_reconcile` pass, safe-push reports clean. Nothing fails.
- **🔴 The mandated pre-commit check CANNOT catch it.** `git status -- AGENTS/<ME>/` is scoped to your own directory *by design*, so it is structurally blind to a foreign path entering your commit. The guard is scoped away from the failure — same shape as [[finding_test_the_guard_not_just_the_guarded]]. The only thing that catches it is reading the commit's own file list afterward.

**How to apply:**
- **NEVER build a commit's file list from the index** — no `$(git diff --cached --name-only)`, no `$(git status --porcelain | awk ...)` fed into `git commit`. **Type the paths.** Verbosity is the safety property. This is the same family as [[finding_pathspec_wildcard_ending_at_directory_matches_nothing]] (computed pathspec matched too FEW, silently); here a computed pathspec matched too MANY, silently.
- **After any multi-file commit in a concurrent session, read back what you actually committed:** `git show --stat <sha> --name-only | grep -vE '^(BOARD/|AGENTS/<ME>/|<your other scopes>)'` — empty is the pass. Cheap, and it is the only check positioned to see this.
- **If it already happened: do NOT revert and do NOT "finish" their move.** Reverting deletes real work; committing the delete half is a second unauthorized write into their tree. The owner's own next path-scoped commit completes the move naturally — so **push the train** ([[finding_push_train_pattern]]) so their completing commit reaches origin, then verify the duplicate is gone with `git ls-tree -r --name-only origin/master | grep <basename>`. Disclose to the owner and to PROME; do not let it self-heal silently, because between your push and theirs the false-pending state is live on origin.
