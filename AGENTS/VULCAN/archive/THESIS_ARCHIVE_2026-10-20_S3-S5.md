## S3 — AI-capex → power demand (feeds WATT) — first sizing done 2026-07-12 (round 2)

| Stage | Mechanism | State |
|---|---|---|
| 1 | AI-capex → datacenter buildout → compute demand | confirmed (macro) |
| 2 | Compute demand → interconnection + grid MW load | **sized: capex-implied ~8-11 GW/yr global 4-name flow (2026) — conversion below** |
| 3 | Grid can't supply → power becomes the binding constraint on AI deployment | open (the WATT coupling) — WATT's P2 capacity leg already FIRED on its side. **🆕 8/27 — THE PORTS-PIKE LOAD NOW HAS A FILED PHASE SCHEDULE, WHICH IS BETTER EVIDENCE THAN A NAMEPLATE NUMBER: nine data centers, first in service expected NVDA FY2029 (~calendar 2028), ~4.25 GW IT load committed + ~3.8 GW optional, PJM territory** [10-Q acc `0001045810-26-000075` Note 10; press release *"Secured land, power and shell capacity through a partnership with SB Energy at the PORTS-Pike Technology Campus in Ohio"*]. **This DATES the load addition that pushes S3 away from its channel-death** (S3 dies if interconnection clears faster than load is added). ⚠️ **FY2029 is NVDA's fiscal year (ends ~late Jan) ⇒ ~calendar 2028 — consistent with the 8-K's "in-service from 2028", NOT a contradiction.** ⚠️ **A dated, phased, contractually-committed load is exactly the quantity the 8/13 nameplate-vs-firm seam was struggling to pin — route WATT.** [KB-126] |

**Repricing:** hands WATT the demand driver (WATT prices the grid response); power-availability as a gate on AI-capex. WATT owns the power price (reconcile to one figure).

### CAPEX → MW CONVERSION (first pass, 2026-07-12 — every step ASSUMPTION-tier unless noted)

**Inputs:** S1 baseline agg FY26 capex guide $710-725B (4-name, EMPIRICAL, KB-009) — ⚠️ **SUPERSEDED 7/31: the realised aggregate is ~$735-760B economic. This input is the FROZEN 7/12 baseline and every result below inherits it (~3-5% low). Re-derive before citing any GW figure; do not quote the band as current.** · capex intensity **$50-60B per GW** all-in AI infrastructure [Jensen Huang, ~May 2026 vintage, NVDA hardware >half of that sum — **incentive-flagged: vendor-sourced**, Barclays has publicly stress-tested the "Jensen math"; Stargate corroborates ~$50B/GW ($500B/~10GW target)] · AI-related share of hyperscaler capex **~70-75%** [industry estimate vs top-5, late-2025/early-2026 vintage; KB-017].

| Step | Calculation | Result | Tier |
|---|---|---|---|
| 1. AI-specific 2026 capex (4-name) | $710-725B × 70-75% | **$500-545B** | ASSUMPTION (share) |
| 2. Implied new AI capacity, global, 2026 flow | $500-545B ÷ $50-60B/GW | **~8.3-10.9 GW/yr** | ASSUMPTION ($/GW) |
| 3. Gross-up for non-big-4 (Oracle/Stargate/xAI/neoclouds/China; 4-name ≈ ~70% of global AI capex) | ÷ 0.7 | **~12-16 GW/yr global all-players** | ASSUMPTION |
| 4. Cumulative 2024-2030, 4-name (2024-25 ~$630B actuals + 2026 guide + FLAT-at-2026 2027-30 — the conservative branch) | ~$4.2T × ~70% ÷ $50-60B/GW | **~48-62 GW global (4-name)** | ASSUMPTION (flat-capex branch) |
| 5. All-players global, 2024-2030 | ÷ 0.7 | **~68-89 GW** | ASSUMPTION |
| 6. US share (~55-60%) → PJM share of US DC (~25-35%, VA data-center alley) | sequential | **~9.5-19 GW PJM, hyperscaler-AI only** | ASSUMPTION ×2 |
| 7. PJM total-DC (hyperscaler-AI ≈ 50-70% of PJM DC growth; rest = colo/enterprise/crypto) | ÷ 0.5-0.7 | **~14-37 GW PJM total-DC, 2024-2030** | ASSUMPTION |

**Honest-uncertainty note:** 5+ stacked assumptions — the band is wide by construction and the deliverable is *which forecast sits inside the band*, not a point estimate. Known biases: (a) GPU-refresh into existing shells inflates $ without net-new MW (overstates GW); (b) capex-year ≠ energization-year (12-24mo lag — 2026 capex powers 2027-28 load); (c) flat-capex 2027-30 is conservative — the 2026 guide is +77% YoY, and if that growth persists the band shifts materially up; (d) S2's component-cost inflation means some capex $ is price, not capacity (same nuance as the S1 read — cuts implied GW further).

### RECONCILIATION vs WATT's P3 range (read-only consume of AGENTS/WATT/, 2026-07-12)

WATT's two seam datums [WATT STATUS P3 row, KB-WATT-012..014]: **PJM-official 32 GW** total peak-load growth 2024-2030, 30 GW (94%) data-center-driven [PJM via DCD, pub 2025-08-12] vs **WoodMac/utility-self-reported 55 GW by 2030** (100 GW by 2037) [via White & Case, pub 2026-03-11] — a 23 GW / 70% unreconciled gap.

> ## 🔴 THE 7/12 VERDICT BELOW IS SUPERSEDED TWICE — READ THIS BOX FIRST (added 2026-08-21)
>
> **This section sat 18 days asserting the OPPOSITE of STATUS.** Two things resolved it and neither was written back here:
>
> **① 2026-07-31 — VULCAN-06 resolved HIT, and it UPGRADED the verdict.** The discriminator named below (the 7/22-7/31 capex cluster) fired on the **(a)** branch: all four guides RAISED (agg **~$735-760B** economic vs the $710-725B baseline) **AND** ≥2 of 4 named power/energy as a binding constraint (MSFT *"capacity constrained, demand exceeds supply"* +1GW +~$80B power-gated Azure backlog; META *"tens of gigawatts this decade"*; AMZN *"still not enough capacity"*). ⇒ **the raised capex + power-as-binding-constraint SUPPORT the WoodMac 55 GW HIGH side.** Routed to WATT 7/31. **The 7/12 "supports 32 GW, not 55" verdict is retired.**
>
> **② 2026-08-13 — the WATT seam closed, and it dissolves the either/or the verdict was built on.** **32 GW and 55 GW are not two rival forecasts of one quantity — they are two different quantities, and both are right:** ~~**~55 GW = nameplate interconnection ceiling**~~ 🔴 **WORDING CORRECTED 2026-09-06:** **~55 GW = AGGREGATE UTILITY-REPORTED FORECAST** (self-reported, non-coincident, contains duplication) **· ~32 GW = FIRM COINCIDENT-PEAK contribution** (PJM-vetted). ⚠️ **Adopt verbatim; never net, never average them; and neither is an interconnection-queue nameplate figure — the ~250 GW active generation queue is a THIRD, separate population.** Curtailability offset is **0 GW today** (NCBL went voluntary, not in effect). ⇒ The question *"is it 32 or 55?"* was **mis-specified** — which is also why the (c) "double-counted/speculative requests" branch below is not the artifact explanation it looked like: nameplate legitimately exceeds firm without anything being double-counted. [KB-087]
>
> ⚠️ **The arithmetic below is ALSO computed off the superseded $710-725B baseline** (actual ~$735-760B, VULCAN-01 HIT 7/31), so every step from AI-specific capex down to the ~14-37 GW band is ~3-5% low. **The band is retained as the 7/12 record, not as a current read** — re-derive before citing.

**~~VULCAN's verdict: hyperscaler-guided capex supports the LOW-to-MID (PJM-official) forecast, not the high one.~~** *(7/12 verdict — RETIRED 7/31, see box above.)* PJM's 32 GW sits inside the upper half of the capex-implied ~14-37 GW band; WoodMac's 55 GW sits ~50% ABOVE the band's top. For 55 GW to be real funded demand, at least one of: **(a)** aggregate capex keeps growing high-double-digits through 2028-30 (2026's +77% raise is a trajectory, not a step), **(b)** PJM's share of the US buildout rises above ~35%, or **(c)** the 55 GW contains double-counted/speculative utility interconnection requests (same project shopped to multiple utilities — a known inflation mechanism in self-reported pipelines; this branch resolves the gap as *artifact*, not demand). **The (a)-vs-(c) discriminator is on VULCAN's clock: the 7/22-7/31 capex-guide cluster.** Continued raises + FY27 acceleration language → (a) gains, 55 GW path stays live; capex plateau/cut → 32 GW is the funded ceiling and the WoodMac excess is likely artifact. Registered as **VULCAN-06** (resolves 7/31).

**Shared-antecedent discipline:** this couples S3's resolver to S1's catalyst — the capex root is shared (per STATUS independence note); a capex disappointment fires BOTH, count the root once. **Double-count guard for the seam:** WATT's IPP PPA datums (VST 3,800MW AWS + 2,609MW Meta; TLN 1,920MW Amazon) are the *utility-side reflection of the same hyperscaler capex* — when reconciling to one figure, PPA-MW and capex-implied-MW are two views of one demand, never additive.

## S4 — Supply-chain / geopolitics (the chokepoint) — first pull done 2026-07-12

| Stage | Mechanism | State |
|---|---|---|
| 1 | Leading-edge fab capacity concentrates at TSMC-Taiwan | confirmed (structural) |
| 2 | US/China export controls tighten the equipment + chip flow | **two-sided, not one-directional — see below.** **🆕 8/27 — AND THE NVDA LEG HAS GONE TO ~ZERO, WHICH RELOCATES THE CHANNEL'S EXPOSURE RATHER THAN QUIETENING IT:** Hopper DC shipments to China were **<1% of Data Center revenue** in the quarter, and the Q3 outlook **assumes no China DC compute revenue at all** [8-K acc `0001045810-26-000073` Ex-99.1/99.2]. ⇒ **Further export-control escalation now has near-zero incremental effect on NVDA REVENUE — the risk is already realised at this issuer — so an S4 shock from here must surface through the EQUIPMENT and FOUNDRY legs (ASML/AMAT/LRCX, TSMC), not through NVDA.** ⚠️ **Do NOT read "NVDA is insulated" as "S4 is quieter": the same shock now lands on different instruments, and TSMC monthly revenue (next ~2026-09-10) is the one this desk actually holds.** [KB-125] |
| 3 | Equipment ban / fab cutoff / Taiwan kinetic → supply shock across the chain | open; TSMC revenue shows no stress yet |

**Repricing:** the semi-supply consequence of ZHAO's China events + HAWK's Taiwan geopolitics. **First pull (2026-07-12):** TSMC May'26 monthly revenue +30.1% YoY (record) — no chokepoint stress on the revenue line; ~~June print delayed to 7/13/26 (typhoon), VULCAN-05 resolves there.~~ ⚠️ **RESOLVED — VULCAN-05 HIT 7/17** (June NT$442.68B, +6.2% MoM; ⚠️ cite **H1 +35.6% YoY**, NOT the +67.9% headline, which is a base effect off a June-2025 trough). **🆕 CURRENT READ, pulled 2026-08-21 — the section above is the 7/12 record, not the live number: TSMC July 2026 revenue NT$467,580M, +5.6% MoM, +44.7% YoY; Jan-Jul +37.0% YoY** (up from H1's +35.6% — a mild acceleration) [**SEC 6-K acc `0001046179-26-000471`, filed 8/10**, own EDGAR pull]. **S4 revenue line clean; NOT-FIRED. Next print ~2026-09-10 — this is a MONTHLY series and must be pulled monthly** (it sat 5 weeks stale through two sessions; the reassuring number is why nobody noticed). [KB-100] **The export-control picture is NOT simply tightening** — it is genuinely two-sided: the US *eased* (BIS approved H200 sales to China 1/13/26, ~10 buyers cleared by 5/14/26, though paired with a 25% tariff), while Taiwan is *tightening* from the other end — weighing a Foreign Trade Act amendment to criminalize unauthorized AI-chip exports to all of China (undated), with a first concrete enforcement event 7/1/26 (Keelung court detained 3 Super Micro/Albatron execs — Taiwan's first criminal AI-chip-diversion probe). No fixed-date resolver exists for the Taiwan legislative side; monitoring item. Kinetic Taiwan = HAWK cross-flag; China macro = ZHAO — **route-out: neither may have this dated 7/1 event logged from the semiconductor angle.**

### 🆕 2026-08-21 — S4 IS INSTRUMENTED, AND IT NOW HAS 20 MONTHS OF RETAINED HISTORY

> **2026-09-11 (21 months):** August 6-K swept — NT$514,806M, +10.1% MoM, +53.3% YoY, **cumulative Jan-Aug +39.3%** (from +37.0%) ⇒ `decel` NOT met, no-stress, re-acceleration continues [KB-157]. Consistent with VULCAN-14 reading HIT at 9/30; graded then, not banked now.
> **2026-10-08 (22 months):** September 6-K swept (filed 10/08) — NT$511,857M, −0.6% MoM, +54.6% YoY, **cumulative Jan-Sep +41.1%** (from +39.3%) ⇒ `decel` NOT met, no-stress, a second month of re-acceleration [KB-195]. Stage 3 stays *open; TSMC revenue shows no stress yet*.

*Added at closeout step 2b. ⚠️ **This is an ADDITION, not a correction** — the three 2b
questions were run against this section and it contradicted nothing: stage 3's "open; TSMC
revenue shows no stress yet" agrees with STATUS, VULCAN-05 was already struck as resolved,
and the 7/12 May'26 +30.1% first-pull figure is reproduced exactly by the new series. The
section was thin, not wrong.*

**`tools/tsmc_watch.py` → `workbook/S4_SERIES.tsv`** — TSMC monthly revenue from its own SEC
Form 6-K (issuer-primary, CIK 0001046179), 20 months backfilled Dec-2024 → Jul-2026, every
row validated by three zero-free-parameter recomputations. **S4 previously had no instrument
and no retained history at all** — which is why it was found **35 days stale on a MONTHLY
series** on 2026-08-21.

**What the history says, and it could not be said before today:**

| | 2025 | 2026 YTD |
|---|---|---|
| Cumulative YoY path | **43.5 → 31.6** — monotone decel, 8 consecutive months | **36.8 → 29.9 → 35.1 → 29.9 → 30.0 → 35.6 → 37.0** — oscillating, no run >1 |
| Shape | a genuine decelerating year | **choppy, and RE-ACCELERATING into July** |

🔑 **The read: ~~2026's cumulative +37.0% now sits ABOVE full-year 2025's +31.6%~~ ⚠️ **PERIOD-MISMATCHED — CORRECTED 2026-08-21 (evening self-check). That set a 7-MONTH YTD against a 12-MONTH FULL YEAR.** Like-for-like at July, **2026 (+37.0%) is BELOW 2025 (+37.6%)**, and 2026 sits below 2025 at **every aligned month except January**. 🔑 **What IS true, and it is the better read: 2026 re-accelerated WITHIN the year — Apr +29.9% → Jul +37.0%, +7.1pp — and has narrowed the gap to 2025's pace from −13.6pp (Apr) to −0.6pp (Jul). It has very nearly CAUGHT 2025, not overtaken it.** The S4 verdict is unchanged (NOT-FIRED; the red band is *decline* and growth is ~37%), but the SHAPE claim was overstated. [`finding_cross_entity_comparison_needs_same_perimeter`]. The
deceleration that ran through all of 2025 did not continue — it reversed.** S4's revenue line
is not merely "clean", it is **re-accelerating**, which strengthens the NOT-FIRED verdict
rather than just failing to contradict it. ⚠️ **Cite the cumulative** — monthly YoY ranges
**16.9% to 67.9%** across these 20 observations (a 51pp spread), so any single month's YoY is
close to meaningless on its own. That spread is the quantified version of the standing
"June's +67.9% was a base artifact" warning.

⚠️ **Two instrument caveats that belong with the read, not buried in the tool:**
- **The RED band (monthly YoY < 0) has occurred 0 times in 20 months.** It is *reachable*
  (proven by fixture 8/21) but **unobserved in-sample**, so it carries no base rate. Do not
  present its silence as evidence of stability.
- **The YELLOW `decel` band fires 7/20 (35%)** even after being tightened to require 2+
  consecutive months. It is honest — TSMC really did decelerate for most of 2025 — but a
  band lit a third of the time is a "look", never an "act". The actionable bands are
  **flat** and **decline**.

## S5 — AI-infra financing — **PROMOTED tier-2 → CORE 2026-08-03** (Will-approved)

| Stage | Mechanism | State |
|---|---|---|
| 1 | AI buildout is funded by debt, off-BS leases and vendor/lessor guarantees rather than operating cash | **confirmed, and larger than the headline names** — ORCL alone: **$260B** off-BS DC lease commitments (FY27-29 commencement, 15-19yr) + **$3.3B** lessor-borrowing guarantee **maturing Sept-2026**; FY26 capex $55.7B vs $32.0B OCF = **−$23.7B** structural gap [FY26 10-K Note 9] 🆕 **Q1 FY27 (8-K 9/10, read 9/11) [KB-156]: capex $28.5B in ONE quarter, FCF −$5B, a $20B ATM equity sale completed, $11.4B of customer prepayments with a significant financing component — the financing MIX moved to equity + customer money in the quarter capex tripled; ~~the $3.3B guarantee is absent from the release and is a 10-Q question (latest ~9/19).~~** 🆕 **2026-09-25 (step 2b) — the 10-Q QUESTION IS SPENT: the Q1 FY27 10-Q (filed 9/11, read 9/25) shows off-BS DC leases $260B → $288B in ONE quarter, and the $3.3B guarantee has ZERO mentions ⇒ its status is UNKNOWN, not resolved; notes FV 84.6% of carrying [KB-168]. And on 9/24 ORCL invoked FORCE MAJEURE on Project Jupiter to defer rent against power delay — the risk-transfer leg of this row exercised for the first time [KB-167/174, FL-VULCAN-13].** *(The $260B above is the FY26 10-K baseline, kept as the record; the current level is $288B.)* |
| 2 | The obligations sit where no leverage ratio computes them | **confirmed** — on balance sheet these look like ordinary levered tech issuers; ⚠️ **CORRECTED 2026-08-27 at closeout step 2b — THIS CELL WAS 31× LOW AND HAD BEEN SINCE 8/17.** ~~entire filed guarantee book **$3.5B gross / $712M escrowed**~~ ⇒ **$108.5B** ($3.5B AI-cloud land/power/shell + **$105.0B** SB Energy residual-value guaranties, 8-K `0001045810-26-000069` 8/17 + 10-Q `0001045810-26-000075` 8/26). **The ~$250B aggregate is still filed NOWHERE and that half of the claim stands** — but *"the filed book is only $3.5B, so the headline node is the wrong one"* no longer follows from it, because the filed book is now large. 🔑 **The two halves failed independently and only one died** [`finding_impeachment_must_be_scoped_to_the_claim_not_the_source`]. ⚠️ **Why it survived the 8/27 morning pass: that pass swept for the NVDA PEAK figure and for S5's live reads, and this is a STAGE-TABLE cell — a content-specific sweep certifies the content it searched for, never the file** [KB-130, one hop out and pointed at the same defect] |
| 3 | Financing capacity is contractually tied to operating inputs, not just leverage | **confirmed, filed** — CRWV's $8.5B DDTL 4.0 re-marks its sizing model for **hedge/SOFR rates and POWER only** (§5.25 Power Cost Protection; §5.23 ≥95% hedging), resolving to **Projected DSCR ≥1.20x** (1.15x maint.), + a **"Negative NOI Event"** repaying **two months before** the first projected-negative month ⇒ **power price → borrowing capacity.** *(Couples S3.)* |
| **3b** | **Regulators write IG thresholds into utility tariffs ⇒ a standing liquidity demand independent of capex** | **🔑 THE INDEPENDENCE LEG. Live.** WI PSC rule (**April 2026**): any DC developer rated **below A-** posts guarantees before service — **>$100M/yr** in deposits/LCs. **NOT downgrade-triggered:** ORCL was already **BBB**, the rule predates the 7/9 cut by 3 months, and ORCL **sued 6/19**. ⇒ **rating LEVEL, not migration, is binding** |
| 4 | Price of access repricing before access is lost | **elevated** — CRWV $2.6B DDTL **cleared +100-125bp wide of talk** (S+550/OID 96-97/**YTM 10.44%**) **at full size**; NVDA 5Y CDS **40→68→~82bp record [all 7/27]**, ORCL **~210-215bp record [7/27]**; GS/JPM **shortable** basket **319bp [7/23]** (18 equal-wtd **neoclouds**) vs HY 279. ⚠️ **CDS AND THE BASKET ARE GENUINELY-UNAVAILABLE TO THIS DESK** (Markit/Bloomberg paywall) — **LIQUID, who owns the spread tell, carries the same 7/27 prints**, so this is a data-access limit on both desks, not a VULCAN collection gap. **Stamp them [7/27]; never state as current.** **🆕 WHAT IS REFRESHABLE, PULLED 8/21: HY OAS 275bp [8/20] — TIGHTER than the 281bp my files carried — and IG OAS 81bp [8/19]. The aggregate-benign leg is intact and slightly STRONGER.** ⚠️ **And the equity counter-leg DECAYED: CRWV +4.8% / ORCL +4.5% on the same 8/3 basis** (was +23.9% / +10.2% at 8/13; do NOT quote "−15.5% since 8/13" — 8/13 is effectively CRWV's peak, so that is extremum-anchored, **L-17**). [KB-104] |
| 5 | Access actually lost → project halts / default | **NOT reached** — no default, no pulled deal, aggregate IG/HY benign, ORCL contesting in court rather than failing to post |

**Repricing:** AI-infra credit spreads (→ **LIQUID**, who owns the spread tells), private-credit marks (→ BROCK), FCF/valuation (→ HENRY), project feasibility (→ WATT).

### Why it was promoted, and the one argument that carried it

The weak case is volume — S5 accreted more filed, dated material in a week than some core channels hold. **That alone would not justify promotion; it would justify a longer sub-read.**

**The argument that carried it: S5 demonstrated it can fire while S1 is NOT firing.** The Oracle collateral requirement is live *while hyperscaler capex is being raised* — it fires on the **balance sheet and the tariff**, not on capex direction. A channel that can only fire when S1 fires is not independent (that is precisely why obsolescence and the returns-case stayed **sub-reads**). S5 cleared that bar; they have not.

⚠️ **Independence is PARTIAL and must be stated every time:** the **ROI-disappointment leg** still shares S1's antecedent — an AI-capex disappointment drives S1 + S3 + S5 at once and **that root is still counted ONCE**. Only the **financing-structure/regulatory leg** is independent.

🔴 **2026-10-09 RECONCILE (closeout step 2b): S5 IS NOW SCORED 4 — the standing rule FIRED on the letter (n=1): Firmus (NVDA-backed AU AI-DC developer) WITHDREW its ~US$4.9B ASX IPO at a ~US$30B valuation, citing market volatility, and pivots to private capital [KB-209]. Graded PULLED under the 9/25 SB Energy pre-statement; Will ruled 10/09 that rule governs over a same-morning 'non-US equity = ambiguous' qualifier written after the event was public. Composition disagrees and is recorded, not used to un-fire: equity not debt, one market, a valuation refusal at ~600× revenue, private capital still open, and no US AI-infra debt deal pulled or flexed +150bp. The ROI leg shares S1's root — counted once. The 'scored 3' reasoning below is retained as the record of the pre-fire state.** ~~⚠️ **Scored 3, not 4, and the reason is sourcing rather than severity:**~~ the two strongest datums are the weakest-sourced. ~~The DDTL terms have **no filing at all** — CRWV's last 8-K of any kind is 6/18, and the terms first become verifiable at its **Q2 10-Q (~Aug)** [KB-068].~~ ⚠️ **THAT NEGATIVE RESOLVED 2026-08-12 AND THIS FILE CARRIED IT AS LIVE FOR 9 DAYS.** **CRWV's Q2 10-Q printed 8/12 (acc `0001769628-26-000366`) and VULCAN read it:** the facility is **DDTL 5.5 — $2.6B at Term SOFR + 5.50%**, commitment termination Dec-2026, **matures Sept-2031, $1.2B drawn**, JPMorgan admin agent. ✅ **The S+550 margin is FILING-CONFIRMED.** ❌ The **OID 96-97 and the 10.44% YTM are NOT in the filing** and remain trade-press/PROVISIONAL — so **the sourcing objection is HALF discharged, not discharged**, and the score stays 3 on the same logic (*a better-sourced 3 is still a 3*). ⚠️ **Naming: say "DDTL 5.5", never "the $2.6B DDTL" — DDTL 3.0 was also $2.6B.** [KB-074/075] And the ORCL headline **did not survive verification**: the "$7B" is uncorroborated and its causation was backwards [KB-069]. **Do not score on numbers that verification just corrected.**

🆕 **2026-10-16 RECONCILE (step 2b): S5 HELD at 4 — Volta GRADED, verdict pending WQ-441.** Volta sold 10/15 at S+650 / OID 95 vs the formal 10/9 launch talk S+625–650 / 97–98 (Bloomberg 19:25 ET, unnamed sources; YTM ~12.4% INFERRED). On the KB-214 letter (reading A) the stage-gate is NOT met: margin < S+800, YTM < 13.25%, sold not pulled. On reading B (the unlaunched SOFR+500 sounding) it IS met, n=2. ① No stage `State` cell contradicts STATUS (S5 = 4, fired-count 1). ② No resolved gate is shown as forward: the Volta test is RESOLVED as computed; only Will's choice of reading (WQ-441) is forward. ③ No calc rests on a superseded baseline — both baselines are named. [KB-227]

**2026-10-15 RECONCILE (step 2b): S5 HELD at 4 — escalating, no 2nd fire.** CRWV's 2032 notes reprice to YTW 15.83% and CDS ~1,059–1,120bp (LIQUID, 10/14). That is SECONDARY-market, and the rule reads NEW issues, so it does not fire. **The next letter test is Volta's $5B loan.** 🔒 Pre-stated before pricing: red if final margin ≥ SOFR+800 or all-in YTM ≥ 13.25% or PULLED, against the FORMAL 10/9 launch talk (SOFR+625–650 / OID 97–98). A priced second fire ⇒ propose 4 → 5 to Will. AirTrunk's postponed REIT IPO is not scored (postponed ≠ withdrawn). [KB-214/218/223]

**Upgrade triggers → 4:** a cleared AI-infra new issue flexing **+150bp or pulled** · a **second jurisdiction** writing an IG threshold into a tariff · ~~CRWV's Q2 10-Q disclosing terms **worse** than trade press.~~ ⚠️ **THIS THIRD TRIGGER HAS FIRED AND ANSWERED — NO.** The 10-Q disclosed the margin **at** trade press (S+550, exactly as reported), not worse. **The trigger is spent; do not carry it as a forward condition.** ⇒ **Two live upgrade triggers remain, not three.**

> 🔑 **What replaced it as the sharpest S5 evidence (8/13):** the 10-Q handed over **a pricing TIME SERIES at one issuer**, which is strictly better than the dealer basket I had retracted as historyless — **DDTL 4.0 (Mar-26) SOFR+225 → 5.0 (May-26) +450 → 5.5 (Aug-26) +550.** ⚠️ **Do NOT quote Mar→Aug as +325bp: DDTL 4.0 is NON-RECOURSE.** The defensible like-for-like claim is **+100bp on the 5.0→5.5 leg in three months.** Routed to **LIQUID**, who owns the spread tell — not maintained here as a rival index. Also filed: recourse debt **$31.4B** (+51.5% in 6mo) at 9-15%, total liabilities **$72.0B**, **$35.5B off-BS leases not yet commenced** (2026-29) = the CRWV analogue to ORCL's $260B in the same window, **interest expense $640M > net loss $626M** (GAAP operating loss only −$49M ⇒ *the loss IS the interest bill*), 6-month funding gap **~−$10.5B** on $4.7B revenue, **RPO $103.7B** against **72% of revenue from three customers**. [KB-076..080]

---

