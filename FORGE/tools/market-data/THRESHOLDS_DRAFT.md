# THRESHOLDS — Layer 2 Config

**Status:** ✅ APPROVED by Will (Mar 28)
**Lens:** Market stress (🔴 = conditions worsening, regardless of position P&L)

Sources: Agent STATUS files (REGINALD, LIQUID, HENRY, LABOR, BROCK, SAM, CARL)

---

## TIER 1 — Decision Drivers

| Series | Source | Agent | 🟢 Green | 🟡 Yellow | 🔴 Red | Direction | Current | Notes |
|--------|--------|-------|----------|-----------|--------|-----------|---------|-------|
| HY OAS | FRED BAMLH0A0HYM2 | REGINALD/LIQUID | <300 | 300-320 | >320 | higher=worse | 321 🔴 | 350=issuance freeze |
| CCC OAS | FRED BAMLH0A3HYM2 | LIQUID | <900 | 900-1000 | >1000 | higher=worse | 977 🟡 | Forced selling regime |
| Brent | yfinance BZ=F | HENRY | <85 | 85-100 | >100 | higher=worse | $112.57 🔴 | Hormuz closed |
| Gas (wkly) | FRED GASREGW | HENRY/CARL | <3.50 | 3.50-4.00 | >4.00 | higher=worse | $3.96 🟡 | $4=behavioral breakpoint |
| USD/JPY | yfinance JPY=X | SAM | <150 | 150-157 | >157 | higher=worse | 159.70 🔴 | 160=MOF intervention |
| Initial Claims | FRED ICSA | LABOR | <225K | 225-280K | >280K | higher=worse | 210K 🟢 | Shadow adj: +55K → est ~265K |
| Continuing Claims | FRED CCSA | LABOR | <1.85M | 1.85-1.95M | >1.95M | higher=worse | 1.819M 🟢 | 2-yr low |
| SOFR | FRED SOFR | LIQUID | <3.60 | 3.60-3.70 | >3.70 | higher=worse | 3.64 🟡 | Quarter-end sensitive |
| 10Y Yield | FRED DGS10 | LIQUID | <4.00 | 4.00-4.50 | >4.50 | higher=worse | 4.42 🟡 | 5.0%=danger level |

## TIER 2 — Position Monitoring

| Ticker | Source | Agent | 🟢 Green | 🟡 Yellow | 🔴 Red | Direction | Current | Notes |
|--------|--------|-------|----------|-----------|--------|-----------|---------|-------|
| KRE | yfinance | LIQUID | >68 | 63-68 | <63 | lower=worse | $63.37 🟡 | $60=major support |
| APO | yfinance | BROCK | >130 | 110-130 | <110 | lower=worse | $108.42 🔴 | Short thesis — 🔴=stress working |
| ARES | yfinance | BROCK | >140 | 110-140 | <110 | lower=worse | $106.28 🔴 | Short thesis — 🔴=stress working |
| OZK | yfinance | REGINALD | >50 | 40-50 | <40 | lower=worse | $44.52 🟡 | Short thesis |
| WAL | yfinance | REGINALD | >78 | 65-78 | <65 | lower=worse | $67.80 🟡 | Fast-transmission |
| FXY | yfinance | SAM | >62 | 57-62 | <57 | lower=worse | $57.36 🟡 | Entry card at $57.36 |
| TLT | yfinance | LIQUID | >95 | 85-95 | <85 | lower=worse | $85.64 🟡 | 30Y approaching 5% |
| VIX | yfinance ^VIX | REGINALD | <20 | 20-30 | >30 | higher=worse | 31.05 🔴 | >30=regime change |

---

## Design Decisions (Will, Mar 28)

1. **Market stress lens.** All colors reflect market conditions deteriorating. Red = bad out there. Our short positions being in 🔴 means stress is hitting those names — which is what we want, but the dashboard reads as "the world is breaking."

2. **Claims shadow adjustment.** Show raw FRED number. Display shadow adjustment alongside as context (e.g. "210K raw | ~265K est w/ shadow adj"). Don't bake adjustment into the threshold comparison.

3. **VIX = market stress.** >30 is 🔴 because it means fear. Good for our book, bad for markets.

4. **Added CCC OAS, SOFR, 10Y.** All from LIQUID's existing threshold framework.
