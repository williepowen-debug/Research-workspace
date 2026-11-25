# VIOLET 11/25 close read (D:L1280) — record

**Session:** violet-29 (Claude Code, Opus 5.5, laptop), Wed 2026-11-25; PROME prome-77 wake at 16:15 ET on D:L1280. Written 16:40 ET (from `date`). KB-VIO-409.
**Basis:** the 16:15 ET close print through a vendor mirror (`FORGE/tools/market-data/fetch.py`, two pulls 16:33 and 16:35 ET, identical). **PROVISIONAL.** Cboe History answered but ends at 11/24 (pulls 16:15, 16:26 and 16:37 ET). History is confirmed at the 11/27 boot. Not used: vendor pulls at 16:07 to 16:20 ET (15-minute delay, still moving: 27.87 to 28.31) and one failed pull 16:20 to 16:22 ET (all ten symbols errored; recovered unaided).

## 1. The close

| Series | 11/25 print | 11/24 History | Change |
|---|---:|---:|---:|
| VIX | **28.29** (high 34.95 at 09:45) | 26.36 | +7.3% |
| VIX9D | 29.61 | 26.68 | +11.0% |
| VIX3M | 26.29 | 25.47 | +3.2% |
| VIX6M | 26.89 | 26.19 | +2.7% |
| VVIX | 115.38 (high 131.48 at 11:20) | 114.07 | +1.1% |
| COR1M | 25.45 | 24.62 | +3.4% |
| S&P 500 (HENRY owns) | 7,182.78 | 7,201.09 (vendor) | -0.25% |
| SKEW | not posted | 139.16 | |
| VIX9D/VIX · VIX3M/VIX | **1.0467 · 0.9293** | 1.0121 · 0.9662 | |

VX settles 11/25 (official Cboe settlement CSV, read 16:19 and 16:35 ET): Z6 **25.0258** (23.9769), F7 24.2921, G7 23.9679, H7 23.5523, M7 23.125 (22.9924). Z6 is 3.26 points under spot.

## 2. Item by item

| Item | Read on the print | State |
|---|---|---|
| (a) 7th straight inverted close | 0.9293 < 1.000 | **MET: prediction 2' ARMED, PROVISIONAL.** 7 closes: 11/17, 18, 19, 20, 23, 24, 25 |
| (a) consequent window | VIX above 25 on every close | **10 closes: 11/27, 11/30, 12/01, 02, 03, 04, 07, 08, 09, 10.** First close at 25.00 or under fails it |
| (a) day-7 VIX against 31 | 28.29 | **under 31: the 0-of-6 half** (descriptive) |
| (b) VIO-PRED-11 (close > 35.89) | 28.29 | NOT RESOLVED, OPEN; 50% frozen |
| (b) 40 line | 28.29 | NOT FIRED |
| (b) VVIX over 120 | 115.38 | NOT MET on the close |
| (b) 30 regime line | 28.29 | NOT FIRED; RISING_VOL, no shift, no broadcast |
| +30% in 5 sessions, credit flat | 24.56 [11/18] to 28.29 = +15.2% | NOT MET |
| (c) HY | **372 [11/24]** first-published (LIQUID 11:45 ET; my FRED pull 15:34 ET same cell), CCC 1,405, IG 98; 11/25 not posted | my written "lasting" line (370 or more on 11/24 or 11/25) **MET by the 11/24 cell**. That line is one of several "what would change my mind" conditions; it scores nothing |
| (d) Artifacts | cheat-sheet version 17, Operating Picture version 19 | REPUBLISHED on the print, labelled provisional |
| (d) convergence | 40/50 (11/20 basis) | NOT RE-SCORED: History not posted |

**My morning odds, graded informally:** 7th inverted close about 90% (happened, provisional); VIX close of 31 or more about 50% (did not: 28.29).

## 3. D:L342, the Thanksgiving bar

**No streak, sustain or consecutive-closes count may advance on an 11/26 VIX value.** NYSE is closed. For my streak: day 7 is 11/25, the next session is 11/27 (short session, one close). Cboe's `VIX_History.csv` has carried a bar on past closures with the companion indices absent; FRED VIXCLS and the vendor inherit it. My ledger refuses an orphan-VIX row (f385b5f0cf); check owed 11/27: no 11/26 VX_DAILY row. RED and REGINALD told by packet.

## 4. WALTER's question 4: dealer hedging under 7,000

**My instruments do not measure dealer hedging or gamma; HENRY owns that (last published map 11/19).** What they show (`under_7000.py`, vendor 1-minute bars, 389 minutes):

| S&P zone | Minutes | One-minute return, standard deviation | VIX points per 1% S&P move |
|---|---:|---:|---:|
| under 7,000 | 37 (09:36 to 11:48) | 7.1 bp | -1.68 |
| 7,000 to 7,050 | 109 | 9.8 bp | -1.81 |
| 7,050 and over | 242 | 7.5 bp | -1.48 |

- **No acceleration under 7,000:** minute moves were smaller below the level than just above it, and VIX did not become more sensitive. The S&P spent 37 minutes under the level and recovered.
- **Cover stayed bid after the low.** At the same S&P (7,005 to 7,045) VIX's median was 32.41 before 10:15 and 33.27 after; VIX6M 28.75 and 29.24. VVIX peaked at 11:20, 95 minutes after the S&P low. Vol came off only as the S&P left 7,000 after 12:00.
- **So:** this fits support at 7,000 rather than hedging that fed the fall. It does not identify who hedged. One day; index bars about 15 minutes delayed; the zone under 7,000 is small.

## 5. Forward view on 2' (unscored; the thesis row grades the event)

**Expect:** 2' fails. **About 88% that VIX closes at 25 or under at least once 11/27 to 12/10; about 60% by 12/02.** Why: day-7 VIX 28.29 is in the half where it held 0 of 6; in the four cases with day-7 VIX 25 to 31 the first close at 25 or under came on session 1, 1, 4 and 6 (2018-02, 2025-03, 2018-12, 2015); the December future settles 25.03 and G7 23.97; the day's high faded 6.7 points.
**Alternative (about 12%):** held above 25 for ten closes, or a second leg. Why it is not smaller: HY 372 is back near its 376 high while equity vol fades; the 9-day premium is back at 1.0467; Nvidia's 10-Q (about 12/04) is inside the window; 2025-03 failed this test and then VIX went to 52 on a new carrier.
**VIO-PRED-11 (close > 35.89 by 12/16):** registered 50% frozen; my unscored view falls to about 22% (from about 40% this morning): it needs +27% from here.
**Horizon:** 12/10 for 2', 12/16 for PRED-11. **What would change my mind:** toward lasting, HY for 11/25 at 370 or more with a VIX close back over 31, VIX6M over 30, or back futures rising more than the front on a down day. Toward fade, VIX9D/VIX under 1 and VIX3M/VIX over 1 by 12/02.

## 6. PREDICTIONS.tsv (PROME's ask; no forecast changed)

- `Confidence` filled from each letter: VIO-PRED-07 0.72, -08 0.25, -09 0.45, -10 0.55 (`research/2026-11-06_wake/LETTERS.md`); -11 already 0.50.
- VIO-FOMC-0916 L1 to L5 and F-B state no probability: `UNSCORED` (a token PROME's scorer reads), never a back-filled number.
- `Date_Made` column added from each letter's registration: 2026-09-02 (FOMC, commit c6851727e2), 2026-09-11 (F-B), 2026-11-06 (07 to 10, commit 5b641d5fe4), 2026-11-21 (11, commit 6fc8a7c3a6). PROME's reader matched the word Date inside `resolve_date`; it looks for `Date_Made` by exact name first.
