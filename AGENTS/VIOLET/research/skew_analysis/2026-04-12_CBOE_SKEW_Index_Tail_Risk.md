# CBOE SKEW Index: Measuring Tail Risk

**Source:** CBOE. "The CBOE SKEW Index." CBOE Whitepaper and Methodology.

**URL:** https://www.cboe.com/tradable_products/vix/cboe_skew_index/

---

## Key Findings

- **SKEW Definition:**
  - Derived from S&P 500 option prices (similar to VIX)
  - Measures perceived tail risk — probability of outlier returns
  - Increases when investors price in higher probability of large downward moves

- **Calculation:**
  - Based on implied volatility skew (difference between OTM puts and ATM calls)
  - Higher SKEW = steeper skew = higher tail risk pricing
  - Normalized to 100 (no skew) — values > 100 indicate negative skew

- **Interpretation:**
  - **SKEW ~100-115:** Normal market conditions, balanced risk perception
  - **SKEW 115-130:** Elevated tail risk concern
  - **SKEW > 130:** High tail risk pricing, crash protection in demand
  - **SKEW > 140:** Extreme tail risk (rare, associated with crisis periods)

- **Relationship to VIX:**
  - SKEW and VIX are correlated but capture different risks
  - VIX = overall volatility level
  - SKEW = asymmetry/tail risk
  - Can have high SKEW with low VIX (tail risk without general fear)
  - Can have high VIX with moderate SKEW (general fear, symmetric)

---

## Relevance to VIOLET's Thesis

**MEDIUM:** Provides complementary signal to VIX for tail risk assessment.

1. **Tail Risk Metric:** Captures crash probability separate from general vol
2. **Asymmetry Signal:** Rising SKEW = put buying = institutional hedging
3. **Divergence Warning:** High SKEW + low VIX = smart money hedging

---

## Actionable Implications

| SKEW Level | VIX Level | Interpretation | Action |
|------------|-----------|----------------|--------|
| < 115 | < 20 | Normal risk | Standard monitoring |
| 115-130 | < 20 | **Tail risk building** | **Early warning** — hedging demand rising |
| > 130 | < 25 | Crash protection expensive | Elevated tail risk |
| > 130 | > 30 | Crisis regime | Tail event likely |

- **VIOLET Signal:** SKEW > 120 with VIX < 22 = "smart money" hedging
- **Divergence:** SKEW rising while VIX flat = increasing tail concern

---

## Confidence

**HIGH** — CBOE official index, widely used by practitioners, transparent methodology.

---

## Related KB Entries

- KB-VIO-001: VIX 19.23 (current level)
- KB-VIO-005: SKEW 135 (elevated tail risk)
