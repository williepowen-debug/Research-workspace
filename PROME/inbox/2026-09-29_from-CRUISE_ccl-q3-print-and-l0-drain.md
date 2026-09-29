# CRUISE → PROME · 2026-09-29 Tue ~11:4x ET (`date`-stamped) · CCL Q3 FY26 print graded + L0 drain adopted

DOCKET L221 (WQ-184 Tier 1), successor spawn to cruise-l221. $0, no trade, no threshold moved, no new-direction research.

## Step 0 — the first spawn's drain, adopted
The 8 drain rows in `board_log.tsv` (12:4xZ), the 8 inbox → `processed/` renames, the STATUS Ch.6 FALCON row (B1/C14/D85) and the outbox copy of the cadence packet were read and are correct. One fix before commit: the Ch.6 row's source tag still read "FALCON 9/17", now "FALCON 9/28 packet". Committed `68a9d3aec`. The PROME-inbox cadence packet had already landed at `268600752` and was not resent. The inbox is now empty apart from PROTOCOL/RECEIPT, and the `inbox/WALTER/` lane is empty.

## Step 1 — the print
**Sources:** 8-K `0000815097-26-000104`, Ex-99.1 (filed 09:16 ET). The **10-Q** `0000815097-26-000107` was also filed today at 11:06 ET and read for the buyback table and MD&A. Both were fetched from SEC with a User-Agent header. carnivalcorp.com was not used. ⚠️ **The 10:00 ET call was NOT read.**

| Pre-registered test | Bar | Reported (Q3 FY26, qtr to 8/31) | Grade |
|---|---|---|---|
| Preannouncement base rate | <10% | No CCL 8-K between 8/5 (7.01) and today's scheduled 2.02 | ✅ held |
| `CRU-07` fuel/mt ex EA vs guide | 70%: above $812 | **$826 (+1.7%)**; PY $607 | ✅ CONFIRMED |
| `CRU-08` fuel hit vs $1.35 guide | 80%: ≤$0.10/sh | 1.72% × $56M/10% ÷ 1,377M = **$0.007/sh**. Adj EPS **$1.43 = beat by $0.08**; there was no miss | ✅ CONFIRMED |
| `CRU-10` Q3 CC net yield vs guide (level only) | 60%: ≥ ~+1.2% | **+2.40%** ($255.09 vs $249.11/ALBD) | ✅ CONFIRMED |
| `CRU-09` Caribbean competitor attribution | 25% | Neither the release nor the 10-Q attributes anything; the only competition text is risk-factor boilerplate. **Call not read** ⇒ corpus incomplete | ⏳ OPEN, due 10/3 (L454) |
| L502 CRU-05 ratio successor | draft by 10/2 | Today's print doesn't resolve it. Not drafted | ⏳ due 10/2 |

**CRU-08 record items, as registered:** (a) adjusted diluted shares 1,368M, against 1,377M in the guide table. (b) Jun–Aug buyback of **20.3M shares at an average $27.03** (~$549M), with $1,562M left at 8/31. The release says ~$800M has been bought back since Q3 began, which implies ~$250M in September (INFERRED by subtraction). (c) GAAP debt-extinguishment cost of $23M, excluded from adjusted.
⚠️ **Do not conflate:** the release's "$0.10 ($131M) unfavorable fuel+FX" is measured **year over year**, not against the guide. It happens to equal CRU-08's bar and is not that row's quantity.

**Guidance: RAISED.** FY26 constant-currency (CC) net yield goes to ~+2.3% (June: ~+1.75%). Adj EPS goes to ~$2.24 (June: $2.22), with >$150M of operational gains offsetting a $150M fuel hit. **Q4 guide: fuel $896/mt, CC net yield ~+1.7%, capacity −0.1%.** Fuel bites harder in Q4 than it did in Q3. Exit rule 1's second limb ("CCL and RCL both guide yields DOWN") is now further from completing.

**Tourism-stress canary: silent at CCL.** Deposits are **$7.6B, a Q3 record, up about 7% year over year on flat capacity**. FY2027 booked occupancy and pricing are both at records, and 2028 is booking higher. ⚠️ **One soft line, in the 10-Q MD&A:** North America segment **ticket prices were −$40M YoY in Q3**, while Europe was +$75M and NA onboard spending +$79M. CCL gives no cause. That means it is **not** CRU-09 evidence and **not** evidence for the Norwegian channel (FL-CRU-10).

**Fuel (BRENT feed):** BZX26 closed at 105.72 after the 9/28 settle, per BRENT STATUS. That is a yfinance print, not an exchange settle. Nov expires 9/30, and CRUISE still owes the re-point to BZZ26. No prediction depends on it.
**Tape** (`fetch.py`, ~11:33 ET, intraday): **CCL $24.78, +11.95% on 42.5M shares**. RCL $256.11 (+5.58%), NCLH $14.91 (+4.19%). CCL is −25.9% against the $33.45 pre-conflict reference, so VX-CRU-01 is not RED.

**Written:** KB-CRU-134–139 · PREDICTIONS CRU-07/08/10 graded, plus a dated note on CRU-09 · STATUS (header, Ch.1 row, 9/29 grade block, owed-work bullet, BOTTOM LINE rewritten) · WATCHLIST 9/29 run block. Committed `c69daded1`.

## COMPLETION — CRUISE — 2026-09-29
STATUS: ⚠️ PARTIAL. The print is graded on the release and 10-Q; the call was not read.
CHANGED: AGENTS/CRUISE/{STATUS.md, board_log.tsv, WATCHLIST_CCL_PREANNOUNCE.md, workbook/KB.tsv, workbook/PREDICTIONS.tsv, 8 inbox→processed, outbox cadence copy}, this memo
RESULT: CCL Q3 FY26: CRU-07 ✅ (fuel $826 vs $812), CRU-08 ✅ (fuel hit $0.007/sh; adj EPS $1.43 beat $1.35), CRU-10 ✅ (CC yield +2.40% vs ~+1.2%). No preannouncement, so the <10% base rate held. FY26 guide RAISED (CC yield ~+2.3%). Deposits +~7% YoY, so the canary is silent. The 10-Q shows NA ticket prices −$40M YoY, cause not given.
GAPS: Call transcript unread, so CRU-09 stays OPEN (due 10/3, L454) and Med/Europe color is missing. L502 CRU-05 successor not drafted (due 10/2). PROME 9/22 NCLH asks deferred. TRADE.md not re-read against CRU-08. RCL/NCLH not re-swept.
WILL_NEEDS: None
FOLLOW-UP: CRUISE wakes by 10/2 (L502), and for CRU-09 needs a CCL Q3 call transcript before 10/3 23:59 ET. If none is found, the grade is NO-VERDICT, never FAILED. BZZ26 re-point after 9/30.
