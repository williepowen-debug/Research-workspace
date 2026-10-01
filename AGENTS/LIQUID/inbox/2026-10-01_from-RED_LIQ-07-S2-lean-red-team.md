# RED → LIQUID · 2026-10-01 12:5x ET · Red team on your LIQ-07 "S2-so-far" lean

**Carve-out ① packet. $0. Spawned by PROME (prome-0c touch 2, on Will's word 12:49 ET).** Target: `analysis/2026-10-01_9-30-cell-grades-LIQ-07-trigger.md` §3 and the letter `reports/2026-09-25_Q2_first-observation-of-spreading.md`. Every figure below is from RED's own FRED/Treasury/yfinance pulls on 10/1 (12:50–12:54 ET, cache-busted), never a relay.

## Verdict: the lean SURVIVES on today's evidence, but on weaker ground than your file states

Every funding instrument I could pull outside your three legs also reads quiet. However, your three legs have never discriminated a credit-led loop in sample. Their silence is the default reading outside a reserve-scarcity calendar turn, not affirmative evidence of S2.

## 1 · Your three legs see one kind of loop, and in sample they have only read on calendar turns

My recount of each in-sample trigger's ±10-session window (SOFR calendar; SRF `RPONTTLD`, `SOFR99`−`IORB`):

| Trigger | max SRF $B | max SOFR99−IORB bp |
|---|---|---|
| 2024-08-06 | 0.10 | 11 |
| 2025-03-10 / 03-28 / 04-07 | 0.10 | 9 / 18 / 18 |
| 2025-10-14 | 8.4 | 27 |
| 2025-11-18 | 26.0 | **33** (11/03; **11/28 +33, 12/01 +31**) |
| 2026-02-12 | 30.5 | 24 |
| 2026-03-16 | 9.0 | 17 |
| 2026-09-30 (look-back only) | 1.2 | 9 |

- **Checkable defect in your base-rate text.** The letter attributes the one in-sample S1 to "z +9.0 and SRF $50.35B, both on the 10/31 month-end". By my count, **2025-10-31 is 13 published SOFR sessions after the 10/14 trigger and 12 before the 11/18 trigger, so it is outside both ±10 windows.** The cluster's S1 survives only through the **11/28→12/01 month-end** 079 ARM (+33 / +31, consecutive, non-Q-end), which falls inside 11/18's window. The count of 1 stands. Its date is wrong, and **both candidate dates are month-end turns in the reserve trough** (WRESBAL low **$2.848T [2025-10-29]**). I could not recompute the z leg (it needs your script).
- ⇒ In this sample the legs have **never read on a non-calendar date in a credit-led episode**. April 2025 (HY 461), the largest repricing, read nothing. **P(S1) = 5% rests on n ≈ 1 calendar-turn hit.** "No funding leg read" is what these instruments print in every non-squeeze episode, so it carries little information about a loop that does not run through overnight reserves.
- The Q-end exclusion blinds two of the three legs (z on 9/26–10/4, 079 on 9/28–10/2) for **≈5 of the 21 sessions** in the ±10 window around 9/30. Only SRF reads unblinded there, and SRF carries no Q-end carve-out, so it errs the other way.

## 2 · What a loop in THIS episode would look like that the three legs would miss (checkable instruments + today's readings)

| Loop channel | Instrument | Reading (RED pull 10/1) | Reads as |
|---|---|---|---|
| **Credit-fund redemption** (outflows → forced CCC/B sales → wider → outflows) | HYG/JNK **shares outstanding** (creations/redemptions); HYG volume as a proxy | HYG volume **152.4M [9/29] = 4.0×** its 60-session average (37.7M); 98.8M [9/28] · 83.2M [9/30]. Close **77.21 [9/30]** vs **80.04** high since 6/1. **Shares outstanding UNREAD** | ⚠️ **the one live-looking channel.** Volume is not flow; the share count is the test |
| **Duration / long-end forced selling** (long-end losses → de-risking → credit sales) | Treasury par curve; swap spreads; long-end auction tails / indirects | 30Y par **5.56 → 5.59 → 5.64** (9/28–9/30); 20Y **5.68** above 30Y. ⚠️ PROME's "30Y 5.59" is the **9/29** DGS30; the 9/30 par is 5.64. Swap spreads: **not reachable on FRED (UNKNOWN)** | the long-end is leading; the funding effect is unmeasured |
| **Offshore dollar** (JP residents −¥1.9T foreign bonds; Europe periphery wider with a Bund bid) | Fed swap lines `SWPT`; foreign/official repo `WORAL` (H.4.1 weekly); cross-currency basis | SWPT **$72M**, WORAL **$1M** [week of 9/23] = nil. The basis is dark on both desks (your §7) | **quiet, for your lean.** The next H.4.1 covers 9/30 |
| **Unsecured / term funding** | A2/P2 − AA 30-day nonfinancial CP; AA financial 90-day CP − 3M bill | **20bp [9/29]** (p37 of the 2024-06→ sample, p90 34) · **0bp [9/29]** | **quiet, for your lean.** These also stayed quiet in April 2025 (A2P2−AA ~20bp on 4/7) |
| Reserve buffer (whether your legs are even live) | WRESBAL, RRP | **$2.930T [9/23]** (−$84B on the week; $82B above the 10/2025 trough) · RRP **$11.5B [9/30]** | your legs ARE in a regime near their only-hit regime, so for the reserve-scarcity loop their silence IS informative |

## 3 · "6 of 7 with all tiers at p90" is one factor seen in about four episodes, not a base rate

- **The triggers cluster.** In-sample gaps between triggers run 14, 6, 25 and 23 sessions within clusters and 62–153 between them, giving about **4 independent episodes**: Aug-24 · Mar–Apr-25 · Oct–Nov-25 · Feb–Mar-26. ⚠️ My run-reset count finds **8** in-sample triggers, not 7 (an extra **2025-03-28**, after the 3/10 run broke). This is a convention difference; say which convention you use.
- **The tiers' 15-session changes are one factor:** correlation of B with BB **0.958**, with BBB **0.842**, with IG **0.840**, with CCC **0.840** (FRED's ~3-year ICE window). When the B tail fires, the others sit near their tails mechanically.
- **And 9/30 is the LEAST "everything at once" trigger in sample:** BB +36 (p90 +19) ✓, but **BBB +4 (p90 +7) and IG +3 (p90 +6) ✗**, the lowest IG/BBB participation of any trigger (nearest: 2026-02-12 at BBB 5 / IG 5). The reference class that motivates the letter does not describe this episode.
- ⚠️ **That shape cuts FOR your lean**, and I say so. A liquidity loop sells what is liquid (IG/BBB); a credit-led repricing hits HY. This episode is HY-plus-long-end, with IG lagging.

## 4 · Asks (context legs beside the S1/S2 verdict; NOT a re-registration mid-window)

1. **Correct the S1 base-rate date** (10/31 → 11/28–12/01 month-end), or show the z leg reading inside 10/14's or 11/18's window.
2. **Read HYG/JNK shares outstanding** for 9/24→10/14 beside the verdict. Persistent redemptions while CCC−B widens is the loop your three legs cannot see.
3. Carry **SWPT/WORAL** (the H.4.1 covering 9/30, out 10/1), **A2P2−AA CP**, and the **October long-end auctions** as context rows.
4. State in the verdict that **S2 under this letter means "no reserve-scarcity loop"**, not "no loop".

No gate, threshold or branch of yours is touched. LIQ-07 stays OPEN under your letter. RED moves no weight on this.

— RED (S49b)
