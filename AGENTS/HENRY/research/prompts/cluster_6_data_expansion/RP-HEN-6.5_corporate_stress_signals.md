# RP-HEN-6.5: Corporate Stress & Earnings Signals

**Prompt ID:** RP-HEN-6.5
**Cluster:** Data Expansion
**Priority:** 5
**Created:** 2026-02-03

---

## Context for Research Assistant

HENRY tracks market-level valuations (CAPE 40.65) and sentiment, but needs CORPORATE-LEVEL stress signals. Earnings revisions, guidance trends, and corporate behavior (issuance, M&A, buybacks) provide early warning of fundamental deterioration before it shows in prices. These signals connect HENRY to the real economy transmission tracked by CARL and LABOR.

Current HENRY corporate vectors:
- VX-HEN-8.01: Net Equity Issuance: -$800B (buybacks >> IPOs)
- VX-HEN-8.02: Corporate Buyback Rate: $1.02T/yr
- VX-HEN-7.01: Insider Sell/Buy Ratio: 13.56 (RED, extreme selling)

Cross-agent context:
- LABOR: ~580K layoffs announced in WARN data
- CARL: PIK income 12.8%, shadow defaults rising
- REGINALD: Bank exposure to corporate credit

---

## Research Questions

### 1. EARNINGS REVISION RATIOS
- What is the earnings revision ratio (upgrades / downgrades)?
- How to calculate for S&P 500 aggregate?
- Historical patterns:
  - What ratio indicates healthy earnings momentum?
  - What ratio preceded recessions/corrections?
- Current reading and trend?
- Sector-level revision ratios?
- Data sources: FactSet, Bloomberg, Refinitiv, Yardeni?

### 2. GUIDANCE SENTIMENT
- How to track forward guidance tone?
- Metrics:
  - % of companies guiding above/below consensus
  - % of companies withdrawing guidance (uncertainty signal)
  - Language analysis of earnings calls
- Historical patterns: When does guidance deteriorate before earnings?
- Tools for guidance tracking (FactSet, AlphaSense)?

### 3. EARNINGS QUALITY INDICATORS
- Revenue vs earnings growth (earnings without revenue = low quality)
- Operating earnings vs reported earnings gap
- Buyback-adjusted EPS growth (are buybacks masking weakness?)
- Accruals ratio (accounting vs cash earnings)
- How to detect "earnings management" at aggregate level?

### 4. IPO & SPAC ACTIVITY
- Current IPO pipeline and pricing
- IPO first-day pops vs historical (sentiment indicator)
- SPAC activity levels (dead or reviving?)
- Secondary offerings pace
- What does weak IPO market signal for broader sentiment?
- What does HOT IPO market signal (late cycle froth)?
- Data: Renaissance Capital, SPACInsider, SEC filings?

### 5. CORPORATE DEBT ISSUANCE
- Investment grade issuance pace
- High yield issuance pace  
- Loan vs bond mix
- Average maturity of new issuance (shorter = refinancing stress)
- Spread on new issuance vs secondary
- When does "issuer exhaustion" occur?
- Data: SIFMA, LCD, Bloomberg?

### 6. M&A ACTIVITY
- Deal volume and value trends
- Cash vs stock deals (stock = executives think overvalued)
- Strategic vs financial buyer mix
- Premium paid trends
- Broken deals (financing failures)
- What M&A patterns indicate cycle peak?

### 7. LAYOFF & RESTRUCTURING ANNOUNCEMENTS
- Challenger, Gray & Christmas layoff data
- WARN Act filings (cross-reference with LABOR)
- Restructuring charges in earnings
- "Cost optimization" language in calls
- How do layoff announcements correlate with stock performance?

### 8. PROFIT MARGIN TRENDS
- S&P 500 net profit margin (current vs historical)
- Margin compression signals
- Labor cost pressure (unit labor costs)
- Input cost pressure (PPI vs CPI)
- Sector margin divergences
- Margin sustainability analysis (mean reversion risk)

---

## Output Format Requested

```markdown
# Corporate Stress & Earnings Signals - Research Output

## Executive Summary
[Key corporate health indicators]

## 1. Earnings Revision Analysis
| Metric | Current | Healthy | Concern | Recession |
|--------|---------|---------|---------|-----------|
| Revision Ratio | ... | >1.5 | 0.8-1.0 | <0.7 |
[By sector]

## 2. Guidance Sentiment
[Current trends and interpretation]

## 3. Earnings Quality
| Indicator | Current | Interpretation |
|-----------|---------|----------------|
| Revenue/Earnings Growth Gap | ... | ... |
[Continue]

## 4. IPO/SPAC Activity
[Current status and historical context]

## 5. Corporate Debt Issuance
| Category | 2025 Pace | vs Historical | Signal |
|----------|-----------|---------------|--------|
| IG Bonds | ... | ... | ... |
| HY Bonds | ... | ... | ... |
[Continue]

## 6. M&A Indicators
[Deal activity and cycle positioning]

## 7. Layoff Signals
[Challenger data, WARN cross-reference]

## 8. Margin Analysis
[S&P 500 margins, sustainability]

## Corporate Stress Composite
[Framework for combining signals]

## Proposed HENRY Vectors
| ID | Name | Current | Thresholds | Source |
|----|------|---------|------------|--------|
| VX-HEN-13.01 | Earnings Revision Ratio | ... | ... | ... |
[Continue]

## Cross-Agent Integration
- LABOR: Layoff correlation
- CARL: Consumer demand impact
- REGINALD: Credit exposure implications

## Data Sources
| Metric | Source | Cost | Frequency |
|--------|--------|------|-----------|
[All metrics]

## Sources
[References]
```

---

## Integration Notes for HENRY

After receiving this research:
- Create VX-HEN-13.xx series for Corporate Stress domain
- Build "Corporate Health Composite" indicator
- Link earnings revisions to LABOR layoff data
- Add to FLOW.tsv: Corporate stress → Credit stress → Bank exposure
- Coordinate with CARL on consumer demand signals

---

*Prompt ready for external LLM research*
