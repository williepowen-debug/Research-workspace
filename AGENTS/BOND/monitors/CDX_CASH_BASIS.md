# BOND Monitor — CDX/Cash Credit Basis

**Owner:** BOND
**Last Updated:** 2026-05-11 by PROME
**Purpose:** Detect when synthetic credit protection demand leads cash spread repricing.

## Working Model

- CDX widening ahead of cash = hedging demand / fast-money stress before bonds trade.
- Cash OAS widening without CDX = slower fundamental repricing.
- Divergence sustained for 2+ weeks matters more than one-day noise.

## Current Read

**🟡 Data gap.** March thesis depended partly on CDX widening while cash HY OAS stayed near 319bps. As of May 11, HY cash OAS is **281bps**, but direct CDX.HY / CDX.IG levels are not wired into the local market-data tool. Treat CDX-cash divergence as **unconfirmed** until refreshed from a reliable source.

## Rolling Table

| Date | HY OAS | CDX.HY 5Y | Basis / divergence | IG OAS | CDX.IG | Read | Source |
|---|---:|---:|---:|---:|---:|---|---|
| 2026-03-21/26 | ~319bps | 9-month high per notes | Synthetic stress > cash | ~87bps | TBD | 🟠/🔴 then | Sentiment Trader/RIA note via LIQUID/BOND seed |
| 2026-05-08/11 | 281bps | TBD | Cannot confirm | 79bps | TBD | 🟡 gap | FRED + missing CDX source |

## Triggers

| Trigger | Action |
|---|---|
| CDX widens while HY OAS stays tight for 2+ weeks | 🟠 signal HENRY/LIQUID — synthetic leading cash |
| CDX and cash widen together >75bps from trough | 🔴 credit-equity lead active |
| CDX normalizes while cash remains tight | downgrade March divergence as resolved / false alarm |

## Automation Need

Find reliable CDX.HY/CDX.IG source or wire a manual weekly check. Without this, BOND cannot cleanly adjudicate “cash calm is fake” vs “March hedge stress resolved.”
