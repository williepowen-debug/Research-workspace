# RP-HEN-6.6: Cross-Asset Signals & Macro Indicators

**Prompt ID:** RP-HEN-6.6
**Cluster:** Data Expansion
**Priority:** 6
**Created:** 2026-02-03

---

## Context for Research Assistant

HENRY primarily tracks equity market internals, but cross-asset relationships often provide early warning. Copper/gold diverging from equities, real yields spiking, or global liquidity contracting can signal regime changes before they appear in stock prices. This research expands HENRY's peripheral vision.

Current HENRY cross-market vectors:
- VX-HEN-5.01: DXY Dollar Index: 120.45 (YELLOW, strong)
- VX-HEN-7.05: Bitcoin vs S&P Divergence: -25% (ORANGE)

Cross-agent context:
- SAM: Japan 40Y JGB at 3.94%, USD/JPY 155.49
- LIQUID: SOFR +3bps above IORB, RRP depleted

---

## Research Questions

### 1. COPPER/GOLD RATIO
- What does the copper/gold ratio measure?
  - Copper = economic growth proxy (industrial demand)
  - Gold = fear/uncertainty proxy
  - Ratio = growth optimism vs pessimism
- Historical relationship with:
  - S&P 500 returns
  - Yield curve
  - Economic recessions
- Current reading and trend?
- What divergences are meaningful?
- Data: Continuous futures, ETFs (CPER, GLD)?

### 2. REAL YIELDS (TIPS)
- What are real yields and how do TIPS measure them?
- 5-year and 10-year real yields — current levels?
- Historical impact of real yields on:
  - Growth stock valuations
  - Gold prices
  - Equity risk premium
- What real yield level is "restrictive"?
- Relationship between real yields and P/E compression?
- Data: FRED (DGS5, DGS10 minus breakevens), Treasury Direct

### 3. BREAKEVEN INFLATION
- 5-year and 10-year breakeven inflation rates
- What do breakevens tell us about inflation expectations?
- When do breakevens diverge from realized inflation?
- Impact on equity valuations?
- Current readings vs Fed target?
- Data: FRED (T5YIE, T10YIE)

### 4. GLOBAL LIQUIDITY PROXIES
- What is "global M2" and how to track it?
- Fed balance sheet + ECB + BOJ + PBOC
- Cross-border dollar liquidity
- Global central bank reserve changes
- Relationship between liquidity and:
  - Risk asset prices
  - Bitcoin (liquidity proxy)
  - Credit spreads
- Is global liquidity expanding or contracting?
- Data: Yardeni, CrossBorder Capital, central bank websites?

### 5. YIELD CURVE SIGNALS
Note: LIQUID covers Treasury specifics. HENRY should track equity-relevant signals:

- 2s10s spread — current inversion/steepening status?
- 3-month/10-year spread (Fed preferred recession indicator)
- Yield curve steepening: bullish or bearish signal?
- "Bear steepening" vs "bull steepening" — what's the difference?
- Historical lead time from inversion to recession?
- Current regime classification?

### 6. CURRENCY CROSS SIGNALS
Beyond DXY:
- EUR/USD — European growth signal
- USD/JPY — carry trade / risk appetite (coordinate with SAM)
- USD/CNY — China stress signal
- EM currency index — global risk appetite
- What currency moves historically preceded equity corrections?
- Current divergences?

### 7. COMMODITY COMPLEX
- Dr. Copper thesis (copper as economic indicator)
- Oil/copper ratio
- Baltic Dry Index (shipping/trade)
- Agricultural commodities (inflation pressure)
- Industrial metals vs precious metals ratio
- What commodity signals matter for equities?

### 8. VOLATILITY CROSS-MARKET
- VIX vs MOVE (equity vol vs bond vol)
- VIX vs EM volatility
- Currency volatility (CVIX or similar)
- Cross-asset volatility correlation
- When do volatility measures diverge, and what does it mean?
- Is there a "global vol" composite?

---

## Output Format Requested

```markdown
# Cross-Asset Signals & Macro Indicators - Research Output

## Executive Summary
[Key cross-asset relationships for equity analysis]

## 1. Copper/Gold Ratio
| Current Ratio | Trend | Equity Signal | Historical Context |
|---------------|-------|---------------|-------------------|
| ... | ... | ... | ... |

## 2. Real Yields Analysis
| Tenor | Current Real Yield | vs History | Impact |
|-------|-------------------|------------|--------|
| 5-Year | ... | ... | ... |
| 10-Year | ... | ... | ... |

## 3. Breakeven Inflation
[Current readings and implications]

## 4. Global Liquidity
| Component | Current | Trend | Equity Impact |
|-----------|---------|-------|---------------|
| Fed B/S | ... | ... | ... |
| ECB | ... | ... | ... |
| BOJ | ... | ... | ... |
| Global M2 | ... | ... | ... |

## 5. Yield Curve Regime
[Current classification and implications]

## 6. Currency Signals
| Pair | Level | Trend | Signal |
|------|-------|-------|--------|
| DXY | 120.45 | ... | ... |
| USD/JPY | 155.49 | ... | ... |
[Continue]

## 7. Commodity Signals
[Key commodity indicators]

## 8. Cross-Market Volatility
| Indicator | Current | vs VIX | Interpretation |
|-----------|---------|--------|----------------|
| MOVE | ... | ... | ... |
[Continue]

## Cross-Asset Warning Framework
[Which divergences matter and why]

## Proposed HENRY Vectors
| ID | Name | Current | Signal | Source |
|----|------|---------|--------|--------|
| VX-HEN-14.01 | Copper/Gold Ratio | ... | ... | ... |
| VX-HEN-14.02 | 10Y Real Yield | ... | ... | ... |
[Continue]

## Agent Coordination
- SAM: JPY dynamics, JGB stress
- LIQUID: Treasury/funding overlap
- CARL: Consumer inflation impact

## Data Sources
| Metric | Free Source | Frequency |
|--------|-------------|-----------|
[All metrics with URLs]

## Sources
[References]
```

---

## Integration Notes for HENRY

After receiving this research:
- Create VX-HEN-14.xx series for Cross-Asset domain
- Build "Macro Regime" indicator
- Coordinate with SAM (JPY), LIQUID (yields)
- Add cross-asset divergence alerts
- Add to FLOW.tsv: Cross-asset stress → Equity repricing

---

*Prompt ready for external LLM research*
