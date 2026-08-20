---
name: finding_overlapping_prereg_branches_restore_grader_discretion
description: Pre-registered branches written at different SCOPES can both be true at once — the grader then picks post-hoc, which is exactly what pre-registration exists to prevent
metadata:
  type: feedback
---

**A pre-registered branch set fails silently when two branches can both be satisfied by one outcome.** The card still looks rigorous — bands, conditions, committed assignments — but at grade time the grader chooses between two live branches, and the pre-registration has bought nothing.

**The cause is almost always a SCOPE shift, not a logic error.** Branches written in sequence read as a clean ladder while quietly changing the surface they quantify over.

**Case (LABOR, 2026-08-20, FOMC minutes card).** Two branches on the same leg:
- **W-2** — *"`strengthened` persists unchanged"* → scoped to the **participants' characterisation**.
- **W-3** — *"softening appears **only** in staff review"* → scoped to **anywhere in the document**.

The minutes satisfied **both**: "strengthened" survived verbatim (W-2) *and* the Staff Review said *"Nonfarm payroll employment growth slowed in June"* (W-3). I graded W-2 on substance — a one-month data note with an explicit offset (*"well above 2025's average pace"*) is not a *characterisation* change — and that argument is sound. **But it was made after reading the text, by the person the card was written to constrain.**

**Why it survives review:** a ladder like *walked-back → survived → softened-but-hedged → not-addressed* looks exhaustive and mutually exclusive because the rungs are ordered by *degree*. The scope shift is invisible in that ordering.

**The check (cheap, pre-freeze, mechanical):**
1. For **each pair** of branches, try to write a single outcome satisfying both. If you can, the partition is broken.
2. Re-scope every branch to the **same named surface** — *"the Participants' Views section,"* not *"the minutes."*
3. Over **qualitative** text, also pre-commit a *"present but in an unanticipated role/polarity"* branch that **moves no score** — the same card's attribution branches were jointly unsatisfiable because supply language showed up arguing the *opposite* case from the one anticipated.

**Distinct from its siblings** — check all three before writing a branch set: [[finding_enumerated_mechanism_test_hides_a_completeness_claim]] is *incompleteness* (outcome arrives off-list); [[finding_compound_gate_jointly_unsatisfiable]] is *joint unsatisfiability* (no outcome satisfies it); this one is *overlap* (more than one branch satisfied). A set can be checked clean on the other two and still fail this. See also [[finding_prereg_branch_label_can_contradict_its_condition]] and [[finding_prereg_verdict_boundary_must_be_a_number]].

**Cost when it fires:** no score moves, so nothing looks broken — the damage is that **the grade's authority is weaker than it appears**. Say so on the card rather than letting the pre-registration launder a post-hoc call.
