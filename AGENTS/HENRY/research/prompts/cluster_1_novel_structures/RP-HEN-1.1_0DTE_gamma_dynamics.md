# RP-HEN-1.1: 0DTE Options & Gamma Dynamics

**Prompt ID:** RP-HEN-1.1
**Cluster:** Novel Market Structures
**Priority:** 1 (Highest)
**Created:** 2026-01-26

---

## Context for Research Assistant

HENRY is investigating systemic risks from market structures that have no historical precedent. 0DTE (zero days to expiration) options on the S&P 500 have exploded in volume since 2022, now representing 40-50% of all SPX options volume. This is potentially the "portfolio insurance" of our era - the 1987 crash was accelerated by mechanical selling from portfolio insurance strategies. We need to understand if 0DTE creates similar systemic risk.

Current HENRY findings for context:
- S&P 500 CAPE ratio: 40.65 (97th percentile)
- Top 10 concentration: 38.22% (all-time high)
- VIX: 16.07 (complacent)

---

## Research Questions

### 1. SCALE & GROWTH
- What is the current daily notional volume of 0DTE SPX options?
- What percentage of total SPX options volume is now 0DTE?
- Chart the growth from 2020 to present
- Who are the primary participants? (Retail vs institutional breakdown)
- What is the typical daily open interest pattern?

### 2. MECHANICS OF GAMMA EXPOSURE
- Explain gamma exposure (GEX) in accessible terms
- How do market makers hedge 0DTE positions?
- What is "delta hedging" and how does it create mechanical buying/selling pressure?
- What is a "gamma squeeze" and under what conditions does it occur?
- How does 0DTE gamma differ from longer-dated options gamma?

### 3. DEALER POSITIONING DYNAMICS
- How do dealers typically position around major 0DTE strikes?
- What happens at key "pin" levels where open interest is concentrated?
- How does dealer hedging affect intraday volatility?
- What is "negative gamma" positioning and why does it amplify moves?

### 4. 1987 PORTFOLIO INSURANCE COMPARISON
- Describe how portfolio insurance worked in 1987
- What were the mechanical selling dynamics that accelerated the crash?
- Compare to 0DTE: What are the similarities?
  - Mechanical/algorithmic selling pressure
  - Feedback loops
  - Concentrated positioning
- Compare to 0DTE: What are the differences?
  - Daily reset vs continuous
  - Dealer hedging vs direct selling
  - Modern circuit breakers

### 5. STRESS SCENARIO ANALYSIS
- Model scenario: SPX gaps down 3% at open with large 0DTE call open interest
  - How do dealers adjust hedges?
  - What is the mechanical selling pressure?
  - Could this create cascade/feedback loop?
- Model scenario: SPX rallies sharply into large put open interest
  - What happens as puts go out of the money?
  - Does this create mechanical buying that amplifies?
- What happened on specific volatile days (e.g., August 5, 2024 Japan carry unwind)?

### 6. REGULATORY & STRUCTURAL CONCERNS
- Have regulators (SEC, CFTC, OCC) expressed concerns about 0DTE?
- Are there any academic papers analyzing 0DTE systemic risk?
- What do market structure experts say about 0DTE risks?
- Are there any proposed rule changes or monitoring efforts?

### 7. DATA SOURCES FOR ONGOING MONITORING
- Where can HENRY track daily 0DTE volume?
- Where are gamma exposure estimates published? (SpotGamma, SqueezeMetrics, etc.)
- What metrics should HENRY add to the vector dashboard?
- Recommended data sources with URLs

---

## Output Format Requested

Please structure your response as:

```markdown
# 0DTE Options & Gamma Dynamics - Research Output

## Executive Summary
[3-5 bullet points of key findings]

## 1. Scale & Growth
[Findings with specific numbers and dates]

## 2. Gamma Mechanics
[Clear explanation with examples]

## 3. Dealer Positioning
[How the market structure works]

## 4. 1987 Comparison
[Table comparing portfolio insurance to 0DTE]

## 5. Stress Scenarios
[Modeled scenarios with estimated impacts]

## 6. Regulatory Status
[Current regulatory stance and concerns]

## 7. Monitoring Recommendations
[Specific metrics and data sources for HENRY]

## Key Risks Identified
[Ranked list of systemic risks]

## Sources
[URLs and citations]
```

---

## Integration Notes for HENRY

After receiving this research:
- Create new vector VX-HEN-6.01 (0DTE Volume % of SPX Options)
- Create new vector VX-HEN-6.02 (Gamma Exposure Estimate)
- Add to FLOW.tsv: 0DTE gamma cascade transmission path
- Update ML.tsv with key findings
- Assess if 0DTE warrants ORANGE/RED status

---

*Prompt ready for external LLM research*
