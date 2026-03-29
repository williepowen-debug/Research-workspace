`pdfminer.six` installed: `from pdfminer.high_level import extract_text`

## Market Data Tool
**Location:** `FORGE/tools/market-data/fetch.py`
**Status:** 🚧 Building — Layer 1 in progress

Pull live prices and economic data. Use this BEFORE citing any price or economic figure — never rely on stale STATUS file numbers.

```bash
python3 FORGE/tools/market-data/fetch.py price KRE APO WAL OZK   # live prices
python3 FORGE/tools/market-data/fetch.py fred ICSA                # FRED series
python3 FORGE/tools/market-data/fetch.py all                      # everything
```

**Tier 1 (decision drivers):** HY OAS, Brent, Gas, USD/JPY, Claims
**Tier 2 (positions):** KRE, APO, ARES, OZK, WAL, FXY, TLT, VIX

Full docs: `FORGE/tools/market-data/README.md`
