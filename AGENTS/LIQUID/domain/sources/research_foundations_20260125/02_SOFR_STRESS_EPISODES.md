# Research Prompt: SOFR Stress Episodes & Early Warning Indicators

## Objective

Research historical episodes of SOFR (Secured Overnight Financing Rate) stress, what caused them, and what early warning indicators preceded them. This supports LIQUID's monitoring of the SOFR-IORB spread as a primary funding stress indicator.

---

## Context

**Current Situation (as of Jan 2026):**
- SOFR is approximately 4.30% (near IORB)
- SOFR-IORB spread is currently ~+3bps (normal)
- LIQUID's thresholds: +15bps Yellow, +25bps Orange, +50bps Red

**Why This Matters:**
SOFR is the benchmark rate for overnight secured (repo) funding. When SOFR spikes above IORB:
- It signals that secured funding is more expensive than it "should" be
- Banks and dealers are competing for funding
- Liquidity is tight in the repo market
- This can cascade to broader credit tightening

**Key Relationship:**
- IORB (Interest on Reserve Balances): What banks earn parking cash at the Fed
- SOFR: What the market pays for overnight secured funding
- Normal: SOFR trades near or slightly below IORB
- Stress: SOFR trades significantly above IORB

---

## Research Questions

### 1. SOFR Mechanics
- How is SOFR calculated? (tri-party repo, bilateral, GCF)
- What is the typical SOFR-IORB spread in normal conditions?
- What drives day-to-day SOFR volatility?
- How does SOFR relate to Fed Funds?

### 2. Historical Stress Episodes
Identify and analyze episodes where SOFR spiked significantly:
- **September 2019** — Repo rate spike (pre-SOFR transition but relevant)
- **Quarter-end spikes** — What happens at quarter-end?
- **Month-end patterns** — Treasury settlement effects
- **Any 2022-2025 stress episodes** — What happened during QT?

For each episode:
- What was the magnitude of the spike?
- How long did it last?
- What caused it?
- How did it resolve?

### 3. Drivers of SOFR Stress
What conditions cause SOFR to spike?
- Reserve scarcity
- Large Treasury settlement
- Quarter-end balance sheet constraints
- Foreign flows (selling pressure)
- Dealer balance sheet capacity
- MMF behavior

### 4. Early Warning Indicators
What metrics tend to move BEFORE SOFR spikes?
- Reserve levels
- Dealer repo positions
- T-bill supply
- Treasury settlement calendar
- Intraday repo rate volatility
- Fed facility usage (SRF, discount window)

### 5. Thresholds and Significance
- What SOFR-IORB spread level is considered "stress"?
- What spread triggered Fed action in the past?
- What is the relationship between spread magnitude and systemic risk?

---

## Data Sources to Check

**Primary (Official):**
- NY Fed SOFR data: https://www.newyorkfed.org/markets/reference-rates/sofr
- NY Fed repo operations data
- FRED SOFR series (SOFR)
- Fed H.15 release (interest rates)

**Analysis:**
- NY Fed Liberty Street Economics (search for SOFR, repo)
- BIS Quarterly Review (money market sections)
- Federal Reserve staff papers
- OFR (Office of Financial Research) money market reports

**Historical:**
- Sept 2019 coverage (WSJ, FT, Bloomberg archives)
- Quarter-end repo market analyses

---

## Deliverables

### A. Narrative Analysis

1. **SOFR Mechanics Explained**
   - How it's calculated, what it represents
   - Normal trading range vs. IORB

2. **Historical Stress Catalog**
   - Timeline of significant SOFR stress events
   - Causes, magnitude, duration, resolution for each

3. **Stress Driver Analysis**
   - What conditions create SOFR stress
   - Which factors are most predictive

4. **Early Warning Framework**
   - Leading indicators to monitor
   - How much advance warning do they provide

### B. Key Numbers

Capture these data points with dates and sources:
- Current SOFR rate
- Current IORB rate
- Normal SOFR-IORB spread range
- Peak spreads during stress episodes (with dates)
- Fed intervention thresholds (if stated)
- SRF usage instances

### C. Threshold Validation

LIQUID currently uses these thresholds for SOFR-IORB spread:
- +15bps = Yellow (Watch)
- +25bps = Orange (Alert)
- +50bps = Red (Critical)

Based on your research:
- Are these thresholds appropriate?
- Should they be adjusted?
- What spread level historically triggered Fed action?

### D. Monitoring Checklist

Provide a practical checklist: What should be monitored daily/weekly to anticipate SOFR stress?

---

## Output Format

```
# SOFR Stress Research Results

## Executive Summary
[Key findings in 2-3 paragraphs]

## 1. SOFR Mechanics
[How it works, normal behavior]

## 2. Historical Stress Episodes
[Catalog of events with analysis]

## 3. Stress Drivers
[What causes SOFR to spike]

## 4. Early Warning Indicators
[Leading indicators with typical lead time]

## 5. Key Data Points
| Metric | Value | Date | Source |
|--------|-------|------|--------|
| ... | ... | ... | ... |

## 6. Threshold Assessment
[Evaluation of LIQUID's current thresholds]

## 7. Monitoring Checklist
[Practical daily/weekly monitoring list]

## 8. Data Gaps
[What couldn't be found]

## Sources
[Full source list]
```

---

## Notes

- SOFR-IORB spread is LIQUID's primary funding stress indicator (VX-LIQUID-1.01)
- Focus on actionable thresholds and early warning
- Sept 2019 is the key historical analog even though it pre-dates SOFR adoption
- Flag any data that's stale or requires terminal access

---

*LIQUID Research Prompt 02 | SOFR Stress Episodes*
