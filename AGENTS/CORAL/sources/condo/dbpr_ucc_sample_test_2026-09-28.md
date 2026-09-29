# DBPR + Florida UCC: small-sample feasibility test for matching association lending records

**Run:** Mon Sep 28 20:11 to 20:23 EDT 2026 (`date`). The file was written after the run finished.
**Method:** read-only public access only. No account was created, no request was submitted, no one was contacted and no fee was paid. Tools: `curl` against the public HTML pages, the DBPR bulk-CSV extracts, and the unauthenticated JSON API that floridaucc.com's own search page calls (`publicsearchapi.floridaucc.com`). Filing images are the free "Document Images" download on that site; I converted TIFF to PNG and read them visually. All DBPR lookups used "Search by Name", with partial-name matching, on board 800 (Condominiums, Cooperatives, Timeshares, & Multi-Site Timeshares) and board 830 (CTMH Other Entities).
**Systems tested:** (A) the Florida DBPR Division of Florida Condominiums, Timeshares and Mobile Homes (CTMH), and (B) the Florida Secured Transaction Registry (UCC), whose data runs through 2026-09-24 per the API field `filingsCompletedThrough`.
**Tags:** [I] = inference. UNKNOWN = not established this session.

---

## Section A: DBPR (what is public)

### A(a) Association/licensee lookup: https://www.myfloridalicense.com/wl11.asp

**The key structural finding:** DBPR keeps the building and the association as two separate license records.
- The **Condominium Project** (license number prefix `PR…`) is the building/regime.
- The **association** is a separate **"Managing Entity"** record (prefix `MA…`) on board 830.
- They are linked on the "View Related License Information" page, where the relationship type is `Managing Entity-Condo` (or `Managing Entity-Timeshare`).
- DBPR's own account tutorial says: *"The managing entity number is unique to the condominium or cooperative association. DO NOT use the building specific project number"* (CTMH Tutorial for Creating an Online Account, PDF).

The pages and fields below are quoted verbatim from what the site returned.

| Page | Verbatim fields shown |
|---|---|
| Search results list | `License Type` · `Name` · `Name Type` · `License Number/ Rank` · `Status/Expires` · `Main Address*` |
| License detail (`/portalsearches/VerifyLicensee/LicenseDetail?ID=`) | `Name` · `Main Address` · `County` · `License Type` · `Rank` · `License Number` · `Status` · `Licensure Date` · `Special Qualifications` · `Qualification Effective` · `Alternate Names` |
| "View Additional Information" (project records only; it errors on MA records: *"Error. An error occurred while processing your request."*) | `Project Summary Information`: `Name`, `Project Number`, `Street`, `Phone` (populated with the project number itself), `City`, `E-Mail`, `State`, `Zip`, `Billing Year`, `Units Recorded`, `Billed`, `Residential Units`, `Penalty`, `Paid`. `Project Detail Information`: `Transaction Described`, `Transaction Number`, `Developer`, `Status`, `Status Code`, `Units Recorded`, `Residential Units`, `Examiner` |
| "View Related License Information" | `License Number` · `Status` · `Related Party` · `Relationship Type` · `Relation Effective Date` · `Rank` · `Expiration Date`. This is where the association (MA#) and the developer (DE#) appear. |

- **Manager:** the lookup does not name a community association manager. The MA record's "Main Address" is often a manager's or PO address (for example Ocean Five, MA64878, at 1680 Michigan Ave, which is the same "c/o Blue Sky Miami" address on its UCC filing).
- **Bulk export: yes, free CSV.** Source page: https://www2.myfloridalicense.com/condos-timeshares-mobile-homes/public-records/
  - "Condominiums by County": five files (`Condo_NF.csv`, `condo_CE.csv`, `Condo_CW.csv`, `Condo_MD.csv`, `condo_PB.csv`), 27,972 project rows downloaded tonight, 23,737 distinct managing-entity names.
  - Verbatim columns: `Project Number, File Number, Condo Name, County, Street City State Zip, Units, Recorded Date, Primary Status, Secondary Status, Managing Entity Number, Managing Entity Name, Managing Entity Route, Managing Entity Street, Managing Entity City, Managing Entity State, Managing Entity Zip`.
  - Coverage per the page: *"Approved, acknowledged and recorded condominium projects and managing entities (terminated, rejected or withdrawn projects are not included)."*
  - Also published: payment history (`paymenthist_8002*.csv`, "Annual Fee Payment history for last 5 years"), conversions, and timeshare lists (`tsmailing.csv`).
- **Identifiers usable for matching:** MA# (association), PR# (project), names, and addresses. **There is no FEIN and no Sunbiz document number in any DBPR field seen.**

### A(b) Building reporting and the SIRS database

- **SIRS Reporting Database.** Page: https://www2.myfloridalicense.com/condos-timeshares-mobile-homes/condominiums-and-cooperatives-sirs-reporting/. There are two public Qlik apps:
  - "SIRS Submitted Prior to July 2025", app `14f1ed21-7b21-4272-af14-9eaad7911440`.
  - "SIRS Submitted July 2025 and After", app `d217126f-2edc-408b-bb98-2c355b6f0429`.
  - Page text: *"Information in the … (SIRS) Reporting Database is displayed exactly as submitted. Only complete submissions of the SIRS Reporting Form are displayed."*
- **"Building reporting for Senate Bill 4 –D"** is a third Qlik app, `a1ab25e1-0aea-46b6-82ee-1829f0ce8ff0`, linked from the public-records page.
- **I could not see the columns or coverage of any of the three apps, so they are UNKNOWN.** The app shell loads (HTTP 200), but the Qlik data connection (websocket `/qpr/app/<id>`) returned **HTTP 403** to every non-browser client I tried, and WebFetch sees only a JavaScript shell.
- **Export:** DBPR's instructions PDF (`Instructions to use the new format.pdf`) says the Qlik reports can be *"exported to Excel … choose Export Data"*. That is browser-only and was not tested.
- **What the SIRS form collects** (from DBPR's `Online Account Instructions for SIRS Reporting.pdf`, "Financial Information" page, verbatim): *"how much did the SIRS cost the association … how much does the association currently have in reserves, the reserve schedule from the SIRS will result in either special assessment, loan, or line of credit or if reserves are sufficient, and what will the amount be of any special assessment, loan, or line of credit."*
  - This form therefore collects a **planned loan or line-of-credit flag and amount, but no lender name.**
  - Whether those fields are displayed in the public database is UNKNOWN (blocked).
- **Identifiers on the SIRS form:** it is filed under the association's MA# account and lists `Project License Number` for each building, so it should join to the PR#/MA# spine [I].

### A(c) Association financial reporting to the Division

1. **The form the outside reviewer described exists.** It is the online-account form **"Building and Assessment Information"** (the Division lists it as required alongside "Association Information" and "Structural Integrity Reserve Study Reporting").
   - Statutory basis: **s. 718.501(3)(c), F.S.** (2026 text on flsenate.gov): *"The association's assessments, including the: 1. Amount of assessment or special assessment by unit type, including reserves. 2. Purpose of the assessment or special assessment. 3. Name of the financial institution or institutions with which the association maintains accounts."*
   - The statute says the information the Division may require *"is limited to"* items (a) through (d). Those items are contacts and board, buildings, assessments with institutions, and a SIRS copy on request. None of them is a loan field.
2. **"Institution" means where the association keeps accounts, not who lent to it.** DBPR's instructions (`Online Account Instructions for Building and Assessment Information.pdf`), verbatim: *"The Financial Institution page is where you list all of the financial institutions that the association maintains an account with."* By that wording this is a list of depository banks [I, from the wording "maintains an account with"; a lender that also holds a deposit account would appear, but not as a lender].
3. **"Reserves collected" is an annual flow, not a balance.** Same PDF, verbatim: *"the total annual amount collected from unit owners excluding reserves, total monetary amount of reserves collected, total number of special assessments issued, and the total monetary amount of special assessments for the current year and for next year's anticipated assessments."* The only reserve balance question I found is on the separate SIRS form ("how much does the association currently have in reserves").
4. **Is Building and Assessment data public? No published dataset found.** Nothing on the CTMH public-records page or the SIRS page exposes it. Whether it can be obtained by a Chapter 119 public-records request is UNKNOWN (not requested, per instructions).
5. **The one published financial dataset covers timeshares, not condos.** `keyfinancialindicators.csv` has 1,883 rows and 401 managing entities, with fiscal years 2020 to 2026.
   - Verbatim columns: `Managing Entity, Fiscal Year End, Total Revenue, Operating Fund, Total Expenses, Operating Fund, Total Revenue, Replacement Fund, Total Expenses, Replacement Fund, Fund Balance, Operating Fund, Fund Balance, Replacement Fund`.
   - 370 of the 401 names appear in the timeshare list `tsmailing.csv`; only 5 appear as condo managing-entity names. It is timeshare-only in practice [I].
   - In the sample only OIRC appears, for fiscal years 2021 to 2023. At 12/31/2023: replacement-fund balance $3,583,496; operating-fund balance $344,307.

### A(d) Does any DBPR field name a lender, a loan, or association borrowing?

| DBPR surface | Lender name | Loan exists / amount | Public? |
|---|---|---|---|
| License lookup (project and managing entity) | No | No | Yes |
| Condo CSV extracts, payment history | No | No | Yes |
| Key Financial Indicators CSV | No | No (fund totals only) | Yes; timeshare-only in practice [I] |
| Building and Assessment Information form | **No** (depository institutions only) | No | No dataset found |
| SIRS Reporting Form | **No** | **Yes, planned** ("special assessment, loan, or line of credit" plus amount) | Database public, but columns UNKNOWN (403) |

**Conclusion for A(d): no DBPR surface observed names a lender.** The only borrowing-related field is the SIRS form's planned funding method and amount, and its public display is unconfirmed.

---

## Section B: UCC (Florida Secured Transaction Registry)

**How the search was run.** I used Organization Debtor Name, list `FiledAndLapsedCompactDebtorNameList`, category `Standard` ("Proximity search"), plus name variants: "CONDO ASSN", bare name, with and without "THE". Each hit's details came from `/filing-details`, its later amendments and terminations from `/filing-history`, and its collateral text from `/filing-image`, all free.

**The API does not return collateral text. Collateral is visible only in the filing image.**

| # | Association | UCC # | Filed | Status (registry) | Secured party (verbatim) | Collateral (from image) | Later filing events |
|---|---|---|---|---|---|---|---|
| 1 | Green Terrace | 980000041311 | 1998-02-24 | Lapsed | FIDELITY FEDERAL SAVINGS BANK OF FLORIDA | not viewed | none |
| 1 | Green Terrace | 990000166066 | 1999-07-22 | Lapsed | FIDELITY FEDERAL SAVINGS BANK OF FLORIDA | not viewed | Terminated 2000-04-26 |
| 1 | Green Terrace | 200000196157 | 2000-08-25 | Lapsed | FIDELITY FEDERAL BANK & TRUST | not viewed | Continued 2005-04-14 |
| 1 | Green Terrace | 200200456804 | 2002-02-26 | Lapsed | FIDELITY FEDERAL BANK & TRUST | not viewed | Continued 2006-11-09 |
| 1 | Green Terrace | 200406152002 | 2004-02-12 | Lapsed | NATIONAL CITY BANK SUCCESSOR BY MERGER TO FIDELITY FEDERAL BANK & TRUST | not viewed | Continued 2008-09-12; secured party changed 2008-09-12; Terminated 2011-04-27 |
| 1 | Green Terrace | **201701017030** | 2017-04-24 | Lapsed (expired 2022-04-24) | **BOK LENDING II, LLC** | Box 4 reads *"see attached Schedule A"*. The attachment (headed Exhibit "A") covers buildings on the land plus *"all rents, royalties, profits, revenues, incomes, assessments, maintenance payments, special assessments…"*, fixtures, personal property and insurance proceeds | none |
| 2 | Ocean Five | 201001970975 | 2010-02-08 | Lapsed | LM FUNDING, LLC. | *"Security interest in all rights of Debtor to recieve and collect proceeds arising pursuant to any and all regular and special assessments levied by debtor and assigned to Secured Party…"* | none |
| 3 | Sunset Palm Villas | 200407522423 | 2004-07-29 | Lapsed | EXECUTIVE NATIONAL BANK | *"Assignment of special and common assessments. … The Bank will have full rights to offset the association's bank account if deemed necessary to pay-off subject loans."* | Terminated 2005-08-12 |
| 4 | Dockside at Ventura | 970000024081 | 1997-02-03 | Lapsed | EASTERN SAVINGS BANK (Hunt Valley, MD) | 22-page image, not reviewed | Terminated 1998-04-16 |
| 4 | Dockside at Ventura | 201105006555 | 2011-07-25 | Lapsed | LM FUNDING, LLC. | Same assessment-proceeds language as Ocean Five | Continued 2016-06-21 |
| 5 | OIRC (timeshare) | 970000178722 | 1997-08-11 | Lapsed | CREDENTIAL LEASING CORP OF FL INC | Phone system; *"filed with respect to a lease transaction and not a security agreement"* | none |
| 6 | Palm Greens at Villa Del Ray Recreation | **no hits** | — | — | — | — | Neighbouring index rows: "PALM GREEN INVESTMENTS LLC" … "PALM GROVE MARINA" |
| 7 | Grande Isle Towers I & II | 201300328329 | 2013-12-04 | Lapsed | MARLIN BUSINESS BANK | *"SEE ATTACHED INVOICE"* (equipment [I]) | none |
| 7 | Grande Isle Towers I & II | **202300207980** | 2023-01-24 | **"Filed" (lapse date 2028-01-24)** | **SUNCOAST CREDIT UNION** | Exhibit A: *"all special assessments now and in the future levied … for the purpose of funding the emergency clean-up … roof replacement, stucco repairs … and pay Loan closing costs … which are necessary as a result of Hurricane Ian"*, plus deposit accounts at Suncoast or *"Pacific West Bank"*. The exhibit excludes *"funds … for statutory reserve accounts"* and insurance proceeds | **UCC-3 TERMINATION filed 2023-10-19** (#202302876669), authorized by Suncoast Credit Union |
| 8 | Windmill Lakes V | 200705018367 | 2007-03-09 | Lapsed | BANKATLANTIC | *"…COLLATERAL ASSIGNMENT OF SPECIAL AND GENERAL ASSESSMENT, DATED FEBRUARY 28,2007…"* | none |
| 9 | Gardens of Forest Lakes | 980000238660 | 1998-10-26 | Lapsed | PREMIER COMMUNITY BANK OF FLORIDA | not viewed | Terminated 2001-07-16 |
| 9 | Gardens of Forest Lakes | 200202511209 | 2002-10-29 | Lapsed | PREMIER COMMUNITY BANK OF FLORIDA | not viewed | Terminated 2003-05-13 |
| 9 | Gardens of Forest Lakes | 200303868749 | 2003-05-02 | Lapsed | FIRST COMMUNITY BANK OF AMERICA | not viewed | Terminated 2004-09-27 |
| 9 | Gardens of Forest Lakes | 200407626709 | 2004-08-11 | Lapsed | MERCANTILE BANK | *"Collateral Assignment of Assessments and Lien Rights…"* | Continued 2009-06-17 |
| 10 | Press-reported repair borrower | NOT RUN (see Section C) | | | | | |

**Excluded as a different entity:** "OCEAN FIVE HOTEL, L.L.C." (436/439 Ocean Drive; secured party OCEAN BANK, #201308268120, status Filed). It is a hotel company, not the association at 458 Ocean Dr.

**Sister associations surfaced but not in the sample:** Windmill Lakes IV has a VALLEY NATIONAL BANK filing (2015, lapsed), a MUTUAL OF OMAHA BANK filing (2019, **Filed**) and a TRUE INVESTORS INC filing (2024, Filed). Grande Isle Towers III & IV has a U.S. SMALL BUSINESS ADMINISTRATION filing (2023, Filed). Windmill Lakes Condo Association and Windmill Lakes II/III have 2007 bank filings.

**Cross-check against the bankruptcy file** (`bk_verification/bk_cases_*.md`):
- Green Terrace's secured claimant "Boken Lending II, LLC f/k/a BOK Lending II LLC" matches UCC 201701017030. That financing statement **lapsed 2022-04-24**, while the claim is still asserted in the bankruptcy. The claim rests on a **recorded mortgage**, which lives in county official records, not the UCC registry [I].
- Dockside's "South Florida Real Estate LLC": no UCC filing against the association.
- Palm Greens' post-petition premium lender FIRST Insurance Funding: no UCC filing found.

**What a UCC record can and cannot prove:**

| Can show | Cannot show |
|---|---|
| That a named secured party filed against a named debtor on a date | Loan amount, commitment, funding, outstanding balance |
| The collateral description (in the image only) | Default, maturity, interest rate |
| Continuation, termination and amendment events | Whether a security agreement was ever signed. A financing statement can be filed before the agreement exists (s. 679.5021(4), F.S. / UCC 9-502(d); statute not re-fetched this session) |
| | Real-property mortgages, which are recorded with the county clerk, not here |
| | Whether a "Filed" record is still in effect: #202300207980 shows status "Filed" but has a filed termination |

---

## Section C: Matching test

**DBPR record** = the association's Managing Entity (MA#) record, found by name. **Join** = whether the two records can be linked. Nine sample rows are reported here; row 10 was not run.

| # | Association | (i) DBPR records found (fields populated) | (ii) UCC | (iii) Join key |
|---|---|---|---|---|
| 1 | Green Terrace (West Palm Beach) | MA00007596 "GREEN TERRACE CONDO ASSN INC" (6131 Lake Worth Rd, Greenacres). Project PR1S015344, 2800 Georgia Ave, **84 units**, status "Approved,Delinquent" | 6 filings; latest BOK LENDING II (2017, lapsed) | Name after normalizing; **street address matches** (2800 Georgia Ave on the project and the UCC) |
| 2 | Ocean Five (Miami Beach) | MA64878 "OCEAN FIVE CONDO ASSN, INC" (1680 Michigan Ave). PR69933, 458 Ocean Drive, Units Recorded 16 / Residential 13 | 1 filing; LM FUNDING (2010, lapsed) | Name after normalizing; **MA address matches the UCC "c/o" address** |
| 3 | Sunset Palm Villas (Miami) | MA00023691 (9999 NE 2nd Ave, Miami Shores). PR1P025327, 400 N.W. 85 Street, Units Recorded 267 / Residential 127 | 1 filing; EXECUTIVE NATIONAL BANK (2004, terminated 2005) | Name only. The UCC address is a manager's "c/o" address |
| 4 | Dockside at Ventura (Orlando) | MA00019742 "DOCKSIDE AT VENTURA CONDO ASSN., INC." (2580 Woodgate Blvd). The **project is named "DOCKSIDE, A CONDO"** (PR1V021243, 266 units) | 2 filings; EASTERN SAVINGS BANK (1997); LM FUNDING (2011) | Name through the MA record only; searching the project name alone misses it. The UCC addresses (Tampa; manager in Orlando) do not match |
| 5 | Orlando International Resort Club (timeshare) | MA00016361 "ORLANDO INT'L RESORT CLUB COND ASSN" (Managing Entity-Timeshare). The association **also appears as developer DE00017826**. Project PRXI000331, "Timeshare Weeks 3213". KFI financials FY2021 to 2023 | 1 filing; CREDENTIAL LEASING (1997 lease) | **Address matches** (5353 Del Verde Way); the name needs INT'L→INTERNATIONAL, and the UCC name is truncated at "ASSOCIATI" |
| 6 | Palm Greens at Villa Del Ray Recreation (Delray Beach) | **Not found as a DBPR entity** (board 800, 830, 840 and 38 searches). Only the sister project "PALM GREENS NO 2 CONDO ASSN AT VILLA DEL RAY INC" (PR1S018893, 5801 Via Delray, which is the bankruptcy debtor's address, 717 units; MA00000174) | **No filings** | None |
| 7 | Grande Isle Towers I & II (Punta Gorda) | MA00024870 "GRANDE ISLE TOWERS I & II CONDO ASSOC, INC. SUITE 300" (**13831 Vector Ave, Fort Myers**, the same as the bankruptcy filing address). PR1P026481, 112 units, **County: Lee** | 2 filings; MARLIN BUSINESS BANK (2013); **SUNCOAST CREDIT UNION (2023, terminated 2023-10-19)** | Name after normalizing; address partial (the UCC's 3313-3321 Sunset Key Circle vs DBPR's "3321 SUNSET CIRCLE") |
| 8 | Windmill Lakes V (Pembroke Pines) | MA63899 (PO Box 10837, Pompano Beach). PR68946, 8734 SW 3rd St, 64 units | 1 filing; BANKATLANTIC (2007, lapsed) | Name after normalizing. The UCC address (450 SW 88th Terrace) equals the address of DBPR **developer** DE00022564 "WINDMILL LAKES INC", not the association |
| 9 | The Gardens of Forest Lakes (Oldsmar) | MA00015862 (570 Carillon Pkwy, St. Petersburg). PR1P013709, "LAKEVIEW DR & FOREST LAKE, PALM HARBOR", 160 units. **The CSV instead lists managing entity MA00003880 "PARK TOWER ASSOCIATION INC"**, while the online relation page lists both | 4 filings, 1998 to 2004 (Premier Community Bank ×2; First Community Bank of America; Mercantile Bank) | Name only, with "THE" dropped. No common address |
| 10 | Press-reported repair borrower | **NOT RUN.** About 15 minutes of searching found no article naming both a Florida association and its lending bank. Results were vendor or lender marketing, a bank-executive column (Hancock Whitney, via Yahoo Finance) and NBC News (2024-08-11); none names an association and its lender | — | — |

**Match rates (out of 9 rows run):**

| Test | Count |
|---|---|
| Association record found in DBPR | 8/9 (Palm Greens Rec. missing) |
| Any UCC filing found | 8/9 |
| Found in both systems | 8/9 |
| Joinable on exact name string | **0/9**. DBPR abbreviates ("CONDO ASSN INC"), while UCC uses the full legal name |
| Joinable after name normalization (CONDO→CONDOMINIUM, ASSN→ASSOCIATION, INT'L→INTERNATIONAL, drop THE, drop punctuation) | 8/9 |
| Address corroborates the name join | 3/9 exact (Green Terrace, Ocean Five, OIRC); 1/9 partial (Grande Isle) |
| Shared numeric identifier | **0/9**. UCC carries no MA# or PR#. Older UCC-1 forms carry a Florida organizational ID (for example Ocean Five N06000012781, Dockside N22197, Gardens N11097), which is a Sunbiz key, not a DBPR key [I] |
| UCC filing not lapsed and not terminated | **0/9** |
| UCC names a lender that also appears in the bankruptcy record | 1/9 (Green Terrace: BOK Lending II / Boken) |

**Which lending facts are available from public records:**

| Fact | Status | Source system |
|---|---|---|
| Lender identity | **Partial.** UCC names the secured party when one filed. Filing is optional, a lapsed filing stays listed, and the mortgage route (county records) and unfiled lenders are invisible | UCC only; DBPR none |
| Committed amount | **Unavailable** | Neither system |
| Funded amount | **Unavailable** | Neither system |
| Outstanding balance | **Unavailable** | Neither system |
| Planned loan or line-of-credit amount (not the lender) | **Partial and unconfirmed.** Collected on the SIRS form; public display UNKNOWN because of the 403 | DBPR SIRS database |
| Collateral | **Available where a UCC exists**, in the filing image only (assessment assignments seen at 7 filings across 7 associations) | UCC |
| Default status | **Unavailable** | Neither system |
| Maturity | **Unavailable.** The UCC lapse date is the 5-year filing life, not the loan maturity | Neither system |
| Loan paid off or released | **Partial.** A UCC-3 termination shows the filing was released, not why | UCC |
| Depository banks | Collected on the Building and Assessment form; **no public dataset found** | DBPR (not published) |

---

## Section D: Source-access log (2026-09-28, about 20:11 to 20:23 EDT)

| URL | Result |
|---|---|
| https://www.myfloridalicense.com/wl11.asp (mode 0/1/2 POST name search, boards 800/830/840/38) | 200; results parsed |
| https://www.myfloridalicense.com/LicenseDetail.asp?SID=&id=… → /portalsearches/VerifyLicensee/LicenseDetail?ID=… | 200 (redirect) |
| /portalsearches/VerifyLicensee/AdditionalInfo (POST ID) | 200 for project records; "Error" page for MA records |
| /portalsearches/VerifyLicensee/LicenseRelation (POST ID) | 200 |
| /portalsearches/VerifyLicensee/ViewComplaint (POST ID) | 200 (boilerplate; no complaint rows shown for Green Terrace) |
| https://www2.myfloridalicense.com/condos-timeshares-mobile-homes/ | 200 |
| https://www2.myfloridalicense.com/condos-timeshares-mobile-homes/public-records/ | 200; column layouts quoted above |
| https://www2.myfloridalicense.com/sto/file_download/extracts/{Condo_NF,condo_CE,Condo_CW,Condo_MD,condo_PB,keyfinancialindicators,tsmailing,paymenthist_8002D}.csv | 200 each (text/csv) |
| https://www2.myfloridalicense.com/instant-public-records/ | 200 |
| https://www2.myfloridalicense.com/condos-timeshares-mobile-homes/condominiums-and-cooperatives-sirs-reporting/ | 200 |
| https://dbpr-publicrecords.myfloridalicense.com/qpr/single/?appid=a1ab25e1-…, 14f1ed21-…, d217126f-… | 200 (JavaScript shell only) |
| wss://dbpr-publicrecords.myfloridalicense.com/qpr/app/<appid> (all three apps) | **403 Forbidden (blocked)** |
| https://dbpr-publicrecords.myfloridalicense.com/qpr/qps/user | 200; `"session":"inactive"` |
| WebFetch of the SIRS July-2025 Qlik link | shell only; no data |
| https://condos.myfloridalicense.com/ , /inspections/ , /services/ , /timeline/ , /faqs/ | 200 |
| https://www2.myfloridalicense.com/condominiums-and-cooperatives/ctmh-forms-and-publications/ | 200 |
| https://www2.myfloridalicense.com/lsc/documents/Online%20Account%20Instructions%20for%20SIRS%20Reporting.pdf | 200; text extracted |
| …/Online%20Account%20Instructions%20for%20Building%20and%20Assessment%20Information.pdf | 200; text extracted |
| …/Online%20Account%20Instructions%20for%20Association%20Information.pdf | 200; text extracted |
| …/CTMH%20Tutorial%20for%20Creating%20an%20Online%20Account.pdf | 200; text extracted |
| …/Instructions%20to%20use%20the%20new%20format.pdf | 200; text extracted |
| …/CondominiumGovernanceForm.pdf | 200; downloaded, not relevant to lending |
| https://www.flsenate.gov/Laws/Statutes/2026/718.501 | 200; subsection (3) quoted |
| https://www.floridaucc.com/ → https://floridaucc.com/ | 200 (React app); bundle `/static/js/main.b002c695.js` 200 |
| https://publicsearchapi.floridaucc.com/search-types , /filings-completed-through-date | 200 |
| https://publicsearchapi.floridaucc.com/search (about 20 queries) | 200 |
| https://publicsearchapi.floridaucc.com/filing-details (about 45 document numbers) | 200 |
| https://publicsearchapi.floridaucc.com/filing-history (18 filings) | 200 |
| https://publicsearchapi.floridaucc.com/filing-image → d3b30j659x3uym.cloudfront.net signed TIFF (12 images) | 200; no charge, no login |
| WebSearch ×6 (repair-borrower search; DBPR form context) | Results; no named association+lender article |
| https://finance.yahoo.com/economy/policy/articles/florida-condos-scrambling-afford-required-083500324.html | 200; no named association or lender |
| https://peterzalewski.substack.com/p/can-special-assessment-loans-rescue | paywall preview only |
| https://www.nbcnews.com/politics/economics/reckoning-coming-floridas-condo-owners-buildings-face-millions-repairs-rcna165764 | 200; no named association+lender |

---

## Section E: Summary

1. **Matching works by name, not by ID.** 8 of the 9 bankrupt associations appear in both DBPR (as a Managing Entity "MA#" record) and the UCC registry, but none join on an exact name or a shared ID (0/9). They join only after name normalization (8/9), with an address check in 3/9. Palm Greens Recreation is in neither system.
2. **DBPR names no lender anywhere I could see.** Its financial-institution field (s. 718.501(3)(c)3) lists banks where the association "maintains accounts". Its "reserves collected" is an annual amount collected, not a balance. That form has no public dataset. The SIRS form asks about a planned loan or line-of-credit amount without the lender, and whether the public SIRS database shows it is UNKNOWN (HTTP 403).
3. **UCC names lenders, but only historical ones in this sample.** 18 association filings were found; every one is lapsed or terminated. The only "Filed" record, Suncoast Credit Union's 2023 Hurricane-Ian special-assessment loan to Grande Isle I & II, carries a termination dated 2023-10-19. Green Terrace's BOK Lending II filing, the one lender that matches the bankruptcy record, lapsed in 2022.
4. **Collateral is visible (images only); money facts are not.** Committed amount, funded amount, balance, default and maturity are unavailable from both systems. A UCC filing shows a secured party and collateral, not a debt, and Florida allows filing before any security agreement exists.
5. **Row 10 was not run.** No press article naming both a Florida association and its lending bank was found in about 15 minutes.
