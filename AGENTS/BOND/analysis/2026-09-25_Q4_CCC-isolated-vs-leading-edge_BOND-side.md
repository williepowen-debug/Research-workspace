# Q4 · Is CCC weakness isolated, or the leading edge of broad repricing? · BOND's side (dealer inventory + sovereign/real-yield driver)

**Packet:** `inbox/2026-09-25_from-PROME_will-directed-six-questions-BOND.md` (`c29e4ca60`; Will 02:55 ET; DOCKET L477, needed by Sat 9/26). **Lead: LIQUID** (`AGENTS/LIQUID/reports/2026-09-25_Q4_ccc-isolated-vs-leading-edge.md`). **Deconflicted 9/25 ~03:2x:** LIQUID owns the ICE tier structure — **cite LIQUID's tier figures; BOND publishes none**. BOND covers (1) dealer inventory and (2) the sovereign/real-yield driver, plus what the fleet holds on issuance. Existing gates only; no new thresholds; no trade. Reproducible: `analysis/2026-09-25_Q4_tier_and_dealer_pull.py`.

> **One caveat, stated once:** the ICE BofA indices on FRED carry a **rolling ~3-year history** (common span here 2023-09-25 → 9/23, n=786). Every percentile below involving ICE spreads describes **that window only**. It contains no 2020 or 2022 stress, so "a 3-year extreme" is not "a cycle extreme".

## 1 · Dealer inventory — FR2004 below-investment-grade corporate bonds (NY Fed pd API `PDPOSCSBND-BEL*`, net outright, $B)
| As-of | Total below-IG | ≤13m | 13m–5y | 5–10y | >10y |
|---|---:|---:|---:|---:|---:|
| 8/26 | −0.01 | 1.51 | 0.03 | −2.21 | 0.66 |
| 9/02 | 2.20 | 1.65 | 1.13 | −1.43 | 0.84 |
| 9/09 | 2.14 | 1.67 | 1.30 | −1.61 | 0.79 |
| **9/16** | **2.91** | 1.70 | **1.83** | −1.28 | 0.67 |

**Read:** dealers added **+$2.2B** of below-IG bonds in the four weeks to 9/16. That's the **96th percentile of 4-week changes** since 2022-01 (n=242). **The level ($2.9B) is ordinary**, at the 65th percentile (median $2.4B, max $5.7B). Almost all of the build is in **13 months–5 years** (+$1.8B since 8/26); the longer buckets are flat to short.
**Limits:** FR2004 does not split HY by rating, so this is **all** below-IG, not CCC. It's net (long − short), and CDX hedges don't show. It publishes weekly with an 8-day lag, so the latest data is **as-of 9/16**.

## 2 · Sovereign / real-yield driver — is the UST real-rate shock reaching all tiers, or only CCC?
10Y real yield (DFII10) **2.85% [9/24, U.S. Treasury real curve] — highest since 2008-11-24.** Measure: sensitivity (beta) of each tier's daily OAS change to the daily DFII10 change, in bp per bp, over the latest 20 sessions to 9/23, set against all 728 rolling 20-session windows in the ICE span:

| Tier | Latest 20-session beta | Percentile vs all rolling windows | Window p10 / median / p90 |
|---|---:|---:|---|
| CCC | **+0.56** | **81st** | −1.57 / −0.20 / +0.95 |
| B | +0.03 | 64th | −1.15 / −0.16 / +0.49 |
| BB | −0.11 | 66th | −0.99 / −0.25 / +0.27 |
| IG | −0.04 | 52nd | −0.19 / −0.05 / +0.06 |

**Read:** on real-yield-up days lately, **only CCC has widened**. The stronger tiers sit near their usual slightly-negative sensitivity (spreads normally *tighten* a little on rising-real-yield growth days). **This is weak evidence:** CCC at the 81st percentile is elevated, not extreme, and a 20-session beta is noisy. It **leans toward (A)**: a refinancing-cost squeeze that binds only on the weakest balance sheets while real yields sit at 2008 levels. It doesn't prove it.

## 3 · Issuance / refinancing data on the fleet
**Pulled deals: ZERO as of 9/17** (`monitors/CREDIT_PRIMARY_MARKET.md`, BOND; refreshed to the 9/15 close; **8 days old**). **HY new-issue volume and the CCC maturity/refinancing wall are NOT held at primary anywhere on the fleet.** IG volume exists only as a secondary poll (~$215B September, Bloomberg via 9/3). ⇒ **GAP**, named: no fleet observable can test the "refinancing wall" story directly.

## 4 · The two explanations, side by side (BOND's evidence only; tier evidence = LIQUID's)
| | **(A) Weakest borrowers only** (idiosyncratic / refinancing wall) | **(B) Leading edge of broad repricing** |
|---|---|---|
| **Supports it TODAY** | Only CCC responds to the real-rate shock (beta +0.56 vs B +0.03, BB −0.11, IG −0.04; §2). Dealer build is in **short HY paper** (13m–5y), consistent with dealers making markets in near-maturity/distressed names rather than absorbing broad duration selling. Primary access open (zero pulled deals, 9/17) | Dealers took a **96th-percentile** 4-week build of below-IG paper (§1): someone is selling HY into dealer balance sheets. The real-rate backdrop (DFII10 2.85, a 2008-level) is common to every tier, so the mechanism exists for all of them |
| **Discriminating observable (BOND side) · date** | **FR2004 as-of 9/23 (Thu 10/1 ~16:15 ET) and 9/30 (Thu 10/8):** the below-IG build **stalls or reverses**, and stays in ≤5y buckets | Same prints: the build **continues** (another positive 4-week change) **and spreads into 5–10y / >10y** |
| | **B-tier real-yield beta stays near its median** (−0.16) through the **10/14 CPI** window | **B-tier beta moves into its own upper decile** (≥ its window p90, +0.49), i.e. the real-rate shock starts reaching B, by **10/28 FOMC** |
| | Zero pulled HY deals through the refreshed check (BOND, next session) | **A pulled/postponed HY deal** before 10/14 |
| **Tier leg (LIQUID's, cited)** | Current episode: 37 sessions since 8/03 without B following (LIQUID) | B reaches its 15-session p90 (+28bp) — historically within 2–13 sessions, with BB/BBB/IG the same day in 6 of 7 (LIQUID) |

**BOND's net read:** today's dealer and sovereign evidence **leans (A) on the mechanism** (only CCC is rate-sensitive) and carries **one (B)-consistent warning** (an unusually fast dealer build in HY). The Thu 10/1 FR2004 print is the first dated test that can separate them from BOND's side. **None of this changes a BOND gate:** CCC 1100 (`BND-27`, resolves on the 9/30 cell), HY 300, and the credit-equity lead (HY +75–100 from 263) are unchanged.

**Consistency with LIQUID:** BOND's figures don't contradict LIQUID's. The dealer build and the "only CCC is rate-sensitive" read are both new, BOND-side, and complement LIQUID's tier paths. **Positions: none; no trade.**
