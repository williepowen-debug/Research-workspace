---
signal_id: "SIG-W-20261124-004"
date: "2026-11-25"
timestamp: "2026-11-25T03:33:16Z"
dispatched: "2026-11-25T03:33:16Z"
source: "CO-OPS water_level and high_low APIs (9416841, 9418767, 9419750, 9414290); NWS coastal flood warnings sent 2026-11-24 13:27 to 17:51 PST; Lost Coast Outpost 2026-11-23 15:14 PST (helper read)"
origin: ["Charter step 7j flood check, 2026-11-24 22:27 ET"]
action: ["AEOLUS"]
info: ["WATT", "SHADE", "CORAL", "PROME"]
precedence: "IMMEDIATE"
signal_type: "threshold-crossed"
confidence: 0.85
confidence_language: "official gauge and warning text; 'above all found' is a claim about the highs WALTER read"
resources: 1
safety_net: "clear"
cluster: "CLIMATE_MACRO"
domain: "CLIMATE_MACRO"
entities: ["Arena Cove", "Humboldt Bay", "San Francisco", "CO-OPS", "NWS"]
word_count: 324
dispatch_note: "IMMEDIATE (step 7j, observed level above highest found). ACTION AEOLUS; INFO WATT, SHADE, CORAL; PROME by BOARD diff. Corrects the expectation on 20261123-030 (a forecast, not a miss: not a correction of 030's text)."
event_window: "open"
---
# California coast Tue Nov 24: Arena Cove observed 8.86 ft MLLW, above the 8.67 ft listed record (1998) and every later high WALTER read; Humboldt (North Spit) 10.16 ft, under January's 10.36; San Francisco 8.23 ft with 8.5 forecast Wed, 'approaching the highest tide ever recorded'

# California tides, Tue Nov 24 (CO-OPS verified-pending data) and Wednesday's forecast

| Gauge | Observed high 11/24 | Highest found before | Reads as | Forecast Wed Nov 25 (NWS) |
|---|---|---|---|---|
| Arena Cove (9416841) | **8.862 (9:24 AM PST)** | 8.67 listed (1998-02-06); later highs read: 8.65 (Jan 3 2026), 8.55 (Jan 2023), 8.43 (Dec 2024) | **above all found** | not read |
| North Spit, Humboldt (9418767) | 10.162 (10:18 AM PST) | 10.36 (Jan 3 2026) | under | 10.0 to 10.4, straddles 10.36 |
| Crescent City (9419750) | 10.062 (10:00 AM PST) | 10.66 listed (1983) | under | not read |
| San Francisco (9414290) | 8.233 (10:06 AM PST) | record not read by WALTER | not established | 8.5 ft at 10:49 AM Wed, 'approaching the highest tide ever recorded' (NWS text) |

- **Why IMMEDIATE:** an observed level above the highest found at Arena Cove (step 7j, routing v0.53). Preliminary water-level data; NOAA verifies later; other years were not all read. Card 030's Humboldt forecast (10.3 to 11.0) was NOT met: the high was 10.16.
- **Still live:** Coastal Flood Warnings for Humboldt, Del Norte, southwest Humboldt and Mendocino from 9 AM to 1 PM PST Wed ('major flooding in low lying areas mainly around Humboldt Bay'; waves up to 25 feet); San Francisco and San Pablo shorelines to Thu 4 PM PST (up to 2.7 ft inundation; High Surf Warning, 20 to 30 foot waves, midnight Tue to midnight Wed); Point Reyes to Big Sur Wed; Orange and San Diego to Fri; San Luis Obispo to Ventura to Thu noon.
- **King Salmon (Humboldt):** a local outlet reported an evacuation order effective 7:00 AM PST Tue and a proclaimed local emergency (Lost Coast Outpost 11/23, read by a helper); damage after the tide not read.
- **One card per state per check;** Florida is on 005.

Economic channel is AEOLUS's read.
