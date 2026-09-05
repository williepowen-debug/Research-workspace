---
name: finding_ambiguous_coordinator_instruction_mints_a_propagating_event
description: "An ambiguous coordinator instruction (a re-date, a relayed deadline) can be read as a concrete EVENT and propagate across many downstream surfaces that then agree with each other. Cross-file agreement is NOT verification — the consistency is inherited from the single bad source, not independently confirmed. PROME re-dated a done-event DOCKET row to a future date on a verifier note that meant an INTERNAL sitting, minting a fake earnings print that spread to 5 CARL surfaces. Codex 2026-09-05."
metadata:
  node_type: memory
  type: feedback
symptoms: "re-dated a row and it became a fake event · an internal deadline read as an external print · the same event appears consistently across calendar/STATUS/ROADMAP/catalysts · cross-file agreement mistaken for verification · a verifier note meant X, the coordinator wrote Y · propagated instruction · fabricated catalyst"
---

**A coordinator instruction that is ambiguous about EVENT-TYPE gets resolved by each downstream reader the same wrong way, and then all the surfaces agree — which reads as confirmation and is not.** The agreement is inherited from the single bad source; nobody re-checked the primary.

**Concrete (PROME, 2026-09-05):** a verification note said a metric "grades at the **V2 registration sitting ≤9/10**" — an INTERNAL table-registration deadline. PROME re-dated a compound DOCKET row whose anchor event ("CVNA Q2 earnings") had **already happened on 7/29 and been graded** — moving its date to 9/10 and keeping the "earnings" description. That minted a fabricated "9/10 CVNA Q2 earnings" print. The desk consuming the instruction propagated it into its **calendar, catalyst ledger, STATUS, ROADMAP and NEXUS brief** — five mutually-consistent surfaces, all wrong, all traceable to one re-date. The row's OWN notes already said the earnings were graded 7/31; the re-date ignored them.

**Why it's dangerous:** the failure is invisible to every consistency check (`docket_view` still passed, cross-file agreement was perfect) because consistency is exactly what propagation produces. A fabricated event survives precisely because it looks agreed-upon. `[[finding_crosscheck_with_free_parameter_validates_nothing]]` — N copies of one source is one source.

**How to apply (as the coordinator):**
- **A re-date of a row anchored on a PAST, already-graded event is almost always wrong** — the event doesn't recur just because a downstream deadline is near. Read the row's own notes before re-dating; if it says "already graded," the forward work needs a NEW row, not a moved date.
- **Distinguish an internal DEADLINE (a sitting, a registration) from an external EVENT (a print, an earnings call).** "Grades by <date>" ≠ "an event occurs on <date>." Name which in the instruction.
- **When you relay a date, name the event TYPE and its primary** so a reader can't resolve the ambiguity into a fake catalyst.
- Verifying a coordinator edit means checking the PRIMARY (did this event happen? when?), never that the downstream surfaces agree — they will agree by construction. `[[finding_directive_overtaken_between_authorship_and_delivery]]` · `[[finding_dormant_instrument_is_a_query_plus_unexercised_reading_rules]]`
