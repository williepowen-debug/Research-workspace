# EARNINGS DOMAIN SKELETON v1.0

# Purpose: Structural scaffold for LLM domain orientation
# Domain:  Corporate Earnings, Guidance, Margin Trends, Revision Breadth, Sector Analysis
# Agent:   EARNINGS (Corporate Earnings Monitoring Agent)
#
# Version: 1.0
# Created: 2026-01-26
# Updated: 2026-01-26
# Author:  PROME Network

---

## 0. QUICK START

*Load this section for any session. Provides minimum viable orientation.*

### About This Agent

EARNINGS monitors S&P 500 corporate earnings with focus on:
- Earnings beat rates and surprise magnitudes
- Forward guidance trends (raises, maintains, cuts)
- Margin trends and pricing power
- Mag 7 concentration risk
- Sector divergences

**Coordination:** Primary linkages to HENRY (valuation), CARL (consumer sectors), REGINALD (bank earnings)

### Current Thesis

**PRIMARY THESIS: Earnings Resilience But Narrowing**

Corporate earnings remain resilient but increasingly concentrated in tech/AI:

1. **Q4 2025 Growth** → +8.2% blended YoY growth; 10th consecutive growth quarter
2. **Beat Rate Below Average** → 75% beating (vs 78% 5Y avg); surprise +5.3% (vs 7.7% avg)
3. **Guidance Positive** → 47% positive guidance (above 42% avg); constructive
4. **Mag 7 Dominance** → Big 6 tech driving 60%+ of earnings growth
5. **2026 Outlook** → Analysts expect 14.9% EPS growth for CY 2026

**Confidence:** Pattern 85% | Timing 80% | Magnitude 75%
**Status:** MONITORING — Q4 2025 earnings season in progress (~25% reported); Mag 7 Week 1 complete (3 BEAT, 1 MIXED)

**Invalidation Criteria:**
- Beat rate falls below 60% for full quarter
- Guidance cuts exceed 40% of companies
- Mag 7 misses broadly (4+ companies)
- Margin compression >100bps across sectors

### Scenario Framework

| Scenario | Probability | Description | Primary Vector |
|----------|-------------|-------------|----------------|
| **A** | 40% | Earnings growth continues; broadens beyond tech | VX-EARN-001 (Beat Rate) |
| **B** | 35% | Growth continues but concentrated in Mag 7 | VX-EARN-005 (Mag 7) |
| **C** | 20% | Guidance deteriorates; margin pressure | VX-EARN-002 (Guidance) |
| **D** | 5% | Earnings recession emerges | VX-EARN-003 (Revision Breadth) |

### Coordinating Agents

| Agent | Domain | Key Linkages |
|-------|--------|--------------|
| **HENRY** | Historical comparisons | Valuation context; CAPE implications |
| **CARL** | Consumer stress | Consumer sector earnings; retail guidance |
| **REGINALD** | Regional banks | Bank earnings; provision trends |
| **BARON** | Political-financial | Policy-sensitive sectors (energy, defense) |

---

## 1. ENTITY TYPES

### Earnings Metrics

| Metric | Description | Current | Benchmark |
|--------|-------------|---------|-----------|
| **Beat Rate** | % companies beating EPS | 75% | 78% (5Y avg) |
| **Surprise Magnitude** | Actual vs estimate | +5.3% | +7.7% (5Y avg) |
| **Revenue Beat Rate** | % beating revenue | ~70% | ~70% (normal) |
| **Blended Growth** | YoY EPS growth | +8.2% | Positive = expansion |
| **Revision Breadth** | Up revisions / Down | >1.0 = positive | <0.8 = deteriorating |

### Guidance Categories

| Category | Definition | Current Mix |
|----------|------------|-------------|
| **Positive** | Raised or above consensus | 47% (above avg) |
| **In-Line** | Maintained or at consensus | ~35% |
| **Negative** | Cut or below consensus | ~18% |
| **Withdrawn** | No guidance provided | Minimal |

### Sector Breakdown

| Sector | Expected Q4 Growth | Status | Key Watch |
|--------|-------------------|--------|-----------|
| **Technology** | +25%+ | STRONG | AI capex sustainability |
| **Communication Services** | +15%+ | STRONG | Mag 7 component |
| **Financials** | +10% | STABLE | Provisions; NII |
| **Consumer Discretionary** | +5% | MIXED | Spending; margins |
| **Healthcare** | +5% | STABLE | Drug pricing |
| **Industrials** | +3% | STABLE | Capex; orders |
| **Energy** | -5% | WEAK | Commodity prices |
| **Materials** | -3% | WEAK | China demand |

---

## 2. KEY ENTITIES

### Mag 7 (Critical Concentration)

| Company | Report Date | Result | Actual | Significance |
|---------|-------------|--------|--------|--------------|
| **AAPL** | Jan 29 | **BEAT (RECORD)** | +16% rev, +19% EPS | All-time records; China rebound |
| **MSFT** | Jan 28 | **BEAT** | +17% rev, +60% EPS | Azure +39%; AI backbone |
| **META** | Jan 28 | **BEAT** | +24% rev | $115-135B capex guidance |
| **TSLA** | Jan 28 | **MIXED** | -3% rev | Revenue down but profitable |
| **GOOGL** | TBD | PENDING | Expected +15% | Ads; AI competition |
| **AMZN** | Early Feb | PENDING | Expected +20% | AWS; retail margins |
| **NVDA** | Late Feb | PENDING | Expected +50%+ | AI demand; Blackwell |

**Concentration Risk:** Big 6 (ex-TSLA) driving 60%+ of S&P 500 earnings growth. Week 1 results supportive — 3 of 4 beat, 1 mixed.

### Bellwether Companies

| Category | Companies | Signal |
|----------|-----------|--------|
| **Consumer** | WMT, TGT, COST | Spending health |
| **Banks** | JPM, BAC, C | Credit; provisions |
| **Industrial** | CAT, DE, UNP | Capex; economy |
| **Housing** | HD, LOW | Consumer; rates |

---

## 3. TRANSMISSION PATHS

### FLOW-EARN-01: Guidance Cut Cascade

```
Speed: WEEKS
Status: LATENT
Layer: Market-wide

Pathway:
  Multiple companies cut guidance
    → Analyst downgrades follow
    → Forward estimates reduced
    → P/E multiples compress
    → Wealth effect on consumers (→ CARL)
    → Further spending decline
    → More guidance cuts (feedback)

Trigger: >30% of companies cutting guidance; revision breadth <0.8
Current Position: 47% positive guidance; breadth healthy
Historical Precedent: Q1 2020 COVID
```

### FLOW-EARN-02: Mag 7 Miss Cascade

```
Speed: DAYS
Status: LATENT — Armed due to concentration
Layer: Index-level

Pathway:
  3+ Mag 7 companies miss expectations
    → Index earnings growth turns negative
    → Passive fund outflows accelerate
    → Broad market selloff
    → Credit spreads widen
    → Wealth effect hits consumer (→ CARL, HENRY)

Trigger: 3+ Mag 7 misses; combined Mag 7 growth <10%
Current Position: Mag 7 expected +19-25%; concentration risk elevated
Historical Precedent: Q4 2022 tech reckoning
```

### FLOW-EARN-03: Margin Compression Wave

```
Speed: QUARTERS
Status: LATENT
Layer: Corporate

Pathway:
  Input costs rise (labor, materials, tariffs)
    → Margins compress >50bps
    → Companies announce layoffs
    → Consumer sentiment drops
    → Spending declines
    → Revenue misses follow margin misses

Trigger: >40% of S&P report declining margins YoY
Current Position: Margins stable; watching tariff impact
Historical Precedent: 2022 inflation squeeze
Coordination: CARL (layoffs), BARON (tariffs)
```

### FLOW-EARN-04: Bank Provision Spike

```
Speed: IMMEDIATE on earnings
Status: MONITORING
Layer: Financial sector

Pathway:
  Major banks increase provisions >25%
    → Credit deterioration signal
    → Credit spreads widen
    → Lending tightens
    → Corporate refinancing stress
    → More defaults → More provisions (feedback)

Trigger: JPM, BAC, C provisions +25% QoQ; guidance on credit quality
Current Position: Provisions stable; watching consumer credit
Historical Precedent: Q1 2020, pre-GFC
Coordination: REGINALD, CARL
```

---

## 4. THRESHOLDS (Consolidated Tripwires)

**Color Coding:** 🟢 GREEN | 🟡 YELLOW | 🟠 ORANGE | 🔴 RED

### BEAT RATE

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **EPS Beat Rate** | 75% | <72% | <68% | <60% | 🟡 YELLOW (below avg) |
| **Surprise Magnitude** | +5.3% | <5% | <3% | <0% | 🟡 YELLOW (below avg) |

### GUIDANCE

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **Positive Guidance %** | 47% | <42% | <35% | <25% | 🟢 GREEN |
| **Negative Guidance %** | 18% | >25% | >35% | >45% | 🟢 GREEN |

### REVISION BREADTH

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **Up/Down Ratio** | ~1.0 | <0.9 | <0.8 | <0.7 | 🟢 GREEN |

### MAG 7

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **Mag 7 Beat Rate** | TBD (not reported) | <70% | <60% | <50% | PENDING |
| **Mag 7 Combined Growth** | Expected +19-25% | <15% | <10% | <5% | PENDING |

### MARGINS

| Metric | Current | Yellow | Orange | Red | Status |
|--------|---------|--------|--------|-----|--------|
| **Net Margin Trend** | Stable | -25bps | -50bps | -100bps | 🟢 GREEN |

---

## 5. VECTOR REGISTRY

### VX-EARN-001: Earnings Beat Rate

| Field | Value |
|-------|-------|
| **Name** | S&P 500 EPS Beat Rate |
| **Current** | 75% (13% reported) |
| **Status** | 🟡 YELLOW |
| **Confidence** | 75% |
| **Context** | Below 5Y avg (78%) and 10Y avg (76%) |
| **Downstream** | Market sentiment; estimates |

### VX-EARN-002: Guidance Trend

| Field | Value |
|-------|-------|
| **Name** | Forward Guidance Mix |
| **Current** | 47% positive (above avg) |
| **Status** | 🟢 GREEN |
| **Confidence** | 80% |
| **Context** | Constructive; above 42% 5Y avg |
| **Downstream** | Analyst estimates; multiples |

### VX-EARN-003: Revision Breadth

| Field | Value |
|-------|-------|
| **Name** | Estimate Revision Ratio |
| **Current** | ~1.0 (balanced) |
| **Status** | 🟢 GREEN |
| **Confidence** | 75% |
| **Context** | Stable; watching for deterioration |
| **Downstream** | Forward earnings path |

### VX-EARN-004: Margin Trends

| Field | Value |
|-------|-------|
| **Name** | S&P 500 Net Margins |
| **Current** | Stable |
| **Status** | 🟢 GREEN |
| **Confidence** | 70% |
| **Context** | Tariff risk could pressure |
| **Downstream** | Layoffs; pricing power |
| **Coordination** | CARL, BARON |

### VX-EARN-005: Mag 7 Concentration

| Field | Value |
|-------|-------|
| **Name** | Mag 7 Earnings Health |
| **Current** | Expected +19-25% growth |
| **Status** | PENDING (reports upcoming) |
| **Confidence** | 70% |
| **Context** | 60%+ of S&P growth; concentration risk |
| **Downstream** | Index-level impact; passive flows |
| **Coordination** | HENRY |

### VX-EARN-006: Consumer Sector Guidance

| Field | Value |
|-------|-------|
| **Name** | Discretionary/Staples Guidance |
| **Current** | Mixed |
| **Status** | 🟡 YELLOW |
| **Confidence** | 70% |
| **Context** | WMT, TGT reports critical |
| **Downstream** | Consumer spending signal |
| **Coordination** | CARL |

### VX-EARN-007: Bank Earnings/Provisions

| Field | Value |
|-------|-------|
| **Name** | Financial Sector Health |
| **Current** | Stable provisions |
| **Status** | 🟢 GREEN |
| **Confidence** | 75% |
| **Context** | Watching consumer credit commentary |
| **Downstream** | Credit availability |
| **Coordination** | REGINALD |

---

## 6. CURRENT WATCHLIST (Jan 26, 2026)

### 🔴 RED STATUS
*None currently*

### 🟠 ORANGE STATUS (24-Hour Watch)
*None currently*

### 🟡 YELLOW STATUS (Daily Monitor)

| Entity | Value | Note |
|--------|-------|------|
| Beat Rate | 75% | Below 5Y avg; early season |
| Surprise Magnitude | +5.3% | Below 5Y avg |
| Consumer Guidance | Mixed | Watch WMT, TGT |

### 🟢 GREEN STATUS (Weekly Check)

| Entity | Value | Note |
|--------|-------|------|
| Positive Guidance | 47% | Above average |
| Blended Growth | +8.2% | 10th consecutive quarter |
| Revision Breadth | ~1.0 | Balanced |
| 2026 EPS Growth | +14.9% expected | Constructive |

### PENDING (Reports Upcoming)

| Entity | Report Window | Significance |
|--------|---------------|--------------|
| Mag 7 | Late Jan - Feb | Index-level impact |
| JPM, BAC | Completed | Provisions stable |
| WMT, TGT | Feb | Consumer barometer |

---

## 7. EARNINGS CALENDAR

### Q4 2025 Season Timeline

| Period | Status | Key Events |
|--------|--------|------------|
| **Jan 13-24** | EARLY | Banks reported; 13% complete |
| **Jan 26 - Feb 27** | PEAK | 1,000+ reports/week |
| **Feb 26** | BUSIEST | 855 companies expected |
| **Mar** | LATE | Stragglers |

### Key Upcoming Reports

| Date | Company | Sector | Watch For |
|------|---------|--------|-----------|
| Late Jan | MSFT | Tech | Cloud; AI capex |
| Late Jan | AAPL | Tech | China; services |
| Late Jan | META | Tech | Ads; efficiency |
| Late Jan | TSLA | Auto | Margins; volumes |
| Early Feb | AMZN | Tech/Retail | AWS; retail |
| Late Feb | NVDA | Tech | AI demand |

---

## 8. DATA SOURCES

### Primary

| Source | Content | Frequency |
|--------|---------|-----------|
| **FactSet** | Beat rates, estimates, guidance | Weekly |
| **Bloomberg** | Earnings, revisions | Real-time |
| **Company Filings** | Actuals, guidance | As reported |

### Secondary

| Source | Content | Frequency |
|--------|---------|-----------|
| Refinitiv | Estimates | Daily |
| Seeking Alpha | Analysis | Daily |
| Earnings Whispers | Expectations | Pre-earnings |

---

## 9. GLOSSARY

| Term | Definition |
|------|------------|
| **Beat Rate** | % of companies exceeding EPS estimates |
| **Surprise** | (Actual - Estimate) / Estimate |
| **Blended Growth** | Mix of actual (reported) and estimated (unreported) |
| **Revision Breadth** | Ratio of upward to downward estimate revisions |
| **Guidance** | Company's forward-looking statements on earnings |
| **Mag 7** | AAPL, MSFT, GOOGL, AMZN, NVDA, META, TSLA |

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-26 | Initial skeleton with Q4 2025 data |
| 1.1 | 2026-01-30 | Session 001: Mag 7 Week 1 results (AAPL, MSFT, META, TSLA); confidence upgraded |

---

*EARNINGS Domain Skeleton v1.1 | Updated: 2026-01-30*
