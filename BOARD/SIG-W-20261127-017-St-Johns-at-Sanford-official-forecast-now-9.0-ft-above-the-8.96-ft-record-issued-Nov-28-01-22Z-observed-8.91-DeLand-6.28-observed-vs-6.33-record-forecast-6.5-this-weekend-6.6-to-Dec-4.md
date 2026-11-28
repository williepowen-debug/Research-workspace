---
signal_id: "SIG-W-20261127-017"
date: "2026-11-28"
timestamp: "2026-11-28T03:38:33Z"
dispatched: "2026-11-28T03:38:33Z"
source: "api.water.noaa.gov/nwps/v1/gauges/SNFF1/stageflow and /DLAF1/stageflow (read 2026-11-28T03:35:45Z); api.water.noaa.gov/nwps/v1/gauges/SNFF1 and DLAF1 (crest history); api.weather.gov/alerts/active?area=FL (read 03:35:32Z)"
origin: ["NWPS api.water.noaa.gov SNFF1 and DLAF1 stageflow and gauge records, read 2026-11-28T03:35:45Z", "api.weather.gov alerts FL, Flood Warnings sent 20:34 to 20:58 ET 11/27, read 2026-11-28T03:35:32Z"]
action: ["CORAL"]
info: ["AEOLUS", "SHADE", "HOMER", "REGINALD", "MARCO", "RED", "PROME"]
precedence: "IMMEDIATE"
signal_type: "threshold-crossed"
confidence: 0.95
confidence_language: "confirmed: NWS and NWPS primary read directly; the record crossing is a forecast"
resources: 1
safety_net: "clear"
cluster: "CLIMATE_MACRO"
domain: "CLIMATE_MACRO"
entities: ["St. Johns River", "Sanford", "DeLand", "Astor", "Lake Harney", "Cocoa", "Seminole County", "Volusia County", "NWS", "NWPS"]
word_count: 412
dispatch_note: "IMMEDIATE by step 7j and card 003's registered line (official Sanford forecast at or above 8.96). Florida: CORAL action, AEOLUS info; other recipients as 003. RED, PROME by BOARD diff."
event_window: "open"
---
# St. Johns at Sanford: the official NWS forecast issued 20:22 ET Fri Nov 27 now crests at 9.0 ft (Sat Nov 28 07:00 ET), ABOVE the 8.96 ft record (Oct 9, 2022), then 8.9 to 9.0 through early next week; observed 8.91 ft at 21:30 ET, 0.05 ft under it. DeLand observed 6.28 ft (record 6.33), forecast 6.5 ft this weekend and 6.6 ft to Fri Dec 4. Sanford becomes the second gauge forecast above its record

# Florida flood check, Fri Nov 27 night (update to 20261127-003)

| Gauge | Observed (NWPS) | Official forecast (issued 01:22Z Nov 28 = 20:22 ET Nov 27) | Record (NWPS crest history) | Change since 20261127-003 |
|---|---|---|---|---|
| **Sanford (SNFF1)** | **8.91 ft at 02:30Z (21:30 ET)**, the highest in the observed series returned | **9.0 ft at 12:00Z Sat Nov 28 (07:00 ET)**; NWS warning 20:47 ET: crest 9.0 ft, then steady 8.9 to 9.0 'through at least early next week'; 8.8 by Dec 5 | **8.96 ft (2022-10-09)** | forecast 8.9 to **9.0, above the record** (NEW); observed 8.86 to 8.91 |
| DeLand (DLAF1) | 6.27 to 6.28 ft, 01:45Z to 02:30Z | 6.3 overnight; NWS 20:52 ET: 6.5 ft late this weekend, 6.6 ft early next week, steady into mid-week; series maximum 6.6, last point 6.5 at 00:00Z Dec 5 | 6.33 ft (2022-10-11) | observed 6.25 to 6.28; forecast timing earlier (6.5 this weekend) |
| Astor (ASTF1) | 4.4 ft at 20:30 ET (NWS); 24-hour max 4.5 | steady 4.3 to 4.4 through early next week | 4.81 ft (2024-10-12, as carried on 003) | small fall |
| Above Lake Harney | 13.1 ft at 19:30 ET, above its old record | very slow decline from this weekend | | continuing state |
| Cocoa 9W | 18.2 ft at 19:15 ET, above its old record | very slow decline to 17.8 ft | | continuing state |

- **Why IMMEDIATE:** card 003 registered it: 'an official Sanford forecast at or above 8.96 is a new IMMEDIATE' (ROUTING_TABLE CLIMATE_MACRO, an officially forecast record river level). This forecast is 9.0 at one decimal; the NWPS series carries one decimal on this gauge, so the margin over the record is 0.04 ft and inside forecast error.
- **Limits:** a forecast, not an observation. Sanford has not observed a record; observed is 0.05 ft under it. DeLand has not observed one either (0.05 ft under). Record values read tonight from the NWPS gauge records (crest history), matching 003.
- **So what:** two Seminole and Volusia reach gauges are now forecast at or above records for most of next week, with Lake Harney and Cocoa already above theirs upstream. Sanford's 9.0 ft impact line: 'flooding becomes more significant to the Sanford waterfront area'. Disaster-declaration coverage of Volusia and Seminole was last read by AEOLUS 11/25 (KB-AEO-331) and by CORAL 00:13Z 11/28 (no DR-4956 amendment); not re-read here.
