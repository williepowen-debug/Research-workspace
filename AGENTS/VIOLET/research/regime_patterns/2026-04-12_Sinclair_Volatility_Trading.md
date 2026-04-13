# Volatility Trading: Position Sizing and Forecasting

**Source:** Sinclair, Euan (2010, 2013). "Volatility Trading" (1st and 2nd Editions). Wiley Trading.

**Related:** Sinclair, E. (2010). "Option Trading: Pricing and Volatility Strategies and Techniques." Wiley.

---

## Key Findings

- **Volatility Forecasting:**
  - Implied volatility (VIX) is a predictor of realized volatility, but biased
  - VIX typically overestimates realized vol (risk premium)
  - Forecasting realized vol requires combining implied vol with historical patterns

- **Mean Reversion in Volatility:**
  - Volatility exhibits strong mean reversion
  - Half-life of vol shocks: ~20-60 days depending on regime
  - High vol periods revert faster than low vol periods

- **Volatility of Volatility:**
  - Vol itself is volatile — VVIX captures this
  - High VVIX periods = uncertainty about future vol = trading opportunity
  - Vol-of-vol is mean-reverting but with longer cycles than vol

- **Position Sizing:**
  - Kelly criterion adaptations for volatility trading
  - Trade sizing based on edge (forecast vs implied) and variance
  - Risk of ruin considerations for short vol strategies

- **Edge Sources:**
  - Forecasting realized vol better than market
  - Understanding term structure dynamics
  - Exploiting skew and smile patterns
  - Event volatility (earnings, FOMC, etc.)

---

## Relevance to VIOLET's Thesis

**MEDIUM:** Provides practical trading framework for vol regime navigation.

1. **Forecasting Framework:** How to think about predicting vol (not just observing)
2. **Mean Reversion Timing:** Understanding vol cycle dynamics
3. **Risk Management:** Position sizing in vol regimes

---

## Actionable Implications

- **Vol Forecasting Model:**
  - Combine: VIX (implied), historical realized vol, GARCH-type models
  - Weight: 40% VIX, 40% historical, 20% regime adjustment
  - Adjust for term structure (near-term vs far-term)

- **Mean Reversion Trades:**
  - VIX > 30: Fade (sell vol) with defined risk
  - VIX < 15: Buy vol (cheap insurance)
  - VIX 15-25: Regime-dependent (hardest to trade)

- **VIOLET Application:**
  - Use mean reversion framework to set VIX targets
  - Identify when VIX is "too low" or "too high" relative to fair value
  - Factor in regime persistence (high vol regimes last longer)

---

## Confidence

**HIGH** — Practitioner bible for vol trading, widely respected, empirical foundation.

---

## Related KB Entries

- KB-VIO-001: VIX 19.23 (moderate level)
- KB-VIO-003: VVIX 107.30 (vol uncertainty)
