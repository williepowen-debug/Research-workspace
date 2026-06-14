# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-14 PM ET (OpenClaw Prome — boot-surface refresh Phase 3 underway)

## What Just Happened

Will returned after a long gap and asked Prome to pull the updated repo from GitHub. The repo fast-forwarded cleanly to `c87c00ac` with a large Jun 8–14 update. No conflicts, no stash/reset needed.

Will then approved a staged **Prome boot-surface refresh**, with one explicit constraint: **do not edit agents**.

Completed so far:

1. **Phase 0 baseline** — repo clean/synced at `c87c00ac`; dashboard anchor pulled; boot surfaces confirmed stale vs current repo. Checkpoint: `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE0.md`.
2. **Phase 1 bounded agent inspection** — read-only top-section inspection across LIQUID/VIOLET/BRENT/HAWK/WALTER/SAM/CARL/LABOR/RED/BROCK/REGINALD/BOND/HENRY/NEXUS/OTTO plus Prome-routed outboxes. No agent edits. Checkpoint: `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE1.md`.
3. **Phase 2 edit map** — file-by-file plan for the boot-surface rewrites. Checkpoint: `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE2_EDIT_MAP.md`.
4. **Daily memory checkpoint** — `memory/2026-06-14.md` created to survive compaction.
5. **Phase 3 started** — `PROME/TODAY.md` rewritten first.

## Current Working Regime

**Surface tape de-risked; tail/private/physical stress stayed sticky.** Broad cascade is not confirmed: HY OAS remains tight at **278bps [FRED 6/11]**, VIX faded to **17.68**, banks rallied, and Brent collapsed sub-$90. But the structural side did not heal: CCC **956**, SKEW held 142+, PC/BDC stress remains hot, consumer-credit stress persists, Japan/BOJ risk is live, and physical energy/chokepoint stress is severe despite the price collapse.

Phase 0 dashboard anchor: HY OAS 278 · CCC 956 · Brent $87.33 · VIX 17.68 · USD/JPY 160.18 · Gas 4.15 · Claims 229k / shadow 284k · 10Y 4.45 · SOFR-IORB -0.05 · KRE 73.41 · WAL 83.67 · OZK 52.10 · APO 133.88 · ARES 134.90 · BIZD 12.71 · FXY 57.26 · TLT 85.77.

## Next Session Entry Point

Continue Phase 3 boot-surface rewrites in this order:

1. `PROME/STATUS.md`
2. `PROME/ACTIVE_DECISIONS.md`
3. `PROME/FLEET_SCAN.md`
4. `HEARTBEAT.md` last
5. Verify with `git diff --stat`, targeted stale-language grep, and a final status check.

`PROME/TODAY.md` is already refreshed for Jun 14/15.

## Cautions

- **No agent edits** unless Will explicitly changes the constraint.
- HENRY/NEXUS/WALTER are stale/dark in important ways: HENRY for GEX/flip level, NEXUS for post-6/12 synthesis, WALTER Iran anchor vs HAWK/BRENT Jun 13.
- Broker/position truth remains unreconciled. Old rails are verification-required only.
- LIQUID says HYG $75P is written off / let expire 6/19. Do not surface HYG as actionable.
- WALTER Iran anchor is stale relative to HAWK/BRENT; use HAWK/BRENT for current energy/geopolitical read until WALTER refreshes.
- Dashboard data was usable but script exited code 1; check automation health later.

## Open Questions for Will

1. Keep Phase0/1/2 checkpoint files as audit trail, archive them after refresh, or delete after folding conclusions into surfaces?
2. Create a durable `PROME/action-cards/WEEK_2026-06-15.md`, or let `TODAY.md` carry the near-gate calendar for now?
3. After boot surfaces, should Prome route/ask for WALTER Iran anchor refresh?
4. After boot surfaces, should HENRY/NEXUS be refreshed ahead of FOMC or only if Will asks?
5. Position reconciliation remains a separate phase unless Will pivots.

## Guardrails

- No trade execution. No trade recommendation unless explicitly requested.
- No external/public messages without approval.
- Push is Will-coordinated — commit locally if approved, push only on Will's explicit call.
- Pathspec commits only; never `git add .`, `git add -A`, or broad `git reset HEAD`.
- GitHub/origin remains source of truth.
