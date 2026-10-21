# WATT — THESIS (per-channel transmission tables)

**Last real data refresh: 2026-10-20** (P1/P3/P4 and stale live-state reconciliation; P2 auction/regulatory vintages remain July14/October12) · *prior: 2026-07-12 (rd-3)* — **⚠️ this file sat 36 days without a refresh while STATUS moved under it, and it contradicted STATUS on 9 load-bearing facts. All 9 are corrected below and each is marked ⟲.** *(Two-clock header adopted per PAT-044 + DAEDALUS D1/D6; the per-channel `[stamp]` lines exist so a reader — or a scanner — can date any single claim without dating the file. That absence is what let this file rot: it was **outside every check's range**, because a staleness checker keyed on STATUS could not see a file with no vintage of its own.)*

**The one-line thesis:** AI-capex data-center load is colliding with a supply-constrained grid, turning wholesale power cost into a first-order AI-buildout FCF input, an industrial-cost channel, and a consumer pass-through — with grid-emergency events as the live tripwire and capacity-auction structure as the slow, high-conviction backbone.

**Thesis refinement, 2026-08-04 (KB-WATT-058) — the mechanism on this axis is cost-per-year-of-DELAY, not cost-per-kWh.** A year of delay on a 1 GW AI data center costs **$201–1,283/MWh-equivalent** against US industrial retail of **$87.1/MWh** and PJM wholesale ~$48–67/MWh ⇒ **delay is 2.3×–14.7× the commodity.** The US is not overpaying for electricity; it is paying a large, invisible **carrying cost on capital that is built but cannot be energized.** **The bust channel is stranded TIME, not expensive power.** *(This does not replace the one-liner above — it says which term in it is load-bearing.)*

*Richness lives here; STATUS.md carries the live 5-pt matrix + reads. Each channel is `event → mechanism → repricing` with a stage table (state ∈ confirmed / open / falsified).*

> ⚠️ **PRECEDENCE:** where this file and `STATUS.md` disagree, **STATUS wins** and this file is the defect. STATUS is refreshed every session; this file is refreshed when the *mechanism* changes, which is rarer — so it must carry stamps, not assume freshness.

---

## P1 — Stress → price (the live tripwire) `[stamp 2026-10-20]`

| Stage | Mechanism | State |
|---|---|---|
| 1 | Weather / outage / export pressure changes deliverable supply versus load | Active mechanism beyond summer: October13–14emergency at ordinary~108GWload with~61GWoutages; October19advisory with~72GWoutageforecast [KB148/151/157]. No reserve-erosion attribution from planned outages alone |
| 2 | Operating constraint → emergency postings | Five tracked capacity episodes throughOct14; September17EEA2 nowverified atposting105532. Prior “two episodes, bothJuly” is historical; historicalC1MET from primaryposting+priorKB121REDtimings, rawreplayunavailable [KB160] |
| 3 | Deliverable-supply stress → wholesale price | DM2five-minuteoperationalread is live; Oct13max2327.04/29consecutiveREDintervals. Oct15–19noobservedRED, Oct20partialmax315.14through22:20. No settlement label; currentP1=5held until completeOct22grade [KB148/157] |
| 3b | Low-load price events: causal alternatives tested | FL10thincommitment and FL13hourlyramp hypotheses REFUTED Aug17 [KB086/087]; causeunexplained. Never inherit a refuted hypothesis as an open mechanism. Subhourly possibility was not directly tested; no successor registered |
| 4 | Powercost / curtailment authority → operator economics | IRAScore rejectedOct9; emergencyauthorityseparate. DOE202-26-50issuedOct12,termendedOct16,noextensionindexedOct20. PJMOct15states large-loadbackupunusedtodate, coveringOct13–14; no laternegative. Hedge share/cash impact unknown [KB140/152/158] |

**Repricing:** IPP power-generator equities (upside on scarcity), industrial power-cost margin compression, neocloud FCF drag.
**Confirms/breaks this channel alone:** summer dormancy was a historical channel state, reopened by September/October scarcity. Current P1=5 held; no early de-escalation before the complete October15–21window. Historical EEA2/RED overlap on September17 meets C1 on recorded evidence; no new live emergency or trade inferred.

> ⚠️ **BAND RE-SPECIFIED 2026-08-17 — the old rule fired on its LETTER and that is preserved, not erased.** The prior band, *"RT LMP >$1,000 sustained 2+ intervals,"* named **no interval length and no instrument**, so the same 8/16 event fires on the 5-min tape (19:50 + 19:55 consecutive ≥$1,000) and cannot fire at all on the verified hourly. **Recorded FIRED-ON-LETTER / MECHANISM-REFUTED.** Replacement, prospective only:
> **RED = LMP ≥$1,000 sustained 2+ CONSECUTIVE 5-min intervals AND (an emergency-class posting is live OR demand ≥97% of the trailing 24h peak).** Price alone = a **logged transient**, not a band. (L-29, KB-WATT-069.)

## P2 — Structural capacity cost (the backbone — FIRED, at MAX) `[stamp 2026-10-12 regulatory; 2026-07-14 auction]`

| Stage | Mechanism | State |
|---|---|---|
| 1 | Data-center load growth outpaces new generation + retirements | confirmed |
| 2 | PJM base residual auction (BRA) clears at the price cap | ⟲ **confirmed ×3** (26/27 **$329.17**; 27/28 **$333.44**; **28/29 $325 = AT its own cap (100%), cleared 2026-07-14**) ✅ *"97.5% of $333.44" RESOLVED 9/6 at PJM primary: $325 IS the 28/29 cap; PJM's "Down 2.5%" is the YoY cap change, mislabelled here as utilisation.* |
| 3 | Cleared capacity falls short of the reliability requirement | ⟲ **confirmed ×2 — two consecutive RTO-wide shortfalls** (27/28 short **6,623 MW**, the first in PJM history where the *entire* RTO fell short; **28/29 short 6,831 MW**). 28/29: 138,318 MW UCAP+DR procured, uncapped sim **$554.72** (ComEd $776.69), **$16.4B** vs ~$30B uncapped. ⚠️ Attribution caveat: the ~$6.3B-of-$16.4B data-center figure is the **Market Monitor's**, not PJM's — PJM isolates no % |
| 4 | Capacity cost → retail/industrial bills | Annual pass-through mechanism, amount/allocation unresolved. Latest boot retail backdropJuly2026industrial9.77c/kWh,residential18.31; not a measured 2028/29auction pass-through [KB157scope/report] |
| 5 | Cost allocation: ratepayers (Door A) versus new large loads (Door B) | **IRAS/BYONC rejected 10/9; definition/registry only accepted**. WATT-10 MISS; WATT-08 **~70%→~50%**, OPEN through 2027-06-30. Only proposed IRAS obligation removed; existing contracts, state tariffs and physical costs persist. Actual socialization unresolved. EL26-67 responses 11/16 with section 205 proviso (KB-140/141) |

**Repricing:** utility retail rate cases, industrial siting economics, consumer energy CPI (→ CARL).
⟲ **Confirms/breaks — CORRECTED, this was the dead flip.** *(The old text named the 28/29 BRA "~Dec-2026" as the flip — an auction that had already **resolved on 2026-07-14**. A falsification surface pointing at a past event is worse than none: it reads as live and can never fire. It also disagreed with STATUS, which had already re-pointed. That is the single worst defect this file carried.)*
**The live flip is now the 29/30 BRA (~mid-2027):** clears at cap again → thesis confirmed structural through the decade; clears **materially below cap AND with queues draining** → the structural leg is falsified. **Both conditions required** — a below-cap clear with queues still full is a supply response, not a demand collapse.
**Near-term flip resolved 10/12:** WATT-10 MISS on the October 9 IRAS/BYONC rejection. Consumer allocation risk gains relative weight; actual allocation remains unresolved. Only the proposed IRAS obligation was removed. Any refile can change the mechanism; companion backstop is not graded here.

## P3 — Data-center demand leg (couples to HEN-36) `[stamp 2026-10-20; demand discriminator July31 carried]`

| Stage | Mechanism | State |
|---|---|---|
| 1 | Hyperscaler + neocloud AI-capex → new data-center interconnection requests | confirmed (macro). **VULCAN owns capex→MW; WATT prices the resulting MW.** Capex-implied PJM data-center band **~14–37 GW (2024–2030)** [KB-VULCAN-016..019]. ⟲ **Superseded upward by VULCAN-06 (7/31):** aggregate FY26 capex **held or RAISED** — economic aggregate **~$735–760B** vs a $710–725B baseline (AMZN $200→**$220B**; MSFT ~$190B economic — the $175B headline is a finance→operating **lease reclass, not a cut**; GOOGL $195–205B; META $130–145B). **STANDING DOUBLE-COUNT GUARD:** never add IPP PPA-MW (VST 3,800+2,609, TLN 1,920), a filer's site MW, or company-stated GW to capex-implied MW — same hyperscaler dollars seen from different sides |
| 2 | Interconnection queue depth balloons; IPPs guide load growth up | **confirmed:** PJM's own 20-yr forecast = **32 GW total / 30 GW (94%) data-center-driven** peak-load growth by 2030 [PJM via DCD, 2025-08-12]; summer peak 2027 **160,451 MW** → 2046 >253,000 MW against ~182,000 MW current capacity. **IPP guidance REAFFIRMED, not raised** — that distinction is the next rung, not a technicality |
| 3 | Queue > system peak-load growth → structural supply-demand imbalance | ⟲ **open — and the ~23 GW gap is a CATEGORY difference, not a disputed estimate (L-18/L-22, 8/4).** **32 GW already IS the firm figure** — PJM's vetted, system-**COINCIDENT** peak growth. **55 GW is an aggregate of utility-REPORTED forecasts**, *not* an interconnection-queue nameplate figure. The residual is **non-coincidence + utility self-report duplication** — **NOT** a vetting haircut (PJM's 2026 trim cut summer-2028 peak 4.4 GW / 2.6%, of which large loads were **0.7%**) and **NOT** queue attrition (the *"~20% reach an IA"* / *"38 GW cancelled 2025"* stats are **GENERATION**-queue numbers — **wrong population**). **Curtailability is a RECLASSIFICATION, not a haircut:** NCBL went **voluntary**, is **NOT in effect**, and the 28/29 BRA cleared at cap AND 6,831 MW short without it ⇒ **capacity-obligation offset = 0 GW today.** **Agreed shared figure with VULCAN, live in its files verbatim:** *~55 GW aggregate utility-reported forecast / ~32 GW firm coincident-peak — two bases, one number each, never netted or averaged* |
| 4 | Power availability becomes the binding constraint on AI-capex deployment | ⟲ **confirmed by the buyers themselves (VULCAN-06, 7/31):** ≥2 of 4 megacaps name power/energy availability as the binding constraint — **MSFT** *"capacity constrained, demand continuing to exceed available supply,"* +1 GW added in-quarter, ~$80B Azure backlog partly power-gated; **AMZN** *"even at [$220B] we will still not have enough capacity to meet all the demand we have in 2026"*; **META** *"build tens of gigawatts this decade."* **NVDA is now investing in the bottleneck itself** — up to $3B into Lancium (4 GW live ERCOT, 15 GW pending), **with the last $1B contingent on grid-hookup thresholds** ⇒ someone has written *time-to-power* into a term sheet (KB-WATT-078) |
| 5 | **⚠️ NEW STAGE — the buildout acquires a RELIABILITY-COMPLIANCE cost** (added 8/17) | **Live regulatory process with dates.** PJM/Dominion's review of the **7/22 Ashburn** event (**~3,800 MW** of data-center load disconnecting in two waves, 2,970 + 1,099, after a mechanical failure took a 230 kV line out of service — largest such event in PJM history) has PJM *"evaluating potential enhancements to reliability requirements… **ride-through standards**"* to be set *"before the load comes on the system."* **FERC has ordered NERC to submit enforcement provisions by 2026-12-31; standards expected 2027.** ⇒ **a compliance cost landing on OPERATORS, not utilities** — degrades AI-capex ROI directly, and **VULCAN carries no such line.** ⚠️ **NOT SIZED** — no dollar figure, no per-MW estimate, no scope. ⚠️ Mechanism is **inverted vs the viral framing**: the disturbance came from the **ABSENCE** of load, so risk scales with **concentration + identical automation**, not demand growth (FL-WATT-09/11) |

**Repricing:** IPP equities; power-availability as a gate on the AI-capex FCF node (HENRY, HEN-36).
⟲ **Escalation trigger — CORRECTED for a SPENT branch.** The old text listed three live triggers. **The 55GW-corroboration branch FIRED on 2026-07-31 (VULCAN-06) and is SPENT — do not re-fire it.** *(Score ≠ triad: it took P3 3→4; it did not fire the exit rule.)*
**Remaining live triggers → 5:** interconnection queue **> 2× system peak load**, **OR** any IPP formally **RAISES** (not reaffirms) guidance.
**Queue rule, now measurable and still unmet:** ~**212,000 MW** of applications (829, as of May-2026, after FERC accepted PJM's **Expedited Interconnection Track on 2026-06-09**) vs the **160,451 MW** 2027 peak = **~1.32×**; it would take ~321,000 MW to trip. ⚠️ **SECONDARY source, PROVISIONAL, population unestablished** (whole active queue vs one cycle's intake vs EIT-eligible subset are three different denominators) — **do not publish the ratio cross-agent until pulled from a PJM primary.**
⚠️ **EXPECTED_SIGNALS running the WRONG way, logged as such (8/17):** the August EIA STEO cut **ERCOT 2027 load growth 14% → 6%** after Texas ordered an audit of every data centre in its queue (**474 GW** of requests, >1,800 projects, **>5× the state's record peak**; Batch Zero postponed). **But the cause is POLICY, not demand withdrawal** — the cut *follows* the pause — so it **confirms administrative rationing while disconfirming naive load-growth extrapolation.** **ERCOT, not PJM; ANALOGUE, NOT TRANSFER** — do not apply an ERCOT attrition rate here. 🔑 **474 GW against a <95 GW record peak cannot all be real demand: Texas has ordered the measurement of exactly the self-report inflation I attribute to PJM's 55 GW and cannot observe.**

**October20 P3 supply/queue reconciliation [KB159/162]:** Cycle1PhaseI168.6GW vs historicalintake220GW; currentactive-total/transitionremainder UNKNOWN, so old~250GW/1.56x is historical. Cycle-only1.051x uses older160.451GWforecastpeak and is not thetriad. Generationattrition is not cancelleddata-centerload. EITfirst3accepted2115MWplannedmid2029 are not online/firmsparecapacity. Amazon/Loughtonexecutionleads supportdelaymechanism only withsource/rebuttal/rights limits inSTATUS/report; no raisedIPPguidance or P3upgrade established.

## P4 — Gas → power coupling (spark spread) `[stamp 2026-10-20]`

| Stage | Mechanism | State |
|---|---|---|
| 1 | Gas benchmark sets gas-fired marginal-cost proxy | NG=F2.970datedOctober20observed22:29ET; vendor daily-closefield, contractroll/settlementclockunverified. Appalachianbasisunknown; provisional, not settledmarginalgas [KB161] |
| 2 | Gas→power clearing-price coupling | HR7 is EIA efficient-CCGTbenchmark, not measuredmarginalunit. Oct15–19RTonpeak49.7217,n958 less7xcurrentOctober20gas2.970 gives+28.93/MWh;HR8+25.96. Not matcheddailysettlements; no directionclaim versus differentstresswindow [KB161] |
| 3 | Sustained negative spark → uneconomic gas-fired operation | Open mechanism, NOT-FIRED on positivecurrentproxy. Need3+sessions on one consistentbasis; currentwindowproxy is not3matchedobservations. Heat-driven priceevents can widenmargins; do not assign everyevent a heatcause |

**Repricing:** the gas↔power handshake with BRENT; power-price floor.
⟲ **Data source — CORRECTED.** Primary is now **PJM Data Miner 2** (`rt_hrl_lmps` verified / `rt_unverified_fivemin_lmps` operational) × Henry Hub. The **EIA biweekly ICE file is demoted to backdrop** (~12-day lag) and must **never** be paired with same-day gas.
**Instrument correction discharged:** leg4 now refuses stale proxy pairing beyond3days and computes a DM2power-windowproxy; verified in October20boot/code. The old August “fix owed” sentence was stale. Basis/settlement and window-composition limits remain; no new instrument change this sweep.
⚠️ **BASIS CAVEAT:** RT on-peak LMP ≠ the ICE peak-period OTC print — **different products.** The two series are **not** interchangeable in a compression time-series, and a level change across them is a **basis change, not a market move** — never score it against the "compresses 50%" trigger.



## P5 — PPA tape (tier-2, NOT in the live matrix) `[stamp 2026-07-12 — unchanged, and that is correct]`

Corporate PPA price trend → contracted-power cost for hyperscalers. Full tape paywalled (LevelTen/BNEF subscriber-only); proxy via the free LevelTen quarterly executive summary + IPP earnings-call PPA commentary. **Build only after P1–P4 prove out** (AEOLUS Tier-2 promotion pattern). *No refresh needed: nothing about this channel has changed, and an unchanged stamp on an untouched tier-2 channel is the correct state — not rot.*

---

## Cross-channel: independence & the shared-antecedent guard

- **P1 and P4 share a heat-dome antecedent** — a hot spell drives both the demand spike and the gas burn. **Count the shared root ONCE**; they are not two confirmations.
- **P2 (auction structure) and P3 (buildout) are the two structural roots that carry the thesis while P1 rests** — ⛔ **but NOT "independent," and that label is WITHDRAWN** [CODEX external review 2026-09-06; L-48]. **PJM's auction reliability requirement is computed FROM the load forecast that P3 measures**, so the two share a root: a rising data-centre forecast raises the requirement that P2 then observes clearing short. They carry **complementary** information — actual offers and observed operations are real added evidence — but **a shortfall at auction and a rising buildout forecast are not two independent measurements of the same stress.** The convergence matrix's own "count the shared root once" rule was being applied to weather and not to this.
- ⚠️ **The 8/16 price event is independent of the summer-heat root** (low demand, no heat) — which is precisely why it is interesting and why it must not be added to the P1 heat-episode count.
- **Predictions WATT-02 (EEA2+ by 9/7) and WATT-06 (EEA-1+ by 8/15) share the summer-heat root** — they were never independent confirmations of each other.

## Mechanism vs thermometer (standing discipline)

The **structural capacity shortfall** (auctions at cap ×3, two RTO-wide shortfalls) is a high-confidence **MECHANISM**. Any single day's LMP print is a confounded **THERMOMETER**. **The thesis survives a mild week — and it has now survived a mild month.** ⚠️ The 8/16 spike is the thermometer at its most misleading: a historical low-demand price spike, later exceeded by September events.

## Boundaries (reconcile-to-one-figure, don't silo)

- **AEOLUS** detects the weather event (C3: CDD/HDD, heat/freeze); **WATT** prices everything after. Shared power/temperature figure → one number, **WATT canonical for power**. ⚠️ **Winter gate (8/12):** El Niño's sign is **DOWN for winter ENERGY (established)** and **NOT ESTABLISHED for winter PEAK** (n=2 analogues, split) — **2023-24 was the warmest US winter on record and PJM still peaked 134,777 MW on Jan 17.** Never register a winter P1 call of the form *"no EEA because El Niño."*
- **BRENT** owns Henry Hub gas; **WATT** owns the power curve + spark-spread coupling.
- **HENRY** owns the AI-capex FCF thesis (HEN-36); **WATT** supplies the power-cost line item.
- **CARL** owns consumer retail pass-through to CPI; **WATT** owns wholesale/industrial.
- **VULCAN** owns capex→MW conversion and AI-capex ROI; **WATT** prices the MW and owns the PJM docket.
- **MIDAS** owns uranium market structure; **WATT** owns the power-demand side of that seam (reactor restarts, data-center nuclear PPAs, load forecasts) — **reconcile to one figure before either publishes a uranium-demand number.**
