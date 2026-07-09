# ORACLE — Divergence Read vs Fleet Marks (2026-07-09 ~20:55Z)

**Context:** catch-up session (last own session 7/2; 7-day inbox-empty gap). Comparing live crowd pricing (Polymarket + Kalshi, pulled 2026-07-09T20:51-54Z) against the fleet marks named in PROME's 7/9 current-events digest: HAWK escalation ladder **B12/C42/D46**, BRENT durable-sustain **~0.55** (Brent >$75 through Fri 7/10 ICE LCOU26 settle).

## 1. HAWK ladder D-rung vs "US blockade on Iran" market → **CONVERGES, no material divergence**

| | Value | Source |
|---|---:|---|
| HAWK D-rung (severe escalation) | 46% | PROME 7/9 digest |
| PM "US blockade on Iran by Dec 31" | **48.0%** (Δ7d +17.5) | Polymarket, $210.0K vol / **$64.7K liq**, pulled 2026-07-09T20:54Z |
| Gap | −2pp | |
| KL(0.46 ‖ 0.48) | **≈0.001 bits** | noise-level per `PREDICTION_MARKET_METRICS.md` (<0.03 = noise) |

Real money independently prices the same severe-escalation tail HAWK's ladder assigns — and it's risen +17.5pp over 7 days, tracking the truce collapse in real time. This is a genuine cross-check win (auto-memory `independent_convergence_validates_schema`): the market didn't need HAWK's read to arrive at nearly the same number. **Liquidity is real ($64.7K)** — not a thin-market artifact.

Secondary corroboration: HAWK's C+D (non-trivial-escalation, 42+46=88%) sits close to "Iran targets shipping by Aug 31" **84.5%** ($12.0K liq) — same direction, same order of magnitude.

## 2. BRENT durable-sustain (~0.55) vs market → **not computable — coverage gap, not a dislocation**

No Polymarket/Kalshi market matches BRENT's exact resolution criteria (Brent, not WTI; >$75 threshold; sustained through Friday's ICE settle, not a monthly-high bracket). The nearest analog, **"WTI hits $80 in July" (33.0%, Δ1d −24.5, Δ7d +19.5, $20.8K liq)**, tests a materially harder bar — WTI $80 ≈ Brent ~$84-85 given the typical $4-5 spread, well above BRENT's $75 sustain-line — so a lower probability there is not informative about the $75 question. Per the metrics doc's audit-before-routing rule, this is reported as **a coverage gap** (ORACLE's book has no clean Brent-sustain proxy), not a scored KL. **Flag for future watchlist**: if a Brent-denominated or lower-threshold WTI market opens, it becomes the clean BRENT cross-check.

**Caveat on the WTI $80 print itself:** Δ1d −24.5pp on $20.8K liq (moderate, not deep) is a single-day swing large enough to warrant a re-check before treating either the high or the low print as signal — thin-liquidity discipline applies.

## 3. Live watch item (not a scored divergence): Fed-hike-2026 recrossed >50%

Fed-hike-in-2026 **50.5%** (Δ1d −10.0, Δ7d **+4.0**) — back above 50% for the first time since the 7/2 STATUS called the hawkish overshoot "rolling over." Cross-platform: Polymarket July-hike **14.5%** (Δ7d +4.9), Kalshi July-hike **15%** (Δp −5.0 intraday, so noisy day-to-day, but level is up from 7/2's cross-platform ~9.7%/14%). No-cuts-2026 still pinned **78.5%** (dovish tell <70% still not fired). The digest doesn't cite an explicit fleet-side Fed-hike probability to diff against, so this isn't scored as a divergence — routing to LIQUID/HENRY as a fresh data point (possible energy-shock → inflation-expectations channel post truce-collapse; HENRY/LIQUID's call, not ORACLE's).

## Bottom line

**No material market-vs-fleet divergence found** on the two named comparators. HAWK's ladder gets an unusually clean, real-money confirmation (KL ≈0.001 bits, $64.7K liq). BRENT's sustain thesis simply has no resolution-matched market to check it against — that absence is itself worth noting (a blind spot, not a disagreement). The one thing actually moving against the "calm" priors this week is the Fed-hike tail ticking back up cross-platform — worth LIQUID/HENRY's eyes, not adjudicated here.

*Re-pull: `python3 AGENTS/ORACLE/scripts/polymarket.py pull --log` + `python3 AGENTS/ORACLE/scripts/kalshi.py pull --log`. KB rows: KB-ORC-025/026/027.*
