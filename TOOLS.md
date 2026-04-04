# Tools

## Utilities
- `pdfminer.six`: `from pdfminer.high_level import extract_text`
- Python venv at `.venv/`
- `web_search` / `web_fetch` — built-in OpenClaw tools. Use for live data verification, fact-checking MEMORY entries, pulling current prices/news.
- OAS overlay: `python3 FORGE/timing/scripts/oas_overlay_2007.py` — 2007 vs 2026 HY/CCC OAS comparison, threshold crossings, credit→equity lag.

---

## Market Data
**Location:** `FORGE/tools/market-data/` | **Docs:** `README.md`

Pull live prices and economic data. Use this BEFORE citing any price or economic figure.

```bash
python3 FORGE/tools/market-data/fetch.py price KRE APO WAL OZK   # live prices
python3 FORGE/tools/market-data/fetch.py fred ICSA                # FRED series
python3 FORGE/tools/market-data/fetch.py all                      # everything
python3 FORGE/tools/market-data/dashboard.py                      # full stress dashboard
python3 FORGE/tools/market-data/dashboard.py --compact            # one-line (Telegram)
python3 FORGE/tools/market-data/dashboard.py --quiet              # red breaches only
```

**Config:** `config.py` — thresholds, tickers, tier assignments. Single source of truth.

---

## News Sweep
**Location:** `FORGE/tools/news-sweep/` | **Docs:** `README.md`

Thesis-tagged news monitoring. Fetches Google News RSS, FT/BBC RSS, ZeroHedge. Classifies against entity index and agent WATCH_FOR lists. Routes to agent inboxes. Suppresses known stories.

```bash
python3 FORGE/tools/news-sweep/sweep.py --compact                # Telegram-friendly summary
python3 FORGE/tools/news-sweep/sweep.py --compact --route         # + write to agent inboxes
python3 FORGE/tools/news-sweep/sweep.py --compact --agent BROCK   # single agent
python3 FORGE/tools/news-sweep/sweep.py --alerts-only             # 🔴 items only
python3 FORGE/tools/news-sweep/sweep.py --dry-run                 # classify but don't save
```

**Config:** `config.py` — queries, entity index, WATCH_FOR lists, keywords, source weights, noise filters.
**Outputs:** Agent inboxes (`AGENTS/{name}/inbox/sweep_*.md`), `latest.json`, `latest.md`.
**Status:** v1 live. First automated cycle Mon Apr 7. v2 (auto entity refresh, embedding matching) after 1 week of data.

---

## Web Dashboard
**Location:** `dashboard/server.py` | **Port:** `:8080`

Serves stress API, news feed, network visualization, and alert state.

| Endpoint | What |
|----------|------|
| `/` | Main dashboard |
| `/api/stress` | Stress data JSON (same as `dashboard.py --json`) |
| `/api/news` | Latest news sweep results |
| `/network.html` | Agent network visualization |

**Restart:** `cd dashboard && python3 server.py &` (or check `ps aux | grep server.py`)

---

## Cron Schedule

| When | What | Script |
|------|------|--------|
| Every 5min M-F | Market data + Telegram alerts on zone changes | `market-data/cron_dashboard.sh` |
| 6:00 AM ET daily | Morning briefing (audio + Telegram) | `market-data/morning_briefing.sh` |
| 8:30 AM ET M-F | News sweep + agent inbox routing | `news-sweep/cron_sweep.sh` |

All cron jobs push to Telegram automatically. Check `crontab -l` to verify.
