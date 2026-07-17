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

### 3c. Deliberate-tail construction note — TT-02 (external research, `options/RESEARCH.md`; SCOPED, not a numbered rule)
**Fires ONLY on cards explicitly tagged "deliberate tail"** (crash-ladder, deep-OTM lottery tickets). **Does NOT apply to directional puts** — see the trap below.
- **Terminal-window convexity is the payoff.** For a *deliberate tail*, the payoff lives in the final ~2 weeks (tastytrade's own 15yr data: seller CVaR explodes there = the buyer's convexity). **Do not roll or close out of that window early** — you'd exit right before the thing you paid for. This is the one place root **rule #7** ("roll duration") tensions; on a true tail, rolling *out* of the terminal window rolls out of the convexity. Flag the tension on the card; do not auto-apply #7.
- **⚠️ The trap:** a *directional* put (needs an ordinary move, e.g. Will's TLT 85P/82P grind) is the opposite — accelerating terminal bleed is a **cost**, not a product. Never let crash-ladder hold-to-expiry logic bleed onto a directional card.
- **Pricing context — the "double tax" (memory `vrp_split_rates_vs_singlename`):** a **TLT/rates crash-ladder pays the vol tax twice** (rates VRP persisted past 2012 + deep-OTM skew), so it is NOT a cheap way to be short bonds — pay it only for the convexity above. A **single-name tail (HBAN) is structurally cheap** except into its own earnings print. Status: unverified secondary (seller-side); promote to a numbered rule only after a deliberate-tail card fires live OR magnitudes are independently verified.

### 3d. Grind-vs-crash tenor/strike discipline (Part B diagnostic, `options/TENOR_DISCIPLINE_PARTB_2026-07-17.md`)
**Before buying a put to express a domain thesis, name which trade it is — they want opposite structures:**
- **SLOW GRIND thesis** (credit transmission re-rates a name 10–20% over 2–4 quarters): **strike ~5–10% OTM, tenor 6–12mo.** A shallower strike carries real delta and is far more reachable on the grind path (WAL 75P/9.5% OTM: 3y realized-reach ~20% vs the 67.5P/18.5% OTM: ~7%). **Fewer, better-positioned puts beat many deep near-dated tickets** — the cheap-looking deep-OTM strike has the *worst* reachability on a grind and just bleeds the tail premium to $0.
- **CRASH tail** (systemic break): deep-OTM (13–20%+) is the *right* tool — but size it as a lottery and apply §3c (TT-02, hold to terminal window). The TLT crash-ladder's deep strikes are correct *because* it's a deliberate tail.
- **⚠️ The failure mode this kills:** expressing a *grind* thesis with *crash* instruments (deep-OTM + near-dated). Pays the deep-OTM tax AND gets near-zero probability on the thesis's actual trajectory. This is rule #7 ("roll duration") + "no expiry drift" in practice: a slow thesis whose puts keep dying wants **longer tenor + shallower strike**, not more deep lottery tickets.
- **Reachability check (cheap, do it):** at entry, compare the strike's %OTM to the name's realized N-day move distribution (`scripts` / yfinance). If the empirical frequency of reaching the strike in the tenor is low single digits, it's a tail bet — construct and size it as one, don't call it a directional expression.

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
