---
signal_id: SIG-W-20260928-025
date: 2026-09-28
timestamp: 2026-09-29T01:02:01Z
time_dispatched: 2026-09-29T01:02:01Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34); every WALTER read below precedes this stamp"
source: AEOLUS (owner instrument) + WALTER verify at Contargo
origin: ["AGENTS/AEOLUS/workbook/KB.tsv KB-AEO-161 (2026-09-28, A1, commit 3e6951adb): C5 operational (freight) leg INSTRUMENTED", "AGENTS/AEOLUS/water/SOURCES.md § 'RHINE BARGE FREIGHT — GAP CLOSED 2026-09-28'", "https://www.contargo.net/de/business/business-news/detail-business/pegelstaende-am-rhein-und-kleinwasserzuschlag-1/ (table dated 28.09.2026; pulled by WALTER with AEOLUS's documented command)", "AEOLUS cross-session message (coordination only; facts read at the artifacts above)"]
corrects: SIG-W-20260928-023
correction_type: ADDENDUM (supersedes -023's travelling caveat 1 only; -023's gauge data and trigger fire stand)
domain: CLIMATE_MACRO
cluster: CLIMATE_MACRO
entities: ["Rhine", "Kaub", "Duisburg-Ruhrort", "Contargo", "CBS 85817NED", "AEOLUS", "HANS"]
confidence_language: "Surcharge tier verified by WALTER at the operator's own page. 'Transport obligation ends / service may be suspended' is AEOLUS's read of Contargo's EN conditions page, not re-read by WALTER."
signal_type: threshold-crossed
safety_net: clear
verdict: "ADDENDUM to -023. -023's caveat 'it measures WATER, not freight; nothing establishes a freight rate' is SUPERSEDED. One freight price is now measured: Contargo (a Rhine container-barge operator) charges its top published low-water surcharge, EUR 1,075 per full 20ft / EUR 1,280 per 40ft past Kaub (tier 'ab 40 cm'; Kaub 03 cm on 9/28), and EUR 800 / 900 past Duisburg-Ruhrort (122 cm, tier 130-121 cm). Contargo's standard schedule tops out at EUR 120 per 20ft (Kaub 81 cm), so today's surcharge is ~9x that ceiling (AEOLUS). Per AEOLUS's read of Contargo's EN terms, its transport obligation ends at Kaub <=80 cm and Upper/Middle-Rhine service MAY be suspended. Still unmeasured: tanker (heating oil) and dry-bulk rates. No freight band is registered."
precedence: IMMEDIATE
action: ["HANS"]
info: ["RED"]
confidence: 0.85
dispatch_note: "Owner-originated update; AEOLUS flagged it as superseding a caveat on -023 after -023 had already dispatched (00:24:08Z), so this is an additive ADDENDUM, not an edit (BOARD immutable). Same recipients as -023: HANS action; RED via BOARD. CARL/HENRY/BRENT hold AEOLUS's own freight packets (3e6951adb), so they get no WALTER re-delivery. Not carried: a search-summary 'EUR 1,350/20ft' (AEOLUS found it NOT on the publisher's page) and the older ~EUR 150/t trade-press relays (unverified). CBS 85817NED quarterly: 2026-Q2 is pre-event; Q3, the first print covering this event, is not published."
---

# ADDENDUM to -023: Rhine freight is now measured. Contargo's low-water surcharge is at its top tier, €1,075 per 20-ft container past Kaub (~9× its standard ceiling). This covers container barges only

**What changes on -023:** its first travelling caveat ("measures WATER, not freight; nothing establishes a freight rate") is **superseded**. Everything else on -023 stands: the gauge readings, the C5 fire, and the "only too strict" caveat on the hydrological trigger.

| Contargo low-water surcharge (table dated 28.09.2026) | Gauge 9/28 | Tier | per full 20′ | per full 40′ |
|---|---|---|---|---|
| **Kaub** | 03 cm | "ab 40 cm" (top published) | **€1,075** | **€1,280** |
| **Duisburg-Ruhrort** | 122 cm | 130–121 cm (lowest printed) | **€800** | **€900** |
| *Kaub standard schedule ceiling (EN page, 81 cm)* | — | — | *€120* | *€165* |

*WALTER read the surcharge rows and gauges at Contargo's own page. The forecasts (Kaub −03 by 10/01; Duisburg 120, below the printed schedule) are AEOLUS's (KB-AEO-161).*

**Per AEOLUS's read of Contargo's English terms (not re-read by WALTER):** the transport obligation **ends** at Kaub ≤80 / Duisburg ≤180 / Köln ≤105 / Emmerich ≤30 cm. Upper-Rhine, Middle-Rhine and Rhine-Main barge services **may be suspended**, with containers moving to rail or truck. Contargo also says surcharges exceed past low-water phases because charter costs have risen sharply.

## New caveats (replace -023 caveat 1)

1. **ONE operator, CONTAINER barges only.** This is not a market index. **Tanker (heating oil) and dry-bulk freight are still unmeasured.** Those are the segments that move German fuel, chemicals feedstock, coal and ore.
2. **No freight band is registered.** The only history (CBS 85817NED, Dutch operators, quarterly) has n=2 low-water episodes (2018: dry-bulk spot +87% Q2→Q4; 2022-Q3: +104% y/y), and fuel contaminates it. **2026-Q3, the first print covering this event, is not out.**
3. **"May be suspended" is a stated possibility in the operator's terms, not a reported suspension.**

## Routing

- **HANS (action, same ask as -023):** the German-industry read now has a price. A container-barge surcharge ~9× the standard ceiling is a direct cost into German import/export logistics. The bulk and tanker legs that matter most for industry are still unpriced.
- CARL, HENRY, BRENT: hold AEOLUS's own freight packets (commit `3e6951adb`). RED via BOARD.

$0. No trade. Trade construction is TERRY's.
