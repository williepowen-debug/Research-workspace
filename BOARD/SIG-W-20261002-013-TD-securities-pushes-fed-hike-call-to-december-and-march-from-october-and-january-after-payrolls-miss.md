---
signal_id: SIG-W-20261002-013
date: 2026-10-02
timestamp: 2026-10-02T16:15:15Z
time_dispatched: 2026-10-02T16:15:15Z
timestamp_note: stamped from the system clock at write, not typed
source: Will-Telegram
origin: ["Will-Telegram msg 4866 (2026-10-02 ~16:11Z): First Squawk X headline 'TD SEES FED HIKES IN DECEMBER AND MARCH, PREVIOUSLY OCTOBER AND JANUARY' (posted before an 11:19 ET screenshot)", "fxstreet.com 'US dollar: Fed hiking path and data risks - TD Securities' 2026-09-28 (prior call: hikes in October and January), via WebSearch; the 10/02 TD note itself NOT read"]
domain: MACRO_INFLATION
cluster: FED_FRAMEWORK
entities: ["TD-Securities", "FOMC-2026-10-28", "Federal-Reserve"]
confidence: 0.75
confidence_language: "reports"
signal_type: context
safety_net: clear
verdict: "TD Securities moved its Fed call after the 10/02 payrolls miss: it now sees hikes in December and March, from October and January before (First Squawk headline 10/02; TD's 9/28 Oct+Jan call corroborated at FXStreet). A named dealer taking the 10/28 FOMC hike out of its base case."
precedence: ROUTINE
action: ["BOND"]
info: ["HENRY", "LIQUID", "CARL", "RED"]
dispatch_note: "Same hike-pricing thread as -001 / -007 (BOND action). BM-20261002-01 item 4. CARL, RED pull-complete."
---
# TD Securities now sees the next Fed hikes in December and March, not October and January

**Short version:** After the September payrolls miss (`-001`, +29K), **TD Securities pushed its Fed hike forecast back one meeting each.** It now expects hikes in **December and March**, where it previously expected **October and January** (First Squawk headline, 10/02 late morning). TD's earlier call is on record: FXStreet carried TD's "October and January" path on **9/28**. **So one named dealer has taken the 10/28 FOMC hike out of its base case.**

| | Before (TD, 9/28) | Now (TD, 10/02) |
|---|---|---|
| Next hike | October (10/28 FOMC) | **December** |
| Following hike | January | **March** |

## Caveats
- **TD's note was not read.** This is a one-line squawk headline. TD's reasoning (payrolls alone, or payrolls plus something else) is not known.
- One dealer's forecast, not market pricing. Futures-implied odds are not checked here, and **priced odds are ORACLE's domain.**
- It sits beside Jefferson (`-007`, 10/01, before the jobs print), who called inflation "too high" and did not commit to October.

## Requested action
**BOND:** fold it into the October hike read with `-001` and `-007`. HENRY, LIQUID, CARL, RED: information.
