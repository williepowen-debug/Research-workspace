---
name: finding_crosscheck_with_free_parameter_validates_nothing
description: "An arithmetic/identity cross-check is only a test if it has ZERO unknowns; with a free parameter it back-solves and \"passes\" on any input — and two agreeing secondaries are one source, not confirmation."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a6915382-0f01-4c86-a253-590c75e1934b
  modified: 2026-08-05T14:27:28.086Z
---

A cross-check that **cannot fail is not evidence** — it is a ritual that manufactures confidence and launders a bad input into a "confirmed" tag.

**Incident (LABOR, 2026-08-05).** `ISM Services June employment` was carried as **47.4, "sub-50, 4th straight month contracting"** for a month, tagged `[CONF]`. The actual figure was **51.2 — an expansion, +3.3pp**: wrong in **sign**, not magnitude. The source tag was the whole failure: *"2 independent web reads + arithmetic cross-check (4 sub-indexes avg 54.0)."*

- **"Two independent web reads" is one source.** Secondary aggregators copy each other; agreement between two of them is one observation reported twice. No primary was ever opened.
- **The cross-check had two free parameters.** The ISM headline is the mean of four sub-indexes; only two were known correctly, so the check **back-solved the rest to fit**. True 51.2 → implies Supplier Deliveries 54.3. False 47.4 → implies 58.1. **Both "pass."**

**Why:** freshness gates, propagation sweeps (`consumer_check`), staleness alerts and format audits all test *whether a number moved or spread* — **none tests whether it was ever right.** A wrong-at-entry figure sails through every one of them indefinitely (see [[finding_freshness_check_cannot_catch_a_fresh_lie]]). Worse, a *plausible* wrong number that continues the current narrative is the least likely to be re-examined ([[finding_plausible_stale_value_evades_review]]). Cost here was not the digit: it was a month of the wrong story — the thaw this figure would have flagged in June was not noticed until a different sector's print in August.

**How to apply:**
1. **Count the unknowns before trusting an identity check.** Zero unknowns = a test. `n` unknowns = `n` degrees of freedom = no test. **If you cannot state what the check would have looked like had it FAILED, you did not run one** ([[finding_test_the_guard_not_just_the_guarded]]).
2. **Reserve "confirmed" tags for a NAMED PRIMARY** — the issuer's own release. Where only secondaries exist, tag it as such and say so. Most primaries (BLS, DOL, ISM, SEC, company 8-K) are one free fetch.
3. **For any recurring release you score a position or vector on, build a path to the primary** rather than re-deriving from aggregators each cycle.
4. **When correcting, separate the legs.** The claim here had a survey leg (false) and an independently-sourced filings leg (true). Retract the failed leg and state explicitly that the other survives — over-retraction is its own error ([[finding_verification_correction_downstream_propagation]]).

Related: [[feedback_pull_live_primary_not_dashboard]] · [[finding_loadbearing_number_must_be_reproducible]] · [[finding_verify_reader_before_source]]
