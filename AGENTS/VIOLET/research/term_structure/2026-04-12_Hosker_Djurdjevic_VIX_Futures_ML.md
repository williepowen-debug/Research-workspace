# Forecasting VIX Futures Using Machine Learning

**Source:** Hosker, James; Djurdjevic, Slobodan; et al. (2018). "Forecasting VIX Futures Using Machine Learning." SMU Data Science Review, Vol. 1, No. 4.

**URL:** https://scholar.smu.edu/datasciencereview/vol1/iss4/6/

---

## Key Findings

- **ML vs Traditional Methods:**
  - RNNs and LSTMs provide **improved forecasting results** over:
    - Linear regression
    - Principal Components Analysis (PCA)
    - ARIMA models
  - Improvement most pronounced for short-term forecasts (1-5 days)

- **Feature Importance:**
  - VIX futures and options data most predictive
  - Lagged VIX values provide significant information
  - Options skew and term structure add predictive power

- **Model Performance:**
  - LSTM captures non-linear patterns in volatility
  - RNN effective for sequence modeling of vol time series
  - Hybrid models (combining multiple approaches) outperform single models

- **Limitations:**
  - ML models require significant data
  - Performance degrades in regime shifts (model trained on low vol fails in high vol)
  - Overfitting risk in volatile environments

---

## Relevance to VIOLET's Thesis

**MEDIUM:** Provides methodological foundation for VIX prediction models.

1. **Prediction Feasibility:** VIX is forecastable with ML methods, not just random walk
2. **Feature Selection:** Identifies which inputs matter (futures curve, options data)
3. **Model Choice:** LSTM/RNN preferred for volatility time series

---

## Actionable Implications

- **Model Architecture:**
  - Implement LSTM for VIX forecasting
  - Input features: VIX spot, VIX3M, VIX9D, VVIX, term structure slope
  - Output: 1-day, 5-day, 10-day VIX forecasts

- **Training Considerations:**
  - Use rolling window to adapt to regime changes
  - Include both low-vol and high-vol periods in training data
  - Monitor for regime shift degradation

- **VIOLET Application:**
  - ML forecasts as input to regime classification
  - Forecast error as uncertainty metric
  - Ensemble: combine ML forecast with term structure signals

---

## Confidence

**MEDIUM** — Academic study with solid methodology, but focused on futures pricing rather than regime prediction.

---

## Related KB Entries

- KB-VIO-001: Current VIX 19.23
- KB-VIO-002: VIX3M/VIX ratio for term structure
