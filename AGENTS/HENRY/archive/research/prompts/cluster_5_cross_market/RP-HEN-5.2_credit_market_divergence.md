# RP-HEN-5.2: Credit Market Divergence

**Prompt ID:** RP-HEN-5.2
**Cluster:** Cross-Market Context
**Priority:** 11
**Created:** 2026-01-26

---

## Context for Research Assistant

HENRY has identified extreme equity valuations, but credit spreads remain tight. This creates a potential divergence: equities are priced for perfection while credit markets also price low default risk. Historically, credit and equity markets don't always agree on risk levels. This research investigates the current divergence and what it signals.

---

## Research Questions

### 1. CURRENT CREDIT SPREAD STATE

**Investment Grade:**
- Current IG OAS (Option-Adjusted Spread)
- Historical average IG OAS
- Current percentile vs history
- Tightest historical spread and when

**High Yield:**
- Current HY OAS
- Historical average HY OAS
- Current percentile
- Tightest historical spread and when

**By Rating:**
- BBB spreads
- BB spreads
- CCC spreads
- Is compression uniform across quality?

### 2. EQUITY VS CREDIT DIVERGENCE

**Historical Relationship:**
- Do credit spreads and equity valuations typically agree?
- Correlation between CAPE and IG/HY spreads
- When have they diverged historically?

**Current State:**
- CAPE: 40.65 (97th percentile - high valuation)
- IG Spreads: Xbps (Yth percentile - tight)
- HY Spreads: Xbps (Yth percentile - tight)
- Are both pricing "no risk" simultaneously?

**Divergence Measure:**
- Create a metric: Equity valuation percentile vs Credit spread percentile
- Current divergence magnitude
- Historical comparison

### 3. WHAT DOES TIGHT CREDIT MEAN?

**Bullish Interpretation:**
- Credit markets are "smart money"
- Tight spreads = low default expectations = economic strength
- If credit is right, maybe equity valuations are justified

**Bearish Interpretation:**
- Both markets are complacent
- Reach for yield compressing spreads artificially
- Fed support expectations in both markets
- Could both be wrong together?

**Structural Explanations:**
- Private credit competition suppressing public spreads
- Insurance company demand for yield
- CLO demand for loans
- Are tight spreads "real" or technical?

### 4. HISTORICAL PRECEDENTS

**2007 (Pre-Crisis):**
- Credit spreads were extremely tight (IG below 100bps)
- Equity valuations elevated but not extreme
- Which was right? (Equities somewhat, credit very wrong)
- Timeline: When did credit start to widen?

**1999-2000:**
- Credit spreads during dot-com peak
- Did credit give warning before equity market topped?
- Telecom credit deterioration as leading indicator

**2021-2022:**
- Credit spreads in late 2021
- Did they lead or lag equity decline in 2022?
- What was the sequence?

### 5. CREDIT AS LEADING INDICATOR

**Does Credit Lead Equity?**
- Academic research on credit leading/lagging equities
- In which episodes did credit provide warning?
- In which did it fail to warn?

**Current Signal:**
- If credit starts widening, does that predict equity correction?
- What spread widening threshold matters?
- How much lead time historically?

### 6. WHEN CREDIT AND EQUITY DISAGREE

**Which is Right?**
- Historical resolution of divergences
- Did equity come to credit, or credit come to equity?
- Base rates for each outcome

**Resolution Scenarios for Current Divergence:**
1. Equity falls, credit widens (both were wrong)
2. Equity stays high, credit stays tight (both right - new paradigm)
3. Equity falls, credit stays tight (credit right, equity wrong)
4. Equity rises, credit widens (equity right, credit wrong)

**Most likely resolution based on history?**

### 7. DEFAULT CYCLE ANALYSIS

**Current Default Rates:**
- HY default rate (trailing 12 months)
- Expected default rate (forward)
- Historical default rates at similar spread levels

**Default Rate and Spreads:**
- Do current spreads adequately compensate for default risk?
- Spread per unit of default risk: historical comparison
- Is the current spread "enough"?

### 8. TECHNICAL FACTORS

**Supply/Demand:**
- IG/HY new issuance trends
- Demand from insurers, pensions, overseas
- Is tight spread technical (demand > supply)?

**Refinancing Wall:**
- When do major maturities hit?
- 2025, 2026, 2027 maturity profiles
- Could refinancing needs widen spreads?

**Private Credit Impact:**
- Has private credit taken risky borrowers out of public market?
- Does this make public HY "safer" and justify tighter spreads?
- Or just move the risk somewhere less visible?

---

## Output Format Requested

```markdown
# Credit Market Divergence - Research Output

## Executive Summary
[Key findings on credit/equity divergence]

## 1. Current Credit Dashboard

| Metric | Current | Hist Avg | Percentile | Tightest Ever |
|--------|---------|----------|------------|---------------|
| IG OAS | | | | |
| HY OAS | | | | |
| BBB Spread | | | | |
| CCC Spread | | | | |

## 2. Equity/Credit Divergence Analysis

### Current State
- Equity valuation percentile: 97th (CAPE)
- Credit spread percentile: Xth
- Divergence: [Quantified]

### Historical Comparison
| Period | Equity Percentile | Credit Percentile | Resolution |
|--------|-------------------|-------------------|------------|
| 2007 | | | |
| 2000 | | | |
| Current | 97th | | ? |

## 3. Interpretation

### If Credit is Right
[Bullish implications]

### If Credit is Wrong
[Bearish implications]

### Structural Explanations
[Why spreads might be artificially tight]

## 4. Historical Precedent Analysis

### 2007
[Detailed sequence]

### 2000
[Detailed sequence]

### 2022
[Detailed sequence]

## 5. Credit as Leading Indicator

| Episode | Credit Lead Time | Useful Warning? |
|---------|------------------|-----------------|

**Track Record:** Credit led equity X% of the time

## 6. Resolution Scenarios

| Scenario | Probability | Trigger |
|----------|-------------|---------|
| Both correct | | |
| Both wrong | | |
| Credit right | | |
| Equity right | | |

## 7. Default Analysis
[Are spreads compensating for default risk?]

## 8. Technical Factors
[Supply/demand dynamics]

## Monitoring Recommendations for HENRY

| Indicator | Threshold | Signal |
|-----------|-----------|--------|
| IG OAS widening | +Xbps | Watch |
| HY OAS widening | +Xbps | Concern |
| BBB-BB compression | | Risk appetite |

## Implications for HENRY
[Should credit inform equity view?]

## Sources
[Citations]
```

---

## Integration Notes for HENRY

After receiving this research:
- Consider adding credit spread vector(s)
- Coordinate with LIQUID on credit/Treasury interactions
- Coordinate with REGINALD on corporate credit
- Add spread widening to FL.tsv watch list

---

*Prompt ready for external LLM research*
