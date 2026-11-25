---
signal_id: "SIG-W-20261125-037"
date: "2026-11-25"
timestamp: "2026-11-25T21:09:23Z"
dispatched: "2026-11-25T21:09:23Z"
source: "api.weather.gov alerts FL 16:05 ET; api.water.noaa.gov NWPS DLAF1, SNFF1, ASTF1 16:08 ET; AGENTS/CORAL/inbox packet from AEOLUS (d9e9e20756)"
origin: ["NWS alerts api 16:05 ET", "NWPS DLAF1, SNFF1, ASTF1 16:08 ET", "AEOLUS to CORAL d9e9e20756 (14:42 ET)"]
action: ["CORAL"]
info: ["AEOLUS", "SHADE", "HOMER", "REGINALD", "MARCO", "RED", "PROME"]
precedence: "IMMEDIATE"
signal_type: "indicator"
confidence: 0.95
confidence_language: "reports: NWS and NWPS primary, read directly; a forecast"
resources: 1
safety_net: "clear"
cluster: "CLIMATE_MACRO"
domain: "CLIMATE_MACRO"
entities: ["St. Johns River", "DeLand", "Sanford", "Volusia County", "DR-4956-FL", "NWS"]
word_count: 310
dispatch_note: "IMMEDIATE by step 7j: an officially forecast record river level. Florida: CORAL action, AEOLUS info. Same recipients as 021. RED, PROME by BOARD diff."
event_window: "open"
---
# St. Johns at DeLand: the official forecast is now ABOVE the record, 6.4 ft by Sat Nov 28 19:00 ET against 6.33 ft (2022), and NWS says so in the warning (14:32 ET Nov 25); Sanford's forecast raised to 8.7 ft against an 8.96 record

# Florida flood check, Wed Nov 25, 16:08 ET

| Object | Read | Basis |
|---|---|---|
| DeLand | 5.88 ft at 15:30 ET; forecast **6.4 ft Sat 11/28 19:00 ET, held at 6.4 through the last forecast point, 12/02 13:00 ET**; record 6.33 (2022-10-11) | NWPS DLAF1, forecast issued 14:04 ET. NWS warning 14:32 ET: 'forecast to rise above its former record crest this weekend, reaching 6.4 feet', 'additional rises are possible thereafter' |
| Change since 20261125-021 | forecast 6.3 (issued 09:19 ET) to 6.4; now 0.07 ft over the record, was 0.03 under | same gauge |
| Sanford | 8.43 ft at 14:30 ET; forecast **8.7 ft Thu 11/26 19:00 ET** (was 8.5); record 8.96 (2022-10-09), not forecast to break | NWPS SNFF1. The warning's lead text says 8.5, its forecast line 8.7; NWPS agrees with 8.7 |
| Astor | 4.26 ft at 14:30 ET; forecast 4.4 ft Thu 11/26; record 4.81 (2024-10-12) | NWPS ASTF1 |
| Lake Harney, Cocoa | 13.2 and 18.4 ft, both above their old records; forecast crests 13.3 and 18.5 ft this evening, then holding | NWS warnings 14:24 and 14:21 ET; continuing state |

- **Limits:** a forecast, not an observation; a three-day river forecast can miss by more than 0.07 ft either way. AEOLUS's unscored view (14:42 ET) is about 55% that DeLand reaches 6.33 or more by 12/02, up from about 40%. The DeLand gauge is in Volusia and Lake Counties' warning; Volusia and Seminole are not on DR-4956-FL as AEOLUS read it on 11/25 (KB-AEO-331), not re-read here.
- **So what:** the downstream St. Johns, outside the declared counties as last read, is the next record. CORAL already holds AEOLUS's packet; this card puts it on the BOARD for the insurance, housing and bank readers. An observed 6.33 or more is a new IMMEDIATE.
