# BOND Monitor — Treasury Auction Health

**Owner:** BOND
**Last Updated:** 2026-07-28 by BOND *(rolling table had gone 27 days stale — 6 auctions back-filled 7/09→7/27)*
**Purpose:** Track whether Treasury market absorption is improving, mechanically supported, or deteriorating.

> ⚠️ **TWO STANDING RULES FOR THIS TABLE (adopted 2026-07-28):**
> **1. The `tail` column is UNSCOREABLE from primaries.** A tail requires the when-issued yield at bid deadline; **TreasuryDirect does not publish it.** That is a structural limit, not a per-session gap — so **no gate, trigger or pre-registration may be keyed on a tail.** Wire-reported tails are `[med-conf]` and are recorded in Notes only, never used to fire a classification.
> **2. Grade COMPOSITION, not the headline cover.** All %s are **% of competitive accepted** (the fleet-reconciled denominator). A thin BTC with indirect holding and dealers un-stuffed is a *price* concession; a demand hole requires **indirect falling AND dealers absorbing.** The 7/27 5Y is the worked example: record-low cover, intact composition.

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
| 2026-06-23 | 2Y | $69B | 2.64 | 4.189% | **55.45** | 34.31 | 10.24 | 🟡 | TreasuryDirect 91282CQY0 | **0.3bp STOP-THROUGH** (biggest since Jan, ZH sec.); HY highest since Jan-2025; indirect <60 but directs absorbed; dealer take lowest since Feb. |
| 2026-06-24 | 5Y | $70B | 2.35 | 4.200% | 61.60 | 25.51 | 12.89 | 🟡 | TreasuryDirect 91282CQX2 | **0.7bp tail = 8th consecutive tailing 5Y** (ZH sec., internals cross-check primary). Indirect −13.3pp m/m (74.85→61.60, lowest since Jan) — directs +13.2pp absorbed ~1:1. |
| 2026-06-25 | 7Y | $44B | 2.50 | 4.260% | **57.55** | 29.70 | 12.75 | 🟡 | TreasuryDirect 91282CQW4 | Indirect −20.8pp m/m (78.39→57.55) — directs +18.5pp absorbed. **Tail UNPINNABLE** (no primary WI; no named secondary) — treat as unknown, not "no tail". |
| 2026-07-09 | 30Y reopening | $22B | 2.44 | 5.058% | **77.74** | 12.21 | 10.05 | 🟢 | TreasuryDirect 912810UU0 | **BND-11 resolved NOT FIRED.** Indirect SURGED (vs June 59.95) — the *inverse* of the masked demand-hole; dealers un-stuffed. Record clearing yield WITHOUT demand failure. |
| 2026-07-22 | 20Y reopening | $12.9B | 2.64 | 5.163% | **69.12** | 16.21 | 14.67 | 🟡 | TreasuryDirect R_20260722_2 | HOLDING. Indirect firm rules out foreign-exit; **dealer 14.67% is the one soft spot** (vs 8.4% June) — logged as a slow-burn tilt to watch, not a trigger. |
| 2026-07-23 | 10Y TIPS (new) | $23.3B | 2.30 | 2.438% (real) | **65.16** | 24.98 | 9.86 | 🟡 | TreasuryDirect R_20260723_3 | BTC at the softening boundary but composition strong: cleared **+26.9bp above 5/21** with ind/dealer 6.6x (vs 5.5x) = **real money buying a higher real yield with LESS dealer help.** |
| 2026-07-27 | 2Y | $69B | **2.66** | 4.3150% | 56.59 | 34.05 | **9.36** | 🟢 | TreasuryDirect 91282CRB9 | STRONG. BTC highest since Jan-26; dealer lowest since Jan; indirect UP vs June (55.45). |
| **2026-07-27** | **5Y** | **$70B** | **2.28** | **4.4080%** | **59.24** | 27.22 | 13.53 | 🟠 | TreasuryDirect 91282CRA1 | **★ FIRST REAL COVER MARKER OF THE CYCLE — lowest 5Y BTC since 2022-09-27 (2.27), by 0.01, in a 50-auction window.** Fires the `BTC<2.3` leg ⇒ vector 2→3. **But composition HELD: indirect ROSE with duration on the day (2Y 56.59 → 5Y 59.24)**, the opposite of a duration-demand step-back; dealer +0.64pp only. Concession is in PRICE (+20.8bp vs June). Threshold fired, mechanism intact. **"14th consecutive tail" (wire) NOT carried — unverifiable.** |

*June bills (6/15–6/18) all cleared clean — BTCs 2.47–3.12; 13W softest (2.47, pre-FOMC re-investment caution), 6W strongest (3.12). No bill stress.*

**Percentile context (PROME dataset v2, 369 rows 2023→5/28, refreshed 6/5):** late-May nominal coupons were **below-median to median on bid-to-cover** (2Y 28th, 5Y 24th, 7Y 50th pctile) — softer than the headline BTCs "look." But all cleared orderly with no tails/dysfunction and strong indirect. Read: **persistent duration fatigue / demand-at-a-discount, not dysfunction.** Note: the dataset's `tail_vs_cmt_bps` is a noisy prior-day-CMT proxy (e.g. -240bp for the 5/21 TIPS vs a nominal CMT is meaningless); rely on BTC percentiles + indirect mix, not that column.

## Open Questions

- ✅ **RESOLVED:** Does 10Y >4.5 / 30Y >5 persist for multiple sessions? **YES** — 30Y >5.0 for ~9 sessions (5/14-5/27), 10Y >4.5 for 6 (5/15-5/22). BND-07 TRUE. But both have since mean-reverted (10Y 4.47, 30Y 4.97 by 6/4) — durable episode, not a one-way break. *(Live again: 30Y 4.97 on 7/1 — BND-12 tests the July repeat.)*
- Does weak-but-not-failed auction demand begin funding through LIQUID plumbing (SOFR-IORB positive, repo pressure)? **No evidence** — SOFR-IORB printed **+3bp on 6/30** but that was clean quarter-end (SRF take-up $0 at both ops, RRP one-day $26.9B blip); watch normalization 7/1-7/2.
- Does foreign official demand deterioration confirm auction-level softness? **Evidence turned 7/1** — June-cluster indirects fell <60 at 2Y (55.45) and 7Y (57.55), with violent m/m slides (5Y −13.3pp, 7Y −20.8pp); composes with TIC-April private outflow (KB-049) + UST allocation multi-decade low (KB-057). **Counterweight: directs absorbed ~1:1 — rotation, not hole.** VX-13 → 3.

## 6/23–25 Cluster Read (RESOLVED — grade C+)

**No hard stress marker** (BND-11's predicates all clear): BTCs 2.64/2.35/2.50 (none <2.3), tails ≤0.7bp where measurable (2Y stop-through 0.3bp; 7Y unknown), dealer takes 10.2–12.9% low-normal. **The story is composition:** indirect <60% at two of three tenors with 13–21pp m/m slides, absorbed almost exactly by direct bidders — foreign/custodial fade rotating to domestic funds at market prices. Demand **rotation**, not demand hole; a ZHAO-thread datapoint, not a LIQUID-grade event. The 5Y's 8th consecutive tail (0.7bp) = chronic mild belly concession — mechanism note. **Next live gate: 7/7–9 mini-refunding (3Y/10Y-R/30Y-R), the 7/9 30Y heaviest — BND-11 pre-registered (70% benign), into a 30Y ~4.97 tape with record dealer inventory.**

## June Refunding + 20Y/TIPS Read (6/9–6/18, RESOLVED)

All cleared — **no stress markers**. The 6/10 10Y reopening was the standout (BTC 2.57, indirect 78.2%, dealer 9.5% — broke the 5th-consecutive-10Y-tail fear); the 6/11 30Y was soft-but-orderly (BTC 2.33 held >2.3, indirect 59.84%, no outlier repeat of the 5/13 11th-pctile print); the **6/16 20Y reopening printed STRONG** (BTC 2.75 — best in 3mo, ~-1bp stop-through, indirect 71.6%), resolving **BND-09 FALSE**; the 6/18 5Y TIPS was solid (BTC 2.61, real 1.955%). The into-gate hawkish FOMC did NOT translate to auction stress. *(The 6/23–25 cluster subsequently resolved C+/no-marker — see section above.)*

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

**Implication for 5/21 10Y** *(frozen May-2026 note — "tomorrow" meant 5/21; retained for the reasoning, NOT current)*: 5th consecutive 10Y was the live escalation gate. If the 10Y printed with a tail, BND-07 "firming" persists but doesn't graduate to "FIRED" unless the tail is sizeable. The 20Y showing foreign demand reduced the base-rate expectation of a 10Y demand hole.

> **⚠️ Note added 2026-07-28:** the reasoning above is superseded in one respect — **it keys the escalation on a TAIL.** Per the standing rules at the top of this file, a tail is unscoreable from TreasuryDirect and **no gate may be keyed on one.** The current-era equivalent of this note is a *composition* gate (indirect AND dealer), not a tail gate. Kept as history so the change in method is visible rather than silently overwritten.
