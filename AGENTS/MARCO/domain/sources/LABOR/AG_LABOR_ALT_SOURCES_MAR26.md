# Alternative Ag Labor Data Sources — Replacing Canceled Federal Surveys
*Generated 2026-03-26 | MARCO Framework*

---

## What Was Lost

### NASS Farm Labor Survey (Agricultural Labor Survey) — **CANCELED**
- **Date:** August 28, 2025. NASS announced discontinuance; Federal Register notice September 3, 2025.
- **Rationale given:** "Deemed duplicative and/or no longer necessary" under Paperwork Reduction Act.
- **What it measured:** Quarterly hired farm worker counts, hours worked, and average hourly wage rates (field, livestock, all hired workers) — the *only* employer-side survey of ag labor in the U.S.
- **Last report:** May 2025 (covering January & April 2025 reference weeks). No November 2025 report was produced.

### NAWS (National Agricultural Workers Survey) — **EFFECTIVELY DEFUNCT**
- **Status:** The DOL/ETA NAWS page returns a challenge wall. The public data site (naws.jbsinternational.com) shows data only through FY2014. No new survey waves have been published since the mid-2010s at the latest, and the program appears defunded under broader DOL cuts.
- **What it measured:** Worker-side demographics, employment conditions, wages, health, immigration status of crop workers via face-to-face interviews.

**Net effect:** The U.S. now has zero dedicated federal surveys measuring agricultural labor supply, demand, wages, or workforce composition from either the employer or worker side.

---

## Replacement Data Sources

### 1. DOL OFLC H-2A Disclosure Data ⭐ PRIMARY
- **URL:** https://www.dol.gov/agencies/eta/foreign-labor/performance (disclosure files) and https://flag.dol.gov/programs/h-2a
- **Frequency:** Quarterly disclosure files + real-time job order database
- **What it measures:** Every H-2A temporary agricultural labor certification — employer name, location, crop/activity, number of positions requested & certified, offered wage rate, dates of need. This is *administrative data*, not a survey, so it can't be canceled by budget cuts.
- **Currency:** Quarterly files typically lag ~1 quarter. Job order database is near-real-time.
- **Why it matters:** H-2A usage is the best available demand signal for ag labor. Rising certifications = domestic labor shortage. The Adverse Effect Wage Rate (AEWR) published for H-2A sets a floor and proxies market wages. H-2A positions certified have grown from ~150K (2015) to ~370K+ (2024) — this trend *is* the labor story.

### 2. BLS Quarterly Census of Employment & Wages (QCEW) — NAICS 11 ⭐ PRIMARY
- **URL:** https://www.bls.gov/qcew/
- **Frequency:** Quarterly (5-month lag)
- **What it measures:** Employment counts and average weekly wages for Agriculture (NAICS 11) by state and county, derived from employer UI tax filings. Covers all employees on payroll, not just hired farm workers.
- **Currency:** Q2 2025 data likely available by ~Nov 2025. Always ~5 months behind.
- **Why it matters:** Administrative data (can't be surveyed away). State-level granularity lets us track regional labor tightness. Wage trends here directly replace the NASS wage series, though with more lag.

### 3. USDA NASS Crop Progress Reports ⭐ PRIMARY
- **URL:** https://usda.library.cornell.edu/concern/publications/8336h188j and https://quickstats.nass.usda.gov/
- **Frequency:** Weekly during growing season (April–November)
- **What it measures:** % of crop planted, emerged, harvested by state. Crop condition ratings.
- **Status:** Still active as of March 2026. Was NOT included in the August 2025 discontinuance.
- **Why it matters as labor proxy:** Harvest delays (% harvested running behind 5-year average) can signal labor constraints. Comparing planting progress vs. weather conditions — if weather is fine but planting lags, labor is the bottleneck. Not a direct labor measure, but the best weekly signal available.

### 4. State Department H-2A Visa Issuance Data
- **URL:** https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics.html
- **Frequency:** Monthly (published with ~2 month lag)
- **What it measures:** Actual H-2A visas issued at consular posts, by nationality. This is the *supply* side — how many workers actually entered, vs. OFLC data which shows how many were *requested*.
- **Why it matters:** Gap between OFLC certifications and actual visa issuances = unfilled labor demand. If certifications rise but issuances don't keep pace, that's acute shortage signal.

### 5. BLS CPI — Food at Home Sub-indices
- **URL:** https://www.bls.gov/cpi/ (Series: Fresh Fruits, Fresh Vegetables, CUSR0000SAF113, CUSR0000SAF114)
- **Frequency:** Monthly
- **What it measures:** Consumer price changes for fresh produce categories.
- **Why it matters as labor proxy:** Labor-intensive crops (berries, lettuce, tree fruit) have high labor cost share (30-50%+ of production cost). Sustained produce price spikes in absence of weather/supply disruptions → labor cost pass-through signal. Lagging indicator but confirms thesis.

### 6. USDA ERS Farm Labor Reports & Ag Prices
- **URL:** https://www.ers.usda.gov/topics/farm-economy/farm-labor/ and https://usda.library.cornell.edu/concern/publications/c821gj76b
- **Frequency:** ERS research papers (irregular); Ag Prices monthly
- **What it measures:** ERS publishes analytical pieces on farm labor markets using multiple data sources. Ag Prices report includes some wage data.
- **Status:** ERS has faced staffing cuts but still publishes. Monitor for discontinuance.

### 7. American Farm Bureau Federation (AFBF) Market Intel
- **URL:** https://www.fb.org/market-intel/
- **Frequency:** Irregular (event-driven analysis pieces)
- **What it measures:** Farm Bureau conducts member surveys and publishes analysis on labor availability, immigration policy impacts, and farm economics. Their September 2025 piece directly addressed the NASS cancellation impact.
- **Why it matters:** Industry-side qualitative/survey data. Not systematic enough to replace federal data but useful for narrative confirmation.

### 8. Academic/NGO Sources
- **UC Davis Agricultural & Resource Economics:** https://are.ucdavis.edu/ — Philip Martin's research group tracks ag labor markets. Irregular but high quality.
- **Farmworker Justice:** https://www.farmworkerjustice.org/ — Advocacy org, publishes reports on workforce conditions.
- **National Center for Farmworker Health:** http://www.ncfh.org/ — Demographic and health data on farmworkers.
- **Frequency:** Annual reports or irregular research papers. Not suitable for regular tracking but valuable for annual framework calibration.

---

## Recommended MARCO Tracking Framework (Top 5)

| Priority | Source | Frequency | Signal Type | Replaces |
|----------|--------|-----------|-------------|----------|
| **1** | **OFLC H-2A Disclosure Data** | Quarterly + real-time | Labor demand, wages (AEWR) | NASS employer-side wage/employment data |
| **2** | **BLS QCEW NAICS 11** | Quarterly (5mo lag) | Employment counts, avg wages by state | NASS state-level employment |
| **3** | **NASS Crop Progress** | Weekly (Apr-Nov) | Indirect — harvest delays as labor proxy | No direct replacement, new signal |
| **4** | **State Dept H-2A Visa Issuances** | Monthly | Labor supply (actual arrivals vs. demand) | NAWS workforce demographics (partial) |
| **5** | **CPI Fresh Fruits/Vegetables** | Monthly | Price pass-through of labor costs | Confirmation/lagging indicator |

### Implementation Notes
- **H-2A data is the backbone.** OFLC disclosure files are downloadable CSVs. Build quarterly pull + AEWR tracking. This is the single most important replacement.
- **QCEW fills the employment gap** but with significant lag. Use for quarterly structural assessment, not real-time.
- **Crop Progress is the only weekly signal.** Build a "harvest delay index" comparing current vs. 5-year avg % harvested for labor-intensive crops (CA, FL, WA, OR).
- **Cross-reference visa issuances vs. OFLC certifications** monthly to detect supply-demand gaps.
- **Nothing replaces NAWS for worker demographics.** This is a permanent data gap. Academic studies and NGO reports are the only partial substitutes.

---

*Sources confirmed active as of March 2026 unless noted. Review quarterly for further federal data discontinuances.*
