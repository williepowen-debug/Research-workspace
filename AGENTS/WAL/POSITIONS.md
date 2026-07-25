# WAL — Positions (canonical for WAL strikes/expiries/quantities)

**Updated:** 2026-07-25 (SPLIT from `../REGINALD/POSITIONS.md` at promotion — WP-W4, OZK pattern. Structural data current to the **7/20 FORGE broker export** via REGINALD's 7/20 fold; independently corroborated vs TERRY's 7/17 snapshot at strike/expiry/qty level.)

> ⚠️ **Broker-truth caveat (rule #4):** strikes/expiries/quantities are structural and hold until a trade fires; **marks/P&L go stale immediately — never cite from here.** Cost-basis/P&L: confirm with Will, not from this file (`[[feedback_position_cost_basis_not_authoritative]]`).
>
> ⚠️ **THIS FILE IS CANONICAL for WAL strikes/expiries.** STATUS/INDEX/THESIS must POINT here, never re-list — re-listing caused the 6/19 desync and the phantom "Sep $77.5P" (see REGINALD LESSONS; the phantom class is why `MARKET/TRADE_LOG.md` is bannered).

## WAL Puts (LIVE) — as of the 7/20 FORGE broker export

| Strike | Expiry | Qty | Notes |
|---|---|---|---|
| $77.5P | Aug-21-2026 | 1 | **NEW (FORGE 7/20 export)** — Robinhood, Will direct entry ~7/17-20. Nearest-money leg (~5.8% OTM at $82.30 entry-window tape); post-print expiry — survived the 7/21 AMC print |
| $67.5P | Sep-18-2026 | 1 | Core REINFORCED-HOLD — caught the 7/21 Q2 print; v2.3 note: EV $73.92 now sits further above this strike than pre-print |
| $70P | Sep-18-2026 | 1 | Core REINFORCED-HOLD — same |

## History (carried from the REGINALD ledger at split)

- **Jul-17-2026 $65P** — LAPSED OTM at $81.88 (broker-confirm was owed; confirmed expired-off per the 7/20 export).
- **Jun-18-2026 cluster** ($65P/$67.5P/$77.5P/$85P) — CLEARED per Will 6/19 ($85P closed ~$5.09 ITM, rest OTM).
- **May-15-2026 $75P** — expired/sold per Will confirm 5/21.
- Phantom "Sep $77.5P" — never existed (mis-recorded Jun-18 leg); purged fleet-wide 7/17 audit.

*Position management = TERRY lane (rules #4/#5/#6/#7 — TERRY + Will [Approve] + live chain before any action). Sep-18 core expiry is on STATUS §EXPECTED SIGNALS. Non-WAL bank/credit legs (KRE/HBAN/APO) remain REGINALD's at `../REGINALD/POSITIONS.md`.*
