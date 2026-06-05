---
name: Verify ETF prices against underlying FX
description: Always cross-check ETF price (FXY) against underlying exchange rate (USD/JPY) before building a narrative — catch data errors early
type: feedback
---

Always cross-check ETF prices against the underlying instrument before treating as signal. FXY should closely track inverse USD/JPY — if they diverge significantly ($1 on a $57 ETF = 1.7%), the data is wrong, not the market.

**Why:** On Apr 7 2026, a web search returned FXY at $58.50 (from a secondary aggregator) while USD/JPY was 159.81. Real FXY was $57.44. SAM built a false "yen strengthening into oil" narrative on bad data and had to correct to Will.

**How to apply:** At boot market refresh, verify FXY price is consistent with USD/JPY before updating STATUS or sending analysis. Use Investing.com historical data as primary source, not Nasdaq/Kraken/secondary aggregators.
