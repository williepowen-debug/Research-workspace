---
name: finding_base_rate_the_instrument_before_its_event_table
description: "A new instrument's event table renders sign/scaling errors as tidy, plausible findings — compute how often the flag fires AT ALL before reading any of its events; and a coverage map, separately, because absence and no-signal look identical"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 914026fb-6f24-494e-980f-e41b33646c8d
  modified: 2026-07-30T15:00:25.249Z
---

When you build a new detector, the first output you want to read is the **event table** — the dates it fired, the leads, the hit rate. **Read the base rate first instead: what fraction of all periods does this flag fire on?** An event table is a *filtered view*; it inherits any sign, scaling, or unit error **silently** and renders it as a tidy set of dates with plausible-looking structure.

**VIOLET, 2026-07-30 (H3: does the front VX basis invert before the VIX3M/VIX index ratio?).** v1 computed `basis = spot − M1` and labelled negative values "backwardation." That is exactly inverted — in normal **contango** the front future trades *above* spot, so `spot − M1 < 0` is the **ordinary state**. The event table it produced looked like clean support for the hypothesis: *basis led 4, ratio led 0, median lead +19.5 td*. Entirely believable. Nothing in the table looked wrong, because a table of dates cannot show you that its predicate means the opposite of what you named it.

Two base rates killed it in one line of code each:
- the flag fired on **85.9% of all days** — a signal that is on 86% of the time cannot be a peak marker;
- it had **zero overlap** with index-ratio inversion — arithmetically impossible for two measures of the same phenomenon unless one is measuring the *opposite* thing.

Corrected (`basis = M1 − spot`, negative = backwardation), it fires on 14.1% of days and the real result is different from the hypothesis: no meaningful timing lead (median **+0.5 td**), but better **coverage and precision** than the incumbent.

**Why:** an event table answers "when did it fire?" and presupposes the flag means what you think. The base rate answers "does this predicate carve the world roughly where I expect?" — the cheaper, prior question. Plausible output is not validation; a wrong instrument produces confident, well-formatted results, which is exactly why it survives review ([[finding_plausible_stale_value_evades_review]]).

**How to apply:** before reading any event/hit table from a newly built detector, print (1) **fire rate** — % of periods flagged; (2) **overlap** with any existing instrument measuring the same thing; (3) a couple of **hand-checked extreme rows** against a source you already trust. If the fire rate is implausibly high or low, or the overlap with a known-good sibling is 0% or 100%, stop — you have a sign/unit/scaling bug, not a finding. Then sanity-check the direction against a value you have already **published** elsewhere (the corrected convention here was the one STATUS.md had been printing all along).

**Run the coverage map too — it is a separate check for a separate defect, and neither finds the other.** The same run had an independent bug: roughly half the requested window had **no source data at all** (CBOE serves VX settlement on a ~12-month rolling window), and the script rendered "no data" **identically to** "no inversion," manufacturing a whole signal bucket out of pure absence ([[finding_silent_blank_evades_review]], [[finding_discovery_tool_wrong_slice_false_zero]], [[finding_partitioned_source_returns_stale_window_at_200]]). The base rate did not catch that; a per-period coverage map did, immediately. **Two checks, two defect classes: base rate for the predicate, coverage map for the data.**

Related: [[finding_sustain_count_role_discriminating_power]] (a trigger needs a stated role — test what it can and cannot catch) · [[finding_perturb_inputs_to_test_base_rate]] (correcting inputs at source) · [[finding_test_the_guard_not_just_the_guarded]] · [[finding_loadbearing_number_must_be_reproducible]].
