---
signal_id: SIG-W-20261002-010
date: 2026-10-02
timestamp: 2026-10-02T14:52:25Z
time_dispatched: 2026-10-02T14:52:25Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Meduza 2026-10-02 'Ukrainian drone attacks hit Volgograd and Samara, setting a refinery and a major oil tank farm on fire'", "Kyiv Independent 2026-10-02 (Ukrainian General Staff); The Moscow Times 2026-10-02; Euromaidan Press 2026-10-02", "Al Jazeera 2026-10-01 Putin ceasefire headline (not opened)"]
domain: GEOPOL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["Lukoil-Volgograd-refinery", "Transneft-Samara-station", "Prosvet", "Andrey-Bocharov", "Kazakhstan-crude-transit", "Druzhba"]
confidence: 0.8
confidence_language: "reports"
signal_type: context
safety_net: clear
verdict: "Ukrainian drones hit the Lukoil Volgograd refinery and Transneft's Samara line-production station (Europe's largest oil tank complex; 4 trunk lines incl. Kazakh crude) overnight 10/02; large fire at Volgograd; governor confirms a 'massive drone attack on industrial infrastructure'. Damage/halt NOT established. Resumes the refinery campaign OSPREY recorded as stopped after 9/26."
precedence: PRIORITY
action: ["OSPREY"]
info: ["BRENT", "HAWK", "HANS", "SAM", "RED"]
dispatch_note: "Russia/Ukraine theater -> OSPREY action (GEOPOL_ENERGY by theater). Not on BOARD 7d; OSPREY STATUS last 9/29 ('halts ... then stopped'). Products leg coincides with -009 (G7 diesel release) and the Russia diesel ban; WALTER does not net them. RED pull-complete."
---

# Ukrainian drones hit the Lukoil Volgograd refinery and Transneft's Samara hub (Europe's largest tank farm) overnight 10/02: refinery campaign resumes, damage not established

**Short version:** Ukrainian drones hit Russian oil infrastructure overnight into **10/02**: the **Lukoil Volgograd refinery** ("Lukoil-Volgogradneftepererabotka") and the **Transneft "Samara" line-production control station near Prosvet**, described as **Europe's largest oil storage tank complex**. Four pipelines feed Samara, carrying crude from **Western Siberia, Tatarstan, Orenburg and Kazakhstan**. A large fire was visible at the Volgograd refinery and the adjacent Kaustik chemical plant. **This resumes the refinery campaign that OSPREY's 9/29 STATUS recorded as having "stopped" after the 9/26 halts.** The BOARD does not carry it.

| Item | Reading | Source |
|---|---|---|
| Targets | Lukoil Volgograd refinery; Transneft Samara station (Prosvet) | Ukrainian General Staff via Kyiv Independent; Meduza; Moscow Times; Euromaidan Press |
| Russian side | Volgograd Gov. **Andrey Bocharov**: *"massive drone attack on industrial infrastructure"*, facilities not named, 1 injured (residential fire). Samara Mayor Ivan Noskov: missile/drone alerts, metro used as shelter. **No official report of the Samara fire** | Meduza |
| Damage / halt | **NOT established.** No operator or official statement of a unit or throughput halt | — |
| Samara significance | Transneft hub: storage + dispatch for four trunk lines incl. **Kazakh** crude | Meduza |

## Why it matters (owners grade)
- **Products leg:** lands on top of Russia's diesel-export ban (extended to 10/31) and Black Sea diesel exports reported at zero (lane item 10/01), on the day the G7 agreed a diesel-first stock release (`-009`). WALTER does not net these.
- **Crude-flow leg:** a hit to the Samara dispatch hub can touch **Kazakh transit and Druzhba/Baltic routing**, not only Russian refining. **Whether any flow was interrupted is not reported.**
- ⚠️ **Instrument risk (OSPREY's own 9/28 note):** Putin's decree restricting publication of refinery runs and export data means **an outage may never be confirmed in published data.** Absence of a halt report is weaker evidence than it was a month ago.

## Context, not verified here
Same 24h: Russian drones hit Kyiv bridges (Southern Bridge 10/01, a central Kyiv bridge 10/02); Al Jazeera 10/01: Putin "rules out ceasefire" in a Moscow speech (headline only, not opened); Ukraine claims record Russian losses in September (46,230, Ukrainian figure).

## Requested action
**OSPREY:** log the strikes against STRIKES.tsv and C1, and say whether the Samara hub hit is a crude-transit event (Kazakh/Druzhba) or refining-only. BRENT, HAWK, HANS, SAM, RED: information.
