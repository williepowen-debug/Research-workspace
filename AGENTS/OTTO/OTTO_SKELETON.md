# OTTO DOMAIN SKELETON v1.0

# Purpose: Structural scaffold for LLM domain orientation
# Domain:  Subprime Auto Lending Fraud, Double-Pledging, ABS Exposure, Warehouse Risk
# Agent:   OTTO (Automotive Fraud & Subprime Auto Monitoring Agent)
#
# Version: 1.0
# Created: 2026-01-26
# Updated: 2026-01-26
# Author:  PROME Network

---

## 0. QUICK START

*Load this section for any session. Provides minimum viable orientation.*

### About This Agent

OTTO monitors the emerging subprime auto lending fraud pattern with focus on:
- Known fraud cases (Tricolor, First Brands, PrimaLend)
- Double-pledging schemes in warehouse lending
- Bank exposure to collapsed lenders
- Systemic transmission to broader auto credit market
- Regulatory/legal developments

**Coordination:** Primary linkages to CARL (consumer auto DQ), REGINALD (bank exposure), LIQUID (funding)

### Current Thesis

**PRIMARY THESIS: Systematic Fraud Uncovered in Subprime Auto**

A pattern of systematic fraud has been uncovered in subprime auto lending, centered on double-pledging schemes:

1. **Tricolor Holdings** → Chapter 7 bankruptcy (Sept 2025); executives charged with fraud (Dec 2025); ~$2B debt; double-pledging + data manipulation
2. **First Brands** → Bankruptcy; double-pledging in supply chain/inventory finance; trial June 2026
3. **PrimaLend** → Chapter 11 (Oct 2025); warehouse line stress; seeking restructuring

**Key Mechanism:** Lenders pledge same collateral (auto loans) to multiple warehouse lenders, fabricate data to make delinquent loans appear current, extract billions before collapse.

**Bank Losses Confirmed:**
- JPMorgan Chase: $170M loss (Tricolor)
- Fifth Third Bank: $200M loss (Tricolor)
- Multiple others exposed (Jefferies, UBS)

**Confidence:** Pattern 90% | Magnitude 75% | Contagion 70%
**Status:** CRITICAL — Active fraud prosecutions; systemic reassessment underway

**Invalidation Criteria:**
- DOJ finds fraud limited to named companies only
- Warehouse lenders resume normal operations without tightening
- No additional subprime lender failures in 6 months
- Bank losses contained to disclosed amounts

### Scenario Framework

| Scenario | Probability | Description | Primary Vector |
|----------|-------------|-------------|----------------|
| **A** | 25% | Fraud contained to known cases | VX-OTTO-001 |
| **B** | 40% | Additional lenders discovered with similar fraud | VX-OTTO-002 |
| **C** | 25% | Systemic credit tightening hits subprime consumers | VX-OTTO-004 |
| **D** | 10% | Major bank takes material losses; contagion | VX-OTTO-003 |

### Coordinating Agents

| Agent | Domain | Key Linkages |
|-------|--------|--------------|
| **CARL** | Consumer stress | Auto DQ already BREACHED (6.65%); credit access tightening |
| **REGINALD** | Regional banks | Warehouse line exposure; ABS holdings |
| **LIQUID** | Treasury/funding | Funding stress from lender collapses |
| **EARNINGS** | Corporate earnings | Bank provisions from auto exposure |

---

## 1. ENTITY TYPES

### Known Fraud Cases

| Entity | Status | Debt | Fraud Allegations | Key Dates |
|--------|--------|------|-------------------|-----------|
| **Tricolor Holdings** | Chapter 7 | ~$2B | Double-pledging; data manipulation; fabricated payments | Filed Sept 2025; Charges Dec 2025 |
| **First Brands** | Bankruptcy | TBD | Double-pledging in supply chain/inventory finance | Trial June 2026 |
| **PrimaLend** | Chapter 11 | $286M | Warehouse line stress; sued by Prime Asset LLC | Filed Oct 2025 |

### Key Executives (Tricolor)

| Name | Role | Status |
|------|------|--------|
| **Daniel Chu** | Founder/CEO | Charged; faces life in prison |
| **Daniel Goodgame** | COO | Charged |
| **Jerome Kollar** | Former exec | Pled guilty; cooperating |
| **Ameryn Seibold** | Former exec | Pled guilty; cooperating |

### Bank Exposure

| Bank | Exposure | Loss Disclosed | Status |
|------|----------|----------------|--------|
| **JPMorgan Chase** | Tricolor | $170M | Disclosed |
| **Fifth Third** | Tricolor | $200M | Disclosed; cooperating with law enforcement |
| **Jefferies** | Multiple | TBD | Reported exposure |
| **UBS** | Multiple | TBD | Reported exposure |

### Warehouse Lenders at Risk

| Type | Description | Risk Level |
|------|-------------|------------|
| **Bank warehouse lines** | Senior secured to SPVs | HIGH — reassessing all subprime exposure |
| **Private credit** | Mezzanine/junior tranches | CRITICAL — first loss position |
| **ABS investors** | Securitization buyers | ELEVATED — deal performance deteriorating |

---

## 2. FRAUD MECHANISMS

### Double-Pledging Scheme

```
HOW IT WORKS:
1. Subprime lender originates auto loans
2. Loans placed in Special Purpose Vehicle (SPV)
3. SPV pledges loans as collateral to Warehouse Lender A
4. SAME loans secretly pledged to Warehouse Lender B (different SPV)
5. Lender extracts funding from both → cash extraction
6. When defaults rise, insufficient collateral to cover both lines
7. Lenders discover duplication only in bankruptcy

WHY IT'S HARD TO DETECT:
- Each warehouse lender examines only their SPV
- No cross-facility collateral reconciliation
- Fragmented oversight across legal entities
- Electronic chattel paper control weaknesses
```

### Data Manipulation

```
HOW IT WORKS:
1. Delinquent loans should be flagged and excluded from borrowing base
2. Lender manipulates loan tapes to show delinquent loans as current
3. Fabricates customer payment records
4. Inflates borrowing base → extracts more funding
5. Audits miss manipulation due to falsified records
```

### Off-Balance Sheet Financing (First Brands)

```
HOW IT WORKS:
1. Aggressive acquisition strategy in aftermarket auto parts
2. Heavy use of off-balance sheet financing (poorly disclosed)
3. Double-pledging in supply chain and inventory finance
4. Investors unaware of true leverage
5. Collapse when financing pulled
```

---

## 3. TRANSMISSION PATHS

### FLOW-OTTO-01: Warehouse Line Contagion

```
Speed: WEEKS
Status: ACTIVE — Lenders reassessing
Layer: Funding

Pathway:
  Fraud discovered at subprime lender
    → Warehouse lenders pull lines (self-protection)
    → Other subprime lenders face liquidity squeeze
    → Unable to fund new originations
    → Origination volume collapses
    → Credit access for subprime consumers tightens
    → CARL auto DQ rises further (can't refinance)
    → Delinquencies accelerate

Trigger: Warehouse lenders broadly tighten; >2 additional lender failures
Current Position: ACTIVE — Lenders reassessing all subprime exposure
Historical Precedent: 2007-2008 mortgage warehouse collapse
```

### FLOW-OTTO-02: Bank Loss Cascade

```
Speed: QUARTERS
Status: ELEVATED — JPM/Fifth Third losses disclosed
Layer: Banking

Pathway:
  Bank discloses auto warehouse losses
    → Investors question other exposures
    → Bank tightens all warehouse/auto lending
    → Provisioning increases
    → Credit availability declines
    → Earnings pressure → REGINALD

Trigger: Bank loss >$500M from auto exposure; multiple banks disclose
Current Position: JPM $170M, Fifth Third $200M — contained so far
Historical Precedent: 2008 bank write-downs
```

### FLOW-OTTO-03: ABS Performance Deterioration

```
Speed: MONTHS
Status: LATENT — Watching deal performance
Layer: Securitization

Pathway:
  Subprime auto ABS deal performance deteriorates
    → Downgrades begin
    → CLO/fund holders face mark-to-market losses
    → Forced selling
    → Spread widening
    → New issuance freezes
    → Origination funding dries up

Trigger: Major subprime auto ABS deal downgraded; spread +100bps
Current Position: Spreads elevated but not crisis; watching
Historical Precedent: 2007 subprime MBS cascade
Coordination: REGINALD (bank ABS holdings), LIQUID (spread widening)
```

### FLOW-OTTO-04: Consumer Credit Crunch

```
Speed: IMMEDIATE — Already active
Status: CRITICAL — Credit tightening underway
Layer: Consumer

Pathway:
  Fraud discovery + lender failures
    → Warehouse lenders tighten across industry
    → Subprime auto origination declines
    → Consumers can't get car loans
    → Can't refinance underwater loans
    → Delinquencies accelerate (CARL already 6.65% BREACHED)
    → Repossessions spike
    → Feedback to bank losses

Trigger: Fed SLOOS shows tightening; subprime origination -20%+
Current Position: ACTIVE — Fed data shows banks tightening standards
Historical Precedent: 2008-2009 credit crunch
Coordination: CARL (consumer DQ)
```

---

## 4. THRESHOLDS (Consolidated Tripwires)

**Color Coding:** 🟢 GREEN | 🟡 YELLOW | 🟠 ORANGE | 🔴 RED

### FRAUD SCOPE

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **Known fraud cases** | 3 (Tricolor, First Brands, PrimaLend) | 4 | 5+ | 7+ | 🔴 RED |
| **Bank losses disclosed** | $370M+ | $500M | $1B | $2B+ | 🟠 ORANGE |
| **DOJ investigations** | 1 active (Tricolor) | 2 | 3+ | Industry-wide | 🟡 YELLOW |

### WAREHOUSE LENDING

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **Warehouse line availability** | Tightening | Selective cuts | Broad cuts | Frozen | 🟠 ORANGE |
| **Subprime origination volume** | Declining | -15% | -25% | -40%+ | 🟡 YELLOW |

### ABS PERFORMANCE

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **Subprime auto ABS spreads** | Elevated | +50bps | +100bps | +200bps | 🟡 YELLOW |
| **Subprime auto ABS downgrades** | Minimal | 3+ deals | 10+ deals | Sector-wide | 🟢 GREEN |

### CONSUMER TRANSMISSION (Link to CARL)

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **Auto DQ rate** | 6.65% (CARL) | >6.5% | >7.0% | >8.0% | 🔴 RED (BREACHED) |
| **Subprime approval rate** | Declining | -10% | -20% | -30%+ | 🟡 YELLOW |

---

## 5. VECTOR REGISTRY

### VX-OTTO-001: Known Fraud Cases

| Field | Value |
|-------|-------|
| **Name** | Identified Fraud Lenders |
| **Current** | 3 (Tricolor, First Brands, PrimaLend) |
| **Status** | 🔴 RED |
| **Confidence** | 90% |
| **Context** | Pattern established; more likely to emerge |
| **Downstream** | Bank losses; credit tightening |

### VX-OTTO-002: Additional Lender Risk

| Field | Value |
|-------|-------|
| **Name** | Undiscovered Fraud Potential |
| **Current** | Unknown — reassessment underway |
| **Status** | 🟠 ORANGE |
| **Confidence** | 70% |
| **Context** | Warehouse lenders auditing all exposures |
| **Downstream** | Cascade if more discovered |

### VX-OTTO-003: Bank Exposure

| Field | Value |
|-------|-------|
| **Name** | Bank Losses from Auto Fraud |
| **Current** | $370M+ (JPM $170M, Fifth Third $200M) |
| **Status** | 🟠 ORANGE |
| **Confidence** | 85% |
| **Context** | Disclosed losses; more may emerge |
| **Downstream** | Provisioning; credit tightening |
| **Coordination** | REGINALD, EARNINGS |

### VX-OTTO-004: Warehouse Line Availability

| Field | Value |
|-------|-------|
| **Name** | Subprime Auto Funding Access |
| **Current** | Tightening across industry |
| **Status** | 🟠 ORANGE |
| **Confidence** | 80% |
| **Context** | Lenders reassessing all subprime exposure |
| **Downstream** | Origination decline; consumer credit crunch |
| **Coordination** | LIQUID |

### VX-OTTO-005: Consumer Credit Access

| Field | Value |
|-------|-------|
| **Name** | Subprime Auto Loan Availability |
| **Current** | Declining; standards tightening |
| **Status** | 🟡 YELLOW |
| **Confidence** | 75% |
| **Context** | Fed SLOOS shows tightening; delinquencies at 2009 levels |
| **Downstream** | CARL auto DQ acceleration |
| **Coordination** | CARL |

### VX-OTTO-006: Legal/Regulatory

| Field | Value |
|-------|-------|
| **Name** | DOJ/SEC Investigation Status |
| **Current** | Tricolor charges filed; First Brands trial June 2026 |
| **Status** | 🟡 YELLOW |
| **Confidence** | 80% |
| **Context** | Cooperating witnesses; investigation may expand |
| **Downstream** | Additional fraud discovery |

---

## 6. CURRENT WATCHLIST (Jan 26, 2026)

### 🔴 RED STATUS (Immediate Action)

| Entity | Value | Note |
|--------|-------|------|
| **Known fraud cases** | 3 lenders | Tricolor, First Brands, PrimaLend |
| **Auto DQ (via CARL)** | 6.65% | ATH; BREACHED threshold |

### 🟠 ORANGE STATUS (24-Hour Watch)

| Entity | Value | Threshold | Note |
|--------|-------|-----------|------|
| **Bank losses** | $370M+ | $1B | More may emerge |
| **Warehouse availability** | Tightening | Broad cuts | Industry reassessing |
| **Additional lender risk** | Unknown | 4th case | Pattern suggests more |

### 🟡 YELLOW STATUS (Daily Monitor)

| Entity | Value | Note |
|--------|-------|------|
| DOJ investigation | Active | May expand |
| ABS spreads | Elevated | Not crisis yet |
| Consumer credit access | Declining | Fed SLOOS confirms |

### 🟢 GREEN STATUS (Weekly Check)

| Entity | Value | Note |
|--------|-------|------|
| ABS downgrades | Minimal | Watching |

---

## 7. CRITICAL TIMELINE

### Past Events

| Date | Event | Impact |
|------|-------|--------|
| 2018 (approx) | Tricolor fraud scheme begins | Per DOJ indictment |
| Sept 2025 | Tricolor Chapter 7 bankruptcy | ~$2B debt; 25,000 creditors |
| Oct 2025 | PrimaLend Chapter 11 | $286M debt; restructuring |
| Oct 2025 | First Brands double-pledging revealed | Cambridge Associates analysis |
| Dec 2025 | Tricolor executives charged | Chu, Goodgame, Kollar, Seibold |
| Jan 2026 | Kollar, Seibold plead guilty | Cooperating with DOJ |

### Upcoming Critical

| Date | Event | Urgency | Why It Matters |
|------|-------|---------|----------------|
| **June 2026** | First Brands trial | 🟠 ELEVATED | Fraud allegations tested |
| **Ongoing** | DOJ investigation | 🟠 ELEVATED | May expand to other lenders |
| **Q1-Q2 2026** | Warehouse lender audits | 🟠 ELEVATED | May discover additional fraud |
| **Monthly** | Auto ABS deal performance | 🟡 YELLOW | Early warning for cascade |

---

## 8. DATA SOURCES

### Primary

| Source | Content | Frequency |
|--------|---------|-----------|
| **PACER/Court filings** | Bankruptcy proceedings, DOJ charges | As filed |
| **DOJ Press Releases** | Criminal charges, plea agreements | As announced |
| **Bank earnings/8-Ks** | Loss disclosures | Quarterly/As filed |

### Secondary

| Source | Content | Frequency |
|--------|---------|-----------|
| Auto Finance News | Industry coverage | Daily |
| Auto Remarketing | Subprime coverage | Daily |
| Bloomberg/Reuters | Bank exposure | As reported |
| Fed SLOOS | Lending standards | Quarterly |

---

## 9. GLOSSARY

| Term | Definition |
|------|------------|
| **Double-pledging** | Fraudulently pledging same collateral to multiple lenders |
| **Warehouse line** | Credit facility to fund loan origination before securitization |
| **SPV** | Special Purpose Vehicle — legal entity holding loan collateral |
| **Borrowing base** | Eligible collateral determining how much can be borrowed |
| **Chattel paper** | Document evidencing monetary obligation + security interest |
| **ABS** | Asset-Backed Security — securitized auto loans |

---

## 10. INVALIDATION FRAMEWORK

### Thesis Invalidation

| Condition | Confidence Impact |
|-----------|-------------------|
| DOJ finds fraud limited to Tricolor only | Pattern -30% |
| No additional lender failures in 6 months | Contagion -25% |
| Warehouse lenders resume normal operations | Magnitude -20% |
| Bank losses contained to current disclosures | Magnitude -15% |

### Escalation Triggers

| Condition | Action |
|-----------|--------|
| 4th fraud case discovered | URGENT to CARL, REGINALD |
| Bank loss >$500M announced | URGENT to REGINALD, EARNINGS |
| Warehouse lines frozen broadly | URGENT to CARL, LIQUID |
| DOJ announces industry-wide probe | ELEVATED to ALL |

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-26 | Initial skeleton with current fraud cases |

---

*OTTO Domain Skeleton v1.0 | Created: 2026-01-26*
