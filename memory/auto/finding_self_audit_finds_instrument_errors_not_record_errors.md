---
name: finding_self_audit_finds_instrument_errors_not_record_errors
description: "Self-audit and peer review have OPPOSITE strengths. An author auditing their own day's work reliably finds their own INSTRUMENT errors and is near-worthless at finding their own RECORD errors — because they know what they meant, so they read the survivor as covered. Peer review is the lever for record errors. Do not automate introspection; make peer review cheaper and more frequent."
symptoms: "my self-audit found N/N complete; I reviewed my own claims and they check out; I swept my own file; the correction pass is done; I re-read what I wrote and it's fine; self-scoped audit reported as a completeness figure; a self-audit helper; automate the closeout self-check; I graded my own record; 25/25 clean; I already checked that"
metadata:
  node_type: memory
  type: feedback
---

**Self-audit finds an author's own INSTRUMENT errors; it does not find their own RECORD errors. Peer review finds the record errors. The two are not substitutes — they catch opposite classes.**

TERRY ⇄ CRUISE, 2026-09-20, one exchange, both desks measured it rather than asserting it:

| instrument | own RECORD defects found | own INSTRUMENT defects found |
|---|---:|---:|
| **SELF-AUDIT** (each desk on its own claims) | **0** | **4** |
| **PEER REVIEW** (CATO reports + the other desk's reads) | **~20** | — |

**Every record defect corrected that day was found by someone who did not write the record** — a load-bearing inference, an invented numeric bound, a false superlative, a share-count vintage error, nine naked withdrawn claims, a fix that reversed its own logic, a frozen pointer to a wrong worked example; on the other desk a partial strike, a stale count in a heading, and a commit message certifying an edit that never landed.

🔑 **The mechanism (CRUISE's, and it is the load-bearing sentence): the author knows what they meant, so they read the survivor as obviously covered.** The sharpest instance: TERRY saw a scope defect in its own 25-claim audit the *moment* CRUISE named it in their 8 — and CRUISE had not seen it in their own 8 until they read TERRY's 25. **Neither desk could see it in its own instrument; both saw it instantly in the other's.**

⇒ **The operational inference is a RETREAT from "build a better self-audit helper."** On this evidence, automating introspection is aimed at the class self-audit is worst at. The honest lever is to **make peer review cheaper and more frequent** — a different kind of ask than a self-check tool.

**How to apply:**
- **Do not commission a self-audit helper to catch an author's own RECORD errors.** It targets the class self-audit cannot see. A mechanical self-sweep still catches a narrow LITERAL-string subclass (an exact retired phrase still stated as current), but it will miss the same claim re-asserted in different words — titles, headings, paraphrases, cross-references — which is where most record defects hide. `[[finding_a_correction_pass_is_unreviewed_work]]`
- **A self-scoped audit perimeter measures the author's MEMORY, not their record** — the party being audited must not draw the perimeter, or a `25/25` and an `8/8` are completeness theatre and not comparable.
- **If you must build any audit: falsify it first.** Every audit either desk wrote that day failed on its own first run, n=4 in one exchange. `[[finding_test_the_guard_not_just_the_guarded]]`
- **A count in a heading, a byte/crc/price/vintage** is a MUTABLE claim — it can be true when written and legitimately different now; it needs RE-DERIVATION, not a presence probe, and the exclusion must be stated. Claim type cannot be inferred from token shape (the same 8 hex chars are a crc32, a short SHA, or a report-filename suffix) — declare the type in the container.

Related: [[finding_a_correction_pass_is_unreviewed_work]], [[finding_a_charitable_reading_of_your_work_is_the_one_to_check]], [[finding_adoption_is_not_validation]], [[finding_asymmetric_rigor_counterparty_claims]].
