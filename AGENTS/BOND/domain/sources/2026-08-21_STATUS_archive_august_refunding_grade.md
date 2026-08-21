# BOND STATUS — archived: the August 2026 Quarterly Refunding grade

**Archived 2026-08-21** by BOND during the Will-tasked STATUS audit — the largest single block on a 250-line-capped file, for an event graded ten days earlier.

⚠️ **This is the RECORD of a recovered gap, not routine history, which is why it is archived verbatim rather than compressed.** The $125B refunding ran 8/11–8/13 and **this desk had no record of it until 8/18** — the quarter's largest supply event passing ungraded while BOND was dark. It is the reason `monitors/docket_check.py` exists.

**Live pointers, so nothing here needs to be cited from this file:** grade → `KB-BND-136`; the benign-distribution read it settles → the FR2004 rows on `STATUS.md` and `monitors/DEALER_CAPACITY.md`; benchmarks re-derivable any time via `monitors/grade_auction.py --cusip <CUSIP>`.

⚠️ **Figures below are as-graded 2026-08-18, and the second of the two limits travels with them: the trailing-12 windows span a repricing regime, so the BTC comparisons (clearing by 0.01–0.07) carry no weight on their own — only the composition margins do.**

---

## ★ AUGUST QUARTERLY REFUNDING — GRADED 2026-08-18, 5 days late, NO COMPOSITION FAILURE (12th straight benign resolution)

> ⚠️ **This is a recovered gap, not a routine grade. The $125B August refunding ran 8/11–8/13 and this desk had no record of it until 8/18** — the largest supply event of the quarter, passing ungraded while BOND was dark. Found by cross-checking a WALTER wire reference against the TreasuryDirect primary. *The `data/auction_history_*.csv` corpus is stale to 2026-05-28, so no monitor would have surfaced it either — see the tooling note in `monitors/AUCTION_HEALTH.md`.*

**All percentages are of COMPETITIVE ACCEPTED** (the fleet-reconciled denominator). Benchmarks are each tenor's **own trailing-12**, derived per tenor from TreasuryDirect and never ported across tenors.

| Date | Tenor | Size | BTC | vs med | Indirect | vs med | Dealer | vs med (max) | High yield | Read |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|
| 8/11 | 3Y `91282CRG8` | $58B | **2.71** | +0.07 | **64.24%** | +1.28pp | **11.74%** | −0.37pp (max 19.50) | 4.2910% | 🟢 Healthy |
| 8/12 | 10Y `91282CRF0` | $42B | **2.53** | +0.07 | **76.73%** | **+8.41pp** | **8.60%** | −1.36pp (max 16.16) | 4.6830% | 🟢 Healthy — strongest leg |
| 8/13 | 30Y `912810UW6` | $25B | **2.39** | +0.01 | **66.85%** | +1.92pp | **11.51%** | +0.12pp (max 17.46) | **5.2160%** | 🟢 Healthy |

**Trailing-12 reference (nominal, same tenor, strictly prior):** 3Y — BTC med 2.64 / ind med 62.96, min 53.99 / dlr med 12.11, max 19.50. 10Y — BTC med 2.46 / ind med 68.32, min 63.95 / dlr med 9.96, max 16.16. 30Y — BTC med 2.38 / ind med 64.93, min 59.52 / dlr med 11.39, max 17.46.

**★ THE FINDING: the 30Y cleared the highest auction yield since 2001 with indirect demand ABOVE its trailing-12 median and dealers AT median.** Every leg of the composition-failure test (indirect below trailing-12 min **AND** dealer above trailing-12 max) fails at every tenor, and not narrowly — the 30Y's indirect clears its failure bar by **7.33pp** and its dealer take sits **5.95pp below** the max. **This is "expensive, not broken" passing the hardest supply test of the quarter: the price concession was paid in yield, and the buyer base did not change.**

**Two things this settles that were open:**
1. **The FR2004 drawdown is BENIGN — confirmed, not assumed.** The −$9.3B long-end decline in the week to 8/05 is dealers clearing balance sheet *ahead of* this refunding; the refunding then cleared into firm end-user demand with dealers at median. The monitor's own discriminator requires weak auctions and/or SOFR-IORB positive for the forced-de-risking branch; **the auctions were firm.**
2. **The 10Y's 76.73% indirect is the second-strongest of its trailing-12** and lands in the same week the 30Y made a 19-year high. **Foreign/custodial demand is not the thing that broke.**

> ⚠️ **Two honest limits on this grade, stated because they cut against how strong it reads.** **(a)** It is **5 days late**, so it is a reconstruction, not a live read — I did not watch the concession get paid and cannot speak to intraday behaviour. **(b)** The trailing-12 windows here span **2025-08 → 2026-07**, a period in which the whole curve repriced; a median drawn across a repricing regime is a weaker benchmark than the same median in a stable one. **The composition margins are wide enough (7.33pp at the 30Y) that benchmark placement error cannot flip the verdict** — the same discount logic I applied to `BND-13` on 7/28 — but the BTC comparisons, which clear by 0.01–0.07, are inside that noise and should carry **no** weight on their own.
