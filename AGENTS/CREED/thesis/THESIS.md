# CREED Thesis Rails

**Created:** 2026-06-21 15:10 ET  
**Status:** Current rails — Phase 3 base (6/21), updated 6/28 + **7/4** (June Trepp + realized-recognition cluster + 7/2 REIT tape; convergence 20/40). See CHANGELOG.  
**Scope:** National CRE / CMBS market-stress synthesis. Not a trade recommendation.

---

## Bottom Line

CREED's current base case is **selective CRE recognition accelerating**, not broad CRE→bank cascade yet.

The clean story:

> CMBS is already showing the pain because securitized loans force recognition faster. Banks are still absorbing/deferring through modifications, reserves, concentration management, and liquidity. The next edge is not “CRE bad”; it is identifying when maturity-default and special-servicing stress crosses into bank provisions, reserve coverage deterioration, forced sales, or funding pressure.

---

## Current State Classification

| Regime | Definition | Current read |
|---|---|---|
| Extend-and-pretend still absorbing | Stress is real, but modifications/cures/denominator effects keep headline bank metrics contained | Still active |
| Selective CRE recognition accelerating | CMBS and specific property types/metros show forced recognition while banks remain uneven | **Base case** |
| Broad CRE→bank transmission | Bank PDNA/provisions/nonaccruals/funding stress confirm CRE losses are moving into financial-system balance sheets | Not confirmed |

Current evidence:
- **Trepp June 2026 CMBS delinquency (latest): 7.35% overall (−20bps MoM, held down by a large lodging cure); office 11.57% (+4bps, ticked back UP); multifamily 7.23% (+28bps — RESUMED rising after the May cure); retail 6.91% (+30bps); lodging 5.22% (−79bps); industrial 1.20% (−11bps).** June newly-delinquent $2.64B; top-5 = $998.9M (SoCal super-regional mall, NH regional mall, NY office complex, Minneapolis mixed-use tower, Manhattan multifamily). **Tell: including past-maturity loans still current on interest, the adjusted rate would be 9.53% — a new multi-year high** — the 7.35% headline understates the maturity-default overhang. [connectcre / Yield PRO / Trepp, Jun 2026 print, ~7/2/26]
- Prior print for reference: Trepp May 2026 delinquency 7.55% overall / office 11.53% / MF 6.95%.
- Trepp **May 2026** special servicing: **10.86%** overall; office **16.75%**. *(⚠️ June SS print not yet published/indexed as of 7/4 — owed; do not advance the office-SS>18% trigger read off May.)*
- 2026 maturity wall remains live: Morningstar DBRS / accessible corroboration points to **>$100B** CMBS maturities and more than half expected not to repay at maturity; Trepp hard maturities **$76.6B**, **39%** in Q4.
- FDIC Q1 2026 bank PDNA: **1.53%** overall; non-owner CRE and multifamily elevated, but large-bank non-owner CRE PDNA improved to **3.40%**. *(Q2 QBP not yet out.)*
- **Realized-recognition comp cluster (Jun–Jul 2026 — the recognition now printing as REALIZED losses, not just marks; mostly single-source/WALTER-routed unless noted):** 205 W Randolph Chicago office liquidated at a **72% haircut = $12.2M realized CMBS loss** (COMM 2015-CR22; single-source, unverified vs remit); Aon Center Chicago **−58% appraisal** ($780M→$330.5M) with 601W seeking another extension; Bank OZK **deed-in-lieu** on the Seattle U-District "Chapter Buildings" (~394K SF office/life-science, ~$126M current OZK exposure; the LOI-for-recap FAILED — **CONFIRMED 0.85**); Galveston vacant office **$8.79/SF, 0% occ**; **S2 Capital $400M multifamily Fund I dissolved, "no return of capital"** to LPs + $311M North Texas MF at foreclosure this month (**CONFIRMED 0.88** vs The Real Deal primary); 75 West N.Dallas ($90M, Ares 2022 lender) + Austin 526-unit MF ($61.1M-2024 → $9.5M opening bid) forced-sale comps; MF rent concessions **16.9%** (12-yr high, Class-C 21.5% / Sunbelt-led).

Primary source pack: `AGENTS/CREED/research/REFRESH_2026-07-04.md` (current — June Trepp + realized-recognition cluster + 7/2 REIT tape; supersedes `REFRESH_2026-06-21.md`, retained for FDIC-Q1 / maturity-wall source-trail).

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

### 🟠 Signal 5: Multifamily term-default broadening

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

### 🟡 Signal 8: Public REIT equity tape confirms CRE recognition

Trigger examples:
- VNQ underperforms SPY by >10% over 3 months while rates/refi stress or property fundamentals worsen
- office REIT NAV discounts exceed 50% with confirming vacancy/leasing/default evidence
- major office/retail/residential REIT cuts dividend because NOI/refi stress is impairing cash flow
- mREIT book-value/dividend shock points to spread/funding stress relevant to LIQUID

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
| 1 | Office CMBS stress re-accelerates | 3 | delinq **11.57% (+4bps, ticked back up)** [Trepp Jun] / SS 16.75% [May; Jun owed] — elevated, near the >12%/>18% trigger, not fired | ⟂ shares maturity-wall/refi-gap root w/ #2 | delinq >12% & holds OR SS >18% |
| 2 | Maturity-default wave confirms | 3 | **maturity-adjusted DQ 9.53% = new multi-year high** [Trepp Jun] — headline 7.35% masks the past-maturity-still-paying overhang; wall live (>$100B, >50% exp. non-repay; $76.6B hard, 39% Q4) — firmer, not yet majority of new delinq confirmed 2 consec mo | ⟂ shares maturity-wall root w/ #1 | matured-balloon = majority of new delinq 2 consec mo |
| 3 | Bank CRE convergence | 2 | FDIC Q1 large-bank non-owner CRE PDNA **improved** to 3.40% — still counter-direction; **BUT Bank OZK deed-in-lieu on the Seattle U-District credits = a realized bank-CRE REO on a watched name** (single credit; OZK Q2 earnings mid-late-July = provision-bump watch) | ⟂ DOWNSTREAM of #1/#2 (transmission, not an independent root) | FDIC PDNA re-rising + reserve-coverage deterioration |
| 4 | Modification exhaustion / re-default | 2 | no clean aggregate evidence — June headline decline was lodging cures + mods (extend-and-pretend still WORKING at the aggregate), yet Aon + Seattle recaps FAILED (mods failing at the asset level) | Independent (mod mechanism) | re-default / 2nd-mod rates rise |
| 5 | Multifamily term-default broadening | **3 ↑** | **MF delinq RESUMED rising to 7.23% (+28bps)** [Trepp Jun — reverses the May cure] + **Sun Belt 2022-vintage foreclosure cluster** (S2 Capital $400M fund dissolved + $311M N.Texas; 75 West N.Dallas $90M; Austin 526-unit) + concessions **16.9%** Class-C/Sunbelt — building; cluster still TX-concentrated, not yet dominating *outside* NY/NJ/Houston | Independent (property-level) — but MF legs share the Sun-Belt-cluster antecedent w/ #6 | term-defaults dominate outside NY/NJ/Houston |
| 6 | Forced-sale / private-NAV recognition | **3 ↑** | **now a CLUSTER of realized comps >30% below basis** (205 W Randolph **−72% realized** CMBS loss; Aon **−58%** mark; Galveston $8.79/SF; Austin MF; S2 Capital "no return of capital"; Seattle OZK deed-in-lieu) — no longer the single Galveston instance | Independent (LGD/recognition) — MF legs share the Sun-Belt-cluster antecedent w/ #5 | sale >30% below basis as a CLUSTER (now met, single-source); open-end fund gates (not yet) |
| 7 | Office-demand structural hit (tape-confirmed) | 2 | AI-narrative only; data-center demand is a STRENGTH counter-signal (capex rising) | ⟂ shares office-demand root w/ #8 | REIT selloff + direct tenant-demand impairment |
| 8 | Public REIT equity tape confirms | 2 | **COUNTER-SIGNAL [7/2 close]** — VNQ −2.9pp vs SPY/3mo (far from −10 trigger), +6.3pp/1mo; office REITs rallied 5–15%; NOT confirming stress (OZK −5.7% lone dissent) | ⟂ equity-tape read of #7's fundamental | VNQ −10% vs SPY/3mo + confirming fundamentals |

**Composite: 20/40 (moderate; was 18/40 on 6/28).** Base case *selective recognition accelerating* holds and **FIRMED** — recognition is now printing as **realized losses** (205 W Randolph −72% closed CMBS loss; Seattle OZK deed-in-lieu) and **broadening into multifamily** (June MF delinq +28bps + Sun Belt 2022-vintage foreclosure cluster). Two upgrades this window: **S5 Multifamily 2→3, S6 Forced-sale 2→3.** Still **nothing FIRED** — no signal crossed a hard trigger. **Counting once for shared antecedents** — maturity-wall root (S1+S2); office-demand root (S7+S8); Sun-Belt-MF-cluster root shared across S5+S6's MF legs; S3 downstream — = **~4–5 independent roots elevated, not 8.** Do not read 20/40 as broad confirmation; read it as *the recognition-acceleration base case getting louder, still pre-bank-transmission.* ⚠️ Most individual comps are single-source/WALTER-routed (SKIP-VERIFY 0.6–0.82); the two 7/4 items (Seattle OZK, S2 Capital) are WALTER-CONFIRMED (0.85–0.88), and the June aggregate MF/office prints are the load-bearing verified inputs — the anecdotes corroborate the aggregate rather than carrying the read alone.

---

## Counter-Signals

Signals that weaken CREED bear intensity:
- CMBS delinquency falls below **6.5%** with special servicing falling for genuine cures/payoffs, not denominator effects.
- office delinquency falls below **9%** and office special servicing below **13%**.
- 2026 maturity repayments materially outperform the >50% default/non-repayment expectation.
- FDIC bank CRE PDNA continues improving while reserve coverage stabilizes.
- transaction volume and price discovery improve without forced-sale discounts.
- funding/rates ease enough to refinance low-debt-yield cohorts.

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
- multifamily term-default evidence
- rent/occupancy/property-level stress with household spillover potential

---

## Current Open Questions

1. Is Q4 2026 the real maturity-wall pain point, or will borrowers pull forward recognition into Q2/Q3?
2. Are May office/multifamily improvements real cures or large-loan/denominator noise?
3. Which regional/community banks have deteriorating reserve coverage plus high CRE concentration?
4. Does multifamily stress remain metro-specific, or does it broaden into a national property-level problem?
5. Does AI office-demand risk become visible in leasing/vacancy/default data, or remain mostly equity narrative?

---

## Operating Rule

Do not trade directly from CREED. CREED identifies stress mechanisms and routes evidence. Trade construction belongs to TERRY; bank execution belongs to REGINALD; Will approves all trades.
