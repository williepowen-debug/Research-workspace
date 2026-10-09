---
signal_id: SIG-W-20261009-004
date: 2026-10-09
timestamp: 2026-10-09T14:02:47Z
time_dispatched: 2026-10-09T14:02:47Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["NHC TCU 7:20 AM CDT 10/9 (PRIMARY, fetched by WALTER sweep agent)", "NHC TCP 11A 7 AM CDT + TCD 11 4 AM CDT (PRIMARY)", "BSEE/MMA hurricane page (PRIMARY listing; no release newer than 10/8 11:00 CDT)", "FOX Weather live / Florida EO 26-202 (RELAY)", "CNBC 10/9 refinery story (403; search layer only)", "AGENTS/WALTER/research/2026-10-09_morning/morning-sweep.md §1"]
domain: CLIMATE_MACRO
cluster: CLIMATE_MACRO
entities: ["Hurricane-Isaias", "AL092026", "NHC", "BSEE-MMA", "Gulf-of-Mexico", "Pensacola", "Destin", "Pascagoula", "Chevron-Pascagoula", "Florida-Panhandle", "Mobile"]
precedence: IMMEDIATE
action: ["AEOLUS", "CORAL", "BRENT"]
info: ["SHADE", "HENRY", "REGINALD", "MARCO", "WATT", "RED", "PROME"]
confidence: 0.9
confidence_language: "NHC primary for intensity/warnings/surge; refinery and port status are search-layer and UNKNOWN"
signal_type: catalyst
safety_net: clear
event_window: closed
word_count: 420
dispatch_note: "Updates -1008-046. Its 'weaker at landfall' is still NHC's forecast, but the storm beat NHC's 18Z peak forecast six hours early and NHC names the upside risk; not correction-class. IMMEDIATE = acute landfall within ~12h on a Florida top-priority geography. Two-leg storm per ROUTING_CARVEOUTS (energy + FL): BRENT and CORAL both on action, neither buried. Next NHC advisory #12 at 10 AM CDT (15:00Z); next BSEE/MMA release ~18:00Z."
---

# Isaias is a MAJOR hurricane (Category 3, 120 mph, 959 mb) at 7:20 AM CDT, ahead of NHC's own peak forecast; landfall tonight or early Saturday between Ocean Springs MS and the Florida Panhandle; 6–9 ft surge forecast for Pensacola–Destin

| Item | Now | Source |
|---|---|---|
| Intensity | **120 mph, 959 mb (Category 3)**, 27.0N 87.6W, ~240 mi S of Pensacola, moving NNE 15 mph | NHC TCU 7:20 AM CDT 10/9 (recon + dropsonde) |
| Forecast | NHC Discussion 11 (4 AM CDT) forecast the 120 mph peak at 18Z; it arrived **~6h early**. Best forecast still **high-end Category 2 at landfall** as shear rises, but NHC writes that a ~6h delay in the shear "could bring a stronger hurricane ashore" | NHC TCD 11 |
| Landfall | **Tonight or early Saturday** in the Hurricane Warning area: **Ocean Springs MS → Bay/Gulf county line FL** | NHC TCP 11A |
| Surge | **6–9 ft AL/FL border → Grayton Beach (Pensacola, Navarre, Destin)**; 4–7 ft Grayton → Indian Pass; 4–6 ft Indian Pass → Steinhatchee and Dauphin Island → AL/FL; 3–5 ft Mobile Bay | NHC TCP 11A |
| Louisiana refining coast | Tropical-storm and surge warnings only; **no hurricane warning west of Ocean Springs** | NHC TCP 11A |
| Gulf shut-in | **Unchanged: 1,282,879 b/d oil (62.89%), 57.35% gas, 121 of 371 platforms** [survey 10/8]; no newer release; next ~18:00Z | BSEE/MMA |
| Refineries | **No cut announced.** Chevron **Pascagoula is inside the Hurricane Warning** (Ocean Springs is its western edge); "remains operational" per a search-layer quote of possibly 10/8 vintage | CNBC via search (403) |
| Ports / LOOP | **UNKNOWN**: no Isaias USCG Zulu or LOOP notice found. Search returned 2017–2021 and **2020-Isaias** items = date traps | — |
| Florida | State of emergency EO 26-202 (25 Panhandle/Big Bend counties, signed 10/6); Escambia/Okaloosa/Santa Rosa schools closed through Friday; long-duration outages forecast; up to 15 in. rain locally | FOX Weather / FL state (RELAY) |

**What changed since `-1008-046` (Cat 2, 100 mph):** stronger and sooner than forecast. The hurricane-force core aims at Mississippi, Alabama and the western Florida Panhandle, so **Florida's exposure is the storm's east side**, the side with the highest surge.

**CORAL (action):** Florida Panhandle surge and wind on insured property, coastal CRE, Panhandle banks, tourism. **AEOLUS (action):** macro read across insurance/reinsurance, energy and property. **BRENT (action):** Pascagoula and the Mobile/Pascagoula port complex sit inside the warning; Gulf shut-ins update ~18:00Z; any refinery cut. **Info:** SHADE (reinsurance), HENRY, REGINALD (Gulf Coast and Florida bank collateral), MARCO (Panhandle tourism), WATT (long-duration outages), RED, PROME.

⛔ **Date traps:** "Isaias makes landfall in North Carolina" and LOOP-suspension stories are the **2020** storm.
