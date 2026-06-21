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
