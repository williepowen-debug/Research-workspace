---
signal_id: SIG-W-20261002-032
date: 2026-10-02
timestamp: 2026-10-02T21:09:26Z
time_dispatched: 2026-10-02T21:09:26Z
timestamp_note: stamped from the system clock at write, not typed
source: Will-Telegram (zerohedge X screenshot) + CBOT fed funds futures (yfinance) + FRED EFFR
origin: ["Will-Telegram msg 4894 (2026-10-02 21:07:56Z): @zerohedge '*FED-DATED SWAPS NO LONGER PRICE ONE FULL RATE HIKE THIS YEAR', posted ~2h before the screenshot; screenshot time not shown", "yfinance daily bars ZQV26/ZQX26/ZQZ26.CBT 9/28-10/02, pulled by WALTER before dispatch (after the CBOT close, before the 18:00 ET evening open)", "FRED EFFR 3.88 (obs 10/01), DFEDTARU 4.00 (10/02)"]
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
entities: ["fed-funds-futures", "FOMC-2026-10-28", "FOMC-2026-12-09", "EFFR", "fed-funds-target-range"]
confidence: 0.75
confidence_language: "reports"
signal_type: context
safety_net: clear
verdict: "Zerohedge headline 10/02 ('Fed-dated swaps no longer price one full rate hike this year', ~2h before Will's screenshot, no number) checks out on CBOT fed funds futures (yfinance daily bars, WALTER arithmetic, EFFR 3.88 [FRED 10/01]): cumulative hikes priced by year-end ~24.7bp on 10/02 (Oct ~5bp, Dec ~20bp) vs ~24.3bp 10/01, ~30.6 9/30, ~33.6 9/29, ~38.6 9/28. So 'below one full hike' happened on 10/01 on this basis and held through the 10/02 close despite the long-end selloff; the drop since 9/28 is ~14bp, mostly the October meeting (~17.5bp -> ~5bp, i.e. ~70% -> ~20% odds)."
precedence: ROUTINE
action: ["BOND"]
info: ["HENRY", "LIQUID", "RED"]
dispatch_note: "Will image BM-20261002-08 item 3. Same routing as -1001-035 / -013 (BOND owns hike pricing). Gives BOND a dated, instrument-based year-end figure while its FedWatch read stays owed. RED pull-complete."
---
# Futures now price a little under one full Fed hike by year-end (~25bp), down from ~1.5 hikes on 9/28. The zerohedge headline holds.

**Short version:** Will sent a zerohedge headline saying the market **"no longer prices one full rate hike this year."** It has no number. **Fed funds futures agree:** by year-end they price about **24.7bp of hikes** (a quarter-point hike is 25bp), as of the 10/02 close. That compares with about **38.6bp on 9/28**. Most of the drop is the **October 28 meeting**, now about 5bp priced (roughly a 1-in-5 chance) against about 17.5bp (roughly 70%) on 9/28. **December** still carries about 20bp. **The crossing below one full hike happened on 10/01 on this basis and held on 10/02**, even though long-dated Treasury yields rose into the close (`-028`).

| CBOT fed funds futures, daily bar (yfinance) | 9/28 | 9/29 | 9/30 | 10/01 | 10/02 |
|---|---|---|---|---|---|
| Nov (ZQX26) → implied rate | 4.055 | 4.005 | 3.975 | 3.94 | 3.93 |
| Dec (ZQZ26) → implied rate | 4.205 | 4.155 | 4.125 | 4.07 | 4.07 |
| October hike priced (Nov − EFFR 3.88) | ~17.5bp | ~12.5 | ~9.5 | ~6 | **~5** |
| December hike priced | ~21 | ~21 | ~21 | ~18 | **~20** |
| **Cumulative by year-end** | **~38.6bp** | ~33.6 | ~30.6 | ~24.3 | **~24.7** |

Method: implied rate = 100 − price. November's average fully reflects the 10/28 decision. December's average reflects the 12/9 decision for 22 of 31 days, so December's hike = (Dec − Nov) ÷ (22/31). EFFR 3.88% (FRED, 10/01); target 3.75–4.00%.

**So what:** The market has gone from expecting **about one and a half hikes this year** to **just under one**, almost entirely by pushing out October. That matches TD's call change (`-013`: December and March, from October and January) and the payrolls miss (`-001`). **December is still close to a coin-flip-plus.** The year-end figure barely moved on 10/02. **The front end did not follow the long end's selloff into the close.**

## Caveats
- **This is WALTER's arithmetic on vendor daily bars, not a dated CME FedWatch read or swap print.** yfinance's daily bar may be the last trade rather than the CBOT settlement. The method assumes EFFR moves one-for-one with the target and ignores month-end effects; results are ±2bp.
- The zerohedge headline names **Fed-dated OIS swaps**, a different instrument from futures. The two usually agree within a few basis points; that was not checked here.
- Earlier October odds on the BOARD came from mixed, undated secondaries (~26% FedWatch screenshot `-1001-035`; ~16% Yahoo `-001`). This ~20% is a different basis; **do not net them**.
- **BOND owns this read.** The dated FedWatch pull owed since `-1001-035` still governs.

## Exposure
Will holds TBT (a short on long Treasuries; BOND/TERRY). This front-end move does not map directly onto TBT, which tracks the 20+ year end.

## Requested action
**BOND:** confirm the year-end and October pricing on your own basis (FedWatch or OIS, dated), and say whether "below one full hike by year-end" changes any registered rates item or the TBT read. HENRY, LIQUID: information. RED: information (pull-complete).
