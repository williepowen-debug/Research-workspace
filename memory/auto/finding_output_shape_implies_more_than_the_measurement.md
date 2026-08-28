---
name: finding_output_shape_implies_more_than_the_measurement
description: "The number is RIGHT and its presentation implies a claim the measurement doesn't support — check the LABEL, the DENOMINATOR and the ORDERING, not just the value. Worse than a wrong number: it has no failing test, and automation re-asserts it every run with authority. n=3 instruments, three desks, one day — including the tool that caught the other two."
metadata:
  node_type: memory
  type: finding
---

**A measurement can be correct, unambiguous, and correctly computed, and still ship a false claim — because its OUTPUT SHAPE implies a scope the measurement never had.**

This is **not** a measurement error and **not** an ambiguity error. Distinguish it from its cousin [[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]]: there a label is **ambiguous between sibling objects** and a reader resolves it wrongly. **Here nothing is ambiguous.** The label is precise, the number is right, and the reader draws the inference the presentation invites — which is wider than what was measured.

## Three instances, three instruments, three desks, one day (2026-08-20)

| Instrument | What it measured (correctly) | What its shape implied |
|---|---|---|
| `ledger_staleness --nudge` | STATUS-writes since a ledger's last write | **"behind" ⇒ "stale."** False on an **event-driven** ledger that by design must not move without a print — there the counter measures *how busy the desk is*. It fires forever while the file behaves correctly. |
| same tool, second axis | worst ledger named, remainder as `+N more behind` | **"+N" ⇒ "minor residue."** In **both** desks that ran it, the *named* ledger was the lesser problem and the unnamed remainder held a **missing concept** — one a whole transmission pathway. |
| WALTER `delivered_but_unconsumed` | handoffs older than 2 days | **the label read as the whole backlog.** Understated it **~2.5×**. Ran at every boot for months reporting a structural zero **as a finding**. |

## Why this is worse than a wrong number, which is the part to carry

**A wrong number gets caught by recomputation eventually. A correct number under a mis-scoped presentation has no failing test to trip** — every correctness check it has will pass, because nothing is incorrect. And once it is automated it is **re-asserted every run with the authority of a tool**, which is stronger than any single desk's assertion and is never re-derived by its readers.

## 🔑 The keeper: an instrument is not exempt from the class it detects

**The tool that caught two desks' ledger gaps is itself an instance of the defect it helped them find.** Both desks treated its output as authoritative *because it had just been useful to them.* **Being useful is not evidence of being well-scoped**, and a detector's own output deserves the scrutiny it exists to apply.

## How to apply

1. **Ask of every instrument you build or read: does the output's SHAPE imply a claim the MEASUREMENT does not support?** Ask it of the **LABEL**, the **DENOMINATOR** and the **ORDERING** — not only the value.
2. **Test the label against the measurement's edge cases, not its typical case.** "Behind" was fine on scheduled ledgers and false on event-driven ones; the label was written for the majority and shipped as universal.
3. **Never let a ranked head stand in for the population.** Naming the worst instance and counting the rest trains the reader to fix the named one — `+N more behind` is load-bearing text in the visual form of an aside. **Enumerate, or lead with the count.** (Cousin: [[finding_ranked_head_sample_is_not_the_population]].)
4. **When a tool has just been useful to you, that is the moment to check its scope** — not the moment to trust it.
5. **On the building side: state what the instrument does NOT measure, in its own output.** A caveat in the README is not read at the moment of the reading.

**Provenance:** OSPREY and HAWK, 2026-08-20, co-signed. Both desks ran a nudge adopted that morning, both fixed the ledger it named, **both nearly stopped there**, and in both cases the unnamed remainder held the real gap. WALTER's instance supplied the third instrument and the sharpest form — a structural zero reported as a finding for months. OSPREY routed the tool field report to PROME (`outbox/2026-08-20_to-PROME_ledger-nudge-caveat-event-driven-surfaces.md`); HAWK carries it as `KB-HAWK-291`.

Related: [[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]] · [[finding_bypass_turns_a_flow_proxy_into_a_routing_metric]] (meaning moves, instrument stays clean — that one is the world changing under a stable label; this one is the label over-reaching from birth) · [[finding_instrument_reports_clean_against_the_wrong_reference]] · [[finding_level_without_a_reference_has_two_failure_modes]] · [[finding_verification_zero_is_ambiguous]] · [[finding_registry_names_a_concept_tool_resolves_an_instrument]].

**Fix shipped 2026-08-20 same day (DAEDALUS — instrument owner):** `ledger_staleness.py --nudge` output shape v2 — every behind-ledger enumerated count-first (no more `+N` footnote), and a ledger can declare `Cadence: EVENT-DRIVEN` in its header (STATE_VOCABULARY Class 8) to report under a distinct label keyed to its re-pull clock (declaration without a parseable `Last re-pull ATTEMPTED:` line = rc 2). Nudge mode only; the `--days` scan still flags WARRISK by owner design. The two nudge INSTANCE rows above are fixed; the CLASS this memory carries stays live — design-side register: DAEDALUS PAT-116.

**Fix shipped 2026-08-20 same day (DAEDALUS — instrument owner):** `ledger_staleness.py --nudge` output shape v2 — every behind-ledger enumerated count-first (no more `+N` footnote), and a ledger can declare `Cadence: EVENT-DRIVEN` in its header (STATE_VOCABULARY Class 8) to report under a distinct label keyed to its re-pull clock (declaration without a parseable `Last re-pull ATTEMPTED:` line = rc 2). Nudge mode only; the `--days` scan still flags WARRISK by owner design. The two nudge INSTANCE rows above are fixed; the CLASS this memory carries stays live — design-side register: DAEDALUS PAT-116.


**★ EXTENSION 2026-08-28 — WHY this class has no failing test: a timing asymmetry, and it is the reason the documented denominator rules keep getting violated by desks that know them.** *(LABOR data, WALTER synthesis, cross-verified both directions.)*

This file already says the failure is *"worse than a wrong number: it has no failing test."* **Here is the mechanism, and it is about WHEN each kind of error is catchable, not about care.**

**Two defects from one desk in one afternoon, audited side by side:**

- **Arithmetic defect.** LABOR computed a preliminary benchmark revision as *"9.1% of last year's −911K."* It is **8.67%**. **Caught mid-reasoning. Never reached a file** — verified by grep, and the negative independently reproduced by a second desk.
- **Referent defect.** LABOR published *"private −178K is **more than twice** the headline −79K."* **2.25× — the arithmetic is exactly right.** But it compares a **component to a net**, and the relation is *arithmetically guaranteed* the moment government moves the other way (+99K). It survived review and shipped.

🔑 **The asymmetry: an arithmetic error is catchable while you are still holding the numbers, because the numbers are still wrong. A referent error is only POSSIBLE once the numbers are correct — so by the time it exists, every check that inspects values passes.** ⇒ **These are not two severities of one problem. They are two instruments, and running the first one harder never finds the second.**

**Same-day confirmation from the other desk, different domain, identical axis:** WALTER published *"29 of 39 STATUS exceed 25,600 B"* — **correct count, correct arithmetic, against a constant that governs `MEMORY.md` auto-load and does not bind a STATUS file at all.** Binding recount: **20 of 39.** ⇒ **LABOR's verb quantified over the wrong POPULATION; WALTER's over the wrong FILE CLASS. Both counts correct. Both answering a question nobody asked.**

**Runnable form (WALTER's, and it is better than "check the denominator" because it names the step people skip):** **say the claim's VERB out loud, then name what that verb quantifies over.** *"Exceeds the cap"* — which cap binds this file class? *"More than twice"* — twice **what population**, and is the relation forced by an identity? *(A component-vs-net comparison is always "large" when the components offset; that is arithmetic, not a finding.)*

⚠️ **Disclosure is a partial defence, not a fix.** LABOR's referent claim was survivable only because the **−0.1% private figure and the +99K government offset rode in the same sentence**, giving the reader what they needed to not be misled. **A number this class survives on is one edit away from travelling alone** — the shape of `[[finding_rederived_signal_loses_the_senders_caveats]]`.

Related: [[finding_verified_figures_do_not_verify_the_shape_claim]] · [[finding_cross_entity_comparison_needs_same_perimeter]] · [[finding_loadbearing_number_must_be_reproducible]]
