# United Fidelity Bank: who borrowed the multifamily loans (sample of 14 properties)

Researcher: read-only public-source agent for PROME. All sources were read on 2026-11-11 (about 19:00 to 20:20 ET).
Tags: VERIFIED (I read the record itself) · INFERRED · SEARCH-NOT-FOUND (a statement about my search, not proof of absence) · UNKNOWN.
**Important limit:** I did **not** read any recorded mortgage. Every county official-records system I tried blocked automated access (details below). The lien evidence here comes from **Florida state UCC-1 fixture filings**, which name United Fidelity Bank, fsb (UFB) as secured party and are labelled "first / second / third / senior mortgage". These are public filings made alongside the mortgages, but they are not the mortgages. So recorded mortgage amounts, maturity dates, modifications, lis pendens and foreclosures are all **UNKNOWN**.

## Five-line answer

1. **Mostly Pedcor-related borrowers, plus a second sponsor group that co-invests with Pedcor.** I matched 14 of UFB's HMDA multifamily loan sets to a property by census tract, then by owner. **9 of the 14** are owned by entities whose recorded owner address is Pedcor's headquarters (One Pedcor Square / 770 3rd Ave SW, Carmel IN). One more is co-owned (24.99%) by a Pedcor Investments partnership. **3** are owned by "New ___ LLC" entities at 8902 N Meridian St Ste 205, Indianapolis, the office of an unrelated-looking sponsor group. **1** has an unidentified sponsor. The Alachua loan remains unmatched.
2. **UFB's own lien filings were prepared by Pedcor.** For **7** properties I read UCC-1s naming UFB as secured party, filed June 2021 to Aug 2022 (VERIFIED). On all **5** whose cover page I viewed, the filer contact and acknowledgement address is a Pedcor employee at One Pedcor Square. That includes the two borrowers *not* at a Pedcor address (New Lakeridge LLC, Cypress West Owner LLC).
3. **They are acquisitions of older, existing apartment complexes, not new construction.** Year built ranges from 1974 to 2005 for every Florida property. Two press items document the purchases: Pedcor Homes Corporation bought The Westcott (Tallahassee, 444 units) in 2022 (Berkadia) and 3531 Plantation Way (Naples, 188 units) in 2020 for $24M. HMDA nonetheless reports 100% of units as income-restricted on most of these loans. I found no recorded state housing-agency restriction to confirm it, because the county records were blocked.
4. **The UCC record shows a deliberate first/second/third-lien stack, no outside transfer, and continued upkeep.** The pattern is one first plus two junior liens per property. At Kings Mill and Oakleigh (Pensacola) and FWB-Greens, one junior lien was terminated in May 2024; the Kings Mill termination is labelled "Release of Third Deed of Trust". On the FWB properties, UFB continued its filings in September 2026. **No UCC shows an assignment to another lender, a Federal Home Loan Bank (FHLB) or a trustee** (VERIFIED for the 7 filings' histories).
5. **Distress at the named properties is unchecked.** I ran no property-specific news or court search inside the budget; the only searches were for the entity names, and they returned no distress items. Mortgage modifications, lis pendens and foreclosures could not be checked: Escambia, Leon and Miami-Dade block automated access, Collier is an interactive app, and Lee and Alachua timed out. A human with a browser can settle this in about an hour using the instructions below.

## Loan-by-loan table

HMDA amounts are bin midpoints (±$5K) from the 2021–2025 HMDA files at `PROME/reports/2026-11-11_united-fidelity-follow-up/hmda/`. "Property match" means the only large multifamily parcel(s) in that census tract owned by the named entity, found by intersecting the Census 2020 tract polygon (TIGERweb ACS2022 layer 6) with county parcel data. A tract match is INFERRED unless a UCC names the entity.

| # | County · HMDA loan(s) | Borrower entity (evidence) | Related party? and evidence | Property (parcel data) | Recorded maturity | Junior lien to UFB? | Later UCC events | Other recorded parties |
|---|---|---|---|---|---|---|---|---|
| 1 | Leon FL · 2022 $77.9M 1st + $16.3M 2nd, 3.25%, 120 mo, PV $111.4M | **TALLAHASSEE-WESTCOTT, LLC**. UCC-1 20220211371X ("SENIOR MORTGAGE") and 202202113728, filed 2022-06-28, secured party UFB (VERIFIED, FL UCC registry) | **Pedcor-related.** Debtor address on the UCC is 770 3rd Ave SW, Carmel. Pedcor Homes Corporation bought the property: Berkadia release dated 2022-08-05 (VERIFIED secondary). UCC filed by a Pedcor contact (VERIFIED) | The Westcott, 3909 Reserve Dr, Tallahassee; 300 + 144 units, built 2000 and 2005; 2026 just value $42.1M + $20.2M (FDOR statewide parcels) | UNKNOWN | Yes: 2 UCCs, matching HMDA 1st + 2nd | none on record | none on UCC record |
| 2 | Escambia FL · 2022 tract 12033003507: one of the two sets {$42.8M + $9.2M + $2.0M, 3.35%, 72 mo} or {$38.5M + $8.3M + $0.9M, 3.25%, 120 mo} | **PENSACOLA-KINGS MILL, LLC**. UCC-1s 202201892928 ("FIRST MORTGAGE"), 202201892936 ("SECOND"), 202201892944 ("THIRD"), filed 2022-06-08, secured party UFB (VERIFIED) | **Pedcor-related.** Debtor address 770 3rd Ave SW, Carmel; parcel owner address One Pedcor Square; UCC filed by a Pedcor contact (VERIFIED). A Pedcor-site page says Pedcor acquired Kings Mill and Crestview at Oakleigh (search snippet only; not fetched) | Kings Mill Apts, 8917 N Davis Hwy, Pensacola; 200 units, built 1998; just value $28.5M | UNKNOWN | Yes: 3 UCCs, matching HMDA 1 + 2 | **Third lien terminated 2024-05-15** (UCC3 202401306070, filer ref "Release of Third Deed of Trust") | none |
| 3 | Escambia FL · the other 2022 set in tract 003507 | Candidate **PENSACOLA-SI LLC** (parcel owner; INFERRED) | Pedcor address: parcel owner at One Pedcor Square | 2220 Gloria Cir, Pensacola; 184 units, built 2004; just value $26.7M | UNKNOWN | UNKNOWN | SEARCH-NOT-FOUND: no FL UCC under "PENSACOLA-SI" | UNKNOWN |
| 4 | Escambia FL · 2022 tract 12033003511, $35.8M + $7.7M + $1.6M, 3.35%, 72 mo, PV $51.1M | **PENSACOLA-OAKLEIGH, LLC**. UCC-1 202201864118 ("FIRST MORTGAGE"), 202201859327, 202201859335, filed 2022-06-06, secured party UFB (VERIFIED) | **Pedcor-related** (770 3rd Ave SW debtor address) | Crestview at Oakleigh, 8990 N Davis Hwy; 176 units, built 1996; just value $26.3M | UNKNOWN | Yes: 3 UCCs, matching HMDA 1 + 2 | One terminated 2024-05-15 (UCC3 202401306062) | none |
| 5 | Collier FL · 2023 $22.3M + $4.8M, 4.0%, 120 mo, PV $31.8M | Candidate **NAPLES 701 OWNER LLC** (parcel owner "% PEDCOR COMPANIES, CARMEL"; INFERRED) | Pedcor address. Pedcor Homes bought 3531 Plantation Way for $24M in Nov 2020 (Business Observer, via search snippet; not fetched) | 3531 Plantation Way, Naples; 188 units, built 1984; just value $19.0M | UNKNOWN | UNKNOWN | SEARCH-NOT-FOUND: no FL UCC under "NAPLES 701 OWNER" | UNKNOWN |
| 6 | Okaloosa FL · 2021 tract 12091021700, $12.2M + $2.6M + $0.5M, 3.22%, 84 mo | **FWB-GREENS, LLC**. UCC-1 202108701301, 20210870131X, 202108701298, filed 2021-10-06, secured party UFB (VERIFIED) | **Pedcor-related by address**: parcel owner mail is 770 3rd Ave SW. The debtor address on the UCC is 3024 Club Dr, Miramar Beach FL. UCC filed by a Pedcor contact (VERIFIED) | 5 Mooney Rd, Fort Walton Beach; built 1983; just value $9.8M (HMDA: 50–99 units) | UNKNOWN | Yes: 3 UCCs | One terminated 2024-05-03; **two continued 2026-09-08** (UFB keeping them in force) | none |
| 7 | Okaloosa FL · 2021 tract 12091022001, $12.6M + $2.7M + $0.4M, 3.22%, 84 mo | **FWB-ELEVATE, LLC**. UCC-1 202108701328, -336, -344, filed 2021-10-06, secured party UFB (VERIFIED) | Pedcor-related by address (parcel owner mail 770 3rd Ave SW) | 600 Denton Blvd, Fort Walton Beach; built 1974; just value $9.6M | UNKNOWN | Yes: 3 UCCs | **All three continued 2026-09-01** | none |
| 8 | Miami-Dade FL · 2022 $46.9M + $5.9M, 3.5%, 72 mo, PV $67.0M; HMDA affordable units = NA | **NEW LAKERIDGE, LLC**. UCC-1 202202537579 ("SENIOR MORTGAGE") filed 2022-08-04 and 202202550966 filed 2022-08-05, secured party UFB (VERIFIED) | **Not at a Pedcor address.** Debtor is at 8902 N Meridian St Ste 205, Indianapolis. A sister entity at that address, New Crawford Crossing LLC, lists **BH Manager, LLC** among its managers (KY SOS annual report 2022-06-09, VERIFIED). New Lakeridge's own managers are UNKNOWN. **But the UCC was filed by a Pedcor contact** (VERIFIED) | 17200 NW 64 Ave, unincorporated Miami-Dade; 175 units, built 1991; just value $32.0M | UNKNOWN | Yes: 2 UCCs | none | none |
| 9 | Lee FL · 2022 tract 12071001711, $38.3M + $4.5M, 3.45%, 72 mo, PV $54.8M | **CYPRESS WEST OWNER, LLC**. UCC-1 202200432125 ("SENIOR MORTGAGE") and 202200432117, filed 2022-02-09, secured party UFB (VERIFIED) | **UNKNOWN.** Debtor address on the UCC is 532 Dorset Boulevard (city not legible in my crop); the parcel owner address is the property itself. UCC filed by a Pedcor contact (VERIFIED) | 6308 Panther Ln, Fort Myers; 200 units, built 1975; just value $32.5M | UNKNOWN | Yes: 2 UCCs | none | none |
| 10 | Hamilton IN · 2022 $63.7M, tract 18057110513 | Candidate **Noblesville SI LLC** (parcel owner; INFERRED) | Pedcor address (One Pedcor Square) | 15001 Creek Stone Way, Noblesville; built 2017; last transfer 2022-09-20; AV $53.0M (Hamilton County GIS) | UNKNOWN | UNKNOWN | not checked (no IN UCC access) | UNKNOWN |
| 11 | Hamilton IN · 2022 $58.1M, tract 18057110600 | Candidate **TB Northlake LLC** (INFERRED) | Pedcor address (One Pedcor Square) | 1100 Northlake Dr, Noblesville; built 1983/1985; transfer 2022-11-23; AV $23.0M + $17.4M | UNKNOWN | UNKNOWN | — | — |
| 12 | Hamilton IN · 2022 $57.6M, tract 18057110301 | Candidate deeded owner "**New Flats at Springmill Station LLC 75.01% int & Pedcor Investments 2000 XLI LP 24.99% int**", tenants in common (INFERRED match) | **Mixed:** a "New ___" entity plus a Pedcor Investments partnership; owner mail 770 3rd Ave SW | 15950 Spring Mill Depot Dr, Westfield; built 2021; **last transfer 2026-02-23**; AV $46.5M | UNKNOWN | UNKNOWN | — | — |
| 13 | Hamilton IN · 2022 $55.3M, tract 18057110811 | Candidate **New Sanctuary LLC** (INFERRED) | Not a Pedcor address: 8902 N Meridian Ste 205 (same office as New Lakeridge) | 11400 Gables Dr, Fishers; built 1995; transfer 2022-10-05; AV $45.7M | UNKNOWN | UNKNOWN | — | — |
| 14 | Franklin OH · 2022 $43.5M, tract 39049006386 | Candidate **NEW DUBLIN SQUARE LLC**. It holds 354 condo-rental parcels in the tract; I cannot tie the loan to it over the other large owner there (Sycamore TIC 1 LLC, 270 parcels). INFERRED, weak | 8902 N Meridian St Ste 205 group (mailing on 4 parcels) | "Dublin Square", Dublin OH; transfer recorded 2025-01-24 (Franklin County Auditor GIS) | UNKNOWN | UNKNOWN | — | — |

Not matched: **Alachua 2022 $48.4M + $10.4M** (tract 12001001515; HMDA affordable units NA, PV $69.2M). The large owners in that tract are Gainesville Place / Gainesville Place Phase II / Oxford Manor / Hidden Village (all at 220 N Main St, Gainesville). Their FL UCC histories show only Freddie Mac/Fannie Mae, CMBS trustees, Wells Fargo and Computershare as secured parties, with **no UFB filing** (SEARCH-NOT-FOUND for UFB). The match is UNKNOWN.

Also seen, but not tied to a loan: **Golf Pointe Property Owner LLC** (One Pedcor Square), which owns 227 condo-rental parcels in Franklin County OH, with a transfer recorded 2025-01-23 and tax bills sent to CoreLogic (a lender tax-service address). The 2021 Franklin loan (tract 39049006990) could not be geocoded: HMDA 2021 uses 2010 tracts and my 2020-tract lookup returned nothing.

## Proportions (sample only; do not generalize)

| Borrower group | Lien-verified by UFB UCC (n=7) | All 14 matches |
|---|---|---|
| Pedcor-named or Pedcor-addressed owner | 5 (Westcott, Kings Mill, Oakleigh, FWB-Greens, FWB-Elevate) | 9 (adds Pensacola-SI, Naples 701, Noblesville SI, TB Northlake, all INFERRED) |
| Mixed: "New ___" LLC with Pedcor Investments LP as tenant in common | 0 | 1 (Springmill, INFERRED) |
| "New ___ LLC" at 8902 N Meridian Ste 205 (BH Manager-type group) | 1 (New Lakeridge) | 3 (adds New Sanctuary, New Dublin Square, both INFERRED) |
| Unknown sponsor | 1 (Cypress West) | 1 |

**Caveat on "Pedcor-related":** this rests on owner and debtor **addresses** (Pedcor HQ) and on Pedcor's documented purchases of The Westcott and Naples. It does not rest on registry manager records: Florida Sunbiz returned a Cloudflare challenge, and the Ohio and Indiana registries were blocked or unavailable. Whether these LLCs are owned by Pedcor Homes Corp, by UFB's subsidiaries (Village Capital Corporation, Pedcor Housing Corporation) or by Pedcor principals personally is **UNKNOWN**, and it matters for affiliate-lending rules.

**The Pedcor-filed UCCs** are a fact about who handled UFB's loan paperwork, not proof of ownership. They show that Pedcor staff also documented the bank's loans to non-Pedcor-address borrowers (New Lakeridge, Cypress West). The "New ___" group co-owns at least one property with a Pedcor partnership.

## Other observations (facts, with their limits)

- **Florida just values sit well below HMDA property values.** Westcott $62.4M vs $111.4M; Oakleigh $26.3M vs $51.1M; New Lakeridge $32.0M vs $67.0M; Cypress West $32.5M vs $54.8M; Naples 701 $19.0M vs $31.8M. Florida assesses rent-restricted property on a restricted-income basis and grants affordable-housing exemptions, so just value is **not** market value. This is not evidence of impairment (INFERRED caution).
- **Florida's documentary stamp box is ticked "paid"** on the Kings Mill UCC. That is routine for a filing that relates to a recorded mortgage.

## What was unreachable, and exact steps for a human with a browser

| Site | Result here | Human steps |
|---|---|---|
| Escambia Clerk Official Records (dory.escambiaclerk.com/LandmarkWeb) | HTTP 403, Cloudflare challenge | Open in a browser and accept the disclaimer. Name search **PENSACOLA-KINGS MILL LLC**, then **PENSACOLA-OAKLEIGH LLC**, then **PENSACOLA-SI LLC**, dates 01/01/2022–today, document types MTG, MOD, ASG, SAT, LP, UCC. Read the mortgages around 06/06–06/08/2022 for amount, maturity, guarantors, and any Land Use Restriction Agreement or Extended Use Agreement |
| Leon Clerk Official Records (cvweb.leonclerk.com) | HTTP 403 (Akamai) | Party search **TALLAHASSEE-WESTCOTT**, from 06/2022 |
| Miami-Dade Clerk Official Records (onlineservices.miamidadeclerk.gov/officialrecords) | Turnstile CAPTCHA (not attempted) | Standard search, party **NEW LAKERIDGE LLC**, from 07/2022 |
| Collier Clerk COR Access (cor.collierclerk.com/coraccess) | Blazor app, not drivable by requests | Name **NAPLES 701 OWNER LLC**, 2020–today (should show the 2020 deed and the 2023 UFB mortgage) |
| Lee Clerk (or.leeclerk.org/LandMarkWeb) | Connection timed out; leeclerk.org returned 403 | Name **CYPRESS WEST OWNER LLC**, from 01/2022 |
| Alachua Clerk (alachuaclerk.org official records) | Timed out | Grantee **UNITED FIDELITY BANK**, 2022 (to find the unmatched $48.4M loan) |
| Okaloosa Clerk | not tried | Names **FWB-GREENS LLC** and **FWB-ELEVATE LLC**, 2021 onward |
| Florida Sunbiz (search.sunbiz.org) | Cloudflare challenge | Entity search for each LLC above. Read the manager/authorized-member lines and the principal address |
| Franklin County OH Recorder and franklincountyohio.gov | HTTP 403 | Recorder search **NEW DUBLIN SQUARE LLC** and **GOLF POINTE PROPERTY OWNER LLC**. Ohio SOS business search returned a 403 "maintenance" page |
| Hamilton County IN Recorder; Indiana INBiz | Not attempted (JavaScript app; Hamilton recorder may be a paid portal) | INBiz business search for Noblesville SI LLC, TB Northlake LLC, New Sanctuary LLC, New Flats at Springmill Station LLC (registered agent, governing persons). Hamilton County Recorder for mortgages to United Fidelity Bank, 2022 |
| Leon Property Appraiser PDF (search.leonpa.gov) | HTTP 403 | Not needed; FDOR statewide parcel data covered it |

What worked:
- the FDOR statewide parcel feature service: services9.arcgis.com/Gh9awoU677aKree0/.../Florida_Statewide_Cadastral/FeatureServer/0 (2026 roll);
- Census TIGERweb tracts;
- the Florida UCC public search API: publicsearchapi.floridaucc.com, endpoints /search, /filing-details, /filing-history and /filing-image (TIFF images read for 10 filings);
- the Franklin County Auditor GIS (gis.franklincountyohio.gov/hosting/.../Parcel_Features/MapServer/0);
- the Hamilton County IN GIS (gis1.hamiltoncounty.in.gov/arcgis/rest/services/HamCoParcelsPublic/MapServer/0);
- Berkadia's news page;
- the KY SOS corporate scan.

Local working files are in this folder: parcels_fl.txt, parcels_fl2.txt, ucc_run1.txt, ucc_run2.txt, hamilton.txt, franklin2.txt, and img/ (UCC images).

## Sources

- Florida UCC registry (FSTR), publicsearchapi.floridaucc.com. Filings listed in the table, with filing dates as shown; filings completed through 2026-11-09; read 2026-11-11. Cover-page images viewed: 202201892928, -936, -944, 202201864118, 20220211371X, 202202537579, 202200432125, 202108701301, 202401306070, 202602794897.
- FDOR statewide cadastral (2026 assessment roll), read 2026-11-11.
- Berkadia, "The Westcott, Tallahassee, FL, sold by Berkadia 2022", https://berkadia.com/news/the-westcott-tallahassee-fl-sold-by-berkadia-2022/ (release dated 2022-08-05), read 2026-11-11.
- Search-engine snippets only (pages not fetched): Business Observer, 2020-11-11, https://www.businessobserverfl.com/news/2020/nov/11/firm-sells-multifamily-complex-for-dollar24m-one-month-after-dollar48m-sale (Pedcor Homes buys 3531 Plantation Way from JWC Naples 701 LLC, $24M); a Pedcor "Jacksonville and Pensacola Acquisitions" page on an AWS mirror host (deliberately not fetched).
- Kentucky SOS annual report, New Crawford Crossing, LLC, filed 2022-06-09, https://web.sos.ky.gov/corpscans/96/1109696-06-99999-20220609-ARP-8910066-PU.pdf, read 2026-11-11.
- Hamilton County IN GIS parcels, and Franklin County OH Auditor GIS parcels, read 2026-11-11.

## Open unknowns

- Recorded mortgage terms (face amount, maturity, rate resets, guarantors), modifications or extensions, lis pendens and foreclosure filings, for every property. **The county records are the gap.**
- Whether any recorded land-use restriction agreement or extended-use agreement (with a state housing agency) exists. This would show whether these older acquisitions are genuinely income-restricted, as HMDA reports.
- The managers of every LLC above (Sunbiz, INBiz and Ohio SOS were not reachable). In particular, whether the Pedcor-addressed owners are held by UFB subsidiaries or by Pedcor principals, and who controls Cypress West Owner LLC.
- Which of the two Escambia 003507 loan sets is Kings Mill. Whether Pensacola-SI LLC is the other, given no UFB UCC under that name.
- Why the Springmill Station deed transferred on 2026-02-23, and the Dublin Square and Golf Pointe deeds in January 2025. These could be restructurings, the "sold to related-party partnerships" pattern the bank describes, or unrelated events. UNKNOWN.
- 2025–2026 news or court records of distress for the named properties: **not searched** (budget). The next step is a search on each property name and address; court dockets are on each county clerk's case search.
