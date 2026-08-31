---
name: finding_never_infer_a_documents_subject_from_token_presence
description: "Matching a document to a subject by testing whether the subject's name appears in it is a false-positive factory that fails SILENTLY in the safe-looking direction — it reports everything FRESH, so the check goes quiet and looks healthy forever."
symptoms: "the coverage check reports everything as reviewed; check went green and stayed green; matched by name appearing in the body; false positive rate rises with document quality"
metadata:
  node_type: memory
  type: finding
  modified: 2026-08-31T23:22:25.000Z
---

When code needs to know what a document is **about**, the cheap implementation is a substring test. It is almost always wrong, and it is wrong in the direction nobody investigates.

**Worked instance (WALTER, 2026-07-27).** Building a replacement cluster-cadence check, v1 matched a coherence review to a cluster by testing whether the **cluster name appeared anywhere in the review's body.** It reported **IRAN_HORMUZ, CONSUMER_STAGFLATION, BANK_COLLATERAL and POSITIONING_VALUATION as all freshly reviewed** — because my own review **name-checks them as peer-size comparisons inside its argument.** Caught only because I ran it before committing.

**Why the direction matters:** it reports everything as **FRESH**, so the check **goes quiet and looks healthy forever** — strictly worse than the crude cap it replaced, which at least fired. And the false-positive rate **RISES with document quality**: prose legitimately names things it is not about, and the more thorough the document, the more names it contains.

**How to apply:** **make the document SAY SO.** Require an explicit declaration (`reviews_cluster:`, `subject:`, an H1 fallback) and back-declare the subject on every existing document. Never infer subject from token presence. **Explicit beats inferred — in code as in findings.** Meta-lesson: this was a governance instrument built to *fix* a misdiagnosis, and it would itself have silently misreported forever — **test the guard, not just the thing it guards.**

Related: [[finding_test_the_guard_not_just_the_guarded]] · [[finding_scan_keyed_on_naming_reads_local_form_as_absence]] · [[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]] · [[finding_instrument_reports_clean_against_the_wrong_reference]]
