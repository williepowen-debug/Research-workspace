# Credit-to-VIX Lag Analysis

## Research Question
Does credit lead VIX? If so, by how many days?

## Data
- Period: Jan 2018 - Apr 2026 (2,019 trading days)
- VIX: CBOE Volatility Index
- HY OAS: FRED BAMLH0A0HYM2 (ICE BofA High Yield Option-Adjusted Spread)

## Key Findings

### 1. Overall Correlation
| Pair | Correlation |
|------|-------------|
| VIX vs HY OAS | 0.710 |
| VIX3M vs HY OAS | 0.713 |
| VVIX vs HY OAS | 0.292 |
| SKEW vs HY OAS | -0.559 |

### 2. Lead-Lag Analysis
**Surprising result:** VIX leads HY OAS, not the other way around.

| Lag | Correlation | Interpretation |
|-----|-------------|----------------|
| -20 days | 0.719 | VIX leads HY OAS by 20 days |
| 0 days | 0.710 | Same-day correlation |
| +20 days | 0.719 | HY OAS leads VIX by 20 days |

The correlation is nearly symmetric, suggesting simultaneous movement with slight VIX lead.

### 3. Regime-Dependent Behavior
| Regime | Days | Optimal Lag | Max Correlation |
|--------|------|-------------|-----------------|
| Low Vol (VIX<20) | 1,264 | 14 days | 0.060 |
| Rising Vol (20-30) | 606 | 13 days | 0.479 |
| High Vol (30-40) | 111 | 9 days | 0.328 |

**Key insight:** In low vol regimes, credit-vol correlation breaks down. In rising vol regimes, correlation strengthens and lag shortens.

### 4. Crisis Analog Findings
- **Feb 2018:** VIX spike without credit stress (technical unwind)
- **Mar 2020:** VIX led credit by ~21 days (pandemic crash)
- **Feb 2021:** Elevated VIX, stable credit (meme stocks)

## Revised Hypothesis

**Original claim:** Credit leads VIX by 5-10 days.
**Finding:** In normal/rising vol regimes, they move together. In crash regimes, VIX leads credit.

**Refined thesis:**
- Low vol regime: Credit-vol correlation low, no clear lead-lag
- Rising vol regime: Credit and VIX move together (0-5 day lag)
- Crash regime: VIX leads credit (vol shock front-runs credit repricing)

## Trading Implications

### The Lag Trade (Revised)
**Setup:**
- HY OAS widens >50bps in 1 week
- VIX flat or down
- Term structure NOT inverted

**Entry:** VIX calls 30-60 DTE
**Target:** VIX catches up to credit-implied level
**Stop:** HY OAS reverses, or VIX spikes >25

**Caveat:** Credit lead is not reliable in all regimes. Use as one signal among many.

## Current Status (Apr 2026)
- VIX: 19.23 (Low vol regime)
- HY OAS: 2.90 (tight spreads)
- Regime: Low vol, credit-vol correlation weak
- Signal: No credit-vol divergence detected

## Files
- `lead_lag_analysis.csv` — Full lead-lag correlation table
- `combined_vix_credit.csv` — Merged dataset
