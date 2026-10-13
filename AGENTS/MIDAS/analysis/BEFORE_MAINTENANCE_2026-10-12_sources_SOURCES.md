# MIDAS — SOURCES register (data-access map)

**Created 2026-07-17** (self-audit — consolidates the source/access-wall map previously scattered across KB rows + LESSONS). One row per live data source: what it feeds, how it's pulled, cadence, and any documented access wall. Update when a source/wall changes; cite KB/LESSONS for the incident detail.

> **Golden rule (L-05):** any structured-data API whose exact numbers are load-bearing must be pulled RAW (urllib/JSON), never summarized by WebFetch's small model — it hallucinates figures. WebFetch is fine for narrative/rendered-page confirmation, not for the number itself.

## Primary sources (live, wired)

| Source | Feeds | Access method | Cadence | Status / wall |
|---|---|---|---|---|
| **FRED DFII10** (10Y TIPS real yield) | M1 real-rate leg + divergence classifier | `fetch.fred_fetch("DFII10")` (FORGE client) → `metals_watch.py` leg 1 | daily, **T+1 publish** (latest obs lags 1 business day) | LIVE. Direct `fred.stlouisfed.org/graph/fredgraph.csv` timed out this session — use the FORGE `fred_fetch` client, not raw CSV |
| **FRED DGS2** (2Y nominal) | rate-expectations cross-check (LIQUID seam) | `fetch.fred_fetch("DGS2")` | daily, T+1 | LIVE. Used 7/17 to verify LIQUID's −8bp (KB-026). Curve/rates = LIQUID/BOND canonical; MIDAS references |
| **yfinance COMEX futures** (GC=F/SI=F/HG=F/PL=F/PA=F) | M1/M2/I1/I2 spot + GSR | `fetch.py` price client → `metals_watch.py` leg 0 (primary) | intraday / last-close (weekend = Fri close) | LIVE. yfinance lives in `.venv` (not system python). **FIXED 2026-07-23: boot.py now self-selects `.venv/bin/python` for its child scripts, so leg 0 runs regardless of the launch interpreter** (previously errored under system `python3`). Manual pulls: `.venv/bin/python …` |
| **yfinance ETF proxies** (GLD/SLV/CPER/PPLT/PALL) | spot cross-check (NOT 1:1 unit-matched) | `metals_watch.py` leg 0 (secondary row) | intraday | LIVE. Secondary confirmation only |
| **westmetall.com** (LME copper stock series) | I1 inventory leg + 2yr-median baseline | HTML-table scrape (browser UA), fail-loud → `metals_watch.py` leg 6 | business-daily | LIVE. Closes the "no free LME source" wall (CME warehouseStockAPI 403'd; LME.com vendor-gated). Baseline = trailing-2yr rolling median (KB-018) |
| **CFTC legacy raw report / Socrata** (gold/silver/Pt/Pd; copper manual) | M1/M2/I1 positioning arc | gold/Pt/Pd/Ag raw `deafut.txt` via `cot_gold.py` / `cot_metals.py`; code/name and totals guards. Copper historical/manual uses Socrata raw JSON | weekly (Fri release, Tue data) | LIVE. Gold freshness is boot leg 3; Ag/Pt/Pd freshness is boot leg 4 (2026-10-12), each against consumed-vintage ledgers. Positioning context, not a standing band. Copper COT remains manual |

## Primary sources (manual / periodic)

| Source | Feeds | Access | Wall / note |
|---|---|---|---|
| **WGC gold.org GDT** (CB gold demand, ETF flows) | M1 CB-floor layer (Tier-2) | WebFetch of the rendered central-banks/ETF pages (primary; carries published figures) | **GDT Excel data-file (file 20499) 403-gates automated curl** (redirects to homepage) — L-09. The rendered pages ARE primary; Q1 = 243.7t CONF (KB-019). "17th consecutive month" streak + 700–900t FY target NOT on the fetched section → STAY PROV. Q2 GDT (~late July) = v2 kill-cond #2 |
| **Federal Register** (PGM antidumping/CVD/injury) | I2 supply/sanctions leg | WebFetch/raw of federalregister.gov docs | Russia-Pd AD final **132.83%** (doc 2026-08487, CONF, KB-020). 828% was preliminary/trade-press (L-08). CVD doc 2026-10342; USITC injury 2026-12219 |
| **WPIC** (platinum quarterly balance) | I2 structural deficit backdrop | PRIMARY perspectives page 2026-10-09 read 2026-10-12 | 2026 forecast **265 koz surplus**, deficit from 2027; retires old provisional deficit backdrop. Primary quarterly PDF still not fetched. See KB-130 and due review |
| **NBS China** (Q2 GDP etc.) | I1 China-demand test anchors | WebSearch + PROME cross-verify | GDP release dates drift ±1d — VERIFY vs stats.gov.cn calendar at registration, not grade time (L-10: MIDAS-04 registered ~7/16, actual 7/15) |
| **PBoC** (LPR fixing) | I1 China-policy test (MIDAS-05) | pbc.gov.cn / WebSearch | Convention = 20th of month (quotes before 9am CST). July fixing ~Mon 7/20; reconcile ZHAO's docketed 7/21 |

## Domain-ownership boundaries (reference, don't re-pull)
- **Real-rate LEVEL / auctions / curve** → BOND canonical (MIDAS references DFII10/DGS2; reconcile to one figure).
- **China macro / capital flows / copper imports** → ZHAO canonical (the −41.3% YoY import series is ZHAO's; base-effect-check owed).
- **HY/credit/liquidity / DXY-squeeze / EndGame** → LIQUID canonical (MIDAS supplies the gold-leg read; LIQUID consumes metals-board gold levels as of 7/17).
- **PGM supply geopol** → HAWK. **Macro velocity** → HENRY.

## Bounded PGM access update — 2026-10-12

CME primary `delivery_reports/PA-PL_Stck_Rprt.xls`: latest report10/12/activity10/9 retrieved with installed curl_cffi browser-like request after urllib403. Latest inventories accessible; September30 matched history not retrieved. Aberdeen PPLT/PALL public fund pages yield dated10/9 raw NAV/assets/market metadata, but no reported share-count or physical-ounce history in the retrieved payload. Lease rates remain missing in existing accessible sources. One-off evidence only; no monitor/pipeline added. Detail `../analysis/2026-10-12_PGM-inventory-flow-followup.md`.

## M1 historical reference — 2026-10-12 second round

Reused `2026-10-12_review/GLD.csv`, `DFII10.json` and `GLD_DFII10_pairs.csv`: 690 matched ending dates, 2024-01-03→2026-10-08; latest-revised snapshot captured October 12, 16:54:07 ET. Rebuilt pairs match exactly; 6 change-start date mismatches, 0 corporate actions. No older reconstructible raw GLD/DFII10 input was found in MIDAS sources, despite the VECTOR-3 historical summary. Draft/reference evidence in `2026-10-12_m1-draft/`: 4 disjoint-input grid episodes, 0 eligible below-flip starts. Longer conditional raw history and historic as-of vintages are missing. No source refresh, new access search or persistent tool.
