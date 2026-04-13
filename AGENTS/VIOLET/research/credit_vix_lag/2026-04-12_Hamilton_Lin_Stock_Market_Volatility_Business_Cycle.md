# Stock Market Volatility and the Business Cycle

**Source:** Hamilton, James D. & Lin, Gabriel (1996). "Stock Market Volatility and the Business Cycle." Journal of Applied Econometrics.

**Related:** Hamilton, J.D. (1989). "A New Approach to the Economic Analysis of Nonstationary Time Series." Econometrica.

---

## Key Findings

- **Markov-Switching Framework:** Hamilton's seminal work introduced regime-switching models to economic time series
  - Latent state variable follows Markov process (probability of switching depends only on current state)
  - Allows for endogenous identification of regime changes without arbitrary thresholds

- **Volatility Regimes:** Stock market volatility clusters in distinct regimes:
  - **Low-volatility regime:** Persistent, mean-reverting, associated with economic expansions
  - **High-volatility regime:** Clustered, persistent, associated with recessions/crises
  - Transition probabilities are asymmetric — harder to exit high-vol than enter it

- **Business Cycle Link:** High volatility regimes coincide with NBER recessions
  - Volatility can serve as a real-time business cycle indicator
  - Lead-lag relationships exist between vol spikes and economic downturns

- **Duration Dependence:** Time spent in a regime affects probability of transition
  - Long periods of low vol increase probability of regime switch (volatility buildup)

---

## Relevance to VIOLET's Thesis

**FOUNDATIONAL:** This is the theoretical basis for all regime-switching approaches to volatility.

1. **Regime Detection:** Provides statistical framework for identifying low→rising vol transitions
2. **Asymmetric Dynamics:** Explains why vol spikes are sudden but vol collapses are gradual
3. **Predictive Content:** Transition probabilities can be monitored as early warning signals

---

## Actionable Implications

- **Model Application:** Implement 2-state Markov-switching model on VIX or VIX futures
  - State 1: Low vol (mean ~15, low variance)
  - State 2: High vol (mean ~30+, high variance)

- **Transition Probability Monitoring:**
  - P(low→high) rising above 10% = early warning
  - P(low→high) rising above 25% = high-probability regime change imminent

- **Duration Signal:** Extended periods (>6 months) of VIX < 20 increase probability of regime switch

---

## Confidence

**HIGH** — Seminal academic work, widely replicated, foundational to modern volatility modeling.

---

## Related KB Entries

- KB-VIO-006: Regime-dependent correlation
- KB-VIO-010: Correlation strengthens in stress
