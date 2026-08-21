---
name: finding_add_with_one_bad_pathspec_stages_nothing
description: "git add with several paths is ATOMIC — one stale path aborts the whole add, staging NOTHING; in an &&-chain the exit code is the only tell and the packets orphan silently"
metadata:
  node_type: memory
  type: finding
---

`git add A B C` is **atomic**: if any one path does not match, git aborts with `fatal: pathspec '...' did not match any files` and stages **NOTHING** — not even A and B, which were perfectly valid. This is the opposite of the intuition that add is per-path and best-effort.

**Why it bites hardest in the multi-packet closeout.** The standard carve-out ① flow stages several self-authored packets into different agents' inboxes in one command. If a *concurrent session has already consumed and moved* one of them (`inbox/X.md` → `inbox/processed/X.md`), that path goes stale **between writing it and staging it** — and the whole add dies. Written as `git add <3 paths> && git status ...`, the `&&` simply stops, so **nothing prints about the failure**, the subsequent `git status` never runs, and the natural next step (`git commit <paths>`) can *also* look fine because path-scoped commit re-stages from the worktree. **The exit code is the only tell**, and an `&&` chain swallows it into "the later command just didn't run."

**Failure mode is silent orphaning, which is the expensive kind:** the packets never reach their recipients and nobody is told anything was sent — the exact class carve-out ① exists to prevent (~12% of packets pre-detector). Hit live 2026-08-20 (LIQUID): three packets staged in one `&&` chain, PROME had already moved its copy to `processed/` minutes earlier, the add aborted whole, and BOND's + CREED's packets would have orphaned. Caught only because PROME independently noticed its own copy arrived untracked and said so.

**How to apply:**
- **Stage packets one path per command**, or run `git add` on its own line and **read its output** — never bury a multi-path add mid-`&&`-chain where a non-zero exit reads as "the chain stopped."
- **Verify what actually staged, don't assume:** `git diff --cached --name-only` after the add. A count that is short — or empty — is the whole finding.
- **Expect the stale path.** On a shared box other sessions consume your packets *while you work*; a path you wrote 20 minutes ago may already be in `processed/`. That is normal traffic ([[finding_dirty_path_means_in_flight_not_orphaned]]), not an error to fix — just re-resolve the path.
- **Backstop:** `bash scripts/orphan_check.sh <NAME>` before closeout, and after pushing confirm your own paths reached origin with `git diff --stat origin/master HEAD -- <your paths>` (empty = delivered) — "Pushed." alone can be true about someone else's commits ([[finding_push_train_hides_a_failed_commit]]).

Distinct from its siblings: [[finding_pathspec_rename_needs_both_paths]] is a rename committing *half*; [[finding_pathspec_wildcard_ending_at_directory_matches_nothing]] is a pattern matching *nothing*; this one is **valid paths staging nothing because an unrelated path in the same command was stale**. Same family as [[finding_pathspec_commit_race_safety]] and [[finding_record_of_an_action_is_not_the_action]] — the record of an intended `git add` is not the add.
