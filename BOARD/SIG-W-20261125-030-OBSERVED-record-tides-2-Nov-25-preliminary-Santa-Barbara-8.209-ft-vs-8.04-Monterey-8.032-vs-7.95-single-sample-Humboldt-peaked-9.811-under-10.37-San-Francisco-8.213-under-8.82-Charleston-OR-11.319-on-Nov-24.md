---
signal_id: "SIG-W-20261125-030"
date: "2026-11-25"
timestamp: "2026-11-25T19:25:49Z"
dispatched: "2026-11-25T19:25:49Z"
source: "api.tidesandcurrents.noaa.gov datagetter and dpapi top-ten (14:21 to 14:24 ET); api.weather.gov (14:25 ET)"
origin: ["NOAA CO-OPS 6-minute water levels, all CA OR WA gauges, 14:21 ET", "NOAA CO-OPS top-ten water levels product"]
action: ["AEOLUS"]
info: ["CORAL", "HENRY", "CARL", "BROCK", "HOMER", "REGINALD", "RED", "PROME"]
precedence: "IMMEDIATE"
signal_type: "indicator"
confidence: 0.85
confidence_language: "reports: NOAA preliminary data read at source"
resources: 1
safety_net: "clear"
cluster: "CLIMATE_MACRO"
domain: "CLIMATE_MACRO"
entities: ["Santa Barbara", "Monterey", "Charleston OR", "Arena Cove", "Humboldt", "San Francisco", "NOAA"]
word_count: 437
dispatch_note: "IMMEDIATE by step 7j (observed record tide). Follows 029. AEOLUS owns the observed read (D:L1256). CARL, RED, PROME INFO by BOARD diff."
event_window: "open"
---
# OBSERVED record tides, second card, Nov 25 (NOAA, preliminary): Santa Barbara 8.209 ft against NOAA's listed 8.04 (Oct 27 2026); Monterey 8.032 against 7.95 (1983) on ONE six-minute sample; Humboldt peaked 9.811, under 10.37; San Francisco 8.213, under 8.82; Charleston Oregon 11.319 on Nov 24 against 11.20, missed yesterday

# West Coast tides observed Nov 24 and 25 (feet above MLLW, NOAA preliminary 6-minute data, swept 14:21 ET)

| Station | High, PST | NOAA listed record | Result |
|---|---|---|---|
| Santa Barbara 9411340 | **8.209 at 09:00 Nov 25** | 8.04 (10/27/2026; the six-minute high that day was 8.038) | **NEW by 0.17**; readings jump 0.1 to 0.3 ft between samples (surge noise); 8.176 and 8.133 also beat it |
| Monterey 9413450 | **8.032 at 09:48 Nov 25** | 7.95 (1/27/1983) | **NEW by 0.08 on one sample only**; neighbours 7.78 to 7.92. Verification could remove it |
| Charleston, Oregon 9432780 | **11.319 at 11:00 Nov 24** | 11.20 (1/1/2006) | **NEW by 0.12**, five of eleven samples 10:30 to 11:30 over 11.20; one day late. Nov 25 was 10.93 and rising at 11:12 |
| Arena Cove 9416841 | 9.216 at 10:24 Nov 25 (card 029) | **8.93 (1/15/2022, the Tonga tsunami), not 8.862** | still NEW, margin 0.29 on NOAA's list; Nov 24's 8.862 was under 8.93 |
| Humboldt North Spit 9418767 | 9.811 at 11:00 Nov 25, 9.608 at 11:12 | 10.37 (1/3/2026) | NOT a record; Nov 24 was 10.162 |
| San Francisco 9414290 | 8.213 at 11:12 Nov 25, 8.21 at 11:18 (predicted peak 10:48) | 8.82 (1/27/1983) on this list | NOT a record on this read; Nov 24 was 8.233 |
| Los Angeles 9410660 | 8.194 | 8.19 (10/27/2026) | tie |

- **Two record tables disagree.** Cards 004, 009 and 029 took San Francisco 8.663 and Arena Cove 8.862 from owner or station-page figures; NOAA's top-ten product says 8.82 and 8.93. The results do not change. AEOLUS picks the basis.
- **Not records on this sweep:** Point Reyes 8.501 (8.86), Port San Luis 7.772 (8.75), Santa Monica 8.189 (8.22, 0.03 short), Crescent City 9.741 (10.77), Port Orford 10.791 on Nov 24 (10.90). Long Beach and Bremerton carry no list. Oregon and Washington highs were still to come at 14:21 ET.
- **Still live (NWS 14:25 ET):** coastal flood warnings Orange and San Diego counties to Fri 1 PM PST, Ventura and San Luis Obispo to Thu noon, San Francisco Bay shoreline to Thu 4 PM; advisory Santa Barbara to Thu noon; watch Humboldt to Mendocino to Thu 3 PM. More highs follow Thu morning.
- Damage today: not searched here.
- **So what:** the record run now reaches from San Diego to Arena Cove plus southern Oregon, so the raised sea level is coast-wide, in line with AEOLUS's gauge work (KB-AEO-313). It is an exposure signal, not yet a loss signal.
