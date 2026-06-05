# HEARTBEAT.md
**Updated:** 2026-06-04 ~17:45 ET (OpenClaw Prome — root heartbeat refresh after Jun 4 boot-surface update)

## Regime

**Substance/tape divergence remains the live read — not broad cascade confirmation.** Public credit and vol are still calm (HY OAS **275bps [FRED 6/3 close]**, VIX **15.40**), while stress remains concentrated in Japan/FX, BDC/private-credit marks, gas/energy, duration, and early labor-softening signals.

Key Jun 4 updates:
- **Tape still refuses cascade:** HY OAS **275bps [FRED 6/3]** and VIX **15.40** are green. Do not upgrade to transmission/cascade language without public-credit/vol confirmation or a concrete funding/auction/bank trigger.
- **SAM / Japan:** USD/JPY is now basically at the 160 line (**160.00-160.01**, dashboard variance), keeping intervention-zone / BOJ Jun 16 risk live.
- **LABOR:** Initial claims moved to **225k [5/30]** with shadow-adjusted estimate **280k**. This is yellow deterioration, not headline labor-break confirmation.
- **BROCK / Private credit:** BIZD remains red at **$12.70**; BROCK Jun 4 updates reportedly added OTF/BCRED/OCIC Q1 reads and moved convergence **46→55**. Read current BROCK before any PC/BDC action.
- **HENRY / TLT:** Old May 22 TLT roll ticket is **superseded**. Jun $85P are a small Will-handled catalyst salvage bet; Sep add is deferred to CPI confirmation. Do not use old TLT `BROKER_PENDING` language.
- **PROME / system safety:** Pathspec migration tracker is live at `PROME/PATHSPEC_MIGRATION_STATUS.md`. Prome/SAM fixed; remaining per-agent CLAUDE.md edits are owner-pending.
- **WALTER / Iran:** Jun 2 frame still applies: **narrative-fork + kinetic-acceleration**. Treat channel state as contested unless WALTER refreshes it; Kuwait strike cadence remains load-bearing.

Working model: substance-side stress channels are active, but the tape is forcing patience. The most important live reds are **USD/JPY ~160**, **BIZD red**, and **gas weekly red**; the most important counter-evidence is **HY/VIX green**.

## Stress dashboard

HY OAS **275🟢** [FRED 6/3] · CCC **947🟡** [FRED 6/3] · 10Y **4.46🟡** [6/2] · TLT **$85.50🟡** · VIX **15.40🟢** · Brent **$95.14🟡** · Gas weekly **4.30🔴** [6/1] · USD/JPY **160.00🔴** · WAL **$80.74🟢** · KRE **$69.98🟢** · OZK **$49.21🟡** · APO **$128.41🟡** · ARES **$130.50🟡** · BIZD **$12.70🔴** · FXY **$57.35🟡** · Initial claims **225k🟡** [5/30] / shadow est **280k** · Continuing claims **1.777M🟢** [5/23]

## Thresholds

| Indicator | Green | Yellow | Red | Current |
|---|---|---|---|---|
| HY OAS | <300 | 300-320 | >320 | **275🟢 [FRED 6/3]** |
| CCC OAS | <900 | 900-1000 | >1000 | **947🟡 [FRED 6/3]** |
| 10Y Treasury | <4.40 | 4.40-4.75 | >4.75 | **4.46🟡 [6/2]** |
| TLT | >$88 | $85-88 | <$85 | **$85.50🟡** |
| Brent | <$85 | $85-100 | >$100 | **$95.14🟡** |
| Gas weekly | <$3.75 | $3.75-4.00 | >$4.00 | **4.30🔴 [6/1]** |
| USD/JPY | <150 | 150-158 | >158 | **160.00🔴** |
| VIX | <18 | 18-25 | >25 | **15.40🟢** |
| SOFR-IORB | <+0.05 | 0.05-0.25 | >0.25 | **-0.04🟢 [6/3]** |
| KRE | >$69 | $65-69 | <$65 | **$69.98🟢** |
| WAL | >$78 | $72-78 | <$72 | **$80.74🟢** |
| OZK | >$50 | $45-50 | <$45 | **$49.21🟡** |
| APO | <$125 | $125-130 | >$130 x3 sessions | **$128.41🟡** |
| ARES | <$125 | $125-132 | >$132 x3 sessions | **$130.50🟡** |
| BIZD | >$13 | $12.50-13 | <$12.50 | **$12.70🔴** |
| Initial claims | <220k | 220-245k | >245k | **225k🟡 [5/30]**; shadow est **280k** |
| Continuing claims | <1.80M | 1.80-1.90M | >1.90M | **1.777M🟢 [5/23]** |

## HEARTBEAT Cadence / Ownership

**Approved Jun 4:** Prome owns `HEARTBEAT.md`. Update it after Prome boot-surface refreshes, regime-level changes, major decision-rail changes, or when it is >48h stale during the market week. Do **not** update daily by default just for hygiene.

## Blocking / Pending

| Pri | Decision / Work | Reference |
|---|---|---|
| ✅ | **HEARTBEAT cadence / ownership** — approved Jun 4. Prome owns updates after boot refreshes, regime changes, major decision-rail changes, or >48h stale during market week; not daily by default. | this file + `PROME/STATUS.md` |
| 🟠 | **Pathspec migration** — shared-repo race risk is real. Prome/SAM fixed; BRENT/HENRY/MARCO/OTTO/OZK/VIOLET/WALTER owner edits remain pending. | `PROME/PATHSPEC_MIGRATION_STATUS.md` |
| 🟠 | **TLT supersession / CPI gate** — May 22 TLT roll ticket is superseded. Jun $85P are Will-handled catalyst salvage; Sep add waits for CPI confirmation. | `PROME/ACTIVE_DECISIONS.md` + `AGENTS/HENRY/outbox/2026-06-03_to-PROME_tlt-ticket-superseded.md` |
| 🟠 | **Old trade rails / non-TLT 6-18 cluster** — remaining May 22-26 `BROKER_PENDING` / trigger language is **verification-required**, not actionable, until broker/Will reconciliation. | `PROME/ACTIVE_DECISIONS.md` |
| 🟠 | **Position-state reconciliation pass** — separate future task if Will asks; do not mix with boot/heartbeat cleanup. | `PROME/ACTIVE_DECISIONS.md` |
| 🔵 | **PROME execution-rails design** — HYG roll Jun→Dec died for lack of mechanism; keep as design debt, not an immediate trade instruction. | BROCK LESSONS #16 / `PROME/ACTIVE_DECISIONS.md` |

## Pointers

- Recent OpenClaw continuity → `PROME/HANDOFF.md`
- Current Prome working state → `PROME/SCRATCH.md`, `PROME/TODAY.md`, `PROME/STATUS.md`, `PROME/FLEET_SCAN.md`
- Active decisions safety index → `PROME/ACTIVE_DECISIONS.md`
- Pathspec migration tracker → `PROME/PATHSPEC_MIGRATION_STATUS.md`
- Agent state → `AGENTS/<NAME>/STATUS.md`
- WALTER Iran anchor → `AGENTS/WALTER/anchors/IRAN_WAR.md` (refreshed Jun 2; re-check if Iran tape becomes decision-relevant)
- SENTRY feed automation → `.github/workflows/feeds.yml` (scheduled pushes disabled Jun 2; manual dispatch only)
- News sweep / routing owner → WALTER owns signal/news routing; Prome owns tasking, rails, synthesis
- BOND matrix v2 deployment (June 9-11) → `AGENTS/BOND/proposals/MATRIX_V2_DRAFT_prome-spawned.md`

## Skip

Late night (11pm-8am ET): urgent only. Weekend: light monitoring.
