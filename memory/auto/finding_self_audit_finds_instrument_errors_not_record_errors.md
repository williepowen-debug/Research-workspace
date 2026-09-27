---
name: finding_self_audit_finds_instrument_errors_not_record_errors
description: "A self-audit and a peer review pose DIFFERENT questions, so they catch different classes — a scope fact, not a verdict on worth. An author's own 'did my edits LAND' check (mechanical / edit-landing) answers that reliably but CANNOT surface reasoning/record defects, because it never poses 'does the conclusion follow from the source' — and the author reads the survivor as covered. Peer review poses that second question. So don't build a self-audit helper to catch your own REASONING errors; make peer review cheaper for those. (A mechanical literal-string helper is a different thing and is fine.)"
symptoms: "my self-audit found N/N complete; I reviewed my own claims and they check out; I swept my own file; the correction pass is done; I re-read what I wrote and it's fine; self-scoped audit reported as a completeness figure; a self-audit helper; automate the closeout self-check; I graded my own record; 25/25 clean; I already checked that"
metadata:
  node_type: memory
  type: feedback
---

**A self-audit and a peer review pose DIFFERENT questions.** An author's own audit is reliable at *"did my edits LAND"* (INSTRUMENT / edit-landing — a mechanical check); it does not surface REASONING/RECORD defects, because it never poses *"does the conclusion follow from the source"* — and the author reads the survivor as covered. Peer review poses that second question. They are not substitutes: they catch different classes. **This is a scope fact, not a verdict on the worth of self-audit** (CATO's correction, relayed by CRUISE 2026-09-21 — the earlier "near-worthless" framing overclaimed).

TERRY ⇄ CRUISE, 2026-09-20, one exchange, both desks measured it rather than asserting it. ⚠️ **The table compares two instruments on two DIFFERENT tasks with different denominators — read the SHAPE, not a head-to-head score:** the self-audits asked "did the edit land" and answered it correctly every time; the ~20 were reasoning defects those self-audits never posed.

| instrument | own REASONING/record defects found | own edit-landing defects found |
|---|---:|---:|
| **SELF-AUDIT** (each desk, "did my edits land") | **0** *(never posed the question)* | **4** |
| **PEER REVIEW** ("does the conclusion follow") | **~20** | — |

**Every record defect corrected that day was found by someone who did not write the record** — a load-bearing inference, an invented numeric bound, a false superlative, a share-count vintage error, nine naked withdrawn claims, a fix that reversed its own logic, a frozen pointer to a wrong worked example; on the other desk a partial strike, a stale count in a heading, and a commit message certifying an edit that never landed.

🔑 **The mechanism (CRUISE's, and it is the load-bearing sentence): the author knows what they meant, so they read the survivor as obviously covered.** The sharpest instance: TERRY saw a scope defect in its own 25-claim audit the *moment* CRUISE named it in their 8 — and CRUISE had not seen it in their own 8 until they read TERRY's 25. **Neither desk could see it in its own instrument; both saw it instantly in the other's.**

⇒ **The operational inference:** automating INTROSPECTION to catch your own REASONING errors is aimed at the question a self-audit never poses, so the honest lever for those is to **make peer review cheaper and more frequent** — a different kind of ask than a self-check tool.

**How to apply:**
- **Do not commission a self-audit helper to catch your own REASONING/record errors** — that class needs a reader who did not write it. ⚠️ **But this is NOT a refusal of a mechanical edit-landing helper:** a literal-string self-sweep (an exact retired phrase still stated as current) targets the class self-audit IS good at, and is fine — it just catches only that narrow subclass and will miss the same claim re-asserted in different words (titles, headings, paraphrases), which needs a reader. The two do not conflict though they read as if they might. `[[finding_a_correction_pass_is_unreviewed_work]]`
- **A self-scoped audit perimeter measures the author's MEMORY, not their record** — the party being audited must not draw the perimeter, or a `25/25` and an `8/8` are completeness theatre and not comparable.
- **If you must build any audit: falsify it first.** Every audit either desk wrote that day failed on its own first run, n=4 in one exchange. `[[finding_test_the_guard_not_just_the_guarded]]`
- **A count in a heading, a byte/crc/price/vintage** is a MUTABLE claim — it can be true when written and legitimately different now; it needs RE-DERIVATION, not a presence probe, and the exclusion must be stated. Claim type cannot be inferred from token shape (the same 8 hex chars are a crc32, a short SHA, or a report-filename suffix) — declare the type in the container.

- **Instance, DEWEY 2026-09-27 (Nano Banc).** DEWEY verified every load-bearing QUOTE against the downloaded filings, and caught a merged quote, a misfiled case ID, a guessed citation path and its own sum error. All of those are instrument/edit-class. It still shipped *"Ontario/Chino: STILL NANO … pass to the receiver"* from debtor filings dated **9/8–9/11 and 8/26**, i.e. a **dated observation extended into state at a later date (the 9/25 failure)**. Quote-checking never asks "does the date of the evidence reach the date of the claim?" Caught by an outside reviewer and by CATO via PROME, not by DEWEY. **Tell:** a state word ("still", "holds", "is") attached to an evidence date that precedes the claim date. Write "X per filing dated D", and name what would prove the later state.

Related: [[finding_a_correction_pass_is_unreviewed_work]], [[finding_a_charitable_reading_of_your_work_is_the_one_to_check]], [[finding_adoption_is_not_validation]], [[finding_asymmetric_rigor_counterparty_claims]].
