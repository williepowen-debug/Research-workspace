---
name: finding_negative_reachability_is_a_claim_about_your_request
description: A source reported UNREACHABLE is a claim about the request you made, not about the source, until host AND scheme have been varied — and the tool may rewrite your request without saying so.
symptoms: "source is unreachable" · "the primary is down" · "WebFetch returned nothing" · "timed out, marking it SEARCH-NOT-FOUND" · a clean-looking probe behind a negative result · "we can't reach that government site"
metadata:
  type: feedback
---

**A negative reachability result is a claim about YOUR REQUEST until host and scheme have been varied.** Not about the source.

HAWK, 2026-09-19, testing a Monday primary four days early: `https://publication.pravo.gov.ru` timed out and its first probe reported **unreachable**. That was **false**. Plain `http://` works — and **WebFetch upgrades HTTP→HTTPS by design**, so the tool silently rewrote the request into the one that fails and reported the failure as the source's. A second batch of hosts and schemes disagreed with the first; stopping at the first would have shipped *"two of three primary classes unreachable"* behind a probe that looked clean.

**Why:** the failing component is between you and the source, and it does not announce itself. The probe returns a real, correctly-formatted negative, so nothing downstream has a reason to doubt it — the same shape as [[finding_instrument_reports_clean_against_the_wrong_reference]] and [[finding_scan_keyed_on_naming_reads_local_form_as_absence]]. An absence produced by your own transport is indistinguishable from an absence in the world, and it is the one an analyst is most likely to bank. It is also how SEARCH-NOT-FOUND gets wrongly upgraded to VERIFIED.

**How to apply:** before recording any source as unreachable, vary **host** and **scheme** and run a second batch — and say in the record which variations were tried. One probe supports "my request failed", never "the source is down". If a fetch tool may rewrite the request (scheme upgrade, redirect following, UA filtering), name the tool in the finding, because the next reader's tool may rewrite it differently: ZHAO's NY Fed pull succeeded on the first try only once the request carried a browser User-Agent. When a dated grade depends on reaching a primary, **test the reachability BEFORE the date, not on it** — HAWK's test was four days early, which is the only reason there is time to switch to `curl` for Monday.

⚠️ The credit belongs to widening the test, not to noticing the result — HAWK said so itself when PROME praised the finding instead of the method. Related: [[finding_declared_data_wall_needs_fleet_memory_check]] (at 3 identical negatives the finding is ACCESS, not data) and [[finding_a_named_unchecked_fallback_makes_an_absence_closable]].
