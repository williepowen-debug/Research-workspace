# ML-CARL-05: Leading Indicator Gaps — Blind Spots in Current Tracking

**ID:** ML-CARL-05
**Timestamp:** 2026-01-24
**Session:** CARL 009
**Domain:** CARL (Methodology)
**Status:** GAP ANALYSIS
**Confidence:** 85%

---

## Summary

Systematic review of CARL and sub-agent vector files reveals a pattern: **lagging indicators are well-tracked, but leading indicators have significant "TBD" gaps**. This creates structural blind spots that may cause CARL to identify stress acceleration AFTER it begins rather than BEFORE.

**Key Finding:** The most critical leading indicators (earnings compression, cash runway, owner compensation, behavioral shifts) are disproportionately unmeasured.

---

## Gap Inventory by Agent

### GIG Agent — Leading Indicators MISSING

| Vector | Name | Status | Priority |
|--------|------|--------|----------|
| VX-GIG-1.01 | Rideshare Earnings/Hour | TBD | HIGH |
| VX-GIG-1.02 | Delivery Earnings/Hour | TBD | HIGH |
| VX-GIG-1.03 | Freelance Platform Rates | TBD | MEDIUM |
| VX-GIG-1.04 | Incentive/Bonus Spend | TBD | MEDIUM |
| VX-GIG-2.01 | Active Driver Count | TBD | MEDIUM |
| VX-GIG-2.02 | Multi-Apping Rate | TBD | HIGH |
| VX-GIG-2.03 | Hours to Target Income | TBD | HIGH |
| VX-GIG-2.04 | New Driver Acquisition Cost | TBD | MEDIUM |
| VX-GIG-4.01 | Platform Take Rate | TBD | MEDIUM |

**Why It Matters:**
GIG earnings compression is a LEADING indicator for:
- Shadow credit dependency (GIG→NICK chain)
- Buffer exhaustion (gig as safety net fails)
- Consumer stress (gig workers ARE consumers)

**Current State:**
We track GIG distress (58% emergency loans) but NOT the earnings pressure causing it.

---

### NICK Agent — Behavioral Indicators MISSING

| Vector | Name | Status | Priority |
|--------|------|--------|----------|
| VX-NICK-1.03 | BNPL Late Fee Revenue | TBD | MEDIUM |
| VX-NICK-2.02 | Payday Rollover Rate | TBD | HIGH |
| VX-NICK-4.02 | EWA Repeat Usage Rate | TBD | HIGH |
| VX-NICK-5.01 | Pawn Transaction Volume | TBD | MEDIUM |
| VX-NICK-5.02 | Title Loan Activity | TBD | HIGH |

**Why It Matters:**
- Rollover/repeat usage indicates desperation cycle
- These are LEADING indicators for default
- High repeat usage = borrowers trapped, not recovering

**Current State:**
We track lender failures (lagging) but NOT borrower desperation patterns (leading).

---

### POP Agent — Owner Stress Indicators MISSING

| Vector | Name | Status | Priority |
|--------|------|--------|----------|
| VX-POP-2.03 | Business Credit Card Utilization | TBD | HIGH |
| VX-POP-2.05 | Cash Reserve Runway | TBD | CRITICAL |
| VX-POP-3.02 | Employment Plans | TBD | HIGH |
| VX-POP-3.03 | Owner Compensation Cuts | TBD | CRITICAL |
| VX-POP-4.02 | Expectations for Conditions | TBD | MEDIUM |
| VX-POP-4.03 | Credit Availability Satisfaction | TBD | MEDIUM |
| VX-POP-5.02 | Business/Personal Blending | TBD | HIGH |
| VX-POP-5.03 | Owner Personal Credit Deterioration | TBD | HIGH |

**Why It Matters:**
- Cash runway = time to failure
- Owner compensation cuts = DIRECT consumer transmission
- Personal/business blending = hidden stress absorption

**Current State:**
We track bankruptcies (lagging) but NOT the runway depletion leading to them.

**Critical Gap:** VX-POP-2.05 (Cash Reserve Runway) is the single most important POP leading indicator. Median small business has ~27 days cash on hand. We should be tracking this.

---

### POLLY Agent — Deductible Burden MISSING

| Vector | Name | Status | Priority |
|--------|------|--------|----------|
| VX-POLLY-1.04 | Homeowners Deductible Burden | TBD | HIGH |
| VX-POLLY-2.02 | Auto Non-Payment Lapse Rate | TBD | CRITICAL |

**Why It Matters:**
- Deductible burden = hidden underinsurance
- Non-payment lapse = direct affordability stress
- These are LEADING indicators for coverage gaps

**Current State:**
We track premium increases (input) and residual market growth (outcome) but NOT the affordability-driven coverage loss in between.

**Critical Gap:** VX-POLLY-2.02 (Auto Non-Payment Lapse) would directly measure how many are losing coverage due to inability to pay.

---

### DOC Agent — Relatively Well-Covered

DOC has fewer TBD gaps. Key vectors are populated:
- VX-DOC-2.02: Deductible burden (populated)
- VX-DOC-4.01: Care deferral rate (populated)

Minor gap:
- VX-DOC-3.03: Average medical debt balance (TBD)

---

## Pattern: Lagging vs. Leading Coverage

| Type | Examples | Coverage |
|------|----------|----------|
| **Lagging** (outcomes) | Delinquencies, bankruptcies, collections, failures | GOOD |
| **Coincident** (current state) | Utilization rates, premium levels, debt levels | GOOD |
| **Leading** (predictive) | Earnings trends, cash runway, rollover rates, behavioral shifts | POOR |

**The structural blind spot:** We're well-equipped to confirm stress AFTER it manifests, but poorly equipped to predict acceleration BEFORE it happens.

---

## Highest Priority Gaps

### Tier 1: CRITICAL (Fill Immediately)

| Vector | Agent | Why Critical |
|--------|-------|--------------|
| VX-POP-2.05 | POP | Cash runway is THE leading indicator for SB failure |
| VX-POP-3.03 | POP | Owner comp cuts = direct consumer transmission |
| VX-POLLY-2.02 | POLLY | Lapse rate = affordability stress manifesting |
| VX-NICK-2.02 | NICK | Rollover rate = trapped borrowers |
| VX-NICK-4.02 | NICK | EWA repeat = desperation pattern |

### Tier 2: HIGH (Fill Within 2-3 Sessions)

| Vector | Agent | Why Important |
|--------|-------|---------------|
| VX-GIG-1.01/1.02 | GIG | Earnings compression drives everything |
| VX-GIG-2.02 | GIG | Multi-apping = stress response |
| VX-GIG-2.03 | GIG | Hours to target = sustainability measure |
| VX-POP-2.03 | POP | CC utilization = liquidity stress |
| VX-POP-5.02 | POP | Blending = hidden absorption |
| VX-NICK-5.02 | NICK | Title loans = severe distress signal |

### Tier 3: MEDIUM (Fill When Capacity)

| Vector | Agent | Notes |
|--------|-------|-------|
| VX-GIG-1.04 | GIG | Incentive spend = platform health |
| VX-GIG-4.01 | GIG | Take rate = pressure on workers |
| VX-NICK-5.01 | NICK | Pawn volume = desperation indicator |
| VX-POLLY-1.04 | POLLY | HO deductible = hidden underinsurance |

---

## Data Source Suggestions

### For GIG Earnings (VX-GIG-1.01, 1.02, 2.03)
- **Gridwise:** Real-time earnings data from driver app
- **Ridester/The Rideshare Guy:** Driver surveys
- **Platform earnings calls:** Disclosed driver/courier economics

### For NICK Behavioral (VX-NICK-2.02, 4.02)
- **CFPB research:** Repeat usage studies
- **Provider earnings:** Some disclose repeat rates
- **Academic studies:** Fintech usage patterns

### For POP Cash Runway (VX-POP-2.05)
- **JPMorgan Chase Institute:** Small business cash buffer research
- **Fed Small Business Credit Survey (SBCS):** Annual data
- **Intuit QuickBooks Capital:** Aggregated data

### For POP Owner Compensation (VX-POP-3.03)
- **NFIB monthly survey:** May include owner compensation questions
- **Gusto:** Payroll data for small businesses
- **Regional Fed surveys:** Sometimes include compensation

### For POLLY Lapse Rate (VX-POLLY-2.02)
- **IRC (Insurance Research Council):** May have lapse data
- **State insurance commissioners:** Some track lapses
- **Carrier earnings calls:** Sometimes disclose retention

---

## Recommended Actions

### Immediate (This Session or Next)
1. **Research data sources** for Tier 1 gaps
2. **Add data sourcing tasks** to next session priorities
3. **Create placeholder alerts** — if we can't fill the vector, define what news/events would signal the condition

### Near-Term (Next 2-3 Sessions)
4. **Populate Tier 1 vectors** with best available data
5. **Establish proxy indicators** where direct data unavailable
6. **Update sub-agent handoffs** to flag gap-filling as priority

### Ongoing
7. **Monitor for new data sources** as fintechs/platforms disclose more
8. **Weight leading indicators higher** in synthesis when available
9. **Track gap-filling progress** in RESEARCH_STATUS.md

---

## Relationship to Research Prompts

Several pending research prompts (LV-03 through LV-08) may provide data to fill gaps:

| Prompt | May Fill |
|--------|----------|
| LV-03 (Conversion Velocity) | Time-to-default data |
| LV-05 (Gig Shadow Credit) | EWA repeat usage, rollover rates |
| LV-06 (Insurance Adequacy) | Deductible burden data |
| LV-07 (Behavioral Trends) | Care deferral trajectory |

---

## Cross-References

- ML-CARL-03 (Pattern Analysis) — Identified leading indicator problem
- Sub-agent VX files — Source of TBD inventory
- LV-03 through LV-08 — Pending research that may fill gaps
- RESEARCH_STATUS.md — Track gap-filling as active research

---

*Created: 2026-01-24 | Session: CARL 009 | Author: CARL*
*Type: Gap Analysis | Diagnostic Value: HIGH*
