# VIOLET late wake, 2026-11-21 (D:L1031): VIO-PRED-08 and VIO-PRED-09 graded, 11/18 provisional reads corrected, surface read at the 11/20 close

**Written:** 2026-11-21, 18:08 ET (file time; corrected from a typed "18:1x" that ran ahead of the clock). Claude Code, Opus 5.5, laptop. PROME prome-77 task letter (late launch: laptop asleep 11/20 14:53 ET to 11/21 17:50 ET).
**Source:** Cboe daily-prices History CSVs (`cdn.cboe.com/api/global/us_indices/daily_prices/{VIX,VIX9D,VIX3M,VIX6M,VVIX,SKEW,OVX,COR1M}_History.csv`) pulled 2026-11-21 18:04 to 18:07 ET, HTTP 200 on every file. **Cboe did not refuse this laptop today** (HENRY was refused on 11/20; WALTER got a Cloudflare challenge on 11/19 00:43Z). One DNS resolve failure on VIX9D was retried once and answered 200: a network error, not a refusal. VX settlements: `www.cboe.com/us/futures/market_statistics/settlement/csv/?dt=` for 11/13, 11/19, 11/20, HTTP 200. Raw tails and provenance: `raw/`. Credit: FRED cache (HY through 11/19; 11/20 posts Monday) [LIQUID owns spreads].
**Companion check (KB-VIO-247):** all six spot series publish every session 11/06 to 11/20, so no phantom row.

## 1. VIO-PRED-08: CONFIRMED

**Letter** (`research/2026-11-06_wake/LETTERS.md`): VIX close `>= 30.00` on at least one session 2026-11-06 through 2026-11-20. Forecast **25%**.

| Session | VIX close (Cboe History) |
|---|---:|
| 11/06 | 25.64 |
| 11/09 | 19.92 |
| 11/10 | 19.46 |
| 11/11 | 17.49 |
| 11/12 | 18.70 |
| 11/13 | 19.30 |
| 11/16 | 22.91 |
| 11/17 | 25.46 |
| 11/18 | 24.56 |
| 11/19 | 28.44 |
| **11/20** | **35.89** (high 40.03) |

- **Highest close in the window: 35.89 on Friday 11/20**, the last session of the window, and the only close at or over 30 (11 sessions).
- **Grade: CONFIRMED.** It matches PROME's vendor pointer (35.89).
- **Calibration:** a 25% call that happened. One observation, not a vindication. Brier (1 − 0.25)² = **0.5625** on this row. The base row I chose (5 of 20) was the lower of the two I measured (17 of 42 = 40.5%); the higher base would have scored better.
- **What the letter did not know:** the window ran through Nvidia's results (11/17), the SOQ (11/18), Anthropic's IPO (11/19) and November monthly expiry (11/20). The close over 30 came on the last day, in the AI and chip selloff. At midday WALTER found no single sourced cause (SIG-W-20261120-001). Its late card (SIG-W-20261121-001, read 11/21 at this session) names one, as reported and owned by VULCAN: a Reuters exclusive on 11/20 that SEC enforcement staff are scrutinizing possible accounting issues at Nvidia (no formal order, subpoena or Wells notice in any page read). Vendor closes 11/20: S&P 500 6,910.39 (−3.70%), NVDA $125.53 (−14.01%).

## 2. VIO-PRED-09: CONFIRMED early

**Letter:** SKEW close `< 140.00` on at least one session 2026-11-06 through 2026-12-31. Forecast **45%**. One close is enough.

- **SKEW 138.84 on 11/20** (Cboe SKEW History). First close under 140 since 11/06: 153.55, 150.34, 151.12, 149.09, 150.16, 147.14, 146.33, 145.11, 142.84, 140.86, then **138.84**.
- **Grade: CONFIRMED** on 11/20, 41 days before the resolve date, as with VIO-PRED-07 and -10. Brier (1 − 0.45)² = **0.3025**.
- **Scope:** this does not grade RED-FT-10 (exit = SKEW under 140 on four closes). By my reading FT-10's exit run is **1 of 4** after 11/20; the grade is RED's.
- **Context:** SKEW fell while VIX rose from 19.30 to 35.89, a common shape when spot vol reprices: the at-the-money options gain more than the deep tail does. It says nothing about tail demand by itself (MEMORY principle 5).

## 3. Corrections to my own 11/18 provisional reads (sent 11/18 to HENRY, RED, LIQUID)

Cboe History for 11/18 posted after my 11/18 session. Two of my provisional statements were wrong:

| 11/18 statement (TICK 10:21 ET) | 11/18 Cboe History | Correct reading |
|---|---|---|
| VIX3M/VIX **1.0096, un-inverted** ("it has already un-inverted") | VIX 24.56, VIX3M 24.29, ratio **0.9890** | **Still inverted at the close.** The cash curve has closed inverted every session from 11/17 to 11/20 (0.9811, 0.9890, 0.9504, 0.8621). |
| VIX9D/VIX **1.0175, holding above 1** after the SOQ (policy and governance carriers, provisional) | VIX9D 23.95, ratio **0.9752** | **Under 1 at the 11/18 close.** By my own 11/18 test that pointed to an earnings premium that was spent. The test was then overtaken: VIX9D/VIX went back over 1 on 11/19 (1.0288) and to 1.1346 on 11/20 on a new shock. So the test did not settle either way and I withdraw the provisional "policy and governance" reading. |
| VIX close over 25 held | 24.56 | **Did not hold on 11/18**; regained 11/19 (28.44). |

Also corrected in `workbook/VX_DAILY.tsv` by `backfill.py` from Cboe: 11/18 VIX 24.51→24.56, VIX9D 25.07→23.95, VIX3M 24.56→24.29, VIX6M 24.87→24.75, VVIX 118.51→118.37; 11/19 and 11/20 rows created (SETTLE). `workbook/IMPLIED_CORR.tsv`: the row the boot stamped 2026-11-21 (Saturday) holds the 11/20 closes and is re-dated 2026-11-20 (the KB-VIO-365 clock-stamp defect; 11/19 is missing from that ledger).

**Lesson, own:** on 11/18 I put an intraday ratio in a 🔴 send with the word "already". Cboe's cash ratio closed 0.989, still inverted. My own threshold table says the VIX3M/VIX line is graded on the close. The send did carry the word TICK, but its prose sentence went further than its basis did.

## 4. Trigger table on History through 11/20

| Row | Values | Grade |
|---|---|---|
| VIX regime line 30 (SETTLE, one close through) | **35.89** [11/20] | **FIRED** 11/20: equity stress confirmed. First close over 30 since 30.61 [3/30/2026]. |
| VIX regime line 40 | close 35.89; **intraday high 40.03** | NOT FIRED (an intraday touch is not a fire). |
| Regime classification | 11/19 RISING_VOL (28.44) → **11/20 HIGH_VOL** (35.89) | Regime shift row FIRED (🟠, all agents): delivered via NEXUS_BRIEF and the SIG below. |
| VIX +30% in 5 days, credit flat (🔴 HENRY, RED) | Window to 11/19: VIX 18.70 → 28.44 (+52.1%), **HY 320 → 352bp (+32bp)**. Window to 11/20: VIX 19.30 → 35.89 (+86.0%), HY 323 → [11/20 unposted], already 352 on 11/19 (+29) | **Credit is no longer flat.** The 11/19 window fails the credit leg (+32 > +25). The 11/20 window can pass only if HY first-publishes at 348 or under for 11/20. The vol-only (Path B) shape of 11/10 to 11/18 has ended; credit is now moving with vol. |
| VIX3M/VIX < 1.000 (🔴 LIQUID, HENRY, peak marker) | 0.9890 [11/18], 0.9504 [11/19], **0.8621** [11/20] | MET every close 11/17 to 11/20; deepest of this episode. |
| VVIX > 120 (🟠 RED, HENRY) | 118.37 [11/18], 127.10 [11/19], **138.03** [11/20] | MET 11/19 and 11/20. |
| Credit-vol WATCH (KB-VIO-328) | HY 352 [11/19] vs size condition 368 | Closed 11/17 (KB-VIO-401); not reopened. 16bp short. |
| Credit-to-vol Path A | Vol moved first (VIX 19 → 36 in five sessions), credit followed (+29bp) | **Vol-led, not credit-led.** Not a Path A sequence. |

## 5. The volatility surface at the 11/20 close

| Tenor | 11/13 close | 11/20 close | Change |
|---|---:|---:|---:|
| VIX9D (9 days) | 17.82 | **40.72** | +22.90 |
| VIX (30 days) | 19.30 | **35.89** | +16.59 |
| VIX3M (3 months) | 20.62 | **30.94** | +10.32 |
| VIX6M (6 months) | 22.03 | **29.54** | +7.51 |
| VX Z6 (Dec 16 expiry) settle | 19.4379 | **28.4582** | +9.02 |
| VX F7 (Jan 20) | 20.1892 | 26.2462 | +6.06 |
| VX H7 (Mar 17) | 20.7984 | 24.6715 | +3.87 |
| VX N7 (Jul 21) | 21.4999 | 23.6250 | +2.13 |
| VVIX | 101.53 | **138.03** | +36.50 |
| SKEW | 147.14 | 138.84 | −8.30 |
| COR1M (1-month implied correlation) | — | **36.05** (16.42 on 11/16) | more than doubled in a week |
| OVX / OVX:VIX | — | 54.12 / 1.51 (CALM) | oil vol is not leading |
| MOVE (investing.com) | — | **106.31** (+10.27) | BOND owns rates |

**Shape:** every point is inverted from front to back. VIX9D/VIX **1.1346**, VIX3M/VIX **0.8621**, VIX6M/VIX 0.823; the futures run downhill: Z6 28.46 > F7 26.25 > G7 25.39 > H7 24.67 > N7 23.63 (Z6 over F7 +8.4%). The December future sits **20.7% under** spot VIX (spot is 26.1% over it).

**What it says about duration:** the market prices this as **acute and front-loaded, not as a lasting regime**.
- The 9-day index is the highest point on the curve. The most stress is priced for the next week (Thanksgiving week, the Bessent deadline about 11/26, Nvidia's 10-Q).
- The December future (prices VIX at the 12/16 open) is about **28.5**, the January about 26, March about 24.7. The market expects VIX to lose about a fifth of today's level within a month and to keep falling.
- **But the floor moved up.** The July future rose 2.13 points in a week; even six months out the market now prices vol near 24 against 21.5 before. A shock that fades still leaves a higher base level.
- **The carrier is named and unresolved inside the window:** the SEC accounting report (VULCAN owns) and Nvidia's 10-Q, not yet filed, due about 12/04 by VULCAN's arithmetic (12/09 with a late-filing notice). A 9-day premium this large fits a market pricing that date.
- Correlation is the main driver: COR1M rose from 16.42 [11/16] to 36.05 [11/20], so stocks are now pricing as one trade. That is the signature of a de-risking flow across the index, not one name's event.

**History of this shape (Cboe, since VIX3M began 2009-09; first close at or under 0.8621 after 20 closes above it; n = 7, small):**

| Day 0 | VIX | Ratio | Higher close within 17 sessions? | VIX after 17 sessions | Sessions to ratio ≥ 1.000 |
|---|---:|---:|---|---:|---:|
| 2010-05-06 | 32.80 | 0.804 | yes, 45.79 (+39.6%) | 35.54 | 7 |
| 2011-08-08 | 48.00 | 0.794 | no | 31.62 | 42 |
| 2015-08-21 (Fri) | 28.03 | 0.837 | yes, 40.74 (+45.3%) | 21.35 | 7 |
| 2018-02-05 | 37.32 | 0.754 | no | 22.47 | 8 |
| 2018-12-24 | 36.07 | 0.800 | no | 17.80 | 2 |
| 2020-02-25 | 27.85 | 0.857 | yes, 82.69 (+196.9%) | 72.00 | 14 |
| 2025-04-04 (Fri) | 45.31 | 0.810 | yes, 52.33 (+15.5%) | 24.70 | 17 |

- After 5 sessions VIX was lower in 6 of 7 (median −18.7%); after 17 sessions lower in 5 of 7 (the exceptions are 2010 and 2020).
- **But a higher close came first in 4 of 7, and when it came it was at least 15% higher.** The deep inversion marks the peak of pricing in 3 of 7 and a stop on the way up in 4 of 7. This refines KB-VIO-034 (inversion = peak marker) at its deepest end: it is a peak marker on a one-month horizon (5 of 7 lower), not on a one-week horizon.
- The ratio got back to 1.000 within 9 sessions in 4 of 7 (2, 7, 7, 8 sessions).

**What would change my mind (acute, fading → lasting):**
1. **Credit keeps widening:** HY first-published over 350 on three closes (REGINALD's REG-T-04 is at 1 of 3), or at or over 368 (the credit-vol WATCH size condition). This is the biggest one: in 2011 and 2020 credit came along and the episode lasted.
2. **The back of the curve rises while the front falls:** VIX6M over 30, or the H7 and N7 futures still rising on a day spot falls. That would say stress is moving into longer horizons.
3. **The inversion outlasts the base rate:** VIX3M/VIX still under 1.000 after about 17 sessions (12/15).
4. VVIX over 150, or a VIX close over 40.

**What would say it is fading faster:** VIX9D/VIX back under 1 after Thanksgiving week, VIX3M/VIX at 1.000 within about 8 sessions, COR1M back under 25.

## 6. FORWARD VIEW: PROJECTION (my judgment, kept apart from the evidence above)

**What I expect:** the 11/20 close is near the high of pricing for this episode on a one-month view, but not necessarily on a one-week view. Most likely: a choppy Thanksgiving week with one more test, then decay toward the futures path (VIX in the high 20s by mid-December).
**Why:** a 9-day-dominated, deeply inverted curve has been lower 17 sessions later in 5 of 7 cases. Thanksgiving week is thin, and November expiry (11/20) has rolled off a large block of dealer gamma (HENRY's figure: about 40% of short-dated gamma).
**The meaningful alternative:** a follow-through on the SEC report or the 10-Q. A named regulatory question about the largest index weight is a carrier that can re-price on any headline, and its date (about 12/04) falls inside the window. Also a Monday follow-through (both Friday analogs, 2015-08-21 and 2025-04-04, printed a higher close on the next sessions). Credit is joining this time (HY +29bp in a week, the first close over 350), unlike Feb 2018 and Dec 2018 which faded fastest.

Separate event probabilities, each on its own question and horizon (not one distribution):

| Event | Horizon | Probability | Status |
|---|---|---:|---|
| A VIX close above 35.89 on at least one session | 11/23 to 12/16 (17 sessions) | **50%** (base 4 of 7) | **Registered: VIO-PRED-11** (`LETTERS.md`) |
| VIX3M/VIX close at or over 1.000 on at least one session | 11/23 to 12/04 (9 sessions) | 50% (base 4 of 7) | Unscored |
| VIX close on 12/16 below 35.89 | 12/16 | about 75% (base 5 of 7; the December future settled 28.46 on 11/20) | Unscored |
| A VIX close at or over 40.00 | 11/23 to 12/16 | about 30% | Unscored |

**Horizon:** to the December VIX expiry, 12/16. **What would change my mind:** the four items in section 5. This projection moves no score, gate, band or trade.
