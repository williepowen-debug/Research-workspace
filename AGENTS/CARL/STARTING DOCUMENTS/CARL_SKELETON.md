# CARL DOMAIN SKELETON

# Purpose: Structural scaffold for LLM domain orientation
# Domain:  US Consumer Financial Stress, Household Balance Sheets, Employment,
#          Cost of Living, Credit Health, Behavioral Economics
# Agent:   CARL (Consumer Carl - Consumer Stress Domain Prome)
#
# Version: 1.3
# Created: 2025-12-17
# Updated: 2026-01-19
# Author:  CARL-I Session (Initial Architecture), CARL-II Session (v1.1 Update),
#          CARL-V Session (v1.2 Log System Architecture), CARL-001 Session (v1.3 Vector Expansion)
#
# Changelog v1.3:
#   - Added 2 new vectors: VX-CARL-2.05 (Utility Cost & Arrears), VX-CARL-2.06 (Healthcare Premium Shock)
#   - Updated vector_count from 19 to 22 (now includes all workbook vectors)
#   - Expanded HOUSING_SHELTER sub-domain to include utility and healthcare stress
#   - Updated tripwire_summary to 22 vectors
#   - Reconciled skeleton with workbook CARL_MLFLFLOWVX_S6.xlsx
#
# Changelog v1.2:
#   - Added SECTION 0: Log System Architecture
#   - Codified ML/FL/FLOW/VX purposes, lifecycles, and relationships
#   - Defined Domain/Sub-Domain taxonomy (CREDIT, HOUSING, EMPLOYMENT, BEHAVIORAL)
#   - Standardized ML ID format: ML-[DOMAIN]-[##]
#   - Updated ml_entries count to 17 (post-cleanup)
#   - Removed cross-PROME references (OTTO, REGINALD, LIQUID, SAM, CEO)
#   - Removed Section 6 (Transmission to Other Agents) - renumbered subsequent sections
#
# Changelog v1.1:
#   - Added 4 new vectors: VX-CARL-1.08, 1.09, 2.04, 3.04
#   - Updated all vector values to Jan 2026 data
#   - Expanded tripwire summary to 19 vectors
#   - Added data sources for new vectors
#   - Added glossary terms: credit_lockout, savings_buffer, auto_insurance_spiral
#   - Renamed VX-CARL-2.03 to "Homeowners Insurance Cost Spiral" (distinguish from 2.04)
#
# Usage:
#   - Load this file at the start of any CARL session
#   - Provides entity types, relationship vocabulary, core architecture
#   - Named transmission paths define known cascade routes
#   - Thresholds define tripwires for escalation
#
# Note: This skeleton defines STRUCTURE. Current VALUES come from live data/handoffs.
#

metadata:
  name: "CARL Domain Skeleton"
  domain: "US Consumer Stress, Household Balance Sheets, Employment, Credit Health"
  version: "1.3"
  created: "2025-12-17"
  updated: "2026-01-19"
  knowledge_cutoff: "2026-01-19"
  
  phase_model: |
    Stage 1 (Stress Emergence) -> Stage 2 (Acceleration/Secondary Wave) -> 
    Stage 3 (Crisis/Structural Amplifier) -> Stage 4 (Recognition Cascade)
    
    Consumer stress LEADS banking stress by 6-18 months.
    Consumer delinquency -> Bank NCOs -> Credit tightening -> More consumer stress (feedback)
    
  primary_agent: "CARL (Consumer Carl)"
  
  core_thesis:
    name: "The Front-Loading Paradigm"
    description: |
      Consumer financial deterioration is LEADING (not lagging) the broader 
      banking and credit crisis. The traditional sequence (recession -> unemployment -> 
      consumer stress) has INVERTED. Consumers are breaking FIRST due to:
      
      1. INFLATION SQUEEZE: Essentials (food, shelter, insurance, utilities) inflating 
         faster than wages, compressing discretionary spending to zero
         
      2. DEBT TRAP: Post-pandemic credit extension created "Zombie Borrowers" making 
         minimum payments at 22%+ APR, functionally insolvent but technically current
         
      3. LIQUIDITY EXHAUSTION: Pandemic savings depleted, BNPL/credit cards maxed, 
         401k hardship withdrawals at all-time highs
         
      4. RATE SHOCK: Fed hikes transmitted to auto loans, credit cards, mortgages 
         while wages stagnant
         
      The "soft landing" narrative is contradicted by granular data showing synchronized 
      stress across ALL consumer credit verticals simultaneously.
      
    confidence: "Pattern 92%, Timing 70%, Magnitude 85%"
    validation_status: "VALIDATED - Multiple tripwires breached Jan 2026"

  current_status:
    system_alert: "STAGE 2 -> STAGE 3 TRANSITION (Auto/Shadow Banking at Stage 3)"
    vector_count: 22
    ml_entries: 17   # Updated Jan 17, 2026 (post-cleanup)
    fl_entries: 34   # Pending review
    flow_count: 7
    breached_vectors: 7
    critical_vectors: 9
    note: "Front-Loading thesis VALIDATED. Synchronized breakage confirmed."

#
# SECTION 0: LOG SYSTEM ARCHITECTURE
#
# CARL maintains four distinct logs, each with a specific purpose.
# Understanding their relationship is critical for proper documentation.
#

log_system:

  overview: |
    The CARL logging system consists of four interconnected components:
    
    VX (Vectors) -> Defines WHAT we measure
         |
    ML (Master Log) -> Documents current STATE of those metrics
         |
    FL (Catalyst Log) -> Watches for TRIGGERS that could change state
         |
    FLOW (Cascade Map) -> Shows HOW changes PROPAGATE across vectors

  logs:
  
    ML:
      name: "Master Log"
      purpose: "Current state documentation"
      question_answered: "What do we know right now?"
      entry_represents: "A phenomenon or stress signal we are actively tracking"
      lifecycle: |
        - Created when new stress signal identified
        - Updated as new data arrives
        - Rarely retired; entries evolve with new evidence
        - Status reflects current severity (BREACHED/CRITICAL/ELEVATED/WATCH/STABLE)
      id_format: "ML-[DOMAIN]-[##]"
      domains:
        CR: "Credit (auto, card, BNPL, student)"
        HS: "Housing & Shelter (rent, HOA, utilities, healthcare)"
        EI: "Employment & Income (labor, government)"
        BP: "Behavioral Psychology (spending, sentiment, retirement)"
        SL: "Student Loans (if tracked separately from CR)"
      columns:
        - Timestamp
        - ID
        - Vectors (VX cross-reference)
        - Domain
        - Sub-Domain
        - Description
        - Analysis
        - Data/Quote
        - Source
        - What to Track
        - STATUS
        - Confidence
        - Next Action
        - Owner
        - Cross-Links
        - STAGE
        - NOTE
        - Invalidation Criteria
        
    FL:
      name: "Catalyst Log (Future Log)"
      purpose: "Dated future triggers and deadlines"
      question_answered: "What should we watch for, and when?"
      entry_represents: "A specific calendar event or deadline that could trigger state change"
      lifecycle: |
        - Created when future catalyst identified
        - Monitored as date approaches
        - RETIRED when date passes (regardless of whether it fired)
        - If fired: relevant ML entry updated with outcome
        - If missed: note the non-event, retire entry
      id_format: "FL-[###]"
      key_fields:
        - Catalyst Date
        - Trigger Condition
        - Expected Impact
        - Related Vectors
        - Related ML Entries
      examples:
        - "Jan 30, 2026: Government funding deadline"
        - "Feb 2026: Q4 2025 NY Fed HHDC release"
        - "March 2026: First garnishment payment impact"
        
    FLOW:
      name: "Cascade Map"
      purpose: "Transmission pathways showing how stress propagates"
      question_answered: "If X breaks, what breaks next?"
      entry_represents: "A structural relationship between stress vectors"
      lifecycle: |
        - Created when cascade mechanism identified
        - Updated when mechanism changes or is validated
        - Persists as long as structural relationship holds
        - Not date-driven; mechanism-driven
      id_format: "FLOW-CARL-[##]"
      key_fields:
        - Pathway stages
        - Trigger conditions
        - Transmission speed
        - Feedback loops
        - Cross-domain transmission (to, etc.)
      note: "FLOW entries are the plumbing diagram - they show HOW, not WHEN"
      
    VX:
      name: "Vector Registry"
      purpose: "Metric definitions, thresholds, and tripwires"
      question_answered: "What are we measuring and what triggers escalation?"
      entry_represents: "A specific metric with defined thresholds"
      lifecycle: |
        - Defined in skeleton; rarely added
        - Thresholds updated when new data justifies
        - Status updated as tripwires approached/breached
      id_format: "VX-CARL-[#.##]"
      structure:
        "1.xx": "Credit (unsecured and secured)"
        "2.xx": "Housing & Shelter"
        "3.xx": "Employment & Income"
        "4.xx": "Behavioral Psychology"
      note: "VX is the measurement framework; ML/FL/FLOW document what we observe"

  workflow:
    new_finding: |
      1. Identify which VX vector(s) it relates to
      2. Create ML entry documenting current state
      3. If future catalyst identified, create FL entry with date
      4. If cascade mechanism identified, update/create FLOW entry
      
    catalyst_fires: |
      1. FL entry: Mark as FIRED, note outcome, retire
      2. ML entry: Update with new data from catalyst
      3. VX status: Update if tripwire breached
      4. FLOW: Validate if cascade occurred as predicted
      
    catalyst_misses: |
      1. FL entry: Mark as MISSED, note why, retire
      2. Consider: Does the miss invalidate our thesis?
      3. Update confidence scores if applicable

  domain_subdomain_taxonomy:
    note: "Domain/Sub-Domain provide granularity beyond what the ID prefix gives"
    
    CREDIT:
      sub_domains: [AUTO, CARD, BNPL, STUDENT]
      vectors: ["VX-CARL-1.01 through 1.09"]
      
    HOUSING:
      sub_domains: [RENT, HOA, UTILITIES, HEALTHCARE]
      vectors: ["VX-CARL-2.01 through 2.06"]
      note: "Healthcare (ACA) included here as cost-of-living burden"
      
    EMPLOYMENT:
      sub_domains: [LABOR, GOVERNMENT]
      vectors: ["VX-CARL-3.01 through 3.04"]
      
    BEHAVIORAL:
      sub_domains: [SPENDING, SENTIMENT, RETIREMENT]
      vectors: ["VX-CARL-4.01 through 4.03"]

# SECTION 1: ENTITY TYPES (The Vocabulary)
#
# These define the categories of objects in the domain.
# Every node belongs to exactly one entity type.

entity_types:

  #
  # CONSUMER SEGMENTS
  #
  
  Consumer_Segment:
    description: "Demographic/credit segments of US consumers"
    subtypes:
      - prime              # FICO 720+
      - near_prime         # FICO 660-719
      - subprime           # FICO 580-659
      - deep_subprime      # FICO <580
      - gen_z              # Age-based: ~18-27
      - millennial         # Age-based: ~28-43
      - boomer             # Age-based: ~60-78
    key_properties:
      - segment_name: string
      - population_millions: float
      - avg_fico: integer
      - debt_to_income: percentage
      - delinquency_rate_30d: percentage
      - delinquency_rate_90d: percentage
      - savings_rate: percentage
      - status: [STABLE, STRESSED, DISTRESSED, DEFAULTING]

  Credit_Product:
    description: "Consumer credit products being tracked"
    subtypes:
      - credit_card        # Revolving unsecured
      - auto_loan          # Secured vehicle
      - student_loan       # Federal and private
      - mortgage           # Home secured
      - heloc              # Home equity line
      - bnpl               # Buy Now Pay Later
      - personal_loan      # Unsecured installment
      - medical_debt       # Healthcare-related debt (added v1.1)
    key_properties:
      - product_type: subtype
      - total_outstanding_trillions: float
      - avg_apr: percentage
      - delinquency_30d: percentage
      - delinquency_90d: percentage
      - charge_off_rate: percentage
      - yoy_growth: percentage

  #
  # COST OF LIVING ENTITIES
  #
  
  Expense_Category:
    description: "Major household expense categories"
    subtypes:
      - housing            # Rent, mortgage, property tax
      - utilities          # Electric, gas, water
      - insurance_home     # Homeowners/renters insurance
      - insurance_auto     # Auto insurance (added v1.1)
      - insurance_health   # Health insurance premiums
      - food               # Grocery and dining
      - transportation     # Gas, maintenance, transit
      - healthcare         # Out-of-pocket medical
      - childcare          # Daycare, education
    key_properties:
      - category: subtype
      - avg_monthly_cost: float
      - yoy_inflation: percentage
      - share_of_income: percentage  # For median household
      - essential: boolean           # TRUE = cannot easily cut

  Housing_Stress_Entity:
    description: "Specific housing-related stress sources"
    subtypes:
      - hoa_assessment     # Special assessments, reserve funding
      - insurance_premium  # Homeowners/renters insurance
      - property_tax       # Local tax increases
      - rent_increase      # Lease renewals
      - utility_arrears    # Past-due utility bills
    key_properties:
      - entity_type: subtype
      - affected_population: integer
      - avg_cost_increase: percentage
      - geographic_concentration: list  # States/regions most affected

  #
  # EMPLOYMENT ENTITIES
  #
  
  Employment_Indicator:
    description: "Labor market indicators tracked"
    subtypes:
      - unemployment_u3    # Headline rate
      - unemployment_u6    # Broader measure (includes underemployed)
      - jobless_claims     # Weekly initial claims
      - long_term_unemployed  # >6 months
      - layoff_announcements  # WARN notices, corporate announcements
      - job_openings       # JOLTS data
      - quit_rate          # Voluntary separations
      - gig_saturation     # Uber/DoorDash driver supply
      - savings_rate       # Personal savings rate (added v1.1)
    key_properties:
      - indicator: subtype
      - current_value: float
      - threshold_watch: float
      - threshold_critical: float
      - trend: [IMPROVING, STABLE, DETERIORATING]

  Government_Program:
    description: "Safety net programs affecting consumer liquidity"
    subtypes:
      - snap               # Food stamps
      - liheap             # Utility assistance
      - medicaid           # Health coverage
      - unemployment_insurance
      - student_loan_programs  # IBR, SAVE, forgiveness
      - aca_subsidies      # ACA premium subsidies (added v1.1)
    key_properties:
      - program: subtype
      - beneficiaries_millions: float
      - avg_monthly_benefit: float
      - funding_status: [STABLE, THREATENED, CUT, ELIMINATED]
      - policy_change_pending: boolean

  #
  # BEHAVIORAL ENTITIES
  #
  
  Behavioral_Indicator:
    description: "Consumer behavior signals indicating stress"
    subtypes:
      - minimum_payment_rate    # % making only minimum on cards
      - hardship_withdrawal     # 401k early withdrawals
      - gambling_losses         # Sports betting, casino
      - bnpl_essential_usage    # BNPL for groceries/utilities
      - trade_down_behavior     # Shopping at dollar stores
      - couponing_surge         # Extreme couponing behavior
      - skip_payment_rotation   # Which bills get skipped first
      - credit_denial_expectation  # Expecting to be denied credit (added v1.1)
    key_properties:
      - indicator: subtype
      - current_rate: percentage
      - historical_avg: percentage
      - stress_threshold: percentage
      - status: [NORMAL, ELEVATED, CRITICAL]

  #
  # TRANSMISSION ENTITIES (Consumer â†' Banking)
  #
  
  Bank_Exposure:
    description: "Banking sector exposure to consumer credit"
    subtypes:
      - credit_card_portfolio
      - auto_loan_portfolio
      - student_loan_servicer
      - mortgage_portfolio
      - heloc_portfolio
    key_properties:
      - exposure_type: subtype
      - total_exposure_billions: float
      - delinquency_rate: percentage
      - reserve_coverage: percentage
      - nco_trend: [IMPROVING, STABLE, DETERIORATING]
    note: "Detailed bank analysis owned by

#
# SECTION 2: RELATIONSHIP TYPES (The Grammar)
#
# These define how entities connect.

relationship_types:

  # Stress Relationships
  strains:
    description: "One factor creates stress on another"
    example: "Inflation strains household budget"
    
  depletes:
    description: "One factor exhausts another"
    example: "Minimum payments deplete savings"
    
  triggers:
    description: "Threshold breach activates cascade"
    example: "90-day DQ triggers charge-off"
    
  amplifies:
    description: "Feedback loop intensifies stress"
    example: "Credit tightening amplifies consumer stress"
    
  masks:
    description: "One metric hides true stress in another"
    example: "Minimum payments mask insolvency"
    
  leads:
    description: "One indicator precedes another"
    example: "Minimum payment surge leads delinquency spike (6-12 months)"
    
  transmits_to:
    description: "Stress in one domain flows to another"
    example: "Consumer defaults transmit_to bank NCOs"
    
  locks_out:
    description: "One condition prevents access to another"
    example: "Credit score collapse locks_out prime borrowing"
    note: "Added v1.1 for credit lockout dynamics"

#
# SECTION 3: SUB-DOMAINS
#
# CARL's domain is organized into six sub-domains.

sub_domains:

  CREDIT_UNSECURED:
    name: "Credit Cards & Unsecured Debt"
    description: |
      Revolving credit, personal loans, BNPL, medical debt. The "liquidity bridge" 
      that becomes a "debt trap" when rates spike and savings deplete. Now includes
      medical debt dynamics (v1.1) and credit lockout tracking.
    key_metrics:
      - total_credit_card_debt_trillions
      - avg_apr
      - utilization_rate
      - delinquency_30d
      - delinquency_90d
      - minimum_payment_rate
      - charge_off_rate
      - credit_denial_rate      # Added v1.1
      - medical_debt_on_reports # Added v1.1
    vectors: ["VX-CARL-1.01", "VX-CARL-1.02", "VX-CARL-1.03", "VX-CARL-1.08", "VX-CARL-1.09"]
    
  CREDIT_SECURED:
    name: "Auto & Secured Consumer Loans"
    description: |
      Auto loans, personal secured loans. Consumer-side view (behavior, affordability).
      Lender/ABS-side owned by
    key_metrics:
      - auto_loan_delinquency_30d
      - auto_loan_delinquency_60d
      - subprime_auto_dq
      - deep_subprime_auto_dq
      - negative_equity_rate
      - avg_monthly_payment
      - loan_to_value
    vectors: ["VX-CARL-1.04", "VX-CARL-1.05"]
    coordination: "Share delinquency data with
    
  STUDENT_LOANS:
    name: "Student Loan Crisis"
    description: |
      Federal and private student loans. Post-pandemic payment resumption shock.
      Geographic and demographic concentration. Garnishment enforcement began Jan 2026.
    key_metrics:
      - total_student_debt_trillions
      - delinquency_rate_90d
      - borrowers_behind_count
      - conditional_delinquency_rate  # % of those required to pay
      - credit_score_impact
      - forbearance_rate
      - garnishment_notices     # Added v1.1
    vectors: ["VX-CARL-1.06", "VX-CARL-1.07"]
    
  HOUSING_SHELTER:
    name: "Housing, Shelter & Insurance"
    description: |
      Rent stress, HOA assessments, insurance premium spikes (home AND auto),
      utility arrears, healthcare premium shock. The "non-discretionary squeeze"
      on household budgets. Auto insurance separated as distinct vector in v1.1.
      Utility arrears and healthcare premiums added as distinct vectors in v1.3.
    key_metrics:
      - rent_late_rate
      - hoa_assessment_avg
      - homeowners_insurance_yoy
      - auto_insurance_yoy      # Added v1.1
      - utility_arrears_billions
      - eviction_filings
      - mortgage_delinquency
      - uninsured_rate          # Added v1.3
      - aca_enrollment          # Added v1.3
    vectors: ["VX-CARL-2.01", "VX-CARL-2.02", "VX-CARL-2.03", "VX-CARL-2.04", "VX-CARL-2.05", "VX-CARL-2.06"]
    
  EMPLOYMENT_INCOME:
    name: "Employment & Income"
    description: |
      Labor market health, wage growth vs inflation, gig economy saturation,
      white-collar recession, government workforce changes. Now includes
      savings buffer tracking (v1.1) as upstream liquidity indicator.
    key_metrics:
      - unemployment_u3
      - unemployment_u6
      - real_wage_growth  # Nominal minus inflation
      - jobs_plentiful_spread  # Conference Board spread
      - long_term_unemployed
      - layoff_announcements
      - gig_driver_earnings
      - personal_savings_rate   # Added v1.1
      - emergency_fund_months   # Added v1.1
    vectors: ["VX-CARL-3.01", "VX-CARL-3.02", "VX-CARL-3.03", "VX-CARL-3.04"]
    
  BEHAVIORAL_PSYCHOLOGY:
    name: "Behavioral Economics & Psychology"
    description: |
      Consumer behavioral signals: doom spending, gambling, retirement leakage,
      trade-down behavior, payment prioritization hierarchy.
    key_metrics:
      - gambling_losses_billions
      - hardship_withdrawal_rate
      - trade_down_index  # Dollar store migration
      - doom_spending_indicators
      - financial_nihilism_survey  # Gen Z specific
      - payment_hierarchy_inversion  # Are consumers skipping auto before cards?
    vectors: ["VX-CARL-4.01", "VX-CARL-4.02", "VX-CARL-4.03"]

#
# SECTION 4: VECTOR DEFINITIONS
#
# CARL's 19 primary stress vectors with tripwires.

vectors:

  # CREDIT UNSECURED VECTORS
  
  VX-CARL-1.01:
    name: "Credit Card Delinquency Surge"
    domain: CREDIT_UNSECURED
    priority: P1
    mechanism: |
      APR at decade high (22.8%) + savings depleted â†' minimum payment only â†'
      functional insolvency â†' eventual 90-day DQ â†' charge-off
    tripwire:
      metric: "Credit Card 90+ DQ Rate"
      threshold: 13.7%  # All-time high (2011)
      current: 11.35-12.3%  # Jan 2026
      buffer: ~140 bps
    what_to_track:
      - Fed G.19 release (monthly)
      - Bank earnings (quarterly NCO guidance)
      - Minimum payment rate (Philadelphia Fed)
    status: "CRITICAL - Approaching threshold; Fed notes flattening but K-shape masks"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    downstream: ["Bank NCOs", "Credit tightening", "VX-CARL-1.02"]
    
  VX-CARL-1.02:
    name: "Zombie Borrower Transition"
    domain: CREDIT_UNSECURED
    priority: P1
    mechanism: |
      Minimum payment users (12-year high) are "Zombie Borrowers" - technically 
      current but functionally insolvent. Transition to delinquency lags 6-12 months.
      15.3% now expect to miss minimum payment (pandemic-level, Jan 2026).
    tripwire:
      metric: "Minimum Payment Only Rate"
      threshold: "12-year high"  # Qualitative
      current: "AT 12-year high"
      note: "Leading indicator for VX-CARL-1.01"
    what_to_track:
      - Philadelphia Fed credit card data
      - Servicer commentary on payment behavior
      - NY Fed SCE expected missed payments
    status: "BREACHED - Leading indicator hit; DQ wave projected Q1-Q2 2026"
    trend: "â†'"
    transmission_speed: "6-12 MONTHS LAG"
    downstream: ["VX-CARL-1.01"]
    
  VX-CARL-1.03:
    name: "BNPL Hidden Leverage"
    domain: CREDIT_UNSECURED
    priority: P1
    mechanism: |
      BNPL invisible to traditional credit scoring until default. 42% miss payments
      (up from 34% in 2023). 25% using for essentials (groceries). Creates "shadow 
      leverage" on households. Gen Z late rate at 51%.
    tripwire:
      metric: "BNPL Late Payment Rate"
      threshold: 45%
      current: 42%  # Jan 2026 (up from 25% essential usage in skeleton v1.0)
    what_to_track:
      - CFPB BNPL reports
      - Affirm/Klarna earnings
      - Delinquency by use-case
      - Credit bureau integration status
    status: "CRITICAL - Accelerating; phantom debt concern validated"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    downstream: ["Shadow leverage", "Credit scoring gaps", "VX-CARL-1.09"]
    
  VX-CARL-1.04:
    name: "Auto Affordability Collapse"
    domain: CREDIT_SECURED
    priority: P1
    mechanism: |
      Average new car payment >$700/month + negative equity widespread â†'
      Prioritization hierarchy breaks â†' Skip auto to pay rent/cards â†'
      Voluntary surrenders increase. Record 1.73M repos (2024).
    tripwire:
      metric: "Subprime Auto 60+ DQ"
      threshold: 7.0%
      current: 6.65%  # Oct 2025 - ALL-TIME HIGH since Fitch tracking began 1994
      note: "RECORD BREACHED"
    what_to_track:
      - Equifax/Experian auto reports
      - Manheim used car index
      - Repo statistics
      - Denial rate (doubled to 15.2%)
    status: "BREACHED - All-time record; cockroach thesis validated (Tricolor, PrimaLend)"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    coordination: "Feed data to
    downstream: [", "FLOW-AUTO-01", "VX-CARL-1.05"]
    
  VX-CARL-1.05:
    name: "Deep Subprime Acceleration"
    domain: CREDIT_SECURED
    priority: P1
    mechanism: |
      Lowest credit tier showing 40% YoY acceleration in delinquencies.
      These borrowers have abandoned collateral entirely (negative equity trap).
      Super-prime showing cracks: 300%+ YoY increase (low absolute level).
    tripwire:
      metric: "Deep Subprime 30+ DQ YoY Change"
      threshold: "+50% YoY"
      current: "+40% YoY"
    what_to_track:
      - Equifax deep subprime segment
      -
      - Prime/super-prime contagion signals
    status: "BREACHED - Accelerating; prime contagion emerging"
    trend: "â†‘"
    transmission_speed: "WEEKS to MONTHS"
    downstream: [", "VX-CARL-1.04"]
    
  VX-CARL-1.06:
    name: "Student Loan Delinquency Shock"
    domain: STUDENT_LOANS
    priority: P1
    mechanism: |
      5-year pandemic pause ended â†' Payment shock â†' 31% conditional delinquency 
      (highest ever, 3x pre-pandemic) â†' 12M+ borrowers behind â†' Credit score collapse.
      Wage garnishment began Jan 7, 2026 (~1,000 initial notices).
    tripwire:
      metric: "Student Loan Conditional DQ Rate"
      threshold: 35%
      current: 31%  # Q3 2025 - HIGHEST EVER
      secondary: "5.5M in default, 3.7M at 181-270 DPD"
    what_to_track:
      - NY Fed Household Debt report (quarterly)
      - FSA data releases
      - SAVE program litigation
      - Garnishment notice volume
    status: "BREACHED - Enforcement phase activated; generational damage"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    downstream: ["Credit score collapse", "Auto loan denial", "Mortgage lockout", "VX-CARL-1.07", "VX-CARL-1.09"]
    
  VX-CARL-1.07:
    name: "Gen Z Credit Destruction"
    domain: STUDENT_LOANS
    priority: P1
    mechanism: |
      Gen Z borrowers hit hardest by student loan resumption + credit card rates.
      14% saw 50+ point FICO drops. Creates "generation of defaulters" locked out
      of prime credit for decades. Prime borrower contagion: 23-24% of defaults
      now from prime borrowers (paradigm shift from subprime-only).
    tripwire:
      metric: "Gen Z Avg FICO Drop"
      threshold: 50 points
      current: "50+ points for 14% of cohort; 23% prime contagion"
    what_to_track:
      - Experian generational credit reports
      - Student loan servicer data
      - Prime borrower share of defaults
    status: "BREACHED - Generational damage confirmed; prime contagion validated"
    trend: "â†'"
    transmission_speed: "YEARS (long-term scarring)"
    downstream: ["Generational wealth lockout", "VX-CARL-1.09"]
    
  VX-CARL-1.08:
    name: "Medical Debt Return"
    domain: CREDIT_UNSECURED
    priority: P1
    mechanism: |
      Court vacated CFPB rule (July 2025) â†' $220B medical debt returns to credit 
      reports â†' 15M Americans see 50-100 pt FICO drops â†' Credit lockout cascade.
      ACA subsidy expiration (Dec 31, 2025) amplifies with premium shock (+114%).
    tripwire:
      metric: "Medical Debt on Credit Reports"
      threshold: "$250B"
      current: "$220B returning"
      secondary: "15M affected immediately"
    what_to_track:
      - CFPB medical debt reports
      - Credit bureau policy changes
      - Court litigation status
      - Collection activity trends
    status: "CRITICAL - Policy reversal confirmed; cliff hit"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    downstream: ["VX-CARL-1.09", "Credit lockout cascade", "FLOW-MED-01"]
    note: "Added v1.1 - Tracks $220B medical debt returning to credit system"
    
  VX-CARL-1.09:
    name: "Credit Lockout Acceleration"
    domain: CREDIT_UNSECURED
    priority: P1
    mechanism: |
      Multiple vectors converging to lock consumers OUT of credit system:
      - Auto denial rate DOUBLED (6.7% â†' 15.2%) in 4 months
      - Card approval tightening
      - Credit limit cuts
      - Medical debt + student loan damage to scores
      Creates "credit desert" for subprime/near-prime segments.
    tripwire:
      metric: "Auto Loan Denial Rate"
      threshold: 20%
      current: 15.2%  # Oct 2025 (doubled from 6.7% in June)
      secondary: "Card limit cuts accelerating"
    what_to_track:
      - NY Fed SCE credit rejection rates
      - Bank earnings commentary on underwriting
      - Approval rate trends by credit tier
      - Credit limit changes
    status: "CRITICAL - Denial rate doubled; lockout accelerating"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    downstream: ["Liquidity exhaustion", "BNPL surge (VX-CARL-1.03)", "Last-resort lending"]
    note: "Added v1.1 - Forward indicator of credit access collapse"
    
  # HOUSING SHELTER VECTORS
  
  VX-CARL-2.01:
    name: "Rent Stress Threshold"
    domain: HOUSING_SHELTER
    priority: P2
    mechanism: |
      Rent is last bill skipped before eviction. 11.7% late rate indicates extreme
      distress - essentials being compromised. Eviction filings follow.
      9-month sustained elevation.
    tripwire:
      metric: "Rent Late Payment Rate"
      threshold: 15%
      current: 11.7%
    what_to_track:
      - RealPage/Yardi rent payment data
      - Eviction Lab filings
      - Census Pulse surveys
    status: "ELEVATED - Distress signal; 9-month sustained"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    downstream: ["Homelessness", "Consumer spending reduction"]
    
  VX-CARL-2.02:
    name: "HOA Assessment Shock"
    domain: HOUSING_SHELTER
    priority: P1
    mechanism: |
      FL SIRS and similar laws forcing structural reserve compliance â†'
      Special assessments $134K-$400K per unit â†' Owners can't pay â†'
      HOA super-liens (priority over mortgage) â†' Foreclosure cascade.
      DEADLINE PASSED Dec 31, 2025.
    tripwire:
      metric: "HOA Special Assessment Average"
      threshold: "$50K per unit"
      current: "$134K-$400K per unit (FL)"
      geographic: ["Florida", "Nevada"]
    what_to_track:
      - State HOA regulatory filings
      - County foreclosure data
      - Condo association financials
      - FL condo prices (-6.1% YoY)
    status: "CRITICAL - Deadline passed; foreclosure wave building"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    downstream: [", "FLOW-CARL-05"]
    note: "Impairs bank mortgage collateral via super-lien mechanism"
    
  VX-CARL-2.03:
    name: "Homeowners Insurance Cost Spiral"
    domain: HOUSING_SHELTER
    priority: P1
    mechanism: |
      Homeowners insurance +24% (2021-2024), high-risk zips +50% YoY.
      Carriers exiting FL/CA â†' state backstops more expensive â†'
      "Hidden tax" on homeownership erodes discretionary income.
    tripwire:
      metric: "Homeowners Insurance Premium YoY (High-Risk Zips)"
      threshold: 60% YoY
      current: 50% YoY
    what_to_track:
      - State insurance commissioner data
      - Citizens (FL) / FAIR Plan (CA) growth
      - Carrier exit announcements
    status: "CRITICAL - Accelerating; carrier exits continuing"
    trend: "â†‘"
    transmission_speed: "MONTHS to YEARS"
    downstream: ["Discretionary squeeze", "Housing affordability"]
    note: "Renamed from 'Insurance Cost Spiral' in v1.1 to distinguish from auto"
    
  VX-CARL-2.04:
    name: "Auto Insurance Spiral"
    domain: HOUSING_SHELTER
    priority: P1
    mechanism: |
      Auto insurance CPI +20-30% YoY, outpacing overall inflation.
      Required for employment in most of US. Rising repair costs (EVs, technology),
      theft rates, litigation costs drive premiums. Different dynamics than
      homeowners insurance (weather-driven). Compounds auto affordability crisis.
    tripwire:
      metric: "Auto Insurance CPI YoY"
      threshold: 35% YoY
      current: 20-30% YoY
    what_to_track:
      - BLS CPI auto insurance component
      - State insurance commissioner rate filings
      - Carrier surcharge announcements
      - Uninsured motorist rates
    status: "CRITICAL - Sustained high inflation; employment access impact"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    downstream: ["Transportation costs", "Employment access", "Discretionary squeeze", "VX-CARL-1.04"]
    note: "Added v1.1 - Distinct from homeowners insurance dynamics"

  VX-CARL-2.05:
    name: "Utility Cost & Arrears Stress"
    domain: HOUSING_SHELTER
    priority: P1
    mechanism: |
      Electricity CPI +29% since 2021. 1-in-6 households (21.5M) behind on utility
      bills. $23B+ in arrears (+31% since Dec 2023). LIHEAP staff eliminated April
      2025 creating processing delays. 4M disconnections projected 2025. Winter
      moratoriums ending triggers spring disconnection wave. Utility stress
      compresses discretionary spending and triggers essential-use credit card debt.
    tripwire:
      metric: "Utility Arrears Total"
      threshold: $30B
      current: $23B (trending to $25B)
      secondary: "1 in 6 households behind"
    what_to_track:
      - NEADA utility arrears data
      - BLS CPI electricity component
      - DOE disconnection reports
      - LIHEAP funding and processing status
      - State moratorium schedules
    status: "CRITICAL - Safety net collapse amplifying stress"
    trend: "↑"
    transmission_speed: "MONTHS"
    downstream: ["Household budget squeeze", "VX-CARL-1.01 (credit card essential usage)", "Homelessness risk"]
    note: "Added v1.3 - Tracks utility cost burden and arrears"

  VX-CARL-2.06:
    name: "Healthcare Premium Shock"
    domain: HOUSING_SHELTER
    priority: P1
    mechanism: |
      ACA enhanced subsidies expired Dec 31, 2025. Premiums +114% avg ($888→$1,904/yr).
      4.8M projected uninsured (Urban Institute). Enrollment already -1.5M (22.8M vs
      24.3M). Bronze plan selection jumped to 59% (higher deductibles). Subsidy cliff
      at 400% FPL creates tax bill trap ($10K+) for 2M+ households. Compounds with
      VX-CARL-1.08 (medical debt returning to credit reports).
    tripwire:
      metric: "Uninsured Rate"
      threshold: 12%
      current: ~10% (trending up)
      secondary: "ACA enrollment <20M"
    what_to_track:
      - CMS enrollment data (effectuated)
      - Uninsured rate surveys
      - Bronze plan selection rates
      - Medical debt trends
      - Congressional action on subsidy extension
    status: "CRITICAL - Cliff activated; coverage loss cascade begun"
    trend: "↑"
    transmission_speed: "MONTHS"
    downstream: ["VX-CARL-1.08 (Medical Debt Return)", "Emergency fund depletion", "Credit score damage"]
    note: "Added v1.3 - Tracks ACA subsidy cliff impact on healthcare access"

  # EMPLOYMENT INCOME VECTORS

  VX-CARL-3.01:
    name: "Labor Sentiment Collapse"
    domain: EMPLOYMENT_INCOME
    priority: P2
    mechanism: |
      "Jobs plentiful" vs "jobs hard to get" spread collapsed from 40 pts to 8 pts.
      Perception leads reality - hiring freezes follow sentiment deterioration.
    tripwire:
      metric: "Conference Board Jobs Spread"
      threshold: 0 (inversion)
      current: 8 points
    what_to_track:
      - Conference Board Consumer Confidence (monthly)
      - JOLTS quits rate
      - Indeed job postings
    status: "WATCH - Approaching inversion"
    trend: "â†“"
    transmission_speed: "MONTHS"
    downstream: ["Hiring freezes", "Consumer confidence"]
    
  VX-CARL-3.02:
    name: "Long-Term Unemployment Surge"
    domain: EMPLOYMENT_INCOME
    priority: P2
    mechanism: |
      Long-term unemployed (>6 months) surged 34% in 3 months (May-Aug 2025).
      These workers exhaust UI benefits, deplete savings, default on credit.
      2025 layoffs hit 1.2M (highest since 2020). Job growth weakest since 2020 (584K).
    tripwire:
      metric: "Long-Term Unemployed Count"
      threshold: 2.5M
      current: 1.95M
    what_to_track:
      - BLS Employment Situation (monthly)
      - UI exhaustion data
      - Challenger Gray layoff reports
    status: "ELEVATED - Accelerating; 1.2M layoffs in 2025"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    downstream: ["Credit defaults", "Safety net strain", "VX-CARL-3.04"]
    
  VX-CARL-3.03:
    name: "Government Workforce Shock"
    domain: EMPLOYMENT_INCOME
    priority: P1
    mechanism: |
      $14.8B resignation program targeting 275K federal employees.
      Largest mass resignation during crisis. 43-day shutdown (Oct 1 - Nov 12, 2025)
      was longest in US history. LIHEAP staff entirely fired April 2025.
      Next funding deadline: Jan 30, 2026.
    tripwire:
      metric: "Federal Workforce Reduction"
      threshold: 275K
      current: "162K dropped Oct-Nov 2025; program ongoing"
    what_to_track:
      - OPM workforce data
      - DC/MD/VA unemployment claims
      - Safety net program processing delays
      - Shutdown risk (next: Jan 30, 2026)
    status: "CRITICAL - Active; longest shutdown completed; LIHEAP staff eliminated"
    trend: "â†‘"
    transmission_speed: "MONTHS"
    downstream: ["Safety net delays", "Regional economic depression"]
    
  VX-CARL-3.04:
    name: "Savings Buffer Exhaustion"
    domain: EMPLOYMENT_INCOME
    priority: P1
    mechanism: |
      Pandemic savings fully depleted. Personal savings rate collapsed.
      Emergency fund surveys show median household has <3 months runway.
      This is the "master switch" - when savings hit zero, all other vectors
      accelerate simultaneously. Upstream of all credit stress.
    tripwire:
      metric: "Personal Savings Rate"
      threshold: 3%
      current: ~4.5%  # Trending down
      secondary: "Emergency fund <3 months for majority"
    what_to_track:
      - BEA personal savings rate (monthly)
      - Fed Survey of Consumer Finances
      - Bankrate emergency fund surveys
      - Pandemic savings depletion estimates
    status: "CRITICAL - Buffer nearly exhausted; upstream trigger for all credit vectors"
    trend: "â†‘"
    transmission_speed: "IMMEDIATE (when depleted)"
    downstream: ["ALL credit vectors", "VX-CARL-4.01", "Liquidity crisis"]
    note: "Added v1.1 - The 'runway' metric; master switch for cascade"
    
  # BEHAVIORAL VECTORS
  
  VX-CARL-4.01:
    name: "Retirement System Leakage"
    domain: BEHAVIORAL_PSYCHOLOGY
    priority: P1
    mechanism: |
      Hardship withdrawals at all-time high (4.8% of participants, up from 3.6%).
      46% of Gen Z taking early withdrawals. +365% vs pre-pandemic average.
      "Demand destruction" for future to fund survival today.
    tripwire:
      metric: "Hardship Withdrawal Rate"
      threshold: 5%
      current: 4.8%  # 2025 - ALL-TIME HIGH
    what_to_track:
      - Vanguard/Fidelity 401k reports (annual)
      - Paychex withdrawal data
      - Plan sponsor surveys
    status: "BREACHED - All-time high; approaching threshold"
    trend: "â†‘"
    transmission_speed: "YEARS (long-term consequence)"
    downstream: ["Long-term wealth destruction", "FLOW-SAV-01"]
    
  VX-CARL-4.02:
    name: "Gambling as Liquidity Desperation"
    domain: BEHAVIORAL_PSYCHOLOGY
    priority: P2
    mechanism: |
      $264B in gambling losses (2023, trending higher). 37% of Gen Z showing 
      addiction signs. 18.7M problem gamblers. When slow accumulation is 
      impossible (inflation), consumers turn to high-variance speculation. 
      Symptom of financial despair.
    tripwire:
      metric: "Gambling Losses Annual"
      threshold: $300B
      current: $264B (trending to $150B+ losses)
    what_to_track:
      - AGA gaming revenue reports
      - Sports betting handle data
      - Bankruptcy filings citing gambling
      - Problem gambler surveys
    status: "ELEVATED - Behavioral despair signal"
    trend: "â†‘"
    transmission_speed: "N/A (symptom, not cause)"
    downstream: ["Behavioral despair signal"]
    
  VX-CARL-4.03:
    name: "Trade-Down Migration"
    domain: BEHAVIORAL_PSYCHOLOGY
    priority: P1
    mechanism: |
      Dollar Tree gained 2.6M new customers in Q1, majority earning >$100K.
      Upper-middle class crowding into discount retail = broad purchasing power
      erosion, not isolated subprime stress. Thrift +11.7%, off-price +6.6%.
      Discretionary units -5% (Dec 2025). Confirms K-shape bifurcation.
    tripwire:
      metric: "High-Income Dollar Store Traffic"
      threshold: "Qualitative - sustained increase"
      current: "2.6M new customers >$100K income; discretionary -5%"
    what_to_track:
      - Dollar Tree/General earnings
      - Consumer sentiment by income bracket
      - Circana discretionary volume
      - Placer.ai foot traffic
    status: "BREACHED - Validated; K-shape consumption confirmed"
    trend: "â†'"
    transmission_speed: "N/A (confirming indicator)"
    downstream: ["Broad stress confirmation", "K-shape validation"]

#
# SECTION 5: NAMED FLOWS (Cascade Pathways)
#
# How stress propagates within and beyond consumer domain.

flows:

  FLOW-CARL-01:
    name: "Grand Unification (Systemic Cascade)"
    description: |
      The master cascade: Inflation squeeze â†' Income insufficiency â†' Front-loading 
      behavior (max cards) â†' Cards max out â†' Auto defaults first (weakest collateral) â†'
      Collateral devaluation â†' Lender insolvency â†' Credit crunch â†' More defaults
    pathway:
      - stage: "Inflation/Policy Shock"
        vectors: ["VX-CARL-2.03", "VX-CARL-2.04", "VX-CARL-3.01"]
        status: "COMPLETE"
        
      - stage: "Income Inversion"
        vectors: ["VX-CARL-3.02", "VX-CARL-3.03", "VX-CARL-3.04"]
        mechanism: "Wages < Expenses â†' Gap funded by credit"
        status: "COMPLETE"
        
      - stage: "Credit Exhaustion"
        vectors: ["VX-CARL-1.01", "VX-CARL-1.02", "VX-CARL-1.03", "VX-CARL-1.08", "VX-CARL-1.09"]
        mechanism: "Cards maxed, BNPL saturated, savings gone, credit lockout begins"
        status: "ACTIVE"
        
      - stage: "Collateral Default"
        vectors: ["VX-CARL-1.04", "VX-CARL-1.05"]
        mechanism: "Auto defaults spike (lowest recovery, most underwater)"

        status: "ENTERING"
        
      - stage: "Banking Transmission"
        mechanism: "Bank NCOs spike â†' Credit tightening â†' Consumer lockout"

        status: "NEXT"
        
    feedback_loops:
      - "Credit tightening â†' More consumer stress â†' More defaults"
      - "Repo flood â†' Used car price collapse â†' Higher LGD â†' Tighter credit"
      - "Credit lockout â†' BNPL surge â†' Hidden leverage â†' Worse defaults"
    breakpoint: "Composite Delinquency >13% OR Prime Auto Defaults >2%"
    confidence: 0.88
    status: "ACTIVE - STAGE 3 (Credit Exhaustion â†' Collateral Default transition)"
    
  FLOW-CARL-02:
    name: "Labor-Credit Death Spiral"
    description: |
      Banks cut credit to small business (SLOOS tightening) â†' SMB layoffs â†'
      Unemployed workers default on personal credit â†' Banks take losses â†'
      Banks tighten credit further
    pathway:
      - "SLOOS tightening (C&I loans)"
      - "Sub-V bankruptcies +17%"
      - "SMB layoffs"
      - "Worker credit defaults"
      - "Bank losses"
      - "More tightening (loop)"
    tripwire: "Jobless Claims >300K sustained"

    confidence: 0.75
    status: "WATCH"
    
  FLOW-CARL-03:
    name: "Minimum Payment â†' Delinquency Wave"
    description: |
      Minimum payment rate hits 12-year high â†' 6-12 month lag â†' 
      Delinquency surge â†' Charge-off wave â†' Bank reserve builds
    pathway:
      - "Minimum payment rate spikes (BREACHED Oct 2025)"
      - "6-12 month lag"
      - "90-day DQ surge (PROJECTED Q1-Q2 2026)"
      - "Charge-off wave (PROJECTED Q2-Q3 2026)"
      - "Bank reserve builds â†' Earnings pressure"
    lag_time: "6-12 months"
    confidence: 0.82
    status: "LEADING INDICATOR BREACHED - Wave projected Q1-Q2 2026"
    
  FLOW-CARL-04:
    name: "Student Loan â†' Credit Lockout"
    description: |
      Student loan delinquency â†' Credit score destruction (50+ pt drops) â†'
      Auto loan denial â†' Mortgage qualification failure â†' Generational 
      wealth accumulation blocked. Garnishment enforcement began Jan 2026.
    pathway:
      - "Payment resumption shock (COMPLETE)"
      - "Delinquency (31% conditional - BREACHED)"
      - "Credit score collapse (ACTIVE)"
      - "Prime credit lockout (ACTIVE)"
      - "No auto, no mortgage (ACTIVE)"
      - "No wealth accumulation (LONG-TERM)"
    affected_population: "12M+ borrowers; 23% prime contagion"
    long_term_impact: "Generational (decades)"
    confidence: 0.90
    status: "ACTIVE - VALIDATED; Garnishment phase begun"
    
  FLOW-CARL-05:
    name: "HOA Super-Lien Cascade"
    description: |
      Structural reserve laws â†' Special assessments â†' Owner default â†'
      HOA super-lien (priority over mortgage) â†' Foreclosure â†'
      Bank collateral impairment
    pathway:
      - "SIRS compliance deadline (PASSED Dec 31, 2025)"
      - "Special assessments issued ($134K-$400K)"
      - "Owners can't pay (ACTIVE)"
      - "HOA files super-lien (BUILDING)"
      - "Foreclosure (PROJECTED Q1-Q2 2026)"
      - "First mortgage impaired (TRANSMISSION TO
    geographic_concentration: ["Florida", "Nevada"]

    confidence: 0.78
    status: "ACTIVE - Deadline passed; foreclosure wave building"
    
  FLOW-CARL-06:
    name: "Medical Debt Credit Score Shock"
    description: |
      Court vacates CFPB rule (July 2025) â†' $220B medical debt returns to 
      credit reports â†' 15M Americans see 50-100 pt FICO drops â†'
      Credit lockout cascade. Amplified by ACA subsidy expiration.
    pathway:
      - "Court ruling (July 2025 - COMPLETE)"
      - "$220B re-enters scoring (ACTIVE)"
      - "15M affected immediately (ACTIVE)"
      - "50-100 pt FICO drops (ACTIVE)"
      - "Credit limit cuts (ACTIVE)"
      - "Auto/card denial (ACTIVE)"
    catalyst: "Court ruling July 15, 2025"
    amplifier: "ACA subsidy expiration Dec 31, 2025 (+114% premium shock)"
    affected_population: "15M Americans; 22M ACA affected"
    confidence: 0.85
    status: "ACTIVE - Policy reversal confirmed; ACA cliff hit"

  FLOW-CARL-07:
    name: "Wealth Effect Cascade"
    description: |
      Equity correction triggers forced selling among levered households,
      collapsing consumer spending and creating regional housing stress.
      Distinct from typical recession pathway - this is ASSET-DRIVEN not
      EMPLOYMENT-DRIVEN consumer stress.
    pathway:
      - stage: "Preconditions Met"
        vectors: ["HENRY-CAPE", "HENRY-HEA"]
        mechanism: "CAPE >40, Household equity allocation 47.08% (ATH)"
        status: "COMPLETE"

      - stage: "Correction Trigger"
        mechanism: "S&P 500 declines >15% from peak"
        trigger: "Recession signal, earnings miss, liquidity event, or Japan repatriation"
        status: "LATENT"

      - stage: "Margin Call Cascade"
        mechanism: |
          Households with margin debt face calls. Estimated 4-6M households
          with leveraged equity positions. Forced liquidation accelerates decline.
        downstream: ["Equity prices gap lower", "401k balances crater"]
        status: "LATENT"

      - stage: "Wealth Effect Transmission"
        vectors: ["VX-CARL-3.04", "VX-CARL-4.01"]
        mechanism: |
          Consumer spending contracts 3-5 cents per dollar of wealth loss.
          At 47% equity allocation, median household ($150K net worth) loses
          ~$10K per 15% correction. Spending cut: $300-500/year per household.
          Aggregate: $40-60B consumer spending reduction.
        status: "LATENT"

      - stage: "Forced Home Sales"
        mechanism: |
          Households unable to meet margin calls or needing liquidity sell
          real estate. Geographic concentration in high-equity-allocation zips.
          Creates regional housing price pressure.
        downstream: ["Regional housing stress", "REGINALD bank exposure"]
        status: "LATENT"

      - stage: "Credit Score Damage"
        vectors: ["VX-CARL-1.09"]
        mechanism: |
          Forced liquidations, late payments, credit utilization spikes as
          households use credit to bridge income gap. Accelerates credit lockout.
        status: "LATENT"

    feedback_loops:
      - "Selling begets selling (margin cascade)"
      - "Wealth loss → spending cut → earnings miss → more selling"
      - "Housing sales → price decline → negative equity → more sales"
    compound_signal: "CMP-05 in COMPOUND_SIGNALS.md"
    cross_agent:
      from_agents: ["HENRY (valuation trigger)", "SAM (Japan repatriation trigger)"]
      to_agents: ["REGINALD (housing/deposit impact)"]
    quantification:
      household_equity_allocation: "47.08% (ATH)"
      margin_debt_estimate: "$800B+ (NYSE margin debt)"
      spending_multiplier: "3-5 cents per dollar wealth loss"
      population_affected: "Concentrated in top 40% by wealth"
    research_gaps:
      - "Households with leverage on equity positions (exact count)"
      - "Geographic concentration of high-allocation households"
      - "Correlation between equity allocation and mortgage status"
    tripwire: "S&P 500 -15% from peak AND VIX >30 sustained"
    confidence: 0.75
    status: "LATENT - Preconditions met, awaiting correction trigger"

#
# SECTION 6: KEY DATA SOURCES
#
# Where CARL gets information.

data_sources:

  primary_monthly:
    - name: "Federal Reserve G.19"
      content: "Consumer credit outstanding, revolving/non-revolving"
      url: "federalreserve.gov/releases/g19/"
      
    - name: "BLS Employment Situation"
      content: "Unemployment, labor force participation, wages"
      url: "bls.gov/news.release/empsit.toc.htm"
      
    - name: "BLS CPI"
      content: "Inflation components including auto insurance"
      url: "bls.gov/cpi/"
      note: "Added v1.1 for VX-CARL-2.04"
      
    - name: "Conference Board Consumer Confidence"
      content: "Sentiment, jobs plentiful/hard-to-get spread"
      
    - name: "CFPB Complaint Database"
      content: "Consumer complaint trends by product"
      
    - name: "BEA Personal Income and Outlays"
      content: "Personal savings rate"
      url: "bea.gov/data/income-saving/personal-income"
      note: "Added v1.1 for VX-CARL-3.04"
      
  primary_quarterly:
    - name: "NY Fed Household Debt Report"
      content: "Comprehensive debt by category, delinquency, credit scores"
      url: "newyorkfed.org/microeconomics/hhdc"
      release: "~6 weeks after quarter end"
      
    - name: "NY Fed Survey of Consumer Expectations"
      content: "Credit access, expected delinquency, denial rates"
      note: "Added v1.1 for VX-CARL-1.09"
      
    - name: "FDIC Quarterly Banking Profile"
      content: "Bank consumer loan performance, NCOs"
      
    - name: "Equifax/Experian Credit Reports"
      content: "Delinquency by credit tier, auto/card specifics"
      
  secondary:
    - name: "Philadelphia Fed Credit Card Data"
      content: "Minimum payment behavior, utilization"
      
    - name: "Vanguard/Fidelity 401k Reports"
      content: "Hardship withdrawals, retirement leakage"
      release: "Annual"
      
    - name: "Paychex Workforce Analytics"
      content: "Hardship withdrawal trends (more frequent updates)"
      note: "Added v1.1"
      
    - name: "RealPage/Yardi"
      content: "Rent payment data, occupancy"
      
    - name: "Manheim Used Vehicle Index"
      content: "Used car prices, auction data"
      
    - name: "AGA Gaming Revenue Reports"
      content: "Gambling losses, sports betting handle"
      
    - name: "Fitch Ratings Auto ABS"
      content: "Subprime auto delinquency tracking (since 1994)"
      note: "Primary source for VX-CARL-1.04"
      
    - name: "State Insurance Commissioner Filings"
      content: "Rate approvals, carrier exits, premium data"
      note: "Added v1.1 for VX-CARL-2.03 and 2.04"
      
    - name: "Bankrate Emergency Fund Survey"
      content: "Household savings buffer data"
      note: "Added v1.1 for VX-CARL-3.04"
      
    - name: "Challenger Gray & Christmas"
      content: "Layoff announcements, workforce reductions"
      note: "Added v1.1"
      
    - name: "CFPB Medical Debt Reports"
      content: "Medical debt on credit reports, policy changes"
      note: "Added v1.1 for VX-CARL-1.08"
      
    - name: "DOE Federal Student Aid"
      content: "Student loan delinquency, garnishment data"
      note: "Added v1.1"

#
# SECTION 7: TRIPWIRE SUMMARY
#
# Quick reference for all 22 tripwires.

tripwire_summary:

  BREACHED:
    - VX-CARL-1.02: "Minimum payment rate (12-year high) - BREACHED"
    - VX-CARL-1.04: "Subprime auto 60+ DQ at 6.65% (ATH since 1994) - BREACHED"
    - VX-CARL-1.05: "Deep subprime +40% YoY acceleration - BREACHED"
    - VX-CARL-1.06: "Student loan conditional DQ at 31% (ATH) - BREACHED"
    - VX-CARL-1.07: "Gen Z credit destruction + 23% prime contagion - BREACHED"
    - VX-CARL-4.01: "Hardship withdrawal rate at 4.8% (ATH) - BREACHED"
    - VX-CARL-4.03: "Trade-down migration validated (2.6M >$100K customers) - BREACHED"

  CRITICAL:
    - VX-CARL-1.01: "Credit card 90+ DQ at 11.35-12.3% (threshold 13.7%) - ~140bps buffer"
    - VX-CARL-1.03: "BNPL late rate at 42% (threshold 45%) - CRITICAL"
    - VX-CARL-1.08: "Medical debt $220B returning (threshold $250B) - CRITICAL"
    - VX-CARL-1.09: "Auto denial rate doubled to 15.2% (threshold 20%) - CRITICAL"
    - VX-CARL-2.02: "HOA assessments $134K-$400K; deadline passed - CRITICAL"
    - VX-CARL-2.03: "Homeowners insurance +50% YoY high-risk (threshold 60%) - CRITICAL"
    - VX-CARL-2.04: "Auto insurance +20-30% YoY (threshold 35%) - CRITICAL"
    - VX-CARL-2.05: "Utility arrears $23B (threshold $30B); 1-in-6 behind - CRITICAL"
    - VX-CARL-2.06: "ACA cliff activated; 4.8M projected uninsured (threshold 12%) - CRITICAL"
    - VX-CARL-3.03: "Govt workforce shock - 162K dropped, LIHEAP staff eliminated - CRITICAL"
    - VX-CARL-3.04: "Savings rate ~4.5% (threshold 3%) - CRITICAL; master switch"

  ELEVATED:
    - VX-CARL-2.01: "Rent late rate at 11.7% (threshold 15%) - ELEVATED"
    - VX-CARL-3.02: "Long-term unemployed at 1.95M (threshold 2.5M) - ELEVATED"
    - VX-CARL-4.02: "Gambling losses $264B (threshold $300B) - ELEVATED"

  WATCH:
    - VX-CARL-3.01: "Jobs spread at 8 pts (threshold 0) - WATCH"

#
# SECTION 8: INVALIDATION FRAMEWORK
#
# What would prove CARL's thesis wrong?

invalidation_criteria:

  overall_thesis:
    description: "What would prove the consumer front-loading thesis wrong?"
    criteria:
      - condition: "Credit card DQ falls below 10% and holds for 2 quarters"
        confidence_impact: "Pattern -20%"
        status: "NOT MET"
        
      - condition: "Real wage growth exceeds inflation for 3+ consecutive months"
        confidence_impact: "Pattern -15%"
        status: "NOT MET"
        
      - condition: "Savings rate recovers to >7% (pre-pandemic normal)"
        confidence_impact: "Pattern -15%"
        status: "NOT MET"
        
      - condition: "Minimum payment rate declines from 12-year high"
        confidence_impact: "Timing -20%"
        status: "NOT MET"
        
      - condition: "Fed cuts rates 150+ bps AND delinquencies stabilize"
        confidence_impact: "Magnitude -25%"
        status: "PARTIAL (cuts yes, DQ stabilization no)"
        
      - condition: "Major fiscal stimulus ($1T+) directly to consumers"
        confidence_impact: "Timing -30%"
        status: "NOT MET"
        
      - condition: "Credit denial rates decline across all tiers"
        confidence_impact: "Pattern -15%"
        status: "NOT MET"
        note: "Added v1.1 for VX-CARL-1.09"

  flow_specific:
    FLOW-CARL-01:
      invalidated_if:
        - "Inflation falls below 2% sustained"
        - "Wage growth >5% for 2+ quarters"
        - "Consumer debt declines (paydown cycle)"
        
    FLOW-CARL-03:
      invalidated_if:
        - "Minimum payment rate declines"
        - "6-12 month lag passes without DQ surge (test: Q1-Q2 2026)"
        
    FLOW-CARL-05:
      invalidated_if:
        - "FL extends SIRS deadline"
        - "Assessment assistance program funded at scale"
        
    FLOW-CARL-06:
      invalidated_if:
        - "Congress restores ACA subsidies"
        - "Court reverses medical debt ruling"

    FLOW-CARL-07:
      invalidated_if:
        - "Equity markets recover without significant correction (>15%)"
        - "Household equity allocation falls below 40% via organic rebalancing"
        - "Margin debt declines significantly before correction"

#
# SECTION 9: GLOSSARY
#

glossary:

  abbreviations:
    DQ: "Delinquency"
    NCO: "Net Charge-Off"
    APR: "Annual Percentage Rate"
    BNPL: "Buy Now Pay Later"
    LGD: "Loss Given Default"
    FICO: "Fair Isaac Corporation (credit score)"
    HOA: "Homeowners Association"
    UI: "Unemployment Insurance"
    SLOOS: "Senior Loan Officer Opinion Survey"
    LIHEAP: "Low Income Home Energy Assistance Program"
    SNAP: "Supplemental Nutrition Assistance Program"
    HELOC: "Home Equity Line of Credit"
    SIRS: "Structural Integrity Reserve Study (FL)"
    ACA: "Affordable Care Act"
    SCE: "Survey of Consumer Expectations (NY Fed)"
    
  key_concepts:
    front_loading:
      definition: |
        Consumer stress LEADS (not lags) banking/corporate stress. Traditional
        sequence (recession â†' unemployment â†' consumer default) has inverted.
        Consumers are breaking FIRST due to inflation/rate squeeze.
        
    zombie_borrower:
      definition: |
        Borrower making only minimum payments, technically current but 
        functionally insolvent. At 22%+ APR, minimum payments cover almost 
        no principal. These borrowers will transition to default 6-12 months
        after exhausting liquidity buffers.
        
    prioritization_hierarchy:
      definition: |
        Traditional order consumers pay bills: (1) Mortgage/Rent, (2) Auto,
        (3) Utilities, (4) Credit Cards. Hierarchy INVERSION (skipping auto
        to pay cards) signals extreme distress and collateral abandonment.
        
    trade_down_behavior:
      definition: |
        When higher-income consumers shift to discount retailers (Dollar Tree,
        Aldi). Indicates broad purchasing power erosion, not isolated subprime
        stress. Key confirming indicator.
        
    super_lien:
      definition: |
        HOA assessment lien that takes PRIORITY over first mortgage. If HOA
        forecloses, mortgage lender's collateral is impaired. Creates hidden
        transmission from consumer (HOA) stress to bank (mortgage) losses.
        
    credit_lockout:
      definition: |
        When consumers are systematically denied access to credit due to 
        converging factors: score damage (student loans, medical debt), 
        tightening underwriting, and rising denial rates. Creates "credit 
        desert" for subprime/near-prime segments. Self-reinforcing as 
        locked-out consumers turn to last-resort options (BNPL, payday).
      note: "Added v1.1"
        
    savings_buffer:
      definition: |
        Household liquid savings available to absorb income shocks. Measured
        by personal savings rate and emergency fund surveys. When buffer 
        depletes to zero, consumer is one paycheck from default. Acts as
        "master switch" for all credit vectors - buffer exhaustion accelerates
        all downstream stress simultaneously.
      note: "Added v1.1"
        
    auto_insurance_spiral:
      definition: |
        Distinct from homeowners insurance crisis. Driven by: (1) rising repair
        costs (EVs, technology), (2) theft rates, (3) litigation costs, 
        (4) reinsurance costs. Unlike weather-driven home insurance, affects
        all geographies. Required for employment in most of US, creating
        inelastic demand and employment access barrier.
      note: "Added v1.1"
        
    k_shape_bifurcation:
      definition: |
        Economic divergence where upper-income households maintain/increase
        spending while lower-income households deteriorate. Masks aggregate
        stress in top-line metrics. Top 10% now 49.2% of consumer spending.
        Aggregate "flattening" in delinquency data often hides continued
        deterioration in lower-income segments.
      note: "Added v1.1"
        
    cockroach_thesis:
      definition: |
        Jamie Dimon quote: "When you see one cockroach, there are probably more."
        Applied to subprime auto lender failures. Tricolor criminal charges
        (Dec 2025) followed by PrimaLend Ch.11 (Oct 2025) validated thesis.
        Suggests additional lender failures likely.
      note: "Added v1.1"

# END OF SKELETON

# Usage Instructions:
#
# 1. LOAD AT SESSION START
#    Upload this file or paste into system prompt
#    LLM now has domain vocabulary and architecture
#
# 2. LOAD HANDOFF + CURRENT DATA
#    Upload latest CARL Handoff (CARL-I, CARL-II, etc.)
#    Upload Consumer_Logs.xlsx if needed for evidence
#    LLM maps current data to skeleton structure
#
# 3. ASK QUESTIONS
#    "What's the current credit card delinquency status?"
#    "Trace FLOW-CARL-01 cascade position"
#    "What would invalidate the front-loading thesis?"
#    "What's currently BREACHED?"
#    LLM uses skeleton to structure answers
#
# 4. COORDINATE WITH OTHER PROMES
#    Reference
#    Reference
#    Reference
#
# 5. GENERATE STATE VECTOR FOR
#    At session end, generate CARL state vector per
#
# 6. WORKING WITH VECTORS TAB
#    The VECTORS tab in Consumer_MLFLFLOW.xlsx contains live status
#    This skeleton defines structure; VECTORS tab has current values
#    Reconcile quarterly or when major changes occur
