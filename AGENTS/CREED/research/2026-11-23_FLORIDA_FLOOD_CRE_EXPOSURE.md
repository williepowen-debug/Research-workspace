# Florida flood, November 2026: where commercial real estate collateral sits, and how it could transmit

**Written:** 2026-11-23 (Mon), session started 16:41 ET (from `date`). **Why:** Will's Florida flood sweep (PROME DOCKET row dated 2026-11-24, "FLORIDA FLOOD TRANSMISSION SWEEP"; Will 16:26 and 16:33 ET). CREED's lane: the commercial real estate collateral side. CORAL leads (insurance, home values, HOAs, condo law); REGINALD owns banks by name; HOMER owns home values, housing finance and multifamily scoring. **Logging and analysis only: no score, band, trigger or prediction letter moved.**

## 0. The event, verified at primary this session

| Fact | Value | Source, time read |
|---|---|---|
| Flood Watch, Palm Beach / Broward / Miami-Dade (metro and coastal zones) | Tue 11/24 19:00 ET to Thu 11/26 01:00 ET | NWS `api.weather.gov/alerts/active?area=FL`, read 16:43 ET 11/23 (PRIMARY-READ) |
| Flood Watch, northern Brevard through Martin, incl. Indian River, St. Lucie, Okeechobee | Wed 11/25 01:00 ET to Thu 11/26 01:00 ET | same |
| Coastal Flood Warning, Flagler (inland and coastal) and eastern Putnam | to Wed 11/25 19:00 ET | same |
| Coastal Flood Watch, Duval, eastern Clay, St. Johns, Nassau (Jacksonville area) | Tue 11/24 15:00 to Wed 11/25 19:00 ET | same; **wider than the brief's county list** |
| River Flood Warnings in force | Seminole, Lake, Volusia, Brevard | same |
| St. Johns at Cocoa | 18.58 ft, steady 18.5 to 18.6 through late week; Lake Harney past its record | AEOLUS packet 2026-11-23 16:22 ET (NWPS; not re-read by CREED) |
| FEMA declarations for Florida since 2026-09-01 | Only Hurricane Isaias: EM-3655 (10/09, 27 counties) and DR-4955 (10/27, 15 counties). **None for the November flood** | OpenFEMA DisasterDeclarationsSummaries, read 16:44 ET 11/23 (PRIMARY-READ) |

⚠️ A watch is a forecast of possible flooding, not flooding. On 11/23 the realized flood is the St. Johns basin (Seminole, Lake, Volusia, Brevard, Putnam, Flagler); the southeast coast is a rain watch on saturated ground.

## 1. Where securitized commercial property sits

### 1a. The one free county-level screen that exists is for a different storm

| Item | Figure | Source |
|---|---|---|
| Trepp's Isaias screen (Panhandle, 15 counties of FEMA EM-3655) | **$3.27B gross** securitized CRE debt, 306 records ($2.922B net of Freddie overlap); multifamily 68.8%, lodging 14.9%, retail 7.8%, self-storage 5.1% | Trepp 2026-10-14, PRIMARY-READ (`KB-CREED-122`) |
| Trepp's boundary rule | the FEMA designated-area list for the declaration | same |
| FEMA declaration for the November flood | **none** (OpenFEMA, 11/23) | PRIMARY-READ |

**So what:** the free, county-level, by-property-type number Will asked for does not exist yet for this event, and the way Trepp builds it means it will probably not exist until FEMA declares. The Panhandle figure is a scale anchor only: those 15 counties are mostly small markets, while the southeast-coast watch counties (Miami-Dade, Broward, Palm Beach) are among the largest securitized CRE markets in the country. ⚠️ CREED has no free figure for those three counties' securitized balance; any multiple of the $3.27B would be an invention.

### 1b. Named Florida loans already on CREED's case ledger in the flood or watch counties (all distressed BEFORE the flood)

| Case | Property, county | Type | Loan | State before the flood |
|---|---|---|---|---|
| `CASE-CREED-147` | The Wymore 360, Altamonte Springs (**Seminole**, St. Johns basin county) | multifamily, 200 units | $33.0M IO 6.839%, BMO 2024-5C8 conduit | special servicing since 2026-08-11 for payment default, strategy code foreclosure |
| `CASE-CREED-146` | Pembroke Lakes Mall, Pembroke Pines (**Broward**, watch) | retail | $260M single-asset CMBS (Goldman), Brookfield borrower | special servicing; maturity default 2025-03-01 |
| `CASE-CREED-005` | Columbus Center, Coral Gables (**Miami-Dade**, watch) | office | $69M (foreclosure suit amount) | sold by receiver 2025-03-05 |

⚠️ None of these is known to be flooded. Altamonte Springs is in Seminole County but CREED has not placed the property against the flood extent. They show only that distress was already present in these counties for demand and rate reasons.

### 1c. Pre-flood Florida CMBS baseline
Florida CMBS retail delinquency **6.72%**; Tampa and Miami regional-mall delinquency **above 30%**; Florida hotel delinquency mostly below the national rate (Trepp 2026-07-16, PRIMARY-READ, `KB-CREED-124`; the data month is not stated in the post). National context: Trepp October overall DQ 7.87%, special servicing 11.74% (`KB-CREED-119`).

### 1d. Public REITs with disclosed Florida concentration
*(Section filled from a read-only research pass; see below.)*

### 1e. Analog base rates from earlier Florida storms

| Event | Securitized CRE in the declared area | Outcome | Source |
|---|---|---|---|
| Isaias, Oct 2026 (Panhandle) | $3.27B gross, 15 counties | no credit outcome published yet | Trepp 10/14 (`KB-122`) |
| Milton, Oct 2024 | KBRA-rated: $8.4B of $261B (**3.2%**), 11 counties, 305 of 658 deals | no published default wave | KBRA 2024-10-09 (`KB-125`) |
| Irma, 2017 | Freddie Mac MF: 1,249 loans, $18.3B in the area | ~70% some damage, **none major** | Freddie Mac Oct 2017 (`KB-125`) |

**What free sources cannot show:** securitized balance by county for the St. Johns basin or the southeast-coast watch counties; agency multifamily (Fannie, Freddie) Florida share (no public figure found; older Fannie 10-Ks name only CA, TX, NY as concentrations); which loans sit inside or outside a mapped flood zone; servicer watchlist codes (CREFC investor reporting is not free). The free primary route to a county-level count is SEC Form ABS-EE loan tapes (registered conduits, about 2017 and later, property ZIP code on every loan). CREED's ABS-EE fetch cache from 11/05 is no longer on disk; a fresh pull is about a gigabyte and was not attempted on battery tonight. It would still miss SASB, CRE CLOs and agency loans.

## 2. The insurance channel for commercial property

| Item | Figure | Date | Source |
|---|---|---|---|
| Florida securitized MF insurance cost, median YoY | 2023 **+42.1%** · 2024 +7.7% · 2025 **−6.2%** (rest of US +3.4%) | Trepp, Aug 2026 | PRIMARY-READ (`KB-123`) |
| Same, chained (CREED arithmetic on medians, not any property's path) | Florida about **2.17x** its 2019 level by 2025; rest of US about 1.73x | — | ANALYTICAL |
| US commercial property insurance rates | Q3 2026 **−10%**, Q2 −13% | Marsh, 2026-10-21 | SECONDARY (`KB-127`) |
| Citizens commercial residential (condo associations, apartments) from 7/1/26 | condo multiperil +7.7%, **wind-only +14.1%**; non-condo +7.2% / +14.4%; nonresidential −1.8% / −5.0% | Citizens 2026-04-30 | PRIMARY (`KB-127`) |
| Force-placed insurance as a CMBS distress route | about **24** CMBS properties watchlisted or sent to special servicing (FL, TX, NY, NJ, AZ); Z Ocean Hotel Miami Beach payments about 4x | Morningstar via Bisnow, 2025-04-02 | SECONDARY (`KB-127`) |

**What the loan documents require** (`KB-126`): CMBS and Fannie Mae require flood cover only for improvements inside a mapped Special Flood Hazard Area (zones A and V): NFIP maximum plus excess flood up to loan balance or insurable value. NFIP pays at most $500K per building for a 5+ unit residential building. Windstorm is required within 25 miles of Florida's Atlantic coast. If the borrower lapses, the servicer force-places cover and charges it to the borrower.

**So what:** this flood is fresh water, not wind. Standard commercial property policies exclude flood. A record river flood reaches buildings outside the mapped zone, where the documents never required flood cover. That uninsured slice, not premiums, is the near-term credit channel: repair cost lands on the borrower's own liquidity. Premiums are a slower channel and are currently falling for most commercial owners; Citizens' condo and wind-only lines are the exception and still rising.

**Has insurance already shown up in DSCR or special servicing?** Yes, nationally, through force-placed insurance in 2024–25 (about 24 properties, Morningstar). For a named Florida loan where insurance alone caused the transfer, CREED and its helper found none in free sources. The named Florida transfers in or near the flood counties (Wymore 360, Estates at Palm Bay $61M in Brevard, `KB-128`) were payment and sponsor failures.

## 3. Condo-adjacent commercial exposure

| Item | Figure | Source |
|---|---|---|
| HB 913 (ch. 2025-175) | associations may fund reserves with **lines of credit or loans** (majority vote), from 2025-07-01 | PRIMARY (`KB-129`) |
| Florida condo/townhouse market, Oct 2026 | **8.0 months of supply**, median $290K (−3.3% YoY), 61,983 active listings | Florida Realtors 2026-11-18 (`KB-129`) |
| Treasure Coast condo prices | "tumble" (TCPalm 11/21, title only) | WALTER card SIG-W-20261121-003 |

**Where it reaches commercial credit:** (a) bank loans to associations to fund special assessments and reserves (legal since HB 913; no free volume figure found); (b) condo construction and inventory loans on unsold new units (bank and debt-fund books; not in CMBS); (c) old buildings sold in bulk to developers when owners cannot fund repairs (condo terminations). **In the commercial credit CREED tracks (CMBS conduit and SASB, CRE CLO, mREIT books), CREED has no evidence that the post-Surfside law has shown up yet.** Condo construction and association loans sit on bank balance sheets (REGINALD's lane) and are invisible in CMBS data. CORAL owns the condo law and the condo market.
