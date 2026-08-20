---
name: finding_banded_threshold_with_no_metric_surface_is_untrippable
description: "A registry row and a dashboard vector are two different instruments — a threshold that exists in only one of them is ungradeable in practice however correctly it is written, and it passes every audit that counts rows"
metadata:
  node_type: memory
  type: finding
---

A threshold can be **fully specified, correctly frozen, properly routed, and structurally impossible to trip.** The failure is not in the rule; it is that **no surface a session actually reads carries the rule's metric**, so the number arrives, gets written down, and is never compared to its own band.

**Worked case (CREED, 2026-08-20).** `CREED-T-02` = *matured-balloon share of new CMBS delinquencies > 50, sustain 2 monthly prints* — a clean numeric band, Will-frozen, transcribed into a machine-readable registry with a recipient chain.

On **2026-08-13** the desk pulled the monthly print and wrote **"66% of $6.0B newly delinquent"** into its history ledger, into another vector's notes, and into its status file. **That is the trigger's metric, against a band of 50, written down three times by the desk that owns the trigger — and never graded.** The condition had by then been satisfied for **six weeks** (met at the June print; discovered 8/20).

**Root cause:** of 31 dashboard vectors, **none carried that metric.** It was the only numerically-banded trigger in the registry with no vector. The number had nowhere to land except **free-text prose inside a different vector's notes — and prose is not graded against bands.**

**The registry file's own header proudly declared "THIS FILE MOVES NOTHING."** Accurate, and that was the defect: transcription without a corresponding metric surface produces a trigger nobody can trip.

**Why it survives audits:** a *prose* gate is visibly unscannable, so nobody trusts it. **A registry row with no metric vector looks fully instrumented.** It has an id, an operator, a value, a sustain window, a recipient chain. Every check that counts rows, validates fields, or greps for bands returns clean. Cf. [[finding_instrument_reports_clean_against_the_wrong_reference]] and [[finding_guard_correctness_and_wiring_are_independent]] — ask "if this fires, what stops?"; here, nothing could fire.

**A second instance surfaced the same session, found by a different instrument.** A closeout `consumer_check --self` caught a transmission-chain row sitting at `ARMED` while its *own* trigger field read, verbatim, the same condition. **Three surfaces carried one condition and exactly one was ever checked** — and the fire adjudication did not find that; a mechanical scan did.

**How to apply:**
1. **For every banded threshold, name the metric surface that carries its value** — a vector, a series, a ledger column. If the metric appears only in free text, the threshold is undetectable, not merely under-instrumented.
2. **Cheap detector:** for each registry row with a numeric band, assert a named vector/series exists carrying that metric; flag rows whose metric appears **only** in prose. In the worked case this would have fired the day the registry was built.
3. **When you write ANY number into a workbook, check it against the threshold registry in the same action.** A boot-time scan of predictions is not a scan of thresholds — those are different lists, and having one invites the belief you have both.
4. **Count surfaces, not rows.** Ask how many places state a condition and how many are actually read. One condition on three surfaces with one reader is a latent six-week miss.
5. **Record the detection lag as its own field** when a late fire is logged. Collapsing "when the band was met" into "when we noticed" erases the only evidence the defect existed.

Related: [[finding_record_of_an_action_is_not_the_action]] · [[finding_registry_names_a_concept_tool_resolves_an_instrument]] · [[finding_registered_gate_captures_attention]].
