# COT #15 (as-of 2026-11-17), live read 2026-11-21 18:0x EST

**Who graded first:** the autonomous Friday Close routine graded #15 from the raw CFTC file and appended the ledger row (`workbook/COT_VINTAGES.tsv`, stamp 2026-11-20T21:17:59Z = 16:17:59 ET, commit f7fd02a504; detail `../../demand_destruction/data/friday_2026-11-20.md`). The live session's own wait job (start 15:36 ET 11/20) did not run in the window: the laptop slept from about 14:53 ET 11/20 to about 17:48 ET 11/21, and its first attempt at 17:48:45 EST 11/21 failed with `Network is unreachable` (log `run_live_fail_2026-11-21.txt`; a local network error, not a CFTC block).

**Live re-read (11/21, after wake):** `cot_grade.py --expect 2026-11-17 --no-record` rc 0, plain client string, raw `f_disagg.txt`: re-issue watch matches the ledger (shorts 137,797, OI 1,869,789). **Socrata 72hh-3qpy cross-check** (`curl`, default client string): shorts 137,797, longs 153,611, OI 1,869,789, identical to the digit. Two CFTC publication paths agree. [CONF CFTC]

| Field | #15 (11/17) | #14 (11/10) | Change |
|---|---|---|---|
| MM gross shorts | 137,797 | 122,378 | **+15,419** |
| MM gross longs | 153,611 | 148,092 | +5,519 |
| Open interest | 1,869,789 | 1,917,473 | −47,684 |
| OI share (Leg B, gating) | 7.3697% | 6.3823% | +0.9874 points |

**Grade: JOINT NOT-SPENT, ninth consecutive.** Leg A 137,797 is 19,471 above the NOT-SPENT floor 118,326; Leg B 7.3697% against 4.909%. Both legs moved away from SPENT. Sizing modifier stays at base case; no entry implication (the grader's non-claims travel: a positioning descriptor, never shown to predict price).

**Size of the move:** the largest weekly change and the highest short level in the 15-row ledger (8/11 to 11/17). ⚠️ **Correction to the routine's packet:** it says prior weekly changes ran −5,980 to +6,644, so this one is about 2.3 times the largest. The ledger has +8,388 (9/15) and +8,074 (9/29), so it is **about 1.8 times** the prior largest. Same conclusion, smaller multiple.

**What drove it (assessment, not decomposed):** managed money added about three new shorts for every new long while total open interest fell, in the week EIA (STEO 11/10, Q4 build 1.47 mb/d) and IEA (OMR 11/13, Q4 surplus +1.7 mb/d) published surplus forecasts. The open-interest fall is consistent with December WTI (CLZ26, last trade 11/20) rolling off. I have not split the position by contract month, and the disaggregated file does not. **Does not change:** BRT-33 (Brent spread, moved away from its line), BRT-31 or BRT-34. Next: #16 as-of 11/24, Monday 11/30 (Thanksgiving delay, CFTC schedule as read 11/13).
