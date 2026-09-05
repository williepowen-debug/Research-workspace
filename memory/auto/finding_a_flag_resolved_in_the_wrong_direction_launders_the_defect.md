---
name: finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect
description: "A detector can fire correctly and the defect still ships — because it is defeated at the RESOLUTION step, not the detection step. A flag resolved in the wrong direction is WORSE than no flag: it launders the defect (now it looks reviewed) and erases the tell (the mismatch that pointed at it). 'A flag is a prompt to LOOK, not a find-replace' is necessary but not sufficient — you can LOOK and still resolve backwards. For a date/weekday mismatch specifically: treat it as POSSIBLE transplantation (ordinary typos cause it too) and verify one occurrence against the originating artifact before changing either field or propagating — the weekday can be the survivor of an earlier true event, the date the fabrication. CARL KB-428, softened by Codex 2026-09-05."
metadata:
  node_type: memory
  type: feedback
symptoms: "claim_check fired and I fixed it the wrong way · resolved a flag backwards · changed the weekday when the date was the wrong half · a flag resolved in the wrong direction · date/weekday mismatch treated as a typo · the detector fired but the defect still shipped · find-replace on a flag · which half is authoritative"
---

**The detector is usually not the weak point — the RESOLUTION step is.** A working tripwire can fire on exactly the right thing and the defect still ships, because someone reads the flag, picks the wrong half to "fix," and the flag goes green. That is strictly worse than no detector at all: the defect is now **laundered** (it looks reviewed and correct) and the **tell is erased** (the very mismatch that pointed at it is gone), so the next reader has nothing to catch.

**Concrete (CARL, 2026-09-05):** `claim_check` fired *"Wed 9/10 — 2026-09-10 is a Thursday"* across five files — a correct fire on PROME's fabricated CVNA event. CARL recorded "the date is right, the weekday label is wrong" and changed **Wed→Thu** in all five. Backwards: 2026-07-29 (the real, transplanted-from event) **was a Wednesday**; 2026-09-10 is a Thursday. The **weekday was the surviving true fragment**; the **date was the fabrication.** The fix erased the only evidence of the transplant, everywhere at once.

**Why "look, don't find-replace" is not enough:** CARL *did* look (the guidance was followed to the letter) and still resolved toward the more load-bearing-looking half (the date). Following the discipline did not save it, because the discipline says LOOK, not *which half is the survivor.*

**How to apply:**
- **Before resolving any two-part mismatch, ask which half is the SURVIVOR of an earlier true state** — do not assume the more prominent/load-bearing field is authoritative. A re-dated row keeps the ORIGINAL event's weekday, which is exactly why the pair disagrees (`[[finding_ambiguous_coordinator_instruction_mints_a_propagating_event]]`).
- **Treat a date/weekday mismatch as POSSIBLE transplantation, not proof of one** (CARL KB-428, softened by Codex 2026-09-05 — ordinary typos also produce the mismatch, so "definitely a transplant, not a typo" is overfit). The durable rule: **verify ONE occurrence against the originating artifact before changing either field OR propagating the correction.** Same shape for any "X said Y, metadata says Z" pair — one field may be the residue of a real earlier state, so establish which before editing either.
- **Resolving a flag is unreviewed work with a HIGHER error rate** (`[[finding_a_correction_pass_is_unreviewed_work]]`): a batch find-replace across N files applies the wrong resolution N times and removes N tells in one pass. Resolve ONE, confirm against the primary, then propagate.
- Systemic read: when a defect ships past a detector that fired, audit the RESOLUTION, not just the detector — "the tripwire works" and "the defect shipped" are both true at once.
