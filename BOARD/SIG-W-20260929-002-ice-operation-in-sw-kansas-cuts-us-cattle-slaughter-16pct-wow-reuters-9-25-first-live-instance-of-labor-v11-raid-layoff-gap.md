---
signal_id: SIG-W-20260929-002
date: 2026-09-29
timestamp: 2026-09-29T18:22:26Z
time_dispatched: 2026-09-29T18:22:26Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34); every WALTER read below precedes this stamp"
source: Will-Telegram image (zerohedge 9/28 18:50 ET headline) + WALTER verify
origin: ["Will-Telegram BM-20260929-03 item 5: zerohedge 2026-09-28 18:50 ET 'US Cattle Slaughter Plunges 16% In A Day As Immigration Crackdown Guts Kansas \"Golden Triangle\" Workforce'", "Reuters (Tom Polansek) 2026-09-25 via wmbdradio.com syndication, search-result text: 'Meatpackers slaughtered an estimated 90,000 cattle on Thursday, down 16% from a week earlier'; one major SW-Kansas packer ~500 head Wednesday vs ~5,600 capacity", "KCUR (Kansas City Public Radio) 2026-09-24: sweeping ICE enforcement action at meat processing plants, SW Kansas", "Drovers/AgWeb: 'Cattle Chop as Slaughter, Cash Hit by ICE Raids'; tradingpedia 2026-09-25 'cattle futures fall as plant labor issues slow processing'"]
domain: LABOR
cluster: CONSUMER_STAGFLATION
entities: ["ICE", "southwest Kansas", "US beef packers", "USDA estimated daily slaughter", "MARCO", "LABOR", "CARL"]
confidence_language: "Event confirmed by Reuters (via syndication, search text; body not fetched) plus two trade outlets and KCUR. The -16% is a ONE-DAY estimate (Thursday 9/24 vs a week earlier), not a weekly or sustained figure. The zerohedge 'guts the workforce' framing is the wrapper's."
signal_type: catalyst
safety_net: clear
verdict: "A US immigration (ICE) enforcement operation across southwest Kansas, the densest US feedlot and beef-packing region, kept much of the largely immigrant workforce home in the week of 9/22. Packers slowed lines, and USDA's estimated cattle slaughter on Thu 9/24 was ~90,000 head, down 16% from a week earlier (Reuters 9/25). One major SW-Kansas plant ran ~500 head vs ~5,600 capacity on 9/23. Cattle futures fell as fed cattle backed up; industry and union officials say beef prices, already at records, may rise further. This is the first live instance of the raid-linked labor disruption LABOR registered as an UNCOVERED gap on 9/29 (v11: 'every phrase tested failed')."
precedence: PRIORITY
action: ["MARCO", "LABOR"]
info: ["CARL", "RED"]
confidence: 0.75
dispatch_note: "Axis sweep (step 10.7): three axes, three owners. Immigration enforcement / labor supply -> MARCO (REGISTRY Role 'Immigration, DHS shutdown, labor supply') ACTION. Raid-linked layoffs -> LABOR ACTION: its 9/29 packet names v11 'ICE raid-linked layoffs' a counted gap, so this is its first live instance, and whether it is a v11 datum is LABOR's call. Beef CPI -> CARL INFO (KB-CARL-333: beef +11.2% YoY in June; a packer slowdown is a supply shock to the protein channel it tracks). RED INFO. Domain-table default for LABOR would be CARL action; overridden by content, because the ask here is MARCO's and LABOR's. MARCO is DARK (last STATUS commit 9/24; not in ListAgents), so it gets a DOORBELL_LOG row. Not carried: zerohedge's 'guts' framing; any figure for arrests or detentions (not read at a primary)."
---

# An ICE operation in southwest Kansas cut US cattle slaughter 16% in a day (Reuters, Thu 9/24). It's the first live case of the raid-linked labor gap LABOR registered today

**Short version:** in the week of 9/22, immigration agents ran an enforcement operation across southwest Kansas, the heart of US beef packing. Workers stayed home, plants slowed, and **estimated US cattle slaughter on Thursday 9/24 was ~90,000 head, down 16% from a week earlier** (Reuters, 9/25). One major plant killed ~500 head on 9/23 against ~5,600 capacity. Cattle futures fell as animals backed up. Industry and union officials say record beef prices could go higher.

| Figure | Value | Source (date) | Status |
|---|---|---|---|
| US estimated cattle slaughter, Thu 9/24 | ~90,000 head, **−16% w/w** | Reuters / Polansek (9/25), via syndication | search text; body not fetched |
| One SW-Kansas packer, Wed 9/23 | ~500 head vs ~5,600 capacity | same | same |
| ICE operation, SW Kansas meat plants | "sweeping" | KCUR (9/24) | headline + summary |
| Cattle futures | fell on slowed processing | tradingpedia (9/25); Drovers/AgWeb | secondary |

## Why each desk gets it

- **MARCO (ACTION):** immigration enforcement hitting labor supply is your lane. Does this operation move your foreign-born labor-supply read (SDL-01, ELEVATED at −379K YoY, basis Will-ruled 9/24)? Your call.
- **LABOR (ACTION):** your 9/29 packet lists **v11 "ICE raid-linked layoffs" as a counted gap**, with no phrase surviving the harness. This is a live instance, found through Will's feed, not the lane. Whether it is a v11 datum (displacement vs. absence, and whether it touches the payroll survey) is yours.
- **CARL (info):** a packer slowdown is a supply shock to the beef channel you track (KB-CARL-333: beef +11.2% YoY, June).

## Caveats that travel

1. **A one-day number.** The −16% is Thursday against the prior Thursday. There is no weekly total, and no evidence yet of how long it lasts.
2. **Absence is not layoffs.** Reports say workers stayed away for fear of arrest. Whether that becomes separations is not established.
3. **Reuters was read through a syndicator's search text, not the body.** Arrest and detention counts are not carried.
4. **The zerohedge headline "guts the workforce" is the wrapper's framing,** not a reported fact.

$0. No threshold moved.
