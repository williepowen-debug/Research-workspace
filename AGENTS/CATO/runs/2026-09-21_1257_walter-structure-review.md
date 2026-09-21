# WALTER structure and workflow review — September 21, 2026

## Disposition and scope

Will requested a review of WALTER's files, structure, process and opportunities to improve. Recommendation: retain the existing architecture; simplify its execution instructions, correct one verification rule, and consider bounded automation of dispatch preparation. No WALTER implementation is authorized by these recommendations or performed here.

Review began at `5a364a7fd`; live WALTER subsequently committed repairs in `1bd26327c`, `1a11a069f`, and `41cc9cff196fa1c3899bdf052a8cad2e1223c0d5`. Structural observations below were rechecked at the latter revision. This is not the acceptance recheck of W1–W4. Those closure conditions remain in [the intake review](2026-09-21_1154_walter-intake-review.md). Concurrent PROME/shared-memory changes were preserved. No owner edits, sends, launches, or operational boot were performed.

Inspected perimeter: WALTER instructions, state/continuity surfaces, design ownership and specifications, routing and intake structure, tool inventory and selected implementations, existing September 21 intake evidence, and read-perimeter checks. This was selective architecture review, not a line-by-line review of every historical file, full code audit, fresh external-source verification, or inspection of the private image collection. No measured session-token or latency claim follows from file sizes. Parts of WALTER's existing guard tooling originated in prior Codex work; assessment of that implementation is author follow-up, not independent certification.

## What is worth preserving

- Canonical BOARD signals, create-only recipient handoffs, and recipient-owned consumption records separate publication, delivery and use. Keep that distinction.
- Batch manifests enumerate dispositions, including NO-ACTION, and refuse closure on declared gaps. Their own documentation correctly disclaims undeclared-input coverage.
- Correction lineage, partial corrections, and separate supersession semantics preserve what survives an update. The earlier failure was partly failure to execute existing controls.
- Canonical ownership tables, a separate boot-provenance file, generated BOARD index, read-only health checks and reconciliation tools are useful foundations. Avoid replacing them with another framework or parallel ledger.
- WALTER's role includes recognizing significance and checking framing. Domain agents own final domain judgments; DEWEY already has a deeper-investigation lane. Simplification must preserve those functions.

## S1 — Medium: the executable instructions are buried in accumulated explanation

**Evidence:** `CLAUDE.md` is 63,848 bytes; `design/SIGNAL_PROCESSING_CHECKLIST.md` 112,494; `design/BOARD_CONSUMPTION_SPEC.md` 136,526; `design/BOOT_PROTOCOL.md` 68,876. These are sizes of different surfaces, not a claim they all load every session. CLAUDE line13 requires boot order `0 → 0.5 → 1–6c → 7–7d → 7g → 7e → 7f → 8–9b`, and closeout step13 precedes12(b). Stable identifiers explain the numbering, but a reader still needs to reconstruct execution order.

`design/SPEC_OWNERSHIP.md:26` contains extensive per-version delivery history immediately before a “CURRENT version + concept map ONLY” instruction. `design/STATE.md:72` describes the former cron feed read as implemented infrastructure without the retirement qualification present in SPEC_OWNERSHIP lines30–32. The old entry is evidence of past implementation, not authority to reactivate it; the directory should make that distinction explicit.

**Consequence:** the agent spends attention distinguishing today's action from the incident that caused yesterday's rule. More words do not reliably prevent omissions, as the intake review illustrates.

**Recommendation:** make existing CLAUDE the concise executable entry point in actual execution order, retaining stable step IDs as cross-reference labels. Each step should identify input, action, completion evidence and failure handling. Move rationale/examples into existing BOOT_PROTOCOL/history homes; reduce SPEC_OWNERSHIP to current owner and section pointers. Preserve cold evidence and existing semantics, including distinct recipient exemptions. Do not merely add a short guide above unchanged contradictory instructions.

**Completion condition:** a reader can resolve boot, one ordinary signal, one correction and closeout without consulting incident history; current routing exceptions survive; existing links/checks remain valid. This is a proposed documentation pass, not a new recurring review requirement.

## S2 — High: the verification verdict conflates unsupported and false

**Evidence:** `design/SIGNAL_PROCESSING_CHECKLIST.md:124` defines FALSE as “Primary source contradicts the claim, or no primary source exists to support it,” and directs KILL with a framing-false reason. Line125 separately offers INDETERMINATE for ambiguous or inconclusive verification. This is an unresolved ambiguity in the written decision rule, beyond the earlier -013 instance.

**Consequence:** absence of supporting evidence can be reported as positive disproof. Even genuinely absent primary support does not by itself establish falsity. The rule risks filtering useful leads and laundering uncertainty into confidence.

**Recommendation:** reserve FALSE for evidence that contradicts the particular claim; use INDETERMINATE for unsupported, inaccessible or insufficient evidence. Whether an unverified item merits routing or investigation remains a separate relevance/urgency decision—this does not require dispatching every rumor. Check the consequential sentence, not just its constituent numbers. Keep the existing distinction between quick framing verification and deeper investigation.

**Completion condition:** cases for a contradicted claim, inaccessible primary, unsupported claim, and mixed true/false claim yield appropriately distinct reasons and preserve surviving facts. Inspect dependent wording identified by SPEC_OWNERSHIP when the owner implements the change. No claim here that every historical kill was wrong.

## S3 — Medium: dispatch preparation still depends on repeated manual bookkeeping

**Evidence:** CHECKLIST Phase3.5 (lines480–523) instructs separate creation of every recipient handoff and append of each delivery row after BOARD/route-log work. Existing `batch_manifest.py` handles input accounting, `gen_board_index.py` renders the index, `reconcile_delivery_log.py` reconciles publication state, and `closeout_check.py` validates a bounded receipt. The inspected tools do not provide one dispatch-preparation operation covering those outputs. This is not a claim no such tool exists elsewhere in the repository.

**Consequence:** correct analytical work can still leave mismatched timestamps, counts, exemptions, links and delivery records. The earlier review supplied actual examples; present repair commits are not independently closed here.

**Recommendation:** after simplifying the contract, consider one bounded preparation command that previews and produces the existing artifacts from an approved signal and explicit recipient-specific asks. It should reuse the index generator and reconciler, enforce current exemption distinctions, refuse collisions, and make retries safe. It must not invent asks, declare consumption, overwrite recipient files, or label a merely written artifact delivered. Commit/push remain under current Git policy. This is a candidate build, not an implemented capability.

**Completion condition:** a normal dispatch, exempt INFO, exempt ACTION, correction, existing-path collision, partial failure and retry produce the intended artifacts without duplicates or false delivery claims. No new database, event bus or parallel delivery ledger is needed for this proposal.

## S4 — Medium: intake provenance and recipient usefulness need a stronger front door

**Evidence:** the earlier pinned intake review found 13 signals with no URLs. FORMAT_SPEC lines205–232 already asks for a short signal summary, facts, relevance and full citation/URL if available. The batch tool's declared-count design cannot independently observe an omitted chat batch. Private processed originals are ignored by Git. Do not confuse an item declaration with verification of its original contents.

**Recommendation:** use the existing signal and manifest: lead with what changed, source/date, unresolved issue, recipient relevance and one concrete ask when ACTION is warranted. Keep details below. Record a stable message/file identifier and item-to-signal mapping; retain originals in an accessible private location. A checksum can identify retained bytes but cannot recreate a missing image or prove extraction accuracy. Where a direct URL is unavailable, say so and supply the available citation; do not fabricate it.

**Completion condition:** for one representative batch, a permitted reviewer can retrieve each original, follow split/combined items through all dispositions, and understand each recipient's task without reading the full narrative. This is a bounded demonstration, not a demand to backfill every historical image.

## S5 — Medium: distinguish declared control coverage from actual assurance

**Checks run:** `python3 PROME/tools/reads_check.py --agent WALTER` returned2/UNKNOWN: September15 attestation predates subsequent boot-defining changes (on recheck, September21 doctor commit). It reported23 cap-bearing and27 declared-not-bearing live reads. `python3 scripts/read_cap_check.py --agent WALTER` returned0 for its measured declared perimeter (19 measured;31 declared-not-counted). These outputs answer different questions. Neither proves the whole runtime is economical or the read enumeration current. No new hard-cap violation is asserted here.

**Recommendation:** after the owner finishes the current edits, refresh the existing read attestation against actual instructions. Use existing receipts to distinguish input coverage, artifact consistency, publication, consumption and substantive integration. A delivered or consumed count alone does not establish usefulness. For a small subsequent sample, inspect whether the intended owner changed a watch, rejected the claim with a reason, or needed more evidence. Use existing recipient dispositions rather than instituting a new scorecard.

**Completion condition:** current enumeration supports the read claim; operator reporting says what each check establishes and what remains unknown. The sample establishes usefulness only for the sampled cases.

## Suggested order and closeout

Finish the already accepted W1–W4 repairs without disturbing live work. Then address S2 and a bounded S1 documentation pass; prove the shorter path on a small batch using S4's existing surfaces. Consider S3 automation only against that settled contract. Re-attest reads after the changes, not before. Prioritize reliable decisions and usable handoffs over more health checks or more routed items.

Delivered: this review and CATO continuity. Implemented: no WALTER changes. Unresolved: S1–S5 are recommendations/owner work, not new assignments; earlier W1–W4 repairs remain unverified by this review. Next CATO action: await Will's chosen follow-up. Git publication receipt is supplied in-session after exact-path closeout.


## Follow-up — WALTER proposal assessed at `cb43e637f`

Will supplied WALTER's response. CATO read `AGENTS/WALTER/outbox/2026-09-21_verdict-letter-FALSE-vs-UNSUPPORTED-PROPOSAL-to-Will.md`, the current verdict table, the specific kill-log row, and PROME's instruction packet from commit `4861c4e79`. No implementation or send performed. WALTER's staged inbox deletion was preserved.

- **CATO-S2 remains open.** The proposal explicitly leaves the letter unchanged. Kill-log line58 contains the Kazakhstan export-ban claim, a FALSE (0.90) verdict, and a no-primary-found rationale. This supports at least one recorded instance of absence-based labeling, not proof that the underlying claim was true, that withholding dispatch was wrong, or that the rule caused the verdict. The same note also invokes pattern matching. CATO did not reproduce the full 635-row census or independently verify the May claim.
- **Correct the diagnosis's overstatement.** Existing INDETERMINATE includes “or verification inconclusive within time budget.” WALTER's claim that uncertainty has no alternative home omits this branch. The defect is conflicting/overlapping instructions, not an enum with no available uncertainty verdict.
- **Prefer the smaller fix.** Retain FALSE for evidenced contradiction of the particular claim; route absence/inaccessibility/inconclusive evidence to existing INDETERMINATE, with a plain-language reason. Keep assessment of truth separate from disposition. A new UNSUPPORTED enum is optional, not a CATO closure requirement. If retained, resolve overlap with the unchanged “inconclusive within budget” branch. The proposed four cases produce three verdict labels, not “four DISTINCT verdicts”; distinct case-specific reasons are what matter. Do not narrow disproof to official admissions or confuse inability to access a source with the source's nonexistence.
- **Preserve history with an explicit correction link.** No wholesale re-adjudication or destructive rewrite is warranted. But the known FALSE(0.90) row should have an additive qualification at an existing correction surface, discoverable from the affected record, so the acknowledged label does not remain unqualified reusable evidence. This correction concerns support for the verdict, not a new truth judgment on the Kazakhstan claim.
- **Approval is already conveyed for the bounded letter fix.** PROME's packet title and opening explicitly record Will's approval; sequencing directs acceptance conditions, PROME's read, then landing under WQ-178 and an independent reader. It expressly says no further Will word is needed for these tasks. CATO has the packet, not the underlying approval transcript. There is no identified reason to reject its authorization merely because it is relayed. Required review steps still apply; optional enum expansion can be avoided by using the existing state.
- **Reviewer and completion limits.** HAWK can review if it did not implement the fix; its stake is useful domain context, not proof of independence. It should devise its own counterexample, including an inaccessible source and partially contradicted claim. “Done or queued” is not verified closure: prior W1–W4, the new verdict repair, instructions cleanup and remaining structural recommendations retain their existing conditions. Numbering should remain qualified CATO-S1–S5 versus PROME ranking; this needs clear references, not a new control framework.

Recommended disposition: proceed with the smaller CATO-S2 correction under existing approval and required review, qualify the known historical label, then the bounded CATO-S1 cleanup. This response evaluates the proposal; it neither performs nor independently certifies repairs.
