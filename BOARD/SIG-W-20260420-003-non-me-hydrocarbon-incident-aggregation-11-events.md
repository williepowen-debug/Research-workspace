---
signal_id: SIG-W-20260420-003
precedence: PRIORITY
timestamp: 2026-04-20T12:45:00Z
source: WALTER
origin: "Aggregation table (author/source of compilation not identified on image — likely analyst compilation): 'Exhaustive List of Hydrocarbon & Major Energy Incidents (Non-Middle East)' — 11 rows spanning 2026-03-01 to 2026-04-15 across 7 countries. Intaken via Will Telegram batch 2026-04-20 12:24 UTC."

to: BRENT (ACTION — oil/energy primary, meta-aggregation frame)
info: HAWK, RED, LIQUID, NEXUS, PROME
group: ENERGY_CHAIN
dispatched: 2026-04-20T12:45:00Z
dispatch_note: "PRIORITY thesis-frame signal. Not a single event — a compilation documenting 11 non-Middle-East hydrocarbon/major-energy infrastructure incidents in a ~6-week window. The meta-read is the signal: global hydrocarbon infrastructure is degrading at elevated rate OUTSIDE the Middle East while Iran/Hormuz + Qatar LNG crash in ME are also live (SIG-014, SIG-030 Apr 19). If the base rate of major non-ME refinery/plant incidents is approx 1-3 per month, 11 in ~6 weeks is 1.5-2x baseline, not extraordinary on its own but meaningful combined with ME. Mix is notable: 4 Russia (war-driven: Lukoil Kstovo drone Apr 4, Primorsk Port drone strikes Apr 3, Tuapse Apr 20 — SIG-001 today — not yet in aggregator's cutoff, + earlier implied), 2 India (Vedanta Sakti boiler 16-19 fatalities Apr 14, ONGC Mumbai platform Apr 3 + Bhilai Steel turbine Apr 7 + now Pachpadra Apr 20 SIG-002), 3 Texas USA (Valero Port Arthur Mar 23, LyondellBasell Bayport Mar 12, Petromax Channelview Mar 5), 1 Mexico (Pemex Olmeca 2nd fire in month Apr 9), 1 Australia (Viva Geelong Apr 15 — already covered SIG-W-20260416-002), 1 Ecuador (Esmeraldas 60-day state of emergency Mar 1). Russia/Ukraine war component is war-driven; India run is plant-specific; US Texas cluster deserves its own investigation. WALTER action: dispatch as thesis-frame and surface to NEXUS for formal cluster classification, cross-linked to ME cluster. BRENT to interpret in oil-tape terms. If author/source of the compilation becomes identifiable, attribute. Original Russia strike list undercounts — SIG-001 Tuapse Apr 20 is incremental."

signal_type: pattern-match
confidence: 0.70
confidence_language: moderate-high (on pattern); per-row accuracy not individually verified
resources: 0.05
safety_net: monitoring (cluster meta-frame)

word_count: 260

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: HYDROCARBON_INFRA
---

## Signal

Aggregated list of 11 hydrocarbon/major-energy infrastructure incidents Mar 1 – Apr 15 2026, all **outside the Middle East**:

| Date | Facility | Location | Nature | Known Impact |
|------|----------|----------|--------|--------------|
| Apr 15 | Viva Energy Geelong Refinery | Geelong, Victoria, Australia | Fire + explosions | 1 of 2 AU refineries, impact under assessment (covered SIG-W-20260416-002) |
| Apr 14 | Vedanta Sakti Plant | Chhattisgarh, India | Massive boiler explosion | **16-19 fatalities**, dozens injured |
| Apr 9 | Pemex Olmeca Refinery | Dos Bocas, Mexico | Fire in coke storage | 2nd fire in a month; limited to storage unit |
| Apr 7 | Bhilai Steel Power Plant-2 | Chhattisgarh, India | Turbine explosion + fire | 7+ injuries; workers jumping from buildings |
| Apr 4 | Lukoil-Nizhegorodnefteorgsintez | Kstovo, Russia | Drone strike + fire | Strike on crude distillation unit; throughput reduction |
| Apr 3 | ONGC Mumbai High Platform | Offshore Mumbai, India | Sudden fire on SHP platform | 10 workers injured; operations briefly suspended |
| Apr 3 | Primorsk Port Infrastructure | Leningrad, Russia | Multiple drone/air strikes | Fires at major oil export terminal + storage depots |
| Mar 23 | Valero Port Arthur Refinery | Texas, USA | Severe explosion + fire | Diesel hydrotreater + central control room destroyed |
| Mar 12 | LyondellBasell Bayport Plant | Texas, USA | Major industrial fire | Targeted hydrocarbon feedstock processing units |
| Mar 5 | Petromax Refining | Channelview, Texas, USA | Pump seal failure + fire | Quick containment; minimal offsite impact |
| Mar 1 | Esmeraldas Refinery | Esmeraldas, Ecuador | Fire in SEVIA unit charge pumps | **60-day state of emergency** due to infrastructure damage |

## Relevance

- **BRENT (ACTION):** Global hydrocarbon disruption thesis is no longer Middle-East-only. Three war-driven Russia incidents + three Texas refinery incidents + Ecuador 60-day state of emergency + Australian refinery down are each individually absorbable, but in aggregate represent ~1.5-2x baseline rate of major non-ME incidents. Combined with active ME disruption (Iran/Hormuz 8-ch cluster, Qatar LNG crash), the global refined-products and feedstock balance is tighter than consensus absorbing.
- **HAWK (info):** Russia/Ukraine kinetic campaign on Russian hydrocarbon infrastructure confirmed pattern (Kstovo, Primorsk, + Tuapse SIG-001 today).
- **RED (info):** Counter-cluster-check — compilation source/author not identified; risk of selection bias (a list of bad news is always long). RED to call out whether 11 incidents in 6 weeks is actually 1.5-2x or within normal variance.
- **LIQUID (info):** Refined-products and crack-spread stress if Texas cluster extends. Esmeraldas 60-day emergency is material for Ecuador output.
- **NEXUS (info):** **Candidate for formal cluster** — "Global Hydrocarbon Infrastructure Stress" — combine with ME cluster (SIG-014 SoH, SIG-030 Qatar LNG) to form a meta-cluster. Base rate / anomaly-vs-noise classification needed.
- **PROME (info):** Coordination — thesis-level pattern deserves routing to all energy-chain agents + RED adversarial.

## Caveats

- **Compilation source unattributed on the image.** Looks like an analyst / X.com aggregator — cannot verify it's exhaustive, balanced, or unbiased.
- **Per-row accuracy not individually verified.** The Vedanta Sakti boiler, Bhilai Steel turbine, Valero Port Arthur, Esmeraldas and Pemex Olmeca entries would benefit from cross-check if they become thesis-load-bearing.
- **Russia incidents are war-driven** — separate causal channel from accident-driven (India/US/Ecuador/Australia). A clean analysis would separate sabotage/war rate from baseline industrial accident rate.
- **Base rate unknown.** A reliable call on "is 11 events in 6 weeks elevated?" requires a rolling history that WALTER doesn't have. NEXUS or Agent 7 research candidate.
- **Pachpadra (SIG-002 today Apr 20)** would be an incremental 12th entry if the compilation were updated to Apr 20.

## Source

- Aggregator compilation (author/publisher TBD) — viewed as screenshot
- Intake: Will via Telegram screenshot batch, 2026-04-20 12:24 UTC
- Individual event sources embedded in aggregator (links visible on Viva Energy, Lukoil-Nizhegorodnefteorgsintez, Valero Port Arthur, Petromax, Esmeraldas); each warrants primary-source check if called upon
