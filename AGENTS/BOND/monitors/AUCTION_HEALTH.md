# BOND Monitor — Treasury Auction Health

**Owner:** BOND
**Last Updated:** 2026-08-20 by BOND — **8/19 20Y and 8/20 30Y TIPS graded and added the same day they printed** (the 8/18 sweep's whole lesson: this table went 27 days stale twice and lost a $125B refunding). *(Prior: 2026-08-18 — full staleness sweep, Will-tasked.)*
**[8/18 entry retained]** — **full staleness sweep (Will-tasked).** ⚠️ **The rolling table was missing FOUR auctions, including the entire August quarterly refunding ($125B, the quarter's largest supply event).** The 7/28 7Y was graded the same day this file was last touched and never reached the table; 8/11–8/13 was never docketed at all. All four back-filled below off TreasuryDirect primaries, with per-tenor trailing-12 benchmarks recomputed 8/18. *(Prior: 2026-07-28 — rolling table 27 days stale, 6 auctions back-filled 7/09→7/27.)*
**Purpose:** Track whether Treasury market absorption is improving, mechanically supported, or deteriorating.

> ⚠️ **TWO STANDING RULES FOR THIS TABLE (adopted 2026-07-28):**
> **1. The `tail` column is UNSCOREABLE from primaries.** A tail requires the when-issued yield at bid deadline; **TreasuryDirect does not publish it** [verified 2026-07-28, **re-checked 2026-08-20** — **re-test: 2026-11-01**, or immediately if TreasuryDirect changes its published field set]. ⚠️ **SCOPE, sharpened 2026-08-20: this is a fact about THIS SOURCE, not about tails.** SAM computes a JGB tail at the MOF primary (lowest-accepted vs average-accepted) and that grade is legitimate — **do not export this retirement to another desk's instrument, and do not let anyone import it against one.** That is a structural limit, not a per-session gap — so **no gate, trigger or pre-registration may be keyed on a tail.** Wire-reported tails are `[med-conf]` and are recorded in Notes only, never used to fire a classification.
> **2. Grade COMPOSITION, not the headline cover.** All %s are **% of competitive accepted** (the fleet-reconciled denominator). A thin BTC with indirect holding and dealers un-stuffed is a *price* concession; a demand hole requires **indirect falling AND dealers absorbing.** The 7/27 5Y is the worked example: record-low cover, intact composition.

## Classification Rules

*Re-specified 2026-07-28 — **every row of this table previously keyed on a tail**, which contradicted the standing rules directly above it. Adding a banner without fixing the table it governs leaves the operative logic unchanged, so the table itself is rewritten on **composition**. Percentages are of **competitive accepted**; cut-offs are trailing-12 **per tenor** — the 7Y figures below are illustrative, re-derive per tenor.*

| State | Criteria (composition-keyed, tail-free) | Signal |
|---|---|---|
| 🟢 Healthy | BTC near/above trailing-12 median **and** indirect at/above median **and** dealer at/below median | No action |
| 🟡 Watch | BTC below trailing-12 median **or** indirect below median, with the other leg intact | Note in STATUS |
| 🟠 Cover marker | **BTC below the trailing-12 minimum while composition HOLDS** (indirect steady/rising, dealer not absorbing) | Fire the vector; **state explicitly that the mechanism did NOT fail.** Signal LIQUID/ZHAO if consequential. *(Worked example: 7/27 5Y.)* |
| 🔴 Composition failure = demand hole | **Indirect below the trailing-12 minimum AND dealer above the trailing-12 maximum**, i.e. foreign stepping away *while* dealers warehouse | Signal LIQUID, ZHAO, PROME **same-day**; this is the thesis-kill leg. |

> **Why the 🟠 and 🔴 rows are different in kind, not degree:** a thin cover is a *price* concession (someone still bought it, cheaper); a composition failure is a *mechanism* failure (the natural buyer left and the dealer ate it). Only the second one transmits to funding stress. Conflating them is the single most likely way this monitor gives a false alarm.

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
| 2026-07-28 | 7Y | $44B | 2.49 | 4.4730% | **70.15** | 16.88 | 12.97 | 🟢 | TreasuryDirect 91282CRC7 | **`BND-13` RESOLVED TRUE on frozen branch B — no composition failure.** BTC dead on its trailing-12 median (2.495); dealer BELOW the trailing-12 max (13.14). The 7/27 5Y cover marker did NOT extend to the back-belly. ⚠️ **Added 8/18 — this grade was completed 7/28 and never reached this table.** End-user take 87.03% vs 87.25% in June = flat, so the headline indirect surge overstates real demand. |
| **2026-08-11** | **3Y** | **$58B** | **2.71** | **4.2910%** | **64.24** | 24.02 | **11.74** | 🟢 | TreasuryDirect 91282CRG8 | **AUGUST REFUNDING leg 1.** BTC +0.07 vs trailing-12 median (2.64); indirect **+1.28pp** over median (62.96), well clear of the 53.99 min; dealer **below** median (12.11) and far below the 19.50 max. Healthy. |
| **2026-08-12** | **10Y** | **$42B** | **2.53** | **4.6830%** | **76.73** | 14.67 | **8.60** | 🟢 | TreasuryDirect 91282CRF0 | **AUGUST REFUNDING leg 2 — the strongest leg.** Indirect **+8.41pp** over its trailing-12 median (68.32) = **2nd-strongest of the trailing 12**, against a failure bar of 63.95. Dealer 8.60 vs median 9.96. **Foreign/custodial demand for the 10Y is not what broke.** |
| **2026-08-13** | **30Y** | **$25B** | **2.39** | **5.2160%** | **66.85** | 21.64 | **11.51** | 🟢 | TreasuryDirect 912810UW6 | **★ AUGUST REFUNDING leg 3 — THE FINDING. Cleared the HIGHEST 30Y AUCTION YIELD SINCE 2001 with indirect ABOVE its trailing-12 median (64.93) and dealers AT median (11.39).** Clears its own composition-failure bar (indirect <59.52) by **7.33pp**; dealer sits **5.95pp below** the 17.46 max. **The concession was paid in yield and the buyer base did not change — "expensive, not broken" at the hardest supply test of the quarter.** |
| **2026-08-19** | **20Y NEW** | **$16B** | **2.53** | **5.2040%** | **62.93** | 24.58 | **12.49** | 🟢 | TreasuryDirect 912810UX4 | **CLEAN on the frozen bars, SOFTEST composition of the run.** Indirect **−2.03pp vs its trailing-12 median** = the **first below-median long-end indirect since 7/9**; dealer above median. No failure (margins +7.76 / −5.10pp), no cover marker. HY **5.2040% = highest 20Y new-issue yield in the held series** (n=15, 2023-02→). **`BND-14` RESOLVED FALSE, −2.02pp — a real miss on a 60% call.** Priced INTO the sb0607 rally and BEFORE the 9/9 official bid exists ⇒ the **pre-op demand baseline**. |
| **2026-08-20** | **30Y TIPS reopening** (29Y-6M) | **$8B** | **2.82** | **2.9730%** (real) | **84.45** | 13.45 | **2.10** | 🟢 | TreasuryDirect 912810US5 | **★ STRONGEST OF THE 7 HELD 30Y TIPS ON ALL THREE LEGS.** Indirect **84.45 vs prior max 78.30** (+6.15pp) · BTC **2.82 vs prior max 2.78** · dealer **2.10 BELOW the prior MIN 2.49** — dealers took less than in any held auction of this instrument. Benchmarks trailing-7 SAME-TENOR SAME-TIPS (2023-02-16→2026-02-19, n=7): BTC med 2.48 · ind med **76.17** · dlr med 6.89. No composition failure (ind +14.01pp over the bar, dlr −7.77pp under), no cover marker. **`BND-17` RESOLVED TRUE, +8.28pp.** ⚠️ **Superlative scope: series 30Y TIPS · basis %-of-competitive-accepted · window 2023-02-16→2026-08-20 · n=8. 30Y TIPS predate 2023 — the earlier window is UNCHECKED, NOT unavailable. **`re-test: 2026-09-20`** — pull the full 30Y TIPS history from TreasuryDirect with an EXPLICIT date range (TA_WS caps at 250 rows and its date filter is inoperative, which is the actual reason the window is short); until then no claim wider than n=8.** The cleanest real-money referendum on the real-yield level available, taken with DFII10 at 2.41: real money did not balk. **14th straight benign resolution.** |

*June bills (6/15–6/18) all cleared clean — BTCs 2.47–3.12; 13W softest (2.47, pre-FOMC re-investment caution), 6W strongest (3.12). No bill stress.*

**Percentile context (PROME dataset v2, 369 rows 2023→5/28, refreshed 6/5):** late-May nominal coupons were **below-median to median on bid-to-cover** (2Y 28th, 5Y 24th, 7Y 50th pctile) — softer than the headline BTCs "look." But all cleared orderly with no tails/dysfunction and strong indirect. Read: **persistent duration fatigue / demand-at-a-discount, not dysfunction.** Note: the dataset's `tail_vs_cmt_bps` is a noisy prior-day-CMT proxy (e.g. -240bp for the 5/21 TIPS vs a nominal CMT is meaningless); rely on BTC percentiles + indirect mix, not that column.

## Per-tenor trailing-12 benchmarks (recomputed 2026-08-18 — RE-DERIVE AT EVERY GRADE)

**All percentages are of COMPETITIVE ACCEPTED.** These drift; the numbers below are a snapshot, not constants.

| Tenor | BTC med | BTC min | Indirect med | **Indirect MIN** | Dealer med | **Dealer MAX** | Window |
|---|--:|--:|--:|--:|--:|--:|---|
| 3Y | 2.64 | 2.53 | 62.96 | **53.99** | 12.11 | **19.50** | 2025-08-05 → 2026-07-07 |
| 7Y | — | — | — | **56.42** | — | **13.14** | (7/28 grade) |
| 10Y | 2.46 | 2.35 | 68.32 | **63.95** | 9.96 | **16.16** | 2025-08-06 → 2026-07-08 |
| 20Y | 2.67 | 2.36 | 64.95 | **55.17** | 9.88 | **17.59** | 2025-08-20 → 2026-07-22 |
| 30Y | 2.38 | 2.27 | 64.93 | **59.52** | 11.39 | **17.46** | 2025-08-07 → 2026-07-09 |
| 30Y TIPS | **2.48** | 2.38 | **76.17** | **70.44** | **6.89** | **9.87** | ⚠️ **RECONCILED 2026-08-20 to `grade_auction.py`: trailing-7 SAME-TENOR SAME-TIPS, 2023-02-16 → 2026-02-19, n=7.** Supersedes the 8/18 hand-derived **n=3** row (2.75 / 2.48 / 77.48 / 70.44 / 4.46 / 7.24) — a **method** difference (12-month calendar window vs trailing-7 auctions), not a data difference. **Re-derive from the tool, never from this row.** |

> ⚠️ **Composition failure = indirect below the tenor's own MIN _and_ dealer above its own MAX.** Never port one tenor's cut-offs to another: the 7Y's 56.42 indirect min against a 10Y auction (min 63.95) is simply the wrong bar. *(This exact error was live in `thesis/THESIS.md`'s kill criterion until 8/18 — it hardcoded the 7Y numbers as if general.)*
> ⚠️ **The 20Y's indirect MIN and dealer MAX come from THE SAME auction (2026-02-18: 55.17 / 17.59)**, so the 20Y failure test is calibrated to reproduce one historical print and fires only on a repeat of it or worse. **A narrow gate, named at authorship rather than after it fails to fire.**
> ⚠️ **The 30Y TIPS row cannot support a composition gate and none is set** — 3 observations spanning a year. Read that auction as a *level* referendum against DFII10. (`finding_base_rate_the_threshold_before_building_it`: "don't build it" is a real answer.)

## Upcoming (dates + instruments VERIFIED at the TreasuryDirect primary, 2026-08-18)

| Date | Instrument | CUSIP | Size | Failure test |
|---|---|---|--:|---|
| Tue 8/25 · Wed 8/26 · Thu 8/27 | 2Y · 5Y · 7Y | `91282CRH6` · `91282CRK9` · `91282CRJ2` | TBA | re-derive per tenor at grade time |

✅ **8/19 20Y and 8/20 30Y TIPS are BOTH GRADED — moved to the rolling table above (2026-08-20).** Next: the **8/25–27 2Y/5Y/7Y cluster**, which is also where the Will-ruled **MATRIX_V2** legs (§1 drop dealer-as-bearish · §3c indirect sufficient ALONE at the 15th per-tenor pctile) are adopted at pre-registration.

## ⚠️ TOOLING DEFECT — the reason this table went stale without anyone noticing

**`data/auction_history_*.csv` (370 rows) is stale to 2026-05-28** and carries three defects reported by DAEDALUS 2026-08-17 (`sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md`), which is why no automated surface flagged the missing August refunding:

1. **Unstamped, unbounded CMT fallback** — `_cmt_for` serves the most-recent-prior close with no lookback bound and **records no date**, so a same-day close and a 90-day-old close write byte-identical `tail_vs_cmt_bps` cells. *(That column is keyed to the auction-tail metric this monitor formally RETIRED on 7/28 as unscoreable — so it should arguably be dropped, not fixed.)*
2. **Documented-and-unguarded empty-200** — the file's own docstring warns that a bad `fields=` projection returns HTTP 200 with zero rows, and the code has no guard: `out.to_csv` **overwrites v1 with an empty file BEFORE validation.** Data destroyed, then a confusing traceback.
3. **429 path** — 4×429 on FRED exits the retry loop without `break` ⇒ `obs=[]` ⇒ an all-null column written at **rc=0**.

**⛔ DO NOT RUN THE REFRESH SCRIPT UNTIL (2) IS FIXED — it can destroy the corpus it is meant to extend.** Fix order: write-to-`.tmp` + validate row count and required columns + `os.replace`; then nonzero rc on the 429-exhausted path; then either stamp `cmt_asof` or drop the tail columns outright. **This corpus is also the blocker on the v1.1.4 spec changes (a)/(b)/(c), which cannot be base-rated without it** — see `thesis/THESIS.md` §ADOPTION NOTE.

*(For balance, DAEDALUS rates `monitors/fr2004_fetch.py` near-exemplary — one gap: its `!! STALE` banner is stderr-only at rc=0, so a stdout-capture path keeps the confident table and loses the warning.)*


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
