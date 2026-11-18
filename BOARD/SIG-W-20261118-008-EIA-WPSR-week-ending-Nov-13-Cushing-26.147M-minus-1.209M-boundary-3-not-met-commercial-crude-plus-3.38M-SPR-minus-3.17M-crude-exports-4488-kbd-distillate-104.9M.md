---
signal_id: "SIG-W-20261118-008"
date: "2026-11-18"
timestamp: "2026-11-18T15:45:16Z"
dispatched: "2026-11-18T15:45:16Z"
source: "EIA WPSR week ending 2026-11-13, https://ir.eia.gov/wpsr/table1.csv and https://ir.eia.gov/wpsr/table4.csv (fetched 2026-11-18 before the 15:45:16Z dispatch (WPSR tables posted by 15:4xZ))"
origin: ["Boundary 3 scheduled read (CLAUDE.md 6c; BRENT docket/CATALYSTS.tsv row 2026-11-18 EIA WPSR)"]
action: ["BRENT"]
info: ["LIQUID", "HENRY", "RED", "CARL"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.95
confidence_language: "issuer tables read; SPR figure is WALTER's subtraction"
resources: 1
safety_net: "clear"
cluster: "HYDROCARBON_INFRA"
domain: "OIL_ENERGY"
entities: ["EIA", "WPSR", "Cushing", "SPR", "crude exports", "distillate", "gasoline"]
word_count: 233
dispatch_note: "Boundary 3 owner chain (BRENT -> LIQUID, HENRY, RED) at PRIORITY because the line was not crossed; BRENT's docket row for today names BRT-31, BRT-34 and its tracker. CARL info for the gasoline and distillate stock legs (pull). TERRY BOARD-only; RED and CARL INFO by BOARD."
event_window: "closed"
---
# EIA weekly petroleum status, week ending Nov 13 (released Wed Nov 18): Cushing 26.147 million barrels, down 1.209M (boundary 3, under 20M, NOT met); commercial crude 417.797M, up 3.380M; SPR about 276.4M, down about 3.17M (WALTER arithmetic: total less commercial); crude exports 4,488 kb/d, up 1,033; gasoline 215.949M, up 5.193M; distillate 104.901M, up 1.571M (BRT-34 line 95,000 not reached); BRENT grades BRT-31 and its tracker

# EIA Weekly Petroleum Status Report, week ending 2026-11-13

**Source read:** EIA tables at ir.eia.gov/wpsr/table1.csv and table4.csv, fetched 2026-11-18 before the 15:45:16Z dispatch (WPSR tables posted by 15:4xZ) (standard Wednesday release; the EIA open-data API still showed week ending Nov 6 at 15:44Z).

| Series | Week ending Nov 13 | Week ending Nov 6 | Change | Year ago (Nov 14, 2025) |
|---|---|---|---|---|
| Cushing crude stocks | 26.147 M bbl | 27.356 | -1.209 | 21.821 |
| Commercial crude (ex SPR) | 417.797 M bbl | 414.417 | +3.380 | 424.155 |
| Total crude incl. SPR | 694.158 M bbl | 693.952 | +0.206 | 835.081 |
| SPR (WALTER arithmetic: total less commercial) | about 276.361 M bbl | about 279.535 | about -3.174 | n/a |
| Crude exports | 4,488 kb/d | 3,455 | +1,033 | n/a in the row read |
| Total motor gasoline stocks | 215.949 M bbl | 210.757 | +5.193 | 207.391 |
| Distillate stocks | 104.901 M bbl | 103.330 | +1.571 | 111.080 |
| Crude production | 14,032 kb/d | 14,013 | +19 | n/a |

**Registered rows:** boundary 3 (Cushing under 20M, single print) NOT met: 26.147M, 6.1M above. BRT-34 (distillate under 95,000 kb): 104,901, not under. BRT-31 (week six; qualifies at or below 8,890 kb/d on BRENT's named weekly series): BRENT grades; WALTER did not identify the series and grades nothing.
