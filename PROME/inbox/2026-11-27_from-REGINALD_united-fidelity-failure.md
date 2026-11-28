# REGINALD -> PROME: United Fidelity Bank failure (11/27): resolution facts, severity, parent paper, read-across, forward view

**Written:** 2026-11-27 from 22:54 ET (`date`), REGINALD session reginald-2026-11-27-8654c74a, PROME prome-80 spawn on WALTER SIG-W-20261127-020. Delivery memo (COMPLETION_SPEC method 1), written at PROME's stop order (22:5x ET: Will opened his own REGINALD window, reginald-96, at 22:54 ET). The full findings sit in this memo only: the harness refused a separate report file under `AGENTS/REGINALD/reports/`, and on the stop order I wrote NO desk state (no STATUS, KB, BOARD_LOG, MEMORY, ROADMAP, receipts or inbox moves). The reginald-96 window carries the desk from here.

## Brief items: DONE / PARTIAL / NOT STARTED

| Brief item | State |
|---|---|
| 1. Primary resolution facts with source and date | DONE (table below; OCC release, First Citizens 8-K, P&A and bid summary NOT FOUND, queries named) |
| 2. Interpretation of the ~31% loss vs the prior read; spread evidence | DONE (here only) |
| 3. Parent notes and preferred | DONE (here only; BANX 9/30 mark read, DOCKET L1127 tell 2) |
| 4. Read-across to my names and bank theses | DONE as observations (here only); nothing graded, no gate touched |
| 5. Forward view | DONE (here only; unscored, no row registered) |
| 6. TERRY facts packet | NOT STARTED (not drafted, so not sent, per the stop order). TERRY already holds its own NO CARD (b521f8025b) and CORAL's Florida packet; the new facts for TERRY are claims 7, 13 and 15 below |
| Inbox drain (14 WALTER cards) | PARTIAL: all 14 READ and dispositions decided (list at end), **NONE marked consumed**: no BOARD_LOG row written, no `git mv` to processed/ |
| Correction receipts (COR-20261127-02, -03, -04, -05) | NOT STARTED (all four read; my intended action NO-OP, none touches a REGINALD figure) |
| STATUS current-state update, KB rows | NOT STARTED |
| Desk closeout | NOT STARTED (stop order: the window carries the desk) |

## Claims table

| # | Claim | Source | Date | Status |
|---|---|---|---|---|
| 1 | Closed by the OCC; FDIC receiver; First-Citizens Bank & Trust assumes substantially all deposits and buys substantially all assets | FDIC press release (fdic.gov/news/press-releases/2026/first-citizens-bank-trust-company-raleigh-north-carolina-assumes); FDIC failure page | 11/27 | VERIFIED |
| 2 | $5.9B assets, $5.4B deposits [9/30]; estimated DIF cost $1.83B = 30.9% of assets | FDIC release; FDIC BankFind API (ASSET $5,915,451K, DEP $5,369,687K) | 9/30; 11/27 | VERIFIED (ratio my arithmetic) |
| 3 | 22 branches IN, IL, FL, CO, USVI | FDIC release | 11/27 | VERIFIED |
| 4 | Holding company Fidelity Federal Bancorp "was not included in the closing of the bank or the resulting receivership" | FDIC FAQ and failure page | 11/27 | VERIFIED |
| 5 | Cede & Co. (brokered) deposits excluded from the assumption | FDIC FAQ; failure page says "certain brokered deposits" | 11/27 | VERIFIED |
| 6 | Claim priority: depositors, general unsecured, subordinated debt, stockholders | FDIC failure page | 11/27 | VERIFIED |
| 7 | First Citizens: assets $5.9B, deposits $4.5B, loans $3.1B; asset discount about $2.6B; no deposit premium; "whole bank purchase"; subsidiaries included, incl. Pedcor Homes Corporation; USVI branches as Bank of St. Croix; subject to closing balance sheet and settlement | First Citizens newsroom release, 11/27 | 11/27 | VERIFIED (issuer release, read via fetch helper) |
| 8 | Loss-share agreement | not in FDIC release, page, FAQ or First Citizens release | 11/27 | NOT FOUND; "no loss share" INFERRED |
| 9 | P&A agreement, bid summary, assets kept by receiver | FDIC pages; bid-summary URL probe 404 at 22:5x ET | 11/27 | NOT FOUND (not posted) |
| 10 | OCC's own release | OCC news RSS (occ.gov/rss/occ_news.xml, HTTP 200): latest nr-ia-2026-105 (11/25), no closing release | read 22:4x ET | NOT FOUND |
| 11 | First Citizens BancShares 8-K | EDGAR CIK 798941: nothing filed 11/27 (latest 8-K 11/19, before the failure) | read 22:47 ET | NOT FOUND |
| 12 | 2026 failures now 7; failed assets about $7.3B YTD | FDIC failed-bank list; QBP Q3 ($1,409M through Q3) | 11/27 | VERIFIED count; sum my arithmetic |
| 13 | **DOCKET L1127 tell (2) READ:** BANX 9/30 NPORT-P (filed 11/25, acc 0000940400-26-047397) marks Fidelity Federal Bancorp cumulative perpetual preferred Series A 2,789,000 at $1,533,950 and Series B 200,000 at $110,000 = 55.0% on both (6/30: 60%); 0.815% of net assets $201.73M; level 3 | EDGAR primary_doc.xml | as of 9/30 | VERIFIED |
| 14 | Spread to other lenders (same sponsors, property type, markets) | one web search; no EMMA, no county records | 11/27 | NOT FOUND tonight (not ruled out) |
| 15 | The 11/27 session (KRE $70.35, WAL $71.38, FCNCA $2,173.50, MBIN $50.10, vendor, retrieved 22:49 ET) closed before the announcement | half session ended 13:00 ET; release time not stated | 11/27 | INFERRED |

**9/30 Call Report cells (FDIC BankFind API, $M):** gross loans 3,059.4 (multifamily 2,721.6 = 89.0%); nonaccrual 2,159.1 (70.6%); allowance 6.3; Q3 net charge-offs 362.6; securities 1,359.3 (HTM 642.9, AFS 716.4); cash 109.2; brokered 1,006.5; equity 389.7.

## What I learned (interpretation, kept apart from the facts above)

**Severity (derived, INFERRED):** DIF cost is 30.9% of assets but 41.2% of the $4,446.9M of non-cash, non-securities assets (loans, $1.03B of real-estate venture equity, the $146.7M related-party fee receivable); the buyer's $2.6B discount is 44.0% of assets and 58.5% of those assets; 6/30 equity ($652.5M, gone) plus DIF cost is 55.8% of them. Deposits not assumed, about $870M, sit close to the $1,006.5M brokered balance. Rough bridge: discount $2.6B less equity $0.39B = $2.21B shortfall vs the $1.83B DIF estimate; the gap is not reconcilable from public data.

**Against the prior read ("isolated in-house concentration, transmission NOT shown"):** the failure CONFIRMS the concentration and LEAVES TRANSMISSION OPEN. A ~41% loss on the risk assets on top of all equity is what the structure the 11/11 record found predicts (stacked first and junior liens to one lender at 85% origination LTV, 2021-22 prices, related-party sponsors Pedcor and Birge & Held, venture equity and fee receivables that recover little, county values 1.54× below origination debt on 23 matched properties). It is not by itself a read on apartment values at other lenders. The resolution adds three containment facts (each INFERRED from the documents): every customer deposit moved whole, so there is no uninsured-depositor loss signal; FHLB advances were $0 since 12/2024; the book and Pedcor Homes went to a ~$230B buyer, so no fire-sale price has printed.

**Spread evidence that would matter:** missed payments or material-event notices on Pedcor or Birge & Held housing bonds (EMMA); lis pendens naming another lender; LIHTC investor write-downs; other banks' multifamily nonaccrual at the 12/31 Call Reports (~late Jan); a receiver pool sale. None found tonight. Nearest listed analogue by state and property type: Merchants Bancorp (MBIN, Indiana); no link to these sponsors is known.

**Parent paper (report D):** the holding company is outside the receivership and behind every bank creditor; at a $1.83B DIF loss nothing reaches stockholders (priority VERIFIED, the zero INFERRED). INFERENCE, no case document read: its outside paper (about $113.75M sub notes plus the ex-TARP preferred) recovers only from other holding-company assets (cash, its third lien on New City Place LLC, any tax refund the FDIC may contest); expect the preferred near zero and the notes deeply impaired, with a payment stop and possibly a bankruptcy filing. Exposure is small: BANX 0.815% of NAV at 55%; FINS 0.66%, Thompson 0.69% (report D). The 12/14 capital-plan date and its guarantee question are moot.

**Read-across (observations only; nothing graded, no gate touched):** none of my 14 is named; no score moved. REG-03 (Q4 industry CRE charge-off rate ≥ 1.5× Q2): a bank closed in Q4 files no 12/31 Call Report, so UFB's losses leave the Q4 industry rate (INFERRED); Q3 ex-UFB was 1.08×; the Q4 test now rests on other banks; not due until the Q4 QBP. REG-T-06: no FHLB exposure. Systemic-backstop exit rule: not fired. REG-T-02: the 11/27 WAL bar is not yet settled in `settled_bars.py`, so 11/27 is not graded (owed next session). Florida: CORAL's figures (3 branches, $668.2M deposits, $597.9M FL apartment originations, no flood-county overlap) are the fleet's one figure.

## Forward view, 1 to 4 weeks (unscored outlook, no row registered)

- **Expect (~80%):** a one-bank event through 12/28: KRE within ±2% of SPY on Mon 11/30, no second multifamily-concentrated failure, no small-bank deposit-flight story. Why: depositors whole, large buyer, in-house related-party book, FHLBs unexposed, two weeks of public warning.
- **Sequence:** FDIC posts P&A and bid summary (~50% by 12/28); First Citizens 8-K or more detail (~40%; the deal is ~2-3% of its size); holding company payment stop, bankruptcy filing within 4 weeks ~35%; BANX next public mark ≤10% of liquidation (~85%, but that filing is for 12/31, ~late Feb).
- **Alternative (~15-20%):** visible spread: a Pedcor or Birge & Held bond default at another trustee or lender, a second action or failure at an affordable-housing or multifamily-heavy small bank, or a listed lender disclosing these sponsors.
- **Would change my mind:** an EMMA failure-to-pay notice on these sponsors; a second OCC or FDIC action naming affordable multifamily; a single-bidder bid summary or a receiver loan-pool sale; KRE more than 3% under SPY Monday with small-bank deposits, not rates, as the stated cause.

## For PROME (row maintenance; your files, not edited by me)

- DOCKET L1127: tell (2) is READ (row 13 above). The row's last tell, "the Q4 Call Report (due 2027-01-30)", will not exist: a bank closed 11/27 files no 12/31 Call Report. The FINS (10/31, ~late Dec) and Thompson (11/30, ~Jan) marks remain readable tells; the P&A agreement and bid summary are new natural tells. Re-dating or closing the row is yours.
- SYNTHESIS.md is untouched (your file, review-limited); its 12/14 capital-plan and brokered-bar material is overtaken by the closing.
- No TERRY packet was sent by me (see the item table).

## Inbox cards: read, intended disposition, consumption state

All 14 at `AGENTS/REGINALD/inbox/WALTER/` remain UNCONSUMED (no BOARD_LOG row, not moved). Intended dispositions, for the reginald-96 window to apply or overrule:

| Card | Intended disposition | Note |
|---|---|---|
| SIG-W-20261127-020 (BANK_COLLATERAL, action REGINALD) | INTEGRATED | this memo |
| -007 and -013 (INFLATION_TRANSMISSION, action REGINALD) | INTEGRATED, one KB row | St. Louis Fed 8th District banking survey (11/17 file, confirmed at issuer by WALTER): loan demand net −30 (prior +11), standards +13, delinquency +28; one district (which includes Evansville), descriptive, no score; national SLOOS not read beside it |
| -006 and -014 (CYBER) | INFO_ONLY + KB row `combo:bank-vendor-breaches` | SAP dev-environment compromise, keys replaced; Lloyds outage cause unstated; no US core-banking vendor named |
| -008 and -012 (AI_INFRA_CAPEX) | INFO_ONLY + KB row `combo:bank-lending-to-private-credit` | Citi and JPM marketing AI loans incl. synthetic risk transfer, no amounts; large banks, not my 14 |
| -003 and -017 (CLIMATE_MACRO) | INFO_ONLY | Sanford forecast 9.0 ft vs 8.96 record; Seminole and Volusia are not in the SBCF five-county map; CORAL: UFB has no flood-county loans |
| -010, -015, -016, -018 (corrections) | INFO_ONLY; receipts COR-20261127-02 to -05 NO-OP | none corrects a figure I cite |
| -019 (MISC) | INFO_ONLY | Paraguay bank failure, no US channel |

BOARD diff beyond the lane: -004, -005, -009, -011, -021 checked by metadata: no REGINALD action, no mediating flag, no bank-ticker hit; none selected.

## COMPLETION — REGINALD — 2026-11-27
STATUS: ⚠️ PARTIAL
CHANGED: this memo only (PROME/inbox/2026-11-27_from-REGINALD_united-fidelity-failure.md)
RESULT: UFB resolution read at FDIC and First Citizens primaries: DIF cost $1.83B (30.9% of assets, 41.2% of risk assets), $2.6B asset discount, no deposit premium, $4.5B of $5.37B deposits assumed, Cede & Co. brokered excluded, holding company outside the receivership, loss share NOT FOUND; BANX 9/30 mark on the parent preferred 55% (from 60%), DOCKET L1127 tell (2) READ. Read: concentration CONFIRMED, transmission OPEN, no spread evidence tonight; forward ~80% one-bank event through 12/28.
GAPS: Stopped by PROME (second REGINALD writer, reginald-96): no STATUS, KB, BOARD_LOG, receipts or inbox moves; TERRY packet not drafted. Harness also refused a report file under reports/. OCC release, First Citizens 8-K, P&A, bid summary not out; EMMA and county records not read; REG-T-02 11/27 not graded.
WILL_NEEDS: None.
FOLLOW-UP: reginald-96 applies the 14 dispositions and 4 NO-OP receipts, writes STATUS/KB, sends TERRY the new facts (claims 7, 13, 15); PROME re-dates DOCKET L1127 (the Q4 Call Report tell cannot happen).
