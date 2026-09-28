# WAL Catalyst Sweep: 2026-08-20 → 2026-09-23

| Field | Value |
|---|---|
| Window | 2026-08-20 (Thu) → 2026-09-23 (Wed) close; EDGAR checked through 2026-09-24 04:10 UTC |
| Swept | 2026-09-24, ~00:05–00:15 ET (04:05–04:15 UTC), read-only subagent sweep for the WAL desk |
| Issuer IDs | CIK 0001212545 · RSSD 3138146 |
| Sources checked | (1) `data.sec.gov/submissions/CIK0001212545.json` (HTTP 200, curl + UA header); (2) EDGAR browse-edgar atom feed (HTTP 200, cross-check); (3) EDGAR full-text search `efts.sec.gov` (issuer CIK; "Western Alliance" filtered to 8-K / 13G / 13D / 144; Jefferies CIK 96223; "Point Bonita"; "Cantor Group V"); (4) 9 Form 4 XMLs parsed line by line; (5) WAL IR Q4 press-release feed + event feed (JSON, primary); (6) web search + fetch: Investing.com (write-up + transcript), Seeking Alpha, Simply Wall St, MarketBeat, GuruFocus, Saxo, Bloomberg/BLaw headlines, CNBC/Yahoo market wraps, TheStreet Pro, Trellis; (7) yfinance closes for the cohort check |
| Blocked / rewritten requests | Seeking Alpha transcript → **HTTP 403** (fell back to the Investing.com transcript page). Trellis (Cantor docket) → **HTTP 403** (no fallback docket found). The first Form 4 fetch hit S3 `NoSuchKey` because of an accession-path typo on my side; fixed and re-fetched, all 9 parsed. WebFetch returns text through a small summarising model, so every "verbatim" quote from a web page below is **model-extracted**. Re-verify against the page before anything is graded off it. |
| Labels | **VERIFIED** = I read the primary. **SECONDARY** = a news write-up or third-party transcript. **SEARCH-NOT-FOUND** = searched and found nothing (queries listed in §6). |

---

## §1 EDGAR filings by or about WAL, 2026-08-20 → 2026-09-24

**Headline: no 8-K, no 10-Q/10-K, no Item 2.06, no 13D/13G, no Form 144, and no open-market insider trade (code P or S) in the window. The only issuer-CIK filings are 9 Form 4s, all of them routine RSU mechanics.** VERIFIED against the submissions JSON; cross-checked with the atom feed and full-text search, and all three agree.

### 1a. Issuer-CIK filing list (complete for the window)

| Filed (acceptance) | Form | Accession | Period | Content |
|---|---|---|---|---|
| 2026-09-17 21:01–21:02 ET | 4 ×9 | 0001628280-26-062566 … -062574 | 2026-09-15 | Monthly cash-settled RSU vest. Detail in 1b |
| — | 8-K | none | — | **SEARCH-NOT-FOUND / none on EDGAR.** Last issuer filings before the window: 13G/A T. Rowe (8/14), 13G Invesco (8/13), 9 Form 4s (8/18), already in KB-WAL-171..174 |

### 1b. Form 4 detail (tx date 2026-09-15; all at $79.03, which matches WAL's 9/15 close of $79.03 on yfinance)

| Filer | Title | Lines | Net common change | Post-tx holdings | Accession |
|---|---|---|---|---|---|
| Vecchione, Kenneth | Chairman, President & CEO | M +539/+437/+595 → D −same @ $79.03 | 0 | 463,178 | -062567 |
| Gibbons, Dale | Vice Chair & CBO, Deposits | M +285/+212/+229 → D | 0 | 267,093 | -062568 |
| Idnani, Vishal | CFO | M +123 → D | 0 | 11,468 | -062566 |
| Herndon, Lynne | Chief Credit Officer | M +35/+22/+27 → D | 0 | 1,880 | -062569 |
| Jarvi, Jessica H | CLO & Secretary | M +58/+46/+64 → D | 0 | 13,707 | -062570 |
| Bruckner, Tim R | CBO Regional Banking | M +158/+115/+142 → D | 0 | 29,068 | -062571 |
| Boothe, Timothy W | Chief Administration Officer | M +97/+69/+69 → D | 0 | 65,417 | -062572 |
| Kennedy, Barbara | CHRO | M +101/+74/+82 → D | 0 | 10,332 | -062573 |
| Nachlas, Emily | Chief Risk Officer | M +72/+53/+64 → D | 0 | 16,575 | -062574 |

- Footnotes (VERIFIED): "These units vest and are payable solely in cash … 1/36th on the 15th day of each month" (2024, 2025 and 2026 grant tranches). The M→D pair is the cash-settled RSU mechanic, the same pattern as KB-WAL-174 (8/15 cycle).
- **Code P: none. Code S: none. Gibbons discretionary sale: none. Mucha: no Form 4 in window. Curley Form 144: none** (the full-text search for form 144 returned 0; the issuer-CIK list has no 144). VERIFIED.
- 13D / 13G / 13G/A with WAL as subject, 8/20→9/24: **0 hits** (full-text search, forms SC 13G, SC 13G/A, SCHEDULE 13G, 13G/A, 13D). VERIFIED as an EDGAR-search negative.
- **Item 2.06 / $99M life-science loan: no 8-K of any kind, so no 2.06.** VERIFIED.
- One-line desk read: the insider tape is zero-signal. The $79.03 settlement price is a free 9/15 price print.

### 1c. Third-party EDGAR filings that name WAL (from full-text search; context only, and relevant to the NDFI lane)

| Filed | Filer | Form / Item | WAL role (VERIFIED, read in the 8-K text) |
|---|---|---|---|
| 2026-08-20 | SLR HC BDC LLC (CIK 1832148) | 8-K 1.01 | Western Alliance **Trust Company, N.A.** is collateral agent/custodian/administrator on the new DB-led SPV facility dated 8/14. Trust fee role, **not a lender** |
| 2026-09-02 | PennantPark Private Income Fund (CIK 2089126) | 8-K 1.01 | WA Trust Co. is collateral agent/document custodian (Amendment 3, 9/1). Not a lender |
| 2026-09-18 (filed 9/23) | Crestline Lending Solutions, LLC (CIK 2035713) | 8-K 1.01/2.03 | **Western Alliance Bank joins as a LENDER** on the DB-agented SPV facility. Committed amount raised from $350M to $550M, max from $400M to $600M. Joining lenders: WAB, East West, Apple Bank. WAL's own commitment size is not disclosed. **New private-credit / NDFI exposure added in the window** |
| 2026-09-18 | AudioEye (CIK 1362190) | 8-K 1.01 | WAB is sole lender. Fourth Loan Modification (Adjusted EBITDA definition change). Small tech C&I, routine |

---

## §2 Q3 2026 earnings date

| Item | Finding | Label | Source |
|---|---|---|---|
| Q3 2026 release/call date | **NOT ANNOUNCED** as of 2026-09-24 04:10 UTC | VERIFIED (primary IR feed) | The WAL IR press-release feed (Q4 JSON, year=2026) lists as its latest item "Western Alliance Bancorporation to Participate in Fireside Chat at Barclays…" dated **2026-09-14 17:51**. There is no Q3 date release. The IR event feed ends at 2026-09-16 10:30 (Barclays), with no Q3 call event. https://investors.westernalliancebancorporation.com/News-and-Presentations/news/default.aspx |
| Pattern (context) | Q2-26: announced 7/7, call 7/22 (Wed). Q1-26: announced 4/8, call 4/22 (Wed). Q3-25: announced 10/2/2025, call 10/22/2025 (Wed) | VERIFIED (IR feed) / SECONDARY for Q3-25 | IR feed; https://www.businesswire.com/news/home/20251002467683/en/ |
| Implication | By the prior-year pattern, expect the announcement around early October and a call around the 3rd–4th Wednesday of October. **This is inference, not an announced date.** | — | — |

---

## §3 Barclays 24th Global Financial Services Conference, 2026-09-16 10:30 ET (Vecchione fireside)

Source tiers:
- **T1:** there is no primary transcript. The IR webcast replay exists but was not accessed, and the Seeking Alpha transcript (https://seekingalpha.com/article/4947104) returned **403**.
- **T2 (SECONDARY, third-party transcript):** Investing.com transcript page https://www.investing.com/news/transcripts/western-alliance-at-barclays-conference-shift-to-profits-buybacks-93CH-4904090 (9/16). Quotes were model-extracted, capped at 125 characters, and some are trimmed.
- **T3 (SECONDARY, AI-assisted write-up):** https://ca.investing.com/news/stock-market-news/western-alliance-at-barclays-conference-shift-to-profits-buybacks-93CH-4842100 (9/16; page says "generated with the support of AI and reviewed by an editor").

| Topic | Quote / figure | Tier |
|---|---|---|
| **Problem credits** | "We mentioned six credits. Two were resolved in Q2. Two have been resolved in Q3, so we are four down, two to go. The other two are on a glide path to be resolved in Q4." | T2 |
| **NPLs** | "We expect our NPLs to come down about 10% this quarter in Q3. They are going to move from $567 million to about $500 million." | T2 (T3 concurs) |
| **Charge-offs** | "We expect our charge-off rate and dollars to be under that of Q2." | T2 |
| **ACL** | "Our ACL to where our NPLs will be at the end of Q3 will be well over 100%, whereas in the previous quarter, they are at 95%." ACL to "grow a couple of basis points per quarter". Peer ACL "about 1.2%". T3 gives WAL CLN-adjusted ACL "about 1.01%". CLN "removes up to 5% of residential losses" | T2 / T3 |
| **$99M life-science loan / appraisal / office** | **No hit** in the transcript for "appraisal", "appraised", "office", "life science", "lab", "nonaccrual", "liens". The only "$99" hit is assets: "$98 billion coming down from almost $99 billion for Q3." **It is not stated whether the $99M loan is one of the "six credits", or whether it is among the two resolved in Q3 or the two slated for Q4.** | T2 (negative within that transcript) |
| Cantor / LAM | "The Cantor and Lam to me is an old story … One was a fraud, which was Cantor. And the Lam for us is a breach of contract." "We expect a favorable outcome, and that will just transpire over the next year or so." "we found no other instance [of double-pledged titles] in our book of business other than what we saw with Cantor." | T2 |
| Jefferies / Point Bonita | No hit in the transcript | T2 (negative) |
| **Buyback** | "We had expected to buy back $150 million in the second half of the year … We're buying a little bit more in Q3 than in Q4 … the company's on sale … [Investor Day had] $200 million to $300 million … over a three-year horizon. Here we are buying back $150 million now, and we'll probably continue with that process into 2027." ⚠️ The T3 write-up misprints this as "second half of **2024**". The T2 transcript reads "second half of the year" | T2 (T3 wrong on year) |
| NIM / NII | "The 360-370 [bp NIM target] … is going to happen over three years." Q3 "headline NIM will just be down maybe about a basis point because of the deposit remix". Adjusted NIM up "several basis points" on lower deposit fees. **No explicit NII-guide change found** (transcript has no hit for "guidance" or "net interest income") | T2 |
| Deposits / ECR | "In Q2, we transitioned $1.4 billion of deposits outside of the bank. In Q3, we've already transitioned $2.5 billion. So now we're a total of $4 billion." Full-year goal was $3B. Q3 deposit growth is still "positive". "about $30 billion of ECR-related … balances". Warehouse deposits "about a 90% beta", other two businesses "50-ish percent" | T2 |
| **Mortgage warehouse** | "Warehouse Lending and MSR lending … [has] been active up to today. Probably won't be as active going forward." | T2 (trimmed quote) |
| Loan growth / size | "We are not going to grow more than $5 billion in total loan growth this year." Assets ~$98B at Q3 vs ~$99B at Q2 | T2 |
| LFI ($100B) | Expects to cross $100B organically by end-Q1 2027. LFI cost "$25 million to $30 million" a year. T3 says most reports are filed in 2028, not 2027 | T2 / T3 |
| Targets | ROAA 120–130bp, ROE 16–17% (medium term) | T3 |

Tape on 9/16 (yfinance closes):

| | 9/15→9/16 | 9/16→9/17 |
|---|---|---|
| WAL | −1.56% | **+2.10%** |
| KRE | −1.77% | 0.00% |
| KBE | −1.72% | −0.15% |
| ZION | −3.71% | +0.35% |
| OZK | −2.38% | −0.31% |

- WAL volume was 2.38M on 9/16, then 1.22M on 9/17 and 2.45M on 9/18.
- **On 9/16 WAL moved in line with the cohort.** The same day, the FOMC **hiked 25bp to 3.75–4.00%**, its first hike in more than 3 years, with Chair Warsh stressing inflation. SECONDARY: https://finance.yahoo.com/markets/stocks/articles/stock-market-today-sept-16-133949098.html, https://www.cnbc.com/2026/09/16/stock-market-today-live-updates.html
- **9/17 was a WAL-specific up day** (+2.1% against a flat KRE). That is consistent with, but not proven to be, a delayed read of the Barclays credit commentary.
- One line for the desk: the conference gave a Q3 credit pre-announcement in all but name (NPLs down ~$67M, NCOs below Q2, 2 of 6 problem credits resolved in Q3), but **said nothing findable about the $99M appraisal.**

---

## §4 News and analyst actions, 2026-08-20 → 2026-09-23

| Date | Item | Detail | Label / source |
|---|---|---|---|
| 2026-09-14 | Barclays fireside PR | Participation notice | VERIFIED: IR feed |
| 2026-09-16 | Weiss Ratings | Downgrade Buy (B-) → Hold (C+) (quant rating service) | SECONDARY, low quality (MarketBeat only): https://www.marketbeat.com/stocks/NYSE/WAL/forecast/ |
| 2026-09-20 | Simply Wall St | Narrative fair value $91.93 against a $78.54 price | SECONDARY: https://simplywall.st/stocks/us/banks/nyse-wal/western-alliance-bancorporation/news/western-alliance-bancorporation-wal-could-be-15-undervalued |
| **2026-09-22 06:24 ET** | **Raymond James initiates at Outperform, PT $90** | "credit remains the central debate for the bank, and execution will determine the magnitude of upside". Valuation "discounts a materially worse credit outcome than current trends and historical experience suggest." MarketBeat's 9/23 item calls it an "upgrade to moderate buy", which is a mislabel: it is an initiation | SECONDARY: https://www.investing.com/news/analyst-ratings/raymond-james-initiates-western-alliance-stock-with-outperform-rating-93CH-4910300 |
| 2026-09-22 | **Citi PT $98 → $95, Buy maintained** (Gerlinger) | No rationale found | SECONDARY, weak (MarketBeat table + search snippet; the GuruFocus page fetched shows an Oct-2023 date, so the 9/22 date is **unconfirmed** at a clean source): https://www.gurufocus.com/news/9091947/ |
| 2026-08-10 (before window, context) | Wells Fargo PT $79 → $90, Equal Weight | — | SECONDARY: MarketBeat |
| Consensus | MarketBeat: $95.00, "Moderate Buy" (16 analysts). S&P via search snippet: $93.07 (15 analysts), range $88–98 | — | SECONDARY |
| Jefferies litigation (WAL v. Jefferies; Jefferies' $25M Point Bonita countersuit) | **No new development found in window.** Latest reporting found is still the 2026-07-02 Bloomberg countersuit story. EDGAR full-text search: 0 hits for "Western Alliance" in Jefferies (CIK 96223) filings and 0 hits for "Point Bonita", 8/20→9/24. Vecchione (9/16) did not name Jefferies and called "Lam" "a breach of contract" | SEARCH-NOT-FOUND |
| Cantor (LA Superior 25STCV24263, Judge Terry A. Green) | **No ruling or new docket development found.** The Trellis docket returned 403. Vecchione (9/16): "a fraud … We expect a favorable outcome … over the next year or so" | SEARCH-NOT-FOUND (docket); SECONDARY (quote) |
| WAL credit headline (new) | **None found** 8/20→9/23. The Yahoo "credit events and target cuts" piece covers the April-2026 cycle only | SEARCH-NOT-FOUND |
| NDFI | WAL joined the Crestline SPV facility as a lender (9/18, see §1c) | VERIFIED |

---

## §5 Sector context 9/16–9/23 (what drove KRE down)

| Date | Driver | Label / source |
|---|---|---|
| 9/16 (Wed) | FOMC +25bp to 3.75–4.00%, first hike in >3 years. The dot plot implies another hike. Dow −1.21% | SECONDARY: Yahoo / CNBC links above |
| **9/22 (Tue)** | **"Meta Muse" AI-agent selloff.** Worries that personal AI agents erode "consumer inertia", including "moving cash into higher-yielding accounts", which is a deposit-franchise narrative. S&P 500 Financials fell ~2% (worst since March, lowest since July). JPM and WFC fell >3%, SCHW −6.1%, Allstate −5.5%. "S&P 500 Bank Index retreated broadly by 3%." Also cited: the 2s10s curve flattened to ~18bp intraday, the flattest since Mar-2025 | SECONDARY: https://www.bloomberg.com/news/articles/2026-09-22/meta-s-muse-drags-down-stocks-that-depend-on-consumer-inertia ; https://ca.investing.com/news/stock-market-news/meta-ai-agent-triggers-heavy-selloff-in-banks-insurers-and-travel-stocks-4848535 ; https://www.home.saxo/content/articles/macro/market-quick-take---oil-slips-under-90-as-bank-shares-slide---23-september-2026-23092026 ; https://www.techflowpost.com/en-US/article/34181 |
| 9/23 (Wed) AM | "Regional Banks [KRE] have now fallen to their lowest prices since June, and are less than 1% away from entering a technical correction" | SECONDARY (Barchart tweet via TheStreet Pro): https://pro.thestreet.com/dougs-daily-diary/2026-09-23 |
| 9/23 (Wed) | Rates shock. Hot PMIs pushed the **10y to 5.135%, highest since Jul-2007**, and the 5y hit 5% for the first time since 2007. S&P −0.75%, Russell 2000 sank. US–Iran headlines | SECONDARY: https://www.cnbc.com/2026/09/22/stock-market-today-live-updates.html ; https://finance.yahoo.com/markets/stocks/articles/stock-market-today-sept-23-134802225.html |
| None of the above | **No regional-bank-specific credit event found for 9/22–9/23.** None of the Muse coverage mentions KRE, regional banks, or WAL | SEARCH-NOT-FOUND |

**Cohort test (yfinance closes, pulled 2026-09-24):**

| Ticker | 9/21→9/23 | 8/20→9/23 |
|---|---|---|
| WAL | −3.88% | −4.49% |
| KRE | −2.24% | −5.80% |
| KBE | −2.36% | −5.99% |
| ZION | −3.59% | −7.72% |
| OZK | −3.48% | −6.47% |
| PNFP | −3.20% | −8.42% |
| COLB | −3.51% | −6.45% |
| EWBC | −2.57% | −4.16% |
| EGBN | +0.36% | +0.83% |

- **Read:** over the whole window WAL is in the middle of the cohort, better than KRE, ZION, OZK and PNFP. Over 9/21→9/23 WAL was about 1.6pp worse than KRE, but in line with ZION, OZK, COLB and PNFP, the higher-beta regionals. **The move is sector plus rates plus the Muse factor. There is no WAL-specific catalyst found.**
- ⚠️ **Data caveats:** (1) yfinance has **no 9/22 row** for WAL or most names; KRE alone shows 9/22 −1.11% and 9/23 −1.14%. The two-session figure is sound; the per-day split for WAL is unavailable from this vendor. (2) yfinance gives WAL's **8/20 close as $79.15**, while the desk carries **$79.89** (KB-WAL-180 cites "$79.89 close 8/20, live $80.05"). This is a vendor or basis discrepancy the desk should reconcile before reusing either figure. (3) The brief's "9/2→9/23" cohort figures were not re-derived here.

---

## §6 SEARCH-NOT-FOUND list (explicit)

| # | Item | Where / what I searched |
|---|---|---|
| 1 | Any WAL 8-K (incl. Item 2.06, 7.01, 8.01) 8/20→9/24 | submissions JSON; browse-edgar atom; full-text search forms=8-K, q="Western Alliance" (only third-party 8-Ks hit) |
| 2 | Any disclosure of the $99M life-science loan appraisal or charge-down in window | EDGAR (above); web "Western Alliance life science office loan nonaccrual appraisal 2026" (returned Q1/Q2 items only); Barclays transcript term scan (appraisal/appraised/office/life science/lab/nonaccrual/liens: no hits) |
| 3 | Form 4 code P, or any code S; Gibbons/Mucha sale; Curley Form 144 | 9 Form 4 XMLs parsed; full-text search form 144 (0); issuer-CIK list |
| 4 | 13D/13G/13G-A with WAL as subject in window | full-text search forms SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SC 13D, SCHEDULE 13D (0) |
| 5 | Q3 2026 earnings date | IR press-release JSON feed; IR event feed; web "Western Alliance third quarter 2026 earnings conference call date" |
| 6 | Primary Barclays transcript / webcast | Seeking Alpha (403); IR webcast not accessed |
| 7 | NII guide change at Barclays | Transcript scan for "guidance", "net interest income", "2026 outlook" (no hits) |
| 8 | Jefferies litigation development (either suit) | web "Western Alliance Jefferies lawsuit Point Bonita September 2026"; "…judge motion dismiss August OR September 2026"; "Jefferies Western Alliance countersuit frozen $25 million account update"; full-text search Jefferies CIK + "Point Bonita" (0). NY Supreme docket (NYSCEF) not accessed |
| 9 | Cantor 25STCV24263 development | web "Western Alliance Cantor lawsuit 25STCV24263 ruling"; Trellis (403); full-text search "Cantor Group V" (0). LA Superior portal not accessed |
| 10 | WAL-specific credit headline, or explanation of the 9/16 or 9/22–23 moves | web "Western Alliance bank news August 2026"; "…news September 23 2026"; "…shares September 16 2026 Barclays…" |
| 11 | Regional-bank-specific (non-Muse, non-rates) driver on 9/22–23 | web "regional bank stocks fall September 22 2026 KRE"; "bank stocks slide September 23 2026 regional lenders"; "regional banks stocks Wednesday September 23 2026…" |
| 12 | Clean-source confirmation of the Citi 9/22 PT cut | web "Citi lowers Western Alliance price target $95 from $98"; GuruFocus page shows an Oct-2023 date |

---

*Annotation 2026-09-28 (audit, `research/AUDIT_2026-09-28.md`; the sweep above stays as the dated record):* the row at line 119 ("Cantor (LA Superior 25STCV24263, Judge Terry A. Green) | No ruling or new docket development found") covered **half the case**. WAL's guaranty and declaratory claims against Stupin and Marcil were removed to bankruptcy court as adversary **8:26-ap-01076-SC** on 6/25/2026, and WAL moved to remand on 7/27; only the claims against Cantor V stayed in LA Superior, before **Hon. Cherol J. Nellon** per the removal notice (KB-WAL-206/-208). The 9/24 search-negative applies to LA Superior only. Open item 12 (the Citi date): a 9/28 web search dates Citi's $98→$95 cut to **9/22/2026** (news tier).
