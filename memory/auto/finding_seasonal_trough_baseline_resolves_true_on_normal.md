---
name: finding_seasonal_trough_baseline_resolves_true_on_normal
description: A falsifier baselined on the LATEST single period of a seasonal series can pick the trough — then ordinary seasonal recovery resolves it TRUE while carrying zero information about the event being tested
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cbf572d5-63c6-4eb0-8e30-e2f903eb8ae6
  modified: 2026-07-27T20:04:49.369Z
---

Setting a prediction's baseline from **the most recent single quarter/month** of a **seasonal** series silently picks whatever point in the cycle you happen to be standing on. If that is the trough, the threshold *"materially above <trough>"* is cleared by **normal seasonal recovery** — the prediction resolves TRUE having measured nothing about the event it was written for.

**Worked instance (SHADE/CREED, 2026-07-27, caught ~7 weeks before the print):** CREED registered `PRED-CREED-006` (65%) — the MBA Q2-2026 life-insurer commercial/multifamily line should move *"materially above its +$3.3B Q1 run-rate"* if Athene's ~$9B ARI purchase landed there. Pulling the MBA Q4-2025 report to primary showed **+$3.3B is the seasonal low, not a run-rate**: Q3-2025 **+$12.1B**, Q4-2025 **+$11.5B**, and H1-2025 added just **+$4.4B across two quarters** against H2-2025's **+$23.6B** (H2 = 5.4× H1). **A +$11B print would have satisfied the test while being exactly the prior-year norm.** Re-spec: threshold ~**+$20B** (≈ the $9B *above* the Q3/Q4 norm), tested against **the prior four quarters** rather than the latest one.

**Why:** a baseline is an implicit claim that the comparison period is *representative*. One period never establishes that, and seasonality makes the error directional rather than random — you are most likely to notice a series right after an unusual print, which is exactly when it is least representative.

**How to apply:** before registering any threshold of the form *"above/below <recent value>"*, **stack the prior 4+ periods of the same series** and ask "is my baseline the median, the trough, or the peak?" State the baseline's percentile, and prefer *"X above the N-period norm"* over *"above last period."* Then check `finding_rebased_metric_check_made_date` — if the re-based metric was already true at Made_Date, retire and replace instead of re-basing. Distinct from [[finding_threshold_level_is_a_measurement_not_a_constant]] (staleness through drift) — here the number is fresh and still wrong, because it is *phase*-wrong. Kin: [[finding_threshold_spec_fails_before_world]], [[feedback_single_month_subcomponent_skepticism]], [[feedback_yoy_baseeffect_use_multiyear_stack]], [[finding_run_the_falsifier_before_promoting]].
