# September STEO versus August — September 9, 2026

September's forecast keeps more pressure in Q4 because its expected supply recovery is smaller. It does **not** move the modeled return of OPEC spare capacity beyond April 2027. The opposing evidence is substantial: Q3 draws are smaller and OECD inventory levels are revised higher. BRENT's timed-race framework remains applicable; this is an evidence update, not a new thesis probability, phase transition, trade signal or verified reopening.

## Source and method

[CONF source vintage] EIA September issue: **September 9**, modeling completed **September 3**. August issue: **August 11**, modeling completed **August 6**. September inputs exclude later market events, including September 8–9 attacks. Retrieved September 9 at approximately 15:24 ET; source URLs, response types and SHA-256 hashes are in [source-manifest.json](source-manifest.json).

Primary sources: [September workbook](https://www.eia.gov/outlooks/steo/archives/sep26_base.xlsx), [September report](https://www.eia.gov/outlooks/steo/archives/sep26.pdf), [August workbook](https://www.eia.gov/outlooks/steo/archives/aug26_base.xlsx). August local evidence remains unchanged in [the morning baseline](../2026-09-09_squeeze-review/august-steo-baseline.json).

All forecast/estimate quantities below are **[EST EIA, September/August 2026 vintages]**; differences and aggregates are BRENT calculations from those files, not observations of realized production. Seven original series are reproduced with the same units and months. Flow/capacity quarters use **simple monthly means**, matching BRENT's saved vintage ladder; stock quarters use **quarter-end levels**. Positive `t3_stchange_world` is a **draw**. The sign is checked against consumption minus production for every month in both vintages. All 24 months of 2026–27 are retained in [comparison.json](comparison.json).

Published EIA quarterly flows are day-weighted. For example, September Q3 draw is **2.9846** on our simple-mean basis and **2.96** rounded in PDF Table 3a. `compare.py` independently reproduces the printed quarterly draws and OECD stocks at published precision; this is not a discrepancy to fix by changing the baseline method. Repeated world-total rows in the workbook are accepted only if their entire contents agree.

## 1. Q4 tightness is a supply revision, partly offset by weaker demand

Million barrels/day; each cell is August → September (revision):

| Series / ID | Q3 2026 | Q4 2026 | Q1 2027 | Q2 2027 |
|---|---:|---:|---:|---:|
| World production `papr_world` | 99.6651 → 100.2573 (+0.5922) | 103.6613 → 102.1536 (−1.5077) | 107.3306 → 106.4750 (−0.8556) | 109.5606 → 110.0427 (+0.4821) |
| World consumption `patc_world` | 103.5105 → 103.2419 (−0.2686) | 104.2870 → 103.8627 (−0.4243) | 103.5330 → 103.5030 (−0.0300) | 104.9728 → 104.9969 (+0.0240) |
| World draw `t3_stchange_world` | 3.8454 → 2.9846 (−0.8608) | 0.6257 → 1.7091 (+1.0834) | −3.7976 → −2.9719 (+0.8256) | −4.5878 → −5.0458 (−0.4580) |
| OPEC+ liquids `papr_opecplus` | 33.1284 → 33.6758 (+0.5474) | 35.8550 → 35.1100 (−0.7450) | 38.7114 → 37.8786 (−0.8327) | 39.7544 → 39.8015 (+0.0470) |

Q4's extra **1.0834 mb/d draw** equals **1.5077 less supply minus 0.4243 less consumption**. The Q3→Q4 world production increase falls from **3.9962** in August to **1.8963 mb/d** in September. OPEC+ liquids' corresponding increase falls from **2.7266 to 1.4342 mb/d**. Recovery remains in the model; substantially less arrives during Q4.

Do not subtract OPEC spare crude capacity from OPEC+ liquids: their membership and product perimeters differ. Nor does this forecast establish compliance with an OPEC announcement.

## 2. Higher stocks qualify the more persistent Q4 draw

OECD commercial crude and other liquids, `pasc_oecd_t3`, million barrels at quarter-end:

| Date | August | September | Revision |
|---|---:|---:|---:|
| June 2026 | 2,643.8990 | 2,735.1589 | +91.2598 |
| September 2026 | 2,527.2544 | 2,650.9098 | +123.6554 |
| December 2026 | 2,476.9002 | 2,568.3135 | +91.4133 |
| March 2027 | 2,563.3893 | 2,633.8249 | +70.4355 |
| June 2027 | 2,688.1409 | 2,773.6648 | +85.5239 |

September's projected Q4 OECD depletion is **82.5963M barrels**, versus **50.3542M** previously. Nevertheless, the revised starting inventory is higher, so year-end stocks also remain higher. This prevents the misleading conclusion that every buffer is now closer to exhaustion. OECD stocks are a subset of global inventory; do not force their change to equal the world residual balance.

## 3. Spare-capacity timing is unchanged

Table 3d's OPEC surplus crude production capacity `cops_opec` remains **0.020 mb/d in July–December 2026**, **0.030 in January–March 2027**, and **2.380 from April 2027**. Middle East OPEC `cops_opec_r05` remains **zero through March 2027**, then **2.350 from April**. Both vintages have the same forward monthly path.

This is still one agency's modeled capacity series, not multiple independent confirmations or physically verified deliverability. September therefore **does not postpone the spare-capacity recovery date** relative to August. Re-read the then-current primary before the October 4 OPEC decision; today's unchanged estimate is not indefinite permission to carry it.

## 4. Product pressure persists under a conditional easing forecast

Table 4a U.S. distillate end-month stocks `DFPSPUS` fall from **104.7256 → 99.4153M** for September and **97.4857 → 92.8305M** for October. December falls **114.0620 → 109.1148M**. This independently specifies the inventory path behind the report's below-100M September outlook; 100M is an EIA descriptive level, **not a newly registered BRENT threshold**.

Table 2 Brent spot-average forecasts `BREPUUS` rise **$78.00 → $90.6667/bbl for Q4** and **$74 → $85 for Q1 2027**, using simple monthly means. Wholesale diesel `DSWHUUS_$` rises **$3.2192 → $4.2831/gal for Q4**. Those monthly forecasts cannot be compared as if they were today's futures quotes or retail pump readings.

The report's petroleum-products section (printed pages 6–7) links later diesel easing to recovering tanker flows, Gulf product exports and Asian refinery feedstock. It retains Russian refinery constraints into H1 2027. These are conditional forecast channels, not a new facility-level verification; no incident row is refreshed from an aggregate narrative. The EIA forecast does not supply BRT-12's missing original crack construction or upstream E&P credit history.

## 5. Source limits that must remain visible

- **2027 timing language differs inside the source.** Printed page 5 describes inventories starting to build in H2 2027, while Table 3a and the monthly workbook already show builds from **January 2027**, with Q1 simple-mean build **2.9719 mb/d**. Use the numeric table for this comparison. Do not silently reinterpret the narrative as an H2-only transition or manufacture an exact date of physical reopening.
- **Notable-changes crack row is not adopted.** Printed page 3's annual distillate-crack summary and pages 6–7's monthly U.S. diesel-crack discussion need a definition/basis reconciliation before reuse as one series. This report uses explicit inventory and price IDs instead; no inferred crack history is promoted into BRT-12.
- Local `global-oil.html` and `products.html` are **EIA “Unexpected Error” pages despite HTTP 200**. They are preserved as failed captures, explicitly classified in `comparison.json`, and are not evidence. The archived PDF provides the narrative above. Overview, XLSX and PDF contents were inspected. Web-reader access to the narrative pages does not repair the failed local captures.
- Higher global shut-in estimates and Vortexa claims quoted by EIA are not independent measurements by BRENT. No aggregate current outage, Saudi throughput, tanker flow, current SPR authority or broker state was verified here.

## What BRENT should do with this

**Assessment:** keep attention on whether operational supply/product flows catch up with demand, and on the inventory starting level. September raises the cost of assuming rapid Q4 relief, but its higher OECD stock base and 2027 builds remain counterevidence to a durable outright-price squeeze. **v5.8 calibration, dated horizons/falsifiers and WQ-189/192 STAND DOWN remain unchanged.**

**Next physical checkpoint:** September 10 WPSR, noon ET headline / 14:00 supporting batch, intended week ending September 4. Apply the already saved worksheet: Cushing, distillate stocks, product supplied, utilization/PADD3 inputs and first registered SPR observation. One week cannot resolve the two-print SPR test, and the contract/authority interpretation gap remains. Then September 11 Baker Hughes/COT. Original BRT-12 construction and the overdue BRT-29 carrier-evidence review remain separate work; scheduler repair is prepared, not installed.

## Reproduction and closeout

From repository root: `.venv/bin/python3 AGENTS/BRENT/research/2026-09-09_steo-comparison/compare.py`. [Validation output](validation.txt) records all checks; source downloads refuse overwrite. The August workbook/baseline were not rewritten.

[Boot output](boot-network.txt): **rc=2, four FINDINGS, no crashed script** — dated August 28 EIA observations, unresolved BRT-29 M sub-obligation, Baker Hughes listing timeout and ledger nudge. Corrections check passed. Incidental boot quotes were not adopted into the dashboard. The boot calendar check precedes this comparison's docket completion.

Ledger dispositions: CATALYSTS receives the completed research read; LESSONS_INDEX unchanged because no new lesson; INCIDENTS unchanged because no facility-specific source verification; board_log unchanged because no packet consumed; TRADE unchanged because no new execution/position decision; REGISTRY unchanged because no instrument or numeric-letter change. Frozen KB/VX/FLOW/TIMELINE and prediction grades remain untouched. Existing OSPREY inbox item remains deferred; WALTER/MSG lanes empty, no outbound message.

Closeout checks passed: generated calendar matches all **21** docket rows; all rows retain the eight-field schema; standing-state check passes. STATUS **30,907 bytes**, SCRATCH **7,214**, and NEXUS/CLAUDE are below the **32,550-byte** budget. Authored changes pass whitespace checks. October **6** next STEO date is confirmed in the captured overview and registered as the monthly successor; it installs no scheduled task.
