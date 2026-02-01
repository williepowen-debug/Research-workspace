# RP-HEN-2.2: Sentiment Extreme Indicators

**Prompt ID:** RP-HEN-2.2
**Cluster:** Timing & Catalysts
**Priority:** 4 (after breadth)
**Created:** 2026-01-26

---

## Context for Research Assistant

HENRY currently tracks VIX (16.07) and equity put/call ratio (0.58) as sentiment indicators. However, sentiment is multi-dimensional and VIX alone may miss important signals. This research compiles a comprehensive sentiment dashboard with indicators that have historically provided warning before market tops.

Current HENRY findings for context:
- VIX: 16.07 (35th percentile - complacent)
- Put/Call: 0.58 (bullish positioning)
- Fundamental vectors: 5 at RED status
- Divergence: Market pricing calm while structural metrics at extremes

---

## Research Questions

### 1. AAII SENTIMENT SURVEY
- Current bull/bear spread (most recent reading)
- Historical average bull/bear spread
- What readings preceded major tops?
  - March 2000
  - October 2007
  - January 2022
- Contrarian reliability: When AAII is extremely bullish, what are forward returns?
- Data source URL for ongoing monitoring

### 2. INVESTORS INTELLIGENCE (ADVISOR SENTIMENT)
- Current bull/bear ratio
- Historical context and extremes
- Comparison to AAII (do they diverge?)
- Track record as contrarian indicator
- Data source URL

### 3. CNN FEAR & GREED INDEX
- Current reading and components
- What are the 7 components?
- Historical readings at market tops/bottoms
- How is it calculated?
- Real-time tracking URL

### 4. NAAIM EXPOSURE INDEX
- Current reading (National Association of Active Investment Managers)
- What does it measure?
- Historical extremes
- Reliability as indicator
- Data source URL

### 5. MARGIN DEBT ANALYSIS (BEYOND LEVEL)
- Current margin debt level ($1.226T as of Dec 2025)
- More important: Rate of change in margin debt
- Does margin debt GROWTH peak before or after market tops?
- Historical pattern:
  - 2000: When did margin debt growth peak relative to market?
  - 2007: Same question
- Free credit balances (cash in brokerage accounts) - bullish or bearish signal?

### 6. EQUITY FUND FLOWS
- Current monthly/weekly equity fund flows (ICI data)
- Are retail investors buying or selling?
- Historical patterns: Do flows peak before market tops?
- ETF flows vs mutual fund flows
- Data source URL

### 7. IPO & SPAC ACTIVITY
- Current IPO issuance rate vs 2021 peak
- SPAC activity current vs peak
- IPO first-day pops (speculative appetite measure)
- Historical: IPO activity at 2000 top, 2007 top
- Is speculative appetite elevated or cooling?

### 8. RETAIL OPTIONS ACTIVITY
- Retail options volume as % of total
- Call buying by small traders (OCC data)
- "YOLO" indicators - far OTM call buying
- Comparison to 2021 meme stock mania
- Current readings vs historical

### 9. MEME STOCK / SPECULATIVE INDICATORS
- GME, AMC current activity vs 2021
- Crypto correlation with equity risk appetite
- Is crypto leading or lagging equity sentiment?
- "Speculative fervor" composite - does one exist?

### 10. INSIDER ACTIVITY
- Current insider buy/sell ratio
- Historical patterns before tops
- Are executives selling?
- Data source (Form 4 aggregators)

### 11. SHORT INTEREST
- Current S&P 500 short interest as % of float
- Is short interest historically low (crowded long)?
- Short interest trends
- Data source URL

---

## Output Format Requested

```markdown
# Sentiment Indicator Dashboard - Research Output

## Executive Summary
[Overall sentiment assessment]

## Sentiment Dashboard

| Indicator | Current | Historical Avg | 2000 Top | 2007 Top | Signal |
|-----------|---------|----------------|----------|----------|--------|
| AAII Bull-Bear | | | | | |
| Investors Intelligence | | | | | |
| CNN Fear/Greed | | | | | |
| NAAIM Exposure | | | | | |
| Margin Debt YoY% | | | | | |
| Fund Flows | | | | | |
| IPO Activity | | | | | |
| Retail Options | | | | | |
| Insider Sell/Buy | | | | | |
| Short Interest | | | | | |

## Indicator Deep Dives

### 1. AAII Sentiment
[Full analysis]

### 2. Advisor Sentiment
[Full analysis]

[Continue for each indicator...]

## Composite Assessment
[Weighted sentiment reading]

## Contrarian Signals
[Which indicators are at contrarian extremes?]

## Data Sources for HENRY Monitoring
| Indicator | URL | Update Frequency |
|-----------|-----|------------------|

## Sources
[Citations]
```

---

## Integration Notes for HENRY

After receiving this research:
- Expand sentiment vectors beyond VIX/Put-Call
- Create composite sentiment indicator
- Add data sources to monitoring routine
- Update VX.tsv with new sentiment vectors

---

*Prompt ready for external LLM research*
