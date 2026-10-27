# ISHM — DATA ROUTES (reachability measured at build, 2026-10-23)

Measured by DAEDALUS and a research helper on 2026-10-23, roughly 09:30–09:55 ET, from this box. Full working record: the build record, `AGENTS/DAEDALUS/builds/ISHM_BUILD_2026-10-23.md` §5. **Re-record a route here the day it changes.** A route marked BLOCKED is data an LLM cannot reach. Tell Will before spending a session on it.

| Route | Reach at build | Use | Notes |
|---|---|---|---|
| **FRED CSV, keyless** (`https://fred.stlouisfed.org/graph/fredgraph.csv?id=<ID>`) | ✅ REACHABLE. INDPRO · IPMAN · TCU (newest 2026-09) · DGORDER · NEWORDER · ANXAVS · AMTMNO (newest 2026-08) | boot.py leg 8, plus history for base rates | FRED serves the **latest-revised** vintage. A first-published value comes from the issuer release (or ALFRED). One curl timed out at 30 s and succeeded on retry |
| **ISM** (ismworld.org calendar and report pages) | ⛔ BLOCKED. A 302 sends the request to a login page with a reCAPTCHA check, both in curl and WebFetch. Not bypassed, and never to be | — | The `baby<YYYYMM>pmi.pdf` press release on ismworld.org loaded (HTTP 200) for September, so the **headline release may be readable as a PDF**. Verify at the first session. **ISM is not on FRED**: every NAPM* id returns 404, and `/series/NAPM` redirects to FRED's 2016 removal notice. **History is paywalled, so survey thresholds cannot be back-tested on free data** |
| **S&P Global PMI** (pmi.spglobal.com, spglobal.com) | ⛔ BLOCKED. 403 or an empty bot-challenge page, in curl and WebFetch | — | Release dates come from MTS Insights / Investing.com (SECONDARY). A headline figure from a secondary source is `SECONDARY-SOURCE` until it is read at the issuer |
| **Census M3** (`census.gov/manufacturing/m3/`) | ✅ REACHABLE. The release schedule and the 2026 economic-indicator calendar agree on every date | Durable goods advance, full factory orders | The next full report after December is 2027-01-07 |
| **Fed G.17** (`federalreserve.gov/releases/g17/`) | ✅ REACHABLE. Release dates + `json/calendar.json` (times) | IP / CU | ⚠️ **Annual revision 2026-11-24**: base year moves to 2022, history back to 1972 restated. Re-base any IP/TCU band |
| **Regional Feds**: NY (Empire) · Philadelphia · Richmond · Dallas | ✅ REACHABLE (PRIMARY schedules) | Survey rows | Two guessed URLs returned 404; the correct pages are linked from each survey's own page (see catalyst notes) |
| **Kansas City Fed** | ⚠️ PARTIAL. curl timed out; WebFetch reached the release-dates page | Survey rows | No release time is published; the 11:00 ET figure is MTS's |
| **AAR weekly rail traffic** (aar.org) | ⚠️ PARTIAL. The Data Center page says "every Wednesday at noon"; later requests got **HTTP 429** (rate-limited) | J2 freight leg | Holiday-week dates unverified. Read each month's weeks in one batch (catalyst design) and space out requests |
| **Cass Freight Index** (cassinfo.com) | ✅ Rule page reachable: "typically released on the 13th", "within two weeks of month-end" | J2 freight leg | There is no dated schedule; a 13th that falls on a weekend moves |
| **Class 8 truck orders** (ACT Research, FTR) | Press-release headlines only (not measured at build) | J2 freight leg | The full data is paid. Headlines are `SECONDARY-SOURCE` unless read at the firm's own release |
| **Census FT-900 trade** (computers and accessories imports) | ✅ Schedules reachable on bea.gov and census.gov, and they agree (Sep data 2026-11-04) | J1 leg 2 | The data pull itself is untested — FIRST_SESSION item 5 |
| **BEA GDP**, equipment / information-processing investment | ✅ `bea.gov/news/schedule` reachable (Q3 advance 2026-10-29) | J1 leg 3 | The data pull itself is untested — FIRST_SESSION item 5 |
| **Bellwether IR pages** (8 names) | ✅ 6 reachable (HON, GE, MMM, UNP via SEC 8-K; PH, EMR via IR). ⛔ **Caterpillar** blocked (Akamai 403 / timeout), so its date is SECONDARY. ⚠️ **Deere**: newsroom empty or 403, events page 404, date not yet announced | Earnings rows | SEC.gov refuses curl as an undeclared automated tool; WebFetch worked. Declare a User-Agent with a contact on any scripted SEC pull |

## Owner remeasurement — October 26, 2026

The build table above is a dated access record. This update is the current route result; raw response status/URL/hash and retrieval UTC are in `research/2026-10-26_first-session/sources/manifest*.json`.

| Route | October 26 result | Consequence |
|---|---|---|
| ISM September release | Direct `baby202609pmi.pdf` HTTP 200, read and saved; ordinary month page returned a 922-byte challenge shell | Current headline/components reachable by public PDF; long component history still not obtained. Do not bypass login/reCAPTCHA |
| S&P current release index / PDFs | Public PressReleases index HTTP 200; October flash and September final PDF links recovered and read HTTP 200. Web open failed while ordinary direct GET succeeded | Current first-party releases are reachable. September flash original fell outside returned index window and was not recovered; final supersedes it. Paid full PMI history remains unavailable |
| Census M3 | Advance/full PDFs HTTP 200; web-open schedule confirms October 27; direct schedule GET returned500 | Read dated PDFs, archive before mutable endpoint rolls. PRIMARY schedule via web works; do not label the whole route blocked |
| Five regional Feds | NY, Philadelphia, Richmond and KC current issuer pages/PDFs plus Dallas read successfully | Correct Richmond path is `/region_communities/regional_data_analysis/business_surveys/`; October27 release window 10:00–10:10 ET. Guessed older paths404 are not source absence |
| Cass | September report and historical XLSX HTTP200 | Publisher/mirror shipment levels reconcile129/129 months, January 2016–September 2026. Report body lacks an independently verified release-day stamp; October 13 timing remains rule-derived |
| AAR | October 21 release for week October 17 HTTP200 | Current one-week primary volume read; full weekly four-week-history calibration remains owed |
| ACT | Issuer North America Class 8 blog datedOctober 20 final 19,172 found | Dated lead supersedes embedded preliminary18,700. Ignore undated key metrics31,751; regulatory transition/orderbook caveat retained |
| FT-900 | BEA August release HTTP200; linked `trad0826.xlsx` HTTP200; Exhibit8 read | Computer/accessory imports measurable. Guessed CensusPDF404/500 does not block paired leg. Exact real-import deflator/end-use reconstruction of the hardware chart remains incomplete |
| BEA equipment | Q2 third-estimate GDP PDF retrieved; detailed equipment tables not recovered from guessed XLSX URL404 | No current Q2 information-processing growth figure asserted. Q3 equipment leg wakes October 29; detailed NIPA table/line required before grading |
| Bellwethers | CAT advisory recovered HTTP200; GE/HON/MMM issuer results and UNP issuer-hosted8-K read; PH/EMR advisories read | CAT date upgraded toPRIMARY. Deere IR dynamic event body empty; indexed issuer November 25 date remains qualified, time unverified |
| FRED histories | All seven boot series current; full Cass mirror starts2016; returned ICEBAMLH0A0HYM2 startsOctober 27,2023 despite requested1996 start | J2 sample restricted to completeNovember 2023–September 2026 months. Broader-cycle credit base rate unavailable from returned route; no invented long history |

Use repository `.venv/bin/python3` for PDF/HTML/Excel analysis. System Python lacks pandas, bs4 and pdfminer here; boot/tests use the standard library and run with `python3`. Source captures are frozen research inputs, not a new collector or recurring monitor.
