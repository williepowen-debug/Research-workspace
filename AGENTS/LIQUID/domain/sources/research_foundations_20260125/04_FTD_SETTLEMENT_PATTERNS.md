# Research Prompt: Treasury Fails-to-Deliver (FTD) Patterns

## Objective

Research Treasury securities Fails-to-Deliver (FTD) patterns — what drives them, historical levels, and what elevated FTD indicates about market stress. This supports LIQUID's monitoring of settlement system health.

---

## Context

**Current Situation (as of Jan 2026):**
- Treasury FTD approximately $42.4 billion
- This is elevated but below crisis levels
- LIQUID's thresholds: $40B Yellow, $50B Orange, $60B Red

**Why This Matters:**
FTD occurs when a party fails to deliver securities on settlement date. Elevated FTD indicates:
- Collateral scarcity (hard to locate specific securities)
- Settlement infrastructure stress
- Short selling pressure without locate
- Potential market dysfunction

Treasury FTD is particularly important because Treasuries serve as collateral throughout the financial system.

---

## Research Questions

### 1. FTD Mechanics
- What exactly is a fail-to-deliver in Treasury markets?
- How does Treasury settlement work (T+1)?
- What are the penalties for failing?
- Who reports FTD data and how often?
- What's the difference between "fails" and "aged fails"?

### 2. Historical FTD Levels
- What is "normal" Treasury FTD?
- What are historical peaks?
- What was FTD during:
  - 2008 financial crisis?
  - March 2020 COVID stress?
  - Other stress periods?
- Is there seasonality (month-end, quarter-end)?

### 3. Drivers of FTD
What causes FTD to rise?
- Collateral scarcity (specific issues in high demand)
- Short selling activity
- Repo market dynamics (collateral re-use)
- Settlement infrastructure issues
- Large auction settlements
- Dealer balance sheet constraints

### 4. FTD and Market Stress
- What is the relationship between FTD and funding stress?
- Does FTD lead or lag other stress indicators?
- At what level does FTD become systemically concerning?
- What happens if FTD stays elevated?

### 5. Fed/FICC Response
- What tools exist to address FTD?
- Securities lending facilities
- FICC (Fixed Income Clearing Corporation) role
- Have regulators expressed concern about FTD levels?

---

## Data Sources to Check

**Primary (Official):**
- Federal Reserve Treasury fails data: https://www.newyorkfed.org/data-and-statistics/data-visualization/treasury-securities-operations
- SEC FTD data (though this is more equity-focused)
- DTCC/FICC reports
- Treasury Market Practices Group (TMPG) reports

**Analysis:**
- NY Fed Liberty Street Economics
- OFR (Office of Financial Research) reports
- TMPG best practices documents
- Academic papers on Treasury market microstructure

**Historical:**
- 2008 fails crisis coverage
- March 2020 Treasury market stress analysis
- TMPG historical reports

---

## Deliverables

### A. Narrative Analysis

1. **FTD Mechanics Explained**
   - What is a fail, why it happens
   - Settlement process and penalties
   - Reporting and data availability

2. **Historical Analysis**
   - Timeline of FTD levels
   - Major spikes and their causes
   - How spikes resolved

3. **Driver Analysis**
   - What conditions elevate FTD
   - Leading vs. lagging relationship to other stress
   - Specific securities vs. broad-based fails

4. **Systemic Implications**
   - What elevated FTD means for markets
   - Relationship to collateral scarcity
   - Connection to repo/funding stress

5. **Mitigation Mechanisms**
   - How the system handles elevated fails
   - Fed/FICC tools
   - Regulatory attention

### B. Key Numbers

| Metric | Value | Date | Context | Source |
|--------|-------|------|---------|--------|
| Current FTD | ~$42.4B | Jan 2026 | Elevated | NY Fed |
| Normal range | ? | - | Baseline | Research |
| 2008 peak | ? | ? | Crisis | Historical |
| March 2020 peak | ? | ? | COVID | Historical |
| ... | ... | ... | ... | ... |

### C. Threshold Validation

LIQUID's current thresholds:
- $40B = Yellow (Watch)
- $50B = Orange (Alert)
- $60B = Red (Critical)

Based on research:
- Are these appropriate?
- What levels historically indicated stress?
- Should thresholds be percentage-based rather than absolute?

### D. Monitoring Guidance

- How often is FTD data updated?
- What lag is there in reporting?
- Are there leading indicators that predict FTD spikes?
- What specific patterns should trigger concern?

---

## Output Format

```
# Treasury FTD Research Results

## Executive Summary
[Key findings]

## 1. FTD Mechanics
[How it works, why it matters]

## 2. Historical Analysis
[Timeline, major episodes]

## 3. Driver Analysis
[What causes FTD to rise]

## 4. Systemic Implications
[What elevated FTD means]

## 5. Mitigation Mechanisms
[How system responds]

## 6. Key Data Points
[Table of values]

## 7. Threshold Assessment
[Evaluation of LIQUID's thresholds]

## 8. Monitoring Guidance
[Practical monitoring advice]

## 9. Data Gaps
[What couldn't be found]

## Sources
[Full list]
```

---

## Notes

- FTD is tracked via VX-LIQUID-1.03
- Note the data lag — FTD reporting is typically delayed
- Focus on Treasury FTD specifically (not equity)
- The $42.4B current level is already in YELLOW territory per LIQUID's thresholds
- Connection to repo market is important — FTD can indicate collateral scarcity

---

*LIQUID Research Prompt 04 | FTD Settlement Patterns*
