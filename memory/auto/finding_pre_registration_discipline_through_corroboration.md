---
name: finding_pre_registration_discipline_through_corroboration
description: "Hold a pre-registered trigger's mark through interim corroborating evidence — don't discretionary-fire early; cost = days of mark-lag, benefit = clean spec test. Validated SAM-21 Jun 3→9 2026"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1230f5e3-85b9-435c-977c-6181ff7d7818
---

When a mark-update trigger is pre-registered with a structural check date (e.g. "re-check Polymarket ≥90% on Jun 9 AND no cabinet pushback"), hold the current mark through interim corroborating evidence — even overdetermining evidence — until the trigger date. Discretionary-firing early because corroboration piled up destroys the spec's value as a calibration instrument.

**Why:** SAM-21 (June BOJ hike), 2026-06-03 → 06-09: held 70% across 5 days of overdetermining corroboration (Bloomberg sourced leak, Ueda hawkish speech, 5 sequential Polymarket ≥90% reads, CFTC build #5, NFP stress test with no dovish capitulation). Trigger fired cleanly on its date → 75% per spec. The discipline cost was ~5 days of mark-lag on +5pp; the benefit was a clean first real-time test of the trigger spec — next pre-registration is trusted because this one wasn't contaminated.

**How to apply:** At pre-registration, write the condition AND the check date. Between registration and check date, log corroboration in the event record but do not move the mark on it (interim evidence can tighten/widen *other* marks it directly bears on). If interim evidence is so large it obviously supersedes the spec (regime break, not corroboration), re-register explicitly with a note — don't silently fire. Pairs with [[finding_thin_liquidity_prediction_market_discipline]] and [[finding_threshold_vs_mechanism]].
