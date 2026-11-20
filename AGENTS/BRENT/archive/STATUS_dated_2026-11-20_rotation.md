# STATUS rotation 2026-11-20 (BRENT, PROME prome-77 wake)

Moved VERBATIM from `STATUS.md` to make room for the November 20 block under the 32,550 B read cap. Zero edits to payloads.

**PAYLOAD RULE:** each set's payload is exactly the text between its `<!-- BEGIN set X -->` line and its `<!-- END set X -->` line, excluding the single newline after BEGIN and the single newline before END. BYTES = `len(payload.encode("utf-8"))`; crc32 = `zlib.crc32(payload.encode("utf-8"))`.

| Set | Content | UTF-8 bytes | crc32 |
|---|---|---|---|
| a | November 16 dated block (COT #14, BRT-33 window 6 of 7, PortWatch token) | 950 | `dc94f333` |
| b | November 14 dated block (IEA OMR grade at secondaries) | 1573 | `aa011644` |
| c | 2026-11-14 rotation receipts line | 365 | `a421f2be` |
| d | November 14 summary for Will | 1244 | `8fe71506` |
| e | earlier-summaries pointer | 126 | `14ca5795` |

<!-- BEGIN set a -->
**November 16 (16:19 EST start, live session for PROME prome-6f, held open on PROME's instruction), SCOPED-PARTIAL:** v5.13 / WAIT unchanged; nothing armed. **COT #14 graded at the CFTC raw file: JOINT NOT-SPENT, eighth consecutive** (row below). **BRT-33 window +4.5200, valid 6 of 7, none under +3.5000** ([note](research/2026-11-16_brt33/NOTE.md)). Inbox drained (6 items; Russia diesel-export headlines, Omsk/Volgograd rows and the Bahrain/Bab el-Mandeb read logged on combo rows, no registered row moved). **PortWatch now needs a token** (own probe 16:23 EST, ArcGIS error 499): no live BRENT registry row reads it; it removes one member source from combo:gulf-flow-basis and leaves the NEXUS C35 Aug 31–Sep 1 rows UNREADABLE-AT-SOURCE. Brent continuous $92.16 (−3.84%) [vendor last 16:23 ET, contract UNKNOWN, about 10 min delayed, NOT a settle]. Morning routine levels → [monday_2026-11-16](demand_destruction/data/monday_2026-11-16.md).
<!-- END set a -->

<!-- BEGIN set b -->
**November 14 (11:25 EST start, PROME commission prome-fe, C9 / WQ-538 A), SCOPED-PARTIAL:** v5.13 / WAIT unchanged; nothing armed. **IEA November OMR (11/13) graded at five secondaries** (iea.org 403 per WALTER, not attempted): the **+1.7 mb/d Q4 surplus is a FORECAST** (Q4 supply 105.0), against EIA STEO +1.47 forecast, so two agencies agree within 0.23. The **observed** part is October: world stocks **+52 mb**, first rise since June, but oil on water **+86 mb**, so land stocks fell about 34 mb (own arithmetic) to the lowest since at least 2016: **the surplus is at sea.** OPEC is the outlier on demand (2026 +0.18 mb/d against IEA −2.7) [EST Argus via search]. **IEA spare capacity NOT FOUND**: the 11/29 spare read stays CONTESTED (EIA 0.01 vs Saudi-implied 1.2–1.3). **Dated Brent is under the future:** FRED DCOILBRENTEU 92.14 on 11/11 vs BZF27 92.76 (−0.62), −1.54 on 11/9; Dated fell 107.03 → 91.84 on 11/4. My "newest $107.03 (11/3)" lines of 11/8–11/11 are overtaken. combo:paper-physical-gap has both what_to_check conditions met (logging only). **FAA ground stop 11/13** (15:54 to about 20:15 EST): 9,132 cancelled Friday, 4,000+ Saturday [FlightAware via ABC/Yahoo]; upper-bound jet dent about 0.39 mb, about 0.056 mb/d on the week to 11/13 (own arithmetic on 1.777 mb/d [CONF EIA]), inside weekly noise; not fuel-driven, not BRT-09 evidence. TSA 11/13–11/14 not posted. **No registered row moves** (BRT-07/32/33/34, BG-02, F-a, price lines) → [note](research/2026-11-14_iea-omr/NOTE.md). Inbox drained: 5 WALTER cards (2 acted, 3 noted).
<!-- END set b -->

<!-- BEGIN set c -->
**Rotated 2026-11-14:** the November 13 block and its receipts, the November 12 and 10 reconciliation receipts, the November 13 refresh segment, the November 13 summary for Will, and the 9/07 dated-detail pointer with the older-receipts index line → [archive](archive/STATUS_dated_2026-11-14_rotation.md), six verbatim sets, bytes and crc32 per set in its header.
<!-- END set c -->

<!-- BEGIN set d -->
**November 14:** The International Energy Agency says the oil market is back in surplus, but read closely, the 1.7 million barrel-a-day surplus is a forecast for the October-to-December quarter, and it matches what the US Energy Information Administration said on November 10. What has actually been measured is October: world oil stocks rose for the first time since June, but more than all of that rise is oil sitting on tankers at sea on longer routes; oil stored on land fell to its lowest since at least 2016. At the same time the physical price of North Sea crude has dropped under the futures price since November 4, so the extra premium buyers were paying for prompt barrels is gone. OPEC still disagrees, because it thinks demand grows this year. ⚠️ The agency report itself was blocked to us; I graded it from five news accounts that agree with each other, and the one number I most wanted, how much spare production capacity the Saudis really have before the 11/29 OPEC+ decision, was not in any of them. Friday's nationwide flight grounding cost at most about 0.4 million barrels of jet fuel, too small to show in Wednesday's government data, and it is not an oil signal. No forecast or gate of mine moves. No decision for Will.
<!-- END set d -->

<!-- BEGIN set e -->
Earlier summaries → [November 14 rotation](archive/STATUS_dated_2026-11-14_rotation.md) set d and the archives it points to.
<!-- END set e -->
