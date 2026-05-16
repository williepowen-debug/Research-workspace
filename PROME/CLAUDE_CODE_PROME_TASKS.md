# Claude Code Prome Task Ladder
**Created:** 2026-05-15 21:55 ET
**Owner:** Prome
**Purpose:** Restart-safe implementation checklist for creating a persistent Claude Code Prome.

---

## Working Rule

Break the build into small, clearable chunks. Each chunk should leave the repo in a state where a fresh Prome can resume from this file plus `PROME/CLAUDE_CODE_PROME_PLAN.md`.

After each chunk:

1. Verify changed files with `git diff -- <files>`.
2. Update this file’s status section.
3. Update `PROME/CLAUDE_CODE_HANDOFF.md` once it exists.
4. If context is crowded, clear before the next chunk.

No commits until Will explicitly approves.

---

## Current Artifacts

| File | Status | Notes |
|---|---|---|
| `PROME/CLAUDE_CODE_PROME_PLAN.md` | ✅ Drafted | Architecture plan / rationale. |
| `PROME/CLAUDE_CODE_PROME_TASKS.md` | ✅ Drafted | This task ladder. |
| `PROME/CLAUDE.md` | ✅ Drafted | Bootstrap prompt for Claude Code Prome. |
| `PROME/CLAUDE_CODE_PROME.md` | ✅ Drafted | Longer operating manual. |
| `PROME/CLAUDE_CODE_HANDOFF.md` | ✅ Created | Dedicated handoff file. |
| `AGENTS_DIRECTORY.md` update | ✅ Complete | Runtime row and shared-state rules added. |
| `PROME/SYSTEM.md` update | ✅ Complete | Runtime split section added; status now points to Phase 3 dry run. |
| `PROME/BOOT.md` update | ✅ Complete | Claude Code handoff behavior integrated into normal boot. |
| `PROME/HANDOFF.md` update | ✅ Pointer added | Fresh sessions can find plan/tasks after clear. |

---

# Phase 0 — Planning / Context Preservation

## Task 0.1 — Preserve plan
**Status:** ✅ Complete
**Output:** `PROME/CLAUDE_CODE_PROME_PLAN.md`

## Task 0.2 — Create task ladder
**Status:** ✅ Complete
**Output:** `PROME/CLAUDE_CODE_PROME_TASKS.md`

## Task 0.3 — Wire plan into boot/transition docs
**Status:** ✅ Complete
**Output:** `PROME/BOOT.md`, `PROME/HANDOFF.md`, partial `PROME/SYSTEM.md` pointers

Fresh sessions can now discover the Claude Code Prome plan/task ladder from normal boot/handoff paths.

**Clear checkpoint:** Safe to clear after this. Fresh session should read:

1. `PROME/CLAUDE_CODE_PROME_PLAN.md`
2. `PROME/CLAUDE_CODE_PROME_TASKS.md`
3. Then continue at Phase 1.

---

# Phase 1 — Bootstrap Files

Goal: create the files Claude Code Prome needs before any architecture integration.

## Task 1.1 — Draft `PROME/CLAUDE.md`
**Status:** ✅ Complete
**Scope:** Small bootstrap instruction file.

Must include:

- Identity: “You are Prome inside Claude Code.”
- One-Prome/two-surfaces rule.
- Boot sequence.
- Runtime boundaries.
- Git discipline.
- Handoff requirement.

**Acceptance criteria:**

- Short enough for Claude Code to load as primary instruction.
- Clear that this is not a separate agent/personality.
- Explicitly says Telegram/OpenClaw Prome owns Will-facing synthesis and approvals.

## Task 1.2 — Draft `PROME/CLAUDE_CODE_PROME.md`
**Status:** ✅ Complete
**Scope:** Longer operating manual.

Must include:

- Runtime role.
- Responsibilities.
- Allowed work.
- Ask-first work.
- Forbidden actions.
- Handoff protocol.
- Example tasks.

**Acceptance criteria:**

- Future Claude Code Prome can read it and know what to do.
- Boundaries are operational, not vague.

## Task 1.3 — Create `PROME/CLAUDE_CODE_HANDOFF.md`
**Status:** ✅ Complete
**Scope:** Initial blank/current handoff.

Must include sections:

- What Changed
- Files Edited
- Decisions Needed from Will
- Risks / Blockers
- Next Suggested Work

**Acceptance criteria:**

- File exists and can be updated every Claude Code Prome session.

**Clear checkpoint:** Safe to clear after Phase 1. Fresh session should inspect the three new files and continue at Phase 2.

**Phase 1 completion note:** Completed 2026-05-15 23:24 ET from Telegram/OpenClaw Prome side. No commits. Repo remains dirty; do not stash/commit/reset/pull without Will approval.

---

# Phase 2 — Architecture Integration

Goal: teach the existing system that Claude Code Prome exists.

## Task 2.1 — Update `AGENTS_DIRECTORY.md`
**Status:** ✅ Complete
**Scope:** Add Claude Code Prome to runtime table.

Potential row:

| **Claude Code** | PROME | Repo-native implementation surface | Shared-state Prome, not a separate domain agent. Owns tools/docs/audits/handoffs. |

Also add rule:

- Claude Code Prome uses shared Prome files, not a siloed domain folder.
- It does not replace Telegram/OpenClaw Prome as Will-facing interface.

## Task 2.2 — Update `PROME/SYSTEM.md`
**Status:** ✅ Complete
**Scope:** Add “Prome Runtime Split” section.

Must define:

- Telegram/OpenClaw Prome role.
- Claude Code Prome role.
- Shared state files.
- Handoff file.
- Split-brain prevention rule.

## Task 2.3 — Update `PROME/BOOT.md`
**Status:** ✅ Complete
**Scope:** Add Claude Code Prome references without overcomplicating boot.

Must include:

- Read `PROME/CLAUDE_CODE_HANDOFF.md` when working after Claude Code Prome changes.
- Claude Code Prome should update that file at session end.
- Continue using normal Prome boot for Telegram/OpenClaw sessions.

**Clear checkpoint:** Safe to clear after Phase 2. Fresh session should diff/read these integration changes and continue at Phase 3.

**Phase 2 completion note:** Completed 2026-05-16 09:14 ET from Telegram/OpenClaw Prome side. Updated `AGENTS_DIRECTORY.md`, `PROME/SYSTEM.md`, `PROME/BOOT.md`, this task ladder, and `PROME/CLAUDE_CODE_HANDOFF.md`. No commits. Repo remains dirty; do not stash/commit/reset/pull without Will approval.

---

# Phase 3 — Dry Run Protocol

Goal: test Claude Code Prome with no risky edits.

## Task 3.1 — Prepare dry-run prompt
**Scope:** Write a reusable prompt for first Claude Code Prome run.

Prompt draft:

> You are Prome inside Claude Code. Read `PROME/CLAUDE.md`, `PROME/CLAUDE_CODE_PROME.md`, `PROME/CLAUDE_CODE_PROME_PLAN.md`, and `PROME/CLAUDE_CODE_PROME_TASKS.md`. Then inspect git status and the Prome state files. Do not edit anything except `PROME/CLAUDE_CODE_HANDOFF.md`. Produce a repo hygiene / readiness report and identify the next safest implementation task. Do not commit, stash, reset, or message externally.

## Task 3.2 — Run dry run in Claude Code
**Scope:** Manual/user action in Claude Code.

**Acceptance criteria:**

- It obeys boundaries.
- It does not try to become a separate identity.
- It writes a useful handoff.
- It identifies stale docs/blockers.

## Task 3.3 — Review dry-run output from Telegram/OpenClaw Prome
**Scope:** Read handoff and decide whether to proceed.

**Clear checkpoint:** Strongly recommended after dry run before real tasks.

---

# Phase 4 — First Real Work Task

Goal: give Claude Code Prome one bounded useful task.

Recommended first task:

## Task 4.1 — Create action-card template
**Scope:** Create `PROME/action-cards/TEMPLATE.md` and update `PROME/SYSTEM.md` reference if needed.

Why this task:

- Useful.
- Bounded.
- Low external risk.
- Tests repo editing discipline.

**Acceptance criteria:**

- Template exists.
- Diff is small and readable.
- Handoff updated.
- No commit without approval.

**Clear checkpoint:** Safe after task review.

---

# Phase 5 — Trust Expansion

Only after Phases 1–4 pass.

Potential future task classes:

1. Refresh stale Prome ops files.
2. Build/repair dashboard endpoints.
3. Create regional-bank action cards.
4. Audit agent folders for stale state.
5. Improve market-data/news-sweep tooling.
6. Maintain system architecture docs.

Before granting commit rights, require at least 2–3 clean task completions with:

- Scoped diffs.
- No blanket git operations.
- Clean handoffs.
- No external messaging.
- No split-brain behavior.

---

## Open Decisions for Will

| Decision | Recommendation | Status |
|---|---|---|
| Can Claude Code Prome make autonomous internal edits? | Yes, for internal docs/tools once scoped. | Pending Will approval |
| Can Claude Code Prome commit? | Not initially. Leave diffs for approval. | Pending Will approval |
| Primary handoff file? | `PROME/CLAUDE_CODE_HANDOFF.md` | Pending Will approval |
| Should it update `PROME/SCRATCH.md`? | Only when next Telegram/OpenClaw session is affected. | Pending Will approval |

---

## Next Recommended Step

Start Phase 3 dry run:

1. Use the dry-run prompt in Task 3.1 from Claude Code.
2. Instruct Claude Code Prome not to edit anything except `PROME/CLAUDE_CODE_HANDOFF.md`.
3. Review the handoff from Telegram/OpenClaw Prome before assigning real work.

Then clear context before Phase 4 if needed.
