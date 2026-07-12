# WATT — THESIS (per-channel transmission tables)

**The one-line thesis:** AI-capex data-center load is colliding with a supply-constrained grid, turning wholesale power cost into a first-order AI-buildout FCF input, an industrial-cost channel, and a consumer pass-through — with grid-emergency events as the live tripwire and capacity-auction structure as the slow, high-conviction backbone.

*Richness lives here; STATUS.md carries the live 5-pt matrix + reads. Each channel is `event → mechanism → repricing` with a stage table (state ∈ confirmed / open / falsified).*

---

## P1 — Stress → price (the live tripwire)

| Stage | Mechanism | State |
|---|---|---|
| 1 | Heat dome / cold snap / generator outage → load spike or supply loss | open (seasonal) |
| 2 | Reserve margin erodes → PJM issues emergency-procedure postings (warnings → EEA1 → EEA2) | open (1 realized: EEA2 7/3) |
| 3 | Reserve shortfall → RT/DA LMP spikes (to scarcity pricing / cap) | **confirmed via proxy** (2026-07-12): EIA's free biweekly wholesale-price file shows a real $574.04/MWh (Orange) print on 7/1, retreating to $72.38 by 7/7. Official PJM Data Miner LMP still not wired (PJM_API_KEY pending) — this is a real-trade proxy, not the official series |
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

## P3 — Data-center demand leg (couples to HEN-36) — reconciled 2026-07-12 (rd-3)

| Stage | Mechanism | State |
|---|---|---|
| 1 | Hyperscaler + neocloud AI-capex → new data-center interconnection requests | confirmed (macro) — **VULCAN completed the capex→MW conversion (rd-3):** FY26 4-name capex ≈$710–725B (+77% YoY) maps to a **capex-implied PJM data-center band ~14–37 GW (2024–2030)** [KB-VULCAN-016..019]. WATT never converts dollars→MW itself (VULCAN's job); WATT prices the resulting MW. **Double-count guard (STANDING RULE):** never add IPP PPA-MW (VST 3,800+2,609, TLN 1,920) to capex-implied MW — same hyperscaler dollars, two views (capex = spend side, PPA-MW = utility-contract side) |
| 2 | Interconnection queue depth balloons; IPPs guide load growth up | **confirmed:** PJM's own 20-yr forecast = 32GW total / 30GW (94%) data-center-driven peak-load growth by 2030 [PJM via DCD, 2025-08-12] — **capex-FUNDED (upper half of VULCAN's 14–37 GW band)**; all 4 IPPs (VST/CEG/NRG/TLN) reaffirmed/beat FY26 guidance, none cut, Q1-2026 |
| 3 | Queue > system peak-load growth → structural supply-demand imbalance | open — **divergence now RECONCILED (rd-3):** WoodMac's 55GW/2030 (utility-self-reported, White & Case 2026-03-11) sits **~50% ABOVE VULCAN's ~37 GW capex-band top** → NOT funded by current capex guides; needs 2028–30 capex acceleration, PJM-share >35%, or is utility self-report inflation. The ~23GW excess being *unfunded* strengthens the utility-over-commitment credit angle (routed REGINALD). *Corrects rd-2's "capex leans toward 55GW" — capex funds 32, not 55.* **Discriminator: the 7/22–7/31 megacap earnings cluster (VULCAN-06 resolver, VULCAN's clock)** — a big upside capex surprise there begins funding the 37→55 gap |
| 4 | Power availability becomes the binding constraint on AI-capex deployment | open (the HEN-36 coupling); new hyperscaler PPAs (VST 3,800MW AWS + 2,609MW Meta; TLN 1,920MW Amazon) confirm contracted demand — but per the double-count guard these are the utility-contract *view* of the same capex dollars, NOT additive to the 14–37 GW band |

**Repricing:** IPP equities, power-availability as a gate on the ~$290B AI-capex FCF node (HENRY). **Escalation trigger:** interconnection queue > 2× system peak load, OR any IPP formally *raises* (not just reaffirms) 2026 guidance, OR the 55GW upside gets capex-corroborated at the 7/22–7/31 cluster.

## P4 — Gas → power coupling (spark spread) — first pull complete 2026-07-12

| Stage | Mechanism | State |
|---|---|---|
| 1 | Henry Hub gas price (BRENT owns) sets gas-fired marginal cost | live: NG=F $2.94/MMBtu (7/10), down ~10% over the week even as power spiked [yfinance] |
| 2 | Gas-fired unit sets the power clearing price → spark spread | **live, first pull:** baseline (7/7) +$49.53/MWh; spike-day (7/1) +$551.50/MWh — both wide and positive. Heat-rate assumption (7.0 MMBtu/MWh, efficient CCGT) is ASSUMPTION-tier, not yet calibrated to the actual PJM gas fleet (EIA-923 would sharpen this) |
| 3 | Spread compresses/negative → gas-fired uneconomic → supply tightens further | open — **mechanism refinement:** the heat-stress regime that drives P1 *widens* the spread (gas captures scarcity rent as marginal price-setter) rather than compressing it. Compression is a *different* regime this thesis hasn't tested yet — likely mild-weather oversupply or high-renewable-curtailment days, not the heat-dome/P1 regime |

**Repricing:** the gas↔power handshake with BRENT; power-price floor. **Data source:** EIA's free biweekly wholesale-price file (`eia.gov/electricity/wholesale`) × yfinance Henry Hub (NG=F) — no PJM_API_KEY required for this proxy-grade read.

## P5 — PPA tape (tier-2, not yet in the live matrix)

Corporate PPA price trend → contracted-power cost for hyperscalers. Full tape paywalled (LevelTen/BNEF subscriber-only); proxy via the free LevelTen quarterly executive summary + IPP earnings-call PPA commentary. **Build only after P1–P4 prove out** (AEOLUS Tier-2 promotion pattern).

---

## Boundaries (reconcile-to-one-figure, don't silo)

- **AEOLUS** detects the weather event (C3: CDD/HDD, heat/freeze); **WATT** prices everything after. Shared power/temperature figure → one number, WATT canonical for power.
- **BRENT** owns Henry Hub gas; **WATT** owns the power curve + spark-spread coupling.
- **HENRY** owns the AI-capex FCF thesis (HEN-36); **WATT** supplies the power-cost line item.
- **CARL** owns consumer retail pass-through to CPI; **WATT** owns wholesale/industrial.
