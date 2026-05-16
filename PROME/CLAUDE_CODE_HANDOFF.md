# Claude Code Prome Handoff
**Updated:** 2026-05-16 09:14 ET

## What Changed
- Phase 2 architecture integration is complete from the Telegram/OpenClaw side.
- `AGENTS_DIRECTORY.md` now lists Claude Code Prome as a repo-native implementation surface for the same Prome identity, not a siloed domain agent.
- `PROME/SYSTEM.md` now has a full “Prome Runtime Split” section defining Telegram/OpenClaw Prome vs Claude Code Prome, shared state files, handoff rules, and split-brain prevention.
- `PROME/BOOT.md` now treats `PROME/CLAUDE_CODE_HANDOFF.md` as live and tells future sessions to read it after Claude Code Prome work.
- Task ladder now marks Phase 2 complete and points to Phase 3 dry run.

## Files Edited
- `AGENTS_DIRECTORY.md` — updated runtime table and multi-runtime rules.
- `PROME/SYSTEM.md` — added runtime split and updated Claude Code Prome status from scaffold pending to dry-run pending.
- `PROME/BOOT.md` — updated doc ownership and boot steps for live Claude Code handoff behavior.
- `PROME/CLAUDE_CODE_PROME_TASKS.md` — marked Phase 2 tasks complete; next step is Phase 3 dry run.
- `PROME/CLAUDE_CODE_HANDOFF.md` — this handoff.

## Decisions Needed from Will
- Whether to run the Phase 3 dry run now from Claude Code.
- Whether Claude Code Prome may make autonomous internal edits once scoped. Current recommendation: yes.
- Whether Claude Code Prome may commit/push after successful tasks. Current recommendation: not initially; leave diffs for approval.

## Risks / Blockers
- Repository is dirty; `git pull --rebase` remains blocked. Do not stash/commit/reset/pull without Will approval.
- Phase 3 dry run has not happened yet. Do not treat Claude Code Prome as fully trusted until it passes the no-risk test.
- Root `CLAUDE.md` and `AGENTS/PROME/CLAUDE.md` still may need reconciliation later, but Phase 2 intentionally only handled architecture integration.

## Next Suggested Work
- Phase 3 dry run prompt:

> You are Prome inside Claude Code. Read `PROME/CLAUDE.md`, `PROME/CLAUDE_CODE_PROME.md`, `PROME/CLAUDE_CODE_PROME_PLAN.md`, and `PROME/CLAUDE_CODE_PROME_TASKS.md`. Then inspect git status and the Prome state files. Do not edit anything except `PROME/CLAUDE_CODE_HANDOFF.md`. Produce a repo hygiene / readiness report and identify the next safest implementation task. Do not commit, stash, reset, or message externally.

- After the dry run, Telegram/OpenClaw Prome should read this handoff and decide whether to proceed to Phase 4 first real work task.
