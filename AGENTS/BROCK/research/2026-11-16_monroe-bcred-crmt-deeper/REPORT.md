# Monroe, BCRED and Car-Mart: deeper read (prome-6f, on Will's 11:05 ET word)

**Written:** 2026-11-16, session 11:07 to about 11:45 ET, desktop, Claude Code (Opus 5.5). BROCK, research only.
**Scope:** PROME's assignment items A1 to A4, B5 to B7, C. Moves no gate, level, band, score, card or charter. **D:L1139, D:L1099 and D:L1071 are NOT graded here**; they stay dated Tue 11/17.
**Labels:** VERIFIED = read this session in the primary filing at sec.gov (accession given). INFERRED = BROCK reasoning or arithmetic on verified figures. UNKNOWN = not found or not read.
**Tools:** EDGAR `data.sec.gov` submissions JSON and the Archives worked (slow; retried). The `browse-edgar` Atom feed failed three times this session, so the Car-Mart read rests on one endpoint (the submissions JSON), read twice. `fetch.py` returned an error for CRMT once, then a price; Nasdaq's real-time quote agreed. Quartr not called (standing rule). No paid source, no PACER.

---

## A. Redemption pressure at Monroe Capital Income Plus and BCRED

### A1. Monroe's Q4 offer: the dates and size, now read

| Item | Figure | Label | Source |
|---|---|---|---|
| Expiry | **11:59 pm ET, Mon 2026-11-30**, "unless the Offer is extended" | VERIFIED | Offer to Purchase, Ex-99(a)(1)(B) to SC TO-I 0001104659-26-119625 (filed 2026-10-28) |
| Size | up to **13,493,156 shares**, "approximately 5.0%" of shares outstanding at 9/30/26 (about 269.9M shares, INFERRED from 5%) | VERIFIED | same |
| Dollar size | **$130,883,613.20** transaction value = 13,493,156 x **$9.70** (9/30/26 NAV per share), for the filing fee only | VERIFIED | filing-fee exhibit to the same SC TO-I |
| Price paid | the price of shares sold at the fund's most recent private-offering closing before expiry, "expected to occur on or about November 2, 2026" | VERIFIED | Offer to Purchase |
| Who can tender | only shares bought **before 10/28/2025**; later shares are under a one-year lock-up and are ineligible | VERIFIED | Offer to Purchase |
| Proration | if oversubscribed, the fund may take up to 2% more under Rule 13e-4(f)(1)(ii), or prorate | VERIFIED | Offer to Purchase |
| Where the Q4 final appears | a **final SC TO-I/A** on Monroe's EDGAR feed (CIK 0001742313). The last four were filed +6, +7, +7 and +4 days after expiry (Q4-25: expired 12/17, filed 12/23; Q1: 2/27 to 3/6; Q2: 5/29 to 6/5; Q3: 8/31 to 9/4) | dates VERIFIED; the forecast is INFERRED | submissions JSON, read 11:13 ET |
| Expected Q4 final | **Fri 12/04 to Mon 12/07**, inside the GATE-BRK-R2 12/07 review. Key the read to the feed, not the date | INFERRED | from the row above |

**Correction to my register:** the modelled "~11/30" was the **expiry**, not the final. The final follows about 4 to 7 days later. The STATUS matrix row reading "Monroe Q4 final ~11/30 INFERRED" is wrong on that basis; I will correct it at closeout.

### A2. By quarter: requested, accepted, satisfaction, net assets

**Monroe Capital Income Plus (CIK 0001742313)**

| Quarter (expiry) | Shares tendered | Shares accepted | Satisfied | Price | $ requested (INFERRED, shares x price) | $ accepted | $ unmet (INFERRED) | Net assets, quarter-end | Unmet as % of net assets (INFERRED) | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Q4-25 (12/17/25) | 6,664,444 | all | **100%** | $9.98 | $66.5M | $66.5M | $0 | $2,830.6M (12/31/25) | 0 | SC TO-I/A 0001742313-25-000088 |
| Q1-26 (2/27/26) | 15,179,052 | all | **100%** | $9.87 | $149.8M | $149.8M | $0 | $2,783.4M (3/31) | 0 | SC TO-I/A 0001742313-26-000018 |
| Q2-26 (5/29/26) | 25,287,143 | 14,229,101 | **56.3%** (issuer-stated) | $9.77 | $247.1M | $139.0M | **$108.0M** | $2,709.7M (6/30) | **4.0%** | SC TO-I/A 0001742313-26-000030 |
| Q3-26 (8/31/26) | 17,848,959 | 13,872,183 | **77.7%** (issuer-stated) | $9.77 | $174.4M | $135.5M | **$38.9M** | $2,617.0M (9/30) | **1.5%** | SC TO-I/A 0001742313-26-000055 |

Net assets: XBRL `AssetsNet` from the 10-K and the 10-Qs 0001742313-26-000026, -046 and -066. Monroe fell 7.5% from 12/31/25 to 9/30/26.

⚠️ **New this session, a correction:** Q2's rate **is** disclosed: 56.3%, in the Q2 final SC TO-I/A. My register said "RATE NOT DISCLOSED" because I read it from the 10-Q footnote. The gate is unaffected: (a)'s run was already counted from the issuer's pro rata statement, and (b) cannot use it (56.3 is above 25, and the 5/29 pricing date is before the 9/3 start of grading). Small mismatch: the Q1 final says 15,179,052 shares and $149.8M; the Q3 10-Q table says 15,199,220 shares and $150.0M. I have not reconciled it; it does not affect the 100% reading.

**BCRED, Blackstone Private Credit Fund (CIK 0001803498)**

| Quarter (expiry) | Shares tendered | Shares accepted | Satisfied | NAV per share (INFERRED, $ ÷ shares) | $ requested (INFERRED) | $ accepted | $ unmet (INFERRED) | Net assets, quarter-end | Unmet as % of net assets (INFERRED) | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Q4-25 (12/2/25) | 85,035,789 | all | **100%** | $24.79 | $2,108M | $2,108M | $0 | $47,612M (12/31/25) | 0 | SC TO-I/A 0001213900-26-010557 |
| Q1-26 (3/2/26) | 133,689,552 | all (cap raised to 7%, per my register) | **100%** | $24.19 | $3,234M | $3,234M | $0 | $45,035M (3/31) | 0 | SC TO-I/A 0001213900-26-050688 |
| Q2-26 (5/29/26) | 191,782,834 | 93,100,272 (5% of 3/31 shares) | **48.5%** (INFERRED from issuer counts) | $23.65 | $4,536M | $2,202M | **$2,334M** | $42,776M (6/30) | **5.5%** | SC TO-I/A 0001213900-26-084924 |
| Q3-26 (8/31/26) | 181,287,647 | 90,421,325 | **49.9%** | $23.51 | $4,262M | $2,126M | **$2,136M** | $41,130M (9/30) | **5.2%** | SC TO-I/A 0001213900-26-114678 |

BCRED's net assets fell 13.6% from 12/31/25 to 9/30/26 (Q3 10-Q 0001803498-26-000063). Q2 and Q3 were paid in non-interest-bearing promissory notes, settled about four weeks after pricing (Q3 paid on or about 10/28; KB-BRK-431).

⚠️ **Unmet dollars do not add across quarters.** Blackstone's 11/3 letter says Q3 requests "largely reflected carryover from Q2'26" (8-K 0001803498-26-000059, Item 7.01). The $2.1B unmet in Q3 is mostly the same investors as the $2.3B unmet in Q2, not $4.5B of separate demand.

⚠️ **Different basis from the issuer:** the same letter says BCRED fulfilled "approximately 75% of requested capital within approximately 90 days" for Q2 and Q3 requesters. That counts an investor's resubmission across two windows. Per window, satisfaction was 48.5% and 49.9%. Same denominator trap as Apollo's "45%" (standing trap 2). Both figures are true, on different bases.

### A3. What a third sub-100% quarter would and would not mean

**What it does, mechanically (GATE-BRK-R2, Will-ruled 9/3/26, WQ-158; `PROME/GATES.tsv`):**
- Leg (a) fires for that fund: three consecutive quarters under 100%. Either fund would be the **third** to fire, after North Haven (9/25) and OCIC (10/2).
- The registered consequence is **"BROCK adjudication + packet to PROME (vehicle + leg); routes LIQUID (X1 wrapper half: evidence for re-adjudication, not a re-arm) + OTTO. Watch-only: NO capital path."** No position action follows by rule.
- My redemption-gates vector is already at its ceiling (5). The Q2 wave counts once, and the P13 latch is in force (Will, 10/31). A third fire **moves no score**.

**What it would not establish:**
- That either fund cannot pay. Both are holding a 5% quarterly cap they set themselves. The unmet requests are a small fraction of what they could borrow (table below).
- Credit losses or insolvency. Proration is a liquidity-terms event.
- Independent evidence. BCRED, Monroe, North Haven, OCIC and ADS all started prorating in H1-2026 (shared antecedent, register line 16), so a third fire is the same wave persisting, not a second wave.
- A "run". BCRED's requests fell (191.8M to 181.3M shares) and were mostly carryover. Monroe's fell harder (25.3M to 17.8M shares), and its satisfaction rose from 56.3% to 77.7%.

**What in the filings separates orderly proration from a liquidity squeeze (all 9/30/26):**

| Tell | Monroe | BCRED | Squeeze would look like |
|---|---|---|---|
| Cap | 5.0% held; Q4 offer filed on schedule 10/28 | 5% held; Q4 offer filed on schedule 11/2 | cap cut below 5%, a skipped quarter, or a suspension |
| Payment | cash, "promptly following expiration" | non-interest-bearing notes settled about 4 weeks after pricing | notes with longer terms, or payment delayed past the next quarter |
| Asset coverage (legal floor 150%) | **184%** (188% at 12/31/25) | **218.1%** (235.7% at 12/31/25) | falling toward 150%, or a covenant waiver |
| Leverage (debt ÷ net assets) | **1.19x** (1.27x at 6/30; INFERRED from $3,106.5M principal ÷ $2,617.0M) | **0.85x** issuer-stated (0.74x at 12/31/25, INFERRED) | rising because debt is drawn to pay redemptions |
| Undrawn credit | **$507.6M** unused across facilities | **$16.7B** available under the borrowing base ($17.3B unused) | undrawn below one quarter's unmet requests |
| Cash | **$23.8M** (down from $69.2M at 12/31/25) | $0.8B unrestricted ($1.7B including restricted) | — |
| Unfunded commitments | **$876.0M** of delayed-draw loans, revolvers and subscription agreements | **$9.16B** | commitments above cash plus undrawn credit |
| Covenants | "in compliance with all covenants" on every facility | Citi revolver: 150% asset coverage and a minimum equity; no waiver or breach in the passages read (not a full search) | a waiver, an amendment, or a borrowing-base deficiency |
| Money in vs out (9 months) | stock sold $180.1M; repurchases $424.6M; cash dividends $100.4M; operating cash +$416.4M (loans repaid or sold) | stock sold $2.09B; repurchases paid $7.54B; sales and repayments $12.8B | — |
| Credit | non-accrual 17 borrowers, $48.8M fair value, 0.9% of investments | non-accrual 2.7% at cost, 1.7% at fair value; average mark ~95; bottom 5% of private loans marked 54.0 | — |

Sources: Monroe 10-Q 0001742313-26-000066 (Note 7 Borrowings, commitments note, cash-flow statement, Note 14); BCRED 10-Q 0001803498-26-000063 (MD&A Liquidity, cash-flow statement, unfunded-commitments schedule) and 8-K 0001803498-26-000059.

**Reading (INFERRED):**
- **BCRED is orderly proration by every tell.** It has about 8 times its Q3 unmet requests available under its credit lines and chooses the 5% cap. Leverage is rising because equity is shrinking, not because it is borrowing to pay redemptions. The real cost is shrinkage: net assets are down 13.6% this year.
- **Monroe is orderly, but on thinner margins.** It shrank total assets by $417.5M in Q3 and paid debt down, funding redemptions from loan repayments. The tight line: cash plus undrawn credit ($531.5M) is less than its $876.0M in unfunded commitments. It needs repayments to keep coming in.
- **What to watch in Monroe's next filings:** a cut in the 5% cap, a facility amendment, asset coverage moving toward 150%, or new subscriptions drying up. Monthly sales were $8.1M on 10/1 and $8.3M on 11/2 (Note 14), against about $131M a quarter going out. Any of those would read as a squeeze. A third sub-100% quarter by itself would not.
- **The lock-up cuts both ways.** It shrinks Monroe's eligible pool now. As shares sold since 10/28/2025 come out of lock-up, more holders can tender.

### A4. The rest of the six-vehicle population

| Fund | (a) state | Can it fire in Q4? |
|---|---|---|
| MS North Haven Private Income Fund | FIRED 9/25 (47.8, 41.6, 43.7) | already fired; latched, so further quarters are recorded but are not new fires |
| OCIC, Blue Owl Credit Income | FIRED 10/2 (22.82, 26.6, 29.8) | already fired; latched |
| BCRED | run 2 | **yes**: a Q4 sub-100% letter, expected about 12/03 to 12/07 |
| Monroe Capital Income Plus | run 2 | **yes**: the Q4 final SC TO-I/A, expected about 12/04 to 12/07 |
| Apollo Debt Solutions (ADS) | run 1 (Q3 33.89%, from issuer counts) | **no**: Q4 would make 2; the earliest fire is the Q1-2027 result |
| CCLFX, Cliffwater Corporate Lending | 0, not measurable | **no**: an interval fund that does not disclose satisfaction |

**Large non-traded credit funds I already hold with a Q3 under 100%, NOT added to the population:**
- **Blue Owl Technology Income Corp (OTIC):** about 13% preliminary, requests 39.0% of shares (KB-BRK-316). It has its own gate, GATE-BRK-OTIC, which grades from Q4-2026.
- **Ares Strategic Income Fund (ASIF):** 38.2% (KB-BRK-304). Permanently excluded by Will's 9/17 ruling (WQ-219).
- **North Haven Private Income Fund A:** 73.1% (KB-BRK-410). Counted inside North Haven's cell.
- **Partners Group Global Value SICAV:** 5% limit exhausted, most requests deferred (KB-BRK-434). Not an SEC registrant.
- Secondary, unverified: Fitch says 9 of 15 perpetual non-traded BDCs had Q3 requests above 5% (KB-BRK-362).

---

## B. America's Car-Mart (CRMT) on the twelfth bridge's standstill date

### B5. EDGAR feed read, dated (a read, NOT the grade of D:L1139)

| Read | Result |
|---|---|
| `data.sec.gov` submissions JSON, CIK 0000799850, read **11:13 ET and 11:19 ET, 2026-11-16** | Newest filing is still the 8-K 0001171843-26-007415 (Item 1.01), accepted 2026-11-13 09:15:15 ET. **Nothing in any form after it.** No thirteenth bridge, waiver, sale agreement, RSA, Item 1.03, 2.04 or Nasdaq 3.01. |
| `browse-edgar` Atom feed | **UNAVAILABLE** this session: three attempts timed out. Single-endpoint read. |
| Press, standard web search, about 11:22 ET | nothing dated after 11/12 |
| Tape | **CRMT $1.03, +10.13%**, Nasdaq real-time, 11:20 ET, volume about 51,000 (bid $1.01, ask $1.06); fetch.py $1.03 +9.57%. **The cause is not established.** No filing explains it. |

Bridges 9 to 12 were filed the morning after the agreement (08:00 to 09:15 ET). A thirteenth bridge agreed today would most likely appear **Tue 11/17, 08:00 to 09:30 ET**, which is the existing D:L1139 wake.

### B6. What can follow a twelfth bridge

| Outcome | Filing that shows it | What it would mean |
|---|---|---|
| Thirteenth bridge | 8-K Item 1.01, a new end date; likely the next morning | the standstill continues; lenders keep a short leash; nothing is resolved |
| Waiver or third amendment (longer relief) | 8-K Item 1.01 with an Ex 10.1 amendment; may carry new money, a fee, sale-process deadlines | lenders commit to a longer runway; any deadlines tell you the endgame and its timing |
| Sale agreement or restructuring support agreement (RSA) | 8-K Item 1.01, often with 7.01 or 8.01 and a press release | the endgame is defined. An RSA usually leads straight into a Chapter 11. A sale for less than about $311M of term debt leaves the stock with little or nothing (INFERRED) |
| Bankruptcy | 8-K **Item 1.03**, usually with 2.04, then Nasdaq 3.01 | a formal restructuring; the stock is most likely wiped out. The securitization trusts are separate legal entities, but Car-Mart services their loans, so a bankruptcy raises the question of who services them (INFERRED) |
| Acceleration | 8-K **Item 2.04** | lenders call the loan and move on the collateral; usually forces a 1.03 soon after |
| Lapse with no filing | nothing | defaults stand and lenders can act at any time; shows only when they do. Silence grades nothing |

**The twelve bridges (VERIFIED in my KB from each 8-K):**
- **Length:** 4, 7, 6, 7, 7, 7, 7, 10, 3, 5, 3, 4 calendar days. Since late October they run 3 to 5 days.
- **Fees and money:** only bridge 8 (Second Amendment, 10/15 to 10/20) added anything. That was $5.0M of new money ranked ahead of the existing loans, a $200,000 fee added to principal, an approved budget, payment of the lenders' Milbank legal bills, and a broad borrower release, including claims "arising under the Bankruptcy Code" (KB-BRK-356/357). The First Amendment had already raised the margin by 300bp to SOFR+10.50%, with a fee paid in kind (KB-BRK-268). Bridges 9 to 12 were Item 1.01 only, with no exhibit and no stated fee.
- **Language:** the "significant progress towards a transaction" paragraph appeared in bridges 1 to 7. It has been absent for **five straight filings**, absent rather than retracted. The 10-Q (9/9) carries substantial doubt about going concern. Car-Mart has no warehouse line to fund new loans (KB-BRK-265/266).

**What the pattern suggests (INFERRED):**
- The lenders prefer control without a filing. They keep the right to act on a few days' notice, have funded only a budgeted $5M, took a release of lender-liability and bankruptcy-law claims, and let the receivables book run off (ACM Auto Trust 2024-2 redeemed 10/20, about $92M of receivables released).
- That fits a lender-steered wind-down or a pre-arranged sale or Chapter 11 being prepared.

**What it does not tell us:**
- whether a buyer or a deal exists;
- the timing;
- recovery values;
- whether the lenders will file. Short bridges can run for months; this one already has run for about ten weeks.

### B7. Exposure to Car-Mart that the fleet tracks

| Who | Exposure | Date and source |
|---|---|---|
| Silver Point Finance (agent) and its lender group | term loans $305,608,825.77 at 10/14, plus the $5.0M ranked ahead; SOFR+10.50% | KB-BRK-357, Second Amendment Ex 10.1, 10/22. Private lender, no listed instrument. **Whether any public BDC holds the loan was NOT CHECKED this session.** |
| ACM Auto Trust securitizations | five trusts, not SEC filers (KB-BRK-270, 9/9); 2024-2 redeemed in full 10/20 (KB-BRK-356) | Noteholders and ratings on the remaining trusts were **not read** this session (private 144A; ratings-agency pages not checked) |
| OTTO's subprime-auto read | V9 "CRMT lender standstill", red 4, in OTTO's 32/50; OTTO re-colours only after BROCK's grade; `combo:lender-standstills` updated 11/13 | `AGENTS/OTTO/STATUS.md`, updated 11/13 10:28 ET; ML-OTTO-388/389 |
| BROCK | BRK-33: petition by 12/31, 35%. **No CRMT vector in my matrix**, and none of my 14 vectors moves on any outcome (pre-registered 9/2, held 9/9, KB-BRK-275) | STATUS 11/16 |
| TERRY | NO CARD 11/13: "CRMT / CABO (no chains)" | `AGENTS/TERRY/STATUS.md` line 14 |

---

## C. For TERRY: listed instruments

| Instrument | Why A or B could matter | BROCK view |
|---|---|---|
| BX, Blackstone: **$117.67, -2.10%** [fetch.py 11/16 ~11:20 ET] | BCRED is Blackstone's flagship private-credit fund. A third fire would make headlines, and fewer net assets (-13.6% this year) mean lower fees | headline risk only; the gate has no capital path. TERRY's call |
| OWL, Blue Owl: **$9.49, -2.67%** | OCIC already fired; OTIC's own gate grades Q4 from about 12/31 | no new mechanism from this read |
| APO, Apollo: **$121.68, -1.45%** | ADS sits at run 1; Will holds an APO Dec18 $95 put x1 (FORGE 10/14) | nothing here changes it; no expiry push |
| CRMT common: **$1.03, +10.13%** [Nasdaq real-time 11:20 ET] | direct: a 1.03 filing or an RSA most likely wipes the equity | no listed options per TERRY 11/13; shorting a $1 stock under a going-concern doubt is TERRY's question, not mine |
| Monroe Capital Income Plus | none: a private BDC, no listed shares | — |

**BROCK's answer: no new instrument with a clean line from these findings.** If any card follows, the names above are where it would sit. Today is a red day for these names (root rule #6, for TERRY).

---

## Not reached (time box)
- ACM Auto Trust remaining noteholders and ratings; any public BDC holding the Car-Mart term loan.
- BCRED facility maturities and the Citi revolver's minimum-equity figure; Monroe's MD&A liquidity paragraph in full.
- Whether CCLFX's 9/30 semiannual report is on EDGAR.
- Reconciling Monroe's Q1 share-count mismatch (final vs 10-Q).
- Surface propagation (STATUS, register cell, CATALYSTS) of the 11/30-is-expiry correction and the Q2 56.3%: KB rows written now; the other surfaces at closeout when PROME asks.
