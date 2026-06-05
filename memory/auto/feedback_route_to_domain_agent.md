---
name: Route To Domain Agent Not PROME
description: When a domain-specific agent exists, route questions/updates through them rather than defaulting to PROME
type: feedback
originSessionId: 3892d800-cf09-4821-98e2-dc6bafc1869e
---
When a specific task falls within another agent's declared domain, route to that agent — don't default to PROME just because PROME is the coordinator.

**Why:** PROME is a coordinator, not a domain expert. Ceasefire/oil questions belong to HAWK/BRENT; consumer belongs to CARL; etc. Routing through PROME adds a hop and loses domain context. Will corrected this when RED proposed asking PROME for position-matrix ceasefire data that HAWK owns.

**How to apply:** Before pinging PROME, ask: is there an agent whose domain this is? If yes, route there. PROME is for cross-domain coordination, trade execution approval, and things no single agent owns. Domain agents: HAWK (geopolitical/ceasefire), BRENT (oil/physical), CARL (consumer), SAM (Japan), REGINALD (credit), LIQUID (market liquidity), HENRY (velocity), LABOR (employment), BROCK (private credit).
