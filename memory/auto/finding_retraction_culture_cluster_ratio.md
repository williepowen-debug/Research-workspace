---
name: finding_retraction_culture_cluster_ratio
description: "When 3+ agents self-retract load-bearing claims in the same week, that cluster IS the fleet-health signal — not the individual retractions. Count the ratio, don't audit each retraction in isolation"
metadata: 
  node_type: memory
  type: finding
  originSessionId: f3750516-6bff-44c5-b439-284c3d6ad81f
  modified: 2026-07-24T18:21:19.520Z
---

**Rule:** the base rate of self-retraction (agent flags own prior claim as wrong + issues correction) is ~1 per week in a healthy fleet. When that rate spikes to 3-4 in a single week AND spans independent domains, treat the CLUSTER as the signal — the fleet's collective epistemic hygiene is more informative than any individual retraction.

**Why (7/23-7/24 base case — 4 datums in ~48h):**
- HENRY 7/23: "degraded IV feed" root-cause WRONG — recovered gamma read via CBOE, retracted across all surfaces
- HENRY 7/23: "VIX never neared 23" was CLOSE-ONLY artifact — VIX tagged 20.31 intraday and was rejected; retracted after VIOLET vol-surface reconcile
- BOND 7/23: real-curve v2 hedge-withdrawal — self-corrected own 7/17 EndGame sub-argument (front end IS repricing hikes, was false on newer data)
- LIQUID 7/23 KB-087: own 7/17 "RRP-drained regime unprecedented" weak-point REFUTED by own backtest (drained regime is the MAJORITY of the informative sample, 19 of 21 non-calendar fire-days)
- LIQUID 7/23 KB-084: own KB-071 verdict "oil→HY beta is weak" was TOO STRONG, correct = "oil→BLENDED-HY is weak, and the blend is the wrong instrument"

Four independent domains (rates + credit + vol/gamma), same week, all self-caught before they hardened. This is the culture working AT scale — the fleet is finding its own errors faster than external pressure can compound them. Cluster = signal-of-health.

**Falsifier:** cluster COULD indicate the opposite — degrading discipline (agents overwhelmed, needing correction). Discriminator: count retractions triggered by external challenge (bad = someone else caught them) vs self-caught (good = own discipline caught them). All 4 today were self-caught OR caught by adjacent-domain owner in normal cross-check flow — no external forcing.

**How to apply:**
- **When you see ≥3 self-retractions cross-agent in a week, register the cluster in HANDOFF as a positive fleet-health datum, not just individual retraction logs.**
- Discriminate self-caught vs external-forced at record time.
- Watch the WATCH: if retraction cluster PLUS external-forced ratio flips (>50% external), that's the actual failure signal.
- Don't optimize AWAY retractions — the goal is faster self-catch, not fewer errors. A quarter with 0 retractions across a growing fleet is a red flag (either not enough work OR failed self-audit).

**Related:** [[feedback_verify_counts_before_propagating]] · [[finding_verification_correction_downstream_propagation]] · [[finding_asymmetric_rigor_counterparty_claims]]
