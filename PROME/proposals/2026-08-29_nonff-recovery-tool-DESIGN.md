# Non-ff recovery tool — DESIGN v3 for RAV review (no code wired)

**Owner:** PROME · **v1:** 2026-08-29 (RAV pass 1: *"does not pass yet"* — five blocking defects) · **v2:** 2026-08-29, pass-1 defects addressed `[RAV-1.n]` · **v3:** 2026-08-29, RAV pass 2 *"not ready to build"* — three mechanical defects addressed `[RAV-2.n]` (§0b). **Status:** DESIGN ONLY — no code until RAV passes it. `scripts/safe-push.sh` stays push-only and non-mutating; nothing here touches it.

## 0. What changed from v1 (RAV pass 1 → v2)

| RAV-1 | Defect | v2 disposition |
|---|---|---|
| 1 | incoming set via three-dot `git diff` did not parse upstream renames — a dirty OLD path evades intersection when upstream renames it | explicit merge-base + `--name-status -z`, BOTH sides of R/C entries join the incoming set (§2 I2) |
| 2 | I10 "own commits only" contradicts the push-train (one closeout sweeps many agents' commits; `user.name` does not identify a session) | I10 REPLACED: enumerate the complete local-only commit set before, account for the same logical commits after, by patch-id (§2 I10) |
| 3 | I9 cannot promise "stash left in place" — `rebase --autostash` owns the stash lifecycle and drops it on success before any external check; content hashes miss deletions, modes, symlinks, staged-vs-unstaged, submodules | `--autostash` DROPPED. The tool creates its own safety objects BEFORE mutation: an index tree, a worktree tree, and a recorded ref; verification compares trees (mode + type + deletions included), not file hashes; staged/unstaged separated; submodules → refuse (§2 I9, §3) |
| 4 | I7 "race detected" overstated — a before/after porcelain diff cannot recover bytes overwritten mid-operation | renamed **post-operation integrity ALARM**; the interval is closed only by a concurrent-writer lock or isolated worktree — v2 adds a best-effort lock AND names the residual honestly (§2 I7) |
| 5 | "any nonempty stash list" is not an unknown state — an unrelated user stash would disable recovery forever | refuse only on a recovery-OWNED unresolved ref under `refs/prome/recovery/`; unrelated stashes are REPORTED, never blocking (§2 I5) |

## 0b. What changed from v2 (RAV pass 2 → v3)

| RAV-2 | Defect | v3 disposition |
|---|---|---|
| 1 | `GIT_INDEX_FILE=tmp git add … && git write-tree` — the env var scoped only to `git add`; `write-tree` read the REAL index; the temp index was never seeded | one exported temp index across BOTH commands, seeded from the real index (`cp .git/index $TMP` — or `git read-tree HEAD` when the index is unusable), dirty paths overlaid with `git add -A -- <dirty>` (deletions included), `write-tree` against the SAME temp index (§2 I9). **Negative control added: an unstaged change must yield `WT != IDX`** (test 14) |
| 2 | "record the stash id in the same recovery ref" — commit objects are immutable | explicit **two-manifest transition**: manifest-1 (pre-state) → stash → manifest-2 (parent = manifest-1, carries stash id) → `git update-ref` atomically moves `refs/prome/recovery/<ts>` from manifest-1 to manifest-2 (§2 I9, §3 steps 7–8). Pre-state objects stay reachable at every crash point because the ref always points at a commit whose ancestry includes manifest-1. Crash-point fixtures between every object/ref transition (tests 15a–15d) |
| 3 | patch-ids do not cover merges, empty commits, unclassifiable diffs, duplicates, or topology changes | **refuse with rc 2** on any local-only merge commit, empty commit, or commit with no usable patch-id (typed manifest classifies each: `PATCH` · `MERGE` · `EMPTY` · `NOPATCH`); otherwise verify the ORDERED list of patch-ids with multiplicity (duplicates are legal and must match count-for-count). A missing patch-id after rebase is never treated as ordinary (§2 I10) |

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
| I9 | **Safety objects BEFORE mutation; tree-level verification AFTER** `[RAV-1.3]` `[RAV-2.1]` `[RAV-2.2]` | **Trees:** `export GIT_INDEX_FILE=$(mktemp)`; seed it: `cp "$(git rev-parse --git-path index)" "$GIT_INDEX_FILE"` (fallback `git read-tree HEAD` if the copy is unusable); `IDX=$(git write-tree)` (= staged state, from the seeded temp index before overlay); then `git add -A -- <dirty paths>` (adds, modifications, deletions, untracked-in-dirty-set, modes, symlinks as blobs) and `WT=$(git write-tree)` — both `write-tree` calls run under the SAME exported temp index; `unset GIT_INDEX_FILE` afterwards. Sanity: if any dirty path is unstaged-modified, require `WT != IDX` else rc 2 (the tool refuses to certify a tree it cannot distinguish). **Manifests:** manifest-1 = `git commit-tree $WT -p HEAD -m <json: IDX, WT, HEAD, origin/master, typed local-commit list>`; `git update-ref refs/prome/recovery/<ts> $M1`. After the explicit stash exists (step 8): manifest-2 = `git commit-tree $WT -p $M1 -m <json: + stash_id>`; `git update-ref refs/prome/recovery/<ts> $M2 $M1` (compare-and-swap on the old value — atomic; failure ⇒ rc 2, nothing else mutated). Pre-state objects are reachable from the ref at every point. **After** rebase + `git stash apply <id>` + `git read-tree $IDX` (restores staged/unstaged split): recompute `IDX'`, `WT'` the same way; require both tree ids equal. Mismatch ⇒ rc 1, ref + stash KEPT, `git diff-tree $WT $WT'` printed. No `--autostash` anywhere |
| I10 | **Local-only commit set typed, accounted for, never single-authored** `[RAV-1.2]` `[RAV-2.3]` | Before: `git rev-list --reverse origin/master..HEAD`; classify each: `MERGE` (≥2 parents) · `EMPTY` (`git diff-tree --quiet` true) · `NOPATCH` (`git patch-id --stable` emits nothing) · `PATCH` (sha, patch-id, subject). **Any MERGE / EMPTY / NOPATCH ⇒ rc 2** — these are not rebased by this tool (recipe printed: resolve by hand or wait for the owner). Otherwise the manifest stores the ORDERED list of patch-ids WITH multiplicity. After rebase: recompute over `origin/master..HEAD`; require identical ordered list, count-for-count. A patch-id absent after rebase is reported as "already upstream" ONLY if that exact patch-id exists in `$base..origin/master`; otherwise rc 1. No commit is ever treated as ordinary by default |
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
    (manifest-2 with stash id; update-ref CAS M1→M2)
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
14. **`WT != IDX` when an unstaged change exists** — file modified but not staged ⇒ the two tree ids differ; file staged ⇒ equal `[RAV-2.1 negative control — without it equal before/after trees could certify the wrong tree twice]`.
15. **Crash points** (process killed by the fixture) `[RAV-2.2]`: 15a after manifest-1 written, before update-ref ⇒ objects dangling but no ref, tool reports "no recovery in progress" and the pre-state is recoverable by hand from reflog; 15b after ref→M1, before stash ⇒ next run: rc 2 recovery-owned ref, pre-state trees readable from M1; 15c after stash, before ref→M2 ⇒ next run: rc 2, stash object findable via `git fsck --unreachable` recipe printed; 15d after ref→M2, before rebase ⇒ next run: rc 2, full recovery recipe (checkout WT, read-tree IDX, stash apply) printed from M2's manifest.
16. **Typed local set** `[RAV-2.3]`: a local merge commit ⇒ rc 2; an `--allow-empty` commit ⇒ rc 2; two local commits with identical patch-ids ⇒ pass only if both survive (count 2 → 2).

## 6. Root-canon consequence (Will-gated, later)

If adopted, root Git Protocol step 3 changes from "run `git pull --rebase --autostash`" to "run `scripts/nonff_recover.sh` (dry-run; `--apply` on a clean verdict)". One line; carried under WQ-120's apply or its own row.

## 7. Ask of RAV (pass 3)

Check I9 (single exported temp index seeded from the real index; two-manifest CAS transition; WT≠IDX control) and I10 (typed local set, MERGE/EMPTY/NOPATCH refused, ordered multiplicity). Name any object/ref transition without a crash fixture, and any local-commit shape the typed manifest still cannot classify.
