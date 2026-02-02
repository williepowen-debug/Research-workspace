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

**Key Transmission Risk:** US credit cycle deterioration → Japan CLO trust NAVs collapse → Forced redemptions → Japan bid disappears → CLO spreads gap wider → Regional bank mark-to-market losses → Deposit flight acceleration. (Note: Japan is BUYING CLOs, not selling — revised per ML-REG-009)

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

## 4. VECTOR STATUS

**Source of truth:** `workbook/VX.tsv`

For all current values, thresholds, and status: load VX.tsv directly.

### Quick Summary (as of 2026-02-01)
| Status | Count |
|--------|-------|
| GREEN | 14 |
| ORANGE | 10 |
| YELLOW | 4 |
| GAP | 1 |

### Key ORANGE Signals
- **VX-REG-2.03** BDC NAV: -16% discount
- **VX-REG-11.03** DC UCFE Claims: +543% YoY
- **VX-REG-11.04** EGBN Deposits: -4% QoQ
- **VX-REG-9.01-9.04** CRE extend-and-pretend indicators

### Federal Employment Context (Layer 11)

**AUB (Atlantic Union Bank - NYSE: AUB)** — YELLOW
- Acquired Sandy Spring Bank (April 2025) — $14.4B assets
- Combined: $38B assets, 175 branches in VA/MD/NC/DC
- **Sold $2B CRE to Blackstone (June 2025)** — de-risking signal
- **Watch:** Q1/Q2 2026 credit quality, mortgage DQ in DC/MD/VA

**EGBN (Eagle Bancorp - NASDAQ: EGBN)** — ORANGE
- Pure DC/NoVA/MD, $10.5B assets
- **Dedicated government contractor lending** (government.eaglebankcorp.com)
- **ALREADY IN CRISIS:** Q3 2025 -$67.5M loss, CEO retiring, dividend $0.01
- Q4 2025: Deposits -4% QoQ (flight signal)
- **Watch:** Deposit trends, government contractor commentary

---

## 5. CROSS-AGENT SIGNALS

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

## 6. DATA SOURCES

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

## 7. GLOSSARY

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
| 1.1 | 2026-02-01 | Consolidated status tracking to VX.tsv; added federal employment channel |

---

*End of REGINALD Domain Skeleton v1.1*
