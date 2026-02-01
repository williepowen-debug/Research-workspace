# POLLY DOMAIN SKELETON

# Purpose: Structural scaffold for POLLY agent operations
# Domain:  Insurance Stress, P&C Markets, Health Coverage, Consumer Protection Gaps
# Agent:   POLLY (Insurance Stress Monitor)
#
# Version: 1.0
# Created: 2026-01-20
# Author:  Initial Architecture Session
#
# Usage:
#   - Load this file at the start of any POLLY session
#   - Provides vocabulary, entities, vectors, and thresholds for insurance monitoring
#   - Companion to POLLY_METHODOLOGY_SKELETON which governs process
#   - This skeleton governs the CONTENT of POLLY's domain
#
# Reporting: POLLY reports to CARL via State Vectors
# Signal:    Consumer financial vulnerability through insurance stress
#            "The safety net fraying"

---

## METADATA

metadata:
  name: "POLLY Domain Skeleton"
  domain: "Insurance Stress, P&C Markets, Health Coverage, Consumer Protection Gaps"
  version: "1.0"
  created: "2026-01-20"
  parent_agent: "CARL"
  
  phase_model: |
    Phase 1 (Stable Coverage) → Phase 2 (Premium Pressure) → Phase 3 (Coverage Erosion) → Phase 4 (Protection Collapse)
    
    Stable Coverage: Consumers adequately insured, premiums manageable
    Premium Pressure: Rate increases outpace income, affordability strain emerges
    Coverage Erosion: Consumers reduce coverage, increase deductibles, drop policies
    Protection Collapse: Widespread underinsurance, coverage gaps, one incident from ruin
    
  core_thesis:
    name: "Insurance Stress Thesis"
    statement: |
      Insurance is both INDICATOR and AMPLIFIER of consumer financial stress:
      
      AS INDICATOR: When consumers can't afford insurance premiums, reduce coverage,
      or let policies lapse, it signals financial strain that may not yet appear in
      credit metrics. Insurance is often the first "discretionary" expense cut.
      
      AS AMPLIFIER: Underinsured consumers are one incident away from financial
      catastrophe. A car accident without adequate coverage, a home repair without
      homeowners insurance, a medical event without health coverage—these become
      transmission mechanisms that convert manageable stress into crisis.
      
      The insurance market is experiencing unprecedented pressure: climate-driven
      P&C losses, medical cost inflation, and carrier exits from high-risk markets.
      This pressure transmits directly to consumer financial vulnerability.
      
    confidence: "65% — thesis logically sound, multiple confirming signals"
    
    invalidation_criteria:
      - "Premium increases moderate to below income growth for 2+ quarters"
      - "Policy lapse rates decline while coverage levels increase"
      - "Carrier exits reverse; capacity returns to stressed markets"
      - "Health coverage rates improve across income segments"
    
    competing_hypotheses:
      - name: "Market Rationalization"
        statement: "Insurance repricing reflects accurate risk; consumers will adapt"
        current_assessment: "Partially valid but ignores affordability constraint"
      - name: "Government Backstop"
        statement: "State/federal programs will prevent coverage collapse"
        current_assessment: "Limited evidence of adequate backstop capacity"

---

## ENTITY DEFINITIONS

### Property & Casualty Insurance

pc_insurance:
  
  major_carriers:
    - name: "State Farm"
      status: "Mutual (private)"
      market_position: "Largest US P&C insurer"
      data_sources: ["AM Best", "state filings", "news coverage"]
      watch_signals: ["Market exits", "rate filings", "non-renewal rates"]
      
    - name: "Allstate"
      ticker: "ALL"
      data_sources: ["SEC filings", "earnings calls", "state filings"]
      watch_signals: ["Combined ratio", "catastrophe losses", "policy count"]
      
    - name: "Progressive"
      ticker: "PGR"
      data_sources: ["SEC filings", "earnings calls"]
      watch_signals: ["Auto loss ratios", "rate adequacy", "growth metrics"]
      
    - name: "GEICO (Berkshire)"
      ticker: "BRK.A/BRK.B"
      data_sources: ["Berkshire filings", "AM Best"]
      watch_signals: ["Combined ratio", "premium growth"]
      
    - name: "Liberty Mutual"
      status: "Mutual (private)"
      data_sources: ["AM Best", "state filings"]
      
    - name: "Farmers"
      parent: "Zurich"
      data_sources: ["Parent filings", "state data"]
      
    - name: "USAA"
      status: "Reciprocal (private)"
      data_sources: ["AM Best", "limited"]
      note: "Military families; bellwether for middle-class stress"
      
  florida_specialists:
    note: "Florida P&C market is canary in coal mine for climate stress"
    entities:
      - name: "Citizens Property Insurance"
        type: "State-run insurer of last resort"
        significance: "Growth indicates private market failure"
        data_sources: ["Citizens public reports", "FL OIR"]
      - name: "Heritage Insurance"
        ticker: "HRTG"
        status: "Watch for distress"
      - name: "Universal Insurance"
        ticker: "UVE"
        status: "Florida-focused"
    recent_failures:
      - "Multiple FL carriers failed 2022-2024"
      - "Indicates market stress, not just company issues"

  california_market:
    note: "CA experiencing carrier exits due to wildfire exposure"
    key_developments:
      - "State Farm announced non-renewal of 72,000 policies (2023)"
      - "Allstate paused new homeowners policies"
      - "FAIR Plan (last resort) enrollment surging"
    data_sources: ["CA DOI", "news coverage", "carrier announcements"]

### Auto Insurance

auto_insurance:
  
  market_dynamics:
    description: |
      Auto insurance experiencing unprecedented rate increases due to:
      - Repair cost inflation (parts, labor)
      - Vehicle replacement cost increases
      - Medical cost inflation
      - Increased accident frequency post-pandemic
      - Distracted driving
      
  key_metrics:
    - "Average premium trends"
    - "Combined ratios by carrier"
    - "Non-standard market share (high-risk drivers)"
    - "Uninsured motorist rates by state"
    
  non_standard_market:
    description: "Insurers specializing in high-risk/low-income drivers"
    significance: "Growth indicates standard market rejections increasing"
    entities:
      - name: "The General"
        parent: "American Family"
      - name: "SafeAuto"
      - name: "Dairyland"
        parent: "Sentry"
    data_sources: ["Industry reports", "state data"]

### Health Insurance

health_insurance:
  
  market_segments:
    
    employer_sponsored:
      description: "Coverage through employment"
      metrics:
        - "Employer offer rates"
        - "Employee take-up rates"
        - "Premium contribution shares"
        - "Deductible trends"
      data_sources: ["KFF Employer Survey", "BLS", "Census"]
      stress_signals:
        - "Declining offer rates at small employers"
        - "Rising employee premium shares"
        - "Deductible increases outpacing wages"
        
    aca_marketplace:
      description: "Affordable Care Act exchange coverage"
      metrics:
        - "Enrollment trends"
        - "Premium changes"
        - "Subsidy levels"
        - "Insurer participation"
      data_sources: ["CMS", "KFF", "state exchanges"]
      note: "Enhanced subsidies (ARP) set to expire — watch for cliff"
      
    medicaid:
      description: "Government coverage for low-income"
      metrics:
        - "Enrollment post-unwinding"
        - "Disenrollment rates"
        - "Coverage gap (too rich for Medicaid, too poor for ACA)"
      data_sources: ["CMS", "KFF", "state reports"]
      key_event: "Medicaid unwinding (2023-2024) — millions lost coverage"
      
    uninsured:
      description: "No health coverage"
      metrics:
        - "Uninsured rate by income"
        - "Uninsured rate by state"
        - "Uncompensated care costs"
      data_sources: ["Census", "KFF", "hospital data"]
      significance: "Uninsured = one medical event from financial ruin"

  major_carriers:
    - name: "UnitedHealth"
      ticker: "UNH"
      data_sources: ["SEC filings", "earnings calls"]
      
    - name: "Elevance (Anthem)"
      ticker: "ELV"
      data_sources: ["SEC filings", "earnings calls"]
      
    - name: "CVS/Aetna"
      ticker: "CVS"
      data_sources: ["SEC filings", "earnings calls"]
      
    - name: "Cigna"
      ticker: "CI"
      data_sources: ["SEC filings", "earnings calls"]
      
    - name: "Humana"
      ticker: "HUM"
      data_sources: ["SEC filings", "earnings calls"]
      note: "Medicare Advantage focused"

### Regulatory Bodies

regulators:
  
  federal:
    - name: "CMS (Centers for Medicare & Medicaid)"
      role: "Health insurance oversight, ACA, Medicare, Medicaid"
      data: "Enrollment data, market reports"
      
    - name: "FEMA / NFIP"
      role: "National Flood Insurance Program"
      significance: "Federal flood insurance backstop"
      stress_signals: ["Rate increases", "participation drops", "claim backlogs"]
      
  state:
    - name: "State Insurance Commissioners"
      role: "P&C and health rate approval, market conduct"
      key_states: ["CA", "FL", "TX", "NY", "LA"]
      data: "Rate filings, market reports, enforcement actions"
      
    - name: "NAIC"
      full_name: "National Association of Insurance Commissioners"
      role: "Industry data aggregation, model regulations"
      data: "Market share reports, financial data"

---

## VECTOR REGISTRY (VX)

### Homeowners Insurance Vectors

vectors:

  VX-POLLY-1.01:
    name: "Homeowners Premium Increase Rate"
    domain: "Homeowners"
    description: "Year-over-year average homeowners premium increase nationally"
    unit: "% YoY"
    current_value: "TBD"
    context: "Income growth ~4% for comparison"
    threshold_elevated: ">8% YoY (2x income growth)"
    threshold_critical: ">12% YoY (3x income growth)"
    tripwire_breached: ">18% YoY (unsustainable)"
    trend: "TBD"
    data_sources: ["Insurance Information Institute", "NAIC", "carrier filings"]
    
  VX-POLLY-1.02:
    name: "Homeowners Policy Non-Renewal Rate"
    domain: "Homeowners"
    description: "Rate at which carriers non-renew existing policies"
    unit: "%"
    current_value: "TBD"
    interpretation: |
      Non-renewals force consumers to find new coverage, often at higher rates
      or from insurers of last resort. Mass non-renewals indicate market stress.
    threshold_elevated: ">3% non-renewal rate"
    threshold_critical: ">5% non-renewal rate"
    tripwire_breached: ">8% non-renewal rate OR major carrier market exit"
    trend: "TBD"
    data_sources: ["State insurance dept data", "carrier announcements"]
    key_states: ["FL", "CA", "LA", "TX"]
    
  VX-POLLY-1.03:
    name: "Insurer of Last Resort Enrollment"
    domain: "Homeowners"
    description: "Policies in state FAIR plans / Citizens-type programs"
    unit: "Policy count or % of market"
    current_value: "TBD"
    interpretation: |
      Last resort insurers grow when private market fails.
      High enrollment = market dysfunction, not consumer choice.
    threshold_elevated: "Last resort share >5% of state market"
    threshold_critical: "Last resort share >10% OR growth >25% YoY"
    tripwire_breached: "Last resort becomes dominant insurer in region"
    trend: "TBD"
    data_sources: ["Citizens (FL)", "CA FAIR Plan", "state reports"]
    focus_states: ["FL", "CA", "LA"]
    
  VX-POLLY-1.04:
    name: "Homeowners Coverage Reduction"
    domain: "Homeowners"
    description: "Evidence of consumers reducing coverage limits or increasing deductibles"
    unit: "Qualitative + data where available"
    current_value: "TBD"
    interpretation: |
      Consumers reduce coverage to manage premium costs.
      This creates protection gaps — underinsured for actual replacement.
    threshold_elevated: "Industry reports increasing deductible selection"
    threshold_critical: "Average coverage-to-value ratio declining"
    tripwire_breached: "Widespread underinsurance documented"
    trend: "TBD"
    data_sources: ["Carrier commentary", "industry surveys", "academic research"]

### Auto Insurance Vectors

  VX-POLLY-2.01:
    name: "Auto Insurance Premium Increase Rate"
    domain: "Auto"
    description: "Year-over-year average auto insurance premium increase"
    unit: "% YoY"
    current_value: "TBD"
    context: "Auto insurance CPI component available from BLS"
    threshold_elevated: ">10% YoY"
    threshold_critical: ">15% YoY"
    tripwire_breached: ">20% YoY"
    trend: "TBD"
    data_sources: ["BLS CPI", "Insurance Information Institute", "carrier filings"]
    cross_reference: "CPI Motor Vehicle Insurance component"
    
  VX-POLLY-2.02:
    name: "Auto Insurance Combined Ratio"
    domain: "Auto"
    description: "Industry combined ratio (losses + expenses / premiums)"
    unit: "Ratio"
    current_value: "TBD"
    interpretation: |
      >100% = carriers losing money on underwriting.
      Sustained losses lead to rate increases or market exits.
    threshold_elevated: ">102%"
    threshold_critical: ">105%"
    tripwire_breached: ">110% sustained"
    trend: "TBD"
    data_sources: ["Carrier filings", "AM Best", "industry reports"]
    
  VX-POLLY-2.03:
    name: "Uninsured Motorist Rate"
    domain: "Auto"
    description: "Percentage of drivers without required auto insurance"
    unit: "%"
    current_value: "TBD"
    baseline: "~12-13% historically"
    interpretation: |
      Rising uninsured rate = consumers can't afford mandatory coverage.
      Direct measure of insurance affordability crisis.
    threshold_elevated: ">14%"
    threshold_critical: ">16%"
    tripwire_breached: ">18%"
    trend: "TBD"
    data_sources: ["Insurance Research Council", "state data"]
    
  VX-POLLY-2.04:
    name: "Non-Standard Auto Market Share"
    domain: "Auto"
    description: "Share of auto insurance market served by non-standard/high-risk carriers"
    unit: "%"
    current_value: "TBD"
    interpretation: |
      Non-standard market serves drivers rejected by standard carriers.
      Growing share = more consumers pushed out of standard market.
    threshold_elevated: "Share growing >10% YoY"
    threshold_critical: "Share growing >20% YoY"
    tripwire_breached: "Non-standard becomes >25% of total market"
    trend: "TBD"
    data_sources: ["Industry reports", "carrier data"]

### Health Insurance Vectors

  VX-POLLY-3.01:
    name: "Employer Health Coverage Offer Rate"
    domain: "Health"
    description: "Percentage of employers offering health insurance"
    unit: "%"
    current_value: "TBD"
    segments: "Track by employer size (small vs. large)"
    threshold_elevated: "Small employer offer rate drops >3pp YoY"
    threshold_critical: "Overall offer rate drops >2pp YoY"
    tripwire_breached: "Sustained multi-year decline in offers"
    trend: "TBD"
    data_sources: ["KFF Employer Survey", "BLS", "Census"]
    
  VX-POLLY-3.02:
    name: "Employee Premium Burden"
    domain: "Health"
    description: "Employee share of health insurance premium as % of income"
    unit: "%"
    current_value: "TBD"
    interpretation: |
      Rising burden = health insurance consuming more of wages.
      High burden leads to coverage declination or financial stress.
    threshold_elevated: "Employee share >8% of median income"
    threshold_critical: "Employee share >10% of median income"
    tripwire_breached: "Employee share >12% of median income"
    trend: "TBD"
    data_sources: ["KFF", "Census", "BLS"]
    
  VX-POLLY-3.03:
    name: "Health Insurance Deductible Trend"
    domain: "Health"
    description: "Average deductible for employer-sponsored coverage"
    unit: "$"
    current_value: "TBD"
    interpretation: |
      Rising deductibles = more out-of-pocket before coverage kicks in.
      High deductibles effectively = underinsurance for many consumers.
    threshold_elevated: "Average deductible >$2,000"
    threshold_critical: "Average deductible >$2,500"
    tripwire_breached: "Average deductible >$3,000"
    trend: "TBD"
    data_sources: ["KFF Employer Survey"]
    
  VX-POLLY-3.04:
    name: "Uninsured Rate"
    domain: "Health"
    description: "Percentage of population without health insurance"
    unit: "%"
    current_value: "TBD"
    segments: "Track by income level, age, state"
    threshold_elevated: ">9% overall"
    threshold_critical: ">10% overall"
    tripwire_breached: ">12% overall OR >25% in any large state"
    trend: "TBD"
    data_sources: ["Census", "KFF", "Gallup"]
    key_event: "Medicaid unwinding impact (2023-2024)"

### Market Stress Vectors

  VX-POLLY-4.01:
    name: "Carrier Market Exits"
    domain: "Market Stress"
    description: "Count and significance of carrier withdrawals from markets"
    unit: "Count + Qualitative"
    current_value: "TBD"
    interpretation: |
      Carrier exits reduce competition and coverage availability.
      Multiple exits in same market = systemic stress.
    threshold_elevated: "1-2 carriers exit major state"
    threshold_critical: "Major carrier (top 10) announces state exit"
    tripwire_breached: "Multiple major carriers exit OR no private options in region"
    trend: "TBD"
    data_sources: ["News", "state insurance dept", "carrier announcements"]
    historical: "State Farm CA non-renewals (2023), FL carrier failures"
    
  VX-POLLY-4.02:
    name: "Insurance Carrier Financial Stress"
    domain: "Market Stress"
    description: "Evidence of carrier financial deterioration"
    unit: "Qualitative"
    current_value: "TBD"
    interpretation: |
      Carrier stress leads to: rate increases, coverage reductions,
      market exits, or failures. Watch for downgrade cascade.
    threshold_elevated: "Multiple carriers report significant losses"
    threshold_critical: "Rating agency downgrades in sector"
    tripwire_breached: "Carrier insolvency OR state receivership"
    trend: "TBD"
    data_sources: ["AM Best", "rating agencies", "SEC filings"]
    
  VX-POLLY-4.03:
    name: "Catastrophe Loss Trend"
    domain: "Market Stress"
    description: "Insured catastrophe losses relative to historical average"
    unit: "$ billions or Index"
    current_value: "TBD"
    interpretation: |
      Rising cat losses drive rate increases and market exits.
      Climate change accelerating loss frequency and severity.
    threshold_elevated: "Annual cat losses >120% of 10-year average"
    threshold_critical: "Annual cat losses >150% of 10-year average"
    tripwire_breached: "Annual cat losses >200% OR multiple $10B+ events"
    trend: "TBD"
    data_sources: ["Swiss Re", "Munich Re", "III", "NOAA"]

---

## FLOW CASCADES

### FLOW-POLLY-01: Premium Affordability Cascade

flow_cascades:

  FLOW-POLLY-01:
    name: "Premium Affordability Cascade"
    pathway: |
      Insurance losses increase (climate, inflation, medical costs) →
      Carriers raise premiums to restore profitability →
      Premium increases outpace income growth →
      Consumers face affordability pressure →
      Consumers reduce coverage, raise deductibles, or lapse policies →
      Protection gaps emerge →
      Next incident becomes financial catastrophe
      
    mechanism: |
      Insurance pricing is actuarially driven — carriers must charge for risk.
      But consumer income doesn't adjust to match. The gap between actuarial
      necessity and affordability creates systematic underinsurance.
      
    breakpoint: "Premium growth exceeds income growth for 3+ consecutive years"
    lag_time: "6-12 months from premium increase to coverage reduction"
    status: "MONITORING"
    cross_domain: ["CARL (consumer stress)", "Housing costs"]

### FLOW-POLLY-02: Coverage Gap Cascade

  FLOW-POLLY-02:
    name: "Coverage Gap Cascade"
    pathway: |
      Consumer reduces/drops insurance coverage →
      Incident occurs (accident, storm, illness) →
      Consumer faces uninsured/underinsured loss →
      Emergency savings depleted (if any) →
      Credit cards / debt used to cover →
      Or loss goes unpaid (medical debt, property damage) →
      Credit deterioration and/or asset impairment →
      Consumer financial stress cascades to traditional metrics
      
    mechanism: |
      Insurance exists to prevent incident → financial ruin transmission.
      Without adequate coverage, minor incidents become major crises.
      This is the AMPLIFIER function of insurance stress.
      
    breakpoint: "Underinsured consumer experiences covered incident"
    lag_time: "Immediate to 6 months (depending on incident type)"
    status: "MONITORING"
    cross_domain: ["CARL (credit)", "Medical debt", "Property values"]

### FLOW-POLLY-03: Market Failure Cascade

  FLOW-POLLY-03:
    name: "Market Failure Cascade"
    pathway: |
      Catastrophe losses overwhelm carrier reserves →
      Carriers exit unprofitable markets →
      Remaining carriers have pricing power; rates spike →
      More consumers can't afford coverage →
      Last resort insurers overwhelmed →
      Last resort rates increase or coverage restricted →
      Widespread uninsurance in affected region →
      Property values affected (can't insure = can't sell/mortgage) →
      Regional economic stress
      
    mechanism: |
      Private insurance markets can fail when risk exceeds viable pricing.
      Government backstops have limited capacity. Market failure creates
      regional economic stress that transmits beyond insurance.
      
    breakpoint: "Private market share drops below 50% in major state"
    lag_time: "12-24 months from carrier exit to property market impact"
    status: "MONITORING"
    cross_domain: ["CARL (housing)", "Regional banking", "Property values"]
    focus_regions: ["Florida", "California", "Louisiana", "Texas coast"]

### FLOW-POLLY-04: Health Coverage Cascade

  FLOW-POLLY-04:
    name: "Health Coverage Cascade"
    pathway: |
      Employer health costs rise →
      Employers shift costs to employees OR drop coverage →
      Employees face higher premiums/deductibles →
      Some employees decline coverage (cost prohibitive) →
      ACA marketplace may be option but subsidies limited →
      Coverage gap emerges (too rich for Medicaid, can't afford ACA) →
      Uninsured consumer experiences medical event →
      Medical debt accumulates (leading cause of bankruptcy) →
      Consumer financial stress
      
    mechanism: |
      Health coverage tied to employment creates vulnerability.
      When employer coverage erodes, alternatives are often inadequate.
      Medical debt is largest source of consumer debt stress.
      
    breakpoint: "Medical event for uninsured/underinsured consumer"
    lag_time: "Immediate for event; 3-12 months for financial stress"
    status: "MONITORING"
    cross_domain: ["CARL (consumer credit)", "DOC (healthcare costs)"]
    note: "Coordinate with DOC agent on medical cost transmission"

### FLOW-POLLY-05: Polly-to-CARL Transmission

  FLOW-POLLY-05:
    name: "Polly-to-CARL Transmission"
    pathway: |
      Insurance stress indicators emerge (POLLY vectors trigger) →
      Consumers experience coverage gaps or premium burden →
      Incident occurs to underinsured consumer →
      Financial stress from uninsured loss →
      Credit utilization increases OR defaults occur →
      Asset impairment (unrepaired property, unpaid medical) →
      Traditional consumer credit metrics deteriorate →
      CARL vectors trigger
      
    mechanism: |
      Insurance stress is LEADING indicator because coverage decisions
      precede incidents. POLLY sees vulnerability building; CARL sees
      the damage when incidents actually occur.
      
    breakpoint: "Insurance-related financial stress appears in credit data"
    lag_time: "6-18 months from coverage gap to CARL visibility (incident-dependent)"
    status: "MONITORING"
    cross_domain: ["CARL (all vectors)"]

---

## DATA SOURCES

### Primary Sources

data_sources:

  insurance_information_institute:
    description: "Insurance industry research and data organization"
    url: "iii.org"
    frequency: "Ongoing reports, fact sheets"
    reliability: "HIGH — industry standard"
    coverage: "P&C primarily; some health"
    
  am_best:
    description: "Insurance rating agency"
    url: "ambest.com"
    frequency: "Ongoing ratings, reports"
    reliability: "HIGH — authoritative for carrier financial health"
    coverage: "All insurance carriers"
    
  naic:
    description: "National Association of Insurance Commissioners"
    url: "naic.org"
    frequency: "Quarterly/annual market data"
    reliability: "HIGH — regulatory data"
    coverage: "All US insurance markets"
    
  state_insurance_depts:
    description: "State-level regulators"
    key_states: ["CA DOI", "FL OIR", "TX TDI", "NY DFS", "LA DOI"]
    frequency: "Varies by state"
    reliability: "HIGH — regulatory filings"
    coverage: "State-specific market data, rate filings"
    
  kff:
    description: "Kaiser Family Foundation"
    url: "kff.org"
    frequency: "Annual employer survey, ongoing research"
    reliability: "HIGH — gold standard for health coverage data"
    coverage: "Health insurance comprehensive"
    
  cms:
    description: "Centers for Medicare & Medicaid Services"
    url: "cms.gov"
    frequency: "Ongoing enrollment data"
    reliability: "HIGH — federal data"
    coverage: "Medicare, Medicaid, ACA marketplaces"
    
  bls:
    description: "Bureau of Labor Statistics"
    url: "bls.gov"
    frequency: "Monthly CPI, periodic surveys"
    reliability: "HIGH"
    coverage: "Insurance price indices in CPI"
    
  carrier_filings:
    description: "SEC filings from public carriers"
    entities: ["ALL", "PGR", "TRV", "UNH", "ELV", "CVS", "CI", "HUM"]
    frequency: "Quarterly"
    reliability: "HIGH — audited"
    
  reinsurance_reports:
    description: "Catastrophe loss data from reinsurers"
    entities: ["Swiss Re", "Munich Re", "Aon"]
    frequency: "Quarterly/annual"
    reliability: "HIGH — authoritative for loss data"

### Data Gaps

data_gaps:
  
  - description: "Real-time policy lapse data (not consistently reported)"
    workaround: "Use carrier commentary, state data where available"
    severity: "MEDIUM"
    
  - description: "Coverage reduction specifics (deductible choices)"
    workaround: "Rely on industry surveys, carrier commentary"
    severity: "MEDIUM"
    
  - description: "Uninsured rate at granular geographic level"
    workaround: "State-level data from IRC; local estimates"
    severity: "LOW-MEDIUM"
    
  - description: "Mutual carrier financials (State Farm, etc.)"
    workaround: "AM Best ratings, state filings, news"
    severity: "MEDIUM — major market share in mutuals"

---

## GLOSSARY

glossary:

  terms:
    
    combined_ratio:
      definition: "Loss ratio + expense ratio; measures underwriting profitability"
      interpretation: ">100% means losing money on underwriting"
      example: "105% combined ratio = $1.05 in claims/expenses per $1.00 premium"
      
    loss_ratio:
      definition: "Claims paid / premiums earned"
      typical_range: "60-75% for healthy P&C business"
      
    non_renewal:
      definition: "Carrier declines to renew existing policy at term end"
      significance: "Forces consumer to find new coverage, often at higher cost"
      contrast: "Cancellation (mid-term termination) vs. non-renewal (at term end)"
      
    insurer_of_last_resort:
      definition: "State-mandated insurance option when private market unavailable"
      examples: ["Citizens (FL)", "FAIR Plans (CA, other states)", "NFIP (flood)"]
      significance: "Growth indicates private market failure"
      
    admitted_carrier:
      definition: "Insurer licensed and regulated by state insurance department"
      contrast: "Surplus lines / non-admitted (less regulated, higher risk)"
      
    surplus_lines:
      definition: "Insurance from non-admitted carriers for hard-to-place risks"
      significance: "Growing surplus lines = standard market shrinking"
      
    rate_adequacy:
      definition: "Whether premiums are sufficient to cover expected losses"
      importance: "Inadequate rates lead to carrier losses, then corrections"
      
    catastrophe_load:
      definition: "Portion of premium allocated to catastrophic event reserves"
      trend: "Increasing due to climate change"
      
    medical_loss_ratio:
      definition: "Health insurer claims paid / premiums (ACA requires minimum 80-85%)"
      acronym: "MLR"
      
    coverage_gap:
      definition: "Situation where consumer has no viable insurance option"
      health_specific: "Income too high for Medicaid, too low for unsubsidized ACA"
      
  acronyms:
    P&C: "Property & Casualty"
    DOI: "Department of Insurance"
    NAIC: "National Association of Insurance Commissioners"
    FAIR: "Fair Access to Insurance Requirements (state plans)"
    NFIP: "National Flood Insurance Program"
    ACA: "Affordable Care Act"
    MLR: "Medical Loss Ratio"
    CPI: "Consumer Price Index"
    KFF: "Kaiser Family Foundation"
    III: "Insurance Information Institute"

---

## REPORTING RELATIONSHIP

### POLLY → CARL State Vector

reporting:
  
  parent_agent: "CARL"
  reporting_frequency: "As significant developments occur; minimum monthly"
  
  state_vector_focus:
    primary_signal: "Consumer financial vulnerability through insurance stress"
    secondary_signals:
      - "Protection gaps creating catastrophe risk"
      - "Premium burden consuming discretionary income"
      - "Market failures in high-risk regions"
    
  key_questions_from_carl:
    - "How much consumer financial vulnerability exists due to insurance gaps?"
    - "What is the transmission mechanism from insurance stress to credit stress?"
    - "Are there regional concentrations of insurance-related vulnerability?"
    
  escalation_criteria:
    - "Any vector moves to BREACHED status"
    - "Major carrier announces significant market exit"
    - "State last-resort insurer shows rapid enrollment growth"
    - "Multiple vectors move to CRITICAL simultaneously"
    
  coordination_with_doc:
    note: "Health insurance overlaps with DOC domain"
    protocol: "Share State Vectors when health coverage affects medical cost exposure"

---

## GEOGRAPHIC FOCUS

### Priority States

geographic_focus:

  florida:
    priority: "CRITICAL"
    issues: ["P&C market crisis", "Carrier failures", "Citizens growth", "Hurricane exposure"]
    data_sources: ["FL OIR", "Citizens reports", "carrier filings"]
    
  california:
    priority: "CRITICAL"  
    issues: ["Wildfire exposure", "Carrier non-renewals", "FAIR Plan growth"]
    data_sources: ["CA DOI", "FAIR Plan reports"]
    
  louisiana:
    priority: "HIGH"
    issues: ["Hurricane exposure", "Carrier exits", "High premiums"]
    data_sources: ["LA DOI"]
    
  texas:
    priority: "HIGH"
    issues: ["Hail/wind exposure", "Market concentration", "Grid vulnerability"]
    data_sources: ["TX TDI"]
    
  national:
    priority: "ONGOING"
    issues: ["Auto insurance inflation", "Health coverage trends", "Overall market health"]
    data_sources: ["National aggregates from above sources"]

---

## SESSION QUICK REFERENCE

### For Update Sessions
Focus on: VX-POLLY-1.xx (Homeowners), VX-POLLY-2.xx (Auto), premium trends
Key question: "Are insurance costs outpacing consumer ability to pay?"

### For Analysis Sessions
Focus on: FLOW cascades, regional deep dives, cross-domain transmission
Key question: "What mechanisms are creating consumer vulnerability?"

### For Reconciliation Sessions
Focus on: State-level data updates, carrier status, cross-reference integrity
Key question: "Is our market picture current and accurate?"

### For State Vector Reports
Include: Highest-concern vectors, regional alerts, protection gap estimates
Format: Per POLLY_METHODOLOGY_SKELETON §6.2

---

# END OF SKELETON

# Maintenance Notes:
# - Update vector current_values as data arrives (varies by source frequency)
# - Track carrier announcements for market exits/non-renewals
# - Monitor catastrophe season (June-November Atlantic hurricane)
# - Watch ACA subsidy policy changes
# - Coordinate with DOC on health coverage overlap
# - Version increment for structural changes
