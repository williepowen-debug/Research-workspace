# BRENT to PROME: COT #13 NOT-SPENT, BRT-33 first session no observation, closeout

**Date:** 2026-11-06, closeout about 15:40 EST. **Session:** brent-0d, under prome-51.

**For Will:** Speculators' bets against oil are still not used up, the seventh straight reading of that kind. It only describes positioning and is not a reason to trade. The March Brent contract did not trade during today's 14:28–14:30 ET window, so the spread forecast (BRT-33) has no reading for its first day. If that keeps happening it could end with no verdict. Nothing fired and no forecast moved.

| Item | Result | Basis |
|---|---|---|
| COT #13, as-of 11/3 | JOINT NOT-SPENT, 7th. Shorts 125,654 (−651), longs 147,382 (−10,051), OI 1,908,732 (+22,452), 6.5831% | [CONF raw CFTC `f_disagg.txt`, grader rc 0, second raw pull matches, no re-issue] |
| BRT-33, 11/6 | NO OBSERVATION: BZH27 no window bar in captures at 14:45 and 15:05 ET. Valid 0 of 1; needs at least 8 or NO-VERDICT | vendor one-minute bars, proxy |
| F-a | window NOT MEASURABLE; same-minute +$5.04 at 14:25 ET is not an observation | vendor |
| BZF27, CLZ26 | 98.35, 90.8551 | [EST vendor window proxy, not settles] |
| Boundary #8, January 3:2:1 | $37.19, count 0 | [EST vendor] |
| December crack | $91.12, record only | [EST vendor] |

**BRT-33 risk:** BZH27 printed in the window on 5 of the last 7 sessions; both misses are the latest two. Chance of under 8 valid sessions: 4–7% at that rate, 50–60% at a 50% rate. Own arithmetic, small sample, guide only. The row stands as registered; any change is Will's.

**Not done:** November 6 settles and Baker Hughes, not found on one search each at 15:0x ET; the Friday Close routine, 16:15 ET, carries them. TANKER-LIVENESS owner grade not run. `boot.py` not re-run at closeout.

**Disclosed:** the system killed BRENT's CFTC polling watcher about 15:26 ET for low memory. It was not restarted; a bare clock timer and one manual grader run replaced it.

**Moved:** no probability, gate, level or threshold. No TERRY packet. No trade.

**Files:** `AGENTS/BRENT/research/2026-11-06_window/NOTE.md`. Commit b5fdbb37e3, on origin/master.
