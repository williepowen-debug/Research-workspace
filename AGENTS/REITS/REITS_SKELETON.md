# REITS DOMAIN SKELETON v1.0

# Purpose: Structural scaffold for LLM domain orientation
# Domain:  REIT Markets, Sector Exposure, NAV Discounts, Dividend Coverage, Rate Sensitivity
# Agent:   REITS (Real Estate Investment Trust Monitoring Agent)
#
# Version: 1.0
# Created: 2026-01-26
# Updated: 2026-01-26
# Author:  PROME Network

---

## 0. QUICK START

*Load this section for any session. Provides minimum viable orientation.*

### About This Agent

REITS monitors publicly traded real estate investment trusts with focus on:
- Sector health (Office, Retail, Residential, Industrial, mREITs)
- NAV discounts/premiums to private market values
- Dividend sustainability and coverage ratios
- Interest rate sensitivity and refinancing risk

**Coordination:** Primary linkages to REGINALD (CRE/bank exposure), LIQUID (rates), CARL (consumer/retail)

### Current Thesis

**PRIMARY THESIS: Rate Sensitivity + Secular Headwinds**

REITs face dual pressures from elevated rates and sector-specific structural challenges:

1. **Office Secular Decline** → WFH/hybrid permanently impaired demand; NAV discounts 30-50%
2. **Rate Sensitivity** → Higher-for-longer compresses valuations across all sectors
3. **mREIT Spread Pressure** → Book value volatility but recent outperformance (+40% AGNC)
4. **Value Opportunity** → Public REITs trade at significant discounts to private values

**Confidence:** Pattern 75% | Timing 70% | Magnitude 70%
**Status:** MONITORING — Sector in transition

**Invalidation Criteria:**
- Office vacancy rates decline to <15% nationally
- Fed cuts rates 200+ bps and REIT valuations normalize
- mREIT book values stabilize for 4+ consecutive quarters
- Private market cap rates converge with public implied rates

### Scenario Framework

| Scenario | Probability | Description | Primary Vector |
|----------|-------------|-------------|----------------|
| **A** | 30% | Rate cuts drive REIT recovery | VX-REITS-001 (VNQ) |
| **B** | 35% | Bifurcation continues (quality vs distressed) | VX-REITS-002 (Office) |
| **C** | 25% | Credit stress triggers dividend cuts | VX-REITS-004 (Div Coverage) |
| **D** | 10% | Office REIT restructurings/bankruptcies | VX-REITS-002 (Office) |

### Coordinating Agents

| Agent | Domain | Key Linkages |
|-------|--------|--------------|
| **REGINALD** | Regional banks/CRE | Bank CRE exposure; CMBS delinquency; loan modifications |
| **LIQUID** | Treasury/funding | Rate sensitivity; refinancing costs |
| **CARL** | Consumer stress | Retail REIT foot traffic; residential rent growth |
| **MARCO** | Regional stress | FL/TX property market exposure |

---

## 1. ENTITY TYPES

### REIT Sectors

| Sector | Key Names | Current Status | Primary Risk |
|--------|-----------|----------------|--------------|
| **Office** | SLG, BXP, VNO | DISTRESSED | WFH secular; NAV discount 30-50% |
| **Retail** | SPG, KIM, O | MIXED | Consumer spending; bifurcation |
| **Residential** | EQR, AVB, AMH | STABLE | Rent growth moderating; supply |
| **Industrial** | PLD, STAG | STRONG | E-commerce tailwind |
| **Data Center** | EQIX, DLR | STRONG | AI/cloud demand |
| **mREIT** | AGNC, NLY, STWD | RECOVERING | Spread volatility; book value |

### Key Metrics by Sector

| Metric | Description | Significance |
|--------|-------------|--------------|
| **NAV Discount/Premium** | Stock price vs private market value | Valuation signal |
| **FFO/AFFO** | Funds from operations | Earnings power |
| **Dividend Coverage** | FFO / Dividend | Sustainability signal |
| **Cap Rate Spread** | Implied cap rate vs Treasuries | Relative value |
| **Debt Maturity** | Upcoming refinancing | Liquidity risk |
| **Occupancy** | % leased | Demand indicator |

---

## 2. SECTOR DEEP DIVE

### Office REITs (HIGH RISK)

**Current State:**
- SLG: $46 (down 29% YoY); large NAV discount; Manhattan focused
- BXP: $72 (down 21% YoY); "premier workplace" strategy; 86% occupancy
- VNO: $40; NYC/Chicago concentrated

**Key Dynamics:**
- Hybrid work permanently reduced demand
- Class A outperforming Class B/C (flight to quality)
- Tariff concerns adding pressure (potential layoffs reduce demand)
- Leasing improving but from depressed base

**Transmission to REGINALD:** Office CMBS delinquency at 11%+ signals bank CRE stress

### Mortgage REITs (RATE SENSITIVE)

**Current State:**
- AGNC: $11.66; book value $8.28; yield 12.4%; +40% 1Y return
- NLY: $21.80; yield 12.8%; trading at 0.98x book
- Sector outperformed despite rate volatility

**Key Dynamics:**
- Agency mREITs benefiting from spread stability
- Book value volatility remains (6% swing quarter-to-quarter normal)
- Share buyback programs active (AGNC $1B, NLY $1.5B)
- Dividend sustainability improved but not guaranteed

**Transmission to LIQUID:** mREIT stress = forced selling of agency MBS

### Retail REITs (CONSUMER LINKED)

**Current State:**
- SPG (Simon): Premium malls; Class A focus
- KIM (Kimco): Strip centers; grocery-anchored
- O (Realty Income): Net lease; diversified

**Key Dynamics:**
- Foot traffic trends critical (link to CARL)
- Bifurcation: Class A malls stable, Class B/C struggling
- E-commerce adaptation ongoing

**Transmission to CARL:** Retail REIT performance = consumer spending barometer

---

## 3. TRANSMISSION PATHS

### FLOW-REITS-01: Rate Shock Cascade

```
Speed: WEEKS to MONTHS
Status: LATENT
Layer: Sector-wide

Pathway:
  Fed hawkish surprise OR long rates spike
    → REIT valuations compress (yield comparison)
    → Refinancing costs spike
    → Dividend coverage deteriorates
    → Dividend cuts announced
    → Forced selling by income funds
    → NAV discounts widen further

Trigger: 10Y Treasury >5% sustained; cap rate spread <100bps
Current Position: 10Y at ~4.5%; spread adequate
Historical Precedent: 2022 rate shock
```

### FLOW-REITS-02: Office Capitulation

```
Speed: MONTHS
Status: ELEVATED — Building
Layer: Office sector

Pathway:
  Office vacancy continues rising
    → NOI declines accelerate
    → Dividend cuts / suspensions
    → NAV discount exceeds 50%
    → Debt covenant breaches
    → Restructuring / bankruptcy filings
    → CRE loan losses hit banks (→ REGINALD)

Trigger: Major office REIT dividend cut; NAV discount >50%
Current Position: SLG/VNO trading at large discounts; stressed but functioning
Historical Precedent: 2009 REIT crisis
```

### FLOW-REITS-03: mREIT Spread Compression

```
Speed: DAYS to WEEKS
Status: LATENT
Layer: mREIT sector

Pathway:
  MBS spreads widen sharply
    → mREIT book values decline
    → Dividend cut announced
    → Retail investors exit
    → Forced MBS selling
    → Spreads widen further (feedback)
    → Agency MBS market stress

Trigger: mREIT book value -15% in quarter; dividend cut
Current Position: Book values recently stable; dividends maintained
Historical Precedent: 2020, 2022
```

---

## 4. THRESHOLDS (Consolidated Tripwires)

**Color Coding:** 🟢 GREEN | 🟡 YELLOW | 🟠 ORANGE | 🔴 RED

### BROAD SECTOR (VNQ)

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **VNQ Price** | $90.54 | <$85 | <$80 | <$75 | 🟢 GREEN |
| **VNQ YTD Return** | +2.3% | <0% | <-5% | <-10% | 🟢 GREEN |
| **Sector 2025 Return** | -3.6% | Negative | <-10% | <-15% | 🟡 YELLOW |

### OFFICE REITs

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **SLG Price** | $46 | <$40 | <$35 | <$30 | 🟡 YELLOW |
| **Office NAV Discount** | 30-40% | >40% | >50% | >60% | 🟠 ORANGE |
| **Office Vacancy** | ~20% | >22% | >25% | >30% | 🟠 ORANGE |

### mREITs

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **AGNC Book Value** | $8.28 | <$8.00 | <$7.50 | <$7.00 | 🟢 GREEN |
| **AGNC Price/Book** | 1.07x | <1.0x | <0.90x | <0.80x | 🟢 GREEN |
| **mREIT Dividend Cut** | None recent | 1 major | 2+ major | Sector-wide | 🟢 GREEN |

### DIVIDEND COVERAGE

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **Sector Avg Coverage** | ~1.2x | <1.1x | <1.0x | <0.9x | 🟢 GREEN |
| **Office Coverage** | ~1.0x | <0.95x | <0.90x | <0.85x | 🟡 YELLOW |

---

## 5. VECTOR REGISTRY

### VX-REITS-001: Broad Sector Health (VNQ)

| Field | Value |
|-------|-------|
| **Name** | VNQ REIT ETF |
| **Current** | $90.54 |
| **Status** | 🟢 GREEN |
| **Confidence** | 80% |
| **Key Metrics** | YTD +2.3%; 2025 -3.6%; yield 3.9% |
| **Downstream** | Sector sentiment; flows |

### VX-REITS-002: Office REIT Stress

| Field | Value |
|-------|-------|
| **Name** | Office REIT NAV/Performance |
| **Current** | NAV discount 30-40%; SLG -29% YoY |
| **Status** | 🟠 ORANGE |
| **Confidence** | 85% |
| **Key Metrics** | Vacancy ~20%; leasing improving but weak |
| **Downstream** | CRE stress; bank exposure |
| **Coordination** | REGINALD (CRE) |

### VX-REITS-003: mREIT Book Value

| Field | Value |
|-------|-------|
| **Name** | Mortgage REIT Health |
| **Current** | AGNC BV $8.28; +6% QoQ |
| **Status** | 🟢 GREEN |
| **Confidence** | 75% |
| **Key Metrics** | AGNC +40% 1Y; NLY +17% 1Y; dividends maintained |
| **Downstream** | Agency MBS market; LIQUID funding |
| **Coordination** | LIQUID |

### VX-REITS-004: Dividend Coverage

| Field | Value |
|-------|-------|
| **Name** | REIT Dividend Sustainability |
| **Current** | ~1.2x sector avg; office ~1.0x |
| **Status** | 🟡 YELLOW |
| **Confidence** | 70% |
| **Key Metrics** | Office coverage thin; other sectors adequate |
| **Downstream** | Income fund flows; forced selling |

### VX-REITS-005: Cap Rate Spread

| Field | Value |
|-------|-------|
| **Name** | REIT Relative Value |
| **Current** | Implied cap 7.7% vs Treasuries |
| **Status** | 🟢 GREEN |
| **Confidence** | 75% |
| **Key Metrics** | Spread attractive; value opportunity |
| **Downstream** | Valuation signal |

### VX-REITS-006: Retail REIT Health

| Field | Value |
|-------|-------|
| **Name** | Retail REIT Performance |
| **Current** | SPG stable; bifurcation ongoing |
| **Status** | 🟢 GREEN |
| **Confidence** | 70% |
| **Key Metrics** | Foot traffic, same-store NOI |
| **Downstream** | Consumer spending signal |
| **Coordination** | CARL |

---

## 6. CURRENT WATCHLIST (Jan 26, 2026)

### 🔴 RED STATUS
*None currently*

### 🟠 ORANGE STATUS (24-Hour Watch)

| Entity | Value | Threshold | Note |
|--------|-------|-----------|------|
| **Office NAV Discount** | 30-40% | >50% | SLG, VNO deeply discounted |
| **Office Vacancy** | ~20% | >25% | Secular pressure continues |

### 🟡 YELLOW STATUS (Daily Monitor)

| Entity | Value | Note |
|--------|-------|------|
| SLG Stock | $46 | Down 29% YoY; watch for dividend action |
| Office Div Coverage | ~1.0x | Thin; vulnerable |
| Sector 2025 Return | -3.6% | Underperformed |

### 🟢 GREEN STATUS (Weekly Check)

| Entity | Value | Note |
|--------|-------|------|
| VNQ | $90.54 | YTD +2.3% |
| AGNC Book Value | $8.28 | +6% QoQ; stable |
| mREIT Performance | +40% (AGNC) | Outperforming |
| Cap Rate Spread | 7.7% implied | Value opportunity |

---

## 7. DATA SOURCES

### Primary

| Source | Content | Frequency |
|--------|---------|-----------|
| Company Filings | FFO, NAV, guidance | Quarterly |
| Green Street | NAV estimates, cap rates | Monthly |
| NAREIT | Sector data | Monthly |

### Secondary

| Source | Content | Frequency |
|--------|---------|-----------|
| Placer.ai | Retail foot traffic | Weekly |
| CoStar | Office vacancy | Monthly |
| FRED | Treasury yields | Daily |

---

## 8. GLOSSARY

| Term | Definition |
|------|------------|
| **FFO** | Funds From Operations — REIT earnings metric |
| **AFFO** | Adjusted FFO — FFO minus maintenance capex |
| **NAV** | Net Asset Value — private market value of properties |
| **Cap Rate** | NOI / Property Value — yield on real estate |
| **mREIT** | Mortgage REIT — invests in mortgages, not properties |
| **Book Value** | mREIT net assets per share |

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-26 | Initial skeleton with current data |

---

*REITS Domain Skeleton v1.0 | Created: 2026-01-26*
