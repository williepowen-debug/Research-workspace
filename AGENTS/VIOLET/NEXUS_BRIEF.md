# VIOLET — NEXUS Brief

**As of:** 2026-09-24 21:1x ET, graded on the **September 24 session close** (post-close catch-up session; Will's ask "get caught up with fresh data"). **STATUS commit:** `56f1c8ffb`. Framework v4.1.1 (**unchanged**). Numerical dashboard: [STATUS](STATUS.md). FOMC grade records: [part 1](research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md) · [part 2](research/2026-09-18_VIO-FOMC-0916_GRADE_part2.md) · **[part 3: LEG 2 + WHOLE LETTER](research/2026-09-24_VIO-FOMC-0916_GRADE_part3.md)**.

## CROSS-DOMAIN

🔴 **HENRY / LIQUID / BOND: rates-vol shock is now a two-day follow-through, not a one-day print.**
- MOVE 78.56 [9/22] → 95.45 [9/23] → **104.58 [9/24]**, cumulative **+33.1%** over two sessions, ledger-max both days. Margins **+32.17 over F1**, **+29.08 over confirm-3**.
- The vol-side signature is **loading, not firing**: VVIX 83.17 → 88.60 → **90.57** (crossed the 90 cheap-line for the first time this run); VIX3M/VIX 1.2393 → 1.193 → **1.1761** (compressing 2 sessions, still contango, no inversion); VIX 14.21 → 15.18 → **15.67** (+10.3% cumulative).
- **The direction of transmission I have not attributed.** Rates substance is HENRY/BOND. My hypothesis for the vol side: if MOVE holds ≥100 and VIX3M/VIX compresses toward 1.10 with VVIX toward 100, that is the transmission signature. Right now none of those thresholds is met.
- ⚠️ **9/23 and 9/24 CBOE history is not yet published.** VIX-complex cells are CBOE delayed-quote + yfinance readings; provisional. `backfill.py --spot-only` yielded 0 corrections this session — the readings are trusted enough to grade against but not enough to close leg 2 formally (margin holds at 2+ points either way).

🟠 **LIQUID: credit tail firmed.** FRED 9/23 readings: HY **2.72**, CCC **10.93** (from 10.75 [9/22]), IG **0.78**, CCC−BB **9.34 pp**. BIN-B block active. The MOVE-plus-CCC pattern is the historical setup for a "credit non-confirmation" event (KB-VIO-071 Path B), not the credit-led Path A. The interpretation is yours.

🔴 **BRENT / HAWK: OVX channel sustained FIRE.** OVX 54.45 p89.7, ratio 3.47 p97.0, gap 38.78 p94.5 [9/24]. Oil-vol → equity-vol transmission channel is LOADED. Substance is yours; I hold only the transmission read.

🟢 **SAM: JPY carry vol collapsed.** RV10 6.5% p29.1 CALM [9/24, USDJPY 158.26], from 11.1% p72.6 [9/18]. The event-conditioned watch resolved. WALTER's ¥158 rate-check report from 9/21 decayed at Tokyo's reopen 9/24 with no confirmation you have relayed.

**RED:** SKEW bars I supply for FT-10: 9/18 **148.10** (CBOE SETTLE) · 9/21 142.19 · 9/22 144.80 · 9/23 146.15 (yf) · 9/24 146.04 (yf). None ≥150. **RED owns the count.** RED-FT-06: VIX 15.67 [9/24].

**HENRY / RED (INFO only, not routed by me):** WALTER SIG-W-20260924-007/014 delivered a negative-beta share chart; treated as INFO. Vol complex does not confirm a breadth-driven regime break (VIX 15.67, VIX3M/VIX 1.1761 contango). Interpretation is not mine.

**VIO-FOMC-0916 is closed. Verdict unchanged: 0 CONFIRM · 2 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect.**
- **Leg 2 KILL** cannot flip at any reading through 9/24: VIX 15.67 = **−11.52%** from the 9/16 close, against a kill line of −1.41%. Margin remains large.
- ⛔ Legs 2, 3 and 4 are one error on one event, not three findings.

## CALIBRATION

- ⭐ **Two consecutive ledger-max prints on a canary is not a "one-day shock" and it is not "a regime."** It is what a canary is for — signal building without VIOLET declaring the ceiling. The move belongs in NEXUS CROSS-DOMAIN, not the 🔴 outbox lane. (WQ-303 class, applied.)
- ⭐ **A leg that borrows a conditioned base rate must also borrow the condition's void clause.** Leg 1 was voided because VIX was above 16. Leg 2 used the same cohort's 88% prior with no void clause; the level cohort that actually applied (n=34) had a 53% prior. Acceptance condition ⑤ for the next letter.
- ⭐ **A correction can sit unread in your own inbox.** WALTER's 9/19 signal carrying the 9/18 MOVE print sat 5 days until a due-row spawn drained the inbox. (KB-VIO-309.)
- **A publisher's delayed-quote "close" is not the settle for every series.** VVIX was 87.63 at the 16:05 stamp against 87.38 in the history file. Grade VVIX on the history file only.
- **The instrument worked and the thesis did not.** Pre-registration made a wrong model fail on schedule and in public. v4.1.1 stands.

## CROSS-AGENT TENSIONS

None active this cycle. Part 3's B-branch-3/3 finding does not shift anything on HENRY's side (branch A is the realised Fed outcome, not a confirmed surface branch).

## FORWARD CATALYSTS

Canonical calendar: [CATALYSTS](workbook/CATALYSTS.tsv).
- **Fri 9/25 15:30 ET:** CFTC TFF report for 9/22 — watch lev-money net for a positioning shift after the two-day rates-vol print.
- **Wed 9/30:** MU FQ4 earnings (VULCAN owner).
- **Wed 12/16:** M1:M2 historical-average re-check (KB-VIO-310; PROME implements the FORGE side).
- **Owed by me:** next post-close boot after CBOE catches up, republish both Will-facing artifacts under WQ-259 (Will-approved 2026-09-24; condition not yet met this session), draft the next pre-registered letter against conditions ①–⑤ with a real FOMC-date base rate.

## VIEW

- The book is **FLAT**. No proposal, order or card; no threshold set or moved; $0 moved.
- Convergence moved **27 → 28/50, +1 net.** Two vectors up 1 (VVIX ⚪1→🟡2 crossing 90; front-curve ⚪1→🟡2 compressing); JPY down 1 (🟡2→⚪1, RV10 collapsed).
- The regime is **LOW_VOL** at 15.67 with the curve compressing but in contango. **The story is the cross-domain rates-vol channel, not the VIX complex on its own.**
