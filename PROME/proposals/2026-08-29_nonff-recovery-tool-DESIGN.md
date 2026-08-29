# Non-ff recovery tool — DESIGN for RAV review (no code wired)

**Owner:** PROME · **Written:** 2026-08-29 · **Status:** DESIGN ONLY — RAV reviews before any code enters the operational path (RAV qualification on F4, Will-endorsed 8/29). `scripts/safe-push.sh` stays push-only and non-mutating; nothing here touches it.

## 1. What this replaces

Root `CLAUDE.md` Git Protocol, closeout step 3: on a non-ff abort, `git pull --rebase --autostash` then re-push, with a prose instruction to "check first that incoming commits don't touch the dirty paths." The check is prose; the rebase mutates a worktree that may hold other sessions' uncommitted files. RAV (8/29): the overlap check is valuable but does not make `--autostash` fully safe — fetch-first, porcelain parsing, staged+unstaged coverage, and the check-to-rebase race all remain.

## 2. Invariants the tool must hold

| # | Invariant | How |
|---|---|---|
| I1 | **`safe-push.sh` never pulls, never mutates** | recovery lives in a separate script, `scripts/nonff_recover.sh` (name TBD by RAV); safe-push only PRINTS the recovery command on rc=1 |
| I2 | **Compare against a FRESH fetch** | step 1 is `git fetch origin` (fail → stop, rc 2 UNKNOWN); incoming set = `git diff --name-only HEAD...origin/master` (three-dot, merge-base) computed AFTER the fetch |
| I3 | **Dirty inventory covers staged + unstaged + untracked tracked-dir files** | `git status --porcelain=v2 -z --untracked-files=all` (v2 + NUL: renames carry both paths explicitly, filenames with spaces/newlines are safe); `-z` parsing only, never line-split v1 |
| I4 | **Refuse on intersection** | `dirty ∩ incoming ≠ ∅` → rc 1, print both sides, print nothing else. No "it's probably fine" branch |
| I5 | **Refuse on unknown state** | in-progress rebase/merge/cherry-pick (`.git/REBASE_HEAD`, `MERGE_HEAD`, `CHERRY_PICK_HEAD`, `rebase-merge/`, `rebase-apply/`), detached HEAD, branch ≠ master, upstream ≠ origin/master, stash list non-empty from a prior autostash → rc 2, name the state |
| I6 | **Refuse on rename ambiguity** | any porcelain v2 `2` (rename/copy) entry in the dirty set → rc 2 (an autostash of a half-renamed file is the class we cannot round-trip-verify) |
| I7 | **Bound the check→rebase race** | snapshot `git status --porcelain=v2 -z` bytes + `git rev-parse origin/master` immediately before the rebase and immediately after; any difference → rc 1 with the diff printed. This does not ELIMINATE the race (RAV is right: nothing user-space can); it makes it DETECTED, which is the property we can actually have |
| I8 | **Two modes, explicit** | default = `--dry-run` (compute, print the verdict and the exact recovery command, exit); `--apply` performs the rebase ONLY if every check passed in the same invocation. No env var, no "yes" prompt — the flag is the record |
| I9 | **Autostash round-trip verified** | with `--apply`: hash every dirty file's content before (`git hash-object` for tracked, sha256 for untracked) and after `stash pop`; mismatch → rc 1, stash left IN PLACE (never dropped), stash ref printed |
| I10 | **Own commits only travel** | pre-check: `git log origin/master..HEAD --format=%an` must be a single author = this session's `git config user.name`; otherwise rc 2 — a rebase of someone else's unpushed commits is not this tool's business |

## 3. Flow

```
nonff_recover.sh [--apply]
 1. state checks (I5, I10)                     → rc 2 on any hit
 2. git fetch origin                            → rc 2 on failure
 3. incoming = diff --name-only HEAD...origin/master
 4. dirty    = status --porcelain=v2 -z (I3, I6)
 5. if dirty ∩ incoming: print both, rc 1 (I4)
 6. print verdict + the exact command it WOULD run; --dry-run exits 0 here
 7. --apply: snapshot A (I7) → hash dirty (I9) → git rebase --autostash origin/master
             → snapshot B; A≠B → rc 1 → hash compare → mismatch → rc 1, stash kept
 8. print "recovered — now run scripts/safe-push.sh" (the tool NEVER pushes)
```

## 4. What it does NOT do (by design)

- Never pushes. Never drops a stash. Never `--amend`. Never resolves conflicts (a conflict mid-rebase → `git rebase --abort` is printed, not run — the user decides; the autostash is re-applied by git's abort path).
- Does not make per-agent branches unnecessary. It narrows the window and makes every failure loud; RAV's architectural point stands and stays on the record (`PROME/AUTONOMY.md` escalation tripwire unchanged).

## 5. Tests (committed fixtures, before wiring)

1. Clean tree, incoming disjoint → dry-run 0, apply 0, round-trip hashes equal.
2. Dirty file ∈ incoming → rc 1, nothing mutated (tree hash before == after).
3. Rename in dirty set → rc 2.
4. In-progress rebase dir present → rc 2.
5. Foreign-author unpushed commit → rc 2.
6. Race simulation: background writer touches a dirty file between snapshot A and B → rc 1, stash present, printed.
7. Negative control: break the intersection check → test 2 must FAIL.

## 6. Root-canon consequence (Will-gated, later)

If adopted, root Git Protocol step 3 changes from "run `git pull --rebase --autostash`" to "run `scripts/nonff_recover.sh` (dry-run first; `--apply` on a clean verdict)". One line; carried under WQ-120's rules-vs-provenance split or as its own row — RAV's call at review.

## 7. Ask of RAV

Review invariants I1–I10 and the test list; name any state the tool can reach that is neither refused nor verified. PROME builds only after that review.
