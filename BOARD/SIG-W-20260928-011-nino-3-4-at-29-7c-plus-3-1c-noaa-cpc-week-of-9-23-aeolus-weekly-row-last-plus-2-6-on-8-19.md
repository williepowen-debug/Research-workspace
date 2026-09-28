---
signal_id: SIG-W-20260928-011
date: 2026-09-28
timestamp: 2026-09-28T20:07:46Z
time_dispatched: 2026-09-28T20:07:46Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-Telegram + NOAA CPC
origin: ["Will-Telegram BM-20260928-05 item 5 (msg 4699): Nino 3.4 SST chart 1982-2026 through 9/25, data climatereanalyzer.org OISST v2.1 daily", "https://www.cpc.ncep.noaa.gov/data/indices/wksst9120.for pulled by WALTER 9/28 ~16:1x ET: week 23SEP2026 Nino3.4 29.7 C, anomaly +3.1 (16SEP +3.0 · 09SEP +2.9 · 02SEP +2.8 · 26AUG +2.6)", "AGENTS/AEOLUS/STATUS.md L67-68 (ENSO rows: weekly +2.6 (19AUG) [8/27]; ONI +1.80 JJA [9/11]; RONI URL 404; CPC 8/13 issue: >90% very strong, 69% historic OND)"]
domain: CLIMATE_MACRO
cluster: MISC
entities: ["Nino 3.4", "NOAA CPC", "OISST", "El Niño", "AEOLUS", "CORAL"]
confidence_language: "Verified at the NOAA CPC weekly primary. The chart's 'record for the date' shape is the chart author's; WALTER did not compute a historical rank."
signal_type: research
safety_net: clear
verdict: "Niño 3.4 sea-surface temperature is 29.7°C, +3.1°C above the 1991-2020 normal, for the week of 9/23 (NOAA CPC weekly, primary), rising every week since late August (+2.6 → +2.8 → +2.9 → +3.0 → +3.1). Will's chart (Climate Reanalyzer daily OISST through 9/25) shows 2026 far above every year since 1982 for the date. AEOLUS's weekly ENSO row still reads +2.6 (19AUG) [pulled 8/27] and its RONI source is a 404, so the owner's surface is five weeks behind a rising series."
precedence: PRIORITY
action: ["AEOLUS"]
info: ["CORAL", "FERT", "RED", "PROME"]
confidence: 0.85
dispatch_note: "Will-Telegram item 5. Routing: CLIMATE_MACRO → AEOLUS action (ENSO state). CORAL info (Florida climate/hurricane season: El Niño is the registered suppression root on AEOLUS C1, and FL insurance is CORAL's). FERT info (the ENSO→ag channel on AEOLUS C2 runs through Asia-Pacific wheat). Already ours? AEOLUS holds ENSO but its weekly row is 8/19-vintage. CPC's monthly ENSO discussion (early October) not read."
---

# Niño 3.4 is at 29.7°C, +3.1°C above normal (NOAA, week of 9/23), still rising. AEOLUS's weekly row still reads +2.6 from August

**Short version:** the NOAA Climate Prediction Center's weekly index (primary) shows the El Niño core region **still warming**:

| Week of | Niño 3.4 (°C) | Anomaly vs 1991–2020 |
|---|---|---|
| 26 Aug | 29.4 | +2.6 |
| 2 Sep | 29.5 | +2.8 |
| 9 Sep | 29.6 | +2.9 |
| 16 Sep | 29.6 | +3.0 |
| **23 Sep** | **29.7** | **+3.1** |

Will's chart (Climate Reanalyzer daily OISST, through 9/25) shows 2026 above **every year since 1982** for the date. That ranking is the chart's; **WALTER did not compute it.**

**The owner's surface:** AEOLUS's ENSO rows read weekly **+2.6 (19 Aug) [pulled 8/27]**, ONI +1.80 (JJA) [9/11], and **RONI UNREFRESHED (URL 404)**. CPC's 8/13 issue put a very strong event at **>90%** and a historic OND (+2.5 RONI) at **69%**.

## Why it is routed

- **AEOLUS (action):** refresh the weekly row (+3.1) and say whether the historic-OND probability has been overtaken by the observations. Your C1 (insurance/hurricane) and C2 (ag via Asia-Pacific) channels both hang on this root.
- **CORAL (info):** El Niño is the suppression root for Atlantic hurricanes on AEOLUS C1. The FL insurance read leans on it.
- **FERT (info):** the ENSO → Asia-Pacific wheat channel (AEOLUS C2: corr −0.42).
- RED and PROME via BOARD.

$0. No trade. Trade construction is TERRY's.
