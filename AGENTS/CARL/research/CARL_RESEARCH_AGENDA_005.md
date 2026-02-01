# CARL Research Agenda — Session 005
## Gap Analysis and External Research Plan

**Created:** 2026-01-20
**Purpose:** Address identified gaps in CARL ecosystem coverage
**Method:** External LLM research agents to preserve CARL context

---

## Research Priority Matrix

| Priority | Gap | Urgency | Impact | Effort | Recommended Action |
|----------|-----|---------|--------|--------|-------------------|
| **P1** | Elder Financial Stress | HIGH | HIGH | MEDIUM | New agent (GRAY) |
| **P1** | Geographic Concentration | HIGH | HIGH | LOW | Overlay layer |
| **P1** | Eviction Pipeline | HIGH | MEDIUM | LOW | Expand CARL vectors |
| **P2** | Tax Debt | MEDIUM | MEDIUM | LOW | Add CARL/NICK vectors |
| **P2** | Food Insecurity | MEDIUM | MEDIUM | LOW | Add CARL vector |
| **P2** | Cross-Agent Intersections | MEDIUM | HIGH | MEDIUM | Formalize tracking |
| **P3** | Childcare Burden | LOW | MEDIUM | MEDIUM | Defer or add to CARL |
| **P3** | Crypto/Speculative Losses | LOW | LOW | LOW | Add behavioral vector |
| **P3** | Regulatory Tracking | LOW | MEDIUM | MEDIUM | Systematize FL approach |

---

## Research Prompt Instructions

**For the human operator:**

Each prompt below is designed to be copy-pasted to an external LLM agent (Claude, GPT, etc.). The prompts are self-contained and specify:
- Context needed
- Specific questions to answer
- Output format required
- Sources to prioritize

**When you receive results:**
1. Save output to `C:\Projects\CARL_Methodology\research\[TOPIC]_research_[DATE].md`
2. Flag key findings for CARL integration
3. Note any data gaps or quality issues
4. Identify potential new vectors or agents

---

# PRIORITY 1 RESEARCH PROMPTS

---

## PROMPT 1A: ELDER FINANCIAL STRESS — Landscape Assessment

```
RESEARCH TASK: Elder/Retiree Financial Stress Assessment

CONTEXT:
You are conducting research to support a consumer financial stress monitoring system. We need to understand the financial stress landscape for Americans aged 60+ (retirees and near-retirees). This population has distinct dynamics from working-age consumers.

RESEARCH QUESTIONS:

1. INCOME & INFLATION
   - What is the gap between Social Security COLA adjustments and actual senior spending inflation (healthcare, housing, food)?
   - What percentage of retirees rely on Social Security as primary income (>50% of income)?
   - What is the trend in real (inflation-adjusted) retiree income over the past 5 years?

2. HEALTHCARE COSTS
   - What are out-of-pocket healthcare costs for Medicare beneficiaries (premiums, deductibles, uncovered services)?
   - What percentage of retirees report delaying care due to cost?
   - What is the average/median long-term care cost, and what percentage have LTC insurance?
   - How many seniors face "Medicare cliff" issues (income-based premium surcharges)?

3. HOUSING STRESS
   - What percentage of seniors are housing cost-burdened (>30% of income)?
   - What are reverse mortgage trends (originations, defaults, foreclosures)?
   - What percentage of seniors still carry mortgage debt into retirement?
   - Are seniors disproportionately affected by property tax increases?

4. DEBT STRESS
   - What is credit card delinquency rate for 60+ population vs younger cohorts?
   - Are seniors showing different auto loan stress patterns?
   - How much student loan debt do borrowers 60+ carry (Parent PLUS, own debt)?
   - What percentage of seniors have debt in collections?

5. RETIREMENT SAVINGS ADEQUACY
   - What percentage of retirees have less than $50K in retirement savings?
   - What is the median retirement account balance by age cohort (60-65, 65-70, 70+)?
   - What are hardship withdrawal rates for near-retirees (55-65)?
   - How many seniors are returning to work due to financial necessity?

6. EXPLOITATION & FRAUD
   - What are annual elder financial exploitation losses?
   - What are trends in scam losses for 60+ population?
   - How does cognitive decline correlate with financial vulnerability?

7. PENSION & SOCIAL SECURITY
   - What is the current state of state/local pension funding (% funded)?
   - Which states/cities have most underfunded pensions?
   - Are any pension plans in "critical" or "endangered" status?
   - What percentage of private sector retirees have defined benefit pensions vs DC only?

OUTPUT FORMAT:
Please provide:
1. Executive summary (1 paragraph) of elder financial stress landscape
2. Key statistics table with source citations and dates
3. Identified stress vectors with potential thresholds
4. Data gaps or quality concerns
5. Recommended data sources for ongoing monitoring
6. Assessment: Is this population showing LEADING, LAGGING, or COINCIDENT stress relative to working-age consumers?

PRIORITIZE SOURCES:
- Federal Reserve Survey of Consumer Finances
- Census Bureau (ACS, SIPP)
- CMS Medicare data
- Social Security Administration
- CFPB elder financial exploitation reports
- Pension Benefit Guaranty Corporation
- Academic research (NBER, Brookings)
- AARP research

DATE CONTEXT: Current date is January 2026. Prioritize 2024-2025 data where available.
```

---

## PROMPT 1B: ELDER FINANCIAL STRESS — Vector Design

```
RESEARCH TASK: Design Monitoring Vectors for Elder Financial Stress

CONTEXT:
Based on elder financial stress research, we need to design specific monitoring vectors for a potential new agent (GRAY) in our consumer stress monitoring system.

Our vector format includes:
- Vector ID and Name
- Mechanism (how stress manifests)
- Tripwire (threshold that triggers escalation)
- What to Track (data sources and indicators)
- Status levels: NORMAL → ELEVATED → CRITICAL → BREACHED
- Transmission (what breaks next if this vector deteriorates)

TASK:
Design 8-12 vectors covering elder financial stress. For each vector, provide:

1. VX-GRAY-X.XX: [Vector Name]
   - Domain: [INCOME, HEALTHCARE, HOUSING, DEBT, RETIREMENT, EXPLOITATION]
   - Priority: P1/P2
   - Mechanism: How does this stress manifest and escalate?
   - Tripwire:
     - Metric: [Specific measurable metric]
     - Threshold: [Level that triggers CRITICAL or BREACHED]
     - Current value: [If known from research]
   - What to Track: [Specific data sources]
   - Transmission: [What downstream effects occur]

ALSO PROVIDE:
1. Suggested FLOW pathways (cascade mechanisms) for elder stress
2. Cross-references to existing CARL vectors that elder stress affects
3. Invalidation criteria (what would prove elder stress thesis wrong)
4. Recommended monitoring cadence (monthly, quarterly, annual data)

EXAMPLE FORMAT (from existing system):
```
VX-CARL-1.04:
  name: "Auto Affordability Collapse"
  domain: CREDIT_SECURED
  priority: P1
  mechanism: |
    Average new car payment >$700/month + negative equity widespread →
    Prioritization hierarchy breaks → Skip auto to pay rent/cards →
    Voluntary surrenders increase
  tripwire:
    metric: "Subprime Auto 60+ DQ"
    threshold: 7.0%
    current: 6.65%
  what_to_track:
    - Equifax/Experian auto reports
    - Manheim used car index
    - Repo statistics
  status: "BREACHED - All-time record"
  transmission: ["Bank NCOs", "Used car price collapse"]
```

Design vectors that are:
- Measurable with available data
- Diagnostic (distinguish elder stress from general consumer stress)
- Actionable (clear thresholds)
- Connected (show transmission to broader system)
```

---

## PROMPT 2: GEOGRAPHIC CONCENTRATION ANALYSIS

```
RESEARCH TASK: Geographic Concentration of Consumer Financial Stress

CONTEXT:
You are researching geographic patterns in consumer financial stress for a monitoring system. National averages mask regional extremes. We need to identify which regions/states/metros are LEADING indicators vs LAGGING.

RESEARCH QUESTIONS:

1. CREDIT STRESS GEOGRAPHY
   - Which states have highest credit card delinquency rates?
   - Which metros have highest auto loan delinquency?
   - Are there regional patterns in subprime concentration?
   - Which states have highest BNPL usage rates?

2. HOUSING STRESS GEOGRAPHY
   - Which metros have highest rent burden (rent as % of income)?
   - Which states have highest eviction filing rates?
   - Where is housing cost growth most outpacing income growth?
   - Which markets have highest mortgage delinquency?

3. EMPLOYMENT STRESS GEOGRAPHY
   - Which metros have highest unemployment/underemployment?
   - Where are tech layoffs concentrated?
   - Which regions have highest long-term unemployment?
   - Where is gig economy saturation worst?

4. INSURANCE STRESS GEOGRAPHY
   - Beyond FL/CA, which states have homeowners insurance crises?
   - Which states have highest uninsured motorist rates?
   - Where are health insurance costs most burdensome?

5. HEALTHCARE STRESS GEOGRAPHY
   - Which states have highest medical debt rates?
   - Where is care deferral most common?
   - Which regions have worst healthcare access?

6. SMALL BUSINESS STRESS GEOGRAPHY
   - Which metros have highest small business closure rates?
   - Where are Chapter 11 filings concentrated?
   - Which regions depend most on small business employment?

7. CLIMATE/DISASTER RISK GEOGRAPHY
   - Which regions face compounding climate + financial stress?
   - Where are insurance availability crises + housing stress overlapping?
   - Which areas have highest disaster-related financial stress?

8. COMPOSITE STRESS CLUSTERS
   - Can you identify 5-10 metro areas or regions showing MULTIPLE stress indicators simultaneously?
   - Are there "canary" geographies that lead national trends?
   - Are there resilient geographies that are weathering stress better?

OUTPUT FORMAT:
1. Heat map description: Which regions are hottest for each stress type
2. Composite stress ranking: Top 10 most stressed metros/regions
3. Leading indicator geographies: Areas that historically lead national trends
4. Data sources for geographic monitoring
5. Recommended geographic segmentation for ongoing tracking

PRIORITIZE SOURCES:
- Federal Reserve regional data
- Census Bureau ACS
- State-level delinquency data
- Eviction Lab
- Urban Institute
- Brookings Metro Monitor
- State insurance commissioner data
```

---

## PROMPT 3: EVICTION PIPELINE ANALYSIS

```
RESEARCH TASK: Eviction and Housing Displacement Pipeline

CONTEXT:
You are researching the eviction pipeline for a consumer financial stress monitoring system. Eviction is often the terminal event in housing stress cascade. We currently track rent late rates (11.7%) but need to understand the full pipeline from late payment to homelessness.

RESEARCH QUESTIONS:

1. EVICTION FILING TRENDS
   - What are current national eviction filing rates vs pre-pandemic baseline?
   - Which metros have returned to or exceeded pre-pandemic eviction levels?
   - What is the typical lag from rent delinquency to eviction filing?
   - What percentage of filings result in actual eviction (judgment + execution)?

2. EVICTION EXECUTION
   - How many households are actually evicted annually?
   - What is the gap between filings and executions?
   - How do eviction moratorium expirations affect execution rates?
   - What is the average time from filing to physical removal?

3. INFORMAL DISPLACEMENT
   - How many households leave before formal eviction (informal displacement)?
   - What percentage of moves are "forced" vs voluntary?
   - How does landlord harassment factor into displacement?

4. POST-EVICTION OUTCOMES
   - What percentage of evicted households become homeless?
   - What is the typical trajectory: doubled-up → shelter → street?
   - How does eviction affect employment (job loss rates)?
   - What is credit score impact of eviction?

5. HOMELESSNESS INFLOW
   - What are current homeless count trends (PIT counts)?
   - What percentage of new homeless cite eviction as cause?
   - Is shelter capacity keeping pace with demand?
   - What are unsheltered population trends?

6. VULNERABLE POPULATIONS
   - Which demographics face highest eviction risk?
   - Are families with children at higher risk?
   - How do eviction rates vary by race/ethnicity?
   - What is eviction impact on children (school, health)?

7. LEGAL AND POLICY CONTEXT
   - Which states have strongest/weakest tenant protections?
   - What is status of pandemic-era eviction protections?
   - Are any new eviction prevention programs active?
   - How does legal representation affect eviction outcomes?

OUTPUT FORMAT:
1. Pipeline flow diagram: Delinquency → Filing → Judgment → Execution → Displacement → Homelessness (with percentages at each stage)
2. Current national eviction metrics with trends
3. Geographic hotspots for eviction stress
4. Recommended vectors and thresholds for monitoring
5. Data sources for ongoing tracking
6. Assessment: Is eviction stress accelerating, stable, or declining?

PRIORITIZE SOURCES:
- Eviction Lab (Princeton)
- HUD Point-in-Time counts
- Census Household Pulse Survey
- National Alliance to End Homelessness
- Urban Institute housing research
- State/local court records
- Legal aid organization reports
```

---

# PRIORITY 2 RESEARCH PROMPTS

---

## PROMPT 4: TAX DEBT AND IRS STRESS

```
RESEARCH TASK: Consumer Tax Debt and IRS Enforcement Stress

CONTEXT:
You are researching tax debt as a potential hidden layer of consumer financial stress. Tax debt is non-dischargeable in bankruptcy, carries federal enforcement powers, and often surprises consumers—especially gig workers who lack withholding. This may be another form of "phantom debt" not captured in traditional credit metrics.

RESEARCH QUESTIONS:

1. TAX DEBT MAGNITUDE
   - What is total outstanding individual tax debt owed to IRS?
   - How many taxpayers have outstanding tax debt?
   - What is the distribution of tax debt (median, mean, concentration)?
   - What are trends in tax debt over past 5 years?

2. PAYMENT PLANS
   - How many taxpayers are on IRS installment agreements?
   - What are trends in installment agreement enrollment?
   - What is the default rate on IRS payment plans?
   - What are typical payment plan terms and monthly amounts?

3. ENFORCEMENT
   - What are trends in IRS wage garnishments?
   - How many tax liens are filed annually?
   - What are bank levy statistics?
   - How has IRS enforcement capacity changed with funding changes?

4. GIG WORKER TAX STRESS
   - What percentage of gig workers face unexpected tax bills?
   - What is estimated tax compliance rate for 1099 workers?
   - How much do gig workers typically owe at tax time?
   - Are gig workers using high-cost tax refund anticipation products?

5. STATE TAX DEBT
   - What are trends in state income tax debt?
   - Which states are most aggressive in tax enforcement?
   - Are state tax liens increasing?

6. REFUND ANTICIPATION PRODUCTS
   - What is the market size for refund anticipation loans/checks?
   - What are typical costs/fees for these products?
   - Which demographics use these products most?
   - How does EITC timing affect low-income tax stress?

7. TAX DEBT AND CREDIT
   - How does tax debt affect credit scores?
   - Are tax liens reported to credit bureaus?
   - How does tax debt interact with other financial stress?

OUTPUT FORMAT:
1. Tax debt landscape summary
2. Key statistics with sources
3. Gig worker tax stress assessment
4. Potential monitoring vectors and thresholds
5. Connection to existing CARL/NICK vectors
6. Data sources for ongoing monitoring

PRIORITIZE SOURCES:
- IRS Data Book (annual)
- Treasury Inspector General reports
- National Taxpayer Advocate reports
- Tax Policy Center
- Urban-Brookings Tax Policy Center
- GAO reports on tax administration
- Academic research on tax compliance
```

---

## PROMPT 5: FOOD INSECURITY ASSESSMENT

```
RESEARCH TASK: Food Insecurity as Consumer Stress Indicator

CONTEXT:
You are researching food insecurity as an acute indicator of consumer financial stress. When people can't afford food, they're at the breaking point. Food insecurity may be a leading indicator that precedes other visible stress signals.

RESEARCH QUESTIONS:

1. CURRENT FOOD INSECURITY RATES
   - What percentage of US households are food insecure?
   - What are trends over past 3 years (post-pandemic)?
   - What is the rate of "very low food security" (severe)?
   - How do rates vary by household composition (children, elderly)?

2. SNAP AND SAFETY NET
   - Current SNAP enrollment vs pre-pandemic?
   - Impact of pandemic SNAP expansion ending?
   - SNAP benefit adequacy vs actual food costs?
   - Application backlogs or processing delays?
   - Work requirement changes and impact?

3. FOOD BANK USAGE
   - Feeding America network demand trends?
   - Are food banks seeing new populations (middle class)?
   - Food bank capacity constraints?
   - Geographic variation in food bank demand?

4. FOOD COSTS
   - Food at home inflation vs overall CPI?
   - Which food categories have highest inflation?
   - Food cost burden as % of income by income level?
   - Are consumers trading down (brand to generic, quantity reduction)?

5. SCHOOL MEALS
   - Free/reduced lunch enrollment trends?
   - Summer meal program participation?
   - Pandemic universal free meals ended—impact?

6. HEALTH CONNECTIONS
   - Food insecurity and health outcome correlations?
   - Diet-related disease trends in food insecure populations?
   - Healthcare cost implications of food insecurity?

7. BEHAVIORAL INDICATORS
   - Meal skipping rates?
   - Food stretching behaviors (watering down, smaller portions)?
   - Adult self-sacrifice for children's food?

OUTPUT FORMAT:
1. Food insecurity landscape summary
2. Key statistics with trends
3. Geographic and demographic hotspots
4. Connection to health outcomes (DOC intersection)
5. Recommended vector design for CARL
6. Leading indicator assessment: Does food insecurity precede other stress?
7. Data sources for monitoring

PRIORITIZE SOURCES:
- USDA Food Security Supplement
- Census Household Pulse Survey
- Feeding America Hunger Statistics
- SNAP administrative data
- Food Research & Action Center
- Urban Institute
```

---

## PROMPT 6: CROSS-AGENT INTERSECTIONS

```
RESEARCH TASK: Cross-Domain Vulnerability Intersections

CONTEXT:
You are researching specific population intersections where multiple stress domains overlap, creating compounded vulnerability. Our monitoring system has identified these intersections but lacks systematic data:

- Gig workers + healthcare needs (GIG + DOC)
- Gig workers + shadow credit (GIG + NICK)
- Small business owners + healthcare (POP + DOC)
- Small business + predatory lending (POP + NICK)
- Medical debt classification (DOC + NICK overlap)

RESEARCH QUESTIONS:

1. GIG WORKERS + HEALTHCARE
   - What percentage of gig workers lack health insurance?
   - What are gig worker healthcare costs vs employed workers?
   - How do gig workers handle medical emergencies financially?
   - What is medical debt prevalence in gig worker population?
   - Are gig workers using ACA marketplace? Impact of subsidy cliff?

2. GIG WORKERS + SHADOW CREDIT
   - We have finding that 58% seek emergency loans quarterly. Can you corroborate?
   - Which shadow credit products do gig workers use most (cash advance apps, BNPL, payday)?
   - What is the debt cycle pattern for gig workers?
   - How does income volatility affect credit access and usage?

3. SMALL BUSINESS OWNERS + HEALTHCARE
   - What percentage of small business owners are self-insured (no employees)?
   - Healthcare costs as percentage of small business revenue?
   - Are SB owners deferring personal healthcare due to business stress?
   - What happens to owner healthcare when business fails?

4. SMALL BUSINESS + PREDATORY LENDING (MCA)
   - What is the merchant cash advance (MCA) market size?
   - What are typical MCA effective interest rates?
   - MCA default rates and enforcement (confession of judgment)?
   - Which businesses are most vulnerable to predatory MCA?
   - Regulatory status of MCA industry?

5. MEDICAL DEBT CLASSIFICATION
   - How much medical debt is in collections ($88B reported)?
   - How much is on payment plans (not yet collections)?
   - How much is held by hospitals vs sold to collectors?
   - CFPB rule vacated—what's current credit reporting status?
   - Is medical debt shadow credit (NICK) or traditional (CARL)?

6. COMPOUNDED VULNERABILITY POPULATIONS
   - Can you identify populations with 3+ overlapping stress factors?
   - What is the prevalence of multi-domain stress?
   - Are there demographic patterns in compounded vulnerability?

OUTPUT FORMAT:
1. Intersection analysis for each of the 5 identified overlaps
2. Population size estimates for each intersection
3. Data quality assessment (what's measurable vs estimated)
4. Recommendations for which intersections to formalize tracking
5. Suggested coordination mechanisms between agents
6. Identification of any additional intersections we're missing

PRIORITIZE SOURCES:
- Freelancers Union surveys
- Kaiser Family Foundation self-employed health data
- Federal Reserve Small Business Credit Survey
- CFPB medical debt reports
- State AG MCA enforcement actions
- Academic research on gig economy
- Aspen Institute Future of Work
```

---

# PRIORITY 3 RESEARCH PROMPTS

---

## PROMPT 7: CHILDCARE BURDEN (If Resources Permit)

```
RESEARCH TASK: Childcare Cost Burden Assessment

CONTEXT:
Childcare costs can exceed housing for families with young children, forcing impossible tradeoffs between work and care. The pandemic childcare support has ended, creating potential "cliffs."

RESEARCH QUESTIONS:
1. Average childcare costs by region and care type
2. Childcare costs as % of income by income bracket
3. Pandemic childcare stabilization fund expiration impacts
4. Childcare workforce shortages and closures
5. Labor force participation impact (especially mothers)
6. Waitlist lengths and availability
7. Employer childcare benefit trends
8. School-age care (before/after school) costs and availability

OUTPUT FORMAT:
1. Childcare cost landscape
2. Workforce participation connection
3. Potential vector design
4. Assessment: Is this significant enough for dedicated tracking or subsume into CARL?

SOURCES: Child Care Aware, BLS, Census SIPP, DOL Women's Bureau
```

---

## PROMPT 8: CRYPTO/SPECULATIVE LOSS ASSESSMENT (If Resources Permit)

```
RESEARCH TASK: Retail Investor Speculative Loss Assessment

CONTEXT:
A cohort of younger investors took substantial losses in crypto (2022), meme stocks, NFTs, and speculative assets. These losses don't appear in consumer debt data but affect financial resilience and psychology.

RESEARCH QUESTIONS:
1. Estimated retail investor crypto losses 2021-2024
2. Meme stock (GME, AMC, etc.) retail investor outcomes
3. NFT market collapse and retail exposure
4. Demographics of affected population (age, income)
5. Behavioral impact (financial nihilism, risk appetite changes)
6. Did losses drive any increase in other debt (covering losses with credit)?
7. Bankruptcy filings citing investment losses

OUTPUT FORMAT:
1. Loss magnitude estimates
2. Affected population profile
3. Behavioral and psychological impacts
4. Connection to existing CARL behavioral vectors (VX-CARL-4.02 gambling, financial nihilism)
5. Assessment: Historical damage or ongoing stress?

SOURCES: Federal Reserve, FINRA, academic research, bankruptcy court data
```

---

# INTEGRATION PLAN

## How to Use Research Results

### Step 1: Conduct Research
- Copy each prompt to external LLM
- Save results to: `C:\Projects\CARL_Methodology\research\[PROMPT_NUMBER]_[TOPIC]_research_[DATE].md`
- Note any data gaps or quality concerns in results

### Step 2: Flag Key Findings
For each research result, identify:
- [ ] Statistics that could become vector thresholds
- [ ] Data sources for ongoing monitoring
- [ ] Populations or geographies of concern
- [ ] Contradictions with current CARL thesis (if any)
- [ ] Connections to existing vectors

### Step 3: CARL Integration Session
Bring research summaries back to CARL for:
- Vector design (if new domain warranted)
- Threshold setting
- FLOW pathway mapping
- Cross-agent coordination protocols
- Update to domain skeleton if needed

### Step 4: Agent Creation (If Warranted)
For ELDER/GRAY agent:
- Create CLAUDE.md
- Create GRAY_DOMAIN_SKELETON.md
- Create GRAY_METHODOLOGY_SKELETON.md (adapt from CARL)
- Initialize workbook
- Create initial handoff

---

## Recommended Research Sequence

**Phase 1 (Immediate):**
1. Prompt 1A: Elder Landscape (highest gap)
2. Prompt 3: Eviction Pipeline (most actionable)
3. Prompt 2: Geographic Concentration (overlay for all)

**Phase 2 (Next):**
4. Prompt 1B: Elder Vector Design (after 1A complete)
5. Prompt 4: Tax Debt
6. Prompt 6: Cross-Agent Intersections

**Phase 3 (If Resources Permit):**
7. Prompt 5: Food Insecurity
8. Prompt 7: Childcare (optional)
9. Prompt 8: Crypto Losses (optional)

---

## Research Tracking

| Prompt | Topic | Status | Assigned To | Completed | Integrated |
|--------|-------|--------|-------------|-----------|------------|
| 1A | Elder Landscape | PENDING | | | |
| 1B | Elder Vectors | PENDING | | | |
| 2 | Geographic | PENDING | | | |
| 3 | Eviction | PENDING | | | |
| 4 | Tax Debt | PENDING | | | |
| 5 | Food Insecurity | PENDING | | | |
| 6 | Cross-Agent | PENDING | | | |
| 7 | Childcare | OPTIONAL | | | |
| 8 | Crypto Losses | OPTIONAL | | | |

---

*Research Agenda Created: CARL 005 | 2026-01-20*
