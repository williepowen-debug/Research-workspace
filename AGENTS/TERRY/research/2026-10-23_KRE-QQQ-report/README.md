# KRE vs QQQ divergence report — working folder (TERRY, 2026-10-23)

Will-requested ("save the report inside TERRY so we can continue working on it"). Ideas only; no card fired, nothing approved or placed.

| What | Where |
|---|---|
| Live report page (Dashboard artifact) | https://claude.ai/artifact/GEqqMLyMMJieo4t2NpeJQq |
| Live divergence map (Dashboard artifact, kept separate at Will's request) | https://claude.ai/artifact/8JAPSUTSqPQL4nEGtSPc6h |
| Readable report (generated from `data/`) | `REPORT.md` — regenerate with `python3 -I make_report_md.py` |
| Page sources | `page/report_index.html`, `page/map_index.html` (the store's `files/index.html` text for each) |
| Datasets (fixed snapshots, yfinance, data through the 10/22/2026 close) | `data/*.csv` |
| Rebuild the report datasets | `build_report_data.py` (writes `data/`; needs network; `px.csv` = frozen backtest prices) |
| Strategy backtest model | `seesaw_bt.py` + `px.csv` |
| Session notes behind it | `../2026-10-23_KRE-QQQ-relationship.md`, `../2026-10-23_seesaw-backtest/` |

**To update the live pages:** rebuild `data/`, upload each changed CSV as an asset to the artifact, `update` its `datasets/<id>` (`url`, `name`, `updated`), and write the page text to `files/index.html` (pin `if_version`). The two artifacts hold separate asset copies; update both if a shared dataset changes (`kre_qqq_daily`, `yearly_corr`, `divergence_episodes`).

Not built here: `kre_qqq_daily.csv` and `yearly_corr.csv` came from the session's first pull (yfinance auto-adjusted closes; KRE/QQQ/^TNX from 2023-12-01, 20-day rolling correlation of daily returns; yearly correlation from 2006-06-23). `book_snapshot.csv` and `trade_ideas.csv` are hand-entered from the FORGE mirror (10/22 11:01 ET) and the 10/23 screening quotes — re-verify before any card.
