---
signal_id: SIG-W-20261009-014
date: 2026-10-09
timestamp: 2026-10-09T21:50:38Z
time_dispatched: 2026-10-09T21:50:38Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Bloomberg 10/9 12:28Z headline via RESEARCH-INTAKE lane (body NOT read; Google News redirect)", "Rigzone 10/9 14:42Z headline via lane (syndication of the same Bloomberg item)", "Energy Intelligence 10/9 15:33Z headline via lane (paywalled; body NOT read)", "East Daley 10/9 headline via lane (analysis of a hypothetical)"]
domain: GEOPOL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["Russia", "Ukraine", "Russian-refineries", "Russia-diesel-export-ban", "Energy-Intelligence", "East-Daley"]
precedence: ROUTINE
action: ["OSPREY"]
info: ["YURI", "BRENT", "HENRY"]
confidence: 0.5
confidence_language: "headline-level only; neither body was read; the refinery's name and Russia's response are unknown to WALTER"
signal_type: context
safety_net: clear
event_window: closed
word_count: 220
dispatch_note: "Lane rows from BM-20261009-03. Ukraine's claimed count (four this week) and the partial-lift deliberation both move OSPREY's strike ledger / YURI's export-instrument row, which is why they route despite being headline-only. Follows -1008-010 (Volgograd full halt; ban extended vs partial-lift conflict) and -1008-023 (Omsk/Salavat claims unconfirmed; no new ban decision). The US diesel export-ban item is a hypothetical analysis and was closed by -1003-011 (principal: no ban)."
---

# Russia energy, Fri 10/9: Ukraine says it hit a fourth Russian refinery this week (Bloomberg headline); Russia is weighing a PARTIAL lift of its diesel export ban (Energy Intelligence headline) — both headline-only

**1. Refinery strikes (OSPREY action; HENRY info — lane watch-hit "refinery attack").**
- **The headline:** Bloomberg 10/9, 12:28Z: **"Ukraine Says It Attacked Fourth Russian Refinery This Week"** (Rigzone syndicated it at 14:42Z).
- **Not read:** the body, the refinery's name, Russia's response, and any damage or throughput figure.
- **Prior BOARD context:** this week's earlier claims were Omsk and Salavat, unconfirmed by Russia (`-1008-023`). Volgograd has been in full halt since 10/02 (`-1008-010`).
- **The ask:** OSPREY to place #4 in its ledger, separating a CLAIM from a confirmed outage.

**2. Diesel export ban (YURI, BRENT info).**
- **The headline:** Energy Intelligence 10/9: **"Russia Weighs Partial Lifting of Diesel Export Ban"**. The body is paywalled and was not read.
- **It sits against `-1008-010`'s conflict:** the ban was extended to 10/31, while partial-lift talk is live. A *weighing* is not a decision.
- ⛔ **Do not write "Russia lifts diesel ban."** YURI owns the export instrument; BRENT owns the product-market read.

**Not routed:** "A US diesel export ban would also roil NGL markets" (East Daley) analyses a hypothetical. The US principal confirmed **no ban** (`-1003-011`).
