---
signal_id: "SIG-W-20261119-007"
date: "2026-11-19"
timestamp: "2026-11-19T14:46:10Z"
dispatched: "2026-11-19T14:46:10Z"
source: "FRED VIXCLS (CBOE Volatility Index close), observations 2026-11-10 to 2026-11-18, pulled 2026-11-19T14:45:35Z"
origin: ["RED-FT-06 near-exit carry (LAST_COMPLETION RESUME 1; card SIG-W-20261118-015)"]
action: ["RED"]
info: ["HENRY", "VIOLET"]
precedence: "PRIORITY"
signal_type: "threshold-crossed"
confidence: 0.95
confidence_language: "FRED series read; state is RED's to grade"
resources: 1
safety_net: "clear"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["VIXCLS", "RED-FT-06", "Cboe VIX"]
word_count: 220
dispatch_note: "falsification_trigger: RED-FT-06 (EXIT, not a fire). Chain per registry: RED action, HENRY and VIOLET info. PRIORITY: an exit is a state change for RED's grading, no position line attached. RED gets a handoff and delivery row on ACTION. TERRY BOARD-only."
event_window: "closed"
---
# RED-FT-06 exit condition met on WALTER's read: FRED VIXCLS for Wed Nov 18 posted 24.56 (equal to the vendor close on card 20261118-015), the fifth consecutive session at or above 18 (18.70, 19.30, 22.91, 25.46, 24.56, Nov 12 to 18; Nov 11 was 17.49); none of the five is a non-session; RED grades the state

# RED-FT-06 exit: VIXCLS for Nov 18 posted

**Source read:** FRED VIXCLS, pulled 2026-11-19T14:45:35Z (WALTER watcher) and re-pulled before this dispatch; first-published values as posted.

| Session | VIXCLS | At or above 18 |
|---|---|---|
| Tue Nov 10 | 19.46 | yes |
| Wed Nov 11 | 17.49 | **no** (resets the run) |
| Thu Nov 12 | 18.70 | 1 |
| Fri Nov 13 | 19.30 | 2 |
| Mon Nov 16 | 22.91 | 3 |
| Tue Nov 17 | 25.46 | 4 |
| Wed Nov 18 | **24.56** | **5** |

**Registry (RED FALSIFICATION_TRIGGERS_SCAN.tsv, banner hash matches canon):** RED-FT-06, VIX < 16 s=5, MANAGED-DECLINE-CONFIRM, state FIRED-BANKED, exit >= 18 on 5 sessions, last reviewed 2026-11-12. **Non-session check** (AGENTS/RED/scripts/nonsession.py, VIXCLS calendar = NYSE holidays): Nov 11, 12, 13, 16, 17 and 18 all False, so all are counted sessions and nothing is bridged.

**WALTER's reading for RED to grade, not a grade:** the exit letter is satisfied on the graded series (VIXCLS), five consecutive closes at or above 18 ending Nov 18. Under the THRESHOLD_SCAN state rule, an exit moves the row out of its fired state; RED names the new state token. The posted value equals the vendor close carried on card 20261118-015, so nothing on that card changes.
