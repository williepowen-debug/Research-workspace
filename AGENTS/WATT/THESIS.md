# WATT — THESIS (per-channel transmission tables)

**The one-line thesis:** AI-capex data-center load is colliding with a supply-constrained grid, turning wholesale power cost into a first-order AI-buildout FCF input, an industrial-cost channel, and a consumer pass-through — with grid-emergency events as the live tripwire and capacity-auction structure as the slow, high-conviction backbone.

*Richness lives here; STATUS.md carries the live 5-pt matrix + reads. Each channel is `event → mechanism → repricing` with a stage table (state ∈ confirmed / open / falsified).*

---

## P1 — Stress → price (the live tripwire)

| Stage | Mechanism | State |
|---|---|---|
| 1 | Heat dome / cold snap / generator outage → load spike or supply loss | open (seasonal) |
| 2 | Reserve margin erodes → PJM issues emergency-procedure postings (warnings → EEA1 → EEA2) | open (1 realized: EEA2 7/3) |
| 3 | Reserve shortfall → RT/DA LMP spikes (to scarcity pricing / cap) | open (LMP leg not yet wired — PJM_API_KEY pending) |
| 4 | Sustained high power cost → industrial curtailment + data-center opex/uptime risk (§202(c) curtailment precedent) | confirmed precedent (7/3 DOE order) |

**Repricing:** IPP power-generator equities (upside on scarcity), industrial power-cost margin compression, neocloud FCF drag. **Confirms/breaks this channel alone:** an EEA2+ event with an LMP spike confirms; a full mild summer with no emergency postings kills the *live read* (migrates to P2/P3, does not kill thesis).

## P2 — Structural capacity cost (the backbone — FIRED)

| Stage | Mechanism | State |
|---|---|---|
| 1 | Data-center load growth outpaces new generation + retirements | confirmed |
| 2 | PJM base residual auction (BRA) clears at the price cap | **confirmed ×2** (26/27 $329.17; 27/28 $333.44) |
| 3 | Cleared capacity falls short of the reliability requirement | **confirmed** (27/28 short 6,623 MW) |
| 4 | Capacity cost passes through to retail/industrial bills (ComEd/BGE/Dominion) | open (in train) |

**Repricing:** utility retail rate cases, industrial siting economics, consumer energy CPI (→ CARL). **Confirms/breaks:** the 28/29 BRA (~Dec-2026) — at cap again confirms structural; materially below cap with draining queues falsifies. This is the cleanest bidirectional flip.

## P3 — Data-center demand leg (couples to HEN-36) — GAP, needs first pull

| Stage | Mechanism | State |
|---|---|---|
| 1 | Hyperscaler + neocloud AI-capex → new data-center interconnection requests | confirmed (macro) |
| 2 | Interconnection queue depth balloons; IPPs guide load growth up | needs first pull (LBNL Queued Up; VST/CEG/NRG/TLN) |
| 3 | Queue > system peak-load growth → structural supply-demand imbalance | open |
| 4 | Power availability becomes the binding constraint on AI-capex deployment | open (the HEN-36 coupling) |

**Repricing:** IPP equities, power-availability as a gate on the ~$290B AI-capex FCF node (HENRY). **WATT owes:** the first interconnection-queue + IPP-load pull.

## P4 — Gas → power coupling (spark spread) — GAP, needs first pull

| Stage | Mechanism | State |
|---|---|---|
| 1 | Henry Hub gas price (BRENT owns) sets gas-fired marginal cost | open |
| 2 | Gas-fired unit sets the power clearing price → spark spread | needs first pull |
| 3 | Spread compresses/negative → gas-fired uneconomic → supply tightens further | open |

**Repricing:** the gas↔power handshake with BRENT; power-price floor. **WATT owes:** the first spark-spread read (Henry Hub from BRENT × PJM power price).

## P5 — PPA tape (tier-2, not yet in the live matrix)

Corporate PPA price trend → contracted-power cost for hyperscalers. Full tape paywalled (LevelTen/BNEF subscriber-only); proxy via the free LevelTen quarterly executive summary + IPP earnings-call PPA commentary. **Build only after P1–P4 prove out** (AEOLUS Tier-2 promotion pattern).

---

## Boundaries (reconcile-to-one-figure, don't silo)

- **AEOLUS** detects the weather event (C3: CDD/HDD, heat/freeze); **WATT** prices everything after. Shared power/temperature figure → one number, WATT canonical for power.
- **BRENT** owns Henry Hub gas; **WATT** owns the power curve + spark-spread coupling.
- **HENRY** owns the AI-capex FCF thesis (HEN-36); **WATT** supplies the power-cost line item.
- **CARL** owns consumer retail pass-through to CPI; **WATT** owns wholesale/industrial.
