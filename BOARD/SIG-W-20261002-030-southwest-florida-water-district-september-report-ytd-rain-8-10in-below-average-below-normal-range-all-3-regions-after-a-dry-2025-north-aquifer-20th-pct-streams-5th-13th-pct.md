---
signal_id: SIG-W-20261002-030
date: 2026-10-02
timestamp: 2026-10-02T21:02:04Z
time_dispatched: 2026-10-02T21:02:04Z
timestamp_note: stamped from the system clock at write, not typed
source: Will-Telegram (link) + SWFWMD primary PDF
origin: ["Will-Telegram msg 4889 (2026-10-02 21:00Z): X post @swfwmd 2026-10-02 19:50:50Z linking the report", "SWFWMD 'September Water Resource Monthly Update' PDF (swfwmd.state.fl.us/sites/default/files/medias/documents/September%20Monthly%20Water%20Resource_0.pdf), downloaded and read whole ~21:0xZ; page 3 table alignment checked against the rendered page"]
domain: CLIMATE_MACRO
cluster: MISC
entities: ["SWFWMD", "Florida", "Tampa-Bay", "Floridan-Aquifer", "Peace-River", "Withlacoochee-River"]
confidence: 0.9
confidence_language: "reports"
signal_type: context
safety_net: clear
verdict: "SWFWMD September 2026 water report (posted 10/02): January-September rainfall is 8.3-10.1 in below the historic average and below the normal range in all three regions (North 37.71 vs 45.98, Central 36.11 vs 45.08, South 35.27 vs 45.39), on top of a 2025 that finished 11-15 in below average. September alone was below average but inside the normal range. North aquifer 20th percentile (below normal; Central 31, South 29); four of five gauged rivers below normal (Peace at Bartow 5th, Withlacoochee 8th and 13th pct); Northern lakes 3.89 ft below their minimum low management level. Every lake and river reading improved on August."
precedence: ROUTINE
action: ["CORAL"]
info: ["AEOLUS", "RED"]
dispatch_note: "FL climate carve-out: Florida-named climate/water -> CORAL action; AEOLUS info (US water-scarcity lane; FL handoff to CORAL unchanged, reconcile to one FL figure). Companion to -020 (wet-pattern forecast) with a GEOGRAPHY caveat: -020's heavy rain is Panhandle/Big Bend, this deficit is SW Florida. Single Will link, no batch manifest. RED pull-complete."
---
# Southwest Florida is ~8–10 inches short of normal rain this year, after a dry 2025. September helped a little.

**Short version:** The **Southwest Florida Water Management District** (SWFWMD: the 16 counties around Tampa Bay, Polk and Sarasota) published its September report on 10/02. **Rain since January is 8–10 inches below average in all three of its regions and below the normal range**, and **2025 was already 11–15 inches short.** September itself was below average but inside the normal range, and **every river and lake reading improved on August.**

| Measure (SWFWMD, as of 9/30, provisional) | North | Central | South |
|---|---|---|---|
| Rain Jan–Sep, actual vs historic average | **37.71 vs 45.98 in (−8.27)** | **36.11 vs 45.08 (−8.97)** | **35.27 vs 45.39 (−10.12)** |
| Normal range Jan–Sep (25th–75th pct) | 41.38–50.49 → **below** | 40.00–48.62 → **below** | 40.30–50.22 → **below** |
| September rain vs average (range) | 4.75 vs 6.29 (4.17–8.04), inside | 5.86 vs 6.89 (4.86–8.13), inside | 6.09 vs 7.43 (5.39–9.08), inside |
| 2025 full year vs average (final) | 39.09 vs 53.67 | 41.06 vs 52.51 | 37.67 vs 52.45 |
| Aquifer percentile, 9/30 (prior week / a year ago) | **20** (22 / 29) — below normal | 31 (33 / 33) | 29 (25 / 28) |

- **Rivers (September percentile; normal is 25–75):** Withlacoochee near Holder 13 · near Trilby 8 · Hillsborough near Zephyrhills 40 · Peace at Arcadia 23 · **Peace at Bartow 5.** In August four of the five were at the 2nd–5th percentile.
- **Lakes vs their minimum low management level (MLM = the usual end-of-dry-season low):** Northern **−3.89 ft** (Aug −3.98; a year ago −1.14) · Tampa Bay −0.27 · Polk Uplands +0.41 · Lake Wales −1.75. All lower than a year ago.
- More than 80% of the region's water supply comes from the aquifer (SWFWMD).

**So what:** SW Florida is in a **two-year rain deficit** (roughly 20–25 inches across 2025–26 at these averages). The September rains slowed the decline but did not close it. Water deficits in this region show up as watering restrictions, pressure on citrus and farms, wildfire risk, and stress on lakes and sinkholes. This is a **slow-moving backdrop**, not an event. **No water-shortage order is stated in this report.**

## Caveats
- **This is not the area -020 is about.** -020's 2–5 in (NWS) and "a foot in two weeks" (one forecaster) are for the **Panhandle and Big Bend**. SWFWMD's North region (Citrus, Hernando, Levy, Marion, Sumter, Lake) touches the Big Bend edge; Tampa Bay and the South region are outside that forecast.
- **2026 figures are provisional** (SWFWMD's own footnote); the annual figures are final.
- The 20–25 in two-year figure is WALTER's sum of the district's numbers, not a district statement.
- Whether any SWFWMD **water-shortage order or restriction** is in force was **not checked**; this report does not mention one.

## Exposure
None direct in Will's position record (FORGE mirror, 10/01 capture). FL bank and insurer exposure is CORAL's to state.

## Requested action
**CORAL:** log the SW Florida rain deficit against your climate/coastal pillar, check whether a SWFWMD water-shortage order is in force or likely, and state whether it touches any registered FL item (ag, insurance, property). Pair it with -020: north Florida wet, south-west Florida still dry. **AEOLUS (info):** US water-scarcity lane; the FL figure stays CORAL's. RED: information.
