# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-14 18:35 ET (OpenClaw Prome — quick closeout before clear)

## What Just Happened

Fresh boot confirmed repo was synced and clean at `ac307e0f` after the Prome boot-surface cleanup and dashboard CLI exit-code fix.

Will asked what Prome-specific tasks remained. Prome identified the active follow-up lanes:

1. Durable week card for Jun 15–22.
2. HENRY/NEXUS/WALTER stale dependency refreshes if decision-relevant.
3. Position-state reconciliation before Jun18/19 expiry cleanup.
4. WALTER feed-stack infra request.
5. Separate-clones migration decision, deferred.
6. Prome execution-rails design debt.

Will approved item 1. Prome created:

- `PROME/action-cards/WEEK_2026-06-15.md`

and updated pointers in:

- `PROME/TODAY.md`
- `HEARTBEAT.md`

These are **local uncommitted changes** as of closeout. Do not lose them.

## Current Working Regime

**Surface tape de-risked; tail/private/physical stress stayed sticky.** Broad cascade is not confirmed: HY OAS remains tight at **278bps [FRED 6/11]**, VIX faded to **17.68**, banks rallied, and Brent collapsed sub-$90. But CCC/SKEW/private-credit/consumer/Japan/physical energy stress remain live.

## Separate-Clones Decision Status

Will wants to think longer. He values agents being able to read each other’s files and message each other. Prome recommendation: **do not rush separate-clones**. Hold as post-FOMC architecture decision; continue interim pathspec discipline.

## Next Session Entry Point

1. Run `PROME/BOOT.md` sequence and `git status --short`.
2. Expected local changes if not committed before clear:
   - `M HEARTBEAT.md`
   - `M PROME/TODAY.md`
   - `M PROME/SCRATCH.md`
   - `M PROME/HANDOFF.md`
   - `M memory/2026-06-14.md`
   - `?? PROME/action-cards/WEEK_2026-06-15.md`
3. Ask Will whether to commit/push the week-card bundle.
4. If proceeding with work before commit, use `PROME/action-cards/WEEK_2026-06-15.md` + `PROME/TODAY.md` as near-gate source.

## Cautions

- No agent edits unless Will explicitly approves.
- Broker/position truth remains unreconciled; old rails verification-required.
- HYG Jun $75P is dead/not actionable per LIQUID.
- HENRY/NEXUS/WALTER stale dependencies remain follow-up decisions.
- WALTER feed-stack request is in `AGENTS/PROME/inbox/SIG-WALTER-PROME-20260610-cron-feed-infra-refresh.md`.

## Git State at Closeout

Before writing this SCRATCH closeout, repo was:

- `HEAD = origin/master = ac307e0f`
- ahead/behind `0/0`
- local changes: week card + TODAY/HEARTBEAT pointers

After this closeout, `PROME/SCRATCH.md` is also modified locally.

## Guardrails

- No trade execution. No trade recommendation unless explicitly requested.
- No external/public messages without approval.
- Push is Will-coordinated.
- Pathspec commits only; never `git add .`, `git add -A`, or broad `git reset HEAD`.
