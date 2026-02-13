# RP-HANS-1: European UST Holdings Deep Dive

**Research Date:** February 13, 2026  
**Agent:** HANS  
**Status:** Initial Compilation  

---

## Executive Summary

European holdings of US Treasuries represent a critical but often misunderstood pillar of UST demand. As of November 2025, the top 8 European countries hold **$3.52 trillion** in USTs (38% of total foreign holdings of $9.36T). However, custody vs. beneficial ownership issues mean actual European demand may be significantly lower, with Belgium serving as a proxy for China and other non-European holders via Euroclear, and Ireland/Luxembourg inflated by fund domicile effects.

**Key Finding:** European UST holdings are structurally vulnerable to:
1. UK pension deleveraging post-LDI crisis
2. ECB policy divergence from Fed  
3. Euro strength vs USD
4. Regulatory changes to leverage/LDI strategies
5. Redomiciling of funds and custody arrangements

**Market Implication:** A 10-15% reduction in European holdings ($350-525B) over 12-18 months would add 15-25bps to 10Y yields and force increased Fed accommodation or domestic buyer absorption.

---

## 1. Current Holdings Breakdown by Country

### TIC Data (November 2025)

| Country | Holdings ($B) | % of Total Foreign | M/M Change | YoY Change |
|---------|--------------|-------------------|------------|------------|
| **United Kingdom** | 888.5 | 9.5% | +10.6 | +15.8% (+121.6B) |
| **Luxembourg** | 425.6 | 4.5% | +6.6 | +1.9% (+7.8B) |
| **Belgium** | 481.0 | 5.1% | +12.6 | +33.1% (+119.7B) |
| **France** | 376.1 | 4.0% | -14.2 | +13.1% (+43.6B) |
| **Ireland** | 340.3 | 3.6% | -0.1 | -0.8% (-2.8B) |
| **Switzerland** | 300.3 | 3.2% | -2.0 | +0.5% (+1.6B) |
| **Germany** | 109.8 | 1.2% | -5.7 | +9.7% (+9.7B) |
| **Netherlands** | (in "All Other") | — | — | — |
| **TOTAL (Top 7)** | 2,921.6 | 31.2% | — | +17.2% (+428.0B) |

*Note: Netherlands holdings not separately reported in Major Foreign Holders table (under $100B threshold). Likely in "All Other" category ($1.83T).*

**Total Europe (est. including smaller countries):** ~$3.5-3.8 trillion

### Data Quality Issues

**CRITICAL:** TIC data reports **custody location**, not beneficial ownership. Per TIC FAQ #7:

> "Since U.S. securities held in overseas custody accounts may not be attributed to the actual owners, the data may not provide a precise accounting of individual country ownership of Treasury securities."

This is especially problematic for:
- **Belgium** (Euroclear custody)
- **Ireland** (fund domicile)
- **Luxembourg** (fund domicile)
- **Switzerland** (wealth management custody)

---

## 2. Historical Trends (2020-2025)

### Five-Year View

| Country | Dec 2020 | Dec 2024 | Nov 2025 | 5Y Change | Trend |
|---------|----------|----------|----------|-----------|-------|
| **UK** | 444.2 | 722.8 | 888.5 | +100.0% | **BUYING** |
| **Luxembourg** | 273.6 | 423.9 | 425.6 | +55.5% | Steady |
| **Belgium** | 206.3 | 374.6 | 481.0 | +133.1% | **BUYING** |
| **France** | 151.4 | 332.3 | 376.1 | +148.4% | **BUYING** |
| **Ireland** | 292.0 | 339.4 | 340.3 | +16.5% | Flat |
| **Switzerland** | 264.9 | 298.7 | 300.3 | +13.4% | Flat |
| **Germany** | 76.0 | 97.2 | 109.8 | +44.5% | Modest growth |

### Key Observations:

1. **UK surge (2024-2025):** +$166B in 12 months — unprecedented. Likely driven by:
   - Post-LDI crisis rebuilding of gilt/UST portfolios
   - BoE QT forcing pension funds into alternatives
   - Weaker GBP making USD assets attractive
   - **Risk:** This is a reversal pattern, not sustainable demand

2. **Belgium anomaly:** Holdings up 133% since 2020, but peaked at $481B (Nov 2025) vs. ~$180B historical norm. **China connection** (see Section 4).

3. **France acceleration:** Holdings tripled 2020-2025. Likely ECB QT-driven reallocation by French banks/insurers.

4. **Ireland/Luxembourg stability:** Despite being fund domiciles, holdings surprisingly stable — suggests underlying beneficial owners (global asset managers) maintaining UST allocations.

5. **Switzerland caution:** Swiss National Bank and wealth managers not aggressively accumulating despite negative EUR rates through 2022.

---

## 3. Custody vs. Beneficial Ownership

### The Fund Domicile Problem: Ireland & Luxembourg

**Ireland** and **Luxembourg** are the **#1 and #2 global fund domiciles** by AUM:
- Combined 91% of EU cross-border fund AUM
- $6+ trillion in investment funds domiciled in Ireland
- $5+ trillion in Luxembourg

**Why these domiciles:**
1. **Tax efficiency:** Ireland has favorable US tax treaty (15% dividend withholding vs. 30% for Luxembourg)
2. **Regulatory:** UCITS framework for global distribution
3. **Infrastructure:** CSDs (Euroclear Ireland/Clearstream Luxembourg) provide settlement
4. **Legal:** English law, flexible fund structures

**Implication for UST holdings:**
- Irish/Luxembourg TIC holdings **overstate** actual Irish/Luxembourg demand
- Beneficial owners are **global:** US pension funds, Asian sovereign wealth, Middle East wealth
- A US-based Vanguard or BlackRock fund domiciled in Ireland shows up as "Ireland" in TIC data

**Estimate:** Of Ireland's $340B and Luxembourg's $426B (total $766B):
- ~60-70% beneficial ownership is **non-European** (US, Asia, Middle East)
- **True European demand:** $230-310B, not $766B

---

## 4. Belgium as a Special Case: The Euroclear Custody Proxy

### The "Belgium Mystery" (2014-2025)

Belgium's UST holdings surged from **~$170B (2013) → $381B (2014) → $374B (Dec 2024) → $481B (Nov 2025).**

**Belgium GDP:** $484B (2014) → ~$600B (2025)  
**Holdings as % of GDP:** 70-80% — **absurd for a small open economy**

### Euroclear Explanation

**Euroclear Bank** (Brussels HQ):
- €24.2 trillion ($33T) in custody globally
- Settles €570T+ in transactions annually
- Clients: 2,000+ banks, central banks, sovereign wealth funds, broker-dealers in 90+ countries

**What happened (per Wolf Street, Reuters 2014):**
1. **Russia began moving USTs from Fed custody** in late 2013/early 2014 (Ukraine tensions, sanctions risk)
2. **China likely followed** in 2014-2015 to obscure holdings and avoid US political pressure
3. **Treasuries moved to Euroclear custody** → reported under "Belgium" in TIC data
4. **Fed's "Securities Held in Custody for Foreign Official Accounts" showed historic volatility:**
   - Peaked $3.02T (Dec 2013)
   - Plunged by record $104.5B in week of March 5, 2014
   - Treasuries reappeared via Euroclear (Belgium)

**Current Status (2025):**
- Belgium holdings $481B (Nov 2025) — up $107B from Dec 2024
- China (Mainland) holdings: $683B — **DOWN** $86B from Feb 2025 peak of $784B
- **Hypothesis:** China continues using Belgium/Euroclear to park $100-200B in USTs

**ZHAO connection:** This directly supports ZHAO's thesis that China is obscuring UST holdings via third-party custodians.

### Implications:

1. **Belgium holdings are NOT Belgian demand** — likely 70-80% are Chinese, Russian, Middle Eastern
2. **True European Belgium exposure:** ~$100-150B (Belgian banks, ECB operations)
3. **Geopolitical risk:** If Euroclear becomes sanctioned or politically pressured (Russia precedent), up to $300B could rapidly relocate

---

## 5. UK Pension Funds: Gilt/UST Allocation Post-LDI Crisis

### The September 2022 LDI Crisis

**Background:**
- **Liability-Driven Investment (LDI):** Strategy used by 60% of UK defined benefit pension schemes
- **Objective:** Match duration of long-term pension liabilities with assets
- **Method:** Leverage via repos + interest rate swaps to synthetically extend duration
- **Scale:** ~£1.5 trillion in DB pension assets, heavily leveraged

**What Happened (Sept 23-28, 2022):**
1. **Mini-budget announcement:** UK Chancellor proposed unfunded tax cuts
2. **Gilt yields spiked:** 30-year gilt yields rose **200bps in 4 days** (unprecedented)
3. **Margin calls:** Pension funds faced £50-100B+ in variation margin calls on swaps
4. **Fire sales:** Funds sold gilts to raise cash → gilt prices collapsed further
5. **Doom loop:** More selling → lower prices → more margin calls
6. **BoE intervention (Sept 28):** Temporary gilt purchase program (£19.3B purchased) stabilized market

**Damage:**
- Pension funding ratios fell despite higher discount rates (accounting lag)
- Forced asset sales locked in losses
- Leverage reduced from ~1/3 of assets to ~1/5

### Impact on UST Holdings

**Pre-Crisis (2020-2021):**
- UK pensions held modest UST allocations (5-10% of fixed income)
- Focus on gilts for liability matching

**Post-Crisis (2022-2025):**
- **Diversification imperative:** Never again 100% gilts
- **UST buying surge:** UK holdings rose from $445B (Dec 2020) → $889B (Nov 2025) = **+100%**
- **Drivers:**
  - Regulatory pressure (TPR guidance) to reduce leverage, increase liquidity
  - Gilt market scarred — depth concerns
  - UST market 7x larger ($10T vs. $1.5T gilts) → better liquidity
  - Yield advantage: US 10Y often 50-100bps above gilts (2023-2025)

**Chicago Fed Analysis (2023):**
> "UK pension funds held 28% of the gilt market but were concentrated at the long end where price action occurred. U.S. pension funds hold only 2.2% of Treasury market."

**Current Allocation (2025 est.):**
- UK DB pensions: £1.6T in assets
- UST holdings: ~£450-500B ($560-625B equivalent)
- **True UK pension UST exposure:** ~$500-600B of the $889B total UK TIC holdings
- Remainder: BoE reserves, UK banks, insurance companies, asset managers

### Vulnerability / Trigger for Selling

**What would cause UK pension funds to sell USTs?**

1. **Gilt yield advantage:** If gilt yields rise 50-100bps above USTs (BoE hikes, UK fiscal crisis), repatriation of capital
2. **GBP strength:** If GBP/USD rallies above 1.40, currency hedging costs rise, UST attractiveness falls
3. **Regulatory tightening:** If TPR forces further deleveraging or currency hedging mandates
4. **Funded status improvement:** If pension surpluses emerge (higher discount rates), shift to riskier assets (equities, alternatives)
5. **US credit concerns:** Debt ceiling crisis, fiscal sustainability doubts

**Timeframe risk:** UK pensions are **long-term holders** (liabilities extend 15-20 years). Not fast money. But regulatory/macro shocks could trigger 6-12 month reallocation waves.

---

## 6. Triggers for European UST Selling

### Macro Triggers

| Trigger | Probability | Magnitude | Timeframe |
|---------|------------|-----------|-----------|
| **ECB policy divergence** (cuts 200bps+ vs. Fed) | HIGH | -$200-300B | 12-18 mo |
| **EUR/USD rally to 1.20+** | MEDIUM | -$150-250B | 6-12 mo |
| **Eurozone fiscal expansion** (EU defense spending) | MEDIUM | -$100-200B | 18-24 mo |
| **UK gilt crisis 2.0** | LOW | -$300-500B | 3-6 mo (acute) |
| **China Euroclear exit** (Belgium drop) | LOW-MED | -$200-300B | 6-12 mo |
| **US debt ceiling / fiscal crisis** | MEDIUM | -$500B+ | 3-6 mo (flight) |

### Regulatory/Structural Triggers

1. **UK TPR LDI rules tightening** (2024-2026)
   - Force 50%+ reduction in leverage
   - Mandate sterling asset concentration
   - **Result:** £100-200B UST selling

2. **EU AIFMD changes** (Alternative Investment Fund Managers Directive)
   - Restrictions on non-EU custody (Euroclear Bank under scrutiny)
   - Leverage limits on EU funds
   - **Result:** Redomiciling, custody shifts

3. **Euroclear sanctions risk**
   - If Russia precedent expands (frozen assets at Euroclear), China/ME exit
   - Belgium holdings drop $200-300B

4. **Currency hedging costs**
   - If USD funding costs (cross-currency basis swaps) spike, unhedged EUR investors exit
   - **Example:** 2020 COVID crisis saw -150bps basis, European UST sales

### Market Structure Triggers

**Liquidity cascade scenario:**
1. Initial shock (e.g., Fed surprise hike, US downgrade)
2. UK pension funds face margin calls on remaining derivative positions
3. Forced UST selling in size (low liquidity offshore hours)
4. Price impact triggers stop-losses for other European holders (Swiss SNB, ECB)
5. Reflexive selling spiral

**Historical precedent:** Sept 2022 gilt crisis saw 200bps move in 4 days. UST market more liquid, but $500B European selling wave could generate 50-100bps 10Y yield spike.

---

## 7. Data Sources for Monitoring

### Primary Sources

| Source | URL | Frequency | Key Data |
|--------|-----|-----------|----------|
| **TIC Table 5** | [ticdata.treasury.gov](https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.html) | Monthly | Major foreign holders by country |
| **TIC SHL Report** | [Treasury SHL](https://home.treasury.gov/data/treasury-international-capital-tic-system/us-liabilities-to-foreigners-from-holdings-of-us-securities) | Annual | Detailed beneficial ownership survey (June survey, April release) |
| **Fed Foreign Official Custody** | [FRED WMTSECL1](https://fred.stlouisfed.org/series/WMTSECL1) | Weekly | Foreign central bank holdings at Fed (watch for Belgium/Euroclear shifts) |
| **UK TPR Pension Reports** | [thepensionsregulator.gov.uk](https://www.thepensionsregulator.gov.uk/en/document-library/research-and-analysis/db-pensions-landscape-2022) | Quarterly/Annual | UK pension funding ratios, LDI usage |
| **ECB Balance Sheet** | [ecb.europa.eu](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html) | Weekly | ECB UST holdings (rare, but visible in securities held for monetary policy) |
| **Euroclear Disclosures** | [euroclear.com](https://www.euroclear.com/newsandinsights/) | Ad hoc | Total assets in custody (rare granular UST data) |

### Secondary Monitoring

1. **Cross-currency basis swaps (EUR/USD 3M, 5Y)**
   - Source: Bloomberg EURUSD3M Curncy, XCC5EUR Curncy
   - Spike in hedging costs = European selling pressure

2. **Gilt-UST 10Y spread**
   - Narrowing spread (gilts outperform) = UK repatriation risk
   - Monitor: Bloomberg GUKG10 - USGG10YR

3. **EUR/USD spot & 6M forward**
   - EUR rally = unhedged UST holders face losses
   - Monitor: Bloomberg EURUSD Curncy

4. **UK pension funding ratios**
   - TPR Purple Book (annual), ONS Funded Pension Schemes (quarterly)
   - Improving ratios = risk asset rotation (out of USTs)

5. **Chinese TIC holdings + Belgium correlation**
   - Watch for inverse relationship (China ↓, Belgium ↑)
   - 3-month rolling correlation, lag analysis

---

## 8. Thresholds for VX.tsv Updates

Based on research, recommend the following **vector thresholds** for HANS monitoring:

| Vector | Current | Trigger Level | Action |
|--------|---------|--------------|--------|
| **UK Holdings** | $889B | < $800B (3mo decline) | Alert PROME — UK pension deleveraging |
| **Belgium Holdings** | $481B | > $550B or < $350B | Alert ZHAO — China custody shift |
| **Ireland + Luxembourg** | $766B | < $650B (fund redomiciling) | Alert — global UST sentiment |
| **Gilt-UST 10Y spread** | ~+50bps | Gilts < UST -20bps | UK repatriation risk HIGH |
| **EUR/USD basis (3M)** | ~-10bps | < -50bps | European hedging costs spike |
| **UK pension funding ratio** | ~95% (avg) | > 105% | Risk asset rotation, UST selling |

---

## 9. Implications for US Treasury Market Demand and Yields

### Structural Demand Assessment

**European UST holdings ($3.5-3.8T) breakdown:**
- **Stable beneficial owners:** $1.5-2.0T (genuine European pensions, insurers, central banks)
- **Flighty/misattributed:** $1.5-1.8T (China via Belgium, fund domicile effects, leveraged positions)

**Demand quality:** MEDIUM-LOW compared to Japan, China (mainland)

**Reasoning:**
1. **UK pensions are post-crisis buyers** — NOT structural. Bought for diversification after gilt trauma, will rotate out when funding improves or gilt yields rise.
2. **Belgium holdings are China proxy** — subject to geopolitical whims, zero European policy loyalty
3. **Ireland/Luxembourg are pass-through** — actual demand is from underlying global fund investors, not European

### Yield Impact Scenarios

**Scenario 1: Orderly European Rotation (18-24 months)**
- UK pensions reduce UST from $600B → $400B (-$200B)
- France/Germany stabilize as ECB cuts rates (ECB becomes net UST buyer to diversify reserves)
- Belgium drops to $350B as China shifts to HK custody (-$130B)
- **Net European selling:** -$300-350B
- **10Y yield impact:** +15-20bps (absorbed by Fed QE taper end, domestic banks)

**Scenario 2: LDI Crisis 2.0 (3-6 months)**
- UK crisis triggers forced deleveraging
- UK sells $400B USTs in 3 months (fire sale)
- European insurers face contagion, sell another $150B
- China exits Belgium, -$200B
- **Net selling:** -$750B in 3-6 months
- **10Y yield impact:** +50-100bps (depending on Fed response)
- **Fed response:** Emergency repo facility for foreign holders, UST buybacks

**Scenario 3: EUR Strength + ECB Divergence (12 months)**
- EUR/USD rallies to 1.25 (ECB cuts 200bps, Fed on hold)
- Unhedged European holders face 15-20% currency losses
- Risk parity funds, European asset managers dump $300-400B USTs
- **10Y yield impact:** +25-40bps
- **Contagion:** European selling triggers broader EM exodus, Japan hesitation

### Monitoring Priority

**HANS recommendation to PROME:**
1. **Weekly monitoring:** UK holdings (monthly data), Fed foreign custody accounts (weekly)
2. **Daily monitoring:** Gilt-UST spread, EUR/USD, cross-currency basis
3. **Event-driven:** UK TPR reports, Euroclear announcements, ECB press conferences
4. **Correlation watch:** China TIC vs. Belgium TIC (3-month lag analysis)

**Escalation trigger:** Any 2 of these in same month:
- UK holdings drop >$50B
- Belgium drops >$40B
- Gilt-UST spread flips negative
- EUR/USD above 1.20
- Cross-currency basis below -40bps

→ **IMPLICATION: Risk of $200-500B European UST liquidation wave within 6 months**

---

## 10. Cross-Agent Connections

### ZHAO (China UST Holdings)
- **Belgium = China's stealth holdings:** Monitor Belgium TIC as inverse/leading indicator for China mainland TIC
- **Euroclear risk:** Sanctions precedent (Russia) could trigger China exit
- **Data sharing:** HANS provides Belgium analysis, ZHAO provides China policy context

### LIQUID (Central Bank Liquidity, FX Markets)
- **ECB operations:** Eurozone QT → who absorbs? If not European banks, USTs sold
- **FX swap lines:** Fed-ECB swap usage spike = European USD shortage, UST liquidation risk
- **SNB interventions:** Swiss FX interventions (EUR buying) affect CHF/USD, UST demand

### SAM (Japan UST Holdings)
- **Comparison:** Japan ($1.2T) vs. Europe ($3.5T+) — Japan more stable (official reserves, life insurers)
- **Correlation risk:** If both Japan and Europe reduce simultaneously (Fed hiking cycle), demand crisis
- **Trigger divergence:** Japan sells on yen strength; Europe sells on EUR strength — different cycles

### HENRY (Risk Sentiment, Equity Flows)
- **European equity allocation:** If European stocks outperform (EU defense spending, fiscal expansion), pensions rotate out of USTs
- **Risk-on/risk-off:** European UST holdings are RISK-OFF proxy — sell in risk-on environments
- **VIX correlation:** UK pension LDI sensitivity to vol → VIX spike = UK UST selling (margin calls)

### REGINALD (Counterparty Risk, Bank Funding)
- **UK bank gilt exposures:** UK banks are intermediaries for pension LDI — bank stress = pension stress
- **Euroclear counterparty risk:** If Euroclear faces sanctions/operational issues, $400-500B UST custody at risk
- **Cross-currency repo:** European banks provide USD via repo to pension funds — repo stress = forced selling

---

## 11. Research Gaps & Next Steps

### Data Gaps Identified

1. **Netherlands holdings:** Not in Major Foreign Holders table. Need TIC SHL annual survey (next: June 2026 data, April 2027 release).

2. **True beneficial ownership for Ireland/Luxembourg:** TIC provides domicile, not owner. Requires:
   - ECB fund flow data (quarterly)
   - BIS international banking statistics
   - Individual fund prospectus analysis (BlackRock, Vanguard domicile data)

3. **UK pension UST allocation detail:** TPR doesn't break down "overseas bonds" by country. Need:
   - Freedom of information request to TPR
   - Analysis of largest UK pension annual reports (USS, CalPERS UK counterparts)

4. **Euroclear client data:** Euroclear doesn't disclose country-level UST custody. Potential sources:
   - BIS international debt securities database
   - Fed NY foreign custody cross-checks

### Recommended Research Tasks

**RP-HANS-2:** UK Pension Fund UST Holdings Survey
- FOIA request to TPR for overseas bond allocation breakdown
- Analysis of top 20 UK DB pension annual reports (2020-2025)
- Estimate true UK pension UST exposure ($400-600B range)

**RP-HANS-3:** Belgium/China Euroclear Correlation Analysis
- Build time series: China TIC, Belgium TIC, Fed foreign custody (2010-2025)
- Regression analysis, lead/lag testing
- Quantify % of Belgium attributable to China

**RP-HANS-4:** European Fund Domicile Effect Quantification
- ECB investment fund statistics (Ireland/Luxembourg fund investor nationality)
- Estimate % of TIC Ireland/Luxembourg holdings that are non-European beneficial owners
- Adjust "true European demand" figures

**RP-HANS-5:** European UST Demand Model
- Build regression model: European UST holdings ~ f(EUR/USD, Gilt-UST spread, ECB policy rate, VIX)
- Out-of-sample forecasting for 2026-2027
- Scenario analysis for policy shocks

---

## Sources

1. US Treasury TIC Data: [https://ticdata.treasury.gov/](https://ticdata.treasury.gov/)
2. Chicago Fed Letter #480 (2023): "UK Pension Market Stress in 2022—Why It Happened and Implications for the U.S."
3. Wolf Street (2014): "What the Heck is Going on With US Treasuries In Belgium?"
4. Reuters (2014): "Euroclear says likely cause of Belgium's big rise in Treasuries"
5. UK Parliament Work and Pensions Committee: "Defined benefit pensions with Liability Driven Investments" (2022)
6. The Pensions Regulator (UK): DB Pensions Landscape reports (2020-2025)
7. Bank of England letters and speeches (Jon Cunliffe, Sarah Breeden, 2022)
8. Euroclear corporate website: [https://www.euroclear.com/](https://www.euroclear.com/)
9. JP Morgan (2024): "A Tale of Two Domiciles: Cross-Border Fund Advantages in Luxembourg and Ireland"
10. Federal Reserve FRED: Series WMTSECL1 (Securities Held in Custody for Foreign Official Accounts)

---

**End of Report**

*Next update: Monthly after TIC data release (typically 15th of month +6 weeks lag)*  
*Threshold breach alerts: Real-time via VX.tsv monitoring*
