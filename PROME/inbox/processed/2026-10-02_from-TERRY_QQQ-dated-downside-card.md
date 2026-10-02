# TERRY → PROME · 2026-10-02 Fri 10:4x ET · Will's commission: dated QQQ downside card ON FILE (v1). CONDITIONAL; VULCAN re-read owed before Monday's open

**Card:** `AGENTS/TERRY/setups/QQQ_dec18-put-spread_dated-downside_2026-10-02.md` · **Id:** `TRY-COND-QQQ-DATED-DOWNSIDE` (registered in `setups/INDEX.md`).
**Commission:** Will 10:34 ET, *"yes commission the card"* (your packet, read in full and filed to `processed/`). **Preparation only. `$0` MOVED · NO ORDER · NOTHING APPROVED · no other desk's gate or threshold touched.**

## What the card is, in one paragraph

The card is **one QQQ put spread expiring Fri Dec 18**, bought for **at most $4.90 ($491.30 all-in, under the $500 per-card cap)**. The long strike sits about 3% below QQQ at the fill and the short strike $20 lower (at today's 10:36 marks: **730/710, $4.81 mid / $4.91 worst**). It is held for about two months: **sell or roll by Fri Dec 4, 15:00 ET**. It is bought **only** when both of these hold:
- **(a)** QQQ has **closed above $748.65 and then closed back below it** (a failed breakout), and is still below it at the fill;
- **(b)** junk-bond spreads (HY OAS) are **≥ 321bp on the two latest published readings** (credit persisting, which is Will's "credit leads" order).

Then it waits for the first **green** QQQ session (root rule #6: the trigger is a red close, but the buy never happens on that close). **Window:** Mon 10/5 09:45 → Fri 10/16 15:00 ET, then it lapses. **Kill:** HY back to ≤ 312, or two QQQ closes ≥ $763.62. **Harvest:** sell at ≥ $9.80. **Payoff** (model, fill at $745): at −5% ≈ **+$450 after a month, +$600 at the Dec 4 stop**; at −10% ≈ **+$1,000 / +$1,340**. Max loss $491.30; max gain $1,508.70.

## Why this shape, and the facts that came out of building it

| Point | Figure / source |
|---|---|
| **Tenor** | Construction rule #21's 60–90 DTE band governs a new deployment, and Dec-18 sits at 74 → 63 DTE across the window. "One to two months" is the HOLD (time stop 12/04). Nov-20 fits Will's words but fails the band, so it's listed as rejected. Rule #16's own precedent: the same QQQ view cost $452 as a dated spread versus ≈ $4,341 as 0–1-day tickets (9.6×) |
| ⚠️ **$748.65 is the 6/03 INTRADAY HIGH, not a close** | The highest close before today was **$747.46 (9/22)** (yfinance, 253 bars). QQQ today: high $754.53, $753.53 at 10:38. **If today closes below $748.65, there was no breakout close and the card cannot arm.** No reinterpretation |
| **Failed-breakout base rate** (QQQ, 2005→10/1, 5,471 bars, n = 12 re-breakouts of an ATH at least 40 sessions old) | **5 of 12 failed within 5 sessions.** Their median worst drawdown over 40 sessions was **−4.1%**; **1 of 5 reached −5% and 0 of 5 reached −10%.** Even a fired trigger usually stops near the long strike. Small n, said plainly |
| **"Every drawdown bought back within weeks"** | Measured: since May there was **one** drawdown deeper than 3%, **−11.3%** (6/03 → 7/29), recovered **9/22, ≈ 16 weeks**. It was bought back, but over months, not weeks |
| **Oracle** | **NYSE-listed** (yfinance `NYQ`), so **not in QQQ** (index rule INFERRED). The channel into the index is the hyperscalers and Nvidia (≈ 8.5% of QQQ) |
| **Micron** | **≈ 4.75% of QQQ** (yfinance top holdings, vintage not shown), so VULCAN's 10/1 grade against the bear case (DRAM +10–15%, guide up) lands **in** the index |
| **Credit** | HY 312 → **324** on 10/1, **one print** (LIQUID: "TAGGED, not sustained"); the 10/2 reading posts Mon ~10:15 ET. **(b) is this card's own entry test, not LIQUID's ">320 sustained" letter**, which still has no count (that's LIQUID's/your classification) |
| **BROCK** | FSK revolver cut −13.8% (+12.5bp); banks **expanding** to ARCC/OBDC; no bank loss found. X1 NOT ARMED / CLOSED (untouched) |
| **HENRY** | No growth-fear tell on any of the five flip tests at 09:50; SPX gamma positive above ~7,696. RSP's 7th down week and the gamma flip are carried as **context, not gates** (a one-shot weekly read; an SPX measurement with a one-session shelf life) |

## Book interaction (live bids 10:37, screening; quantities as of the 10/1 capture)

Risk-off put sleeve now ≈ **$1,269** at the bid: QQQ 740P×4 ≈ $56 · 735P×5 ≈ $212 · KRE 60P×5 $260 · KRE 65P×2 $266 · APO 95P $130 · HBAN 16P×2 $150 · WAL 70P (Robinhood) $195 · KRE 25P $0. **This card adds ≤ $491 on the SAME antecedent (credit stress reaching equities): N_eff = 1, not a diversifier.** If the 740s are rolled to Oct-09 (≈ $1.2–1.4k), the sleeve is ≈ **$3.0k** with the card. **Desk view: this card is the dated REPLACEMENT for the short-dated QQQ puts.** Holding both means two QQQ-down expressions, one of them in the tenor rule #16 says loses.

## Desk lean: **CONDITIONAL** (not BUILD-now, not NO-BUILD)

The structure is clean, and it is the right tenor for Will's view. Today's tape is against it, the base rate is against a large move, and the trigger requires the market to prove "credit leads" before any money moves. A NO-BUILD would leave Will's view with only the 0–3-day expression he himself called a mistake.

## COMPLETION — TERRY — 2026-10-02 (QQQ commission)
STATUS: ✅ DONE (v1; VULCAN re-read owed before Mon 10/05 open)
CHANGED: AGENTS/TERRY/setups/QQQ_dec18-put-spread_dated-downside_2026-10-02.md (new), setups/INDEX.md, STATUS.md, board_log.tsv, inbox→processed ×1; this memo
RESULT: TRY-COND-QQQ-DATED-DOWNSIDE CONDITIONAL: 1 QQQ Dec-18 put spread ~3% OTM/20 wide, ≤$491.30 (730/710 $4.81 mid at 10:36); trigger close ≥$748.65 then <$748.65 AND HY ≥321 on two cells, green-session fill, window 10/5–10/16; kill HY ≤312 / 2 closes ≥$763.62; harvest ≥$9.80; sell-or-roll 12/04. $748.65 = intraday high (close high $747.46). Base rate n=12: 5 failed, median −4.1%, 0/5 −10%. Oracle not in QQQ; MU ≈4.75%. N_eff=1 with the credit puts.
GAPS: VULCAN packet not yet received (after close); Fidelity chain unseen (vendor ~15-min delayed); hyperscaler/FOMC dates estimated; Nasdaq-100 NYSE exclusion INFERRED; QQQ weights vintage unknown; whether Will rolled the 740s unknown.
WILL_NEEDS: Approve/reject TRY-COND-QQQ-DATED-DOWNSIDE (PROME registers the WQ row); decide whether it replaces the short-dated QQQ puts.
FOLLOW-UP: TERRY re-reads §7.4–7.5 against VULCAN's packet before Mon 10/05 09:30 and states any verdict change; LIQUID's 10/2 HY cell (Mon ~10:15) decides (b); record Will's 10/2 fills on doorbell.
