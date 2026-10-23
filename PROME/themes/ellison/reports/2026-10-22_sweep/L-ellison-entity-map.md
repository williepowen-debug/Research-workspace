# L - The Ellison entity map (every entity, its claim on or contribution to Larry Ellison's liquidity)

**Reader L (read-only; Sonnet 5.5).** Written 2026-10-23 00:0x ET (`date` run at 00:01:13 EDT). WebSearch used: 25 of 25 (the cap was reached on the last call). EDGAR, Companies House and company pages read directly (WebFetch / curl). Not committed.
**Tokens:** VERIFIED = read at a primary document this session. INFERRED = derived or supported, not directly established. REPORTED = press only (secondary). SEARCH-NOT-FOUND = query returned nothing; UNKNOWN = could not reach. No trade recommendation.
**Prices (fetch.py, 2026-10-22 close; FX not fetched):** ORCL $125.54 · SKYD $7.79 · TSLA $374.58 · SPCX $144.75 (vendor marks the SPCX bar "stale"; day change -9.14%, so treat the level as soft). GBP/USD was NOT verified; any dollar conversion of sterling below assumes $1.30-1.35 per pound and is labelled INFERRED.

---

## 0. Findings that change the picture (read these first)

1. **The EIT funding is large, recent and is paid in CASH into a UK company, and it was still running in the last 30 days.** Ellison Institute of Technology, Oxford Limited (Companies House 13773507) issued shares "for cash" at GBP 5,000,000 each on 2026-03-11 (59 shares, GBP 295M), **2026-09-24 (70 shares, GBP 350M)** and **2026-09-25 (33 shares, GBP 165M)** = **GBP 810M in 2026 so far**, of which **GBP 515M in the two days 9/24-9/25** (the proxy was filed 9/25; the Citi/JPMorgan collateral additions were reported ~9/25-10/1; the Skydance deal closed 10/6). Calendar 2025: GBP 725M of shares plus GBP 91.2M of capital contributions; 2024: GBP 516.1M of shares plus GBP 208.8M of contributions. Nothing was paid in before 2024 (equity -GBP 4.0M at 1/1/2024). VERIFIED (accounts to 12/31/2025 filed 2026-09-28; SH01 filings 2026-04-20, 2026-09-25, 2026-10-12). The source of the cash is not disclosed (see section 3). The carve-out of EIT from the Skydance guarantee covenants therefore matters: EIT is the one large, dated, recurring cash outflow that is not inside Skydance.
2. **Annapurna is NOT a precedent for an unconditional backstop. It is a precedent for a negotiated discount buyout with no guarantee.** Reported (Deadline 2019-08-07): "there was no commitment from Larry Ellison in the final documents"; banks expected him to step in; he pushed hard terms; lenders settled at about 82 cents on the dollar on more than $200M (Variety via Moviefone 2019-08-27). All press. No filing exists (private company). Detail in section 1.
3. **The "Skydance 13D/A filed 2026-10-08, accession 0001193125-26-418066" is not an Ellison-family filing.** It is Amendment No. 4 to the Schedule 13D on **Anghami Inc.** (subject CIK 1871983), filed by Skydance Corporation, Warner Bros. Discovery and Dplay Entertainment Limited to report that Skydance now owns WBD's 7,417,345 Anghami shares (71.3%, incl. 1,342,624 warrants at $115). It names no Ellison trust or LLC. VERIFIED (https://www.sec.gov/Archives/edgar/data/1871983/000119312526418066/primary_doc.xml). The Ellison entity names come from the Skydance 10-K/A instead (section 10).
4. **The SpaceX stake reconciles.** The earlier "~0.15% = ~$2.7B" is consistent with the xAI exchange terms and the IPO price (section 4). It is an estimate derived from a Forbes figure, not a filed number.
5. **A 2026 liquidity tell exists, and so does a counter-signal.** WSJ (via Billionaires.Africa 2026-10-02): the 8.4-acre North Palm Beach estate was **relisted at $165M** (bought 2021 at $80M; listed $145M in 2022, unsold). Same article: in 2026 he **bought** a 2.15-acre parcel next to his Manalapan compound for about $34.4M. Also: San Francisco Pacific Heights house sold off-market for $45M (closed 2025-12-12). REPORTED.

---

## 1. Annapurna Pictures (Megan Ellison) - the precedent case

**Documented (primary) vs reported (press), kept separate.**

| Item | Fact | Date | Source | Token |
|---|---|---|---|---|
| Credit facility | $350M revolving credit facility arranged by a syndicate led by J.P. Morgan (administrative agent) and Comerica; funding lineup reported as City National, First Republic, HSBC, MUFG Union, SunTrust, Wells Fargo | closed fall 2017 | Deadline via Yahoo https://www.yahoo.com/entertainment/annapurna-bailout-larry-ellison-likely-205057723.html ; Screen Daily https://www.screendaily.com/news/megan-ellison-responds-to-reports-of-annapurna-financial-woes-update/5141807.article ; trade note https://abladvisor.com/news/12557/indie-film-company-nabs-350mm-from-lending-syndicate-led-by-j-p-morgan | REPORTED (private; no SEC or Companies House filing exists) |
| Prior family capital | Megan and Larry made an initial investment of "more than $200 million"; Larry "reluctant to invest further" | 2018-10-09 | TheWrap https://www.thewrap.com/welcome/2702210/single/~annapurna-upheaval-megan-ellison-reevaluating-film-division~/ | REPORTED (unnamed sources; Annapurna called it "unfounded rumors") |
| Default | Facility mostly drawn; company "defaulted or about to default"; lenders set a deadline that week; Chapter 11 preparations (Delaware or California) | 2019-08-07 | Deadline via Yahoo (above); IndieWire via Yahoo https://www.yahoo.com/entertainment/annapurna-faces-bankruptcy-bailout-larry-211727391.html | REPORTED |
| Larry's role going in | "no commitment from Larry Ellison in the final documents"; bankers "betrayed" because marketing materials had portrayed family-office involvement; banks "expected him to step in"; he was negotiating to buy the debt at about 80 cents, possibly funded off his own credit lines (JPMorgan and Wells Fargo, both lenders on the facility, reportedly extended him $1B lines) | 2019-08-07 | Deadline via Yahoo | REPORTED, single origin; the $1B lines are an unverified aside |
| Bankruptcy alternative | A Chapter 11 would likely return 50-60 cents on the dollar to senior lenders, so a deal was "more attractive" | 2019-08-07 | Deadline via Yahoo | REPORTED |
| Resolution | Ellison made a "last and final offer" at 80-85 cents; participants in the revolver to receive "roughly $0.82 on the dollar" on "more than $200 million" resolved; Annapurna to seek no new credit line and instead finance case by case or be "wholly financed by Ellison herself" | 2019-08-27 | Deadline 2019-08 (402-blocked; headline and snippet read via search); Variety figure via Moviefone https://www.moviefone.com/news/annapurna-resolves-debt-problems-to-live-another-day/ | REPORTED; who funded the payoff (Larry, the family office or Annapurna) is NOT stated in any source I reached |
| Implied cost | 82% x ">$200M" is at least about $164M paid; lenders absorbed at least about $36M | - | arithmetic on the reported figures | INFERRED |
| After | 2020-04 Annapurna executive cuts incl. CFO James Pong (Deadline URL seen in search only); 2024-09-12 entire Annapurna Interactive staff resigned after a failed spin-off negotiation with Megan (Bloomberg https://bnnbloomberg.ca/business/company-news/2024/09/12/annapurna-video-game-team-resigns-leaving-partners-scrambling); **2026-08-26 Annapurna Pictures laid off about 30 staff**, "shifting market conditions"; 2026 slate is two co-productions; no new series since 2024 (TheWrap https://www.thewrap.com/creative-content/movies/annapurna-layoffs-30-staffers/ - article does not say who finances the company) | 2020-2026 | as listed | REPORTED |
| Skydance tie | **None found.** Skydance Corp FY2025 10-K (filed 2026-02-25): zero occurrences of "Annapurna" (text grep of the full 10-K). Megan is described in press as David's sister only | 2026-10-23 | https://www.sec.gov/Archives/edgar/data/2041610/000204161026000011/psky-20251231.htm | VERIFIED absence in that filing; relationship otherwise SEARCH-NOT-FOUND |

**Read:** Larry did not guarantee and did not write a par rescue. He treated the lenders as counterparties, used the default as leverage, and settled at a 17-20% discount, with the bank syndicate (his own relationship banks) taking the loss. The scale was about $0.2B, small against his Oracle stake even then (net worth in 2019 not re-sourced this session), so it was not a capacity test. The lesson for the present case is about behaviour (negotiate, do not backstop at par, no guarantee in documents), not about capacity. Two caveats that survive: every fact above is press; and the company has needed support again in 2024-26 (layoffs, Interactive walkout), with the funding source undisclosed.

---

## 2. MASTER TABLE

Legend: Liq = S (saleable, liquid market) / P (pledgeable) / PL (already pledged, reported) / I (illiquid). $ in USD, GBP in sterling. "src" = source class: SEC = SEC filing; CH = UK Companies House; PR = press; CO = company statement.

| # | Entity | Who holds | Public / private | Own % | Known debt | Known cash commitments / capital calls (dates) | Liq | Distress or support signals 2019-2026 | Src / token |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Oracle (ORCL)** | Larry (beneficial, incl. trust) | Public | 1,158,375,174 sh = 38.2% (DEF 14A 2026-09-25) | 413M sh pledged for "personal term loans only used to fund outside personal business ventures" (35.7% of his holdings); loan size, LTV, lenders not disclosed | None to Oracle. Dividend inflow about $2.32B/yr gross at $0.50/qtr x 1.158B (computed; payable 10/23) | Unpledged 745.4M sh = $93.6B at $125.54 (computed); S but control block and signalling; PL 413M = $51.9B | Pledges: 305M (2019), 317M (2020-21), 307M (2022-23), 277M (2024), 346M (2025), **413M (2026)**. Last open-market sale 2024-07-15/16: 2,250,000 sh at about $142.5-146.3 = about $322M (Form 4 0001127602-24-020602, option exercise and sale); 10b5-1 plan for 50M sh adopted 6/22/2026, **cancelled 9/12/2026, nothing sold** | SEC VERIFIED |
| 2 | **Skydance Corp (SKYD; ex-Paramount Skydance)** | Lawrence J. Ellison Revocable Trust u/a/d 1/22/88 (subscriber, with Larry personal guarantor); Pinnacle Media Ventures I-III LLC, Sayonara LLC, Skydance Entertainment Group LLC, Harbor Lights Entertainment Inc (David-managed, Ellison-family-controlled) | Public (NYSE) | Pre-WBD: David Ellison reported 600,717,731 Class B (48.63%) incl. 155M warrants at $30.50; ex-warrants 445,717,731 sh (about $3.5B at $7.79); Harbor Lights holds 100% of Class A (31,500,087); family about 77.5% of Class A indirectly. Post-WBD: family cheque about $17B for about 1.4B sh (Bloomberg est.) | Company debt about $30.0B first-lien + $11.4B + EUR 885M second-lien (8-K 2026-10-06) is company-level; Larry's exposure = guarantee ($45.72B equity piece, 8-K 2026-03-02) and pledges of SKYD stock to Citi/JPM (WSJ) | Equity funding closed 10/6/2026 at $12.00 (PIPE $47.01B). Contingent: ticking fee, termination amounts under the guarantee | S in principle (affiliate; registered?) but PL in part (WSJ) | SKYD $7.79 vs $12.00 = -35%; low $6.80 10/19; -23.8% one day 10/14 (D). Larry is landlord to the company: leases with an entity "owned and controlled by Lawrence Ellison", liability $174M, lease cost $20M for 8/7-12/31/2025 (10-K FY25) = support flowing TO Larry | SEC VERIFIED (shares, debt); family cheque and pledges PR |
| 3 | **Ellison Institute of Technology, Oxford Limited (EIT)** (Co. 13773507) and parent **EIT Oxford Holdings, LLC** (101 Ygnacio Valley Rd, Ste 320, Walnut Creek, CA); earlier US entity Ellison Institute, LLC (California) | Larry (PSC, with Paul Marinelli: "75% or more of shares and voting rights, control over trustees of a trust"; PSC notified 2021-11-30) | **Private limited company by shares (for-profit; not a charity - no Charity Commission registration found)** | 100% via parent | **No borrowing and no registered charges** in Companies House filing history; creditors GBP 66.2M are trade (GBP 52.5M) and accruals | **Contractual: GBP 1,244M construction commitments + GBP 127.3M collaboration agreements at 12/31/2025 (2024: GBP 1,137M), operating leases GBP 40.3M; post-year-end GBP 15.6M further collaboration capex.** Cash in: GBP 810M of shares in 2026 (3/11, 9/24, 9/25); GBP 725M of shares + GBP 91.2M contributions in 2025 | I (equity in a loss-making UK company; assets: tangible GBP 913.4M, of which land and buildings GBP 226.3M) | Loss GBP 120.5M (2025), GBP 25.8M (2024); staff 220 (45). Accounts say the parent "has confirmed that on-going funding will continue" (going-concern basis). Director churn: John Bell left 2025-09-16; Santa Ono (global president) left board 2026-09-02; McVean and Kelly appointed 9/14/2026. Press: scaled back Nov 2025 (FT via Cherwell); "only GBP 2bn committed so far"; opening 2027. Carved out of the WBD guarantee covenants | CH VERIFIED; press REPORTED |
| 4 | **Pulama Lanai / Lanai Resorts LLC; Sensei Lanai (wellness resort); Sensei Ag; two Four Seasons resorts** | Larry (reported) | Private | About 98% of the island, bought 2012 for about $300M (reported) | Not disclosed; no loan or lien found | Reported $75M upgrade of the hotels; privately funded 76-unit Hokuao housing (undisclosed cost; 2022); fuel subsidy; 4/15/2026 Land Use Commission petition A26-812 to reclassify about 170 acres (up to 9 villas, 5 spa units); total invested since 2012 NOT disclosed | I | 2025-09-25 closed rock/concrete unit (15 of 400 jobs; "not about cost savings"); cancelled 150-unit affordable project (press); **Hurricane Lowell damaged Kaumalapau Harbor, 9/2026** (editorial, no dollar figure). No sale, loan or pledge found | PR REPORTED; filing-level SEARCH-NOT-FOUND |
| 5 | **SpaceX (SPCX)** (ex-X Holdings / xAI) | Larry (trust; reported) | Public since June 2026 (IPO $135, $1.77T, 555.6M sh) | About 0.15% (INFERRED; section 4) | Reported pledged to Citi/JPM about 9/25-10/1/2026 (WSJ) | None | S nominally, but 366-day lockup for early holders reported (to about June 2027); PL (WSJ) | Value about $2.7B at IPO price, about $2.9B at $144.75 (INFERRED). SPCX -9.14% on 10/22 | PR + INFERRED |
| 6 | **Tesla (TSLA)** | Lawrence J. Ellison Revocable Trust | Public | Last Form 4: 3,001,250 sh on 2020-02-14 (pre-splits); x15 for the 5:1 (2020) and 3:1 (2022) splits = 45,018,750 sh, about $16.9B at $374.58 IF fully retained | Reported pledge to Citi: 3M cut to 1.5M sh (WSJ; unit pre/post split not stated) | None | S; partly PL | Director 2019-2022; no filing since. Current holding: SEARCH-NOT-FOUND (no Form 4 after directorship; Tesla's 10-K, 10-Q and proxies do not name him per reader K) | SEC VERIFIED to 2020; rest INFERRED |
| 7 | **TikTok USDS Joint Venture LLC** | **Oracle Corporation (corporate asset, not Larry)** | Private JV | Oracle 15%, equity method (FY26 10-K) | None disclosed | Oracle's contribution in dollars NOT itemised: non-marketable investments total $2.3B at 5/31/2026 ($2.1B at 5/31/2025), "substantial majority" with the JV; press says about $2.2B (10-Q Feb 2026) | n/a to Larry | Larry personal stake: SEARCH-NOT-FOUND. Governance (press): board seat; Adam Presser CEO | SEC VERIFIED (15%, $2.3B); rest PR |
| 8 | **Oracle Health (Cerner) breach** | Oracle liability | - | - | - | Texas AG portal 2026-10-02: 2,992,244 Texans; national about 19.93M (Bloomberg, citing the portal); consolidated class action W.D. Mo. (29 cases); motion to dismiss denied June 2026 (press); Oracle "declined to comment". Reserve / accrual: **SEARCH-NOT-FOUND** (FY26 10-K to 5/31/2026 has no Cerner breach disclosure; Q1 FY27 10-Q filed 9/11/2026 could not be retrieved as text, so UNKNOWN there). HHS OCR action: SEARCH-NOT-FOUND | n/a | Scale-only note | PR; SEC partly |
| 9 | **Annapurna Pictures / Annapurna Interactive** | Megan Ellison (founder, CEO); Larry's role undocumented | Private | Not disclosed | $350M facility (2017), settled 2019 at about 82c (section 1) | None known | I | 2019 default and settlement; 2024 Interactive walkout; **2026-08-26 layoffs (about 30)** | PR REPORTED |
| 10 | **Lawrence Investments, LLC** | Larry owns; President Paul Marinelli (since 2015; VP 2004-2015) | Private | 100% (per Skydance 10-K/A) | Not disclosed | n/a | n/a | The investment firm; Marinelli is also EIT Oxford director and PSC, and a Skydance director | SEC VERIFIED (10-K/A 2026-04) |
| 11 | **Delphi Asset Management Corporation (Reno, NV)** | Larry's management company (c/o on his Oracle and Tesla Form 4s) | Private | n/a | n/a | n/a | n/a | Address moved 5525 Kietzke Lane to 200 S. Virginia St, Ste 625 between 2024 and 2025 filings | SEC VERIFIED (address only) |
| 12 | **Palm Beach / Manalapan / Boynton Beach, FL** | Larry (via LLCs) | Private real estate | North Palm Beach 8.4 ac bought 2021 $80M; Manalapan compound bought 2022 $173M (+2.15 ac parcel 2026 $34.4M, 24+ acres); 8 Boynton Beach homes about $10M (2023, staff housing) | No mortgage found | None | I / S slowly | **North Palm Beach relisted $165M (WSJ ~2026-10-02)**; first listed $145M 2022-08, unsold. Counter-signal: still buying | PR REPORTED |
| 13 | **California / other real estate** | Larry | Private | SF Pacific Heights 2850 Broadway sold $45M (closed 2025-12-12; bought 1990 $3.9M); Woodside estate (primary; reported $200M renovation); Malibu: 11 properties assessed over $180M (Business Insider via Robb Report, date unspecified); Lake Tahoe | None found | None | I | SF sale is the only 2025-26 sale found; no Malibu or Woodside listing found | PR REPORTED |
| 14 | **Newport RI (Beechwood and Bellevue Ave); Kyoto (Nanzen-ji villa)** | Larry | Private | Beechwood bought 2010 for $10.5-16M (sources conflict); reported $152M renovation into a private art museum; Kyoto villa reported $86M | None found | Beechwood renovation reported as under way (undated spend) | I | none | PR REPORTED (aggregators; weak) |
| 15 | **Indian Wells Tennis Garden / BNP Paribas Open (Tennis Ventures LLC)** | Larry | Private | Bought 2009 for about $100M; reported $200M+ in rebuilds | None found | None | I | BNP Paribas title sponsor renewed through 2029; 2026 attendance record 504,268 | PR REPORTED |
| 16 | **Yachts, aircraft** | Larry | Private | - | - | - | I | **SEARCH-NOT-FOUND** (no 2025-26 listing, sale or mortgage found) | SEARCH-NOT-FOUND |
| 17 | **Philanthropy** | Larry / foundations | - | Giving Pledge 2010 (95%); Ellison Medical Foundation (1997; ~$430M to labs per one source, ~$1B per reader D; closed); USC $200M cancer institute (reported; date unverified); **EIT** per row 3 | - | Oxford: GBP 20M per year plus one-off GBP 30M scholarships (FT via Cherwell, 2025-11); GBP 100-130M Dec 2024 alliance (sources differ); GBP 118M AI-vaccine programme (press, undated); no Oracle-stock gifts seen on Form 4 2022-2026 | - | No dated instalment schedule found for the "$1B" EIT pledge. 990s: ProPublica search returned 0 organizations for "Lawrence J Ellison Foundation" and "Ellison Medical Foundation": SEARCH-NOT-FOUND | mixed |
| 18 | **SpaceX/xAI-adjacent: Elon Musk to Skydance ~$1B** | Musk (entity unspecified) | - | - | - | Reported by Semafor 2026-10-22; see reader K | - | Outside money, not a claim on Larry | PR (K) |
| 19 | **Laurene Powell Jobs / Emerson (Skydance holder)** | Form 3 and Form 4 filed 2026-10-08 for event date 2026-10-06 as a reporting person on Skydance Corp | - | Not read (document fetch failed) | - | - | - | Appears among Skydance equity syndicate holders; details UNKNOWN. Flag to K/D | SEC VERIFIED (existence of filings), contents UNKNOWN |

---

## 3. EIT in detail (item 2)

Source: Companies House company 13773507; accounts to 12/31/2025 filed 2026-09-28 (21 pages, small-company regime, audited, Blick Rothenberg Audit LLP, unqualified, signed 2026-08-04; the filed document is a scanned image, read page by page); SH01 forms; officers and PSC pages. https://find-and-update.company-information.service.gov.uk/company/13773507

| Item | Value | Token |
|---|---|---|
| Legal form | Private company limited by shares, England and Wales; incorporated 2021-11-30; renamed from "ellison oxford LIMITED" 2024-12-17; SIC 72190 research | VERIFIED |
| Charity status | Not a charity (no Charity Commission entry found; register search blocked 403, so SEARCH-NOT-FOUND, not VERIFIED) | SEARCH-NOT-FOUND |
| Control | Immediate parent EIT Oxford Holdings, LLC (101 Ygnacio Valley Rd Ste 320, Walnut Creek CA). PSCs: Lawrence Joseph Ellison and Paul Timothy Marinelli | VERIFIED |
| Equity paid in (share premium + capital contribution reserve) | Through 12/31/2025: GBP 516.1M + GBP 725.0M + GBP 300.0M = **GBP 1,541M**. 2026 so far: **+GBP 810M** shares (59 on 3/11 GBP 295M; 70 on 9/24 GBP 350M; 33 on 9/25 GBP 165M, each "for cash" at GBP 5,000,000 per share). Floor total through 10/12/2026: **GBP 2,351M** (2026 capital contributions, if any, unknown). At an assumed $1.30-1.35/GBP that is about $3.1-3.2B (INFERRED, FX not verified) | VERIFIED (GBP); USD INFERRED |
| Balance sheet 12/31/2025 | Net assets GBP 1,390.8M (2024: 695.0M); fixed assets GBP 1,155.0M (tangible 913.4M; investments in subsidiaries 229.2M; intangibles 12.4M); cash GBP 71.5M; debtors GBP 229.8M (group undertakings GBP 52.4M unsecured, interest-free, repayable on demand; prepayments GBP 110.3M); creditors GBP 66.2M | VERIFIED |
| P&L | Loss GBP 120.5M (2025), GBP 25.8M (2024) | VERIFIED |
| Commitments | GBP 1,244M construction; GBP 127.3M collaboration agreements; GBP 40.3M operating leases (GBP 8.6M within a year) | VERIFIED |
| Going concern wording | "The parent undertaking has confirmed to the directors that the on-going funding will continue for both operating costs and capital expenditure" | VERIFIED |
| Subsidiaries | Generative Biology Limited (asset-holding), Ellison SPV 2 Limited (property), SPV 3-6 (dormant) | VERIFIED |
| Construction status | Press: Littlemore House topped out Feb 2026; first Daubeny building topped out Apr 2025; 3 Foster + Partners buildings; Oct 2025 expansion plan to 2M sq ft, up to 7,000 staff; "in use in 2027" (EIT press office via Cherwell 2026-03) | REPORTED |
| Headline pledges | GBP 1B initial plus GBP 890M added Oct 2025 (Times Higher Education); original "GBP 10B over a decade" now questioned (FT via Cherwell 2025-11: "only GBP 2 billion committed so far") | REPORTED |
| Stock gifts or cash? | **Cash.** The accounts show cash share subscriptions and capital contributions from the parent, not shares of Oracle. Whether the parent was funded from dividends, loans against the pledged shares or other sources is not disclosed: UNKNOWN. Observable: Larry made no open-market Oracle sale after 2024-07 (about $322M then), yet GBP 725M (2024), GBP 816M (2025) and GBP 810M (2026 YTD) went in | VERIFIED (form of funding); source of cash UNKNOWN |
| Why carved out of the covenants | Not stated in anything I read. 8-K 2026-03-02 (read by reader D, not re-read by me) excludes Oracle and EIT from what Ellison must cause. INFERRED purpose: lets him keep funding a GBP 1.37B contractual build-out without covenant limits | INFERRED |

---

## 4. SpaceX and Tesla reconciliation (item 4)

| Step | Figure | Source | Token |
|---|---|---|---|
| Twitter take-private equity | $1B from the Lawrence J. Ellison Revocable Trust (2022) | Musk 13D/A per reader K | VERIFIED (K) |
| X Holdings to xAI (2025-03-28) to SpaceX (2026-02-02) | Share exchanges, no cash | K | VERIFIED (K) |
| xAI stake after the Jan 2026 round at $250B | "about 0.8% of xAI, worth about $2.1B" (Forbes, early 2026) | https://www.forbes.com.au/news/billionaires/elon-musk-nears-800-billion-net-worth-after-latest-funding-round/ | REPORTED, estimate |
| Exchange terms | 0.1433 SpaceX shares per xAI share; SpaceX valued $1T, xAI $250B, combined $1.25T, so xAI holders own 20% | WSJ via press, e.g. https://www.fool.com/investing/2026/02/22/what-you-need-to-know-about-the-spacex-xai-merger/ | REPORTED (consistent across sources) |
| Pre-IPO stake | 0.8% x 20% = **0.16%** of SpaceX | arithmetic | INFERRED |
| IPO | Priced $135, valued $1.77T, 555.6M new shares ($75B), Nasdaq SPCX, 366-day lockup for founder and early holders | https://www.barchart.com/story/news/2306340/spacex-prices-ipo-at-135-per-share ; Benzinga | REPORTED |
| Post-IPO stake | 0.16% x (1 - 555.6M/13.11B) = about **0.153%** | arithmetic | INFERRED |
| Value | 0.153% x $1.77T = **$2.7B at the IPO price**; about **$2.9B at $144.75** (mcap about $1.90T) | arithmetic | INFERRED |

So the reported "~0.15% = ~$2.7B" is the IPO-price value of an xAI-derived stake. The input (0.8%) is a Forbes estimate; no SEC filing names Ellison as a SpaceX holder (SpaceX S-1/A and 10-Q have zero mentions, per reader K), so the precision is about +/-20%. The 366-day lockup (about June 2027) is reported for founder and early holders; whether it covers him, and whether a bona fide pledge was permitted, is UNKNOWN.

**Tesla:** the only primary data are the Form 3 (3,000,000 sh, 2018-12-27) and a Form 4 (2020-02-14: bought 1,250 sh at $767 in the offering, total 3,001,250 sh, indirect via the trust). Splits since: 5-for-1 (Aug 2020) and 3-for-1 (Aug 2022) = x15, i.e. 45.0M sh if untouched. The WSJ-reported "3M reduced to 1.5M" collateral shares may be unadjusted (would be 45M to 22.5M adjusted) or adjusted (about $1.1B to $0.56B): unit unknown. Current holding: SEARCH-NOT-FOUND.

---

## 5. TikTok USDS JV (item 5)

- Oracle FY2026 10-K (filed 2026-06-22, accession 0001193125-26-277521): "The substantial majority of the non-marketable investments we held as of May 31, 2026 were with TikTok USDS Joint Venture LLC, an equity method investee in which we have an ownership interest of 15%." Non-marketable debt investments and equity securities "totaled $2.3 billion and $2.1 billion as of May 31, 2026 and 2025." The same 10-K shows a $2.7B gain on selling Ampere in FY26, so the $2.3B is mostly the JV after Ampere left. VERIFIED. Carrying value of the JV stake is therefore below $2.3B; the dollar contribution is not separately stated: SEARCH-NOT-FOUND. Press repeats about $2.2B from the Feb-2026 10-Q (Outlook Business). An Ellison personal stake: SEARCH-NOT-FOUND. Governance strings (board seat; CEO Adam Presser) are press only.

## 6. Oracle Health / Cerner (item 6)

See master row 8. For scale: a liability inside Oracle (Oracle FY26 cash used for capex $55.7B, 10-K). No reserve found.

## 7. Philanthropy (item 7)

See row 17. Primary-source gap: the foundations' Forms 990 were not reachable (ProPublica returned zero matches). Form 4 pattern: Ellison's Oracle Form 4s in the EDGAR list 2022-2026 are option exercises, option grants, and the 2024-07 sales; no gift (code G) transaction was seen in the six I read (2022-06, 2023-06, 2024-06, 2024-07, 2025-10 plus the list). A "Harvard $800M pledge" surfaced in search is a 2006 FT story (pledge March 2005, late 2006), not current: ignore.

## 8. Real estate and toys (item 8)

See rows 12-16. Carrying values are press purchase prices, not marks; the only 2025-26 transactions found: sale SF $45M (12/12/2025), relist N. Palm Beach $165M (~10/2/2026), purchase Manalapan parcel about $34.4M (2026). No mortgage or lien on any property was reported anywhere I reached; county records not searched.

## 9. David's other vehicles (item 9)

- The pre-deal Skydance Media entities (Skydance Entertainment Group LLC, Pinnacle Media Ventures I-III, Sayonara) now hold SKYD stock (section 2 row 2). Skydance Sports, Animation and Games: the FY25 10-K has zero hits for those names; they were operating units merged into the public company, so obligations sit in Skydance Corp, not in Larry's personal balance sheet (INFERRED). Tencent and KKR: **zero mentions in the 10-K (VERIFIED grep) and the 10-K/A beneficial-ownership table**; press says Tencent bought a minority stake in 2018, RedBird and CJ ENM in 2020. Whether they sold out before 2025: SEARCH-NOT-FOUND. RedBird: Form 4 (Cardinale, 2026-10-06) shows RB Tentpole LP bought 175,000,000 sh and RB Tentpole Holdings II LP 158,333,333 sh at $12.00 = **$4.0B**, confirming the reported RedBird cheque. VERIFIED (https://www.sec.gov/Archives/edgar/data/2041610/000089534526000454/form4.xml).
- David's personal borrowing: SEARCH-NOT-FOUND.
- Related-party flows from Skydance Corp to Ellison companies (VERIFIED, 10-K FY25): $12M paid to Oracle for SaaS (8/7-12/31/2025); six-year, $300M Oracle cloud infrastructure commitment signed Feb 2026; leases from a Larry-owned lessor, $174M liability at 12/31/2025.

## 10. Family office and holding vehicles (item 10)

| Vehicle | Role | Evidence | Token |
|---|---|---|---|
| The Lawrence J. Ellison Revocable Trust u/a/d 1/22/88 | Filer of record; subscriber of the Class B (about $43.9B at $16.02, plus contingent amounts; later assigned in part); holder of Tesla; reported SpaceX holder; Larry is settlor and co-trustee | Skydance 10-K/A (accession 0001140361-26-016758, filed 2026-04) Related-party section | VERIFIED |
| Lawrence Investments, LLC | "an investment firm owned by Lawrence J. Ellison" (President Paul Marinelli) | same 10-K/A, director bio | VERIFIED |
| Delphi Asset Management Corporation, Reno NV | c/o address on Larry's Form 4s | Form 4s 2022-2025 | VERIFIED (address) |
| Pinnacle Media Ventures LLC / II / III; Sayonara LLC; Skydance Entertainment Group LLC | Hold 413.7M Class B (ex-warrants) plus 155M warrants; managed by David; address 101 Ygnacio Valley Rd Ste 320, Walnut Creek CA | 10-K/A beneficial-ownership table, footnote 2 | VERIFIED |
| Harbor Lights Entertainment, Inc. (846 University Ave, Norwood MA) and two subsidiaries | 31,500,087 Class A (100%) + 32,012,190 Class B; formerly National Amusements | 10-K/A footnote 1 | VERIFIED |
| EIT Oxford Holdings, LLC | Parent of EIT Oxford Ltd; same Walnut Creek suite | Companies House accounts note 18 | VERIFIED |
| RB Maverick LLC, RB Tentpole LP I-III | RedBird side (not family) | Form 4 | VERIFIED |

**Pattern:** the Walnut Creek, CA suite (101 Ygnacio Valley Rd, Suite 320) is the common address of the Pinnacle entities, Sayonara, Skydance Entertainment Group and EIT Oxford Holdings: one operating office for the family's private holdings (INFERRED from the shared address; no filing calls it "the family office"). Lien-filing debtor names (California UCC) were not reachable; the WSJ lien article itself was not read.

---

## 11. Dated claims and signals timeline (2019-2026)

| Date | Event | Token |
|---|---|---|
| 2019-08-07 to 08-27 | Annapurna default; no Larry commitment in documents; settlement about 82c on more than $200M | REPORTED |
| 2022-08 | N. Palm Beach listed $145M (unsold) | REPORTED |
| 2024-07-15/16 | Last open-market Oracle sale, 2.25M sh, about $322M | VERIFIED |
| 2024 (full year) | EIT: GBP 724.9M equity paid in | VERIFIED |
| 2025 (full year) | EIT: GBP 816.2M paid in; Oracle pledges 346M (9/19/2025) | VERIFIED |
| 2025-09-16 | John Bell leaves EIT Oxford board | VERIFIED |
| 2025-12-12 | SF house sold $45M off-market | REPORTED |
| 2026-03-02 | $45.72B equity guarantee (8-K) | VERIFIED (D) |
| 2026-03-11 | EIT: GBP 295M share issue | VERIFIED |
| 2026-06-22 / 09-12 | 10b5-1 sale plan adopted / cancelled, nothing sold | VERIFIED (D) |
| 2026-08-26 | Annapurna lays off about 30 | REPORTED |
| 2026-09-02 | Santa Ono leaves EIT Oxford board | VERIFIED |
| 2026-09-24 / 09-25 | EIT: GBP 350M + GBP 165M cash share issues | VERIFIED |
| 2026-09-25 | Proxy: 413M pledged; about 9/25-10/1 Citi/JPM add SpaceX and Skydance stock (WSJ) | VERIFIED / REPORTED |
| 2026-10-02 | N. Palm Beach relisted $165M | REPORTED |
| 2026-10-06 | Skydance/WBD closes; RedBird pays $4.0B | VERIFIED |

## 12. What I could not reach

- WSJ lien article and California UCC filings (debtor entity names, loan sizes): not reached.
- Oracle Q1 FY27 10-Q (filed 2026-09-11) as text: three fetches returned errors, so the Cerner reserve and any Oracle-Ellison related-party notes there are UNKNOWN.
- Charity Commission register (403) and the foundations' 990s; Hawaii state business records; county mortgage records; the Skydance Form 4 of Laurene Powell Jobs (fetch 404).
- Annapurna: who paid the 2019 payoff; any 2023-26 financing source.
- Sensei / Lanai capital invested since 2012 and any island debt.
- Whether the EIT parent's cash came from loans on pledged stock.

---

## SUMMARY FOR PROME

1. **Annapurna precedent (all press, no filing exists):** Annapurna defaulted on a $350M JPMorgan/Comerica-led revolver in Aug 2019 with "no commitment from Larry Ellison in the final documents"; he negotiated a discounted buyout and lenders took about 82 cents on more than $200M (Deadline 8/7 and Variety 8/27/2019). So the documented behaviour is a haircut settlement with no guarantee, not a par backstop; who funded the payoff is not stated anywhere I reached. Annapurna laid off about 30 staff on 2026-08-26; no Skydance tie found.
2. **Three largest dated cash claims on Larry outside Skydance:** (a) EIT Oxford contractual commitments GBP 1,244M construction + GBP 127M collaboration = GBP 1.37B at 12/31/2025 (Companies House accounts, VERIFIED; roughly $1.8B at an assumed $1.32/GBP, INFERRED), parent says funding "will continue"; (b) EIT cash share issues already wired in 2026: GBP 295M (3/11), GBP 350M (9/24), GBP 165M (9/25) = GBP 810M (VERIFIED, SH01 forms); (c) EIT operating burn: loss GBP 120.5M in 2025 plus Oxford GBP 20M a year (press). Pledged-loan principal and interest is the biggest claim and is UNKNOWN. Other items (Beechwood $152M renovation, Lanai villas, Manalapan parcel $34.4M) are press, undated.
3. **Saleable / pledged / illiquid:** ORCL 1,158M sh: 413M pledged ($51.9B at $125.54), 745M unpledged ($93.6B, computed) but selling is signalled off the table (10b5-1 plan cancelled 9/12). Last open-market sale 7/2024, about $322M. SpaceX about 0.15% (about $2.7-2.9B, INFERRED, reported pledged, 366-day lockup reported). Tesla up to 45M sh split-adjusted (about $16.9B if untouched, current holding SEARCH-NOT-FOUND; part pledged per WSJ). SKYD about 1.8B sh family-wide at $7.79 (INFERRED). Illiquid: EIT, Lanai, real estate, Indian Wells. TikTok and Cerner sit inside Oracle, not Larry.
4. **Liquidity tells 2025-26:** SF house sold $45M (12/12/2025); North Palm Beach relisted at $165M (~10/2/2026, WSJ); EIT director churn (Ono left 9/2/2026); Annapurna layoffs. Counter-signal: bought a $34.4M Manalapan parcel in 2026.
5. **Correction to the brief:** accession 0001193125-26-418066 is Skydance's 13D/A on Anghami Inc., not an Ellison-family filing. Entity names come from the Skydance 10-K/A: Lawrence J. Ellison Revocable Trust, Lawrence Investments LLC (President Paul Marinelli, also EIT director and Skydance director), Pinnacle Media Ventures I-III, Sayonara LLC, Skydance Entertainment Group LLC, Harbor Lights Entertainment; common Walnut Creek address with EIT Oxford Holdings LLC.
6. **SpaceX 0.15% reconciles:** 0.8% of xAI (Forbes) x 20% (0.1433 exchange, $250B/$1.25T) x IPO dilution = 0.153%; $2.7B at the $1.77T IPO value.
7. **Not reached:** WSJ lien article and UCC debtor names and loan sizes; Oracle Q1 FY27 10-Q text (Cerner reserve UNKNOWN; FY26 10-K has none); foundations' 990s; Charity Commission; Lanai capital invested and debt; source of the EIT parent's cash; Laurene Powell Jobs's Skydance Form 3/4 contents (a filing exists, contents UNKNOWN).
