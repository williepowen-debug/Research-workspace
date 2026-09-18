---
name: finding_crash_residue_over_claims_toward_completion
description: a crashed session's uncommitted files describe the closeout it was ABOUT to perform, so the residue is not merely incomplete — it is false in one predictable direction, toward looking finished
symptoms: "session crashed mid-closeout", "uncommitted work after a crash", "recovering a dead session's files", "handoff says pushed but nothing was pushed", "STATUS says session in progress", "machine crashed before closeout", "is this residue safe to commit"
metadata:
  node_type: memory
  type: finding
---

When a session dies before its closeout, its uncommitted files are **not a truncated version of the truth**. They contain sentences written in anticipation of a closeout that never ran, so the residue **over-claims in one predictable direction: toward looking more finished than it is.**

**Measured 2026-09-18** (one machine crash, two desks recovered by spawning each desk to commit its own residue): **five over-claims, every one pointing the same way.**
- BRENT's handoff **read as a clean closeout, claiming a push that never happened.**
- A line instructed the next session to rotate blocks **that session had already rotated.**
- A tracker alert line still read *"No September15 observation yet"* **inside the block whose own heading says three routines read it at run time** — the observation had been graded 15:30:53, minutes before the crash. The numbers in that cell were correctly vintage-labelled; the un-vintaged sentence beside them had gone false.
- AEOLUS's STATUS carried an **unfilled `"session IN PROGRESS; four domain workers running"` placeholder where its conclusion belonged.**
- Its convergence matrix and exit triad were never refreshed and **contradicted the body of their own file.**

**Why:** a closeout is written forward. A session drafts "what I did / what is pushed / what the next session should do" *before* performing the acts those sentences describe. The crash freezes the draft, not the deed. Nothing in the file marks the difference, and the prose is confident because it was true-when-intended.

**How to apply.**
- **The owning desk commits its own residue; a coordinator must not commit it blind.** Only the owner can tell whether a claim in its own file was performed or merely intended. On 2026-09-18 PROME could not have caught any of the five and would have committed all of them as fact.
- **Take a per-file hash inventory BEFORE any recovery touches anything**, so afterwards you can prove which files changed and match each change to something the desk reported. The test is not "did nothing change" — a desk *should* correct its own over-claims — it is "is every path accounted for, and does every change match a stated correction".
- **Audit forward-tense and completion language first**: "pushed", "committed", "closed out", "rotated", "no observation yet", "in progress". Those are where the lie lives.
- **A mechanical tell exists**: the residue's own stamps stop at one instant. AEOLUS's six files all stopped at `14:28:05`. That is a process death, not a wind-down.
- ⛔ **Absence of residue proves nothing.** A desk idle with everything committed and no dirty paths is **indistinguishable on disk** from one that closed out properly — see [[finding_record_of_an_action_is_not_the_action]].

Related: [[finding_a_correction_pass_is_unreviewed_work]] · [[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]] · [[finding_correction_beside_an_instruction_leaves_two_live_instructions]]
