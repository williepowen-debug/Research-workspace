# Q3 10-Q grading frame: dry run against the Q2 10-Q

**Run:** Fri 2026-10-30 14:07–14:10 ET. WAL (Claude Opus 5.5, Will-interactive; Will 14:07 ET: "okay lets do 1 through 3").
**Source:** Q2 2026 10-Q, acc 0001628280-26-051418 (`sources/q2_2026/wal-20260630.htm`, local copy pulled 10/13), converted to text for the search. The line numbers below refer to that text and are given for orientation only. **On filing day, search by the heading or the phrase, never by line.**
**Frame:** `Q3_10Q_GRADING_FRAME_2026-09-24.md` (frozen 10/22) + `Q3_10Q_RESCORE_RULE_2026-10-22.md` (incl. §6 Amendment 1, ruled 10/30).
**Purpose:** confirm that every cell the frame reads exists in this filer's 10-Q layout, and record where it lives, before the Q3 10-Q lands. **No cell, threshold or letter is changed.** The findings that affect reading go into the frame as a dated §8 reader note (non-gating), which the 10/22 freeze note permits.

## 1. Cell map (the frame's read order, §6)

| Frame cell | Where it lives in the Q2 10-Q (heading / exact phrase) | Q2 value (6/30/26) | Located? |
|---|---|---|---|
| ① Subsequent events | **No such note in the Q2 10-Q.** The Q1 10-Q carried Note 19 only because of the $99M event | — | ⚠️ May be absent at Q3 too: see finding F1 |
| ② $99M narrative | MD&A "Non-performing Assets": "primarily due to the migration of **a life science laboratory/office CRE loan, as previously disclosed**" | named as a driver of the NPL rise | ✅ Search "life science" (3 hits at Q2: this sentence + the property-type table) |
| ② Nonaccrual by segment | Note 4 "nonperforming loan balances by loan portfolio segment" (columns: Nonaccrual **with No Allowance** / **with an Allowance** / Total / 90+ accruing); MD&A "composition of nonaccrual loans HFI by loan portfolio segment" | Other CRE-NOO 279 (215 no-ACL / 64 with-ACL) · C&LD 109 (108 / 1) · Other C&I 142 (123 / 19) · total 562 (456 / 106) | ✅ |
| ③ NCO ratio (WAL-02) | MD&A sentence "annualized net loan charge-offs to average loans outstanding were X%" | 0.37% | ✅ printed |
| ③ ACL roll-forward | Note 4 "activity in the ACL on loans HFI by loan portfolio segment" (quarter and YTD tables) | — | ✅ |
| ③ Unfunded ACL (coverage leg) | MD&A sentence "This allowance balance totaled $…" (off-balance-sheet ACL) | $52.0M | ✅ |
| ④ Cantor / LAM | Note 15 "Legal Disputes Related to Credit Facilities": sub-heads "Cantor Group V, LLC" and "Leucadia Asset Management LLC and Jefferies Financial Group" | — | ✅ |
| ⑤ Classified loans (WAL-01 cross-check) | Note 4 "**Total by Risk Category**", row "Classified", Total column | **$1,002M** (ties KB-151) | ✅ ⚠️ The same text has a 12/31 block ($950M); take the block under the 9/30 date |
| ⑤ OREO balance + count | Note 6 "OTHER ASSETS ACQUIRED THROUGH FORECLOSURE": "The Company held N properties…"; MD&A NPA table "Other assets acquired through foreclosure, net" | $126M · 22 properties | ✅ Valuation losses: Note 6 activity text |
| ⑥ NDFI (V3) | MD&A "Concentrations of Lending Activities": row "Total loans to NDFIs" | $15,812M = 25.9% of HFI | ✅ |
| ⑥ Buyback | Part II "Item 2. Unregistered Sales of Equity Securities and Use of Proceeds" | Q2 program shares 31,924; remaining authorization $179,592,035 | ✅ ⚠️ No dollar column: see F4 |
| ⑥ AOCI / AFS | balance sheet; Note 2; Note 12 "DERIVATIVES AND HEDGING ACTIVITIES" (fair value hedges) | — | ✅ |
| §5 Full NPL | MD&A NPA table: "Total nonaccrual loans" + "Loans past due 90 days or more on accrual status" + "Accruing restructured loans" = "Total nonperforming loans" | 562 + 55 + 164 = **781** (ties KB-156) | ✅ ⚠️ See F3 |
| §5 PCD purchase ($64M tie) | MD&A NPA sentence "purchase of $64 million of loans with more-than-insignificant deterioration" | $64M | ✅ |
| O1–O3 HFF | Note 4 segment rows "Hotel franchise finance" (risk category, nonaccrual, charge-offs) | special mention 31 · classified 4 (risk table) | ✅ |
| O4 Property type | MD&A CRE-NOO property-type table (Hotel, Office, Life sciences rows) | Life sciences $418M (4.1%, LTV 52.7%) | ✅ |
| Collateral-dependent loans | Note 4 "**Collateral-Dependent Loans**" table by segment; Note 16 fair value, Level 3 "collateral dependent loans … net of a specific ACL of $X" | Other CRE-NOO 266 · C&LD 108 · Other C&I 129 · total 504; Level 3 FV $481M net of **specific ACL $23M** (12/31: $15M) | ✅ **Not read by the frame:** see F2 |
| Problem loans by count | MD&A "Problem Loans" table (number of loans + balance by segment; performing, not individually evaluated) | 277 loans · $755M | ✅ Not read by the frame (LOG only) |

## 2. Findings

| # | Finding | Effect on grading | Disposition |
|---|---|---|---|
| **F1** | The Q2 10-Q has **no subsequent-events note**. The Q1 note existed only because of the $99M event | Read-order step ① may find nothing. Absence of the note is **uninformative** (not "no subsequent events"); go on to ② | Reader note |
| **F2** | **The 10-Q's most likely trace of a below-book appraisal is unnamed and aggregate:** (a) a ~$99M move from "Nonaccrual **with No Allowance**" to "**with an Allowance**" within one segment; (b) a jump in the Level-3 "**specific ACL**" on collateral-dependent loans (6/30 $23M); (c) a change in the collateral-dependent table. WAL names single loans only in narrative ("as previously disclosed") | Under the frame's explicit-only principle (W9), aggregates **never assign a letter**. A tell with no naming narrative leaves the letter where §4 puts it (B if the loan is named as still nonaccrual; otherwise NO-VERDICT). The tell is **LOGGED as CANDIDATE evidence** and becomes a direct question for the Q4 call | Reader note: log cells with Q2 anchors |
| **F3** | "90+ days accruing" has two figures: the Note 4 table's $303M **includes** $248M government-guaranteed EBO; the MD&A NPA table's $55M **excludes** it. The full-NPL basis that ties to $781M uses **$55M** | Prevents a ~$248M overstatement in the full-NPL line | Reader note: use the MD&A NPA-table basis |
| **F4** | Item 2 has **no dollar column**. Q3 program dollars = the fall in "Approximate Dollar Value … Yet Be Purchased" across the quarter (or the program-column shares × average price). The total-shares column includes tax-withholding shares outside the program | The ≥ $75M / $50–75M / < $50M test reads program dollars only | Reader note |
| **F5** | The risk-category table appears twice (9/30 and 12/31 blocks) in the same layout | Take the "Total by Risk Category" block under the 9/30 date | Reader note |

## 3. What the dry run cannot test

- It shows the cells **exist in this filer's layout**; WAL can change its layout in Q3 (it created the life-sciences category in Q1, KB-141). A cell that is missing on filing day grades by the frame's own "missing means" column.
- It does not test the frame's thresholds or letters. Those are frozen; only the re-score rule's §6 window (closed for B′ on 10/30) allowed changes.
