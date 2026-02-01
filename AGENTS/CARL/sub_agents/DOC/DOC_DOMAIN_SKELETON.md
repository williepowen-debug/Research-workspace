# DOC DOMAIN SKELETON

# Purpose: Structural scaffold for DOC agent operations
# Domain:  Healthcare Cost Stress, Medical Expenses, Provider Economics, Access Barriers
# Agent:   DOC (Healthcare Cost Monitor)
#
# Version: 1.0
# Created: 2026-01-20
# Author:  Initial Architecture Session
#
# Usage:
#   - Load this file at the start of any DOC session
#   - Provides vocabulary, entities, vectors, and thresholds for healthcare cost monitoring
#   - Companion to DOC_METHODOLOGY_SKELETON which governs process
#   - This skeleton governs the CONTENT of DOC's domain
#
# Reporting: DOC reports to CARL via State Vectors
# Signal:    Healthcare costs as non-discretionary financial burden
#            "The bill you can't refuse"

---

## METADATA

metadata:
  name: "DOC Domain Skeleton"
  domain: "Healthcare Cost Stress, Medical Expenses, Medical Debt, Provider Economics"
  version: "1.0"
  created: "2026-01-20"
  parent_agent: "CARL"
  
  phase_model: |
    Phase 1 (Manageable) → Phase 2 (Straining) → Phase 3 (Deferring) → Phase 4 (Drowning)
    
    Manageable: Healthcare costs absorbable within budget; care accessed when needed
    Straining: Costs consuming increasing share of income; beginning to affect other spending
    Deferring: Consumers delaying/avoiding care due to cost; medical debt accumulating
    Drowning: Medical debt in collections; bankruptcy risk; care access severely limited
    
  core_thesis:
    name: "Healthcare Cost Stress Thesis"
    statement: |
      Healthcare costs represent a uniquely destructive form of consumer financial stress:
      
      1. NON-DISCRETIONARY: Unlike most expenses, healthcare cannot be refused or 
         indefinitely deferred. Acute needs must be addressed regardless of ability to pay.
         
      2. UNPREDICTABLE: Costs are largely unforeseeable. A single event can generate
         five or six figure bills with no warning.
         
      3. OPAQUE PRICING: Consumers rarely know costs before receiving care. Price
         discovery is nearly impossible. Surprise billing remains common.
         
      4. ASYMMETRIC POWER: Providers and insurers have leverage; consumers do not.
         Negotiation is difficult; debt collection aggressive.
         
      Healthcare costs are rising faster than wages across all dimensions:
      - Insurance premiums (tracked by POLLY)
      - Deductibles and out-of-pocket maximums
      - Drug prices
      - Facility and provider charges
      
      The result: Medical debt is the LEADING cause of bankruptcy filings and a major
      source of credit stress. Even insured consumers face catastrophic exposure through
      high deductibles, coverage gaps, and surprise bills.
      
      Healthcare cost stress transmits to CARL through:
      - Direct spending reduction (healthcare crowds out other consumption)
      - Medical debt accumulation (credit deterioration)
      - Deferred care consequences (acute events from delayed treatment)
      
    confidence: "70% — thesis well-supported by data; structural drivers clear"
    
    invalidation_criteria:
      - "Healthcare cost growth decelerates below wage growth for 2+ years"
      - "Medical debt in collections declines significantly"
      - "Out-of-pocket burden decreases as share of income"
      - "Care deferral rates decline across income segments"
    
    competing_hypotheses:
      - name: "Coverage Expansion Effect"
        statement: "ACA and coverage expansion have reduced catastrophic exposure"
        current_assessment: "Partially true; coverage improved but deductibles offset gains"
      - name: "Price Transparency Effect"
        statement: "New transparency rules will enable price shopping and reduce costs"
        current_assessment: "Too early to assess; implementation limited"

---

## ENTITY DEFINITIONS

### Healthcare Cost Categories

cost_categories:

  insurance_premiums:
    description: "Monthly/annual cost for health insurance coverage"
    significance: "Tracked primarily by POLLY; DOC monitors premium-to-income burden"
    cross_reference: "POLLY VX-POLLY-3.01"
    
  deductibles_and_oop:
    description: "Out-of-pocket costs before insurance coverage kicks in"
    significance: |
      Rising deductibles mean insured consumers still face significant exposure.
      Average single deductible ~$1,700; family higher. Must be paid before
      insurance provides meaningful coverage. Creates "functionally uninsured."
    metrics:
      - "Average deductible (single/family)"
      - "Average out-of-pocket maximum"
      - "Percent of plans with high deductibles (HDHP)"
      
  facility_charges:
    description: "Hospital and facility fees"
    significance: |
      Hospital charges have increased dramatically. Average hospital stay costs
      often exceed $10,000. Emergency room visits average $1,000-2,000+.
      Chargemaster rates bear little relation to actual costs.
    metrics:
      - "Average hospital stay cost"
      - "Average ER visit cost"
      - "Hospital charge inflation"
      
  provider_fees:
    description: "Physician and specialist charges"
    significance: |
      Provider fees vary dramatically by specialty and geography.
      Out-of-network charges can be 2-10x in-network rates.
    metrics:
      - "Average specialist visit cost"
      - "Out-of-network rate differentials"
      
  prescription_drugs:
    description: "Medication costs — retail and specialty"
    significance: |
      Drug costs are major burden, especially for chronic conditions.
      Specialty drugs can cost thousands per month. Generic availability
      helps but brand pricing continues rising.
    metrics:
      - "Average prescription cost"
      - "Brand vs. generic pricing trends"
      - "Specialty drug costs"
      - "Insulin and essential drug pricing"
      
  surprise_billing:
    description: "Unexpected charges from out-of-network providers in in-network facilities"
    significance: |
      Despite No Surprises Act (2022), consumers still face unexpected bills
      from anesthesiologists, radiologists, and other facility-based providers.
      Ground ambulance not covered by federal rules.
    recent_developments:
      - "No Surprises Act effective 2022"
      - "Ground ambulance still exposed"
      - "Implementation and enforcement ongoing"

### Medical Debt

medical_debt:

  description: "Healthcare costs that consumers cannot pay, becoming debt obligations"
  
  scale:
    - "~$220 billion in medical debt outstanding (2022 estimate)"
    - "~100 million Americans have medical debt"
    - "Medical debt is leading cause of bankruptcy"
    
  characteristics:
    - "Often unexpected and unplanned"
    - "Typically not chosen by consumer (unlike other debt)"
    - "Can result from single acute event"
    - "Interest rates and collection practices aggressive"
    - "Recent changes to credit bureau reporting (paid medical debt removed)"
    
  transmission_to_carl:
    description: |
      Medical debt transmits to consumer credit through:
      1. Direct credit utilization (credit cards used to pay bills)
      2. Medical debt in collections (historically on credit reports)
      3. Bankruptcy filings
      4. Reduced ability to service other debt
      
  cross_reference:
    - "POLLY VX-POLLY-3.04 (Medical Debt Prevalence)"
    - "NICK (medical debt as shadow obligation if not yet in collections)"

### Care Access and Deferral

care_deferral:

  description: "Consumers delaying or avoiding healthcare due to cost"
  
  significance: |
    Care deferral is both indicator and accelerant of stress:
    - Indicator: People defer care when they can't afford it
    - Accelerant: Deferred preventive care leads to acute (costly) events
    
  metrics:
    - "Percent delaying care due to cost"
    - "Percent unable to afford prescription"
    - "Percent skipping doses to stretch medication"
    - "Percent with unmet medical need"
    
  socioeconomic_gradient:
    note: "Care deferral rates are dramatically higher for lower-income households"
    
### Healthcare Providers

providers:

  hospitals:
    description: "Acute care facilities"
    financial_dynamics: |
      Hospital finances affect consumer costs through:
      - Pricing power (consolidated markets charge more)
      - Uncompensated care burden (shifts to paying patients)
      - Facility fees added to services
      
    major_systems:
      - name: "HCA Healthcare"
        ticker: "HCA"
        note: "Largest for-profit hospital operator"
      - name: "CommonSpirit"
        status: "Non-profit"
        note: "Largest non-profit system"
      - name: "Kaiser Permanente"
        status: "Integrated"
        note: "Combined insurer-provider"
      - name: "Ascension"
        status: "Non-profit"
      - name: "Trinity Health"
        status: "Non-profit"
        
    stress_signals:
      - "Hospital closures (especially rural)"
      - "Financial distress/downgrades"
      - "Labor cost pressure"
      - "Uncompensated care increases"
      
  rural_hospitals:
    description: "Critical access and rural facilities"
    significance: |
      Rural hospitals face unique pressures: lower volume, worse payer mix,
      difficulty recruiting staff. Closures leave communities without access.
      ~150 rural hospital closures since 2010.
    stress_signals:
      - "Closure announcements"
      - "Financial distress"
      - "Service line reductions"
      
  physicians:
    description: "Physician practices and provider groups"
    trends:
      - "Increasing consolidation (PE ownership, health system acquisition)"
      - "Independent practice decline"
      - "Specialty vs. primary care economics"

### Payers and Intermediaries

payers:

  health_insurers:
    note: "Tracked primarily by POLLY; DOC monitors cost transmission"
    cross_reference: "POLLY health insurance entities"
    
  pharmacy_benefit_managers:
    description: "PBMs that manage drug benefits for insurers"
    entities:
      - name: "CVS Caremark"
        parent: "CVS Health"
        ticker: "CVS"
      - name: "Express Scripts"
        parent: "Cigna"
        ticker: "CI"
      - name: "OptumRx"
        parent: "UnitedHealth"
        ticker: "UNH"
    significance: |
      PBMs influence drug pricing through formularies, rebates, and 
      spread pricing. Increasingly scrutinized for role in high drug costs.
    stress_signals:
      - "Formulary restrictions affecting patients"
      - "Rebate transparency issues"
      - "Regulatory action"

---

## VECTOR REGISTRY (VX)

### Healthcare Cost Growth Vectors (1.xx)

vectors:

  VX-DOC-1.01:
    name: "Healthcare Cost Inflation"
    domain: "Cost Growth"
    description: "Year-over-year change in medical care CPI component"
    unit: "% YoY"
    current_value: "TBD"
    threshold_elevated: ">4% YoY"
    threshold_critical: ">6% YoY"
    tripwire_breached: ">8% YoY"
    trend: "TBD"
    data_sources: ["BLS CPI Medical Care"]
    note: "Compare to general CPI and wage growth"

  VX-DOC-1.02:
    name: "Hospital Price Growth"
    domain: "Cost Growth"
    description: "Year-over-year change in hospital services pricing"
    unit: "% YoY"
    current_value: "TBD"
    threshold_elevated: ">5% YoY"
    threshold_critical: ">8% YoY"
    tripwire_breached: ">12% YoY"
    trend: "TBD"
    data_sources: ["BLS Hospital CPI", "HCCI"]
    note: "Largest cost driver in healthcare"

  VX-DOC-1.03:
    name: "Prescription Drug Cost Growth"
    domain: "Cost Growth"
    description: "Year-over-year change in prescription drug costs"
    unit: "% YoY"
    current_value: "TBD"
    context: "IRA allows Medicare negotiation for some drugs starting 2026"
    threshold_elevated: ">5% YoY"
    threshold_critical: ">8% YoY"
    tripwire_breached: ">12% YoY"
    trend: "TBD"
    data_sources: ["CMS", "IQVIA", "KFF"]
    note: "Watch IRA drug pricing impact"

### Out-of-Pocket Burden Vectors (2.xx)

  VX-DOC-2.01:
    name: "OOP as Share of Income"
    domain: "OOP"
    description: "Household out-of-pocket healthcare spending as percentage of income"
    unit: "%"
    current_value: "TBD"
    threshold_elevated: ">5%"
    threshold_critical: ">7%"
    tripwire_breached: ">10%"
    trend: "TBD"
    data_sources: ["MEPS", "Census", "BLS CEX"]
    note: "Key affordability measure"

  VX-DOC-2.02:
    name: "Average Deductible Burden"
    domain: "OOP"
    description: "Average annual deductible relative to median income"
    unit: "$ or %"
    current_value: "TBD"
    context: "Was ~$1,735 in 2023 per KFF"
    threshold_elevated: ">$2,000 single"
    threshold_critical: "Exceeds liquid savings"
    tripwire_breached: ">5% of income"
    trend: "TBD"
    data_sources: ["KFF Survey"]
    cross_reference: "POLLY VX-POLLY-3.02"
    note: "High deductibles = barrier to care"

  VX-DOC-2.03:
    name: "Catastrophic Cost Exposure"
    domain: "OOP"
    description: "Share of population with catastrophic medical cost vulnerability"
    unit: "%"
    current_value: "TBD"
    interpretation: |
      Includes underinsured (insured but with high deductibles/OOP relative to income)
      and uninsured populations. Catastrophic = unable to absorb major medical event.
    threshold_elevated: ">30%"
    threshold_critical: ">40%"
    tripwire_breached: ">50%"
    trend: "TBD"
    data_sources: ["Commonwealth Fund", "KFF", "Census"]
    note: "Includes underinsured"

### Medical Debt Vectors (3.xx)

  VX-DOC-3.01:
    name: "Medical Debt Prevalence"
    domain: "DEBT"
    description: "Share of adults with any medical debt"
    unit: "%"
    current_value: "TBD"
    context: "Various surveys show 20-40% depending on definition"
    threshold_elevated: ">25%"
    threshold_critical: ">30%"
    tripwire_breached: ">35%"
    trend: "TBD"
    data_sources: ["KFF", "Fed SCF", "Census"]
    cross_reference: "POLLY VX-POLLY-3.04"
    note: "~25-30% typical"

  VX-DOC-3.02:
    name: "Medical Debt in Collections"
    domain: "DEBT"
    description: "Share of adults with medical debt in third-party collections"
    unit: "%"
    current_value: "TBD"
    context: "Credit bureaus changed reporting 2022 — may affect visibility"
    interpretation: |
      Medical debt in collections represents most severe cases.
      Recent policy changes: paid medical debt removed from reports,
      unpaid debt <$500 not reported, 1-year waiting period.
    threshold_elevated: ">10%"
    threshold_critical: ">13%"
    tripwire_breached: ">16%"
    trend: "TBD"
    data_sources: ["CFPB", "credit bureaus"]
    cross_reference: "NICK (shadow debt)"
    note: "Credit bureau changes may affect visibility"

  VX-DOC-3.03:
    name: "Average Medical Debt Balance"
    domain: "DEBT"
    description: "Average medical debt balance among those with debt"
    unit: "$"
    current_value: "TBD"
    threshold_elevated: ">$2,500"
    threshold_critical: ">$4,000"
    tripwire_breached: ">$6,000"
    trend: "TBD"
    data_sources: ["CFPB", "credit bureau studies"]

### Care Deferral/Behavior Vectors (4.xx)

  VX-DOC-4.01:
    name: "Care Deferral Rate"
    domain: "BEHAVIOR"
    description: "Share of adults who delayed or skipped care due to cost"
    unit: "%"
    current_value: "TBD"
    context: "Typically 25-40% report delaying care due to cost"
    threshold_elevated: ">30%"
    threshold_critical: ">40%"
    tripwire_breached: ">50%"
    trend: "TBD"
    data_sources: ["Gallup", "KFF", "Commonwealth"]
    note: "25-40% typical"

  VX-DOC-4.02:
    name: "Medication Non-Adherence Rate"
    domain: "BEHAVIOR"
    description: "Share not taking medications as prescribed due to cost"
    unit: "%"
    current_value: "TBD"
    interpretation: |
      Prescription non-adherence leads to worse health outcomes and
      often more costly acute care later. Particularly concerning for
      chronic conditions (diabetes, hypertension, mental health).
    threshold_elevated: ">20%"
    threshold_critical: ">25%"
    tripwire_breached: ">30%"
    trend: "TBD"
    data_sources: ["KFF", "Commonwealth", "CDC"]
    note: "High risk: insulin, CV, mental health"

  VX-DOC-4.03:
    name: "Unmet Healthcare Need"
    domain: "BEHAVIOR"
    description: "Share with unmet healthcare need due to cost"
    unit: "%"
    current_value: "TBD"
    threshold_elevated: ">15%"
    threshold_critical: ">20%"
    tripwire_breached: ">25%"
    trend: "TBD"
    data_sources: ["NHIS", "MEPS", "Commonwealth"]
    note: "Dental often highest"

---

## FLOW CASCADES

### FLOW-DOC-01: Cost Growth Cascade

flow_cascades:

  FLOW-DOC-01:
    name: "Cost Growth Cascade"
    pathway: |
      Healthcare costs rise > wages →
      Premiums increase →
      Employers shift costs to employees →
      Higher OOP exposure →
      More spending to healthcare →
      Less discretionary spending

    mechanism: |
      Healthcare cost growth has structural drivers (aging, technology, consolidation)
      that aren't easily contained. Costs flow through to consumers regardless of insurance.
      Higher costs → more uninsured → more uncompensated care → higher costs.

    feedback_loops: "Higher costs → more uninsured → more uncompensated care → higher costs"
    breakpoint: "Healthcare spending crowds out other essential spending"
    lag_time: "6-18 months"
    confidence: "HIGH 80%"
    trigger: "Wage-adjusted healthcare cost growth"
    status: "MONITORING"
    cross_domain: ["POLLY (premiums)", "CARL (consumer spending)"]

### FLOW-DOC-02: Care Deferral Cascade

  FLOW-DOC-02:
    name: "Care Deferral Cascade"
    pathway: |
      Consumer can't afford healthcare costs →
      Defers or avoids needed care →
      Condition worsens over time →
      Eventually requires acute/emergency care →
      Acute care far more expensive than preventive →
      Large unexpected bill →
      Medical debt accumulation →
      Financial stress
      
    mechanism: |
      Deferral appears to save money short-term but often results in worse
      health outcomes and higher eventual costs. The diabetic who skips
      insulin ends up in ER with ketoacidosis; the person avoiding
      colonoscopy presents with advanced cancer.
      
    breakpoint: "Deferred condition becomes acute"
    lag_time: "Months to years (condition-dependent)"
    status: "MONITORING"
    cross_domain: ["CARL (unexpected expense shock)"]

### FLOW-DOC-03: Medical Debt Spiral

  FLOW-DOC-03:
    name: "Medical Debt Spiral"
    pathway: |
      Major medical event →
      Costs exceed ability to pay →
      Medical debt accrues →
      Payment plan OR collections →
      Credit damage →
      Reduced access to credit →
      Financial fragility →
      Potential bankruptcy

    mechanism: |
      Medical debt is uniquely damaging: unchosen, unforeseeable, potentially massive.
      A single diagnosis can generate debt taking years to resolve.

    feedback_loops: "Debt stress → reduced care adherence → worse health → more debt"
    breakpoint: "Medical costs exceed ability to pay"
    lag_time: "Immediate to 180 days"
    confidence: "HIGH 80%"
    trigger: "Medical event for underinsured"
    status: "MONITORING"
    cross_domain: ["NICK (debt)", "CARL (credit)"]

### FLOW-DOC-04: Medication Non-Adherence Cascade

  FLOW-DOC-04:
    name: "Medication Non-Adherence Cascade"
    pathway: |
      Rx prescribed →
      OOP cost exceeds comfort →
      Patient skips/splits doses →
      Condition poorly controlled →
      Preventable crisis →
      Hospitalization/ER →
      Higher costs + worse outcomes

    mechanism: |
      Non-adherence is dangerous cost-saving. Insulin rationing has caused deaths.
      Cardiovascular non-adherence causes preventable heart attacks.

    feedback_loops: "Non-adherence → crisis → fear → over-adherence → cost → non-adherence"
    breakpoint: "Condition decompensates due to non-adherence"
    lag_time: "Weeks to months"
    confidence: "HIGH 75%"
    trigger: "Non-adherence rate increase"
    status: "MONITORING"
    cross_domain: ["Mortality", "ER utilization"]
    note: "Insulin, CV, mental health highest risk"

### FLOW-DOC-05: Doc-to-CARL Transmission

  FLOW-DOC-05:
    name: "Doc-to-CARL Transmission"
    pathway: |
      Healthcare cost stress signals emerge (DOC vectors trigger) →
      Consumers face direct financial burden →
      Channel 1: Spending reduction (crowd-out effect) →
      Channel 2: Medical debt accumulation →
      Channel 3: Care deferral → eventual acute event →
      All channels lead to: credit utilization, debt accumulation,
      reduced financial resilience →
      CARL vectors show deterioration
      
    mechanism: |
      DOC transmits to CARL through multiple channels. The crowd-out effect
      is immediate (less discretionary spending). Medical debt accumulation
      is medium-term. Deferred care consequences may be long-term but severe.
      
    breakpoint: "Healthcare costs cause measurable credit/financial impact"
    lag_time: "Immediate (crowd-out) to months (debt) to years (deferred care)"
    status: "MONITORING"
    cross_domain: ["CARL (all vectors)"]

---

## DATA SOURCES

### Primary Sources

data_sources:

  kff:
    description: "Kaiser Family Foundation — gold standard for health cost data"
    url: "kff.org"
    key_reports:
      - "Employer Health Benefits Survey (annual)"
      - "Health care costs surveys"
      - "Medical debt tracking"
    frequency: "Annual survey + ongoing tracking"
    reliability: "HIGH"
    
  cms_nhe:
    description: "CMS National Health Expenditure data"
    url: "cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/NationalHealthExpendData"
    content: "Official healthcare spending data"
    frequency: "Annual"
    reliability: "HIGH — official government data"
    
  bls_cpi:
    description: "Bureau of Labor Statistics CPI components"
    url: "bls.gov"
    content: "Medical care CPI, hospital CPI, prescription drug CPI"
    frequency: "Monthly"
    reliability: "HIGH"
    
  cfpb_medical_debt:
    description: "CFPB medical debt research and reports"
    content: "Medical debt in collections, consumer impacts"
    frequency: "Periodic"
    reliability: "HIGH — regulatory"
    
  commonwealth_fund:
    description: "Commonwealth Fund health system research"
    url: "commonwealthfund.org"
    content: "Healthcare access, affordability, international comparisons"
    frequency: "Periodic surveys and reports"
    reliability: "HIGH"
    
  gallup:
    description: "Gallup health and wellbeing tracking"
    content: "Care deferral, cost concerns"
    frequency: "Ongoing"
    reliability: "MEDIUM-HIGH"
    
  hospital_financial_data:
    description: "Hospital financial tracking"
    sources:
      - "KaufmanHall National Hospital Flash Report"
      - "AHA data"
      - "Moody's/Fitch healthcare ratings"
    frequency: "Monthly/Quarterly"
    reliability: "HIGH"
    
  rural_hospital_tracking:
    description: "Chartis Center for Rural Health"
    url: "chartis.com/insights/rural-health"
    content: "Rural hospital closures, at-risk facilities"
    frequency: "Ongoing"
    reliability: "HIGH — authoritative source"

### Data Gaps

data_gaps:
  
  - description: "Real-time medical debt accumulation (lagged reporting)"
    workaround: "Use survey data, credit bureau studies"
    severity: "MEDIUM"
    
  - description: "True out-of-pocket burden by income (survey limitations)"
    workaround: "Use KFF/Commonwealth income-stratified data"
    severity: "MEDIUM"
    
  - description: "Care deferral consequences (long lag to outcomes)"
    workaround: "Use condition-specific studies, academic research"
    severity: "HIGH — key transmission mechanism is hard to see"
    
  - description: "Surprise billing prevalence post-No Surprises Act"
    workaround: "Track complaints, CMS data, news coverage"
    severity: "MEDIUM"

---

## GLOSSARY

glossary:

  terms:
    
    deductible:
      definition: "Amount consumer must pay before insurance coverage begins"
      significance: "Rising deductibles = rising consumer exposure"
      
    out_of_pocket_maximum:
      definition: "Maximum consumer pays in a plan year before insurer covers 100%"
      significance: "ACA sets limits, but maximums are high ($9,450 individual 2024)"
      
    hdhp:
      definition: "High-Deductible Health Plan — deductible ≥$1,600 single / $3,200 family"
      significance: "HDHPs shift first-dollar costs to consumers"
      
    medical_debt:
      definition: "Healthcare costs consumer owes but cannot immediately pay"
      significance: "Leading cause of bankruptcy; unique in being unplanned/unchosen"
      
    care_deferral:
      definition: "Delaying or avoiding needed healthcare due to cost"
      significance: "Both indicator of stress AND cause of worse outcomes"
      
    chargemaster:
      definition: "Hospital's list of prices for all services"
      significance: "Notoriously inflated; rarely reflects actual payment"
      
    balance_billing:
      definition: "Provider billing patient for difference between charge and insurance payment"
      note: "Federal No Surprises Act limits for emergency, but gaps remain"
      
    pbm:
      definition: "Pharmacy Benefit Manager — manages drug benefits for insurers"
      significance: "Influence drug pricing through formularies and rebates"
      
    uncompensated_care:
      definition: "Healthcare provided without payment (charity + bad debt)"
      significance: "Costs shifted to other payers/patients"
      
    functionally_uninsured:
      definition: "Consumer with insurance but unable to afford deductible/OOP costs"
      significance: "Insurance card doesn't mean access if costs are too high"

  acronyms:
    OOP: "Out-of-Pocket"
    HDHP: "High-Deductible Health Plan"
    HSA: "Health Savings Account"
    PBM: "Pharmacy Benefit Manager"
    ACA: "Affordable Care Act"
    IRA: "Inflation Reduction Act (drug pricing provisions)"
    CMS: "Centers for Medicare & Medicaid Services"
    NHE: "National Health Expenditure"
    KFF: "Kaiser Family Foundation"
    CFPB: "Consumer Financial Protection Bureau"
    ABI: "American Bankruptcy Institute"

---

## REPORTING RELATIONSHIP

### DOC → CARL State Vector

reporting:
  
  parent_agent: "CARL"
  reporting_frequency: "As significant developments occur; minimum monthly"
  
  state_vector_focus:
    primary_signal: "Healthcare costs as non-discretionary financial burden"
    secondary_signals:
      - "Medical debt accumulation and transmission"
      - "Care deferral indicating stress and creating future risk"
      - "Provider stress affecting access and costs"
    
  key_questions_from_carl:
    - "How much are healthcare costs squeezing consumer budgets?"
    - "What is the medical debt transmission to credit metrics?"
    - "Are care deferral rates indicating rising consumer stress?"
    
  escalation_criteria:
    - "Any vector moves to BREACHED status"
    - "Medical debt prevalence increases significantly"
    - "Care deferral rate spikes"
    - "Major hospital system distress or closures"
    
  coordination_with_polly:
    note: "Health insurance (premiums, coverage) tracked by POLLY; DOC tracks costs/debt"
    overlap: "Medical debt prevalence appears in both domains"
    protocol: "Share relevant observations; avoid duplication"
    
  coordination_with_nick:
    note: "Medical debt can be 'shadow' obligation before collections"
    protocol: "Coordinate on medical debt as hidden leverage"

---

## SESSION QUICK REFERENCE

### For Update Sessions
Focus on: VX-DOC-1.xx (Out-of-Pocket), VX-DOC-2.xx (Medical Debt)
Key question: "Are OOP costs rising? Is medical debt accumulating?"

### For Analysis Sessions
Focus on: FLOW cascades, transmission mechanisms
Key question: "How are healthcare costs transmitting to financial stress?"

### For Reconciliation Sessions
Focus on: Cross-reference integrity, POLLY coordination
Key question: "Is our data current? Are we coordinating with POLLY on overlap?"

### For State Vector Reports
Include: Highest-concern vectors, transmission mechanism assessment
Format: Per DOC_METHODOLOGY_SKELETON §6.2

---

# END OF SKELETON

# Maintenance Notes:
# - Update vector current_values as data arrives
# - Annual update after KFF Employer Survey (September)
# - Monitor CMS NHE release (typically December for prior year)
# - Track CFPB medical debt reports
# - Coordinate with POLLY on health insurance/coverage metrics
# - Version increment for structural changes
