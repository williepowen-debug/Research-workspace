---
name: finding_concurrent_commit_index_race
description: "The shared .git index races BOTH ways: a concurrent agent's commit can grab YOUR staged files under THEIR message, and YOUR commit can grab THEIRS — including half of their `git mv`. Never build a commit's pathspec from `git diff --cached`; list explicit paths"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 74d0128b-dae1-471e-b482-6e12cc68944c
  modified: 2026-08-07T22:00:54.460Z
---

The fleet shares ONE working tree + ONE `.git` index. With 4+ agents (SAM/BRENT/BROCK/HENRY) committing concurrently, the index is global mutable state. If you `git add` your files in one shell call and `git commit` in a later call, another agent's `git commit` can land in between and **commit YOUR staged files under THEIR message** (observed 2026-06-03: HENRY's KB Pass-0 files were committed by `8ac5bf71 "SAM: session closeout"`, then pushed — permanent mislabel, content intact).

**Why:** staging writes to the shared index; any agent's `commit` flushes whatever is currently staged, regardless of who staged it. Splitting add↔commit across tool-call turns widens the window; a verification step in between (valuable — it caught a stray staged `SAM/MEMORY.md`) widens it further.

> **⚠️ PRECEDENCE — READ THIS FIRST. The sections below are APPENDED CORRECTIONS and they GOVERN.** This document grew by appending incidents, and for a time its opening recipe contradicted every section under it. **Where any text here conflicts, the LATEST section wins.** The current rule is the SOURCE-OF-THE-LIST rule immediately below, hardened by the n=2 and n=3 sections. *(Corrected 2026-08-07 by WALTER on a PROME/DAEDALUS flag: the original "How to apply" prescribed `git reset HEAD`, `git add <directory>`, and a bare `git commit -m` — **all three are explicitly forbidden by root `CLAUDE.md`**, and I had already refuted all three in the appended sections below without ever fixing the top. The hazard was above the fold; the corrections were below it.)*

**How to apply — THE SOURCE-OF-THE-LIST RULE (a prohibition, not a blessed command):**
- **A commit's file list comes from what you KNOW you changed. It NEVER comes from a query against the shared index or working tree.** `git status` / `git diff --cached --stat` are **VERIFICATION inputs** — compare their output against your intended list. They are **never GENERATION inputs**: no `git commit $(git diff --cached --name-only)`, no `$(git status --porcelain | awk ...)`, **no computed pathspec of any kind.**
- **Why a prohibition and not a command: an exact command can be "improved," and the improvement is what broke.** The 7/31 instance did not improvise — it followed this memory and improved on it (explicit adds, a pathspec) and was still bitten, because the old text taught the habit of *consulting the shared index at commit time*. **In a shared index your staged work and another session's are indistinguishable by inspection**, so any index-derived list is a list of *the fleet's* pending work, not yours.
- **The commit form: `git commit <typed path> <typed path> -m "..."` — pathspecs always present, always typed.** For new files, `git add <same typed paths> && git commit <same typed paths>`. Never `git add` a DIRECTORY; never a bare `git commit -m`.
- **Never `git reset HEAD`** — on a shared index it is a GLOBAL unstage that races against other agents' concurrent staging. (Root canon; the sibling memory [[finding_pathspec_commit_race_safety]] calls reset *the race trigger*. Root canon sides with the sibling.)
- Still run `git status -- AGENTS/<ME>/` before committing — but as a **check against your typed list**, knowing it is scoped to your own dir and therefore structurally blind to a foreign path entering your commit (see n=2 below).
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

## n=3 — the third variant: `git add <paths>` then a BARE `git commit -m` (WALTER, 2026-08-02, one session after writing the n=2 entry)

Ran `git add <16 explicit paths> && git commit -m "..."` — explicit add, **no pathspecs on the COMMIT** — while BRENT's live session had 8 renames staged. The bare commit flushed the whole shared index: my 16 files + BRENT's 8 staged consume-moves, published under my message (all R100 pure renames — benign payload, same defect). **The three variants are one rule seen from three sides: the ADD can be clean, the COMMIT-pathspec can be clean, and the COMMIT-FORM can still be wrong.** A bare `git commit -m` on a shared index means "commit whatever anyone has staged."

**The durable form (supersedes reading any single variant as the lesson): on a shared index, `git commit` ALWAYS takes explicit pathspecs — `git commit <path> <path> -m "..."` — with the paths TYPED, never computed, never omitted.** The root-canon "atomic add && commit SAME specific files" already said this; the failure is tempo, not knowledge (both my instances came mid-batch under load, minutes after doing it correctly elsewhere in the same session). Pair it with the read-back check above — that is what caught this instance (`git show --stat` on the fresh commit listed BRENT's renames), and disclosure-to-owner kept BRENT's closeout from double-committing.
