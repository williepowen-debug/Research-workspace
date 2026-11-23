# VIOLET 11/23 close read (D:L1229 items 1 to 3)

**Session:** PROME prome-77 wake on D:L1229, Monday 2026-11-23, boot 16:08 ET (from `date`). Claude Code, Opus 5.5, laptop on battery. KB-VIO-406.
**Basis rule:** a registered prediction grades only on Cboe `VIX_History.csv` (its letter). Everything below marked PRINT is the 16:15 ET close print read through a vendor mirror, and is PROVISIONAL until Cboe History posts the 11/23 row.

## 1. Item (1): high-yield spread for 11/20, and the "+30% in 5 days, credit flat" row

**Basis (LIQUID's method):** FRED `BAMLH0A0HYM2`, `output_type=4` (initial release only), the same call as `AGENTS/LIQUID/scripts/hy_oas_watch.py` `_first_published`. My pull 16:10 ET 11/23. LIQUID has not itself graded the 11/20 cell (its last own commit is 11/20, before the cell posted); this is LIQUID's basis read by me, and LIQUID owns the figure.

| Date | HY OAS first-published | CCC |
|---|---:|---:|
| 11/12 | 320 bp | 1,314 |
| 11/13 | 323 | 1,316 |
| 11/19 | 352 | 1,361 |
| **11/20** | **376** | **1,402** |

Agrees with PROME's dashboard pull (376, CCC 1,402, 12:04 ET) and HENRY's read (12:07 ET).

**The row's letter** (charter outbound table): VIX up more than 30% in 5 sessions with HY OAS's 5-session change no wider than +25bp, first-published FRED, same 5 sessions.

| Window (5 sessions) | VIX, Cboe History | HY, first-published | Credit leg |
|---|---|---|---|
| 11/12 to 11/19 | 18.70 → 28.44, **+52.09%** | 320 → 352, **+32bp** (pass needs ≤ 345) | **FAILS** |
| 11/13 to 11/20 | 19.30 → 35.89, **+85.96%** | 323 → 376, **+53bp** (pass needs ≤ 348) | **FAILS** |

**Verdict: the credit leg fails on both windows.** The vol leg is met on both; the row is NOT MET on either. The 11/17 MET (KB-VIO-402, sent 11/18) stands as recorded: on 11/17 vol moved alone; by 11/19 and 11/20 credit had followed. No send is owed for a row that did not fire.

**Also crossed, not graded here:** 376 is +108bp over the 268bp base of 9/22, past the 368bp size line of the credit-vol WATCH (KB-VIO-328). That watch closed terminally at its 11/17 endpoint (KB-VIO-401) and is not reopened: this is three sessions after the window and a watch, not a letter (WQ-611 A). It does meet one of my own written "acute → lasting" conditions (STATUS 11/21: "HY over 350 on three closes or at 368"). REGINALD's REG-T-04 (over 350 three closes) is at 2 of 3 on 11/19 and 11/20; REGINALD grades.

## 2. Item (2): the 11/23 close (PROVISIONAL: not graded)

**Source and time:** the 16:15 ET close print through the vendor mirror (`FORGE/tools/market-data/fetch.py price`, Yahoo), pulled **16:32 ET** after the vendor values stopped moving (they changed between 16:13, 16:18 and 16:19 ET pulls: a 15-minute delay). Cboe's own History files answered **HTTP 200** at 16:10 ET but end at **11/20**; the 11/23 rows were not posted. Cboe's delayed-quote JSON (`cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json`) returned **403** at 16:12 ET (see section 4).

| Series | 11/23 print (provisional) | 11/20 Cboe History | Change |
|---|---:|---:|---:|
| VIX | **26.62** | 35.89 | −25.83% |
| VIX9D | 27.76 | 40.72 | −31.8% |
| VIX3M | 25.50 | 30.94 | −17.6% |
| VIX6M | 25.96 | 29.54 | −12.1% |
| VVIX | 117.36 | 138.03 | −15.0% |
| COR1M | 25.68 | 36.05 | −28.8% |
| OVX | 49.19 | 54.12 | −9.1% |
| SKEW | not available (vendor stale at 11/20, Cboe quote refused) | 138.84 | n/a |

**Ratios on the print:** VIX9D/VIX **1.0428** (from 1.1346) · VIX3M/VIX **0.9579** (from 0.8621) · VIX6M/VIX 0.9752. The cash curve is still inverted: a 5th straight close if History agrees (11/17, 18, 19, 20, 23).

**VX futures settle 11/23 (official, Cboe settlement CSV, pulled 16:17 ET, HTTP 200):** Z6 **24.0844** (28.4582 on 11/20, −15.4%), F7 23.7164, G7 23.5635, H7 23.3021, N7 23.0980 (23.6250, −2.2%). Still backwardated, but nearly flat: Z6 over N7 by 0.99 points against 4.83 on 11/20.

**VIO-PRED-11 (VIX close above 35.89, 11/23 to 12/16):** **NOT RESOLVED, stays OPEN.** The print is 9.27 under the line; a confirming close now needs +34.8% from 26.62. Not graded: the letter grades only on Cboe `VIX_History.csv` with companions present, and a print below the line cannot resolve a one-close-is-enough YES letter anyway. Registered 50% stands frozen.
**VIX 40 line:** **NOT FIRED** (print 26.62; no intraday touch needed or claimed).
**Regime:** RISING_VOL on the print (20 to 30). The regime-shift row HIGH_VOL → RISING_VOL fires only on Cboe History, not on the print (practice since KB-VIO-399).

**What remains and when:** the six Cboe History rows for 11/23 (VIX, VIX9D, VIX3M, VIX6M, VVIX, SKEW). They post file by file, observed between about 17:30 and 21:30 ET (KB-VIO-390, an observation, not a schedule). The next wake (Wed 11/25, D:L1229 second read) confirms 11/23 and 11/24 from History, runs `backfill.py` to replace today's TICK row in `VX_DAILY.tsv`, and then reads the 11/25 close for item (4).

## 3. Item (3): the two Will-facing Artifacts

Republished in place through the method in my charter and the two memory files (Claude Artifact tool, `url` of each; each live page read first and matched the repo source on its 11/09 snapshot):
- **Vol cheat-sheet** → version **16**, `https://claude.ai/code/artifact/c2129279-b677-4093-be68-ccdbe0df76b3` (tool printed `claude.ai/artifact/QxxwekNaRcorjaXeYahwAa`). Markers recomputed on the page's documented mapping: VIX 66.5%, VVIX 68.2%, SKEW 52.4%, TERM 85.5%.
- **Operating Picture** → version **18**, `https://claude.ai/code/artifact/8eb52313-be4e-49a3-8555-e5cc23b44c60` (printed `claude.ai/artifact/Jd5sjALgQKrjpamhQ33pJT`).
Only the dated bands changed: the 20 Nov shift (35.89, HIGH_VOL, HY 376), the 23 Nov print labelled provisional, the forecasts, next dates. Both pages say the 23 Nov figures await Cboe's archive. Private links: Will sees them only if PROME brings them to him.

## 4. Cboe access from this box, 11/23 (for HENRY's report and WQ-735)

| Endpoint | Client | Result, time ET |
|---|---|---|
| `cdn.cboe.com/api/global/us_indices/daily_prices/<SYM>_History.csv` (307 → cdn-api) | research-bot/1.0 | **200**, 16:10 (six files, last row 11/20) |
| `www.cboe.com/us/futures/market_statistics/settlement/csv/?dt=2026-11-23` | research-bot/1.0 | **200**, 16:17 |
| `cdn.cboe.com/data/us/futures/.../VX_<expiry>.csv`, CFE archive CSV | research-bot/1.0 | **200**, about 16:12 |
| `cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json` | research-bot/1.0 | **403** (HTML block page), 16:12 |
| same, via `thresholds.py` `cboe_quote` (default urllib client, unchanged) | Python-urllib | unusable (returns None), about 16:21 |

So from this laptop at this hour the publisher-of-record files answer and the live quote endpoint refuses. HENRY's "Cboe refuses since 11/20" matches the quote endpoint, not the History files. No client string was changed to test the refusal; nothing was worked around.

## 5. Forward view (Will 11/19; unscored unless named)

**Expect (about 60 to 65%):** VIX drifts lower into the December expiry, the curve back above 1.000 within about 8 sessions, and prediction 2' does not arm or arms and fails. Why: the carrier partly reversed in one session (the CEO's return), the front premium is mostly gone (VIX9D/VIX 1.0428 from 1.1346), Z6 sits 2.5 points under spot, and the deep-inversion base had VIX lower 17 sessions later in 5 of 7.
**Meaningful alternative (about 35 to 40%):** a second leg before 12/16. Why: credit printed its widest of the year on the last session it has (376), the reported SEC accounting question is untouched by the 8-K, and the 10-Q (about 12/04, VULCAN) is a dated resolver inside the window. VIO-PRED-11 stays at its frozen 50%; my unscored view of it today is about 25%.
**Horizon:** to 12/16. **What would change my mind:** toward fading, HY 11/23 or 11/24 first-published back under 350; toward the alternative, HY holding at or above 370, VIX6M back over 30, or the back futures rising on a day spot falls.
