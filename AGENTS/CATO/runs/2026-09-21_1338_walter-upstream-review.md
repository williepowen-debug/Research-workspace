# WALTER — are we fixing outputs instead of upstream causes?

## Disposition

Yes: the inspected workflow has a concrete upstream weakness at the point where evidence becomes a verdict and then a summary. Correcting the FALSE clause is useful but cannot by itself prevent unsupported observations, overbroad interpretations, or unsupported explanations of mistakes. Recommend a small change to the existing verification/output contract, evaluated on bounded examples, before another broad instructions expansion.

Scope: Will asked CATO to examine upstream causes of the recurring output defects. Read-only owner review pinned to `ba148c152` on September 21. Inspected Phase1.5 and final quality checks, operator-brief instructions, role boundaries, recent amendment and review request, previous review evidence and this conversation's owner responses. Live WALTER was editing signal020 and preparing021; those working changes are not adjudicated here. No owner changes, sends or launches. Full underlying verifier transcripts and runtime prompts were not available in the inspected evidence, so this review cannot establish the model's internal cause, prove that a particular prompt clause caused an error, or measure error prevalence. Some existing tooling has prior Codex authorship; observations about its coverage are author follow-up, not independent certification.

## U1 — High: evidence is optional in the upstream verifier response contract

**Evidence:** `design/SIGNAL_PROCESSING_CHECKLIST.md:116` explicitly says: “Require a single-line VERDICT at the top of the response — everything else is optional.” The final quality check at line542 asks “source cited, confidence language applied?” Phase1.5 includes source-language triggers and a separate shape-claim guard (line140 onward), so the desk is not wholly without analytical safeguards. However, the literal response contract permits a verdict without the passage or observation that justifies it. A citation can exist while failing to support the consequential conclusion.

**Consequence:** the downstream writer can inherit a confident label and reconstruct a rationale that the verifier never demonstrated. Fixing the labels does not fix that handoff. The historical Kazakhstan row proves a recorded verdict with no demonstrated contradiction; it does not prove this exact mechanism caused that verdict.

**Proposed correction:** replace the optional-support instruction in the existing Phase1.5 contract. Within its existing short response budget, require the exact claim checked, a source locator and short supporting observation/passage (or explicit absence/access limit), and the bounded conclusion. The label can stay first. The receiving writer must be able to identify how that evidence supports this claim. A source's existence, a verifier's confidence number, and a verdict are not substitutes for that link.

**Completion condition:** a source-free confident verdict cannot pass as verified; a real source that addresses a different claim cannot pass; an inaccessible source remains unresolved; a partly wrong claim retains its supported part. Use existing artifacts, not a new evidence database or universal second-agent requirement.

## U2 — High: the writer's own consequential statements can escape the checks applied to incoming claims

**Trace through three examples:**

| Available evidence | New statement introduced during interpretation/summary | Missing check |
|---|---|---|
| No current corroboration of a vague secrecy claim | The class is unfalsifiable; downstream state-actor-only gate | Could independent evidence bear on the claim? |
| INDETERMINATE includes ambiguity **or verification inconclusive within time budget** | There is no uncertainty alternative to FALSE | Does the conclusion survive the full source sentence? |
| Historical note predicts a market move if an export ban is real | The predicted move did not happen | Is there an actual dated observation of the response? |

The first trace is documented in the intake review; the latter two are visible in WALTER's proposal/this conversation and the Kazakhstan row. These examples establish changes in meaning, not intent to deceive or an internal psychological diagnosis.

**Existing protection:** `design/OPERATOR_BRIEF_SPEC.md:53–65` already prohibits losing caveats, explicitly including the direction of a conditional. The checklist already warns that verified figures do not certify a derived shape claim. The gap is execution and coverage at the final inference, not lack of a general warning to be accurate.

**Proposed correction:** apply the existing evidence discipline to the final consequential sentence WALTER adds, including titles, verdicts, operator summaries and correction explanations. Identify which part is observed, which is inferred, and which remains unknown. Do this during drafting; do not burden Will with a new multi-field template. If no support exists for a new observation, remove it or state the uncertainty. Checking incoming headlines alone misses the desk's own strongest claims.

**Completion condition:** the three transformations above are stopped before publication while useful bounded inference remains possible. This extends CATO-S4's concise lead and strengthens S2's implementation; it does not require a new role or banning analysis needed for routing.

## U3 — Medium: the correction loop can add unsupported causal stories and more instructions

**Evidence:** WALTER successively characterized the old rule as a sealed dead end, proposed another enum, defended the historical verdict with an unrecorded observation, and described a further evidence-absence clause as “the real fix.” Each explanation created another proposition to review. At `8d2c9b8ef`, the checklist grew from112,494 to115,710 bytes (+3,216) for the bounded verdict amendment, largely including incident explanation, measurement notes and review status. The historical material is useful, but the prior S1 finding already identifies a separate provenance home.

**Consequence:** a small repair can expand into a policy-design project; incident narratives accumulate in executable instructions. These observations show expansion, not proof that document length caused the day's errors. HAWK's bounded independent read remains legitimate and outstanding; do not remove it merely to shorten the loop.

**Proposed correction:** keep the repair record to the observed defect, bounded change, evidence of the change and open conditions. Keep an explanation of why it happened explicitly provisional unless demonstrated. Put historical rationale in the existing provenance/report home. Correct the minimum active contract; do not convert every correction into a new universal policy. Preserve the old example as a counterexample for the relevant check.

**Completion condition:** the S2 review can close once its specified cases pass, without first solving all reasoning about absent evidence. A bounded S1 cleanup leaves actionable instructions shorter while retaining semantics and references.

## U4 — Medium: bookkeeping and reasoning need different upstream repairs

WALTER called future timestamps, a false-zero grep, and the invented price observation the same defect. All produced unsupported assurance, but their immediate mechanisms differ:

- **Timestamps/counts:** obtain real clock values and derive totals from artifacts. Use existing generation/reconciliation tools; do not estimate operational facts in prose. This is the S3 automation opportunity.
- **False-zero search:** inspect the data's actual vocabulary and verify the query can find a known matching example before interpreting zero as absence. A narrower claim about the search perimeter is appropriate when coverage is uncertain.
- **Invented observation:** require support for the observation at the final inference, as U2 describes. More timestamp validation will not catch it.

The doctor already covers structural consistency; its passing checks never established semantic correctness. Its scope is not itself a defect. The upstream mistake is allowing those receipts to carry assurance they do not provide. WALTER's operator instructions say to report a pattern rather than enumerate errors (`OPERATOR_BRIEF_SPEC.md:73`); that is communication guidance, not evidence that heterogeneous failures share a single cause. CATO likewise must not promote today's three examples into a universal fleet mechanism.

**Completion condition:** each selected failure is paired with a control that could actually detect/prevent it; no single all-clear is used to certify unrelated properties. No new omnibus checker is proposed.

## Smallest useful next step

Keep HAWK's current S2 acceptance read separate. For a subsequent owner-authorized pass, start with U1 and U2 at the existing Phase1.5/finalization steps rather than cleaning all313KB at once. Trial the change on five cases: inaccessible source, irrelevant-but-real citation, mixed true/false claim, conditional prediction without an observed outcome, and a properly supported claim. Have a non-implementing reader provide at least one unseen counterexample. A tabletop replay can establish that the revised contract handles these cases; it cannot establish live reliability. Observe a small fresh batch afterward using existing records before generalizing.

Success means the supported claim survives without strengthening its certainty, and every consequential new fact has support. It does not mean longer reports, more apologies, more checks, or zero legitimate inference. Use actual elapsed work/context measurements if claiming cost improvement; file-byte counts are not runtime-token measurements.

## Approval and review limits

No implementation approval is being requested here; this is a review recommendation. Earlier approval analysis concerns the bounded S2 amendment only. Root `CLAUDE.md` points to messaging rule3, whose full text permits Will's verbatim word in a committed artifact verified by the acting session; PROME's packet contains such a recorded quotation and explicit scope. Do not generalize that instance to “peer assurances clear Will gates.” This upstream review grants no authority over a new change.

No new tests of owner code were run: the assignment is architectural/causal review, not implementation validation. Sources were read at artifacts; the checklist byte delta was measured from Git objects. Earlier W1–W4/S1–S5 retain their original closure conditions. This report introduces upstream hypotheses and concrete contract findings, not automatic closure or a new assigned build. Next: Will chooses whether to commission the small U1/U2 pass.
