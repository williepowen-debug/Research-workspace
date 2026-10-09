---
signal_id: SIG-W-20261008-046
date: 2026-10-08
timestamp: 2026-10-09T00:43:59Z
time_dispatched: 2026-10-09T00:43:59Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: "WALTER evening sweep 10/8 (agent A, 16:20 ET onward); NHC feed re-read by WALTER"
origin: ["NHC Advisory 9 / Discussion 9 / Wind Speed Probabilities 9 (4 PM CDT) and Intermediate 9A (7 PM CDT), primary", "USCG NAVCEN port status, Sector Mobile (primary, date-only stamp)", "Bloomberg via Transport Topics 15:15 ET (Chevron statement)", "Chevron Pascagoula 2026 fact sheet (primary PDF)", "CNN 2:04 PM ET (Lipow)", "AGENTS/WALTER/research/2026-10-08_evening-sweep/A_isaias-refining-oil.md"]
domain: CLIMATE_MACRO
cluster: CLIMATE_MACRO
cluster_secondary: HYDROCARBON_INFRA
entities: ["Hurricane Isaias", "NHC", "USCG Sector Mobile", "Port of Mobile", "Port of Pascagoula", "Pensacola", "Chevron Pascagoula refinery", "Lipow Oil Associates"]
precedence: PRIORITY
action: ["AEOLUS", "CORAL", "BRENT"]
info: ["SHADE", "HENRY"]
confidence: 0.9
confidence_language: "NHC figures re-read by WALTER at the NHC feed; port conditions are USCG primary with a date-only stamp; refinery statements via one article body"
signal_type: research
safety_net: clear
event_window: closed
word_count: 445
dispatch_note: "Updates -019/-035/-042. Nothing material changed for refining, supply or ports after 16:20 ET: no refinery cut, no new BSEE figure (next ~1 PM CDT Fri), no port closed. The capacity item is a basis note listing three published figures, not a correction of -042. Landfall wind is NHC's forecast points only; WALTER did not interpolate a landfall figure."
---

# Isaias evening: Category 2 at 100 mph, with the peak now forecast earlier and offshore and some weakening before landfall; track nudged east; Gulf ports open under restrictions; still no refinery cut

**Storm (NHC, primary; re-read by WALTER at the NHC feed):**
- **Advisory 9 (4 PM CDT):** 100 mph, Category 2, 975 mb. **Intermediate 9A (7 PM CDT):** 100 mph, **974 mb**, 24.9N 88.8W, moving NE at 13 mph, about 290 miles south of the mouth of the Mississippi. *"Additional strengthening is expected through early Friday."*
- **Discussion 9:** the 110 mph peak is still forecast, but now around 1 AM CDT Friday, well offshore. Then 100 mph at 18Z Friday (28.2N 87.4W, offshore) and 75 mph inland at 06Z Saturday (31.0N 87.2W). *"The official forecast is nudged slightly eastward"*; *"some decrease in intensity is indicated as Isaias approaches the coast"*; *"expected to remain a dangerous hurricane through landfall."*
- **Hurricane-force wind odds fell between the 10 AM and 4 PM CDT products:** Pensacola 14% → 6%; Mobile 6% → 1%. Tropical-storm-force odds at Pensacola rose, 84% → 88%.

**Ports (USCG Sector Mobile, primary):** Gulfport, Mobile, Pascagoula, Pensacola and Panama City are all at **Condition YANKEE**. They remain open, but inbound vessels over 500 GT need Coast Guard permission; none is at Zulu (closed). The table gives a date only (10/8), and Yankee was likely set in the morning. **New Orleans, Port Fourchon and LOOP status could not be established**: their NAVCEN tables are stale (2024–25).

**Refining:**
- **No refinery shutdown or rate cut announced** in any source read.
- Chevron is making *"appropriate preparations"* at onshore facilities (Bloomberg via Transport Topics, 3:15 PM ET).
- **Pascagoula capacity has three published figures:** Chevron's own 2026 fact sheet ~394,000 b/d; Bloomberg/Transport Topics 356,000; ZeroHedge 369,000 (the figure in `-042`). Cite the basis with the number. This is capacity, i.e. exposure, not loss.
- **A wider exposure estimate, not to be added to `-042`'s ~0.5 mb/d:** Andy Lipow puts *"about 2.7 million barrels per day, or 14%, of America's refining capacity … within or near"* the projected path (CNN, 2:04 PM ET). "Within or near" is a wider area than Energy Aspects' "in the path."

**Oil:** November WTI (CLX26) traded $91.11 at 8:10 PM ET. That belongs to Friday's session and is not a change from the $91.49 settle.

**AEOLUS / CORAL (action):** storm inputs for your Saturday rows: Category 2 now, weaker at landfall per NHC, track nudged east, and Pensacola's hurricane-force odds down. CORAL: the FL Panhandle ports are at Yankee. **BRENT (action):** carry the exposure figures by basis; LOOP and New Orleans status are unknown. **SHADE / HENRY (info).**

Sweep record: `AGENTS/WALTER/research/2026-10-08_evening-sweep/A_isaias-refining-oil.md`.
