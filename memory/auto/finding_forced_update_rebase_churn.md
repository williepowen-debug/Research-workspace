---
name: ""
metadata: 
  node_type: memory
  originSessionId: 4ee26111-1449-4eef-83c9-717df4b05511
---

The fleet's `git pull --rebase`-on-a-single-shared-branch protocol (CLAUDE.md) **rewrites local-commit SHAs on every rebase** — that is the inherent cost of keeping master linear. A 2-day-stale observer whose `origin/master` tracking ref points at an old commit then cannot fast-forward to the churned tip, so `git fetch` labels it **"forced update"** even though no one ran `push --force` and nothing was lost.

**Do not alarm on "forced update" alone.** Verify benign:
- `git rev-parse --is-shallow-repository` → `false` means merge-base is trustworthy (see [[finding_shallow_clone_false_fork]]).
- `git merge-base --is-ancestor <old-sha> origin/master` → exit 0 means the old commit's content is preserved in current history.
- `git fsck --lost-found` → dangling commits are expected: they're rebase-orphans (same commit message exists on the main line under a new SHA) plus git stash/autostash internals (`"On master: temp"` / `"On master: autostash"`). All harmless.
- **Only escalate if fsck shows a dangling commit with unique work and no same-message twin on `origin/master`.**

This is why hash-pins in state files decay within 2-3 commits — same root cause (see [[feedback_behavior_language_over_hash_pinning]]). Use behavior-language ("clean, synced to origin"), not SHA pins. First diagnosed when Will flagged a `791e71da→85b55b20` "forced update" on master 2026-06-03; trace showed clean fast-forward push + all dangling commits accounted for.
