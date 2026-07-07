# Extraction Patterns by Source Type

## Images/Screenshots

**What to extract:**
- Headline (largest text)
- Source/publication (logo or byline)
- Date (if visible)
- Key numbers (prices, percentages, dollar amounts)
- Ticker symbols
- Quotes (in quotation marks)

**Process:**
1. Ask user to describe content if OCR unavailable
2. Focus on numerical data — most actionable
3. Note: screenshot date vs article date

## News Articles

**Structure:**
```markdown
**Source:** [Publication]
**Date:** [Date]
**Headline:** [Title]

**Core Claim:** [1-2 sentence summary]

**Key Data:**
- [Metric]: [Value]
- [Metric]: [Value]

**Quotes:**
> "[Relevant quote]" — [Speaker]

**Thesis Relevance:** [Why this matters to the thesis]
```

## YouTube Transcripts

**Structure:**
```markdown
**Source:** [Channel/Video Title]
**Date:** [Upload Date]
**Speaker:** [Name, if known]

**Core Claims:**
1. [Claim 1]
2. [Claim 2]

**Key Data:**
- [Data point with timestamp if relevant]

**Thesis Relevance:** [Analysis vs opinion]
```

## PDF Documents

**Process:**
1. Use `pdfminer.six` or similar for text extraction
2. Look for: executive summary, key findings, tables
3. Extract: title, author, date, key metrics
4. Note: page numbers for citations

## Market Data/Charts

**Always extract:**
- Ticker/symbol
- Price/value
- Change (absolute and %)
- Time/date of data
- Source (Bloomberg, Refinitiv, etc.)

**Context to note:**
- Real-time vs delayed
- Pre-market/after-hours
- Historical comparison (52-week high/low)

## Earnings Reports

**Key fields:**
- Company/ticker
- Quarter/year
- Revenue (actual vs consensus)
- EPS (actual vs consensus)
- Guidance (raised/lowered/maintained)
- Key management quotes
- Segment performance

## Macroeconomic Data

**Key fields:**
- Indicator name (NFP, CPI, Claims, etc.)
- Print value
- Consensus expectation
- Prior period (revised?)
- Change from prior
- Components (what drove the number)

## Headlines (Batch Processing)

**Triage rules:**
- 🔴 Threshold breaches
- 🟡 Thesis-relevant keywords
- 🟢 Market noise (ignore)

**Keywords by agent:**
- **BROCK:** gate, redemption, BDC, CLO, private credit
- **REGINALD:** regional bank, CRE, OZK, WAL, allowance
- **CARL:** mortgage, housing, home price, affordability
- **BRENT:** Brent, WTI, oil, Hormuz, OPEC
- **HAWK:** Iran, war, escalation, ceasefire, strike
- **SAM:** JPY, BOJ, Ueda, carry trade
- **ZHAO:** China, TIC, UST, outflow, Gulf
- **LABOR:** claims, NFP, unemployment, jobs
- **HENRY:** HY OAS, CCC, VIX, spread
- **LIQUID:** repo, SOFR, liquidity, systemic
- **SHADE:** reinsurance, captive, annuity, Athene

## Priority Classification

**🔴 Critical:**
- HY OAS >320
- CCC OAS >1000
- Brent >$100
- Gas >$4.00
- USD/JPY >158
- VIX >30
- Gating events (>5% redemption requests)
- War escalation
- Bank failure/regulatory action

**🟡 Important:**
- Earnings from thesis-relevant companies
- Economic data prints
- Sector stress signals
- Reserve/allowance changes

**🟢 Context:**
- Analyst upgrades/downgrades
- General market commentary
- Non-thesis sector news
