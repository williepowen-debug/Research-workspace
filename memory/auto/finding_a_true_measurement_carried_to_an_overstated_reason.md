---
name: finding_a_true_measurement_carried_to_an_overstated_reason
description: Correct figures get attached to a reason stronger than they support — the tell is reaching for a principle-shaped justification when a plain one already settles it
metadata:
  type: feedback
symptoms: "every number checked out but the reviewer still rejected the conclusion; 'this erases the evidence'; 'this means X is broken'; the operator said 'too strong'; the byte counts were right and the verdict was wrong; I justified a decision three times and each justification was overturned while the decision stood"
---

**A measurement can be exactly right and the REASON attached to it exactly wrong.** The failure is not in
the figure, the source, or the date — all of those verify — it is in the sentence that says *what the
figure means*. Because the verifiable part passes every check, nothing in a normal review fires.

⚠️ **The tell: you reached for a PRINCIPLE-SHAPED reason when a plain one already settled the question.**
"This erases the evidence" instead of "no consumer benefits and a rewrite carries risk." The plain reason
was true and sufficient. The principle-shaped one was false — and it was the one that got written down,
because it sounds like it generalises.

**Why it survives:** a principle-shaped reason is *more* satisfying to write and *harder* to check. It
recruits a real finding-name, sits next to correct figures, and reads as rigour. A reviewer who checks
the figures finds them clean and moves on; only a reviewer who separately asks *"does this conclusion
follow?"* catches it. That is a different question from *"is this true?"* and almost nothing asks it.

**Measured 2026-09-12 — three in ONE session, all caught by the operator, none by me:**
- ORCH_LOG: counts correct (26 `yes`-leading, dates exact) → *"normalizing erases the evidence"* — false;
  committed git history preserves every original value and the record documents it.
- `.claude/settings.json`: byte sizes and hook lists correct → *"a session launched from the repo root
  runs with no git_guard"*, framed as operationally live — but the repo says launch PROME from `PROME/`,
  and location-specific config may legitimately differ. Accurate fact, unsupported conclusion.
- `git_guard` F-6: rc values correct → *"the git command runs unlinted"* as though general — the blocking
  path was never broken; only the input-validation path crashed.

**How to apply:**
- After writing a conclusion from verified numbers, ask the separate question: **"what is the WEAKEST
  reason that fully settles this?"** If a weaker reason settles it, the stronger one is decoration and is
  probably also false. Write the weak one.
- **Grade the decision and its justification independently.** In all three cases the DECISION survived and
  the justification did not. A justification being overturned is not a reason to reopen a sound decision —
  and a sound decision is not evidence its stated reason is sound.
- Watch for a conclusion that upgrades a scoped fact into a systemic one: *this path* → *the system*,
  *this validation branch* → *the guard*, *this file's history* → *the evidence*.
- A relayed finding's stated CONSEQUENCE needs reproducing just as much as its mechanism does. Two of
  three overstatements I passed on tonight originated in someone else's report and I relayed them.
  `[[finding_asymmetric_rigor_counterparty_claims]]` — relaying is asserting.

Related: [[finding_verified_figures_do_not_verify_the_shape_claim]] (same family, but about SHAPE words
over a series and their denominators) · [[finding_exact_level_authenticates_a_wrong_direction]] ·
[[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]] ·
[[finding_naming_a_caveat_can_substitute_for_fixing_it]]
