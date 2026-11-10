# Git Coordination

**Owner:** Prome  
**Status:** Live coordination rail · **Updated:** 2026-11-09 (Will 22:27 ET: bounded cleanup; retired YEYOU material and superseded recipe text moved to `PROME/archive/GIT_COORDINATION_2026-11-09_pre-cleanup.md`; no Git rule or authority changed; record `PROME/proposals/2026-11-09_git-guide-cleanup-RULED.md`). Earlier edits: `git log -p -- PROME/GIT_COORDINATION.md`.
**Scope:** every agent operating in this shared repo/worktree (fleet size → `PROME/ROSTER.md`).

## Purpose

Keep concurrent agent runtimes from clobbering one another through shared-index git operations, stale Prome paths, or unsafe pushes. *(Agents may run under different supported runtimes; identity, ownership and Git rules are unchanged. Operation is **serial multi-machine** — Will runs one box at a time, desktop ⇄ laptop, close-out-push before switching; OpenClaw/VPS was cut 2026-06-26. Machine-local inventory → `PROME/MACHINE_LOCAL.md`.)*

This doc is the live coordination surface (vs the archived `AGENTS/PROME/` tree); **root `CLAUDE.md` Git Protocol is canon** — this doc mirrors it and adds the PROME cookbook (per `SYSTEM.md` Canonical→Mirrors). The old `AGENTS/PROME/` tree is archived at `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/` and is not live intake, boot, or git protocol.

## Hard Rules

- Run repo-state checks before sync or write work: `git status --short`, staged paths, and ahead/behind.
- Never use broad index operations: no `git add .`, no `git add -A`, no `git reset HEAD`, no force-push, no broad checkout. **Never `git commit --amend`** (root Git Protocol 4b: amend rewrites whoever holds HEAD, which may not be you). Write EVERY message via quoted-heredoc `git commit -F <file>`, never inline `-m`; an inline `-m` in any recipe is subject-line shorthand.
- Dirty tree means inspect and triage. Do not stash, reset, or pull to make the dirt disappear.
- Use explicit pathspecs for adds and commits.
- Local scoped commits use explicit pathspecs; **push is automated at closeout via `scripts/safe-push.sh`** (ff-gated, fails safe; serial multi-machine predicate). **Auto-push exceptions (full list, root canon):** TERRY self-sweeps · WALTER architectural per `BOARD_CONSUMPTION_SPEC` §7 (see Push Discipline).
- No trade execution or external/public sends are authorized by this document.

## Ownership

### Prome

Live Prome state lives in root `PROME/`.

Prome may write:

- Root `PROME/` owner docs.
- `HEARTBEAT.md` and `FORGE/` — PROME-standard commits (freed 8/23 and 7/30; explicit-path, never swept blind). `memory/auto/` files PROME authored — MANDATORY self-commit (carve-out ③ below); daily `memory/YYYY-MM-DD.md` = standard closeout set.
- Explicitly scoped integration/archive paths approved by Will.

Prome must not treat archived `AGENTS/PROME/` files as live instructions.

**Cross-dir carve-outs (root canon ①–⑤ — mirror re-synced 2026-08-29 audit #11, ⑤ added 2026-10-29 audit #18):**
- **① Self-authored inbox packets (ratified 2026-07-23 — HENRY orphan-gap memo):** a packet **PROME authored** into another agent's `inbox/` is PROME's to commit, **and PROME must** — an uncommitted packet never reaches the recipient (~12% orphaned this way pre-detector). Commit it explicitly-pathed with the recipient named in the subject (`PROME -> <RECIPIENT>: <what>`).
- **② Self-authored shared-log rows (ratified 2026-07-25):** a row PROME authored in a shared cross-agent log (`AGENTS/SIGNALS.md` class) is PROME's to commit, explicitly path-scoped. Rows other agents wrote and file restructures stay off-limits.
- **③ Self-authored auto-memory files (ratified 2026-07-27, MANDATORY):** any memory file under `memory/auto/` that PROME authored or appended MUST be self-committed — the shared `MEMORY.md` index row rides out on whoever commits next while the FILE needs a deliberate add, so an uncommitted memory leaves the index advertising content the other machine doesn't have (worse than the memory not existing). Enforcement at closeout: `python3 scripts/memory_index_check.py --strict --slug <slug>` per memory written — **the `--slug` form, never bare `--strict`** (bare gates the whole index and blocks on OTHER agents' orphans ③ forbids PROME to commit).

- **④ Gate C Kernel — root's domain-agent SUBMISSION carve-out (window-gated: a Will-ruled window naming the desk) plus, SEPARATELY, PROME's custody grant (root's paragraph after the numbered carve-outs, not a numbered one), which needs an operator-activated packet:** under an approved activation PROME is the sole acceptance custodian for `KERNEL/shadow/events/`, `KERNEL/audit/commands/`, the four registered `KERNEL/views/` projections and the sitting's governance records — additions-only, exact pathspecs, never a directory. Domain agents may commit only their own `AGENTS/<NAME>/outbox/kernel/submissions/<command_id>.json`. Full text = root Git Protocol ④ + the custody paragraph (reconciled 8/27 C8).
- **⑤ Self-authored FORUM posts** (WQ-486 A, Will 2026-10-24) — root carve-out ⑤: a standing-bucket post **you authored** (`FORUM/<bucket>/<stamp>_<YOU>_<slug>.md`) is yours to commit, explicitly pathed, and only that file; no other `FORUM/` file.

Someone else's work outside `PROME/` remains strictly off-limits. Root `CLAUDE.md` Git Protocol owns the full carve-out text; on any drift, root wins.

**Session-end orphan check (root canon step 1b, adopted 2026-07-23):** before the closeout commit batch, run `bash scripts/orphan_check.sh PROME` — read-only advisory (~5s, exit 0 always). `[likely YOURS]` = packets PROME authored → commit under carve-out ①; `[not yours]` = **for files under `AGENTS/<other>/`**, someone else's work → flag, never sweep. ⚠️ **Exception the label cannot see: `memory/auto/` files.** `orphan_check` classifies by PATH, so every memory file reads `[not yours]` regardless of authorship — for memories PROME wrote, that label is NOT an authorship verdict and carve-out ③ makes committing them mandatory. Use `memory_index_check --strict --slug` as the authorship-scoped gate there.

**Subject ≤100 chars, receipts in the body (root Git Protocol 4d, WQ-171, 2026-09-03); `commit_check.py` enforces it.** Commit commands: § Commit cookbook below.

## Commit cookbook

**Step 0: run ALL git ops (and `safe-push.sh`) from the repo root:** `cd "$(git rev-parse --show-toplevel)"` first. Pathspecs resolve relative to cwd; from a launch dir, `git status -- PROME/` silently false-passes.

One route per case. The named home owns the commands and their rules.

| Case | Route | Home |
|---|---|---|
| A closeout whose freeze wrote a review candidate | `python3 PROME/tools/argus_scope.py --deliver-candidate -F <msg.txt> [--carry <path> …]`, then verify, then push | `PROME/CLOSEOUT.md` § The routine step 10; details `PROME/CLOSEOUT_PROCEDURES.md` § Delivery verification details |
| Every other PROME commit: an intra-day `light` closeout, a mid-session batch, any commit without a candidate | `python3 PROME/tools/commit_check.py commit [--stage] -F <msg.txt> -- <exact paths>` | this section; the intra-day closeout also follows step 10's verify and push |
| The wrapper is broken (PROME), or a desk without the wrapper | the raw pathspec recipe. For PROME this is the one exception to the wrapper, and the breakage is declared in that commit's body | `docs/GIT_WORKTREE_PROCEDURES.md` § Before committing (for PROME, `PROME/` replaces `AGENTS/<NAME>/`) |

**What the wrapper does:** it writes an intent manifest, REFUSES before git runs if any intended path has no change, commits by pathspec, then verifies HEAD against the manifest and against paths named in the message (advisory; `--strict-message` blocks). `--stage` stages only the exact files named. A mismatch is fixed by a follow-up commit, never `--amend`.

**Rules that hold on every route:**
- Stage, commit and verification must each pass before any push. On any failure stop dependent commands and inspect state.
- Literal filenames only; directory and symlink scopes are refused.
- ⛔ **`--push` on the wrapper is FORBIDDEN at the closeout commit**: it ships the bytes before the delivery check runs. The closeout order is commit → record the immutable delivery SHA → `argus_scope.py --verify-review --ref <DELIVERY_SHA>` (never `--ref HEAD`; HEAD moves in this shared clone) → `scripts/safe-push.sh`, and the review gates the push. The wrapper's `--push` exists only for a mid-session batch that no review gates, and even there safe-push's ff gate is the preferred final step.
- The wrapper is not transaction isolation. The shared intent file and moving HEAD still require this coordination protocol.
- **Renames:** `git mv` first, then name BOTH paths in the batch. `--stage` skips a path that is gone from disk and already staged (the mv source) and the pathspec commit records the rename.
- **Option order in a raw recipe:** put `-m` or `-F` before `--`; everything after `--` is a pathspec.

Push is auto at closeout via ff-gated `scripts/safe-push.sh`. A non-ff abort is routine: never force; recovery and its dirty-path overlap check, which comes FIRST, before any `--autostash`, are § Push Discipline below and root `CLAUDE.md` Git Protocol session-end step 3. Root `CLAUDE.md` / `AGENTS.md`-core commits still need Will scope (HEARTBEAT and FORGE are PROME-standard since 8/23 / 7/30).

## Push Discipline

Push is **automated at closeout** via `scripts/safe-push.sh`, predicated on **serial multi-machine operation** (Will 2026-07-01: one machine at a time, close-out-push before switching; original single-machine decision Will 2026-06-26 — OpenClaw/VPS cut). The script:

1. On-branch + shallow-clone guards, `git fetch origin master`, then a `merge-base --is-ancestor` fast-forward gate (one-sided `rev-list --count origin/master..HEAD` for the commit count).
2. Pushes only on a clean **fast-forward**; **aborts cleanly if origin has commits we don't** (never force, never pull a shared tree).
3. One closeout push sweeps all agents' local commits — the push-train, now automated.
4. **Post-push confirm (⑦b, 2026-08-28, NEXUS/RAV):** fresh fetch + merge-base ancestor check; rc 0 = the `Pushed. CONFIRMED…` receipt · rc 1 = NOT PUSHED · rc 2 = CANNOT-CONFIRM — on either failure path the script prints that no earlier `Pushed.` line is a receipt.

**Non-ff abort (re-based 2026-08-03, CORAL packet + RED 7/31 precedent, Will-approved; prior 2026-07-01 framing said "the other machine"):** = **another SESSION pushed since this clone last fetched — usually a concurrent agent on the SAME box** (verified: same-box committers, zero path overlap; non-ff is a COMMIT-GRAPH property, not a file-path one — separate trees cannot prevent it, only per-agent branches could). Do NOT force; recovery = root `CLAUDE.md` Git Protocol session-end step 3 IN FULL: FIRST the dirty-path overlap check (incoming commits vs `git status --porcelain`; any overlap ⇒ stop, flag PROME), THEN the autostash-rebase + re-push (`--autostash` stashes the WHOLE dirty tree, others' work included, restores byte-identical — RED-verified). The receipt is the line `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` — a bare `Pushed.` or a log tail is NOT a receipt (safe-push ⑦b, 2026-08-28) — and note the sweep **rewrites unpushed commit hashes** (verify by subject when a recorded hash goes missing). **Tripwire (escalate to Will, consider per-agent branches):** rebase conflicts outside your own dir, or non-ff **persisting through a completed rebase→re-push cycle** — bare mid-session recurrence is routine concurrent traffic, and the old tripwire's false fire cost an unnecessary escalation (CORAL 8/3). **Post-`git mv` assertion (WALTER 8/3, adopted):** after any commit containing a rename, run `git status --porcelain -- AGENTS/<ME>/ | grep '^ D\|^D '` — a stranded deletion = a FAILED commit, not residue (a rename is TWO paths; typed pathspecs alone don't guarantee both halves).

**Auto-push exceptions (root canon; full list in root `CLAUDE.md` Git Protocol scope note):** **TERRY** (self-sweeps, live) and **WALTER** (architectural, per its `BOARD_CONSUMPTION_SPEC` §7).

## Boot Integration

Prome boot should reference this doc when:

- The repo is dirty and multiple agents have local work.
- A commit/push/merge decision is being considered.
- The old `AGENTS/PROME/` tree appears in a search result or proposal.

## History

YEYOU, the repo-wide reviewer, was RETIRED 2026-09-05 (Will, WQ-181 ①; `PROME/ROSTER.md`). Its write scope, branch-model push exception, the 2026-06-25 landing rail and its reporting route are history, kept verbatim with the superseded cookbook text in `PROME/archive/GIT_COORDINATION_2026-11-09_pre-cleanup.md`. None of it is a live instruction.
