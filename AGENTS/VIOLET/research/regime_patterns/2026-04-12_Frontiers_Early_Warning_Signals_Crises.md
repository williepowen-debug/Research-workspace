# Early Warning Signals of Financial Crises Using Persistent Homology

**Source:** Frontiers in Applied Mathematics and Statistics (2022). "Early Warning Signals of Financial Crises Using Persistent Homology and Critical Slowing Down."

**URL:** https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2022.940133/full

---

## Key Findings

- **VIX Patterns Before Crises:**
  - **Uptrend patterns in VIX observed before financial crises**
  - **BUT: Low-level VIX also observed before financial crises**
  - This creates a paradox: both rising AND low VIX can precede crashes

- **Critical Slowing Down:**
  - Financial systems exhibit "critical slowing down" before regime shifts
  - Recovery from perturbations becomes slower
  - Variance and autocorrelation increase before transitions

- **Persistent Homology:**
  - Topological data analysis approach to detect structural changes
  - Identifies when market microstructure changes (increasing complexity)
  - Complements traditional time-series methods

- **VIX as Early Warning:**
  - VIX CAN provide early warning signals
  - BUT requires sophisticated methods — simple thresholds insufficient
  - Need to distinguish between "healthy" low vol and "precursor" low vol

---

## Relevance to VIOLET's Thesis

**HIGH:** Directly addresses the challenge of identifying pre-crash VIX patterns.

1. **The Paradox:** Low VIX doesn't always mean safety — can be complacency
2. **Complexity Metric:** VIX behavior (variance, autocorrelation) matters more than level
3. **Multi-Modal Approach:** Need to combine VIX with other indicators

---

## Actionable Implications

- **Low VIX Regime Analysis:**
  - VIX < 20 + low variance = complacency (dangerous)
  - VIX < 20 + rising variance = building pressure
  - Monitor VIX variance, not just level

- **Critical Slowing Indicators:**
  - VIX autocorrelation rising = system losing resilience
  - VIX mean-reversion slowing = regime shift approaching

- **VIOLET Refinement:**
  - Track VIX 30-day rolling variance
  - Track VIX autocorrelation (5-day lag)
  - Combine with VVIX and term structure for composite signal

---

## Confidence

**MEDIUM-HIGH** — Academic research with novel methodology, validates VIX as EWS but with caveats.

---

## Related KB Entries

- KB-VIO-001: VIX 19.23 (low but not extreme)
- KB-VIO-003: VVIX 107.30 (vol uncertainty elevated)
