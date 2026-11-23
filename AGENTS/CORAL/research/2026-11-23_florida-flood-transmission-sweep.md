# Florida flood transmission sweep — insurance, home values, condo associations, tradeability (CORAL coral-al, 2026-11-23)

**Written:** Mon 2026-11-23, 16:48 ET onward (`date`). **Task:** PROME prome-77 wake on Will's word (16:26 / 16:33 ET): DOCKET D:L1243 (FLORIDA FLOOD TRANSMISSION SWEEP, CORAL lead) + D:L1204 (CORAL flood re-read, due 11/24, taken a day early). **Peers in their own lanes tonight:** REGINALD (banks), CREED (CRE/CMBS), HOMER (home values, housing finance); MARCO next wake; AEOLUS hazard. **Basis key:** PRIMARY = read at the issuer, regulator, statute or government dataset this session (by CORAL, or by a CORAL read-only helper and spot-checked by CORAL where marked ✔); PRESS = article opened; SUMMARY = search summary only. Helper notes (not repo files): two read-only helpers, insurance and condo law, 16:36–16:58 ET.

## 0. Bottom line (plain words)

1. **Most of this flood is uninsured, and the insured part is federal, not Florida insurers'.** Home policies, Citizens included, exclude rising water. Only 11.8% of Brevard homes carry a federal flood policy (FEMA, 8/03/2026), 4.0% in Seminole, 2.6% in Putnam. The first insured figure exists: **1,157 federal flood claims in Florida for losses 11/01–11/12, 745 in Brevard, $4.84M of building damage paid so far** (OpenFEMA, data to 11/16 ✔). The South Florida flood and the St. Johns crest are not in that data yet.
2. **The cost reaches households through a law already on the books, not through this flood's insurance bill.** From **1/1/2027 every remaining Citizens home policy that covers wind must also carry flood insurance** (627.351(6)(aa), 2026 statutes ✔). That turns the flood-cover gap of the uninsured Citizens households into a required new premium at their 2027 renewal: 168,941 multiperil personal policies statewide at 10/31, 4,840 in Brevard (Citizens ✔ by helper; some already carry flood). Ordinary home-insurance prices are going the other way: filed rate changes averaged −4.8% (September, press) and reinsurance is expected to fall at least 10% at 1/1/2027 (KBW, press). The federal flood program's own authority lapses 12/11 unless Congress extends it, three weeks before that mandate.
3. **Home values: no county-level flood signal, and history says not to expect one soon.** County indices in October were flat to slightly down year on year across all twelve flood and watch counties. In 2017, when the St. Johns last set a record at Cocoa, Brevard, Volusia and Seminole kept pace with Florida over the next 24 months. The damage shows up on the flooded parcels: since 10/1/2025 every Florida seller must disclose known flood damage, flood claims and flood aid (689.302 ✔), so the discount attaches to the house, not the county.
4. **Condos: the hard deadline is five weeks away, and the floods land on top of it.** The structural reserve study must be done by **12/31/2026, "in no event" later** (718.112(2)(g) ✔). Fannie Mae's reserve test rises from 10% to 15% for loan applications from **1/4/2027**. Associations are **not required** to carry flood insurance (718.111(11) ✔ "may"), and Citizens' condo-association policies are outside the flood mandate. So an association that took flood damage in Broward, Palm Beach or Miami-Dade outside a mapped flood zone most likely pays for it out of reserves or a new assessment, on top of the study's bill. **No named association with flood damage has been found** (helper searched press; association notices are not public). This is still a mechanism, not an observation.
5. **Tradeability: no supported implication tonight.** Florida bank stocks moved with the regional-bank index since 10/30 (USCB −0.8%, BKU −2.9%, SBCF −3.3%, SSB −4.5% vs KRE −3.4%), and the Florida home insurers split (UVE +1.6% to ACIC −9.2%) for reasons that are not the flood, because the flood is excluded from their policies.

## 1. D:L1204 — the due row, item by item

| Item | Reading | Basis, time |
|---|---|---|
| St. Johns near Cocoa (COCF1) crest | **High 18.77 ft at 06:30Z 11/21** (observed window); **18.58 ft at 20:15Z 11/23**; forecast **18.5–18.6 ft through 12Z 11/28**. ⇒ **No fall has started**; water stays above 17.2 ft (homes flood) through at least 11/28. CORAL's 11/19 call (18.4 ft held to 11/24) was **0.37 ft low** at the high | NWPS API, PRIMARY, pulled 21:42Z 11/23 |
| Above Lake Harney (GENF1) | **13.09 ft (20:30Z)**, above its **12.67 ft 2022 record**; forecast 12.1 ft by 12Z 11/28 ⇒ cresting now | NWPS, PRIMARY; record per WALTER card 017 gauge-page read |
| Sanford (SNFF1) | 7.79 ft, forecast **8.2 ft (major) 00Z 11/26**, flat to 11/28; record 8.96 (2022) | NWPS, PRIMARY |
| DeLand (DLAF1) | 5.52 ft, forecast **6.1 ft at 06Z 11/27**; record 6.33 (2022) | NWPS, PRIMARY |
| Astor (ASTF1) | 4.13 ft, forecast 4.4 by 11/26; record 4.81 (2024) | NWPS, PRIMARY |
| New alerts | Flood Watch Palm Beach/Broward/Miami-Dade **19Z 11/24 → 01Z 11/26**; Flood Watch Okeechobee and Brevard to Martin **01Z 11/25 → 01Z 11/26**; Coastal Flood Warning Flagler/E Putnam to 19Z 11/25; Coastal Flood Watch NE FL; river Flood Warnings Brevard, Seminole, Volusia/Lake | api.weather.gov, PRIMARY, ~21:45Z 11/23 (AEOLUS correction verified) |
| Federal declaration | **NONE** for the November floods. OpenFEMA FL rows since 10/20 = 15, all DR-4955 (Isaias, 10/27). ⚠️ Row lastRefresh max 11/13: the dataset can lag. Press (WPTV, undated, the 11/09 request): Martin County 66 homes damaged, 25 destroyed | OpenFEMA DisasterDeclarationsSummaries v2, PRIMARY, 21:42Z 11/23; WPTV PRESS |
| Permission vs money | A declaration is permission to pay; even a grant pays nothing for weeks. No county or city flood appropriation, reserve draw, fee or borrowing was checked this session (GAP, see § 6) | — |
| Insured loss | **First figure: NFIP 1,157 FL claims, loss dates 11/01–11/12; Brevard 745 (642 on 11/02), St. Lucie 191, Palm Beach 89, Broward 35, Indian River 32, Martin 21; building paid $4,844,412.** FEMA's event label: "2026-11-Florida-King Tides" (1,140 claims). Data as of 11/16; the 11/17–19 SE FL flood and the St. Johns crest are **not in it** | OpenFEMA NfipClaims v3, PRIMARY ✔ (CORAL re-ran 21:47Z) |
| Citizens / OIR | No OIR flood data call (flood excluded from HO). Citizens PIF **196,511 at 11/20** (−18,886 vs 215,397 at 11/06); mechanism **UNKNOWN** (the takeout stats PDF still dated 10/26; a November takeout round is the likely cause by the 10/20 precedent, not established) | citizensfla.com, PRIMARY ✔ |
| Rain, one figure (AEOLUS owns) | Event 1 (11/01–03): **24.69 in, Malabar 1.9 SE** (WPC final). SE FL 11/17–19: **17.59 in, 72 h, 2 SE Plantation** (NWS Miami PNS 11/19 17:06 EST, preliminary single-station); 16.65 in is "48 h, earlier bulletin". Event 2 Brevard (11/18–19) total: **none received from AEOLUS** | AEOLUS packets 11/23 (KB-AEO-305, -306) |

### CATO's four tests, applied

| Test | Applied |
|---|---|
| Cause not isolated | Florida bank prices since 10/30 track KRE (§ 5); credit spreads (VIOLET: HY 376, 11/23) and rates move the same stocks. Insurer price moves have rivals (Q3 results, softening reinsurance, depopulation). No price move is attributed to the flood |
| Permission is not funding | No federal declaration; a grant would be permission. NFIP claims are the only money moving, $4.84M building paid of an unknown total |
| Dated horizon | Every expectation in § 2–4 carries a date |
| Search limits kept | § 6 |

## 2. Question 1 — home insurance cost and availability

### Established

| Item | Figure | Date | Basis |
|---|---|---|---|
| What is insured | Standard HO and Citizens policies exclude flood (rising water, surface water); they pay wind and wind-driven rain. NFIP or private flood pays building (to $250K) and contents (to $100K); NFIP pays no additional living expenses | statute notice text 689.302; DFS flood FAQ (via CATO 11/23) | PRIMARY |
| NFIP residential take-up (contracts ÷ FEMA residential structures) | Brevard **11.8%** (29,365) · Volusia 11.1% · Seminole **4.0%** · Indian River 17.8% · St. Lucie 8.7% · Martin 14.1% · Palm Beach 13.0% · Broward 19.2% · Miami-Dade **33.4%** · Putnam **2.6%** · St. Johns 23.2% · Flagler 15.2% · **Florida 13.7%** (1,040,662) | FEMA as of 2026-08-03 | PRIMARY (helper; `NfipResidentialPenetrationRates`) — ⚠️ SFHA ratios for Flagler (115%) and St. Johns (342%) are FEMA denominator anomalies |
| High-risk-zone (SFHA) take-up | Brevard 47.0%, Seminole 47.1%, Broward 76.1%, Miami-Dade 74.5% | 2026-08-03 | same |
| NFIP claims, early November | 1,157 FL; Brevard 745 = 2.5% of its contracts; $4.84M building paid | data 11/16 | PRIMARY ✔ |
| Citizens flood mandate | Wind-covering personal residential policies must carry flood: ≥$600K from 1/1/2024, ≥$500K 2025, ≥$400K 2026, **all others 1/1/2027**; SFHA policies since 2023. **Exempt: wind-only (PR-W) policies and condo-unit forms**; condo associations (commercial residential) not in the personal-lines mandate | 627.351(6)(aa), 2026 statutes | PRIMARY ✔ |
| Citizens size | PIF **196,511 (11/20)**; 10/31 month-end **216,447** (−38,389 m/m), exposure $57.6B (−$12.0B); PR-M 168,941, PR-W 43,622 | Citizens | PRIMARY (✔ 11/20; 10/31 PDF by helper) |
| Citizens by county, 10/31 (PR-M / PR-W) | Brevard 4,840 / 230 · Volusia 2,430 / 1,176 · Seminole 883 / — · Palm Beach 14,073 / 4,598 · Broward 28,902 / 8,095 · Miami-Dade 43,650 / 9,382 · St. Lucie 1,939 / 119 · Martin 1,143 / — | Citizens county PDF | PRIMARY (helper) |
| Home-insurance price trend | OIR 30-day avg requested change **−4.8%** (Sep 2026; −1.1% a year earlier); Oct: >824,300 homeowners getting decreases up to −12.1%; Citizens 2026 HO multiperil avg −8.8% | Sep–Oct 2026 | SUMMARY (press citing OIR) — not read at OIR |
| Reinsurance 1/1/2027 | US property-cat XoL expected **−10% or more** (KBW, 9/11); Fitch (8/26): softening continues into 2027 absent a big 2H loss; FL property mid-2026 down up to 25%; 6/1/2026 FL renewals −15/−20% risk-adjusted (CORAL record) | Aug–Sep 2026 | PRESS |
| Private flood | US 683K private flood policies end-2025 (NAIC; likely ~100K understated); **no Florida 2026 count found** | NAIC 5/2026 | PRIMARY (helper) |
| NFIP authority | Expires **12/11/2026** unless extended (H.R. 6500) | 9/2/2026 | CORAL record |
| Citizens 2027 rate | **UNKNOWN**: no 2027 recommendation found; last cycle board voted 12/10/2025 | — | SUMMARY |
| Citizens CEO (WALTER title 11/21) | **UNVERIFIED**: "Tim Cerio to step down in January" (Florida's Voice, TBT titles); the only article found is paywalled and undated | — | not opened |

### Which parts of the loss are insured

| Loss | Who pays | Insured? |
|---|---|---|
| Flooded house structure and contents, owner with NFIP/private flood | NFIP (federal Treasury-backed program) or private flood carrier, after deductible, to $250K/$100K | Yes, partly |
| Same, owner without flood cover (88% of Brevard homes, 96% of Seminole) | Household savings, credit, SBA disaster loan (only if declared), FEMA household aid (only if declared, capped) | **No** |
| Temporary housing while repairing | Household (NFIP excludes it; HO pays only for covered perils) | **No** |
| Roof/wind-driven rain damage, EF-1 tornado (S Palm Beach 11/21) | HO / Citizens after hurricane-or-AOP deductible | Yes |
| Flooded cars | Auto comprehensive | Yes |
| Condo common elements (garages, elevators, ground floors) | Association master policy only if it bought flood (optional, § 4); else reserves or special assessment on all owners | Mostly **no** outside mapped zones (inference) |
| Public roads, water systems, debris | County/city; FEMA Public Assistance only if declared (cost share set in FEMA's Federal Register notice; DR-4955's still unpublished, L784) | No (self-funded until declared) |

### Expected, and by when (unscored outlooks unless stated)

| Expectation | Horizon | Probability (CORAL judgment) | Meaningful alternative | What would change my mind |
|---|---|---|---|---|
| Ordinary home insurance (HO, Citizens) does **not** reprice up because of these floods; Citizens' 2027 statewide personal-lines recommendation is flat or down | Citizens board ~Dec 2026; OIR approval early 2027 | ~85% | A rate *increase* recommendation citing non-weather water or litigation | A Citizens recommendation > 0% statewide, or Brevard/Broward territory increases |
| The household cost lands through **flood cover**, not HO: Citizens' 1/1/2027 mandate forces flood purchase at renewal on the remaining uncovered PR-M policies; some leave Citizens for private carriers that do not require flood (rival: they buy NFIP, cost rises) | renewals from 1/1/2027 through 12/2027 | direction ~80%; size UNKNOWN (no count of PR-M policies already carrying flood) | Legislature delays the mandate in the 2027 session (opens 3/2/2027) — possible after a flood, sign unknown | A bill or OIR order moving the date; Citizens publishing the count of mandate-affected policies |
| NFIP claims for the November floods rise well above 1,157 once 11/17–21 losses load (Broward/Palm Beach/St. Johns) | OpenFEMA refreshes, ~2–6 weeks | ~90% | — | — |
| NFIP lapse at 12/11 | 12/11 | **UNKNOWN** (no basis to set odds; lapses have happened before) | Extension in a funding bill | Congressional action before 12/11 |
| Reinsurance 1/1/2027: no Florida reversal from these floods (flood is excluded from most cat treaties' HO books) | 1/1/2027 | ~85% | A late-season loss elsewhere tightens capacity | Broker 1/1 reports showing FL-specific firming |

## 3. Question 2 — home values in the flooded and watch counties

### Established

| County | Zillow ZHVI Oct 2026 (mid-tier, all homes, SA) | YoY | vs peak (date) |
|---|---|---|---|
| **Florida** | $375,056 | −0.48% | −7.0% (5/2024) |
| Brevard | $342,450 | −0.06% | −6.1% (4/2024) |
| Volusia | $323,377 | +0.14% | −6.4% (5/2024) |
| Seminole | $400,274 | −0.07% | −5.0% (5/2024) |
| Indian River | $364,850 | −0.31% | −7.6% (4/2024) |
| St. Lucie | $370,971 | −0.53% | −6.1% (4/2024) |
| Martin | $451,876 | +1.60% | −6.1% (12/2023) |
| Palm Beach | $479,514 | +2.98% | −4.3% (5/2024) |
| Broward | $423,434 | −1.14% | −6.7% (5/2024) |
| Miami-Dade | $524,772 | +0.93% | −3.0% (10/2024) |
| Flagler | $350,580 | +0.55% | −13.3% (8/2022) |
| Putnam | $214,503 | +0.54% | −3.6% (6/2024) |
| St. Johns | $488,780 | −0.29% | −7.5% (8/2022) |

Source: Zillow Research public CSV `County_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv` and the State file, downloaded 16:4x ET 11/23 (PRIMARY for Zillow's own index; a model index, smoothed, mixes SF and condo). October predates the 11/17–21 flooding; event 1 (11/01–03) is also after October. CORAL's own statewide series (FL Realtors Oct, FMHPI Sep) are in STATUS. Florida Realtors metro (Oct, helper, column order inferred): Palm Bay–Melbourne–Titusville condo/TH sales 160 (+3.2%), median $299,790 (+3.4%); Miami–Fort Lauderdale–West Palm condo/TH 2,537 (−7.6%), $315,500 (−4.4%).

### What a flood of record did before (county level)

| Event | County | 12 m before | +6 m | +12 m | +24 m (county vs FL) |
|---|---|---|---|---|---|
| Irma, Sep 2017 (St. Johns at Cocoa 17.43 ft, then 2nd highest) | Brevard | +11.9% vs +8.1% | +4.9% vs +4.0% | +8.7% vs +7.6% | +12.3% vs +12.4% |
| | Volusia | +10.7% vs +8.1% | +6.1% vs +4.0% | +10.2% vs +7.6% | +16.3% vs +12.4% |
| | Seminole | +8.8% vs +8.1% | +4.2% vs +4.0% | +7.8% vs +7.6% | +14.6% vs +12.4% |
| Ian, Sep 2022 (surge and wind, catastrophic insured loss) | Lee | +33.6% vs +26.7% | −2.9% vs −1.1% | −1.7% vs +0.5% | **−5.7% vs +1.6%** |
| | Charlotte | +33.1% vs +26.7% | −3.3% vs −1.1% | −3.8% vs +0.5% | **−9.1% vs +1.6%** |

Base date = the month before the event; Zillow ZHVI as above; CORAL arithmetic. ⚠️ **Inference audit:** (1) the rival for Lee/Charlotte's underperformance is mean reversion from a bigger run-up (+33% vs +27% the year before) plus the 2023–24 insurance and condo-law shock — all move the same statistic the same way, so Ian's −7 to −11 pp is **not** a clean flood effect; (2) a county average dilutes a neighbourhood loss — Irma's "no effect" says the county index will not show it, not that flooded streets kept their value; (3) refuter for "no county signal": Brevard ZHVI underperforming Florida by >2 pp over the next 6 months with the same rate backdrop.

### Expected, and by when

| Expectation | Horizon | Probability | Alternative | What would change my mind |
|---|---|---|---|---|
| No county-level price break in Brevard, Seminole or Volusia attributable to the flood | Zillow/FL Realtors prints through May 2027 | ~70% | An Ian-type divergence if the flood combines with the 2027 flood-cover cost and the flood-disclosure form | Brevard ZHVI < Florida by >2 pp over 6 months; Space Coast MLS listings withdrawn/expired jump in Palm Bay, Rockledge, Cocoa ZIPs |
| Discount and stalled sales concentrate on flooded parcels (Silver Pines Rockledge, Palm Bay Port Malabar, Lake Poinsett, Geneva/Lake Harney, DeLand riverfront), carried by the mandatory flood-history disclosure (689.302, since 10/1/2025) | Space Coast MLS Nov (~mid-Dec) through spring | direction ~75%; size UNKNOWN | Buyers discount little in a falling-rate market | HOMER's ZIP-level listing/price-cut read |
| Counties to watch, in order | — | — | — | Brevard (epicentre, two events, low take-up) · Seminole and Volusia (river crest moving downstream, take-up 4% and 11%) · Broward (17.59 in, core condo metro) · Martin/St. Lucie (66 homes damaged in Martin, press) · Putnam (2.6% take-up, coastal warning) |

**Needed from HOMER (its lane):** ZIP-level listings, price cuts and withdrawals for the flooded ZIPs; whether the flood-disclosure form shows up in pending-sale fall-through; agency vs non-agency share in Brevard condo/TH.

## 4. Question 3 — HOAs and condominium associations

### Established (law and agency rules)

| Rule | Text / figure | Date | Basis |
|---|---|---|---|
| SIRS deadline | Default 12/31/2025; an association whose milestone inspection is due by 12/31/2026 may do them together; **"In no event may the structural integrity reserve study be completed after December 31, 2026"** | 718.112(2)(g)7, 2026 statutes | PRIMARY ✔ |
| Milestone inspection | Buildings of three habitable stories or more; first by 12/31 of the year the building turns 30, then every 10 years; 25 years near the coast is a local option; buildings 30+ before 7/1/2022 were due 12/31/2024; local extension for good cause | 553.899, 2026 | PRIMARY (helper) |
| Reserve pause (HB 913, 2025) | For budgets adopted by **12/31/2028**: after a milestone inspection in the prior 2 years, a majority of all voting interests may pause or reduce reserves for up to 2 budgets; SIRS before resuming; reserves may be funded by loan or credit line with majority approval | 718.112, 2026 | PRIMARY (helper) |
| 2026 session | No change to SIRS, milestone or reserves; condo omnibus HB 657 / SB 1498 died 3/13/2026; ch. 2026-14 (SB 104) technical | flsenate.gov | PRIMARY (helper; 2026-14's 718.112 text not read) |
| Association flood insurance | **Optional**: the association "may also obtain and maintain … flood insurance" | 718.111(11), 2026 | PRIMARY ✔ |
| NFIP association policy (RCBAP) | Building cover to $250K × units | FEMA RCBAP summary | PRIMARY (helper) |
| Fannie/Freddie 8/3/2026 | Limited Review (Fannie) / Streamlined Review (Freddie) ended; Fannie says this ends its remaining Florida geographic restrictions; a lender relying on a reserve study must confirm the budget funds the study's highest recommended amount ("baseline" method no longer allowed) | LL-2026-03 / Bulletin 2026-C (3/18/2026) | PRIMARY text via a lender-hosted copy (helper) |
| Reserve test | **10% → 15% for applications on/after 2027-01-04** | LL-2026-03 | PRIMARY (CORAL record, CATO `a0fb85230`) |
| Master-policy deductible | ≤ $50,000 per unit for applications from 7/1/2026; HOA in bankruptcy/receivership ineligible (B4-2.1-03) | Fannie | PRIMARY (helper; CORAL record) |
| Fannie unavailable-project list, Florida | **UNKNOWN for 2026**; last public count 1,438 FL buildings, ~700 tri-county (Real Deal, 4/2025, SUMMARY) and now stale after 8/3 | — | — |
| Citizens condo-association policies | Commercial residential; **outside** the personal-lines flood mandate | 627.351(6)(aa) | PRIMARY ✔ (inference from scope "personal lines residential") |

### Established (market and stress observations)

| Item | Figure | Date | Basis |
|---|---|---|---|
| Statewide condo | Oct median $290K (−3.3%), 8.0 months, financed condo −8.34% vs SF −12.43% (CORAL-02 FALSE) | FL Realtors 11/16 | CORAL record (STATUS) |
| Tri-county condo/TH (Miami MSA) | 2,537 sales (−7.6%), median $315,500 (−4.4%) | Oct 2026 | FL Realtors metro PDF (helper, column order inferred) |
| Miami-Dade condo | 907 sales (−10%), $397,500 (−1%) | Oct 2026 | SUMMARY (broker relay) — MIAMI REALTORS refused automated access (403), **not read** |
| Association stress Sep–Nov | **No named special assessment, association loan default, receivership or buyout found** in press search; association bankruptcies ≥9 since 1/2025 (CORAL 9/28, ungraded) | 11/23 | helper search; CORAL record |
| Flood damage to a named association | **None found.** Hollywood apartment complex evacuated (90+ residents, name only in a URL, unconfirmed); 72 h ~15.4 in Sunrise/Hollywood/Plantation (CBS Miami 11/19) | 11/19 | PRESS |
| Association lender books | USCB condo-association commercial $66.252M, NPL 0.33% (Q3 10-Q, CORAL 11/06); Avidia association loans $491.9M (Q3 release); BKU HOA deposits $2.4B | Q3 2026 | CORAL record |

### The combination — where inspection/reserve cost and flood cost meet

| Building type | Inspection & reserve cost (law) | Flood exposure (Nov 2026) | Insurance | Stack |
|---|---|---|---|---|
| SE FL (Broward, Palm Beach, Miami-Dade) 3+ story condo, 30+ years, outside SFHA, no RCBAP | SIRS due ≤12/31/2026; milestone repairs; reserves fully funded unless paused; lenders need ≥15% from 1/4/2027 | Pluvial flood 11/17–19 (17.59 in max), watch again 11/24–25 | Flood optional and likely absent outside mapped zones (inference); deductible ≤$50K/unit to stay agency-eligible | **Highest**: uninsured common-element repair joins the SIRS-funded bill in the same budget year |
| Same, inside SFHA with RCBAP | same | same | RCBAP pays to $250K × units after deductible | Medium: flood partly insured; still SIRS |
| Brevard / Volusia / Seminole riverfront and canal condos and HOAs | SIRS applies only to 3+ story condos; most single-family HOAs carry no SIRS | River flood of record, homes flooded at 17.2 ft, water held ≥18.5 ft to 11/28 | Low take-up (Brevard 11.8%, Seminole 4.0%) | Household-level (owners), HOA common areas small |
| Ordinary HOA (single-family subdivision) | No SIRS/milestone (condo-only law) | Streets, ponds, amenities | HOA policies rarely carry flood | Low to the association; high to owners' houses |

**Where it shows first, in order (expected):**

| Observable | First date | What it would show | Reachability |
|---|---|---|---|
| Older-building condo listings and price cuts in Broward / Miami-Dade | MIAMI REALTORS / Broward November report ~mid-Dec | supply up, realization down in 30+ yr stock | ⛔ MIAMI REALTORS refuses automation (403, helper 11/23): needs Will or HOMER by another route |
| Special-assessment notices / board minutes | rolling | assessment size, flood line items | not public; DBPR request route closed (WQ-668 B) |
| SIRS completion compliance at 12/31/2026 | 1/2027 | how many buildings miss the hard deadline | DBPR building reporting (not read this session) |
| Agency-eligibility failures (reserve 15%, deductible $50K) | applications from 1/4/2027; FL Realtors Jan (≈2/2027) | financed condo share falling vs SF | CORAL WQ-704 series (FL Realtors Dec print 12/16 for Nov) |
| Association delinquencies → association loans | USCB Q4 release ~late Jan 2027; Avidia 10-K ~Mar 2027 | past-dues in the association book | public, quarterly |

**Expected:** no association-loan credit signal in Q4 2026 prints (~80%): associations spread assessments over years and borrow to do it, so the first stress is in listings and prices of older buildings (Dec–Feb), then delinquency (2027). Alternative: a cluster of flood-hit associations in Broward forced into emergency assessments, showing in USCB's association book by Q1 2027 prints (Apr 2027). What would change my mind: a named Broward/Palm Beach association with flood damage plus an assessment; any past-due in USCB or Avidia association segments.

## 5. Question 4 — tradeability (WQ-696 form; sent to TERRY)

| Instrument family | Price evidence (live, CORAL pull 16:44 ET 11/23; closes since 10/30 via yfinance) | Implication |
|---|---|---|
| FL banks | USCB $19.72 (−0.8% since 10/30) · BKU $41.77 (−2.9%) · SBCF $31.95 (−3.3%) · SSB $100.43 (−4.5%) · KRE $69.54 (−3.4%) · SPY −4.4% | Moving with the index; no flood-specific pricing; county CRE exposure **unestablished** (REGINALD's lane; CATO FF23-1) |
| FL home insurers | UVE $49.29 (+1.6%) · HCI $191.91 (−3.0%) · HRTG $32.54 (−8.7%) · ACIC $9.91 (−9.2%) | Split; causes not isolated; flood excluded from their policies |
| Muni (Brevard, Palm Bay, Jacksonville) | not reachable free (BOND 11/18: EMMA 403) | none |

**WQ-696 statement:** the evidence supports **no investment implication tonight**. Why: the insured loss sits with the federal flood program and households, not with listed Florida insurers or banks; bank exposure by county is undisclosed; the condo stack is a mechanism with no named case. **Horizon** of the first test: Q4 bank releases (late Jan 2027) and the 1/1/2027 Citizens flood mandate. **What would create one:** a named association default or a past-due line in USCB/Avidia association books; a Citizens or OIR figure for policies forced to add flood (cost to households, and whether they leave Citizens for takeout carriers that do not require flood — a possible policy-count tailwind for UVE/HCI-type takeout carriers, unestablished); a federal denial plus county borrowing. **Unknown:** the uninsured dollar loss; how many Citizens PR-M policies already carry flood; NFIP's 12/11 fate.

## 6. Search limits (what was looked for, where, and what refused)

| Source | Result |
|---|---|
| MIAMI REALTORS county reports | ⛔ **403 to automation** (helper, 11/23) — stopped, no workaround; Miami-Dade figure above is a broker relay only |
| Citizens press releases | JavaScript-rendered, not extractable; 2027 rate recommendation not found |
| Citizens takeout stats PDF | last modified 10/26; no November round shown |
| Insurance Insider (Citizens CEO) | paywall; not opened |
| OpenFEMA NfipPolicies v3 | no county field; RCBAP (association) policy count by county not derived |
| OIR newsroom | not read directly (rate figures are press summaries) |
| County/city flood spending (Brevard, Palm Bay, Rockledge, Seminole, Volusia agendas) | **not checked this session** |
| FDEM request letter | not read |
| Guy Carpenter 2027 outlook PDF | not opened |
| Event-2 Brevard rain total | not received from AEOLUS |
