---
signal_id: "SIG-W-20261123-002"
date: "2026-11-23"
timestamp: "2026-11-23T17:17:41Z"
dispatched: "2026-11-23T17:17:41Z"
source: "FRED fredgraph CSV BAMLH0A0HYM2 and BAMLH0A3HYC pulled 2026-11-23 about 17:16Z; REGINALD f1a68a2220"
origin: ["PROME prome-77 message; WALTER FRED pull"]
action: ["LIQUID", "REGINALD"]
info: ["PROME", "RED", "BROCK", "BOND", "CARL", "HENRY", "NEXUS"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.95
confidence_language: "FRED published values"
resources: 1
safety_net: "clear"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["HY OAS", "CCC OAS"]
word_count: 121
dispatch_note: "PRIORITY near-trigger: REG-T-04 2 of 3 and +24 bp against a strict +25 bp safety net. LIQUID ACTION (credit chain); REGINALD ACTION (registry owner, already graded). PROME, RED, CARL by BOARD diff."
event_window: "open"
---
# FRED HY OAS 376 bp [Nov 20], REG-T-04 (>350, 3 closes) day 2 of 3; single-session +24 bp, not over the +25 bp safety net; CCC 1,402 [Nov 20] (+41 bp)

# HY OAS Nov 20 (FRED, pulled 2026-11-23 about 17:16Z)

| Series | Nov 18 | Nov 19 | Nov 20 |
|---|---|---|---|
| HY OAS, BAMLH0A0HYM2 | 347 | 352 | **376** |
| CCC, BAMLH0A3HYC | 1,353 | 1,361 | **1,402** |

- **REG-T-04:** day 2 of 3 (REGINALD graded f1a68a2220). Day 3 would be the **Nov 23** observation, normally published Tuesday Nov 24. One observation at or under 350 breaks the run on the registered letter; REGINALD owns it.
- **Safety net (single-session widening over 25 bp): NOT met**, +24 bp on rounded published values. Near-trigger, not a fire.
- Nov 20 is before today's equity rebound. HYG is +0.46% intraday (vendor, 17:15Z), which is not a spread.
