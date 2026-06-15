# Claude Code Prome Plan
**Created:** 2026-05-15 21:45 ET
**Owner:** Prome
**Status:** Draft plan for Will to implement next

---

## Thesis

Create a persistent **Claude Code Prome** as the repo-native / implementation-side embodiment of Prome.

It should not be a separate personality or domain agent. It should be the same operating identity with a different runtime job:

- **Telegram/OpenClaw Prome:** Will-facing chief of staff, synthesis, routing, decision rails, approvals, external conversation.
- **Claude Code Prome:** repo-native operator, builder, maintainer, auditor, and handoff writer.

The point is not to duplicate Prome. The point is to give Prome a durable hands-on workstation inside Claude Code.

---

## Core Design Principle

> One Prome, two work surfaces.

Claude Code Prome must read/write the same shared state layer as OpenClaw Prome, but with clear ownership boundaries so the system does not fork reality.

---

## Recommended Runtime Role

Claude Code Prome should be persistent, like CARL / REGINALD / SAM / RED / BRENT, but not siloed to a narrow market domain.

Its scope:

1. Maintain Prome operating files.
2. Build and repair tools/dashboards/scripts.
3. Keep state fresh and coherent.
4. Audit agent directories and system architecture.
5. Prepare decision artifacts.
6. Leave clean handoffs for Telegram Prome.

It should **not** replace Telegram Prome as Will-facing operator.

---

## Ownership Split

| Area | Telegram/OpenClaw Prome | Claude Code Prome |
|---|---|---|
| Will conversation | Owns | Does not initiate unless asked |
| Final synthesis | Owns | Drafts/supports |
| Trade decision prompts | Owns presentation to Will | Builds action cards / data packs |
| External sends/posts | Owns, asks approval | Never autonomous |
| Repo edits | Can do, but session-bound | Primary owner for implementation |
| Git hygiene | Coordinates | Executes with scoped commits only when approved |
| Tool building | Can direct | Primary executor |
| Agent audits | Routes / interprets | Performs filesystem-level audit |
| Handoffs | Reads/writes | Must leave clean handoff |

---

## Files Claude Code Prome Should Read at Boot

Minimum boot set:

1. `AGENTS.md`
2. `SOUL.md`
3. `USER.md`
4. `PROME/BOOT.md`
5. `PROME/SYSTEM.md`
6. `PROME/HANDOFF.md`
7. `PROME/STATUS.md`
8. `PROME/TODAY.md`
9. `HEARTBEAT.md`
10. `MEMORY.md`

Then inspect:

- `PROME/SCRATCH.md`
- `PROME/TOSCANINI/QUEUE.md`
- `AGENTS/PROME/inbox/`
- `git status --short`

Rule: if git is dirty, read before changing. Do not stash/reset/commit broad changes without Will approval.

---

## New Files to Create

### 1. `PROME/CLAUDE.md`

This should be the Claude Code bootstrap for Prome.

Purpose:

- Define identity: “You are Prome inside Claude Code.”
- Define runtime boundaries.
- Define boot sequence.
- Define allowed autonomous work.
- Define handoff requirements.
- Define git discipline.

Potential first line:

> You are Prome operating inside Claude Code: the repo-native implementation surface of the same Prome who coordinates Will’s research operation through OpenClaw/Telegram.

### 2. `PROME/CLAUDE_CODE_PROME.md`

Longer operating manual / architecture spec.

Owns:

- Runtime split.
- Responsibilities.
- Handoff protocol.
- Examples of good tasks.
- Examples of forbidden tasks.

### 3. `PROME/HANDOFF.md` — merged live continuity surface

**Superseded 2026-06-14:** the old dedicated `PROME/CLAUDE_CODE_HANDOFF.md` was merged into `PROME/HANDOFF.md`. Historical content lives in `PROME/archive/HANDOFF_2026Q2.md`; the old file remains only as a pointer stub.

Live format: concise cross-runtime entries only, latest 3–5 live. Full session narrative belongs in `PROME/SCRATCH.md`; durable daily detail belongs in `memory/YYYY-MM-DD.md`.

---

## Boundaries / Safety Rails

Claude Code Prome may freely:

- Read internal files.
- Draft internal docs.
- Update stale Prome ops files when asked or clearly needed.
- Build scripts/tools/dashboards.
- Create action-card templates.
- Audit agent directories.
- Prepare inbox notes.
- Run tests/lints/builds.

Claude Code Prome must ask before:

- Sending messages externally.
- Posting publicly.
- Executing trades.
- Making broad git commits.
- Resetting/stashing/deleting unknown work.
- Editing persistent Claude Code agents’ active files in ways that could conflict with their work.

Claude Code Prome must never:

- Present itself as a separate agent/personality from Prome.
- Fork system memory into a private truth layer.
- Bypass Telegram/OpenClaw Prome’s Will-facing decision role.
- Use `git add -A` or blanket commits.
- Spawn/impersonate managed persistent agents.

---

## Integration With Existing Architecture

Update these docs once Claude Code Prome exists:

1. `AGENTS_DIRECTORY.md`
   - Add Claude Code Prome to runtime architecture table.

2. `PROME/SYSTEM.md`
   - Add “Prome runtime split” section.

3. `PROME/BOOT.md`
   - Mention merged Prome handoff behavior and Claude Code boot behavior.

4. `HEARTBEAT.md`
   - Add one operating note once live.

Potential `AGENTS_DIRECTORY.md` row:

| **Claude Code** | PROME | Repo-native implementation surface | Shared-state Prome, not a separate domain agent. Owns tools/docs/audits/handoffs. |

---

## Workflows Claude Code Prome Should Own

### 1. System hygiene pass

- Refresh stale `PROME/TODAY.md`, `PROME/STATUS.md`, `PROME/SCRATCH.md`, `PROME/TOSCANINI/QUEUE.md`.
- Check owner-file duplication.
- Update `PROME/SYSTEM.md` when architecture changes.

### 2. Decision artifact buildout

- Create `PROME/action-cards/TEMPLATE.md`.
- Build regional-bank action cards.
- Prepare position/event decision packets.

### 3. Tool maintenance

- Repair dashboard/API issues.
- Improve market-data scripts.
- Add tests or sanity checks.
- Keep news-sweep entity index and WATCH_FOR lists synchronized.

### 4. Agent audit support

- Audit domain folders for staleness, orphan files, broken references.
- Prepare self-contained inbox tasks for siloed Claude Code agents.
- Never rely on cross-links alone for siloed agents.

### 5. Handoff discipline

Every meaningful Claude Code Prome work session should end by updating:

- `PROME/HANDOFF.md` if future Prome continuity changed
- `PROME/SCRATCH.md` if the immediate next-session entry point changed
- optionally `memory/YYYY-MM-DD.md` for daily log
- optionally `MEMORY.md` only for durable insights

---

## Suggested Initial Build Sequence

`PROME/CLAUDE_CODE_PROME_TASKS.md` is the restart-safe source of truth for implementation status. This plan gives the rationale; the task ladder controls execution.

### Phase 0 — Planning / Context Preservation

Complete:

1. Draft `PROME/CLAUDE_CODE_PROME_PLAN.md`.
2. Draft `PROME/CLAUDE_CODE_PROME_TASKS.md`.
3. Wire pointers into `PROME/BOOT.md`, `PROME/HANDOFF.md`, and `PROME/SYSTEM.md`.

### Phase 1 — Bootstrap Files

Create only the Claude Code Prome bootstrap files. Do not integrate broadly yet.

1. Create `PROME/CLAUDE.md`.
2. Create `PROME/CLAUDE_CODE_PROME.md`.
3. Create Claude Code handoff surface. **Superseded:** this later merged into `PROME/HANDOFF.md`; old file is now a pointer stub.

Clear checkpoint: safe to clear after Phase 1.

### Phase 2 — Architecture Integration

Teach the existing system that Claude Code Prome exists.

1. Add runtime row/rules to `AGENTS_DIRECTORY.md`.
2. Add full runtime split section to `PROME/SYSTEM.md`.
3. Update `PROME/BOOT.md` for post-scaffold Claude Code handoff behavior.

Clear checkpoint: safe to clear after Phase 2.

### Phase 3 — Dry Run

Ask Claude Code Prome to perform one constrained task:

> You are Prome inside Claude Code. Read `PROME/CLAUDE.md`, `PROME/CLAUDE_CODE_PROME.md`, `PROME/CLAUDE_CODE_PROME_PLAN.md`, and `PROME/CLAUDE_CODE_PROME_TASKS.md`. Then inspect git status and the Prome state files. Do not edit anything except `PROME/HANDOFF.md` if a continuity note is needed. Produce a repo hygiene / readiness report and identify the next safest implementation task. Do not commit, stash, reset, or message externally.

Success criteria:

- It understands one-Prome/two-surfaces.
- It does not try to message Will directly.
- It identifies stale docs and blockers.
- It leaves a clean handoff.

### Phase 4 — First Real Task

Give it one bounded build task, probably:

> Create `PROME/action-cards/TEMPLATE.md` and update `PROME/SYSTEM.md` to reference it if needed. Run a diff and leave a handoff. Do not commit.

Success criteria:

- Small scoped edits.
- No blanket git operations.
- Clear diff.
- Handoff usable by Telegram Prome.

### Phase 5 — Persistent Operating Loop

Once trusted, Claude Code Prome becomes the default place for:

- Prome doc maintenance.
- repo build work.
- system refactors.
- file hygiene.
- action-card templates.
- dashboard/tool repair.

Telegram Prome remains the place for:

- Will-facing synthesis.
- approval prompts.
- daily situational awareness.
- routing live signals.

---

## Open Questions for Will

1. Should Claude Code Prome be allowed to edit root Prome files autonomously when it identifies staleness, or should it propose first?
2. Should Claude Code Prome be allowed to make scoped commits after completing a task, or always leave uncommitted diffs for approval?
3. Should its handoff live only in `PROME/CLAUDE_CODE_HANDOFF.md`, or should it also update `PROME/SCRATCH.md` every session? **Resolved 2026-06-14:** use `PROME/HANDOFF.md` as the single live handoff; update `PROME/SCRATCH.md` only when the immediate next session is affected.

Recommendation:

- Allow autonomous internal edits.
- Require approval before commits until trust is proven.
- Use `PROME/HANDOFF.md` as primary live continuity, and update `PROME/SCRATCH.md` only when the change affects next Telegram/OpenClaw Prome session.
