---
signal_id: "SIG-W-20261022-041"
date: "2026-10-22"
timestamp: "2026-10-22T23:40:22Z"
dispatched: "2026-10-22T23:40:22Z"
source: "LIQUID"
origin: "LIQUID packet AGENTS/WALTER/inbox/2026-10-22_from-LIQUID_076-W2-first-fire-dealer-IG-5-10y.md (route INFO to NEXUS, HENRY; PROME by BOARD); owner grade in AGENTS/LIQUID/STATUS.md §2"
domain: "FUNDING_LIQUIDITY"
cluster: "BANK_COLLATERAL"
action: []
info: ["NEXUS", "HENRY", "PROME"]
precedence: "ROUTINE"
signal_type: "threshold-crossed"
confidence: 0.85
confidence_language: "NY Fed primary as first published; owner-graded; a net position is a stock, not selling"
resources: 1
safety_net: "clear"
word_count: 190
entities: ["GATE-LIQ-076", "NY-Fed-Primary-Dealer-Statistics", "PDPOSCSBND-G5L10", "MOVE", "VIX"]
event_window: "closed"
dispatch_note: "Owner-fired leg relayed as the owner asked (INFO). Owner says no second write-up owed (9/29 MET episode never re-armed)."
---
# LIQUID: one leg of its dealer-balance-sheet watch fired for the first time since July. Primary dealers were net short investment-grade corporate bonds due 5–10 years for two straight weeks (−$1,717M as of 10/14). The three-leg watch reads 2 of 3, but no new write-up is owed

| Leg | Reading | Line | State |
|---|---|---|---|
| W2 dealer IG 5–10y net | −$1,462M [10/7], −$1,717M [10/14, published 10/22] (prior +$847M [9/30]) | −$800M, two weeks | **FIRED, first time since 7/11** |
| W3 rates vol vs equity vol | MOVE >85 while VIX <20, every gradeable session since 9/23 | — | met |
| W1 CFTC SOFR-3M | not met as of 10/13; next print Fri 10/23 | — | not met |

Also: IG >10y −$10,307M (line −$12,000M, not met); below-IG 5–10y −$2,186M [10/14] from −$298M [9/30].

**LIQUID's caveats:** a net position is a stock, not gross selling, and not a dealer refusing to bid; no funding leg is showing (SOFR99 − IORB +6bp [10/21], standing repo facility about $0). The 9/29 MET episode never re-armed, so no second write-up is owed.

**INFO:** NEXUS (convergence), HENRY (credit-market structure), PROME by BOARD. Never a position; TERRY constructs, Will decides.
