# RP-HEN-6.3: Fund Flow Data & Positioning

**Prompt ID:** RP-HEN-6.3
**Cluster:** Data Expansion
**Priority:** 3
**Created:** 2026-02-03

---

## Context for Research Assistant

HENRY tracks the "Structural Bid" thesis — passive flows, buybacks, 401(k) automatic investment, and foreign demand create persistent buying pressure that keeps valuations elevated. But current data is AGGREGATE. We need GRANULAR flow data to detect when flows shift — because when the structural bid breaks, the repricing will be violent.

Current HENRY structural bid vectors:
- Net Equity Issuance: -$800B (buybacks > issuance)
- Corporate Buyback Rate: $1.02T/yr (ATH)
- Passive Flow Momentum: +$380B/yr
- 401(k) Flow Stability: STABLE
- Foreign Equity Demand: +$150B/yr
- Inelastic Market Multiplier: 5-17x

Key insight from HENRY research: The market has become "inelastic" — $1 of flow creates $5-17 of market cap change. This works both directions.

---

## Research Questions

### 1. CFTC COMMITMENTS OF TRADERS (COT)
- What futures contracts are most relevant for equity positioning?
  - E-mini S&P 500 (ES)
  - E-mini Nasdaq (NQ)
  - E-mini Russell (RTY)
  - VIX futures
- How to interpret COT data:
  - Commercial vs Non-Commercial vs Non-Reportable
  - Net long/short positioning
  - Changes week-over-week
- What extreme readings have historically preceded reversals?
- Where to access: CFTC website, Barchart, TradingView?
- Update schedule and lag time?

### 2. EPFR FUND FLOW DATA
- What does EPFR Global track?
- Coverage: Mutual funds, ETFs, by geography, by sector?
- How to access (cost, data format)?
- Key metrics:
  - Weekly equity fund flows (US, Global, EM)
  - Sector rotation flows
  - Bond vs equity allocation shifts
- Historical patterns: What flow patterns preceded corrections?
- Alternatives to EPFR (ICI, Lipper, Morningstar)?

### 3. ETF CREATION/REDEMPTION
- How does ETF creation/redemption work mechanically?
- What does large creation (inflow) vs redemption (outflow) signal?
- Key ETFs to monitor:
  - SPY, IVV, VOO (S&P 500)
  - QQQ (Nasdaq)
  - IWM (Russell)
  - HYG, LQD (credit)
  - TLT (long bonds)
- Where to find creation/redemption data?
- How to detect "smart money" vs retail flows?

### 4. SECTOR ROTATION TRACKING
- How to measure capital rotating between sectors?
- Key rotation pairs:
  - Growth vs Value (QQQ/VTV ratio)
  - Large vs Small (SPY/IWM ratio)
  - Cyclicals vs Defensives
  - US vs International (SPY/EFA ratio)
- What rotation patterns are predictive?
- Tools/data sources for rotation analysis?

### 5. RETAIL VS INSTITUTIONAL FLOW
- How to distinguish retail from institutional flows?
- Retail indicators:
  - Robinhood data (if available)
  - Small lot options trades
  - Odd lot transactions
  - Retail sentiment surveys
- Institutional indicators:
  - 13F filings (quarterly, lagged)
  - Block trades
  - Dark pool activity
- Is there a "retail capitulation" indicator?

### 6. MONEY MARKET & CASH POSITIONING
- Total money market fund assets (current level?)
- Historical relationship: MM assets vs equity returns
- "Cash on sidelines" — is this actually a bullish indicator?
- When does cash move INTO vs OUT OF equities?
- Track: Money market yields vs equity earnings yield differential

### 7. FOREIGN FLOW TRACKING
- TIC data (Treasury International Capital) — what does it show?
- Which countries are buying/selling US equities?
- How to detect repatriation risk (Japan, China)?
- Currency hedging by foreign holders — data available?
- Lead time: Do foreign flows lead or lag?

### 8. BUYBACK EXECUTION TRACKING
- How to track actual buyback execution vs announcements?
- Blackout periods around earnings — when do buybacks pause?
- Which companies are largest buyers?
- Is there a "buyback exhaustion" signal?
- Real-time vs quarterly data availability?

---

## Output Format Requested

```markdown
# Fund Flow Data & Positioning - Research Output

## Executive Summary
[Key findings on flow data availability and signals]

## 1. CFTC COT Analysis
[Interpretation guide with current readings]

| Contract | Net Positioning | Percentile | Signal |
|----------|-----------------|------------|--------|
| ES (S&P) | ... | ... | ... |
| NQ (Nasdaq) | ... | ... | ... |
[Continue]

## 2. Fund Flow Data Sources
| Provider | Coverage | Cost | Frequency | Access |
|----------|----------|------|-----------|--------|
| EPFR | ... | ... | ... | ... |
| ICI | ... | ... | ... | ... |
[Continue]

## 3. ETF Flow Monitoring
[Key ETFs and interpretation]

## 4. Sector Rotation Framework
[Rotation pairs and signals]

## 5. Retail vs Institutional
[How to distinguish and what each signals]

## 6. Cash/Money Market Analysis
[Current levels and interpretation]

## 7. Foreign Flow Tracking
[TIC data and repatriation risk]

## 8. Buyback Execution
[Tracking methods and exhaustion signals]

## Proposed HENRY Vectors
| ID | Name | Definition | Source | Frequency |
|----|------|------------|--------|-----------|
| VX-HEN-11.01 | ES Net Positioning | COT non-commercial net | CFTC | Weekly |
[Continue for all recommended vectors]

## Flow Reversal Warning System
[Framework for detecting when structural bid is breaking]

## Sources
[URLs, data feeds, access methods]
```

---

## Integration Notes for HENRY

After receiving this research:
- Create VX-HEN-11.xx series for Flow Positioning domain
- Build "Flow Momentum" composite indicator
- Add to FLOW.tsv: Flow reversal → Repricing cascade
- Coordinate with Structural Bid vectors (VX-HEN-8.xx)
- Establish weekly flow monitoring routine

---

*Prompt ready for external LLM research*
