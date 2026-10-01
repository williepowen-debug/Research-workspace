---
signal_id: SIG-W-20261001-009
date: 2026-10-01
timestamp: 2026-10-01T16:31:23Z
time_dispatched: 2026-10-01T16:31:23Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: Will (Telegram) — Will-Telegram 7-image batch 2026-10-01 ~16:28Z (msgs 4796-4802), batch manifest BM-20261001-01
origin: ["Will Telegram photo (msg 4797): X @zerohedge 10/01 10:22 ET, quoting its own post 39 min earlier; Bloomberg-screen chart FRANCE CDS USD SR 5Y D14 last 75.340", "ANSA 10/01: BTP-Bund spread surges past 118bp; ANSA 9/30: closes at 102.9 (Google News headlines, 10/01 WALTER pull)", "HANS STATUS 10/01: OAT-Bund 130.3bp i-i (17:35 CEST), Bund ~flat, read France-idiosyncratic; BTP-Bund 91.9 [9/18, TE-derived, not re-pulled]"]
domain: EUROPE_MACRO
cluster: FED_FRAMEWORK
entities: ["BTP-Bund spread", "OAT-Bund spread", "France 5Y CDS", "HANS-T-09", "HANS-T-10"]
confidence: 0.7
confidence_language: "Italy move: ZeroHedge squawk + ANSA headlines, consistent direction (102.9 close 9/30 -> 113-118 intraday 10/01); vendor bases differ, so no single level. France CDS 75: one chart (Bloomberg screen via ZeroHedge); the '13-year wide' label is ZeroHedge's."
signal_type: divergence
safety_net: clear
verdict: "Italy's 10Y spread to Bunds widened ~10bp to ~113bp on 10/01 (ZeroHedge; ANSA intraday 'past 118', from a 102.9 close 9/30), alongside France +8bp to 135bp, and France 5Y CDS printed ~75, labelled a 13-year wide. HANS's 10/01 grade read the OAT move as France-idiosyncratic (Bund flat); a same-day ~10bp BTP move is evidence it is spreading to the periphery. Neither Italy line is near HANS-T-09 (spread >200 AND BTP >5.50). T-10 (France) is already firing."
precedence: PRIORITY
action: ["HANS"]
info: ["BOND", "LIQUID", "REGINALD", "CARL", "RED"]
dispatch_note: "Source: Will-Telegram 7-image batch 2026-10-01 ~16:28Z (msgs 4796-4802), batch manifest BM-20261001-01, item 2 of 7 (image 2). 'Already ours?' HANS's 10/01 STATUS has France at 130.3 i-i and its Italy row is 9/18-stale, so the Italy leg and the CDS print are new to the owner. Domain EUROPE_MACRO -> HANS action (re-test the 'idiosyncratic' read), BOND backup for time-critical per the row's Limit 1. Info BOND, LIQUID, REGINALD, CARL per row; RED info (signal_type divergence vs the owner's read). HANS liveness: its session messaged WALTER at ~16:2xZ (socket), so it is doorbelled directly."
---

# Italy's bond spread jumped ~10bp alongside France's today. France's 5-year credit default swaps (CDS) are at a 13-year wide. The French sell-off no longer looks France-only.

| Line, 10/01 | Level | Change | Basis |
|---|---|---|---|
| Italy–Germany 10Y spread | **~113bp** (ANSA intraday: "past 118") | **+10bp** · ANSA close 9/30: 102.9 | ZeroHedge 10:22 ET; ANSA headlines |
| France–Germany 10Y spread | ~135bp (ZeroHedge) · **130.3bp** (HANS, i-i, 17:35 CEST, the governing basis) | +8 to +13bp | HANS grades on i-i only |
| France 5Y CDS (USD, senior) | **~75** | "13-year wide" (ZeroHedge's label) | One Bloomberg-screen chart |

**So what:** HANS's own 10/01 grade called the French move **France-specific** (the Bund held flat, and the trigger was the 2027 budget's €54bn package). **Italy moving ~10bp the same day is the first sign it is spreading**, the channel that turns a French budget problem into a euro-periphery one. France's own fire line (`HANS-T-10`) is already open. **Italy is nowhere near its line:** `HANS-T-09` needs a spread >200bp **and** a BTP yield >5.50%, and neither fires alone.

## Caveats
- **Vendor bases differ by up to ~12bp** on these spreads (HANS's own note). The table gives directions and bases, not one level.
- The CDS figure comes from **one chart image**; "13-year wide" is ZeroHedge's description, not checked against a CDS history.
- **One day is not a contagion regime.** A same-direction close on 10/02 is the confirmation test.

Action HANS: re-test the "France-idiosyncratic" read against the Italy leg. Canon: HANS. Time-critical backup: BOND.
