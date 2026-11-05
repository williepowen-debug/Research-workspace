# HENRY Session 001 Research Plan

**Objective:** Establish baseline readings for all 11 core vectors and identify closest historical analogue

---

## PHASE 1: Valuation Data (Highest Confidence Sources)

### VX-HEN-2.01: CAPE/Shiller P/E
- **Source:** multpl.com/shiller-pe
- **Action:** Fetch current CAPE value
- **Historical context needed:** 1929, 2000, 2007 readings for comparison
- **Percentile:** Calculate vs 1881-present distribution

### VX-HEN-2.02: Buffett Indicator
- **Source:** FRED series WILSHIRE5000INDX divided by GDP (or use currentmarketvaluation.com)
- **Action:** Fetch current ratio
- **Historical context:** 2000 peak (~140%), 2007 (~105%)
- **Note:** Currently estimated ~190% - verify

---

## PHASE 2: Concentration Data

### VX-HEN-1.01: Top 10 S&P 500 Weight
- **Source:** Yardeni Research (yardeni.com) or slickcharts.com/sp500
- **Action:** Sum market cap weights of top 10 holdings
- **Historical context:** 1980s (~20%), 2000 (~27%), current estimate ~37%
- **This is critical** - if >35%, exceeds all historical precedents

### VX-HEN-1.02: Market Breadth (% Above 200 DMA)
- **Source:** Barchart.com or stockcharts.com
- **Action:** Find % of S&P 500 stocks above 200-day moving average
- **Threshold:** <50% = narrow, <40% = concerning, <30% = critical

### VX-HEN-1.03: Equal-Weight vs Cap-Weight Spread
- **Source:** Compare RSP vs SPY YTD performance (Yahoo Finance)
- **Action:** Calculate spread (SPY return - RSP return)
- **Interpretation:** Large positive spread = concentration benefiting returns

---

## PHASE 3: Leverage/Positioning Data

### VX-HEN-3.01: Margin Debt % of GDP
- **Source:** FINRA margin statistics + FRED GDP
- **Action:** Calculate ratio, determine percentile
- **Note:** FINRA publishes monthly with ~6 week lag

### VX-HEN-3.02: Household Equity Allocation
- **Source:** Federal Reserve Z.1 (quarterly, lagged)
- **Alternative:** FRED series (search "household equity allocation")
- **Historical context:** 2000 peak ~42%, current estimate ~42%
- **This is critical** - matches 2000 peak

---

## PHASE 4: Sentiment Data

### VX-HEN-4.01: VIX vs Realized Volatility
- **Source:** CBOE for VIX, calculate 20-day realized vol from SPY
- **Action:** Compute ratio (VIX / Realized Vol)
- **Interpretation:** <0.8 = complacency (implied underpricing risk)

### VX-HEN-4.02: Equity Put/Call Ratio
- **Source:** CBOE daily statistics
- **Action:** Get equity-only put/call ratio (not total, not index)
- **Threshold:** <0.6 = extreme bullish positioning

---

## PHASE 5: Currency Context

### VX-HEN-5.01: DXY Dollar Index
- **Source:** FRED (DTWEXBGS) or tradingview
- **Action:** Note current level and recent trend
- **Context:** Not threshold-based; note if at extremes or moving rapidly

---

## PHASE 6: Equity Risk Premium (Calculated)

### VX-HEN-2.03: Equity Risk Premium
- **Formula:** (1/CAPE) + expected growth - 10Y Treasury yield
- **Simplified:** Earnings yield (E/P from CAPE inverse) minus 10Y yield
- **Source:** Combine CAPE data with FRED 10Y Treasury (DGS10)
- **Threshold:** <2% = stocks barely compensating for risk

---

## ANALYSIS TASKS

### A. Historical Percentile Calculation
For each vector with sufficient history:
1. Note current value
2. Estimate percentile rank (where does it fall in historical distribution?)
3. Sources like multpl.com often provide percentile context

### B. Closest Analogue Determination
Compare current readings to pre-crisis readings:

| Vector | Current | 1929 | 1973 | 1987 | 2000 | 2007 | Japan 89 |
|--------|---------|------|------|------|------|------|----------|
| Top 10 Weight | ~37% | ~25% | ? | ? | ~27% | ? | ? |
| CAPE | ~36 | 32.6 | 18 | 18 | 44 | 27 | ~90 |
| Buffett | ~190% | ? | ? | ? | 140% | 105% | ? |
| HH Equity % | ~42% | ? | ? | ? | 42% | 36% | ? |

**Hypothesis:** Current conditions most closely match 2000 (concentration + valuations + household exposure), but with higher concentration than any prior period.

### C. Divergence Analysis
Note where current conditions DIFFER from historical analogues:
- 0DTE options (no precedent)
- Passive investing dominance (limited precedent)
- Fed balance sheet size (post-2008 phenomenon)
- Private credit growth (less visible than 2008 bank leverage)

---

## OUTPUT DELIVERABLES

1. **VX.tsv** - Update all 11 vectors with verified current readings
2. **VX_HISTORY.tsv** - Add first data point for each vector
3. **ML.tsv** - Log key findings:
   - ML-HEN-002: Baseline readings summary
   - ML-HEN-003: Closest analogue analysis
   - ML-HEN-004: Key divergences from historical patterns
4. **FL.tsv** - Add upcoming catalysts:
   - Fed meetings
   - Major earnings (Mag 7)
   - Quarterly data releases (GDP, Z.1)
5. **HENRY_001_HANDOFF.md** - Session summary

---

## PRIORITY ORDER

If time-constrained, prioritize:
1. **CAPE** (VX-HEN-2.01) - most reliable, longest history
2. **Top 10 Weight** (VX-HEN-1.01) - core concentration thesis
3. **Buffett Indicator** (VX-HEN-2.02) - currently at ATH
4. **Household Equity %** (VX-HEN-3.02) - consumer exposure link
5. **Market Breadth** (VX-HEN-1.02) - real-time health check

Lower priority (more volatile/noisy):
6. Put/Call Ratio
7. VIX/Realized Vol
8. DXY

---

## CROSS-AGENT SIGNALS TO CONSIDER

After baseline established, evaluate if any signals should be sent:
- **To CARL:** If household equity >40% confirmed, signal consumer overexposure
- **To SAM:** If Japan 1989 emerges as relevant analogue, share context
- **To ALL:** If CAPE >35 or Top 10 >35% confirmed, note elevated status (not URGENT unless >40)

---

*Plan created: 2026-01-26*
*Execute in HENRY Session 001*
