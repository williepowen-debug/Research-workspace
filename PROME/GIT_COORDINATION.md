# Git Coordination

**Owner:** Prome  
**Status:** Live coordination rail; push policy updated to auto-push 2026-06-26  
**Scope:** Prome, YEYOU, and any future agent operating in this shared repo/worktree.

## Purpose

Keep multiple concurrent Claude Code agents from clobbering one another through shared-index git operations, stale Prome paths, or unsafe pushes. *(All agents are Claude Code sessions under **serial multi-machine** operation — Will runs one box at a time, desktop ⇄ laptop, close-out-push before switching; OpenClaw/VPS was cut 2026-06-26. Machine-local inventory → `PROME/MACHINE_LOCAL.md`.)*

This doc is the live coordination surface (vs the archived `AGENTS/PROME/` tree); **root `CLAUDE.md` Git Protocol is canon** — this doc mirrors it and adds the PROME cookbook (per `SYSTEM.md` Canonical→Mirrors). The old `AGENTS/PROME/` tree is archived at `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/` and is not live intake, boot, or git protocol.

## Hard Rules

- Run repo-state checks before sync or write work: `git status --short`, staged paths, and ahead/behind.
- Never use broad index operations: no `git add .`, no `git add -A`, no `git reset HEAD`, no force-push, no broad checkout.
- Dirty tree means inspect and triage. Do not stash, reset, or pull to make the dirt disappear.
- Use explicit pathspecs for adds and commits.
- Local scoped commits use explicit pathspecs; **push is automated at closeout via `scripts/safe-push.sh`** (ff-gated, fails safe; serial multi-machine predicate). **Auto-push exceptions (full list, root canon):** YEYOU manual/branch · TERRY self-sweeps · WALTER architectural per `BOARD_CONSUMPTION_SPEC` §7 (see Push Discipline).
- No trade execution or external/public sends are authorized by this document.

## Ownership

### Prome

Live Prome state lives in root `PROME/`.

Prome may write:

- Root `PROME/` owner docs.
- Selected root state files, such as `HEARTBEAT.md` or memory logs, only when scoped.
- Explicitly scoped integration/archive paths approved by Will.

Prome must not treat archived `AGENTS/PROME/` files as live instructions.

**Cross-dir carve-out (root canon, ratified 2026-07-23, Will-approved — HENRY orphan-gap memo):** a packet **PROME authored** into another agent's `inbox/` is PROME's to commit, **and PROME must** — an uncommitted packet never reaches the recipient (~12% of packets orphaned this way pre-detector). Commit it explicitly-pathed with the recipient named in the subject (`PROME -> <RECIPIENT>: <what>`). Someone else's work outside `PROME/` remains strictly off-limits.

**Session-end orphan check (root canon step 1b, adopted 2026-07-23):** before the closeout commit batch, run `bash scripts/orphan_check.sh PROME` — read-only advisory (~5s, exit 0 always). `[likely YOURS]` = packets PROME authored → commit under the carve-out above; `[not yours]` = someone else's work → flag, never sweep.

Example:

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

## Commit cookbook (PROME pathspec)

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

Push is auto at closeout via ff-gated `scripts/safe-push.sh` (see Push Discipline below + root `CLAUDE.md` Git Protocol). Non-ff abort = **routine** (serial multi-machine): don't force — `git pull --rebase` + re-push; escalate to Will only on the tripwire signatures in Push Discipline. Shared/root-doc commits still need Will scope.

## Push Discipline

Push is **automated at closeout** via `scripts/safe-push.sh`, predicated on **serial multi-machine operation** (Will 2026-07-01: one machine at a time, close-out-push before switching; original single-machine decision Will 2026-06-26 — OpenClaw/VPS cut). The script:

1. On-branch + shallow-clone guards, `git fetch origin master`, then a `merge-base --is-ancestor` fast-forward gate (one-sided `rev-list --count origin/master..HEAD` for the commit count).
2. Pushes only on a clean **fast-forward**; **aborts cleanly if origin has commits we don't** (never force, never pull a shared tree).
3. One closeout push sweeps all agents' local commits — the push-train, now automated.

**Non-ff abort (updated 2026-07-01):** = the other machine pushed since this clone last pulled — **routine** under serial multi-machine. Do NOT force; `git pull --rebase` + re-push. **Tripwire (escalate to Will, consider per-agent branches):** rebase conflicts outside your own dir, or non-ff recurring mid-session — the signatures of two machines running simultaneously, which the protocol forbids. Fully reversible (revert the closeout step + restore the manual line = one commit).

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
