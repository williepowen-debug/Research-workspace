# STUE SPAWN 2: Deep Dive Analysis
**Date:** 2026-04-06 | **Analyst:** CARL/STUE | **Status:** DRAFT — web search unavailable, synthesized from KB + training data

**NOTE:** WebSearch and WebFetch were denied during this session. This analysis synthesizes existing CARL/STUE knowledge base data (KB-CARL-145 through KB-CARL-151, StudentLoan_Data_2026-02.md, VX-CARL-SL-01 through SL-07) with analyst training knowledge through early 2025 and publicly available structural data. All claims sourced from KB are tagged. Claims derived from structural analysis or training knowledge are tagged [STRUCTURAL/TRAINING]. **Web-verified refresh needed** on all sections — flag to Will for permission or next session with web access.

---

## 1. STATE-LEVEL STUDENT LOAN DQ MAP

### 1A. Worst States by Student Loan DQ/Default Rate

**Available data:** Education Data Initiative and FSA historically report 3-year cohort default rates (CDR) by state. The NY Fed Q4 2025 QHDC reports aggregate national DQ but does NOT break out student loan DQ by state in the public release (it does for mortgages). State-level student loan data comes primarily from FSA CDR data and Education Data Initiative compilations.

**Historical pattern (CDR data, pre-forbearance):** [STRUCTURAL/TRAINING]

| Rank | State | 3-Year CDR (Pre-Forbearance) | Key Driver |
|------|-------|------------------------------|------------|
| 1 | Mississippi | ~18-20% | Lowest median income, for-profit concentration |
| 2 | West Virginia | ~17-19% | Economic decline, aging population |
| 3 | Louisiana | ~16-18% | Low income, high poverty, energy dependence |
| 4 | Alabama | ~16-18% | Structural poverty, low wage base |
| 5 | South Carolina | ~15-17% | Manufacturing decline, for-profit schools |
| 6 | Arkansas | ~15-17% | Rural poverty, limited job market |
| 7 | New Mexico | ~14-16% | Low income, tribal populations |
| 8 | Georgia | ~14-16% | Atlanta metro masks rural distress |
| 9 | Nevada | ~13-15% | For-profit school concentration (ITT, Corinthian legacy) |
| 10 | Tennessee | ~13-15% | Income stratification |

**Post-forbearance DQ explosion (2025-2026):** These historical CDR patterns almost certainly amplified as forbearance ended. The structural drivers (low income, limited labor markets, for-profit school concentration) have not changed. States with high pre-forbearance CDRs are the same states that will have the highest post-forbearance DQ rates.

### 1B. Overlap with CARL Priority States

| CARL State | Student Loan Stress | Overlap Assessment |
|------------|--------------------|--------------------|
| **FL** | MODERATE-HIGH. FL has ~2.5M student loan borrowers. Not in top-10 CDR historically (~11-12%), but: (1) high cost of living amplifies payment burden, (2) UI exhaustion Wave 1 already fired Mar 24 [KB-CARL-113], (3) DOGE RIF cliff June-July compounds student loan stress for federal workers with debt, (4) insurance + HOA squeeze reduces disposable income for loan payments | **STRONG OVERLAP** via cost squeeze amplification |
| **TX** | HIGH. TX has ~3.5M student loan borrowers (2nd largest state portfolio). CDR historically ~12-14%, above national average. (1) Large for-profit school footprint (Dallas, Houston, San Antonio), (2) high subprime concentration in border communities, (3) SSB 19% exposure [KB-CARL-031], (4) energy sector volatility hits borrowers' employment | **STRONG OVERLAP** — volume alone makes TX critical |
| **MD** | CRITICAL. MD is DOGE ground zero [KB-CARL-140]. Federal workers carry above-average student debt. (1) 5.4% of civilian nonfarm is federal [MD Deep Dive], (2) 15K-25K federal jobs lost in 2025, (3) federal workers tend to have graduate degrees with $50K-$150K+ in student debt, (4) MOHELA is primary servicer for many federal PSLF participants — those now losing federal employment ALSO lose PSLF eligibility, creating a double hit: job loss + student loan plan destruction | **CRITICAL OVERLAP** — DOGE + PSLF loss = unique double hit |

### 1C. 18-29 Cohort Geographic Concentration

The 18-29 cohort at 21% 90+ DQ [VX-CARL-SL-02, NY Fed Q4 2025] is concentrated in: [STRUCTURAL/TRAINING]

- **Southern states:** Highest student debt burden relative to income. MS, AL, LA, SC, GA, NC have young borrowers with the lowest starting salaries and highest DQ propensity.
- **Metro areas with for-profit school legacy:** Phoenix, Las Vegas, Orlando, Atlanta, Dallas, Houston — cities where ITT Tech, Corinthian, DeVry, University of Phoenix had highest enrollment.
- **College towns with thin labor markets:** Young graduates in areas without employment opportunities commensurate with their debt load.
- **Gig economy concentration:** 18-29 cohort overlaps heavily with gig workers [KB-CARL-139: gig oversupply confirmed]. Gig workers earn 50-65% of prior traditional pay. Gas $4+ directly squeezes net gig income, reducing capacity to service student loans.

**Key finding:** The 21% 90+ DQ rate for 18-29 is not uniformly distributed. States with low median income, high for-profit school concentration, and thin labor markets likely have 25-30%+ 90+ DQ rates for this cohort. These are the same states where subprime auto DQ and CC DQ are worst — **the stress is additive, not independent.**

### 1D. New Thresholds for STUE to Track

| Metric | Proposed Threshold | Rationale |
|--------|--------------------|-----------|
| State-level 90+ DQ (when available) | >15% for any state | Would confirm geographic concentration thesis |
| 18-29 cohort 90+ DQ | >25% | Currently 21%; crossing 25% = 1-in-4 youngest borrowers in severe distress |
| FL student loan borrowers in default (FSA) | Track absolute count | Cross-reference with UI exhaustion + DOGE |
| MD student loan borrowers in default (FSA) | Track absolute count | DOGE double-hit monitoring |

---

## 2. SAVE TRANSITION PAYMENT SHOCK MODELING

### 2A. SAVE Plan Payment Structure

**SAVE plan payments (current/ending):** [STRUCTURAL/TRAINING, ED.gov]

The SAVE plan (Saving on a Valuable Education), launched August 2023, was the most generous IDR plan ever:
- **Undergraduate only:** 5% of discretionary income (vs 10-20% under prior IDR plans)
- **Graduate + undergrad:** Weighted between 5-10% of discretionary income
- **Discretionary income threshold:** 225% of federal poverty level ($33,975 for single filer in 2025)
- **Result:** Borrowers earning under ~$34K owed **$0/month**
- **Average SAVE payment:** Estimated **$50-70/month** for those with payments >$0; ~50% of SAVE enrollees had **$0 payments** [STRUCTURAL/TRAINING based on ED data]
- **7.5M enrolled** [VX-CARL-SL-03, KB-CARL-147]

### 2B. Standard 10-Year Plan Payment (Auto-Transition Default)

Non-selectors who fail to choose a new plan by ~Oct 1 auto-transition to the 10-year standard plan [KB-CARL-147]:

| Loan Balance | Monthly Payment (10-yr Standard) | SAVE Payment (est.) | Payment Shock Multiple |
|-------------|----------------------------------|---------------------|----------------------|
| $20,000 | ~$220/mo | $0-30/mo | **7-INF x** |
| $30,000 | ~$330/mo | $0-50/mo | **7-INF x** |
| $40,000 | ~$440/mo | $0-70/mo | **6-INF x** |
| $50,000 | ~$550/mo | $0-90/mo | **6-INF x** |
| $75,000 | ~$825/mo | $0-120/mo | **7-INF x** |
| $100,000 | ~$1,100/mo | $0-150/mo | **7-INF x** |

**Average federal student loan balance:** ~$37,000 [Education Data Initiative 2025]
**Average standard 10-year payment at $37K:** ~$407/month

**For borrowers currently paying $0 on SAVE, the shock is from $0 to ~$407/month overnight.** This is not a gradual ramp. It is a cliff.

### 2C. Payment Shock for Non-Selectors

**Critical question: What % of borrowers historically fail to respond to plan selection notices?**

**Precedent — October 2023 forbearance end:** [STRUCTURAL/TRAINING]
- When the COVID forbearance ended (payments resumed Oct 2023), the "on-ramp" protection meant no credit reporting for missed payments through Sep 2024.
- Despite 12+ months of communication, **~20-30% of borrowers failed to resume payments** during the on-ramp period.
- By end of on-ramp (Sep 2024), shadow DQ had already exceeded pre-pandemic levels [StudentLoan_Data_2026-02.md: shadow DQ 15.6% by Sep 2024].
- After on-ramp ended, DQ exploded to 16.3% 30+ (worst ever) [KB-CARL-029].

**For the SAVE→RAP transition, non-selection risk is HIGHER because:**
1. **Borrowers must take affirmative action** — choosing SAVE was opt-in; now they must opt-in AGAIN to RAP or another plan.
2. **Servicer capacity is worse** — MOHELA has 7x-50x peer wait times [VX-CARL-SL-07]. Borrowers who TRY to call may not get through.
3. **Trust is destroyed** — 2.5M received no bills, 800K were made DQ by servicer error, ~2M have credit report errors [KB-CARL-150]. Borrowers may not open mail from servicers they no longer trust.
4. **Information confusion** — SAVE, RAP, PAYE, REPAYE, ICR, Standard, Graduated, Extended, Tiered Standard — the plan landscape is genuinely confusing.

**Estimated non-selection rate: 30-45% of 7.5M = 2.25M-3.375M borrowers auto-transitioned to standard plan.**

This is the most dangerous segment. These borrowers go from $0-70/mo to $330-550/mo with no preparation. At the CARL-confirmed payment hierarchy [FLOW-CARL-4.01], student loan payments compete directly with CC and auto payments for limited income.

### 2D. RAP as Mitigation (Partial)

The RAP (Repayment Assistance Plan) launching July 1 offers: [KB-CARL-147]
- 1-10% of AGI
- $10/month minimum
- 30-year forgiveness

**RAP is less generous than SAVE** (no 225% FPL exemption, no 5% rate for undergrad-only). But it IS more affordable than standard. The question is: **how many borrowers will successfully enroll?**

**Operational capacity concern:**
- MOHELA services ~16.5M accounts (largest servicer) [STRUCTURAL/TRAINING]
- 2.5M already didn't receive bills [KB-CARL-150]
- July 1 = 7.5M simultaneous transition notices
- If even 30% call for help = 2.25M calls in weeks
- MOHELA wait times already 7x-50x peers [VX-CARL-SL-07]
- Treasury transfer (Phase 1 active Mar 19) creating additional operational chaos [KB-CARL-148]

**Assessment:** RAP will absorb 40-55% of SAVE borrowers who actively select. The remaining 30-45% will either default to standard plan (payment shock) or simply stop paying (adding to default pipeline). Net effect: RAP reduces the July shock but does not prevent it. **Estimated 2.25M-3.375M borrowers face unmitigated payment shock.**

### 2E. Dollar Impact on Consumer Spending

**Back-of-envelope:**
- 7.5M borrowers x average payment increase of ~$200-350/mo (from $0-70 to $200-407 depending on plan)
- Conservative: 7.5M x $200/mo = **$1.5B/month redirected from consumption**
- Mid-range: 7.5M x $275/mo = **$2.06B/month**
- Aggressive (non-selectors at standard): 3M x $350/mo = **$1.05B/month from this cohort alone**

**For context:** JPMorgan estimated collections on defaulted loans could reduce disposable income $3.1-8.5B/month [StudentLoan_Data_2026-02.md]. The SAVE transition adds another $1.5-2B/month of spending destruction on TOP of collections resumption.

**Timeline:** This spending destruction begins July 1 and accelerates through Q3 — landing squarely in CARL's "consumption stress quarter" when UI exhaustion ($800M-$930M/mo), gas $4+, and food CPI loading are all simultaneously active [CARL STATUS.md Danger Window].

---

## 3. CREDIT SCORE DESTRUCTION CASCADE

### 3A. Quantifying the Population at Risk

**Starting population:** [KB-CARL-145, KB-CARL-146, KB-CARL-150]
- 7.7M already in default ($180B) as of Dec 2025
- 7.5M on SAVE facing transition (some overlap with default population)
- ~9M+ facing credit score damage (NY Fed estimate)
- 13M projected default by EOY 2026 (TCF projection) [KB-CARL-146]
- 800K made DQ by MOHELA servicer failure alone [KB-CARL-150]
- ~2M credit report errors (balance duplication) [KB-CARL-150]

**Unique at-risk population (deduped estimate):** 10-12M borrowers will experience meaningful credit score damage in 2026.

### 3B. Credit Score Drop Magnitude

From NY Fed Liberty Street Economics (Mar 2025) [StudentLoan_Data_2026-02.md]:

| Prior Credit Score | Average Score Drop | Post-DQ Score | Credit Access Impact |
|--------------------|-------------------|---------------|---------------------|
| 760+ (Superprime) | **-171 pts** | ~589-600 | Loses prime mortgage/auto eligibility |
| 720-759 (Prime) | **-165 pts** | ~555-594 | Drops to deep subprime |
| 660-719 (Near-prime) | **-165 pts** | ~495-554 | Below most lending thresholds |
| 620-659 (Subprime) | **-143 pts** | ~477-516 | Effectively locked out |
| <620 (Deep subprime) | **-87 pts** | ~<533 | Already locked out; score damage is symbolic |

**The most destructive impact is on PRIME and NEAR-PRIME borrowers.** A 760+ borrower dropping to ~590 goes from qualifying for the best mortgage rates to being denied entirely. This is not a marginal shift — it is a categorical reclassification from "creditworthy" to "subprime."

### 3C. Downstream Credit Product Impact

**How many lose mortgage eligibility?**

Minimum credit scores for mortgage products: [STRUCTURAL/TRAINING]
- Conventional (Fannie/Freddie): 620 minimum (practically 680+ for competitive rates)
- FHA: 580 minimum (500 with 10% down)
- VA: No minimum but most lenders require 620+
- USDA: 640 typically

**Estimate:** Of the 10-12M borrowers facing credit score damage:
- ~3-4M currently have scores 660-760+ and would drop below conventional mortgage thresholds
- ~1-2M are actively in the housing market or planning to buy within 2 years
- **Net housing demand suppression: 1-2M potential buyers removed from the market**

This reinforces CARL's housing thesis: 878K already in 90+/foreclosure pipeline [CARL STATUS.md], cure rates -40%, and now 1-2M additional buyers removed from demand side = price support eroding from both supply (foreclosures) and demand (credit destruction).

**How many lose auto loan eligibility?**

Auto loan minimums: [STRUCTURAL/TRAINING]
- Prime auto: 660+
- Near-prime: 620-659
- Subprime: 580-619
- Deep subprime: <580

**Estimate:** ~4-5M borrowers would drop below 620, significantly limiting auto loan access or repricing to subprime rates (+3-5% interest rate increase = $100-200/mo on a $30K loan).

**How many lose CC eligibility or get repriced?**

- Issuers tighten at portfolio level when DQ rates rise
- Individual score drops trigger: (1) credit line reductions, (2) APR increases to penalty rate (often 29.99%), (3) new application denials
- **Estimate:** 6-8M borrowers face CC access reduction or repricing

### 3D. Payment Hierarchy Cascade Model

CARL's established payment hierarchy [FLOW-CARL-4.01]: **Auto > Mortgage > Student > CC**

When a borrower faces a student loan payment shock (e.g., $0 → $400/mo), the cascade plays out:

1. **Month 0-1:** Borrower attempts to pay all obligations. Savings depleted or CC used to bridge.
2. **Month 2-3:** CC minimum payments missed first (last priority in hierarchy). CC 30+ DQ.
3. **Month 4-6:** If stress persists, auto payment strain begins. Auto 30+ DQ.
4. **Month 6-9:** Mortgage stress if income insufficient. Mortgage 30+ DQ.
5. **Month 9+:** Full default cascade across all products.

**BUT student loan is UNIQUE in the hierarchy because of credit score destruction:**

The -87 to -171 point credit score drop from student loan DQ ITSELF triggers:
- CC line cuts → reduced float → cash flow emergency → CC DQ accelerates (Months 1-2 instead of 2-3)
- Auto refinancing blocked → trapped in high-rate loan → cash flow squeeze
- Mortgage application denied → forced to rent at higher cost → further cash flow reduction

**Net effect: Student loan DQ doesn't just compete in the payment hierarchy — it ACCELERATES all downstream DQ through the credit score destruction channel.** This is a cascade amplifier, not just another competing payment.

### 3E. Quantified Cascade Estimate

| Product | Borrowers Impacted (from SL stress) | Timeline | Mechanism |
|---------|-------------------------------------|----------|-----------|
| CC 30+ DQ | 3-5M additional | Q3-Q4 2026 | Payment hierarchy + CC line cuts from score drops |
| Auto 30+ DQ | 1.5-2.5M additional | Q4 2026-Q1 2027 | Score-driven repricing + payment competition |
| Mortgage DQ | 0.5-1M additional | Q1-Q2 2027 | Score below threshold + income squeeze |
| Rental denials | 1-2M additional | Q3 2026+ | Landlords screen credit; score drops = denials |

**For CARL's CC thesis:** If even 2-3M student loan borrowers cascade into CC DQ, that adds approximately 0.5-1.0pp to the CC 90+ DQ rate over 2-3 quarters. Current CC 90+ DQ: 12.70%. Adding student loan cascade: **13.2-13.7% — essentially AT or ABOVE GFC peak (13.74%).**

This means the student loan vector may be the mechanism that pushes CC 90+ DQ past the GFC threshold (CRL-05, currently at 75% confidence). **Recommend upgrading CRL-05 confidence to 80-85%** based on this cascade analysis.

---

## 4. SERVICER PERFORMANCE DEEP DIVE

### 4A. MOHELA — Operational Failure at Scale

**Established facts:** [KB-CARL-150, VX-CARL-SL-07]
- 2.5M borrowers did not receive bills → 800K became delinquent
- DOE withheld $7.2M as penalty (inadequate — amounts to $2.88 per affected borrower)
- Wait times: 7x ED Financial Partners, 50x Aidvantage/CRI/Nelnet
- AFT (American Federation of Teachers) lawsuit filed
- Multiple state AG investigations
- Senate investigation (Warren) found MOHELA contributed to ~2M credit report errors
- MOHELA is the largest federal student loan servicer (~16.5M accounts) [STRUCTURAL/TRAINING]

**What this means for July 1:** MOHELA will be responsible for notifying millions of SAVE borrowers about the transition and helping them select new plans. Given that:
- They already failed to deliver bills to 2.5M borrowers
- Their call center capacity is 7-50x worse than peers
- They are simultaneously under investigation by multiple state AGs and the Senate
- The Treasury transfer is creating organizational uncertainty

**The probability of a clean July 1 transition is near zero.** MOHELA's operational failures will AMPLIFY the non-selection rate, pushing more borrowers into the auto-transition to standard plan (payment shock) and generating additional manufactured delinquency.

**Estimated MOHELA-caused additional defaults from July transition:** 500K-1M borrowers who would have selected RAP or another affordable plan but fail due to servicer inability to process their request in time.

### 4B. Nelnet — Credit Reporting Errors

**Established facts:** [KB-CARL-150]
- Class action filed Feb 18, 2026 for credit report balance duplication
- Affects both MOHELA and Nelnet borrowers
- Doubled balances on credit reports = artificially inflated DTI ratios
- Impact: mortgage denials, auto loan denials, CC line reductions — even for borrowers who are CURRENT on payments

**This is particularly insidious because:** A borrower who is doing everything right — paying on time, in an affordable plan — can still have their credit destroyed by a servicer error that doubles their reported balance. The borrower may not discover this until they apply for a mortgage or auto loan and get denied.

### 4C. State AG and Legal Activity

**Known investigations/actions:** [VX-CARL-SL-07, STRUCTURAL/TRAINING]
- Multiple state AG investigations into MOHELA (states not fully enumerated in KB)
- AFT lawsuit
- Senate investigation (Warren)
- Class action (Feb 18, 2026) for credit report errors
- CFPB complaints trending upward [STUE CLAUDE.md references CFPB as data source]
- Sweet v. McMahon: Ninth Circuit rejected DOE delay (Mar 25, 2026) — 205K auto-discharges proceeding [KB-CARL-149]

**Expected escalation:**
- As July 1 approaches and servicer failures compound, expect: (1) additional state AG actions, (2) possible Congressional hearings, (3) class action expansion, (4) CFPB enforcement actions (if CFPB survives current political environment)
- Treasury transfer legal challenges may create jurisdictional confusion — who is responsible for borrower harm when the portfolio is being transferred mid-crisis?

### 4D. Servicer Performance Thresholds for STUE

| Metric | Current | Watch | Alert | Critical | Source |
|--------|---------|-------|-------|----------|--------|
| MOHELA call abandonment rate | Unknown — needs research | >20% | >35% | >50% | DOE/CFPB |
| CFPB student loan complaints (monthly) | Unknown — needs pull | >5,000 | >10,000 | >20,000 | CFPB |
| Credit report error class actions | 1 (Feb 18) | 2 | 3+ | 5+ | Court dockets |
| State AG investigations | Multiple | 5+ | 10+ | 15+ | State AG offices |
| Servicer penalty amounts (DOE) | $7.2M | $15M | $25M | $50M+ | DOE |
| New borrower defense claims/month | Unknown | >10,000 | >25,000 | >50,000 | FSA |

---

## 5. SYNTHESIS: INTEGRATION WITH CARL'S THESIS

### 5A. Student Loan Vector as Cascade Amplifier

The student loan crisis is not just one of CARL's 10 convergence vectors — it is a **cascade amplifier** that intensifies at least 4 other vectors:

1. **CC 90+ DQ → GFC (Vector 1):** Student loan payment shock and credit score destruction directly cascade into CC DQ. Estimated +0.5-1.0pp to CC 90+ DQ rate. This may be the mechanism that pushes CC past GFC peak.

2. **Subprime Auto 60+ DQ (Vector 2):** Credit score destruction from student loans locks borrowers out of prime auto refinancing, trapping them in high-rate loans. Additional auto DQ from payment competition.

3. **K-Shape Converging (Vector 9):** Student loans are the K-shape convergence vector par excellence. The 18-29 cohort at 21% 90+ DQ are overwhelmingly in the bottom 60%. But PSLF participants losing federal jobs (MD/DC) are in the top 40% — college-educated, $80K-150K earners whose PSLF eligibility evaporates with their federal employment. Student loan stress is hitting BOTH K-shape cohorts simultaneously.

4. **Foreclosure Acceleration (Vector 10):** 1-2M potential buyers removed from housing demand through credit score destruction. Price support erodes. Existing borrowers with student loan + mortgage stress face payment hierarchy competition.

### 5B. Timing Alignment with Q3 2026 Consumption Stress Quarter

The student loan vector's July 1 trigger date is **perfectly aligned** with CARL's Q3 2026 consumption stress quarter:

| Vector | Q3 Trigger | Monthly Impact |
|--------|-----------|---------------|
| UI exhaustion peak | July-Aug | $800M-$930M/mo spending hole |
| Student loan SAVE transition | July 1 | $1.5-2.0B/mo redirected from consumption |
| Gas $4+ sustained | Ongoing | $150-200/mo per 2-car household |
| Food CPI loading | Q3-Q4 onset | TBD (fertilizer → grocery 4-6mo lag) |
| FL UI exhaustion cliff | June-July | $7.4M/mo FL spending hole |

**Combined Q3 spending destruction estimate:** $3-4B/month minimum from these vectors alone. This is before any employment deterioration (which would accelerate all of these).

### 5C. Implications for Convergence Score

Current student loan vector: **5/5 (max)** [CARL STATUS.md Convergence Matrix]

This analysis confirms the max score is justified. The July 1 catalyst creates a hard date for stress acceleration. The cascade amplification effect means the student loan vector's true contribution to systemic risk exceeds its own 5/5 score — it raises the effective score of Vectors 1, 2, 9, and 10.

### 5D. Predictions / Recommendations

**For CARL thesis:**

1. **Upgrade CRL-05 confidence** (CC 90+ DQ >13.74% GFC breach): Current 75% → recommend 80-85%. Student loan cascade into CC DQ provides an additional pathway to GFC breach beyond employment deterioration.

2. **New prediction candidate:** SAVE non-selection rate >35% (est. 2.6M+ borrowers auto-transition to standard plan). Timeframe: Oct 1, 2026 (end of selection window). Confidence: 70%.

3. **New prediction candidate:** MOHELA-caused additional defaults from July transition: 500K-1M. Timeframe: Q3-Q4 2026. Confidence: 65%.

4. **Watch for:** NY Fed Q1 2026 QHDC release (May-Jun) — first data point showing post-collections-resume DQ. If 90+ DQ crosses 10% (currently 9.6%), student loan DQ will be the WORST of any consumer credit category by historical comparison.

### 5E. Data Gaps Requiring Web Research (Next Session)

These items need live web research — flag for next session with WebSearch/WebFetch enabled:

| Topic | Why It Matters | Priority |
|-------|---------------|----------|
| State-level student loan DQ data (FSA/Ed Data Initiative) | Confirm geographic concentration thesis | HIGH |
| MOHELA call center metrics (Apr 2026) | Pre-July operational capacity assessment | HIGH |
| CFPB student loan complaint volume (2026 monthly) | Servicer performance leading indicator | HIGH |
| RAP enrollment rate (if any early data) | Mitigant assessment | HIGH |
| New class actions / state AG actions (Apr 2026) | Legal environment monitoring | MEDIUM |
| SAVE borrower demographics by state | Refine geographic concentration model | MEDIUM |
| Historical IDR plan non-selection rates | Validate 30-45% non-selection estimate | MEDIUM |
| Post-Oct 2023 forbearance-end outcomes study | Improve precedent model | MEDIUM |

---

## 6. RISK MATRIX SUMMARY

| Risk | Probability | Impact | Timeline | Mitigant |
|------|------------|--------|----------|----------|
| 30-45% SAVE non-selection → payment shock | 70% | HIGH — 2.25-3.375M face $0→$400+/mo cliff | Oct 2026 | RAP enrollment (partial) |
| MOHELA operational failure during transition | 85% | HIGH — 500K-1M additional manufactured DQ | Jul-Oct 2026 | DOE penalties (inadequate) |
| Credit score cascade → CC/auto DQ | 80% | HIGH — +0.5-1.0pp to CC 90+ DQ | Q3-Q4 2026 | None identified |
| Student loan DQ 90+ crosses 10% | 90% | SIGNAL — worst consumer credit category | Q1-Q2 2026 data | Forbearance restoration (unlikely) |
| 13M default by EOY 2026 | 60% | EXTREME — generational credit event | EOY 2026 | Mass forgiveness (unlikely under current admin) |
| Housing demand suppression (1-2M buyers removed) | 75% | MEDIUM-HIGH — reinforces housing price decline | Q3 2026+ | Score repair takes 12-24 months |
| PSLF participants lose eligibility (DOGE) | 70% (for MD/DC affected) | HIGH for affected borrowers (top-40% K-shape) | Ongoing | Rehiring (unlikely) |

---

*Analysis complete. Web-verified data refresh needed on all sections. Recommend next STUE spawn with WebSearch enabled to fill data gaps identified in Section 5E.*

*Sub-agent of CARL. See CARL STATUS.md and STUE STATUS.md for dashboard context.*
