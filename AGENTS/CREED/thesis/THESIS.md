# CREED Thesis Rails

**Created:** 2026-06-21 15:10 ET  
**Status:** Current rails — Phase 3 base (6/21), updated 6/28 + 7/4 + **7/27** (CRE lender leg discovered; S8 split into equity/credit legs; S5 demoted to HOMER-fed cross-ref; convergence 20/40 → 23/45; **8/20: S2 FIRED, 23/45 → 25/45**). See CHANGELOG.  
**Scope:** National CRE / CMBS market-stress synthesis. Not a trade recommendation.

---

## Bottom Line

CREED's current base case is **selective CRE recognition accelerating**, not broad CRE→bank cascade yet.

The clean story:

> CMBS is already showing the pain because securitized loans force recognition faster. Banks are still absorbing/deferring through modifications, reserves, concentration management, and liquidity. The next edge is not “CRE bad”; it is identifying when maturity-default and special-servicing stress crosses into bank provisions, reserve coverage deterioration, forced sales, or funding pressure.

**Refinement added 7/27 — recognition speed is a property of the *holder*, not just the *wrapper*.** The fast-recognition channel is not only "CMBS"; it is every **publicly-marked, quarterly-reporting** CRE holder — which includes the **commercial mortgage REITs**. The slow-recognition channel is not only "banks"; it includes **insurance balance sheets**. The 7/27 session found this printing as a single named transaction: **ARI sold ~$9B of CRE loans to Athene (closed 4/24/26) and its board then resolved to dissolve** — the loans did not go away, they **moved from a fast-recognition holder to a slow-recognition one**. Track the *migration*, not just the delinquency rate.

---

## Current State Classification

| Regime | Definition | Current read |
|---|---|---|
| Extend-and-pretend still absorbing | Stress is real, but modifications/cures/denominator effects keep headline bank metrics contained | Still active |
| Selective CRE recognition accelerating | CMBS and specific property types/metros show forced recognition while banks remain uneven | **Base case** |
| Broad CRE→bank transmission | Bank PDNA/provisions/nonaccruals/funding stress confirm CRE losses are moving into financial-system balance sheets | Not confirmed |

Current evidence:
- **Trepp JULY 2026 CMBS delinquency (latest — PRIMARY-READ): 7.86% overall (+51bps MoM, the largest monthly move in the tracked series); office 11.91% (+34bps); multifamily 7.69% (+46bps); retail 6.96% (+5bps); lodging 5.35% (+13bps); industrial 1.13% (−7bps — the only decline).** July newly-delinquent **$6.00B** (vs $2.64B in June — **2.3×**); top-5 = $2.6B (~44%): a NC/Nevada showroom-and-exhibition portfolio, two Times Square properties, a Chicago office tower, a Seattle office portfolio. **Tell: the maturity-adjusted rate is 9.62% — a new multi-year high** (June 9.53%). ⚠️ **BASIS NOTE:** these are Trepp's **headline** rates (defeased loans included in the denominator). The same report separately prints a **CMBS-2.0 set** — retail 6.66%, lodging 5.34%, multifamily 7.72% — **do not mix the two bases or compare across them.** [Trepp July 2026 CMBS Delinquency Report PDF, **PRIMARY-READ** 2026-08-20, archived `AGENTS/WALTER/sources/`]
- 🔴 **The composition is the finding, not the level: non-performing matured balloon = 66% of newly delinquent balances**, the third consecutive print above 50 → **`CREED-T-02` FIRED 2026-08-20, effective the June print** (see §Convergence Matrix S2 and `registry/CREED_T_FIRED_LOG.tsv`). ⚠️ **Read it in DOLLARS, not share:** the share (May 70 / Jun 65 / Jul 66) looks like decay only because the denominator swings 2.3×; derived matured-balloon dollars run **$1.10B / $2.83B / $1.72B / $3.96B — July is the series PEAK**, +40% vs May and +131% vs June.
- Prior prints for reference: Trepp June 2026 delinquency **7.35%** overall / office **11.57%** / MF 7.23% / maturity-adj 9.53%; May **7.55%** / office 11.53% / MF 6.95%.
- **Trepp JULY 2026 special servicing (latest — PRIMARY-READ): overall 11.09% (−11bps); office 16.58% (−53bps); lodging 8.63% (−26bps); multifamily 8.39% (**+16bps**); retail 13.28% (**+33bps, the largest riser**); mixed-use 11.93% (+2bps); industrial 1.34% (−3bps).** ⚠️ **Three property types ROSE in July — retail, multifamily and mixed-use — not retail alone.** **142bps BELOW the >18% office S1 trigger and MOVING AWAY from it — `CREED-T-01b` does not fire.** ⚠️ **This is NOT an office-healing signal.** Trepp attributes the decline to *"resolutions, paydowns, and workout activity across the office book that outweighed the month's new office transfers"* — i.e. the **seasoned** book clearing, while new **maturity** distress enters through the DQ door instead (office DQ +34bps the same month). **Different doors, one mechanism.** Office SS series as Trepp actually prints it — **Jul-26 16.58 · Jun-26 17.11 · May-26 16.75 · 3mo-ago (Apr-26) 17.66 · 6mo-ago (Jan-26) 17.11 · 12mo-ago (Jul-25) 16.21.** ⚠️ **Only the first three are CONSECUTIVE months; the last three are point-in-time lookbacks, not Apr/Mar/Feb.** April is the highest observable point (17.66%) but **CREED holds no continuous Feb–Apr series, so "peaked" is not claimable.** *(Prior print: June 17.11% / overall 11.2%.)* *(The 7/20 "contested 17.11% vs 16.75% / possible January-conflation" flag was a **false alarm** — WALTER refuted its own recirculation hypothesis: 17.11% is an authentic office figure in both January and June, a coincidence of level. `SIG-W-20260717-005`.)* ⚠️ **SOURCE TIER (corrected 2026-08-20):** this line previously read *"Trepp PDF paywalled = primary-CITED, not primary-READ."* **Apr–Jul 2026 are archived as readable PDFs at `AGENTS/WALTER/sources/` and were read directly** — the July figures above are **PRIMARY-READ**. **Month-scoped: paywalled/primary-CITED remains the default for months not in that folder.** The "retail 12.95%" circulating alongside is still **UNVERIFIED — do not cite.**
- **The SS−DQ gap is the extend-and-pretend signature — and it NARROWED in July, which is the tell.** Office SS runs above office DQ because special servicing fires **pre-delinquency** on maturity/covenant events (a loan can sit in SS while current on interest). The gap went **5.54pp (Jun: 17.11 − 11.57) → 4.67pp (Jul: 16.58 − 11.91)** — **both legs converging, SS down and DQ up.** ⚠️ **A narrowing gap here is RECOGNITION, not repair:** the same conversion Trepp names on the maturity-adjusted series (*distress "shifting out of performing matured balloon status and into non-performing matured balloon status"*) drains the pre-delinquency buffer into the headline. **The extend-and-pretend cushion is thinning, not thickening.** Servicer mechanism unchanged: unwilling to seize, resolutions via extension/forbearance/new equity — but see the S4 caveat, mods are exhausting one credit at a time.
- **⭐ NEW 7/27 — the CRE lender leg is recognizing while the CRE equity leg rallies.** Over 3mo, office equity REITs are **+14% to +77%** while **7 of 11 CRE mortgage REITs are negative** (median ≈ −9%). Two named actions inside that window, and **they are different mechanisms that must not be fused**: **(a) ARI — lender-economics exit**, ~$9B book sold to Athene at **99.7% of total loan commitments** (closed 4/24/26), board resolved 6/15/26 that dissolution/liquidation/wind-down is "advisable" [SEC 8-K, primary]. ⚠️ **TWO VOTES — do not conflate: the SALE was stockholder-APPROVED (special meeting 4/21/26, via a special committee with BofA Securities and Fried Frank as independent advisers); the DISSOLUTION was NOT** — preliminary proxy still pending; the clean 99.7% clearing is evidence **against** the "CRE marks are fictional" leg. **(b) KREF — credit-loss recognition**, dividend **−60%** ($0.25→$0.10), Q2 GAAP **−$121.8M (−$1.95/sh)**, 6-mo provision **$148.6M**, ACL **$293.1M**, book $10.24, reserves attributed to **risk-rated 5 loans in office, multifamily and life science**; legacy office 21%→**18%**, targeting **<10% by YE26**. **8 of 11 held dividends flat — this is selective, not a cohort cascade.**
- **Life science is BIFURCATED, not collapsing** [Savills Q2-26]: the over-built distressed markets are **past peak and absorbing** (Chicago 37.6%, improved from 39.2%; Denver-Boulder 23.8% from 27.0%) while Boston-Cambridge (26.4%, **+610bps**) and SF Bay (26.2%) worsen because **inventory grew, not because tenants left** (~2.5M sf new lab deliveries in Boston). A "national life-science vacancy near records" line fuses two opposite mechanisms and destroys the read. CBRE's national 23.2–23.3% is a **different provider/methodology — do not stack.** *(Closes a coverage gap WALTER named: CREED+REGINALD grep = zero life-science hits, on the exact asset class in OZK's Seattle credit and KREF's risk-5 reserves.)*
- 2026 maturity wall remains live: Morningstar DBRS / accessible corroboration points to **>$100B** CMBS maturities and more than half expected not to repay at maturity; Trepp hard maturities **$76.6B**, **39%** in Q4.
- FDIC Q1 2026 bank PDNA: **1.53%** overall; non-owner CRE and multifamily elevated, but large-bank non-owner CRE PDNA improved to **3.40%** *(still counter-direction, 6th straight improving quarter)*. 🔴 **Q2 QBP expected ~8/24–8/29 — imminent, and it is `CREED-T-03`'s actual trigger.** **S3 has NOT moved and is still 2: the fire in S2 is a CMBS-recognition event, not a bank-transmission event.**
- **Realized-recognition comp cluster (Jun–Jul 2026 — the recognition now printing as REALIZED losses, not just marks; mostly single-source/WALTER-routed unless noted):** 205 W Randolph Chicago office liquidated at a **72% haircut = $12.2M realized CMBS loss** (COMM 2015-CR22; single-source, unverified vs remit); Aon Center Chicago **−58% appraisal** ($780M→$330.5M) with 601W seeking another extension; Bank OZK **deed-in-lieu** on the Seattle U-District "Chapter Buildings" (~394K SF office/life-science, ~$126M current OZK exposure; the LOI-for-recap FAILED — **CONFIRMED 0.85**); Galveston vacant office **$8.79/SF, 0% occ**; **S2 Capital $400M multifamily Fund I dissolved, "no return of capital"** to LPs + $311M North Texas MF at foreclosure this month (**CONFIRMED 0.88** vs The Real Deal primary); 75 West N.Dallas ($90M, Ares 2022 lender) + Austin 526-unit MF ($61.1M-2024 → $9.5M opening bid) forced-sale comps; MF rent concessions **16.9%** (12-yr high, Class-C 21.5% / Sunbelt-led).

Primary source pack: `AGENTS/CREED/research/REFRESH_2026-07-27.md` (current — CRE lender leg, June SS resolution, life-science bifurcation, mall-cadence kill, 7/27 intraday tape). Supersedes `REFRESH_2026-07-04.md` (retained for the June Trepp print + realized-recognition cluster source-trail) and `REFRESH_2026-06-21.md` (FDIC-Q1 / maturity-wall source-trail).

---

## Mechanism Map

### 1. Maturity-default channel

Loans can still cash-flow and still default at maturity if refinance proceeds no longer cover prior debt. This is the cleanest 2026 CREED forcing function.

Watch:
- non-performing matured balloon share of new CMBS delinquencies
- hard-maturity loans with no remaining extension options
- low debt-yield cohorts, especially debt yield <=8%
- Q4 2026 maturity bulge

### 2. Special-servicing / appraisal channel

Special servicing forces updated appraisals, modification decisions, or liquidation paths. Large-loan cures/returns can improve headline rates without genuine market repair.

Watch:
- special servicing rate by property type
- new transfer volume and largest loan transfers
- repeat transfers / re-defaults after modification
- office and mixed-use concentration

### 3. Bank-recognition channel

Banks can lag CMBS because they can modify, extend, reserve, or hold collateral at non-market-clearing marks. The trade-relevant signal is convergence: bank PDNA/provisions/charge-offs catching up to CMBS stress.

Watch:
- FDIC non-owner CRE PDNA by bank size
- community/regional reserve coverage
- provision spikes and CRE-specific charge-offs
- modifications and second modifications
- FHLB/repo/funding usage if CRE losses start forcing liquidity needs

### 4. Multifamily property-level channel

Multifamily is not only a maturity wall. March 2026 evidence showed term defaults tied to property-level fundamentals: occupancy, operating costs, market-specific weakness, or tax/expense resets.

Watch:
- term defaults vs maturity defaults
- NY/NJ, Houston, Sunbelt, and Florida-specific stress splits
- DSCR deterioration in recent vintages
- agency vs private-label divergence

### 5. Forced-sale / NAV channel

CRE valuation truth appears when assets transact under pressure. Forced sales can turn private marks into public/comparable marks, pressuring funds, banks, and REITs.

Watch:
- large sales >30% below prior appraisal / loan basis
- open-end fund gates or redemption queue reversal
- appraisal reductions and LTV covenant breaches
- ODCE / private CRE fund redemption data

---

## Expected Signals — Current v1.0

### 🔴 Signal 1: Office CMBS stress re-accelerates

Trigger examples:
- office CMBS delinquency breaks back above **12%** and holds
- office special servicing moves above **18%**
- multiple gateway-city loans transfer to special servicing in one month

Response:
- update CREED refresh note or monthly tracker
- alert REGINALD if bank-exposed metros/property types overlap
- alert LIQUID if refi/funding conditions are the driver

### 🔴 Signal 2: Maturity-default wave confirms

Trigger examples:
- non-performing matured balloon loans remain majority of new delinquencies for consecutive months
- Trepp/Morningstar data shows >50% of 2026 CMBS maturities failing to repay as projected
- Q4 hard-maturity cohort starts transferring to special servicing early

Response:
- upgrade maturity wall from risk to active forcing mechanism
- route to LIQUID and REGINALD

### 🔴 Signal 3: Bank CRE convergence

Trigger examples:
- FDIC/bank filings show non-owner CRE PDNA rising after Q1 improvement
- community/regional reserve coverage deteriorates further while CRE noncurrents rise
- CRE-specific provisions or charge-offs jump across multiple REGINALD watchlist banks

Response:
- urgent handoff to REGINALD
- CREED provides property/metro/source map, not trade execution

### 🟠 Signal 4: Modification exhaustion / re-default

Trigger examples:
- declining new modifications because extension capacity is exhausted
- second-modification or re-default rates rise
- loans returned to master servicer re-transfer to special servicing

Response:
- classify extend-and-pretend as failing in affected segment
- update thesis state toward broad transmission if bank evidence confirms

### 🟠 Signal 5: Multifamily term-default broadening — **HOMER-FED CROSS-REFERENCE (demoted 2026-07-27)**

> **Ownership ruling applied 7/27** (DAEDALUS packet 2026-07-12, Will-approved HOMER promotion). **HOMER is the primary owner of the Trepp CMBS-multifamily row, the GSE-vs-CMBS divergence, and Sun-Belt-MF realization tracking.** CREED no longer scores S5 as an independent vote — it is carried as a **cited cross-reference to `AGENTS/HOMER/STATUS.md`**. CREED continues to pull the *whole* Trepp print for office/retail/industrial/lodging; the MF row routes to HOMER rather than being independently parsed. **S5 is NOT retired** — it stays in the matrix with its score visible for continuity, but it is excluded from CREED's independent-root count. This fixes a live double-count: HOMER's SV-HOMER-2026-07-10-02 and CREED's S5/S6 were independently tracking the same Sun-Belt 2022-vintage foreclosure cluster as separate findings.

Trigger examples:
- multifamily CMBS delinquency/special servicing resumes uptrend after May cure
- term defaults dominate new multifamily delinquencies outside isolated NY/NJ/Houston cases
- DSCR stress appears in 2022–2023 vintages

Response:
- feed CARL for household/housing-consumer overlap
- feed CORAL only when Florida-specific

### 🟠 Signal 6: Forced-sale / private-NAV recognition

Trigger examples:
- large CRE sale >30% below appraisal/loan basis
- open-end CRE funds impose gates or redemption queues reverse
- appraisal marks force LTV/covenant consequences

Response:
- route funding implications to LIQUID
- route bank collateral/LGD implications to REGINALD

### 🟡 Signal 7: Office demand structural hit becomes tape-confirmed

Trigger examples:
- office REITs/brokers sell off alongside direct evidence of tenant demand impairment
- AI/automation job cuts translate into leasing cancellations, sublease supply, or vacancy acceleration

Response:
- treat AI as accelerator/narrative until supported by vacancy/leasing/default data

### 🟡 Signal 8: Public-market tape confirms CRE recognition — **SPLIT INTO TWO LEGS (2026-07-27)**

> **Why the split.** Through 7/20 this signal was scored off VNQ-vs-SPY and office-REIT *equity*, and it read as a clean counter-signal. The 7/27 pull showed that framing was **a blended vector masking a bifurcation**: the public market has two CRE legs and they are telling **opposite stories** — equity REITs +14-77%/3mo while 7 of 11 CRE mortgage REITs are negative, with one lender liquidating and another cutting its dividend 60%. Scoring them as one number destroys the information. **Signal numbering is unchanged (1–8) so existing citations still resolve; S8 now carries legs 8a and 8b.**

#### Signal 8a — CRE **equity** tape (office/retail/diversified REITs)

Trigger examples:
- VNQ underperforms SPY by >10% over 3 months while rates/refi stress or property fundamentals worsen
- office REIT NAV discounts exceed 50% with confirming vacancy/leasing/default evidence
- major office/retail/residential REIT cuts dividend because NOI/refi stress is impairing cash flow

#### Signal 8b — CRE **credit / lender** tape (commercial mortgage REITs) — *new leg*

Trigger examples:
- CRE mREIT book-value/dividend shock: dividend cuts or realized book-value erosion **across multiple names** (not one)
- a CRE lender **exits, liquidates, or sells its loan book** rather than redeploying capital — lender-appetite/credit-availability withdrawal
- credit-loss provisions or realized write-offs rising **across** the CRE-lender cohort, especially on risk-rated-5 credits
- CRE lenders trading persistently below book while dividends are cut → refi-capacity headwind feeding the maturity wall (S2)

**Discipline on 8b — three traps, all live:**
1. **Separate lender-ECONOMICS from CREDIT-LOSS.** A lender exiting because the business no longer earns its cost of capital (ARI: book cleared at **99.7% of commitments**) is *not* the same event as a lender reserving against impaired credits (KREF: risk-5 write-offs). ARI's clean clearing is evidence **against** the "marks are fictional" bear leg even as its exit is evidence **for** credit withdrawal. Do not fuse them.
2. **Check corporate actions before reading a price.** ARI printed **−33.4% in one session** on 7/16 — that was a **$3.75/sh return-of-capital going ex**, not a crash; on a total-return basis it rose. Never cite a CRE mREIT price move without checking the dividend record.
3. **Count the cohort, not the headline.** 8 of 11 CRE mREITs held dividends flat. Selective ≠ cascade.

Response:
- update `AGENTS/CREED/research/REIT_EQUITY_TAPE_MODULE_2026-06-21.md` or monthly tracker
- route property/collateral implications to REGINALD when bank exposure matters
- route funding/spread implications to LIQUID
- route retail/residential consumer spillovers to CARL
- do not treat REIT price action alone as broad CRE→bank confirmation

---

## Convergence Matrix (5-pt stackable handle)

*Added 2026-06-28 per DAEDALUS BATCH_01.* Maps the 8 Expected Signals onto the universal 5-pt scale so NEXUS/PROME can stack CREED's national-CRE read **without spawning the tier-2 agent**. Scale: 5 firing → 4 🔴 elevated → 3 🟠 building/near-trigger → 2 🟡 latent → 1 ⚪ dormant. Independence = shared-antecedent flag (count a shared root once). *Current reads carry as-of dates (June Trepp + 7/2 REIT tape refreshed into the pack 7/4); re-verify the monthly CMBS special-servicing print + office-REIT tape before re-scoring.*

| # | Vector (Expected Signal) | Score | Local state / current read [as-of] | Independence | Upgrade trigger |
|---|---|---:|---|---|---|
| 1 | Office CMBS stress re-accelerates | 3 | **UPDATED 8/20 [Trepp Jul, PRIMARY-READ]:** delinq **11.91% (+34bps)** — **9bps below** the >12 trigger, the nearest registered trigger on the fleet board / **SS 16.58% (−53bps)** — **142bps below >18 and moving AWAY.** Still **not fired**, held at 3. ⚠️ **The two legs now diverge and it is not a data problem:** SS fell on *"resolutions, paydowns, and workout activity"* (Trepp) clearing the **seasoned** book, while DQ rose on **named matured-balloon conversions** (Chicago office tower, Seattle office portfolio) entering through a different door. Extend-and-pretend still working on old distress; new distress is maturity-driven → see #2 | ⟂ shares maturity-wall/refi-gap root w/ #2 | delinq >12% & holds OR SS >18% |
| 2 | Maturity-default wave confirms | **5 🔴 FIRED** | **maturity-adjusted DQ 9.53% = multi-year high** [Trepp Jun] — headline 7.35% masks the past-maturity-still-paying overhang; wall live (>$100B CMBS, >50% exp. non-repay; $76.6B hard, 39% Q4). **Reinforced 7/27:** all three July mall SS transfers were **maturity/extension failures, not NOI stress** (Sangertown = a 3rd extension refused on a DSCR hurdle after rolling twice — extend-and-pretend ending on schedule). **⭐ FIRED 2026-08-20 (effective the JUNE print, ~6wk detection lag) — `CREED-T-02`, the first fire of any CREED trigger.** Matured-balloon share of newly delinquent balances: **Apr 42% ❌ / May 70% ✅ / Jun 65% ✅ ← sustain met / Jul 66% ✅** — PRIMARY-READ off four Trepp PDFs. ⚠️ **The share (70→65→66) reads as decay ONLY as a ratio — its denominator swings 2.3×.** Derived matured-balloon **dollars**: Apr $1.10B / May $2.83B / Jun $1.72B / **Jul $3.96B = the series peak, +40% vs May, +131% vs Jun.** Volume is rising while the ratio plateaus. **Maturity-adjusted DQ 9.62% [Trepp Jul] = new multi-year high**, and its gap to headline NARROWED 218→176bps **because distress converted from *performing* to *non-performing* matured balloon (Trepp verbatim) — recognition, not repair.** | ⟂ shares maturity-wall root w/ #1 — **counts as ONE root escalating, not two** | ✅ **MET:** matured-balloon = majority of new delinq 2 consec mo |
| 3 | Bank CRE convergence | 2 | FDIC Q1 large-bank non-owner CRE PDNA **improved** to 3.40% — still counter-direction; FDIC Q2 QBP ~late Aug. **OZK Q2 graded 7/21 exactly per the CREED pre-position: Seattle charge-offs = KNOWN-workout recognition → S3 held.** ⚠️ **Watch-add: Special Mention +$219M fresh and UNATTRIBUTED while ACL was RELEASED $10.7M** — a reserve release into a classified build is the opposite of convergence, which is itself the tell | ⟂ DOWNSTREAM of #1/#2 (transmission, not an independent root) | FDIC PDNA re-rising + reserve-coverage deterioration |
| 4 | Modification exhaustion / re-default | 2 | no clean aggregate evidence — extend-and-pretend still WORKING at the aggregate (servicers unwilling to seize; resolutions via extension/forbearance). **Firmer at the asset level 7/27:** Aon + Seattle recaps FAILED, and Sangertown is a **3rd extension refused on a DSCR hurdle** — mods exhausting one credit at a time, not yet in the aggregate | Independent (mod mechanism) | re-default / 2nd-mod rates rise |
| 5 | Multifamily term-default broadening | *(3)* | **⟵ HOMER-FED CROSS-REF as of 7/27, not independently scored by CREED** (DAEDALUS ruling 7/12). HOMER carries the Trepp MF row: MF DQ **7.23%** June (+28bps), maturity-adj 9.53%, GSE-vs-CMBS divergence **WIDENING**, Sun Belt 2022-vintage cluster. **Cite `AGENTS/HOMER/STATUS.md`.** Score shown for continuity only — **excluded from CREED's independent-root count** | **NOT an independent CREED vote** — HOMER-owned; previously shared the Sun-Belt-cluster antecedent w/ #6 | *(HOMER's call)* |
| 6 | Forced-sale / private-NAV recognition | 3 | **CLUSTER of realized comps >30% below basis** holds (205 W Randolph −72% realized CMBS loss; Aon −58% mark; Galveston $8.79/SF; Seattle OZK deed-in-lieu). ⚠️ **Material COUNTER-datum added 7/27: ARI's ~$9B CRE loan book cleared at 99.7% of total loan commitments** — the largest clean mark-validation in the pack, and direct evidence *against* the "CRE marks are fictional" leg. **Held at 3, not raised** | Independent (LGD/recognition) | open-end fund gates (not yet); a >30%-below-basis cluster in *performing* collateral |
| 7 | Office-demand structural hit (tape-confirmed) | 2 | AI-narrative only; data-center demand still a STRENGTH counter-signal (capex raised; the 7/20 DLR/EQIX softness **largely unwound** — DLR −13.4%→−3.0%/3mo). **Life-science leg added 7/27: BIFURCATED, not collapsing** — distressed markets absorbing (Chicago 37.6% improving), Boston/SF worsening on **new supply, not tenant loss**. 🆕 **Q2-2026 NATIONAL PRINTS (added 8/20, `KB-CREED-021`) MOVE THE SECOND LEG AWAY FROM FIRING:** all three reachable providers show office vacancy improving — **CBRE 18.3% (−30bp QoQ, largest decline since 2015; net absorption +12.6M sf, 9th consecutive positive quarter; leasing +16% YoY)**, **JLL −60bp QoQ (+30M sf TTM occupancy gains, availability down 8 straight quarters)**, **C&W 20.1% (−10bp YoY)**. ⚠️ **C&W's improvement is substantially a DENOMINATOR effect** (Q2 absorption −360K sf; inventory −33M sf over 5 quarters via conversion/demolition — ≥37% vacant share of removed stock accounts for the whole −10bp) — **but that caveat does NOT transfer to CBRE/JLL, whose declines come with large positive absorption.** 🔴 **HELD at 2 — and the Q2 evidence is a reason it should NOT rise.** `CREED-T-07` is a **two-leg AND** requiring *direct tenant-demand impairment*; that leg is **moving away from the trigger, not toward it** 🔴 **BASIS-CHANGE GUARD (2026-08-20, Will-ruled rider):** `VX-9.03`'s canonical provider was re-spec'd **Moody's → CBRE**, moving its band state **RED (>20) → ORANGE (>18) PURELY BECAUSE THE INSTRUMENT CHANGED** (21.0% vs 18.3%, a ~2.4–2.7pp methodology spread). **NO BAND WAS EDITED AND NO STRESS ABATED. THIS IS NOT AN S7 IMPROVEMENT AND IS NOT COUNTED AS ONE — S7 stays at 2 on the evidence, not on the band state.** Never run a trend read across the swap without saying so. ⚠️ **The bands are UNCALIBRATED for CBRE** (set against Moody's-like levels) — **indicative only until re-based at 3–4 quarters of overlap; n=1 today and re-basing was refused as a base-rate violation.** **Grade this leg on ABSORPTION DIRECTION, not the level** — positive net absorption means tenant demand is not impairing, whatever the rate reads. | ⟂ shares office-demand root w/ #8a | REIT selloff + direct tenant-demand impairment |
| 8a | CRE **equity** tape confirms | 2 | ⚠️ **DIRECTION CLAIM WITHDRAWN 2026-08-20 (afternoon) — this row asserted "COUNTER-SIGNAL NOW DECAYING, direction reversed" that morning and it is NOT SUPPORTABLE.** Live close basis: **+0.07pp total-return / −0.58pp price-only** (`scripts/s8a_relative.py`). ⚠️ **The level sits inside its own noise** — 10-session stdev **2.01pp**, full-sample **4.70pp**; the 7/27→8/20 move is **−1.55pp like-for-like, under one stdev**, and it hides a round trip through **−4.30pp (8/10) then eight straight sessions UP.** ⚠️ **Sign robust to NEITHER basis (0.65pp spread) NOR window start (−0.78→+2.80pp across ±9 sessions).** ⚠️ **And the band was BREACHED 78 days ago (6/01–6/03, low −11.84pp), seven weeks BEFORE it was written — no fire missed, but ~0pp is only ~2.1 sigma from the trigger, not a safe distance.** **HELD at 2 — unchanged, and now held on the level and its noise rather than on a trend claim.** Office REITs +14→+77%/3mo and mall REITs up are **7/27 observations, NOT re-verified 8/20** | ⟂ equity-tape read of #7's fundamental | VNQ −10% vs SPY/3mo + confirming fundamentals |
| 8b | CRE **credit / lender** tape | **3 ★NEW** | **⭐ the leg S8 was structurally blind to.** 7 of 11 CRE mREITs negative/3mo (median ≈ −9%) while equity REITs rallied. **ARI: ~$9B book → Athene at 99.7%, board resolved to dissolve** (8-K primary; stockholder-UNAPPROVED). **KREF: dividend −60%, Q2 GAAP −$121.8M, 6-mo provision $148.6M, ACL $293.1M, risk-5 reserves in office/MF/life-science, office 21%→18% targeting <10%.** BXMT −17.1%/3mo w/ dividend held. **8 of 11 held dividends — selective, not a cascade** | **Independent** (lender-capital/credit channel — a NEW root, not a re-read of #7) | multi-name dividend cuts + realized book erosion **across** the cohort |

**Composite: 25/45 (55.6%), from 23/45 (51.1%) — updated 2026-08-20 on the `CREED-T-02` fire (S2: 3 → 5).**

> **This window DID escalate the thesis — the first time that sentence has been true.** The 7/27 window explicitly did not (it resolved a blended vector); this one fired a Will-frozen trigger on pre-written terms.
>
> ⚠️ **But read the escalation narrowly, three ways.** ① **S1 and S2 share the maturity-wall root**, so this is **one root escalating, not two** — the independent-root count is **unchanged at ~4–5**. ② **S3 (bank convergence) did not move and is still 2** — the FDIC PDNA series remains counter-direction, and **S3 is the trade-relevant one.** ③ **The fire is a CMBS-recognition event, not a bank-transmission event.** The base case *selective CRE recognition accelerating* is now better evidenced **in its own channel**; **broad CRE→bank transmission remains NOT confirmed.** FDIC Q2 QBP (~8/24–8/29) is the next real test of ③.

> **⚠️ How S5 is counted — stated explicitly because the phrasing was ambiguous when first written (fixed in the 7/27 audit sweep).** There are **two different exclusions** and they are not the same thing:
> - **The COMPOSITE (25/45) INCLUDES S5's score of 3.** CREED still *tracks* multifamily as a CRE-stress vector; it simply no longer *sources* it independently.
> - **The INDEPENDENT-ROOT COUNT EXCLUDES S5.** It is not a CREED vote and must not be stacked as separate corroboration alongside HOMER's own reading of the same data.
>
> **Do not "simplify" this by dropping S5 from the composite.** Doing so yields **20/40 — numerically identical to the pre-7/27 composite** by pure coincidence, which would read as "nothing changed" when in fact a signal was split, an ownership boundary moved, and a new independent root was added. If a future session wants a single S5-free number, state it as **20/40 on an 8-vector basis, NOT comparable to the 7/20 20/40.** Base case *selective CRE recognition accelerating* **holds**. **Nothing FIRED** — no signal crossed a hard trigger.

**Two structural changes, both applied 7/27** (denominator moved 40→45; both directions disclosed so nothing is silently lost): **(i) S5 demoted** to a HOMER-fed cross-reference per the Will-approved DAEDALUS ruling — kept in the matrix, removed from CREED's independent-root count, MF figure now cited from HOMER; **(ii) S8 split into 8a/8b** because the equity and credit legs of the public CRE tape diverged hard enough that one score destroyed the information. Signal numbering 1–8 is unchanged so existing citations still resolve.

**Counting once for shared antecedents:** maturity-wall root (S1+S2); office-demand root (S7+S8a); S3 downstream of S1/S2; S5 no longer a CREED vote. **S8b is a genuinely new independent root** (lender-capital withdrawal is not a re-read of property fundamentals). = **~4–5 independent roots elevated, not 8.** Do not read 25/45 as broad confirmation; read it as *the recognition-acceleration base case now visible in a second channel, still pre-bank-transmission.*

⚠️ **Evidence quality this window is BETTER than usual, and the direction of the strongest evidence is mixed.** The ARI wind-down is **SEC-primary, read directly** — the highest-grade single item in CREED's rails — and it carries a **counter**-datum (99.7% clearing) alongside its bear datum (lender exit). KREF is secondary-sourced (10-Q not read). The June SS resolution is primary-*cited*, paywalled, not primary-*read*. The mall-cadence "signal" was **tested and killed** (§9 of the 7/27 pack): 3-in-3-days is **not established as anomalous** against a ≥2/month floor derivable from June's top-5 new delinquencies. Anecdotes corroborate aggregates here; they do not carry the read.

---

## Counter-Signals

Signals that weaken CREED bear intensity:
- CMBS delinquency falls below **6.5%** with special servicing falling for genuine cures/payoffs, not denominator effects.
- office delinquency falls below **9%** and office special servicing below **13%**.
- 2026 maturity repayments materially outperform the >50% default/non-repayment expectation.
- FDIC bank CRE PDNA continues improving while reserve coverage stabilizes.
- transaction volume and price discovery improve without forced-sale discounts.
- funding/rates ease enough to refinance low-debt-yield cohorts.

**Live counter-signals as of 2026-07-27 — actively weighing against the bear read:**
- **ARI's ~$9B CRE loan portfolio cleared at 99.7% of total loan commitments** (closed 4/24/26). A book that size clearing essentially at par is the strongest available evidence that CRE marks in the performing bank/lender channel are **not** fictional. This is the single most important counter-datum CREED holds.
- ~~**The CRE equity tape counter-signal STRENGTHENED and flipped positive** — VNQ +2.04pp vs SPY/3mo~~ ⚠️ **SUPERSEDED TWICE, 2026-08-20.** The 8/20-morning replacement (*"−0.34pp … DECAYING … moved ~2.4–3.0pp TOWARD the trigger"*) is **itself withdrawn as a trend claim.** Live close basis: **+0.07pp TR / −0.58pp price-only**; the 7/27→8/20 move is **−1.55pp like-for-like, inside one 10-session stdev (2.01pp)**, and the series has risen **eight consecutive sessions** off its 8/10 low of −4.30pp. **The honest statement: the equity-tape counter-signal is roughly FLAT and its short-run direction is not measurable on this instrument.** It still weighs against the bear read — but as a level near zero, not as a trend in either direction. *(Office REITs +14→+77%/3mo and mall REITs up are 7/27 observations, **NOT re-verified** as of 8/20.)*
- 🆕 **NATIONAL OFFICE LEASING FUNDAMENTALS TURNED UP IN Q2 2026 — added 2026-08-20, and it is a genuine counter-signal, not a caveat.** All three reachable providers: **CBRE 18.3% (−30bp QoQ, largest quarterly decline since 2015; net absorption +12.6M sf, 9th consecutive positive quarter; leasing +16% YoY)** · **JLL −60bp QoQ (availability down 8 straight quarters, +30M sf TTM occupancy gains)** · **C&W 20.1% (−10bp YoY)**. For three cycles CREED carried Moody's Q1 *"21.0%, record high, still rising"* as its office anchor; **the direction has turned and CREED does not water that down.** ⚠️ *C&W's leg is substantially a **denominator** effect (Q2 absorption −360K sf; inventory −33M sf over 5 quarters) — **but CBRE's and JLL's are real absorption.*** `KB-CREED-021`.
> 🔴 **AND THIS IS THE SYNTHESIS THAT MATTERS — IT SHARPENS THE THESIS RATHER THAN WEAKENING IT.** Office **leasing** improved in Q2 while office **CMBS credit** deteriorated in the very same window (office DQ **11.91%, +34bp**; matured-balloon dollars at a series peak **$3.96B**). Those do not conflict — **they identify the distress as a CAPITAL-STRUCTURE / MATURITY event, not a TENANT-DEMAND event. Buildings are leasing better and still failing to refinance.** That is precisely why **`CREED-T-02` (maturity wave) fired on 8/20 while `CREED-T-07` (office demand) did not and should not** — independent corroboration that the signal architecture is cutting along the right seam. ⚠️ **It also narrows the bear case: the office leg of a CRE→bank transmission has to run through VALUES AND DEBT, not through emptying buildings.**
- **8 of 11 CRE mortgage REITs held their dividend flat**; KREF is **+22.6%/3mo *after* a 60% cut.** The lender leg is selective, not cascading.
- **Life science is bifurcating with the worst markets HEALING** (Chicago 37.6% from 39.2%; Denver-Boulder 23.8% from 27.0%) — the deterioration that exists is a **supply** event, not a demand collapse.
- **Data-center softness did not persist** — the 7/20 "lone weak leg" (DLR −13.4%/3mo) unwound to −3.0%/3mo by 7/27. Correctly not scored as stress at the time.
- **REGINALD's mall-cadence signal was tested and did not survive** — 3-in-3-days is not established as anomalous against the observable run-rate.

---

## Agent Handoffs

### REGINALD

CREED sends:
- bank-size CRE PDNA and reserve-coverage deterioration
- property/metro maps tied to bank exposures
- modification exhaustion and re-default evidence

CREED does not send:
- bank trade recommendations or position sizing

### CORAL

CREED sends:
- Florida-specific CMBS / hotel / multifamily / condo-linked stress
- national CRE context that affects Florida banks or migration/tourism exposures

CREED does not send:
- whole-Florida synthesis or insurance/tourism thesis ownership

### LIQUID

CREED sends:
- maturity-wall funding/refi pressure
- forced-sale / NAV cascade evidence
- lender appetite and credit-market closure signs

### CARL

CREED sends:
- rent/occupancy/property-level stress with household spillover potential

*(Multifamily term-default evidence now routes via **HOMER**, not CREED — see below.)*

### HOMER *(added 2026-07-27)*

**HOMER owns** the Trepp CMBS-multifamily row, the GSE-vs-CMBS divergence, and Sun-Belt-MF realization tracking (DAEDALUS ruling 7/12, Will-approved). CREED **cites** `AGENTS/HOMER/STATUS.md` for the MF figure rather than pulling it independently.

CREED sends:
- the multifamily row from its whole-Trepp-print pull (one pull, one MF owner, no duplicate parse)
- MF-relevant lender evidence surfacing in CREED's channels (e.g. KREF's risk-rated-5 **multifamily** reserve build)

CREED does not send:
- an independent MF term-default score or a second Trepp-MF citation

### SHADE *(added 2026-07-27)*

CREED sends:
- **CRE-asset migration into insurance balance sheets** — the slow-recognition sink. Named instance: **~$9B of ARI's CRE loans sold to Athene, closed 2026-04-24 at 99.7% of commitments**, ahead of ARI's board resolving to dissolve.
- the CRE leg of the aggregate absorption series: MBA CM/MF life-insurer holdings **+$3.3B in Q1 → $775B** of the $5.02T market (Q2 print ~mid-Sept).

CREED does not own:
- the combined-sink question or any insurer-side credit judgment — SHADE owns both. CREED supplies the CRE leg only.

---

## Current Open Questions

1. Is Q4 2026 the real maturity-wall pain point, or will borrowers pull forward recognition into Q2/Q3?
2. Are May office/multifamily improvements real cures or large-loan/denominator noise?
3. Which regional/community banks have deteriorating reserve coverage plus high CRE concentration?
4. ~~Does multifamily stress remain metro-specific…~~ **→ HOMER's question as of 7/27.**
5. Does AI office-demand risk become visible in leasing/vacancy/default data, or remain mostly equity narrative?
6. **⭐ How much CRE credit is migrating from fast-recognition holders (mortgage REITs, CMBS) to slow-recognition holders (insurers, banks), and does that migration *defer* recognition or merely *relocate* it?** The ARI→Athene $9B is one named instance; the MBA quarterly flow series is the aggregate. If the fast channel keeps shedding at par into balance-sheet buyers, headline CMBS/mREIT stress metrics will **understate** system CRE risk by construction — the stress leaves the measured population. *(SHADE owns the insurer side.)*
7. **Why did the CRE equity and CRE credit tapes diverge this hard?** Equity REITs +14-77%/3mo against a lender cohort 7-of-11 negative is a large, systematic split. Candidate reads: (a) equity is pricing rate relief and credit is pricing spread/funding; (b) equity is pricing *asset* recovery while credit prices *lender-economics* (cost of capital, not collateral); (c) one of the two is wrong. **This is the highest-value open question in the rails** — it determines whether S8a's counter-signal or S8b's build is the leading indicator.
8. **Is ARI idiosyncratic or the first of several?** A public CRE lender concluding the business no longer earns its cost of capital and handing capital back is a strategic verdict on CRE lending economics, not on CRE credit. Watch whether other sub-scale mREITs follow (BXMT is the name to watch — largest office-exposed, −17.1%/3mo, dividend still intact).

---

## Operating Rule

Do not trade directly from CREED. CREED identifies stress mechanisms and routes evidence. Trade construction belongs to TERRY; bank execution belongs to REGINALD; Will approves all trades.
