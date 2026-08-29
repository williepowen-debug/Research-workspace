---
name: finding_gate_pass_is_not_evidence_it_found_the_best_reason
description: A gate that PASSES certifies that one criterion was met — not that the strongest available criterion was found; soaks that record only PASS/FAIL cannot tell the two apart.
metadata:
  type: feedback
symptoms: "the gate fired so it worked"; "PASS, no action needed"; a soak or calibration log that stores only PASS/FAIL; "our criteria caught it"; a multi-leg gate where one leg passed and nobody recorded which; reviewing a gate by its hit rate
---

A multi-leg gate that fires on its **weakest** leg looks identical, in the log, to one that fired on its **strongest**. The record says PASS. It does not say *which leg carried it*, or whether a better reason existed and was invisible to the evaluator.

⇒ **A PASS certifies that A criterion was met. It is not evidence the gate found the BEST reason, and it is not evidence the evaluator could see the full basis.** The mirror of `[[finding_verification_zero_is_ambiguous]]`: that one is about an ambiguous negative, this is about an ambiguous positive.

**Why it bites:** a calibration soak scores gates on outcomes. A gate that keeps passing on a weak leg while stronger legs go unseen **scores as well-calibrated** and gets tuned in the wrong direction — because the data it generates cannot distinguish "the test is sensitive" from "the evaluator is under-informed."

**How to apply:**
- On any multi-leg gate, **record WHICH leg carried the pass**, not just the verdict. One extra field turns an uninformative PASS into a diagnosable one.
- When a downstream party (a coordinator, a reviewer, the owner) supplies a **better reason than the one you gated on**, write their reason onto the record — do not bank the pass as clean. The gap between your basis and theirs is the finding.
- Ask at evaluation time: *what would I need to know that I don't, and would it change which leg fires?* If the answer is unknowable from where you sit, say so on the record.

**Why:** bought 2026-08-28. WALTER doorbelled two desks (SHADE, BROCK) on rule-6b **leg 3b, cadence** — 15 days dark. PROME's triage then supplied **dated referents WALTER never had** (a market open, a fund tender, a wrapper adjudication, a bankruptcy re-size) that would have satisfied the **stronger L3a** leg outright. The doorbell was *more* warranted than its own gate could show, and the pass had been recorded against the weaker basis. Same sitting, PROME also refuted WALTER's follow-on recommendation using WALTER's **own spec** — a reminder that the party running a gate is often the party least able to see its full input set. Related: `[[finding_verification_zero_is_ambiguous]]`, `[[finding_instrument_reports_clean_against_the_wrong_reference]]`, `[[finding_guard_correctness_and_wiring_are_independent]]`.
