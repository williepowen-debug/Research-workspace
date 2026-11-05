# RP-HEN-6.4: Technical Breadth & Internal Market Health

**Prompt ID:** RP-HEN-6.4
**Cluster:** Data Expansion
**Priority:** 4
**Created:** 2026-02-03

---

## Context for Research Assistant

HENRY already tracks basic breadth (% above 200 DMA) and the Zweig Breadth Thrust. But historical analysis shows that INTERNAL market deterioration often precedes price breaks by months — the 2000 advance-decline line peaked 23 MONTHS before the S&P 500. We need deeper breadth metrics to detect "internal rot" while the index looks healthy.

Current HENRY breadth vectors:
- VX-HEN-1.02: Market Breadth (% >200 DMA): 58.25% (GREEN)
- VX-HEN-1.03: Equal-Weight vs Cap-Weight Spread: 4.03% (YELLOW)
- VX-HEN-7.07: Zweig Breadth Thrust: ACTIVE (GREEN) — bullish signal
- VX-HEN-7.08: Sector Breadth - Tech: 52.85% (ORANGE)

Key HENRY finding: Top 10 stocks = 38.22% of S&P 500. Index can rise while most stocks fall.

---

## Research Questions

### 1. ADVANCE-DECLINE LINE
- What is the NYSE Advance-Decline Line?
- How is it calculated (cumulative advances minus declines)?
- Historical divergences:
  - 2000: A-D peaked March 1998, SPX peaked March 2000 (23 months)
  - 2007: When did A-D diverge?
  - 2015, 2018, 2022: Divergence patterns?
- How to calculate "new highs in price with lower A-D line"?
- Best data source for A-D line (real-time)?

### 2. NEW HIGHS MINUS NEW LOWS
- Definition: NYSE stocks making 52-week highs vs 52-week lows
- How to interpret:
  - Healthy market: Highs >> Lows
  - Deteriorating: Lows expanding while index rises
  - Breadth thrust: Massive highs surge
- Historical thresholds for concern?
- Cumulative NH-NL line vs daily readings?
- Data sources: Barchart, StockCharts, WSJ?

### 3. McCLELLAN OSCILLATOR & SUMMATION INDEX
- McClellan Oscillator: What is it and how calculated?
  - 19-day EMA vs 39-day EMA of advances minus declines
  - Interpretation of readings (+/- ranges)
- McClellan Summation Index: Cumulative oscillator
  - What levels indicate overbought/oversold?
  - Historical extremes and what followed?
- How do these differ from simple A-D line?
- Data sources?

### 4. PERCENT OF STOCKS IN DOWNTRENDS
- % below 50-day MA (short-term trend)
- % below 200-day MA (long-term trend)
- % making new 52-week lows
- % down >20% from 52-week high ("bear market territory")
- How to track by sector and by market cap?
- What thresholds indicate broad weakness?

### 5. SECTOR BREADTH ANALYSIS
- Calculate breadth for each S&P sector:
  - Technology (XLK)
  - Financials (XLF)
  - Energy (XLE)
  - Healthcare (XLV)
  - Consumer Discretionary (XLY)
  - Industrials (XLI)
  - etc.
- What divergences between sector breadth and sector performance matter?
- Current readings by sector?
- How to build a "sector breadth heat map"?

### 6. SMALL CAP VS LARGE CAP BREADTH
- Russell 2000 breadth indicators
- Compare IWM (small cap) breadth to SPY (large cap) breadth
- When do small caps lead? When do they lag?
- Current divergence (Russell 2000 breadth vs S&P 500 breadth)?
- Is small cap weakness a leading indicator?

### 7. VOLUME PATTERNS
- Up volume vs down volume
- Volume on advancing stocks vs declining stocks
- Accumulation/Distribution indicators
- On-Balance Volume (OBV) divergences
- How does volume confirm or contradict breadth?

### 8. BREADTH THRUST INDICATORS
Beyond Zweig, other breadth thrusts:
- Whaley Breadth Thrust
- 10-day A/D ratio extremes
- % stocks up >25% in 50 days
- What makes a breadth thrust "legitimate"?
- Historical success rates of various thrust signals?

---

## Output Format Requested

```markdown
# Technical Breadth & Internal Market Health - Research Output

## Executive Summary
[Key breadth indicators and current readings]

## 1. Advance-Decline Line Analysis
[Current status, historical divergences, interpretation]

## 2. New Highs - New Lows
[Current reading, historical context, thresholds]

## 3. McClellan Indicators
| Indicator | Current | Overbought | Neutral | Oversold |
|-----------|---------|------------|---------|----------|
| Oscillator | ... | >+100 | -50 to +50 | <-100 |
| Summation | ... | ... | ... | ... |

## 4. Downtrend Metrics
| Metric | Current | Healthy | Concern | Danger |
|--------|---------|---------|---------|--------|
| % <50 DMA | ... | ... | ... | ... |
| % <200 DMA | ... | ... | ... | ... |
[Continue]

## 5. Sector Breadth Heat Map
| Sector | % >200 DMA | % >50 DMA | Trend | vs Index |
|--------|------------|-----------|-------|----------|
| Technology | ... | ... | ... | ... |
[All sectors]

## 6. Small vs Large Cap Breadth
[Comparison and divergence analysis]

## 7. Volume Confirmation
[Volume breadth indicators]

## 8. Breadth Thrust Catalog
| Indicator | Last Signal | Success Rate | Current Status |
|-----------|-------------|--------------|----------------|
| Zweig | Nov 28 2025 | 100% | ACTIVE |
[Others]

## Internal Rot Detection Framework
[How to identify "healthy index, sick market" conditions]

## Proposed HENRY Vectors
| ID | Name | Current | Thresholds | Source |
|----|------|---------|------------|--------|
| VX-HEN-12.01 | A-D Line Divergence | ... | ... | ... |
[Continue]

## Data Sources
| Metric | Free Source | URL | Update Freq |
|--------|-------------|-----|-------------|
[All metrics]

## Sources
[References]
```

---

## Integration Notes for HENRY

After receiving this research:
- Create VX-HEN-12.xx series for Breadth Depth domain
- Build "Internal Health Composite" indicator
- Add A-D divergence detection to monitoring
- Create sector breadth dashboard
- Add to FLOW.tsv: Breadth deterioration → Index breakdown

---

*Prompt ready for external LLM research*
