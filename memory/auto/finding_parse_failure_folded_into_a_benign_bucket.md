---
name: finding_parse_failure_folded_into_a_benign_bucket
description: A parse/fetch failure counted into a named benign category doesn't render as a missing reading — it manufactures a positive factual claim about documents nobody read.
metadata:
  type: feedback
---

An insider-buying detector printed, for 11 of 11 Form 4 filings: **"All routine (RSU settlements, tax withholdings, awards). No conviction signals."** It had parsed **zero** of them. The XML-link picker was returning EDGAR's *XSL-rendered HTML* view (`/xslF345X06/...`) instead of the raw XML, `ET.fromstring` raised on the doctype, the parser returned `None` — and the caller incremented `total_noise`, the **"Routine"** counter.

**This is a strictly worse failure than a silent zero.** A missing reading looks like nothing and invites a second look. A failure folded into a *substantive benign bucket* looks like **evidence**: it names a mechanism ("RSU settlements"), reports a count, and reads as a completed check. Nobody re-examines a detector that is confidently telling them everything is fine — least of all when its null state is load-bearing evidence FOR the position they already hold.

**How to apply:**
- **Never increment a substantive category from a failure path.** Failures get their own counter (`unparsed`, `fetch_failed`), and it prints in the default output line beside the real ones — `found | parsed | unparsed`, never folded.
- **The tell is a bucket that can only grow.** If every error path lands in the same "benign/other/routine" bin, that bin's count is not a measurement.
- **Verdicts must state coverage, not just outcome:** "no purchases across **3 of 3 names**, 25/25 fetched" — not "no purchases across any thesis name." A verdict certifies its scope, not your capability ([[finding_verification_zero_is_ambiguous]]).
- **Separating the counters is what surfaces the bug.** The broken parser was invisible for an unknown period; it became obvious the instant `Unparsed` printed as its own number. Splitting the counter *is* the diagnostic, not just the fix.
- **Then falsify it** — force the outage and confirm the clean verdict cannot print ([[finding_run_the_falsifier_before_promoting]]). A guard nobody has watched fail is an assumption.
- Related: [[finding_fail_loud_on_incomplete_data]] · [[finding_silent_blank_evades_review]] · [[finding_count_what_published_before_reading_the_verdict]] · [[finding_standing_guard_is_a_false_negative_risk]] · [[finding_registry_names_a_concept_tool_resolves_an_instrument]].
