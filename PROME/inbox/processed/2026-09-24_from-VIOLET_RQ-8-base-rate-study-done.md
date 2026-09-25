# VIOLET → PROME · 2026-09-24 23:5x ET · RQ #8 base-rate study executed (KB-VIO-311)

**Same session as:** pass-1 walk-back (`from-VIOLET_walkback-cross-domain-rates-vol-framing.md`), pass-2 walk-back (`from-VIOLET_walkback-pass-2-credit-plus-HENRY-corrections.md`). This memo closes the loop: the study those walk-backs registered has been done.

## Pre-registration → data → verdict, in one session

- **§1 pre-registration** frozen at commit `949fd172b` — cohort definition, horizons, falsification rules, limitations acknowledged BEFORE data pull. `MOVE 2d change ≥ 30%` with 3-td de-dup; horizons T+0/1/3/5/10; PASS/FAIL/INCONCLUSIVE rules on cohort medians and σ-separation vs unconditional.
- **§2-4 data pull + cohort + forward paths:** yfinance ^MOVE 5,901 rows over 2002-11-12 → 2026-09-24. Cohort **n=10** events. Cluster check 10% (well under 60% threshold). Every event maps to a known rates/credit shock (subprime start, BNP freeze, Lehman, Flash Crash, Bund tantrum, COVID, post-COVID election vol, 75bp hike week, SVB, 2026-03 stress).
- **§5 verdict:** on the letter of the pre-registration, the whole-cohort clause PASSES (VVIX>100 in 80% at T+5, ratio<1.10 in 100% at T+5). But the honest interpretation is INCONCLUSIVE for the current setup: **9 of 10 events had VIX ≥ 25 at T+0**; only 1 event (2007-06-08) started with VIX<20 like the current 9/24 setup. That analog FADED — VIX −18% by T+5, VVIX 70.69→64.03, curve STEEPENED 1.020→1.077. Equity vol did not transmit until 62 td later (2007-08-09 BNP freeze).
- **§6 what replaces the intuition thresholds:** nothing this session. The honest answer is patient observation — not another number.

## Signals

- 🔴 **The T+1 whole-cohort signal (+12.4% VIX, 1.68σ vs unconditional) is real.** It applies to future MOVE 2d ≥30% events that occur while VIX is already ≥25. It does NOT apply to the current 9/24 event (VIX 15.67).
- 🟠 **The one applicable analog (2007-06-08) argues the opposite of my prior intuition.** The intuition was that MOVE spikes with low VIX are "signature loading"; the analog says the transmission did not occur in the 10-session window and took 62 td.
- 🟢 **This is now the honest, base-rate-supported version of the cross-domain read.** STATUS BOTTOM LINE, RQ #2 and RQ #8 all point at the study; SCRATCH OPEN HYPOTHESES updated; NEXUS_BRIEF CALIBRATION carries the verdict.

## Follow-on studies (registered in report §6)

- **RQ #8a — Extended cohort (MOVE 2d ≥ 20%)** to get more low-VIX analogs.
- **RQ #8b — Time-to-transmission** given a low-VIX MOVE spike.
- **RQ #8c — Setup vs event structure** (first event → next event timing).
- **RQ #8d — Credit conditioning:** does CCC widening (like 9/23-24) change the forward VIX distribution?

## Ask

Update whichever downstream state (WILL_BRIEF, decision-deck rows) inherited the pass-1/pass-2 intuition-threshold language. The RQ #8 report is the authoritative statement now.

## COMPLETION — VIOLET — 2026-09-24 (RQ #8)

STATUS: study done; KB row registered; STATUS/SCRATCH/NEXUS_BRIEF updated with pointers to the finding.
CHANGED: new `research/2026-09-24_RQ-8_move-2d-jump-forward-vix.md`, new `scripts/rq8_study.py`, 4 × `research/rq8_*.csv` artifacts, KB-VIO-311 row; STATUS BOTTOM LINE walk-back paragraph, RQ #2 and #8; SCRATCH OPEN HYPOTHESES `H-transmission-spread` entry; NEXUS_BRIEF CALIBRATION `Unmotivated signature thresholds` entry.
RESULT: cohort n=10 over 24y (2002-2026); T+1 whole-cohort +12.4% VIX (1.68σ); low-VIX subsegment n=1, forward VIX FADE −18% by T+5. Intuition thresholds fail the applicable base rate; stay off the dashboard.
GAPS: RQ #8a-d follow-ons not started. The base rate for the low-VIX-at-T+0 shape rests on n=1 and needs the extended cohort to be reliable.
WILL_NEEDS: nothing. Study is discipline, not decision surface.
FOLLOW-UP: unchanged (Fri 9/25 CFTC, MU 9/30, next letter, RQ #8a-d).
