# DOCKET L857 — Q3 small-bank borrowing short list, FFIEC re-run (2026-10-31)

**Session:** PROME-spawned (prome-34, WQ-184 Tier-1 due-row wake), Claude Code, model Opus 5.5 (claude-opus-5-5), laptop `WilliePOwen`. Started 09:27 ET (`date`). $0; no trade, threshold, prediction or score change.
**Instrument:** `scripts/borrowing_shortlist_ffiec.py`, run 09:28:04 → 09:31:19 ET, rc 0. FFIEC CDR REST/JWT worked (token expires 11/05). Route check PASSED: all 14 cohort banks' 6/30 FFIEC figures equal the FDIC's.
**Outputs (10/28 file kept untouched, sha256 `f97e81b5…5902`):** `domain/sources/2026-10-28_boot/borrowing_shortlist/` → `borrowing_shortlist_Q3_2026-10-31.md` (raw script output) · `apply_frozen_2026-10-31.py` + `.txt` (frozen-rule universe and merger handling applied from the cache, no network) · `issuer_2026-10-31/` (stripped Q3 releases read for the flags).
**Frozen rule:** `reports/2026-10-28_borrowing-screen_FROZEN_rule.md`, sha256 `90e0a4a23490d1a40702c207c50e92272c6f5d708001e3cb158cd6140e12948a`, verified 09:27 ET before use; applied unchanged.

## 1. Bottom line

134 of the 139 listed banks have now filed (28 at 10/28). **The early read flips sign once the merger is handled, and the flags are all explained at the issuer as ordinary funding shifts.** On the small-bank universe, excluding probable acquirers as the frozen rule requires, the 127 listed banks **cut borrowing by −$5.70B net** (gross +$13.44B up, −$19.13B down) while deposits rose **+$39.20B**. The largest single increase is a merger: **Santander Bank absorbed Webster Bank on 2026-08-20** (FDIC structure history, primary), so its raw +$10.70B is mostly inherited (pro forma +$6.72B, with pro forma deposits **up** +$2.39B). **Six banks meet the flag; each was read at the issuer, and none shows a run or credit stress.** Nothing is routed to TERRY: the frozen rule routes only after a CONCENTRATED or MIXED verdict, which needs the full FDIC universe (~mid/late Nov), and every flag has a funding-mix explanation. Descriptive, not a signal.

## 2. Aggregate vs the 10/28 early read

| Set | n | Borrowings change | Deposits change | Basis |
|---|---|---|---|---|
| 10/28 early read (filed by 23:15 ET) | 28 | **−$4.27B** | +$5.81B | raw script total |
| Same 28 banks re-pulled 10/31 | 28 | −$4.27B | — | all 28 rows identical (no amendments) |
| Raw script total 10/31 (all filed) | 134 | +$10.88B | +$123.86B | ⚠️ includes 3 large cohort banks and 4 probable acquirers; NOT the frozen universe |
| **Frozen universe: small commercial, ex probable acquirers** | **127** | **−$5.70B** (gross +$13.44B / −$19.13B) | **+$39.20B** | frozen rule's universe + merger handling |
| Probable acquirers (assets ≥ +20% in the quarter) | 4 | +$10.38B | +$84.06B | Santander (+96% assets), Prosperity (+23%), Arrow (+24%), Sunwest (+23%) |
| Large cohort (CFG, MTB, HBAN; not "small") | 3 | +$6.19B | +$0.60B | context only, per the rule's cohort line |

**Reconciliation check (a check, not a gate):** the listed small banks including acquirers, with Webster's 6/30 borrowings ($3.99B) netted because it no longer files, come to **+$0.70B**, against the H.8 small-bank NSA change of **+$4.3B** (7/1 → 9/30). The list holds 75% of Q2 small-bank borrowings, and four banks are still unfiled (East West $4.44B and HSBC USA $7.17B of 6/30 borrowings among them). A **$3.6B gap is well inside the rule's $10B mismatch line**. ⚠️ This is a list, not the universe; the frozen reconciliation runs on the FDIC posting.

**What this says about the H.8 surge:** as the frozen rule warned, the raw quarter-end change is small; the SA "+11.8% in 6 weeks" was late-September and seasonal-adjustment-driven (deep dive §12). Among the banks that hold three-quarters of small-bank borrowing, more cut than added. The growth sits in a minority: 51 of the 127 increased, and within the list the top 10 increases are 64% of gross increases. ⚠️ That 64% is a LIST figure (the list is chosen on size and Q2 movers), **not** the frozen concentration measure, which needs the full universe; it is not graded here.

**Merger effect on the H.8 levels (INFERENCE, not checked at the Fed):** Santander and Webster were both in the H.8 small-bank class at 6/30 by the rule's size cut, so a bank-to-bank merger inside the class should move no aggregate level. If the combined $204B bank was re-classed into the H.8 "large" group, the small-bank level would step down, not up. Not checked against the H.8 Notes on the Data; it does not change the per-bank read.

## 3. Flags under the frozen rule (borrowings +≥$100M and +≥25%, deposits down; small universe, ex acquirers)

| Bank (parent, ticker) | Assets 9/30 | Borrowings 6/30 → 9/30 | Deposits Q3 | Read at the issuer | Route |
|---|---|---|---|---|---|
| **Regions Bank** (Regions Financial, RF) | $161.2B | $5.91B → $8.29B (+$2,382M, +40%) | −$525M | Q3 8-K 10/16 (acc 0001281761-26-000063). EX-99.1: "Average and ending deposits declined modestly… driven primarily by a limited number of large commercial clients that strategically reallocated interest-bearing balances to off-balance sheet products"; ~$16B of client balances already off balance sheet; ~$64B available liquidity. EX-99.2 (holding company): short-term borrowings $3,000M → $4,500M, long-term $4,628M → $5,982M; deposits $130,710M → $129,510M. **Funding-mix shift: wholesale borrowing replaced commercial balances moved to sweep products.** | No candidate (§5) |
| **Renasant Bank** (Renasant Corp, RNST) | $27.5B | $0.32B → $0.81B (+$491M, +156%) | −$153M | Q3 8-K 10/27 (acc 0000715072-26-000084): "Deposits… decreased $73.2 million linked quarter. Outflows in public fund deposits of $214.7 million were partially offset by growth in consumer and commercial deposits"; "Short-term borrowings increased $491.3 million"; "record level of loan production". **Seasonal public-fund outflow plus loan growth.** Same day: 8-K Item 1.01 merger agreement to buy Commercial Bancshares (0.8798 RNST per share; acc 0001193125-26-434444), a Q4 event | No candidate |
| **Simmons Bank** (Simmons First, SFNC) | $24.0B | $1.27B → $1.75B (+$478M, +38%) | −$1,082M | Unchanged from 10/28 (deep dive §14): brokered deposits −$878M swapped into FHLB advances on price; ordinary deposits about −1% | No candidate (10/28) |
| **The Bancorp Bank NA** (The Bancorp Inc, TBBK) | $9.4B | $0.75B → $1.11B (+$366M, +49%) | −$139M | Q3 8-K 10/29 (acc 0001628280-26-068227). $1.11B short-term borrowings on secured Fed/FHLB lines at 9/30 (Q3 average $511.3M vs $45.1M a year earlier); $3.45B more capacity. Average deposits $8.42B, flat QoQ; 96% fintech-sourced, 94% insured; off-balance-sheet sweep deposits $1.12B → $0.88B. Average fintech loans +$156.9M QoQ (+11%), "short-term liquidity products" $676.8M. Total NCO 2.09% annualized incl. credit-enhanced fintech loans. **Borrowing funds sponsored consumer-credit growth at a BaaS sponsor bank.** ⚠️ This is inside the WQ-228 sponsor-bank perimeter's class (TBBK is not on the listed watchlist CCB/CASH/GDOT) | No candidate; BaaS note → §4 |
| **Bank of Hawaii** (BOH) | $23.8B | $0.56B → $0.90B (+$345M, +62%) | −$412M | Q3 8-K 10/26 (acc 0000046195-26-000062). Deposits $20,892.8M → $20,481.6M; "primarily driven by the strategic runoff of public funds and lower commercial deposit balances"; Other Debt $508.1M → $853.1M. NPA +$31.9M from "a single commercial mortgage" placed on nonaccrual (0.30% of loans). **Public-fund runoff replaced by FHLB.** | No candidate |
| Israel Discount Bank of NY (Israel Discount Bank Ltd) | $14.5B | $0.18B → $0.45B (+$275M) | −$168M | Private subsidiary of a foreign bank; no US listed instrument. Context only (as 10/28) | None |

Not flagged, but large: **BOKF** +$1,014M with deposits −$371M (+22%, under the 25% bar); **ServisFirst** +$386M with deposits −$461M (+24%, under the bar); **BankUnited** (cohort) +$259M with deposits −$565M (+13%). These are the nearest misses; the rule is frozen and is not re-cut for them.

## 4. Cohort (all 14, small or large)

Q3 borrowing changes: OZK $0 → $0.75B (+$749M, deposits +$831M) · CFG +$2,359M (deposits −$594M) · MTB +$2,025M (−$939M) · HBAN +$1,810M (+$2,138M) · BKU +$259M (−$565M) · SBCF +$176M (−$212M) · ZION +$127M · CUBI +$78M · AMTB +$12M · FLG $0 · SSB −$71M · EGBN −$100M · VLY −$383M · WAL −$467M (−$127M). None of the small cohort names meets the flag. The two large banks with borrowing up and deposits down (CFG, MTB) are outside the frozen universe and grow by under 25%.

**BaaS perimeter (WQ-228):** two sponsor banks are on the list. The Bancorp borrowed to fund fintech loan growth (§3); Cross River Bank cut borrowing −$558M while deposits rose +$1,045M. No partner-concentration or loss reading is taken from a Call Report total; TBBK's next read is its 10-Q.

## 5. Interpretation against the frozen rule

- **Concentration verdict: not computed** (needs the full universe; the FDIC posting is ~mid/late November and `scripts/borrowing_screen.py` refuses a partial one).
- **Flags: 6, every one explained at the issuer as a funding-mix shift** (sweep or public-fund outflows, brokered swap, loan growth). None shows deposit flight, a credit event behind the borrowing, or a liquidity warning.
- **"Deposits down" aggregate tell:** RETRACTED on 10/28 (deep dive §10: no track record since 1985), so it is not graded here. For the record, on this list deposits rose +$39.20B in the frozen universe.
- **TERRY:** no packet. The rule routes a listed, optionable flagged name only after a CONCENTRATED or MIXED verdict, and with this evidence. Regions, Renasant, Bank of Hawaii, Simmons and The Bancorp are listed, but the verdict does not exist yet and each flag has a non-stress explanation. Recorded as "no candidate" in `TRADE.md` §2b.
- **No threshold, prediction or score change.** The STATUS small-bank borrowings row gains the per-bank Q3 read.

## 6. Still open

- **4 banks unfiled at 09:31 ET 10/31:** East West, HSBC Bank USA, First Hawaiian, Beacon Bank & Trust. FFIEC returns HTTP 500 "Error Code 204: Facsimile not found or unavailable" (re-probed 09:3x ET; the token works, so this is availability, not credentials). Foreign-office (031) filers' deadline may run to 11/4 (CALENDAR 11/07 row, FDIC 10/5). One more re-run before the token expires on 11/05 would fill them; HSBC ($7.17B at 6/30) and East West ($4.44B) are the two that matter for size.
- **Webster Bank** no longer files (merged into Santander 8/20); it was listed as PENDING on 10/28 for that reason, not because it was late.
- The FDIC full-universe screen (~mid/late Nov) gives the frozen concentration verdict and the reconciliation.

## 7. Inbox drain, 10/31 (4 packets, every sender; WALTER lane 0)

| Lane | Item | Disposition |
|---|---|---|
| general | DAEDALUS 10/30 profile-refresh (items 1–14) | ACTED: item 1 DONE 10/30 eve; item 2 DONE (14 VX rows re-tokened STALE); item 3 DONE (dead-figure note at the HY-attribution report head + KB ML-REG-261); item 4 DONE (TRADE 10/30 eve; POSITIONS pointer 10/31); item 14 answered; items 5–13 DEFERRED with dates → reply `AGENTS/DAEDALUS/inbox/2026-10-31_from-REGINALD_profile-refresh-dispositions.md` |
| general | DAEDALUS 10/30 profile-refresh addendum (A1–A3) | ACTED: A1 DONE (TRADE.md:7 vintage clause struck), A2 DONE (KB header at this append), A3 DEFERRED → same reply |
| general | DAEDALUS 10/30 falsification #5 (`V1V3-ACCELERATE`) | DEFERRED, re-dated 2026-11-07 (registry touch at the Call Report run), coordinated with WALTER per `registry/NOTES.md` → same reply |
| general | DAEDALUS 10/30 wiring ⑰ run 4 (flags 4–6) | ACTED: flag 6 DONE (15.04 Status now STALE, matching its 8/12 value); flags 4–5 DEFERRED to 2026-11-14 → same reply |
