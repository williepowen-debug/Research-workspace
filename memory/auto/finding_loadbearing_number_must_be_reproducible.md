---
name: finding_loadbearing_number_must_be_reproducible
description: "A load-bearing derived number that can't be regenerated from its stated recipe is the tell it's wrong — the ship-gate for any count/stat is re-running it, not eyeballing it"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b61ebe00-b3e8-47e8-8a3a-08bdb30dca0a
  modified: 2026-07-24T18:12:22.815Z
---

The ship-gate for any **load-bearing derived number** (a census count, an FP rate, a percentile, a ratio) is: **can I regenerate it from a stated recipe (series + window + transform)?** If not, it must not ship. Un-reproducibility is the *diagnostic*, not a footnote.

**Why:** DEWEY's 2026-07-16 funding-gate (07b) report shipped a +30bp fire-day census of "26 (8 TP / 18 FP / 2 non-cal)". LIQUID's independent rebuild (`fp_backtest_079.py`) got **48** raw fire-days and 62% episode-FP vs the report's "~20%". On the reconcile, DEWEY re-derived independently from raw FRED (own code path) and reproduced LIQUID **exactly** — 48, not 26. The "26" reproduced under **no** construction tried (strict `>30`=42, median-SOFR=10, unrounded=45): it was an un-reproducible sub-agent intermediate mis-transcribed into a table, and the "8 TP / 2 non-cal" cells had mislabeled the 8 *non-calendar episodes* as a TP/FP split. Two compounding errors: (1) a bad count, (2) a **day-weighted** FP that flattered the gate because one true event (Sep-2019) supplied ~8–9 of 21 non-cal fire-days — the episode-level unit is the honest one.

**How to apply:** (a) For any derived stat that gates a decision, **re-run it from the recipe before shipping** — especially if a sub-agent produced it (`[[finding_workflow_scratch_crash_recovery]]`). (b) State the recipe *in the report* so a reader can regenerate it — a number with no reproducible recipe is a red flag on its own. (c) Pick the **decision-relevant unit**: count distinct events (episodes), not days, when day-weighting lets one long event drown many short false alarms. (d) When a counterparty's independent rebuild disputes your number, **re-derive independently** — don't just defer and don't just dig in; the re-derivation is what settles it (`[[finding_asymmetric_rigor_counterparty_claims]]`, `[[feedback_verify_state_before_propagating]]`, `[[finding_verification_correction_downstream_propagation]]`). (e) Correct via a dated addendum that preserves the original and flags the wrong cells, don't silently rewrite (`[[finding_pov_changelog_pattern]]`).
