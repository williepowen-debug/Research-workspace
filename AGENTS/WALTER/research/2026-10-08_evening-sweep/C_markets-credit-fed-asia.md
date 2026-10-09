# Evening sweep C: markets after the close, credit, banks, private credit, CRE, Fed, and the Asia/Europe open

- **Window:** 2026-10-08 20:20Z (16:20 ET) to about 00:40Z on 10/9 (20:40 ET). Report written 00:37Z. The PBOC yuan fix (01:15Z) and the Hong Kong open (01:30Z) came after this cut and are **not covered**.
- **Researcher:** WALTER evening sweep, agent C. I found and verified items only: no routing, no threshold grading, no commits.
- **Dedup basis:** I checked against the 45 headlines in `today_titles.txt` and grepped the bodies of `BOARD/SIG-W-20261008-0*` where needed.
- **Labels:**
  - **PRIMARY:** the issuer, agency or filing itself.
  - **SECONDARY-READ:** I fetched and read the article body.
  - **SNIPPET-ONLY:** I saw only a search snippet or headline.
  - **VENDOR:** a market-data quote, not an official close.

## Summary of material items

| # | Item | Verdict | Basis |
|---|---|---|---|
| 1 | Fed + OCC enforcement against American Express: $350M OCC penalty for anti-money-laundering failures; Fed cease-and-desist order; no asset cap | **NEW-ESTABLISHED** | PRIMARY (Fed 16:30 ET, OCC NR 2026-87, AXP 8-K 16:38:48 ET) |
| 2 | Fed H.4.1: discount-window primary credit on Wednesday 10/7 was **$9.965B**, the highest since at least Jan 2024 (FRED). Weekly average **$7.701B**, up from $5.102B five weeks earlier | **NEW-ESTABLISHED** | PRIMARY (H.4.1 16:30 ET) |
| 3 | America's Car-Mart (CRMT): lenders extended the waiver again, now to **10/15** (sixth extension since 9/7) | **CHANGE-TO-ROUTED** (SIG-W-20260925-004) | PRIMARY (8-K 16:05:15 ET, 15 min before the window opened) |
| 4 | The Wymore 360 (Altamonte Springs, FL), $33.0M CMBS loan: specially serviced since 8/11/26 for payment default; foreclosure is the stated strategy | **CHANGE-TO-ROUTED** (-040 had held it) | PRIMARY (BMO 2024-5C8 10-D, filed 10/2) |
| 5 | JGBs at the Tokyo open: 30Y **4.073% (−11.3bp)**, 10Y **3.042% (−4.2bp)** at 09:30 JST | **NEW-ESTABLISHED** (vendor level) | VENDOR (CNBC quote service) |
| 6 | Japan August household spending: **−3.1% y/y**, against −3.6% expected | **NEW-ESTABLISHED** | PRIMARY (Stat. Bureau) + SNIPPET (consensus) |
| 7 | St. Luke's Office, Allentown PA: specially serviced since 8/13/26 for "imminent default due to cash flow issues" | **NEW-ESTABLISHED** (not window-new) | PRIMARY (JPMCC 2017-JP7 10-D) |
| 8 | Bloomberg 10/8: Ares, Barings, BC Partners and Churchill are looking at troubled BDCs being offloaded | **NEW-UNVERIFIED** (publish time unknown) | SNIPPET-ONLY |
| 9 | After-hours movers: telecoms fell 5–7% on SpaceX buying Grain's 800 MHz spectrum; Humana +12% and Alignment −23% on the CMS 2027 Star Ratings | **NEW-ESTABLISHED** (off-beat) | SECONDARY-READ (CNBC) + PRIMARY (ALHC 8-K) |

**Searched, nothing new:**
- No Fed speaker after 16:20 ET.
- No bank failure: the FDIC list's latest is Nano Banc, 9/25.
- No HY or IG deals pulled.
- No new BDC or interval-fund gate.
- No new update on Bank OZK's RaDD loan.
- No WAL, ZION, FLG or VLY news.
- No MOF or BOJ intervention talk.
- No UK, France or ECB item after 22:20 CET.
- No new FRED HY OAS print (the latest is still 10/7 = 3.09).

---

## (a) Fed, Treasury, FDIC and OCC releases after 16:20 ET

### a1. Fed and OCC enforcement actions against American Express (NEW-ESTABLISHED, PRIMARY)

- **Fed press release** — https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261008a.htm
  - Marked *"For release at 4:30 p.m. EDT"* (20:30Z, inside the window).
  - Verbatim: *"The Federal Reserve Board on Thursday announced an enforcement action against American Express Company to address, among other things, the firm's failure to sufficiently detect and report certain suspicious activity related to money laundering."* Also: *"The Board also identified significant deficiencies in how American Express Company's enterprise-wide anti-money laundering program was implemented, in particular at the firm's subsidiary national bank."*
  - The order (PDF `enf20261008a1.pdf`) is a consent **Order to Cease and Desist**, Docket No. 26-052-B-HC, against American Express Co. and American Express Travel Related Services Co. **The Fed order itself carries no Fed penalty.**
- **OCC News Release 2026-87, dated October 8, 2026** — https://www.occ.gov/news-issuances/news-releases/2026/nr-occ-2026-87.html
  - A cease-and-desist order plus a **$350 million civil money penalty** against American Express National Bank (Sandy, Utah).
  - Verbatim: *"systemic breakdowns in its suspicious activity monitoring and reporting processes, resulting in a failure to timely identify, evaluate, and sufficiently report approximately $13 billion of suspected trade-based money laundering activity that took place over the past decade."*
  - Comptroller Jonathan Gould: *"American Express failed to maintain a BSA/AML compliance program properly aligned with the money laundering risks of its operations…"*
  - The penalty goes to the US Treasury. The OCC page shows no release time.
- **AXP 8-K, Item 7.01** — accepted **2026-10-08 16:38:48 ET**, accession 0000004962-26-000376.
  - Verbatim: *"AENB also agreed to pay a civil money penalty of $350 million to the OCC. A portion of the civil money penalty was reserved for in prior periods and it does not impact the full-year 2026 guidance … The consent orders do not impose an asset cap on the Company and costs associated with addressing the requirements of the consent orders are not anticipated to affect the Company's 2027 guidance."*
  - Context: Amex's Q2 2026 10-Q had already said it expected an AML enforcement action (SECONDARY-READ via search summary).
- **Price reaction:**
  - AXP regular close $308.10 (10/8). Last post-market print $303.85 (Yahoo 5-minute bars at 23:55Z and 00:00Z; zero reported volume on those bars), about −1.4%. VENDOR, thin.
- **Unknowns:**
  - Exact OCC release time.
  - What remediation the OCC consent order requires (PDF not read).
  - Whether FinCEN or DOJ actions follow. Neither release mentions them.

### a2. Fed H.4.1, released 16:30 ET 10/8: discount-window use keeps rising (NEW-ESTABLISHED, PRIMARY)

Source: https://www.federalreserve.gov/releases/h41/20261008/ (table 1, $ millions; week ended Wed 10/7/2026).

| Week ended (H.4.1 date) | Primary credit, weekly avg | Primary credit, Wednesday level |
|---|---|---|
| 9/2 (9/3) | 5,102 | 5,282 |
| 9/9 (9/10) | 5,351 | 5,838 |
| 9/16 (9/17) | 6,608 | 6,879 |
| 9/23 (9/24) | 6,343 | 6,235 |
| 9/30 (10/1) | 6,871 | 8,738 |
| **10/7 (10/8)** | **7,701** (+830 w/w, +2,079 y/y) | **9,965** |

- **Five-week change:** the weekly average is up 51% since 9/2, and the Wednesday level is about 1.9× its 9/2 value.
- **Longer history:** FRED `WLCFLPCL` (Wednesday level) shows **9,965 on 2026-10-07 as the highest since at least 2024-01-01**. The next highest are 9,874 (2025-12-24) and, for 2024 to Aug 2025, 8,559 (2024-04-17). I ran two WebFetch passes over https://fred.stlouisfed.org/data/WLCFLPCL.txt and did not hand-check every row. The 2023 SVB-era readings were far higher, so "highest" means since Jan 2024 only.
- **Other lines, week ended 10/7:**
  - Total loans: avg 7,744; Wednesday 10,006.
  - Reserve balances: avg $3,029.7B (+81.6B w/w).
  - Treasury General Account: avg $880.3B (−68.4B w/w).
  - Overnight reverse repo, "Others": avg $1.2B.
  - Seasonal credit $35M; secondary credit $0.
- **Caveats:**
  - Wednesday levels are noisy, and the 9/30 week includes quarter-end.
  - H.4.1 does not say which banks borrowed.
  - The year-on-year change is erratic: it was −532 at the 10/1 release and +2,079 at this one.
- I found no BOARD signal tracking this series; the only hit was SIG-W-20260828-031, which is about discount-rate requests.

### a3. Fed speakers after 16:20 ET (NOTHING-NEW)

- **Fed Board calendar** (https://www.federalreserve.gov/newsevents/2026-october.htm): 10/8 shows only Waller (04:30 ET, Istanbul), already routed in -030. **10/9 shows no Board events.**
- **Musalem**, at Bloomberg's Future of Fixed Income event in New York around 13:57 ET, is already in -036 and outside the window. One third-party calendar listed a "Musalem 5:40 pm" slot with no detail. I found no evening remarks; it is probably a mis-listing of the same event (unverified).
- **Upcoming:** Kansas City Fed's Schmid, Fri 10/9 09:30 ET (Kiplinger's calendar, SNIPPET). Outside the window.
- **Market pricing:** FXStreet, republished by Mitrade, Unix timestamp = 21:05:52Z 10/8: *"near 81%"* odds of a December 25bp hike; October *"a long shot."* Attributed only to "money markets", not CME FedWatch. SECONDARY-READ: https://www.mitrade.com/au/insights/news/live-news/article-2-2149033-20261009

### a4. FDIC, Treasury and other OCC releases (NOTHING-NEW)

- **FDIC failed-bank list** (https://www.fdic.gov/bank-failures/failed-bank-list): latest entry **Nano Banc, Irvine CA, closed 2026-09-25**. Nothing for 10/8 or 10/9.
- **FDIC press releases:** latest 10/5, the CRA exam list. The page may be a cached snapshot. Failures are usually announced on Friday evenings, so tonight's absence is not informative about 10/9.
- **Treasury press releases:** 10/8, "Operation Economic Outcast…" (the Iran shadow fleet item), already in -034. Nothing dated 10/9.
- The government shutdown has been running since 10/1, per Waller's 10/8 text. The Fed, OCC and FDIC are self-funded and are still publishing.

---

## (b) After-hours: earnings, guidance and large moves

### b1. Telecoms fall after hours on SpaceX buying Grain's 800 MHz spectrum (NEW-ESTABLISHED, off-beat for credit)

- **CNBC live blog, post at 22:25:43Z** (SECONDARY-READ) — https://www.cnbc.com/2026/10/08/stock-market-today-live-updates.html
  - *"T-Mobile dropped 6%, AT&T fell almost 7% and Verizon lost more than 6%."*
  - SpaceX shares rose 2–3% after hours (separate CNBC post at 22:26:07Z).
- **Deal facts:**
  - Terms not disclosed; FCC approval pending (Via Satellite 10/8, SNIPPET).
  - Up to 14 MHz of paired 800 MHz spectrum.
  - T-Mobile sold this block to Grain in August for $2.9B plus 600 MHz licenses (SNIPPET).
- **Relevance:** these three carriers are among the largest issuers of investment-grade bonds. A 5–7% equity move is a credit-desk context item only. There is no rating action.

### b2. Humana up 12%, Alignment Healthcare down 23% on the CMS 2027 Star Ratings (NEW-ESTABLISHED, off-beat)

- CNBC, 22:25:43Z (SECONDARY-READ).
- **ALHC 8-K Item 7.01**, accepted 17:13:20 ET (PRIMARY):
  - Its California HMO contract H3815 (*"approximately 75% of the Company's health plan membership"*) is expected to fall to **3.5 stars for 2027, from 4.0**.
  - Verbatim on the cause: *"higher industry cut points and a decline in certain triple-weighted measures."*

### b3. Earnings after the close (NOTHING-NEW for the beat)

- Calendar: Earnings Whispers listed 6 reports after the close; Kiplinger listed *"no noteworthy"* ones.
- Park Aerospace (PKE, 8-K 2.02 at 16:27 ET): $0.21 EPS on $20.8M revenue; traded −1% after hours (CNBC).
- Oil-Dri and Nurix: not material.
- **Delta Air Lines reports Friday before the open** (outside the window).

### b4. Other after-close 8-Ks scanned (EDGAR latest-8-K feed, 16:00–17:30 ET), none material

| Filer | Accepted (ET) | What it says | Verdict |
|---|---|---|---|
| Super Micro (SMCI) | 16:31:30 | Item 5.02: Shesha Krishnapura (ex-Intel IT CTO) joins the board 10/9; Judy Lin retires *"not the result of any disagreement."* | NOTHING-NEW (AI-infra governance only) |
| Byline Bancorp (BY) | 17:15:13 | Chief Credit Officer Mark Fucinato and Head of Commercial Banking Brogan Ptacin retire 12/31/26; successors named, *"ongoing succession planning."* | NOTHING-NEW (no credit event) |
| Citizens (CFG) | 16:54:27 | Series G 4.000% preferred redeemed 10/6; certificate of elimination | NOTHING-NEW |
| MFA Financial (MFA) | 16:30:20 | CEO Knutson retires 6/30/27; Wulfsohn becomes CEO | NOTHING-NEW |
| Brookdale (BKD) | 16:19:01 | Sept occupancy 83.4% weighted average (consolidated) | Off-beat |
| Braemar Hotels (BHR) | 16:08:32 | Agreement to sell the **Four Seasons Resort Scottsdale for $372M**; activist settlement | Before the window; not distress |
| EOG, Diamondback, Devon | 16:01–16:18 | Items 2.02 / 7.01 | Before the window; energy, not this beat (not read) |

- AI names after hours were roughly flat (Yahoo post-market, VENDOR): NVDA $230.74 vs $230.48 close; ORCL $136.02 vs $135.69; CRWV $81.85 vs $81.58.
- The OpenAI $50B-revenue sell-off is already routed (-038). CNBC adds *"A $68 billion figure was widely reported last month"*; -038 used about $70B. That is a figure-basis difference, not a new event.

---

## (c) Credit and private credit

### c1. America's Car-Mart (CRMT): sixth lender bridge, now to 10/15 (CHANGE-TO-ROUTED SIG-W-20260925-004, PRIMARY)

- **8-K** accession 0001171843-26-006538, accepted **2026-10-08 16:05:15 ET (20:05:15Z)**, 15 minutes before the window opened. It is not in today's 45 titles.
- **Item 1.01**, verbatim: *"On October 8, 2026, the Agent and Lenders agreed to further extend the Scheduled Termination Date and the temporary relief with respect to the minimum liquidity thresholds and minimum Collateral Coverage Ratio through October 15, 2026."* The agent is Silver Point Finance.
- **Extension sequence**, from EDGAR submissions for CIK 799850: 9/7 → 9/11 → 9/18 → 9/24 → 10/1 → 10/8 → **10/15**.
  - The 10/1 extension (8-K accepted 10/1 08:30 ET) does not appear in WALTER's route_log after -0925-004. It may have gone straight to BROCK/OTTO; not checked.
  - Bridges 3, 4 and 6 were filed at about 16:05 ET on the expiry day itself.
- **Item 8.01**, verbatim:
  - *"The Company believes it has made significant progress towards a transaction and that discussions remain active with third-parties, the Agent, and the Lenders."* The same wording was used on 9/24, per OTTO STATUS.
  - *"the Company has experienced, or anticipates experiencing, events of default under the Credit Agreement."*
- **Owners per OTTO's docket:** BROCK grades; OTTO reads the consumer angle.

### c2. Private-credit vehicles selling or merging: Bloomberg 10/8 (NEW-UNVERIFIED, SNIPPET-ONLY)

- **Story:** "Ares, Apollo Among Firms Eyeing Troubled BDCs in Private Credit Shakeup" — https://www.bloomberg.com/news/articles/2026-10-08/private-credit-firms-see-rare-growth-shortcut-with-bdcs-for-sale
  - Snippet: *"Private credit managers increasingly looking to offload battered funds are drawing interest from rivals eyeing cheap deals…"*
  - *"Ares, Barings, BC Partners and Churchill Asset Management are among the firms that have run the rule over troubled funds"*; talks *"preliminary and may not result in any transactions."*
- **Publish time unknown** (Bloomberg returned 403), so I cannot say whether it falls inside the window. It is not in today's 45 titles, and I found no BOARD 10/0x match for the related terms.
- **Same day, probably Asia daytime (before the window):** Bloomberg, "Legacy Private Credit Loans Face Refinancing Risks as Rates Rise" (Milken Asia, Singapore; Lord Abbett flags 2021–22 vintage loans). SNIPPET-ONLY.

### c3. BDC unsecured bond issuance (NEW-ESTABLISHED, PRIMARY, context)

- **Bain Capital Private Credit (non-traded BDC)**, 8-K accepted 17:29:30 ET: **$350M of 7.600% unsecured notes due 10/8/2031**, a new base indenture with U.S. Bank Trust. Proceeds go to general purposes and revolver paydown.
- **Hercules Capital (HTGC)**, 8-K accepted 16:19:12 ET, just before the window: **$400M of 6.700% notes due 10/8/2029**. Underwriting agreement dated 10/5 (Goldman Sachs, SMBC Nikko).
- Both deals priced earlier in the week, so these are disclosures, not new prints. No pulled deals were found.

### c4. Other BDC 8-Ks (NOTHING-NEW)

- **FS KKR (FSK)**, 16:30:53 ET: Q4 distribution of $0.44 plus a **$0.20 special** (from spillover income), both declared 10/7; Q3 results due 11/5, before the open. No distress language.
- **Trinity Capital (TRIN)**, 17:30:13 ET: Q3 commitments $880M, funded $614M, repayments and exits $495M.
- **Crestline Lending Solutions**, 15:14 ET (before the window): base management fee cut to 0.85% annualized from 10/1.

### c5. Gates, defaults, downgrades, deal pulls (NOTHING-NEW in the window)

- **Gates:** most recent items are already known. KKR K-FITS went slightly over its 5% cap (Bloomberg 10/5). BCRED held 5% against about 10% requested. Blue Owl capped two BDCs (10/2; the tech fund had 39% requested).
- **Ratings:** nothing found dated 10/8 from Moody's, S&P or Fitch. Fitch's 10/8 AI stress-test report is a report, not a rating action.
- **Deal pulls:** no HY or IG pulls found. The muni deferrals were Bloomberg 10/5 (stale).
- **FRED HY OAS** (BAMLH0A0HYM2): latest observation is still **3.09 = 309bp [FRED, obs 10/7]**. There is **no 10/8 print yet** (checked about 00:30Z 10/9). The table also shows 10/6 3.03, 10/5 3.12, 10/2 3.10, 10/1 3.24.

---

## (d) Banks and CRE

### d1. Bank OZK RaDD/IQHQ $915M loan, maturing Fri 10/9 (NOTHING-NEW)

- Searched to about 00:40Z 10/9. I found no announcement, filing, or report of a longer-term extension, recapitalization, or default.
- The only 10/8 item is The Real Deal, "Loan modification again highlights Bank OZK exposure" — datePublished **18:53:40Z** (before the window), relaying Bisnow. Its spokesperson quote (*"short-term extensions routinely occur as the parties finalize documentation for longer-term extensions"*) is **already in SIG -017**. **STALE.**
- Background, SNIPPET: on the Q2 call, OZK President Hamblen said the bank was in talks with IQHQ and a mezzanine lender on a *"multiyear extension and recapitalization"* and said *"hopefully in around 92 days, we'll have more to report."*
- **Note:** Bank OZK files with the FDIC, not the SEC, so EDGAR silence is **not** evidence. Watch San Diego County recorder filings and OZK's Q3 release.
- OZK closed $44.86 [10/8]; flat after hours ($44.86 at 20:45Z, Yahoo).

### d2. Regional banks: WAL, ZION, FLG, VLY, KRE (NOTHING-NEW)

- No after-hours price moves (Yahoo, last bar 20:00–20:45Z): KRE $69.59, WAL $75.50, ZION $62.73, VLY $12.75, FLG $11.35.
- EDGAR filings since 10/6: WAL, ZION and VLY only Form 4s; latest VLY 8-K 9/28. FLG has no recent 8-K on EDGAR.
- Byline's Chief Credit Officer retirement is in b4 (succession, no credit event).

### d3. The Wymore 360, Altamonte Springs FL: Florida multifamily CMBS in special servicing (CHANGE-TO-ROUTED SIG -040, which "HELD pending an EDGAR check"; PRIMARY)

- **Source:** BMO 2024-5C8 Mortgage Trust 10-D, filed 2026-10-02, distribution date 09/17/26, determination 09/11/26. Ex-99.1: https://www.sec.gov/Archives/edgar/data/2044614/000188852426018403/bmo245c8_ex991-202609.htm
- **Loan:** Pros ID 10, loan 329221010, **$33,000,000**, interest-only, 6.839%, maturity 11/06/29.
- **Status:** paid through 07/06/26; one month delinquent; outstanding P&I advances $388,541.08.
- **Collateral and metrics:** 200-unit multifamily property, built 1973, renovated 2024. Appraisal $46.5M (5/10/24). DSCR **0.6528** (6/30/26). NOI $744,849.40.
- **Special servicing:** transferred **08/11/26**; resolution strategy code **2 = Foreclosure**. The trust-level special servicer named in the 10-D is CWCapital, which replaced Greystone effective 7/29/26 per the trust's 8-K. I did not confirm that CWCapital services this particular loan.
- **Servicer comment, verbatim:** *"The loan transferred to special servicing effective 8/11/2026 due to Payment Default … As of July 2026, the collateral was 89.5% occupied. The Borrower signed a PNA in August 2026. Borrower noted in the initial discussions that they wanted to work with the special servicer on a transition of the property. The special servicer is evaluating rights and remedies."*
- **Not new in the window.** The fact dates to 8/11, and the Connect CRE relay ("Return to Lender: Week of Oct. 8, 2026") is SNIPPET-ONLY. What is new is the PRIMARY confirmation that resolves -040's hold. Florida item (CORAL / HOMER / CREED case feed).

### d4. St. Luke's Office, Allentown PA: special servicing confirmed (NEW-ESTABLISHED, not window-new, PRIMARY)

- **Source:** JPMCC 2017-JP7 10-D, filed 2026-09-28, distribution 09/17/26. Ex-99.1: https://www.sec.gov/Archives/edgar/data/1709967/000188852426017410/jpc17jp7_ex991-202609.htm
- **Loan:** Pros ID 14, loan 307331013, office, Allentown PA.
  - This trust's piece: **$14.47M**.
  - Total: **$43.4M** split across JPMCC 2017-JP7 and CSAIL 2017-C8, per Morningstar Credit via Connect CRE (SNIPPET).
- **Special servicing:** transferred **08/13/26**, *"Imminent default due to cash flow issues"*; strategy code 13 (TBD).
- **Metrics:** paid through 08/06/26 (current). DSCR 1.2952 (6/30/26). Appraisal $92.0M (12/05/16). Maturity 05/06/27.
- **Cause per Morningstar (SNIPPET):** Intel, the second-largest tenant (24% of space, 32.5% of underwritten base rent), left in 2026.

### d5. 70 Broad St (American Bank Note Co. Building), Manhattan: sold below the loan (STALE, 10/6, but I found no BOARD match; possible case lead)

- Sold for **$9.35M** by Wilmington Trust (CMBS trustee), with Rialto Capital as special servicer.
- The 2015 loan was **$15M** (Silverpeak). The foreclosure judgment was $24.7M, and the lender took the building with a $20M credit bid in 2025.
- Connect CRE cites a $14.1M loan balance (SNIPPET).
- Sources: The Real Deal 10/6 (https://therealdeal.com/new-york/2026/10/06/historic-fidi-building-sells-for-miniscule-9-4m-sum/), Commercial Observer (SNIPPET).

### d6. Other CRE (NOTHING-NEW in the window)

- The Connect CRE roundup also cites an Everett, WA office site (Rialto foreclosed 3/2025, $28M CMBS). Stale.
- No new named-property default, receivership or note sale found with a 10/8-evening timestamp. Bisnow, Commercial Observer and CRE Direct searches turned up only September items.

---

## (e) Asia open (Fri 10/9; Tokyo opened 00:00Z)

### e1. JGBs rally at the open, led by the 30-year (NEW-ESTABLISHED as a vendor level; cause UNKNOWN)

- **CNBC quote service**, quotes stamped 09:23–09:30 JST 10/9 = 00:23–00:30Z. VENDOR.

| JGB | Last | Change | Prior close (CNBC basis) |
|---|---|---|---|
| 30Y | **4.073%** | −11.3bp | 4.186% |
| 10Y | **3.042%** | −4.2bp | 3.084% |
| 2Y | 1.918% | −2.1bp | 1.939% |

- Trading Economics separately shows the 10Y at **3.044%** dated Oct 9 (−0.042), which agrees.
- **Cause unknown.** I found no news of an MOF issuance change. One possible input is Thursday's 30Y auction result (e2), which came before the window. SIG -029 already carries Takaichi's pledge to keep JGB sales around the FY25 level. The rally is consistent with that but is **not established** as its cause.
- A one-day move of this size in super-long JGBs is worth SAM/HANS attention, but these are early-session vendor prints, not closes.

### e2. MOF 30Y JGB auction, Thu 10/8 (before the window; I found no BOARD match; PRIMARY)

- Source: https://www.mof.go.jp/english/policy/jgbs/auction/calendar/eresul/eresul20261008.htm
- **Issue 92**, 4.2% coupon, maturing 9/20/2056.

| Measure | Value |
|---|---|
| Competitive bids | ¥1,747.2bn |
| Accepted | ¥450.7bn |
| Bid-to-cover | 3.88× (my calculation from the two lines above) |
| Lowest accepted price | 101.05 (yield **4.121%**) |
| Average price | 101.21 (yield **4.109%**) |
| Price tail | 0.16 (about 1.2bp in yield) |
| Non-price-competitive I | ¥148.9bn |

- Bloomberg called demand *"firm"* and above the 12-month average of 3.56× (SNIPPET).
- Relevant because -021 records the 30Y high at 4.168% on 10/6 (MOF basis).

### e3. Japan August household spending (NEW-ESTABLISHED; PRIMARY y/y, SNIPPET for consensus and m/m)

- **Statistics Bureau of Japan, released 9 Oct 2026** (08:30 JST = 23:30Z 10/8): real consumption expenditure of two-or-more-person households, **−3.1% y/y**. https://www.stat.go.jp/english/data/kakei/156.html
- **Newsquawk headline (SNIPPET, relative time "1 hour ago" at about 00:30Z):** −3.1% vs −3.6% expected (prior −3.6%); m/m +0.1% vs +0.5% expected (prior +0.5%).
- Context: BOJ's Sato (Kyodo, 10/6, stale) tied the timing of the next hike to *"developments in consumption and income."*

### e4. USD/JPY, Nikkei and regional markets (NOTHING-NEW in direction)

- **USD/JPY 158.06** at 00:30Z (Yahoo; day range 157.77–158.13; prior close 157.79). Trading Economics shows 158.04 dated 10/9. VENDOR.
- **No MOF/BOJ remarks found.** Katayama: searches returned nothing dated 10/9; the latest is the Japan Times 10/8 piece, "Takaichi isn't a reflationist." Mimura: latest 9/28.
- **Nikkei 225: 68,243** at 00:15Z, **−1.16%** vs 69,042.11 (Yahoo, VENDOR). CNBC (23:29:56Z): CME futures 68,515, Osaka 68,390 before the open.
- **Other markets:**
  - Korea is closed (Hangul Day) per CNBC.
  - ASX 200 +0.4% early (CNBC; Yahoo 8,697.7 vs 8,660.9).
  - Hang Seng futures 23,802 vs 23,785.79 close (CNBC).
- **China:** mainland markets **reopened Thu 10/8, not 10/9**. The Shanghai Composite closed 3,811.90 on 10/8 (−0.79%, Yahoo). Offshore yuan (CNH) 6.7025 at 00:30Z. **The PBOC fix (01:15Z) and the Hong Kong open (01:30Z) are after this report.**
- **China property / Vanke:** nothing dated October found (latest April 2026).
- Other overnight quotes (Yahoo, 00:16–00:20Z): S&P futures 7,826.75 (+0.13%); Brent $103.81 (−0.45%); gold $4,173.2 (+0.4%).

---

## (f) Europe overnight (after 16:20 ET = 22:20 CET)

### f1. UK gilts and the Budget (NOTHING-NEW; one vendor-basis note for HANS)

- No Treasury or BoE releases and no Budget leaks found after 22:20 BST. The chancellor is **John Healey** and the Budget is Wed 10/28. The latest options piece is Reuters' factbox of 10/7 (stale).
- **Vendor-basis note on SIG -032 and -037 (not a grade):** CNBC's quote service shows a different "previous close" from the Trading Economics closes routed in -037.

| Gilt | CNBC "prev close" | CNBC last (00:25–00:30Z 10/9) | TE close (in -037) |
|---|---|---|---|
| 30Y | **5.9972%** | 5.9888% | 5.9384% |
| 10Y | **5.4852%** | 5.4231% | 5.4238% |

  - The CNBC close cut-off time is undocumented, likely a New York time.
  - The 30Y is under 6.00 on both bases. On CNBC's basis it is **0.3bp** from the T-13 line, not about 6bp. This adds to -037's warning that the basis is "still too close." HANS needs its declared official basis (the DMO/BoE close), not either vendor.

### f2. France / OATs (NOTHING-NEW in the window)

- The OAT–Bund spread of about 139–142bp and Lescure's quote are already in -022.
- CNBC 18:50 CEST quotes give FR10Y 4.8199% and DE10Y 3.4585% (about 136bp; VENDOR, before the window).
- A paid-newsletter snippet (Trader Alpha, "Hypo 8th October") says the Bank of France governor said *"conditions for ECB intervention aren't met"* and that December ECB hike odds slipped to 85%. SNIPPET-ONLY, timing unclear, and it does not look like it is in -022. Low weight.
- No new no-confidence or Lecornu news found.

### f3. ECB (NOTHING-NEW)

- No ECB publication found after 22:20 CET. The ECB publications-by-date page did not render a list. The September account (10/8) is already in -022.

---

## Out-of-beat items seen (for the other sweep agents)

- **CNBC 23:29:56Z:** *"oil prices rose after President Donald Trump said he was not keen on making a deal with Iran to end the war."* That is the Iran beat (compare -034).
- **Newsquawk, about 5h before 00:30Z:** French Armed Forces chief, *"about 2,000 soldiers have been deployed to the Gulf"*; Yanbu options *"still being studied."* That is -043's beat.
- **Japan pre-market:** Fast Retailing guided FY27 net profit to ¥560bn (Newsquawk SNIPPET). Off-beat.

## Method / sources checked

- Fed recent postings, calendar and H.4.1; OCC news release; FDIC failed-bank list and press releases; Treasury press releases.
- EDGAR latest-8-K atom feed (100 entries, 09:46–17:30 ET 10/8), plus EDGAR submissions JSON for AXP, CRMT, OZK, WAL, ZION, FLG, VLY, ALHC, HUM, BMO 2024-5C8 and JPMCC 2017-JP7.
- CNBC live blog via curl (JSON-LD timestamps); CNBC quote service; Yahoo chart API; FRED; MOF; Statistics Bureau of Japan; Trading Economics.
- Newsquawk headline page (relative timestamps); WebSearch for Bloomberg, Reuters, Bisnow, The Real Deal, Commercial Observer, CRE Direct and Connect CRE (several returned 403 / snippet-only).
- Downloaded copies are in the scratchpad `sweepC/` folder, not the repo.
