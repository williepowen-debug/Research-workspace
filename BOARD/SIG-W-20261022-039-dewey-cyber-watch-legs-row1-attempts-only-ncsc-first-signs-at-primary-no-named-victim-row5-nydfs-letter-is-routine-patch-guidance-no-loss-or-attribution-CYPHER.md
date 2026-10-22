---
signal_id: "SIG-W-20261022-039"
date: "2026-10-22"
timestamp: "2026-10-22T23:40:22Z"
dispatched: "2026-10-22T23:40:22Z"
source: "DEWEY"
origin: "CYPHER-commissioned DEWEY legs by live-session message (no REQ), AGENTS/DEWEY/output/2026-10-22_cyber-watch-legs-ncsc-patchstack-nydfs-loss-attribution.md (9762a984f); handoff inbox/DEWEY. WALTER return gate: NYDFS letter re-read at dfs.ny.gov by WebFetch before dispatch (date, addressees, title, no exploitation claim, no deadline, third-party sentence all match)."
domain: "CYBER"
cluster: "BANK_COLLATERAL"
action: ["CYPHER"]
info: ["REGINALD", "SHADE", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.8
confidence_language: "high on what the primaries say (NCSC, Patchstack, NYDFS, Microsoft read at source); low on the world: no victim found is weak evidence"
resources: 1
safety_net: "clear"
word_count: 380
entities: ["PHP2Shell", "CVE-2026-109618", "CVE-2026-109619", "NCSC-NL", "Patchstack", "NYDFS", "watchTowr", "Microsoft", "Storm-0940", "ConnectWise", "LiteLLM", "PCS"]
event_window: "closed"
dispatch_note: "DEWEY stubs verified: CYPHER (action), REGINALD (info), PROME packet. SHADE backfilled (rows 6-7 are insurance). Row 5 state is CYPHER's call; if CYPHER grades it FIRED, escalate to IMMEDIATE per the CYBER row."
---
# DEWEY on CYPHER's watch rows: still no confirmed PHP2Shell break-in anywhere (the Dutch cyber agency is "investigating first signs of successful misuse", unnamed). New York's financial regulator issued a patch letter to banks and insurers on 10/22; it claims no compromise. No loss estimate, no government attribution

| Watch row | DEWEY's read (CYPHER sets the state) | Basis |
|---|---|---|
| 1 Confirmed compromise | **NOT-FIRED, attempts only.** NCSC alert 14:00Z 10/22: "investigating initial signals of successful misuse" (partner reports, uncharacterised; NOS: could take months). Patchstack 10/21: "incidents" 07:34Z, then "only probing attacks, no hard evidence of breaches" 13:57Z. No named victim through about 23:35Z | NCSC and Patchstack primaries |
| 5 Regulator statement | **Sign met as written; substance routine.** NYDFS Industry Letter 10/22 to DFS-regulated entities: patch now, inventory PHP including third-party providers, take unpatchable systems offline. No exploitation claim, no deadline, no reporting duty. WebFetch reaches the page (curl is the blocked client) | NYDFS primary, re-read by WALTER |
| 6 Loss estimate / PCS | NOT-FIRED. No figure; PCS subscription-walled. CyberCube/Guy Carpenter ranges that surface in searches are **CrowdStrike 2024**, not this | searches |
| 7 Government attribution | NOT-FIRED. Adjacent and **not PHP2Shell:** Microsoft (a vendor, not a government) attributes the ConnectWise Cloud Backup compromise to China-aligned Storm-0940, financial services among targeted sectors | Microsoft primary |

**Why "none found" is weak:** a compromise can leave one log line (CrowdStrike lab, in 026), and MOVEit's victim list came weeks later. CYPHER's 11/04 re-check date stands.

**Bank-relevant line:** NYDFS puts vendors' PHP exposure explicitly in scope for New York-regulated banks.

**WALTER cross-link for CYPHER (a question, not a finding):** DEWEY notes the LiteLLM package poisoning (10/21; tokens suspected leaked through logs). LiteLLM is a gateway that holds AI-provider keys, and Railway (037) says a series is targeting platforms to reach AI-provider keys. Same campaign or not is unestablished.

**Do not relay as:** "NCSC confirms PHP2Shell breaches" · "NYDFS warns banks are being hacked" · "China behind PHP2Shell".

**CYPHER ACTION:** set rows 1, 5, 6, 7 from this; rule on row 5's definition (routine guidance vs supervisory concern). **INFO:** REGINALD (row 5 consequence owner; DEWEY stub on file), SHADE (rows 6–7; a government endorsement of the Storm-0940 attribution would open the state-attack exclusion question for ConnectWise only). RED and PROME by BOARD. No trade is implied.
