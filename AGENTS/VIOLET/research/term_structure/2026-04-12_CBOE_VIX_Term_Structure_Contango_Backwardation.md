# VIX Futures Term Structure: Contango, Backwardation, and Regime Signals

**Source:** CBOE (Multiple). "Inside Volatility Trading: Is VIX Backwardation Necessarily a Sign of a Future Down Market?" (July 26, 2022). CBOE Insights.

**Additional Sources:**
- Quantpedia: "Exploiting Term Structure of VIX Futures" (2022)
- Velasquez, Cristian: "Detecting VIX Term Structure Regimes" (Medium, 2025)

---

## Key Findings

- **Term Structure Basics:**
  - **Contango (upward sloping):** Short-term VIX futures < Long-term VIX futures
    - Normal state (~80% of time)
    - Market expects volatility to fade over time
    - Associated with low/steady VIX environments
  
  - **Backwardation (downward sloping):** Short-term VIX futures > Long-term VIX futures
    - Stress state (~20% of time)
    - Market expects near-term uncertainty to resolve
    - Associated with elevated VIX, hedging demand

- **Predictive Power:**
  - Contango→Backwardation flips often precede equity selloffs
  - Backwardation does NOT always mean market will decline (can persist during rallies)
  - **Key signal:** Speed of curve inversion matters more than inversion itself

- **Roll Yield:**
  - Contango erodes long vol products (VXX, UVXY) via negative roll yield
  - Backwardation creates positive roll yield for long vol positions

- **Quantified Signals (from Velasquez PCA/HMM analysis):**
  - Principal Component 1 (level) explains ~85% of variance
  - Principal Component 2 (slope) explains ~12% of variance
  - Slope component most predictive of regime changes

---

## Relevance to VIOLET's Thesis

**HIGH:** Term structure is a real-time measure of vol expectations and hedging pressure.

1. **Early Warning:** Curve flattening/inversion precedes vol spikes
2. **Regime Identification:** Contango = low vol regime; Backwardation = high vol regime
3. **Risk Premium:** Shape of curve reflects vol risk premium (steeper = higher premium)

---

## Actionable Implications

| Term Structure Signal | Interpretation | Action |
|----------------------|----------------|--------|
| Steep contango (VIX3M/VIX > 1.15) | Complacency, low hedging | Monitor; vol cheap to buy |
| Flat contango (VIX3M/VIX 1.05-1.10) | Elevated concern | **Early warning** — curve flattening |
| Mild backwardation (VIX3M/VIX < 0.95) | Near-term stress | **Activation signal** — vol spike likely |
| Steep backwardation | Crisis pricing | Vol peak may be near |

- **VIOLET Trigger:** VIX3M/VIX ratio crossing below 1.0 (backwardation) = vol regime shift
- **Confirmation:** Backwardation persisting >3 days = sustained stress, not spike

---

## Confidence

**HIGH** — CBOE official research, extensive practitioner use, quantified signals.

---

## Related KB Entries

- KB-VIO-002: VIX3M/VIX=1.14 (current contango reading)
