# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-19 21:15 ET (OpenClaw Prome — closeout after CORAL Phase 1 + Geneva heartbeat)

## What Just Happened

1. **CORAL Phase 1 maturity scaffold landed and pushed.**
   - Added `AGENTS/CORAL/SCRATCH.md`, `AGENTS/CORAL/NEXUS_BRIEF.md`, and `AGENTS/CORAL/board_log.tsv`.
   - Patched `AGENTS/CORAL/CLAUDE.md` to mirror mature BRENT/VIOLET patterns: read SCRATCH at boot, rewrite SCRATCH at closeout, refresh NEXUS_BRIEF every session, and consume WALTER inbox handoffs through `board_log.tsv` + `git mv` to `processed/`.
   - Commit `08c0d42b CORAL: add phase 1 boot maturity surfaces` was pushed to origin after clean ahead/behind check.

2. **CORAL peer-integration drift was fixed and pushed earlier in the session.**
   - Mechanical patches included root roster, CORAL boot git protocol, WALTER registry routing note, REGINALD stale CORAL paths/snapshots, and daily memory.
   - Commit `ed13ffc1 CORAL: fix peer integration drift` is on origin.

3. **Heartbeat materially updated after Geneva gate.**
   - Live check confirmed dashboard: HY OAS **263 [FRED 6/17]**, CCC **939 [6/17]**, Brent **$80.59**, VIX **16.78**, KRE **$71.72**, WAL **$79.91**, USD/JPY **161.28**, FXY **$56.85**, BIZD **$12.36**.
   - Web check confirmed U.S.–Iran MOU / Strait reopening / ceasefire framework with a 60-day negotiation fuse. Immediate Hormuz/oil-shock tail is deferred, not eliminated.
   - `HEARTBEAT.md` now frames the regime as energy shock deferred, broad credit cascade unconfirmed, HY <260 kill still unconfirmed, carry still red.
   - Heartbeat commit `151b80dd PROME: update heartbeat after Geneva MOU` is local only as of this closeout.

4. **WALTER v0.18 boundary remains unchanged.**
   - Prome should monitor WALTER behavior/doctor output, not edit WALTER specs.
   - Quick-WALTER remains barred from fresh-news routing and deep-research judgment.

## Current Git State

- Working tree expected clean after this closeout commit.
- Local branch is ahead of origin because the Geneva heartbeat update and this closeout are local-only unless/until Will asks to push.
- Use pathspec-only commits; do not broad add/reset/stash.

## Current Operating Picture

- **Regime:** Geneva de-escalation branch fired; energy shock deferred; broad cascade not confirmed.
- **Market lane:** HY OAS **263 [FRED 6/17]** remains 3bp above the <260 blended-credit kill line. Banks/vol calm; BDC/PC weak spot persists; carry red.
- **System lane:** CORAL is now mechanically closer to mature-agent boot grade; next CORAL session should actually consume pending WALTER inbox items and move them to processed.
- **Positions:** no position/expiry action without broker/Will truth.

## Next Reboot Entry Point

1. Run repo-state first. Expect local ahead-of-origin closeout/heartbeat commits unless Will asks to push before then.
2. If market lane: refresh dashboard/FRED HY; key question remains whether HY breaks <260 or banks/PC re-weaken enough to offset.
3. If SAM lane: check Jun20 CFTC against SAM v1.6 carry-convexity survival gates.
4. If CORAL lane: spawn/ask CORAL to consume `SIG-W-20260619-002` and `SIG-W-20260619-007`, append `board_log.tsv`, and `git mv` both to `inbox/WALTER/processed/`.
5. If WALTER lane: monitor v0.18 behavior / `walter_doctor`; do not tune specs from Prome unless Will explicitly scopes it.

## Cautions

- Local-only commits need push coordination; do not assume origin has the heartbeat/closeout unless verified.
- Do not edit WALTER specs from Prome; WALTER owns WALTER spec changes.
- Do not spawn Quick-WALTER for fresh news/screenshots/research-flag judgment.
- No trade execution or old option/expiry cleanup without broker/Will reconciliation.
