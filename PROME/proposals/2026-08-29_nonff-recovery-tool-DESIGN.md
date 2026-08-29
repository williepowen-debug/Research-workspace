# Non-ff recovery tool — DESIGN v2 for RAV review (no code wired)

**Owner:** PROME · **v1:** 2026-08-29 (RAV pass 1: *"does not pass yet"* — five blocking defects) · **v2:** 2026-08-29, every pass-1 defect addressed below and marked `[RAV-1.n]`. **Status:** DESIGN ONLY — no code until RAV passes it. `scripts/safe-push.sh` stays push-only and non-mutating; nothing here touches it.

## 0. What changed from v1 (RAV pass 1 → v2)

| RAV-1 | Defect | v2 disposition |
|---|---|---|
| 1 | incoming set via three-dot `git diff` did not parse upstream renames — a dirty OLD path evades intersection when upstream renames it | explicit merge-base + `--name-status -z`, BOTH sides of R/C entries join the incoming set (§2 I2) |
| 2 | I10 "own commits only" contradicts the push-train (one closeout sweeps many agents' commits; `user.name` does not identify a session) | I10 REPLACED: enumerate the complete local-only commit set before, account for the same logical commits after, by patch-id (§2 I10) |
| 3 | I9 cannot promise "stash left in place" — `rebase --autostash` owns the stash lifecycle and drops it on success before any external check; content hashes miss deletions, modes, symlinks, staged-vs-unstaged, submodules | `--autostash` DROPPED. The tool creates its own safety objects BEFORE mutation: an index tree, a worktree tree, and a recorded ref; verification compares trees (mode + type + deletions included), not file hashes; staged/unstaged separated; submodules → refuse (§2 I9, §3) |
| 4 | I7 "race detected" overstated — a before/after porcelain diff cannot recover bytes overwritten mid-operation | renamed **post-operation integrity ALARM**; the interval is closed only by a concurrent-writer lock or isolated worktree — v2 adds a best-effort lock AND names the residual honestly (§2 I7) |
| 5 | "any nonempty stash list" is not an unknown state — an unrelated user stash would disable recovery forever | refuse only on a recovery-OWNED unresolved ref under `refs/prome/recovery/`; unrelated stashes are REPORTED, never blocking (§2 I5) |

## 1. What this replaces

Root Git Protocol, closeout step 3: on non-ff, `git pull --rebase --autostash` then re-push, with a prose instruction to check that incoming commits don't touch dirty paths. The check is prose and the autostash mutates a worktree that may hold other sessions' uncommitted files.

## 2. Invariants (v2)

| # | Invariant | How |
|---|---|---|
| I1 | **`safe-push.sh` never pulls, never mutates** | recovery = separate `scripts/nonff_recover.sh`; safe-push only PRINTS the recovery command on rc=1 |
| I2 | **Incoming set from a fresh fetch, rename-complete** `[RAV-1.1]` | `git fetch origin` (fail → rc 2) · `base=$(git merge-base HEAD origin/master)` · `git diff --name-status -z -M -C "$base..origin/master"` parsed NUL-wise; for `R`/`C` entries BOTH old and new paths enter `incoming` |
| I3 | **Dirty inventory = staged + unstaged + untracked, rename-aware** | `git status --porcelain=v2 -z --untracked-files=all`; entry types `1`,`2` (both paths),`?`; `u` (unmerged) → rc 2 |
| I4 | **Refuse on intersection** | `dirty ∩ incoming ≠ ∅` → rc 1, print both sides; no override flag exists |
| I5 | **Refuse on unknown state — precisely** `[RAV-1.5]` | rc 2 on: in-progress rebase/merge/cherry-pick/bisect (`rebase-merge/`, `rebase-apply/`, `MERGE_HEAD`, `CHERRY_PICK_HEAD`, `BISECT_LOG`); detached HEAD; branch ≠ `master` or upstream ≠ `origin/master`; any unmerged index entry; any submodule present (`.gitmodules` or gitlink `160000` in `ls-files -s`); **an unresolved recovery-owned ref `refs/prome/recovery/*`** (a prior run that did not reach step 9). Unrelated `stash@{n}` entries are LISTED in the report and do not block |
| I6 | **Refuse on rename ambiguity in the DIRTY set** | any porcelain-v2 `2` entry → rc 2 (a half-renamed file is the class whose round-trip we cannot certify) |
| I7 | **Post-operation integrity ALARM, not race prevention** `[RAV-1.4]` | Best-effort **lock**: create `.git/prome_recovery.lock` (O_EXCL, holds pid + timestamp; stale after 10 min → rc 2, never auto-cleared). The lock is honoured only by this tool and `commit_check.py`/`safe-push.sh` (they refuse while it exists) — other sessions' plain `git` and editors are NOT bound by it, so the check→rebase interval is **narrowed, not closed**. After the operation, tree comparison (I9) is the alarm: any drift → rc 1 with the diff. Closing the interval fully = per-agent worktrees/branches (the standing architectural tripwire); this tool does not claim to |
| I8 | **Two explicit modes** | default `--dry-run`: compute, print verdict + the exact `--apply` command, exit. `--apply` performs the operation only if every check passed in THIS invocation. No env var, no prompt |
| I9 | **Safety objects BEFORE mutation; tree-level verification AFTER** `[RAV-1.3]` | Before: `IDX=$(git write-tree)` (staged state); `WT=$(GIT_INDEX_FILE=tmp git add -A -- <dirty paths> && git write-tree)` (worktree state incl. untracked-in-dirty-set, modes, symlinks as blobs, deletions as absence); record both + HEAD + `origin/master` + the local-only commit list in **`refs/prome/recovery/<UTC-ts>`** (a commit object whose message carries the manifest, parented on HEAD — reachable, never GC'd until step 9 deletes it). After: recompute `IDX'`, `WT'`; require `IDX == IDX'` and `WT == WT'` byte-for-byte as tree ids (mode, type, path, content, deletions all inside the id). Mismatch → rc 1, the ref STAYS, the report prints `git diff-tree $WT $WT'`. No `--autostash`: the tool itself does `git stash push --include-untracked -- <dirty paths>` ONLY under `--apply`, records the stash commit id in the same recovery ref, rebases, then `git stash apply <id>` (apply, not pop — the stash object is kept until step 9 verifies). Staged vs unstaged preserved by restoring `IDX` via `git read-tree` after apply |
| I10 | **Local-only commit set accounted for, not single-authored** `[RAV-1.2]` | Before: `git rev-list --reverse origin/master..HEAD` → list of (sha, patch-id via `git patch-id --stable`, subject). After rebase: recompute over `origin/master..HEAD`; require the multiset of patch-ids to be identical and in the same order. Any patch-id missing (a commit silently dropped as "already upstream" is REPORTED, since that is legitimate when origin already has it — the tool distinguishes it by checking the patch-id exists in `$base..origin/master`) or any extra → rc 1 |
| I11 | **The tool never pushes** | final line prints `now run scripts/safe-push.sh`; nothing else |

## 3. Flow (`--apply`; `--dry-run` stops after step 6)

```
 1. lock (I7)                                      → rc 2 if held/stale
 2. state checks (I5, I6)                          → rc 2
 3. git fetch origin                               → rc 2 on failure
 4. base = merge-base; incoming = name-status -z -M -C base..origin/master (I2)
 5. dirty = porcelain v2 -z (I3); local_commits = rev-list + patch-ids (I10)
 6. dirty ∩ incoming ≠ ∅ → rc 1 (I4); else print verdict + apply command
 7. safety objects: IDX, WT trees; recovery ref with manifest (I9)
 8. stash push --include-untracked -- <dirty>; record stash id in the ref
    git rebase origin/master            (conflict → print `git rebase --abort` +
                                          `git stash apply <id>`; NOT run; ref stays; rc 1)
    git stash apply <id>; git read-tree IDX (restore staged state)
 9. verify: IDX'==IDX, WT'==WT (I9); patch-id multiset (I10)
    pass → delete refs/prome/recovery/<ts>, drop the stash object, release lock, rc 0
    fail → ref + stash KEPT, lock released, rc 1, diff printed
10. print "recovered — now run scripts/safe-push.sh" (I11)
```

## 4. Residuals stated plainly (RAV — these are the claims I am NOT making)

- The check→mutation interval is narrowed by the lock, not closed; a session that ignores the lock can still write into it. Detection is after the fact (I7). Closing it requires per-agent worktrees/branches.
- Recovery objects make the pre-state RECOVERABLE (`git checkout $WT -- .`, `git read-tree $IDX`); they do not make the operation atomic.
- Untracked files OUTSIDE the dirty set are untouched by design and therefore unverified — the tool only certifies what it stashed.
- A rebase conflict is never resolved by the tool; it stops with the abort recipe printed and the recovery ref intact.

## 5. Tests (committed fixtures, before wiring)

1. Clean tree, disjoint incoming → dry-run 0; apply 0; `IDX==IDX'`, `WT==WT'`; recovery ref deleted.
2. Dirty file ∈ incoming → rc 1; tree ids unchanged; no ref created.
3. **Upstream RENAMES a file that is dirty locally under the OLD name** → rc 1 `[RAV-1.1 fixture]`.
4. Rename in the dirty set → rc 2.
5. In-progress rebase dir present → rc 2.
6. **Two authors in the local-only set (push-train shape)** → passes; patch-id multiset identical after rebase `[RAV-1.2 fixture]`.
7. Local commit already present upstream (identical patch-id) → reported as "dropped: already upstream", rc 0.
8. Unrelated `stash@{0}` present → listed, does not block `[RAV-1.5 fixture]`.
9. Recovery-owned ref left from a simulated aborted prior run → rc 2 until cleared by hand.
10. Staged-vs-unstaged split (file A staged, file B unstaged) → identical split after apply.
11. Executable bit + symlink + deleted-tracked-file in the dirty set → tree ids equal after apply `[RAV-1.3 fixture]`.
12. Background writer modifies a dirty file between steps 7 and 9 → rc 1, ref + stash kept, diff printed `[RAV-1.4 fixture — alarm, not prevention]`.
13. Negative control: disable the intersection check → test 2 must FAIL; disable tree verification → test 12 must FAIL.

## 6. Root-canon consequence (Will-gated, later)

If adopted, root Git Protocol step 3 changes from "run `git pull --rebase --autostash`" to "run `scripts/nonff_recover.sh` (dry-run; `--apply` on a clean verdict)". One line; carried under WQ-120's apply or its own row.

## 7. Ask of RAV (pass 2)

Check I2 (rename parsing), I9 (tree-id verification replaces hashes; explicit stash + recovery ref replaces autostash), I10 (patch-id multiset replaces single-author), I7 (alarm + best-effort lock, residual stated) and I5 (recovery-owned refs only). Name any state still neither refused nor verified.
