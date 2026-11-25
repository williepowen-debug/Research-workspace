# VIOLET -> PROME: the 11/25 VIX FLASH read at the open, D:L1229 second read, the streak count, and what to register for the close

**From:** VIOLET (Claude Code, Opus 5.5, laptop) · **Written:** 2026-11-25, 10:18 ET (from `date`) · **Task:** your prome-77 launch letter (D:L1229 and WALTER FLASH SIG-W-20261125-005) · **Record:** `AGENTS/VIOLET/research/2026-11-25_flash-and-streaks/GRADE.md` (KB-VIO-407).

**Boot reads (bounded reader, each to `eof: true`):** root `CLAUDE.md` 4 pages · `USER.md` 3 · `AGENTS.md` 1 · `AGENTS/VIOLET/CLAUDE.md` 4. Then STATUS, SCRATCH, MEMORY, CALENDAR, `boot.py` (09:15 ET, ran 140 s). **Not run:** boot step 0 `git pull --rebase`: the tree carries other desks' uncommitted work (CARL, LABOR and others), so no pull and no stash, per the spawn rules.

**The whole story.** Monday's calm lasted two sessions. Cboe's official history now confirms Monday 11/23 (VIX 26.62) and Tuesday 11/24 (26.36), and on both days the cash curve stayed inverted: six straight closes where three-month implied volatility sat below thirty-day. This morning, with chips selling off again in Asia and New York, VIX was over 30 from 06:28 ET, peaked at 34.95 at 09:45 as the S&P 500 hit 6,970 (−3.2% on the day), then eased to 31.91 by 09:58. None of that is a close; my lines grade only on the close, and none fired intraday anyway (the confirm line for VIO-PRED-11 is a close above 35.89; the next regime line is 40). The answer to Will's question: five straight inverted closes is uncommon but not extreme (15 completed streaks since 2009), every streak that reached six also reached seven, and what happened next split cleanly on how high VIX was on day seven.

## 1. The FLASH: open and first half hour (vendor 1-minute bars, about 15 minutes delayed; NOT graded)

| ET | VIX | VIX9D/VIX | VIX3M/VIX | VVIX | S&P 500 |
|---|---:|---:|---:|---:|---:|
| premarket | over 30 from 06:28; 31.5 to 31.7 from 09:00 | | | | |
| 09:31 | 32.41 | 1.1228 | 0.8880 | 126.14 | 7,020.47 |
| **09:45** | **34.75** (bar high **34.95**) | 1.1387 | **0.8587** | 128.29 (high 129.05) | 6,984.44 (low **6,970.11**) |
| 09:58 | 31.91 | 1.1012 | 0.8881 | 124.58 | 7,038.25 |

- **Futures (Cboe delayed quotes):** December VX (Z6) 27.25 at 10:17 ET (high 28.20) against a 23.9769 settle [11/24]; June (M7) 23.70 (+0.71). The front rose about 3.3 points, the back under 1: the market prices this as front-loaded, and December sits about 15% under spot.
- **My lines:** VIO-PRED-11 needs a CLOSE above 35.89: intraday high 34.95, not a close and short of it. The 40 line: not near. VVIX over 120 counts on a close. The curve touched 0.8587, a shade deeper than the 11/20 close (0.8621).
- **Cause:** not mine; WALTER lists the chip selloff, proposed Section 301 tariffs and core PCE together and finds no single cause; VIX passed 30 before the 08:30 data.

## 2. D:L1229: 11/23 and 11/24 confirmed (Cboe History, pulled 09:17 ET; all six files answered `research-bot/1.0`)

| Close | VIX | VIX9D/VIX | VIX3M/VIX | VVIX | SKEW |
|---|---:|---:|---:|---:|---:|
| 11/23 | 26.62 | 1.0428 | 0.9579 | 117.36 | 140.37 |
| 11/24 | 26.36 | 1.0121 | 0.9662 | 114.07 | 139.16 |

- My 11/23 provisional print **agrees with History on every spot cell.** One ledger fix: my VX_DAILY row had carried the 11/20 SKEW (138.84) into 11/23; History says 140.37 (corrected by `backfill.py`). On my reading RED-FT-10's exit count resets on 11/23 and is 1 again on 11/24; RED grades.
- **High yield (FRED first-published, my pull 09:18 ET; LIQUID owns):** **363bp [11/23]**, from 376 [11/20]; CCC 1,387; IG 97. 11/24 not posted. 363 is between my fade line (under 350) and lasting line (370 or more): undecided, leaning to stickier than vol.
- **Graded: nothing.** VIO-PRED-11 OPEN; 40 line NOT FIRED; the +30% credit-flat row stands as graded 11/23. Regime on History: RISING_VOL 11/23 and 11/24.
- ⚠️ **Cboe History's high and low cells carry bad prints:** the 11/24 HIGH is 32.38, exactly the flat value WALTER called a bad tick; the 11/23 LOW is 15.39 on a 26.62 close. Closes are sound; Cboe intraday extremes prove nothing. Logged on WALTER's 001 card row.

## 3. The streak count (Will, 11/23 16:49 ET: is five straight inverted closes a lot?)

Cboe History since 2009-09-18 (when the three-month file starts, so 2008 is missing), VIX3M/VIX under 1.000 on the close:
- 332 inverted closes in 107 streaks; most last 1 to 2 days.
- **Streaks of 5 or more: 15 completed** (plus this one, at 6). Two stopped at 5. **Every completed streak that reached 6 reached 7: 13 of 13.**
- **After day 7, VIX stayed above 25 on all of the next 10 closes in 5 of 13** (thesis prediction 2's consequent). **Split on the day-7 level: VIX 31 or more, 5 of 7; under 31, 0 of 6.**
- **The worst close came at or before day 7 in 9 of 13.** The four exceptions were 2011 (twice), March 2020, and March 2025, which the April tariff shock overtook.
- About 10 separate episodes (overlapping); descriptive counts, no new score or rule. Full table in the record, §3.

## 4. What PROME should register for the after-close read (item 4)

Row for the re-wake after 16:15 ET today, Wed 11/25 (Thanksgiving follows; next session Fri 11/27, short):
> **VIOLET WAKE 11/25 after 16:15 ET (D:L1229 item 4):** read the 11/25 close, print first and Cboe History when posted (files post one by one in the evening; if not posted by the session, the print is PROVISIONAL and History is confirmed at the 11/27 boot). (a) VIX3M/VIX under 1.000 on the close = 7th straight inverted close = thesis prediction 2' ARMED; its consequent window is the next 10 closes (11/27 to 12/10); record the day-7 VIX against the 31 split (descriptive). (b) VIO-PRED-11 confirms on any close above 35.89; the 40 line fires on a close over 40; VVIX over 120 and the 30 regime line on the close. (c) HY 11/24 first-published (and 11/25 if posted). (d) Republish both Artifacts on the close; re-score the convergence matrix on History. Prediction 2' arming is a registered antecedent, not a new score.

## 5. Inbox, housekeeping, artifacts

- **Inbox drained, every sender (census `inbox_census.py` 09:19 ET: top-level 0, WALTER 5):** 20261124-001 acted (History confirms its close; its bad-tick reading is consistent with History's high cell); 20261124-007 noted (`combo:ai-trade-unwind`); 20261124-022 noted (LIQUID's IG fire; credit moved with vol here, so not a credit-flat Path B; `combo:ai-credit-repricing`); 20261125-001 noted; 20261125-005 acted (this read). All five in `board_log.tsv` and moved to `processed/`.
- **WQ-712 line (D:L1189):** `scripts/writeback_order_check.py` re-keyed. The pin check no longer searches only the last 30 STATUS commits; a pin passes if it names any commit on this branch that touched STATUS, however old, and still fails closed on a pin that names no STATUS revision (WQ-721 A unchanged). Acceptance written first, 9 of 9 cases pass, including a STATUS commit off HEAD (fails) and the oldest STATUS commit (passes); live run rc 0. **No authority, route or threshold moved.** IMPLEMENTED and TESTED by me; not independently read.
- **Artifacts: NOT republished.** Today's shift is intraday; a page republished at 10:20 ET would show numbers stale by the close. Both republish on the close at the re-wake (in the row above).
- **Cheap-tail ledger:** 11/23 (2 of 4) and 11/24 (1 of 4) regraded on History; DORMANT.

## 6. Forward view (unscored, mine)

- 7th inverted close today: **about 90%** (the curve is at 0.888; it would need VIX to fall about 11% relative to VIX3M by 16:15).
- VIX close of 31 or more today: **about 50%**: it gave back from 34.95 to 31.91 in 13 minutes, and the day before Thanksgiving trades thin.
- Prediction 2' consequent (VIX above 25 on each of the next 10 closes): **about 40%.** History says it holds mostly when day 7 closes at 31 or more; the December future at 27.25 says the market expects VIX near the mid-20s by 12/16.
- VIO-PRED-11 (a close above 35.89 by 12/16; frozen at 50%): my view rises from **about 25% to about 40%**: a second leg came early and VVIX is back over 120 intraday.
- **What would change my mind:** toward lasting, HY at or above 370 on the 11/24 or 11/25 cell, VIX6M over 30, or the back futures rising faster than the front; toward a fade, VIX9D/VIX under 1 and VIX3M/VIX above 1 by 12/02.
- **TERRY:** packet `AGENTS/TERRY/inbox/2026-11-25_from-VIOLET_vix-over-30-seventh-inversion-tradeability.md` (two-sided, no structure, no expiry language).

**Commits (local, not pushed; PROME pushes):** `1acf4452c4` write-back · `218fbc9553` NEXUS_BRIEF (pin `1acf4452c4`) · `d288b95909` TERRY packet · this memo in the next commit. Closeout guard 10:21 ET: all blocking contracts green.

## COMPLETION — VIOLET — 2026-11-25
STATUS: DONE for the morning scope; item (4) of D:L1229 is the 11/25 close and is armed for PROME's re-wake after 16:15 ET (row text in §4).
CHANGED: STATUS, SCRATCH, NEXUS_BRIEF, KB-VIO-407, VX_DAILY (11/23 SKEW fix, 11/24 row), CHEAP_TAIL, CATALYSTS/CALENDAR note, board_log + 5 cards filed, MAINTENANCE, writeback_order_check.py, research/2026-11-25_flash-and-streaks/; TERRY packet.
RESULT: History confirms 11/23 (26.62) and 11/24 (26.36), 6 straight inverted closes; HY 363 [11/23]; FLASH intraday VIX high 34.95 at 09:45, 31.91 at 09:58, curve low 0.8587, nothing graded; streaks: 15 of 5+, 13 reached 7, consequent held 5 of 13 (5 of 7 at day-7 VIX ≥31, 0 of 6 under).
GAPS: no pull (other desks' dirty tree); HY 11/24 not posted at 09:18 ET; Artifacts held for the close (intraday would be stale); the script re-key is author-tested only; 2008 not in the streak sample (VIX3M file starts 2009-09).
WILL_NEEDS: nothing; the streak answer is for his 11/23 question (§3).
FOLLOW-UP: register the §4 row for the re-wake after 16:15 ET today; push is PROME's.
