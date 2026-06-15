# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-14 20:58 ET (OpenClaw Prome — protocol-prune closeout before reboot)

## What Just Happened

Will asked to reduce Prome startup/context load and consolidate duplicate starting/handoff documents.

Completed and pushed this session:

1. **Jun15 week card + audit cleanup** — `0c012e29 PROME add Jun15 week card and audit cleanup`.
   - Added `PROME/action-cards/WEEK_2026-06-15.md`.
   - Cleaned Prome surface residue after the boot refresh.
2. **HEARTBEAT resolved-blocker cleanup** — `de95ae74 PROME clear resolved heartbeat blocker`.
   - Removed stale “commit/push week-card bundle” blocker after it was done.
3. **Handoff surface merge/prune** — `2d3c0216 PROME merge handoff surfaces`.
   - Archived old OpenClaw + Claude Code handoff history to `PROME/archive/HANDOFF_2026Q2.md`.
   - Made `PROME/HANDOFF.md` the single live cross-runtime continuity surface.
   - Replaced `PROME/CLAUDE_CODE_HANDOFF.md` with a pointer stub.
4. **Boot/closeout protocol hardening** — `b0736265 PROME harden boot and closeout protocols`.
   - `BOOT.md` now checks repo status before pull/rebase.
   - `HANDOFF.md` is read early; `FLEET_SCAN` and inbox/outbox scans are conditional.
   - `BOOT.md` and `CLOSEOUT.md` now use correct `git commit -m ... -- <paths>` syntax.

No agent files were edited. No trade work or position reconciliation was done.

## Current Working Regime

Use `HEARTBEAT.md`, `PROME/TODAY.md`, and `PROME/action-cards/WEEK_2026-06-15.md` as current near-gate surfaces. Working model remains: **surface tape de-risked; tail/private/physical stress stayed sticky.** Broad cascade not confirmed; HY OAS remains the broad-cascade line.

## Next Reboot Entry Point

1. Follow the new `PROME/BOOT.md` order:
   - check git status / ahead-behind first;
   - pull only if clean/safe;
   - read `PROME/HANDOFF.md`, then `SCRATCH`, `TODAY`, `ACTIVE_DECISIONS`, `STATUS`;
   - read `FLEET_SCAN` only if needed.
2. Verify repo is clean/synced at `b0736265` or later.
3. Choose next work lane:
   - position-state reconciliation before Jun18/19 expiry cleanup;
   - HENRY/NEXUS/WALTER refresh if decision-relevant before FOMC/expiry;
   - WALTER feed-stack infra request;
   - separate-clones migration later, not half-way;
   - Prome execution-rails design debt.

## Cautions

- No agent edits unless Will explicitly approves.
- Broker/position truth remains unreconciled; old rails verification-required.
- HYG Jun $75P is dead/not actionable per LIQUID.
- Separate-clones migration remains deferred; Will values cross-agent file visibility/messaging.
- Push remains Will-coordinated; pathspec only; never `git add .`, `git add -A`, or `git reset HEAD`.
