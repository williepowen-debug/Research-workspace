# RP-HEN-1.2: Passive Investing Dominance

**Prompt ID:** RP-HEN-1.2
**Cluster:** Novel Market Structures
**Priority:** 7
**Created:** 2026-01-26

---

## Context for Research Assistant

HENRY is investigating whether passive investing dominance (index funds + ETFs) fundamentally changes market dynamics and mean reversion patterns. Passive funds now hold over 50% of US equity market capitalization. This concentration of assets in price-insensitive vehicles may impair price discovery and create structural risks during redemption scenarios.

Current HENRY findings for context:
- Top 10 S&P 500 concentration: 38.22% (all-time high)
- Passive flows mechanically increase concentration (cap-weighted buying)
- No historical precedent for markets this dominated by passive strategies

---

## Research Questions

### 1. SCALE OF PASSIVE DOMINANCE
- What percentage of US equity AUM is now in passive vehicles (index funds + ETFs)?
- Breakdown: Index mutual funds vs ETFs vs other passive structures
- Growth trajectory: What was the passive share in 2000, 2010, 2020, today?
- Monthly/annual net flow rates into passive vehicles
- Which firms dominate? (Vanguard, BlackRock, State Street market share)

### 2. PRICE DISCOVERY IMPLICATIONS
- Academic research on passive investing and price discovery
  - Cite Greenwood & Thesmar, Israeli, etc.
- "Index inclusion effect" - what happens when a stock enters S&P 500?
- Are stock prices less informationally efficient due to passive dominance?
- Evidence of reduced analyst coverage or active manager influence?
- Does passive dominance increase correlation between stocks?

### 3. CONCENTRATION FEEDBACK LOOP
- Explain the mechanical concentration effect:
  - If NVDA is 7% of SPX, every $1 into SPY puts $0.07 into NVDA regardless of valuation
- Quantify: How much of the concentration increase (from 27% in 2000 to 38% today) is attributable to passive flows vs fundamental outperformance?
- Does passive create "momentum on steroids" - winners keep winning mechanically?
- Research on passive flows and factor tilts

### 4. LIQUIDITY & REDEMPTION SCENARIOS
- ETF liquidity mismatch: Are ETFs promising daily liquidity on less liquid underlyings?
- What happened during March 2020 COVID crash with ETF discounts/premiums?
- Model a scenario: 2008-level redemption rates applied to current passive AUM
  - What is the mechanical selling pressure?
  - Can authorized participants keep up with creation/redemption?
- Bond ETF risks vs equity ETF risks
- "Doom loop" scenarios in academic literature

### 5. HISTORICAL PRECEDENT
- Has any major market ever been >50% passive/index?
- Japan's Government Pension Investment Fund (GPIF) - lessons?
- What does market microstructure research say about stability at high passive %?
- Are there theoretical limits to passive share before price discovery breaks?

### 6. STRUCTURAL BID HYPOTHESIS
- Do passive flows create a "permanent bid" that alters mean reversion?
- Quantify the consistent inflow: 401k auto-enrollment, pension contributions
- Does this structural demand change the equilibrium valuation level?
- Counter-argument: Does it just compress the time between corrections?

### 7. ACTIVE MANAGER ECOSYSTEM
- What percentage of trading volume is still active managers?
- Are there "enough" active managers for price discovery?
- Hedge fund AUM trends - is smart money shrinking?
- Market making capacity relative to passive AUM

---

## Output Format Requested

```markdown
# Passive Investing Dominance - Research Output

## Executive Summary
[Key findings in 3-5 bullets]

## 1. Scale & Market Share
[Current passive %, growth trajectory, major players]

## 2. Price Discovery Impact
[Academic findings, index effect evidence]

## 3. Concentration Mechanics
[Quantified feedback loop analysis]

## 4. Redemption Risk Assessment
[Stress scenarios, liquidity analysis]

## 5. Historical Context
[Precedents and theoretical limits]

## 6. Structural Bid Analysis
[Does passive change mean reversion?]

## 7. Active Ecosystem Health
[Is there enough active management for stability?]

## Risk Assessment Matrix
| Risk | Likelihood | Impact | Timeframe |
|------|------------|--------|-----------|

## Monitoring Metrics for HENRY
[What to track ongoing]

## Sources
[URLs and citations]
```

---

## Integration Notes for HENRY

After receiving this research:
- Assess if passive dominance warrants a dedicated vector
- Update mean reversion assumptions in analogue analysis
- Consider passive flow data in forward-looking catalysts
- Document in ML.tsv

---

*Prompt ready for external LLM research*
