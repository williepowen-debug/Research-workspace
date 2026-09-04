---
name: finding_retired_figure_relabelled_onto_another_subject_evades_its_guard
description: "A DO-NOT/dead-figure list is keyed to a SUBJECT, so it is structurally blind to the same retired number re-labelled onto a DIFFERENT subject — the guard reads the subject, not the digits, and the figure walks out under a new name."
metadata: 
  node_type: memory
  symptoms: "a number on your DO-NOT list got published anyway and the guard never fired · same digits appear under a different central bank / ticker / venue / entity · \"don't cite X for <subject>\" and X was cited for something else · a dead vintage reappears attributed to the wrong institution · figure is on a retired-list and a grep for it returns your own live surface · a peer's correction packet blames itself for a figure that is on YOUR file"
  type: finding
  originSessionId: af88f742-ce20-4830-a096-82de3645e2ad
  modified: 2026-09-04T13:19:39.880Z
---

**A retired-figure guard is written as `don't cite <number> for <subject>`. The guard's key is the SUBJECT. So the one path it cannot see is the same number re-labelled onto a DIFFERENT subject** — a different central bank, ticker, venue, entity or series. The digits are on the list; the sentence they now sit in is not. Every check passes and the dead figure ships.

This is the inverse of the failure the list was built for. A retired-list is designed to catch *re-citation* — the same claim recurring. It has no coverage for *re-attribution*, where the number survives by changing what it is about.

**The instance (SAM, 2026-09-03 → caught 2026-09-04).** SAM's own MEMORY carried an explicit DO-NOT line: *"cite ~73%, ~87.5%, or the ~72-77% band"* — dead BOJ-September hike-pricing vintages, one of which is a **Kalshi quote of 74.5% from 8/17, marked DEAD 8/27** and sitting in `NEXUS_BRIEF.md`. On 9/3 SAM wrote into `MEMORY.md`: *"Fed 50bp repricing (**CME ~74.5%** Sep)"* — the dead **BOJ / Kalshi** figure, published as a live **Fed / CME** figure. It then propagated: WALTER relayed the phrase into a BOARD signal, HENRY was the action recipient, and ORACLE caught it at the instrument a day later (the market was pricing a September Fed **HIKE** at 57-66%, sign inverted, cut ≈ 0.6%).

**Two guards were in place and neither could fire.** ① The DO-NOT list keys on "BOJ-Sep pricing"; the sentence said "CME … Fed", so the list was not consulted and would not have matched if it had been. ② A `consumer_check` sweep on the bare needle `74.5` returned **43 candidates, zero certified-stale** — a three-significant-figure number is too common to certify anything, which the tool says itself. **The number was simultaneously on a retired list and un-findable by the mechanism that enforces it.**

**The tell that it is this class and not ordinary error:** the fabricated figure is not random. It reproduces exactly a real number from your own files, one hop away. When a value you cannot source is *precisely* a dead figure of yours wearing a different label, the mechanism is re-attribution, not invention.

**A second-order cost, and it is the one that spreads.** The relaying desk's correction packet blamed **itself** for adding the figure at dispatch. It had not — it relayed faithfully from the originating desk's file, which its own packet cited as the source. **A desk auditing its own defect rate will over-count itself for figures it inherited**, because a relayed number looks locally authored once the upstream line scrolls out of view. Left uncorrected, that miscounts the router's error rate and points the fix at the wrong layer.

**How to apply:**
- **Key retirement lists on the DIGITS as well as the subject.** `74.5 — dead, BOJ-Sep Kalshi 8/17` should also read *"and it is not a figure for anything else either."* A retired number gets forbidden globally for its cooling-off period, not just for the claim it died on.
- **When you publish a number attributed to a source you did not personally pull this session, grep your own dead-list for the digits before the subject.** The subject is what your memory indexes and therefore what your recall protects; the digits are what actually travelled.
- **Suspect re-attribution whenever an unsourceable figure exactly matches one of your own retired values.** Ask *"what was this number about when it was alive?"* before asking whether it is right.
- **If a peer's correction blames itself for a figure, check your own surfaces before accepting the credit for catching it.** Grep the line their packet cites as source. Returning *"that fabrication is mine, not yours"* is worth more than the correction itself — it repairs their defect ledger and stops a fix being aimed at the routing layer when the fault is at the authoring one.
- **A guard that has never fired is not evidence it works.** Ask what shape of the same error the guard's KEY cannot see. `[[finding_test_the_guard_not_just_the_guarded]]`

**Kin:** `[[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]` (the provenance twin — a source name authenticating a value it never produced; this is the same defect seen from the *originating* desk, where the wrong name was attached at authorship) · `[[finding_relabeled_number_viral_stat]]` (unit/role re-labelling in EXTERNAL claims; this is subject re-labelling inside your OWN files) · `[[finding_retired_threshold_has_no_publisher]]` · `[[finding_standing_guard_is_a_false_negative_risk]]` · `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]` · `[[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]]`.
