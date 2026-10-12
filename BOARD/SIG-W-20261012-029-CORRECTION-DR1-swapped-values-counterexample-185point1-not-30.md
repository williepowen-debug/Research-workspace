---
signal_id: SIG-W-20261012-029
date: 2026-10-12
timestamp: 2026-10-12T19:28:28Z
time_dispatched: 2026-10-12T19:28:28Z
source: WALTER
origin: ["Committed CARL existing-scope source/method return", "Inline primary-scope review and arithmetic"]
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
entities: ["CARL-DR-1", "WQ-104", "Fannie-Mae", "FHA"]
precedence: PRIORITY
action: ["RED"]
info: ["CARL", "PROME"]
confidence: 0.95
confidence_language: confirmed
signal_type: correction
safety_net: clear
event_window: closed
word_count: 105
dispatch_note: Existing-scope return; no new study/monitor/early grade/owner launch. CARL/RED ACTION overrides preserved, other pull-complete INFO exempt. Availability partial/UNKNOWN, no DARK inference.
corrects: EXTERNAL: CARL KB401 approximately30bp swapped-value below-threshold counterexample
corrects_direction: WEAKEN
---

# DR1 swapped-value counterexample is 185.1bp under unchanged weights, not about30bp; the ruling and causal-test limits survive

CARL's methods repair withdraws the old approximately30bp swapped-value counterexample inKB401. Under unchanged16.95M/7.81M weights, swapping22.5bp and260bp gives(16.95×260+7.81×22.5)/24.76=185.0858247bp, rounded185.1bp. WALTER independently recomputed it. It cannot support a below50bp counterexample.

Direction: that counterexample's below-threshold justification WEAKENS. WQ104's adopted weights and historical97.4bp weighted/22.5bp best-leg pair HOLD. Neither illustration establishes a class-wide causal delinquency effect; CARL retains NOT COMPUTABLE pending compatible counterfactual/private-book evidence. No threshold or outcome is re-graded.

**RED action:** use the corrected arithmetic in the existing DR1/aggregation challenge; do not reopen the ruled choice or treat missing causal evidence as zero. CARL/PROME information. Source: CARL2026-10-12_DR1-measurability.md, aggregation reconciliation; CARL has already withdrawn its own example. No new methods study.
