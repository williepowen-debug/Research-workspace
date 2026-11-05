# RP-HEN-6.2: Credit Market Stress Signals

**Prompt ID:** RP-HEN-6.2
**Cluster:** Data Expansion
**Priority:** 2
**Created:** 2026-02-03

---

## Context for Research Assistant

HENRY focuses on equity market structure but credit markets often lead equities in signaling stress. The 2007-08 crisis showed credit stress (subprime, CDOs) preceded equity collapse by months. HENRY needs credit market vectors to complete the picture. Currently HENRY only tracks VIX for volatility — we need the bond equivalent (MOVE index) plus spread indicators.

Relevant HENRY context:
- Private Credit AUM: $3.0T (YELLOW, shadow leverage)
- PIK Income %: 12.8% (YELLOW, shadow default proxy)
- Equity Risk Premium: -1.80% (RED, negative)
- Household Equity Allocation: 47.08% (RED, ATH)

Cross-agent context:
- LIQUID tracks Treasury/funding markets
- CARL tracks consumer credit stress
- REGINALD tracks bank credit exposure

---

## Research Questions

### 1. CREDIT SPREAD INDICES
For each index, provide: definition, calculation, history, current level, stress thresholds

- **CDX.NA.HY** (North American High Yield CDS Index)
  - What spread level indicates stress? (Historical ranges)
  - How does it compare to HYG/JNK ETF spreads?
- **CDX.NA.IG** (Investment Grade CDS Index)
  - Normal range vs crisis levels?
  - Relationship to corporate bond ETF (LQD) spreads?
- **iTraxx Europe** indices
  - Crossover vs Main — which is more predictive?
- **OAS (Option-Adjusted Spread)** for HY and IG
  - How to interpret tightening/widening?

### 2. MOVE INDEX (Bond Volatility)
- What is the MOVE index and how is it calculated?
- Historical range and current reading?
- Relationship between MOVE and VIX?
- When does MOVE lead vs lag VIX?
- What MOVE levels correspond to:
  - Normal conditions
  - Elevated stress
  - Crisis conditions
- How did MOVE behave in:
  - March 2020 (COVID)
  - March 2023 (SVB)
  - October 2023 (Treasury selloff)

### 3. BANK CDS SPREADS
- Which major bank CDS should HENRY track?
  - US: JPM, BAC, C, GS, MS, WFC
  - European: DB, CS (now UBS), BNP, HSBC
- What CDS levels indicate systemic concern?
- How to create a "Bank CDS Index" composite?
- Historical case studies: Bear Stearns, Lehman, Credit Suisse CDS behavior before failure

### 4. CREDIT-EQUITY DIVERGENCE
- How to measure credit vs equity disagreement?
- Historical examples where credit led equity:
  - 2007: When did CDX HY widen vs S&P peak?
  - 2015-16: Energy credit stress
  - 2020: Credit froze before equity crash
- Is there current divergence? (Credit tight while equity elevated = complacency)
- Academic research on credit-equity lead/lag relationships?

### 5. FUNDING STRESS INDICATORS
Note: LIQUID covers Treasury/repo markets. HENRY should track corporate/credit-specific:

- **Commercial Paper spreads** (A2/P2 vs AA)
- **LIBOR-OIS spread** successor (SOFR spreads)
- **FRA-OIS spread** (forward rate agreement stress)
- **Cross-currency basis** (USD funding stress globally)
- **TED spread** equivalent in post-LIBOR world?

### 6. PRIVATE CREDIT SIGNALS
HENRY tracks Private Credit AUM and PIK %. Additional metrics:

- **BDC discounts to NAV** (publicly traded BDC price vs stated NAV)
- **Leveraged loan prices** (LSTA index)
- **CLO AAA spreads** (securitization market stress)
- **Middle market default rates** (Proskauer, Lincoln)
- **Covenant-lite loan %** (structural weakness indicator)

### 7. DATA SOURCES & ACCESS
For each metric:
- Free sources (FRED, Yahoo Finance, etc.)
- Paid sources (Bloomberg, ICE, Markit)
- Update frequency
- Historical data availability

---

## Output Format Requested

```markdown
# Credit Market Stress Signals - Research Output

## Executive Summary
[Key findings on credit market monitoring]

## 1. Credit Spread Indices
| Index | Current Level | 1Y Range | Crisis Level | Data Source |
|-------|---------------|----------|--------------|-------------|
| CDX HY | ... | ... | ... | ... |
| CDX IG | ... | ... | ... | ... |
[Continue]

## 2. MOVE Index Analysis
[Detailed breakdown with thresholds]

## 3. Bank CDS Dashboard
| Bank | Current CDS | Normal Range | Stress Level | Notes |
|------|-------------|--------------|--------------|-------|
[Major banks]

## 4. Credit-Equity Divergence
[Historical patterns and current status]

## 5. Funding Stress Indicators
[Corporate/credit specific funding metrics]

## 6. Private Credit Signals
[Shadow credit market health indicators]

## 7. Data Access Summary
| Metric | Free Source | Paid Source | Frequency |
|--------|-------------|-------------|-----------|
[All metrics]

## Proposed HENRY Vectors
| ID | Name | Current | Thresholds | Source |
|----|------|---------|------------|--------|
| VX-HEN-10.01 | CDX HY Spread | ... | G/Y/O/R | ... |
[Continue]

## Credit-Equity Lead/Lag Framework
[How to use credit signals for equity timing]

## Sources
[URLs and references]
```

---

## Integration Notes for HENRY

After receiving this research:
- Create VX-HEN-10.xx series for Credit domain
- Add MOVE index to existing volatility comparison (vs VIX)
- Build credit-equity divergence indicator
- Coordinate with LIQUID on funding stress overlap
- Add transmission path: Credit stress → Equity repricing

---

*Prompt ready for external LLM research*
