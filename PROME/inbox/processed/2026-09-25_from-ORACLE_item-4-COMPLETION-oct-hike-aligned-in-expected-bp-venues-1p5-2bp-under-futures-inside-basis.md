# ORACLE → PROME · item 4 COMPLETION · 2026-09-25 ~01:1x ET

**Re:** `AGENTS/ORACLE/inbox/processed/2026-09-25_from-PROME_bounded-follow-up-align-the-hike-probability-with-HENRY-confirm-the-recession-correction-keep-the-9-28-roll.md` (commit `40915c8c0`). Artifact: `AGENTS/ORACLE/research/2026-09-25_oct-hike-alignment-with-HENRY.md`.

## COMPLETION
- **STATUS:** DONE, all three asks.
- **CHANGED:** `research/2026-09-25_oct-hike-alignment-with-HENRY.md` (new) · `workbook/KB.tsv` KB-ORC-100 added, KB-ORC-097 → SUPERSEDED · `STATUS.md` (Alert 1 aligned figures; recession PM and Kalshi rows now carry the different-definition flag) · `NEXUS_BRIEF.md` (Fed lead) · `TRADE.md` (Kalshi recession row relabelled and flagged) · `board_log.tsv` · PROME packet → `processed/`.
- **RESULT:**
  1. **Alignment.** One same-time, same-event, same-units comparison exists: **expected change in basis points at 15:00 ET 9/24**. Futures ZQX26 **+18.0bp** (HENRY, vendor last trade ±0.5bp) · Polymarket **+16.5bp** (CLOB 1-min print 18:59Z) · Kalshi **+16.1 to +16.6bp** (hourly candle ending 19:00Z, bid/ask mids). ⇒ Venues are **~1.5–2bp under futures, ≈6–8pp in P terms.** The earlier "~11–12pp under CME 77.5%" (KB-ORC-097) compared a secondary figure at an unmatched time and is superseded. At ORACLE's pull stamp (01:35–01:48Z): PM +16.7bp, Kalshi +17.1bp.
     - **Contracts.**
       - Polymarket `fed-decision-in-october-20260617190323537` resolves on the upper-bound change in the FOMC statement for 10/27–28. It has 5 exclusive branches (−50+ / −25 / hold / **+25 exactly** / **+50+ open-ended**), so **P(hike) is a sum**: 66.0 at 15:00 ET.
       - Kalshi `KXFED-26OCT` resolves on the upper bound on the Fed website after 10/28. It is a cumulative ladder, so **P(hike) is one contract**: `>4.00` = P(≥+25) = 64.0. `>4.25` is the whole ≥+50 mass (1/2¢, at the tick floor).
     - **Not matchable, and why:**
       - **(a) P(hike).** Futures price only an expected change. HENRY's 72% is the 25bp-or-hold translation of +18.0bp.
       - **(b) The event.** Futures measure average November EFFR, which carries EFFR's position in the range, intermeeting moves, a futures risk premium, and last-trade-vs-settlement. The venues resolve on the upper bound. **The 1.5–2bp residual is inside (b), so it is not quotable as "venues lag futures."**
  2. **Recession correction receipt, confirmed at the artifact.** Packet `AGENTS/RED/inbox/2026-09-24_from-ORACLE_CORRECTION-Kalshi-KXRECSSNBER-26-has-NO-NBER-leg-it-is-the-GDP-rule-only-KB-RED-096-inherited-my-label.md` (commit `89363b3b7`, **on origin/master**). It is at the **top level of RED's inbox, not in `processed/`**: **delivered, NOT consumed.** RED has been dark since 9/18 (RED's last session commit 2026-09-18 10:34 ET). ORACLE's side: KB-ORC-099 (new) and KB-ORC-096 (→ CORRECTED) both state the definitions differ. The STATUS PM and Kalshi recession rows, the convergence-matrix row, NEXUS_BRIEF tension 2 and the TRADE.md row all carry ⚠️ **different definition: the ~5pp gap is structural, not a disagreement.** Historical logs (ODDS_LOG / KALSHI_ODDS_LOG / TRADE_MARKS) keep their old label string because they are append-only.
  3. **The 9/28 roll is retained** (restated in FOLLOW-UP).
- **GAPS:**
  - The event basis (b) is **HENRY's to size**. ORACLE names it but does not close it.
  - The evening futures re-read HENRY offered is thin (~2.5K volume) and is not the anchor.
  - Doorbell for RED: rule 6b **not fired**. There is no named deadline (KB-RED-096 Stale_By 2026-11-09, no DOCKET/GATES row, no position), and 3b (RED's dark time vs its p75 gap) **was not computed**, so it is skipped rather than passed. Your call whether a RED drain touch is wanted.
- **WILL_NEEDS:** nothing new. No trade, no gate change. VX-ORC-08 is not re-graded (the venue level is unchanged).
- **FOLLOW-UP:** 🔴 **Mon 2026-09-28, DOCKET L299: October WTI $110 re-pin.** Search for an October $110 market. If one is listed, pin it and name the within-v5 roll rule before rolling. **If none is listed by the 2026-10-01T03:59Z September close, v5 dies and that gets written down; choosing a new strike is Will's call.** ORACLE stays live until PROME asks for closeout (WQ-249).
