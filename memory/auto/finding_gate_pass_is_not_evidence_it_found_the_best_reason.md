---
name: finding_gate_pass_is_not_evidence_it_found_the_best_reason
description: A gate that PASSES certifies that one criterion was met — not that the strongest available criterion was found; soaks that record only PASS/FAIL cannot tell the two apart.
metadata:
  type: feedback
symptoms: "the gate fired so it worked"; "PASS, no action needed"; "all three options pass the test so any of them is fine"; "the guard is silent here so I am free to choose"; using an eligibility test to pick a winner; a menu where every candidate clears the bar; "test 4 passes, therefore this is the right drawing"; a soak or calibration log that stores only PASS/FAIL; "our criteria caught it"; a multi-leg gate where one leg passed and nobody recorded which; reviewing a gate by its hit rate
---

A multi-leg gate that fires on its **weakest** leg looks identical, in the log, to one that fired on its **strongest**. The record says PASS. It does not say *which leg carried it*, or whether a better reason existed and was invisible to the evaluator.

⇒ **A PASS certifies that A criterion was met. It is not evidence the gate found the BEST reason, and it is not evidence the evaluator could see the full basis.** The mirror of `[[finding_verification_zero_is_ambiguous]]`: that one is about an ambiguous negative, this is about an ambiguous positive.

**Why it bites:** a calibration soak scores gates on outcomes. A gate that keeps passing on a weak leg while stronger legs go unseen **scores as well-calibrated** and gets tuned in the wrong direction — because the data it generates cannot distinguish "the test is sensitive" from "the evaluator is under-informed."

**How to apply:**
- On any multi-leg gate, **record WHICH leg carried the pass**, not just the verdict. One extra field turns an uninformative PASS into a diagnosable one.
- When a downstream party (a coordinator, a reviewer, the owner) supplies a **better reason than the one you gated on**, write their reason onto the record — do not bank the pass as clean. The gap between your basis and theirs is the finding.
- Ask at evaluation time: *what would I need to know that I don't, and would it change which leg fires?* If the answer is unknowable from where you sit, say so on the record.

**Why:** bought 2026-08-28. WALTER doorbelled two desks (SHADE, BROCK) on rule-6b **leg 3b, cadence** — 15 days dark. PROME's triage then supplied **dated referents WALTER never had** (a market open, a fund tender, a wrapper adjudication, a bankruptcy re-size) that would have satisfied the **stronger L3a** leg outright. The doorbell was *more* warranted than its own gate could show, and the pass had been recorded against the weaker basis. Same sitting, PROME also refuted WALTER's follow-on recommendation using WALTER's **own spec** — a reminder that the party running a gate is often the party least able to see its full input set. Related: `[[finding_verification_zero_is_ambiguous]]`, `[[finding_instrument_reports_clean_against_the_wrong_reference]]`, `[[finding_guard_correctness_and_wiring_are_independent]]`.

---

## 2026-09-19 — THE SECOND FACE: A GUARD THAT PASSES *EVERY* OPTION CANNOT RANK THEM, AND ITS SILENCE READS AS PERMISSION

The body above is about **which leg carried one pass**. This is the mirror at the level of the **menu**: an eligibility test applied to a set of candidates that **all clear it**.

> ⛔ **A test that admits every option on the menu has told you the menu is legal. It has told you NOTHING about which option to take — and on the choice where the chooser's interest is largest, silence is exactly what a captured guard looks like from the inside.**

**Worked, OSPREY 2026-09-19, and the value of the case is that the SAME test discriminated on one question and not on its sibling.** Two scope questions about the desk's own kill letters, both routed to the operator on the grounds that *"the desk that owns the letter should not interpret a letter it benefits from interpreting"* — a claim about motives, which no third party can check.

- **Channel 3 — a BINARY.** `DELEGATION_TIER` test 4 (*is the falsifier easier to trigger, or unchanged?*) ranked the two answers **uniquely**: one put the clock at 16/21, the other at 6/21. **The test selected, so the desk had no discretion left to exercise, so there was nothing for a conflict of interest to act on.** Self-ruled.
- **Channel 2 — a MENU OF THREE.** Test 4 passed **all** of A (18/30), B (10/30) and D (unchanged at 9/30) — "unchanged" satisfies the test by its own wording. **The only anti-self-serving guard in the tier was therefore silent across a choice spanning 9 days of a 30-day clock on the desk's highest-scored channel.** Routed.

**⇒ The reusable discriminator, and it replaces an unfalsifiable claim about motive with a check anyone can run:**

> **Ask whether the guard SELECTS a unique answer, or merely ADMITS the field.**
> **SELECTS ⇒ act — the guard, not your judgement, is choosing.**
> **ADMITS ⇒ escalate — you are about to exercise discretion the guard was written to remove, and the guard will report PASS while you do it.**

⚠️ **The trap is that "it passed the anti-self-serving test" is TRUE and reassuring in both cases**, and it is load-bearing only in the first. Reaching for the most self-adverse option instead is **not** a repair: on the OSPREY case the most self-adverse drawing (A, 18/30) rested on a premise the desk had retracted the same morning, so adopting it for adverseness alone would have encoded a reading nobody believed. **Self-flagellation is not judgement either.**

**Companion:** `[[finding_a_scope_rule_allocates_visibility_not_superior_judgement]]` (a rule that says who may SEE is not a rule about who judges better) and `[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]` (a guard that only prints gets overridden) — this is the third member: **a guard that only ADMITS gets mistaken for one that endorses.**

