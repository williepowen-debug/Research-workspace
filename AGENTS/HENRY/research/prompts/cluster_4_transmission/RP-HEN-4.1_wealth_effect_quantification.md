# RP-HEN-4.1: Wealth Effect Quantification

**Prompt ID:** RP-HEN-4.1
**Cluster:** Transmission Mechanisms
**Priority:** 4
**Created:** 2026-01-26

---

## Context for Research Assistant

HENRY has identified that household equity allocation is at an all-time high of 47.08% of financial assets. This creates unprecedented sensitivity to market declines through the "wealth effect" - the tendency for consumers to spend more when they feel wealthy and less when portfolio values decline. This research quantifies the transmission mechanism from market declines to consumer spending to understand real economy vulnerability.

Current HENRY findings for context:
- Household equity allocation: 47.08% (all-time high, exceeds 2000's 42%)
- Total household equity holdings: ~$66.5 trillion
- Consumer spending: ~70% of US GDP

---

## Research Questions

### 1. MARGINAL PROPENSITY TO CONSUME (MPC) FROM WEALTH

**Academic Estimates:**
- What is the estimated MPC out of equity wealth?
- Range of estimates from academic literature
- Key studies: Case, Quigley, Shiller (2005, 2013), others
- Is MPC different for:
  - Housing wealth vs equity wealth?
  - Different wealth levels (top 10% vs median)?
  - Different age groups?

**Current Best Estimate:**
- What MPC should HENRY use for modeling?
- Confidence interval around estimate

### 2. HISTORICAL EPISODE ANALYSIS

**2000-2002 Dot-Com Bust:**
- Peak-to-trough equity market decline: -49%
- Estimated household equity wealth loss: $X trillion
- Consumer spending change over the period
- Calculated wealth effect (spending change / wealth change)
- Lag structure: How quickly did spending respond?

**2007-2009 Financial Crisis:**
- Peak-to-trough decline: -57%
- Household wealth loss (equity + housing)
- Consumer spending decline
- This episode included housing wealth effect - can we isolate equity?
- Was the wealth effect larger due to housing involvement?

**2020 COVID Crash:**
- Decline: -34% (rapid, then V-recovery)
- Why didn't wealth effect materialize significantly?
- Was it the speed of recovery?
- Fiscal support offsetting?
- Lessons for future episodes

**2022 Decline:**
- Decline: -25%
- Consumer spending behavior
- Was there a measurable wealth effect?
- Why or why not?

### 3. CURRENT SENSITIVITY MODELING

**Baseline Scenario:**
- Current household equity holdings: $66.5 trillion
- Household equity % of financial assets: 47.08%
- If equities decline 20%:
  - Dollar wealth loss: $X trillion
  - Using MPC estimate, consumption impact: $Y
  - As % of GDP: Z%

**Severe Scenario:**
- If equities decline 40% (2000/2008 magnitude):
  - Dollar wealth loss
  - Consumption impact
  - GDP impact
  - Second-order effects (employment, confidence)

**Scenario Matrix:**

| Decline | Wealth Loss | Consumption Impact | GDP Impact |
|---------|-------------|-------------------|------------|
| -10% | | | |
| -20% | | | |
| -30% | | | |
| -40% | | | |

### 4. DISTRIBUTIONAL CONSIDERATIONS

**Who Owns Equities?**
- Equity ownership by wealth percentile
- Top 10% share of equity wealth
- Bottom 50% share
- Median household equity exposure

**Does Distribution Mute or Amplify Wealth Effect?**
- If wealthy own most equities, and wealthy have lower MPC, does this reduce aggregate wealth effect?
- Counter: Wealthy may have higher absolute spending changes
- Counter: "Aspirational" spending by non-wealthy may be influenced by perceived wealth

**Retirement Account Consideration:**
- How much equity is in retirement accounts (less accessible)?
- Does 401(k)/IRA equity have lower MPC than brokerage?

### 5. LAG STRUCTURE

**How Quickly Does Wealth Effect Hit?**
- Immediate (same quarter)?
- Lagged 1-2 quarters?
- Academic evidence on timing
- Does the lag differ by:
  - Magnitude of decline?
  - Speed of decline (crash vs grind)?

### 6. ASYMMETRY

**Is the Wealth Effect Asymmetric?**
- Is MPC larger for wealth losses than gains?
- Do consumers cut spending faster than they increase it?
- Evidence from behavioral economics
- "Loss aversion" in spending decisions

### 7. FEEDBACK LOOPS

**Second-Order Effects:**
- Wealth effect reduces spending
- Reduced spending hits corporate earnings
- Lower earnings hit stock prices
- Further wealth effect
- Can this create a spiral?

**Employment Channel:**
- Consumer spending decline leads to layoffs
- Layoffs reduce spending further
- Interaction between wealth effect and employment

### 8. CURRENT VULNERABILITY ASSESSMENT

**Comparison to Prior Peaks:**
- 2000: Household equity % was ~42%
- 2026: Household equity % is 47%
- Is current economy MORE sensitive to wealth effect than 2000?
- Quantify the difference

**Spending Composition:**
- What categories of spending are most sensitive to wealth effect?
- Durable goods?
- Discretionary services?
- Which sectors would be hit first?

---

## Output Format Requested

```markdown
# Wealth Effect Quantification - Research Output

## Executive Summary
[Key findings on wealth effect transmission]

## 1. MPC Estimates

| Source | Equity Wealth MPC | Housing Wealth MPC | Notes |
|--------|-------------------|--------------------| ------|

**HENRY Should Use:** MPC of X% (range: Y% - Z%)

## 2. Historical Episodes

### 2000-2002
- Equity decline: -49%
- Wealth loss: $X trillion
- Consumption impact: Y%
- Lag: Z quarters

### 2007-2009
[Same structure]

### 2020
[Same structure]

### 2022
[Same structure]

## 3. Current Sensitivity Model

### Scenario Matrix
| Equity Decline | Wealth Loss ($T) | Consumption Impact ($B) | GDP Impact (%) |
|----------------|------------------|------------------------|----------------|
| -10% | | | |
| -20% | | | |
| -30% | | | |
| -40% | | | |

### Key Assumptions
- MPC used: X%
- Current equity holdings: $66.5T
- Baseline consumption: $Y

## 4. Distributional Analysis
[Does concentration in wealthy households mute or amplify?]

## 5. Timing
- Expected lag: X quarters
- Confidence: [Low/Medium/High]

## 6. Asymmetry Assessment
[Evidence on loss vs gain sensitivity]

## 7. Feedback Loop Risk
[Can wealth effect create spiral?]

## 8. Vulnerability Comparison

| Factor | 2000 | 2026 | Implication |
|--------|------|------|-------------|
| HH Equity % | 42% | 47% | |
| Total Equity $ | | $66.5T | |
| Consumption/GDP | | ~70% | |

**Assessment:** Current economy is [More/Less/Equally] vulnerable to wealth effect vs 2000

## Implications for HENRY
[What threshold should trigger concern?]

## Cross-Agent Signal Guidance
[When should HENRY alert CARL?]

## Sources
[Citations]
```

---

## Integration Notes for HENRY

After receiving this research:
- Update transmission path in FLOW.tsv with quantified estimates
- Refine signal thresholds for CARL communication
- Add wealth effect sensitivity to HENRY assessment framework
- Consider vector tracking consumer spending leading indicators

---

*Prompt ready for external LLM research*
