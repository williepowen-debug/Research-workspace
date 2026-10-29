# WAL credit ratings baseline: first build

- **Subject:** Western Alliance Bancorporation (HoldCo; SEC CIK 0001212545) and Western Alliance Bank (Bank; FDIC RSSD 3138146). Subsidiaries are shown where the agency rates them.
- **Built:** 2026-10-28, retrieval window 23:03–23:15 ET (see §4).
- **Builder:** WAL-desk research subagent. Read-only to the repo.
- **Grade key:**
  - **A1:** the agency's own page, or a WAL/SEC document stating the rating.
  - **B2:** reputable secondary source citing a dated agency action.
  - **B2-snippet:** search-engine snippet of a page that returned 403 to every client. Weakest; treat as a lead, not as evidence.

**One-line state:**
- Four agencies plus Egan-Jones rate WAL. S&P does not appear to.
- On the HoldCo the spread is two notches: Moody's Baa3 (lowest) → Fitch BBB → KBRA BBB+ and Morningstar DBRS BBB (high) (highest).
- Every outlook or trend that could be read is Stable.
- No downgrade, negative outlook or watch placement was found at any agency from 2025-01-01 to 2026-10-28.
- Three upgrades were found in the window: Fitch and Moody's in Feb-2025, DBRS in Dec-2025.

---

## 1. Current ratings

The company's own ratings page is the master list. That page is A1 for the letter grades. It states **"WA Corporate Ratings as of: 5/12/26"**, columns Fitch | Moody's | Kroll | Morningstar DBRS | Egan-Jones. It shows **no outlooks**, and it does not mention S&P anywhere.

Source: https://investors.westernalliancebancorporation.com/financials/credit-ratings/default.aspx (below: "IR page").

### Moody's

| Entity | Rating type | Rating | Outlook | As-of / last action date | Source (URL) | Grade |
|---|---|---|---|---|---|---|
| HoldCo | LT issuer | **Baa3** | Stable | IR page 2026-05-12. Upgrade Ba1→Baa3 on 2025-02-25. Affirmation on 2026-02-09 (see §2). | IR page; https://www.investing.com/news/stock-market-news/moodys-upgrades-western-alliance-bancorporation-ratings-outlook-stable-93CH-3892741 (2025-02-26) | A1 rating / B2 outlook |
| HoldCo | Subordinated debt | **Baa3** | n/a | IR page 2026-05-12. Ba1→Baa3 on 2025-02-25. | IR page; Investing.com 2025-02-26 | A1 |
| HoldCo | Preferred (Series A) | **NOT VERIFIED** | — | — | §3 | — |
| Bank | LT issuer | **Baa3** | not stated | IR page 2026-05-12. Ba1→Baa3 on 2025-02-25. | IR page; Investing.com 2025-02-26 | A1 |
| Bank | LT deposit | **A3** | Stable | IR page 2026-05-12. Baa1→A3 on 2025-02-25. Affirmed 2026-02-09. | IR page; WAL "Strength of WAL – Special Edition March 2026" (A3/P-2): https://www.westernalliancebancorporation.com/sites/default/files/2026-03/StrengthofWAL-SpecialEdition-March-2026.pdf ; Cbonds title https://cbonds.com/news/3785959/ | A1 rating / B2-snippet outlook |
| Bank | ST deposit | **P-2** | n/a | IR page 2026-05-12; WAL March-2026 document | IR page; WAL March-2026 PDF | A1 |
| Bank | Subordinated debt | **Baa3** | n/a | IR page 2026-05-12. Assignment on the Nov-2025 $400M notes: date not seen (§2). | IR page | A1 |
| Bank | Counterparty Risk Ratings LT/ST | **Baa2 / P-2** | n/a | 2025-02-25 (from Baa3/P-3) | Investing.com 2025-02-26 | B2 |
| Bank | Counterparty Risk Assessment | **Baa1(cr)** | n/a | 2025-02-25 (from Baa2(cr)) | Investing.com 2025-02-26 | B2 |
| Bank | BCA / Adjusted BCA | **baa2** | n/a | 2025-02-25 (from baa3) | Investing.com 2025-02-26 | B2 |
| Trust Co. (WATC) | Counterparty Risk Rating | **Baa2** | n/a | IR page 2026-05-12 (footnote "*Counterparty Risk Rating"). WATC LT issuer Ba1→Baa3 on 2025-02-25. | IR page; Investing.com 2025-02-26 | A1 / B2 |
| BW Real Estate, Inc. (Bank REIT sub) | Series B preferred | **Ba2** (expected at pricing) | — | 2025-03-24 term sheet | SEC 8-K EX-1.1, acc 0001212545-25-000113: https://www.sec.gov/Archives/edgar/data/1212545/000121254525000113/wal-purchaseagreement.htm | A1 (expected rating only) |

### Fitch

| Entity | Rating type | Rating | Outlook | As-of / last action date | Source (URL) | Grade |
|---|---|---|---|---|---|---|
| HoldCo | LT IDR | **BBB** | Stable | IR page 2026-05-12. Upgrade BBB-→BBB on 2025-02-24. Affirmation reported 2025-06-30. | IR page; https://www.marketscreener.com/quote/stock/WESTERN-ALLIANCE-BANCORPO-14844/news/Fitch-Upgrades-Western-Alliance-Bancorporation-to-BBB-Outlook-Stable-49151110/ (2025-02-25); Cbonds title https://cbonds.com/news/3473219/ | A1 rating / B2 outlook |
| HoldCo | ST IDR | **F3** | n/a | Affirmed 2025-02-24 | MarketScreener 2025-02-25; https://ng.investing.com/news/stock-market-news/fitch-boosts-western-alliance-bancorporations-rating-to-bbb-with-stable-outlook-93CH-1778417 | B2 |
| HoldCo and Bank | Viability Rating | **bbb** | n/a | 2025-02-24 (from bbb-) | same | B2 |
| HoldCo | Subordinated debt | **BBB-** | n/a | IR page 2026-05-12 | IR page | A1 |
| HoldCo and Bank | Government Support Rating | **No Support** | n/a | stated in the 2025-02-24 release | MarketScreener 2025-02-25 | B2 |
| Bank | LT IDR | **BBB** | Stable | IR page 2026-05-12. Upgrade on 2025-02-24. Affirmation reported 2025-06-30. | IR page; MarketScreener; Cbonds title https://cbonds.com/news/3473371/ | A1 / B2 |
| Bank | LT deposit | **A-** per IR page (see CONFLICT below) | n/a | IR page 2026-05-12 | IR page | A1, but contradicted by WAL's own 2026-03 document |
| Bank | ST deposit | **F2** per IR page (see CONFLICT below) | n/a | IR page 2026-05-12 | IR page | A1, but contradicted by WAL's own 2026-03 document |
| Bank | Subordinated debt | **BBB-** | n/a | IR page 2026-05-12 | IR page | A1 |
| WATC | — | "Private" | — | IR page 2026-05-12 | IR page | A1 |
| BW Real Estate, Inc. | Series B preferred | **BB-** (expected at pricing) | — | 2025-03-24 term sheet | SEC 8-K EX-1.1, acc 0001212545-25-000113 | A1 (expected only) |

> ⚠️ **CONFLICT on Fitch deposit ratings.** Three WAL-side or secondary sources give three different answers.
> 1. **Fitch, Feb-2025 (via MarketScreener 2025-02-25).** The uninsured LT deposit rating is "one notch higher" than the Bank IDR, which implies BBB+. The ST deposit rating is in line with the ST IDR, F3.
> 2. **WAL's own client document, "Special Edition March 2026"** (PDF last modified 2026-03-05). It says "Bank Deposit Ratings: Investment Grade A3/P-2 Moody's A-/K2 Kroll **BBB/F3 Fitch**".
> 3. **WAL's IR page (as of 2026-05-12).** Fitch deposits "Long-term: **A-**; Short-term: **F2**".
>
> The Fitch action that moved the deposit ratings (if any) was **not seen**. A lead, not evidence: a search snippet says Fitch published updated Bank Rating Criteria on 2026-05-08 and took criteria-driven actions on "five U.S. banking groups" on 2026-05-12. Whether WAL was among them is UNVERIFIED (inference from date coincidence only). Treat the Fitch deposit rating as **A- / F2 per company, unconfirmed at Fitch**.

### KBRA (Kroll Bond Rating Agency)

All rows below come from KBRA, "KBRA Affirms Ratings for Western Alliance Bancorporation", New York, **2026-05-08**: https://www.kbra.com/publications/psgndtpD. Grade A1. KBRA states "The Outlook for all long-term ratings is Stable."

| Entity | Rating type | Rating | Outlook | As-of / last action date |
|---|---|---|---|---|
| HoldCo | Senior unsecured debt | **BBB+** | Stable | Affirmed 2026-05-08 |
| HoldCo | Subordinated debt | **BBB** | Stable | Affirmed 2026-05-08 |
| HoldCo | Preferred stock | **BBB-** | Stable | Affirmed 2026-05-08 |
| HoldCo | Short-term debt | **K2** | n/a | Affirmed 2026-05-08 |
| Bank | Deposit and senior unsecured debt | **A-** | Stable | Affirmed 2026-05-08 |
| Bank | Subordinated debt | **BBB+** | Stable | Affirmed 2026-05-08 |
| Bank | Short-term deposit and debt | **K2** | n/a | Affirmed 2026-05-08 |
| WATC | Issuer | **BBB+** | Stable | Affirmed 2026-05-08 |
| AmeriHome Mortgage Company, LLC | Issuer | **A-** | Stable | Affirmed 2026-05-08 |
| BW Real Estate, Inc. | Preferred stock | **BBB** | Stable | Affirmed 2026-05-08 (first assigned 2025-03-19) |

The IR page (2026-05-12) matches these: HoldCo BBB+, Bank A-, WATC BBB+, AmeriHome A-, deposits A-/K2, sub debt BBB (HoldCo) and BBB+ (Bank).

### S&P Global Ratings

| Entity | Rating type | Rating | Outlook | As-of | Source | Grade |
|---|---|---|---|---|---|---|
| HoldCo / Bank | any | **No S&P rating found** | — | 2026-10-28 | See §3. The IR page (2026-05-12) lists five agencies and no S&P. The 2025-03-24 BW REIT term sheet lists expected ratings from "Moody's/Fitch/Kroll" only. | A1 evidence of absence (not proof) |

### Morningstar DBRS

Not on the requested list, but it does rate WAL.

| Entity | Rating type | Rating | Trend | As-of / last action date | Source (URL) | Grade |
|---|---|---|---|---|---|---|
| HoldCo | LT issuer | **BBB (high)** | Stable | Upgraded from BBB. MarketScreener reprint stamped 2025-12-15 05:05 EST; the DBRS release date was not shown. | https://www.marketscreener.com/news/morningstar-dbrs-upgrades-western-alliance-bancorporation-s-long-term-issuer-rating-to-bbb-high-fr-ce7d50d9d98cf72d ; IR page 2026-05-12 | B2 action / A1 level |
| Bank | LT issuer | **A (low)** | Stable | Upgraded from BBB (high), ~2025-12-15 | same | B2 / A1 |
| Bank | LT deposits | **A (low)** | — | IR page 2026-05-12 | IR page | A1 |
| Bank | ST | **R-1 (low)** | Stable | Confirmed ~2025-12-15 | MarketScreener | B2 |
| WATC | LT issuer / ST | **A (low)** / **R-1 (low)** | Stable | Upgraded from BBB (high) / confirmed, ~2025-12-15 | MarketScreener; IR page | B2 / A1 |
| Bank | Intrinsic Assessment / Support Assessment | A (low) / SA1. HoldCo Support Assessment SA3. | — | ~2025-12-15 | MarketScreener | B2 |

> ⚠️ **Discarded:** the DBRS report page (https://dbrs.morningstar.com/research/474616/western-alliance-bancorporation-credit-rating-report, report dated 2026-02-20) renders a row "Apr 17, 2026 | Issuer Rating | Confirmed | **A** | Stable". The raw HTML shows that row sits inside `<tbody class="ratings-placeholder__blurred">` behind a login gate. It is a **dummy placeholder, not WAL's rating**. Do not cite it.

### Egan-Jones (company-reported only)

Company-reported on the IR page as of 2026-05-12: HoldCo **BBB**, Bank **BBB+**, HoldCo sub debt **BBB-**. Grade A1 as a company statement. Not checked at the agency.

---

## 2. Rating-action history, 2025-01-01 → 2026-10-28

Rows marked "event" are WAL disclosures, included for the fraud-timing question. Rows marked "no action" are agency publications that changed no rating.

| Date | Agency | Entity | Action | Detail | Source | Grade |
|---|---|---|---|---|---|---|
| 2025-02-24 | Fitch | HoldCo + Bank | **Upgrade** | LT IDR BBB- → **BBB**, Outlook Stable. VR bbb- → bbb. ST IDR F3 affirmed. Cited higher capital (CET1 11.3% YE24 vs 10.8% YE23), lower loan-to-deposit ratio, less brokered/FHLB reliance. Asset quality viewed "with caution". | Investing.com (ng) 2025-02-24 23:50; MarketScreener 2025-02-25 05:43 EST | B2 |
| 2025-02-25 | Moody's | HoldCo, Bank, WATC | **Upgrade** | HoldCo LT issuer and sub Ba1 → **Baa3**, outlook **Stable from Positive**. Bank LT issuer and sub Ba1 → Baa3. Bank LT deposit Baa1 → **A3**. CRR Baa3/P-3 → Baa2/P-2. CR Assessment Baa2(cr) → Baa1(cr). BCA baa3 → baa2. ESG CIS-4 → CIS-3, G-4 → G-3. Downgrade triggers quoted: "the capital falls below 11.0%", "liquidity weakens", "CRE credit costs rise substantially", "the firm's risk appetite becomes more aggressive". | Investing.com 2025-02-26 08:37. Action date 2025-02-25 from Cbonds title https://cbonds.com/news/3282861/ | B2 (date: B2-snippet) |
| 2025-03-19 | KBRA | BW Real Estate, Inc. | **New rating** | Preferred stock **BBB** | https://www.kbra.com/publications/GgMnkykH | A1 |
| 2025-03-24 | (term sheet) | BW Real Estate Series B pref ($300M, 9.500%) | Expected ratings | "Expected Ratings (Moody's/Fitch/Kroll): **Ba2 / BB- / BBB**" | SEC 8-K EX-1.1 acc 0001212545-25-000113 | A1 |
| 2025-05-07 | KBRA | HoldCo, Bank, WATC, AmeriHome, BW RE | **Affirmation** | All ratings as in §1; Stable | https://www.kbra.com/publications/LkbPvBbX | A1 |
| 2025-06-25 | KBRA | HoldCo group | Surveillance report (no action) | Restates the 2025-05-07 affirmation | https://www.kbra.com/publications/hjCmYJhn | A1 |
| 2025-06-30 | Fitch | HoldCo + Bank | **Affirmation** (reported) | 'BBB', outlook stable. Cbonds headline: "Fitch Ratings affirms Western Alliance Bancorp at "BBB" … outlook stable". Fitch text not seen. | https://cbonds.com/news/3473219/ and /3473371/ (HTTP 403; title and snippet only) | B2-snippet |
| 2025-10-16 | — (event) | WAL | 8-K: Cantor Group V fraud suit | — | SEC acc 0001628280-25-045169 | A1 |
| 2025-10-17 | DBRS | sector | Commentary (no action) | "Zions and Western Alliance Announcements Set Off U.S. Regional Bank Jitters". WAL is in the issuer list. Sector view: "we view our rated banks as well positioned to absorb higher loan losses". | https://dbrs.morningstar.com/research/465072 | A1 |
| 2025-11 (date NOT seen) | Moody's | Bank | **New rating** (inferred timing) | "Moody's Ratings assigns Baa3 to subordinated debt issued by Western Alliance Bank". The only Bank sub issue since the 2024 "Moody's Ratings" rebrand is the $400M 6.537% notes due 2035, priced 2025-11-19 and settled 2025-11-24, so Nov-2025 timing is an **inference**. | Title: https://app.researchpool.com/provider/moodys-investors-service/moodys-ratings-assigns-baa3-to-subordinated-debt-issued-by-western-all-qrHDXriv9N (HTTP 403); notes: SEC 8-K acc 0001628280-25-053176 | B2-snippet |
| ~2025-12-15 | Morningstar DBRS | HoldCo, Bank, WATC | **Upgrade** | HoldCo BBB → **BBB (high)**. Bank and WATC BBB (high) → **A (low)**. ST R-1 (low) confirmed. Trend Positive → **Stable** ("The trend on all credit ratings is now Stable"). Quote: "Despite recent idiosyncratic credit events, the broader loan portfolio has held up well with the net charge-off ratio stable at 22 basis points for Q3 2025." Downgrade driver: "a material deterioration in asset quality". | MarketScreener reprint 2025-12-15 05:05 EST | B2 |
| 2026-02-09 | Moody's | Bank (likely group-wide) | **Affirmation** | Bank LT deposit **A3**, outlook stable (Cbonds). An undated Moody's title, "Moody's Ratings affirms Western Alliance's ratings; holding company issuer rating Baa3; outlook stable", is probably the same action (inference). | https://cbonds.com/news/3785959/ (HTTP 403; title and snippet); researchpool 8PkRlaYSy7 (HTTP 403) | B2-snippet |
| 2026-02-20 | DBRS | HoldCo | Credit rating report (no action) | Login-walled | https://dbrs.morningstar.com/research/474616/western-alliance-bancorporation-credit-rating-report | A1 (existence only) |
| 2026-03-02 / 03-06 | — (event) | WAL | 8-K: "$126.4 million" non-cash impairment, recognized in Q1-2026 (counterparty breach; claims asserted) | — | SEC 8-K acc 0001628280-26-015454 | A1 |
| 2026-03-05 | (company) | Bank | Ratings as stated by WAL | "Bank Deposit Ratings: Investment Grade A3/P-2 Moody's A-/K2 Kroll BBB/F3 Fitch" | WAL March-2026 PDF | A1 |
| 2026-05-08 | KBRA | HoldCo, Bank, WATC, AmeriHome, BW RE | **Affirmation** | All ratings unchanged; Stable. Quote: "A recent increase in credit costs associated with two large NDFI exposures are considered to be idiosyncratic … and not indicative of any broader asset quality or risk management issues." | https://www.kbra.com/publications/psgndtpD | A1 |
| 2026-03-05 → 2026-05-12 | Fitch | Bank | **Deposit-rating change: action NOT seen** | Company-stated Fitch deposits moved from BBB/F3 (Mar-2026 PDF) to A-/F2 (IR page, 2026-05-12). See CONFLICT box in §1. | — | UNVERIFIED |
| 2026-05-12 → 2026-10-28 | all | — | **No action found** | Includes the window around the Q3-2026 print (8-K 2026-10-19) | searches listed in §3 | — |

### Fraud-timing check (the specific ask)

**Oct-2025 Cantor Group V disclosure (8-K 2025-10-16).**
- No Moody's, Fitch, KBRA or DBRS rating action was found between 2025-10-16 and 2025-11-30.
- The only agency output in that window is DBRS's sector commentary of 2025-10-17, which made no WAL-specific statement.
- About two months later, DBRS **upgraded** WAL (~2025-12-15), explicitly looking through "recent idiosyncratic credit events".

**Mar-2026 $126.4M impairment (8-K 2026-03-06); the desk's Q1-2026 fraud-related total is $152.5M.**
- Moody's affirmation of 2026-02-09 **predates** the event, so it does not price it.
- No action was found in March or April 2026.
- The first agency action seen after the event is KBRA's **affirmation** of 2026-05-08. It labels the NDFI credit costs "idiosyncratic".
- No Moody's or Fitch text addressing either loss was seen. Their pages could not be read (§3).

**Net:** no agency downgraded WAL, cut an outlook or placed it on watch in response to either event. That conclusion is search-based for Moody's and Fitch.

---

## 3. What could NOT be verified, and why

1. **Moody's primary pages were unreadable.**
   - `https://ratings.moodys.com/ratings-news/401772` returns HTTP 200, but as an empty JS shell: WebFetch saw only "Ratings.Moodys.com".
   - `https://www.moodys.com/credit-ratings/Western-Alliance-Bancorporation-credit-rating-809874476` gave HTTP 403 to WebFetch and a 302 redirect to curl.
   - All three researchpool mirrors of Moody's releases gave HTTP 403 (Cloudflare block, Ray ID a51ef38aad0e5593).
   - **Unverified as a result:** current Moody's outlooks (the IR page shows none); the scope and text of the 2026-02-09 affirmation; the date of the Bank sub-debt Baa3 assignment; the Moody's rating on WAL's Series A preferred. Per a search snippet of 2021 FWP d202271dfwp.htm, the Series A was expected Ba1 at its 2021 issue, when the HoldCo was Baa2; that figure was not fetched.
2. **Fitch primary pages were unreadable.**
   - `fitchratings.com` is refused by WebFetch ("unable to fetch") and domain-blocked for WebSearch.
   - curl on `https://www.fitchratings.com/entity/western-alliance-bancorporation-80361793` returns a Gatsby JS shell with no rating data. That entity ID was not confirmed.
   - Cbonds pages (3473219, 3473371) gave HTTP 403 (Cloudflare "Just a moment").
   - **Unverified as a result:** the text of the 2025-06-30 affirmation; any 2026 Fitch action; the deposit-rating change (BBB/F3 vs A-/F2); Fitch's preferred rating on WAL's Series A.
3. **Morningstar DBRS:** the Dec-2025 upgrade press release was not located on dbrs.morningstar.com, so its exact release date is unknown. MarketScreener carries the full text with a 2025-12-15 stamp.
4. **S&P:** no S&P rating was found in any WAL, SEC or news source. The S&P ratings directory itself was not searched (`disclosure.spglobal.com` redirect and JS app). Absence is inferred, not proven.
5. **SEC filings do not state agency ratings.**
   - The full-text grep of the FY2025 10-K (acc 0001628280-26-010336) and the Q2-2026 10-Q (acc 0001628280-26-051418) found only generic credit-rating risk-factor language.
   - The 2026-05-12 Investor Day deck (8-K acc 0001628280-26-033850) has no ratings slide text.
   - The Nov-2025 sub-note 8-Ks state no ratings.
6. **WAL Corporate Profile page** (`/about-contact/CorporateProfile`) returned HTTP 404. A search snippet attributed "Long-Term Issuer Default Rating, BBB; Long-Term Deposit Rating, BBB+" (Fitch) to it. This is not readable, so it is not used beyond noting it as the third input to the Fitch deposit conflict.
7. **Egan-Jones** figures are company-reported only; not checked at the agency.
8. **Wayback Machine:** there are no snapshots of the IR ratings page (CDX empty / 502), so its change history could not be reconstructed.

---

## 4. Retrieval timestamps (ET, 2026-10-28; clock from `date` on this box)

| Time (EDT) | Item |
|---|---|
| 23:03–23:04 | Initial web searches. The three researchpool Moody's pages returned HTTP 403 at 23:04:10. |
| ~23:04 | WAL IR credit-ratings page via WebFetch, read twice and consistent. curl got a Cloudflare 403 at 23:04:39. |
| ~23:05 | KBRA publications psgndtpD (2026-05-08), sGpBQqKG (2024-05-02), LkbPvBbX (2025-05-07) |
| ~23:05–23:06 | Investing.com Moody's (2025-02-26) and Fitch (2025-02-24) articles; DBRS 444963 and 465072; DBRS 474616 (raw HTML 23:06:00) |
| 23:06:51–23:07:07 | SEC EDGAR full-text search; 10-K FY2025; 10-Q Q2-2026; 8-Ks 2025-11-19 and 2025-11-24; 2025-03-24 purchase agreement |
| ~23:08–23:10 | MarketScreener Fitch 2023, 2024 and 2025 items; Fitch/Cbonds attempts (Cbonds 403 at 23:10:14) |
| 23:11:12 | Fitch entity page via curl (JS shell) |
| 23:12:06–23:12:29 | EDGAR submissions JSON; 2026 8-Ks; Investor Day deck |
| ~23:13 | MarketScreener DBRS Dec-2025 upgrade (two reads, consistent) |
| 23:14:12 | WAL "Strength of WAL – Special Edition March 2026" PDF (pdfminer text extract) |
| ~23:14 | KBRA GgMnkykH (2025-03-19), KBRA hjCmYJhn and SwWYdqgR, remaining searches |
| 23:15 | File written |

The raw downloads (HTML/HTM/JSON) are in `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-WAL/097a6cca-41ca-4913-907d-08649fe0ad54/scratchpad/dl/` as top-level files only; the subfolders there are not this task's. The PDF text is in `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-WAL/097a6cca-41ca-4913-907d-08649fe0ad54/scratchpad/pdf_sow/`.

---
*Desk note 2026-10-28: this file is a subagent output copied into the repo. The scratchpad `dl/` copies it mentions are not retained; re-fetch from the URLs above and compare the sha256 prefixes. Load-bearing A1 facts used in KB rows were re-read by the desk (see each KB row's Source/Notes).*
