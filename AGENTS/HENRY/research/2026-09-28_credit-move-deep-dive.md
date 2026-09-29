# Credit move deep dive — 9/22 → 9/25 (Will-directed, 2026-09-28 evening)

**Basis:** FRED ICE BofA OAS series, obs through **2026-09-25** (the 9/28 cell posts ~9/29). Percentiles are over FRED's available window **2023-09-29 → 2026-09-25** (n≈785) — a 3-year window, not all history. Pulled 2026-09-28 ~20:50 EDT.

## 1. The ladder
| Tier | 9/25 | 1-day | since 9/22 | 20d | 3mo | 2026 range | 3y pct |
|---|---|---|---|---|---|---|---|
| IG | 81 | +2 | +4 | +2 | +5 | 73–94 | 31 |
| BBB | 99 | +2 | +4 | +2 | +4 | 92–116 | 19 |
| BB | 176 | +12 | +20 | +26 | +12 | 150–222 | 36 |
| B | 300 | +14 | +29 | +28 | +1 | 270–377 | 42 |
| **CCC** | **1,128** | +16 | +53 | +102 | **+158** | 838–1,128 | **~100** |
| HY | 293 | +13 | +25 | +33 | +18 | 260–346 | 42 |
| HY all-in yield | 7.87% | +7 | +39 | +85 | +88 | 6.43–7.87% | 90 |
| CCC all-in yield | 16.14% | +10 | +66 | +152 | +224 | 12.02–16.14% | ~100 |

## 2. Two processes, superimposed
- **Slow (3 months): the tail only.** CCC +158 while BB +12 and B +1. This is the K-shape the desk has tracked since June — the weakest borrowers repricing alone.
- **Fast (3 sessions, 9/22→9/25): broad.** HY +25 = **97th pct** of 3-session moves in the window; BB +20 = 96.8th. **In PERCENT of starting spread, the quality tiers moved MORE than CCC** (BB +12.8% · B +10.7% · CCC +4.9%). LIQUID graded 9/24 and 9/25 **BROADENS**, BB-led, and withdrew its "isolated CCC" lean.
- **Investment grade did not follow:** IG +4 / BBB +4 since 9/22, at the 31st / 19th pct. No systemic signature.

## 3. Is it just the rate move? No — the biggest day decoupled
| Day | HY | BB | CCC | 10Y | SPX |
|---|---|---|---|---|---|
| 9/23 | +5 | +3 | +18 | +15 | −0.75% |
| 9/24 | +7 | +5 | +19 | +7 | −0.02% |
| **9/25** | **+13** | **+12** | +16 | **−1** | **+0.51%** |

**The largest widening came on the day Treasury yields FELL and stocks ROSE.** That is the credit-leads-equity pattern (H4), not rates-beta. Candidate drivers — **none adjudicated:** (a) supply: SoftBank ~$10–11B priced 9/23–24, Paramount ~$44B marketed this week (BOND: primary access OPEN for large credits — a supply-indigestion read, not a closed-market read); (b) AI-agent ("Muse") disruption hitting cable/subscription credits, where CCC damage is reported concentrated (newsletter, Bloomberg basis, not verified); (c) AI-financing names (ORCL CDS reported at a record, SECONDARY). ⛔ No pulled HY deal is verified (BOND `KB-BND-346`).

## 4. Where the move sits vs the March 2026 episode
| | HY | BB | B | CCC |
|---|---|---|---|---|
| 3/30 (2026 peak) | 346 | 222 | 377 | 1,020 |
| **9/25** | 293 | 176 | 300 | **1,128** |

The index is **53bp below** March's peak; the tail is **108bp above** it. **This is a different animal from March: less broad, deeper at the bottom.**

## 5. What it means for borrowers
Spreads for BB/B are only mid-range (36th–42nd pct), but **all-in junk yields are at the top of the window** (HY 7.87%, 90th pct; CCC 16.14%, the max) because the Treasury base rose underneath them. **The refinancing bill is set by the yield, not the spread** — BOND: the CCC refi wall is real but narrow (index-level exposure small).

## 6. Rules touched (counts are the owners')
- HENRY CCC >1,100 red: 🔴 through (9/24, 9/25).
- RED-FT-01 (HY ≥280 ×3): 2 of 3 — the 9/28 cell decides (RED's).
- LIQUID X1: CLOSED since 8/28, no capital path. LIQUID >320 confirmation: 27bp away. BB >220 (AI-credit funded leg): 44bp away. IG >94: 13bp away.
- BOND row 4: HY >300 with velocity — 7bp short, velocity leg present.
- Twin soft-kill / `GATE-HY-REKILL` (<260): 33bp away and moving away.

## 7. What would tell us which way it goes (existing gates only)
- **Transmission:** B ≥305/304/308 on 9/28/9/29/9/30 (LIQUID LIQ-07/D1) · HY >300 with velocity (BOND) · HY >320 (LIQUID confirmation) · IG >94 (LIQ-072).
- **Against transmission:** HY back under 280 while CCC holds ⇒ the fast broad leg was supply/rates noise and the slow tail story resumes alone.
- **Funding:** clean on every gauge LIQUID observes (SOFR99−IORB +5bp [9/23], 25bp under its ARM line). A credit move without funding stress is repricing, not a spiral — so far.

## Caveats
- ICE basis only; Bloomberg-basis press figures (CCC 968) are a different index.
- HY-ETF flow proxy returned NaN (vendor gap) — flows are **unmeasured**, not flat.
- Energy HY OAS is permanently unmeasured (LIQUID CANNOT-FIRE declaration 9/26).
- One-day decoupling (9/25) is n=1; the 9/28 cell (~9/29) is the next test.
