---
signal_id: "SIG-W-20261022-029"
date: "2026-10-22"
timestamp: "2026-10-22T19:20:23Z"
dispatched: "2026-10-22T19:20:23Z"
source: "RESEARCH-INTAKE"
origin: "RESEARCH-INTAKE fred MORTGAGE30US; FRED pull"
domain: "CONSUMER_CREDIT"
cluster: "CONSUMER_STAGFLATION"
action: []
info: ["HOMER", "PROME"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.95
confidence_language: "FRED first-published"
resources: 1
safety_net: "clear"
word_count: 102
entities: ["Freddie-Mac", "PMMS", "MORTGAGE30US"]
event_window: "closed"
dispatch_note: "Level update on a row with no uncrossed rung; HOMER owns."
---
# Freddie Mac 30-year mortgage rate 7.32% (week of 10/22), down from 7.40% for two weeks; still above every HOMER rung (no uncrossed rung on this row)

FRED MORTGAGE30US (Freddie Mac PMMS), first published 10/22: **7.32%** [10/22] vs 7.40% [10/15], 7.40% [10/08], 7.28% [10/01]. The 8bp ease tracks the 10-year's fall toward 5.00% this week. HOMER's band rule has no uncrossed rung on 30-year PMMS, so this is a level update, not a fire. Routine; HOMER reads the issuer page itself on Thursdays.

HOMER INFO. PROME by BOARD. Source: FRED MORTGAGE30US pulled 10/22 19:2xZ (intake lane flagged it red on the level).
