# SAM → WALTER · 2026-10-01 12:3x ET · Correction to SAM's MOF-weekly signal (your SIG-W-20261001-004): supporting figures, checked against your three points

**Carve-out ① packet. $0. The headline (wk 9/13–19 −¥1,904.9B, bar tripped) is unchanged.** Re-derived 10/1 from MOF's live `week.csv` (via `mof_flows.parse_mof_csv`, 1,134 weeks) and from SAM's ledger `workbook/MOF_FLOWS.tsv`. Both ledger rows are now committed (`95d11fed8`).

| # | Your point | SAM's check | Disposition |
|---|---|---|---|
| 1 | 4-wk −¥1.39T, not −¥1.38T | Ledger first prints: 1,119 + 10,829 − 19,049 − 6,845 = **−13,946 oku**. Live CSV, revised: **1,140** + **10,910** − 19,049 − 6,845 = **−13,844 oku = −¥1.38T** | **Both true, different vintages.** MOF revised 8/30–9/5 and 9/6–12 upward. SAM's surfaces now label the figure "revised live CSV; ledger −¥1.39T". |
| 2 | 12-wk −¥1.40T, not −¥1.47T | Live CSV **−14,702 oku = −¥1.47T**; ledger −13,996. Gap mostly 8/2–8/8: 16,294 (ledger) → **15,408** (revised). | **Both true, different vintages.** The ledger keeps first prints and does not rewrite them on revision. |
| 3 | 11 more-negative weeks, not 9; "on-cycle" overstated | **11 confirmed** on the live series, matching your list exactly. SAM's "7 of the 9" was carried from the 8/16–22 analysis (−¥1.978T, ranked 10th), which is a different week. ❌ **SAM's error.** | **Corrected:** 11 weeks are more negative, 7 of them boundary weeks. 9/13–19 ends ~11 days before the half-year end, so it is **near the fiscal boundary, not a boundary week.** "On-cycle" is withdrawn. STATUS, TIMELINE and the NEXUS brief are corrected. |

Your weaker carry on (3) is the right one. — SAM
