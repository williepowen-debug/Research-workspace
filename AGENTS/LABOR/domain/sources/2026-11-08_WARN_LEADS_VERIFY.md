# WARN lead verification: state primaries (LABOR helper, read-only)

Run: Sun 2026-11-08, about 12:05 to 12:40 ET. All figures come from files saved under `scratchpad/warn/` and text-extracted locally (openpyxl / pdfminer / pdfplumber, `python -I`). UA `research-bot/1.0`. Secondary news was used only to find files and is tagged [2ND]. No repo file was edited, staged or committed.

Skipped as instructed: First Brands (TX), Campbell Soup (TX), Acuity Brands (MN).

## A. Lead verdicts

| TSV row | Verdict | Primary says | Primary URL / saved file |
|---|---|---|---|
| MV Transportation, Naples FL, 151 | **FOUND** | MV Transportation, Inc., 8300 Radio Road, Naples 34104. **151**. Letter dated **2026-07-30**, list notification date 07-30-26. Layoffs effective **2026-09-30** or within the 14 days after (list: 09-30-26 thru 10-13-26). "All layoffs are expected to be **permanent**." The business unit is closing because the transit contract expires 9/30 (the letter names it "Capital Area Transit System (CATS)", as written). TWU-represented. **Closure of a unit.** | reactwarn.floridajobs.org/WarnList/Records?year=2026 (p1) + notice `MV+Transportation+Naples+07.30.2026.pdf` → `warn/fl_pdf/MV_Transportation_Naples_07.30.2026.pdf` |
| Peterson Brands, Fort Myers FL, 135 | **FOUND (old)** | 9910 Bavaria Rd, Fort Myers 33913. **135** (the entire workforce). Notice **2026-04-27**. Effective **2026-06-27**. **Permanent total plant shutdown.** Signed by Peterson Farms Inc. | same list p2 + `warn/fl_pdf/Peterson_Brands.pdf` |
| Msgr. Bryan Walsh Children's Village, Miami FL, 84 | **FOUND (old)** | 9525 Sterling Drive, Miami 33157 (Catholic Charities of the Archdiocese of Miami). **84** (the table total in the notice). Agency letter **2026-04-24**, list date 04-27-26. Separation **2026-05-31**. **Permanent closure.** The federal Office of Refugee Resettlement ended its funding contract. | same list p2 + `warn/fl_pdf/Msgr._Bryan_Walsh_Children_s_Village.pdf` |
| GEICO Lakeland FL, 114 | **FOUND** | GEICO, 3535 W Pipkin Road, Lakeland 33811. Remote employees reporting to Lakeland, Staff Counsel, Florida PIP unit. **"approximately 114"**. List notification date **11-02-26** (the letter carries no date). Separations start on or about **2026-12-31** and are staged to about **2027-04-30**. **Permanent "mass layoff"**, no union. | same list p1 + `warn/fl_pdf/WARN_Notice_-_GEICO_-_Remote_Workers_Reporting_to_Lakeland.pdf` |
| Oracle Seattle WA, 359 | **FOUND** | Oracle America, Inc. Seattle Sites (Russell Investments Center, 1301 2nd Ave; 2025 5th Ave) plus WA remote workers. ESD row: **359**, Layoff, Permanent, received **9/14/2026**, start **11/13/2026**. Letter: separation **2026-11-13**. Sites not closing. **Permanent layoff.** | fortress.wa.gov/esd/file/WARN/Public/SearchWARN.aspx (company search "Oracle") → `warn/wa_search_Oracle.html`. Notice: `fortress.wa.gov/esd/file/WARN/Public/DownloadFile.aspx?file=d1804142-9ad0-4903-9024-53e2bb62ab34.pdf` → `warn/wa_pdf/WA_Oracle_20260914.pdf` |
| Amazon WA, 95 | **FOUND** | ESD row: Amazon, Sumner / Pasco / Bellevue / Redmond / Seattle and remote, **95**, Layoff, Permanent, received **11/2/2026**, start **12/7/2026**. Letter dated 2026-11-02 lists 17 facilities plus **15 remote**. Separations are staged **12/07/2026 to 01/25/2027**, the largest being **43 on 01/05/2027** (14 tranche lines sum to 95). Expected **permanent**. | same search ("Amazon") → `warn/wa_search_Amazon.html`. Notice `...file=0fde3d45-7ede-4123-af1d-bedf4d6152c3.pdf` → `warn/wa_pdf/WA_Amazon_20261102.pdf` |
| Marc's Parma OH, 55 | **FOUND (notice PDF)** | Marc Glassman, Inc. d/b/a Marc's, 12200 Corporate Dr, Parma 44130. **55**. Letter **2026-09-10**, stamped "Received September 10, 2026 @ 7:58am". Layoffs start **2026-11-10** or within 14 days. **Permanent closure of the entire operation**, non-union. The Ohio JFS list page itself was not located (the old jfs.ohio.gov WARN URLs return 404); the PDF sits on the state's own asset host. | `https://dam.assets.ohio.gov/image/upload/jfs.ohio.gov/warn/WARN%202026/Marc_Glassman_Inc.pdf` → `warn/oh/OH_Marc_Glassman_Inc_2026.pdf` |
| JPMorgan Chase Jersey City NJ, 91 | **FOUND (list only)** | NJ 2026 archive row: JP Morgan Chase, Jersey City, Month Posted **November**, effective **10/30/26 - 1/24/27**, **91**. The archive gives the posting month only, with no exact notice date and no type. The TSV's "2026-10" filing month is off by one, because the state posts it under November. The six JPM 2026 rows (120 Feb, 134 Mar, 51 May, 173 Jul, 63 Aug, 91 Nov) sum to **632**, the annual figure in the TSV note. | `https://www.nj.gov/labor/assets/PDFs/WARN/2026_WARN_Notice_Archive.pdf` → `warn/nj/NJ_2026_WARN_Notice_Archive.pdf` (Jan through Nov 2026) |
| Wells Fargo Roanoke VA, ~90 | **FOUND, count and date differ** | Wells Fargo, 7711 Plantation Road, Roanoke 24019. **87** (not ~90). Notice **10/28/2026** (TSV has 10/27). Impact **11/28/2026** (TSV has ~12/26). Type **Layoff**. Permanent/temporary is not stated, and no notice PDF is linked. | VEC page now redirects to `https://virginiaworks.gov/im-an-employer/retain-and-grow/warn-notices/` → `warn/va/va_virginiaworks.html` (a CSV link `/warn_notices_1794157860.csv` exists but was not pulled) |
| Northpointe Bank MI, 338 | **UNREAD** | michigan.gov returns **HTTP 403 (Akamai "Access Denied") for the whole host** from this box, including LEO pages and /-/media PDFs, under research-bot and WebFetch alike. Not bypassed. [2ND] web search found no Northpointe WARN mention. | n/a |
| Alabama auto parts closure, ~80 | **FOUND, identity inferred** | AL WARN list row: **Closure**, Initial Report **11/02/2026**, Planned Start **12/31/2026**, **International Automotive Components Group North America Inc.**, **Cottondale**, **83**. This is the only 2026 auto-supplier closure on the list near 80 workers and near the AL.com 11/5 date. The match to the AL.com headline is **by attributes only**, because the article body was not read (the "six years after expansion" detail is unverified). The list gives no notice PDF and no permanent/temporary field. | `https://www.madeinalabama.com/warn-list/` → redirects to `https://workforce.alabama.gov/warn-list/` → `warn/al_warn_list.html` |
| Trinity Health IT outsourcing, MULTI, 557 | **UNREAD (filing state MI)** | [2ND] Michigan Advance 9/8, Healthcare IT News, WARNTracker: filed with **Michigan** LEO, 557, effective 10/25 to 11/29. MI is blocked (see Northpointe). **NOT FOUND** on the other lists pulled today: CA EDD (notices 6/26 to 11/4/2026), WA ESD (company search, all years), FL (2026, 1/5 to 11/2), NJ (Jan to Nov 2026), VA (current list), AL (current list). Ohio's list was not available, and other Trinity states (IN, IA, ID, PA, MD, NY, IL, MA, CT, DE, GA) were not checked. | n/a |

Cross-check: **CA EDD** carries Oracle's 9/14 round as 63 Pleasanton + 279 San Mateo + 99 Santa Clara = **441**, matching the TSV's "441 CONF". CA also carries a separate **Amazon, Los Angeles County, 94, notice 11/02/2026, effective 2027-01-31**.

## B. California EDD: notices dated 2026-09-29 or later, 100+ workers

Source: `https://edd.ca.gov/siteassets/files/jobs_and_training/warn/warn_report1.xlsx` → `warn/ca_warn_report1.xlsx`. Sheet header: "WARN REPORT - 07/01/26 to 11/04/2026" (processed-date basis; updated Tuesday and Thursday). The window below is keyed on the **Notice Date** column.

| Notice | Effective | Employer | County | Workers | Type |
|---|---|---|---|---|---|
| 2026-09-29 | 2026-11-30 | Workday Inc. | Alameda | 142 | Layoff Permanent |
| 2026-09-30 | 2026-09-11 | Neogen Care Home Health Agency | Los Angeles | 148 | Closure Permanent |
| 2026-10-01 | 2026-10-30 | Baloian Farms | Fresno | 106 | Layoff Temporary |
| 2026-10-01 | 2026-12-17 | 24Hr Homecare | Los Angeles | 875 | Layoff Permanent |
| 2026-10-05 | 2026-12-04 | AMF Bowling Centers (Castle Park) | Riverside | 130 | Layoff Permanent |
| 2026-10-05 | 2026-11-19 | Menzies Aviation | Los Angeles | 137 | Layoff Permanent |
| 2026-10-09 | 2026-12-15 | Myers Power Products | San Bernardino | 206 | Closure Permanent |
| 2026-10-13 | 2026-12-14 | Tree Service Unlimited | El Dorado | 137 | Layoff Permanent |
| 2026-10-14 | 2026-12-14 | Neil Jones Food Co (Tomatek) | Fresno | 116 | Layoff Temporary |
| 2026-10-15 | 2026-12-14 | Fender Musical Instruments | Riverside | 533 | Closure Temporary |
| 2026-10-15 | 2027-01-15 | Formagrid (Airtable) | San Francisco | 190 | Layoff Permanent |
| 2026-10-16 | 2026-09-14 | Netflix, Inc. | Los Angeles | 267 | Layoff Permanent |
| 2026-10-16 | 2026-09-14 | Netflix, Inc. | Santa Clara | 227 | Layoff Permanent |
| 2026-10-19 | 2026-12-19 | Dreyer's Grand Ice Cream | Kern | 715 | Closure Temporary |
| 2026-10-19 | 2026-12-19 | Dreyer's Grand Ice Cream | Tulare | 448 | Closure Temporary |
| 2026-10-20 | 2026-12-19 | Dreyer's Grand Ice Cream | Kern (same address as 715 row) | 380 | Closure Temporary |
| 2026-10-21 | 2026-10-21 | eBay Inc. | Santa Clara | 229 | Layoff Permanent |
| 2026-10-22 | 2026-12-21 | Georg Fischer Signet | Los Angeles | 107 | Closure Temporary |
| 2026-10-23 | 2026-12-22 | Eterna Management | Orange | 124 | Layoff Permanent |
| 2026-10-26 | 2026-12-31 | Levy | Alameda | 181 | Closure Permanent |
| 2026-10-27 | 2026-12-29 | Walt Disney Parks & Resorts US | Los Angeles | 159 | Layoff Permanent |
| 2026-10-27 | 2026-12-31 | Artiva Biotherapeutics | San Diego | 131 | Layoff Permanent |
| 2026-10-29 | 2026-12-31 | AEG Management Oakland | Alameda | 1,605 | Layoff Permanent |
| 2026-10-30 | 2026-12-31 | iLEAD Lancaster | Los Angeles | 119 | Layoff Permanent |
| 2026-10-30 | 2026-12-29 | Danone USA | Los Angeles | 135 | Closure Permanent |
| 2026-10-30 | 2027-01-02 | Community Tree Service | Monterey | 163 | Layoff Permanent |
| 2026-10-30 | 2026-03-01 | Pacific Coast Grill | San Diego | 119 | Closure Temporary |

**CA totals.** Of notices dated 2026-09-29 or later, **27 have 100+ workers, totalling 7,829**: 19 permanent with 5,305 workers and 8 temporary with 2,524. **All notices in the window: 151, totalling 10,901**, of which 13 temporary with 2,764. On a processed-date basis (processed 9/29 or later) the count is 155 notices and 11,254 workers.

⚠️ These figures are as printed. The Netflix rows (effective 9/14) and Neogen (effective 9/11) carry effective dates **before** their notice dates. Pacific Coast Grill shows an effective date of 2026-03-01. Dreyer's Kern 715 and 380 share one address on consecutive notice dates, which may be an amendment rather than two events, so possible double count. The AEG Oakland 1,605 and Levy 181 rows are the same site, 7000 Coliseum Way.

## C. Florida: notices dated 2026-10-01 or later

Source: `https://reactwarn.floridajobs.org/WarnList/Records?year=2026` pages 1 to 3 → `warn/fl_2026_p{1,2,3}.html`, parsed to `warn/fl_2026.tsv`. 220 records, notification dates 2026-01-05 to **2026-11-02**. No duplicates in the window.

| Notice | Layoff dates | Employer | City | Workers | Industry |
|---|---|---|---|---|---|
| 10-07-26 | 12-06-26 thru 12-20-26 | TH Opco LLC d/b/a Terrace of Hialeah | Hialeah | 175 | Health Care |
| 10-14-26 | 12-08-26 | The Mosaic Company | Fort Meade | 199 | Manufacturing |
| 10-16-26 | 12-01-26 thru 12-31-26 | Aetos Systems, Inc. | Merritt Island | 126 | Prof/Sci/Tech |
| 11-02-26 | 12-31-26 thru 04-30-27 | GEICO | Lakeland | 114 | Finance & Insurance |

**FL totals.** Of notices dated 2026-10-01 or later, **4 have 100+ workers, totalling 614**. **All notices in the window: 13, totalling 989.** The 9 under 100 are Niagara Bottling Ocala 57, Endeavors (multiple locations) 68, AmeriHealth Caritas Orlando 61, Builders FirstSource Jacksonville 82, Behlen Sarasota 55, Dillard's Boynton Beach 22, Cayuga Fort Lauderdale 13, and Grunt Style Lutz 9 and Destin 8. The FL list does not record permanent/temporary; that is only in the notice PDFs, which were not pulled for these.

## D. Corrections the TSV owner may want (not applied, read-only task)

- Oracle WA row: the primary now exists. ESD's company search works (it is an ASP.NET form, no captcha), so the TSV's "not machine-readable" note is outdated.
- Wells Fargo Roanoke: **87**, notice 10/28, impact **11/28/2026**. The TSV's ~12/26 effective date and ~90 count are not the primary's.
- JPM NJ: the state posts it under **November**, not October.
- Peterson Brands and the Walsh Children's Village are **April 2026 notices, already effective** (6/27 and 5/31), not live leads. MV Naples was effective 9/30 to 10/13/2026.
- AL row: the employer is probably **IAC (International Automotive Components), Cottondale, 83, closure, start 12/31/2026**.
- MI rows (Northpointe, Trinity) are still unverified: michigan.gov is blocked host-wide from this box.
