# H1 data refresh — CREED VX-3.03 / 9.03 / 9.02 (pulled 2026-10-28 late ET, read-only helper)

Tier key: PRIMARY-READ = publisher's own page/doc read this session · PRIMARY-CITED · SECONDARY (named outlet) · SEARCH-NOT-FOUND.

## 1. VX-CREED-3.03 — 2026 maturities (each perimeter separate, never sum)

| Source / pub date | Figure | Perimeter | Tier | Notes |
|---|---|---|---|---|
| Morningstar DBRS, "U.S. CRE 2026 Outlook" (dbrs.morningstar.com/research/471472), 2026-01-12 | "More than $100 billion in fixed- and floating-rate CMBS loans are coming due in 2026"; "more than half of those loans will not repay at maturity" | US CMBS, fixed + floating, calendar 2026, scheduled at Jan-2026 | PRIMARY-READ (summary page; full report gated) | This is the source of the current cell. Still the latest full-year DBRS total found; no update to the $100B. |
| Same outlook via CommercialSearch, 2026-01-22 | ~$57.7B expected maturity default + $9.9B "on the cusp"; mods expected to extend many | Same | SECONDARY | $57.7B / $9.9B NOT on the DBRS public summary page; cite as secondary. |
| Morningstar DBRS "U.S. CMBS Q2 2026 Maturity Research", 2026-07-29 (…/commentary/486444) | Q2 2026 payoff rate **59.5%**; Q3 2026 maturities **$9.7B** (office $3.6B, retail $3.2B); Q3 payoff forecast **65–70%** (fixed-rate) | Fixed-rate US CMBS, quarterly maturity cohort | PRIMARY-READ (release-style summary, Rachel Sill quote; PDF login-gated) | Payoff = share of the quarter's maturing balance; the rest = extended/defaulted. |
| Morningstar DBRS "U.S. CMBS Q3 2026 Maturity Research", 2026-10-19 (…/commentary/491633) | Q4 2026: **$13.4B** coming due, hotel largest; "expected payoff rates — from 65% in Q3 to roughly 55% in Q4" | "U.S. CMBS" (fixed vs floating not stated on page) | PRIMARY-READ but **page labels its own summary "Summary generated with AI assistance"** — grade lower (B3-ish) | Ambiguous whether 65% is Q3 ACTUAL or expected. PDF (491633.pdf) redirects to login. Q3 actual matured volume not on page. |
| MBA 2025 CRE Survey of Loan Maturity Volumes, rel. 2026-02-09 (MBA NewsLink newslink.mba.org/?p=270033; mba.org page 403s to curl) | **$875B (17%)** of $5.0T matures in 2026 (−9% vs $957B 2025); 2027 **$652B**. **Lender type in DOLLARS:** depositories $396B (21%), **CMBS/CLO/ABS $200B (25%)**, credit cos/warehouse/other $163B (29%), life cos $76B (10%), GSE/FHA/Ginnie $39B (4%). **Property type in PERCENT only:** hotel 30%, industrial 23%, office 17%, healthcare 15%, multifamily 13% | All commercial/MF mortgages held by lenders/investors; UPB at 2025-12-31 (balances at maturity will be lower) | PRIMARY-READ (MBA's own NewsLink) | No extension/not-repay share. The $200B CMBS/CLO/ABS bucket is NOT comparable to DBRS $100B (includes CRE CLO + ABS, UPB basis, MBA perimeter). No property-type dollars (trap #5). |
| KBRA 2026 US CMBS Outlook, 2025-11-21 (kbra.com/publications/dncMHcjj) | "A total of **$525 billion** in loans will mature in 2026, followed by **$587 billion** in 2027" | **UNSTATED** in release; context ("more loans may find their way into CRE securitizations" from banks) implies whole CRE-loan market, NOT CMBS | PRIMARY-READ | Do not put in a CMBS cell. Pre-2026 forecast. |
| KBRA "2025 CMBS Loan Maturities" research, 2026-01-12 (BusinessWire) | Search snippet: $131.7B CMBS maturing over next two years | KBRA-rated conduit/SASB (unverified) | SEARCH-NOT-FOUND at primary (BusinessWire 403 via WebFetch and curl) | Snippet only; do not cite. |
| CRED iQ | Only Feb-2025 figure found (~$163B securitized maturing 2026; $440B through 2026) via GlobeSt | Conduit+SASB+CRE CLO+GSE MF | SECONDARY, stale (2025) | No 2026 update found (web search, one query). |
| MSCI | none | — | SEARCH-NOT-FOUND (one search, no 2026 maturity figure surfaced) | Not pursued further. |

**Read for the cell:** DBRS full-year ">$100B; >50% not repay" (Jan-2026) remains the latest DBRS full-year statement; it is a FORECAST at Jan-2026. Realized quarterly path: Q1 payoff 60.0% (secondary, pulse.bot), Q2 59.5% (primary), Q3 ~65% (AI-summary page, actual-vs-expected ambiguous), Q4 expected ~55% on $13.4B. Payoff ~55–65% means ~35–45% of fixed-rate quarterly maturities NOT paying off — this is a different metric from ">50% of $100B (fixed+floating) not repaying"; don't conflate.

## 2. VX-CREED-9.03 — US office vacancy (CBRE canonical)

| Source | Q3 2026 vacancy | Change | Net absorption | Tier |
|---|---|---|---|---|
| **CBRE "Q3 2026 U.S. Office Market Report"**, 2026-10-23, https://www.cbre.com/insights/figures/q3-2026-us-office-market-report | **18.2%** | −10 bp QoQ, −60 bp YoY (5th consecutive quarterly decline) | **+4.9M sf** Q3 (10th straight positive qtr); T4Q +29.2M sf (vs 27.3M prior T4Q) | PRIMARY-READ |
| CBRE same page, context | prime vacancy 11.9% (−60bp QoQ, −250bp YoY); leasing 63.8M sf (+4% YoY), T12M 244M sf (+2%); completions 1.5M sf (−76% YoY), YTD 4.7M sf; avg asking rent $37.95/sf (+3.1% YoY) | | | PRIMARY-READ (no PDF link on page) |
| Consistency check | Q2 cell 18.3% → Q3 18.2% = −10bp, matches CBRE's stated QoQ. Absorption slowed 12.6M → 4.9M sf (shape: still positive, decelerating) | | | |
| Cushman & Wakefield Q3 2026 Office MarketBeat, BusinessWire 2026-10-13 (via Finviz repost) | **19.8%** | −25 bp YoY (QoQ not stated) | **+50,000 sf** Q3; T12M +15.5M sf | PRIMARY-CITED (wire repost); C&W site page did not render figures |
| JLL "U.S. Office Market Dynamics, Q3 2026" (jll.com/en-us/insights/us-office-market-dynamics) | NOT in page text | — | **+6.0M sf** Q3 (5th positive qtr); YTD +21M sf; 9.6M sf removed from inventory in Q3; asking $40.51 (+60bp QoQ) | PRIMARY-READ (absorption); vacancy SEARCH-NOT-FOUND (shapes checked: narrative bullets, raw HTML; chart not read) |
| Colliers Q3 2026 | — | — | — | SEARCH-NOT-FOUND (one search; latest found Q1 2026) |
| Moody's Q3 2026 | — | — | — | SEARCH-NOT-FOUND; Scotsman Guide (SECONDARY) cites Moody's 20.7% "as of August 2026", record high, rising — opposite direction to CBRE/C&W; different method |

Note the absorption dispersion in one quarter: CBRE +4.9M, JLL +6.0M, C&W +0.05M sf — never blend.

## 3. VX-CREED-9.02 — Green Street CPPI

| Item | Value | Tier |
|---|---|---|
| Latest US release: "Waiting For Price Clarity", 2026-10-06, https://www.greenstreet.com/waiting-for-price-clarity/ (September data) | All-property CPPI **−0.1% MoM** (Sept); **+4.7% YoY** | PRIMARY-READ |
| Quote | "If this rise in yields sticks, property prices are likely to go down" — P. Rothemund | PRIMARY-READ |
| Prior months (Green Street releases) | Aug +0.8% MoM / +5.0% YoY (2026-09-04); Jul +1.0% / +5.2% (2026-08-06); Jun 0.0% / +4.1% | PRIMARY-READ (Aug, Jul); Jun via CRE Daily |
| Office, September | **flat MoM, +5% YoY, −33% vs 2022 peak**; all-property −12.8% vs 2022 peak; student housing −4.7% MoM was the only mover | SECONDARY — CRE Daily 2026-10-08 (credaily.com/?p=223773) |
| Office trail | June: −34% from peak, ~+5% YoY (CRE Daily 2026-07-09); May/April ~−35% (GlobeSt 2026-05-07) | SECONDARY |
| Index level | Not in public release. Secondaries: all-property 130.9 (May, GlobeSt); office 75.1 (June, search snippet — unverified) | SECONDARY / unverified |
| **Office in public release?** | **No.** Green Street's public release carries all-property only. Checked: release narrative, raw HTML (no table, no PDF, no chart image other than a stock photo), /resources/pricing-index/ page (no sector table/downloads). Sector table is in Green Street's subscriber/email CPPI report; CRE Daily evidently has it. | — |
| October CPPI | Not yet published (expected ~early Nov) | — |

Rate-sensitivity flag: Sept print is the first MoM decline after +1.0/+0.8; Green Street itself signals downside if yields stick. One print; shape ungraded.
