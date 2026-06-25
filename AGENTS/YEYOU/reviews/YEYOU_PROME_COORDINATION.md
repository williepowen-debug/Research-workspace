# YEYOU × PROME Git Coordination Protocol
**Date:** 2026-06-24
**Status:** Approved — YEYOU branch reconciled, ready for first live run

---

## Context

YEYOU and PROME both operate on the same repo. YEYOU is a repo-wide reviewer (reads everywhere, writes only to `AGENTS/YEYOU/` and `AGENTS/YEYOU/outbox/` per SOUL.md), but both agents need to avoid shared-index footguns (no `git add .`, `git reset HEAD`, broad stash/checkout).

PROME has identified 5 immediate recommendations:
1. YEYOU should not share Prome's casual commit lane
2. Pushes need a lease model, not vibes
3. No shared-index footguns (explicit pathspec commits only)
4. Best architecture: separate worktree/branch per active agent
5. First reconcile YEYOU's branch vs current dirty `AGENTS/YEYOU/*`

---

## Proposed Coordination Protocol

### 1. Commit Discipline (No Shared-Index Footguns)

**YEYOU commits:**
- Only pathspec-scoped commits: `git commit -m "YEYOU: <subject>" -- AGENTS/YEYOU/<file>`
- Only to `AGENTS/YEYOU/` directory
- No `git add AGENTS/YEYOU/` (directory-level add)
- No `git add -A`, `git add .`, `git reset HEAD`, or broad checkout

**PROME commits:**
- Only pathspec-scoped commits: `git commit -m "PROME: <subject>" -- PROME/<file>`
- Only to root-level `PROME/` directory and selected root state files (e.g., `HEARTBEAT.md`, memory logs when scoped)
- No `git add PROME/` (directory-level add)
- No `git add -A`, `git add .`, `git reset HEAD`, or broad checkout

**Scope rule:** Pathspec-only, scoped to the owner docs for the task. Live PROME owns root `PROME/`; the archived `AGENTS/PROME/` tree is not a normal write surface.

**Shared rule:** Explicit pathspecs only. Never directory-level adds.

---

### 2. Push Discipline (Lease Model, Not Vibes)

**Local commits are autonomous:**
- Both agents may commit locally without coordination
- No push required immediately after local commit
- Commits are staged locally, not pushed to GitHub

**GitHub pushes require coordinated flush:**
- Rule: `git status` → `git fetch` → ahead/behind check → inspect dirty tree → push in order
- Push only during a Will-coordinated flush (PROME-led)
- Before flush: `git status` to check for uncommitted changes, `git fetch` to check ahead/behind, inspect dirty tree, then push in order

**Push order:**
1. YEYOU's branch (if ahead)
2. PROME's branch (if ahead)
3. Master (if ahead)

**YEYOU push autonomy:**
- YEYOU may commit locally and branch locally
- YEYOU may NOT push its branch to GitHub until Will/PROME coordinates flush
- YEYOU can prepare work, but push requires coordinated approval

---

### 3. Branch Architecture

**YEYOU's branch:** `origin/claude/busy-rubin-bo2hu5` (current)
- Commits: scaffold GLM work-review agent, tighten boot/closeout + boot.py, add SOUL.md + IDENTITY.md
- Status: Diverged from `master` by 3 commits

**PROME's branch:** `master` (current)
- Status: Diverged from YEYOU's branch by 3 commits (HANS work)
- Has uncommitted YEYOU files

**Branch landing strategy:**
- Keep YEYOU on its current branch (`busy-rubin-bo2hu5`) until Will approves merge
- After reconciliation, Will-approved squash/cherry-pick or clean merge onto `master`
- YEYOU does NOT push its branch until Will/PROME coordinates flush

**Rationale:**
- YEYOU's branch is 3 commits ahead of `master`
- `master` has HANS work and uncommitted YEYOU files
- Merge requires reconciliation of dirty `AGENTS/YEYOU/*` against `origin/claude/busy-rubin-bo2hu5`
- YEYOU stays autonomous for reviews, but not autonomous for pushing to shared `master`

---

### 4. Boot Protocol Integration

**YEYOU boot:**
1. Check for uncommitted changes in `AGENTS/YEYOU/`
2. If dirty, inspect/triage — do NOT stash/reset/pull to resolve
3. Run review work
4. Commit locally (pathspec only)
5. Do NOT push automatically

**PROME boot:**
1. Check for uncommitted changes in `PROME/` and selected root state files (e.g., `HEARTBEAT.md`, memory logs)
2. If dirty, inspect/triage — do NOT stash/reset/pull to resolve
3. Run PROME work
4. Commit locally (pathspec only, scoped to owner docs for the task)
5. Do NOT push automatically

**PROME closeout:**
1. Check YEYOU's branch status: `git fetch origin; git log HEAD..origin/claude/busy-rubin-bo2hu5 --oneline`
2. If YEYOU's branch is ahead, propose merge in `PROME/SCRATCH.md` or `PROME/HANDOFF.md`
3. If Will approves, merge YEYOU's branch into `master` as one clean commit
4. Push to GitHub

---

### 5. Conflict Prevention

**YEYOU never touches:**
- `PROME/` (except via outbox signals)
- Any other agent's files (per SOUL.md)

**PROME never touches:**
- `AGENTS/YEYOU/` (except via outbox signals)
- Any other agent's files (except via outbox signals)

**Scope rule:** PROME does not edit YEYOU content during ordinary work; any YEYOU edits/integration require explicit Will-scoped coordination.

**Shared rule:** Only PROME can merge YEYOU's branch into `master`. YEYOU never merges into `master` directly.

---

### 6. Outbox Routing (Phase 1)

**YEYOU → PROME only:**
- YEYOU writes findings/proposals under `AGENTS/YEYOU/reviews/` or `AGENTS/YEYOU/outbox/`
- PROME reads those directly and escalates to Will
- YEYOU does NOT write directly to Will yet

**Rationale:**
- YEYOU writes to its own review/outbox surface
- PROME reads those directly (not via inbox)
- PROME records decisions in live `PROME/` docs (`GIT_COORDINATION.md`, `SCRATCH.md`, `HANDOFF.md`)
- Direct-to-Will outbox can be added later if needed

---

### 7. Canonical Coordination Surface

**Primary doc:** `PROME/GIT_COORDINATION.md`
- Contains full coordination protocol
- Reference from `PROME/BOOT.md` (short pointer)
- YEYOU-specific pointer in `AGENTS/YEYOU/CLAUDE.md`/boot surface (later)

**YEYOU reporting:**
- YEYOU writes findings/proposals under `AGENTS/YEYOU/reviews/` or `AGENTS/YEYOU/outbox/`
- Prome reads those directly and records decisions in live `PROME/` docs
- Do NOT use derelict `AGENTS/PROME/INBOX.md` as canonical (legacy surface, not revived unless explicitly needed)

**Rationale:**
- `AGENTS/PROME/INBOX.md` is stale/derelict with HERMES-era delivery language
- `AGENTS/PROME/CLAUDE.md` has old unsafe git instructions (pull/stash/push-at-end)
- Canonical coordination should use live PROME surfaces: `GIT_COORDINATION.md`, `BOOT.md`, `SCRATCH.md`, `HANDOFF.md`
- YEYOU should reference canonical surfaces, not legacy inboxes
- Live PROME owns root `PROME/`; archived `AGENTS/PROME/` tree is not a normal write surface

---

## Implementation Steps

### Step 1: Reconcile YEYOU's branch vs current dirty `AGENTS/YEYOU/*`
- Check `git status` for uncommitted changes in `AGENTS/YEYOU/`
- If dirty, inspect/triage — do NOT stash/reset/pull to resolve
- Inspect dirty tree to understand what needs reconciliation
- Verify stash is clean

### Step 2: Decide YEYOU's landing strategy
- Keep YEYOU on its current branch (`busy-rubin-bo2hu5`) until Will approves merge
- After reconciliation, Will-approved squash/cherry-pick or clean merge onto `master`
- YEYOU does NOT push its branch until Will/PROME coordinates flush

### Step 3: Write coordination rule into `PROME/GIT_COORDINATION.md`
- Document commit discipline (pathspec-only, scoped to owner docs for the task)
- Document push discipline (lease model, not vibes)
- Document branch architecture (YEYOU stays on its branch until merge)
- Document boot protocol integration (inspect/triage dirty tree, commit locally, push only on coordinated flush)
- Add short pointer in `PROME/BOOT.md` referencing `GIT_COORDINATION.md`
- Add YEYOU-specific pointer in `AGENTS/YEYOU/CLAUDE.md`/boot surface (later)

### Step 4: Update YEYOU's SOUL.md (if needed)
- SOUL.md already says YEYOU writes only to `AGENTS/YEYOU/` and `AGENTS/YEYOU/outbox/`
- No update needed

### Step 5: Test coordination protocol
- Run YEYOU boot → inspect/triage dirty tree → commit locally → check local status → verify no push
- Run PROME boot → inspect/triage dirty tree → commit locally → check local status → verify no push
- Run PROME closeout → check YEYOU's branch → propose merge → verify merge succeeds

---

## Approval Requirements

**PROME must approve:**
- Coordination protocol (this document)
- Branch landing strategy (keep separate until Will-approved merge)
- Implementation steps

**YEYOU must approve:**
- Coordination protocol (this document)
- Branch landing strategy (keep separate until Will-approved merge)

**Will must approve:**
- Reconciliation of YEYOU's branch vs current dirty `AGENTS/YEYOU/*`
- Merge of YEYOU's branch into `master` (after reconciliation)
- Any deviation from the coordination protocol

---

## Rationale

**Why separate commit lanes:**
- YEYOU is a repo-wide reviewer, not a domain agent
- YEYOU reads everywhere, but writes only to its own directory
- Separating commit lanes prevents accidental clobbering of other agents' work

**Why lease model for pushes:**
- Local commits are autonomous
- GitHub pushes require coordination to avoid race conditions
- Lease model ensures only one agent pushes at a time (PROME-led)

**Why separate worktree/branch per active agent:**
- Prevents merge conflicts between YEYOU and PROME
- Keeps YEYOU's work isolated until Will approves merge
- Makes merge conflict surface minimal (one clean integration commit)

**Why explicit pathspec commits only:**
- Prevents shared-index footguns (no `git add .`, `git reset HEAD`)
- Ensures only intended files are staged
- Makes git history clean and auditable

**Why inspect/triage dirty tree (no stash/pull automation):**
- Dirty tree means inspect/triage, don't stash/reset/pull to resolve
- Existing PROME rule is explicit: dirty tree → inspect, not auto-fix
- YEYOU should follow that rule

**Why PROME scope is root-level `PROME/`:**
- Live PROME owns root `PROME/`; archived `AGENTS/PROME/` tree is not a normal write surface
- The real rule is "pathspec-only, scoped to the owner docs for the task"
- PROME commits to `PROME/` and selected root state files (e.g., `HEARTBEAT.md`, memory logs when scoped)

**Why YEYOU can't push yet:**
- YEYOU can commit locally and branch locally
- YEYOU can prepare work, but push requires coordinated approval
- YEYOU may NOT push its branch to GitHub until Will/PROME coordinates flush

**Why YEYOU outbox goes to PROME only (Phase 1):**
- YEYOU writes to its own review/outbox surface
- PROME reads those directly (not via inbox)
- PROME records decisions in live `PROME/` docs (`GIT_COORDINATION.md`, `SCRATCH.md`, `HANDOFF.md`)
- Direct-to-Will outbox can be added later if needed

**Why canonical doc is `PROME/GIT_COORDINATION.md`:**
- `AGENTS/PROME/INBOX.md` is stale/derelict with HERMES-era delivery language
- `AGENTS/PROME/CLAUDE.md` has old unsafe git instructions (pull/stash/push-at-end)
- Canonical coordination should use live PROME surfaces: `GIT_COORDINATION.md`, `BOOT.md`, `SCRATCH.md`, `HANDOFF.md`
- YEYOU should reference canonical surfaces, not legacy inboxes
- Live PROME owns root `PROME/`; archived `AGENTS/PROME/` tree is not a normal write surface

---

**Status:** Approved — YEYOU branch reconciled, ready for first live run.
