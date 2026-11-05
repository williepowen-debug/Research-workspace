# Credit Market Stress Signals - Research Output

**Prompt ID:** RP-HEN-6.2
**Completed:** 2026-02-03
**Research Source:** Web research, FRED, Schwab, provider documentation

---

## Executive Summary

- **Credit spreads are historically tight** — HY OAS at ~2.7% vs 20-year average of 4.9%; IG yields still elevated but spreads compressed
- **MOVE Index** (bond volatility) often leads VIX in signaling stress — currently less correlated as rate path has clarified
- **Low spreads = poor risk compensation** — When HY spreads <3%, high-yield bonds outperform Treasuries only 39% of the time (vs 83% when >5%)
- **Credit often leads equity** — 2007 credit widening preceded equity peak; March 2020 credit froze before stock crash
- **Key monitors:** CDX HY spread, CDX IG spread, MOVE index, HY OAS (FRED), bank CDS, credit-equity divergence
- **Current regime:** Complacent — low spreads + low VIX = underpriced risk in both markets

---

## 1. Credit Spread Indices

### ICE BofA US High Yield Index OAS (BAMLH0A0HYM2)

**Definition:** Option-adjusted spread between below investment grade corporate bonds and spot Treasury curve

**Current Status (Late 2025/Early 2026):**
- **Current spread:** ~2.7% (270 bps)
- **20-year average:** 4.9% (490 bps)
- **15-year range:** 2.4% to 21.5% (COVID peak)
- **Status:** Historically tight — YELLOW/ORANGE for HENRY

**Historical Context:**
| Period | HY OAS | Interpretation |
|--------|--------|----------------|
| Normal | 4-5% | Fair compensation |
| Tight | 2.5-3.5% | Complacent, low risk premium |
| Stress | 5-8% | Elevated concern |
| Crisis | >8% | Risk-off, potential opportunity |
| COVID Peak (Mar 2020) | 10.8%+ | Panic |
| GFC Peak (2008) | 21%+ | Systemic crisis |

**Data Source:** FRED (BAMLH0A0HYM2) — free, daily updates
https://fred.stlouisfed.org/series/BAMLH0A0HYM2

### CDX.NA.HY (High Yield CDS Index)

**Definition:** Tradable index of credit default swaps on basket of North American high-yield issuers

**Key Characteristics:**
- Most liquid HY credit derivative
- 5-year maturity standard
- Rolls every 6 months (new series)
- Spread quoted in basis points

**Current Status:** Tight (tracking HY bond OAS closely)

**Data Sources:**
- Cbonds: https://cbonds.com/indexes/204391/
- Bloomberg terminal (CDX HY)
- ICE (requires subscription)

### CDX.NA.IG (Investment Grade CDS Index)

**Definition:** Tradable index of credit default swaps on 125 investment grade North American issuers

**Current Status:**
- IG spreads also historically tight
- IG bond yields ~4.8% (down from 6.4% peak in late 2023)
- Still above 15-year average of 3.2%
- Credit quality improving: A-rated now largest share of IG index (46%), surpassing Baa (45%)

**Data Source:** 
- Cbonds: https://cbonds.com/indexes/204395/
- FRED: BAMLC0A0CM (IG OAS)

### Spread Thresholds for HENRY

| Index | GREEN | YELLOW | ORANGE | RED |
|-------|-------|--------|--------|-----|
| HY OAS | 4-5% | 3-4% | 2.5-3% OR >6% | <2.5% OR >8% |
| IG OAS | 1-1.5% | 0.8-1% | <0.8% OR >2% | <0.6% OR >3% |
| CDX HY | 350-450 bps | 300-350 bps | 250-300 bps OR >500 bps | <250 bps OR >600 bps |
| CDX IG | 60-80 bps | 50-60 bps | <50 bps OR >100 bps | <40 bps OR >150 bps |

**Note:** Both very tight AND very wide spreads are concerning — tight = complacency, wide = stress

---

## 2. MOVE Index Analysis

### What is MOVE?

**Merrill Lynch Option Volatility Estimate (MOVE)** — measures implied volatility in US Treasury options across 2Y, 5Y, 10Y, and 30Y maturities. Often called the "VIX for bonds."

**Calculation:** Weighted average of 1-month options on Treasury futures

**Current Status:**
- 200-day MA: ~110
- Most of 2024-2025: Below 120
- Current environment: Moderate, less correlated with VIX

### Historical Ranges

| Level | Interpretation | Historical Context |
|-------|----------------|-------------------|
| <80 | Very low vol | Rare, typically before vol events |
| 80-100 | Low/normal | Stable rate expectations |
| 100-120 | Normal | Typical range 2024 |
| 120-140 | Elevated | Rate uncertainty, mild stress |
| 140-170 | High | Significant uncertainty |
| >170 | Crisis | Banking crisis Mar 2023 reached ~198 |

### MOVE vs VIX Relationship

**Key insight from Schwab research:**
- MOVE and VIX correlation peaks at 60-70% during stress periods
- MOVE often LEADS VIX when bond volatility drives equity concerns
- March 2023: MOVE rose several days before VIX during banking crisis
- 2022: MOVE rose before VIX as Fed signaled rate hikes

**When MOVE leads:**
- Rate policy uncertainty
- Banking/financial stress
- Treasury market dislocations

**When less correlated (current regime):**
- Rate path clearer
- Stock market decoupled from rate sensitivity
- Mid-2024 onward: Lower MOVE/VIX correlation

### MOVE Thresholds for HENRY

| Level | Status | Action |
|-------|--------|--------|
| <90 | GREEN | Normal monitoring |
| 90-110 | YELLOW | Watch for divergence from VIX |
| 110-130 | ORANGE | Elevated bond stress |
| >130 | RED | High stress, expect equity spillover |

**Data Sources:**
- Yahoo Finance: ^MOVE
- TradingView: TVC:MOVE
- thinkorswim: MOVE:GIF
- CNBC: .MOVE

---

## 3. Bank CDS Dashboard

### Major Bank CDS to Monitor

| Bank | Ticker | Normal Range (bps) | Stress Level | Notes |
|------|--------|-------------------|--------------|-------|
| JPMorgan (JPM) | JPM CDS | 40-70 | >100 | Largest US bank, systemic |
| Bank of America (BAC) | BAC CDS | 50-80 | >120 | Consumer exposure |
| Citigroup (C) | C CDS | 60-100 | >140 | Global operations |
| Goldman Sachs (GS) | GS CDS | 50-90 | >130 | Trading/investment bank |
| Morgan Stanley (MS) | MS CDS | 50-90 | >130 | Wealth mgmt + trading |
| Wells Fargo (WFC) | WFC CDS | 45-75 | >110 | Consumer/mortgage focus |

### Historical Bank CDS Behavior

**Pre-failure patterns:**
- Bear Stearns (2008): CDS rose from ~80bps to 800+ bps weeks before collapse
- Lehman (2008): CDS spiked to 700+ bps before bankruptcy
- Credit Suisse (2023): CDS rose to 400+ bps before UBS rescue

**Current status:** Major US bank CDS relatively calm; regional bank stress not fully reflected in majors

**Data access:** 
- Bloomberg (CDS pricing)
- Reuters/Refinitiv
- IHS Markit (subscription)
- Limited free access — consider tracking via bank bond spreads as proxy

### Bank CDS Composite Idea

Create simple average of top 6 US bank CDS as "Financial Stress Index":
- Normal: <70 bps average
- Elevated: 70-100 bps
- Stress: 100-150 bps
- Crisis: >150 bps

---

## 4. Credit-Equity Divergence

### Why Credit Leads Equity

Credit markets are often "smarter" than equity markets because:
1. Institutional-dominated (less retail noise)
2. Focus on downside risk (default probability)
3. Direct connection to corporate fundamentals
4. Less momentum-driven than equities

### Historical Lead Times

| Event | Credit Signal | Equity Peak | Lead Time |
|-------|---------------|-------------|-----------|
| 2007-08 GFC | CDX HY widening mid-2007 | S&P 500 Oct 2007 | ~3-4 months |
| 2015-16 Energy | HY energy spreads blew out Q3 2015 | S&P 500 correction Jan 2016 | ~4-5 months |
| COVID 2020 | Credit froze March 9-12 | S&P 500 bottom March 23 | Credit slightly ahead |
| 2018 Q4 | IG/HY widened Sept-Oct | S&P 500 peaked Sept, crashed Dec | Credit concurrent |

### Current Divergence Analysis

**Current situation (Feb 2026):**
- HY spreads: Historically tight (~2.7%)
- IG spreads: Tight
- S&P 500: Near all-time highs
- VIX: Low (16)

**Interpretation:** NO DIVERGENCE currently — both credit and equity complacent
- This is CONCERNING from a risk perspective
- Both markets pricing minimal risk simultaneously
- When divergence eventually appears (credit widens while equity flat), it's a strong signal

### Divergence Detection Framework

Monitor weekly:
1. HY OAS 4-week change
2. SPX 4-week change
3. Divergence score = HY change - SPX change (inverted)

**Alert triggers:**
- HY widening >50bps while SPX flat/up = bearish divergence
- HY tightening while SPX falling = bullish divergence (credit doesn't confirm equity weakness)

---

## 5. Funding Stress Indicators

*(Note: LIQUID tracks Treasury/repo; these are corporate/credit-specific)*

### Commercial Paper Spreads

| Metric | Normal | Elevated | Stress |
|--------|--------|----------|--------|
| A2/P2 - AA spread | 20-40 bps | 40-80 bps | >100 bps |

Commercial paper is short-term corporate IOUs — spread widening signals funding stress.

### Cross-Currency Basis

- EUR/USD basis, JPY/USD basis
- Negative basis = premium for USD funding globally
- Coordinate with SAM for JPY basis (Japan repatriation risk)

### SOFR Spreads

*(Tracked by LIQUID)*
- SOFR-IORB spread currently +3bps (YELLOW per LIQUID)

---

## 6. Private Credit Signals

### BDC Discounts to NAV

**Business Development Companies (BDCs)** are publicly traded private credit vehicles.

| BDC | Ticker | Watch for |
|-----|--------|-----------|
| Ares Capital | ARCC | Largest BDC |
| Main Street Capital | MAIN | High quality |
| Owl Rock Capital | ORCC | Tech focus |
| Golub Capital | GBDC | Middle market |

**Signal:** Premium to NAV = bullish; Discount to NAV = stress
- Normal: 0-5% premium
- Concern: >10% discount
- Stress: >20% discount

### Leveraged Loan Prices

**S&P/LSTA Leveraged Loan Index:**
- Price: 96-99 = normal
- Price: 93-96 = concern
- Price: <93 = stress

**Data:** S&P Global, LCD

### CLO AAA Spreads

CLO (Collateralized Loan Obligation) AAA tranches:
- Normal: 100-130 bps
- Elevated: 130-180 bps
- Stress: >200 bps

### Current Private Credit Status (from HENRY VX)

| Metric | Current | Status |
|--------|---------|--------|
| Private Credit AUM | $3.0T | YELLOW (unprecedented scale) |
| PIK Income % | 12.8% | YELLOW (shadow default proxy) |

---

## 7. Data Access Summary

| Metric | Free Source | URL | Frequency |
|--------|-------------|-----|-----------|
| HY OAS | FRED | fred.stlouisfed.org/series/BAMLH0A0HYM2 | Daily |
| IG OAS | FRED | fred.stlouisfed.org/series/BAMLC0A0CM | Daily |
| MOVE Index | Yahoo Finance | finance.yahoo.com/quote/^MOVE | Daily |
| VIX | Yahoo Finance | finance.yahoo.com/quote/^VIX | Real-time |
| CDX HY | Cbonds | cbonds.com/indexes/204391 | Daily |
| CDX IG | Cbonds | cbonds.com/indexes/204395 | Daily |
| Bank CDS | Limited free | Track via bond spreads | N/A |
| Leveraged Loans | LCD/S&P (paid) | N/A | Daily |
| CLO Spreads | Bloomberg (paid) | N/A | Daily |
| BDC Prices | Yahoo Finance | Various tickers | Real-time |

---

## Proposed HENRY Vectors

| ID | Name | Current | Thresholds (G/Y/O/R) | Source | Frequency |
|----|------|---------|----------------------|--------|-----------|
| VX-HEN-10.01 | HY OAS | ~2.7% | 4-5% / 3-4% / 2.5-3% / <2.5% or >6% | FRED | Daily |
| VX-HEN-10.02 | IG OAS | TBD | 1-1.5% / 0.8-1% / <0.8% / <0.6% or >2% | FRED | Daily |
| VX-HEN-10.03 | MOVE Index | ~105 | <90 / 90-110 / 110-130 / >130 | Yahoo | Daily |
| VX-HEN-10.04 | MOVE/VIX Ratio | TBD | 5-7 / 4-5 or 7-9 / <4 or >9 / extreme | Calculated | Daily |
| VX-HEN-10.05 | Credit-Equity Divergence | None | No divergence / Mild / Moderate / Strong | Calculated | Weekly |
| VX-HEN-10.06 | Bank CDS Composite | TBD | <70 / 70-100 / 100-150 / >150 bps | Proxy | Weekly |

---

## Credit-Equity Lead/Lag Framework

### Decision Tree

```
1. Check HY OAS trend (4-week)
   ├── Widening while SPX flat/up → BEARISH DIVERGENCE → Reduce equity exposure
   ├── Tightening while SPX up → CONFIRMATION → Maintain/add
   ├── Tightening while SPX down → BULLISH DIVERGENCE → Credit doesn't confirm weakness
   └── Widening while SPX down → CONFIRMATION → Credit confirming equity stress

2. Check MOVE vs VIX
   ├── MOVE rising, VIX flat → Bond stress coming, may spill to equity
   ├── MOVE and VIX both rising → Broad stress
   └── MOVE falling, VIX rising → Idiosyncratic equity event

3. Check spread level (absolute)
   ├── HY OAS <3% → Complacency, eventual widening likely
   └── HY OAS >5% → Opportunity if fundamentals stable
```

### Current Assessment (Feb 2026)

| Factor | Reading | Interpretation |
|--------|---------|----------------|
| HY OAS | ~2.7% (tight) | Complacent |
| MOVE | ~105 (normal) | Stable |
| VIX | 16 (low) | Complacent |
| Divergence | None | Both markets complacent together |
| **Overall** | **YELLOW** | Low risk premium across markets; eventual correction likely but no imminent signal |

---

## Cross-Agent Integration

### LIQUID Coordination
- LIQUID tracks: SOFR spreads, RRP, SRF, Treasury auctions
- HENRY tracks: Corporate credit, HY/IG spreads, MOVE
- **Overlap:** MOVE index (bond vol) — HENRY to add, coordinate with LIQUID
- **Transmission:** Treasury stress (LIQUID) → Corporate stress (HENRY) → Equity stress (HENRY)

### CARL Coordination
- CARL tracks: Consumer credit stress, phantom debt, household vulnerability
- **Transmission:** Consumer defaults → Bank credit losses → Corporate stress → HY widening
- **Signal:** Watch PIK % (CARL/HENRY) as early corporate stress indicator

### REGINALD Coordination
- REGINALD tracks: Regional bank exposure
- **Transmission:** Bank CDS widening → Regional bank stress → Credit contraction
- **Signal:** If HENRY Bank CDS Composite rises, alert REGINALD

---

## Sources

### Data Sources
- FRED: https://fred.stlouisfed.org
- Yahoo Finance: https://finance.yahoo.com
- Cbonds: https://cbonds.com
- ICE: https://www.theice.com/market-data/indices

### Research
- Charles Schwab (2026): "2026 Corporate Credit Outlook"
- Charles Schwab: "What's the MOVE Index and Why It Might Matter?"
- CFA Institute (2025): "Volatility Signals: Do Equities Forecast Bonds?"
- SOA (2025): "Using Bond and Equity Volatility Indices for Investment Allocation"

### Index Providers
- ICE BofA Indices (via FRED)
- S&P/LSTA (leveraged loans)
- Markit CDX indices

---

*Research completed 2026-02-03 for HENRY agent integration*
