# RP-HEN-2.3: Breadth Deterioration Patterns

**Prompt ID:** RP-HEN-2.3
**Cluster:** Timing & Catalysts
**Priority:** 3
**Created:** 2026-01-26

---

## Context for Research Assistant

HENRY tracks market breadth as an indicator of market health. Currently, ~58% of S&P 500 stocks are above their 200-day moving average, which appears healthy. However, market tops are often preceded by breadth deterioration - the index makes new highs while fewer stocks participate. With top 10 concentration at 38.22% (all-time high), the index could remain elevated even as underlying breadth collapses.

Current HENRY findings for context:
- % Above 200 DMA: ~58% (healthy)
- Top 10 Concentration: 38.22% (all-time high)
- EW vs CW Spread: 4.03% YTD (SPY outperforming RSP)
- VIX: 16.07 (complacent)

---

## Research Questions

### 1. CURRENT BREADTH STATE
- Current % of S&P 500 above 200 DMA
- Current % of S&P 500 above 50 DMA
- Current advance/decline line level and trend
- New 52-week highs vs new 52-week lows (ratio)
- McClellan Oscillator and Summation Index readings
- Percentage of stocks in uptrends by sector

### 2. HISTORICAL BREADTH AT TOPS

**1999-2000 Dot-Com:**
- When did the advance/decline line peak relative to the index?
- % above 200 DMA trend in 1999 leading to March 2000 top
- How narrow was leadership at the top?
- Timeline: How many months did breadth deteriorate before index topped?

**2007 Financial Crisis:**
- Advance/decline line behavior in 2007
- % above 200 DMA at October 2007 top
- Breadth divergence timeline
- Did breadth give warning?

**2021-2022:**
- Recent example of breadth deterioration
- When did breadth peak vs index peak?
- How severe was the divergence?
- Lessons for current environment

### 3. DIVERGENCE ANALYSIS
- Define "bearish breadth divergence" precisely
- When index makes new high but breadth doesn't confirm:
  - What is typical lag to index correction?
  - What is typical depth of correction?
- Statistical analysis: Breadth divergence as predictive indicator
- False positives: When did breadth diverge but market kept rising?

### 4. CONCENTRATION CONTEXT
- At 38% top 10 weight, how does this affect breadth signals?
- Can breadth deteriorate significantly while index stays elevated?
- Model: If top 10 rise 10% but other 490 stocks fall 5%, what happens to index vs breadth?
- "Stealth bear market" concept - is this possible currently?
- Equal-weight vs cap-weight as breadth proxy

### 5. SECTOR BREADTH
- Current breadth by sector
- Which sectors have strong breadth? Weak breadth?
- Historical pattern: Do certain sectors lead breadth deterioration?
- Defensive vs cyclical breadth divergence

### 6. SMALL CAP / MID CAP BREADTH
- Russell 2000 breadth vs S&P 500 breadth
- Historical: Do small caps show breadth problems first?
- Current small cap breadth readings
- Mid cap (S&P 400) breadth

### 7. INTERNATIONAL BREADTH CONTEXT
- Global equity breadth (% of countries in uptrends)
- Does US breadth typically lead or lag global?
- Current international breadth readings

### 8. BREADTH THRUST INDICATORS
- Zweig Breadth Thrust - current status
- Other breadth thrust indicators
- Can breadth thrusts occur in late-stage markets?

---

## Output Format Requested

```markdown
# Breadth Deterioration Analysis - Research Output

## Executive Summary
[Current breadth health assessment]

## 1. Current Breadth Dashboard

| Indicator | Current | 3-Month Trend | Signal |
|-----------|---------|---------------|--------|
| % > 200 DMA | | | |
| % > 50 DMA | | | |
| A/D Line | | | |
| New Highs/Lows | | | |
| McClellan Osc | | | |

## 2. Historical Breadth at Tops

### 2000 Top
- A/D Line peaked: [date] ([X months] before index)
- % > 200 DMA at top:
- Leadership narrowing timeline:

### 2007 Top
[Same structure]

### 2022 Top
[Same structure]

## 3. Divergence Statistics
[How predictive is breadth divergence?]

## 4. Concentration Impact Analysis
[How 38% concentration affects breadth interpretation]

## 5. Sector Breadth Matrix

| Sector | % > 200 DMA | Trend | Concern Level |
|--------|-------------|-------|---------------|

## 6. Small/Mid Cap Breadth
[Leading indicator analysis]

## 7. Breadth Warning Checklist

HENRY should escalate if:
- [ ] % > 200 DMA drops below [X]%
- [ ] A/D line diverges for [X] weeks
- [ ] New highs/lows ratio falls below [X]
- [ ] [Other thresholds]

## Data Sources
| Indicator | Source | URL |
|-----------|--------|-----|

## Sources
[Citations]
```

---

## Integration Notes for HENRY

After receiving this research:
- Refine VX-HEN-1.02 thresholds based on historical patterns
- Add advance/decline line tracking
- Create breadth deterioration checklist in FL.tsv
- Consider sector-level breadth vectors

---

*Prompt ready for external LLM research*
