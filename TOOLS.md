`pdfminer.six` installed: `from pdfminer.high_level import extract_text`

## Market Data Tool
**Location:** `FORGE/tools/market-data/`
**Status:** ✅ Complete (all 3 layers)

Pull live prices and economic data. Use this BEFORE citing any price or economic figure — never rely on stale STATUS file numbers.

```bash
# Layer 1: Raw data
python3 FORGE/tools/market-data/fetch.py price KRE APO WAL OZK   # live prices
python3 FORGE/tools/market-data/fetch.py fred ICSA                # FRED series
python3 FORGE/tools/market-data/fetch.py all                      # everything

# Layer 3: Stress dashboard (uses config.py thresholds)
python3 FORGE/tools/market-data/dashboard.py                      # full dashboard
python3 FORGE/tools/market-data/dashboard.py --tier 1             # decision drivers only
python3 FORGE/tools/market-data/dashboard.py --agent LABOR        # single agent
python3 FORGE/tools/market-data/dashboard.py --quiet              # red breaches only
python3 FORGE/tools/market-data/dashboard.py --compact            # one-line (Telegram)
python3 FORGE/tools/market-data/dashboard.py --json               # structured output
```

**Thresholds:** `FORGE/tools/market-data/config.py` — single source of truth for CLI + web dashboard.
**Tier 1 (decision drivers):** HY OAS, CCC OAS, Brent, Gas, USD/JPY, Claims, Cont Claims, SOFR, 10Y
**Tier 2 (positions):** KRE, APO, ARES, OZK, WAL, FXY, TLT, VIX

**Cron:** Runs every 5min (self-throttled: 15min market hours, 60min off-hours, 4hr weekends). Telegram alerts on zone transitions. Morning briefing at 6 AM ET.
**Web:** Dashboard at :8080, stress panel at `/api/stress`.

Full docs: `FORGE/tools/market-data/README.md`
