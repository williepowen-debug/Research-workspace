---
name: finding_the_artifact_built_to_prevent_bias_is_the_one_nobody_audits
description: "A pre-registration, frozen prep file or blind spec is treated as the check, so nothing checks IT — and when it is wrong, its errors point the same way as the bias it was built to stop."
metadata: 
  node_type: memory
  symptoms: "the prep file was frozen before the close so I trusted its numbers · re-derived the screen and got n=24 where the frozen file said n=23 · my pre-registration excluded a session and never said why · both errors in my own evidence file favoured my own prepared verdict · I read the figures off the frozen page instead of recomputing them · the anti-fitting artifact was itself fitted · dropped the observation most favourable to the row I was grading · 'identical persistence' was asserted, not measured"
  type: feedback
  originSessionId: 183b776e-9bc1-4efb-bb1d-d25ecd0e6777
  modified: 2026-09-19T15:38:45.587Z
---

**A document written to stop you fitting the answer is still your work, produced under the same incentives — and because its whole purpose is to be the safeguard, it is the one artifact nobody re-derives.**

The failure is not that the safeguard is skipped. The safeguard runs, is respected, and is cited at grading time. The defect is that **its contents were never audited**, because freezing it *felt* like the audit. And the errors will not be random: they inherit the direction of the bias the file was built to prevent.

**Measured case (SAM, 2026-09-19, grading SAM-28/SAM-31).** A prep file was deliberately frozen on 9/18 *before* the close, with its stated purpose written at the top: *"so the grade cannot be fitted to the outcome afterwards."* It was honest in intent, it disclosed the alternative reading, and it argued against its own row paying. Grading the next day, I re-derived every figure from the instrument rather than reading them off the page. **Two errors, and both favoured the verdict the file had prepared:**

1. **A silent sample exclusion.** Its risk-off screen reported `n=23`, yen up `6 of 23 = 26%`, mean `−0.226%`. Re-running the screen *as that file itself defines it* gave `n=24`. Dropping exactly one session — 2026-09-08 — reproduced all five of its statistics to the third decimal, which identified the exclusion beyond doubt. That session (VIX +1.19, S&P −0.58%, FXY **+1.52%**) was **the single observation most favourable to the row being graded**. A defensible reason to exclude it existed — that date carried an open official-intervention attribution, and an operation-driven move is not evidence about haven behaviour — **but it was never written down.** An unstated exclusion is a defect whatever its unstated justification would have been.
2. **An asserted equality.** It claimed two episodes "identical in persistence (6 sessions each)" and leaned on that in its control argument. Measured: 5 and 6. The word doing the rhetorical work had not been computed.

Neither error changed either verdict, which is exactly why they would have survived. **A defect that does not flip the answer is invisible to every check that only looks at answers.**

**Why the direction is not a coincidence.** You build the safeguard *while already holding a view*. Every judgement call inside it — which sessions qualify, which window, which word means what — gets made by the same mind the safeguard is meant to constrain. The safeguard constrains the *conclusion*; it does not constrain its own *inputs*. So the residual bias migrates from the verdict into the evidence file, where it is safest.

**Defaults:**
- **Re-derive a frozen artifact's numbers at use time; never read them off the page.** Reproducing them costs minutes and is the only thing that can catch this. Cheap tell: if you cannot reproduce a stated `n`, try dropping single observations until it matches — the one that reconciles is the finding.
- **Every exclusion is stated in the artifact, with its reason, at freeze time.** "I dropped this and here is why" is a pre-registration. Dropping it silently is not, even when the reason would have been good.
- **Any comparative word carrying argumentative weight — "identical", "same", "comparable" — is computed, not asserted.**
- **When you find a defect in your own safeguard, record it above the grades it bears on, not in a footnote.** It is more transferable than the verdict.
- **Apply this hardest when the correction favours you.** Both of these made my prepared answer look better; that is the signature, not the exception — see [[finding_a_charitable_reading_of_your_work_is_the_one_to_check]].

Related: [[finding_a_correction_pass_is_unreviewed_work]] (fix passes are the least-reviewed work; this is its pre-registration twin) · [[finding_adoption_is_not_validation]] · [[finding_crosscheck_with_free_parameter_validates_nothing]] · [[finding_test_the_guard_not_just_the_guarded]] · [[finding_gate_pass_is_not_evidence_it_found_the_best_reason]].
