# MARCO Migration Data Sources Assessment

**Research Session:** 7 (2026-01-22)
**Purpose:** Evaluate alternative data sources to improve migration measurement accuracy
**Result:** 6 valuable sources identified; IRS baseline established; multiple near-real-time alternatives documented

---

## EXECUTIVE SUMMARY

### Key Findings

1. **IRS Migration Data** provides the authoritative baseline (2021-2022 most recent):
   - Florida: +261,863 net individuals (+126,837 returns)
   - Texas: +182,704 net individuals (+83,136 returns)
   - California: -355,809 net individuals (largest outflow)

2. **Florida's net domestic migration collapsed** 80% from 2022 to 2024:
   - 2022: +317,923 net
   - 2023: +185,067 net
   - 2024: +63,346 net (Census Bureau)
   - Still positive but dramatically slowing

3. **Multiple near-real-time sources exist** with varying quality:
   - Moving company indices (U-Haul, UVL): Monthly/Annual, ~50% sample
   - Redfin buyer search data: Quarterly, intent not actual moves
   - Apartment List renter searches: Quarterly, renter-specific
   - Credit bureau data: Exists but not publicly accessible

4. **Florida DMV data NOT publicly accessible** for migration tracking
   - License statistics available but not transfer origin data
   - Would require FOIA request

5. **School enrollment confirms FL family outmigration**:
   - Miami-Dade: -13,059 students YoY (2024-25)
   - Statewide: -12,379 students projected (2024-25)
   - Superintendent cites "families leaving South Florida"

---

## SOURCE-BY-SOURCE ASSESSMENT

### 1. IRS SOI Migration Data

| Attribute | Value |
|-----------|-------|
| **Source** | https://www.irs.gov/statistics/soi-tax-stats-migration-data |
| **Coverage** | All tax filers (~95-98% of filers) |
| **Geography** | State-to-state, county-to-county |
| **Timeliness** | 18-24 month lag (most recent: 2021-2022) |
| **FL/TX Data** | Yes, full state pages available |
| **Cost** | Free download |

**Key Data Extracted (2021-2022):**

| State | Net Returns | Net Individuals | AGI Gained/Lost |
|-------|-------------|-----------------|-----------------|
| Florida | +126,837 | +261,863 | Top gainer |
| Texas | +83,136 | +182,704 | #2 gainer |
| N. Carolina | +40,999 | +79,317 | #3 gainer |
| California | -154,412 | -355,809 | Largest loser |
| New York | -140,246 | -267,156 | #2 loser |
| Illinois | - | -106,716 | #3 loser |

**Top Origins for Florida Inflows:** New York (largest corridor, 91K/year), New Jersey, Pennsylvania, Illinois, California

**Age Demographics:** Florida attracts OLDER migrants (55+); Texas attracts YOUNGER (60.4% ages 26-45)

**Recommendation:** TRACK ONGOING — Authoritative baseline. Update annually when new year released.

**Limitations:**
- 18-24 month lag means 2023-2024 migration shift not yet captured
- Does not capture non-filers (lower income, recent immigrants)
- AGI data may not reflect full economic impact

---

### 2. Census Bureau Population Estimates

| Attribute | Value |
|-----------|-------|
| **Source** | https://www.census.gov/newsroom/press-releases/2024/population-estimates-international-migration.html |
| **Coverage** | All residents (estimated) |
| **Geography** | State and county |
| **Timeliness** | 12 month lag (Dec 2024 release covers through Dec 2024) |
| **FL/TX Data** | Yes |
| **Cost** | Free |

**Key Data (2024 Release):**

| Metric | 2022 | 2023 | 2024 | Change |
|--------|------|------|------|--------|
| FL Net Domestic Migration | +317,923 | +185,067 | +63,346 | **-80%** |
| TX Net Domestic Migration | - | - | +85,000 | Positive |
| FL Total Pop Growth | - | - | +467,347 | 2.0% |
| FL International Migration | - | - | +411,322 | Strong |

**Critical Finding:** Florida's net domestic migration collapsed from 318K to 63K in two years. International migration (+411K) now drives FL population growth.

**Recommendation:** TRACK ONGOING — Best available for recent trends. Annual release ~December.

**Limitations:**
- Estimates, not counts
- Net figures mask gross flows (both in and out increasing)

---

### 3. Moving Company Indices

#### 3A. U-Haul Growth Index

| Attribute | Value |
|-----------|-------|
| **Source** | https://www.uhaul.com/About/Migration/ |
| **Coverage** | 2.5M+ one-way transactions annually |
| **Geography** | State and metro |
| **Timeliness** | Annual (Jan release), Midyear update |
| **FL/TX Data** | Yes, detailed |
| **Cost** | Free |

**2025 Findings:**

| State | Rank | Inbound % | YoY Change |
|-------|------|-----------|------------|
| Texas | #1 | 50.7% | +3% arrivals, +1% departures |
| Florida | #2 | 50.6% | +2% arrivals, +1% departures |
| N. Carolina | #3 | - | - |
| California | #50 (last) | - | 6th consecutive year |

**Florida City Rankings:** 8 of top 10 US growth cities are in Florida (Ocala #1)

**Recommendation:** TRACK ONGOING — Near real-time, large sample, free. BUT shows FL still positive while UVL shows "balanced."

#### 3B. United Van Lines (UVL) Study

| Attribute | Value |
|-----------|-------|
| **Source** | Annual National Movers Study |
| **Coverage** | Full-service household moves |
| **Geography** | State |
| **Timeliness** | Annual (Dec release) |
| **FL/TX Data** | Yes |
| **Cost** | Free |

**2025 Findings:**
- Florida now "BALANCED" state (52.2% inbound, 47.8% outbound)
- Dropped from "high-inbound" list (was on since 2018)
- Threshold for "high-inbound" is 55%

**Recommendation:** TRACK ONGOING — Different methodology than U-Haul captures different customer segment.

**Methodological Note:** U-Haul (DIY movers) and UVL (full-service) diverge on FL interpretation. Both show ~50-52% inbound but interpret differently. U-Haul ranks by net gain; UVL uses 55% threshold.

---

### 4. Redfin Migration Data

| Attribute | Value |
|-----------|-------|
| **Source** | https://www.redfin.com/news/migration-news/ |
| **Coverage** | ~2M Redfin.com users viewing 10+ homes |
| **Geography** | Metro-level |
| **Timeliness** | Quarterly, ~1 month lag |
| **FL/TX Data** | Yes, detailed |
| **Cost** | Free |

**Key Findings (Oct-Dec 2025):**

| Metric | Florida | Texas |
|--------|---------|-------|
| Top destinations | Sarasota (#4), Cape Coral (#5) | - |
| Miami net outflow | -67,418 (largest in US) | - |
| Primary origins | New York, Chicago | California, New York |
| Climate factor | #1 reason for FL departure | - |

**Miami-Dade Outflow:** 67,418 more people moved OUT than in — largest net outflow among 310 high-flood-risk counties analyzed.

**Recommendation:** TRACK ONGOING — Valuable for intent signals and metro-level detail. Quarterly release.

**Limitations:**
- Search intent, not actual moves
- Redfin user base skews certain demographics
- Does not capture renters

---

### 5. Apartment List Renter Migration Report

| Attribute | Value |
|-----------|-------|
| **Source** | https://www.apartmentlist.com/research/apartment-list-renter-migration-report-2025 |
| **Coverage** | Apartment List users searching for rentals |
| **Geography** | State and metro |
| **Timeliness** | Annual with quarterly updates |
| **FL/TX Data** | Yes |
| **Cost** | Free |

**Key Findings (2025):**

| State | Inbound Searches | Key Origins | Key Destinations |
|-------|------------------|-------------|------------------|
| Texas | 12.4% from CA | California, NY, IL | - |
| Florida | 4.2% from CA (down from 5.3%) | NY, NJ, IL | - |

**Florida Metro Details:**
- Miami: 33.2% outbound, 29.9% inbound (net negative)
- Tampa: 30.4% outbound, 36.1% inbound (net positive)
- Orlando: 44.4% outbound, 37.4% inbound (net negative)

**Recommendation:** TRACK ONGOING — Valuable renter-specific data, free.

**Limitations:**
- Renter-only (misses homebuyers)
- Search intent, not moves

---

### 6. Florida School Enrollment Data

| Attribute | Value |
|-----------|-------|
| **Source** | https://www.fldoe.org/accountability/data-sys/edu-info-accountability-services/pk-12-public-school-data-pubs-reports/ |
| **Coverage** | All FL public school students |
| **Geography** | State and district |
| **Timeliness** | Annual with 10-day counts |
| **FL/TX Data** | FL only |
| **Cost** | Free |

**Key Findings (2024-25):**

| District | Enrollment Change | Notes |
|----------|-------------------|-------|
| Statewide | -12,379 projected | 0.5% decline |
| Miami-Dade | -13,059 | 313K vs 326K prior year |
| Pinellas | -3,651 | 77.8K to 74.2K |
| Tampa Bay area | Declining | Larger than expected |

**Root Causes per Superintendent Dotres:**
1. Lower birth rates
2. **Families leaving South Florida**
3. Fewer new students entering country

**Context:** FL school choice program now has 13% of students in private voucher programs (highest in nation). But family departure cited as key factor.

**Recommendation:** TRACK ONGOING — Independent validation of family outmigration. Annual release.

**Limitations:**
- Conflated with school choice shifts
- Families only (misses singles, retirees)

---

### 7. Texas School Enrollment (Comparison)

| Metric | Value |
|--------|-------|
| TPS enrollment 2019 | 5,218,791 |
| TPS enrollment 2024 | 5,167,868 |
| Change | -50,923 (-1.0%) |
| Charter growth | +99,084 (+29%) |

**Texas vs Florida:** Both experiencing traditional public school enrollment decline, but Texas has stronger charter offset. Texas decline attributed more to COVID impact and birth rates; Florida decline includes explicit "families leaving" attribution.

---

### 8. Credit Bureau Migration Data

| Attribute | Value |
|-----------|-------|
| **Source** | Equifax, TransUnion, Experian |
| **Coverage** | All credit file holders |
| **Geography** | Address-change based |
| **Timeliness** | Near real-time |
| **FL/TX Data** | Likely |
| **Cost** | Not publicly accessible |

**Finding:** No public migration reports found from credit bureaus. They track address changes internally but do not publish migration reports.

**Recommendation:** DEPRIORITIZE — Data exists but not accessible without commercial relationship.

---

### 9. Florida DMV License Data

| Attribute | Value |
|-----------|-------|
| **Source** | https://www.flhsmv.gov/resources/driver-and-vehicle-reports/ |
| **Coverage** | Licensed drivers |
| **Geography** | County-level |
| **Timeliness** | Annual |
| **FL/TX Data** | FL only |
| **Cost** | Free (limited) |

**Available Data:**
- Licensed Drivers by Age, Sex and County (2006-2025)
- Motorcycle endorsements
- Insured motorist rates

**NOT Available:**
- Out-of-state license transfers
- Origin state of new FL licenses
- Departure data (licenses surrendered)

**Recommendation:** LIMITED VALUE — County-level license counts may show population shifts but origin/destination data not published. Would require FOIA.

---

### 10. Utility Connection Data

| Attribute | Value |
|-----------|-------|
| **Source** | FPL, Duke Energy Florida |
| **Coverage** | Electric service customers |
| **Geography** | Service territory |
| **Timeliness** | Quarterly (in regulatory filings) |
| **FL/TX Data** | FL only |
| **Cost** | Buried in rate filings |

**Duke Energy Florida Findings:**
- Customer growth: 1.72M (2015) → 2.01M (2024) = 1.73% annual
- Projected growth 2025-2034: 1.64% annual (SLOWING)
- Duke notes: "reversion to pre-pandemic levels, higher mortality among baby-boomers, slowing real estate market, increasing insurance costs"

**FPL:** Serves 12M+ residents, growth data in rate filings but not easily extracted.

**Recommendation:** LIMITED VALUE — Data exists in regulatory filings but not formatted for migration tracking. Duke explicitly cites insurance/real estate as growth slowdown factors.

---

### 11. Medicare Enrollment

| Attribute | Value |
|-----------|-------|
| **Source** | https://data.cms.gov/tools/medicare-enrollment-dashboard |
| **Coverage** | Medicare beneficiaries |
| **Geography** | State and county |
| **Timeliness** | Monthly |
| **FL/TX Data** | Yes |
| **Cost** | Free |

**Florida:** 5,095,344 Medicare enrollees (2nd highest after California)

**Recommendation:** MODERATE VALUE — Tracks elderly population (key FL demographic). Monthly data available. But Medicare follows residence, doesn't drive it.

---

### 12. Voter Registration

| Attribute | Value |
|-----------|-------|
| **Source** | https://dos.fl.gov/elections/data-statistics/voter-registration-statistics/ |
| **Coverage** | Registered voters |
| **Geography** | State and county |
| **Timeliness** | Monthly updates |
| **FL/TX Data** | FL available |
| **Cost** | Free |

**Florida (Nov 2025):**
- Total registered: ~13.6M
- Republican: 5,522,017 (40.8%)
- Democrat: 4,211,158 (30.7%)
- GOP lead: 1.35M (largest in FL history)

**Shift:** Dems fell from 4.9M to 4.2M while GOP grew from 4.7M to 5.5M.

**Migration Signal:** Party registration shifts could indicate partisan migration patterns (Dems leaving, GOP arriving), but confounded by party switching.

**Recommendation:** LIMITED VALUE — Available but conflates migration with party switching.

---

## SOURCE RANKING

### By Value (How much does this improve measurement?)

| Rank | Source | Value | Notes |
|------|--------|-------|-------|
| 1 | Census Bureau Net Domestic Migration | **HIGH** | Best official measure, annual |
| 2 | IRS SOI Migration | **HIGH** | Authoritative baseline, county-level |
| 3 | Moving Company Indices (U-Haul/UVL) | **HIGH** | Large samples, near real-time |
| 4 | School Enrollment | **MEDIUM-HIGH** | Family migration proxy, independent validation |
| 5 | Redfin Migration | **MEDIUM** | Intent data, metro-level, quarterly |
| 6 | Apartment List | **MEDIUM** | Renter-specific, quarterly |
| 7 | Medicare Enrollment | **LOW-MEDIUM** | Elderly tracking only |
| 8 | Credit Bureau Data | **HIGH (if accessible)** | Not publicly available |
| 9 | FL DMV Data | **LOW** | Limited public data |
| 10 | Voter Registration | **LOW** | Confounded by party switching |

### By Timeliness

| Source | Lag | Frequency |
|--------|-----|-----------|
| U-Haul Growth Index | 1 month | Annual + midyear |
| Moving company indices | 1-2 months | Annual |
| Redfin | 1 month | Quarterly |
| Apartment List | 1-2 months | Annual |
| School enrollment | 2-3 months | Annual |
| Census estimates | 12 months | Annual |
| IRS SOI | 18-24 months | Annual |

### By Accessibility

| Source | Accessibility | Format |
|--------|---------------|--------|
| Census Bureau | **Easy** | API, downloads |
| IRS SOI | **Easy** | Excel downloads |
| U-Haul | **Easy** | Press releases |
| UVL | **Easy** | Annual report |
| Redfin | **Easy** | Blog posts |
| Apartment List | **Easy** | Annual report |
| FL DOE | **Moderate** | Portal navigation |
| Medicare/CMS | **Moderate** | Dashboard |
| FL DMV | **Limited** | Basic reports only |
| Credit bureaus | **Not accessible** | Commercial only |

---

## RECOMMENDATIONS FOR MARCO

### Immediate Actions

1. **Add IRS SOI to annual tracking calendar** — Update VX-MARCO-3.03 notes with 2021-2022 baseline
2. **Add Census net domestic migration to FL catalysts** — December release is critical validation
3. **Continue tracking U-Haul and UVL** — Divergence between sources is informative (already in ML-IMG-06, ML-IMG-07)
4. **Add school enrollment tracking** — New catalyst for FL DOE annual release

### New Data Points for VX-MARCO-3.03

Current value should reflect:
- Census 2024: +63,346 net domestic (down 80% from 2022)
- IRS 2021-22: +261,863 net individuals (baseline)
- U-Haul 2025: #2 state, 50.6% inbound
- UVL 2025: "Balanced" (52.2% inbound)
- Miami-Dade: -67,418 net (Redfin, largest US outflow)

### Sources to DEPRIORITIZE

- Credit bureau data (not accessible)
- FL DMV transfer data (not published)
- Voter registration (confounded by party switching)

### FOIA Consideration

FL DMV license transfer data by origin state would be valuable. Consider FOIA request for:
- New FL licenses issued by prior state of licensure
- Annual totals by county

---

## CROSS-LINKS TO EXISTING ENTRIES

| Existing Entry | Update Needed |
|----------------|---------------|
| VX-MARCO-3.03 | Add Census 2024 data showing 80% collapse |
| ML-IMG-05 | Already notes FL lagging, add Census validation |
| ML-IMG-06 | UVL "balanced" finding — no update needed |
| ML-IMG-07 | U-Haul divergence — no update needed |
| FL-IMG-01 | Census 2025 catalyst — already exists |

---

## SUCCESS CRITERIA ASSESSMENT

| Criterion | Status |
|-----------|--------|
| 1. Obtain IRS migration baseline for FL/TX | **ACHIEVED** — 2021-22 data extracted |
| 2. Identify 2+ near-real-time sources | **ACHIEVED** — U-Haul, UVL, Redfin, Apartment List |
| 3. Determine FL DMV accessibility | **ACHIEVED** — Not accessible (origin data not published) |
| 4. Document all sources | **ACHIEVED** — This document |
| 5. Improve migration measurement confidence | **ACHIEVED** — Multiple converging sources |

---

## NEW ML ENTRIES TO CREATE

### ML-MIG-01: Census Net Domestic Migration (Florida)

**Title:** Florida Net Domestic Migration Collapse — Census 2024
**Vectors:** VX-MARCO-3.03
**Description:** Census Bureau: FL net domestic migration fell from +317,923 (2022) to +63,346 (2024), an 80% collapse. International migration (+411,322) now drives FL population growth. Total population still growing (+467,347) due to international inflows.
**Analysis:** This is the strongest official validation of the leading indicators (insurance, housing) transmitting to migration faster than the expected 12-24 month lag. The 80% collapse in two years is unprecedented for a top destination state.
**Status:** ACTIVE
**Confidence:** 90%
**Diagnostic Value:** HIGH

### ML-MIG-02: IRS Migration Baseline (2021-2022)

**Title:** IRS SOI Migration Data — Pre-Shift Baseline
**Vectors:** VX-MARCO-3.03
**Description:** IRS tax filer data (2021-2022): FL +261,863 net individuals (+126,837 returns). TX +182,704 net. CA -355,809 (largest outflow). NY→FL was second largest corridor (91K/year). FL attracted older migrants (55+); TX attracted younger (60% ages 26-45).
**Analysis:** This establishes the pre-shift baseline when FL was still the dominant destination. The IRS data has 18-24 month lag, so 2023-2024 shift not yet captured. When 2022-2023 data releases, watch for FL decline.
**Status:** ACTIVE
**Confidence:** 85%
**Diagnostic Value:** MEDIUM (baseline reference)

### ML-MIG-03: School Enrollment as Migration Proxy

**Title:** Florida School Enrollment Decline — Family Outmigration Signal
**Vectors:** VX-MARCO-3.03
**Description:** Miami-Dade lost 13,059 students in first 9 days of 2024-25 school year vs prior year. Statewide decline of 12,379 projected. Superintendent attributes to: (1) lower birth rates, (2) families leaving South Florida, (3) fewer immigrants. State forecasters project enrollment will not return to pre-pandemic levels in next decade.
**Analysis:** Independent validation of family outmigration. School data is less confounded than moving company data (families with children are more "sticky" — they don't move casually). Miami-Dade superintendent explicitly citing departure is notable.
**Status:** ACTIVE
**Confidence:** 75%
**Diagnostic Value:** MEDIUM-HIGH

---

---

## ADDENDUM: INTERNATIONAL MIGRATION SUSTAINABILITY RESEARCH

*Added: 2026-01-22 (Session 7, continued)*

### Key Finding: Florida's International Migration Pipeline is Collapsing

The 2024 international migration (+411K) that masked Florida's domestic outflow collapse is **not sustainable**.

#### Triple Chokepoint

| Policy Change | Population Affected | FL Concentration |
|---------------|--------------------| -----------------|
| CHNV Parole Terminated (Mar 2025) | 532,000 lost status | ~80% in South FL |
| TPS Venezuela Cancelled (Oct 2025) | 350,000+ affected | 404,000 TPS holders in FL (most in US) |
| Darién Gap Closed (99% drop) | 302K→3K crossings | Pipeline to FL severed |

#### Miami-Dade Dynamics

- **2024 International:** +123,835 (highest county in US)
- **2024 Domestic:** -67,418 (highest outflow in US)
- **Net:** +56,417 (international barely offsetting domestic exodus)

If international drops 50-75%, Miami-Dade could flip to net population decline.

#### Affected Population Profile

| Origin | Est. FL Population | Status | Risk |
|--------|-------------------|--------|------|
| Venezuela | ~300,000 | TPS cancelled, CHNV ended | CRITICAL |
| Haiti | ~141,000 | TPS cancelled, CHNV ended | CRITICAL |
| Cuba | ~110,000 CHNV | Cuban Adjustment Act path | MODERATE |
| Nicaragua | ~93,000 CHNV | Parole ended | HIGH |

#### Economic Vulnerability

- 18% of Venezuelan immigrants in FL live in poverty (2x national average)
- 95% of TPS holders were employed — now lose work authorization
- 60% of FL renters pay >30% of income on housing (highest in nation)
- FL immigrant workforce: 47% of agriculture, 38% of construction, 25% of hospitality

#### Labor Market Paradox

Florida faces a **dual labor supply shock**:
1. Domestic workers leaving (insurance/affordability — MARCO thesis)
2. Immigrant workers losing status (policy — new vector)

Result: 500K+ job vacancies but policy removing workers who fill them.

#### Projection

Florida's international migration could drop **50-80%** in 2025-2026, removing the last buffer masking domestic outmigration. If both domestic AND international turn negative, Florida faces a potential **population cliff** in 2026-2027.

#### New Entries Created

- **VX-MARCO-3.04:** Florida International Migration (CRITICAL status)
- **ML-MIG-04:** Florida International Migration Pipeline Collapse
- **ML-MIG-05:** Florida Immigrant Workforce Loss — Dual Labor Supply Shock
- **FL-MIG-04:** Census International Migration (Dec 2026)
- **FL-MIG-05:** ICE/DHS Florida Deportation Data
- **FL-MIG-06:** Florida Labor Market Indicators

---

*Research completed: 2026-01-22 (Session 7)*
*Sources: IRS, Census Bureau, U-Haul, United Van Lines, Redfin, Apartment List, Florida DOE, FLHSMV, CMS, DHS, USCIS, Migration Policy Institute, TRAC Syracuse*
