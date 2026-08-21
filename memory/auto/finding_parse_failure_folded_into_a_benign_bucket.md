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

---

**Extension 2026-08-21 (VULCAN, S4 instrument build) — the sharper form: the parse failure can be CORRELATED WITH THE SIGNAL CLASS, making the instrument untrippable by construction.**

The base finding's failures were random with respect to content. VULCAN's were not: TSMC's 6-K writes negative months in **accounting parentheses — `(1.1)`, not `-1.1`** — so its revenue parser dropped 8 of 16 months, **every dropped month a DECLINE**, while writing 8 clean-looking "validated" rows under a success line. **S4's red band IS "decline" — the instrument could not, by construction, ever see the condition it existed to flag.** Not a degraded detector; a detector whose failure mode selects exactly the alert class, wearing a validation stamp.

**Added to how-to-apply:**
- **Ask whether your failure mode is INDEPENDENT of the signal.** A random 50% parse loss degrades an instrument; a loss correlated with the alert condition (negatives formatted differently, halted days missing from a feed, outage-days unlogged) **blinds it specifically to fires while it validates cleanly on quiet data**. Test with a known-positive from the alert class, not a random sample.
- **Grep-bait for one recurring cause:** financial primaries write negatives as `(x.x)` — any parser reading filings/IR tables must handle parenthesized negatives or it silently drops exactly the bad months. (VULCAN's fix re-pulled 20/20 clean; it also base-rated its new band before shipping — 50% fire-rate → tightened to 2-consecutive, 35% — per [[finding_base_rate_the_threshold_before_building_it]].)
