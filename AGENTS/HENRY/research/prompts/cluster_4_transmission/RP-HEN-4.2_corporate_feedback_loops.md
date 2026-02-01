# RP-HEN-4.2: Corporate Sector Feedback Loops

**Prompt ID:** RP-HEN-4.2
**Cluster:** Transmission Mechanisms
**Priority:** 9
**Created:** 2026-01-26

---

## Context for Research Assistant

HENRY focuses primarily on how market conditions affect households, but corporations also depend on elevated stock prices in ways that could create feedback loops during a decline. Stock-based compensation, M&A currency, collateral values, and executive incentives all rely on high equity prices. This research maps the corporate feedback mechanisms that could amplify a market correction.

---

## Research Questions

### 1. STOCK-BASED COMPENSATION

**Current Scale:**
- What percentage of S&P 500 total compensation is equity-based?
- Dollar value of annual stock compensation across S&P 500
- Growth trend in equity compensation over past 10 years

**By Company Type:**
- Tech sector equity compensation % vs other sectors
- Mag 7 equity compensation as % of total comp

**Decline Impact:**
- If stock falls 30%, what happens to:
  - Employee retention (unvested options/RSUs lose value)
  - Employee morale and productivity
  - Employee personal spending (they feel poorer)
- Historical examples: 2000 tech bust impact on retention

**Repricing Pressure:**
- Do companies reprice options after declines?
- Does this create additional dilution?
- 2000-2002 repricing history

### 2. M&A CURRENCY

**Stock-Based M&A:**
- What percentage of M&A uses stock as currency?
- Recent large all-stock or mostly-stock deals
- Dollar value of stock-financed M&A annually

**Decline Impact:**
- If acquirer stock falls 30%, does M&A freeze?
- Historical: Did M&A activity collapse in 2000-2002? 2008?
- How long does M&A take to recover after market decline?

**Strategic Implications:**
- Companies use acquisitions for growth
- Frozen M&A market slows growth strategies
- Feedback to earnings expectations

### 3. CORPORATE CREDIT & COLLATERAL

**Equity-Linked Credit Facilities:**
- Do corporate credit facilities include stock price covenants?
- Market cap minimums in credit agreements
- Ratings agency sensitivity to stock price

**Cross-Default Risk:**
- Stock price decline triggers covenant breach
- Covenant breach triggers credit default
- Credit default triggers further stock decline
- Is this loop material?

**Secured Lending:**
- Margin loans secured by executive stock holdings
- Corporate loans secured by subsidiary stock
- NAV lending against portfolio values

### 4. EXECUTIVE INCENTIVE STRUCTURES

**Option/RSU Values:**
- At what stock price levels do executive options go underwater?
- How much executive net worth is tied to company stock?
- "Skin in the game" becomes "anchors" in decline

**Behavioral Impact:**
- Do executives take more risk when underwater (gambling for resurrection)?
- Or become more conservative (protect remaining value)?
- Research on executive behavior during stock declines

**Retention Risk:**
- Executives with underwater options - flight risk?
- Talent war dynamics in declining market
- 2000 example: Tech executive turnover

### 5. SHARE REPURCHASE DYNAMICS

**Procyclical vs Countercyclical:**
- Do buybacks accelerate when stocks fall (value buying)?
- Or pause (cash conservation)?
- Empirical evidence from past declines

**2020 Example:**
- What happened to buybacks during COVID crash?
- Speed of resumption?

**2022 Example:**
- Buyback behavior during 2022 decline?

**Modeling:**
- If stocks fall 30%, what is likely buyback response?
- Does this support price or does conservation dominate?

### 6. PENSION & INSURANCE COMPANY LOOPS

**Corporate Pension Funding:**
- Many companies still have defined benefit pensions
- Pension funding status depends on stock returns
- If stocks fall, pension becomes underfunded
- Underfunding requires cash contributions
- Cash contributions reduce earnings
- Lower earnings hit stock price

**Insurance Company Dynamics:**
- Insurance portfolios include equities
- Mark-to-market losses affect capital ratios
- Capital concerns force selling
- Forced selling depresses prices further

### 7. EARNINGS ESTIMATE REVISIONS

**Stock Price and Estimates:**
- Do analysts revise estimates after stock declines?
- Is there reflexivity (lower price -> lower estimates -> lower price)?
- Historical pattern during bear markets

**Guidance Behavior:**
- Do companies lower guidance after stock falls?
- Does this become self-fulfilling?

### 8. VENTURE & PRIVATE EQUITY FEEDBACK

**Startup Ecosystem:**
- Venture valuations marked to public comparables
- If public tech falls 50%, private marks follow
- Down rounds reduce employee equity value
- Startup hiring/spending slows
- Feedback to tech employment and spending

**PE Portfolio Companies:**
- Leveraged companies in PE portfolios
- If public markets fall, exit valuations drop
- PE extends holding periods
- Impact on PE fund returns and investor allocations

---

## Output Format Requested

```markdown
# Corporate Feedback Loops - Research Output

## Executive Summary
[Key amplification mechanisms identified]

## 1. Stock Compensation Channel

### Scale
- S&P 500 equity comp: $X billion annually
- As % of total comp: Y%

### Decline Impact
| Scenario | Employee Wealth Loss | Retention Risk | Spending Impact |
|----------|---------------------|----------------|-----------------|
| -20% decline | | | |
| -40% decline | | | |

## 2. M&A Currency Channel
[Quantified impact of frozen M&A]

## 3. Credit & Collateral Channel
[Covenant breach risks]

## 4. Executive Incentive Channel
[Behavioral impacts]

## 5. Buyback Response
| Decline | Historical Buyback Response | Expected Response |
|---------|----------------------------|-------------------|
| -20% | | |
| -30% | | |
| -40% | | |

## 6. Pension & Insurance Channel
[Forced selling dynamics]

## 7. Earnings Estimate Reflexivity
[Evidence of self-fulfilling dynamics]

## 8. Private Market Feedback
[VC/PE transmission]

## Feedback Loop Map

```
Stock Decline
    ↓
├── Employee wealth effect
├── M&A freezes
├── Covenant stress
├── Executive behavior change
├── Buyback pause?
├── Pension contributions rise
├── Insurance forced selling
├── Estimate revisions
└── Private market marks down
    ↓
Further Stock Decline?
```

## Amplification Assessment
- Which channels are most material?
- Estimated amplification factor: X%
- Confidence: [Low/Medium/High]

## Historical Evidence
[Did these loops operate in 2000, 2008?]

## Implications for HENRY
[How does this affect drawdown estimates?]

## Sources
[Citations]
```

---

## Integration Notes for HENRY

After receiving this research:
- Add corporate feedback paths to FLOW.tsv
- Consider tracking stock compensation trends
- Factor amplification into scenario analysis
- Coordinate with REGINALD on bank/pension channels

---

*Prompt ready for external LLM research*
