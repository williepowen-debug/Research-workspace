# Existing profile-clock checker — owner-relative comparison repair

Authority: Will 2026-11-02 “proceed with overdue/gaps now”; boot named HENRY and OSPREY comparisons CANNOT-EVALUATE. No new standing checker or profile trigger.

Acceptance before implementation:
1. Evaluate the existing STATUS-stamp-relative predicate against the named desk's STATUS.md header, preserving each profile's body vintage and strict >N-day operator. No wall-clock substitution, mtime or Git fallback.
2. Read only anchored Last owner update / Last Updated / As of declarations before the first content section. Exactly one distinct valid date; absent, malformed, conflicting, future or before-body dates return CANNOT-EVALUATE. No arbitrary date extraction from prose/history.
3. Ordinary wall-clock profiles unchanged. A relative day clause uses owner-stamp minus body date; a separately declared hard floor remains as-of-based. Print owner path/date and measured lead.
4. Add --owners-root for disposable deterministic tests; default repository AGENTS. Tests never depend on live production owners.
5. Frozen real profile evidence remains immutable. Check clean boundary 21d, alert 22d, missing/invalid/future/conflicting owner headers and body/owner chronology. Old unsupported form must fail the capable test before repair. Production run HENRY/OSPREY should classify FIRED, not healthy or refreshed. Tests must distinguish an erroneous wall-clock implementation.

REVIEW: REQUIRED — existing checker scope becomes able to evaluate a declared predicate; UPGRADE_PROTOCOL rule 4/4a. Before implementation a non-author verifies proposed parsing/consumer scope and states a counterexample; final changed code/tests receive a counterexample read. No changes to caller rc meanings, profile vintages, or completeness of content triggers.

## POST-REVIEW correction 1

Reader's final-result HOLD correctly found that initial parser stopped only at ## headings. Subsequent H1/Setext or fenced history could supply a false clean owner date. The corrected parser allows only an initial H1 document title, then stops at any ATX heading, Setext boundary, or code fence. Added regression exercises missing owner header and valid prior-header cases for all three forms. 17 focused tests pass. Final re-read remains owed; this correction is not folded into the prior reviewed version.

POST-REVIEW correction 2: independent recheck found valid short Setext underlines (`--`/`-`) remained in the same boundary class. Regex now accepts one-or-more dashes/equals, with one/two/seven-dash and one-equals cases in the existing regression. No other predicate/parser boundary changed. Final recheck owed; prior HOLD preserved.
