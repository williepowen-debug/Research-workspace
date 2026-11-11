---
signal_id: "SIG-W-20261111-023"
date: "2026-11-11"
timestamp: "2026-11-11T19:21:45Z"
dispatched: "2026-11-11T19:21:45Z"
source: "WALTER"
origin: ["WALTER one-time re-read of skipped intake batches (WQ-676 A)"]
action: ["VULCAN"]
info: ["HENRY", "RED"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.7
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "AI_CAPEX"
entities: ["TrendForce", "optical fiber", "Seagate", "Western Digital", "HDD"]
word_count: 204
dispatch_note: "WQ-676 A re-read of the 10/19, 10/20, 10/25, 10/27 and 11/07 batches (85 alert-class items). Dup grep: no BOARD card or VULCAN KB row on fiber; HDD context in KB-VULCAN-192/-200. Figures from search summaries of the TrendForce release (not opened). ROUTINE: 23 days late, input-cost context, no gate."
event_window: "open"
---
# TrendForce (October 19): a 2026 optical-fiber shortfall of 180 million fiber-km lasting at least through 2028, with spot prices for in-data-center bend-resistant fiber forecast above 5x the 2025 level, AI backbone fiber about 2.8x, telecom fiber about 3.7x; HDD shortage timeline unsettled (Seagate nearline allocated through 2028 vs a 2H27 easing view); found in a skipped intake batch

Found by the one-time re-read of five intake batches WALTER's scan never displayed (WQ-676 A, Will 2026-11-11). Batch 10/19, TrendForce watch items.

| Item | Figures (source) |
|---|---|
| Optical fiber | 2026 global shortfall 180M fiber-km, shortage at least through 2028; spot finished fiber: bend-resistant in-data-center more than 5x 2025, AI backbone about 2.8x, telecom about 3.7x; utilization about 92%; inventory about one month vs four in 2024; preform expansion takes 18 to 24 months (TrendForce press release 2026-10-19; Xenospectrum adds these are spot outlooks, not contract prices) |
| HDD | TrendForce 10/2: nearline shortage persists; Seagate has most nearline capacity allocated through 2028, Western Digital most of 2027 (TrendForce News). A separate TrendForce-attributed view has easing in 2H27, date and context unconfirmed: **timeline unsettled** |

**Why VULCAN:** an input-cost leg of the build (your memory and input-cost axis), alongside the HDD supply discipline in KB-VULCAN-192 and -200 (Toshiba capacity, TDK heads). Not on the BOARD; no VULCAN KB row found for the fiber figures.

**Limits:** WALTER read search summaries of the TrendForce release, not the release page. Spot outlooks, not transaction prices.

**Ask:** VULCAN — does fiber or HDD input cost move your capex-cost or margin read? Context only otherwise.

Sources: TrendForce https://www.trendforce.com/presscenter/news/20261019-13275.html ; Xenospectrum https://xenospectrum.com/en/fiber-shortage-contracts-capacity-timeline/ ; TrendForce News https://www.trendforce.com/news/?p=64773 ; Research-Intake data/2026-10-19/news.json (items 11, 16, 17 in research/2026-11-11_intake-catchup/reread_items.tsv)
