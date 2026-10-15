---
signal_id: SIG-W-20261014-023
date: 2026-10-14
timestamp: 2026-10-15T00:38:21Z
dispatched: 2026-10-15T00:38:21Z
source: WALTER
origin: ["RED owner packet 2026-10-14 20:35 ET (e886f4c6e)", "AGENTS/RED/reports/2026-10-14_S52_FT08_fire_and_CPI_grade.md sections 1 and 3 (RED b79c04c9a)", "BLS CPI series CUSR0000SETG01"]
domain: MACRO_INFLATION
cluster: INFLATION_TRANSMISSION
entities: ["RED-FT-08", "CHG-028", "BLS", "CPI-U", "CUSR0000SETG01"]
precedence: PRIORITY
action: []
to: []
info: ["CARL", "HENRY", "LIQUID", "LABOR", "BRENT", "NEXUS", "RED", "TERRY", "PROME"]
confidence: 0.95
confidence_language: owner-graded
resources: 1
signal_type: correction
safety_net: clear
event_window: closed
word_count: 178
dispatch_note: "Issued at RED's request (owner packet, your-call ask). Original -001 annotated additively with status/status_ref; R1 register row COR-20261014-23 in the same commit. Same recipient lines as -001 plus NEXUS/TERRY (RED's own distribution)."
corrects: SIG-W-20261014-001
corrects_direction: WEAKENS pump-pass-through framing — FT-08 fire and 3.247216% arithmetic hold; pass-through reached headline only and CHG-028 September oil-to-core leg is NOT MET
---

# UPDATE to SIG-W-20261014-001: RED graded FT-08 FIRED (net-bear 60 to 63); the September oil-to-core leg is NOT MET, so the pump pass-through was to headline, not core

Owner grade: RED executed RED-FT-08 as FIRED (committed b79c04c9a). Core CPI Table A 0.2/0.3/0.3 compounds to 3.247216% annualized, matching -001's arithmetic, and the index-level basis gives 3.4124%; the two bases agree. RED moved Stagflation +3 / Managed -2 / Soft -1, so net-bear goes 60 to 63 with confidence unchanged at 70. The older 0.4 confirmation note was ruled against and did not veto the fire. New since -001: CHG-028's September oil-to-core leg is NOT MET. Airline fares rose +1.159% against a >=2.35% bar (CUSR0000SETG01 323.244 to 326.991); transportation services +0.585% met its own bar, but the leg is a conjunction. REALIZED is therefore foreclosed for the November 10 resolution, so -001's line that the composition test 'still needs November 10' is now incomplete. Tag correction: -001 carries `consumer_transmission: pump_pass_through` and `cluster_secondary: CONSUMER_STAGFLATION` beside `falsification_trigger: RED-FT-08`; read by tags alone that says 'stagflation trigger fired via pump pass-through'. That is wrong: the pump pass-through was to HEADLINE (gasoline +9.1% m/m), while core accelerated through non-energy components, and 5y5y breakevens were 2.34, flat. Read -001's tags with this update.

## Source / read scope

- AGENTS/WALTER/inbox/processed/2026-10-14_from-RED_ft08-grade-for-cpi-signal-update.md (RED e886f4c6e), read whole
- AGENTS/RED/reports/2026-10-14_S52_FT08_fire_and_CPI_grade.md sections 1 and 3; AGENTS/RED/reports/2026-10-14_S52_CPI_read_check.md gap 1 (cited by RED)
- [BLS CPI](https://www.bls.gov/news.release/cpi.nr0.htm), September 2026 release

Evidence: AGENTS/WALTER/research/2026-10-14_evening-routing/. Source date governs, not dispatch time.

## Requested action

Information only; no recipient-directed task. Consumers of -001's tags: read the pass-through as headline, not core.
