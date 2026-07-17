# CHART + OPTIONS WORKFLOW
**Purpose:** make Terry's chart/structure work repeatable instead of vibes-based.

## 1. Price / chart workflow

Before citing levels:

1. Prefer Terry's snapshot wrapper for trade-card work:
   ```bash
   python3 AGENTS/TERRY/scripts/snapshot.py TICKER [TICKER...] --benchmark BENCHMARK --days 30 --stress
   ```
2. Pull live/latest price directly through FORGE market-data when needed:
   ```bash
   python3 FORGE/tools/market-data/fetch.py price TICKER
   ```
3. If broader stress context matters, run compact dashboard:
   ```bash
   python3 FORGE/tools/market-data/dashboard.py --compact
   ```
4. Check at least two horizons:
   - **Daily:** tactical entry, support/resistance, momentum, gaps.
   - **Weekly:** regime/trend and where the trade is fighting the tape.
5. Compare relative strength to the right benchmark:
   - banks → KRE / XLF
   - credit → HYG / JNK / BIZD
   - energy → XLE / Brent proxy
   - duration → TLT / 10Y
   - broad market → SPY / QQQ
5. Record levels in the trade card with as-of timestamp.

## 2. Chart checklist

| Check | Why it matters |
|---|---|
| Trend | Do not buy puts into vertical support or calls into exhaustion without a trigger. |
| Support/resistance | Defines entry quality and invalidation distance. |
| Volatility regime | Determines shares vs options/spreads and expected move. |
| Liquidity/volume | Wide spreads and thin options can make a correct thesis untradeable. |
| Relative strength | Weak thesis expression may be crowded or already priced. |
| Catalyst timing | Entry must match event clock and confirmation lag. |

## 3. Option-chain fields Terry needs

If live chain data is unavailable, ask Will/broker for these before making a firm options recommendation:

| Field | Required? | Use |
|---|---|---|
| Bid/ask by leg | Required | Slippage / executable debit-credit |
| Open interest / volume | Required | Liquidity and exit risk |
| Implied volatility / IV rank if available | Required if obtainable | Outright vs spread decision |
| Delta | Required | Exposure sizing and strike choice |
| Theta/day | Required | Time-decay budget |
| Expected move through catalyst | Preferred | Strike/target sanity check |
| Skew | Preferred | Put/call spread attractiveness |

### 3b. Settlement / assignment taxonomy (external research — `options/RESEARCH.md` TT-05/TT-09)
Matters most **near expiry**, where TERRY already operates (e.g. the 7/16 USO 1-DTE triage):
- **Cash-settled index options** (SPX, XSP, NDX, RUT): **no assignment risk**, no early exercise; **larger** contract size.
- **ETF options** (SPY, QQQ, IWM): deepest liquidity, easiest sizing — **but carry assignment risk.**
- **Futures options** (ES/MES, NQ/MNQ): ~24h, SPAN margin; **settle to the futures contract**, not to cash.
- **⚠️ Broker-specific and NOT assumable:** assignment handling, product fees, and **auto-liquidation if you can't settle** (can close a position at a bad price/time). **Ask Will/broker — do not infer.**

## 4. Structure selection heuristics

- **Shares/ETF:** use when timing is uncertain but thesis is durable and loss can be stopped mechanically.
- **Outright options:** use only when move timing is tight and convexity justifies theta/IV.
- **Vertical spreads:** default when direction is clear but IV/theta is expensive or target is bounded.
- **Calendars/diagonals:** use only when timing/vol view is explicit; otherwise they hide complexity.
- **No trade:** use when invalidation is too far, catalyst is too vague, liquidity is bad, or option pricing eats the edge.

## 5. Minimum output for chart-only requests

Even if Will asks only for chart analysis, Terry should end with:
- `Tradeable now? yes/no/conditional`
- `Best entry trigger`
- `Invalidation level`
- `Do-not-chase level`
- `What would change the answer`
