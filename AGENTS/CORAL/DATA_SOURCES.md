# CORAL Data Sources
## Where to Get Florida Real Estate Stress Data

---

## Research Archive

### SBCF Research (Feb 11, 2026)

**Location:** `sources/SBCF_Research_Feb2026/`

| File | Content | Key Finding |
|------|---------|-------------|
| SBCF_Earnings_Call_Q4_2025.md | Full transcript | Management bullish, 3 bps NCOs |
| SBCF_Condo_Crisis_Exposure.md | HOA lending analysis | Counter-cyclical strategy, lending INTO crisis |
| SBCF_Portfolio_Composition.md | Loan book breakdown | 47% CRE, 216% concentration, granular |
| SBCF_Credit_Quality.md | 8-quarter credit trends | NPLs 0.57%, exited fintech book |
| SBCF_MA_Analysis.md | M&A target viability | 80% institutional, takeout risk |
| SBCF_Capital_Regulatory.md | Capital & regulatory | 14.4% Tier 1, no MOUs, Fed waiver granted |
| SBCF_Deposit_Stability.md | Deposit analysis | Top 10 = 3%, 167% liquidity coverage |
| FL_Bank_Comparison_SBCF_ABCB_HOMB.md | Peer comparison | SBCF most FL-concentrated but strongest |
| FL_Bank_Concentration_Rankings.md | FL exposure rankings | SBCF ~100%, BKU ~47%, VLY 27% |

**Conclusion:** SBCF is NOT a short target. Fortress balance sheet, M&A target risk.

---

## Primary Sources

### Regulatory & Government

| Source | Data | URL | Update Frequency |
|--------|------|-----|------------------|
| **DBPR (FL Dept of Business & Professional Regulation)** | Condo complaints, SIRS database, building reports | https://condos.myfloridalicense.com/ | Ongoing |
| **OIR (Office of Insurance Regulation)** | Insurer stability reports, market share, enhanced monitoring | https://floir.gov/ | Monthly |
| **Citizens Property Insurance** | Policy counts, depopulation, market share reports. **⚠️ Scope rule (7/21): use the policies-in-force DETAIL reports (`citizensfla.com/policies-in-force`) which split personal vs commercial — press paraphrases mislabel totals as "personal" (KB ML-CORAL-035). Depop rounds → `/depopulation-resources`** | https://www.citizensfla.com/policies-in-force | ~Weekly/monthly |
| **FHCF (FL Hurricane Catastrophe Fund)** | Fund balance, bonding capacity | https://fhcf.sbafla.com/ | Quarterly |
| **FIGA (FL Insurance Guaranty Association)** | Assessments, companies in receivership | https://figafacts.com/ | As needed |
| **FL DFS (Dept of Financial Services)** | Companies in receivership | https://myfloridacfo.com/division/receiver/companies | As needed |

### Market Data

| Source | Data | URL | Update Frequency |
|--------|------|-----|------------------|
| **Florida Realtors** | Inventory, sales, pricing by county (June release verified pub ~7/17 — ~3rd week for prior month) | https://www.floridarealtors.org/ | Monthly |
| **Parcl Labs — Motivated Seller Index map** | Metro/county MSI, % price cuts, % below purchase (the MSI tripwire pull source; metro-level all-seller ≠ builder cells) | https://www.parcllabs.com/research/motivated-sellers/map | Daily map; pull dated snapshots |
| **Zillow ZHVI — FL statewide** | Typical home value (repeat-value stock index; carries the cycle-low marker vs mix-sensitive medians) | https://www.zillow.com/home-values/14/fl/ | Monthly (~3rd week) |
| **NHC advisories** | Active-storm truth: use the full public advisory (MIATCPAT#) not just the outlook (MIATWOAT) — the outlook omits track/intensity (7/21 Bertha lesson) | https://www.nhc.noaa.gov/ | Live in season |
| **Miami Realtors** | Southeast FL specific data | https://www.miamirealtors.com/ | Monthly |
| **ATTOM Data** | Foreclosure rates, REO, delinquencies | https://www.attomdata.com/ | Monthly |
| **Cotality (fka CoreLogic)** | Delinquency trends | https://www.cotality.com/ | Monthly |

### Bank Filings

| Bank | Ticker | IR Page | Key Filings |
|------|--------|---------|-------------|
| **Valley National Bank** | VLY | https://www.valley.com/investor-relations | 10-Q, 10-K, Earnings presentations |
| **Seacoast Banking** | SBCF | IR page | 10-Q, 10-K |
| **BankUnited** | BKU | IR page | 10-Q, 10-K |
| **Popular Inc** | BPOP | IR page | Association lending data |

### Research & Analysis

| Source | Data | URL | Notes |
|--------|------|-----|-------|
| **TD Economics** | FL condo market analysis, blacklist estimates | https://economics.td.com/ | Periodic reports |
| **Florida Policy Project** | Condo crisis research, at-risk estimates | https://floridapolicyproject.com/ | Research papers |
| **Artemis.bm** | Reinsurance pricing, cat bond market | https://www.artemis.bm/ | Ongoing |
| **Insurance Journal** | FL insurance news, carrier actions | https://www.insurancejournal.com/ | Daily |

---

## Key Reports to Track

### Monthly

| Report | Source | What to Look For |
|--------|--------|------------------|
| OIR Stability Report | OIR | Enhanced monitoring list changes |
| Citizens Market Share | Citizens | Policy count, TIV trends |
| FL Residential Market Share | OIR | Private carrier health |
| ATTOM Foreclosure Report | ATTOM | FL ranking, starts, completions |

### Quarterly

| Report | Source | What to Look For |
|--------|--------|------------------|
| VLY Earnings | VLY IR | Non-accruals, FL CRE, HOA lending |
| SBCF Earnings | SBCF IR | FL-specific stress |
| FHCF Bonding Capacity | FHCF | Cat fund health |

### Annual / Periodic

| Report | Source | What to Look For |
|--------|--------|------------------|
| DBPR Complaint Data | DBPR | YoY complaint trends |
| FL Policy Project Reports | FPP | At-risk association estimates |
| TD Economics FL Condo | TD | Blacklist updates, market analysis |

---

## Data Gaps (Known Limitations)

| Data Point | Issue | Workaround |
|------------|-------|------------|
| **Fannie/Freddie Blacklist** | Confidential, not public | Media reports, TD Economics estimates |
| **Association Bridge Loans** | Private contracts, not reported | Proxy via bank HOA lending data |
| **Condo vs SFR Delinquency** | Not broken out at county level | Use overall FL trends |
| **Real-time Receiverships** | County-by-county, no central registry | Monitor major cases manually |
| **Small Building Compliance** | <3 stories exempt from inspections | Data gap, limited visibility |

---

## Search Queries for Monitoring

### Google Alerts (Suggested)

```
"Florida condo" AND ("bankruptcy" OR "receivership" OR "special assessment")
"Florida insurance" AND ("insolvency" OR "liquidation" OR "OIR")
"Valley National" AND "Florida"
"Fannie Mae" AND "condo" AND "Florida"
"FIGA" AND "assessment"
site:floir.gov "enhanced monitoring"
site:citizensfla.com "depopulation"
```

### SEC EDGAR Searches

```
VLY 10-Q Florida
VLY 8-K
SBCF 10-Q
BKU 10-Q Florida
```

---

## Court Dockets (Major Cases)

| Case | Court | Status | Significance |
|------|-------|--------|--------------|
| **Heron Pond Receivership** | Broward Circuit (CACE 24-005243) | Auction completed? | Valuation benchmark |
| **Biscayne 21 (Avila v TRD)** | FL Supreme Court | Declined review Oct 2025 | Termination precedent |
| **Palm Greens Bankruptcy** | Bankruptcy Court | Chapter 11 active | First association bankruptcy |
| **Grenadier Lakes v City National** | TBD | Active | Origination quality |

---

## API / Data Feeds (If Available)

| Source | Access | Notes |
|--------|--------|-------|
| ATTOM | Paid API | Foreclosure data |
| Zillow/Redfin | Public | Inventory trends (limited for condos) |
| FRED | Free | Macro indicators, FL employment |

---

## Update Checklist

### Weekly
- [ ] Check Insurance Journal for FL carrier news
- [ ] Check Artemis for reinsurance updates
- [ ] Google News search for FL condo bankruptcy/receivership

### Monthly
- [ ] Pull OIR market share report
- [ ] Check Citizens policy count
- [ ] Review ATTOM foreclosure data
- [ ] Update VX_Vectors with new data

### Quarterly
- [ ] Bank earnings (VLY, SBCF, BKU)
- [ ] FHCF capacity report
- [ ] Update ML_Master_Log with key events

---

## Contact Points (For Deep Research)

| Entity | Contact | Purpose |
|--------|---------|---------|
| DBPR Condo Division | Public records request | Complaint details |
| OIR Consumer Services | Public inquiry | Insurer status |
| County Clerk of Courts | Docket search | Receivership filings |
| Avison Young (Heron Pond) | Press contact | Auction results |

---

*Last Updated: 2026-02-05*
