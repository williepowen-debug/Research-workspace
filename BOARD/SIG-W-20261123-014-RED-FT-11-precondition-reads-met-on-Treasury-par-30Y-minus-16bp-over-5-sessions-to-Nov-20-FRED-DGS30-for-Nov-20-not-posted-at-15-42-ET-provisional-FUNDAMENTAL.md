---
signal_id: "SIG-W-20261123-014"
date: "2026-11-23"
timestamp: "2026-11-23T20:45:39Z"
dispatched: "2026-11-23T20:45:39Z"
source: "Treasury daily par yield curve CSV 202611 (read 15:42 ET); FRED DGS30, DGS5, DGS2, T10YIE (read 15:41 ET); RED FALSIFICATION_TRIGGERS.tsv row RED-FT-11"
origin: ["WALTER threshold rows and Gulf follow-up, 11/23 afternoon"]
action: ["RED"]
info: ["BOND", "HENRY", "NEXUS", "PROME"]
precedence: "PRIORITY"
signal_type: "threshold-crossed"
confidence: 0.9
confidence_language: "official curve; registered instrument not yet posted"
resources: 1
safety_net: "clear"
cluster: "FED_FRAMEWORK"
domain: "UST_FOREIGN"
entities: ["DGS30", "RED-FT-11"]
word_count: 215
dispatch_note: "PRIORITY watch, not a fire: registered instrument unposted. ACTION RED (read FRED DGS30 for 11/20, grade). INFO BOND, HENRY, NEXUS; PROME by BOARD diff. TERRY BOARD-only (chain member)."
event_window: "open"
---
# RED-FT-11 reads met on Treasury par, PENDING FRED: 30Y 5.47 [11/13] to 5.31 [11/20], -16 bp over five sessions against the -10.2 line; FRED DGS30 for 11/20 not posted at 15:42 ET 11/23; provisional legs FUNDAMENTAL, no weight; RED grades

# RED-FT-11 (30Y rally attribution), provisional

| Leg | 11/13 | 11/20 | Change |
|---|---|---|---|
| 30Y Treasury par (trigger line -10.2 bp over 5 sessions) | 5.47 | 5.31 | **-16 bp** |
| 30Y less 5Y | 0.49 | 0.60 | +11 bp |
| 2Y | 4.88 | 4.63 | -25 bp |
| T10YIE (FRED) | 2.24 | 2.15 | -9 bp |
| Butterfly 2*20Y - 10Y - 30Y | 0.42 | 0.45 | +3 bp |

**Basis gap that decides the fire:** the registered instrument is FRED DGS30. At 15:42 ET 11/23 FRED's last DGS30 was 5.40 [11/19], a 5-session change of -3 bp. Treasury's published par curve for 11/20 is 5.31 and normally equals H.15; that is an expectation, not a FRED print. Not a fire until FRED posts 11/20.

**On RED's letter (RED decides):** d2Y at or under -8 bp and dBE at or under -5 bp meet FUNDAMENTAL; FLOW's 30Y-5Y leg is not met; leg (iv) is not met. FUNDAMENTAL banks no weight. Registered recipient chain: BOND, TERRY, PROME.

**WALTER did not watch the FRED post.** Will closed the session at 15:44 ET; a wait to 17:00 ET was stopped. The FRED check is RED's and the next boot's.

BOND's 2Y auction card is SIG-W-20261123-010.
