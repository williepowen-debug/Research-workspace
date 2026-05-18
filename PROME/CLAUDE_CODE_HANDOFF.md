# Claude Code Prome Handoff
**Updated:** 2026-05-17 (Phase 3 dry run) ET
**Surface:** Claude Code Prome
**Run type:** Phase 3 dry run — readiness audit, no mutating edits outside this file.

> **Hash-refresh note (2026-05-17 evening cleanup pass):** The "Repo Hygiene Snapshot" table below has been updated to current HEAD (`8a44dbe2`). The dry-run report itself was performed at HEAD `e87724e1` and committed as `dddce166`. The "Stale Docs / Contradictions Identified" findings are preserved as the original dry-run record; several have since been addressed in this cleanup pass — see the new "Current Session" section appended at end of file.

---

## Identity / Model Confirmation

**One Prome, two work surfaces — confirmed.**

- Telegram/OpenClaw Prome owns Will-facing conversation, synthesis, approvals, decision rails, external sends.
- Claude Code Prome (this session) owns repo-native implementation: docs, tools, audits, handoffs, scoped edits.
- Shared state lives in `PROME/`, `AGENTS/`, `HEARTBEAT.md`, `MEMORY.md`, etc. No private truth layer. No fork of memory.
- I do **not** message Will directly, execute trades, push commits, or impersonate a separate identity. I am Prome on a different work surface.

Boot reading completed this session: `CLAUDE.md`, `AGENTS.md`, `SOUL.md`, `USER.md`, `PROME/CLAUDE.md`, `PROME/CLAUDE_CODE_PROME.md`, `PROME/CLAUDE_CODE_PROME_PLAN.md`, `PROME/CLAUDE_CODE_PROME_TASKS.md`, `PROME/SYSTEM.md`, `PROME/HANDOFF.md`, `PROME/STATUS.md`, `PROME/TODAY.md`, `HEARTBEAT.md`, `MEMORY.md`, plus cross-reference reads of `PROME/SCRATCH.md`, `PROME/BOOT.md`, `PROME/CLAUDE_CODE_HANDOFF.md` (this file pre-edit), and `AGENTS_DIRECTORY.md`.

---

## Repo Hygiene Snapshot

| Dimension | State |
|---|---|
| Branch | `master` |
| Local HEAD | `8a44dbe2` ("SENTRY: feed update 2026-05-17-2240") |
| `origin/master` | matches HEAD |
| Working tree | clean before this cleanup pass; dirty during the pass itself |
| Recent commit chain | `8a44dbe2` ← `dddce166` ← `e87724e1` ← `728e9f78` ← `270b6d1d` (WALTER closeout → Prome state refresh → handoff clear → Phase 3 dry run record → SENTRY feed update) |
| Phase 0 (planning) | ✅ Complete |
| Phase 1 (bootstrap files) | ✅ Complete — all four scaffold files present |
| Phase 2 (architecture integration) | ✅ Complete — AGENTS_DIRECTORY.md, PROME/SYSTEM.md, PROME/BOOT.md all carry Claude Code Prome references |
| Phase 3 (dry run) | ▶️ Running now |

Scaffold files verified present and coherent:
- `PROME/CLAUDE.md` — bootstrap, identity, one-Prome/two-surfaces, boot sequence, git discipline.
- `PROME/CLAUDE_CODE_PROME.md` — longer operating manual, allowed/ask-first/forbidden lists.
- `PROME/CLAUDE_CODE_PROME_PLAN.md` — architecture rationale.
- `PROME/CLAUDE_CODE_PROME_TASKS.md` — phased task ladder.
- `PROME/CLAUDE_CODE_HANDOFF.md` — this file.

---

## Stale Docs / Contradictions Identified

1. **`PROME/CLAUDE_CODE_HANDOFF.md` was 2 commits stale.** It said local `master` = `origin/master` at `270b6d1d`. Actual HEAD is `e87724e1`. Fixed in this update.
2. **`PROME/STATUS.md` carries the same `270b6d1d` claim** ("Latest Sync / Architecture State" → "GitHub sync ✅ Complete | Pulled cleanly; local `master` = `origin/master` at `270b6d1d`."). STATUS.md is Telegram/OpenClaw-owned; flagging only, not editing.
3. **`PROME/HEARTBEAT.md` Operating Notes** asserts "PROME/SCRATCH.md, PROME/CLAUDE_CODE_HANDOFF.md ... are refreshed / clear-ready as of May 17 10:45 ET." True for SCRATCH.md (post-`e87724e1` clear) but the CLAUDE_CODE_HANDOFF.md was older than the SCRATCH.md until this dry run. Same flag — Telegram/OpenClaw to refresh on its next pass if it matters.
4. **`AGENTS_DIRECTORY.md` runtime table omits RED and OZK from the Claude Code runtime row.** Root `CLAUDE.md` lists `CARL*, REGINALD*, OZK*, SAM*, RED*` (`* = Claude Code`); AGENTS_DIRECTORY.md only lists `REGINALD, CARL, SAM`. Either CLAUDE.md or AGENTS_DIRECTORY.md needs reconciliation. Recommend updating AGENTS_DIRECTORY.md (the directory is younger / more easily reconciled than the root rules file).
5. **`MEMORY.md` "Last Updated: 2026-04-05"** at the top — over a month stale at the index level. Daily entries in `memory/YYYY-MM-DD.md` are fresher; MEMORY.md itself appears curated long-term so the staleness may be intentional. Worth Will/Telegram Prome confirming whether a weekly maintenance pass is overdue.
6. **`PROME/TOSCANINI/QUEUE.md` flagged stale** in SYSTEM.md and STATUS.md ("⚠️ Stale until rebuilt"). Known issue, not a new finding.
7. **`FORGE/STATUS.md` flagged stale** per Prome inbox signal (per SYSTEM.md). Known issue.
8. **Phase 4 first task collision.** `PROME/CLAUDE_CODE_PROME_TASKS.md` Task 4.1 says "Create `PROME/action-cards/TEMPLATE.md`" — but that file **already exists** (alongside `FSK_MAY11_ACTION_CARD.md` and `REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md`). Phase 4 should be reframed as "audit / refine existing TEMPLATE.md against acceptance criteria" rather than "create from scratch." Flagging so Telegram/OpenClaw Prome knows before assigning Phase 4.
9. **`PROME/HANDOFF.md`** explicitly says the *next* session priority is "install Agents View" — orthogonal to the Phase 3 dry-run path. Not a contradiction (different work, both queued), but Telegram/OpenClaw Prome should be aware that Will may flip between the two streams.

No active blockers preventing Phase 3 → Phase 4 progression. All issues above are documentation hygiene or minor reconciliation, not gating.

---

## What Changed This Session

- Read all required boot files plus cross-reference docs.
- Verified scaffold integrity, git cleanliness, and Phase 2 integration completeness.
- Updated this file (`PROME/CLAUDE_CODE_HANDOFF.md`) with the dry-run report.

## Files Edited

- `PROME/CLAUDE_CODE_HANDOFF.md` (this file) — full rewrite to report Phase 3 dry-run results.

No other files touched. No commits, pushes, stashes, resets, deletes, external messages, or domain-agent edits.

---

## Phase 3 Acceptance Check

| Criterion (from PLAN.md) | Result |
|---|---|
| Understands one-Prome/two-surfaces | ✅ Confirmed at top of this file. |
| Does not try to message Will directly | ✅ No external action attempted. |
| Identifies stale docs and blockers | ✅ See "Stale Docs / Contradictions" section above. |
| Leaves a clean handoff | ✅ This file. |

---

## Decisions Needed from Will

1. **Pass Phase 3 dry run?** If yes, Claude Code Prome can proceed to Phase 4.
2. **Phase 4 scope clarification.** TEMPLATE.md already exists. Want me to (a) audit and refine the existing file against PLAN/TASKS acceptance criteria, or (b) substitute a different bounded first real task (e.g., reconcile AGENTS_DIRECTORY.md runtime row to include RED + OZK)?
3. **Autonomous internal edits going forward?** Current recommendation in PLAN.md: yes for scoped Prome docs; commits still gated on approval.
4. **Commit policy.** Current recommendation: Claude Code Prome leaves uncommitted diffs; Telegram/OpenClaw Prome or Will commits. Confirm or relax.

---

## Risks / Blockers

- **None blocking** the dry run itself.
- **Soft risks:** stale references in STATUS.md / HEARTBEAT.md (commit hash drift), Phase 4 task description vs reality mismatch, AGENTS_DIRECTORY.md / root CLAUDE.md runtime-row contradiction. None of these gate further work; they will compound if not addressed within a few sessions.

---

## Next Suggested Work (post-dry-run)

**Recommended:** Phase 4 audit pass on `PROME/action-cards/TEMPLATE.md`.

- Scope: read the existing TEMPLATE.md, compare against Plan §"Decision Artifact Buildout" + TASKS.md §Task 4.1 acceptance criteria, identify gaps, propose a small refinement diff.
- Why this is the safest next task: bounded to one file, no cross-agent state, exercises the Claude Code Prome edit/handoff loop on real content rather than meta-docs, and resolves the Phase 4 collision noted above.
- Output: a proposed diff plus an updated handoff, no commit until approval.

**Alternate bounded task (if Will prefers a different first real edit):** reconcile `AGENTS_DIRECTORY.md` runtime table with root `CLAUDE.md` agent list (add RED + OZK to the Claude Code runtime row, or remove them from root if the directory is authoritative). Equally bounded, single-file diff.

**Out of scope for next CC-Prome session:** Toscanini QUEUE rebuild, FORGE/STATUS.md refresh, Agents View install (Will-directed Telegram/OpenClaw thread), trade decision prompts. These belong to Telegram/OpenClaw Prome or are Will-gated.

---

## Rules I Held To This Session

- No commits, pushes, pulls, stashes, resets, or deletes.
- No external messages.
- No edits outside `PROME/CLAUDE_CODE_HANDOFF.md`.
- No domain-agent file edits.
- No persistent-agent spawns (CARL, REGINALD, SAM, RED, BRENT).
- No `git add -A` or `git add .`.
- Read-before-edit honored.

---

## Current Session — Cleanup Pass (2026-05-17 evening ET)

**Run type:** Will-directed self-cleanup; addresses dry-run findings + context refresh.
**HEAD at start:** `8a44dbe2`. Working tree clean before edits.

**Decisions received from Will this session:**
- Phase 3 — PASSED.
- Autonomous internal-edit rights — SCOPED YES. Free within `AGENTS/PROME/` and `PROME/`. Propose-then-approve for other agents' files, root-level CLAUDE.md, shared infrastructure. Approval required for anything outside `~/Research-workspace/`.
- Commit policy — show-diff-then-approve, always for now. Push only on explicit instruction.

**Context update absorbed:**
- Agent View install: ✅ done on this machine + laptop. Persistent dashboard / session manager now operational.
- New active experiment: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. Teams maps more directly than vanilla Agent View onto the chief-of-staff / named-teammates / mailbox / shared-task architecture we've been building. Small bounded test planned, likely later today.
- The "install Agents View" priority in `HANDOFF.md` is superseded — refreshed accordingly.

**Files edited this session (all in autonomous scope):**
- `PROME/STATUS.md` — hash `270b6d1d` → `8a44dbe2`.
- `PROME/TODAY.md` — hash `270b6d1d` → `8a44dbe2`.
- `PROME/HANDOFF.md` — HEAD hash + Clear Handoff section rewritten to "Active Thread" (Agent View done, teams experiment is new thread).
- `PROME/SCRATCH.md` — hash references brought current.
- `PROME/CLAUDE_CODE_HANDOFF.md` (this file) — hash refresh in snapshot table + this Current Session section.
- `PROME/CLAUDE_CODE_PROME_TASKS.md` — Task 4.1 reframed from "Create TEMPLATE.md" to "Audit/refine existing TEMPLATE.md."

**Propose-only (not edited; awaiting approval):**
- `AGENTS_DIRECTORY.md` Runtime row reconciliation (the CARL/REGINALD/OZK/SAM/RED contradiction with root `CLAUDE.md`). Proposal: align AGENTS_DIRECTORY.md to root CLAUDE.md as the more recently-authoritative source. Details in session output.

**Three softer-inconsistency questions answered with recommendations (not acted on):**
- `MEMORY.md` root staleness.
- `AGENTS/PROME/CLAUDE.md` "OpenClaw" framing.
- `AGENTS/PROME/LAST_COMPLETION.md` + trailing-off inboxes.

See conversation log for the full recommendations.

**Next session start:**
- Pull, confirm clean.
- If teams experiment fires today, read this section + `PROME/HANDOFF.md` Active Thread for the latest state.
- The dry-run "Stale Docs / Contradictions Identified" section above is now partially obsolete — items 1, 2, 5 (hash drift) are resolved; item 8 (Phase 4 collision) is resolved; items 3, 4, 6, 7, 9 are unresolved or out of scope for this pass.
