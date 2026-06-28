# CREED Thesis Rails

**Created:** 2026-06-21 15:10 ET  
**Status:** Current rails v1.0 after Phase 3 refresh  
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
- Trepp May 2026 CMBS delinquency: **7.55%** overall; office **11.53%**; multifamily **6.95%**.
- Trepp May 2026 special servicing: **10.86%** overall; office **16.75%**.
- 2026 maturity wall remains live: Morningstar DBRS / accessible corroboration points to **>$100B** CMBS maturities and more than half expected not to repay at maturity; Trepp hard maturities **$76.6B**, **39%** in Q4.
- FDIC Q1 2026 bank PDNA: **1.53%** overall; non-owner CRE and multifamily elevated, but large-bank non-owner CRE PDNA improved to **3.40%**.

Primary source pack: `AGENTS/CREED/research/REFRESH_2026-06-21.md`.

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

*Added 2026-06-28 per DAEDALUS BATCH_01.* Maps the 8 Expected Signals onto the universal 5-pt scale so NEXUS/PROME can stack CREED's national-CRE read **without spawning the tier-2 agent**. Scale: 5 firing → 4 🔴 elevated → 3 🟠 building/near-trigger → 2 🟡 latent → 1 ⚪ dormant. Independence = shared-antecedent flag (count a shared root once). *Current reads carry as-of dates — refresh on the Monday pulls before re-scoring.*

| # | Vector (Expected Signal) | Score | Local state / current read [as-of] | Independence | Upgrade trigger |
|---|---|---:|---|---|---|
| 1 | Office CMBS stress re-accelerates | 3 | delinq 11.53% / SS 16.75% [Trepp May] — elevated, near the >12%/>18% trigger, not fired | ⟂ shares maturity-wall/refi-gap root w/ #2 | delinq >12% & holds OR SS >18% |
| 2 | Maturity-default wave confirms | 3 | wall live (>$100B, >50% exp. non-repay; $76.6B hard, 39% Q4) — building, not yet majority of new delinq | ⟂ shares maturity-wall root w/ #1 | matured-balloon = majority of new delinq 2 consec mo |
| 3 | Bank CRE convergence | 2 | FDIC Q1 large-bank non-owner CRE PDNA **improved** to 3.40% — counter-direction | ⟂ DOWNSTREAM of #1/#2 (transmission, not an independent root) | FDIC PDNA re-rising + reserve-coverage deterioration |
| 4 | Modification exhaustion / re-default | 2 | no current evidence | Independent (mod mechanism) | re-default / 2nd-mod rates rise |
| 5 | Multifamily term-default broadening | 2 | multifamily delinq 6.95% [Trepp May], some cure — not broadening | Independent (property-level) | term-defaults dominate outside NY/NJ/Houston |
| 6 | Forced-sale / private-NAV recognition | 2 | Galveston = single instance, NOT a cluster | Independent (LGD/recognition) | sale >30% below basis as a CLUSTER; open-end fund gates |
| 7 | Office-demand structural hit (tape-confirmed) | 2 | AI-narrative only; data-center demand is a STRENGTH counter-signal (capex rising) | ⟂ shares office-demand root w/ #8 | REIT selloff + direct tenant-demand impairment |
| 8 | Public REIT equity tape confirms | 2 | VNQ vs SPY not confirmed; Monday pull owed | ⟂ equity-tape read of #7's fundamental | VNQ −10% vs SPY/3mo + confirming fundamentals |

**Composite: 18/40 (low-moderate).** Base case *selective recognition accelerating* holds — nothing fired; office-CMBS (S1) is the hottest at near-trigger. **Counting once for shared antecedents** (maturity-wall root S1+S2; office-demand root S7+S8; S3 downstream) = **~4 independent roots elevated, not 8** — do not read 18/40 as broad confirmation.

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
