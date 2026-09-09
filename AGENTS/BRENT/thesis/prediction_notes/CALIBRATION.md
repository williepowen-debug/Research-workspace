# Prediction registration: calibration evidence

Read before registering an industrial-transmission prediction. This preserves the original calibration guidance; the source’s “no FAILED above 70%” tally is dated history and disagrees with later failed rows. Do not treat it as a current reliability guarantee. BRT-06 is now excluded from calibration under the September 7 convention; it cannot support a newly recomputed forecast score. Use the current scoring conventions in PREDICTIONS.tsv.

# DIRECTIONAL FAILURES (read before writing the next industrial-transmission prediction):
#   BRT-23 @ 70% — DRC SX-EW FM via sulphur cost → outcome via cobalt EXPORT BAN (policy confound, wrong mechanism)
#   BRT-24 @ 65% — Taiwan industrial rationing if Hormuz >30d → outcome avoided via record US LNG (mitigation channel underweighted)
#
# RESOLVED-SPECIAL (threshold-vs-mechanism split per [[finding_threshold_vs_mechanism]] — cross-agent 3-of-3 confirmed):
#   BRT-22 @ 75% — Dar es Salaam $800/t FCA: MECHANISM CONFIRMED (sulphur transmission firing); THRESHOLD untestable from BRENT data
#
# CALIBRATION FINDINGS (apply when writing the next prediction):
#   - Direct-supply / chokepoint / storage predictions: BRENT systematically UNDER-confident.
#     Anchor 80-95% when storage math + chokepoint geometry binds. (BRT-06 @ 55% overshot threshold by ~2000%.)
#   - Industrial-transmission (third-order: oil → input cost → industrial outcome): BRENT systematically OVER-confident.
#     Anchor 40-55% when chain has 2+ intermediating actors with optionality. (Failure pattern, n=2.)
#   - No FAILED above 70% conf — high-conviction predictions are reliable. Trust 85%+ calls.
#
# PRE-FLIGHT CHECK before writing the next prediction:
#   (1) Could this fail to fire entirely (nested conditional, out-of-lane, untestable threshold)? If yes, reframe.
#   (2) What makes it TRUE for wrong reasons? FALSE while thesis holds? If plausible, split mechanism + threshold sub-predictions.
#   (3) Mechanism attribution explicit ("via X, not Y")?
