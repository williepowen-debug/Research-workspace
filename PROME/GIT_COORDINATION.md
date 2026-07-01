# Git Coordination

**Owner:** Prome  
**Status:** Live coordination rail; push policy updated to auto-push 2026-06-26  
**Scope:** Prome, YEYOU, and any future agent operating in this shared repo/worktree.

## Purpose

Keep multiple concurrent Claude Code agents from clobbering one another through shared-index git operations, stale Prome paths, or unsafe pushes. *(All agents are single-machine Claude Code sessions now; OpenClaw/VPS was cut 2026-06-26.)*

This doc is the canonical coordination surface. The old `AGENTS/PROME/` tree is archived at `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/` and is not live intake, boot, or git protocol.

## Hard Rules

- Run repo-state checks before sync or write work: `git status --short`, staged paths, and ahead/behind.
- Never use broad index operations: no `git add .`, no `git add -A`, no `git reset HEAD`, no force-push, no broad checkout.
- Dirty tree means inspect and triage. Do not stash, reset, or pull to make the dirt disappear.
- Use explicit pathspecs for adds and commits.
- Local scoped commits use explicit pathspecs; **push is automated at closeout via `scripts/safe-push.sh`** (ff-gated, fails safe; single-machine predicate). YEYOU stays manual/branch (see Push Discipline).
- No trade execution or external/public sends are authorized by this document.

## Ownership

### Prome

Live Prome state lives in root `PROME/`.

Prome may write:

- Root `PROME/` owner docs.
- Selected root state files, such as `HEARTBEAT.md` or memory logs, only when scoped.
- Explicitly scoped integration/archive paths approved by Will.

Prome must not treat archived `AGENTS/PROME/` files as live instructions.

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

Push is auto at closeout via ff-gated `scripts/safe-push.sh` (see Push Discipline below + root `CLAUDE.md` Git Protocol). Non-ff abort → stop, don't force, flag Will. Shared/root-doc commits still need Will scope.

## Push Discipline

Push is **automated at closeout** via `scripts/safe-push.sh`, predicated on **single-machine operation** (Decision, Will 2026-06-26 — OpenClaw/VPS cut). The script:

1. `git status --short --branch` + `git fetch` + `git rev-list --left-right --count HEAD...origin/master`.
2. Pushes only on a clean **fast-forward**; **aborts cleanly if origin has commits we don't** (never force, never pull a shared tree).
3. One closeout push sweeps all agents' local commits — the push-train, now automated.

**Tripwire:** a non-ff abort = a 2nd machine pushed to origin → stop, flag Will, switch to per-agent branches. Fully reversible (revert the closeout step + restore the manual line = one commit).

**YEYOU exception (Decision C, Will 2026-06-26):** YEYOU is a repo-wide reviewer on a branch model — it stays **manual/branch** (commits and branches locally, does **not** auto-push) until Will reviews. Its current landing rail is unchanged (below).

## Current YEYOU Landing Rail

As of 2026-06-24:

- `master` is ahead of `origin/master` with HANS work.
- YEYOU has branch work at `origin/claude/busy-rubin-bo2hu5`.
- Current `master` also has dirty/untracked `AGENTS/YEYOU/*` files.

Do not blindly merge or push. First reconcile current dirty `AGENTS/YEYOU/*` against the YEYOU branch. Then land YEYOU via Will-approved squash, cherry-pick, or clean merge onto `master`.

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

YEYOU should eventually add a short pointer to this doc in its live boot surface after its branch/worktree is reconciled.
