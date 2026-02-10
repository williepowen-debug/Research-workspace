# STATE STRESS FRAMEWORK
**Version:** 1.0  
**Last Updated:** 2026-02-09  
**Owner:** CARL (Consumer Stress Agent)

---

## PURPOSE

Track state-level consumer stress using composite early-warning indicators. Geography matters — employment shocks hit regionally before going national, and consumer stress follows the same pattern.

**Thesis:** Multi-indicator state scoring detects stress transmission 3-6 months before it appears in national aggregates.

---

## DATA SOURCES

### 1. UNEMPLOYMENT INSURANCE CLAIMS
**What:** Initial claims + continued claims (state-level weekly)  
**Sources:**
- U.S. Department of Labor ETA (Employment & Training Administration)
  - Weekly state initial claims: https://oui.doleta.gov/unemploy/claims.asp
  - State continued claims: https://oui.doleta.gov/unemploy/DataDownloads.asp
- State workforce agency websites (faster, less revised)
- FRED (Federal Reserve Economic Data): state-level series

**Cadence:** Weekly (Thursday release)  
**Threshold Logic:**
- 🟢 GREEN: 4-week MA claims within ±15% of prior year
- 🟡 YELLOW: Claims +15-30% YoY
- 🟠 ORANGE: Claims +30-50% YoY
- 🔴 RED: Claims >50% YoY or absolute spike (e.g., FL +76%)

**Key Metric:** YoY % change + absolute level per 1,000 labor force

---

### 2. WARN NOTICES (Mass Layoff Announcements)
**What:** Employer-filed notifications of plant closures or mass layoffs (60-day advance notice required)  
**Sources:**
- State workforce agency WARN portals (primary source):
  - Florida: FloridaJobs.org WARN page
  - California: EDD WARN page
  - Texas: TWC WARN page
  - New York: NYS DOL WARN page
  - Arizona: DES WARN page
- Layoffs.fyi (tech sector aggregator)
- BLS Mass Layoff Statistics (discontinued 2013, but some states maintain)

**Cadence:** Daily/weekly (varies by state)  
**Threshold Logic:**
- Aggregate affected workers per month
- 🟢 GREEN: <5,000 affected/month (large state) or <2,000 (small state)
- 🟡 YELLOW: 5,000-10,000 (large) or 2,000-5,000 (small)
- 🟠 ORANGE: 10,000-20,000 (large) or 5,000-10,000 (small)
- 🔴 RED: >20,000 (large) or >10,000 (small) or major employer (>5% local workforce)

**Key Metric:** YoY % change in affected workers + concentration by county

---

### 3. FORECLOSURE FILINGS
**What:** Default notices, auction notices, REO filings (county recorder offices)  
**Sources:**
- ATTOM Data Solutions (commercial, most comprehensive)
- CoreLogic (commercial)
- RealtyTrac (acquired by ATTOM)
- County recorder offices (public records, state-specific):
  - Florida: Clerk of Court websites (Miami-Dade, Broward, Palm Beach, etc.)
  - California: County recorder offices
  - Texas: County deed records
- Judicial vs non-judicial states (different timelines)

**Cadence:** Monthly aggregation  
**Threshold Logic:**
- 🟢 GREEN: Foreclosures flat or declining YoY
- 🟡 YELLOW: +10-30% YoY
- 🟠 ORANGE: +30-60% YoY
- 🔴 RED: >60% YoY (e.g., FL +57% → RED)

**Key Metric:** YoY % change + absolute filings per 10,000 households

**Geographic Note:** Florida is a judicial foreclosure state (slow process) — filings today reflect stress from 6-12 months ago. Non-judicial states (TX, CA, AZ) move faster.

---

### 4. CONSUMER CREDIT DATA (State-Level Delinquencies)
**What:** Credit card, auto, mortgage delinquency rates by state  
**Sources:**
- NY Fed Consumer Credit Panel (Equifax-based, quarterly, county-level):
  - https://www.newyorkfed.org/microeconomics/hhdc
  - Download "Geographic" data files
- Experian State of Credit Reports (annual/semi-annual)
- TransUnion Industry Insights (commercial subscription)
- FDIC state-level bank data (aggregated, less granular)
- Bankrate / LendingTree consumer surveys (directional)

**Cadence:** Quarterly (NY Fed), varies by source  
**Threshold Logic (Credit Cards 30+ DQ):**
- 🟢 GREEN: <3.5% state average
- 🟡 YELLOW: 3.5-5.0%
- 🟠 ORANGE: 5.0-7.0%
- 🔴 RED: >7.0%

**Threshold Logic (Auto 60+ DQ):**
- 🟢 GREEN: <3.0%
- 🟡 YELLOW: 3.0-4.5%
- 🟠 ORANGE: 4.5-6.5%
- 🔴 RED: >6.5% (national is 6.65% → already RED)

**Key Metric:** State delinquency rate vs national average (deviation score)

---

### 5. UTILITY DISCONNECTIONS
**What:** Electric/gas/water shutoffs due to non-payment  
**Sources:**
- State public utility commission reports (varies widely):
  - California PUC: https://www.cpuc.ca.gov/ (quarterly disconnection reports)
  - Florida PSC: http://www.psc.state.fl.us/
  - New York PSC: https://dps.ny.gov/
  - Texas PUC: https://www.puc.texas.gov/
- Utility company investor filings (10-Q/10-K: "uncollectible accounts")
- National Energy Assistance Directors Association (NEADA): LIHEAP data
- Local news monitoring (mass shutoff events)

**Cadence:** Quarterly (formal reports), ad-hoc (news events)  
**Threshold Logic:**
- Baseline: 2-3% of accounts disconnected annually (normal)
- 🟢 GREEN: <3% disconnection rate
- 🟡 YELLOW: 3-5%
- 🟠 ORANGE: 5-8%
- 🔴 RED: >8% or moratorium extensions (political response to crisis)

**Key Metric:** YoY % change in disconnections + % of accounts in arrears (leading indicator)

**Note:** Winter moratoriums (many states) suppress disconnections Nov-Mar. Watch for "catch-up" spikes Apr-May.

---

### 6. SUPPLEMENTARY SIGNALS

**Medical Debt in Collections (State-Level):**
- Urban Institute Debt in America tool: https://apps.urban.org/features/debt-in-america/
- Quarterly updates, county-level resolution
- Threshold: >10% of population with medical debt in collections = stress

**Food Stamp (SNAP) Enrollment:**
- USDA FNS state-level data: https://www.fns.usda.gov/data-research
- Monthly, 2-month lag
- Threshold: +10% YoY enrollment = rising economic stress

**Eviction Filings:**
- Eviction Lab (Princeton): https://evictionlab.org/ (discontinued 2018 baseline, some metros continue)
- Local court records (varies by county)
- Threshold: >2x pre-pandemic baseline = housing stress

**Payday Loan Default Rates:**
- State banking regulator reports (limited availability)
- CFPB complaint database (directional, not comprehensive)
- Threshold: complaints spiking = stress signal

---

## COMPOSITE STRESS SCORE

### Formula

Each state receives a score from 0-100, weighted across components:

```
State_Stress_Score = (UI_Claims × 0.25) + (WARN × 0.20) + (Foreclosures × 0.20) + 
                     (Credit_DQ × 0.20) + (Utility_Disconnects × 0.15)
```

**Component Scoring (0-100):**
- 🟢 GREEN = 0-25 points
- 🟡 YELLOW = 26-50 points
- 🟠 ORANGE = 51-75 points
- 🔴 RED = 76-100 points

**Composite Thresholds:**
- **0-25:** 🟢 **GREEN** — Baseline stress, normal churn
- **26-40:** 🟡 **YELLOW** — Elevated stress, monitor closely
- **41-60:** 🟠 **ORANGE** — High stress, conversion active
- **61-100:** 🔴 **RED** — Crisis conditions, widespread distress

### Adjustments

**+10 bonus points** for any of:
- Major single-employer layoff (>5% of county workforce)
- Natural disaster in past 6 months (hurricane, wildfire, flood)
- State fiscal crisis (pension shortfall, budget cuts)
- Insurance market collapse (homeowners, auto)

**-10 points** for:
- Strong in-migration (labor supply absorption)
- Major economic development announcements (factory openings, HQs)

---

## GEOGRAPHIC COVERAGE

### Priority States (Core Tracking)

1. **Florida** 🔴 — Current canary; employment→housing transmission active
2. **California** 🟠 — Fire insurance crisis, high cost-of-living, tech layoffs
3. **Texas** 🟡 — Large population, immigration disruption, energy volatility
4. **Arizona** 🟡 — Growth slowdown, construction exposure, border effects
5. **New York** 🟠 — Labor supply>demand reversal, financial sector exposure

### Border/Metro Zones (Supplementary Tracking)

**Why metros matter:** Stress often appears in metros before statewide aggregates show it.

- **Miami-Dade, Broward, Palm Beach (FL)** — Housing stress leaders
- **Los Angeles, San Diego, Sacramento (CA)** — Fire zones, cost-of-living extremes
- **Houston, Dallas, Austin (TX)** — Energy, tech, and construction exposure
- **Phoenix (AZ)** — Construction boom/bust cycle
- **NYC, Long Island, Buffalo (NY)** — Financial sector, manufacturing decline

### Watch List States (Tier 2)

- **Georgia** — Atlanta metro tech exposure
- **Illinois** — Chicago fiscal stress, out-migration
- **Pennsylvania** — Rust belt erosion
- **North Carolina** — Banking sector exposure (Charlotte)
- **Ohio** — Manufacturing decline
- **Nevada** — Tourism/hospitality concentration (Las Vegas)
- **Michigan** — Auto industry cycle

---

## TRACKING TABLE STRUCTURE

### STATE_STRESS.tsv (Main Table)

**Columns:**
```
State | UI_Claims_YoY | WARN_Affected | Foreclosures_YoY | CC_DQ_30 | Auto_DQ_60 | Utility_Disc | Composite_Score | Status | Last_Updated | Notes
```

**Example row (do not populate yet):**
```
Florida	+42%	12,450	+57%	4.8%	7.2%	4.1%	68	🔴 RED	2026-02-09	Housing stress active; Miami-Dade leading
```

### METRO_STRESS.tsv (Supplementary)

**Columns:**
```
Metro | State | UI_Claims_YoY | Foreclosures_YoY | Evictions | SNAP_Change | Composite_Score | Status | Last_Updated | Notes
```

**Focus metros:**
- Miami-Fort Lauderdale-West Palm Beach, FL
- Los Angeles-Long Beach-Anaheim, CA
- San Diego-Chula Vista-Carlsbad, CA
- Houston-The Woodlands-Sugar Land, TX
- Dallas-Fort Worth-Arlington, TX
- Phoenix-Mesa-Chandler, AZ
- New York-Newark-Jersey City, NY-NJ-PA

---

## UPDATE CADENCE

**Weekly:**
- UI claims (every Thursday)
- WARN notices (scan state portals Friday)

**Monthly:**
- Foreclosure filings (first week of month for prior month)
- Utility disconnection news scan

**Quarterly:**
- NY Fed Consumer Credit Panel (6-8 weeks after quarter end)
- Composite score recalculation
- STATUS.md update

**Ad-Hoc:**
- Major layoff announcements (>1,000 workers)
- Natural disasters
- State policy changes (moratoriums, stimulus)

---

## INTERPRETATION GUIDELINES

### Signal Sequencing (What Leads What)

1. **WARN notices** (60 days advance) → leading indicator
2. **UI claims spike** (0-30 days post-layoff) → confirmation
3. **Utility disconnects** (30-90 days post-income loss) → early distress
4. **Credit card DQ** (60-120 days) → payment hierarchy breakdown
5. **Auto DQ** (90-180 days) → deeper stress (people hold car as long as possible)
6. **Foreclosures** (120-360 days) → lagging indicator, severe stress

**Key insight:** By the time foreclosures spike, the stress originated 6-12 months earlier. WARN + UI claims give you the early signal.

### Geographic Contagion Patterns

**Pattern 1: Border Spread**
- Stress starts in one metro, spreads to adjacent counties
- Example: Miami → Fort Lauderdale → West Palm Beach → Orlando

**Pattern 2: Industry Clustering**
- Stress hits metros with shared industry exposure simultaneously
- Example: Tech layoffs → San Francisco + Seattle + Austin together

**Pattern 3: Migration Reversal**
- High-growth states that reverse (FL, TX, AZ) hit harder — infrastructure overbuilt, speculative housing, newcomers with weak local ties

### False Positives to Avoid

- **Seasonal volatility:** UI claims spike in winter (weather, retail), dip in summer
- **One-time events:** Single large employer closure ≠ systemic stress (unless dominates local economy)
- **Reporting changes:** State methodology changes can create artificial spikes
- **Moratorium distortions:** Eviction/foreclosure/utility moratoriums suppress signals, then spike on expiration

### Confidence Levels

- **High confidence:** 3+ indicators elevated in same state within same quarter
- **Medium confidence:** 2 indicators elevated, or 1 indicator + supplementary signals
- **Low confidence:** Single indicator elevated, no corroboration

---

## TRANSMISSION TO REGINALD (Banks)

State-level stress matters for REGINALD because:

1. **Regional bank exposure:** Community banks have concentrated geographic footprints
   - FL stress → FL regional banks hit first (BANC, SBCF, etc.)
   - CA stress → Western Alliance, PacWest, etc.

2. **Asset class concentration:**
   - FL: Residential real estate, condo lending
   - CA: Commercial real estate (offices), jumbos
   - TX: Energy, small business (O&G services)
   - AZ: Construction, residential development

3. **Deposit flight risk:** States in stress see deposit outflows as consumers draw down savings → liquidity pressure on local banks

**Handoff logic:**
- CARL identifies state stress → Flags state for REGINALD
- REGINALD maps regional bank exposure to that state
- Combined: Geographic stress + Bank exposure = Targeted risk assessment

---

## RESEARCH INFRASTRUCTURE

### Data Collection Scripts (Future)
- State WARN portal scrapers (Python/Playwright)
- UI claims API pulls (DOL ETA)
- NY Fed data downloads (quarterly automation)
- Foreclosure RSS monitors (RealtyTrac, local news)

### Storage
- Raw data: `domain/workbook/data/state_stress/`
- Processed tables: `domain/workbook/STATE_STRESS.tsv`, `METRO_STRESS.tsv`
- Evidence logs: `domain/workbook/ML.tsv` (link via `Vector_Link` to state stress)

### Alerts
- Threshold breach → Auto-update STATUS.md
- 🟠 ORANGE → Flag in daily summary
- 🔴 RED → Immediate escalation to PROME → Will

---

## VALIDATION & CALIBRATION

**Backtest against known events:**
- Florida 2025-2026 (current): Does framework capture the stress we see?
- COVID shutdowns (2020): Would spikes have been detected?
- 2008 housing crisis: Would FL, CA, AZ, NV light up first?

**Calibration:**
- Adjust component weights if one signal consistently leads/lags
- Recalibrate thresholds annually based on economic regime (low-rate vs high-rate environment)

**Falsifiability:**
- If state hits 🔴 RED but no bank stress appears within 6 months → false positive, recalibrate
- If bank stress appears without state stress signal → missed indicator, add data source

---

## NEXT STEPS (Do Not Execute — Research Only)

1. ✅ Framework documented (this file)
2. ⬜ Create STATE_STRESS.tsv (structure only, no data yet)
3. ⬜ Populate for FL, CA, TX, AZ, NY using latest available data
4. ⬜ Validate FL composite score against known conditions (should be 🔴 RED)
5. ⬜ Establish baseline for other states
6. ⬜ Set up quarterly update process
7. ⬜ Cross-link to REGINALD (bank exposure mapping)

---

**Framework Status:** 🟢 DOCUMENTED — Ready for implementation
