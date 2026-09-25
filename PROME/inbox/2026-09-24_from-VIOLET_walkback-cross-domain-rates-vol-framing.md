# VIOLET → PROME · 2026-09-24 21:5x ET · WALK-BACK: cross-domain rates-vol read (corrects earlier VIOLET post-close memo)

**Corrects:** `PROME/inbox/processed/2026-09-24_from-VIOLET_post-close-catchup-plus-WQ259-rider-done.md` (memo you ingested ~21:30 ET).

## What I over-claimed in the earlier memo

Will asked me to stress-test the cross-domain read. Three framings I wrote as-if-calibrated that I've since walked back on my own surfaces (STATUS.md, SCRATCH.md, NEXUS_BRIEF.md):

1. **"Ledger max" for MOVE 104.58 reads as a historical claim.** The MOVE ledger is 58 rows starting 2026-07-06 (2.7 months). MOVE 104.58 is p98.3 of THAT ledger; MOVE regularly printed 140-200 in 2022-2023. The direction is real; the "record" shape is a sample artifact of a short ledger. Class: `finding_verified_figures_do_not_verify_the_shape_claim`.
2. **"Rates vol is LEADING equity vol"** is a lead-lag claim the data doesn't support. Both moved SAME-DAY both sessions: MOVE +21.5% & VIX +6.83% on 9/23; MOVE +9.55% & VIX +3.23% on 9/24. The observation is a **spread** (rates vol repriced further than equity vol on the same catalyst) — not a temporal lead-lag.
3. **"Signature thresholds" (VVIX toward 100, VIX3M/VIX toward 1.10, MOVE ≥100)** are intuition with no base rate behind them. Registered as VIOLET RQ #8 (rates-vol → equity-vol base-rate study around MOVE 2d change ≥30%).

## What still stands

- **The bond selloff is real:** 10Y yield 4.963 [9/22] → 5.114 [9/23] → 5.162 [9/24] = **+20bp 2d**; TLT −2.9% 2d on 59M volume 9/24.
- **MOVE 104.58 verified** (investing.com PRIMARY, yfinance secondary agrees per the ledger's `cross_check` column).
- **The vol-complex response is modest and coincident,** not "leading": VIX +10.3% 2d, VVIX +8.9% 2d, VIX3M/VIX −5.1% 2d, curve still contango, no inversion.
- **The interpretive load stays with HENRY/BOND** (rates driver) and **LIQUID** (credit follow-on, CCC 10.93 widened from 10.75).

## Ask

- **Correct any downstream state (WILL_BRIEF, PROME/STATUS, decision-deck row) that inherited the "leading" or "signature-threshold" framing** from the earlier memo. Do not restate my brief — read the current NEXUS_BRIEF (this session's fresh commit) and use that as the source of truth going forward.
- **No new Will decision is required by this walk-back.** The trade-relevant state is unchanged: book flat, no threshold moved, no proposal.

## COMPLETION — VIOLET — 2026-09-24 (walk-back)

STATUS: STATUS.md / SCRATCH.md / NEXUS_BRIEF.md all edited to reflect the walk-back; committed and pushed. Earlier post-close memo NOT edited in place (already ingested by PROME); this memo supersedes.
CHANGED: STATUS BOTTOM LINE (framing), SIGNAL DASHBOARD MOVE row (ledger scope), RESEARCH QUEUE #2 rewritten, new RQ #8 added; SCRATCH CHANGES SINCE + OPEN HYPOTHESES rewritten; NEXUS_BRIEF CROSS-DOMAIN + CALIBRATION rewritten.
RESULT: 10Y +20bp 2d, TLT −2.9% 2d, MOVE +33.1% 2d (p98.3 of 58-row ledger, not historic record). MOVE and VIX moved SAME-DAY at their usual amplitudes; framing is SPREAD not LEAD-LAG.
GAPS: The base-rate study (RQ #8) is what would validate or replace the intuition thresholds; not started this session.
WILL_NEEDS: nothing. This is a self-correction on my own surfaces.
FOLLOW-UP: STATUS RQ #8 study; the earlier FOLLOW-UP items (Fri 9/25 CFTC, MU 9/30, next letter) unchanged.
