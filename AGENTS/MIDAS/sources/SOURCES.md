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
| **CFTC Socrata API** (COT: gold/silver/copper net NC positioning) | M1/M2/I1 positioning arc | raw `urllib` JSON pull, schema-field-verified (L-05) | weekly (Fri release, Tue data) | LIVE but **manual** — not yet wired to a cadence leg (OPEN item; boot doesn't auto-pull COT) |

## Primary sources (manual / periodic)

| Source | Feeds | Access | Wall / note |
|---|---|---|---|
| **WGC gold.org GDT** (CB gold demand, ETF flows) | M1 CB-floor layer (Tier-2) | WebFetch of the rendered central-banks/ETF pages (primary; carries published figures) | **GDT Excel data-file (file 20499) 403-gates automated curl** (redirects to homepage) — L-09. The rendered pages ARE primary; Q1 = 243.7t CONF (KB-019). "17th consecutive month" streak + 700–900t FY target NOT on the fetched section → STAY PROV. Q2 GDT (~late July) = v2 kill-cond #2 |
| **Federal Register** (PGM antidumping/CVD/injury) | I2 supply/sanctions leg | WebFetch/raw of federalregister.gov docs | Russia-Pd AD final **132.83%** (doc 2026-08487, CONF, KB-020). 828% was preliminary/trade-press (L-08). CVD doc 2026-10342; USITC injury 2026-12219 |
| **WPIC** (platinum quarterly deficit) | I2 structural deficit backdrop | not yet primary-pulled | ~240koz 2026 Pt-deficit STAYS PROVISIONAL (KB-008) — WPIC quarterly not fetched. OPEN |
| **NBS China** (Q2 GDP etc.) | I1 China-demand test anchors | WebSearch + PROME cross-verify | GDP release dates drift ±1d — VERIFY vs stats.gov.cn calendar at registration, not grade time (L-10: MIDAS-04 registered ~7/16, actual 7/15) |
| **PBoC** (LPR fixing) | I1 China-policy test (MIDAS-05) | pbc.gov.cn / WebSearch | Convention = 20th of month (quotes before 9am CST). July fixing ~Mon 7/20; reconcile ZHAO's docketed 7/21 |

## Domain-ownership boundaries (reference, don't re-pull)
- **Real-rate LEVEL / auctions / curve** → BOND canonical (MIDAS references DFII10/DGS2; reconcile to one figure).
- **China macro / capital flows / copper imports** → ZHAO canonical (the −41.3% YoY import series is ZHAO's; base-effect-check owed).
- **HY/credit/liquidity / DXY-squeeze / EndGame** → LIQUID canonical (MIDAS supplies the gold-leg read; LIQUID consumes metals-board gold levels as of 7/17).
- **PGM supply geopol** → HAWK. **Macro velocity** → HENRY.
