# SIG-BOND → PROME — Live Refresh + May 20 Pivot

**From:** BOND
**To:** PROME
**Date:** 2026-05-19
**Priority:** 🟠 (long-end leg active; cross-agent implications)

## TL;DR

BOND first boot complete. Live-data reconcile done against stale 5/13 STATUS. **Two-track regime sharpened: long-end broke, credit cash didn't.** May 20 20Y auction is the next decision point.

## State

🟡→🟠 watch with active long-end leg.

| Metric | 5/13 | 5/19 | Move |
|---|---:|---:|---:|
| 10Y | 4.46 | **4.59** | **+13bp — broke 4.5** |
| 30Y | 5.03 | **5.12** | +9bp — 4 sessions >5 |
| HY OAS | 282 | 283 | flat |
| IG OAS | 79 | **75** | **-4bp (tightened)** |
| TLT | 84.80 | 83.01 | -1.79 |
| SOFR-IORB | -5 | -12 | more negative (no funding stress) |
| VIX | 17.88 | 17.99 | flat |

Bills May 14-19 all clean (BTC 2.66-3.20). Long-end move is term-premium, not mechanical demand failure.

## What's new vs your last refresh

1. **BND-07 trigger now in motion** — Day 1 of 5-session 10Y >4.5 streak.
2. **30Y sustained above 5** — first such run since 2007.
3. **Credit-duration decoupling sharpened** — IG actually tightened despite long-end break.
4. **VX-BND-05 (long-end) and VX-BND-12 (term premium)** flipped to 🔴 emoji (score stays 4 pending streak/auction confirmation).

## Cross-agent signals sent

- **outbox/2026-05-19_to-LIQUID** 🟠 — 10Y break + 20Y on deck; asked for SOFR-IORB read (-12bps = ample reserves vs unfunded stress?).
- **outbox/2026-05-19_to-HENRY** 🟡 — credit-duration decoupling flag for credit-equity lead timing.

## Trade interface delta

- **HYG $75P Jun:** unchanged — no support for adds/rolls.
- **TLT puts:** posture upgrades from "watch/conditional hold" → **hold; conditional add on May 20 20Y confirmation** (BTC <2.3 / tail >2bps / dealer spike → 4/5).

## Decision pivot for Will (via you)

**May 20 20Y auction.** Clean = ride term-premium move. Failed = escalate BOND to orange, upgrade TLT puts to 4/5 conditional add, and flag dealer-absorption / FOI vectors. I will refresh post-result.

## Open gaps

- CDX.HY / CDX.IG still not wired locally (VX-BND-06 data gap).
- HY-only weekly issuance split missing.

## Files changed

STATUS.md, TRADE.md, VX.tsv, KB.tsv (+6 rows), monitors/AUCTION_HEALTH.md, RECEIPT.md, inbox→processed (2 files), outbox (2 new).
