# VIOLET Research Summary

**Compiled:** 2026-04-12

> ⚠️ **SCOPE — READ THIS FIRST (banner added 2026-07-30).** This indexes **only the original 2026-04-12 academic/practitioner source corpus** (`credit_vix_lag/`, `regime_patterns/`, `term_structure/`, `skew_analysis/`, `crisis_analogs/`). It is **NOT a complete index of `research/`** — ~20 further files have been added since (postmortems, backtests, audits, adjudications) and **none of them appear below.** It is kept as a map of the founding literature, not as a directory listing. **For the live file map use `README.md`; for what the framework currently rests on use `thesis/VIX_THESIS.md`.**

This directory contains academic and practitioner research on VIX prediction, regime dynamics, and volatility forecasting. Sources are organized by topic area.

---

## Research Topics

### 1. Credit → VIX Transmission (Priority 1)

| File | Source | Key Finding |
|------|--------|-------------|
| `2026-04-12_Soper_McAlley_VIX_Credit_Spreads_Threshold.md` | Soper & McAlley (2025) | Three VIX regimes: <20, 20-30, >30 with different credit-vol relationships |
| `2026-04-12_Davernas_Credit_Spreads_Equity_Volatility.md` | Davernas (JMP) | Joint determination via Merton framework; regime-dependent causality |

**Key Takeaway:** Credit-vol correlation is regime-dependent. Low VIX = weak correlation; High VIX = strong correlation. Fed rates moderate the relationship.

---

### 2. Regime-Switching Models (Priority 2)

| File | Source | Key Finding |
|------|--------|-------------|
| `2026-04-12_Hamilton_Lin_Stock_Market_Volatility_Business_Cycle.md` | Hamilton & Lin (1996) | Markov-switching framework; asymmetric transition probabilities |
| `2026-04-12_Cole_Artemis_Allegory_Hawk_Serpent.md` | Cole (2019) | Hawk/Serpent metaphor; long vol as strategic allocation |
| `2026-04-12_Frontiers_Early_Warning_Signals_Crises.md` | Frontiers (2022) | Both rising AND low VIX can precede crashes; critical slowing down |
| `2026-04-12_Sinclair_Volatility_Trading.md` | Sinclair (2010) | Mean reversion with 20-60 day half-life; position sizing framework |

**Key Takeaway:** Vol regimes are persistent with asymmetric transitions. Long periods of low vol increase probability of regime shift.

---

### 3. Term Structure Predictors (Priority 3)

| File | Source | Key Finding |
|------|--------|-------------|
| `2026-04-12_CBOE_VIX_Term_Structure_Contango_Backwardation.md` | CBOE (2022) | Contango→backwardation flips precede selloffs |
| `2026-04-12_Hosker_Djurdjevic_VIX_Futures_ML.md` | Hosker et al. (2018) | LSTM/RNN outperform traditional methods for VIX forecasting |

**Key Takeaway:** VIX3M/VIX ratio < 1.0 (backwardation) = vol regime shift signal.

---

### 4. Pre-Crash Patterns (Priority 4)

| File | Source | Key Finding |
|------|--------|-------------|
| `2026-04-12_Thrasher_Volatility_Tsunami_VVIX.md` | Thrasher (2018) | VVIX > 120 with VIX < 25 = vol tsunami warning |
| `2026-04-12_Fed_Volatility_Volatility_Tail_Risk.md` | Fed (2013) | VVIX² = RVV + VVRP; both predict tail risk hedges |
| `2026-04-12_VIX_Seasonality_FOMC_Effects.md` | Multiple | FOMC day VIX decline; September-October seasonality |

**Key Takeaway:** VVIX is earliest warning system. High VVIX + low VIX = complacency with embedded tail risk.

---

### 5. Skew Analysis

| File | Source | Key Finding |
|------|--------|-------------|
| `2026-04-12_CBOE_SKEW_Index_Tail_Risk.md` | CBOE | SKEW > 130 = elevated tail risk; diverges from VIX |

**Key Takeaway:** SKEW provides tail risk signal separate from VIX level.

---

## Actionable Thresholds Summary

| Indicator | Normal | Warning | Critical |
|-----------|--------|---------|----------|
| VIX | < 20 | 20-30 | > 30 |
| VVIX | < 100 | 100-120 | > 120 |
| VIX3M/VIX | > 1.10 | 1.00-1.10 | < 1.00 |
| SKEW | < 115 | 115-130 | > 130 |
| VIX-Credit Correlation | < 0.2 | 0.2-0.5 | > 0.5 |

---

## Confidence Levels

- **A1:** Seminal academic work, widely replicated
- **A2:** Peer-reviewed research or official institution
- **B1:** Practitioner research with empirical backing
- **B2:** Working papers or preliminary research

---

## Next Research Priorities

1. **Historical Crash Case Studies:** Detailed VIX behavior 1mo/1wk/1day before 2008, 2020, etc.
2. **Machine Learning Implementation:** Code LSTM model for VIX forecasting
3. **Cross-Asset Vol Transmission:** VIX → other asset class vol dynamics
4. **Options Flow Analysis:** Unusual options activity as VIX predictor
