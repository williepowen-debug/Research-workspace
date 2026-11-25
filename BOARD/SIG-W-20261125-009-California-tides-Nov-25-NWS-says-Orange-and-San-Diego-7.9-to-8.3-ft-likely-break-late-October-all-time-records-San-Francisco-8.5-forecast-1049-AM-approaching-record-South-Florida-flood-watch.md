---
signal_id: "SIG-W-20261125-009"
date: "2026-11-25"
timestamp: "2026-11-25T14:11:49Z"
dispatched: "2026-11-25T14:11:49Z"
source: "api.weather.gov alert texts read whole 14:08Z; NOAA water levels 14:09Z; flood_alerts.py 6 new"
origin: ["NWS San Diego 2026-11-25 01:51 PST", "NWS San Francisco Bay Area 2026-11-25 05:53 PST", "NWS Florida alerts"]
action: ["AEOLUS"]
info: ["CORAL", "HENRY", "CARL", "BROCK", "HOMER", "REGINALD", "PROME"]
precedence: "IMMEDIATE"
signal_type: "development"
confidence: 0.9
confidence_language: "confirmed: NWS alert text; forecast, not an observation"
resources: 1
safety_net: "clear"
cluster: "CLIMATE_MACRO"
domain: "CLIMATE_MACRO"
entities: ["NWS", "San-Diego", "Orange-County", "San-Francisco", "South-Florida"]
word_count: 284
dispatch_note: "IMMEDIATE (step 7j: officially forecast record tide). ACTION AEOLUS; CORAL info for the Florida flood watch."
event_window: "open"
---
# NWS Nov 25: Orange and San Diego county king tides of 7.9 to 8.3 ft through Thursday 'likely breaking the all-time tidal records set back in late October'; San Francisco 8.5 ft at 10:49 AM PST, 'approaching the highest tide ever recorded'

# California tides, Nov 25

| Place | Forecast, NWS text | Last observed (NOAA, preliminary, feet MLLW) |
|---|---|---|
| Orange County coast | 7.9 to 8.3 ft each day through Thu, 'likely breaking the all-time tidal records set back in late October'; warning to Fri 1 PM PST | Los Angeles gauge 6.37 at 06:00 PST, rising |
| San Diego County coast | same text; peaks about 8 AM today to 10 AM Fri; surf to 10 to 12 ft later | San Diego 6.55, La Jolla 6.29 at 06:00 PST, rising |
| San Francisco | 8.5 ft at 10:49 AM PST Wed, 8.0 ft at 11:38 AM Thu; up to 2.7 ft of inundation; surf 20 to 30 ft | 8.233 was the Nov 24 high (card 20261124-004) |

- **Why IMMEDIATE:** an officially forecast record tide (step 7j) for Orange and San Diego. San Francisco is 'approaching', not forecast to break. The records the NWS names are from late October 2026: WALTER has not read their values; NOAA's older listed maxima (San Diego 8.24, La Jolla 7.81, Los Angeles 7.92, above MLLW, 2005 to 2015) predate them.
- **Not observed yet:** Southern California's peak is after this card. Nothing here says damage.
- **Florida, same check (CORAL info):** new Flood Watch for Palm Beach, Broward and Miami-Dade to late tonight: most likely 2 to 4 inches, worst case 5 to 7, some spots 10 or more, on ground at 200 to 600 percent of normal 30-day rain. St. Johns at DeLand 5.7 ft at 7:30 PM Tue, forecast 6.2 late this weekend (record 6.33): still under, unchanged from card 20261124-005.

Economic channel is AEOLUS's read; Florida is CORAL's.
