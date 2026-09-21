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


## Implementation investigation — v0.48 at `c47c33418`

Will explicitly asked CATO to inspect WALTER's files after the owner reported implementation. Reviewed commit `b1d6ff592`, the complete changed U1/U2 clauses, `research/2026-09-21_U1-U2-tabletop-validation.md`, `design/history/CHECKLIST_VERSION_HISTORY.md`, and HAWK's `SIG-W-20260921-022` handoff. This is CATO's non-implementing static review of the resulting contract, informed by CATO's earlier recommendations; it is not a blind behavioral test or a substitute for HAWK's assigned S2 read. No owner edits or sends. Concurrent PROME/shared-memory work preserved.

### Verified implementation and preservation

- U1 now requires claim, locator/access limit, supporting observation and bounded conclusion. Asking the verifier for missing information is explicit. U2 now checks observations/inferences/unknowns in WALTER's own consequential sentence. The previous citation-presence box is explicitly limited.
- Git-object measurements reproduce115,710 bytes at v0.47 and117,112 at v0.48: +1,402 bytes for this pass, +4,618 from112,494 before the two amendments. These are document sizes, not token/cost measurements.
- FALSE and INDETERMINATE rows are byte-identical between `8d2c9b8ef` and `b1d6ff592`. The complete prior amendment block (2,385 bytes with outer whitespace stripped) is retained verbatim in the history file. This verifies preservation; it does not reproduce the owner's differently bounded1,811-byte narrative-only measure.
- `python3 AGENTS/WALTER/tools/version_drift_check.py` returned0: registered spec versions and split companions match. This is version consistency only; CATO has prior authorship in parts of that guard.
- HAWK's notice actually exists, includes the retrieval command, distinguishes its old review from U1/U2, and explicitly records the unseen case as unfilled. The pinned rows are preserved; unchanged rows do not establish unchanged behavior when a new preceding gate is introduced.

### U1 remains PARTIAL — access-limit handling conflicts with the new routing gate (high)

The four-field contract permits an explicit access limit in field2 but demands a supporting passage/figure in field3 without an explicit no-observation alternative. It then says “A VERDICT WITHOUT FIELD 2 AND FIELD 3 IS NOT A VERIFICATION RESULT — do not route on it” and “Inability to check is not permanent and is never a reason to route anyway.” “Do not route on it” could reasonably mean do not rely on that verdict; the last sentence and validation file's “is not routable” broaden that reading.

The adjacent INDETERMINATE row permits unconfirmed routing and separates verdict from disposition. Case1 of the author's validation simultaneously says the missing observation fails the routable test and the disposition remains a separate urgency/relevance call. Thus the proposed failure is present in actual text, not merely in Will's relay. This is an ambiguity/contradiction; this review does not establish that a live dispatch was blocked.

**Reviewer-designed counterexample:** A fictional, time-sensitive operational alert is reported by a named source. The original notice is inaccessible. A verifier returns the exact claim, publisher/date/locator, the access failure, and “no supporting passage obtained; claim remains unverified.” Assume the item independently meets the desk's criteria for an explicitly unconfirmed alert. Should WALTER request clarification, abandon unsupported CONFIRMED, and still consider unverified routing—or block the alert until a passage arrives? The current clauses support both readings. Repeatedly asking a verifier cannot guarantee a paywall/outage/access barrier clears before the information expires.

**Minimal proposed replacement, not applied:** “A missing required field makes the verifier response incomplete; request it before relying on a CONFIRMED/FALSE verdict. Field3 may explicitly state that no supporting observation was obtained, with the limitation. This does not prohibit separately routing the underlying item as unverified under existing relevance, urgency and disclosure rules.” Preserve the four fields and the short response budget. Distinguish an omitted observation field from an honestly populated field saying no observation was available. No new enum or approval loop is needed to describe this proposal; implementation authority remains with the owner/user.

**Closure condition:** the example cannot pass as verified and is not automatically killed or delayed solely by the verification result. Relevance/urgency may still justify withholding dispatch. This is a reader-created static counterexample, now disclosed, not an unseen live test administered to WALTER.

### U2 remains PARTIAL — its new explanatory sentence violates its own requirement (medium)

The new finalization block claims: “every defect this desk shipped on2026-09-21 entered at exactly this step — during interpretation, downstream of correctly-sourced inputs.” This is not established. The inspected record includes a search keyed to the wrong vocabulary, an overdue-label arithmetic defect and manual accounting errors; not all are errors in final inference from correctly sourced inputs. The earlier upstream report explicitly separated mechanisms. The new U1 explanation similarly shifts from a contract that *could* omit evidence to a narrative that the writer *then inherited* a label and reconstructed a rationale. The latter is a plausible mechanism, not demonstrated causation for the historical case.

**Correction:** delete the universal causal sentence and describe U2's purpose without asserting a census or cause. Keep the instruction itself. Qualify the U1 historical mechanism as a possibility. The operative U2 check is useful, but its author's own explanation demonstrates why written adoption is not evidence of application.

### U3/U4 and validation — useful design examples, not measured performance

The owner correctly labels the cases author-selected/author-graded and disclaims live reliability. Nevertheless, several OLD-contract entries overstate what the prior rules required or permitted as a compliant result:

- Case1 says inaccessible material would route to FALSE/KILL. The earlier INDETERMINATE time-budget branch also existed; the prior problem was conflicting instructions, not a mandatory single outcome.
- Case2 says a real-but-irrelevant citation “passes.” It passes the citation-presence checkbox, but the older CONFIRMED definition required the primary to support the claim as written. The defect was weak evidence handoff/check execution, not absence of that semantic requirement.
- Case3 presents only FALSE or CONFIRMED for a mixed claim, although CORRECTED-framing and INDETERMINATE existed. Its hypothetical input is a useful test, but it is not a verbatim replay of signal005, whose actual core defect involved treating incomparable series as a stale vintage; the superlative separately propagated into the closeout.

These should be labeled possible failure modes, not baseline test outcomes. The document contains scenarios, expected handling and author judgments; it does not supply independent execution traces showing WALTER receiving and responding to these cases. The caveats are appropriate, but “5 of5” adds no measured behavioral success rate. Do not use it to quantify improvement.

The broad instructions cleanup remains open; net growth alone is not a reason to reject this bounded evidence-contract change. The new history file is not inherently a defect: it follows the existing version-history convention and preserves the removed text. Fix misleading wording and trial the behavior before a broader rewrite.

### Bounded next step

Owner corrects the U1 access-limit/routing ambiguity and removes U2's unsupported causal explanation, then aligns the validation commentary with the actual old contract. Notify the relevant reviewer of the resulting target; HAWK's v0.47 acceptance must not be represented as acceptance of all v0.48 behavior. Complete a non-implementer-designed behavioral test with actual WALTER responses and a small fresh batch using existing records. A test result must distinguish the evidence supplied, WALTER's actual action, and whether that action preserved the claim's uncertainty. No extra general-purpose checker, new ledger or permanent per-signal outside review is recommended.

**Disposition:** implementation inspected; useful core changes present; U1/U2 not closed. Independent live/unseen execution and fresh-batch evidence remain unperformed by CATO and explicitly outstanding in WALTER's validation. Earlier S2/HAWK closure remains separate. This investigation delivers a concrete counterexample and wording proposal, not authority to edit the live owner's files.
