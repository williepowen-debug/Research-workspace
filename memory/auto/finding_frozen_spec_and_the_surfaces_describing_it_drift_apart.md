---
name: finding_frozen_spec_and_the_surfaces_describing_it_drift_apart
description: "A frozen spec cannot go stale, but the surfaces that DESCRIBE it can — and the surfaces are what a session actually reads at grade time, so the drift is executed, not noticed"
symptoms: "grading off what STATUS says the test is; 'the letter says X but my notes say Y'; a dated adjudicator that turns out not to be a leg; carrying a dead instrument for days; three surfaces agree with each other and disagree with the spec; the pre-registration was fine and the grade was still wrong"
metadata:
  type: feedback
---

A pre-registration is frozen precisely so it cannot drift. **The surfaces that point at it are not frozen, and they drift — toward what the desk expects the test to be.** At grade time the session reads its STATUS row, its MEMORY handoff and its sub-agent state, not the sealed letter. **So the drift is not noticed, it is EXECUTED.**

Measured instance (SAM, 2026-09-01, caught two days before the grade). The frozen letter's auction leg was *"the 8/20 20Y auction"*, which had graded AMBIGUOUS — making **both directional branches unreachable from 8/20 onward.** Meanwhile `STATUS.md`, `MEMORY.md` and `METSUKE_MEMORY.md` all described the 9/3 adjudicator as *"the 30Y auction + slope."* **The letter contained no 30Y leg at all.** Three surfaces agreed with each other and disagreed with the spec; the instrument had been dead for twelve days and was still on the books as live.

**Why this is worse than an ordinary stale doc:** grading the 30Y into that test would have looked like *running the frozen letter* while actually re-tuning it — the failure wears the costume of the discipline that prevents it.

**How to catch it:**
- **Before any grade, re-read the SEALED LETTER itself and diff it against the surfaces that describe it.** Do this *before* the print, when the answer cannot yet be motivated. The check is cheap and it is the only one that works.
- **After the grade, ask what the test could still return.** An adjudicator whose branches are already unreachable is not "pending", it is finished — and a modal NO-VERDICT branch is exactly the shape that hides this, because a null looks like the instrument working.
- **When the spec is internally ambiguous, rule the DEFINITION, never re-tune the bar** — and only trust your ruling if the alternative reading returns the SAME verdict. If the ruling changes the outcome, you are selecting, not disambiguating. Say so and escalate.
- **Name the failure class correctly.** "Unreachable by construction" is neither *weak discriminator* nor *out-of-universe driver*, and it must not be counted toward a retire-the-instrument clause: retiring for low power when the fault was wiring destroys the evidence about what actually broke.

Related: [[finding_prereg_branch_label_can_contradict_its_condition]] (label vs condition INSIDE the letter — this one is the letter vs its DESCRIPTIONS) · [[finding_a_ruling_governs_the_next_write_not_the_existing_state]] · [[finding_option_menu_omitting_the_owners_choice_reads_as_silence]] · [[finding_banded_threshold_with_no_metric_surface_is_untrippable]] · [[finding_record_of_an_action_is_not_the_action]]

---

**n+1 (2026-09-02, MIDAS) — THE REGISTRATION SPLIT: the sharp version went to the COUNTERPARTY, the vague one stayed on the author's own book, and the grader read the book.**

**What happened.** MIDAS sharpened a discriminator on 8/23 and wrote the sharp version into its **outbound packet** to ZHAO: *"the discriminator now watches the **construction sub-index** against copper, not just the composite; a second record-low construction print with copper still firm is materially stronger evidence."* Its own ledger row (`KB-051`), written the **same day**, recorded only the weaker *"second sub-50 **composite**."*

**At grade time ten days later it read its own book**, graded the composite — which was *rebounding* — and published a deduction **against itself**: *"strengthens less than my spec's language implies."* **The construction leg had in fact printed a new record low with copper firm: the registered condition FIRED and the desk missed it.** ZHAO quoted the registration back, and MIDAS verified it verbatim in its own outbound packet before accepting.

⭐ **The mirror-image pairing is what makes this worth banking.** Six days earlier BOND **wrote a packet and never delivered it** (finding lived only in the author's outbox; the reader never saw it). Here a desk **delivered a packet and never recorded it at home** (registration lived only in the recipient's inbox; the *grader* never saw it). **Same class, opposite direction: the spec ends up on exactly one surface, and it is not the surface consulted when it matters.**

**Why it is easy to commit — and this is the non-obvious part.** Writing the sharper version *to a counterparty* **feels like the more rigorous act**, because you are exposing the spec to someone who can attack it. It *is* rigorous. That is exactly why the effort lands there and not in the ledger row: **the upgrade felt registered because it had an audience.**

**How to apply:**
- **A spec is not registered until it sits on the surface the GRADER reads.** Sharpen a spec inside outbound correspondence and the same edit goes to the ledger row **in the same commit**, or the packet is a letter *about* a registration, not one.
- **At grade time, grep your own outbox for the spec's subject before grading.** The counterparty may be holding a sharper letter than your book does.
- ⚠️ **The diagnostic is shared with a very different failure.** "A peer quotes your spec back and you cannot find it on your surfaces" is *also* the signature of a misattribution ([[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]). **The check is identical either way — go find it in your own record** — and only the search distinguishes "they invented it" from "I failed to record it." Both occurred on the same desk on the same day, resolving opposite ways.
