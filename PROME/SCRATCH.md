# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-02 ~10:55 ET (OpenClaw Prome — closeout after boot-surface + HEARTBEAT rehab)

## What Just Happened

Will asked to get Prome updated/caught up, explicitly deprioritizing trade-position work. Session completed the Prome boot-state rehab and closed the loop on SENTRY friction.

Completed and pushed:
- Synced local repo to GitHub/source-of-truth after discarding stale local generated edits with Will approval.
- Ran bounded read-only fleet scan (`fleet-scanner-2026-06-02`) to identify stale Prome surfaces vs fresh agent state.
- Refreshed and pushed core boot surfaces: `PROME/SCRATCH.md`, `PROME/TODAY.md`, `PROME/STATUS.md`, `PROME/FLEET_SCAN.md`, `PROME/ACTIVE_DECISIONS.md`.
- Audited SENTRY feed automation. Found twice-daily scheduled commits with weak signal value and repo-friction cost; disabled scheduled runs while preserving manual `workflow_dispatch`.
- Integrated WALTER's Jun 2 Iran anchor refresh into Prome surfaces: current frame is **narrative-fork + kinetic-acceleration**, not simple “talks suspended.”
- Added fresh OpenClaw continuity block to `PROME/HANDOFF.md`.
- Refreshed root `HEARTBEAT.md` with live Jun 2 dashboard and updated regime framing.

## Current Operating Posture

**Priority:** Prome is boot-safe again. State hygiene pass is complete; do not reopen broad cleanup unless something is concretely stale or blocking.

**Regime:** substance/tape divergence remains the live read, not broad cascade confirmation. Public credit and vol are calm; stress remains concentrated in Japan/FX, energy/geopolitical risk, BDC/private-credit marks, and duration.

**Trade rails:** old May `BROKER_PENDING` / 6-18 trigger language remains **verification-required**, not actionable. Will explicitly deferred positions during this rehab pass.

## Live Dashboard Anchor — Jun 2 ~10:45 ET

Pulled with `python3 FORGE/tools/market-data/dashboard.py --compact` before HEARTBEAT refresh.

- HY OAS **272bps [FRED 6/1]** 🟢
- CCC OAS **946bps [FRED 6/1]** 🟡
- VIX **16.12** 🟢
- Brent **$94.90** 🟡
- Gas weekly **4.30 [6/1]** 🔴
- USD/JPY **159.82** 🔴
- KRE **$69.19** 🟢; WAL **$79.42** 🟢
- APO **$127.76** 🟡; ARES **$127.36** 🟡; BIZD **$12.78** 🔴
- TLT **$85.72** 🟡; 10Y **4.45 [5/29]** 🟡

## Current Prome File Trust

| File | Status |
|---|---|
| `HEARTBEAT.md` | ✅ Current Jun 2 regime/levels; cadence ownership still undecided. |
| `PROME/SCRATCH.md` | ✅ Current closeout / next-session entry point. |
| `PROME/TODAY.md` | ✅ Current Jun 2 cleanup surface; naturally daily and will stale tomorrow. |
| `PROME/STATUS.md` | ✅ Current operational state after cleanup. |
| `PROME/FLEET_SCAN.md` | ✅ Current bounded Jun 2 fleet scan + SENTRY/WALTER follow-ons. |
| `PROME/ACTIVE_DECISIONS.md` | ✅ Current safety index; old trade rails verification-required. |
| `PROME/HANDOFF.md` | ✅ Current OpenClaw continuity top block. |

## Next Session Entry Point

1. Start from `HEARTBEAT.md` + `PROME/STATUS.md`; Prome no longer needs boot-surface rehab.
2. If Will wants more cleanup, choose one bounded lane:
   - HEARTBEAT cadence/ownership decision,
   - Prome inbox triage,
   - position-state reconciliation,
   - domain revive shortlist for stale REGINALD/BROCK/HENRY/LIQUID/BOND.
3. Do **not** mix position reconciliation with boot hygiene unless Will explicitly asks.

## Guardrails

- No trade execution. No trade recommendation unless explicitly requested.
- No external/public messages without approval.
- No `git add .` / `git add -A`; stage explicit files only.
- Do not spawn persistent agents casually: CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- GitHub/origin remains source-of-truth.
