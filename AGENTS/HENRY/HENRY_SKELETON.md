# HENRY Domain Skeleton

**Agent:** HENRY (Historical Economic Norm Reference Yields)
**Domain:** Historical Market Comparisons & Anomaly Detection
**Version:** 1.0
**Created:** 2026-01-26

---

## QUICK START

HENRY identifies stress-predictive market abnormalities by comparing current conditions to historical periods. The core premise: when multiple metrics simultaneously reach historical extremes, systemic stress typically follows.

**Primary Question:** Do current market abnormalities resemble pre-crisis patterns, or represent a sustainable "new normal"?

**Core Method:**
1. Track key market metrics with 30+ years of history
2. Calculate current readings' historical percentiles
3. Compare to pre-crisis readings from reference periods
4. Identify which historical period current conditions most resemble

---

## ENTITY TYPES

### Vectors (VX)
Quantifiable market metrics tracked over time.

**Naming Convention:** VX-HEN-[Domain].[Number]
- Domain 1: CON (Concentration)
- Domain 2: VAL (Valuation)
- Domain 3: LEV (Leverage)
- Domain 4: SEN (Sentiment)
- Domain 5: CUR (Currency)

### Historical Periods
Reference periods for comparison.

| Code | Period | Primary Characteristics |
|------|--------|------------------------|
| P29 | 1929 | Concentration, leverage, retail |
| P74 | 1973-74 | Inflation, policy error |
| P87 | 1987 | Derivatives, speed |
| P00 | 1999-2000 | Tech, valuations, mania |
| P08 | 2007-08 | Hidden leverage, complacency |
| PJ89 | Japan 1989 | Valuations, currency |

### Indicators
Derived metrics combining multiple vectors.

---

## RELATIONSHIP TYPES

### compares_to
Current reading vs historical period reading.
```
[Vector] compares_to [Period]: [Current] vs [Historical]
Example: VX-HEN-2.01 compares_to P00: 36 vs 44
```

### exceeds
Current reading surpasses historical level.
```
[Vector] exceeds [Period]: [Current] > [Historical]
Example: VX-HEN-1.01 exceeds P29: 37% > 25%
```

### matches
Current pattern resembles historical period.
```
[Vector_Set] matches [Period]: [Similarity_Score]
Example: {CON, VAL, LEV} matches P00: 0.85
```

### precedes
Historical relationship where condition A preceded outcome B.
```
[Condition] precedes [Outcome] in [Period]: [Lag_Time]
Example: CAPE >40 precedes >30% drawdown in P00: 6 months
```

---

## TRANSMISSION PATHS

How historical patterns inform stress prediction.

### Concentration -> Fragility Path
```
High concentration (>35%)
  -> Reduced diversification benefit
  -> Correlated selling in stress
  -> Amplified drawdowns
Historical precedent: P29, P00
```

### Valuation -> Mean Reversion Path
```
Extreme valuations (CAPE >30)
  -> Compressed forward returns
  -> Catalyst triggers repricing
  -> Multi-year normalization
Historical precedent: P00, PJ89
```

### Leverage -> Forced Selling Path
```
Elevated household equity allocation (>40%)
  -> Wealth effect dependence
  -> Margin calls in decline
  -> Pro-cyclical selling
Historical precedent: P29, P08
```

### Complacency -> Shock Path
```
Low VIX / high realized vol gap
  -> Underpriced tail risk
  -> Short vol positioning
  -> Violent repricing
Historical precedent: P87, P08
```

---

## THRESHOLDS (Tripwires)

### Concentration Domain (CON)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED |
|--------|--------|-------|--------|--------|-----|
| VX-HEN-1.01 | Top 10 S&P Weight | <25% | 25-30% | 30-35% | >35% |
| VX-HEN-1.02 | % Stocks >200 DMA | >60% | 50-60% | 40-50% | <40% |
| VX-HEN-1.03 | EW vs CW Spread | <3% | 3-5% | 5-10% | >10% |

### Valuation Domain (VAL)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED |
|--------|--------|-------|--------|--------|-----|
| VX-HEN-2.01 | CAPE Ratio | <20 | 20-25 | 25-35 | >35 |
| VX-HEN-2.02 | Buffett Indicator | <80% | 80-120% | 120-180% | >180% |
| VX-HEN-2.03 | Equity Risk Premium | >4% | 2-4% | 1-2% | <1% |

### Leverage Domain (LEV)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED |
|--------|--------|-------|--------|--------|-----|
| VX-HEN-3.01 | Margin Debt % GDP | <P50 | P50-75 | P75-90 | >P90 |
| VX-HEN-3.02 | Household Equity % | <30% | 30-38% | 38-42% | >42% |

### Sentiment Domain (SEN)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED |
|--------|--------|-------|--------|--------|-----|
| VX-HEN-4.01 | VIX/Realized Ratio | 0.9-1.1 | 0.7-0.9 | 0.5-0.7 | <0.5 |
| VX-HEN-4.02 | Equity Put/Call | >0.8 | 0.65-0.8 | 0.55-0.65 | <0.55 |

### Currency Domain (CUR)

| Vector | Metric | Context |
|--------|--------|---------|
| VX-HEN-5.01 | DXY Index | Context-dependent; extreme moves in either direction signal stress |

---

## VECTOR REGISTRY

### CON - Concentration

**VX-HEN-1.01: Top 10 S&P 500 Weight**
- Description: Combined market cap weight of top 10 stocks in S&P 500
- Source: Yardeni Research, S&P Global
- History: 1980+
- Current Est: ~37%
- Historical Context:
  - 1929: ~25%
  - 2000: ~27%
  - Current exceeds both pre-crisis peaks
- Update: Weekly

**VX-HEN-1.02: Market Breadth (% Above 200 DMA)**
- Description: Percentage of S&P 500 stocks above their 200-day moving average
- Source: Barchart
- History: 1990+
- Interpretation: <50% = narrow leadership, bearish divergence risk
- Update: Daily

**VX-HEN-1.03: Equal-Weight vs Cap-Weight Spread**
- Description: RSP (equal-weight) vs SPY (cap-weight) performance spread
- Source: Calculated from Yahoo Finance
- History: 2003+
- Interpretation: Large gap = concentration risk
- Update: Daily

### VAL - Valuation

**VX-HEN-2.01: CAPE/Shiller P/E**
- Description: Cyclically Adjusted Price-to-Earnings ratio (10-year avg earnings)
- Source: multpl.com (Robert Shiller data)
- History: 1881+
- Current Est: ~36
- Historical Context:
  - 1929: 32.6
  - 2000: 44.2
  - 2007: 27.5
  - Long-term avg: ~17
- Update: Monthly

**VX-HEN-2.02: Buffett Indicator**
- Description: Total stock market cap / GDP
- Source: FRED (WILSHIRE5000INDX / GDP)
- History: 1970+
- Current Est: ~190%
- Historical Context:
  - 2000: 140%
  - 2007: 105%
  - Current at all-time high
- Update: Quarterly

**VX-HEN-2.03: Equity Risk Premium**
- Description: Expected equity return - risk-free rate
- Source: Calculated
- History: 1960+
- Interpretation: <2% = stocks offer little compensation for risk
- Update: Monthly

### LEV - Leverage

**VX-HEN-3.01: Margin Debt % of GDP**
- Description: FINRA margin debt as percentage of nominal GDP
- Source: FINRA + FRED
- History: 1970+
- Interpretation: Percentile-based; >P90 = extreme
- Update: Monthly

**VX-HEN-3.02: Household Equity Allocation**
- Description: Household direct + indirect equity holdings as % of financial assets
- Source: Federal Reserve Z.1 Flow of Funds
- History: 1950+
- Current Est: ~42%
- Historical Context:
  - 2000: 42%
  - 2007: 36%
  - 1950-2000 avg: ~25%
- Update: Quarterly

### SEN - Sentiment

**VX-HEN-4.01: VIX vs Realized Volatility**
- Description: Ratio of implied (VIX) to realized volatility
- Source: CBOE, calculated
- History: 1990+
- Interpretation: Ratio <0.8 = complacency, underpriced risk
- Update: Daily

**VX-HEN-4.02: Equity Put/Call Ratio**
- Description: Volume of equity puts / volume of equity calls
- Source: CBOE
- History: 1990+
- Interpretation: <0.6 = extreme bullish positioning
- Update: Daily

### CUR - Currency

**VX-HEN-5.01: DXY Dollar Index**
- Description: Trade-weighted dollar index
- Source: FRED (DTWEXBGS)
- History: 1971+
- Interpretation: Context-dependent; rapid moves indicate stress
- Update: Daily

---

## HISTORICAL ANALOGUES DETAIL

### 1929 Crash (P29)
**Period:** August 1929 - November 1929
**Drawdown:** -89% peak to trough (by 1932)

Key Pre-Crash Conditions:
- Market concentration in "Radio" stocks (tech of the era)
- Margin debt explosion (buying on 10% margin)
- Retail participation surge (first mass market)
- Unprecedented valuations

Relevance to Current:
- Concentration pattern matches
- Retail participation via apps parallels 1920s bucket shops
- Leverage through derivatives rather than margin

### Stagflation Crisis (P74)
**Period:** January 1973 - October 1974
**Drawdown:** -48%

Key Pre-Crisis Conditions:
- "Nifty Fifty" concentration (50 stocks everyone owned)
- Oil shock catalyst
- Fed policy error (too loose, then too tight)
- Inflation surge

Relevance to Current:
- Magnificent 7 parallels Nifty Fifty
- Inflation regime uncertainty
- Policy error risk persists

### 1987 Crash (P87)
**Period:** August 1987 - October 1987
**Drawdown:** -34% (22% in one day)

Key Pre-Crash Conditions:
- Portfolio insurance (algorithmic selling)
- Low VIX / complacency
- Speed of decline unprecedented
- Fed response (Greenspan put birth)

Relevance to Current:
- 0DTE options = modern portfolio insurance?
- Algorithmic trading dominance
- Gamma exposure could accelerate moves
- Speed risk from electronic markets

### Dot-Com Bubble (P00)
**Period:** March 2000 - October 2002
**Drawdown:** -49% (Nasdaq -78%)

Key Pre-Crisis Conditions:
- Tech concentration (MSFT, CSCO, INTC, etc.)
- CAPE at 44 (all-time high)
- Retail mania (day trading)
- "New paradigm" narrative

Relevance to Current:
- Mag 7 tech concentration
- CAPE approaching 2000 levels
- AI = new paradigm narrative
- Retail options trading surge

### Global Financial Crisis (P08)
**Period:** October 2007 - March 2009
**Drawdown:** -57%

Key Pre-Crisis Conditions:
- Hidden leverage (CDOs, SIVs)
- Low VIX (complacency)
- Credit default swaps unregulated
- Housing as collateral

Relevance to Current:
- Basis trade leverage hidden
- VIX often below realized
- Private credit growth unmonitored
- Complexity in derivatives market

### Japan 1989 (PJ89)
**Period:** December 1989 - Present (33 years to recover)
**Drawdown:** -82%

Key Pre-Crisis Conditions:
- CAPE equivalent ~90
- Real estate bubble
- Yen strength concerns
- Demographic peak

Relevance to Current:
- Valuation extremes possible
- Multi-decade recovery scenario
- Currency dynamics (SAM domain)
- Demographic headwinds in developed markets

---

## GLOSSARY

**Breadth:** Number of stocks participating in market move
**CAPE:** Cyclically Adjusted Price-to-Earnings (Shiller P/E)
**Concentration:** Market cap weight in top N stocks
**DMA:** Day Moving Average
**DXY:** Dollar Index (trade-weighted)
**ERP:** Equity Risk Premium
**Gamma:** Rate of change of delta; affects dealer hedging
**Margin Debt:** Borrowed money to buy securities
**Percentile:** Ranking within historical distribution (P90 = top 10%)
**Realized Vol:** Actual historical volatility (vs implied)
**VIX:** CBOE Volatility Index (implied volatility)
**0DTE:** Zero Days to Expiration (same-day options)

---

## DATA SOURCE URLS

| Source | URL | Notes |
|--------|-----|-------|
| Shiller CAPE | multpl.com/shiller-pe | Monthly updates |
| FRED | fred.stlouisfed.org | Various series |
| FINRA Margin | finra.org/investors/learn-to-invest/advanced-investing/margin-statistics | Monthly |
| Fed Z.1 | federalreserve.gov/releases/z1 | Quarterly |
| Barchart | barchart.com/stocks/indices | Daily |
| CBOE | cboe.com/vix | Daily |
| Yardeni | yardeni.com | Weekly updates |

---

*HENRY Domain Skeleton v1.0*
*Created: 2026-01-26*
