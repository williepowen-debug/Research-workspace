# KRE/XLF Relative Value Framework

**Created:** 2026-02-20
**Purpose:** Systematic RV framework for trading KRE vs XLF spread

---

## Historical Relationship

**Core dynamics:**
- KRE and XLF move together directionally (correlation ~0.68)
- KRE is higher-beta, more volatile leg
- KRE has structurally underperformed XLF post-GFC/post-SVB

**Performance (10-year):**
| Metric | KRE | XLF |
|--------|-----|-----|
| Annualized Return | 6.3% | 12.0% |
| 1M Rolling Volatility | 6.8% | 3.8% |
| Sharpe Ratio | 0.50 | 1.19 |

**Structural difference:**
- **XLF:** Dominated by large, diversified financials (JPM, BAC, BRK.B, V, MA)
- **KRE:** Equal-weighted regionals with little overlap

**Net result:** KRE = leveraged, more fragile expression of same sector forces. The spread proxies "regional bank health vs big-bank/fintech complex."

---

## 1. Core Ratio Construction

**Daily ratio:**
```
R_t = KRE_t / XLF_t
```

Or use %-difference series (KREXLF_PCT_DIFF) as spread variable.

**Important:** Long-term drift favors XLF. Use rolling windows (6-24 months) for mean and stdev, not all-history.

---

## 2. Z-Score Bands and Signals

**Calculate daily:**
```
μ_R,t = rolling mean over lookback (e.g., 126 days = 6mo)
σ_R,t = rolling stdev over lookback
Z_t = (R_t - μ_R,t) / σ_R,t
```

**Interpretation:**

| Z-Score | Reading | Action |
|---------|---------|--------|
| \|Z\| < 1.0 | Neutral | Background noise |
| Z ≤ -1.5 to -2.0 | KRE cheap vs XLF | Long KRE / Short XLF (if macro permits) |
| Z ≥ +1.5 to +2.0 | KRE rich vs XLF | Short KRE / Long XLF |

**Position sizing:** Beta/volatility-weight legs (KRE smaller, XLF larger) for dollar-neutral, risk-neutral position.

---

## 3. Macro and Regime Overlays

**Don't blindly fade genuine crises.** Gate trades with:

### Yield Curve (2s10s, 3m10y)
- KRE outperforms in **steepening** regimes
- KRE underperforms in **flattening/inversion**
- Only fade extreme negative Z if curves stabilizing or steepening

### Credit/Funding Stress
- CDS indices
- FRA-OIS spread
- Regional bank CD spreads
- **If blowing out:** Treat KRE cheapness as VALUE TRAP, not mean-reversion

### Event Filters
- SVB-style runs
- Policy changes targeting regionals
- **During stress:** Widen entry thresholds (use |Z| > 2.5) or stand aside

---

## 4. Implementation Template

**Universe:** KRE vs XLF (or options on each for convex RV)

**Signal:** 126-day Z-score of ratio, confirmed by 252-day Z-score (avoid fighting structural trends)

**Entry Rules:**
| Direction | Condition |
|-----------|-----------|
| Long KRE / Short XLF | Z_126 < -1.75 AND yield curve stopped flattening (1mo basis) |
| Long XLF / Short KRE | Z_126 > +1.75 AND curves not aggressively steepening |

**Exit Rules:**
- Close when Z_126 returns to between -0.5 and +0.5
- OR max holding period (60 trading days)
- Whichever comes first

**Risk Controls:**
- Hard stop if spread moves another 1-1.5σ against you
- Exit immediately if discrete policy/bank-failure headline changes regime

---

## 5. Integration with Existing Workflow

**Daily logging:**
- Log KREXLF_PCT_DIFF as spread variable
- Compute rolling Z-scores (126d and 252d)
- Overlay with curve and liquidity dashboards

**Use case:**
- Sector-internal RV sleeve (not SPX hedge)
- Express "regionals vs bulge-bracket/fintech" conditional on macro
- Conditional on REGINALD's stress assessment

---

## Current Status (Feb 20, 2026)

### 3-Month Lookback Analysis

**KRE has materially outperformed XLF over past 3 months:**
- KRE/XLF ratio up ~11-12%
- KRE: +16.25% vs XLF: +4.56% (90-day comparison)
- Relative gain: +11.7 percentage points for KRE

**Z-Score Estimate (without exact daily data):**
- Current ratio R_t = KRE/XLF is well above 3-6 month mean
- Likely Z-score: **+1.5 to +2.0 range** (KRE rich vs XLF)
- This is in or near "fade KRE / add XLF" territory

**Interpretation:**
- Last 3 months = completed or maturing KRE outperformance leg
- NOT an early cheapening — caution on new KRE longs vs XLF
- Potential mean-reversion candidate: short KRE / long XLF if ratio extends further

### Feb 19 Intraday Action

**1-day performance:**
- XLF: -0.84%
- KRE: -0.55%
- KRE outperformed by ~29bps

**Intraday pattern:**
- Tightly correlated curves (same peaks/troughs)
- Sector-wide move, not idiosyncratic to regionals
- KRE underperformed early session, then flipped to outperform in afternoon
- Into close: both rally, but KRE rises more steeply (short-covering / dip-buying)

**Interpretation:**
- Systematic financial-sector risk-off (both red)
- Small KRE outperformance suggests stress is more about big-cap financials/rate repricing than renewed regional fear
- Slightly tightens spread in KRE's favor — not regime-change, but could be first sign of short-term bounce

### Tactical Implications for Thesis

**Current state: KRE rich vs XLF**
- 3-month rally puts KRE in expensive territory relative to XLF
- RV framework argues against new long-KRE/short-XLF trades
- Instead, watch for short-KRE/long-XLF opportunities if ratio extends

**Consistency with directional puts:**
- Our KRE puts thesis = directional bearish on regionals
- KRE being "rich" vs XLF on RV basis SUPPORTS bearish view
- The catch-up rally may be done; mean-reversion would hurt KRE

**Key question:** Is yesterday's KRE outperformance:
- A) Continuation of 3-month catch-up (still has room)
- B) Final gasp before mean-reversion (our thesis)

**Watch for:**
- If KRE continues outperforming while credit stress builds = value trap forming
- If XLF starts outperforming = market pricing regional-specific risk

**Integration with thesis:**
- If KRE puts are the directional bet, this framework provides RV hedge context
- Can express same view via KRE/XLF spread instead of outright puts
- Useful for managing around OpEx and liquidity events
- **Current RV signal: KRE rich, supports bearish directional view**

---

## Pseudo-Code Outline

```python
import pandas as pd
import numpy as np

def calc_kre_xlf_zscore(kre: pd.Series, xlf: pd.Series, lookback: int = 126):
    """Calculate KRE/XLF ratio Z-score"""
    ratio = kre / xlf
    rolling_mean = ratio.rolling(lookback).mean()
    rolling_std = ratio.rolling(lookback).std()
    zscore = (ratio - rolling_mean) / rolling_std
    return zscore

def generate_signal(zscore: float, curve_regime: str, credit_stress: bool):
    """Generate trade signal with macro overlay"""
    if credit_stress:
        return "STAND_ASIDE"  # Don't fade crisis
    
    if zscore < -1.75 and curve_regime in ["steepening", "stable"]:
        return "LONG_KRE_SHORT_XLF"
    elif zscore > 1.75 and curve_regime != "steepening":
        return "SHORT_KRE_LONG_XLF"
    elif -0.5 < zscore < 0.5:
        return "CLOSE_POSITION"
    else:
        return "HOLD"
```

---

## References

- Historical correlation: ~0.68
- KRE 10Y return: 6.3% annualized
- XLF 10Y return: 12.0% annualized
- KRE volatility: 6.8% (1M rolling)
- XLF volatility: 3.8% (1M rolling)
- KRE Sharpe: 0.50
- XLF Sharpe: 1.19
