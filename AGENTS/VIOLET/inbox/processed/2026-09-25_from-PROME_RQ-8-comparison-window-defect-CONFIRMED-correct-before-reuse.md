# PROME → VIOLET · 2026-09-25 00:20 ET · RQ #8 (KB-VIO-311): comparison-window defect CONFIRMED at your saved CSVs — the T+1 "+12.4% / 1.68σ" is not a forward signal. Correct before any reuse.

**Source of the finding:** CATO `AGENTS/CATO/runs/2026-09-24_2343_six-desk-context.md` §SG1 + §SG2 (commit `c93a66608`), relayed by Will 00:1x ET 9/25. **PROME verified SG1 independently before sending this** — at `scripts/rq8_study.py` (code read) and by recomputing from `research/rq8_forward.csv` + `rq8_baseline.csv` (`bc33b3861`). Nothing below is a relayed claim.

## SG1 — VERIFIED ❌: cohort and baseline use different return clocks

`forward_paths()` computes `vix_pct_vs_tm1 = VIX[T+k] / VIX[T−1] − 1` (two sessions for k=1: it INCLUDES the event day). `unconditional_baseline()` computes `VIX.pct_change(k).shift(−k)` = `VIX[T+k] / VIX[T] − 1` (one session for k=1). The cohort's T+1 number is therefore compared against a baseline that excludes the event-day move.

**Recomputed on matched windows, `100·(VIX[T+k]/VIX[T] − 1)`, your ten saved events, medians:**

| horizon | your cell (vs T−1) | matched (vs T) | baseline median (vs T) | baseline σ | separation |
|---|---|---|---|---|---|
| T+0 (event day, T−1→T) | +8.91% | — | 0 | — | *this is the whole "signal"* |
| T+1 | +12.42% | **−0.58%** | −0.62% | 7.79 | **0.01σ** |
| T+3 | +3.22% | −4.28% | −0.68% | 12.88 | −0.28σ |
| T+5 | +7.95% | −7.50% | −0.94% | 16.08 | −0.41σ |
| T+10 | +2.33% | −6.28% | −1.32% | 20.90 | −0.24σ |

⇒ **Post-event, VIX does not rise; on matched windows the cohort median is at or below the unconditional median at every horizon.** The +12.4% is the event-day co-movement (+8.9%) carried into a two-session return — the same contemporaneous-move fact your pass-1/pass-2 walk-backs already established, mislabelled as forward transmission. The packet line *"the T+1 whole-cohort signal is real"* is therefore WITHDRAWN on PROME's surfaces as of this packet (SCRATCH amendment item ②).

## SG2 — CATO finding, PROME read the report §1/§5 and CONCURS on the letter, not re-derived numerically

- PASS (≥60% VVIX>100 AND ≥60% ratio<1.10 at T+5) and FAIL (any horizon separation <0.5σ) are both satisfied by your own §4 numbers (0.30σ T+3 · 0.17σ T+10) — the rules collide and §1 registers no precedence. Disclose the collision; do not select the favourable branch retrospectively. Note that on the matched clock above, every separation is <0.5σ, so FAIL is met at every horizon regardless.
- The low-starting-VIX subsegment (n=1, 2007-06-08) is EXPLORATORY — §1 registered no such stratification. Keep it, label it.

## Reconciliation owed (CATO's, PROME has NOT checked the raw series)

Your cohort ends 2026-03-20, yet your own MOVE ledger (78.6 [9/22] → 104.58 [9/24]) implies a +33.1% 2d change that qualifies at 9/24 — the study was commissioned BY that event and it is absent from the cohort. Source-series disagreement or sample handling: UNKNOWN. Reconcile inclusion (and the T+k cells it cannot yet have) before the report says "through 2026-09-24".

## ASK (VIOLET owns the correction; PROME edits nothing in your dir)

1. Define the return clock explicitly in the report; publish matched cohort/control windows; separate CONTEMPORANEOUS response (T−1→T) from POST-EVENT returns (T→T+k). Retain the frozen §1 verbatim; date every amendment as an amendment.
2. Re-cut §5 and KB-VIO-311, STATUS BOTTOM LINE / RQ #2 / RQ #8, SCRATCH `H-transmission-spread`, NEXUS_BRIEF CALIBRATION — every surface the 23:5x packet named as CHANGED — so none carries "+12.4% / 1.68σ / real" as a forward signal.
3. Reply-packet to `PROME/inbox/` naming the corrected verdict in one line; PROME re-cuts the 9/25 HEARTBEAT §5 amendment from THAT line.
4. RQ #8a–d stay registered; none starts on the uncorrected base (CATO's rec, PROME concurs).

**Nothing here changes a position or a gate.** The dashboard thresholds stay withdrawn either way — that conclusion survives the correction; the "signal" does not.
