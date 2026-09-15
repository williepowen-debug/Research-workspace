**Historical snapshot from earlier in this session. Current completion and next steps: [closeout](2026-09-14_codex-closeout.md).**

Observed: 2026-09-14 20:50:09 EDT

# Decision Deck review

## Verdict

Updates required in the source explainers and decision-state handling before republishing. A fresh build reproduces the substantive defects.

Scope: current local HTML, current generator, all rendered card membership compared with a new scratch build, and focused semantic checks of WQ-213/228/229/230/243/251/252 against their queue rows. This is not a complete factual re-verification of every historical card. Hosted private artifact and rulings database could not be read through the available tools; publication/tap state remains UNKNOWN this turn. The last closeout reports publication failure, but that is carried evidence, not a fresh hosted-page inspection.

## Verified findings — claim / artifact / verification / observation / proposed change

### 1. WQ-213 gives the wrong current action and controls — high priority

Artifact: PROME/registry/WQ_EXPLAINERS.tsv row 213 (physical line 24); PROME/tools/decision_deck.py parse_open (line 148), render_owed (line 345); PROME/WILL_QUEUE.md row 213.
Verification: parse current OPEN rows, inspect answered flag, and inspect article #wq-213 in both stored and freshly generated HTML.
Observation: answered=True; title is "VLO refiner leg: place it at a fresh mark"; only DONE/LATER buttons. Explainer repeats the withdrawn crack-collapse objection and an expired intraday mark. Latest queue text explicitly records condition 2 tripped, fresh reaffirmation required, and Will's September 15 reassessment instruction. The parser classifies from the old APPROVED lead without accounting for the subsequent return-to-Will condition.
Proposed change: show "VLO: reassess and reaffirm or withdraw"; preserve card ARMED, required fresh conditions and September 18 needed-by. Retire the false margin-collapse objection from the current explainer. Model reopened approval explicitly so reaffirmation cannot be mistaken for a completed fill. Do not infer a ruling or fill from this review.

### 2. WQ-251 retains the superseded framing — high priority

Artifact: WQ_EXPLAINERS.tsv row 251 (line 55), queue row 251, rendered article #wq-251.
Verification: compare displayed name/what/if_yes with the corrected queue headline and tier-test paragraph.
Observation: card headline says the old reason turned out false; if_yes says the stand-down is "lifted or re-based". Queue explicitly recommends re-basing on the tier test and NOT lifting: BB/B tightened while CCC widened, a concentrating-tail interpretation.
Proposed change: lead with "Retain the credit stand-down; update its rationale" and make the yes consequence acknowledge that basis without lifting or re-arming anything. Carry the concentration-versus-migration distinction into the plain-English explanation.

### 3. WQ-252 offers approval without selecting a defined remedy — decision clarity

Artifact: WQ_EXPLAINERS.tsv row 252 (line 56), queue row 252, briefing pilot draft.
Verification: compare if_yes and rec_reason to the registered options and timing.
Observation: generic Approve says the letter gets repaired by one of several materially different remedies, while PROME and HENRY explicitly recommend no remedy. The title also calls it a live position even though the associated VLO purchase remains unfilled. The separate briefing-format pilot is DRAFT.
Proposed change: distinguish format adoption from the substantive design decision; state NOT FIRED and retain the scheduled decision window. Require a named remedy or an explicit decision to retain the letter rather than treating a generic approval as authority to choose a threshold change. Do not adopt the draft merely by regenerating the page.

### 4. WQ-229 summary broadens the proposed review burden — secondary

Artifact: WQ_EXPLAINERS.tsv row 229 (line 39), current queue row 229 and PROME/CLAUDE.md repair-completion bullet.
Verification: compare "every repair ... tests at least one independent counterexample" with the consequential-repair qualifier and considered-with-N/A neighbor categories.
Observation: the explainer drops the scoping qualification. Its four states read as exclusive choices, while the operating record expects separate evidence for implementation, tests, independent verification and unresolved coverage.
Proposed change: retain the consequential-repair boundary, state the four dimensions separately, and preserve the pending ruling status.

### 5. Publication size and generation freshness remain separate issues

Verification: generated /tmp/prome-decision-deck-review-20260914.html with --today 2026-09-14; compared section article IDs and normalized article text to PROME/artifacts/decision_deck.html; measured both via PROME/tools/measure.py.
Observation: stored build 19:44/b2d4e1cce; scratch build 20:48/a993a451b. All Owed, Decided and In-flight card contents unchanged; Docket gains L393. Both local builds already contain WQ-252, unlike the prior report about the older HOSTED version. Stored HTML is 484349 B; scratch 487615 B. Raw queue/history prose is embedded even when collapsed. The existing selftest PASSES and all 28 OPEN rows have explainers (24 ruling / 3 hands / 1 blocked); those checks do not validate semantic currency.
Proposed change: repair the source/state defects before regeneration. Address L393's publication burden while preserving access to provenance and the private rulings store. Rebuilding alone carries the same obsolete explainers forward.

## Delivery

Review only. No live source, controls, ruling, tap state or hosted artifact changed. Scratch build is a diagnostic copy, not a corrected candidate. Existing prior-turn local changes remain intact. Priority order: WQ-213 action/state; WQ-251 rationale; WQ-252 decision specificity; WQ-229 qualification; publication-size remedy and authenticated publication check.
