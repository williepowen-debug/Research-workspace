# WAL — Positions (canonical for WAL strikes/expiries/quantities)

**Updated:** 2026-08-20 (WAL session #3 — **Aug-21 $77.5P row moved LIVE → History: CONFIRMED SOLD 8/18**, Will in-session, artifact-verified at `FORGE/STATUS.md` D-18. Live book is now the two Sep-18 cores only.) Prior: 2026-07-25 (SPLIT from `../REGINALD/POSITIONS.md` at promotion — WP-W4, OZK pattern. Structural data current to the **7/20 FORGE broker export** via REGINALD's 7/20 fold; independently corroborated vs TERRY's 7/17 snapshot at strike/expiry/qty level.)

> ⚠️ **Broker-truth caveat (rule #4):** strikes/expiries/quantities are structural and hold until a trade fires; **marks/P&L go stale immediately — never cite from here.** Cost-basis/P&L: confirm with Will, not from this file (`[[feedback_position_cost_basis_not_authoritative]]`).
>
> ⚠️ **THIS FILE IS CANONICAL for WAL strikes/expiries.** STATUS/INDEX/THESIS must POINT here, never re-list — re-listing caused the 6/19 desync and the phantom "Sep $77.5P" (see REGINALD LESSONS; the phantom class is why `MARKET/TRADE_LOG.md` is bannered).

## WAL Puts (LIVE) — 2 legs, both Sep-18 cores *(Aug-21 $77.5P sold 8/18 → History)*

| Strike | Expiry | Qty | Notes |
|---|---|---|---|
| $67.5P | Sep-18-2026 | 1 | Core REINFORCED-HOLD — caught the 7/21 Q2 print. ⚠️ **v2.4 note (8/20, supersedes the v2.3 note): EV is now $75.96, so this strike sits $8.46 BELOW EV** — on the central estimate it expires worthless, $2.04 worse than at v2.3 |
| $70P | Sep-18-2026 | 1 | Core REINFORCED-HOLD — same. ⚠️ **v2.4: $5.96 BELOW EV $75.96** |

## History (carried from the REGINALD ledger at split)

- **Aug-21-2026 $77.5P ×1 (Robinhood)** — ✅ **CONFIRMED SOLD**, Will in-session **2026-08-18** (operator's own word, relayed via TERRY; artifact of record `FORGE/STATUS.md` **D-18**). Entered ~7/17-20 off the 7/20 FORGE export; absent from the 8/14 Robinhood capture. ⚠️ **The confirm covers the FACT of the sale ONLY — sale date and proceeds are UNRECORDED, so the P&L is UNRECORDED, NOT ZERO. Do not book this leg at $0.** Residual closes on a Robinhood history view (FORGE D-18, Will-side, not urgent). *Encoded here 8/20 on PROME's boot packet — this file carried it as LIVE for 2 days past the confirm, one day before its expiry; that is the phantom-position class this file's own header warns about.*
- **Jul-17-2026 $65P** — LAPSED OTM at $81.88 (broker-confirm was owed; confirmed expired-off per the 7/20 export).
- **Jun-18-2026 cluster** ($65P/$67.5P/$77.5P/$85P) — CLEARED per Will 6/19 ($85P closed ~$5.09 ITM, rest OTM).
- **May-15-2026 $75P** — expired/sold per Will confirm 5/21.
- Phantom "Sep $77.5P" — never existed (mis-recorded Jun-18 leg); purged fleet-wide 7/17 audit.

> ⚠️ **EV-vs-strike read, stated here because this is the canonical strike file (8/20):** both live cores are **below** the v2.4 EV of **$75.96**, i.e. my own central estimate has them expiring worthless. **BUT THE TWO LEGS ARE BOTH TRUE AND NEITHER RESOLVES THE OTHER:** the tape is at its period low with the **$78 threshold only +2.6% away, and that trigger fires on a CLOSE regardless of EV.** A model saying "worthless at expiry" and a threshold saying "about to trip" are answering different questions. **No action here — TERRY + Will [Approve] + live chain (root #4/#5).**

*Position management = TERRY lane (rules #4/#5/#6/#7 — TERRY + Will [Approve] + live chain before any action). Sep-18 core expiry is on STATUS §EXPECTED SIGNALS. Non-WAL bank/credit legs (KRE/HBAN/APO) remain REGINALD's at `../REGINALD/POSITIONS.md`.*
