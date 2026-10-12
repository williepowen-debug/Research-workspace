# Regional bank market and technical research

Start here for REGINALD's regional-bank prices, performance, KRE holdings, charts and technical studies. Dated snapshots keep each observation's timestamp and comparison window attached to its figures. Original source records remain at their established paths.

## Saved market data

| Material | Observation date | Open |
|---|---|---|
| Maintained bank cohort and benchmarks | October 12, 2026, 11:16 EDT quote snapshot; July 10–October 9 price window | [Regional bank tape CSV](snapshots/2026-10-12/regional-bank-tape.csv) |
| KRE ten heaviest bank holdings and KRE benchmark | October 12, 2026, 13:33 EDT fetch; each row carries its trade timestamp | [Top ten performance CSV](snapshots/2026-10-12/kre-top10-performance.csv) |
| Full published KRE holdings | October 9, 2026 holdings, retrieved October 12 | [Holdings CSV](snapshots/2026-10-12/kre-holdings.csv) |
| Will's six-panel bank chart | Supplied October 12; capture timestamp unknown; three-month view with 30-minute bars | [Original chart](charts/2026-10-12_regional-banks_3m_30m.jpg) |

[Snapshot provenance](snapshots/2026-10-12/provenance.json) records the source paths, hashes, export time, row counts and chart limitations. CSV files are derived exports of the preserved source records; they are dated observations, not live quotes. [SNAPSHOTS.tsv](SNAPSHOTS.tsv) inventories the saved snapshots, and [RESEARCH_INDEX.tsv](RESEARCH_INDEX.tsv) locates related source files, studies and tools.

The top-ten historical returns end on October 9 and exclude dividends. Bank feeds declare 15–20-minute delays; Nicolet's last recorded trade in the 13:33 fetch was 13:12 EDT. KRE holdings weights are also dated October 9. The chart's selected candle values may differ from its latest-price labels.

## Source records and analysis

Latest synthesis: [KRE price patterns through October 9](studies/2026-10-12_KRE_price_patterns.md) — recent weakness, former relative winners turning down, and the gap between current holding weights and historical fund contributions.

| Subject | Canonical records |
|---|---|
| Morning prices and three-month comparison | [Quotes](../../domain/sources/2026-10-12_morning-bank-tape/quotes.json), [settled comparison](../../domain/sources/2026-10-12_morning-bank-tape/settled-history.json), [tape analysis](../../reports/2026-10-12_morning-regional-bank-tape.md) |
| KRE composition and weighting | [Issuer spreadsheet](../../domain/sources/2026-10-12_KRE_holdings/holdings-daily-us-en-kre.xlsx), [top ten weights](../../domain/sources/2026-10-12_KRE_holdings/top10.tsv), [weighting rules](../../domain/sources/2026-10-12_KRE_holdings/weighting-rules.json) |
| Top ten price performance | [Calculated returns](../../domain/sources/2026-10-12_KRE_top10_performance/performance.json), [daily price history](../../domain/sources/2026-10-12_KRE_top10_performance/settled-history.json), [interpretation and feed limits](../../domain/sources/2026-10-12_KRE_top10_performance/summary.json) |
| Volume and accumulation or distribution | [April 9 volume study](../../trade/market-microstructure/RP-REG-5.1_KRE_Volume_Analysis.md), historical findings and methods |
| Existing technical checks | [Settled-price ladder](../../scripts/vx_ladder_check.py), [KRE float tool](../../scripts/kre_float.py), [monitoring entry point](../../scripts/boot.py) |
| Credit explanation for EGBN's divergence | [EGBN cleanup verification](../../reports/2026-10-12_EGBN_cleanup_figure_verification.md), June 30 credit vintage checked October 12 |

The older short-interest, short-volume, dark-pool and options-open-interest ledgers are **FROZEN**. They remain historical references in the research index. Indexing them here does not refresh their figures. Price divergence and volume patterns require evidence before being attributed to credit improvement, institutional buying or short covering.

## Saving subsequent work

Save each market observation under `snapshots/YYYY-MM-DD/`, using a time suffix when there is more than one observation that day. Store new technical analysis under [studies/](studies/README.md) and supplied or generated charts under `charts/`. Create those dated study files when research is performed. Retain earlier observations.

Every saved observation or study needs the tickers, source, retrieval time and timezone, actual trade or bar timestamps, interval, comparison dates, dividend or split treatment, and any feed delay. Technical indicators also need their parameters and input series. For moving averages, RSI, support or resistance, distinguish calculated measurements from judgment about a price level.

Keep original downloaded data and receipts in `domain/sources/`; link them from the study and record derived CSV exports in `SNAPSHOTS.tsv`. Treat exports as reproducible views of those originals. Add substantive findings to `workbook/KB.tsv` and point desk state to the relevant artifact. Reopening an old snapshot does not make its prices current.

REGINALD owns the cohort view. WAL, OZK and FLG retain their existing desk ownership and canonical paths. Credit filings, funding research and trade construction retain their established homes and can be linked from a market study when relevant.
