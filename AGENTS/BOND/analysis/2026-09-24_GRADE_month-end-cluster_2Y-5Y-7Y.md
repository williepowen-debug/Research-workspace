# GRADE — September month-end coupon cluster: 2Y 9/22 · 5Y 9/23 · 7Y 9/24

**Graded:** 2026-09-24 13:0x–13:3x ET (BOND `bond-b0`). ⚠️ **The 2Y and 5Y are graded LATE — 2 days and ~24h after the print — because BOND had no session 9/18–9/23. Nobody else on the fleet graded the 5Y (grep of AGENTS/PROME/HEARTBEAT for `91282CRN3` at 13:2x found no grade).**
**Instrument:** `monitors/grade_auction.py --cusip` (venv; `--selftest` 21/21 at 13:0x), print re-verified field-by-field at the TreasuryDirect `TA_WS/securities/search?cusip=` primary. Percentages = % of COMPETITIVE ACCEPTED. **No tail computed** (retired 2026-07-28; wire tails are `[med-conf]` and fire nothing).
**Bars:** frozen 2026-09-17 (STATUS / CATALYSTS): `I'` 54.82 · 60.27 · 57.24; OLD 53.21/24.12 · 59.24/15.61 · 56.42/13.14; cover 2.44 · 2.28 · 2.40.

## Results

| Leg | 2Y `91282CRP8` 9/22 | 5Y `91282CRN3` 9/23 | 7Y `91282CRM5` 9/24 |
|---|---|---|---|
| Size / high yield | $69B / 4.787% | $70B / 5.033% | $44B / 5.085% |
| BTC (cover bar) | 2.63 (2.44) ✅ | **2.21 (2.28) 🔴 −0.07** | 2.42 (2.40) ✅ +0.02 |
| Indirect % (OLD min) | 57.79 (53.21) ✅ | **54.31 (59.24) 🔴 −4.93pp** | 57.20 (56.42) ✅ +0.78 |
| Dealer % (OLD max) | 13.19 (24.12) ✅ | **15.77 (15.61) 🔴 +0.16pp** | 12.53 (13.14) ✅ |
| `I'` P15 bar | 54.82 ✅ +2.97 | **60.27 🟠 FIRED −5.96pp** | **57.24 🟠 FIRED −0.04pp** |
| **Verdict** | 🟢 CLEAN | 🔴 **OLD CONJUNCTIVE COMPOSITION FAILURE + `I'` + cover marker** | 🟠 `I'` MARKER only (by 0.04pp) |

**7Y precision:** ind = 24,869,544,500 / 43,480,804,500 = 57.198%; P15 (linear, n=12, 2025-09-25→2026-08-27) = 56.65 + 0.65×(57.55−56.65) = **57.235** ⇒ strict fire by **0.037pp**. Exact-dollar inputs, so the fire is on the letter. A margin that thin carries no information beyond the marker.

## 5Y — what the letter says, and what it does not

1. **OLD conjunctive test FIRED** (base rate 4/224 = 1.8%/auction, the WQ-157 join). Under `TRADE.md` Reactivation Matrix (WQ-99, Will 9/1) this is the **PRIMARY TLT-put ADD RE-ARM**. ⛔ **Re-arm ≠ add:** Will's 7/16 NO-ADD, root rule #5, and TERRY's construction lane (TLT 25× Sep-30 77P, **expiry 9/30, 6 days**) all govern. BOND proposes no trade.
2. **Paired thesis KILL does NOT fire** (WQ-157 leg ① letter, paired since 9/11): funding leg **SOFR−IORB = 3.87 − 3.90 = −3bp [FRED 9/23]** ⇒ not positive ⇒ not met. FR2004 leg is UNEVALUABLE until the as-of straddling 9/23 publishes (~mid-October). WQ-157 leg ② is still unruled on Will's queue.
3. **Superlatives verified at primary** (5Y nominal, TD `TA_WS`, 2017-01-25→2026-09-23, n=117): indirect 54.31% = **lowest since 2020-03-25** (52.06) ✅ · BTC 2.21 = **lowest since 2018-12-26** (2.09) ✅. ⚠️ **Dealer 15.77% is NOT historically high** — five 5Y prints in 2023-10→2024-05 took more (max 20.37% 2024-01-24). **The dealer leg fired against a trailing-12 max set in a low-dealer year, by 0.16pp.** Dealers did not warehouse on any multi-year standard.
4. **Backdrop (5/21 rule):** 9/23 was a macro sell-off day — hot flash PMIs; vendor `^FVX` 4.834 [9/21] → 4.997 [9/23] (+16bp), `^TNX` +15bp, `^TYX` +10bp, TLT −1.58% (yfinance closes; H.15 9/23 cells unpublished at grading). The 5Y crossed 5% for the first time since 2007 (Bloomberg 9/23, secondary). **A print clearing into a same-day macro repricing is the ordinary way auctions tail. That pushes toward "expensive" and away from "broken", but it does NOT unfire the letter.** Two readings, not adjudicated here: (a) concession into a data shock (mechanism intact; the demand came at a price); (b) a genuine foreign step-back (indirect at a 6.5-year low). **The funding leg (−3bp) and the unexceptional dealer share favour (a); the indirect low is the part (a) does not explain.**
5. **Say it out loud: THRESHOLD FIRED — MECHANISM NOT SHOWN TO HAVE FAILED.** Funding is calm and dealer share is ordinary for the post-2023 regime.

## Counters
- **Downgrade counter stays 0.** 2Y fails the dealer-at/below-median leg (13.19 vs 11.33); the 5Y and 7Y fail indirect-at/above-median. Next eligible: the October 3Y 10/6.
- **`I'` fires this cycle:** 5Y + 7Y (plus the 9/15 20Y-R) = three markers in eight sessions, none pairable yet.

## Instrument defect found while grading (verdict-neutral) — `KB-BND` row
**`grade_auction.py` keys the benchmark tenor on ORIGINAL security term, so the 2026-01-26 2Y-cycle auction (a reopening of the old 5Y `91282CGH8`, maturing 2028-01-31) sits in the 5Y pool and is missing from the 2Y pool.** The effects:
- **5Y window:** 2025-10-27→2026-08-26 (11 true 5Y plus the stray 2Y). The 2025-09-24 5Y was displaced. The stray row supplies the spurious dealer min 7.33 and BTC max 2.75. The correct `I'` P15 = **59.48, not 60.27** (the frozen bar was looser by 0.79pp). **The OLD min/max are identical on the correct set (59.24 / 15.61) ⇒ no verdict changes.**
- **2Y window:** January 2026 is missing and August 2025 is included instead. P15 = 54.82 on both sets; min/max unchanged ⇒ no verdict changes.
- **Class:** every auction that reopens an older, longer original issue. The fix is owed (key on the auction-cycle term, with selftest fixtures); until then, re-check the window listing on any grade near a bar. **The 9/17 re-freeze did not catch this because the freeze reuses the same function.**

## Routing
LIQUID 🔴 (the TRADE.md/CLAUDE.md composition-failure route, unchanged by the 8/27 ruling) · ZHAO 🟠 (foreign-demand leg: indirect at its 6.5-year low) · PROME (the ADD re-arm is Will-gated; the kill did not fire) · TERRY (the construction lane on a 6-DTE position). Packets filed 2026-09-24.
