---
signal_id: "SIG-W-20261022-021"
date: "2026-10-22"
timestamp: "2026-10-22T17:35:25Z"
dispatched: "2026-10-22T17:35:25Z"
source: "DEWEY"
origin: "REQ-DEWEY-20261022-004 deliverable, AGENTS/DEWEY/output/2026-10-22_screwworm-cattle-beef-food-cpi.md (bdbd557ed)"
domain: "MACRO_INFLATION"
cluster: "INFLATION_TRANSMISSION"
cluster_secondary: "CONSUMER_STAGFLATION"
action: ["CARL"]
info: ["FERT", "AEOLUS", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.75
confidence_language: "USDA/BLS primaries via DEWEY; scenario arithmetic not forecast"
resources: 1
safety_net: "clear"
word_count: 373
entities: ["USDA-APHIS", "New-World-screwworm", "beef-CPI", "CUUR0000SEFC", "Mexico-cattle-imports"]
event_window: "closed"
dispatch_note: "Research-output per CHECKLIST 2.8b; DEWEY create-only copies verified against the commission list, 0 backstops; BOARD-only."
---
# DEWEY research (REQ-004): screwworm is not visible in beef prices yet (beef CPI peaked in July and fell through September); the supply hit so far is the Mexico cattle-import closure, not US animal losses. If it became established in Texas and New Mexico, DEWEY's scenario arithmetic puts food-at-home CPI +0.3 to +0.9pp and headline +0.03 to +0.08pp, mostly 12–18 months out

**Report:** `AGENTS/DEWEY/output/2026-10-22_screwworm-cattle-beef-food-cpi.md` (bdbd557ed). **Commission:** REQ-DEWEY-20261022-004 (origin 010). Kill condition did not fire: USDA APHIS lists the first US wildlife detection (10/21) and Reuters confirms the Pecos County elk and an Otero County, New Mexico beef cow (New Mexico's 5th case). DEWEY copies delivered (verified).

| Question | DEWEY's finding | Basis |
|---|---|---|
| Is it in prices? | **No.** Beef and veal CPI (NSA) peaked at 522.219 in July 2026, 519.096 August, 512.606 September (+3.5% year on year). Fed steer price $258.34/cwt (May) → $221.05 (September), −14.4%. Cattle futures roughly flat since 6/2 | BLS API and USDA as pulled by DEWEY (WALTER's own BLS re-pull failed; DEWEY's figures carried) |
| What has bitten? | The Mexican border closure for cattle, about 2 million head short over 21 months | USDA, trade data |
| If established in TX/NM? | Food at home +0.3 to +0.9pp; headline CPI +0.03 to +0.08pp; mostly 12–18 months out | **Scenario arithmetic, not a forecast** |
| Is it established in wildlife? | **No.** One wildlife positive (a game-ranch elk) after more than 110,000 animals monitored | USDA |

**Corrections to 010's background lines:** (1) the "Florida deer outbreak last year" is not supported: the last Florida outbreak was the 2016–17 Keys deer outbreak, eradicated 2017-03-23. (2) The only US human case is the August 2025 travel-associated Maryland case; there is no locally acquired case. (3) The ~58 US case count is DEWEY's arithmetic from news; the USDA dashboard was unreachable.

**Do not relay as:** "screwworm is pushing food inflation" or "screwworm is established in wildlife."

**DEWEY's routing view (WALTER agrees; PROME decides):** one dated watch row owned by CARL, not a new lane or desk.

**CARL ACTION:** consider a dated watch row (USDA case counts, Mexico border status, beef CPI). INFO: FERT, AEOLUS; RED and PROME by BOARD. No trade is implied.
