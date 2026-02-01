# MARCO Research Session: Alternative Migration Data Sources

**Purpose:** Investigate alternative data sources to improve migration measurement accuracy
**Priority:** HIGH — Migration data is currently one of MARCO's weakest evidence areas
**Estimated Scope:** Full research session

---

## CONTEXT FOR CLAUDE

You are MARCO (Migration And Regional Change Observer). Your thesis tracks population movement disruptions creating regional economic stress. Current migration data relies heavily on:
- Census Bureau (12-24 month lag)
- CBO projections (models, not measurements)
- Moving company surveys (UVL, U-Haul) — partial samples only

**Problem:** We can't confidently measure real-time migration. This research session aims to identify and evaluate alternative data sources.

**Key states of interest:** Florida, Texas, California, Nevada, Arizona

---

## RESEARCH PLAN

### Phase 1: IRS Migration Data (HIGH PRIORITY)

**What:** IRS publishes county-to-county migration data based on tax return address changes.

**Tasks:**
1. Go to: https://www.irs.gov/statistics/soi-tax-stats-migration-data
2. Download the most recent state-to-state and county-level migration files
3. Extract data for FL, TX, CA, NV, AZ for all available years
4. Calculate:
   - Net migration by state (inflows - outflows)
   - Top origin states for FL/TX inflows
   - Top destination states for FL/TX outflows
   - Year-over-year trend (is FL inflow slowing?)
5. Note the most recent year available and the lag

**Output:** Create ML entry with baseline IRS migration data and trend analysis

---

### Phase 2: Credit Bureau Migration Reports

**What:** Equifax and other credit bureaus publish migration reports based on address changes in credit files. Near real-time.

**Tasks:**
1. Search: "Equifax migration report 2025" "Equifax migration trends Florida"
2. Search: "TransUnion migration data" "Experian population migration"
3. Search: "credit bureau migration Florida Texas 2025"
4. Look for:
   - Quarterly migration reports
   - State-level inflow/outflow data
   - Any FL or TX specific analysis
5. If reports found, extract key metrics and compare to moving company data

**Output:** Create ML entry documenting credit bureau data availability and findings

---

### Phase 3: Florida DMV / License Data

**What:** When people move to Florida, they must get a FL driver's license within 30 days. Out-of-state license transfers = direct migration measurement.

**Tasks:**
1. Search: "Florida DHSMV license statistics" "Florida driver license transfers out of state"
2. Search: "Florida new driver licenses issued 2024 2025"
3. Check: https://www.flhsmv.gov/resources/statistics/
4. Look for:
   - Monthly/quarterly new license issuances
   - Breakdown by transfer vs. new (transfers = migrants)
   - Any reporting on origin states
5. If not publicly available, note whether FOIA/public records request would be appropriate

**Output:** Document what's available and create FL entry if promising data exists

---

### Phase 4: School Enrollment Data

**What:** Family migration shows up in school enrollment. If families are leaving FL, school districts should see enrollment declines.

**Tasks:**
1. Search: "Florida school enrollment 2024 2025" "Florida DOE enrollment statistics"
2. Check: Florida Department of Education data portal
3. Search: "Miami-Dade school enrollment decline" "Broward school enrollment"
4. Look for:
   - Statewide enrollment trends
   - District-level data for South FL (Miami-Dade, Broward, Palm Beach)
   - Comparison to pre-pandemic baseline
5. Same for Texas: "Texas school enrollment 2024 2025"

**Output:** Create ML entry with school enrollment trends as migration proxy

---

### Phase 5: Cell Phone Mobility Studies

**What:** Companies like SafeGraph, Placer.ai, Unacast track phone location data. Academics and journalists use this for migration research.

**Tasks:**
1. Search: "cell phone mobility data migration Florida 2024 2025"
2. Search: "SafeGraph migration study" "Placer.ai population movement"
3. Search academic sources: Google Scholar for "internal migration United States 2024 mobility data"
4. Look for:
   - Recent papers or articles using mobility data for FL/TX/Sunbelt migration
   - Any findings on pandemic migration reversal
   - Methodology notes (how reliable is this data?)

**Output:** Document any studies found and extract relevant findings

---

### Phase 6: Additional Sources Check

**Quick searches for each:**

| Source | Search Query |
|--------|-------------|
| Medicare/Medicaid enrollment | "Medicare enrollment by state 2024 2025 Florida" |
| Professional licenses | "Florida medical license applications out of state 2024" |
| Utility hookups | "Florida Power Light new connections 2025" "Duke Energy Florida new customers" |
| Property buyer origin | "Redfin migration report 2025" "Zillow buyer origin Florida" |
| Apartment applications | "RentCafe migration report" "Apartment List migration 2025" |
| Voter registration | "Florida voter registration new 2024 2025" |

**For each:** Note if data exists, accessibility, and potential value

---

## OUTPUT REQUIREMENTS

### For Each Source Investigated:

Create a summary with:
1. **Source name and URL**
2. **Data availability:** What's actually accessible?
3. **Coverage:** Who/what does it capture?
4. **Timeliness:** How current is the data? What's the lag?
5. **FL/TX relevance:** Does it have state-level or regional breakdowns?
6. **Key findings:** If data obtained, what does it show?
7. **Limitations:** What are the caveats?
8. **Recommendation:** Should MARCO track this ongoing?

### Workbook Updates:

1. **Create ML entries** for each valuable source discovered
2. **Create FL entries** for any recurring data releases worth tracking
3. **Update VX-MARCO-3.03** (Florida Net Domestic Migration) notes if new sources improve measurement

### Summary Document:

Create a synthesis document ranking the sources by:
- Value (how much does this improve our measurement?)
- Accessibility (how easy to obtain ongoing?)
- Timeliness (how current?)

---

## SUCCESS CRITERIA

This session is successful if we:
1. Obtain IRS migration baseline data for FL/TX
2. Identify at least 2 additional near-real-time sources
3. Determine whether FL DMV data is accessible
4. Document all sources for future tracking
5. Improve confidence in migration measurement capability

---

## FILES TO UPDATE

- `MARCO WORKBOOK (TSV)/ML.tsv` — New entries for each source
- `MARCO WORKBOOK (TSV)/FL.tsv` — New catalysts for recurring releases
- `MARCO WORKBOOK (TSV)/VX.tsv` — Update VX-3.03 notes if warranted
- Create summary: `RESEARCH_OUTPUTS/MIGRATION_DATA_SOURCES_ASSESSMENT.md`

---

## AFTER COMPLETION

Update the operational skeleton to note improved migration data sources and revised confidence in migration vectors.

If findings are significant, send a SIGNAL to CARL inbox noting any consumer-relevant migration insights.

---

*Research prompt created: 2026-01-22 (Session 7)*
*Use with fresh context window*
