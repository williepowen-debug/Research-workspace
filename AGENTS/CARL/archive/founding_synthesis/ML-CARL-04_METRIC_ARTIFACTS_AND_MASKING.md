# ML-CARL-04: Metric Artifacts & Masking Effects

**ID:** ML-CARL-04
**Timestamp:** 2026-01-24
**Session:** CARL 009
**Domain:** CARL (Methodology)
**Status:** WARNING
**Confidence:** 80%

---

## Summary

Several metrics tracked by CARL and sub-agents are **artifacts** or subject to **masking effects** that make stress appear lower than reality. This entry documents known distortions to prevent over-reliance on misleading indicators.

**Key Warning:** Aggregate metrics (savings rate, medical debt, CPI) systematically mask distributional stress. The "average" American doesn't exist — K-shape bifurcation means top 20% and bottom 60% are in fundamentally different financial realities.

---

## Artifact 1: Medical Debt Collections ($88B)

### The Metric
- $88B medical debt in collections
- Cited by: DOC, POLLY, CARL
- Trend: Appears stable/improving

### The Artifact
VX-DOC-3.02 notes: *"Apparent improvement is policy artifact; underlying debt unchanged"*

**What happened:**
- Major credit bureaus removed small medical debts from reports (2022-2023)
- This made the VISIBLE number decline
- Underlying debt did NOT decline
- People still owe the money; it just doesn't show on credit reports

### True State
- $88B is the VISIBLE floor
- Additional $50-100B in pre-collections (ML-CR-18)
- True medical debt likely **$140-220B**

### Action
Do NOT interpret $88B stability as improvement. Track medical debt complaints (CFPB) as alternative signal.

---

## Artifact 2: Aggregate Savings Rate (4.5%)

### The Metric
- Personal savings rate: 4.5%
- VX-CARL-3.04 threshold: 3%
- Status: CRITICAL (but above threshold)

### The Masking Effect
**K-shape bifurcation:**

| Segment | Estimated Rate | Population |
|---------|----------------|------------|
| Top 10% | 15-25% | Pulling average up |
| Next 20% | 5-10% | Moderate savers |
| Middle 30% | 0-3% | Break-even |
| Bottom 40% | ~0% (negative) | Dissaving |

**Weighted average = 4.5%, but MEDIAN ≈ 0%**

### Evidence
- 37% can't cover $400 (VX-CARL-5.01)
- 62% paycheck-to-paycheck (VX-CARL-5.04)
- 4.8% hardship 401k withdrawals ATH (VX-CARL-4.01)

These are incompatible with a "healthy" 4.5% savings rate.

### True State
For the **bottom 60%**, the savings rate master switch is already at 0%. The 3% threshold is irrelevant for this population.

### Action
- Track savings by income quintile when data available
- Weight bottom 40% savings rate as the relevant stress indicator
- Consider 4.5% aggregate as **non-informative** for stress analysis

---

## Artifact 3: BNPL Delinquency Rates (2.3%)

### The Metric
- Affirm 30+ DQ: 2.3%
- Status: NORMAL
- Trend: Declining

### The Masking Effect
**Correlation risk hidden by individual metrics:**

| Factor | Value | Implication |
|--------|-------|-------------|
| Stacking rate | 63% | Most borrowers have multiple loans |
| Cross-firm stacking | 32% | Loans across different providers |
| Individual DQ | 2.3% | Each loan performing "fine" |

When 63% are stacking, one trigger event (job loss, medical) causes borrower to miss ALL loans simultaneously. The 2.3% could spike to **15-20%** very quickly.

### Historical Parallel
2008 CDOs: Individual mortgage performance was acceptable, but systemic correlation (housing prices) meant cascading failure when trigger hit.

### True State
BNPL is a **correlated system** masquerading as diversified risk. Individual delinquency rates are misleading.

### Action
- Track stacking rate (VX-NICK-1.02) as PRIMARY risk indicator
- Treat 2.3% DQ as floor, not ceiling
- Model correlation scenario: 63% × trigger probability = cascade DQ

---

## Artifact 4: CPI-Based Cost Metrics

### The Metrics
- Healthcare CPI: 3.2% YoY
- Auto insurance: In CPI basket
- Homeowners insurance: In CPI basket

### The Masking Effect

| Category | CPI Says | Reality | Gap |
|----------|----------|---------|-----|
| Healthcare | 3.2% | 7-9% (employer actual) | 2-3x |
| Auto insurance | Weighted in basket | +64% cumulative 2020-2025 | Cumulative masked |
| Homeowners | Weighted in basket | +50% YoY in high-risk zips | Geographic masked |

**CPI methodology issues:**
- Substitution effects (assumes switching to cheaper options)
- Geographic averaging (masks regional extremes)
- Quality adjustment (assumes "improvements" offset price)
- Weighting (may not match actual household budget)

### True State
**Real household cost burden is 1.5-2x what CPI suggests** for key stress categories.

### Action
- Do NOT use CPI as primary stress threshold
- Use category-specific data (KFF for health, III for insurance)
- Adjust CPI-based thresholds upward by 1.5x minimum

---

## Artifact 5: Uninsured Motorist Rate (15.4% vs 33.4%)

### The Metrics
- Uninsured motorists: 15.4% (NAIC/IRC)
- "Inadequately insured": 33.4% (CARL boot doc)

### The Confusion
These are DIFFERENT metrics:
- 15.4% = literally no insurance
- 33.4% = uninsured + underinsured combined
- Underinsured = ~18% (have insurance but inadequate limits)

### Why It Matters
For conversion analysis:
- Uninsured + accident = 100% personal liability
- Underinsured + accident = liability EXCEEDING coverage (partial protection)

The 33.4% faces financial risk from accidents; severity differs.

### Action
- Clarify which metric is being used in each context
- Track both separately
- Note: 4% of settlements exceed policy limits (LV-01 research)

---

## Artifact 6: Credit Card DQ Rate (11.35-12.3%)

### The Metric
- VX-CARL-1.01: 11.35-12.3%
- Threshold: 13.7%
- Status: CRITICAL (approaching)

### Potential Masking
This measures **visible** delinquency. It does NOT capture:
- Zombie borrowers (minimum payment only, technically current)
- Phantom debt (cash advances, BNPL not on credit report)
- Payment prioritization (people may pay CC while missing other bills)

### Context from Other Data
- VX-CARL-1.02: Minimum payment rate at 12-year HIGH (BREACHED)
- ML-CR-18: $150-200B phantom debt
- 62% paycheck-to-paycheck

The 11.35-12.3% is the **floor** of stress, not the full picture.

### Action
- Weight VX-CARL-1.02 (minimum payment) as leading indicator
- The DQ rate will spike AFTER zombie borrowers exhaust options
- Current DQ understates true stress by estimated 20-30%

---

## Artifact 7: Unemployment Rate

### The Metric
- Headline U-3: ~4%
- Often cited as "economy healthy"

### The Masking Effects
Not tracked as CARL vector, but relevant context:

| Issue | Effect |
|-------|--------|
| Labor force participation | Dropouts not counted |
| Underemployment (U-6) | Part-time wanting full-time not counted |
| Gig classification | Some gig workers not counted as employed |
| Quality of employment | Full-time vs. gig not distinguished |

### Relevance to CARL
- VX-CARL-3.01 (Jobs spread) is better leading indicator
- VX-GIG-2.06 (Utilization) captures gig underemployment
- VX-POP employment vectors capture small business reality

### Action
Do NOT rely on headline unemployment as stress invalidation signal.

---

## Summary: Metric Reliability Matrix

| Metric | Reliability | Issue | Alternative |
|--------|-------------|-------|-------------|
| Medical debt ($88B) | LOW | Policy artifact | CFPB complaints, pre-collections estimate |
| Savings rate (4.5%) | LOW | K-shape masking | Bottom 40% rate, $400 coverage |
| BNPL DQ (2.3%) | MEDIUM | Correlation hidden | Stacking rate (63%) |
| CPI components | LOW-MEDIUM | Methodology masks reality | Category-specific sources |
| Credit card DQ | MEDIUM | Misses zombies, phantom | Minimum payment rate |
| Unemployment | LOW | Multiple exclusions | Jobs spread, GIG utilization |

---

## Recommendations

### For Threshold Setting
- Adjust CPI-based thresholds upward by 1.5x
- Use distribution-aware metrics over aggregates
- Weight leading indicators (behavior) over lagging (delinquency)

### For Interpretation
- Treat "healthy-looking" aggregates with skepticism
- Cross-reference with distributional data
- When aggregate and distributional data conflict, trust distributional

### For Reporting
- Note artifact/masking issues when citing affected metrics
- Provide context from alternative indicators
- Avoid false precision from artifacted data

---

## Cross-References

- ML-CARL-03 (Pattern Analysis) — Identifies these issues in context
- VX-DOC-3.02 (Medical Debt note)
- VX-CARL-3.04 (Savings rate)
- VX-NICK-1.01, 1.02 (BNPL metrics)
- ML-CR-18 (Phantom Debt)

---

*Created: 2026-01-24 | Session: CARL 009 | Author: CARL*
*Type: Methodology Warning | Diagnostic Value: HIGH*
