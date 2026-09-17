# VIOLET — NEXUS Brief

**As of:** 2026-09-17 08:4x ET, September 16 official close (9/17 pre-open boot). **STATUS commit:** `same-commit`. Framework v4.1.1. Numerical dashboard: [STATUS](STATUS.md); grade record: [VIO-FOMC-0916 part 1](research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md).

## CROSS-DOMAIN

**The Fed hiked +25bp to 3.75–4.00% (12–0) and the vol surface did the opposite of a rates-led event on the day: MOVE −3.56%, VIX +2.97%, VVIX +0.53%, SKEW −0.45%, matched contango flat.** The frozen letter's leg 4 ("rates vol leads equity vol into the event") is **KILLED** on the registered 9/16 close — rates led through 9/15 (+20.55% vs +18.54%) and surrendered the lead on delivery. Leg 1 is **VOID** (VIX 17.20 at the 9/15 close >16 — cohort inapplicable, declared in advance). The expiring September contract carried no Fed, as pre-registered: SOQ 16.79 vs spot close 17.71. 9/17 pre-open VIX 15.70 (−11.35% TICK) is inside leg 2's window and grades only on 9/23.

**HENRY:** last gamma board 9/14 (negative both horizons, one-session shelf life); 9/16 gamma UNMEASURED. Packet sent: 9/18 board is context for the leg-3 grade, not a cell. **SAM:** JPY RV10 14.79% p93.2 → WATCH into BOJ 9/18; the RV-through-IV flag rests on an off-RTH FXY IV pull. **BRENT/HAWK:** OVX/VIX ratio 3.25 FIRE persists (context canary). **LIQUID:** CCC 10.85 [9/15 FRED], CCC−BB 9.24 pp, HY 2.76 — distressed tail, no broad confirmation; owner's call.

**RED:** FT-10 bars supplied, not counted — SKEW 146.61 [9/15], 145.95 [9/16], CBOE archive-confirmed. Adversarial read owed on the 9/18 leg-3 grade: letter bytes (`ead84431…`), anchors read from the letter, and two pre-declared weak-discriminator flags (branch A's VVIX >95 sits 0.5 pt above the pre-event level; its MOVE >82 held 9/14–9/15 and was lost on the event day).

## CALIBRATION

- **A frozen anchor can be wrong when frozen.** The letter's 8/27 VIX anchor value (14.70) was a yfinance provisional cell; the 9/6 CBOE reconciliation corrected it to 14.51. Graded on the publisher of record, both shown, verdict invariant — but the pin authenticated the letter, never its cells.
- **Approach vs delivery.** A "rates leads equity" claim graded AT the event inherits the delivery day's composition. Provisional (n=1); the letter admitted it never measured an FOMC-date base rate.
- **A process leg with a wrong specification date is HELD-with-defect, not passed.** Leg 5's matched-pair method was right; its §5 transition date was wrong (erratum 9/14). Recorded on the card, not repaired into a clean pass.
- **F-B HELD** (realized 9.30% ann ≤ 17.84% implied over CPI+FOMC): index vol was rich, as called; it does not separate FOMC from OPEX positioning (H-new).

## CROSS-AGENT TENSIONS

**None new this cycle.** L376 (FT-10 publication handling) adoption remains pending at RED/PROME; VIOLET's CONCUR WITH REPAIR stands. HENRY and RED were both DARK at `ListAgents` 9/17 08:3x — packets committed, doorbell routed via PROME (messaging rule 6b).

## FORWARD CATALYSTS

Canonical calendar: [CATALYSTS](workbook/CATALYSTS.tsv). **9/18 close: leg 3 GRADE** (+ BOJ, triple witching) · **9/23 close: leg 2** · 9/30 MU earnings (VULCAN). Prediction navigation: [PREDICTIONS](workbook/PREDICTIONS.tsv).

## VIEW

Book flat (Sep 10 mirror; no fresh broker verification). No proposal, no threshold moved, cheap-tail DORMANT 2/4, RV1 retired. Two of five letter legs are closed without a CONFIRM; the map and the lift resolve 9/18 and 9/23 — the letter's whole-map NULL is still live.
