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
