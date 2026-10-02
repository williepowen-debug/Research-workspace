---
signal_id: SIG-W-20261002-020
date: 2026-10-02
timestamp: 2026-10-02T18:30:13Z
time_dispatched: 2026-10-02T18:30:13Z
timestamp_note: stamped from the system clock at write, not typed
source: Will (terminal screenshot, Dylan Federico X post) + NWS Tallahassee AFD
origin: ["NWS Tallahassee Area Forecast Discussion, issued 12:21 PM EDT Fri 2026-10-02, read via WebFetch ~18:2xZ", "Will screenshot: @DylanFedericoWX (meteorologist) X post ~2h before capture, ECMWF 72h total precipitation map init 00Z 02OCT2026 (max 7.0 in, areal avg 1.54 in)"]
domain: CLIMATE_MACRO
cluster: MISC
entities: ["Florida", "Florida-Panhandle", "Big-Bend", "NWS-Tallahassee", "El-Nino"]
confidence: 0.8
confidence_language: "reports"
signal_type: context
safety_net: clear
verdict: "NWS Tallahassee (10/02 12:21 EDT): 'a very wet pattern' through early next week, 2-5 in widespread and locally 5-7 in along the immediate coast; WPC Marginal (Level 1) risk of excessive rain Fri-Sat in the Panhandle, Slight (Level 2) on Sunday; moisture near or above record for early October; main threat urban/poor-drainage flooding, some rivers could reach action stage. A meteorologist (Dylan Federico) goes further: over a foot possible in the Panhandle/Big Bend over two weeks, 6+ in widely, potentially Florida's wettest October on record, as El Nino sets in."
precedence: PRIORITY
action: ["CORAL"]
info: ["AEOLUS", "RED"]
dispatch_note: "FL climate carve-out: Florida-named climate -> CORAL action. AEOLUS info: the El Nino attribution and the macro-climate read. No insurance-transmission figure yet, so REGINALD/SHADE not added; add on any loss or claims number. Will batch BM-20261002-04 item 1. Cluster MISC: no climate cluster in the 12 (CLUSTER_TAXONOMY). RED pull-complete."
---
# Florida: a very wet pattern into next week. NWS says 2–5 inches, locally 5–7 on the Panhandle coast, with a Slight flood risk Sunday. A forecaster says a foot is possible over two weeks.

**Short version:** The **National Weather Service in Tallahassee** (10/02, 12:21 PM EDT) forecasts **"a very wet pattern"** through early next week: **2–5 inches widely, locally 5–7 inches along the immediate coast.** The Weather Prediction Center has a **Marginal (Level 1) risk of excessive rainfall Fri–Sat** for the Panhandle and SE Alabama, rising to **Slight (Level 2) on Sunday.** Atmospheric moisture is **near or above record for early October.** The main threat is **flooding in urban and poorly drained areas.** *"Should the higher end rainfall amounts of widespread 6" or more verify ... some rivers could reach action stage."*

**The screenshot Will sent goes further:** meteorologist **Dylan Federico** says **over a foot is possible in the Panhandle and Big Bend over two weeks**, 6+ inches likely elsewhere, "the equivalent of 10 trillion gallons", with **"the potential to be the wettest October on record for Florida"**, as **El Niño** establishes itself. His map is the **ECMWF 72-hour total** (run of 00Z 10/02): **max 7.0 in, average 1.54 in across the area.**

**So what:** This is the **storm-season tail** in CORAL's coastal pillar. Two weeks of heavy rain over the Panhandle and Big Bend is a **flood and property** story: urban flooding, rivers, and potentially NFIP/Citizens claims later. **No tropical system is named.**

## Caveats
- **"Over a foot" and "wettest October on record" are one forecaster's two-week outlook. NWS is not saying that.** NWS says 2–5 in (locally 5–7) through early next week.
- **The map in the screenshot covers 72 hours, not two weeks.** Its "max 7.0 in" fits NWS's locally 5–7 in.
- El Niño "establishing itself" is the forecaster's framing. **AEOLUS owns the ENSO state.**

## Exposure
None direct in Will's position record.

## Requested action
**CORAL:** log it against your coastal/climate pillar (Panhandle/Big Bend first) and say whether a wet October feeds any registered Florida property, insurance or flood item worth watching after the weekend. AEOLUS (El Niño, macro), RED: information.
