# RP-HEN-5.1: Global Valuation Comparison

**Prompt ID:** RP-HEN-5.1
**Cluster:** Cross-Market Context
**Priority:** 10
**Created:** 2026-01-26

---

## Context for Research Assistant

HENRY has established that US equity valuations are at or near all-time extremes (CAPE 40.65, Buffett Indicator 230%). However, valuation analysis requires global context. If the entire world is expensive, that's different than if the US is uniquely overvalued. This research compares US valuations to other major markets and assesses whether the US premium is justified.

---

## Research Questions

### 1. CURRENT GLOBAL CAPE COMPARISON

**Get CAPE ratios for:**
- US (S&P 500): 40.65 (confirmed by HENRY)
- Europe (STOXX 600 or Euro STOXX 50)
- UK (FTSE 100)
- Japan (Nikkei 225 or TOPIX)
- Emerging Markets (MSCI EM)
- China (Shanghai Composite or MSCI China)
- India (Nifty 50)
- Canada (TSX)
- Australia (ASX 200)

**For Each:**
- Current CAPE
- Historical average CAPE
- Current percentile vs own history

### 2. US PREMIUM ANALYSIS

**Current US Premium:**
- US CAPE vs Developed Markets CAPE (ex-US)
- US CAPE vs World CAPE
- Quantify the premium: US is X% more expensive

**Historical Premium:**
- What has been the average US premium historically?
- 10-year average
- 20-year average
- Is current premium above or below historical?

**Premium Chart:**
- How has US vs EAFE CAPE spread evolved over time?
- When was US premium largest? Smallest?
- What happened after periods of extreme premium?

### 3. JUSTIFICATION FOR US PREMIUM

**Earnings Growth Differential:**
- US earnings growth vs Europe, Japan, EM (10-year)
- Does higher growth justify higher multiple?
- Quantify: What premium is "fair" given growth differential?

**Sector Composition:**
- US has more tech (higher growth/multiple)
- Adjust for sector mix: Is US still expensive on sector-adjusted basis?
- What would US CAPE be with European sector weights?

**Quality Factors:**
- ROE comparison (US vs other regions)
- Profit margins
- Balance sheet strength
- Do these justify premium?

**Governance/Rule of Law:**
- Argument for US premium due to property rights, legal system
- Is this quantifiable?
- Has this premium always existed?

**Currency Considerations:**
- Dollar strength impact on relative valuations
- For foreign investor: US returns in local currency vs USD

### 4. FLOW IMPLICATIONS

**Historical Pattern:**
- When US was extremely expensive vs world, what happened to flows?
- Did money rotate to cheaper markets?
- Timeline for rotation if it occurred

**Current Flows:**
- Net flows to US vs other regions
- Are foreign investors still buying US?
- Any signs of rotation beginning?

### 5. RELATIVE VALUE OPPORTUNITIES

**Cheapest Markets:**
- Which markets have lowest CAPE currently?
- Historical context for those markets
- Quality-adjusted cheapness (cheap for good reason?)

**Historical Examples:**
- After 2000, US underperformed international for years
- After 2008, same pattern initially
- Is rotation due?

### 6. GLOBAL MARKET CAP WEIGHTS

**US Share of Global Market:**
- What % of global equity market cap is US?
- Historical trend
- Is US share at extreme?

**Concentration Comparison:**
- US Top 10 concentration: 38.22%
- Other markets' concentration
- Is US uniquely concentrated?

### 7. SYNCHRONIZED RISK

**Global Valuation Correlation:**
- If all markets are elevated (not just US), what does that mean?
- Global CAPE percentile vs history
- Is there a global overvaluation?

**Synchronized Correction Risk:**
- If correction occurs, do all markets fall together?
- Correlation in down markets
- Diversification benefit (or lack thereof)

---

## Output Format Requested

```markdown
# Global Valuation Comparison - Research Output

## Executive Summary
[Key findings on US relative valuation]

## 1. Global CAPE Dashboard

| Region/Index | Current CAPE | Historical Avg | Percentile | vs US |
|--------------|--------------|----------------|------------|-------|
| US (S&P 500) | 40.65 | 17.33 | 97th | - |
| Europe | | | | |
| Japan | | | | |
| EM | | | | |
| UK | | | | |
| China | | | | |

## 2. US Premium Analysis

### Current Premium
- US vs Developed ex-US: +X%
- US vs World: +Y%

### Historical Premium
| Period | Avg US Premium |
|--------|---------------|
| 10-year avg | |
| 20-year avg | |
| Current | |
| Percentile | |

### Premium Chart Description
[When were premiums similar? What happened?]

## 3. Premium Justification Analysis

| Factor | Justifies Premium? | Quantified Impact |
|--------|-------------------|-------------------|
| Earnings growth | | |
| Sector mix | | |
| ROE/Quality | | |
| Governance | | |

**Adjusted View:** After adjustments, US is still X% expensive

## 4. Flow Analysis
[Current flows and rotation potential]

## 5. Relative Value Map

| Market | CAPE | Percentile | Quality-Adjusted | Verdict |
|--------|------|------------|------------------|---------|
| [Cheapest markets] | | | | |

## 6. Global Market Structure
- US share of global: X%
- Historical: This is [high/normal/low]

## 7. Synchronized Risk Assessment
[Is this a US problem or global problem?]

## Implications for HENRY
[How should global context affect US assessment?]

## Sources
[Citations with URLs for ongoing data]
```

---

## Integration Notes for HENRY

After receiving this research:
- Add global context to HENRY framework
- Consider international CAPE comparison as context vector
- Note rotation potential in FL.tsv
- Coordinate with SAM on Japan specifically

---

*Prompt ready for external LLM research*
