# RP-MARCO-MBS_BASELINE.md
**Research Package: Municipal Bond Spread Baseline for Border Cities**  
**Domain:** MARCO (Immigration & Labor Supply)  
**Date:** 2026-02-09  
**Status:** BASELINE RESEARCH

---

## Executive Summary

This document establishes baseline research protocols for monitoring municipal bond market stress in border-dependent cities. Focus: fiscal exposure transmission from immigration enforcement/labor supply shocks → municipal creditworthiness.

**Target Cities:** El Paso (TX), Pharr (TX), McAllen (TX), Nogales (AZ), Imperial County (CA)

---

## 1. EMMA Data Access Protocol

### Primary Source
**EMMA (Electronic Municipal Market Access)**  
- **URL:** https://emma.msrb.org/
- **Operator:** Municipal Securities Rulemaking Board (MSRB)
- **Status:** SEC-designated official repository for municipal securities data
- **Access:** Free public access, no subscription required

### Key Features
- Official statements (bond prospectuses)
- Ongoing disclosure documents
- Credit ratings from Moody's, S&P, Fitch
- Trade prices, yields, historical trading data
- Material event notices (ratings changes, defaults, covenant breaches)

### Search Methods
1. **By Issuer:** Search city/county name → Homepage → Outstanding bonds
2. **By CUSIP:** Direct bond lookup if identifier known
3. **Advanced Search:** Filter by state, maturity, rating, size

### Relevant Data Points
- **Spread to AAA benchmark:** Current yield minus AAA muni yield (BVAL Muni AAA Yield Curve)
- **Recent trades:** Last 10 trades, avg price/yield
- **Rating history:** Moody's/S&P actions, outlook changes
- **Disclosure filings:** Annual financials, budget updates, material events

---

## 2. Target Cities — Current Bond Profile

### El Paso, Texas
- **Profile:** Border city, 680k population, significant trade/immigration flows
- **EMMA Search:** "City of El Paso, Texas"
- **Key Bonds:** General obligation bonds, water/sewer revenue bonds
- **Baseline Status:** Research general obligation bonds with 10+ year maturity
- **Current Spread:** [TO BE MONITORED — baseline not yet established]

### Pharr, Texas
- **Profile:** Hidalgo County border city, 100k population, Pharr-Reynosa International Bridge
- **EMMA Search:** "City of Pharr, Texas"
- **Key Bonds:** General obligation, certificates of obligation
- **Baseline Status:** [TO BE MONITORED]

### McAllen, Texas
- **Profile:** Hidalgo County seat, 143k population, major border crossing
- **EMMA Search:** "City of McAllen, Texas"
- **Key Bonds:** General obligation bonds
- **Baseline Status:** [TO BE MONITORED]

### Nogales, Arizona
- **Profile:** Santa Cruz County, 20k population, Nogales port of entry (major produce gateway)
- **EMMA Search:** "City of Nogales, Arizona"
- **Key Bonds:** General obligation, industrial development bonds
- **Baseline Status:** [TO BE MONITORED]

### Imperial County, California
- **Profile:** Border county, 180k population, heavy agricultural dependence
- **EMMA Search:** "County of Imperial, California"
- **Key Bonds:** General obligation, lease revenue bonds
- **Baseline Status:** [TO BE MONITORED]

---

## 3. Spread Thresholds (Basis Points vs AAA Benchmark)

### GREEN: <100bp
- **Status:** Normal market conditions
- **Interpretation:** No significant fiscal stress signal
- **Action:** Routine monitoring

### YELLOW: 100-200bp
- **Status:** Elevated caution
- **Interpretation:** Market pricing modest fiscal risk or liquidity concerns
- **Action:** Weekly monitoring; check for recent disclosure filings

### ORANGE: 200-350bp
- **Status:** Significant stress
- **Interpretation:** Market pricing material fiscal deterioration; possible ratings watch
- **Action:** Daily monitoring; cross-reference with H-2A visa data, remittance flows, local employment reports

### RED: >350bp
- **Status:** Severe distress
- **Interpretation:** Market pricing default risk or imminent rating downgrade
- **Action:** Immediate escalation to PROME; full diagnostic across VX vectors

---

## 4. Credit Rating Baseline

### Rating Agency Sources
- **Moody's:** Available on EMMA bond pages (Ratings tab)
- **S&P Global Ratings:** Available on EMMA bond pages
- **Fitch Ratings:** Less common for smaller munis

### Rating Scale (Investment Grade)
- **Aaa/AAA:** Highest quality
- **Aa/AA:** High quality
- **A/A:** Upper-medium grade
- **Baa/BBB:** Lower-medium grade (lowest investment grade)

### Watch List Indicators
- **Negative Outlook:** Rating agency signals potential downgrade within 12-24 months
- **Review for Downgrade:** More urgent; decision expected within 90 days
- **Watch List:** Formal monitoring due to fiscal stress or external shock

### Monitoring Protocol
- Check EMMA for "Rating Change Notices" under each issuer
- Set up Google Alerts for: `"[City Name] municipal bonds rating"`
- Cross-reference with Moody's/S&P press releases (public access)

---

## 5. Data Update Cadence

### Weekly (Normal Conditions)
- Check EMMA for new disclosure filings
- Note any spread widening >25bp week-over-week
- Review recent trades (if <5 trades/month, note illiquidity)

### Daily (Yellow/Orange Status)
- Monitor spreads for acceleration
- Check for material event notices
- Cross-reference with VX-MARCO vectors (H-2A, remittances, state fiscal)

### Real-Time (Red Status)
- Continuous EMMA monitoring
- Immediate correlation with policy shocks (ICE raids, H-2A suspensions, border closures)
- Coordinate with LABOR/REGINALD for transmission mapping

---

## 6. Benchmark Comparison

### AAA Municipal Yield Curve
- **Source:** BVAL (Bloomberg Valuation) AAA Muni Curve on EMMA
- **Alternative:** S&P Municipal Bond Index (AAA-rated)
- **Use:** Subtract AAA yield from target city yield = spread (basis points)

### Example Calculation
- **El Paso 10-year GO bond yield:** 4.25%
- **AAA 10-year muni yield:** 3.50%
- **Spread:** 75bp (GREEN)

---

## 7. Limitations & Caveats

### Market Liquidity
- Smaller border city bonds trade infrequently (monthly or less)
- Wide bid-ask spreads during low liquidity = noisy signal
- Illiquidity ≠ distress, but can amplify stress signals

### Confounding Factors
- **Federal policy:** Fed rate changes affect all munis
- **State fiscal health:** Texas/Arizona/California budget stress affects local credits
- **Sector-wide shocks:** Pension crises, natural disasters

### Cross-Validation Required
- Bond spreads are **lagging indicators**
- Must correlate with:
  - H-2A visa issuance data (VX-MARCO-01)
  - Remittance flows (VX-MARCO-03)
  - Local employment data (LABOR domain)
  - State budget stress (VX-MARCO-05)

---

## 8. Recent Market Context (2025-2026)

### General Municipal Market
- **2026 Outlook (Schwab):** Stable demand for tax-exempt income; supply constraints
- **Risks:** Federal budget consolidation, potential reduction in state/local aid
- **Texas Border Cities:** Heightened sensitivity to immigration policy changes post-2024 election

### H-2A Program Delays (Dec 2025)
- **Source:** Florida farmer reports (Dec 2025)
- **Issue:** Government shutdown delayed 2026 Adverse Effect Wage Rate publication
- **Impact:** Harvest delays → potential local sales tax revenue declines in border ag-dependent counties

### Border City Fiscal Exposure
- **Texas cities:** Property tax base tied to trade/logistics; sales tax from cross-border retail
- **Arizona/California:** Agricultural sector reliance on H-2A labor; sales tax from seasonal spending

---

## 9. Next Steps

1. **Establish Baseline Spreads:**
   - Pull current 10-year GO bond yields for all 5 targets from EMMA
   - Record AAA benchmark yield
   - Calculate initial spread (bp)
   - Log to VX.tsv (Vector Tracking)

2. **Set Up Monitoring:**
   - Weekly EMMA checks (Friday close)
   - Google Alerts for rating actions
   - Sync with CALENDAR.md for policy catalysts (court rulings, H-2A deadlines)

3. **Integration with VX-MARCO:**
   - Link MBS spread data to VX-MARCO-06 (Municipal Bond Spreads)
   - Cross-reference with VX-MARCO-01 (H-2A Issuance)
   - Flag threshold breaches in STATUS.md

4. **Coordination with LABOR/REGINALD:**
   - If spreads move to ORANGE: Alert LABOR for employment data dive
   - If spreads move to RED: Alert REGINALD for regional bank exposure to muni portfolios

---

## 10. Sources & References

- **EMMA:** https://emma.msrb.org/
- **SEC Investor Guidance:** https://www.investor.gov/introduction-investing/getting-started/researching-investments/using-emma-researching-municipal
- **MSRB Glossary:** http://msrb.org/glossary.aspx
- **Schwab 2026 Muni Outlook:** https://www.schwab.com/learn/story/municipal-bond-outlook
- **Raymond James Bond Commentary (Feb 2026):** Weekly municipal bond investor reports

---

**Status:** Baseline framework established. Awaiting initial spread data collection to populate VX-MARCO-06.

**Next Action:** Pull current bond yields from EMMA for all 5 target cities and establish GREEN/YELLOW/ORANGE/RED baseline.
