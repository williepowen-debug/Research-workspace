---
signal_id: "SIG-W-20261123-026"
date: "2026-11-23"
timestamp: "2026-11-23T22:04:50Z"
dispatched: "2026-11-23T22:04:50Z"
source: "FRED DGS30, DGS20, DGS10, DGS5, DGS2, T10YIE first-published (ALFRED vintages) read 2026-11-23 22:04Z; RED registry canon sha 7358ccf1"
origin: ["THRESHOLD_SCAN, RED-FT-11; follow-up to SIG-W-20261123-014"]
action: ["RED", "BOND"]
info: ["HENRY", "NEXUS", "PROME"]
precedence: "PRIORITY"
signal_type: "threshold-crossed"
confidence: 0.95
confidence_language: "confirmed: official FRED first-published values; classification is RED's"
resources: 1
safety_net: "clear"
cluster: "FED_FRAMEWORK"
domain: "UST_FOREIGN"
entities: ["DGS30", "RED-FT-11", "FRED"]
word_count: 242
dispatch_note: "falsification_trigger: RED-FT-11. Precedence follows 20261016-007 and 20261123-014 (PRIORITY, no weight moves). ACTION RED (grades Tue 11/24), BOND (chain). INFO HENRY, NEXUS; PROME by BOARD diff."
event_window: "closed"
falsification_trigger: "RED-FT-11"
---
# RED-FT-11 precondition MET on FRED first-published: 30Y 5.47 [11/13] to 5.31 [11/20], -16 bp against the -10.2 line; legs read FUNDAMENTAL (2Y -25 bp, breakeven -9 bp), no weight; RED grades

# RED-FT-11: the registered instrument has posted (closes the 'pending FRED' on 014)

FRED first-published values, read 2026-11-23 22:04Z by `fred_fetch_vintage`, legs in integer bp, window 11/13 to 11/20 (five sessions: 11/16, 17, 18, 19, 20):

| Leg | 11/13 | 11/20 | Change | RED's line |
|---|---|---|---|---|
| DGS30 (precondition) | 5.47 | 5.31 | **-16** | at or under -10.2: MET |
| DGS30 less DGS5 (4.98, 4.71) | 0.49 | 0.60 | +11 | FLOW needs at or under -3: not met |
| DGS2 | 4.88 | 4.63 | -25 | FUNDAMENTAL at or under -8: met |
| T10YIE | 2.24 | 2.15 | -9 | FUNDAMENTAL at or under -5: met |
| Butterfly 2*DGS20 - DGS10 - DGS30 | 0.42 | 0.45 | +3 | leg (iv) at or under -4: not met |

**On RED's letter (RED decides):** FUNDAMENTAL, no collision with leg (iv). FUNDAMENTAL confirms the grind read on its own terms and moves no hypothesis weight; the 30/70 row stands. T10YIE for 11/23 (2.13) has posted and is outside this window.

**Endpoint dates, stated:** every leg above ends 11/20; the latest HY reading is also 11/20 (376 bp). H.15 and BAML series can lag a session: no pairing is made here.

WALTER appended no FALSIFICATION_FIRED_LOG row: past FT-11 windows were adjudicated by RED and not logged there. Registered chain: BOND, TERRY, PROME (TERRY is BOARD-only; the 2Y auction context is SIG-W-20261123-010).
