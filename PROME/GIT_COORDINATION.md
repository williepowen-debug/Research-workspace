# Git Coordination

**Owner:** Prome  
**Status:** Live coordination rail; push policy updated to auto-push 2026-06-26  
**Scope:** every agent operating in this shared repo/worktree (fleet size → `PROME/ROSTER.md`, the countless pointer [audit #10 — the hand-carried count had drifted 30→33]; PROME + YEYOU were the founding two).

## Purpose

Keep multiple concurrent Claude Code agents from clobbering one another through shared-index git operations, stale Prome paths, or unsafe pushes. *(All agents are Claude Code sessions under **serial multi-machine** operation — Will runs one box at a time, desktop ⇄ laptop, close-out-push before switching; OpenClaw/VPS was cut 2026-06-26. Machine-local inventory → `PROME/MACHINE_LOCAL.md`.)*

This doc is the live coordination surface (vs the archived `AGENTS/PROME/` tree); **root `CLAUDE.md` Git Protocol is canon** — this doc mirrors it and adds the PROME cookbook (per `SYSTEM.md` Canonical→Mirrors). The old `AGENTS/PROME/` tree is archived at `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/` and is not live intake, boot, or git protocol.

## Hard Rules

- Run repo-state checks before sync or write work: `git status --short`, staged paths, and ahead/behind.
- Never use broad index operations: no `git add .`, no `git add -A`, no `git reset HEAD`, no force-push, no broad checkout. **Never `git commit --amend`** (root Git Protocol 4b, Will-approved 8/21 — amend rewrites whoever holds HEAD, which may not be you; write messages via quoted-heredoc `git commit -F <file>`, not inline `-m`, for EVERY message (root 4b — nothing to remember under tempo; the cookbook's inline `-m` forms below are subject-line shorthand)) *(mirror synced audit #10)*.
- Dirty tree means inspect and triage. Do not stash, reset, or pull to make the dirt disappear.
- Use explicit pathspecs for adds and commits.
- Local scoped commits use explicit pathspecs; **push is automated at closeout via `scripts/safe-push.sh`** (ff-gated, fails safe; serial multi-machine predicate). **Auto-push exceptions (full list, root canon):** YEYOU manual/branch · TERRY self-sweeps · WALTER architectural per `BOARD_CONSUMPTION_SPEC` §7 (see Push Discipline).
- No trade execution or external/public sends are authorized by this document.

## Ownership

### Prome

Live Prome state lives in root `PROME/`.

Prome may write:

- Root `PROME/` owner docs.
- `HEARTBEAT.md` and `FORGE/` — PROME-standard commits (freed 8/23 and 7/30; explicit-path, never swept blind). `memory/auto/` files PROME authored — MANDATORY self-commit (carve-out ③ below); daily `memory/YYYY-MM-DD.md` = standard closeout set.
- Explicitly scoped integration/archive paths approved by Will.

Prome must not treat archived `AGENTS/PROME/` files as live instructions.

**Cross-dir carve-outs (root canon ①–③ + ④ — mirror re-synced 2026-08-29 audit #11):**
- **① Self-authored inbox packets (ratified 2026-07-23 — HENRY orphan-gap memo):** a packet **PROME authored** into another agent's `inbox/` is PROME's to commit, **and PROME must** — an uncommitted packet never reaches the recipient (~12% orphaned this way pre-detector). Commit it explicitly-pathed with the recipient named in the subject (`PROME -> <RECIPIENT>: <what>`).
- **② Self-authored shared-log rows (ratified 2026-07-25):** a row PROME authored in a shared cross-agent log (`AGENTS/SIGNALS.md` class) is PROME's to commit, explicitly path-scoped. Rows other agents wrote and file restructures stay off-limits.
- **③ Self-authored auto-memory files (ratified 2026-07-27, MANDATORY):** any memory file under `memory/auto/` that PROME authored or appended MUST be self-committed — the shared `MEMORY.md` index row rides out on whoever commits next while the FILE needs a deliberate add, so an uncommitted memory leaves the index advertising content the other machine doesn't have (worse than the memory not existing). Enforcement at closeout: `python3 scripts/memory_index_check.py --strict --slug <slug>` per memory written — **the `--slug` form, never bare `--strict`** (bare gates the whole index and blocks on OTHER agents' orphans ③ forbids PROME to commit).

- **④ Gate C Kernel custody (inactive outside an operator-activated packet):** under an approved activation PROME is the sole acceptance custodian for `KERNEL/shadow/events/`, `KERNEL/audit/commands/`, the four registered `KERNEL/views/` projections and the sitting's governance records — additions-only, exact pathspecs, never a directory. Domain agents may commit only their own `AGENTS/<NAME>/outbox/kernel/submissions/<command_id>.json`. Full text = root Git Protocol ④ + the custody paragraph (reconciled 8/27 C8).

Someone else's work outside `PROME/` remains strictly off-limits. Root `CLAUDE.md` Git Protocol owns the full carve-out text; on any drift, root wins.

**Session-end orphan check (root canon step 1b, adopted 2026-07-23):** before the closeout commit batch, run `bash scripts/orphan_check.sh PROME` — read-only advisory (~5s, exit 0 always). `[likely YOURS]` = packets PROME authored → commit under carve-out ①; `[not yours]` = **for files under `AGENTS/<other>/`**, someone else's work → flag, never sweep. ⚠️ **Exception the label cannot see: `memory/auto/` files.** `orphan_check` classifies by PATH, so every memory file reads `[not yours]` regardless of authorship — for memories PROME wrote, that label is NOT an authorship verdict and carve-out ③ makes committing them mandatory. Use `memory_index_check --strict --slug` as the authorship-scoped gate there.

Example:

**Subject ≤100 chars, receipts in the body (root Git Protocol 4d, WQ-171, 2026-09-03) — `commit_check.py` enforces it.**
```bash
git commit -m "PROME: <subject>" -- PROME/<file>
```

For new files:

```bash
git add -- PROME/<newfile>
git commit -m "PROME: <subject>" -- PROME/<newfile>
```

### YEYOU

YEYOU is a repo-wide reviewer: read broadly, write narrowly.

YEYOU may write:

- `AGENTS/YEYOU/`
- `AGENTS/YEYOU/reviews/`
- `AGENTS/YEYOU/outbox/`

YEYOU does not edit other agents' files, Prome docs, root state files, or live market/trade rails. Findings are proposals, not fixes.

Example:

```bash
git commit -m "YEYOU: <subject>" -- AGENTS/YEYOU/<file>
```

For new files:

```bash
git add -- AGENTS/YEYOU/<newfile>
git commit -m "YEYOU: <subject>" -- AGENTS/YEYOU/<newfile>
```

## Commit cookbook

**Default from 2026-08-29 (RAV review, Will-endorsed): commit through `PROME/tools/commit_check.py`** — `python3 PROME/tools/commit_check.py commit -F <msg.txt> -- <exact paths>` writes an intent manifest, REFUSES before git runs if any intended path has no change (the d3915f75d / 6704cfc37 overclaim shape — a script died, the file was unchanged, the message was written anyway), commits by pathspec, then verifies HEAD against the manifest and against paths named in the message (advisory; `--strict-message` to block). A mismatch is fixed by a follow-up commit, never `--amend` (root 4b). The recipes below remain valid as the underlying git; the wrapper is the checked path.
 (PROME pathspec)

*(Relocated from `BOOT.md` 2026-07-01. Path-scoped commits avoid the shared-`.git/index` race — `[[finding_pathspec_commit_race_safety]]`.)* **Option order matters: put `-m` before `--`; everything after `--` is a pathspec.**

**Step 0 — run ALL git ops (and `safe-push.sh`) from the repo root:** `cd "$(git rev-parse --show-toplevel)"` first. Pathspecs resolve relative to cwd — from a launch dir, `git status -- PROME/` silently false-passes (root `CLAUDE.md` Before-committing step 0, landed 2026-07-01).

Modified tracked files — no staging step:

```bash
git commit -m "PROME: <subject>" -- PROME/<file> PROME/<file>
```

New files — add only explicit paths:

```bash
git add -- PROME/<newfile>
git commit -m "PROME: <subject>" -- PROME/<newfile>
```

Mixed modified + new:

```bash
git add -- PROME/<newfile>
git commit -m "PROME: <subject>" -- PROME/<modified> PROME/<newfile>
```

Push is auto at closeout via ff-gated `scripts/safe-push.sh` (see Push Discipline below + root `CLAUDE.md` Git Protocol). Non-ff abort = **routine** (usually a concurrent same-box session, not the other machine — see Push Discipline; serial multi-machine): don't force — `git pull --rebase --autostash` + re-push (full form + caveats in Push Discipline below); escalate to Will only on the tripwire signatures in Push Discipline. Root `CLAUDE.md` / `AGENTS.md`-core commits still need Will scope (HEARTBEAT and FORGE are PROME-standard since 8/23 / 7/30).

## Push Discipline

Push is **automated at closeout** via `scripts/safe-push.sh`, predicated on **serial multi-machine operation** (Will 2026-07-01: one machine at a time, close-out-push before switching; original single-machine decision Will 2026-06-26 — OpenClaw/VPS cut). The script:

1. On-branch + shallow-clone guards, `git fetch origin master`, then a `merge-base --is-ancestor` fast-forward gate (one-sided `rev-list --count origin/master..HEAD` for the commit count).
2. Pushes only on a clean **fast-forward**; **aborts cleanly if origin has commits we don't** (never force, never pull a shared tree).
3. One closeout push sweeps all agents' local commits — the push-train, now automated.

**Non-ff abort (re-based 2026-08-03, CORAL packet + RED 7/31 precedent, Will-approved; prior 2026-07-01 framing said "the other machine"):** = **another SESSION pushed since this clone last fetched — usually a concurrent agent on the SAME box** (verified: same-box committers, zero path overlap; non-ff is a COMMIT-GRAPH property, not a file-path one — separate trees cannot prevent it, only per-agent branches could). Do NOT force; `git pull --rebase --autostash` + re-push — `--autostash` stashes the dirty tree (others' work included), rebases, restores byte-identical (RED-verified); check incoming commits don't touch the dirty paths first. Confirm the literal `Pushed.` line — a log tail is not a push receipt — and note the sweep **rewrites unpushed commit hashes** (verify by subject when a recorded hash goes missing). **Tripwire (escalate to Will, consider per-agent branches):** rebase conflicts outside your own dir, or non-ff **persisting through a completed rebase→re-push cycle** — bare mid-session recurrence is routine concurrent traffic, and the old tripwire's false fire cost an unnecessary escalation (CORAL 8/3). **Post-`git mv` assertion (WALTER 8/3, adopted):** after any commit containing a rename, run `git status --porcelain -- AGENTS/<ME>/ | grep '^ D\|^D '` — a stranded deletion = a FAILED commit, not residue (a rename is TWO paths; typed pathspecs alone don't guarantee both halves).

**YEYOU exception (Decision C, Will 2026-06-26):** YEYOU is a repo-wide reviewer on a branch model — it stays **manual/branch** (commits and branches locally, does **not** auto-push) until Will reviews.

**Other auto-push exceptions (root canon — full list in root `CLAUDE.md` Git Protocol scope note):** **TERRY** (self-sweeps, live) and **WALTER** (architectural, per its `BOARD_CONSUMPTION_SPEC` §7). *(Added 7/11 spine-audit — this doc had drifted to naming YEYOU alone.)*

## YEYOU Landing Rail — RESOLVED 2026-06-25

The 2026-06-24 landing situation (master ahead with HANS work; YEYOU branch at `origin/claude/busy-rubin-bo2hu5`; dirty `AGENTS/YEYOU/*`) was resolved 2026-06-25 via a Will-approved curated worktree landing — the branch is gone from origin (`[[finding_curated_worktree_branch_landing]]`). For any future YEYOU branch landing, reuse that pattern: isolated worktree, curate file-by-file, FF-only merge.

## Reporting

YEYOU Phase 1 reports to Prome only:

- Write findings/proposals under `AGENTS/YEYOU/reviews/` or `AGENTS/YEYOU/outbox/`.
- Prome reads those directly.
- Prome records decisions in live `PROME/` docs, usually this file, `PROME/SCRATCH.md`, or `PROME/HANDOFF.md`.
- Do not use archived `AGENTS/PROME/INBOX.md` as canonical.

Direct-to-Will YEYOU routing can be added later only after Will approves that escalation path.

## Boot Integration

Prome boot should reference this doc when:

- The repo is dirty and multiple agents have local work.
- YEYOU has active review or branch work.
- A commit/push/merge decision is being considered.
- The old `AGENTS/PROME/` tree appears in a search result or proposal.
