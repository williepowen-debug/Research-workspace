---
signal_id: SIG-W-20261001-027
date: 2026-10-01
timestamp: 2026-10-01T21:07:31Z
time_dispatched: 2026-10-01T21:07:31Z
timestamp_note: stamped from `date -u` at write, not typed
source: RESEARCH-INTAKE
origin: ["RESEARCH-INTAKE lane 2026-10-01 news batch, WATCH_HIT FALCON 'East-West pipeline': Newsquawk headline 2026-10-01 16:18 UTC (page fetched by WALTER ~21:0xZ)", "Argus original NOT found by WALTER (argusmedia.com search returned only April/earlier pieces)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
entities: ["Petroline", "East-West-pipeline", "Yanbu", "Argus", "Kpler", "Bloomberg", "FAL-05", "FALCON-marks-B1-C14-D85"]
confidence: 0.55
confidence_language: one trade-press source citing one unnamed source, read only as a Newsquawk headline; the number is a FLOW figure and sits well above two other live estimates
signal_type: research
safety_net: clear
verdict: "Newsquawk 2026-10-01 16:18 UTC: crude flows through Saudi Arabia's East-West pipeline have recovered to around 5.5 mb/d, according to Argus citing a source, allowing a restart of exports from Yanbu. This is a third live FLOW estimate for the line: Kpler ~2.65 mb/d and Bloomberg ~3.5 mb/d (9/28, one source). Not operator-confirmed. Do not average."
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "HAWK", "SAM", "RED"]
dispatch_note: "Iran pre-dispatch guard run: anchor IRAN_WAR.md read at boot (full sweep 10/01); GUARDS read for KILL-ON-SIGHT ① capacity-as-loss, ADD#24 capacity-vs-loss, Petroline 2019 trap, syndication-not-corroboration. The 5.5 is reported FLOW, not capacity (WSJ capacity 7 mb/d). FALCON owns FAL-05 and the B1/C14/D85 marks; this is an input to its downgrade-trigger review, not a re-grade. Same batch KILLED: EnergyNow 'Oil Loadings Suspended at Yanbu' surfacing 9/30 = Reuters 9/15 (date trap). DUP: Reuters 9/22 restart, Reuters/TRT 9/29 + Marine Insight 10/01 loadings resumed (on BOARD -0928-019/-020), Reuters 9/24 Houthi Yanbu claim (-0924-015). RED is pull-complete (no handoff)."
---

# Petroline flows reported back to ~5.5 mb/d (Argus, one source, via Newsquawk): a third estimate, well above Kpler and Bloomberg

**Short version:** A Newsquawk headline at **2026-10-01 16:18 UTC** says crude flows through Saudi Arabia's East-West pipeline (Petroline) **"have recovered to around 5.5mln BPD, according to Argus citing a source, allowing for a restart of exports from the Red Sea port of Yanbu."** This is now the **third live flow estimate** for the line, and the highest. **It is not operator-confirmed.**

| Estimate | Figure | Date | Source tier |
|---|---|---|---|
| Kpler (line throughput) | ~2.65 mb/d | late Sept (anchor) | vendor ship-tracking |
| Bloomberg | ~3.5 mb/d flowing | 9/28 | one person with knowledge (`-0928-020`) |
| **Argus** | **~5.5 mb/d "recovered"** | **10/01** | **one unnamed source, read through a Newsquawk headline** |
| Capacity (not a flow) | up to 7 mb/d | WSJ 9/11 | explicit capacity language |

⛔ **Three estimates on different bases. Do not average them into a figure none of them reported.**

## Why FALCON
FAL-05 resolved FAILED on route (c) on 9/28, and the D85 mark carries FALCON's own caveat: *"a ROUTE loss, not a demonstrated BARREL loss … the firing event is reversing."* A flow near the line's normal export level is an input to FALCON's **§2 downgrade-trigger review**. Whether it counts is FALCON's call. WALTER does not re-grade the marks.

## Caveats
- **Single source, secondhand.** WALTER read only the Newsquawk headline. Argus's own article was not found, and Argus is paywalled.
- **5.5 mb/d is also a pre-war HORMUZ figure.** A search summary of argusmedia.com pages (not an article WALTER opened) says ~5.5 mb/d of Saudi crude was previously shipped via the Gulf. Before anyone carries the number, confirm it is the **pipeline flow** and not that figure relabeled. A search-summary layer during this check implied the two were the same; that was **not** verified.
- **Flow is not loadings.** Yanbu loadings were ~2 mb/d (trade sources, anchor). A pipeline flow figure does not establish export volumes.
- **No Aramco or Ministry of Energy statement.** DAMAGED is still "per nobody."

## Same-batch dispositions (no dispatch)
- **KILLED (date trap):** EnergyNow "Oil Loadings Suspended at Saudi's Red Sea Port of Yanbu, Shipping Sources Say", which surfaced in the lane stamped **9/30**. It is the **Reuters story of 9/15** (BOE Report and Times of Israel carry that date). Carrying it would have reversed the current "loadings resumed" state.
- **DUP:** Reuters 9/22 restart (`-0924-002`) · Reuters/TRT 9/29 and Marine Insight 10/01 "loadings resumed" (`-0928-019`/`-020`) · Reuters 9/24 Houthi Yanbu claim (`-0924-015`).

## Requested action
FALCON: decide whether the Argus figure bears on your §2 downgrade triggers for FAL-05 / D85, and on what tier. BRENT, HAWK, SAM: information only.
