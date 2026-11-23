# Flooded homes to recorded lenders: Silver Pines Estates, Rockledge (Brevard), St. Johns River flood, November 2026
**Date:** 2026-11-23 (work 17:20 to 18:10 ET, times from `date`) | **Mode:** Cold, commissioned by PROME (Florida flood transmission sweep, DOCKET row dated 2026-11-24; Will's word 2026-11-23 16:26 and 16:33 ET) | **Confidence:** High on records read; Medium on the flood link (NWS stage-impact, not a damage survey); Low on today's holder of each loan

## Key finding
A named basin subdivision can be traced from flood to recorded debt with free records. In a seeded sample of 20 single-family homes in Silver Pines Estates (Rockledge), which the National Weather Service names as a place where water enters low-lying homes at 17.2 ft on the St. Johns near Cocoa (stage 18.6 ft on 11/23), 13 carry a recorded mortgage tied to the parcel's legal description: 8 of the 10 inside FEMA's mapped flood zone and 5 of the 10 outside it. The originators of record are mostly non-bank lenders (6 of 13 first liens) and government-insured loans (at least 4 of 13 FHA, 1 VA inferred), with three banks (Fifth Third, SunTrust Mortgage, PrimeLending) and one credit union (Space Coast) as originators. No foreclosure filing since 2014 was found in the sample. Three of the 13 carry a recorded HUD subordinate mortgage of the kind FHA uses for partial claims, one of them recorded 2026-05-06, six months before the flood.

⚠️ The recorded lender is the originator of record, not necessarily today's holder. Loans are sold and serviced by others; the MERS system hides assignments from the county index (3 of 13 first liens show only MERS as nominee). Nothing here says who holds these loans today.

## The chain (each link labelled)

| Link | Evidence | Label |
|---|---|---|
| Hazard: river above home-flooding stage | NWS Melbourne Flood Statement, 947 AM EST Mon 2026-11-23, St. Johns River near Cocoa: stage 18.6 ft at 8:15 AM, 24-h max 18.7 ft, "approaches the flood of record", steady near 18.5 to 18.6 ft through late week. NWPS gauge COCF1 observed 18.59 ft at 21:15Z 11/23 [PRIMARY: api.weather.gov product fcdaa809-9452-447f-bdd1-3a1bbed94dc7; api.water.noaa.gov/nwps/v1/gauges/COCF1, pulled 17:22 ET] | CONFIRMED |
| Place named: Silver Pines | Same statement's IMPACTS line: "At 17.2 feet, Water enters homes along the St Johns River in the Lake Poinsett area west of Cocoa, also low lying homes in the Silver Pines subdivision in Rockledge and the Shakespeare Park area of Cocoa." At 17.0 ft: "water approaching low lying homes in the Silver Pines subdivision in Rockledge" | CONFIRMED that NWS names it |
| Homes in Silver Pines actually took water in this event | The impact line is NWS's standing stage-to-impact table, not an observation. No city, county or news report found naming Silver Pines in this event (searches 17:23 and 17:45 ET; WFTV 2026-11-05 says Brevard officials were watching "low-lying areas west of Interstate 95 in Rockledge and West Cocoa" without saying homes flooded) | PROXY |
| Which homes are low-lying | FEMA mapped zone used as the stand-in: 32 of 185 single-family parcels have their centre in zone AE (the 1%-a-year mapped flood zone), 59 in shaded X (0.2%), 94 in X (minimal) [PRIMARY: FEMA NFHL layer 28, FIRM panel 12009C0428H effective 2021-01-29; Brevard County GIS parcel layer]. AE parcels sit on Matthew Dr (18), Shepard Dr (10), Judith Ter (3), Lee Ave (1). 20 of 20 sampled points agree between FEMA's service and the county's copy | CONFIRMED (map); PROXY (map zone = flooded) |
| Coverage | Mapped-zone homes with a federally regulated or insured mortgage must carry flood insurance by law; whether a policy is in force on any parcel is not in any free record | UNKNOWN per parcel |
| Debt on the parcel | Brevard Clerk Official Records index, matched on lot, block and subdivision in the recorded legal description (table below) | CONFIRMED (originator of record) |
| Today's holder | FHA and VA loans are usually pooled into Ginnie Mae securities, with FHA or VA insuring the credit loss and the servicer advancing payments; conventional loans usually go to Fannie Mae or Freddie Mac; credit-union and bank second liens are more often kept. None of this is shown for these loans | PROXY |

## Sample design
Population: 185 single-family parcels in the five Silver Pines Estates plats (Brevard County GIS parcel layer, `SUBDIVISION_NAME LIKE '%SILVER PINE%'`, pulled 17:29 ET; one parcel with a confidential address excluded). Stratified by mapped zone at the parcel centre: AE (32) and X (153). Ten drawn from each stratum with Python `random.Random(20261123).sample` over parcels sorted by parcel ID. Owner type from the parcel layer's owner name (individual 157, company 17, trust 11 across the population; 114 of 185 carry a homestead exemption). Owner names were used only as transient search keys and are not recorded here.

## Results by parcel (most recent recorded mortgage first; amounts as recorded; book/page in Brevard Official Records)

| Stratum | Parcel | Street | Owner type | Recorded mortgage(s) matched to the lot | Originator of record (type) | Note |
|---|---|---|---|---|---|---|
| AE | 25 3617-25-K-3 | Judith Ter | individual, homestead | 2021-10-18, $160,000, OR 9294/2606 | Space Coast Credit Union (credit union) | Also 2022-11-21 $500,000 to Palmetto Surety Corp (private, a surety's collateral mortgage, not a home loan) |
| AE | 25 3617-03-E-8 | Matthew Dr | individual | 2023-08-03, $324,022, OR 9854/1001 | Fifth Third Bank NA (bank) | Purchase 2023, $330,000 |
| AE | 25 3617-25-K-2 | Judith Ter | trust | none matched | UNKNOWN | Trust-name search returned no record on this lot |
| AE | 25 3617-05-K-9 | Matthew Dr | individual, homestead | 2012-04-11, $61,646, OR 6576/2214 | SunTrust Mortgage Inc (bank subsidiary, now Truist) | Plus 2021-06-28 $7,392.35 to HUD (subordinate; FHA partial-claim form INFERRED) |
| AE | 25 3617-04-F-7 | Shepard Dr | individual | 2022-12-29, $63,800, OR 9687/305 (second lien) | Launch Credit Union (credit union) | First lien 2019-04-18 $175,000, MERS as nominee; lender read from the document: Mortgage Research Center LLC dba Veterans United Home Loans (non-bank); VA loan INFERRED from the case number |
| AE | 25 3617-03-E-5 | Matthew Dr | individual | 2003-12-30, $77,400, OR 5159/2324 | Countrywide Home Loans Inc (non-bank, legacy) | May be paid off: satisfactions without a legal description were not matched |
| AE | 25 3617-17-M-1 | Matthew Dr | individual, homestead | 2024-11-25, $249,399, OR 10208/1100 | Bayshore Mortgage Funding LLC (non-bank) | Plus 2026-05-06 $9,396.38 to HUD (FHA partial claim INFERRED), 18 months after purchase |
| AE | 25 3617-04-E-20 | Shepard Dr | individual, homestead | none found | none found | Bought 2012 for $44,900 |
| AE | 25 3617-05-K-7 | Matthew Dr | individual, homestead | 2023-10-10, $73,000, OR 9905/2038 | Space Coast Credit Union (credit union) | First lien 2016-09-21 $126,750, MERS as nominee; lender read from the document: PrimeLending, a PlainsCapital Company (bank subsidiary), a Florida housing-bond loan; plus Florida Housing Finance Corp $15,000 (state agency) |
| AE | 25 3617-25-K-1 | Judith Ter | individual, homestead | 2023-01-24, $242,165, OR 9702/692 | Rocket Mortgage LLC (non-bank), MERS as nominee | Document read: "FHA Florida Mortgage" with an FHA case number. CONFIRMED FHA |
| X | 25 3617-03-A-7 | Lee Ave | individual | none found | none found | Bought 2025 for $220,000 |
| X | 25 3617-03-C-8 | Lee Ave | individual, homestead | none matched | UNKNOWN | |
| X | 25 3617-03-E-2 | Matthew Dr | individual | 2020-01-13, $133,500, OR 8636/1234 | MERS as nominee; originator UNKNOWN | Document download timed out 18:03 ET |
| X | 25 3617-17-M-2 | Matthew Dr | individual, homestead | 2014-12-17, $145,500, OR 7267/284 | MERS as nominee; originator UNKNOWN | Document not read |
| X | 25 3617-05-C-23 | Slayton Ave | individual | none found | none found | Bought 2015 for $57,526 |
| X | 25 3617-04-C-9 | Lee Ave | individual, homestead | 2019-11-19, $175,518, OR 8592/50 | MERS as nominee; originator UNKNOWN | Document not read |
| X | 25 3617-03-C-3 | Lee Ave | individual, homestead | none matched | UNKNOWN | |
| X | 25 3617-05-C-26 | Slayton Ave | company | none found | none found | Bought 2016 for $92,000 |
| X | 25 3617-05-K-6 | Matthew Dr | individual, homestead | 2025-04-22, $180,000, OR 10316/854 | Swift Home Loans Inc (non-bank) | Lis pendens 2014-07-29 by Deutsche Bank National Trust Co, trustee (OR 7176/320); a 2013 MERS assignment; outcome not traced |
| X | 25 3617-25-K-22 | Martha Lee Ave | individual, homestead | 2024-04-17, $299,475, OR 10040/1723 | Lower LLC (non-bank) | Plus 2025-06-26 $15,909.47 to HUD (FHA partial claim INFERRED) |

## Counts

| Measure | AE (in mapped zone) | X (outside) | All 20 |
|---|---|---|---|
| Recorded mortgage matched to the lot | 8 | 5 | 13 |
| None found on a matched purchase deed | 1 | 3 | 4 |
| No record matched at all (UNKNOWN) | 1 | 2 | 3 |
| Lis pendens or foreclosure filing since 2015 | 0 | 0 | 0 (one in 2014) |
| HUD subordinate mortgage recorded | 2 | 1 | 3 |

First-lien originator of record, the 13 mortgaged homes: non-bank 6 (Rocket Mortgage, Veterans United, Bayshore Mortgage Funding, Swift Home Loans, Lower, Countrywide), bank or bank subsidiary 3 (Fifth Third Bank NA, SunTrust Mortgage, PrimeLending/PlainsCapital), credit union 1 (Space Coast), MERS with originator unread 3. Second liens: Space Coast Credit Union 1, Launch Credit Union 1, Florida Housing Finance Corp 1, HUD 3. Private: Palmetto Surety Corp 1. Insured: FHA at least 4 (1 CONFIRMED from the document, 3 INFERRED from HUD subordinate liens), VA 1 INFERRED. No Seacoast, SouthState or other basin-concentrated listed bank appears as originator in the sample.

## Counter-evidence and limits
- The flood link is the weakest: NWS's line is a stage threshold for "low lying homes", not a count of flooded homes, and Silver Pines sits several miles east of the river; the mapped zone is a proxy for which homes are low. A street survey or the county's damage-report data would settle it.
- Twenty of 185 is a sample; with 8 of 10 versus 5 of 10, the AE-versus-X difference in mortgage share is not statistically meaningful.
- "None found" can be a miss: the match keys on the recorded legal description; mortgages indexed without one (dropped as unmatchable, since common names pull in unrelated county records) and satisfactions are not counted. Old first liens (2003, 2012, 2014) may be paid off.
- MERS hides the originator in the index and hides all later transfers; the three unread MERS documents need one browser view each.
- The HUD-lien reading (a partial claim after a missed-payment workout) is INFERRED from the lender and amounts; the documents were not read.
- Will's hypothesis that banks will hide losses is not tested by this: the sample's first liens are mostly not bank-held at origination, and where FHA or VA insure the loan the credit loss falls on the federal programme, not a lender's books.

## Source quality
Records are primary (NWS products, FEMA NFHL, Brevard County GIS, Brevard Clerk index and recorded images). The ownership-to-debt matching is mechanical and reproducible; the flood-to-parcel link is a proxy.

## References (accessed 2026-11-23 ET)
- NWS Melbourne Flood Statement 947 AM EST 2026-11-23 (St Johns River near Cocoa): https://api.weather.gov/products/fcdaa809-9452-447f-bdd1-3a1bbed94dc7
- NWPS gauge COCF1: https://api.water.noaa.gov/nwps/v1/gauges/COCF1
- FEMA NFHL MapServer layers 28 and 3: https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer
- Brevard County GIS parcels (layer 4) and FEMA copy: https://gis.brevardfl.gov/gissrv/rest/services/Base_Map/Parcel_New_WKID102100/MapServer/4 ; .../Flood_Hazard/Flood_FEMA_WKID102100/MapServer/0
- Brevard Clerk Official Records (AcclaimWeb): https://vaclmweb1.brevardclerk.us/AcclaimWeb/
- WFTV, 2026-11-05: https://www.wftv.com/news/local/thousands-report-damage-brevard-county-flood-recovery-continues/U4FFZDMKHRFXFLIIS4OYUROZ5Y/

## Process Report
**Searches run:** 3 web searches, 3 page fetches; ~35 GIS and NWS API calls; 21 clerk name searches; 3 recorded-document downloads.
**Routes and where they stopped (client name `research-bot/1.0` throughout):**

| Site | Time (ET) | Response | Disposition |
|---|---|---|---|
| Brevard Property Appraiser, www.bcpao.us (site and API) | 17:22:54, retested 17:30:12 after PROME's network-drop notice | HTTP 403 with `cf-mitigated: challenge` (Cloudflare managed challenge) | STOPPED; not retried further. Its data was reached through the county's own GIS parcel layer instead |
| Brevard County GIS, gis.brevardfl.gov | 17:22 to 17:42 | 200, open ArcGIS REST | used |
| FEMA NFHL, hazards.fema.gov | 17:30, 17:42 | 200 (one query returned empty once, then 200 on retry) | used |
| Brevard Clerk AcclaimWeb | 17:30 to 18:03 | 200 after clicking through the public-records disclaimer (an accuracy and statutory-notice page, no CAPTCHA, no account) | used. One connection reset at about 17:48 (site answered 200 at 17:48:59; one slower retry completed). Document download timed out at 18:03:31; stopped document pulls there |

**Data gaps:** flood-insurance status per parcel; today's holder and servicer; originators behind three MERS mortgages; event-specific damage confirmation for Silver Pines.
**Source frustrations:** the appraiser's challenge page; MERS hides lenders in the index; clerk search is by name only in practice (the legal-description search returned "Error in executing the search").
**If I had more time/tools:** read the three MERS documents and the HUD liens; pull Brevard's self-reported damage data if published by area; repeat the method on Lake Harney (Seminole County, Whitcomb Drive).
**Suggestions:** promote the clerk name-search client to `scripts/` (needs Will's build word; recipe below).

**Reproduction recipe:** (1) parcels: Brevard GIS `Base_Map/Parcel_New_WKID102100/MapServer/4/query` with the subdivision filter above, `outSR=4326`; (2) zones: FEMA NFHL layer 28 envelope query (-80.7536, 28.3090, -80.7422, 28.3167), point-in-polygon at each parcel's polygon centroid, SFHA wins on overlap; (3) clerk: accept disclaimer (`POST /AcclaimWeb/search/Disclaimer`), `POST /AcclaimWeb/search/SearchTypeName?Length=6` with `SearchOnName` = "LAST,FIRST", `BookTypes=3`, `DocTypes` = the deed, mortgage, satisfaction, assignment and lis pendens type codes, then `POST /AcclaimWeb/Search/SearchTypePreName` with the returned name list, then `POST /AcclaimWeb/Search/GridResults`; keep rows whose `DocLegalDescription` matches lot, block and "SILVER PINES"; (4) documents: `GET /AcclaimWeb/Details/Index/<TransactionItemId>`, `GET /AcclaimWeb/Image/StartImageRetrieval/<id>/0`, `GET /AcclaimWeb/Image/DocumentPdfAllPages/<id>`.
