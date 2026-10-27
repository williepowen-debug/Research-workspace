# ISHM data library

These are **frozen October 26, 2026 current-vintage histories**, built from accepted issuer downloads and labeled FRED mirrors. Live release truth remains [PRINTS](../workbook/PRINTS.tsv); do not cite a historical row as a first-published observation. Keep the underlying snapshots when new vintages arrive.

| File | What it contains | Basis and use |
|---|---|---|
| [SOURCES.tsv](SOURCES.tsv) | Source, unit, adjustment, vintage, endpoint and snapshot map | Metadata home for every panel column/source ID |
| [HARD_DATA_MONTHLY.tsv](HARD_DATA_MONTHLY.tsv) | 14 series aligned across 1,293 monthly dates | Real IP/capacity, nominal orders/shipments, Cass and monthly rail; heterogeneous units, not additive |
| [REGIONAL_MONTHLY.tsv](REGIONAL_MONTHLY.tsv) | 1,974 region-month records; five regional Feds | Current SA activity/orders/shipments/jobs/price diffusion measures; source eras differ |
| [REGIONAL_BREADTH.tsv](REGIONAL_BREADTH.tsv) | Same-month new-orders sign comparison; 268 complete months | Complete June 2004–September 2026; October 4/5 coverage, aggregate withheld |
| [EQUIPMENT_QUARTERLY.tsv](EQUIPMENT_QUARTERLY.tsv) | BEA equipment growth/levels over 317 quarterly dates | Growth begins 1947Q2; selected real levels begin 2007Q1. Latest 2026Q2; chained components not additive |
| [CALIBRATION.tsv](CALIBRATION.tsv) | 24 persistence/reference comparisons | Full history, recent window and pandemic-excluded samples; research candidates, no new registered gate |

Reproduce this **fixed snapshot**, without network access:

```sh
.venv/bin/python3 AGENTS/ISHM/research/2026-10-26_buildout/build_panels.py
```

The script uses exact snapshot columns/BEA table lines and refuses incorrect latest-source checks, empty BEA extraction, a missing-region aggregate, or a calendar-gap persistence join. `UNKNOWN` is missing; numeric zero is an observed zero. Source dates on month-end or KC's arbitrary day labels are normalized to the reference month, never used as release timestamps.

Important comparisons: Dallas `vnwo` is volume of new orders; `gro` is growth rate of orders and is excluded. Kansas City uses current-month SA rows, not future/year-ago/NSA rows. Philadelphia's September new orders are 29.2 in both the original saved release and the historical file; 29.5 in the initial notes was an ISHM transcription error. October 4.3 remains unchanged.

This reproducer is not a collector, scheduler or installed daily monitor. A future refresh saves a new dated source vintage and validates it against the new issuer release before updating working comparisons. First-published history, ISM component history, weekly AAR history and the broader freight/HY sample remain separate gaps.
