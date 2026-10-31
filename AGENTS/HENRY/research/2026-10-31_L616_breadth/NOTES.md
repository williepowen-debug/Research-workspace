# L616 market breadth: method, definitions, files (HENRY, 2026-10-31)

Commission: PROME C9 research commission (WQ-538 class), DOCKET L616; Will's request of 2026-10-07 ("investigate ... the breadth of the market"). Delivery memo: `PROME/inbox/2026-10-31_from-HENRY_L616-market-breadth.md`. One bounded session; no threshold, monitor, gate, card or capital action.

## Sources (all free)

| Source | What | As of |
|---|---|---|
| SSGA daily holdings files, `downloads/` (SPY, MDY, SPSM and the 11 Select Sector SPDRs) | membership of the S&P 500 (503), S&P 400 (400), S&P 600 (603); GICS sector for S&P 500 members by Select Sector SPDR membership; SPY shares held for cap weights | "As of 29-Oct-2026", downloaded 2026-10-31 13:04-13:05 ET |
| yfinance daily bars (`pull_prices.py`, `retry_failed.py`) | constituents 2024-01-02 to 2026-10-30; ETFs and indexes 2003 to 2026-10-30 | pulled 2026-10-31 13:07-13:10 ET; cache not committed (size) |
| `FORGE/tools/market-data/fetch.py` | cross-check of the 10/30 ETF and index closes | 2026-10-31 ~13:0x ET |
| yfinance `Ticker.info["industry"]` (`semis_set.py`, `semis.json`) | semiconductor set: 19 S&P 500 IT members labelled Semiconductors or Semiconductor Equipment & Materials | 2026-10-31 |
| VULCAN `workbook/MAG7_SERIES.tsv` | Mag-7 share of SPY fund weight and its RSP/SPY 63-session breadth leg (reused, reproduced at 10/29) | holdings 10/29 |

Non-equity holdings rows (an acquisition contra entry, two earnout rights, one index-futures leg) are excluded by rule in `build_universe.py`.

## Definitions

- **Above 50/200-day:** Close > simple average of the last 50/200 Closes (split-adjusted price); a full window is required, so the denominator is printed beside each figure.
- **Advance/decline:** Close against the prior Close (price basis). Cumulative A/D line based at 2025-01-02 (only differences between dates are meaningful).
- **New 52-week high/low:** intraday basis, High >= the highest High of the prior 251 sessions (Low <= lowest Low); 252 sessions of history required.
- **Horizon return:** dividend-adjusted close (total return); reference = last session on or before the anchor date (1 day 10/29, 1 week 10/23, October 9/30, 3 months 7/31, 6 months 4/30, YTD 12/31/2025, 12 months 10/30/2025).
- **Relative return:** ratio basis, (A/B) at 10/30 divided by (A/B) at the reference, minus 1, in percentage points (the VULCAN `mag7.py` basis).
- **Cap-weighted member return / contribution:** SPY fund shares held (29-Oct-2026) x Close at the reference date, constant shares. Tracks the index within 0.04pp (1 day) and 0.15pp (3 months); about 1pp at YTD/12 months, so longer-horizon contributions are approximate.

## Known limits

Survivorship (today's members applied backwards); exchange-wide NYSE/Nasdaq A/D and new-high/new-low series not reached; "% above 50/200-day" not validated against a published series (none reachable free: no Yahoo series, Barchart page empty to the fetcher); Nasdaq-100 and Russell 2000 member lists not obtained (ETF proxies only); Friday confounds (month-end rebalancing, 10/30 options expiry, tech earnings) not instrumented. Full list in the memo.

## Files

`build_universe.py` -> `universe.csv` · `pull_prices.py` + `retry_failed.py` -> price cache · `semis_set.py` -> `semis.json` · `breadth_compute.py` -> `breadth_daily.csv` (daily breadth by universe, 2025-01-02 to 2026-10-30), `stock_snapshot.csv` (1,506 members at 10/30), `results.json`, `report.txt` · `breadth_extra.py` -> `report_extra.txt` (tier base rates, October rarity, trajectory, weekly highs/lows, Friday decliners, KRE) · `verify_claims.py` -> `verify_claims.txt` (claims checked before the memo shipped).

Re-run: from the repository root, `.venv/bin/python3 -I <script> AGENTS/HENRY/research/2026-10-31_L616_breadth <cache_dir>` in the order above (`build_universe.py` and `semis_set.py` take the research directory only).
