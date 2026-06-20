# BOND Monitor — Treasury Auction Health

**Owner:** BOND
**Last Updated:** 2026-06-20 by BOND
**Purpose:** Track whether Treasury market absorption is improving, mechanically supported, or deteriorating.

## Classification Rules

| State | Criteria | Signal |
|---|---|---|
| 🟢 Healthy | BTC near/above recent avg, stop-through/small tail, indirect demand stable | No action |
| 🟡 Watch | BTC below recent avg or modest tail; dealer take-down elevated once | Note in STATUS |
| 🟠 Stress building | BTC <2.3 or tail >2bps; weak indirect demand | Signal LIQUID/ZHAO if consequential |
| 🔴 Auction dysfunction | 2+ weak auctions in same tenor sector or large tail + dealer absorption spike | Signal LIQUID, ZHAO, PROME |

## Rolling Table

| Date | Tenor | Size | BTC | High Yield | Indirect % | Direct % | Dealer % | Read | Source | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 2026-04-22 | 20Y reopening | $13B | 2.68 | 4.883% | 59.6 | 20.2 | 8.6 | 🟢/🟡 | FiscalData | Good cover; long-end yield high. |
| 2026-04-23 | 5Y TIPS | $26B | 2.57 | 1.367% | 57.0 | 23.7 | 7.5 | 🟢 | FiscalData | Improved vs March stress. |
| 2026-04-27 | 2Y | $69B | 2.65 | 3.812% | 49.7 | 27.8 | 10.4 | 🟢/🟡 | FiscalData | Adequate. |
| 2026-04-27 | 5Y | $70B | 2.33 | 3.955% | 64.1 | 13.3 | 11.2 | 🟡 | FiscalData | Soft BTC but indirect strong. |
| 2026-04-28 | 7Y | $44B | 2.51 | 4.175% | 51.7 | 26.6 | 10.3 | 🟢/🟡 | FiscalData | No failure. |
| 2026-05-11 | 3Y | $58B | 2.54 | 3.965% | 63.0 | 20.1 | 16.9 | 🟡 | Treasury PDF / InvestingLive | +0.6bp tail; BTC below 6mo avg; dealer take elevated. |
| 2026-05-12 | 10Y | $42B | 2.40 | 4.468% | 64.0 | 24.1 | 12.0 | 🟡 | Treasury PDF / ZH | +0.4bp tail to 4.464 WI; below avg BTC; 4th consecutive 10Y tail per market commentary. |
| 2026-05-13 | 30Y | $25B | 2.30 | 5.046% | 66.6 | 21.7 | 11.7 | 🟡 | Treasury PDF / InvestingLive | +0.5bp tail to 5.041 WI; below avg BTC; demand mix not failed. |
| 2026-05-14 | 4W Bill | — | 2.66 | — | — | — | — | 🟢 | TreasuryDirect | Clean. |
| 2026-05-14 | 8W Bill | — | 2.72 | — | — | — | — | 🟢 | TreasuryDirect | Clean. |
| 2026-05-18 | 13W Bill | — | 3.17 | — | — | — | — | 🟢 | TreasuryDirect | Clean. |
| 2026-05-18 | 26W Bill | — | 3.07 | — | — | — | — | 🟢 | TreasuryDirect | Clean. |
| 2026-05-19 | 6W Bill | — | 3.01 | — | — | — | — | 🟢 | TreasuryDirect | Clean. |
| 2026-05-20 | **20Y Bond (new issue)** | $16B | **2.55** | **5.122%** (tail **0bp**, ZH) | **67.7** | **22.9** | **9.4** | 🟢/🟡 | FiscalData CUSIP 912810UV8 + ZH 5/20 ~1:30pm ET (single-source) | **Tail 0bp — stopped on the screws.** New issue (NOT reopen — coupon 5.000%, dated 5/15) vs 4/22 reopen $13B. Indirect rose vs 4/22 (67.7 vs 59.6); dealer near baseline (9.4 vs 8.6). BTC 2.55 below 2.60 clean threshold but above 2.30 stress floor. WI 5.122% at 1pm ET matched high yield exactly (ZH recap). DGS20 5/18 was 5.14% → today priced ~2bp THROUGH prior CMT (demand below the screen). Broke an 11-of-12 stop-through streak but did NOT tail. **No orange trigger fired.** ZH headline mislabeled "7Y"; body is unambiguously 20Y. URL: https://www.zerohedge.com/markets/solid-7y-auction-prices-screws-solid-foreign-demand |
| 2026-05-21 | **10Y TIPS reopen** (9Y8M) | $19B | 2.52 | **2.169% (real)** | 61.4 | 27.5 | 11.1 | 🟢 | FiscalData CUSIP 91282CPU9 | **CORRECTION: this was a 10Y TIPS reopening, NOT a nominal 10Y.** Real HY 2.169%. No stress. Prior STATUS mislabeled it the nominal "Leg 2" demand gate (TIPS-vs-nominal conflation). |
| 2026-05-26 | 2Y | $69B | 2.64 | 4.071% | 57.6 | 30.1 | 12.3 | 🟡 | FiscalData | BTC 28th-pctile of 81 2Y since 2023 — below-median, not "solid." Cleared orderly. |
| 2026-05-27 | 5Y | $70B | 2.34 | 4.182% | 74.9 | 12.3 | 12.8 | 🟡 | FiscalData | BTC 24th-pctile of 54 5Y — soft, in-pattern (≈Apr-27's 2.33); strong indirect offsets. |
| 2026-05-28 | 7Y | $44B | 2.52 | 4.290% | 78.4 | 11.2 | 10.4 | 🟢 | FiscalData | BTC 50th-pctile (median); foreign sponsorship solid. |
| 2026-06-09 | 3Y | $58B | 2.64 | 4.192% | 63.7 | 21.0 | 15.3 | 🟡 | TreasuryDirect | Solid front-end; PD take a touch elevated. |
| 2026-06-10 | 10Y reopening | $39B | **2.57** | 4.538% | **78.2** | 12.3 | 9.5 | 🟢 | TreasuryDirect 91282CQQ7 | **STRONG** — record-ish indirect, dealers barely absorbed; broke the 5th-tail fear. |
| 2026-06-11 | 30Y reopening | $22B | 2.33 | 5.020% | 59.84 | 25.3 | 14.7 | 🟡 | TreasuryDirect 912810UU0 | **Soft-but-orderly** — BTC held >2.3, indirect a hair <60; ~8bp same-day rally. *(secondary "6/12 BTC 2.43" = WRONG, misdated.)* |
| 2026-06-16 | 20Y reopening | $13B | **2.75** | 4.927% | **71.6** | 19.9 | 8.5 | 🟢 | TreasuryDirect 912810UV8 | **STRONG** — ~-1bp stop-through, best BTC in 3mo (breaks 2.76→2.68→2.55 trend); BND-09 FALSE. |
| 2026-06-18 | 5Y TIPS reopening | $24B | 2.61 | 1.955% (real) | 68.6 | 28.0 | 3.4 | 🟢 | TreasuryDirect 91282CQP9 | Solid real-money; dealer 3.4% lowest in 1yr+. *(NOT a 10Y — the soft 10Y TIPS was 5/21.)* |

*June bills (6/15–6/18) all cleared clean — BTCs 2.47–3.12; 13W softest (2.47, pre-FOMC re-investment caution), 6W strongest (3.12). No bill stress.*

**Percentile context (PROME dataset v2, 369 rows 2023→5/28, refreshed 6/5):** late-May nominal coupons were **below-median to median on bid-to-cover** (2Y 28th, 5Y 24th, 7Y 50th pctile) — softer than the headline BTCs "look." But all cleared orderly with no tails/dysfunction and strong indirect. Read: **persistent duration fatigue / demand-at-a-discount, not dysfunction.** Note: the dataset's `tail_vs_cmt_bps` is a noisy prior-day-CMT proxy (e.g. -240bp for the 5/21 TIPS vs a nominal CMT is meaningless); rely on BTC percentiles + indirect mix, not that column.

## Open Questions

- ✅ **RESOLVED:** Does 10Y >4.5 / 30Y >5 persist for multiple sessions? **YES** — 30Y >5.0 for ~9 sessions (5/14-5/27), 10Y >4.5 for 6 (5/15-5/22). BND-07 TRUE. But both have since mean-reverted (10Y 4.47, 30Y 4.97 by 6/4) — durable episode, not a one-way break.
- Does weak-but-not-failed auction demand begin funding through LIQUID plumbing (SOFR-IORB positive, repo pressure)? **No evidence yet** — SOFR-IORB **-2bp (6/17)**, tighter than the -12bps of 5/19 but still negative; no funding stress through the June gate.
- Does ZHAO see TIC / foreign official demand deterioration confirming auction-level softness? **Still open** — late-May indirects were strong (5Y 74.9%, 7Y 78.4% of comp), arguing against a foreign demand hole.

## June Refunding + 20Y/TIPS Read (6/9–6/18, RESOLVED)

All cleared — **no stress markers**. The 6/10 10Y reopening was the standout (BTC 2.57, indirect 78.2%, dealer 9.5% — broke the 5th-consecutive-10Y-tail fear); the 6/11 30Y was soft-but-orderly (BTC 2.33 held >2.3, indirect 59.84%, no outlier repeat of the 5/13 11th-pctile print); the **6/16 20Y reopening printed STRONG** (BTC 2.75 — best in 3mo, ~-1bp stop-through, indirect 71.6%), resolving **BND-09 FALSE**; the 6/18 5Y TIPS was solid (BTC 2.61, real 1.955%). The into-gate hawkish FOMC did NOT translate to auction stress. **Next live gate: the 6/23–25 2Y/5Y/7Y cluster** — first coupons under the hawkish-FOMC regime (record MMF cash a demand headwind).

## May 2026 Refunding Read

All three coupon auctions tailed modestly: 3Y +0.6bp, 10Y +0.4bp, 30Y +0.5bp. Bid/covers were below recent averages, but tails were not large, indirect demand was not collapsing, and dealer take was contained outside the 3Y. Classification: **yellow duration fatigue, not red auction dysfunction**.

## 5/20 20Y Read (post-print, ~2:55pm ET)

**Verdict: Soft-but-functional. Did NOT trigger orange escalation criteria.**

- BTC 2.55 — slightly soft (below 2.60 clean threshold) but well above 2.30 stress floor
- Indirect 67.7% — **rose** vs Apr 22 reopen (59.6%) and well above 58% clean threshold
- Dealer 9.4% — near Apr 22 baseline (8.6%); well below 12% watch level
- Tail: **0bp confirmed (ZH single-source, second-source pending).** WI 5.122% = high yield 5.122%, stopped on the screws. DGS20 5/18 was 5.14% → today priced ~2bp THROUGH prior CMT. Broke 11-of-12 stop-through streak but did NOT tail.
- **Context:** $16B new issue (not $13B reopen); larger size with strong foreign demand mix is a structurally clean print

**Read against §2 verdict matrix:** sits at the boundary of "clean" (row 1) and "soft but functional" (row 2). Only BTC is in row 2's band. Indirect, dealer, and tail are all in row 1. Tie-breaker rule ("worse of the two") would push to row 2 strictly, but mix is genuinely strong. **Net: yellow duration fatigue confirmed; demand-hole thesis weakened, not strengthened.**

**Implication for 5/21 10Y:** 5th consecutive 10Y is the live escalation gate. If 10Y prints with a tail, BND-07 "firming" persists but doesn't graduate to "FIRED" unless tail is sizeable. The 20Y showing foreign demand reduces base-rate expectation of a 10Y demand hole tomorrow.
