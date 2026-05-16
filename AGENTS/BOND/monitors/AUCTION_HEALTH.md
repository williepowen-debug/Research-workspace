# BOND Monitor — Treasury Auction Health

**Owner:** BOND
**Last Updated:** 2026-05-13 by PROME
**Purpose:** Track whether Treasury market absorption is improving, mechanically supported, or deteriorating.

## Classification Rules

| State | Criteria | Signal |
|---|---|---|
| 🟢 Healthy | BTC near/above recent avg, stop-through/small tail, indirect demand stable | No action |
| 🟡 Watch | BTC below recent avg or modest tail; dealer take-down elevated once | Note in STATUS |
| 🟠 Stress building | BTC <2.3 or tail >2bps; weak indirect demand | Signal LIQUID/ZHAO if consequential |
| 🔴 Auction dysfunction | 2+ weak auctions in same tenor sector or large tail + dealer absorption spike | Signal LIQUID, ZHAO, PROME |

## Rolling Table

| Date | Tenor | Size | BTC | High Yield | Indirect % | Direct % | Dealer % | Read | Source | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 2026-04-22 | 20Y reopening | $13B | 2.68 | 4.883% | 59.6 | 20.2 | 8.6 | 🟢/🟡 | FiscalData | Good cover; long-end yield high. |
| 2026-04-23 | 5Y TIPS | $26B | 2.57 | 1.367% | 57.0 | 23.7 | 7.5 | 🟢 | FiscalData | Improved vs March stress. |
| 2026-04-27 | 2Y | $69B | 2.65 | 3.812% | 49.7 | 27.8 | 10.4 | 🟢/🟡 | FiscalData | Adequate. |
| 2026-04-27 | 5Y | $70B | 2.33 | 3.955% | 64.1 | 13.3 | 11.2 | 🟡 | FiscalData | Soft BTC but indirect strong. |
| 2026-04-28 | 7Y | $44B | 2.51 | 4.175% | 51.7 | 26.6 | 10.3 | 🟢/🟡 | FiscalData | No failure. |
| 2026-05-11 | 3Y | $58B | 2.54 | 3.965% | 63.0 | 20.1 | 16.9 | 🟡 | Treasury PDF / InvestingLive | +0.6bp tail; BTC below 6mo avg; dealer take elevated. |
| 2026-05-12 | 10Y | $42B | 2.40 | 4.468% | 64.0 | 24.1 | 12.0 | 🟡 | Treasury PDF / ZH | +0.4bp tail to 4.464 WI; below avg BTC; 4th consecutive 10Y tail per market commentary. |
| 2026-05-13 | 30Y | $25B | 2.30 | 5.046% | 66.6 | 21.7 | 11.7 | 🟡 | Treasury PDF / InvestingLive | +0.5bp tail to 5.041 WI; below avg BTC; demand mix not failed. |

## Open Questions

- Does 10Y >4.5 / 30Y >5 persist for multiple sessions or fade after refunding supply clears?
- Does weak-but-not-failed auction demand begin funding through LIQUID plumbing (SOFR-IORB positive, repo pressure)?
- Does ZHAO see TIC / foreign official demand deterioration that would confirm the auction-level softness?

## May 2026 Refunding Read

All three coupon auctions tailed modestly: 3Y +0.6bp, 10Y +0.4bp, 30Y +0.5bp. Bid/covers were below recent averages, but tails were not large, indirect demand was not collapsing, and dealer take was contained outside the 3Y. Classification: **yellow duration fatigue, not red auction dysfunction**.
