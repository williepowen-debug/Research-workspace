# RP-ZHAO-6: Data Sources & Monitoring Reference Guide
**Source:** Gemini Deep Research  
**Date:** 2026-02-13  
**Category:** Monitoring Infrastructure

---

## Executive Summary

Comprehensive reference guide for monitoring China-linked stress across four domains:
1. **Capital Flows** (TIC, SAFE, reserves)
2. **LGFV/Banking** (provincial NPLs, ChinaBond curves, land revenue)
3. **Hong Kong Peg** (Aggregate Balance, HIBOR, Currency Board)
4. **Property** (NBS sales, developer credit)

**Key operational reality:** Much of what markets call "flow" is published with lag and partly inferred. Cadence must be mixed: daily for HK, monthly for TIC/SAFE, quarterly for provincial banking.

---

## Publication Lag Timeline

| Source | Frequency | Typical Lag |
|--------|-----------|-------------|
| **HKMA Aggregate Balance** | Daily | Near-real-time (API) |
| **HIBOR fixings** | Daily | Same-day |
| **SAFE reserves** | Monthly | ~7 days after month-end |
| **SAFE FX settlement** | Monthly | ~15 days after month-end |
| **TIC Table 5 (monthly)** | Monthly | **~1.5 months** |
| **NFRA provincial NPLs** | Quarterly | Variable (weeks) |
| **TIC SHL survey (annual)** | Annual | **8-10 months** after June 30 |

---

## CAPITAL FLOWS — Primary Sources

### TIC Data (U.S. Treasury)

| Metric | URL | Frequency | Lag |
|--------|-----|-----------|-----|
| **Major Foreign Holders (Table 5)** | https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.html | Monthly | ~1.5 months |
| **Table 5 text (attribution notes)** | https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.txt | Monthly | Same |
| **Historical file (Belgium series)** | https://ticdata.treasury.gov/Publish/mfhhis01.txt | Monthly | Same |
| **SHL Survey (Agency MBS by country)** | https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/shl2024r.pdf | Annual | 8-10 months |

**Key notes:**
- Belgium line historically included Luxembourg prior to June 2002
- Custodial attribution can be distorted by custody chains
- SHL survey = best granularity for Agency MBS, but SLOW

### SAFE (China FX Regulator)

| Metric | URL | Frequency | Lag |
|--------|-----|-----------|-----|
| **Official Reserve Assets** | https://www.safe.gov.cn/en/OfficialReserveAssets/index.html | Monthly | ~7 days |
| **FX Settlement & Sales** | https://www.safe.gov.cn/en/ForeignExchangeSettlementandSa/index.html | Monthly | ~15 days |
| **Gold reserves** | Included in Official Reserve Assets | Monthly | Same |

**Interpretation resource:**
- CFR "Backdoor Intervention" methodology: https://www.cfr.org/blog/chinas-backdoor-intervention

### Gold Reserves (Alternative)

| Source | URL | Frequency |
|--------|-----|-----------|
| **World Gold Council** | https://www.gold.org/goldhub/data/gold-reserves-by-country | Quarterly |

---

## LGFV & BANKING STRESS — Primary Sources

### Provincial NPL Data (NFRA Branches)

| Province | URL (Example) | Frequency |
|----------|---------------|-----------|
| **Guizhou** | https://www.nfra.gov.cn/branch/guizhou/view/pages/common/ItemDetail.html?docId=1182161&itemId=1928 | Quarterly |
| **Henan** | https://www.nfra.gov.cn/branch/henan/view/pages/common/ItemDetail.html?docId=1193714&itemId=1390 | Quarterly |
| **Liaoning** | https://www.nfra.gov.cn/branch/liaoning/view/pages/common/ItemDetail.html?docId=1181032&itemId=1697 | Monthly-ish |

**Alternative:** PBOC provincial branch financial operation reports (annual)
- Example Guizhou: https://guiyang.pbc.gov.cn/guiyang/113274/2025111716512860440/2024072611192040517.pdf

### ChinaBond Yield Curves

| Metric | URL | Frequency | Update Time |
|--------|-----|-----------|-------------|
| **Yield curves main** | https://yield.chinabond.com.cn/cbweb-mn/yield_main?locale=en_US | Daily | ~17:30 |
| **Local Government Bond curve** | https://yield.chinabond.com.cn/cbweb-czb-web/czb/bzcxsmDfDown?locale=en_US | Daily | ~17:30 |
| **PBOC endorsement** | https://www.pbc.gov.cn/english/130721/2025080815064687606/index.html | Daily | — |

**Use for:** LGFV spread monitoring (LGFV yield - LGB yield)

### Land-Transfer Revenue

| Level | URL (Example) | Frequency |
|-------|---------------|-----------|
| **National (MOF)** | https://gks.mof.gov.cn/tongjishuju/202512/t20251217_3979392.htm | Monthly YTD |
| **Provincial (Jilin)** | https://czt.jl.gov.cn/zwgk/czsj/202512/t20251216_3518504.html | Monthly YTD |

**Note:** No centralized province-by-province dataset. Must combine MOF national + provincial bulletins.

---

## HONG KONG PEG — Primary Sources

### HKMA Daily Monitoring

| Metric | URL | Frequency | Access |
|--------|-----|-----------|--------|
| **Aggregate Balance API** | https://apidocs.hkma.gov.hk/documentation/market-data-and-statistics/daily-monetary-statistics/daily-figures-monetary-base/ | Daily | Free API |
| **Currency Board Account** | https://www.hkma.gov.hk/eng/key-functions/money/hong-kong-currency/currency-board-account/ | Daily | Web |
| **Press Releases API** | Available via HKMA API | Event-driven | Free API |

### HIBOR (Hong Kong Interbank)

| Metric | URL | Frequency |
|--------|-----|-----------|
| **HIBOR fixings** | https://www.hkab.org.hk/en/interest-rates/hibor | Daily |

### Deposit Flows & Statistics

| Metric | URL | Frequency |
|--------|-----|-----------|
| **Monthly Statistical Bulletin** | https://www.hkma.gov.hk/eng/data-publications-and-research/data-and-statistics/monthly-statistical-bulletin/release-schedule/ | Monthly |

**Key release timing:** Sections released 3rd-6th business day after month-end (varies)

### HK IPO/Capital Markets

| Metric | URL | Frequency |
|--------|-----|-----------|
| **New Listing Statistics** | https://www.hkex.com.hk/Market-Data/Statistics/Consolidated-Reports/New-Listing-Statistics | Monthly |
| **Listing Applications** | https://www.hkex.com.hk/Listing/IPO/Landing-of-Listing-Applicant-Information | Near-real-time |

---

## PROPERTY SECTOR — Primary Sources

### NBS Real Estate Data

| Metric | URL | Frequency |
|--------|-----|-----------|
| **Press releases** | https://www.stats.gov.cn/english/PressRelease/ | Monthly |
| **Database (EasyQuery)** | https://data.stats.gov.cn/english/easyquery.htm?cn=C01 | Monthly |

**What's available:** New home sales (value/area), commercial housing sold, regional breakdowns

### Developer Credit (Not Free)

| Metric | Source | Access |
|--------|--------|--------|
| Developer bond prices | Market data (terminals) | Paid |
| Restructuring status | Exchange filings, court documents | Fragmented |
| Earnings/guidance | Issuer IR sites, exchange portals | Mixed |

---

## MONITORING CADENCE RECOMMENDATIONS

### Daily (Automate)

| Check | Why | Source |
|-------|-----|--------|
| HKMA Aggregate Balance | Peg plumbing, liquidity shocks | HKMA API |
| HIBOR fixings | HKD funding stress | HKAB |
| CU-related press releases | Convertibility Undertaking triggers | HKMA press API |

### Weekly

| Check | Why | Source |
|-------|-----|--------|
| LGFV/property credit spreads | Market pricing leads official data | ChinaBond curves + terminals |
| Bank consolidation news | Event-driven stress signals | News synthesis |

### Monthly

| Check | Why | Source |
|-------|-----|--------|
| TIC Table 5 | China + Belgium holdings | Treasury TIC |
| SAFE reserves | FX regime pressure | SAFE |
| SAFE FX settlement | Hidden intervention proxy | SAFE |
| NBS property sales | Demand pulse | NBS |

### Quarterly

| Check | Why | Source |
|-------|-----|--------|
| Provincial NPL ratios | Credit stress (slow but high signal) | NFRA branches |
| Land-transfer revenue | Fiscal capacity | MOF + provincial bulletins |

### Annual

| Check | Why | Source |
|-------|-----|--------|
| TIC SHL survey | Agency MBS by country (best decomposition) | Treasury |

---

## FREE AGGREGATORS (X/Twitter)

| Source | Handle | Focus |
|--------|--------|-------|
| **Brad Setser** (CFR) | @Brad_Setser | Reserves, capital flows, TIC analysis |
| **Michael Pettis** | @michaelxpettis | China macro, balance sheets |
| **China Beige Book** | @ChinaBeigeBook | Ground-level China data |

**Site:** https://www.chinabeigebook.com/

---

## DATA PIPELINE VISUALIZATION

```
                        LAG TIMELINE
                        ─────────────
                        
DAILY (Near-Real-Time)
├── HKMA Aggregate Balance (API)
├── HIBOR fixings
└── ChinaBond curves (~17:30)

MONTHLY (~7-45 day lag)
├── SAFE Reserves (~7 days)
├── SAFE FX Settlement (~15 days)
├── TIC Table 5 (~45 days)
└── NBS Property (~30 days)

QUARTERLY (~60-90 day lag)
└── NFRA Provincial NPLs

ANNUAL (~8-10 month lag)
└── TIC SHL Survey (Agency MBS)
```

---

## KEY INTERPRETATION NOTES

### TIC Attribution Caveats
- Holdings collected from U.S.-based custodians/broker-dealers
- Attribution distorted by custody chains
- **This is why Belgium matters** — Euroclear custody masks true ownership
- Belgium line included Luxembourg prior to June 2002

### LGFV Stress Decomposition
Three components to monitor:
1. **Funding cost** — yields/spreads (ChinaBond curves)
2. **Refinancing volume** — issuance/rollover
3. **Fiscal backstop** — land-transfer revenue, intergovernmental capacity

### HK Peg Mechanics
- CU (Convertibility Undertaking) triggers at 7.85 (weak side)
- Trigger → HKMA sells USD → Aggregate Balance falls
- AB changes → HIBOR moves → carry/forward repricing
- **Aggregate Balance is THE daily signal**

---

## WHAT'S FREE vs PAYWALLED

| Free | Paywalled/Fragmented |
|------|---------------------|
| TIC data (full) | Developer bond prices |
| SAFE reserves/settlement | Real-time LGFV quotes |
| HKMA APIs | Restructuring tracking |
| ChinaBond benchmark curves | Provincial-level granular data |
| NBS property (national) | Bloomberg/Refinitiv fields |
| Provincial NPL (effort required) | Comprehensive credit research |

---

## Status: ✅ COMPLETE

This document serves as the operational reference for ZHAO monitoring infrastructure. Key URLs and cadences validated.

**Research batch status: 8/9 COMPLETE**
- Only RP-ZHAO-8 (Counter-thesis) remaining
