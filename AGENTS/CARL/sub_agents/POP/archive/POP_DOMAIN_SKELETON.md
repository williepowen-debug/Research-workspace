# POP DOMAIN SKELETON v1.0

# Purpose: Structural scaffold for Small Business Stress monitoring
# Domain:  Small Business Stress → Consumer Financial Transmission
# Agent:   POP (Small Business Stress Monitor)
#
# Version: 1.0
# Created: 2026-01-20
# Author:  Initial Architecture Session
#
# Usage:
#   - Load this file at the start of any POP session
#   - Provides vocabulary, vectors, thresholds, and domain structure
#   - Companion to METHODOLOGY_SKELETON which governs process
#   - This skeleton governs the CONTENT of small business stress monitoring
#
# Relationship: POP reports to CARL via State Vectors
#              POP does NOT assess overall consumer stress—that's CARL's role

---

## METADATA

```yaml
metadata:
  name: "POP Domain Skeleton"
  domain: "Small Business Stress"
  version: "1.0"
  created: "2026-01-20"
  reports_to: "CARL"
  
  core_thesis:
    name: "Small Business Stress Transmission"
    description: |
      Small business deterioration is both a LEADING INDICATOR and 
      AMPLIFIER of consumer financial stress through multiple channels:
      
      1. OWNER-CONSUMER DUALITY: Small business owners ARE consumers.
         Their business stress is their personal financial stress.
         
      2. EMPLOYMENT TRANSMISSION: Small business failures destroy jobs.
         Local employment depends heavily on small business health.
         
      3. WEALTH DESTRUCTION: Business equity is household wealth.
         When businesses fail, owner net worth collapses.
         
      4. LOCAL MULTIPLIER: Small business spending supports other
         local businesses. Contraction cascades locally.
         
      5. CREDIT CONTAMINATION: Business defaults become personal
         defaults via personal guarantees.
         
    confidence: "Theoretical HIGH, Empirical monitoring underway"
    
  phase_model: |
    Phase 1 (Stress Accumulation) → Phase 2 (Liquidity Crisis) → 
    Phase 3 (Closure Wave) → Phase 4 (Consumer Transmission)
    
    Stress accumulates silently. Liquidity crisis forces visible action.
    Closures accelerate. Consumer impact follows with 3-6 month lag.
```

---

## 1. ENTITY DEFINITIONS

### 1.1 Business Segments

| Segment | Definition | Consumer Exposure |
|---------|------------|-------------------|
| **Micro** | 1-9 employees, typically owner-operated | HIGHEST—owner IS the business |
| **Small** | 10-99 employees | HIGH—significant local employment |
| **Lower-Middle** | 100-499 employees | MEDIUM—broader employment base |
| **Franchise** | Franchised operations of any size | HIGH—personal guarantee exposure |
| **Sole Proprietor** | No employees, owner-only | HIGHEST—complete overlap |

### 1.2 Sector Categories

| Sector | Examples | Consumer Stress Relevance |
|--------|----------|--------------------------|
| **Retail** | Shops, stores, boutiques | Local spending indicator; employment |
| **Restaurant/Food Service** | Restaurants, cafes, bars | Discretionary spending canary |
| **Personal Services** | Salons, gyms, repair shops | Consumer discretionary indicator |
| **Professional Services** | Accountants, lawyers, consultants | Business-to-business stress |
| **Construction/Trades** | Contractors, plumbers, electricians | Housing market linkage |
| **Healthcare Services** | Dental, PT, independent clinics | Consumer healthcare stress |
| **Transportation** | Trucking, delivery, logistics | Supply chain indicator |
| **Hospitality** | Hotels, event venues | Discretionary/travel indicator |

### 1.3 Stress Stages

| Stage | Name | Characteristics | Consumer Impact |
|-------|------|-----------------|-----------------|
| **Stage 1** | Margin Compression | Revenues flat/declining, costs rising | Owner compensation cuts |
| **Stage 2** | Liquidity Squeeze | Cash reserves depleting, credit tightening | Owner personal assets pledged |
| **Stage 3** | Survival Mode | Layoffs, hour cuts, distressed borrowing | Employment transmission begins |
| **Stage 4** | Closure/Failure | Bankruptcy, dissolution, abandonment | Full consumer transmission |

---

## 2. VECTOR REGISTRY (VX)

### 2.1 Business Formation & Closure

```yaml
VX-POP-1.01:
  name: "Net Business Formation Rate"
  description: "New formations minus closures, monthly"
  data_source: "Census Business Formation Statistics, BLS"
  threshold: "Negative for 3+ consecutive months"
  tripwire: "Year-over-year decline >15%"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Formation decline = future employment decline"
  update_frequency: "Monthly"

VX-POP-1.02:
  name: "Business Bankruptcy Filings"
  description: "Chapter 7 and Chapter 11 filings by small businesses"
  data_source: "US Courts, Epiq Bankruptcy Analytics"
  threshold: "YoY increase >20%"
  tripwire: "YoY increase >40% OR absolute level exceeds 2020 peak"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Bankruptcies = job losses + owner financial destruction"
  update_frequency: "Monthly/Quarterly"

VX-POP-1.03:
  name: "Restaurant/Retail Closure Rate"
  description: "Net closures in consumer-facing sectors"
  data_source: "Yelp Economic Average, BLS QCEW, local permits"
  threshold: "Closure rate exceeds formation rate for 2+ quarters"
  tripwire: "Net closure rate >5% annualized"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Direct employment loss; local spending multiplier"
  update_frequency: "Monthly"
```

### 2.2 Credit & Liquidity

```yaml
VX-POP-2.01:
  name: "Small Business Loan Delinquency"
  description: "30+ and 90+ day delinquency on SB loans"
  data_source: "Fed Senior Loan Officer Survey, SBA, bank call reports"
  threshold: "30+ DQ >5%"
  tripwire: "90+ DQ >3% OR rapid acceleration (>50bps in quarter)"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Defaults often become personal via guarantees"
  update_frequency: "Quarterly"

VX-POP-2.02:
  name: "SBA Loan Default Rate"
  description: "Default rate on SBA 7(a) and 504 loans"
  data_source: "SBA Office of Advocacy"
  threshold: "Default rate >3%"
  tripwire: "Default rate >5% OR YoY increase >100bps"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "SBA defaults typically have personal guarantees"
  update_frequency: "Quarterly"

VX-POP-2.03:
  name: "Business Credit Card Utilization"
  description: "Average utilization on business credit cards"
  data_source: "Fed G.19, issuer reports, surveys"
  threshold: "Average utilization >60%"
  tripwire: "Average utilization >75% OR minimum payment rate at highs"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Business cards often personally guaranteed"
  update_frequency: "Monthly"

VX-POP-2.04:
  name: "Merchant Cash Advance Usage"
  description: "Volume and growth of MCA lending"
  data_source: "Industry reports, fintech disclosures"
  threshold: "YoY volume growth >30%"
  tripwire: "Rapid growth combined with rising default reports"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "MCA is distress borrowing; leads to business failure"
  note: "MCA growth is a DISTRESS signal, not health signal"
  update_frequency: "Quarterly"

VX-POP-2.05:
  name: "Cash Reserve Runway"
  description: "Median weeks of cash on hand for small businesses"
  data_source: "JPM Chase Institute, Fed surveys, NFIB"
  threshold: "Median <4 weeks"
  tripwire: "Median <2 weeks OR >30% with <1 week"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Low runway = one shock from closure"
  update_frequency: "Quarterly"
```

### 2.3 Revenue & Operations

```yaml
VX-POP-3.01:
  name: "Small Business Revenue Index"
  description: "Indexed revenue trends from payment processors/surveys"
  data_source: "Intuit QuickBooks, Square, NFIB, regional Fed surveys"
  threshold: "YoY decline >5% for 2+ months"
  tripwire: "YoY decline >10% OR accelerating decline"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Revenue stress → wage/hour cuts → employment loss"
  update_frequency: "Monthly"

VX-POP-3.02:
  name: "Small Business Employment Plans"
  description: "Net % planning to increase vs decrease employment"
  data_source: "NFIB Small Business Optimism Survey"
  threshold: "Net positive <5%"
  tripwire: "Net negative (more planning cuts than hires)"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "LEADING indicator of actual employment changes"
  update_frequency: "Monthly"

VX-POP-3.03:
  name: "Owner Compensation Cuts"
  description: "% of owners reporting reduced personal compensation"
  data_source: "NFIB, regional Fed surveys, Gusto data"
  threshold: ">20% reporting cuts"
  tripwire: ">35% reporting cuts OR cuts accelerating"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "DIRECT owner-consumer stress transmission"
  update_frequency: "Quarterly"
```

### 2.4 Sentiment & Outlook

```yaml
VX-POP-4.01:
  name: "NFIB Optimism Index"
  description: "Headline small business optimism measure"
  data_source: "NFIB Monthly Survey"
  threshold: "Below 95 (historical average ~98)"
  tripwire: "Below 90 OR largest monthly decline on record"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Sentiment precedes action; optimism leads hiring"
  update_frequency: "Monthly"

VX-POP-4.02:
  name: "Expectations for Business Conditions"
  description: "Net % expecting improvement vs deterioration"
  data_source: "NFIB Survey"
  threshold: "Net negative for 2+ months"
  tripwire: "Net negative >30% OR worst reading on record"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Expectations drive investment and hiring decisions"
  update_frequency: "Monthly"

VX-POP-4.03:
  name: "Credit Availability Satisfaction"
  description: "% satisfied with credit availability"
  data_source: "NFIB, Fed SBCS"
  threshold: "<30% satisfied"
  tripwire: "<20% satisfied OR YoY decline >15pp"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Credit tightening → liquidity crisis → failures"
  update_frequency: "Quarterly"
```

### 2.5 Owner Stress (Consumer Crossover)

```yaml
VX-POP-5.01:
  name: "Personal Guarantee Exposure"
  description: "Estimated % of SB loans with personal guarantees"
  data_source: "SBA data, Fed surveys, industry estimates"
  threshold: "Rising guarantee requirements from lenders"
  tripwire: "Lenders requiring additional collateral/guarantees"
  current_value: "[TBD—baseline typically 60-80%]"
  status: "[TBD]"
  consumer_transmission: "Business failure = personal financial destruction"
  update_frequency: "Quarterly"

VX-POP-5.02:
  name: "Business/Personal Finance Blending"
  description: "% of owners using personal funds for business"
  data_source: "Fed SBCS, surveys"
  threshold: ">40% using personal savings for business"
  tripwire: ">50% OR increasing trend"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "Personal savings depletion for business = consumer stress"
  update_frequency: "Annual (Fed SBCS)"

VX-POP-5.03:
  name: "Owner Personal Credit Deterioration"
  description: "Credit score changes for identified business owners"
  data_source: "Credit bureau data (if accessible), surveys"
  threshold: "Average score decline >20 points"
  tripwire: "Significant increase in owners with subprime personal scores"
  current_value: "[TBD]"
  status: "[TBD]"
  consumer_transmission: "DIRECT measure of owner-consumer stress"
  update_frequency: "Quarterly"
```

---

## 3. FLOW CASCADES

### FLOW-POP-01: "Owner Squeeze Cascade"

```yaml
flow_id: "FLOW-POP-01"
flow_name: "Owner Squeeze Cascade"
pathway: |
  Revenue decline → Margin compression → Owner compensation cut →
  Personal savings depletion → Personal credit stress →
  Consumer financial deterioration
mechanism: |
  Small business owners typically absorb early stress personally.
  They cut their own pay before cutting employees.
  They use personal savings to cover business shortfalls.
  Their personal credit suffers as business struggles.
  Eventually, owner IS a stressed consumer.
lag_time: "3-12 months from revenue decline to personal credit impact"
breakpoint: "Owner compensation cuts sustained >2 quarters"
consumer_transmission: "DIRECT—owner stress IS consumer stress"
status: "ACTIVE"
```

### FLOW-POP-02: "Employment Transmission Cascade"

```yaml
flow_id: "FLOW-POP-02"
flow_name: "Employment Transmission Cascade"
pathway: |
  Business stress → Hiring freeze → Hour cuts → Layoffs →
  Local unemployment spike → Consumer spending decline →
  Further business stress (feedback loop)
mechanism: |
  Small businesses employ ~47% of private workforce.
  Employment decisions follow stress with 3-6 month lag.
  Local areas dependent on small business suffer concentrated impact.
  Multiplier effect as laid-off workers reduce spending.
lag_time: "3-6 months from business stress to employment action"
breakpoint: "Net employment plans go negative"
consumer_transmission: "EMPLOYMENT channel—job/income loss"
feedback_loop: "Consumer spending decline worsens business stress"
status: "ACTIVE"
```

### FLOW-POP-03: "Credit Contamination Cascade"

```yaml
flow_id: "FLOW-POP-03"
flow_name: "Credit Contamination Cascade"
pathway: |
  Business loan delinquency → Personal guarantee called →
  Owner personal default → Consumer credit deterioration →
  Reduced access to consumer credit
mechanism: |
  Most small business loans require personal guarantees.
  Business default = personal default for owner.
  Owner's personal credit score destroyed.
  Owner loses access to mortgage refinancing, auto loans, credit cards.
  Owner household becomes stressed consumer household.
lag_time: "6-12 months from business distress to personal default recognition"
breakpoint: "SBA default rates exceed 5%"
consumer_transmission: "CREDIT channel—personal credit destruction"
status: "ACTIVE"
```

### FLOW-POP-04: "Local Multiplier Collapse"

```yaml
flow_id: "FLOW-POP-04"
flow_name: "Local Multiplier Collapse"
pathway: |
  Small business closures → Lost local wages →
  Reduced local spending → Neighboring business stress →
  Accelerated local closure wave
mechanism: |
  Small businesses buy from other local businesses.
  Employees spend locally.
  Closure removes both business spending AND employee spending.
  Neighboring businesses lose customers.
  Closure becomes contagious within geographic area.
lag_time: "6-18 months for full local multiplier impact"
breakpoint: "Multiple closures in same commercial district"
consumer_transmission: "LOCAL ECONOMY channel—concentrated geographic impact"
status: "ACTIVE"
```

### FLOW-POP-05: "Franchise Failure Wave"

```yaml
flow_id: "FLOW-POP-05"
flow_name: "Franchise Failure Wave"
pathway: |
  Franchisor squeeze on terms → Franchisee margin collapse →
  Franchisee defaults → Personal guarantee destruction →
  Franchisee becomes distressed consumer
mechanism: |
  Franchise agreements often require significant personal investment.
  Franchisees typically personally guarantee buildout loans.
  Franchisor can tighten terms (royalties, required investments).
  Franchisee bears concentrated risk.
  Failure destroys franchisee's total net worth.
lag_time: "12-24 months from franchise system stress to wave of closures"
breakpoint: "Major franchise system reports elevated franchisee failures"
consumer_transmission: "WEALTH DESTRUCTION—total net worth loss for owners"
status: "ACTIVE"
```

---

## 4. DATA SOURCES

### Primary Sources

| Source | Data Provided | Frequency | Access |
|--------|---------------|-----------|--------|
| **NFIB Small Business Optimism** | Sentiment, employment plans, credit satisfaction | Monthly | Public |
| **Census Business Formation Statistics** | Applications, formations | Monthly | Public |
| **Fed Small Business Credit Survey** | Financing, credit availability, owner stress | Annual | Public |
| **SBA Office of Advocacy** | Loan performance, business demographics | Quarterly | Public |
| **BLS QCEW** | Employment by establishment size | Quarterly | Public |
| **US Courts PACER** | Bankruptcy filings | Ongoing | Public |
| **Fed Senior Loan Officer Survey** | Lending standards, demand | Quarterly | Public |

### Secondary Sources

| Source | Data Provided | Frequency | Access |
|--------|---------------|-----------|--------|
| **Regional Fed Surveys** | Local business conditions | Monthly | Public |
| **Intuit QuickBooks** | Revenue, hiring, cash flow | Monthly | Subscription/reports |
| **Square/Toast** | Restaurant/retail transaction data | Monthly | Reports |
| **JPM Chase Institute** | Cash balances, flows | Periodic | Reports |
| **Gusto** | Payroll, employment | Monthly | Reports |
| **Yelp Economic Average** | Local business openings/closures | Monthly | Public |
| **Alignable** | Small business surveys | Monthly | Reports |

### Distress Indicators (High Signal Value)

| Source | Signal | Interpretation |
|--------|--------|----------------|
| **Merchant Cash Advance volume** | Distress borrowing | Desperate for liquidity |
| **Business credit card utilization** | Cash flow stress | Relying on expensive credit |
| **Equipment financing defaults** | Operational stress | Can't service equipment debt |
| **Commercial rent delinquency** | Severe cash stress | Choosing between rent and payroll |

---

## 5. GLOSSARY

### Key Terms

| Term | Definition | Consumer Relevance |
|------|------------|-------------------|
| **Owner-Consumer Duality** | Small business owners are simultaneously business operators and consumers; their business stress is their personal stress | FUNDAMENTAL—owner stress IS consumer stress |
| **Personal Guarantee** | Owner's personal obligation to repay business debt if business defaults | Business failure → personal financial destruction |
| **Zombie Business** | Operating but unable to invest, hire, or grow; surviving but not thriving | Employment stagnation; owner income suppression |
| **Merchant Cash Advance (MCA)** | High-cost short-term financing based on future receivables | DISTRESS SIGNAL—indicates conventional credit exhausted |
| **Cash Runway** | Weeks of operating expenses covered by cash on hand | Low runway = one shock from closure |
| **Net Formation Rate** | New business formations minus closures | Negative = shrinking business population |
| **NFIB Optimism Index** | Headline small business sentiment measure | LEADING indicator of employment/investment |
| **Franchise Agreement** | Contract governing franchisee-franchisor relationship | Concentrates risk on franchisee |
| **SBA 7(a) Loan** | Most common SBA-backed small business loan | Requires personal guarantee |
| **Local Multiplier** | Economic ripple effect of local spending | Business closure removes multiplied spending |

### Status Definitions

| Status | Definition | Action Required |
|--------|------------|-----------------|
| **NORMAL** | Below threshold, no concern | Routine monitoring |
| **ELEVATED** | Approaching threshold, watch closely | Increased monitoring frequency |
| **CRITICAL** | At or near threshold, high concern | Prepare State Vector for CARL |
| **BREACHED** | Tripwire crossed, immediate attention | Issue State Vector to CARL |

---

## 6. STATE VECTOR PROTOCOL

### When to Issue State Vector to CARL

Issue a State Vector when:
1. Any vector status changes to BREACHED
2. Multiple vectors move to CRITICAL simultaneously
3. Novel pattern emerges not captured by existing vectors
4. Significant contradiction to CARL's current thesis detected
5. Request from CARL for status update

### State Vector Template

```yaml
state_vector:
  # IDENTITY
  id: "SV-POP-[YYYY-MM-DD]-[##]"
  from_agent: "POP"
  to_agent: "CARL"
  timestamp: "[ISO timestamp]"
  
  # SYNTACTIC (shared vocabulary)
  domain: "Small Business Stress"
  vector_ref: "[VX-POP-#.##]"  # Primary vector driving this report
  metric: "[Metric name]"
  value: "[Current value]"
  threshold: "[Threshold value]"
  status: "NORMAL | ELEVATED | CRITICAL | BREACHED"
  
  # SEMANTIC (local interpretation)
  interpretation: |
    [What this means in small business terms]
    [How this transmits to consumer stress]
    [Relevant context and patterns]
  confidence: [XX]%
  confidence_reasoning: |
    [Why this confidence level]
    [What would change it]
  translation_flags:
    - "[Concepts that may need additional translation for CARL]"
  
  # PRAGMATIC (recommended action)
  recommended_action: "IGNORE | WATCH | INCORPORATE | ESCALATE"
  action_rationale: "[Why this recommendation]"
  transmission_mechanism: "[Which FLOW cascade is relevant]"
  lag_estimate: "[Expected time until consumer impact]"
  
  # VALIDITY
  sources:
    - "[Data source 1]"
    - "[Data source 2]"
  invalidation_conditions:
    - "[What would change this assessment]"
  next_update: "[Expected next data point]"
```

---

## 7. RELATIONSHIP TO CARL

### What POP Does

- Monitors small business stress signals across all defined vectors
- Interprets signals within small business domain context
- Identifies transmission mechanisms to consumer stress
- Reports findings to CARL via State Vectors
- Maintains domain-specific logs (ML, FL, FLOW)

### What POP Does NOT Do

- Assess overall consumer financial stress (CARL's role)
- Synthesize signals from other domains (CARL's role)
- Make system-wide thesis assessments (CARL's role)
- Override or contradict CARL's conclusions directly

### Communication Protocol

```
POP detects signal → POP assesses in domain context → 
POP creates State Vector → State Vector delivered to CARL →
CARL integrates with other domain signals → CARL updates system thesis
```

### When CARL May Override POP

CARL may discount or recontextualize POP's State Vectors when:
- Conflicting signals from other domains provide context
- System-wide patterns suggest different interpretation
- Timing or lag considerations change relevance

POP should document any cases where CARL's treatment differs from POP's recommendation for methodology refinement.

---

## 8. SESSION PROTOCOLS

### On Session Start

1. **Load context:**
   - This domain skeleton
   - POP_METHODOLOGY_SKELETON.md
   - Most recent POP handoff
   - POP WORKBOOK/ (or relevant entries)

2. **Check CARL context:**
   - Review CARL's current thesis status (if available)
   - Note any requests or focus areas from CARL
   - Check for pending data releases

3. **State session intent:**
   - Session type (Update, Analysis, Reconciliation)
   - Specific objectives
   - Expected outputs

### On Session End

1. **Update logs:**
   - New observations to ML
   - Retire any passed FL entries
   - Update cross-references

2. **Assess State Vector need:**
   - Any BREACHED vectors?
   - Significant pattern changes?
   - If yes → prepare State Vector for CARL

3. **Create handoff:**
   - Follow I-PASS adapted template
   - Include any State Vectors issued
   - Note pending data releases

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-20 | Initial skeleton creation |

---

*End of POP Domain Skeleton*
