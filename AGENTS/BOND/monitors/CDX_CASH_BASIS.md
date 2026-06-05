# BOND Monitor — CDX/Cash Credit Basis

**Owner:** BOND
**Last Updated:** 2026-06-05 by BOND
**Purpose:** Detect when faster synthetic/hedging credit demand leads cash spread repricing.

## Working Model

- Synthetic/fast layer widening ahead of cash = hedging demand / fast-money stress before bonds trade.
- Cash OAS widening without the fast layer = slower fundamental repricing.
- Divergence sustained for 2+ weeks matters more than one-day noise.

## Data Reality (read before citing)

True **CDX.HY / CDX.IG index levels are owned by S&P Global / Markit and are NOT free.** For weeks this vector sat as "🟡 data gap" — effectively dark. As of 6/5 it is monitored via a **free proxy**, with explicit limits:

- **Proxy (BOND, free):** `monitors/cdx_proxy.py` — the **HYG/IEF ratio** (HY credit ETF stripped of duration via the 7-10Y UST ETF) isolates the credit component of HYG. LQD/IEF gives the IG cross-check. Run it any session; cross-check vs cash HY OAS (FRED `BAMLH0A0HYM2`).
- **What the proxy CAN see:** faster-cash (liquid ETF/hedging layer) vs slower-cash (computed OAS) lead/lag.
- **What it CANNOT see:** HYG is *cash*, not *synthetic*. The genuinely synthetic, fast-money signal is **HYG option put-skew / implied vol** — that lives in **VIOLET's** domain (options/vol). For the true synthetic read, request HYG skew from VIOLET. True CDX needs the **S&P Global MCP connector (auth required)** or a paid Markit feed.

## Current Read (6/5)

**🟢 Proxy live — NO divergence. Cash calm is corroborated, not fake.** HYG/IEF = 0.8484, **91st percentile** of its 3-month range (0.8219-0.8507) — credit-excess is *rich*, not stressed. 20d z-score +0.36, well off the 5/20 peak of +1.86 (which was just IEF/duration weakness during the long-end episode, since normalized). LQD/IEF (IG) similarly rich. Both confirm HY OAS 274 / IG OAS 74: the long-end duration move never transmitted to credit, and the fast/hedging layer shows no hidden stress underneath the calm.

## Rolling Table

| Date | HY OAS | HYG/IEF (z20) | LQD/IEF | Read | Source |
|---|---:|---:|---:|---|---|
| 2026-03-21/26 | ~319bps | n/a (not wired) | n/a | 🟠/🔴 then — CDX widening per notes | Sentiment Trader/RIA via LIQUID/BOND seed |
| 2026-05-08/11 | 281bps | n/a (data gap) | n/a | 🟡 gap — could not adjudicate | FRED + missing CDX source |
| 2026-05-20 | 286bps | 0.8504 (+1.86) | — | proxy z-spike = IEF/duration weakness, NOT credit | yfinance + FRED |
| 2026-06-05 | 274bps | 0.8484 (+0.36) | 1.1554 | 🟢 no divergence — credit-excess rich | yfinance + FRED |

## Triggers

| Trigger | Action |
|---|---|
| HYG/IEF breaks to bottom of range (z20 < -1.5) while HY OAS stays tight for 2+ weeks | 🟠 signal HENRY/LIQUID — fast layer leading cash |
| HYG/IEF and HY OAS both deteriorate >75bps-equiv from trough | 🔴 credit-equity lead active |
| HYG/IEF normalizes while cash stays tight | downgrade prior divergence as resolved (current state) |
| VIOLET reports HYG put-skew steepening while cash OAS flat | 🟠 true synthetic-leading-cash — escalate (BOND proxy blind to this) |

## Automation Status

- ✅ Free proxy wired (`cdx_proxy.py`) — repeatable, no auth needed.
- ⬜ Synthetic/options leg: request HYG put-skew from VIOLET (BOND-blind).
- ⬜ True CDX: S&P Global MCP connector (auth) — evaluate when connectors are live headless.
