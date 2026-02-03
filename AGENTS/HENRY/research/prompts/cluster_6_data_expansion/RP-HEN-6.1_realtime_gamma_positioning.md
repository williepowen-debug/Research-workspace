# RP-HEN-6.1: Real-Time Gamma & Options Positioning Data

**Prompt ID:** RP-HEN-6.1
**Cluster:** Data Expansion
**Priority:** 1 (Highest)
**Created:** 2026-02-03

---

## Context for Research Assistant

HENRY tracks market structure and systemic risk. We already know 0DTE options represent ~59% of SPX volume (VX-HEN-6.01), but we lack REAL-TIME positioning data that shows when dealer hedging flips from suppressing volatility to amplifying it. This research should identify the best data sources, metrics, and thresholds for monitoring gamma exposure in real-time.

Current HENRY context:
- 0DTE Volume Ratio: 59% of SPX options (ORANGE)
- VIX: 16.07 (complacent)
- Retail Options % Volume: 48% (RED, ATH)
- Sentiment Composite: 8.5/10 (RED)

---

## Research Questions

### 1. GAMMA EXPOSURE (GEX) FUNDAMENTALS
- What exactly is Gamma Exposure Index (GEX)?
- How is aggregate market GEX calculated?
- What does positive vs negative GEX mean for price behavior?
- What is the "Gamma Flip" or "Gamma Neutral" level?
- How does GEX affect expected daily price ranges?

### 2. DATA PROVIDERS & SOURCES
- **SpotGamma**: What metrics do they provide? Cost? Data format?
- **SqueezeMetrics**: What is their DIX/GEX offering?
- **GammaLab**: Capabilities and coverage?
- **Unusual Whales**: Options flow data quality?
- **CBOE**: What raw data is publicly available?
- **Bloomberg/Refinitiv**: Professional terminal gamma tools?
- Rank providers by: accuracy, timeliness, cost, accessibility

### 3. KEY METRICS TO TRACK
For each metric, provide:
- Definition and calculation methodology
- Interpretation (what values are bullish/bearish/neutral)
- Historical ranges and current readings if available
- Recommended thresholds for HENRY alerts

Metrics to research:
- **Net GEX** (aggregate gamma exposure)
- **Gamma Flip Level** (price where dealers flip long/short gamma)
- **Vanna Exposure** (sensitivity to volatility changes)
- **Charm Exposure** (time decay positioning effects)
- **Put Wall / Call Wall** (concentrated strike levels)
- **0DTE-specific GEX** (same-day gamma vs longer-dated)
- **Dealer Delta** (net directional exposure)
- **Vol Trigger** (level where volatility regime shifts)

### 4. INTRADAY PATTERNS & SIGNALS
- How does GEX typically evolve through a trading day?
- What patterns emerge around OPEX (options expiration)?
- How does GEX behave on volatile days vs calm days?
- What are reliable leading indicators of gamma-driven moves?
- How quickly can GEX flip from positive to negative?

### 5. HISTORICAL CASE STUDIES
Analyze gamma positioning during:
- **August 5, 2024** (Japan carry trade unwind, VIX spike to 65)
- **March 2020** (COVID crash)
- **January 2021** (GME/meme stock gamma squeeze)
- **February 2018** (Volmageddon)
- What did GEX readings show before/during these events?

### 6. INTEGRATION WITH OTHER INDICATORS
- How does GEX interact with VIX?
- Relationship between GEX and realized volatility?
- Does GEX predict next-day returns?
- How to combine GEX with put/call ratio for better signals?
- Academic research on gamma's predictive power?

### 7. PRACTICAL IMPLEMENTATION
- What update frequency is needed? (Real-time vs EOD vs weekly)
- Can gamma data be approximated without paid subscriptions?
- Open-source tools or APIs for gamma calculation?
- What raw CBOE/OCC data could HENRY use to calculate own estimates?

---

## Output Format Requested

```markdown
# Real-Time Gamma & Options Positioning - Research Output

## Executive Summary
[5-7 bullet points of key findings]

## 1. GEX Fundamentals
[Clear explanations with examples]

## 2. Data Provider Comparison
| Provider | Metrics | Cost | Timeliness | Accessibility | Recommendation |
|----------|---------|------|------------|---------------|----------------|
| ... | ... | ... | ... | ... | ... |

## 3. Key Metrics for HENRY
| Metric | Definition | Bullish | Neutral | Bearish | Alert Threshold |
|--------|------------|---------|---------|---------|-----------------|
| Net GEX | ... | ... | ... | ... | ... |
| Gamma Flip | ... | ... | ... | ... | ... |
[Continue for all metrics]

## 4. Intraday Patterns
[Typical patterns with times/triggers]

## 5. Historical Case Studies
| Event | Date | GEX Before | GEX During | Key Lesson |
|-------|------|------------|------------|------------|
| ... | ... | ... | ... | ... |

## 6. Indicator Integration
[How GEX combines with existing HENRY vectors]

## 7. Implementation Recommendations
[Practical steps for HENRY to add gamma monitoring]

## Proposed New Vectors for HENRY
[Specific vector definitions ready for VX.tsv]

## Sources
[URLs, papers, data feeds]
```

---

## Integration Notes for HENRY

After receiving this research:
- Create VX-HEN-9.01 (Net GEX)
- Create VX-HEN-9.02 (Gamma Flip Level)
- Create VX-HEN-9.03 (0DTE GEX)
- Create VX-HEN-9.04 (Put Wall)
- Create VX-HEN-9.05 (Call Wall)
- Add gamma cascade to FLOW.tsv transmission paths
- Establish daily monitoring routine

---

*Prompt ready for external LLM research*
