# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-15 00:05 ET (OpenClaw Prome — context-weight cleanup closeout)

## What Just Happened

Will and Prome finished the Prome context-weight cleanup and pushed it cleanly.

Completed and pushed:

1. **Context surface prune** — `44271ffe PROME: prune context surfaces`.
   - Slimmed `PROME/BOOT.md` and clarified safe boot/push rules.
   - Compressed root `MEMORY.md` from ~12.0k chars to ~7.8k durable kernels.
   - Archived original memory at `memory/archive/MEMORY_ROOT_PRE_PRUNE_2026-06-14.md`.
   - Added `PROME/MEMORY_PRUNE_PLAN_2026-06-14.md` and refreshed the context-weight report.
   - Corrected `PROME/STATUS.md` agent map: most core agent statuses refreshed Jun14; do not assume HENRY/NEXUS/WALTER stale solely from old map.
2. **Lean tool-output protocol** — `0147347a PROME: add lean tool output protocol`.
   - Added boot rule: compact diagnostics first, full reads/diffs when correctness requires.
   - Added closeout transcript-hygiene reminder.

No `AGENTS/*` files were edited. No trade work or position reconciliation was done.

## Current Git State

Clean and synced to origin after the context-weight cleanup commits. Push discipline remains Will-coordinated and pathspec-only.

## Current Working Regime

Use `HEARTBEAT.md`, `PROME/TODAY.md`, and `PROME/action-cards/WEEK_2026-06-15.md` as current near-gate surfaces. Working model remains: **surface tape de-risked; tail/private/physical stress stayed sticky.** Broad cascade not confirmed; HY OAS remains the broad-cascade line.

## Next Reboot Entry Point

1. Follow `PROME/BOOT.md`; lean tool-output protocol is now active.
2. Verify repo clean/synced before pull.
3. Choose next lane:
   - **OpenClaw update check/maintenance:** installed `2026.5.6`; npm latest observed `2026.6.6`; beta `2026.6.8-beta.1`. Recommendation was stable update, not beta, when Will wants maintenance.
   - **TODAY vs HEARTBEAT dedupe:** next context-weight target if continuing Prome surface cleanup.
   - **Position-state reconciliation** before Jun18/19 expiry cleanup if Will wants trade hygiene.
   - **HENRY/NEXUS/WALTER content freshness check** only if decision-relevant before FOMC/expiry; files refreshed Jun14 but content still needs verification before use.
   - Separate-clones migration remains deferred; do not do halfway.

## Cautions

- No agent edits unless Will explicitly approves.
- Broker/position truth remains unreconciled; old rails verification-required.
- HYG Jun $75P is dead/not actionable per LIQUID.
- Push remains Will-coordinated; pathspec only; never `git add .`, `git add -A`, or `git reset HEAD`.
