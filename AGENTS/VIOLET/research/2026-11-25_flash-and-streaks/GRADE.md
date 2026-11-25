# D:L1229 second read and the 11/25 FLASH — record

VIOLET, Wed 2026-11-25, PROME prome-77 wake (D:L1229, WALTER FLASH SIG-W-20261125-005). Claude Code, Opus 5.5, laptop. Session began 09:13 ET (`date`). Every intraday number below is a vendor or delayed quote with its time; **nothing intraday is a close and nothing intraday is graded.**

## 1. 11/23 and 11/24 confirmed on Cboe History (pulled 09:17 ET, `research-bot/1.0`, all six files 200)

| Close | VIX | VIX9D | VIX3M | VIX6M | VVIX | SKEW | COR1M | VIX9D/VIX | VIX3M/VIX |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11/20 | 35.89 | 40.72 | 30.94 | 29.54 | 138.03 | 138.84 | 36.05 | 1.1346 | 0.8621 |
| **11/23** | **26.62** | 27.76 | 25.50 | 25.96 | 117.36 | **140.37** | 25.68 | **1.0428** | **0.9579** |
| **11/24** | **26.36** | 26.68 | 25.47 | 26.19 | 114.07 | 139.16 | 24.62 | **1.0121** | **0.9662** |

- The 11/23 provisional print of my 11/23 session **agrees with History on all five spot cells**. One ledger correction: VX_DAILY 11/23 SKEW held 138.84 (the 11/20 value filled forward); History says **140.37** (`backfill.py --spot-only` 09:18 ET, CBOE wins; 11/23 and 11/24 rows now SETTLE, the 11/24 row created).
- **Cash-curve inversion count: 6 straight closes under 1.000 (11/17, 11/18, 11/19, 11/20, 11/23, 11/24).** Item (4) needs a 7th on the 11/25 History close.
- Regime row on History: RISING_VOL on 11/23 and 11/24 (20 to 30), from HIGH_VOL [11/20].
- SKEW 140.37 [11/23] is back above 140, then 139.16 [11/24]. On my reading RED-FT-10's exit count (<140 ×4) goes 1 [11/20], reset [11/23], 1 [11/24]. RED grades; this is my read only.
- ⚠️ **History's high/low cells carry bad prints.** 11/24 VIX HIGH 32.38 is the same flat value WALTER called a bad tick (08:08 to 08:12 ET); 11/23 VIX LOW **15.39** on a 26.62 close (11/20 close 35.89) cannot be a real index level. Closes are graded; Cboe intraday extremes certify nothing.
- VX settles 11/24 (Cboe settlement CSV): Z6 **23.9769** (from 24.0844), F7 23.6437, G7 23.5233, H7 23.3278, M7 22.9924; weekly VX47/X6 expired 11/24 at 29.22.

**Nothing graded by these closes.** VIO-PRED-11 (any close above 35.89 by 12/16) stays OPEN; the 40 line has not fired; the +30% credit-flat row was graded 11/23 (KB-VIO-406) and nothing here re-opens it.

## 2. High-yield cells (FRED, first-published `output_type=4`, my pull 09:18 ET; LIQUID owns spreads)

| Cell | HY OAS | CCC | IG |
|---|---:|---:|---:|
| 11/19 | 352 | 1,361 | 94 |
| 11/20 | 376 | 1,402 | 98 |
| **11/23** | **363** | **1,387** | **97** |
| 11/24 | not posted at 09:18 ET | | |

My 11/23 decider was "under 350 = fade; 370 or more = lasting". **363 sits between: undecided.** Credit gave back 13bp of the 24bp jump while VIX gave back 26%: credit is stickier than vol, which leans toward my "lasting" branch without reaching it.

## 3. The streak count Will asked about (11/23 16:49 ET: is five straight inverted closes a lot?)

Cboe History, VIX3M/VIX < 1.000 on the close; the VIX3M file starts 2009-09-18, so **2008 is not in the sample**; 4,323 matched sessions to 11/24. Scripts and raw outputs in this directory (`inversion_streaks.py`, `inversion_after_day7.py`, run against the 09:17 ET pull).

- **332 inverted closes in 107 streaks.** Most are short: 52 lasted one day, 25 two, 9 three, 5 four.
- **Streaks of 5 or more: 15 completed, plus the live one (6 so far).** Two stopped at 5 (Nov 2016 election, Mar 2018). **Every completed streak that reached 6 went on to reach 7: 13 of 13.**
- **Reached 7: 13** (about 10 separate episodes: three 2011 streaks are one crisis, the March and April 2025 streaks one shock).

| Streak (closes) | Length | VIX on day 7 | Next 10 closes above 25 | VIX 20 sessions after day 7 | Episode's top close |
|---|---:|---:|---:|---:|---|
| May 2010 | 7 | 38.32 | 10 of 10 | 27.05 | 45.79, at or before day 7 |
| Jul–Aug 2011 | 25 | 31.66 | 10 of 10 | 31.82 | 48.00, AFTER day 7 |
| Sep 2011 (a) | 7 | 36.91 | 10 of 10 | 32.86 | 45.45, AFTER |
| Sep–Oct 2011 (b) | 10 | 38.84 | 10 of 10 | 25.46 | 45.45, AFTER |
| Oct 2014 | 7 | 21.99 | 0 of 10 | 13.31 | 26.25, at or before |
| Aug 2015 | 9 | 26.05 | 6 of 10 | 27.63 | 40.74, at or before |
| Feb 2018 | 8 | 25.61 | 0 of 10 | 16.35 | 37.32, at or before |
| Oct 2018 | 7 | 21.23 | 0 of 10 | 18.79 | 25.23, at or before |
| Dec 2018 | 12 | 30.41 | 4 of 10 | 17.42 | 36.07, at or before |
| Feb–Apr 2020 | 43 | 36.82 | 10 of 10 | 53.54 | 82.69, AFTER |
| Oct–Nov 2020 | 7 | 35.55 | 4 of 10 | 21.17 | 40.28, at or before |
| Mar 2025 | 9 | 26.92 | 0 of 10 | 52.33 | 52.33, AFTER (the April tariff shock, a new carrier) |
| Apr 2025 | 16 | 40.72 | 9 of 10 | 21.90 | 52.33, at or before |

**What it says, plainly.**
1. Five straight is uncommon (15 times in 17 years) but not extreme; six and seven are the same club, since nothing that reached six stopped there. Long streaks (10 or more) are the real crises: 2011, Dec 2018, 2020, April 2025.
2. Thesis prediction 2's consequent (VIX above 25 for the next 10 closes) held in **5 of 13**. It split cleanly on the level at day 7: **VIX at 31 or more on day 7: 5 of 7 held; under 31: 0 of 6.** Today's close is day 7 if the curve stays inverted, and today's intraday VIX is near that boundary (section 4).
3. **The worst close came at or before day 7 in 9 of 13.** In the four that went higher (2011 twice, 2020, 2025), the further rise came within days and, in 2025, from a new carrier. Consistent with my standing reading that inversion marks peaks more often than onsets (KB-VIO-034), not proof of it.
4. Small sample, overlapping episodes, one regime (post-2009). Descriptive counts, **no new score or rule.**

## 4. The 11/25 FLASH: the open and the first half hour (intraday, NOT graded)

Vendor 1-minute bars (yfinance, pulled 10:16 ET; index bars run about 15 minutes late, so the last bar was 09:58), filtered to today's date. ⚠️ A pre-open pull with `period=1d` returned the PRIOR session's bars for VIX9D/VIX3M/VIX6M/VVIX, which would have produced a cross-date ratio (the KB-VIO-139 hazard); the filter is in `open_bars.py`.

| ET | VIX | VIX9D | VIX3M | VIX6M | VVIX | S&P 500 | 9D/VIX | 3M/VIX |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 09:30 | 31.72 | | | | | 7,038.45 | | |
| 09:31 | 32.41 | 36.39 | 28.78 | 28.77 | 126.14 | 7,020.47 | 1.1228 | 0.8880 |
| 09:35 | 33.11 | 36.84 | 28.98 | 28.96 | 126.50 | 7,010.03 | 1.1127 | 0.8753 |
| 09:40 | 33.70 | 37.78 | 29.28 | 29.26 | 126.88 | 6,992.46 | 1.1211 | 0.8688 |
| **09:45** | **34.75** (bar high 34.95) | 39.57 | 29.84 | 29.58 | 128.29 (high 129.05) | 6,984.44 (low 6,970.11) | 1.1387 | **0.8587** |
| 09:50 | 34.10 | 38.38 | 29.57 | 29.49 | 127.24 | 6,987.11 | 1.1255 | 0.8672 |
| 09:55 | 32.56 | 36.04 | 28.72 | 28.81 | 125.00 | 7,024.13 | 1.1069 | 0.8821 |
| 09:58 | 31.91 | 35.14 | 28.34 | 28.47 | 124.58 | 7,038.25 | 1.1012 | 0.8881 |

- **Premarket (WALTER 005 and my 09:21 ET read):** VIX over 30 from 06:28 ET, 31.5 to 31.7 from 09:00 to the open; the overnight low was 27.63 at 03:35.
- **The first half hour peaked at 09:45 with the S&P low:** VIX 34.95 bar high, under 35.89 and far under 40. 3M/VIX touched **0.8587**, slightly deeper than the 11/20 close (0.8621). By 09:58 VIX had given back to 31.91 and the S&P was back at 7,038; the S&P printed 7,063.54 at 10:06.
- **VX futures (Cboe delayed quotes, no trade time):** Z6 26.55 at 09:19, 26.69 at 09:31, 27.60 at 09:48 (high 28.20), 27.25 at 10:17; F7 25.75, H7 24.55, M7 23.70 at 10:17. The front rose about 3.3 points, the back about 0.7: the shock is priced as front-loaded, and Z6 sits about 15% under spot.
- **My written lines:** VIO-PRED-11 needs a CLOSE above 35.89 (intraday high 34.95 is not a close and did not reach it anyway); the 40 line is a close line, not near; VVIX over 120 counts on a close only; the 30 regime line grades on the close. **Nothing here is graded.**
- **Cause:** not mine to assign. WALTER lists the chip selloff, proposed Section 301 tariffs and core PCE 3.3% together; VIX passed 30 at 06:28 ET, before the 08:30 data.
