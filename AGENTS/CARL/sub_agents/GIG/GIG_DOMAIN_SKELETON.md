# GIG DOMAIN SKELETON

# Purpose: Structural scaffold for GIG agent operations
# Domain:  Gig Economy Saturation, Platform Labor Markets, Worker Financial Stress
# Agent:   GIG (Gig Economy Saturation Monitor)
#
# Version: 1.0
# Created: 2026-01-20
# Author:  Initial Architecture Session
#
# Usage:
#   - Load this file at the start of any GIG session
#   - Provides vocabulary, entities, vectors, and thresholds for gig economy monitoring
#   - Companion to GIG_METHODOLOGY_SKELETON which governs process
#   - This skeleton governs the CONTENT of GIG's domain
#
# Reporting: GIG reports to CARL via State Vectors
# Signal:    Consumer income fragility and gig worker financial stress
#            "Cracks forming underneath the ice"

---

## METADATA

metadata:
  name: "GIG Domain Skeleton"
  domain: "Gig Economy Saturation, Platform Labor, Worker Financial Stress"
  version: "1.0"
  created: "2026-01-20"
  parent_agent: "CARL"
  
  phase_model: |
    Phase 1 (Expansion) → Phase 2 (Saturation) → Phase 3 (Compression) → Phase 4 (Distress)
    
    Expansion: Platforms growing, worker earnings healthy, demand exceeds supply
    Saturation: Worker supply catches demand, earnings plateau, competition increases
    Compression: Oversupply, earnings decline, hours increase for same income
    Distress: Mass worker financial stress, platform consolidation, labor market dysfunction
    
  core_thesis:
    name: "Gig Saturation Thesis"
    statement: |
      The gig economy has shifted from opportunity to trap. What began as flexible 
      supplemental income has become primary income for workers squeezed out of 
      traditional employment. Simultaneously, platform oversupply is compressing 
      per-worker earnings. This creates a doom loop: workers flee TO gig work as 
      traditional jobs fail, but gig earnings are ALSO failing due to saturation.
      
      The gig economy is both SYMPTOM (people flee to gig work when employment fails)
      and CAUSE (declining gig income accelerates consumer financial stress).
      
      Gig worker stress is a LEADING indicator of broader labor market deterioration—
      these workers are the first to feel compression and the last to show up in 
      official unemployment statistics.
      
    confidence: "65% — thesis plausible, evidence accumulating, needs validation"
    
    invalidation_criteria:
      - "Per-worker earnings rise sustainably for 2+ consecutive quarters"
      - "Active worker counts decline while platform revenue grows (healthy equilibrium)"
      - "Multi-apping rates decline significantly (workers don't need multiple platforms)"
      - "Traditional employment recovery absorbs gig-dependent workers"
    
    competing_hypotheses:
      - name: "Healthy Flexibility"
        statement: "Gig work remains voluntary supplemental income; workers can exit to traditional jobs"
        current_assessment: "Weakening — evidence of involuntary gig dependence increasing"
      - name: "Platform Rationalization"
        statement: "Platforms will reduce worker supply through deactivation, restoring earnings"
        current_assessment: "Possible — but creates different stress (unemployment)"

---

## ENTITY DEFINITIONS

### Platform Categories

platforms:
  rideshare:
    description: "On-demand transportation services"
    entities:
      - name: "Uber (Rides)"
        ticker: "UBER"
        data_sources: ["SEC filings", "earnings calls", "Gridwise", "driver forums"]
      - name: "Lyft"
        ticker: "LYFT"
        data_sources: ["SEC filings", "earnings calls", "Gridwise", "driver forums"]
    key_metrics: ["active drivers", "rides per driver", "earnings per hour", "incentive spend"]
    
  delivery:
    description: "Food, grocery, and package delivery platforms"
    entities:
      - name: "DoorDash"
        ticker: "DASH"
        data_sources: ["SEC filings", "earnings calls", "driver forums", "Gridwise"]
      - name: "Uber Eats"
        ticker: "UBER"
        data_sources: ["SEC filings (segment)", "earnings calls"]
      - name: "Instacart"
        ticker: "CART"
        data_sources: ["SEC filings", "earnings calls", "shopper forums"]
      - name: "Grubhub"
        parent: "Just Eat Takeaway"
        data_sources: ["Parent company filings", "industry reports"]
      - name: "Amazon Flex"
        parent: "AMZN"
        data_sources: ["Limited — driver forums", "industry estimates"]
    key_metrics: ["active dashers/drivers", "deliveries per hour", "base pay trends", "tip rates"]
    
  freelance:
    description: "Skilled service marketplaces"
    entities:
      - name: "Upwork"
        ticker: "UPWK"
        data_sources: ["SEC filings", "earnings calls", "freelancer forums"]
      - name: "Fiverr"
        ticker: "FVRR"
        data_sources: ["SEC filings", "earnings calls"]
      - name: "Toptal"
        status: "Private"
        data_sources: ["Industry reports", "freelancer forums"]
    key_metrics: ["active freelancers", "GSV per freelancer", "hourly rates", "project fill rates"]
    
  task_based:
    description: "Local task and service marketplaces"
    entities:
      - name: "TaskRabbit"
        parent: "IKEA"
        data_sources: ["Limited — industry reports", "tasker forums"]
      - name: "Thumbtack"
        status: "Private"
        data_sources: ["Industry reports", "funding announcements"]
      - name: "Handy"
        status: "Acquired by Angi"
        data_sources: ["Angi filings (limited)"]
    key_metrics: ["active taskers", "jobs per tasker", "hourly earnings", "platform fees"]
    
  emerging_and_other:
    description: "Other gig platforms and emerging categories"
    entities:
      - name: "Rover" 
        note: "Pet services"
      - name: "Care.com"
        note: "Caregiving services"
      - name: "Wonolo"
        note: "Warehouse/logistics staffing"
      - name: "Instawork"
        note: "Hospitality/event staffing"
      - name: "Shiftsmart"
        note: "Shift-based work marketplace"
    key_metrics: ["Varies by platform — track as encountered"]

### Worker Segments

worker_segments:
  
  full_time_dependent:
    description: "Workers relying on gig work as primary income (30+ hours/week)"
    stress_indicators:
      - "Hours worked increasing while income flat/declining"
      - "Multi-apping (working 2+ platforms simultaneously)"
      - "Vehicle financing stress (high DTI, subprime auto)"
    estimated_population: "~4-5 million workers"
    data_sources: ["BLS Contingent Worker Survey", "platform disclosures", "academic studies"]
    
  supplemental:
    description: "Workers using gig work to supplement other income (<20 hours/week)"
    stress_indicators:
      - "Shift from supplemental to primary (traditional job loss)"
      - "Increasing hours to maintain supplemental income"
    estimated_population: "~10-15 million workers"
    note: "Transition from supplemental to dependent is key stress signal"
    
  churned:
    description: "Workers who have exited gig platforms"
    stress_indicators:
      - "Churn rate acceleration"
      - "Exit surveys/forum sentiment"
      - "Deactivation rates"
    note: "High churn can indicate either healthy alternatives OR platform-forced exits"

### Vehicle/Asset Exposure

vehicle_exposure:
  description: |
    Many gig workers (especially rideshare/delivery) depend on personal vehicles.
    Vehicle financing stress is a direct transmission mechanism to consumer credit stress.
    
  key_relationships:
    - "Subprime auto loans disproportionately held by gig workers"
    - "Vehicle depreciation accelerated by gig use (high mileage)"
    - "Insurance costs elevated for gig use"
    - "Maintenance/repair costs compress net earnings"
    
  vectors_to_watch:
    - "Gig worker auto loan delinquency (if trackable)"
    - "Average vehicle age in gig fleets"
    - "Insurance premium trends for rideshare"

---

## VECTOR REGISTRY (VX)

### Earnings & Compensation Vectors

vectors:
  
  VX-GIG-1.01:
    name: "Rideshare Earnings Per Active Hour"
    domain: "Earnings"
    description: "Average gross earnings per active (online) hour for rideshare drivers"
    unit: "$/hour"
    current_value: "TBD"
    threshold_elevated: "<$20/hour (after expenses, approaches minimum wage)"
    threshold_critical: "<$15/hour"
    tripwire_breached: "<$12/hour (below minimum wage after expenses)"
    trend: "TBD"
    data_sources: ["Gridwise reports", "driver surveys", "academic studies"]
    note: "Gross earnings; net after expenses (gas, maintenance, depreciation) ~40-50% lower"
    
  VX-GIG-1.02:
    name: "Delivery Earnings Per Active Hour"
    domain: "Earnings"
    description: "Average gross earnings per active hour for delivery drivers"
    unit: "$/hour"
    current_value: "TBD"
    threshold_elevated: "<$18/hour"
    threshold_critical: "<$14/hour"
    tripwire_breached: "<$11/hour"
    trend: "TBD"
    data_sources: ["Platform disclosures", "driver forums", "Gridwise"]
    
  VX-GIG-1.03:
    name: "Freelance Platform Hourly Rates"
    domain: "Earnings"
    description: "Median effective hourly rate on major freelance platforms"
    unit: "$/hour"
    current_value: "TBD"
    threshold_elevated: "Rate compression >10% YoY"
    threshold_critical: "Rate compression >20% YoY"
    tripwire_breached: "Rate compression >30% YoY"
    trend: "TBD"
    data_sources: ["Upwork/Fiverr earnings reports", "freelancer surveys"]
    
  VX-GIG-1.04:
    name: "Incentive/Bonus Spend (Platform)"
    domain: "Earnings"
    description: "Platform spending on driver/worker incentives and bonuses"
    unit: "% of gross bookings"
    current_value: "TBD"
    interpretation: |
      HIGH incentive spend = worker undersupply (bullish for workers)
      LOW/declining incentive spend = worker oversupply (bearish for workers)
    threshold_elevated: "Incentive spend declining >20% YoY"
    threshold_critical: "Incentive spend declining >40% YoY"
    tripwire_breached: "Incentives effectively eliminated"
    trend: "TBD"
    data_sources: ["Platform earnings calls", "SEC filings"]

### Supply & Saturation Vectors

  VX-GIG-2.01:
    name: "Active Driver/Worker Count"
    domain: "Supply"
    description: "Total active workers across major platforms"
    unit: "Millions of workers"
    current_value: "TBD"
    interpretation: |
      Rising active count + flat/declining earnings = SATURATION
      Rising active count + rising earnings = HEALTHY GROWTH
      Declining active count + rising earnings = EQUILIBRIUM
      Declining active count + declining earnings = PLATFORM DISTRESS
    threshold_elevated: "Active count rising while earnings flat"
    threshold_critical: "Active count rising while earnings declining"
    tripwire_breached: "Active count up >20% YoY with earnings down >10% YoY"
    trend: "TBD"
    data_sources: ["Platform disclosures", "SEC filings"]
    
  VX-GIG-2.02:
    name: "Multi-Apping Rate"
    domain: "Supply"
    description: "Percentage of gig workers active on 2+ platforms simultaneously"
    unit: "%"
    current_value: "TBD"
    interpretation: |
      High/rising multi-apping = workers need multiple platforms to earn enough
      This is a STRESS indicator, not efficiency
    threshold_elevated: ">50% of full-time workers multi-apping"
    threshold_critical: ">65% of full-time workers multi-apping"
    tripwire_breached: ">75% of full-time workers multi-apping"
    trend: "TBD"
    data_sources: ["Gridwise", "driver surveys", "academic studies"]
    
  VX-GIG-2.03:
    name: "Hours to Target Income"
    domain: "Supply"
    description: "Average weekly hours required to earn $1,000 gross"
    unit: "Hours/week"
    current_value: "TBD"
    interpretation: |
      Rising hours for same income = compression
      Direct measure of worker time-poverty
    threshold_elevated: ">45 hours/week for $1,000"
    threshold_critical: ">55 hours/week for $1,000"
    tripwire_breached: ">65 hours/week for $1,000 (unsustainable)"
    trend: "TBD"
    data_sources: ["Driver surveys", "Gridwise", "academic studies"]
    
  VX-GIG-2.04:
    name: "New Driver Acquisition Cost"
    domain: "Supply"
    description: "Platform cost to acquire and onboard a new driver"
    unit: "$/driver"
    current_value: "TBD"
    interpretation: |
      HIGH acquisition cost = undersupply (platforms competing for workers)
      LOW acquisition cost = oversupply (workers competing for platforms)
    threshold_elevated: "Acquisition cost declining >30% YoY"
    threshold_critical: "Acquisition cost approaching zero (organic supply)"
    tripwire_breached: "Platforms implementing waitlists/caps (extreme oversupply)"
    trend: "TBD"
    data_sources: ["Platform earnings calls", "industry analysis"]

  VX-GIG-2.05:
    name: "Platform Deactivation Rate"
    domain: "Supply"
    description: "Rate at which platforms deactivate (terminate) workers"
    unit: "% of active workers deactivated per quarter"
    current_value: "TBD"
    interpretation: |
      LOW deactivation = platforms need workers (undersupply)
      HIGH deactivation = platforms culling excess supply OR quality issues
      RISING deactivation + FALLING earnings = Platform Rationalization in progress
      RISING deactivation + STABLE earnings = healthy quality management
    threshold_elevated: "Deactivation rate >5% quarterly"
    threshold_critical: "Deactivation rate >10% quarterly"
    tripwire_breached: "Deactivation rate >15% quarterly OR mass deactivation events"
    trend: "TBD"
    data_sources: ["Platform disclosures (rare)", "driver forums", "news coverage", "litigation filings"]
    note: "Key indicator for Platform Rationalization hypothesis — if platforms reduce supply via deactivation, earnings may stabilize but creates unemployment"
    cross_reference: "FLOW-GIG-03 (Platform Rationalization Cascade)"

### Financial Stress Vectors

  VX-GIG-3.01:
    name: "Gig Worker Auto Loan Delinquency"
    domain: "Financial Stress"
    description: "Delinquency rate on auto loans held by identified gig workers"
    unit: "%"
    current_value: "TBD — may need proxy"
    interpretation: |
      Gig workers disproportionately hold subprime auto loans
      Vehicle is both tool and liability — delinquency = cascade risk
    threshold_elevated: ">8% 60+ day delinquency"
    threshold_critical: ">12% 60+ day delinquency"
    tripwire_breached: ">15% 60+ day delinquency"
    trend: "TBD"
    data_sources: ["Limited — may need subprime auto as proxy", "academic studies"]
    note: "Direct gig worker data rare; may use subprime auto 60+ DQ as correlated proxy"
    cross_reference: "VX-CARL-1.04 (Subprime Auto 60+ DQ)"
    
  VX-GIG-3.02:
    name: "Gig-to-Traditional Employment Flow"
    domain: "Financial Stress"
    description: "Net flow of workers between gig and traditional employment"
    unit: "Net flow direction and magnitude"
    current_value: "TBD"
    interpretation: |
      Net flow INTO gig = traditional employment distress (workers fleeing to gig)
      Net flow OUT OF gig = healthy labor market (workers finding better options)
    threshold_elevated: "Sustained net inflow to gig work"
    threshold_critical: "Accelerating net inflow + declining gig earnings"
    tripwire_breached: "Simultaneous gig inflow AND gig earnings collapse"
    trend: "TBD"
    data_sources: ["BLS data", "platform disclosures", "academic studies"]
    
  VX-GIG-3.03:
    name: "Platform Worker Sentiment"
    domain: "Financial Stress"
    description: "Aggregate sentiment from gig worker forums and surveys"
    unit: "Qualitative scale: POSITIVE | NEUTRAL | NEGATIVE | DISTRESSED"
    current_value: "TBD"
    interpretation: |
      Leading indicator — sentiment deteriorates before hard data
      Forums capture lived experience not in official statistics
    threshold_elevated: "NEGATIVE"
    threshold_critical: "DISTRESSED"
    tripwire_breached: "DISTRESSED + organized labor action/strikes"
    trend: "TBD"
    data_sources: ["r/uberdrivers", "r/doordash_drivers", "Gridwise forums", "driver Facebook groups"]

### Platform Health Vectors

  VX-GIG-4.01:
    name: "Platform Take Rate Trends"
    domain: "Platform Health"
    description: "Platform commission as percentage of gross transaction value"
    unit: "%"
    current_value: "TBD"
    interpretation: |
      RISING take rate = platforms extracting more from workers (bearish for workers)
      Often disguised through fee restructuring
    threshold_elevated: "Take rate increase >2 percentage points YoY"
    threshold_critical: "Take rate increase >5 percentage points YoY"
    tripwire_breached: "Take rate exceeds 30% (delivery) or 35% (rideshare)"
    trend: "TBD"
    data_sources: ["Platform earnings", "driver earnings screenshots", "fee analysis"]
    
  VX-GIG-4.02:
    name: "Platform Profitability Pressure"
    domain: "Platform Health"
    description: "Platform progress toward profitability and investor pressure"
    unit: "Qualitative assessment"
    current_value: "TBD"
    interpretation: |
      Unprofitable platforms under investor pressure will cut worker pay
      Path to profitability = extract more from workers/customers
    threshold_elevated: "Explicit profitability mandates in earnings calls"
    threshold_critical: "Active cost-cutting targeting worker compensation"
    tripwire_breached: "Platform viability concerns (bankruptcy risk)"
    trend: "TBD"
    data_sources: ["Earnings calls", "analyst reports", "news coverage"]

---

## FLOW CASCADES

### FLOW-GIG-01: Saturation Doom Loop

flow_cascades:

  FLOW-GIG-01:
    name: "Saturation Doom Loop"
    pathway: |
      Traditional employment stress → 
      Workers flee TO gig economy → 
      Gig worker oversupply → 
      Per-worker earnings decline → 
      Hours increase for same income → 
      Worker financial stress → 
      Auto loan delinquency / expense cutting → 
      Further economic contraction → 
      More traditional employment stress
      
    mechanism: |
      This is a reinforcing feedback loop. As traditional employment deteriorates,
      workers enter gig economy as perceived safety valve. But gig economy cannot
      absorb unlimited supply — saturation compresses earnings for ALL gig workers.
      This converts what workers thought was escape into another trap.
      
    breakpoint: "Gig earnings fall below subsistence level for full-time workers"
    lag_time: "3-6 months from traditional employment shock to gig saturation"
    status: "MONITORING"
    cross_domain: ["CARL (consumer stress)", "Employment indicators"]

### FLOW-GIG-02: Vehicle Asset Cascade

  FLOW-GIG-02:
    name: "Vehicle Asset Cascade"
    pathway: |
      Gig earnings decline → 
      Deferred vehicle maintenance → 
      Accelerated depreciation from high mileage → 
      Underwater on auto loan → 
      Miss payments OR exit gig (can't work without car) → 
      Auto loan default OR income loss → 
      Consumer credit deterioration
      
    mechanism: |
      Rideshare/delivery workers' vehicles are both productive asset and liability.
      High-mileage gig use accelerates depreciation faster than loan paydown.
      Many workers become underwater on auto loans. This creates binary choice:
      continue working with deteriorating asset, or exit and lose income entirely.
      
    breakpoint: "Widespread negative equity in gig worker vehicles"
    lag_time: "12-18 months from earnings compression to vehicle stress"
    status: "MONITORING"
    cross_domain: ["CARL (subprime auto)", "Consumer credit"]

### FLOW-GIG-03: Platform Rationalization Cascade

  FLOW-GIG-03:
    name: "Platform Rationalization Cascade"
    pathway: |
      Platform profitability pressure → 
      Reduce incentives / raise take rates → 
      Worker earnings decline → 
      Best workers exit (adverse selection) → 
      Service quality declines → 
      Customer demand declines → 
      Further platform pressure → 
      More worker cuts OR platform failure
      
    mechanism: |
      Investor pressure forces platforms to path toward profitability.
      Primary lever is extracting more from workers. But this triggers
      adverse selection — best workers with alternatives leave first.
      Service quality declines, customers defect, revenue pressure increases.
      
    breakpoint: "Platform enters death spiral (quality/demand decline)"
    lag_time: "6-12 months from profitability pivot to quality deterioration"
    status: "MONITORING"
    cross_domain: ["Platform equity values", "Consumer spending"]

### FLOW-GIG-04: Gig-to-CARL Transmission

  FLOW-GIG-04:
    name: "Gig-to-CARL Transmission"
    pathway: |
      Gig worker financial stress → 
      Consumer spending contraction (gig workers cut discretionary) → 
      Credit utilization increase (workers bridge with cards) → 
      Auto loan stress (vehicle-dependent workers) → 
      Broader consumer credit deterioration → 
      CARL consumer stress indicators trigger
      
    mechanism: |
      Gig workers are ~5-10% of labor force but are leading indicator.
      Their stress transmits through: 
      1) Direct spending reduction
      2) Credit utilization as bridge financing
      3) Auto loan stress (disproportionate subprime exposure)
      4) Sentiment contagion to broader consumer confidence
      
    breakpoint: "Gig worker stress becomes visible in CARL credit metrics"
    lag_time: "3-6 months from gig stress to CARL vector movements"
    status: "MONITORING"
    cross_domain: ["CARL (all vectors)"]

---

## DATA SOURCES

### Primary Sources

data_sources:

  platform_filings:
    description: "SEC filings and earnings calls from public platforms"
    entities: ["UBER", "LYFT", "DASH", "CART", "UPWK", "FVRR"]
    frequency: "Quarterly"
    reliability: "HIGH — audited financials"
    limitations: "Platforms may obscure unfavorable worker metrics"
    
  gridwise:
    description: "Gig worker earnings tracking app and reports"
    url: "gridwise.io"
    frequency: "Monthly reports, real-time app data"
    reliability: "MEDIUM-HIGH — self-reported but large sample"
    limitations: "Selection bias toward engaged/tracking workers"
    
  driver_forums:
    description: "Reddit, Facebook groups, and forums for gig workers"
    entities: 
      - "r/uberdrivers"
      - "r/lyftdrivers"
      - "r/doordash_drivers"
      - "r/InstacartShoppers"
      - "r/UberEats"
      - "Uberpeople.net forums"
    frequency: "Real-time"
    reliability: "LOW-MEDIUM — anecdotal but captures sentiment"
    limitations: "Selection bias, complaints overrepresented"
    use_case: "Sentiment analysis, early warning signals, qualitative color"
    
  bls_data:
    description: "Bureau of Labor Statistics contingent worker surveys"
    frequency: "Irregular (every few years)"
    reliability: "HIGH — methodologically rigorous"
    limitations: "Infrequent, lags current conditions significantly"
    
  academic_studies:
    description: "Peer-reviewed research on gig economy"
    sources: ["NBER", "Economic Policy Institute", "UC Berkeley Labor Center"]
    frequency: "Irregular"
    reliability: "HIGH — rigorous methodology"
    limitations: "Significant publication lag"
    
  industry_reports:
    description: "Reports from consulting firms and industry analysts"
    sources: ["McKinsey", "Deloitte", "Edison Research", "MBO Partners"]
    frequency: "Annual or ad-hoc"
    reliability: "MEDIUM — may have sponsor bias"
    
  news_coverage:
    description: "Journalism covering gig economy trends"
    sources: ["NYT", "WSJ", "Bloomberg", "The Verge", "rest-of-world.org"]
    frequency: "Ongoing"
    reliability: "MEDIUM — variable quality, useful for leads"

### Data Gaps

data_gaps:
  - description: "Gig worker credit profiles (auto loans, credit cards)"
    workaround: "Use subprime auto as correlated proxy"
  - description: "True multi-apping rates across platforms"
    workaround: "Rely on Gridwise estimates and surveys"
  - description: "Net gig-to-traditional employment flows"
    workaround: "Infer from platform active user counts + BLS data"
  - description: "Private platform data (Amazon Flex, TaskRabbit)"
    workaround: "Forum sentiment, industry estimates"

---

## GLOSSARY

glossary:

  terms:
    
    active_worker:
      definition: "Worker who completed at least one gig in the measurement period (usually month/quarter)"
      note: "Platforms define 'active' differently — watch for definitional changes"
      
    take_rate:
      definition: "Platform commission as percentage of gross transaction value"
      example: "If customer pays $20 for delivery and driver receives $14, take rate is 30%"
      
    multi_apping:
      definition: "Working for 2+ gig platforms simultaneously or in the same time period"
      significance: "Indicator of earnings insufficiency from single platform"
      
    deadhead:
      definition: "Time/miles spent without a paying passenger or delivery"
      significance: "Uncompensated time that reduces effective hourly rate"
      
    surge_pricing:
      definition: "Dynamic pricing that increases fares during high-demand periods"
      note: "Increasingly rare as platforms prioritize predictability"
      
    incentive_bonus:
      definition: "Extra payments from platforms to encourage work during certain times/conditions"
      significance: "Declining incentives = worker oversupply"
      
    deactivation:
      definition: "Platform termination of a worker's ability to work"
      causes: ["Low ratings", "Safety incidents", "Fraud", "Oversupply management"]
      
    upfront_pricing:
      definition: "Showing workers the full pay before accepting a gig"
      note: "Lack of upfront pricing associated with worker exploitation"
      
    gig_dependent:
      definition: "Worker relying on gig income as primary (>50%) source"
      contrast: "Gig supplemental — using gig as secondary income"
      
    saturation:
      definition: "Market state where worker supply exceeds demand, compressing earnings"
      indicators: ["Declining per-worker earnings", "Rising wait times between jobs", "Reduced incentives"]
      
    platform_rationalization:
      definition: "Platform cost-cutting measures to achieve profitability"
      typical_actions: ["Raise take rates", "Cut incentives", "Reduce support staff", "Deactivate underperformers"]

  acronyms:
    GSV: "Gross Services Value — total transaction value before platform take"
    DAU: "Daily Active Users"
    MAU: "Monthly Active Users"
    PMAU: "Paying Monthly Active Users"
    AOV: "Average Order Value"
    LTV: "Lifetime Value (of customer or worker)"
    CAC: "Customer Acquisition Cost"
    WAC: "Worker Acquisition Cost"
    IC: "Independent Contractor"

---

## REPORTING RELATIONSHIP

### GIG → CARL State Vector

reporting:
  
  parent_agent: "CARL"
  reporting_frequency: "As significant developments occur; minimum monthly"
  
  state_vector_focus:
    primary_signal: "Consumer income fragility from gig economy"
    secondary_signals:
      - "Leading indicator of traditional employment stress"
      - "Vehicle/auto loan exposure"
      - "Sentiment deterioration"
    
  key_questions_from_carl:
    - "Is gig economy absorbing displaced workers or creating more distress?"
    - "What is transmission lag from gig stress to consumer credit metrics?"
    - "Are platform dynamics compressing worker earnings systemically?"
    
  escalation_criteria:
    - "Any vector moves to BREACHED status"
    - "Multiple vectors move to CRITICAL simultaneously"
    - "New cascade pathway identified"
    - "Evidence of thesis invalidation"

---

## SESSION QUICK REFERENCE

### For Update Sessions
Focus on: VX-GIG-1.xx (Earnings vectors), VX-GIG-2.xx (Supply vectors)
Key question: "Are earnings and supply moving in concerning directions?"

### For Analysis Sessions
Focus on: FLOW cascades, cross-references to CARL vectors
Key question: "What mechanisms are driving observed changes?"

### For Reconciliation Sessions
Focus on: Cross-reference integrity, FL retirement, data source verification
Key question: "Is our data consistent and current?"

### For State Vector Reports
Include: Highest-concern vectors, key FLOW activations, recommended action for CARL
Format: Per GIG_METHODOLOGY_SKELETON §6.2

---

# END OF SKELETON

# Maintenance Notes:
# - Update vector current_values as data arrives
# - Add new platforms to entity registry as discovered
# - Refine thresholds based on operational experience
# - Version increment for structural changes
