# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-04 ~17:35 ET (OpenClaw Prome — boot surface refresh after Jun 3-4 signal ingestion)

## What Just Happened

Will asked Prome to pull extensive GitHub updates, then ingest the two direct Prome signals, then refresh the Prome boot surface.

Completed and pushed before this refresh:
- Pulled GitHub cleanly: fast-forward to `687e2968`, then Prome signal-ingestion commit `55e5b634` pushed.
- Ingested **HENRY TLT supersession**: old 5/22 TLT 2/1 roll ticket is no longer actionable. Jun $85P are now Will-handled catalyst salvage; Sep add waits for CPI confirmation.
- Ingested **SAM pathspec migration audit**: created `PROME/PATHSPEC_MIGRATION_STATUS.md`; fixed Prome's own `AGENTS/PROME/CLAUDE.md` to remove broad `git reset HEAD` protocol.

This refresh updates `SCRATCH`, `TODAY`, `STATUS`, and `FLEET_SCAN` so Prome no longer boots from Jun 2 cleanup language.

## Current Operating Posture

**Priority:** Boot surface is being updated from Jun 2 rehab mode to Jun 4 operating mode. This is still not a full position reconciliation pass.

**Regime:** Substance/tape divergence persists. Public credit and vol remain calm; stress is concentrated in Japan/FX, BDC/private-credit marks, duration, and energy/gas pressure. Do not upgrade to cascade language without HY/VIX confirmation or a concrete funding/bank/auction trigger.

**Safety:** Shared-repo race risk is now an explicit workstream. Prome uses pathspec commits only. Remaining per-agent CLAUDE.md fixes are tracked in `PROME/PATHSPEC_MIGRATION_STATUS.md` and should be done by each owning agent at next boot.

**Trade rails:** TLT is no longer stale-BROKER_PENDING: HENRY/Will superseded it Jun 3. Remaining non-TLT old 6/18 rails remain verification-required, not actionable.

## Live Dashboard Anchor — Jun 4 ~17:30 ET

Pulled with `python3 FORGE/tools/market-data/dashboard.py --compact`.

- HY OAS **275bps [FRED 6/3]** 🟢
- CCC OAS **947bps [FRED 6/3]** 🟡
- VIX **15.40** 🟢
- Brent **$95.14** 🟡
- Gas weekly **4.30 [6/1]** 🔴
- USD/JPY **160.01** 🔴
- KRE **$69.98** 🟢; WAL **$80.74** 🟢; OZK **$49.21** 🟡
- APO **$128.41** 🟡; ARES **$130.50** 🟡; BIZD **$12.70** 🔴
- TLT **$85.50** 🟡; 10Y **4.46 [6/2]** 🟡
- Initial claims **225k [5/30]** 🟡; shadow-adjusted est **280k**
- Continuing claims **1.777M [5/23]** 🟢

## Current Prome File Trust

| File | Status |
|---|---|
| `PROME/SCRATCH.md` | ✅ Current Jun 4 boot handoff. |
| `PROME/TODAY.md` | ✅ Current Jun 4 operating surface. |
| `PROME/STATUS.md` | ✅ Current after Jun 3-4 signal ingestion + dashboard anchor. |
| `PROME/FLEET_SCAN.md` | ✅ Current Jun 4 bounded scan. |
| `PROME/ACTIVE_DECISIONS.md` | ✅ Current safety index; TLT supersession ingested. |
| `PROME/PATHSPEC_MIGRATION_STATUS.md` | ✅ Current tracker; Prome/SAM done, other owner edits pending. |
| `HEARTBEAT.md` | 🟡 Still Jun 2 root regime file; levels mostly directionally consistent but should be refreshed separately if Will wants injected root state current. |
| `PROME/HANDOFF.md` | 🟡 Top block Jun 2; read before `/clear`, but not refreshed in this pass unless closeout asks for it. |

## Next Session Entry Point

1. Start with `PROME/STATUS.md`, `PROME/TODAY.md`, and `PROME/PATHSPEC_MIGRATION_STATUS.md`.
2. If continuing cleanup: refresh root `HEARTBEAT.md` next, because it is injected and still carries Jun 2 levels.
3. If switching to decisions: do a separate position-state reconciliation pass before touching old 6/18 rails.
4. If reducing repo risk: coordinate remaining per-agent pathspec CLAUDE.md edits by owner; do not bulk-edit other agents from Prome unless Will explicitly overrides.

## Guardrails

- No trade execution. No trade recommendation unless explicitly requested.
- No external/public messages without approval.
- Use pathspec commits only; never `git add .`, `git add -A`, or broad `git reset HEAD`.
- Do not spawn persistent agents casually: CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- GitHub/origin remains source-of-truth.
