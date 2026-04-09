# NICK DOMAIN SKELETON

# Purpose: Structural scaffold for NICK agent operations
# Domain:  Shadow Credit, Non-Bank Lending, Alternative Credit Stress
# Agent:   NICK (Shadow Credit Monitor)
#
# Version: 1.0
# Created: 2026-01-20
# Author:  Initial Architecture Session
#
# Usage:
#   - Load this file at the start of any NICK session
#   - Provides vocabulary, entities, vectors, and thresholds for shadow credit monitoring
#   - Companion to NICK_METHODOLOGY_SKELETON which governs process
#   - This skeleton governs the CONTENT of NICK's domain
#
# Reporting: NICK reports to CARL via State Vectors
# Signal:    Hidden consumer leverage and stress invisible to traditional metrics
#            "The debt you can't see"

---

## METADATA

metadata:
  name: "NICK Domain Skeleton"
  domain: "Shadow Credit, Non-Bank Lending, Alternative Credit Signals"
  version: "1.0"
  created: "2026-01-20"
  parent_agent: "CARL"
  
  phase_model: |
    Phase 0 (Pre-Monitoring) → Phase 1 (Supplement) → Phase 2 (Bridge) → Phase 3 (Dependence) → Phase 4 (Collapse)

    Pre-Monitoring: System initialized, baseline data being collected (current phase)
    Supplement: Shadow credit used occasionally for convenience (healthy BNPL, rare payday)
    Bridge: Shadow credit increasingly used to bridge cash flow gaps (stress building)
    Dependence: Shadow credit becomes essential liquidity source (traditional credit exhausted)
    Collapse: Shadow credit capacity exhausted, defaults cascade to visible credit
    
  core_thesis:
    name: "Shadow Credit Thesis"
    statement: |
      Traditional consumer credit metrics systematically understate true consumer leverage.
      Shadow credit (BNPL, payday, fintech, cash advance apps) represents HIDDEN DEBT that:
      
      1. Does not appear on credit reports (or appears with delay)
      2. Is not captured in Fed consumer credit data
      3. Allows consumers to appear stable while actually distressed
      
      Shadow credit is the BRIDGE between apparent stability and visible default. Consumers
      exhaust shadow credit BEFORE defaulting on traditional obligations. Therefore:
      
      - Rising shadow credit usage is a LEADING indicator of traditional credit stress
      - Shadow lender distress (fintech failures) reveals hidden consumer deterioration
      - BNPL stacking and payday rollovers signal liquidity exhaustion
      
      When shadow credit capacity is exhausted, stress becomes visible—but by then,
      the deterioration is already advanced.
      
    confidence: "75% — CFPB stacking data (63%) and cockroach pattern (3 failures) validate thesis; Affirm resilience suggests possible segment bifurcation"
    
    invalidation_criteria:
      - "BNPL delinquency rates decline while usage grows (healthy expansion)"
      - "Payday loan volumes decline without regulatory cause (reduced need)"
      - "Fintech lenders report improving credit quality across portfolios"
      - "Shadow credit usage declines as traditional credit access improves"
    
    competing_hypotheses:
      - name: "Financial Innovation"
        statement: "Shadow credit represents healthy innovation providing consumer flexibility, not stress"
        current_assessment: "Partially valid for prime consumers; less valid for subprime/stressed"
      - name: "Substitution Effect"
        statement: "Shadow credit replaces rather than supplements traditional debt"
        current_assessment: "Limited evidence — most research shows additive, not substitutive"

---

## ENTITY DEFINITIONS

### Buy Now Pay Later (BNPL)

bnpl_entities:
  
  major_providers:
    - name: "Affirm"
      ticker: "AFRM"
      model: "Installment loans at POS; longer terms available"
      data_sources: ["SEC filings", "earnings calls", "ABS data"]
      key_metrics: ["GMV", "delinquency rates", "allowance for losses", "active consumers"]
      
    - name: "Klarna"
      status: "Private (IPO expected)"
      model: "Pay-in-4, financing options"
      data_sources: ["Press releases", "funding announcements", "European filings"]
      key_metrics: ["GMV", "credit losses", "consumer base"]
      
    - name: "Afterpay (Block)"
      ticker: "SQ"
      model: "Pay-in-4, integrated with Cash App"
      data_sources: ["Block SEC filings (segment)", "earnings calls"]
      key_metrics: ["GMV", "loss rates", "active users"]
      
    - name: "PayPal Pay Later"
      ticker: "PYPL"
      model: "Pay-in-4 and Pay Monthly"
      data_sources: ["SEC filings", "earnings calls"]
      key_metrics: ["Originations", "loss rates"]
      
    - name: "Apple Pay Later"
      ticker: "AAPL"
      model: "Pay-in-4, Apple-financed"
      data_sources: ["Limited — Apple disclosures minimal"]
      status: "DISCONTINUED (2024)"
      note: "Launched 2023, discontinued 2024. Apple partnered with Affirm instead. No longer a direct monitoring target."

  key_metrics_definitions:
    gmv: "Gross Merchandise Value — total value of transactions"
    delinquency_rate: "% of balances past due (varies by provider definition)"
    loss_rate: "Net charge-offs as % of originations"
    stacking: "Consumer using multiple BNPL plans simultaneously"

### Payday and Short-Term Lending

payday_entities:
  
  major_players:
    - name: "CURO Group"
      ticker: "CURO"
      status: "Filed Chapter 11 (2024)"
      significance: "Major payday/installment lender failure — cockroach signal"
      
    - name: "Enova International"
      ticker: "ENVA"
      model: "Online payday and installment loans"
      data_sources: ["SEC filings", "earnings calls"]
      
    - name: "Elevate Credit"
      status: "Acquired"
      model: "Online installment lending"
      
    - name: "OppFi"
      ticker: "OPFI"
      model: "Near-prime installment lending"
      data_sources: ["SEC filings", "earnings calls"]
      
    - name: "QC Holdings / Check Into Cash"
      status: "Private"
      model: "Storefront payday"
      data_sources: ["Limited — industry reports"]
      
  industry_bodies:
    - name: "Community Financial Services Association (CFSA)"
      function: "Payday industry trade group"
      data: "Occasional industry statistics"

### Fintech Consumer Lenders

fintech_entities:
  
  personal_loan_fintechs:
    - name: "Upstart"
      ticker: "UPST"
      model: "AI-underwritten personal loans via bank partners"
      data_sources: ["SEC filings", "earnings calls"]
      key_metrics: ["Originations", "conversion rates", "delinquency", "bank partner status"]
      significance: "Bellwether for fintech lending health"
      
    - name: "LendingClub"
      ticker: "LC"
      model: "Personal loans, now a bank"
      data_sources: ["SEC filings", "call reports"]
      
    - name: "SoFi"
      ticker: "SOFI"
      model: "Personal loans, student refi, now a bank"
      data_sources: ["SEC filings", "earnings calls"]
      
    - name: "Prosper"
      status: "Private"
      model: "Marketplace personal loans"
      data_sources: ["ABS data", "occasional disclosures"]
      
    - name: "Avant"
      status: "Private"
      model: "Near-prime personal loans"
      data_sources: ["ABS data"]
      
    - name: "Best Egg (Marlette)"
      status: "Private"
      model: "Personal loans"
      data_sources: ["ABS data"]

  failure_watch_list:
    note: "Track for cockroach thesis validation"
    signals:
      - "Funding cost spikes"
      - "Bank partner withdrawals"
      - "Underwriting tightening"
      - "Headcount reductions"
      - "Going concern warnings"

### Cash Advance Apps (Earned Wage Access)

cash_advance_entities:
  
  providers:
    - name: "Dave"
      ticker: "DAVE"
      model: "Cash advances against upcoming paycheck, tips-based"
      data_sources: ["SEC filings", "earnings calls"]
      key_metrics: ["ExtraCash advances", "advance volume", "user growth"]
      
    - name: "Earnin"
      status: "Private"
      model: "Earned wage access, tips-based"
      data_sources: ["Limited — funding announcements"]
      
    - name: "MoneyLion"
      ticker: "ML"
      model: "Cash advances, banking, investing"
      data_sources: ["SEC filings", "earnings calls"]
      
    - name: "Brigit"
      status: "Private"
      model: "Cash advances, budgeting tools"
      
    - name: "Branch"
      status: "Private"
      model: "Employer-integrated earned wage access"
      
    - name: "DailyPay"
      status: "Private"
      model: "Employer-integrated on-demand pay"
      
    - name: "Payactiv"
      status: "Private"
      model: "Employer-integrated earned wage access"

  regulatory_note: |
    Earned wage access exists in regulatory gray area. CFPB considering rules.
    If classified as credit, could face significant constraints.

### Other Alternative Credit

other_entities:
  
  pawn:
    - name: "FirstCash Holdings"
      ticker: "FCFS"
      model: "Pawn shops, retail"
      data_sources: ["SEC filings", "earnings calls"]
      significance: "Pawn volume is distress indicator"
      
    - name: "EZCORP"
      ticker: "EZPW"
      model: "Pawn shops"
      data_sources: ["SEC filings"]
      
  title_loans:
    - name: "TitleMax (TMX Finance)"
      status: "Private"
      model: "Auto title loans"
      data_sources: ["Limited"]
      significance: "Title loans = severe distress (risking vehicle)"
      
  rent_to_own:
    - name: "Rent-A-Center"
      ticker: "RCII"
      model: "Rent-to-own furniture, electronics"
      data_sources: ["SEC filings"]
      
    - name: "Aaron's (Upbound Group)"
      ticker: "UPBD"
      model: "Lease-to-own"
      data_sources: ["SEC filings"]

---

## VECTOR REGISTRY (VX)

### BNPL Vectors

vectors:

  VX-NICK-1.01:
    name: "BNPL Aggregate Delinquency Rate"
    domain: "BNPL"
    description: "Weighted average delinquency rate across major BNPL providers"
    unit: "%"
    current_value: "TBD"
    threshold_elevated: ">4% 30+ day delinquency"
    threshold_critical: ">6% 30+ day delinquency"
    tripwire_breached: ">8% 30+ day delinquency"
    trend: "TBD"
    data_sources: ["Affirm SEC filings", "CFPB reports", "ABS data"]
    note: "Definitions vary by provider; normalize where possible"
    
  VX-NICK-1.02:
    name: "BNPL Stacking Prevalence"
    domain: "BNPL"
    description: "Percentage of BNPL users with 2+ simultaneous active plans"
    unit: "%"
    current_value: "TBD"
    interpretation: |
      Stacking indicates BNPL is being used as credit line, not convenience.
      High stacking = hidden leverage, liquidity stress.
    threshold_elevated: ">25% of users stacking"
    threshold_critical: ">35% of users stacking"
    tripwire_breached: ">45% of users stacking"
    trend: "TBD"
    data_sources: ["CFPB reports", "credit bureau studies", "academic research"]
    
  VX-NICK-1.03:
    name: "BNPL Late Fee Revenue Trend"
    domain: "BNPL"
    description: "Growth rate of late fee revenue at major BNPL providers"
    unit: "% YoY growth"
    current_value: "TBD"
    interpretation: |
      Rising late fee revenue = more consumers missing payments.
      Providers profit from distress — watch for acceleration.
    threshold_elevated: ">20% YoY late fee growth"
    threshold_critical: ">40% YoY late fee growth"
    tripwire_breached: ">60% YoY late fee growth"
    trend: "TBD"
    data_sources: ["Provider earnings reports", "SEC filings"]
    
  VX-NICK-1.04:
    name: "BNPL Merchant Pullback"
    domain: "BNPL"
    description: "Evidence of merchants reducing or eliminating BNPL options"
    unit: "Qualitative"
    current_value: "TBD"
    interpretation: |
      Merchants pull BNPL when: costs outweigh benefits, brand risk, or
      consumer defaults create chargebacks. Pullback = stress signal.
    threshold_elevated: "Isolated merchant exits"
    threshold_critical: "Major retailer exits or category-wide reduction"
    tripwire_breached: "Systematic merchant retreat from BNPL"
    trend: "TBD"
    data_sources: ["News coverage", "merchant announcements", "provider commentary"]

### Payday/Short-Term Vectors

  VX-NICK-2.01:
    name: "Payday Loan Volume Index"
    domain: "Payday"
    description: "Indexed measure of payday loan origination volume"
    unit: "Index (100 = baseline)"
    current_value: "TBD"
    interpretation: |
      Rising volume = more consumers needing liquidity of last resort.
      EXCEPT: volume may drop due to regulation, not reduced need.
    threshold_elevated: "Index >115 (15% above baseline)"
    threshold_critical: "Index >130 (30% above baseline)"
    tripwire_breached: "Index >150 OR sharp regulatory-unrelated spike"
    trend: "TBD"
    data_sources: ["Pew Research", "state regulator data", "industry reports"]
    note: "Must distinguish demand-driven vs regulatory-driven changes"
    
  VX-NICK-2.02:
    name: "Payday Rollover/Renewal Rate"
    domain: "Payday"
    description: "Percentage of payday loans rolled over or immediately renewed"
    unit: "%"
    current_value: "TBD"
    interpretation: |
      Rollover = borrower couldn't repay, took new loan to cover old.
      High rollover = debt trap, severe liquidity stress.
    threshold_elevated: ">60% rollover rate"
    threshold_critical: ">70% rollover rate"
    tripwire_breached: ">80% rollover rate"
    trend: "TBD"
    data_sources: ["CFPB studies", "state regulator reports", "academic research"]
    
  VX-NICK-2.03:
    name: "Payday Lender Financial Health"
    domain: "Payday"
    description: "Composite assessment of public payday lender financial stability"
    unit: "Qualitative"
    current_value: "TBD"
    interpretation: |
      Payday lender distress = either regulatory pressure OR consumer
      credit quality deterioration. Distinguish cause.
    threshold_elevated: "Multiple lenders report margin compression"
    threshold_critical: "Lender announces restructuring or going concern"
    tripwire_breached: "Major lender failure (CURO-level event)"
    trend: "TBD"
    data_sources: ["SEC filings", "news coverage", "credit ratings"]
    historical: "CURO Chapter 11 (2024) — significant cockroach event"

### Fintech Lending Vectors

  VX-NICK-3.01:
    name: "Fintech Personal Loan Delinquency"
    domain: "Fintech"
    description: "Average delinquency rate across major fintech personal loan originators"
    unit: "%"
    current_value: "TBD"
    threshold_elevated: ">6% 30+ day delinquency"
    threshold_critical: ">9% 30+ day delinquency"
    tripwire_breached: ">12% 30+ day delinquency"
    trend: "TBD"
    data_sources: ["Upstart/LC filings", "ABS performance data", "Kroll/Fitch reports"]
    
  VX-NICK-3.02:
    name: "Fintech Credit Tightening Index"
    domain: "Fintech"
    description: "Composite measure of fintech underwriting standard changes"
    unit: "Qualitative scale"
    current_value: "TBD"
    interpretation: |
      Tightening = fintechs seeing stress, reducing risk.
      LEADING indicator — they see problems before defaults peak.
    threshold_elevated: "Multiple fintechs report tightening"
    threshold_critical: "Industry-wide tightening, approval rates dropping >20%"
    tripwire_breached: "Fintechs exiting segments or pausing originations"
    trend: "TBD"
    data_sources: ["Earnings calls", "SEC filings", "analyst reports"]
    
  VX-NICK-3.03:
    name: "Fintech Funding Stress"
    domain: "Fintech"
    description: "Evidence of funding cost increases or capital market access problems"
    unit: "Qualitative"
    current_value: "TBD"
    interpretation: |
      Fintechs depend on warehouse lines and ABS markets.
      Funding stress = either macro conditions OR portfolio concerns.
    threshold_elevated: "Spreads widening on fintech ABS"
    threshold_critical: "Bank partner withdrawals or warehouse line reductions"
    tripwire_breached: "Fintech unable to fund originations"
    trend: "TBD"
    data_sources: ["ABS spreads", "SEC filings", "news coverage"]
    
  VX-NICK-3.04:
    name: "Fintech Lender Failure Watch"
    domain: "Fintech"
    description: "Count and significance of fintech lender failures or severe distress"
    unit: "Count + Qualitative"
    current_value: "TBD"
    interpretation: |
      Cockroach thesis: visible failures indicate hidden problems.
      One failure = possible idiosyncratic. Multiple = systemic.
    threshold_elevated: "1 significant failure"
    threshold_critical: "2-3 failures OR 1 major player"
    tripwire_breached: "Widespread failures, funding market freeze"
    trend: "TBD"
    data_sources: ["News coverage", "SEC filings", "bankruptcy filings"]
    cross_reference: "CARL cockroach thesis (subprime auto)"

### Cash Advance / EWA Vectors

  VX-NICK-4.01:
    name: "Cash Advance App Usage Volume"
    domain: "Cash Advance"
    description: "Aggregate volume of cash advances from major apps (Dave, Earnin, etc.)"
    unit: "Index or $ billions"
    current_value: "TBD"
    interpretation: |
      Rising usage = more consumers can't make it to payday.
      Frequency matters: occasional use vs every pay period.
    threshold_elevated: "Volume up >30% YoY"
    threshold_critical: "Volume up >50% YoY"
    tripwire_breached: "Volume up >75% YoY OR frequency indicating dependence"
    trend: "TBD"
    data_sources: ["Dave SEC filings", "MoneyLion filings", "industry estimates"]
    
  VX-NICK-4.02:
    name: "Earned Wage Access Repeat Usage"
    domain: "Cash Advance"
    description: "Percentage of EWA users accessing advances every pay period"
    unit: "%"
    current_value: "TBD"
    interpretation: |
      Repeat usage every cycle = structural cash flow deficit.
      Not occasional smoothing — chronic shortfall.
    threshold_elevated: ">40% of users repeat every period"
    threshold_critical: ">55% of users repeat every period"
    tripwire_breached: ">70% of users repeat every period"
    trend: "TBD"
    data_sources: ["Provider disclosures", "CFPB research", "academic studies"]

### Alternative Credit Vectors

  VX-NICK-5.01:
    name: "Pawn Transaction Volume"
    domain: "Alternative"
    description: "Pawn loan origination volume at major chains"
    unit: "Index or $ millions"
    current_value: "TBD"
    interpretation: |
      Pawn = distress indicator. Consumers liquidating/pledging assets.
      Rising pawn volume = consumers exhausting other options.
    threshold_elevated: "Volume up >15% YoY"
    threshold_critical: "Volume up >25% YoY"
    tripwire_breached: "Volume up >40% YoY"
    trend: "TBD"
    data_sources: ["FirstCash/EZCORP SEC filings"]
    
  VX-NICK-5.02:
    name: "Title Loan Activity"
    domain: "Alternative"
    description: "Auto title loan origination trends"
    unit: "Qualitative + directional"
    current_value: "TBD"
    interpretation: |
      Title loans = SEVERE distress. Consumer risking vehicle (often
      essential for work). Rising title loan activity is serious signal.
    threshold_elevated: "Industry reports rising volume"
    threshold_critical: "Significant volume increase + rising defaults"
    tripwire_breached: "Title loan surge + vehicle repossession wave"
    trend: "TBD"
    data_sources: ["Limited — industry reports", "state data", "news coverage"]
    cross_reference: "GIG vehicle exposure (gig workers use title loans)"

---

## FLOW CASCADES

### FLOW-NICK-01: Shadow to Visible Credit Transmission

flow_cascades:

  FLOW-NICK-01:
    name: "Shadow to Visible Credit Transmission"
    pathway: |
      Consumer exhausts traditional credit headroom →
      Turns to shadow credit (BNPL, payday, cash advance) →
      Shadow credit obligations accumulate (invisible) →
      Cash flow further constrained by shadow payments →
      Eventually defaults on EITHER shadow OR traditional →
      If shadow default: collections, but limited credit report impact →
      If traditional default: credit score damage, cascading defaults
      
    mechanism: |
      Shadow credit extends the apparent runway for stressed consumers.
      But it doesn't solve the underlying cash flow problem — it delays
      and often worsens the eventual reckoning. Traditional credit metrics
      look stable while shadow leverage builds. Then sudden visible deterioration.
      
    breakpoint: "Shadow credit capacity exhausted; consumer must choose what to default on"
    lag_time: "6-12 months from shadow credit dependence to visible default"
    status: "MONITORING"
    cross_domain: ["CARL (consumer credit)", "Traditional credit metrics"]

### FLOW-NICK-02: BNPL Stacking Cascade

  FLOW-NICK-02:
    name: "BNPL Stacking Cascade"
    pathway: |
      Consumer uses BNPL for convenience →
      Cash flow tightens; uses BNPL to preserve cash →
      Opens second BNPL plan (stacking begins) →
      Multiple BNPL payments due; opens third to cover →
      BNPL payments consume increasing share of income →
      Misses BNPL payment; late fees compound →
      Either defaults on BNPL or diverts from other obligations →
      Traditional credit deterioration follows
      
    mechanism: |
      BNPL's ease of access enables rapid leverage accumulation.
      No credit check means no friction. Consumers can stack 5+
      plans before any provider knows. The visibility gap IS the trap.
      
    breakpoint: "BNPL payments exceed manageable share of income (>15%)"
    lag_time: "3-6 months from stacking to cash flow crisis"
    status: "MONITORING"
    cross_domain: ["Consumer spending", "Traditional credit cards"]

### FLOW-NICK-03: Payday Debt Trap Cascade

  FLOW-NICK-03:
    name: "Payday Debt Trap Cascade"
    pathway: |
      Consumer faces emergency expense →
      Takes payday loan (2-week term, high fee) →
      Cannot repay full amount at term end →
      Rolls over loan (pays fee, extends principal) →
      Cycle repeats; fees accumulate →
      Total fees exceed original principal multiple times →
      Consumer trapped: can't exit without windfall →
      Eventually defaults OR diverts from other obligations
      
    mechanism: |
      Payday loans designed for short-term but profit from long-term
      rollover. Average payday borrower is in debt 200+ days/year.
      This is not bridge financing — it's chronic debt servitude.
      
    breakpoint: "Consumer in perpetual rollover (>6 consecutive months)"
    lag_time: "Immediate trap; long-term extraction"
    status: "MONITORING"
    cross_domain: ["Consumer savings", "Bank overdrafts"]

### FLOW-NICK-04: Fintech Cockroach Cascade

  FLOW-NICK-04:
    name: "Fintech Cockroach Cascade"
    pathway: |
      Consumer credit quality deteriorates (invisible at first) →
      Fintech portfolios show rising delinquencies →
      Fintechs tighten underwriting (first visible signal) →
      Weaker fintechs face funding pressure →
      Fintech failure(s) occur (cockroach visible) →
      Funding markets tighten for all fintechs →
      Credit availability contracts →
      Consumers lose access to non-bank credit →
      Stress concentrates in traditional channels →
      Traditional metrics finally show deterioration
      
    mechanism: |
      Fintechs are early warning system. Their underwriting sees stress
      before traditional metrics. Their failures reveal what's coming.
      "When you see one cockroach..."
      
    breakpoint: "Multiple fintech failures; funding market stress"
    lag_time: "3-9 months from fintech stress to traditional credit visibility"
    status: "MONITORING"
    cross_domain: ["CARL (all vectors)", "Bank credit tightening"]

### FLOW-NICK-05: Nick-to-CARL Transmission

  FLOW-NICK-05:
    name: "Nick-to-CARL Transmission"
    pathway: |
      Shadow credit stress signals emerge (NICK vectors trigger) →
      Consumers exhaust shadow credit runway →
      Defaults begin appearing in traditional metrics →
      Credit card delinquency rises →
      Auto loan stress increases →
      Consumer credit data shows deterioration →
      CARL vectors trigger
      
    mechanism: |
      NICK sees stress first because shadow credit is the buffer.
      When buffer is exhausted, stress transmits to visible channels.
      NICK is early warning; CARL is confirmation.
      
    breakpoint: "Shadow credit stress appears in traditional metrics"
    lag_time: "6-12 months from shadow stress to CARL vector movement"
    status: "MONITORING"
    cross_domain: ["CARL (credit exhaustion)", "Bank credit quality"]

---

## DATA SOURCES

### Primary Sources

data_sources:

  sec_filings:
    description: "Public company filings for BNPL, fintech, payday lenders"
    entities: ["AFRM", "SQ (Afterpay)", "PYPL", "UPST", "LC", "SOFI", "ENVA", "DAVE", "ML"]
    frequency: "Quarterly"
    reliability: "HIGH — audited financials"
    limitations: "Private companies (Klarna, Earnin) not covered"
    
  cfpb_research:
    description: "Consumer Financial Protection Bureau reports and data"
    url: "consumerfinance.gov"
    frequency: "Periodic reports"
    reliability: "HIGH — regulatory data"
    key_reports:
      - "BNPL Market Report (periodic)"
      - "Payday Lending Studies"
      - "Consumer Credit Trends"
    limitations: "Publication lag; not real-time"
    
  abs_data:
    description: "Asset-Backed Securities performance data"
    sources: ["Kroll", "Fitch", "S&P", "DBRS", "Bloomberg"]
    frequency: "Monthly remittance reports"
    reliability: "HIGH — audited trust data"
    coverage: "Affirm, LendingClub, Prosper, Avant, SoFi securitizations"
    limitations: "Only covers securitized portions; selection bias"
    
  credit_bureau_studies:
    description: "Periodic research from Equifax, Experian, TransUnion"
    frequency: "Quarterly or periodic"
    reliability: "MEDIUM-HIGH — proprietary methodology"
    key_topics: ["BNPL reporting", "Fintech loan performance", "Credit trends"]
    
  academic_research:
    description: "Peer-reviewed studies on alternative credit"
    sources: ["NBER", "Fed working papers", "Journal of Finance", "university research"]
    frequency: "Irregular"
    reliability: "HIGH — rigorous methodology"
    limitations: "Significant publication lag"
    
  news_and_industry:
    description: "Journalism and industry publications"
    sources: ["American Banker", "Bloomberg", "WSJ", "Fintech-focused outlets"]
    frequency: "Ongoing"
    reliability: "MEDIUM — useful for leads, requires verification"

### Data Gaps

data_gaps:
  
  - description: "Private BNPL providers (Klarna) — no public financials"
    workaround: "Monitor European filings, press releases, funding rounds"
    severity: "MEDIUM — Klarna is major player"
    
  - description: "True BNPL stacking rates — no centralized data"
    workaround: "Rely on CFPB studies, credit bureau research (delayed)"
    severity: "HIGH — core thesis metric"
    
  - description: "Cash advance app detailed performance — limited disclosure"
    workaround: "Dave/MoneyLion public; others estimated"
    severity: "MEDIUM"
    
  - description: "Payday loan industry-wide data — fragmented, state-level"
    workaround: "Use Pew Research, CFPB, state regulator aggregation"
    severity: "MEDIUM"
    
  - description: "Real-time shadow credit usage — no live feed"
    workaround: "Quarterly earnings cycle; ABS monthly"
    severity: "HIGH — inherent lag in domain"

---

## GLOSSARY

glossary:

  terms:
    
    shadow_credit:
      definition: "Lending that occurs outside traditional bank/credit bureau visibility"
      examples: ["BNPL", "payday loans", "cash advance apps", "earned wage access"]
      significance: "Creates hidden leverage not captured in standard consumer credit metrics"
      
    bnpl_stacking:
      definition: "Consumer having multiple active BNPL plans simultaneously"
      significance: "Indicates BNPL used as credit line, not convenience; hidden leverage"
      
    rollover:
      definition: "Extending a short-term loan by paying fee and re-borrowing principal"
      context: "Payday loan term; indicates inability to repay"
      
    earned_wage_access:
      definition: "Accessing wages before payday, typically via app"
      also_called: "EWA, on-demand pay, paycheck advance"
      regulatory_status: "Gray area — may be classified as credit"
      
    liquidity_of_last_resort:
      definition: "Credit sources used when all other options exhausted"
      examples: ["Payday loans", "title loans", "pawn"]
      significance: "Usage indicates severe financial distress"
      
    cockroach_thesis:
      definition: "Visible failures indicate larger hidden problems"
      application: "Fintech failures suggest broader consumer credit deterioration"
      origin: "CARL system principle"
      
    underwriting_tightening:
      definition: "Lenders raising credit standards, approving fewer loans"
      significance: "LEADING indicator — lenders see stress before it defaults"
      
    warehouse_line:
      definition: "Credit facility used by fintechs to fund loan originations before securitization"
      significance: "Warehouse stress = fintech funding crisis"
      
    abs_performance:
      definition: "How loans in asset-backed securities are performing"
      metrics: ["Delinquency", "default", "loss severity", "prepayment"]
      
    regulatory_arbitrage:
      definition: "Structuring products to avoid regulatory requirements"
      examples: ["BNPL avoiding TILA disclosure", "EWA avoiding credit classification"]
      
  acronyms:
    BNPL: "Buy Now Pay Later"
    EWA: "Earned Wage Access"
    ABS: "Asset-Backed Securities"
    CFPB: "Consumer Financial Protection Bureau"
    TILA: "Truth in Lending Act"
    GMV: "Gross Merchandise Value"
    POS: "Point of Sale"
    APR: "Annual Percentage Rate"

---

## REPORTING RELATIONSHIP

### NICK → CARL State Vector

reporting:
  
  parent_agent: "CARL"
  reporting_frequency: "As significant developments occur; minimum monthly"
  
  state_vector_focus:
    primary_signal: "Hidden consumer leverage and credit stress invisible to traditional metrics"
    secondary_signals:
      - "Early warning from fintech underwriting tightening"
      - "Cockroach signals from lender failures"
      - "BNPL/payday usage indicating liquidity exhaustion"
    
  key_questions_from_carl:
    - "How much hidden leverage exists beyond traditional credit metrics?"
    - "Are shadow credit sources showing stress before traditional channels?"
    - "What is the transmission lag from shadow stress to visible metrics?"
    
  escalation_criteria:
    - "Any vector moves to BREACHED status"
    - "Fintech lender failure (cockroach event)"
    - "CFPB or major research reveals significant hidden leverage"
    - "Multiple vectors move to CRITICAL simultaneously"

---

## SESSION QUICK REFERENCE

### For Update Sessions
Focus on: VX-NICK-1.xx (BNPL), VX-NICK-3.xx (Fintech)
Key question: "Are BNPL delinquencies or fintech credit quality deteriorating?"

### For Analysis Sessions
Focus on: FLOW cascades, cross-references to CARL vectors
Key question: "What transmission mechanisms are activating?"

### For Reconciliation Sessions
Focus on: Data source verification, cross-reference integrity
Key question: "Is our data current given shadow credit opacity?"

### For State Vector Reports
Include: Highest-concern vectors, cockroach events, lag estimates for CARL
Format: Per NICK_METHODOLOGY_SKELETON §6.2

---

# END OF SKELETON

# Maintenance Notes:
# - Update vector current_values as data arrives (quarterly cycle)
# - Add new shadow credit products as they emerge
# - Track regulatory changes that affect data availability
# - Monitor for new fintech lenders to add to watch list
# - Version increment for structural changes
