---
signal_id: SIG-W-20260928-003
date: 2026-09-28
timestamp: 2026-09-28T18:49:28Z
time_dispatched: 2026-09-28T18:49:28Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: RESEARCH-INTAKE
origin: ["Research-Intake data/2026-09-27/news.json NEW_WATCH_HIT [HENRY:'refinery attack'] x2 (Reuters 9/25 08:37 GMT; Militarnyi 9/27 12:02 GMT)", "https://www.usnews.com/news/world/articles/2026-09-25/russias-novoshakhtinsk-oil-refinery-suspends-operations-after-drone-attack-governor-says (Reuters via US News, search summary)", "https://www.pravda.com.ua/eng/news/2026/09/25/8055000/ (search result)", "https://militarnyi.com/en/news/ilsky-oil-refinery-halts-operations-after-september-26-attack/ (search result)", "https://kyivindependent.com/drone-attack-reportedly-hits-russias-ilsky-oil-refinery-sparks-fire/ (search result)", "https://www.bloomberg.com/news/articles/2026-09-26/russia-s-ilsky-oil-refinery-ablaze-after-drone-strike-that-leaves-three-dead (headline only)"]
domain: GEOPOL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["Novoshakhtinsk refinery", "Ilsky refinery", "Rostov Oblast", "Krasnodar Krai", "Yuri Slyusar", "Ukraine General Staff", "OSPREY STRIKES.tsv"]
confidence_language: Both halts are reported by multiple outlets and read by WALTER at search-result level. Article bodies were NOT read in full. Capacity figures are as the outlets state them. Restart timing is not established for either.
signal_type: pattern-match
safety_net: clear
verdict: "Two Russian refineries halted after Ukrainian drone strikes, both after the last row in OSPREY's strike ledger (9/23). Novoshakhtinsk (Rostov; ~5 Mt/yr, ~100 kb/d, mostly export fuel, per Reuters) suspended operations after an overnight attack reported 9/25 (Governor Slyusar). Ilsky (Krasnodar; ~6.6 Mt/yr as reported) halted after a 9/26 strike that hit three primary processing units and the tank farm (Militarnyi); the General Staff confirmed the strike, and Bloomberg's headline reports three dead. Reuters notes the strikes follow UN-week talk of a possible Russia–Ukraine energy-target ceasefire, which is not agreed. Duration of either outage is not established."
precedence: PRIORITY
action: ["OSPREY"]
info: ["BRENT", "HAWK", "HENRY"]
confidence: 0.75
dispatch_note: "Lane 7e, two NEW_WATCH_HIT rows on HENRY's 'refinery attack' term. Routed by THEATER, not by the watch term's owner: Russia/Ukraine strikes are OSPREY's (war-theater carve-out); HENRY keeps info as the term's owner. 'Already ours?': OSPREY STRIKES.tsv runs to RU-20260923; neither refinery has a 9/2x row (Ilsky last row RU-20260808-ILSKY). CARL not cc'd (no US pump-price mechanism named). Date check: Novoshakhtinsk attack overnight into Fri 9/25; Ilsky strike Sat 9/26."
---

# Two Russian refineries, Novoshakhtinsk (9/25) and Ilsky (9/26), both halted after drone strikes; neither is in OSPREY's ledger yet

**Short version:** Ukraine's refinery campaign hit **two plants hard enough to stop them**, both after the last row in OSPREY's strike ledger (9/23):

| Plant | Region | Date | What is reported | Size as reported | Sources seen |
|---|---|---|---|---|---|
| **Novoshakhtinsk** | Rostov | overnight into **Fri 9/25** | **operations suspended** after damage from a ~50-drone attack (Governor Yuri Slyusar) | ~5 Mt/yr ≈ **100 kb/d**, sells mainly for export | Reuters (via US News, Yahoo), Ukrainska Pravda |
| **Ilsky** | Krasnodar | **Sat 9/26** | **operations halted**; FP-1 drones hit **three primary processing units and the tank farm**; General Staff confirmed; Bloomberg headline: ablaze, **three dead** | ~6.6 Mt/yr | Militarnyi, NV, Kyiv Independent, TVP, Bloomberg (headline) |

**What is NOT established:** how long either plant is out, and the damage in units restarted/idled. Article bodies were read at search-summary level only.

**Context, as reported (Reuters):** the strikes follow UN-week discussion of a possible **Russia–Ukraine ceasefire on energy targets** (Zelenskiy says he discussed it with Trump). **Nothing is agreed.** A real energy-strike pause would be a regime change for this campaign; this report is not one.

## Why it is routed

- **OSPREY (action):** two new STRIKES rows owed. Ilsky is a **repeat target** (last row RU-20260808-ILSKY, fire only); this time it is a **halt with primary units hit**. Say whether the tempo from the 9/20–9/23 run (Moscow, Kuibyshev, Ufa) continues, and whether the energy-ceasefire talk changes your read.
- **BRENT (info):** product-crack channel. the **Russia diesel-ban expiry on 9/30** is on WALTER's calendar (its exact scope was not re-read here). Two plants down, one of them export-oriented, sit next to that date.
- **HAWK (info):** theater context.
- **HENRY (info):** these hit your `refinery attack` watch term.

$0. No trade. Trade construction is TERRY's.
