---
name: git-crash-object-corruption-recovery
description: "Crash mid-commit truncates the tip commit + its new objects to zero bytes → all git ops fail with 'object file is empty' / 'bad object HEAD'. Fix: restore the branch ref to the last COMPLETE reflog entry (after verifying it walks clean), quarantine the empties. Working-tree files are never lost — only .git metadata."
metadata:
  node_type: memory
  type: finding
  originSessionId: b45cd14c-62a9-4304-b4d0-5ca7880a0397
---

A hard crash (power loss, WSL kill) during a `git commit` can truncate the just-written loose objects to **zero bytes**. Git writes a commit as blobs → trees → commit object, then updates the branch ref; a crash before the OS flushes leaves the whole batch as empty files while `refs/heads/<branch>` already points at the (now zero-byte) tip commit. Result: **every git command fails fleet-wide** with `error: object file .git/objects/xx/… is empty` and `fatal: bad object HEAD`. This blocks ALL agents on the shared clone, not just the one that crashed.

**The reassuring core fact:** the damage is confined to `.git` metadata. **Your working-tree files are intact on disk** — the crash didn't touch your edits. Even the *crashed commit's own file content* survives in the working tree and is re-committable. Nothing in completed history is lost. Don't panic-reset to origin.

**Diagnosis (all read-only — do these FIRST, before touching anything):**

1. `find .git/objects -type f -size 0` — enumerate every zero-byte object. Typically the dead tip commit + its handful of new trees/blobs (≈3–6 files), all from the one interrupted commit.
2. `cat .git/refs/heads/<branch>` (or `grep <branch> .git/packed-refs`) — confirm the ref points at one of those zero-byte SHAs. That confirms "dead tip," the benign case.
3. `tail .git/logs/HEAD` — the reflog is **plain text and survives object corruption.** Its last COMPLETE entry's *new* SHA is your last-good commit. (`.git/logs/refs/heads/<branch>` is the per-branch twin.)
4. `cat .git/COMMIT_EDITMSG` — also plain text; **recovers the crashed commit's intended message** so you know exactly WHAT died and who owns it.
5. **CRITICAL gate — prove the corruption is confined before repairing.** Walk the last-good commit's entire object graph:
   `git rev-list --objects <lastgood> | awk '{print $1}' | git cat-file --batch-check` — any `missing`/error line = corruption reaches good history (a much bigger problem; stop and escalate). A clean walk (empty stderr, every object typed) = the dead tip is unreachable garbage and safe to drop.
6. `git merge-base --is-ancestor origin/master <lastgood>` — confirm you're a clean fast-forward ahead (you may be hundreds of commits ahead of origin; **never** "fix" by resetting to origin or you lose all unpushed work).

**Repair (only after step 5 confirms good history is clean):**

1. `git update-ref refs/heads/<branch> <lastgood>` — surgical. Restores a valid HEAD without touching the index or working tree. (`git rev-parse HEAD` should now resolve.)
2. **Quarantine, don't hard-delete** the zero-byte objects — `mkdir` a backup dir and `mv` them there (reversible; they're empty so this is just hygiene). Some may already be gone after the ref move.
3. Verify: `git status` works again + `git fsck --full` reports **zero** error/corrupt/empty/missing lines (dangling objects are normal). Fleet is unblocked.

**Gotchas:**
- **Never `git reset --hard`** (discards the working tree = your actual recovered work) and **never reset to origin** when ahead. `update-ref` to the last-good reflog SHA is the whole fix.
- A `git fsck` cache-tree warning (`invalid sha1 pointer in cache-tree of .git/index`) is harmless — git recomputes it on the next index write.
- After repair, a **pathspec commit unstages other staged files** as a side-effect ([[finding_pathspec_commit_race_safety]]); content stays on disk, just re-`git add` when re-committing.

**Validated:** 2026-06-22 (SAM session, this repo). Crash during a Will-authorized BRENT inbox commit truncated tip `002e726f` + 4 objects to 0 bytes; `refs/heads/master` was restored to last-good `45f07e75` (CARL commit, per `.git/logs/HEAD`); the dead-tip graph never referenced good history (step-5 walk clean), so **775 local commits + the full SAM v1.6 finalize were recovered with zero data loss.** The crashed commit's file (`AGENTS/BRENT/inbox/2026-06-18_from-HAWK_…`) was intact on disk for re-commit.

Cross-agent transferable to ANY agent on the shared clone. **Should propagate to root `CLAUDE.md` Git Protocol** as the standard crash-recovery runbook — flag to PROME (don't edit the shared file directly; [[feedback_agent_git_isolation]]). Related: [[finding_two_machine_partition_clean_merge]], [[feedback_defer_push_coordinate]], [[finding_concurrent_commit_index_race]].
