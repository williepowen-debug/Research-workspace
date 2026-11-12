# United Fidelity Bank: building values against the bank's debt, and how far the borrower population reaches

Researcher: read-only public-source agent for PROME. All sources were read on 2026-11-11, about 20:30 to 21:40 ET.
Tags: VERIFIED (read at the record) · INFERRED · SEARCH-NOT-FOUND (a statement about my search, not proof of absence) · UNKNOWN.
Working files are in this folder. They are `matched_properties.csv` (one row per matched property, all fields), `hmda_groups.csv`, `recon.json`, `prop_debt.json`, `fl_matched_parcels.csv`, `hamilton_pop.csv`, `hamilton_apts.csv`, `marion_pop.csv`, `franklin_pop.csv`, `franklin_owners.csv`, `nc_pop.csv` and `ucc_details_NEW_CITY_PLA.json`; the scripts are in `scripts/`.

## Six-line answer

1. **On the one public marker available, the debt is well above the buildings' value.** I matched 23 property rows (25 complexes) at strong or probable grade that have a county value. They carry **$1,336.3M** of United Fidelity (UFB) HMDA originations against **$865.0M** of current county market/assessed value. That is **1.54× the county value**, a **$471.4M gap**.
2. **The bank's own origination values sat about 85% above the county figures.** Its HMDA property values for the same rows total **$1,572.6M**, so the loans were written at **85.0%** combined loan-to-value. The county values equal only **55%** of the bank's values (FL 53%, IN 50%, OH 52%, NC 69%). A county assessor's value is not an appraisal, and both readings are rough, so the true position lies somewhere between "about 85% loan-to-value" and "about 154%". **Neither number is a measured current market value.**
3. **Purchase prices are almost entirely missing from public parcel data.** Florida's statewide roll carries no sale on these parcels, Hamilton County IN publishes no price, and Franklin County OH shows only the January 2025 re-titlings at $0. The one price found is Naples, **$24.0M in November 2020** (press snippet), against UFB debt of **$27.04M** (1.13×). For everything else, HMDA property value is the best available proxy for price.
4. **Population: about 46% of UFB's HMDA multifamily dollars tie to a parcel owned by one of the two address groups, at any grade.** Pedcor-addressed owners hold **$847.6M (20.3%)**: $705.4M probable or better and $142.2M weak. The 8902 N Meridian group holds **$977.1M (23.4%)**: $550.7M probable or better and $426.4M weak. A co-owned property (Springmill, Pedcor partnership plus a "New ___" LLC) accounts for **$71.7M (1.7%)**, and Cypress West, whose sponsor is unknown, for **$42.8M (1.0%)**. **$2,236.6M (53.6%) is unmatched.** That includes all of Georgia ($509.5M) and Colorado ($446.5M), which I did not search.
5. **The 8902 N Meridian group is larger than the 14-property sample suggested, and it is very likely Birge & Held.** Marion County IN owner records at that suite read "AVONDALE MEADOWS LP, %BIRGE & HELD" and "NEW MAXWELL LLC, %BH MAXWELL LLC" (VERIFIED in the records; the identity of the group is INFERRED). The group owns about 33 apartment complexes across the counties I searched. 11 tie to UFB loans at probable grade or better, and about 8 more weakly.
6. **A new lien fact: UFB's parent holding company is itself a secured lender to one of the 8902 group's properties.** New City Place LLC, a 111-unit complex in Gainesville FL built in 2021, has two UCC-1s naming UFB and a third naming **Fidelity Federal Bancorp** (770 3rd Ave SW, Carmel), all filed 2022-06-16 (VERIFIED, Florida UCC registry). No other non-group secured party appears on any Florida filing checked.

## 1. Per-property value table

**How debt was measured.** "UFB debt" is the sum of every UFB HMDA multifamily origination in the matched census tract and year (all liens), in $M. It is an origination amount, not today's balance:
- Third liens at Kings Mill, Oakleigh and FWB-Greens were released in May 2024 (report E). They are small, $0.5–2.0M each.
- Q3 2026 charge-offs ($362M bank-wide) are not allocated to any loan.
- Refinances inside the window can double-count. I checked each row's lien total against HMDA's own combined loan-to-value (CLTV); rows where they disagree are flagged.

**How value was measured.** "County value" is the latest public assessor figure. It is the Florida just value on the 2026 roll (FDOR statewide cadastral); the Indiana gross assessed value, tax year 2026 (Hamilton County GIS) or the assessor year (Indianapolis MapIndy parcel layer); the Franklin County OH Auditor TOTVALUEBASE (INFERRED to be the 100% market value, not the 35% taxable figure); or the North Carolina county assessed value through NC OneMap (reappraisal year varies by county, UNKNOWN per county). **Prior-year trend: UNKNOWN.** None of the layers reached carries prior years: FDOR's service is the 2026 roll only, and Franklin's PR_ fields read 0.

| Property (owner) | Group | Match | Units · built | County value $M | UFB debt $M | HMDA PV $M (CLTV) | Debt ÷ county value | Debt ÷ HMDA PV | Gap $M | Debt per unit $K | Purchase |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| The Westcott, Tallahassee (TALLAHASSEE-WESTCOTT LLC) | Pedcor | strong | 444 · 2000/05 | 62.37 | 94.23 | 111.36 (85) | 1.51 | 0.85 | 31.87 | 212 | Aug 2022 (Berkadia), price UNKNOWN |
| Kings Mill + 2220 Gloria Cir, Pensacola (PENSACOLA-KINGS MILL / -SI LLC) | Pedcor | strong / probable | 384 · 1998/2004 | 55.23 | 101.61 | 116.11 (85) | 1.84 | 0.88 | 46.38 | 265 | Kings Mill 2022-05-24 (Pedcor page snippet), price UNKNOWN |
| Crestview at Oakleigh, Pensacola | Pedcor | strong | 176 · 1996 | 26.30 | 45.02 | 51.11 (85) | 1.71 | 0.88 | 18.72 | 256 | 2022-05-24 (snippet), price UNKNOWN |
| 3531 Plantation Way, Naples (NAPLES 701 OWNER LLC) | Pedcor | probable | 188 · 1984 | 19.01 | 27.04 | 31.81 (85) | 1.42 | 0.85 | 8.03 | 144 | **$24.0M, Nov 2020** (Business Observer snippet) |
| 5 Mooney Rd, Fort Walton Beach (FWB - GREENS LLC) | Pedcor | strong | 50–99 · 1983 | 9.83 | 15.22 | 17.38 (85) | 1.55 | 0.88 | 5.39 | — | UNKNOWN |
| 600 Denton Blvd, Fort Walton Beach (FWB - ELEVATE LLC) | Pedcor | strong | 50–99 · 1974 | 9.55 | 15.79 | 18.06 (85) | 1.65 | 0.87 | 6.24 | — | UNKNOWN |
| 17200 NW 64 Ave, Miami-Dade (NEW LAKERIDGE LLC) | 8902 | strong | 175 · 1991 | 32.00 | 52.76 | 67.01 (78) | 1.65 | 0.79 | 20.76 | 301 | UNKNOWN |
| 6308 Panther Ln, Fort Myers (CYPRESS WEST OWNER LLC) | unknown | strong | 200 · 1975 | 32.51 | 42.79 | 54.76 (78) | 1.32 | 0.78 | 10.28 | 214 | UNKNOWN |
| 15001 Creek Stone Way, Noblesville (Noblesville SI LLC) | Pedcor | probable | >149 · 2017 | 53.05 | 81.38 | 91.01 (85) | 1.53 | 0.89 | 28.33 | — | transfer 2022-09-20 |
| 1100 Northlake Dr, Noblesville (TB Northlake LLC, 2 parcels) | Pedcor | probable | >149 · 1983/85 | 40.44 | 116.66 | 135.01 (84–85) | **2.88** | 0.86 | **76.22** | — | transfer 2022-11-23 |
| 15950 Spring Mill Depot Dr, Westfield (New Flats at Springmill 75.01% + Pedcor Investments 2000 XLI LP 24.99%) | mixed | probable | >149 · 2021 | 46.50 | 71.73 | 82.26 (85) | 1.54 | 0.87 | 25.23 | — | last transfer 2026-02-23 |
| 11400 Gables Dr, Fishers (New Sanctuary LLC) | 8902 | probable | >149 · 1995 | 45.70 | 64.53 | 79.01 (82) | 1.41 | 0.82 | 18.83 | — | transfer 2022-10-05 |
| 5475 Winding River Rd, Noblesville (New Pebble Brook LLC) | 8902 | probable | >149 · 2001 | 31.32 | 42.51 | 48.21 (85) | 1.36 | 0.88 | 11.19 | — | transfer 2023-01-19 |
| 9815 Seasons West Dr, Carmel (New Seasons LLC) | 8902 | probable | >149 · 2015 | 47.77 | 72.47 | 87.30 (83–85) | 1.52 | 0.83 | 24.70 | — | transfer 2023-05-05 |
| 9 Municipal Dr, Fishers (New Nickel Plate LLC) | 8902 | probable | 100–149 · 2016 | 15.78 | 19.52 | 23.19 (84) | 1.24 | 0.84 | 3.74 | — | transfer 2021-12-14 |
| 5140 Emerson Village Pl, Indianapolis (EMERSON OWNER LLC, 2 parcels) | Pedcor | probable | >149 + 100–149 · UNKNOWN | 32.91 | 66.81 | 82.27 (80–85) | 2.03 | 0.81 | 33.90 | — | UNKNOWN |
| New Alexander Park + New Stafford House, Columbus | 8902 | probable | 300 · 2008/2016 | 40.37 | 69.15 | 80.04 (85) | 1.71 | 0.86 | 28.78 | 230 | re-titled Jan 2025 at $0 |
| New Grafton Park, Columbus | 8902 | probable | 252 · 2015 | 37.77 | 61.17 | 69.71 (85) | 1.62 | 0.88 | 23.40 | 243 | re-titled 2025-01-08 at $0 |
| NEW SAILPOINTE LLC, Mecklenburg NC | 8902 | probable | >149 · 1994 | 58.80 | 81.45 | 96.61 (84) | 1.39 | 0.84 | 22.65 | — | UNKNOWN |
| NEW SOUTHPOINT GLEN LLC, Durham NC | 8902 | probable | >149 | 66.94 | 69.21 | 82.51 (84) | 1.03 | 0.84 | 2.27 | — | UNKNOWN |
| NEW SUTTON PLACE LLC, Durham NC | 8902 | probable | 50–99 | 14.89 | 17.89 | 21.96 (81) | 1.20 | 0.81 | 3.00 | — | UNKNOWN |
| DENVER-SI LLC, Lincoln NC | Pedcor | probable | >149 | 59.10 | 64.00 | 76.71 (83) | 1.08 | 0.83 | 4.90 | — | UNKNOWN |
| ASHEVILLE-WOODBERRY LLC, Buncombe NC | Pedcor | probable | >149 | 26.83 | 43.38 | 49.26 (85) | 1.62 | 0.88 | 16.55 | — | UNKNOWN |
| WS HIGHLAND OAKS LLC, Forsyth NC | Pedcor | probable | >149 | value field empty | 34.26 | 40.31 (85) | — | 0.85 | — | — | UNKNOWN |

**Weak matches**, shown for completeness and **excluded from every aggregate ratio**:

| Weak match | UFB debt $M | County value $M | Why weak |
|---|---:|---:|---|
| New City Place, Gainesville FL (8902) | 58.83 | 32.13 | UFB UCCs VERIFIED, but the parcel sits in tract 12001002219 while HMDA puts the only Alachua loan in 001515, and the parcel shows 111 units against HMDA's >149. Its terms (3.5%, 72 months, affordable units NA) mirror New Lakeridge |
| New Pullman Pointe, Fishers (8902) | 79.05 (likely ~59.2) | 30.59 | The 2023 $19.84M loan probably replaced the 2021 $19.80M set; the summed debt is 166% of HMDA PV |
| Carmel City Center tract (Village Capital Corp, Pedcor Housing Corp, CCC entities) | 122.81 | 59.51 | Tract-level only; the 2025 loans look like refinances of the 2022 loans |
| Marion tract 18097320700 (New Line, New Park 66, New River House; Broad Ripple Edgewater) | 77.22 | 70.48 | 3 loan sets against 4 owners |
| New Dublin Square, Dublin OH (8902) | 85.99 | 36.71 | Shares the tract with Sycamore TIC 1 LLC (270 parcels) |
| New Timbers, Columbus (8902) | 54.55 | 44.94 | The 2021 loan is on a 2010 tract (006990); the parcel is in 2020 tract 006991 |
| Tract 39049007965 (New Hilliard Station or New Sheldon Park) | 43.52 | 89.96 or 29.34 | Ambiguous between the two |
| 39049006302 2023 set (PV $32.1M) | 27.29 | — | Different PV from New Grafton Park; the owner is UNKNOWN |
| AHP of Gastonia NC (Pedcor) | 19.43 | 2.01 | The value is on a "Charitable" (likely exempt) basis, so not comparable |

## 2. Aggregate ratios and their limits

Arithmetic from `matched_properties.csv`. Strong plus probable rows with a county value: 23 rows (25 complexes).

| Slice | n | UFB debt $M | County value $M | Debt ÷ county value | Gap $M | HMDA PV $M | Debt ÷ HMDA PV | County value ÷ HMDA PV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **All** | 23 | **1,336.3** | **865.0** | **1.54** | **471.4** | 1,572.6 | 0.850 | 0.550 |
| Florida | 8 | 394.5 | 246.8 | 1.60 | 147.7 | 467.6 | 0.844 | 0.528 |
| Indiana | 8 | 535.6 | 313.5 | 1.71 | 222.1 | 628.2 | 0.853 | 0.499 |
| Ohio | 2 | 130.3 | 78.1 | 1.67 | 52.2 | 149.8 | 0.870 | 0.522 |
| North Carolina | 5 | 275.9 | 226.6 | 1.22 | 49.4 | 327.0 | 0.844 | 0.693 |
| Pedcor-addressed | 11 | 671.1 | 394.6 | 1.70 | 276.5 | 780.1 | 0.860 | 0.506 |
| 8902 N Meridian | 10 | 550.7 | 391.3 | 1.41 | 159.3 | 655.5 | 0.840 | 0.597 |

Per unit, for the 8 rows with a unit count (FL and OH, 2,119 units): UFB debt is **$233K per unit** and county value **$144K per unit**.

**Limits. Read these before quoting any figure above.**
- **A county value is not an appraisal.** Florida just value for income property commonly sits below sale price (INFERRED; not measured here), and Florida applies restricted-rent valuation (s. 193.017) to qualifying affordable housing. HMDA marks most of these loans 100% income-restricted, but no restriction is VERIFIED. Indiana values apartments "in use" by an income approach that commonly lags transactions. North Carolina values are frozen at each county's last reappraisal (Mecklenburg 2023, Durham 2025, etc.; INFERRED from general schedules, not checked here). Franklin County's 2025 values are a 2023 reappraisal rolled forward (INFERRED). **The 1.54× figure overstates the shortfall to the extent assessors understate apartments; treat it as an upper-side marker, not a measurement.**
- **HMDA property value is the bank's own figure at origination, mostly in 2022, the market peak.** It probably equals price or appraisal at that date, and it has not been checked against either.
- **Debt is origination totals, not balances.** Interest-only loans (report C) keep balances close to origination unless released, paid off or charged off. Releases of third liens in 2024 and the Q3 2026 charge-offs are not netted.
- **A better marker** would be a current appraisal or broker opinion of value per property; second best, recorded sale prices from the deeds (Florida documentary-stamp amounts; Indiana sales disclosure forms). Neither was reachable (section 5).
- **Market context, national, not these properties (secondary):**
  - MSCI Real Capital Analytics apartment prices: **22.3% below the July 2022 level as of July 2026**.
  - Green Street apartment index: **19% to 22% below its 2022 peak** in 2026 readings.
  - Trepp median appraisal cap rate: **4.83% (2022) to 5.64% (2025)**. At constant income that alone is a 14% value fall (4.83 ÷ 5.64 = 0.856).
  - *Illustrative arithmetic only:* marking the bank's $1,572.6M of origination values down 22% gives $1,226.6M, against which $1,336.3M of debt is **1.09×**.
  - Sources: search snippets for MSCI and Green Street (GlobeSt 2026-01-08 and 2026-02-09, CRE Daily; pages not fetched; a GlobeSt article on deepest falls in lower-tier Sun Belt assets returned 403); Trepp figures via CRE Daily, 2026-08-20 (fetched). No metro-level comparables for Pensacola, Tallahassee, Indianapolis suburbs or Columbus were found within budget: UNKNOWN.

**The five largest debt-over-county-value gaps (strong or probable):**

| Property | UFB debt $M | County value $M | Gap $M | Debt ÷ value |
|---|---:|---:|---:|---:|
| TB Northlake, Noblesville IN | 116.66 | 40.44 | 76.22 | 2.88 |
| Kings Mill + Pensacola-SI, Pensacola FL | 101.61 | 55.23 | 46.38 | 1.84 |
| Emerson Owner, Indianapolis IN | 66.81 | 32.91 | 33.90 | 2.03 |
| The Westcott, Tallahassee FL | 94.23 | 62.37 | 31.87 | 1.51 |
| New Alexander Park + New Stafford House, Columbus OH | 69.15 | 40.37 | 28.78 | 1.71 |

TB Northlake carries a caveat. The bank's two values ($83.0M + $52.0M) are 3.3× the county value. Either the county understates it badly or one of the two loan sets belongs to another property in the tract (match probable, not strong).

## 3. Population reconciliation by state (HMDA multifamily originations 2021–2025: 256 loans, $4,175.8M)

Each cell gives the loan count, then $M (share of that state's HMDA dollars). The assignment rules are in `scripts/build.py`.

| State | All | Pedcor-addressed (probable+) | Pedcor (weak) | 8902 N Meridian (probable+) | 8902 (weak) | Mixed (Springmill) | Unknown sponsor | Unmatched |
|---|---|---|---|---|---|---|---|---|
| IN | 73 · 1,257.3 | 13 · 264.8 (21%) | 6 · 122.8 (10%) | 10 · 199.0 (16%) | 11 · 156.3 (12%) | 3 · 71.7 (6%) | 0 | 30 · 442.6 (35%) |
| FL | 46 · 597.9 | 19 · 298.9 (50%) | 0 | 2 · 52.8 (9%) | 2 · 58.8 (10%) | 0 | 2 · 42.8 (7%) | 21 · 144.6 (24%) |
| NC | 31 · 560.1 | 7 · 141.6 (25%) | 3 · 19.4 (3%) | 6 · 168.6 (30%) | 0 | 0 | 0 | 15 · 230.4 (41%) |
| OH | 43 · 530.6 | 0 | 0 | 10 · 130.3 (25%) | 12 · 211.3 (40%) | 0 | 0 | 21 · 189.0 (36%) |
| GA | 25 · 509.5 | not searched | | | | | | 25 · 509.5 (100%) |
| CO | 19 · 446.5 | not searched | | | | | | 19 · 446.5 (100%) |
| TN | 8 · 138.9 | not searched | | | | | | 8 · 138.9 (100%) |
| SC | 8 · 69.6 | not searched | | | | | | 8 · 69.6 (100%) |
| TX | 2 · 63.5 | not searched | | | | | | 2 · 63.5 (100%) |
| OR | 1 · 1.9 | not searched | | | | | | 1 · 1.9 (100%) |
| **Total** | **256 · 4,175.8** | **39 · 705.4 (16.9%)** | **9 · 142.2 (3.4%)** | **28 · 550.7 (13.2%)** | **25 · 426.4 (10.2%)** | **3 · 71.7 (1.7%)** | **2 · 42.8 (1.0%)** | **150 · 2,236.6 (53.6%)** |

**Do not generalize.** In the four states searched, 66% of dollars ($1,939.3M of $2,945.9M) tie to the two groups, the co-owned property or Cypress West, at some grade. That is a statement about where I looked, not about Georgia, Colorado or the other states. The remaining unmatched dollars in the searched states are mostly in counties I could not reach:
- Indiana: Hendricks $188.3M, Boone $113.2M, Steuben, Montgomery, Jackson and Vanderburgh, plus Hamilton's $70.1M on a 2010 tract and its $15.0M separate set.
- Ohio: Delaware County $87.0M and four Franklin tracts, $102.0M.
- North Carolina: Onslow $80.6M, Guilford $93.2M and Gaston tract 032600, $56.7M.
- Florida: Lee 001300/080300, Manatee, Pinellas, Okaloosa 020600/020900, $144.6M in total. Report E's tract scans found no Pedcor or 8902 owner there, but the 2021 loans use 2010 tracts.

### Parcel population found (owner mailing address at One Pedcor Square / 770 3rd Ave SW / PO Box 574 Carmel, or at 8902 N Meridian St Ste 205/250; or "Pedcor" in the owner name)

| Area · coverage | Pedcor-addressed apartment owners | 8902 N Meridian apartment owners |
|---|---|---|
| **Florida** · Pedcor address scanned in 13 of 67 counties (11–15, 17, 19–22, 24, 25, 32) plus every UFB HMDA tract (report E). The statewide scan timed out (HTTP 504 and 55-second query timeouts) for the rest. 8902 group: statewide, complete for owner names beginning "NEW " on 10+ unit parcels | Tallahassee-Westcott (2 parcels), Pensacola-Kings Mill, Pensacola-SI, Pensacola-Oakleigh, Naples 701 Owner, FWB-Greens, FWB-Elevate. 7 complexes; all tied to UFB HMDA (Pensacola-SI at tract level) | New Lakeridge (Miami-Dade, UFB HMDA), New City Place (Gainesville, UFB UCC, weak HMDA tie), **New Pomelo LLC** (19279 NW 27 Ave, Miami Gardens; 259 units, built 2021, just value $56.5M; no UFB HMDA in its tract; no Florida UCC under the name) |
| **Indiana, Hamilton County** · countywide, complete (157 parcels) | Noblesville SI; TB Northlake; Springmill (co-owned); Village Capital Corporation (a UFB service subsidiary, 0 Veterans Way, AV $22.9M, built 2023); Pedcor Housing Corporation (800 Monon Green Blvd, AV $9.7M); CCC Residences, CCC Nash, CCC Hamilton. Plus non-apartment holdings (hotel, offices, retail in Carmel City Center) | New Signature at Carmel (AV $60.4M, transfer 2026-07-02), New Prairie Lakes ($61.6M), New Seasons, New Sanctuary, New Pebble Brook, New Pullman Pointe, Cumberland Crossing Fishers LP ($23.4M, transfer 2025-08-22), New Nickel Plate. Plus medical offices (CCI, Bridges MOB) |
| **Indiana, Marion County** · countywide, complete for these address strings (42 parcels) | Emerson Owner LLC; Broad Ripple Edgewater LLC; tax-credit partnerships Pedcor Investments 2021 CLXXXV, 2008-CXV, 2010 CXXIX, 2011 CXLI | New Lakeshore 1 (AV $81.3M), New Stone Ridge (3 parcels, $71.5M), New Grounds ($57.8M), Avondale Meadows LP **"%BIRGE & HELD"** ($25.9M), New Maxwell **"%BH MAXWELL LLC"** ($25.8M), New Park 66, New Regency Park LP, New River House, New Line, New Lodge, New E'Laan, New MLK II |
| **Ohio, Franklin County** · countywide by mailing address, then by owner name (1,078 parcels) | Golf Pointe Property Owner LLC (228 condo-rental parcels, $13.8M; re-titled 2025-01-23; no UFB HMDA in its tract 008166) | New Hilliard Station (810 parcels, $90.0M, transfer 2022-02-08), New Dublin Square, New Timbers, New Grafton Park, New Sheldon Park, New Alexander Park, New Stafford House. Six of them were re-titled 2024-12-26 to 2025-01-24 at $0 |
| **North Carolina** · statewide (NC OneMap, every parcel with mailing state IN: 2,873; no transfer limit hit) | Asheville-Woodberry, Denver-SI, WS Highland Oaks, AHP of Gastonia; Pedcor Investments tax-credit partnerships in Durham, Cabarrus, Mecklenburg (3) and Wake; SVMP Developer LLC (Union County land and lots); Village Capital Corporation (Durham vacant land; Mecklenburg) | New Sailpointe, New Southpoint Glen, New Sutton Place; plus CCI medical offices (Brunswick, Pitt) |

**The pattern (INFERRED).** The "City-Name LLC" owners at Pedcor's address and the "New ___ LLC" owners at 8902 N Meridian are the entities behind the 2021–2023 acquisition loans. The many "Pedcor Investments [year] [numeral] LP" owners are tax-credit developments, mostly mailed to PO Box 574. None of those sits in a UFB HMDA tract I matched; their lenders are UNKNOWN.

### Florida UCC check (Florida Secured Transaction Registry, publicsearchapi.floridaucc.com, read 2026-11-11)

| Debtor searched | Result | Secured parties |
|---|---|---|
| NEW CITY PLACE, LLC | 3 UCC-1s filed 2022-06-16: 202201982137, 202201982129, 202201982110 (VERIFIED) | UNITED FIDELITY BANK, FSB (×2); **FIDELITY FEDERAL BANCORP, 770 3rd Ave SW, Carmel** (×1) |
| NEW POMELO | SEARCH-NOT-FOUND (filed and lapsed lists) | — |
| PENSACOLA-SI | SEARCH-NOT-FOUND | — |
| NAPLES 701 OWNER | SEARCH-NOT-FOUND | — |
| The 7 debtors in report E (Westcott, Kings Mill, Oakleigh, FWB-Greens, FWB-Elevate, New Lakeridge, Cypress West) | UFB only; no assignment, no other secured party (report E, VERIFIED there) | UFB |

The New City Place filings are the only place where a group party other than the bank holds a lien. Whether the parent's filing secures a third-lien loan, a guarantee or something else is UNKNOWN; the filing image was not read.

## 4. Sources (all read 2026-11-11)

- HMDA LAR extracts: `PROME/reports/2026-11-11_united-fidelity-follow-up/hmda/ufb_2021.csv` to `ufb_2025.csv`, filtered to multifamily originations (256 loans, $4,175.81M, matching the synthesis).
- FDOR statewide cadastral, 2026 roll: services9.arcgis.com/Gh9awoU677aKree0/.../Florida_Statewide_Cadastral/FeatureServer/0, and its centroid version (Florida_Statewide_Parcel_Centroid_Version/FeatureServer/0), queried by parcel ID and owner-name prefix.
- Hamilton County IN GIS: gis1.hamiltoncounty.in.gov/arcgis/rest/services/HamCoParcelsPublic/MapServer/0 (AVTAXYR 2026).
- Indianapolis/Marion County: gis.indy.gov/server/rest/services/MapIndy/MapIndyProperty/MapServer/10 (parcel layer with owner and assessed value).
- Franklin County OH Auditor: gis.franklincountyohio.gov/hosting/rest/services/ParcelFeatures/Parcel_Features/MapServer/0.
- NC OneMap: services.nconemap.gov/secure/rest/services/NC1Map_Parcels/FeatureServer/1.
- Census TIGERweb ACS2022 tracts (layer 6), used for every point-to-tract lookup.
- Florida UCC public search API (as above).
- Market context: CRE Daily, "Cap Rate Hikes Drive US Multifamily Value Reset," 2026-08-20 (Trepp data), https://www.credaily.com/?p=221733. Search snippets only: GlobeSt 2026-01-08 and 2026-02-09 (Green Street); MSCI RCA via search summary; Pedcor "Jacksonville and Pensacola Acquisitions" page (AWS mirror; snippet, not fetched); Business Observer 2020-11-11 (Naples, $24M; snippet).

## 5. What was unreachable (failures reported as failures)

| Source | Result |
|---|---|
| FDOR statewide service, statewide address search | HTTP 504 and 400 query timeouts (55 s). A per-county loop completed only 13 counties before repeated timeouts. **The Florida Pedcor-address population outside HMDA tracts is incomplete** |
| Florida prior-year values | Not available in the service (2026 roll only). The FDOR data-portal page loaded but exposed no file links to automation. Trend UNKNOWN |
| Florida purchase prices | Sale fields are blank (0) on every matched parcel, because the roll only carries recent sales. County clerk deed records were blocked in report E. Doc-stamp prices UNKNOWN |
| Indiana statewide (IndianaMap parcels) | Reachable, but the layer has no owner fields, so it cannot be used for an owner search |
| Hendricks, Boone (IN) and Delaware (OH) county GIS | Guessed REST endpoints returned 404 or nothing; no further search inside budget. Together these cover about $388M of HMDA |
| Indiana sales-disclosure prices | DLGF page reached; the data link is a separate search application (gatewaysdf); not attempted |
| Georgia, Colorado, Tennessee, South Carolina, Texas | Not searched (budget). North Carolina was the one chosen |
| Metro-level comparable sales | Not found; one GlobeSt article returned 403 |

## 6. Open unknowns

- Current market value of any matched property: no appraisal, broker opinion or recorded price found. Purchase prices UNKNOWN except Naples.
- Outstanding balances: whether the 2024 lien releases and Q3 2026 charge-offs touched these loans.
- Whether TB Northlake's two loan sets are both on Northlake, which Escambia set is Kings Mill, and which owner holds the weak-matched Ohio, Carmel and Marion loans.
- Whether New City Place is the Alachua HMDA loan, and what Fidelity Federal Bancorp's lien secures.
- The managers of the 8902 N Meridian entities. "Birge & Held" rests on two owner care-of lines, not on a registry record.
- Why six Franklin County "New ___" properties and Golf Pointe were re-titled at $0 between 2024-12-26 and 2025-01-24, and Springmill on 2026-02-23.
- Who the borrowers are behind $2.24B (53.6%) of unmatched HMDA dollars, including all of Georgia and Colorado.
