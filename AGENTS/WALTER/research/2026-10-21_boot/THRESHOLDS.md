# October 21 threshold execution — PARTIAL

Fresh retrieval evidence: source-refresh.json / Cboe CSVs, hans-observations.json and prices.txt. Observation dates govern. No current whole-registry clearance. All four registry families loaded: RED12, REGINALD8, CREED11, HANS17. RED scan changed during the live RED owner session; updated scan was read whole and its banner matches canon SHA256 32203f81d7d4e5fe172204270ba4c1364df9058cc5d59d19163a1fc24a5b6da4. No owner files edited.

| IDs | Execution and current limit |
|---|---|
| RED01/02/12; REG03/04 | Latest retrieved HY329bp, observation October19; prior331 October16. Existing October19 signal003 records the three-print >320 entry; no duplicate fire. RED now records execution October21. Below350, above280/260. Exit counts zero on both distinct owner exit letters. API first_published labels alone do not prove the actual T+1 publication vintage. |
| RED03/04 | Registered official ICE front settlement sequence not obtained; UNGRADED. No continuous-ticker substitution. |
| RED05; REG05 | ICSA199K week endedOctober10, releasedOctober15; below250/300. October3 198K is revised, not a new first print. |
| RED06 | FRED VIXCLS18.44 October19, following19.99 October16 and16.46 October15: registered exit2/5, still banked. Cboe October20 close17.31 is visible but cannot complete the FRED-registered counter. Once that observation is published on VIXCLS, <18 would reset the exit; do not reset early. |
| RED07 | CCC1310bp October19, versus1297 October16; existing fired state, no new cycle or exit. |
| RED08 | No new CPI release; September fire remains banked. No hand recomputation or new grade. |
| RED09 | T5YIFR2.31% October20, below2.55 entry. No proximity claim from a stale distance. |
| RED10 | Publisher SKEW160.40 October20 versus161.86 October19; existing October14 fire, exit<140 count0/4. Cboe VVIX97.15 October20 is context, no new registered fire. |
| RED11 | H.15/FRED endpointOctober19; DGS30 5.48 versus5.60 October9, −12bp over five bond sessions. Updated RED owner scan explicitly classifies October9→19 FLOW with no weight and re-arms. Owner classification reported, not independently re-adjudicated from an incomplete letter. |
| REG01/02 | Vendor pre-open fetch supplies October20 KRE70.62/WAL75.30, explicitly stale/current-day unavailable. Neither supports a new KRE<60 entry or WAL>=81.90 exit; no new live-price claim. Existing WAL fired cycle retained, but complete current exit sequence not independently rebuilt. |
| REG06/07/08 | Quarterly FHLB and monthly Trepp are not new daily releases. Latest same-date SOFR3.88%−IORB3.90%=−2bp October20, not>15. FHLB official-print and Trepp cohort/source obligations remain owner-specific; no daily auto-clear. |
| CREED01a/01b/02/03/04/05/06/06b/07/08a/08b | Complete row set loaded with frozen/amended terms and owner fire log. Current property/event/cohort and TR-price evaluation incomplete. No fire or all-clear inferred from stale band_status cells. T05 belongs to HOMER; no CREED scoring. |
| HANS01/02/03/04 | Monthly PMI/final and scheduled ECB terms retained; no new release-grade executed. T02 post-hoc evidence caveat retained. |
| HANS05/06/09/10/13 | Registered benchmark-close/compound and France governing-screen sequences not refreshed sufficiently for a current grade. BOE fitted10Y5.374 October19 is a different instrument from TE benchmark close. ECB AAA request returned empty; no invented referee or UK near-trigger distance. |
| HANS07/11 | TTFX26 vendor87.38 October21 has contract metadata unresolved; not a settlement grade. EURUSD rounded1.12 is indicative, not spot-close certification. |
| HANS08 | Direct AGSI gasdayOctober19 EU74.62−AGSI-native norm89.236=−14.616pp. Existing orange remains open; latest day does not qualify for >−12 exit. Baseline composition/economic validation limits retained. Signal006 distinguishes Dutch national target from this EU metric. |
| HANS12/14/15/16/17 | T12 UNINSTRUMENTED. Qualitative banking/allocations perimeter and final inflation release checks incomplete; T15(b) instrument issue unresolved. No clean credit from silence or missing sources. |
| Cushing boundary3 | Direct EIA26.607M barrels, weekOctober9, versus20M threshold; no fire on retrieved print. October21 release not yet in this retrieval. |

Eligible-session calendar from RED/scripts/nonsession.py applies; October12 cash-bond holiday bridges the OAS run. Current named-contract official energy settlements and remaining boundary perimeter remain ungraded; Worldscale boundary5 has no instrument. No universal FRED publication clock assumed. Source limitations prevent a full 6c completion claim.
