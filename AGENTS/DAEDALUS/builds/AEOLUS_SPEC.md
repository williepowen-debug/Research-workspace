# BUILD SPEC — AEOLUS (climate → economy agent)

> 🗄 **DATED BUILD RECORD — states herein are as-of the build day; do NOT cite as current.** AEOLUS ran its first data pass 6/28 and holds L2 (25 commits/30d as of 7/22). Current truth = FLEET_MAP row + `upgrades/PRODUCTION_REVIEW_2026-07-22.md`.

**Status:** 🟢 EXECUTED — Will approved 2026-06-28; scaffolded + wired this session. AEOLUS is live (awaiting its own first data pass).
**Owner:** DAEDALUS (design + build) / Will (decisions)
**Created:** 2026-06-28 · **Branch:** `claude/climate-economy-agent-t8xdwj`
**Class:** Market-agent (forms theses, scores risk vectors, feeds trades) → graded against `BLUEPRINTS/market-agent.md`
**Name:** AEOLUS — Greek keeper of the winds, the weather-systems god. Fits the pantheon (DAEDALUS, PROME); distinct from all current agents.

---

## 1. Locked decisions (Will, 2026-06-28)

| # | Decision | Resolution | Consequence |
|---|---|---|---|
| Altitude | **Channels-first** | Anchor on 3–5 concrete transmission channels, each `weather/climate event → mechanism → tradeable repricing`. | The DARWIN antidote (PAT-001/002). No open-ended "watch all weather." |
| Horizon | **Both, tiered** | Tier-1 live tradeable-weather signal (weeks–months, → option expiries) over a Tier-2 structural-climate backdrop the live events confirm/break. | Live layer feeds trades; backdrop carries the slow thesis. |
| CORAL line | **Macro owner, CORAL keeps FL** | AEOLUS owns climate→economy globally; CORAL stays FL deep-specialist and reconciles FL numbers upward. | Mirrors CORAL/MARCO reconcile pattern. Minimal rewiring; no CORAL ref breaks. |
| Name | **AEOLUS** | — | — |

---

## 2. The channel set (channels-first core)

Each channel is a standing `event → mechanism → repricing` transmission line, NOT a topic to monitor. An empty channel with no live read is a failure signal (DARWIN lesson).

### Core 3 (launch with these — highest-conviction climate→repricing)

| # | Channel | Event → mechanism → repricing | Tradeable surface | Routes to |
|---|---|---|---|---|
| C1 | **Insurance / reinsurance** | Catastrophe losses → reinsurance rate-on-line ↑ → primary insurer solvency stress + coastal insurability collapse | Reinsurers, P&C insurers, FL/coastal carriers | CORAL (FL), REGINALD (bank exposure) |
| C2 | **Agriculture / food** | Drought·heat·flood → crop yield ↓ → grain & softs prices ↑ → food inflation + fertilizer demand | Ag commodities, food producers, fertilizer (revives FERT channel) | FERT (dormant—revive internally), MARCO (CPI bridge) |
| C3 | **Energy demand** | Heat dome → cooling/power demand ↑; polar vortex → heating demand ↑ (Uri-style nat-gas spike) | Nat gas, power, utilities | BRENT (energy), HAWK (geopolitical energy) |

### Tier-2 expansion (list now, build after core 3 prove out)

| # | Channel | Mechanism | Routes to |
|---|---|---|---|
| C4 | **Property / physical assets** | Chronic peril (SLR, wildfire, flood) → property values ↓ → mortgage/CRE/muni credit risk | CORAL, REGINALD, CREED |
| C5 | **Supply chain / logistics** | Drought (Panama Canal), low rivers (Rhine/Mississippi), storms → freight disruption → goods inflation | MARCO |

*Resolved 2026-06-28: Will promoted BOTH C4 and C5 from Tier-2 to core — AEOLUS now runs **5 core channels** (C1–C5). No Tier-2 expansion queued. Files updated to full core parity (transmission tables, thresholds, exit triad, matrix rows).*

---

## 3. Horizon tiers (both, tiered)

- **Tier 1 — live signal (weeks–months):** seasonal forecasts (NOAA/CPC), ENSO state (El Niño/La Niña), active storm tracking, hurricane-season outlook (CSU/NOAA), heat/freeze episodes. This is the layer that maps to dated option positions and the existing trade cadence.
- **Tier 2 — structural backdrop (multi-year):** insurance-market retreat, sea-level rise, chronic drought regions, water stress, climate migration. Slow thesis; the Tier-1 events are its live tests (EXPECTED_SIGNALS discipline — absence is data).

---

## 4. Blueprint instantiation (market-agent.md sections → AEOLUS)

| Blueprint § | AEOLUS instantiation |
|---|---|
| §1 Thesis structure | Channels = independent causal lines (C1–C3). Transmission-stage table per channel: `stage \| mechanism \| state: confirmed/open/falsified`. |
| §2 Convergence matrix | Universal 5-pt score per channel (5 🔴🔴 peril firing → 1 ⚪ benign), + local state, + independence column (shared antecedent: e.g. one ENSO state drives multiple channels — count once). |
| §3 Thresholds | Banded `Metric \| Yellow \| Orange \| Red \| Routes to →` (e.g. ACE index, reinsurance ROL, crop-condition %, HDD/CDD vs normal). Durable rules in CLAUDE.md, live read in STATUS w/ `[src M/D]`. |
| §4 Invalidation / exit | Channel-kill vs thesis-kill + migration (a benign hurricane season kills *that* channel, not the climate-stress thesis—it migrates to drought/heat). Session counts mandatory. |
| §5 Predictions | `PREDICTIONS.tsv` (seasonal-forecast & event calls) + archive + calibration. Weather is uniquely calibratable — forecasts resolve on a fixed clock. Strong fit. |
| §6 Cross-agent routing | Standing route-matrix (table in §2 above) + NEXUS_BRIEF writeback + outbox crisis-only. |
| §7 Disciplines | Mechanism-vs-thermometer (the climate mechanism is high-conf; the seasonal-forecast readout is confounded). EXPECTED_SIGNALS. |
| §8 BOTTOM LINE | Required, every session. |

---

## 5. File scaffold plan (what gets created on approval)

```
AGENTS/AEOLUS/
  CLAUDE.md            # built from market-agent.md blueprint, channel-instantiated
  STATUS.md            # live state + per-channel 5-pt + BOTTOM LINE
  THESIS.md            # the channel transmission tables (richness lives here)
  PREDICTIONS.tsv      # seasonal/event forecast ledger
  KB.tsv               # knowledge base (climate→econ linkages, sourced)
  inbox/  outbox/      # cross-agent messaging
  sources/             # research corpus, briefings
```

## 6. Wiring plan (the "build" job — gated on approval + idle targets)

1. Create `AGENTS/AEOLUS/` scaffold (above).
2. Add AEOLUS to `PROME/ROSTER.md` (market-agent, active).
3. Add to root `CLAUDE.md` active-agents line + transmission chain (`HAWK → BRENT`; add `AEOLUS → {BRENT, CORAL, MARCO}`).
4. Add to `AGENTS/_INDEX.md` roster + `_ENERGY.md` group (primary) w/ cross-links to Credit (CORAL) + Funding/Macro (food-CPI).
5. CORAL coordination note → `AGENTS/CORAL/inbox/`: AEOLUS now macro climate owner; CORAL keeps FL, reconciles upward. (CORAL is live → task-packet, not direct edit — PAT-004.)
6. Record build in `FLEET_MAP.tsv` (new AEOLUS row) + `EVOLUTION.md` changelog + any new `PATTERNS.tsv` lesson.

---

## 7. Proposal summary (What / Why / Effort / EV / First Step)

- **What:** A market-class climate→economy agent, AEOLUS, scoped to 3 core transmission channels (insurance, ag/food, energy demand) on a tiered weather/structural horizon.
- **Why:** Vacant seat; climate→price linkages are real, calibratable, and under-covered (only CORAL touches it, FL-only). Channels-first + tiered horizon makes it tradeable and drift-resistant.
- **Effort:** ~1 session to scaffold + wire (Phase 3 build pipeline, first real use). Channel content accrues over subsequent sessions.
- **Expected value:** A continuous climate-stress signal feeding BRENT (energy), CORAL (property/insurance), MARCO (food-CPI/migration) — plus standalone tradeable seasonal/event calls with a calibration scoreboard.
- **First step:** On approval — scaffold `AGENTS/AEOLUS/` from the market-agent blueprint with C1–C3 instantiated, then wire (steps 1–6).
