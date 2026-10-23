# Reader C: Paramount Skydance / Skydance Corp (SKYD), the WBD deal, credit, and the Musk $1B report

**Prepared:** 2026-10-22 20:42 ET (per `date`) (read-only reader C for PROME). **Method:** SEC EDGAR direct pulls (data.sec.gov submissions, filing documents, XBRL), company press release (8-K Ex. 99.1), WebSearch/WebFetch for press, `FORGE/tools/market-data/fetch.py` for the live price. 16 of 25 web searches used.
**Confidence tokens:** VERIFIED = checked at the primary artifact. INFERRED = supported, not directly established. SEARCH-NOT-FOUND = query returned nothing. UNKNOWN. Press-only claims are labelled SECONDARY.

## 0. Corrections to what was pasted / assumed

| Item | Finding | Token |
|---|---|---|
| Company name / ticker | "Paramount Skydance (PSKY)" is retired. Renamed **Skydance Corporation**, Class B moved Nasdaq to **NYSE: SKYD** on 2026-10-06. Warrants trade as **SKYD WS** (NYSE). PSKY still appears in the EDGAR ticker list as a legacy tag. | VERIFIED (8-K filed 2026-10-06, Explanatory Note; 8-K filed 2026-10-13) |
| WBD deal status | **CLOSED 2026-10-06.** WBD is a wholly owned subsidiary. Not pending. | VERIFIED (8-K 0001104659-26-113913, Ex. 99.1) |
| "Controlling CBS, CNN, HBO, Warner Bros." | Matches the company's own closing release (CBS, HBO, CNN, CBS News, TNT Sports, two studios, two streamers). | VERIFIED (Ex. 99.1) |
| Musk $1B | **Reported only** (Semafor exclusive 2026-10-22, anonymous sources). No filing found. See section 4. | VERIFIED as "reported"; filing SEARCH-NOT-FOUND |

## 1. Skydance-Paramount merger (closed 2025-08-07) and Ellison/RedBird equity

| Fact | Value | Source / date | Token |
|---|---|---|---|
| Closing | 2025-08-07: Paramount Global and Skydance Media became wholly owned subs of Paramount Skydance Corp | 8-K Ex. 99.2 pro forma notes (filed 2026-10-06) | VERIFIED |
| PIPE at that closing | $6.0B for 400M Class B at $15.00; NAI equity investors also got 200M five-year warrants at $30.50 | same | VERIFIED |
| Use of PIPE | ~$4.5B funded the cash-election leg for Paramount Global holders; ~$1.5B to the company | same | VERIFIED |
| Control | Entities controlled by the Ellison Family (Lawrence J. Ellison and David Ellison) hold ~77.5% of Class A indirectly via NAI (renamed Harbor Lights Entertainment); RedBird holds the rest. Ellison Family + RedBird are sole Class A holders = **100% of voting power** (Class B is nonvoting). | same; Ex. 99.1 (2026-10-06) | VERIFIED |
| Ellison Family total economic stake today | Press release says "largest equity stake"; no percentage found. Depends on how much of the Trust's $46.7B allocation was retained vs syndicated (section 2). | | UNKNOWN |
| Paramount-side debt pre-WBD | Long-term debt $14,491M + current $665M at 2026-06-30 | Ex. 99.2 pro forma balance sheet | VERIFIED |

## 2. The WBD transaction (status as of 2026-10-22: CLOSED)

**Timeline (primary unless marked):**

| Date | Event | Source | Token |
|---|---|---|---|
| 2025-12-04 | Netflix-WBD merger agreement signed (Netflix, Nightingale Sub, New Topco 25) | 8-K filed 2025-12-22 (risk-factor text) | VERIFIED |
| 2025-12-08 | Paramount commitment letter: $49.0B 364-day bridge (BofA, Citi, Apollo) | 8-K filed 2026-10-06 Item 1.01 | VERIFIED |
| 2025-12-22 | Paramount amended hostile tender; Larry Ellison "irrevocable personal guarantee" of $40.4B reported | 8-K filed 2025-12-22; amount SECONDARY (TheWrap/CNN 12/22) | VERIFIED (tender) / SECONDARY (amount) |
| 2026-01-19 | Netflix-WBD agreement amended and restated | 8-K filed 2026-03-02 | VERIFIED |
| 2026-02-27 | **WBD-Paramount merger agreement signed** ($31.00 cash/share plus ticking fee $0.00277778/day after 2026-09-30). Netflix agreement terminated before signing. Paramount paid the **$2.8B Netflix termination fee**. | 8-K filed 2026-03-02 | VERIFIED |
| 2026-06 | DOJ cleared with no conditions (eight-month review) | SECONDARY (CNN/KRDO 2026-06-12; Variety AU) | SECONDARY |
| ~late 2026-09 | 12-state AG litigation settled, last major hurdle (company agreed commitments Fitch calls "largely achievable") | SECONDARY (TheWrap 2026-10-06 quoting Fitch; Semafor/IBTimes) | SECONDARY |
| 2026-10-05 | Notes issued, TLB funded | 8-K | VERIFIED |
| **2026-10-06** | **Closing.** Cash $31.01666668/share. "Nearly 70 jurisdictions" cleared (company claim). | 8-K Ex. 99.1 | VERIFIED |
| 2026-10-13 | 470,746,773 warrants (strike $12.00, 10-year) distributed as a dividend to Class B holders of record 10-05 other than Ellison/Cardinale/Trust/RedBird and benefit plans | 8-K filed 2026-10-13 | VERIFIED |
| 2026-10-09 | Exchange offers settled: ~99.15% of WBD (DCL/DGH) exchange-offer notes tendered into new second-lien notes: $11,983,970,000 + EUR 546,547,000 | 8-K filed 2026-10-13 | VERIFIED |

**Price and consideration.** $31.00 plus $0.01666668 ticking = $31.01666668/share. Total cash to WBD holders $77,990M (incl. ticking $41.9M). Total cash consideration incl. WBD debt settlement $93,772M; with the Netflix fee, total purchase consideration $97,186M. EV ~ $110B (press). Source: Ex. 99.2 and 8-K Item 2.01. VERIFIED (pro forma is "preliminary").

**Competing bidders.** Netflix: signed 2025-12-04, lost; received $2.8B fee paid by Paramount (VERIFIED). **Comcast:** no Comcast bid found in the filings or in my searches (SEARCH-NOT-FOUND; not exhaustively checked).

**Financing, as filed (8-K 0001104659-26-113913, Items 1.01, 3.02):**

| Layer | Amount | Terms | Token |
|---|---|---|---|
| **Equity (PIPE)** | 3,917,657,246 Class B shares x $12.00 = **$47.0B** (company: "$47 billion") | Nonvoting Class B. Subscription agreements (2026-02-27) with Lawrence J. Ellison Revocable Trust affiliates (up to $46.72B + ticking) and RedBird ($250M); rights **assigned to a syndicate**: Trust/RedBird affiliates, **PIF, L'imad (Abu Dhabi), QIA, LionTree** (Ex. 99.2; Ex. 99.1). Per-party allocations not disclosed in what I read. 180-day lock-up, pledging of PIPE shares expressly permitted. | VERIFIED |
| First-lien senior secured notes | **$30.0B**, 8 series 2028-2066, coupons 6.30% to 8.90% (e.g., 2033 $5.25B at 7.55%; 2036 $5.25B at 7.90%; 2046 $1.25B at 8.65%; 2056 $3.5B at 8.75%; 2066 $1.25B at 8.90%) | Investment-grade-event lien release clause | VERIFIED |
| Second-lien notes | **$11.4B** USD (2031 $6.0B at 8.25%; 2034 $4.0B at 8.875%; 2036 $1.4B at 9.125%) + **EUR 885M** 7.00% 2031 | | VERIFIED |
| Term B-1 | $8.5B + EUR 850M, 7-yr, SOFR/EURIBOR + 2.50-2.75% | | VERIFIED |
| Term A / revolver (existing, 2026-04-07) | $2.5B Term A-1 (3-yr) + $2.5B Term A-2 (5-yr); $5.0B revolver undrawn at close | | VERIFIED |
| Bridge | $49.0B commitments reduced to $0, terminated at close | | VERIFIED |
| Debt-side arrangers | BofA, Citigroup, Apollo (Apollo Global Securities was a representative of the initial purchasers) | | VERIFIED |
| Exchanged WBD notes | $11.98B + EUR 0.55B now second-lien Skydance notes (above, 2026-10-09) | | VERIFIED |

**Pro forma debt (Ex. 99.2, balance at 2026-06-30, preliminary):** long-term debt $80,323M + current $2,158M = ~$82.5B; pro forma cash $7,888M; six-month pro forma net interest expense $3,090M. Other estimates differ: Fitch ~$87.5B total debt (TheWrap 2026-10-06, SECONDARY); Debtwire net debt $84.3B at close and "$80B" press shorthand. Reconcile before quoting a single figure. Net leverage target 3.0x by end-2029, >$6B run-rate synergies in 3 years, >$10B FCF by 2030 (company, forward-looking). Debt-in-equity-terms: SKYD at $7.79 (2026-10-22, fetch.py) is **35% below the $12.00 PIPE price** ((12.00 - 7.79)/12.00); ~5.0B shares x $7.79 = ~$39B market cap is INFERRED (share count = ~1.07B Class B at 2025-11-05 per XBRL + 3.918B PIPE; not read from a current cover page).

## 3. Ratings, bonds, CDS

| Agency | Issuer | Secured notes | Date / action | Source | Token |
|---|---|---|---|---|---|
| Fitch | **BB** (from BB+) | 1L **BBB-/RR1**, 2L BB/RR4, sr unsecured BB-/RR5, WBD sr unsecured B+/RR6 | At closing, article 2026-10-06; leverage est. 7.8x FY26, 6.2x FY27, 4.5x FY28; says 3x by 2029 likely needs equity/asset sales. Earlier 2026-03 cut BBB- to BB+ on watch negative | TheWrap 2026-10-06 | SECONDARY (Fitch release not retrieved) |
| S&P | **BB** (from BB+) on 2026-09-24; leverage ~7.6x through 2027; downgrade threshold had been 4.25x | 1L investment grade (per Bloomberg 9/30 via Tiger summary) | Earlier 2026-02-27 CreditWatch; March BB+ outlook negative | IBTimes 2026-10-15; Tiger/Bloomberg 2026-09-30 | SECONDARY |
| Moody's | Issuer rating not found. New 1L and 2L notes rated **speculative grade** (1L one notch below IG); cites ~7x leverage and "highly concentrated equity ownership" governance risk. WBD unsecured cut to Ba1 earlier. | | late 2026-09 | Bloomberg via Tiger 2026-09-30; TheWrap | SECONDARY / issuer UNKNOWN |

Reading: Fitch and S&P put the **issuer in junk (BB)** while the 1L notes get IG at Fitch/S&P (and not at Moody's). Bloomberg: Paramount joins "biggest junk borrower ranks" (headline, SECONDARY).

**Market levels:**

| Metric | Level | Date | Source | Token |
|---|---|---|---|---|
| 5Y CDS ("Paramount Global" reference) | **577 bp** (from 268 bp on 2026-09-17) | 2026-10-13 | Debtwire via IBTimes 2026-10-15 | SECONDARY; reference-entity label is the legacy name, successor mapping UNKNOWN |
| 5Y CDS, second report | 576 bp "record", ~39.5% implied default probability, LSEG data | 2026-10-14 | rallies.ai headline surfaced by search; I could not retrieve the figure from the page | UNVERIFIED (my arithmetic: 576 bp x 5 / 0.6 recovery gives ~38%, consistent but not a confirmation) |
| DTCC | DTCC publishes notional/trade-count, not single-name spread levels | | | SEARCH-NOT-FOUND |
| 2036 2L 9.125% notes | ~**91** (issued at par 2026-09-30) | 2026-10-13 | IBTimes 2026-10-15 | SECONDARY; implied yield ~10.4% is my approximation, INFERRED |
| 8-yr USD notes (2033 1L 7.55% by tenor) | ~96 (par 9/30), ~95 per another report | 2026-10-01 | Bloomberg (BGOV, truncated) | SECONDARY |
| 10-yr $5.25B note (2036 1L 7.90%) | quoted near +278 bp over Treasuries | ~2026-10-01 | newsletter summary via search | SECONDARY, not fetched |
| New IG issues vs JPM IG index | lagged by 27 bp over 10 days to 2026-10-08, "weakest since April 2020" (ex-Skydance +4 bp) | 2026-10-08 | Bloomberg bank note via IBTimes | SECONDARY |
| Financing package | ~$52B (about $30B IG-rated, $12.4B HY, ~$9.5B loans) priced the week of 9/28; IG book reported >$109B of orders | 2026-09-28 to 10-01 | Bloomberg via Tiger | SECONDARY |
| Media peer comparison (WBD legacy, Comcast, Netflix CDS/spreads) | not retrieved | | | UNKNOWN |

**Distress language** appears in press ("junk," "bond selloff signals doubts," "default risk," "lower expected recoveries," CreditSights: "historical record of media megamergers is abysmal"). No distressed-exchange or covenant event found. Warrant SKYD WS closed $2.20 on 2026-10-13 (rallies.ai); director Gerald Cardinale bought 4.9M warrants at $2.80 on 2026-10-16 (Form 4 filed 2026-10-20, accession 0000895345-26-000470). The stock fell ~24% on 2026-10-14 (largely warrant ex-date, IBTimes).

## 4. The Musk $1B

| Question | Answer | Token |
|---|---|---|
| Origin | Semafor "Exclusive: Elon Musk makes $1 billion investment in Ellison's Skydance," Rohan Goswami, 2026-10-22 (page also lists an update that day). URL: https://www.semafor.com/article/10/22/2026/elon-musk-makes-1-billion-investment-in-ellisons-skydance. Bloomberg ("Musk Has Invested $1 Billion in Skydance, Semafor Reports"), CNBC, TheWrap, Deadline, Yahoo followed. TheWrap states it did not independently confirm. Investing.com says Semafor is the only original reporter. | VERIFIED (that it was reported); the facts themselves SECONDARY, single-source |
| Precursor | Semafor 2026-09-23: Paramount executives "discussed asking Musk to join a syndicate of equity investors"; size unknown; Musk one of several wealthy individuals David Ellison had considered. https://www.semafor.com/article/09/23/2026/paramount-weighs-tapping-musk-for-equity-investment | VERIFIED as reported |
| Amount | "roughly $1 billion," people familiar | SECONDARY |
| Entity (Musk personally vs a company) | **Not stated.** SpaceX did not respond (TheWrap). Per reports (Jan-Feb 2026) xAI, Grok and X were folded into SpaceX; a Yahoo page shows SpaceX quoted as SPCX, so a corporate buyer could be a public company with its own disclosure duties. That is INFERRED context, not a finding about this deal. | UNKNOWN |
| Instrument, price, stake | **Not stated.** "Equity investments" is the word applied to Skydance's other backers around the same time, including director Laurene Powell Jobs. Valuation and percentage undisclosed. | UNKNOWN |
| Part of the WBD financing package? | The closing PIPE (8-K Item 3.02) lists PIF, L'imad, QIA, LionTree, Trust/RedBird affiliates; Musk is **not named**. Semafor frames his money as arriving "at roughly the same time" as other investors' equity. Whether it is a slice of the 3.918B-share PIPE (e.g., sold by the Trust or syndicate), a later issuance, or a secondary purchase is unknown. | UNKNOWN |
| Comparable verified item | Laurene Powell Jobs: Form 4 (filed 2026-10-08) shows 20,833,333 Class B at $12.00 on 2026-10-06 = **$250.0M** (accession 0001193125-26-418171). She is a director so a Form 4 was mandatory. | VERIFIED |
| Filing check | EDGAR submissions for CIK 2041610 through 2026-10-22 20:39 ET: **no 8-K, 13D, or Form D referencing Musk**; latest filings are S-8 (2026-10-21), Form 4s (10-19, 10-20), 8-K (10-16). EDGAR full-text query "Skydance" + "Musk" for 2026-10-01 to 10-22 returned 0 hits (index may lag). Absence does not refute: a ~$1B stake at $12 is ~83M shares (INFERRED, ~1.7% of ~5.0B), under the 5% Schedule 13D and 10% Section 16 thresholds, and a Form D is not used for a registered issuer's Section 4(a)(2) PIPE. An Item 3.02 8-K would be expected within four business days only if it were a new unregistered issuance above 1% of the class (INFERRED rule application; no such 8-K by 10-21). | SEARCH-NOT-FOUND (owner-declared EDGAR path checked; no fallback exhausted) |
| Strategic or support capital? | **Unknown.** Press speculates about a Starlink/SpaceX distribution tie. John Malone (Paley summit, 2026-10-21): "I think there's a deal coming there," predicting $8-10B cross-investment and a global content distribution partnership (SECONDARY via TheWrap/Yahoo; unconfirmed, Malone is not a party). No xAI, X or Grok content/data counterparty found anywhere in the filings or reports. | UNKNOWN |
| Market reaction | SKYD jumped ~6% then reversed to about -2%/-2.4% after a halt (Investing.com 2026-10-22). Live: **$7.79, -1.02%, volume 55.8M** (fetch.py, as-of 2026-10-22). Note: Musk $1B vs ~$39B INFERRED market cap and ~$82-87B debt is small. | VERIFIED (price) / SECONDARY (intraday) |
| Pasted text accuracy | "Larry invested $1B in Twitter, backed Tesla, Tesla board": repeated in Semafor/CNBC (SECONDARY); not checked in primary filings by me. | SECONDARY |

## 5. Larry Ellison's role in the deal documents

| Item | Finding | Source | Token |
|---|---|---|---|
| Equity commitment | Lawrence J. Ellison Revocable Trust: subscription for up to **$46.72B** (+ ticking, + contingent equity, + amended-notes amount); RedBird $250M | 8-K filed 2026-03-02 (Subscription Agreements) | VERIFIED |
| Guarantee (filed form) | **The Trust AND Larry Ellison personally, jointly and severally**, guaranteed to WBD: the Netflix termination fee, the "Amended Notes Payment Amount," **$45.72B of the Merger Consideration** + Contingent Equity Amount, damages for breach/fraud, the **$7.0B Regulatory Termination Fee**, certain costs. Covenants: reasonable best efforts on regulatory approvals; litigate to defend; no actions impairing ability to perform. Controlled affiliates covenant **excludes Oracle Corporation and Ellison Institute of Technology**. | 8-K filed 2026-03-02 | VERIFIED |
| "$40B+" figure in the press | "$40.4B irrevocable personal guarantee" (Dec 2025 version); Semafor now repeats "more than $40 billion." The Feb-2026 filed guarantee is larger ($45.72B of consideration). Different versions; use the filed text. | TheWrap 2025-12-23; Semafor | SECONDARY / VERIFIED |
| Syndication effect | Equity syndicated to PIF, L'imad, QIA, LionTree and affiliates; "aggregate allocations covered the full amount committed." What the Ellison Family kept is not in what I read. Whether the guarantee is discharged post-closing is INFERRED (consideration paid; filings after 10-06 do not mention it). | Ex. 99.2 | INFERRED |
| Oracle share pledge tied to the financing | Paramount said (Dec 2025) the Trust holds ~1.16B Oracle shares and committed not to revoke/adversely transfer it while the deal was pending (SECONDARY). No pledge of Oracle stock **disclosed in the deal documents** I read (8-K filed 2026-03-02, 8-K and Ex. 99.2 filed 2026-10-06). A Motley Fool piece cites 346M Oracle shares pledged against personal debts per Oracle's proxy (SECONDARY, unverified; reader D covers the proxy). The 10-06 8-K lock-up expressly allows PIPE investors to **pledge** their new shares. | | SEARCH-NOT-FOUND for deal-doc pledge |
| Not read | Schedule 13D / Section 16 filings for the Trust's current Skydance holdings; the Trust's actual post-syndication stake; the full subscription/assignment exhibits | | UNKNOWN |

## 6. Gaps and what I could not reach
- Primary rating-agency releases (Moody's, S&P, Fitch): paywalled; ratings are from press.
- CDS: only Debtwire/LSEG-via-press; no Markit/ICE/Bloomberg screen, no DTCC single-name level; peer CDS/spreads not retrieved; reference-entity (legacy "Paramount Global" vs Skydance Corp) after the exchange unknown.
- Bloomberg, Deadline, CNBC, Variety primary pages blocked (403/paywall); content taken from Semafor, Yahoo, TheWrap, Investing.com, Stocktwits summaries.
- Musk: entity, instrument, price, whether in the PIPE or a secondary: not found anywhere.
- Current share count and Ellison Family percentage: not retrieved.
- Competing bidder Comcast: SEARCH-NOT-FOUND.

## SUMMARY FOR PROME
1. **WBD deal CLOSED 2026-10-06** (8-K 0001104659-26-113913); company renamed Skydance Corp, now **NYSE: SKYD** (PSKY retired). Cash $31.01666668/share; ~$110B EV (press). Netflix lost; Paramount paid its $2.8B break fee. Comcast bid: SEARCH-NOT-FOUND.
2. **Funding (filed):** $47.0B Class B PIPE at $12.00 (3.918B shares; Ellison Trust/RedBird, PIF, L'imad, QIA, LionTree), $30.0B 1L notes, $11.4B + EUR885M 2L notes, $8.5B + EUR850M TLB, $49B bridge terminated unused; BofA/Citi/Apollo. Pro forma debt ~$82.5B (6/30 basis); Fitch says ~$87.5B.
3. **Stock is 35% below the PIPE price:** SKYD $7.79 (-1.02%) on 2026-10-22 vs $12.00; 471M warrants at $12 strike were dividended 10/13.
4. **Credit:** Fitch BB (10/6; 1L BBB-), S&P BB (9/24; 1L IG), Moody's notes junk. 5Y CDS reported 577 bp on 10/13 vs 268 bp on 9/17 (Debtwire, legacy "Paramount Global" label); 2036 2L 9.125% ~91. All SECONDARY.
5. **Musk $1B: REPORTED, NOT FILED.** Single source Semafor (2026-10-22), amount "roughly $1B," unnamed sources; entity (Musk vs SpaceX), instrument and price unstated. No 8-K, 13D or Form D found through 2026-10-22 20:39 ET; absence is not disproof (~1.7% stake, below 5%/10% thresholds).
6. **Musk is not among the named PIPE parties** in the 10/6 8-K. Verified comparable: Laurene Powell Jobs bought $250M at $12.00 (Form 4, 10/8). Musk's money may be a slice of the PIPE, a later issuance, or a secondary; unknown.
7. **Strategic vs support:** no xAI/X/Grok/Starlink contract found; only Malone's unconfirmed prediction (10/21) of an $8-10B cross-investment and distribution deal. Treat as unconfirmed.
8. **Larry Ellison (filed, 8-K 2026-03-02):** Trust plus Larry personally, jointly and severally, guarantee $45.72B of consideration, the Netflix fee, and the $7B regulatory break fee; Oracle and the Ellison Institute are carved out of the covenants. No Oracle share pledge disclosed in the deal documents; press cites 346M pledged (reader D's lane).
9. **Load-bearing uncertainties:** (a) how much of the $47B the Ellison Family retained after syndication (sets their real exposure and whether the guarantee still binds); (b) the Musk vehicle and terms, resolvable by an 8-K/13D/Form 4 or SpaceX disclosure.
10. **Not reached:** agency releases, CDS screens or DTCC single-name levels, peer spreads, current share count.
