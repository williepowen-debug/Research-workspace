# Real-Time Gamma & Options Positioning - Research Output

**Prompt ID:** RP-HEN-6.1
**Completed:** 2026-02-03
**Research Source:** Web research + provider documentation

---

## Executive Summary

- **GEX (Gamma Exposure)** measures dealers' hedging obligations — positive GEX = volatility suppression, negative GEX = volatility amplification
- **Gamma Flip Level** is the critical price where dealer positioning flips from long to short gamma — below this level, dealers sell into weakness (amplifying moves)
- **Key providers:** SpotGamma (professional, paid), SqueezeMetrics (free DIX/GEX), Barchart (free basic GEX), GEXStream (emerging)
- **0DTE concentration** creates unique intraday gamma dynamics not present in historical data
- **August 5, 2024** stress test showed 0DTE volume collapsed 26% during VIX spike — gamma mechanics can self-reinforce in crisis
- **HENRY should track:** Net GEX, Gamma Flip Level, Put/Call Walls, 0DTE-specific gamma, DIX (dark pool sentiment)

---

## 1. GEX Fundamentals

### What is Gamma Exposure (GEX)?

**Gamma Exposure** measures the aggregate hedging obligations of options market makers based on their positions. It quantifies how much dealers need to buy or sell the underlying asset as prices move.

**Key mechanics:**
- **Positive GEX (Long Gamma):** Dealers hedge by *buying* as prices fall and *selling* as prices rise → stabilizes market, suppresses volatility
- **Negative GEX (Short Gamma):** Dealers hedge by *selling* as prices fall and *buying* as prices rise → amplifies moves, increases volatility

**Calculation (simplified):**
```
GEX = Σ (Option Gamma × Open Interest × Spot Price² × 100)
Calls contribute positive GEX
Puts contribute negative GEX
```

### Gamma Flip Level

The **Gamma Flip** (or "Gamma Neutral") level is the price at which aggregate dealer gamma transitions from positive to negative:
- **Price ABOVE Gamma Flip:** Dealers are net long gamma → market stabilization
- **Price BELOW Gamma Flip:** Dealers are net short gamma → volatility acceleration

This level functions as a critical support/resistance zone. Breaking below Gamma Flip often precedes accelerated selling.

### Put Wall / Call Wall

- **Put Wall:** Strike with highest put gamma/OI — acts as support (dealers buy to hedge)
- **Call Wall:** Strike with highest call gamma/OI — acts as resistance (dealers sell to hedge)
- Prices tend to gravitate between these walls during normal trading

---

## 2. Data Provider Comparison

| Provider | Metrics | Cost | Timeliness | Accessibility | Recommendation |
|----------|---------|------|------------|---------------|----------------|
| **SpotGamma** | GEX, Gamma Flip, Put/Call Walls, HIRO (real-time), SIV Index | $99-499/mo | Real-time | Subscription | **BEST for professional use** |
| **SqueezeMetrics** | DIX (dark pool), GEX (aggregate), G-ratio | Free (basic), API paid | EOD | Free charts | **BEST free option** |
| **Barchart** | Strike-level GEX, Flip Point, Walls | Free (delayed) | ~30min delay, EOD | Free with account | **Good for basic tracking** |
| **GEXStream** | Real-time GEX analytics | ~$50/mo | Real-time | Subscription | Emerging provider |
| **CBOE/OCC** | Raw options data | Free | EOD | Manual calculation | DIY approach |

### SpotGamma Key Features
- Proprietary GEX modeling beyond standard assumptions
- HIRO indicator: Real-time options flow detection
- SIV Index: Implied volatility forecasting
- 0DTE-specific filters
- Daily analysis reports

### SqueezeMetrics Key Features
- **DIX (Dark Index):** Dollar-weighted measure of dark pool buying vs selling
  - Higher DIX = bullish dark pool sentiment
  - Lower DIX = bearish/uncertain sentiment
- **GEX:** Aggregate gamma exposure for S&P 500
  - High GEX = low expected volatility
  - Low/negative GEX = high expected volatility, but losses unlikely to extend
- **G (Gamma Ratio):** Proportion of call gamma to total gamma (0.5 = balanced)
- Free charts at squeezemetrics.com/monitor/dix
- API available for paid subscribers

### Barchart Key Features
- Free GEX by strike visualization
- Configurable expiration dates (weekly/monthly)
- Gamma Flip point calculated from aggregate positioning
- Put/Call Wall identification
- Updated every ~5 minutes (25-30 min delay)
- Available at barchart.com/stocks/quotes/$SPX/gamma-exposure

---

## 3. Key Metrics for HENRY

| Metric | Definition | Bullish | Neutral | Bearish | Alert Threshold |
|--------|------------|---------|---------|---------|-----------------|
| **Net GEX** | Aggregate gamma exposure ($ billions) | >$5B | $0-5B | <$0 | Flip to negative |
| **Gamma Flip Level** | Price where dealer gamma flips | Price well above | Price near | Price below | SPX breaks below |
| **Put Wall** | Highest put OI/gamma strike | Price above | Price at | Price below | Break of wall |
| **Call Wall** | Highest call OI/gamma strike | Approaching | Price at | Price well above | Sustained above |
| **DIX** | Dark pool buying ratio | >45% | 40-45% | <40% | <38% or divergence |
| **G (Gamma Ratio)** | Call gamma / total gamma | >0.55 | 0.45-0.55 | <0.45 | Extreme readings |
| **0DTE GEX %** | 0DTE contribution to total GEX | <30% | 30-50% | >50% | >60% concentration |

### Interpretation Framework

**Bullish Setup:**
- GEX positive and rising
- Price above Gamma Flip
- DIX rising (dark pool accumulation)
- Put Wall providing support below

**Bearish Setup:**
- GEX negative or falling toward zero
- Price approaching or below Gamma Flip
- DIX falling (dark pool distribution)
- Call Wall providing resistance above

**High Volatility Warning:**
- GEX deeply negative
- Price below Gamma Flip and Put Wall
- Large 0DTE concentration
- Low DIX

---

## 4. Intraday Patterns

### Typical Daily GEX Evolution

| Time (ET) | Pattern | Notes |
|-----------|---------|-------|
| Pre-market | GEX calculated from prior EOD | Sets opening expectations |
| 9:30-10:00 | High gamma activity | 0DTE opening flow, dealer hedging |
| 10:00-11:30 | Gravitational pull to key levels | Price tends toward Put/Call walls |
| 11:30-14:00 | Lower gamma activity | Midday lull |
| 14:00-15:00 | 0DTE gamma intensifies | Same-day expiration hedging accelerates |
| 15:00-16:00 | Maximum 0DTE gamma | Final hour most gamma-sensitive |
| 15:45-16:00 | Gamma collapse | 0DTE expires, hedges unwound |

### OPEX (Options Expiration) Patterns
- **Monthly OPEX (3rd Friday):** Largest gamma unwind, increased volatility
- **Weekly OPEX:** Moderate gamma effects
- **0DTE daily:** Intraday gamma "reset" at 4pm ET

### Gamma-Driven Move Signatures
1. **Pin action:** Price gravitates to high-OI strike as expiration approaches
2. **Gamma squeeze (up):** Short calls force dealer buying, accelerating rally
3. **Gamma squeeze (down):** Short puts force dealer selling, accelerating decline
4. **Vol expansion:** Break of Gamma Flip triggers dealer selling into weakness

---

## 5. Historical Case Studies

| Event | Date | GEX Before | GEX During | Key Lesson |
|-------|------|------------|------------|------------|
| **Japan Carry Unwind** | Aug 5, 2024 | Moderately positive | Deeply negative | 0DTE volume collapsed 26% as VIX spiked to 65; gamma mechanics accelerated selloff |
| **COVID Crash** | Mar 2020 | Negative | Extremely negative | Put buying overwhelmed; no 0DTE then but similar dealer short gamma dynamics |
| **GME Squeeze** | Jan 2021 | Negative (puts) | Extremely positive (calls) | Massive call buying forced dealer buying; gamma squeeze mechanics textbook |
| **Volmageddon** | Feb 2018 | Mixed | VIX product collapse | Not pure gamma event but showed reflexivity in vol products |

### August 5, 2024 Detailed Analysis

The Japan carry trade unwind stress test revealed critical 0DTE dynamics:

1. **Pre-event:** 0DTE representing ~55-60% of SPX volume
2. **During event:** 0DTE volume dropped 26% — traders avoided same-day exposure
3. **Gamma effect:** With fewer 0DTE trades, dealer hedging dropped; remaining positions forced aggressive selling
4. **VIX spike:** Reached 65 intraday — highest since March 2020
5. **Key insight:** 0DTE can *withdraw liquidity* in crisis, not provide it

**HENRY implication:** 0DTE suppresses volatility in normal times but creates air pockets in stress. Track 0DTE volume ratio as stress indicator.

---

## 6. Indicator Integration

### GEX + VIX Relationship
- **Low VIX + High GEX:** Stable, low-vol environment (current HENRY status)
- **Low VIX + Low/Negative GEX:** Complacency + fragility (WARNING)
- **High VIX + Negative GEX:** Crisis mode, dealer amplification
- **Falling VIX + Rising GEX:** Recovery, stabilization

### GEX + Put/Call Ratio
Combine for confirmation:
- High P/C ratio + Negative GEX = bearish (put buying + dealer short gamma)
- Low P/C ratio + Positive GEX = bullish (call buying + dealer long gamma)
- Divergences = potential inflection points

### GEX + DIX (Dark Index)
- DIX rising + GEX stable = institutional accumulation (bullish)
- DIX falling + GEX falling = distribution (bearish)
- DIX high + GEX negative = smart money buying into weakness (contrarian bullish)

### Research on Predictive Power
- SqueezeMetrics white paper: High GEX historically correlates with 0.55% daily std dev vs 0.85% for lower GEX
- CFA Institute research (2025): VIX changes forecast MOVE (bond vol), suggesting equity vol leads
- Academic studies show gamma positioning explains portion of next-day returns

---

## 7. Implementation Recommendations

### Immediate Actions (Free Tier)
1. **Bookmark Barchart GEX page:** barchart.com/stocks/quotes/$SPX/gamma-exposure
2. **Track SqueezeMetrics daily:** squeezemetrics.com/monitor/dix
3. **Record EOD:** Net GEX, Gamma Flip, DIX, G-ratio

### Enhanced Monitoring (Paid)
1. **SpotGamma subscription** for real-time data and 0DTE analysis
2. **API integration** for automated tracking

### HENRY Daily Routine
1. Morning: Check prior EOD GEX, Gamma Flip level, major walls
2. Note: Is SPX above or below Gamma Flip?
3. Track: DIX trend (5-day MA)
4. Alert: If Gamma Flip breaks or DIX diverges from price

### Data Collection Without Subscription
Raw CBOE/OCC data can approximate GEX:
1. Download daily options chain (cboe.com)
2. Calculate gamma for each strike using BSM
3. Multiply by OI and spot price²
4. Sum calls positive, puts negative
5. Labor-intensive but possible for EOD tracking

---

## Proposed New Vectors for HENRY

| ID | Name | Current | Thresholds (G/Y/O/R) | Source | Frequency |
|----|------|---------|----------------------|--------|-----------|
| VX-HEN-9.01 | Net GEX ($ billions) | TBD | >$5B / $2-5B / $0-2B / <$0 | SpotGamma/Barchart | Daily |
| VX-HEN-9.02 | Gamma Flip Level | TBD | >2% above / 0-2% above / at level / below | SpotGamma/Barchart | Daily |
| VX-HEN-9.03 | DIX (Dark Index) | TBD | >45% / 42-45% / 40-42% / <40% | SqueezeMetrics | Daily |
| VX-HEN-9.04 | Gamma Ratio (G) | TBD | >0.55 / 0.50-0.55 / 0.45-0.50 / <0.45 | SqueezeMetrics | Daily |
| VX-HEN-9.05 | 0DTE GEX Contribution | ~59% | <40% / 40-50% / 50-60% / >60% | SpotGamma | Daily |
| VX-HEN-9.06 | Put Wall (SPX strike) | TBD | Record as level | Barchart | Daily |
| VX-HEN-9.07 | Call Wall (SPX strike) | TBD | Record as level | Barchart | Daily |

### Transmission Path Addition (FLOW.tsv)

```
GAMMA_CASCADE: Negative GEX → Price breaks Gamma Flip → Dealer selling → Accelerated decline → VIX spike → 0DTE withdrawal → Liquidity vacuum → Gap down risk
```

---

## Sources

### Data Providers
- SpotGamma: https://spotgamma.com
- SqueezeMetrics: https://squeezemetrics.com/monitor/dix
- Barchart: https://www.barchart.com/stocks/quotes/$SPX/gamma-exposure
- GEXStream: https://gexstream.com

### Documentation
- SpotGamma Support: https://support.spotgamma.com
- SqueezeMetrics Docs: https://squeezemetrics.com/monitor/docs
- SqueezeMetrics White Paper: https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf

### Research
- CFA Institute (2025): "Volatility Signals: Do Equities Forecast Bonds?"
- Reddit r/algotrading: GEX calculation methodology discussions
- Finance TLDR: "Predict the Market With Dark Index and Gamma Exposure"

---

*Research completed 2026-02-03 for HENRY agent integration*
