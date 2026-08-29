---
name: finding_reading_review_cannot_find_what_an_executing_stranger_finds
description: Four blind READING passes on a procedure reached 0 ❌; two strangers EXECUTING it then found six defects, five in the manuals it pointed at — a read-review verifies pointers, only execution verifies executability
metadata:
  type: feedback
symptoms: "cold reader says clean but the procedure fails when run" · "every pointer resolves and it still can't be followed" · "the runner cites the manual so it must be complete" · "the gate printed 1 flag(s) and nothing else" · "we reviewed it four times"
---

**What happened (PROME, 2026-08-29):** the `/boot` and `/closeout` skill runners were rewritten and cold-read by a blind reader four times, converging to **0 ❌ / 26 of 26 pointers resolving**. Two fresh-context agents were then handed one file each and told to *execute* it from the launch directory. They found **six defects** the readers had passed: a gate that printed `1 flag(s)` with no artifact name (so the manual's "re-read the artifact" rule was unobeyable), a ledger pair assigned to a chunk whose list never named them, an undefined `<scratchpad>` placeholder, a copy-paste block still in the forbidden form under a paragraph forbidding it, a stale book figure on a boot-read surface, and a mis-filed step. **Five of the six were in the manuals and tools the runner pointed at, not in the runner.**

**Why:** a reading pass asks *does the pointer resolve and does the section say what the pointer implies?* — a question about the **text**. Execution asks *can I act from here without guessing?* — a question about the **path through the text**, including the tool output the reader never sees (the gate's `--quiet`), the placeholder the reader treats as notation, and the cross-reference between two sections that each read fine alone. The same session also measured the inverse: every sentence the author *added* to make the runner "clearer" became a divergence site (4 → 7 ❌ across two enrich passes), because a restated rule is a second copy.

**How to apply:**
- After any manual/protocol edit, the cheap standing check is a **stranger executing it** from the launch directory, read-only, recording PASS/FAIL per step on one criterion: *could I act without guessing?* (~2 agents, ~4 min). Do this *after* a reading pass reaches 0 ❌, not instead of it — they find different classes.
- A stranger's FAIL is usually upstream of the file being tested. Fix at the source the pointer lands on; do not add a sentence to the runner (that is the enrich-pass failure mode).
- Treat "the reviewer said clean" as a claim about pointers. Related: [[finding_instrument_reports_clean_against_the_wrong_reference]] (the parity gate that compared copies to each other, never to the manual) · [[finding_a_correction_pass_is_unreviewed_work]] · [[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]].
