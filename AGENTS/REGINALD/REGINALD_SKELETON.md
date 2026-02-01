# REGINALD DOMAIN SKELETON v1.0

# Purpose: Structural scaffold for LLM domain orientation
# Domain:  Regional Banks, CRE Exposure, CLO Holdings, BDC Credit,
#          Deposit Flows, Hidden Leverage Transmission
# Agent:   REGINALD (Regional Banks/Credit Monitoring Agent)
#
# Version: 1.0
# Created: 2026-01-25
# Author:  SAM Network Enhancement
#
# Usage:
#   - Load this file at the start of any REGINALD session
#   - Provides entity types, relationship vocabulary, core architecture
#   - Thresholds define tripwires for escalation
#
# Methodology Compliance: Aligned with CARL Methodology Skeleton v0.2

---

## 0. QUICK START

*Load this section for any session. Provides minimum viable orientation.*

### About This System

A **session** is one continuous LLM interaction window. Sessions are numbered sequentially (REGINALD-I, REGINALD-II, etc.). At session end, handoff documents transfer context to the next session.

**Two Documents:**
- **Domain skeleton** (this document): Defines *what* REGINALD monitors — entities, vectors, glossary, thresholds
- **Methodology skeleton** (separate): Governs *how* to operate — principles, protocols, templates

Load both at session start.

### Current Thesis

**PRIMARY THESIS: Hidden Leverage Concentration**

US regional banks face concentrated exposure to CRE and shadow banking:
1. **CRE CONCENTRATION** — Regional banks hold 80%+ of CRE loans, many underwater
2. **CLO EXPOSURE** — Some regionals have significant CLO holdings (marks vulnerable)
3. **BDC LINES** — Hidden credit lines to BDCs create liquidity risk
4. **DEPOSIT FRAGILITY** — Post-SVB deposit flight risk persists

**Key Transmission Risk:** Japan CLO selling (Norinchukin) → CLO spread widening → Regional bank mark-to-market losses → Deposit flight acceleration.

**Confidence:** Pattern 80% | Timing 65% | Magnitude 75%
**Status:** MONITORING — Elevated CRE delinquency, watching CLO transmission

### Coordinating Agents

| Agent | Domain | State Vector Exchange |
|-------|--------|----------------------|
| **SAM** | Japan Sovereign, CLO Nuclear | VX-REG ↔ CLO spreads, Norinchukin |
| **LIQUID** | Treasury/Funding, FHLB | VX-REG ↔ Bank funding stress |
| **MASTER** | Cross-Domain Synthesis | Receives REGINALD bank stress indicators |

### Session Type Routing

| Session Type | Load Sections | Purpose |
|--------------|---------------|---------|
| Update | 0, 4 (thresholds) | Ingest new data, update logs |
| Analysis | 0, 3, 4 | Deep dive on specific bank/sector |
| Crisis | 0, 4, 6 | Active bank stress monitoring |
| Reconciliation | 0, 4 | Cross-reference audit, cleanup |
| Handoff | Full skeleton | Explicit knowledge transfer |

---

## 1. ENTITY TYPES

*The vocabulary of the domain. Every node belongs to exactly one entity type.*

### Regional Banks

**Category A: Super-Regionals** (Assets $50B-$500B)
- Examples: US Bancorp, PNC, Truist
- Systemic relevance: Moderate-High
- Stress indicator: Stock price, CDS if available

**Category B: Mid-Size Regionals** (Assets $10B-$50B)
- Examples: Zions, Comerica, KeyCorp
- CRE concentration: HIGH (often 30%+ of loans)
- Stress indicator: Stock price, deposit flows

**Category C: Small Regionals** (Assets <$10B)
- Count: 4,000+ institutions
- Regulatory: State-level, less scrutiny
- Stress indicator: Call Report data (quarterly lag)

### CRE Exposure

| Property Type | Risk Level | Regional Concentration |
|---------------|------------|------------------------|
| Office | HIGH | Major metros (NYC, SF, Chicago) |
| Multifamily | MEDIUM | Sunbelt overbuilt |
| Retail | MEDIUM-HIGH | Secondary markets |
| Industrial | LOW | Logistics demand supports |

### Shadow Banking Entities

**CLOs (Collateralized Loan Obligations)**
- AAA spread: 125bps current (threshold: 150 yellow, 180 red)
- Regional bank exposure: Variable (call report data)
- Transmission from Japan: Norinchukin price-setter

**BDCs (Business Development Companies)**
- Combined exposure: $142B unfunded commitments
- Credit lines from regional banks: Significant (opaque)
- Stress trigger: CLO/credit spread widening

---

## 2. RELATIONSHIP TYPES

*How entities connect. Every edge has exactly one relationship type.*

### Lending Relationships
- `lends_CRE`: Bank has CRE loan exposure
- `lends_C&I`: Bank has commercial & industrial exposure
- `credit_line`: Bank provides unfunded commitment (to BDC, etc.)

### Funding Relationships
- `deposit_base`: Bank funds via deposits
- `FHLB_member`: Bank can borrow from FHLB
- `repo_funding`: Bank uses repo for liquidity

### Stress Relationships
- `transmits`: Stress propagates (CLO spreads → bank marks)
- `amplifies`: Second-order factor (deposit flight amplifies CRE stress)
- `draws`: Commitment is activated (BDC draws credit line)

---

## 3. TRANSMISSION PATHS (Named Cascade Routes)

*Documented pathways for regional bank stress propagation.*

### FLOW-REG-1.01 — CLO Transmission Path

```
Speed: DAYS
Status: LATENT — Awaiting CLO stress trigger
Layer: 1 (Mark-to-Market)

Pathway:
  Norinchukin Forced Selling (SAM monitors)
    → CLO AAA Spreads Widen (>150bps Yellow, >180bps Red)
    → Regional Bank CLO Holdings Mark Down
    → Capital Ratios Compressed
    → Market Panic / Deposit Flight Risk
    → Bank Forced to Raise Capital or Sell Assets

Trigger: CLO AAA >150bps sustained
Current Position: 125bps (25bps cushion)
Key Insight: Japan → US transmission in hours/days
```

### FLOW-REG-2.01 — CRE Doom Loop

```
Speed: QUARTERS
Status: ACTIVE (slow burn)
Layer: 2 (Credit Quality)

Pathway:
  Office Property Values Decline
    → CRE Loan-to-Value Ratios Deteriorate
    → Loan Modifications / Extensions Fail
    → Non-Performing Loans Increase
    → Loan Loss Provisions Rise
    → Earnings Collapse
    → Stock Price Decline → Deposit Flight

Trigger: CRE DQ >5% (Orange), >7% (Red)
Current Position: Monitoring — TBD from FRED data
Key Insight: Slow-moving but large exposure
```

### FLOW-REG-3.01 — BDC Credit Line Cascade

```
Speed: DAYS (when triggered)
Status: LATENT — Chained to FLOW-REG-1.01
Layer: 3 (Hidden Leverage)

Pathway:
  Credit Stress Event (CLO spreads, recession)
    → BDC Portfolio Losses (mark-to-market)
    → BDCs Draw Bank Credit Lines ($142B unfunded / ~45% = $64B)
    → Bank Liquidity Drain (exactly when banks need cash)
    → Banks Forced to Tap FHLB / Sell Assets
    → [Feedback to LIQUID agent on FHLB stress]

Trigger: CLO AAA >165bps (BDC mark-downs begin)
Current Position: LATENT — awaiting CLO trigger
Key Insight: Hidden second-order effect
```

### FLOW-REG-4.01 — Deposit Flight Cascade

```
Speed: HOURS (in acute phase)
Status: LATENT — Post-SVB vigilance
Layer: 1 (Funding)

Pathway:
  Bank Stress Signal (earnings miss, CRE loss, stock drop)
    → Depositor Panic (>FDIC limit at risk)
    → Deposit Outflows (digital-age bank run)
    → Bank Liquidity Crisis
    → FHLB Advance Surge
    → [Transmission to LIQUID]

Trigger: Any regional bank stock -20% in day
Current Position: LATENT
Key Insight: Social media accelerates runs
```

---

## 4. THRESHOLDS (Consolidated Tripwires)

*All escalation thresholds. Initial values as of 2026-01-25.*

**Color Coding:** GREEN = Normal | YELLOW = Watch | ORANGE = Alert | RED = Critical

### SECTOR HEALTH INDICATORS

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-REG-1.01 | KRE ETF Price | $67.61 (-5%) | -10% | -15% | -20% | GREEN |
| VX-REG-1.02 | Regional Bank CDS | TBD | Research | Research | Research | GAP |

### CONCENTRATION BELLWETHERS

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-REG-6.01 | RF (Regions Financial) | $28.60 (-1%) | -10% | -15% | -20% | GREEN |
| VX-REG-6.02 | **VLY (Valley National)** | $11.90 (-2%) | -10% | -15% | -20% | GREEN |
| VX-REG-6.03 | FLG (Flagstar/NYCB) | $13.10 (-5%) | -10% | -15% | -20% | GREEN |
| VX-REG-6.04 | WAL (Western Alliance) | $88.00 (-7%) | -10% | -15% | -20% | GREEN |
| VX-REG-6.05 | CFG (Citizens Financial) | $64.00 (high) | -10% | -15% | -20% | GREEN |
| VX-REG-6.06 | CMA (Comerica) | $95.00 (merger) | -10% | -15% | -20% | GREEN |
| VX-REG-6.07 | KEY (KeyCorp) | $21.20 (-3%) | -10% | -15% | -20% | GREEN |
| VX-REG-6.08 | ZION (Zions) | $60.50 (-2%) | -10% | -15% | -20% | GREEN |
| VX-REG-6.09 | **AUB (Atlantic Union)** | ~$37.00 | -10% | -15% | -20% | **YELLOW** |

### FEDERAL EMPLOYMENT EXPOSURE (NEW - Added 2026-02-01)

*Banks with significant exposure to federal employment metros. DOGE cuts create new transmission channel.*

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-REG-11.01 | **AUB Federal Metro Exposure** | HIGH | UCFE +200% | UCFE +400% | Credit losses rise | **YELLOW** |
| VX-REG-11.02 | DC Metro Unemployment | 3.5% | >4.5% | >5.5% | >6.5% | GREEN (lagging) |
| VX-REG-11.03 | DC UCFE Claims YoY | +543% | +200% | +400% | +600% | **ORANGE** |

**AUB Context (Atlantic Union Bank - NYSE: AUB):**
- Acquired Sandy Spring Bank (April 2025) — $14.4B assets, leading MD regional
- Combined: $38B assets, 175 branches in VA/MD/NC/DC
- **Sold $2B CRE to Blackstone (June 2025)** — de-risking signal
- Management claims "defense focus" insulates them — skeptical
- **LABOR→REGINALD transmission channel:** Federal job losses → mortgage/consumer stress → credit losses
- **Watch:** Q1/Q2 2026 credit quality, mortgage DQ in DC/MD/VA, further CRE sales

### SYSTEMIC AMPLIFIERS

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-REG-7.01 | FHLB System Advances | Baseline | $700B | $750B | $800B | GREEN |
| VX-REG-7.02 | FHLB Collateral Haircuts | Baseline | +5% | +10% | +15% | GREEN |

### REGIONAL CATALYSTS

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-REG-8.01 | HOA/Condo Assessments | Active | >$5K/door | >$10K/door | >$15K/door | ORANGE |

### ACCOUNTING MANIPULATION / EXTEND-AND-PRETEND

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-REG-9.01 | CRE Modification Wave | $7.7B+ | >$10B | >$15B | >$20B | ORANGE |
| VX-REG-9.02 | Modification Exhaustion | Active | 2nd mod >30% | >40% | >50% | ORANGE |
| VX-REG-9.03 | Open-End CRE Fund NAV | $130-217B | Queue >10% | >15% | >20% | ORANGE |
| VX-REG-9.04 | BDC PIK Inflation | Golub 173% | PIK >15% | >20% | >25% | ORANGE |

### FUNDING STRESS INDICATORS

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-REG-10.01 | Deposit Composition | Monitoring | Uninsured >40% | >50% | >60% | YELLOW |
| VX-REG-10.02 | NIM Compression | Monitoring | -5bps QoQ | -10bps | -15bps | YELLOW |

### ASSET QUALITY

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-REG-2.01 | Regional CLO Holdings | TBD | Research | Research | Research | GAP |
| VX-REG-2.02 | CLO AAA Spreads | ~115bps | 150bps | 165bps | 180bps | GREEN |
| VX-REG-2.03 | BDC NAV Discount | TBD | >10% | >15% | >20% | TBD |
| VX-REG-3.01 | CRE Loan 90+ DQ | TBD | >3% | >5% | >7% | TBD |

### FUNDING/DEPOSIT

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-REG-4.01 | Deposit Flight Rate | TBD | -2% QoQ | -4% | -6% | TBD |

### JAPAN REGIONAL BANK EXPOSURE

| Vector | Metric | Current | Yellow | Orange | Red | Status |
|--------|--------|---------|--------|--------|-----|--------|
| VX-REG-5.01 | Japan Regional Bank Losses | Unquantified | Research | Research | Research | GAP |

---

## 5. VECTOR REGISTRY

*Full tracking in VX sheet.*

### Layer 1: Sector Health

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-REG-1.01** | KRE Sector Health | GREEN | 85% | $67.61, -5% from high |

### Layer 6: Concentration Bellwethers (Bank Watchlist)

| Vector | Name | Status | Confidence | Key Metric | Primary Risk |
|--------|------|--------|------------|------------|--------------|
| **VX-REG-6.01** | RF Stock | GREEN | 80% | $28.60, -1% from high | CLO concentration ($4.17B) |
| **VX-REG-6.02** | **VLY Stock** | GREEN | 95% | $11.90, -2% from high | **#1 CRISIS BANK: 475% CRE + 6.65% Auto NCO** |
| **VX-REG-6.03** | FLG Stock | GREEN | 89% | $13.10, -5% from high | 2026 maturity wall + $13.9B FHLB |
| **VX-REG-6.04** | WAL Stock | GREEN | 82% | $88.00, -7% from high | Fraud exposure ($98.6M, $0 provision) |
| **VX-REG-6.05** | CFG Stock | GREEN | 75% | $64.00, at high | Fund finance transmission ($10-11B) |
| **VX-REG-6.06** | CMA Stock | GREEN | 79% | $95.00, merger premium | 312% CRE concentration |
| **VX-REG-6.07** | KEY Stock | GREEN | 78% | $21.20, -3% from high | Office NPL + equipment fraud |
| **VX-REG-6.08** | ZION Stock | GREEN | 73% | $60.50, -2% from high | FHLB haircuts + $50M fraud charge |

### Layer 7: Systemic Amplifiers

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-REG-7.01** | FHLB System Advances | GREEN | 90% | Baseline. Peak $675B (2023). Joint & several liability. |
| **VX-REG-7.02** | FHLB Collateral Haircuts | GREEN | 85% | Baseline. 77.2% real estate collateral. |

### Layer 8: Regional Catalysts

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-REG-8.01** | HOA/Condo Assessments | ORANGE | 85% | Active in FL/NV. Super-lien priority. |

### Layer 9: Accounting Manipulation / Extend-and-Pretend

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-REG-9.01** | CRE Modification Wave | ORANGE | 99% | $7.7B+ modified to avoid NPL recognition |
| **VX-REG-9.02** | Modification Exhaustion | ORANGE | 90% | FLG 142bps allowance cut = reverse indicator |
| **VX-REG-9.03** | Open-End CRE Fund NAV | ORANGE | 95% | $130-217B hidden losses, BREIT gated |
| **VX-REG-9.04** | BDC PIK Inflation | ORANGE | 85% | Golub 173% spike, cash NII diverging |

### Layer 10: Funding Stress Indicators

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-REG-10.01** | Deposit Composition | YELLOW | 80% | Tracking uninsured %, brokered CD growth |
| **VX-REG-10.02** | NIM Compression | YELLOW | 82% | Tracking sequential NIM changes |

### Layer 2: Asset Quality

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-REG-2.01** | CLO Holdings | GAP | 60% | Requires call report research |
| **VX-REG-2.02** | CLO Transmission | GREEN | 75% | ~115bps AAA spread (PSQA proxy) |
| **VX-REG-2.03** | BDC Stress | TBD | 65% | NAV discount |
| **VX-REG-3.01** | CRE Delinquency | TBD | 75% | FRED data |

### Layer 4: Funding

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-REG-4.01** | Deposit Stability | TBD | 70% | Call report quarterly |

### Layer 5: Japan Cross-Border

| Vector | Name | Status | Confidence | Key Metric |
|--------|------|--------|------------|------------|
| **VX-REG-5.01** | Japan Regional Bank | GAP | 50% | BOJ FSR research needed |

---

## 6. CURRENT WATCHLIST

### Research Required (Data Gaps)

| Topic | Source Needed | Priority |
|-------|---------------|----------|
| KRE current level | Yahoo Finance | HIGH |
| CRE 90+ DQ rate | FRED | HIGH |
| Regional CLO holdings | Call Reports (FFIEC) | MEDIUM |
| BDC NAV discounts | CEF Connect | MEDIUM |
| Japan regional bank losses | BOJ FSR | LOW (monitor) |

### Cross-Agent Signals to Monitor

| From SAM | Trigger | REGINALD Response |
|----------|---------|-------------------|
| CLO AAA >150bps | Mark-to-market risk | Elevate VX-REG-2.02 |
| Norinchukin stress | CLO selling imminent | Prepare crisis protocols |

| From LIQUID | Trigger | REGINALD Response |
|-------------|---------|-------------------|
| SOFR +25bps | Bank funding cost spike | Monitor deposit flows |
| FHLB stress | System-wide funding | Coordinate crisis response |

---

## 7. DATA SOURCES

### Primary (OSINT)

| Metric | Source | URL | Cadence |
|--------|--------|-----|---------|
| KRE ETF | Yahoo Finance | finance.yahoo.com | Daily |
| CLO Spreads (Proxy) | Palmer Square ETFs | PSQA ticker (AAA); CLOZ is BBB-B | Daily |
| CRE Delinquency | FRED | fred.stlouisfed.org | Quarterly |
| BDC NAV | CEF Connect | cefconnect.com | Daily |

### Regulatory (OSINT - Lagged)

| Metric | Source | Cadence | Lag |
|--------|--------|---------|-----|
| Bank Call Reports | FFIEC | Quarterly | 45 days |
| FHLB Advances | FHLB Annual | Annual | Months |
| Deposit Flows | Call Reports | Quarterly | 45 days |

### Japan (Research Gap)

| Metric | Source | Frequency |
|--------|--------|-----------|
| BOJ Financial System Report | boj.or.jp/en | Semi-annual |
| Regional bank JGB exposure | Individual disclosures | Semi-annual |

---

## 8. GLOSSARY

### Acronyms

| Acronym | Definition |
|---------|------------|
| BDC | Business Development Company |
| C&I | Commercial & Industrial (loans) |
| CDS | Credit Default Swap |
| CLO | Collateralized Loan Obligation |
| CRE | Commercial Real Estate |
| DQ | Delinquency |
| FHLB | Federal Home Loan Banks |
| KRE | SPDR S&P Regional Banking ETF |
| LTV | Loan-to-Value |
| NAV | Net Asset Value |
| NPA | Non-Performing Assets |

### Key Concepts

**CLO Transmission:** When CLO spreads widen, banks holding CLOs mark positions to market, reducing regulatory capital. This can trigger deposit flight or force asset sales.

**BDC Hidden Leverage:** BDCs have $142B in unfunded credit commitments from banks. In stress, BDCs draw these lines exactly when banks need liquidity — a procyclical accelerant.

**CRE Doom Loop:** Office vacancies rise → property values fall → LTV ratios breach → loan modifications fail → non-performing loans spike → bank earnings collapse → stock falls → deposit flight.

**Deposit Flight Rate:** Post-SVB, depositors (especially >$250K) are hair-trigger. Any stress signal can cause rapid outflows via digital banking.

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-25 | Initial skeleton created |

---

*End of REGINALD Domain Skeleton v1.0*
