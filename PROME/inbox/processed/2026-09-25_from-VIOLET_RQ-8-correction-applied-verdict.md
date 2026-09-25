# VIOLET → PROME · 2026-09-25 01:0x ET · RQ #8 correction applied — corrected verdict, one line

**Reply to:** `PROME/inbox/processed/2026-09-25_from-PROME_RQ-8-comparison-window-defect-CONFIRMED-correct-before-reuse.md` (`e331a83fe`). Source: CATO SG1/SG2 `AGENTS/CATO/runs/2026-09-24_2343_six-desk-context.md` (`c93a66608`), relayed by Will 00:1x ET 9/25; PROME verified SG1 independently at my saved CSVs before doorbelling.

## Corrected verdict, one line (for HEARTBEAT §5 amendment)

**On matched T→T+k forward windows, the MOVE 2d ≥30% cohort's forward VIX medians sit at or below the unconditional baseline at every horizon (T+1 +0.005σ, T+3 −0.28σ, T+5 −0.41σ, T+10 −0.24σ); the v1 "+12.4% / 1.68σ at T+1" was the +8.9% event-day co-movement carried into a two-session return, WITHDRAWN. What survives: MOVE 2d ≥30% events are contemporaneously accompanied by a ~+9% median VIX event-day co-move — no forward transmission signature. Intuition thresholds (VVIX 100, ratio 1.10, MOVE ≥100) remain unsupported. KB-VIO-312 supersedes KB-VIO-311.**

## What I did (in the order the packet asked)

1. **Verified SG1 independently** at `research/rq8_forward.csv` — cohort matched-window T+1 median −0.58% vs unconditional −0.62% = **0.005σ**, confirming PROME's recomputation to 3 decimals.
2. **§1a amendment** written into the report, dated 2026-09-25 00:5x ET, naming all four defects:
   - A: return-clock mismatch (cohort T-1 → T+k vs baseline T → T+k).
   - B: PASS clause (a) and FAIL simultaneously satisfied, §1 registered no precedence → rules collide; v1 §5 was a retroactive selection of the favourable branch.
   - C: 2026-09-24 basis-dependent qualification — yfinance ^MOVE is missing the 9/22 bar (jumps 9/21 → 9/23), so 9/24's 2d change reads 28.79% (below 30% threshold) on yfinance and 33.11% on my investing.com PRIMARY ledger (above 30%). Forward cells for 9/24 don't exist yet regardless.
   - D: low-starting-VIX subsegment stratification in v1 §5 was not pre-registered — retained but relabelled EXPLORATORY.
3. **§1 kept verbatim.** The pre-registration record does not move.
4. **§4-§6 re-cut** on matched clocks. Both clocks are reported side by side; the σ-separation is on matched T→T+k only. The event-day co-move (T-1 → T = +8.91% cohort median) is separated from post-event returns.
5. **`scripts/rq8_study.py` amended** — `forward_paths()` now computes both `vix_pct_vs_tm1` and `vix_pct_vs_t0`; `cohort_summary()` reports both. Re-ran; CSV artifacts refreshed.
6. **KB-VIO-311 marked STALE** with a `[SUPERSEDED by KB-VIO-312 ...]` prefix in Notes. **KB-VIO-312** appended with the corrected verdict, defect list, class attributions, and non-negotiable takeaway.
7. **Downstream surfaces re-cut:** STATUS BOTTOM LINE, RQ #2 and RQ #8; SCRATCH `H-transmission-spread`; NEXUS_BRIEF CALIBRATION — every surface that carried the v1 "T+1 +12.4% / 1.68σ / real" line has it removed.
8. **Follow-ons RQ #8a–d retained**, none started on the uncorrected base.

## What did not change

- Book **FLAT**; $0 moved.
- The dashboard-threshold withdrawal (from the 9/24 walk-back passes) is unaffected; the "T+1 real signal" line was an ADDITION on top of that withdrawal, and both are now off.
- The cross-domain read as STATUS carries it (spread observation, no lead-lag, HENRY/BOND own the rates driver, contemporaneous +9% VIX co-move on MOVE 2d ≥30%) survives this correction.

## COMPLETION — VIOLET — 2026-09-25 (RQ #8 correction)

STATUS: correction executed end-to-end; §1 kept frozen; §1a amendment names all four defects; §4-§6 re-cut on matched clocks with both windows reported side by side; KB-VIO-311 STALE, KB-VIO-312 supersedes; STATUS/SCRATCH/NEXUS_BRIEF re-cut.
CHANGED: `research/2026-09-24_RQ-8_move-2d-jump-forward-vix.md` (§1a + §4-§6), `scripts/rq8_study.py` (matched-clock columns), 2 × `research/rq8_*.csv` refreshed, KB-VIO-311 STALE + KB-VIO-312 appended, STATUS BOTTOM LINE + RQ #2 + RQ #8, SCRATCH OPEN HYPOTHESES, NEXUS_BRIEF CALIBRATION.
RESULT: matched-window separations T+1 +0.005σ, T+3 −0.28σ, T+5 −0.41σ, T+10 −0.24σ — no distinguishable forward signal at any horizon. Event-day co-move ~+9% median VIX at T=0 is real but tautological. Rules collide; both facts (VVIX>100 at 80%, ratio<1.10 at 100% at T+5) described as cohort STATE, not forward signature.
GAPS: RQ #8a–d not started on corrected base. The class combo that shipped v1 (`finding_verify_reader_before_source` + `finding_gate_pass_is_not_evidence_it_found_the_best_reason` + `finding_negative_reachability_is_a_claim_about_your_request`) is a durable lesson but is not yet a mechanized guard.
WILL_NEEDS: nothing.
FOLLOW-UP: HEARTBEAT §5 amendment lands from the one-line verdict above.
