# Closeout repairs: current choices and delivery evidence

Date: 2026-10-14. Owner: PROME. Status: PROPOSAL; no runtime change installed.

Will's instruction: “Okay lets do it. Can you move forward with this?” following PROME's recommendation to prepare one bounded proposal for CATO PC14-1/2 alongside relevant already-approved maintenance. This authorizes preparing this design and advancing existing authorized work; this document does not silently change maintenance ordering, the process ceiling, capital authority or review requirements. No new approval is needed to repeat an already-ruled maintenance instruction.

Source: `3b65fc460:AGENTS/CATO/runs/2026-10-14_1529_prome-closeout-review.md`. Existing work: DOCKET L367 (delivery boundary and separate fail-closed residue), L402 (authorship), L688 (UNKNOWN broker as-of); maintenance order L675/L628/L676 and Helm encoding L665/L647. This is one design with two implementation episodes, not one bundled exception to the one-process-change ceiling.

## Result sought and scope

Keep independent review. Reduce obsolete choices reaching it and remove dependence on unrelated desks finishing their files. HANDOFF remains navigation; FORGE/owner records and existing review receipts retain authority. No new daily checklist, monitor, auditor, portfolio database, publishing service or trade rule.

Implementation is prospective. Today's corrected TLT/TBT displays remain the last accepted result; this proposal does not certify subsequent holdings or restore hosted publication. Local build, committed content, pushed content and hosted publication remain separate receipts. JANUS remains its separately approved boot trial, with no promised closeout savings.

## Evidence checked for this proposal

| Claim | Artifact and verification | Observed | Disposition |
|---|---|---|---|
| Delivery verification compares foreign pending packets against PROME's commit | `tools/argus_scope.py::record_review`, `verify_review`, `build_scope`; historical SHA256 replay of every manifest path at dc1abc44f and 27a26d1cd | VERIFIED: four absent DEWEY packets at the first commit, zero mismatches at the later commit | Repair delivery/dependency membership, retain inventory |
| Option-source matching alone does not establish applicability to today's holdings | `tools/decision_deck.py::validate_options`, `options_for`, `render_owed`; CATO's cited WQ302/357/360 correction | VERIFIED at code: offered text is checked against the card, but these functions do not bind it to an accepted holding version | Add holding applicability before any action rendering |
| Holdings and management are different sources | `FORGE/STATUS.md` header and `FORGE/position_management.tsv` header | VERIFIED: STATUS owns mirrored holdings; management map owns approval/order/fill references, not quantities | Do not derive holdings from management prose |
| Calendar patch remains directly applicable | DAEDALUS L548 bundle's target_hashes.json versus current prome_gate.py SHA256 | NOT ESTABLISHED: current whole-file hash differs from required before hash | Refresh patch against current source; never force/three-way the old bundle |

Machine evidence: `PROME/reports/2026-10-14_closeout-repair-readiness.json`. Historical blob identity verifies persistence, not correctness of financial content or full review coverage.

## A. Position facts and applicability of recommendations

### Proposed change

Use one read-only adapter over the accepted FORGE holdings mirror and its cited broker evidence. Reuse an existing suitable parser if one is established during implementation; do not promote an unrelated market-data dashboard or the management map into holdings authority. Adapter output is a projection, not a second hand-maintained book.

Each projected position needs account scope, instrument type, symbol, option expiry/strike/right when applicable, quantity, explicit disposition, source path/version and evidence vintage. Preserve UNKNOWN account identity, lot identity and capture time. A receipt date is not a quote/capture timestamp. An absent row is not sufficient evidence of closure, especially for accounts missing from the latest export. If separate lots cannot be identified, refuse a lot-specific choice rather than invent IDs or silently aggregate it.

Extend the existing explainer sidecar's header-driven metadata with a proposed `position_basis` field, bound per WQ decision unit. Each binding identifies its holding(s), accepted holding fingerprint, owner card path/hash and explicit scope (held-position action or separately proposed new entry). A fingerprint covers identity, quantity/disposition, account scope and relevant evidence identity; routine market-mark changes alone must not invent a new investment decision. Portfolio-relative recommendations bind every relevant holding, not only the symbol in their title. Missing or ambiguous bindings on a held-position action fail closed.

Populate current factual displays from this adapter. Validate applicability BEFORE `render_unit` or any fallback control is produced. A closed holding, partial exit, changed account scope, changed owner card or changed bound portfolio basis withholds the affected current recommendation and its controls pending owner reconciliation. The existing PLAIN fallback is NOT automatically safe: its approve/decline meanings can still be obsolete. Cover bare buttons, PLAIN meanings, table/grid/peek and stored selection/export paths. Unaffected units on a combined card remain available under their own IDs.

Withheld units show the reason, source and responsible owner; old rationale remains clearly historical and cannot appear as current advice above disabled controls. Never automatically rewrite the owner's judgment, sizing rationale or approval consequences. Re-enabling requires explicit reconciliation to the current basis and the existing review discipline. A broker fill does not approve a new recommendation.

Capture each holdings, broker-evidence and owner-card input once; parse and fingerprint the SAME captured bytes. Never parse a path and then reopen its potentially changed contents to assign a fingerprint. Register those captured versions in the existing build/review evidence and validate their mutual consistency and continued acceptance/currentness before review promotion and delivery. Any detected change requires rebuilding/reconciliation; an unstable input cannot certify a current result. A holdings change after generation invalidates the dependent current recommendation until rebuilt/reconciled; a reproducible old snapshot alone cannot certify a display as current. Hosted pages remain dated snapshots and cannot detect future changes while offline. At selection import/consumption, check the recorded basis again before treating a selection as applicable; no client-side or offline click executes anything.

Initial migration: enumerate all current held-position decision units, then explicitly bind or withhold each; do not silently leave older unbound trade rows actionable. Preserve historical rows. Non-position decisions keep their existing behavior. A genuinely new-entry proposal is explicitly classified and retains Will's approval boundary rather than being mistaken for a closed held-position action.

### Acceptance before implementation

| ID | Required result / neighbour |
|---|---|
| A1 Ordinary | Frozen TLT/TBT reproduction: closed TLT cannot render a live held-position choice; TBT displays the accepted five shares and no ten-share premise remains current. A valid unchanged holding/card still renders usable controls. |
| A2 Overlap | Partial exit updates facts but withholds stale action meanings and relative-sizing rationale; closing TLT on a combined TLT/HBAN card leaves independently valid HBAN choices correctly keyed. |
| A3 Wrong owner | Same symbol in two accounts or option expiries/strikes does not cross-bind. A lot-specific choice with unresolved lot identity is withheld. No owner card is edited by the renderer. |
| A4 Missing information | Missing account export, explicit UNKNOWN quantity/state, malformed binding or missing card produces a named unavailable unit, never inferred closure/zero or bare fallback approval. Unknown capture time stays unknown. |
| A5 Concurrent activity | Induce parse-old/hash-new: read five shares, change the input to three before fingerprinting; the system cannot certify five against the three-share fingerprint. Parsing and fingerprinting must use identical captured bytes for every input. Alter bound holdings/card after build and before promotion/delivery; dependent output fails validation. Alter an unrelated holding and show only genuinely dependent portfolio units are invalidated. |
| A6 History and controls | Historical decisions remain readable; current stale prose, PLAIN controls, alternate views and stale saved selections cannot evade withholding. New-entry and non-position decisions retain their proper approval behavior. |

Use temporary repository fixtures, assert rendered behavior and induce a stale basis to falsify the guard. Do not test by counting words in live holdings. Candidate files: `PROME/tools/decision_deck.py`, a small PROME-owned adapter if necessary, `PROME/registry/WQ_EXPLAINERS.tsv`, its existing build/selection consumers and focused tests. Identify the selection consumer and complete binding inventory in the plan before editing it. FORGE data schema, TERRY cards and financial rules are not silently widened into this patch. L688's separate consumers remain open unless their own tests are included in an explicitly scoped episode.

## B. Delivery membership and evidence dependencies

### Proposed change

Extend the existing ARGUS manifest; do not discard its inventory. Path ownership and delivery role are independent attributes. Delivery is an exact path set plus commit identity, not a directory, Git username, last-writer guess or filename containing PROME. Mixed authorship stays SHARED; insufficient evidence stays UNATTRIBUTED per L402.

Three roles, with overlapping delivery/evidence membership allowed:

1. **Delivered:** all PROME changes since the recorded baseline that this closeout claims, including earlier mid-session commits, pending changes and PROME-authored nested inbox/data paths. Record provenance and frozen bytes or explicit deletion. The final commit's explicit pathspec is a subset of this complete delivery set, not a replacement for it.
2. **Relied-on evidence:** exact version, hash and dependent claim/artifact for each source supporting the delivery. A source may also be delivered. State whether the claim is historical/version-pinned or current-state dependent; current-state dependencies require freshness validation as well as persistence.
3. **Observed concurrent work:** retained inventory/provenance with an explicit reason it neither belongs to delivery nor supports its claims. Its unrelated edits/additions do not block. Ambiguous assignment remains unresolved, not automatically observed-only.

At freeze, record the delivery plan and dependencies, independent of the path-prefix inventory. Discover additions across the full perimeter, including excluded paths, and reconcile each potentially relevant candidate. Review checks the classifications and any unresolved items. Missing provenance cannot be cured by an observed-only label. Do not use blanket inbox exclusions.

At promotion, evaluate the same frozen delivery/dependency contract used by the gate and post-commit check. Explicit `--paths` validates the current commit set against this contract; omitting it cannot create a more permissive route. An empty list, missing/unusable baseline, malformed schema, unresolved delivery membership or unavailable required evidence returns a non-pass with a named reason.

At delivery, resolve a named commit to its full immutable SHA once and verify delivered bytes against that SHA. Check the actual commit paths against the reviewed explicit delivery plan, not only a caller-supplied list. Verify earlier claimed changes at their named commits and at the final delivery snapshot as appropriate; moving HEAD must not silently change the object being certified. Changes to the manifest's membership, roles, dependency versions or hashes invalidate its verdict and require review of the changed portion.

Dependencies must be reproducibly persisted before certification, using an existing committed owner version or an approved captured evidence artifact. If PROME relies on an uncommitted owner packet, it remains a real blocker until the owner commits, an authorized preserved snapshot is reviewed, or PROME removes the dependent claim. Never force the owner to commit unrelated work, commit their files for them, or reclassify used evidence to pass.

Keep existing receipt exclusions and consumed-move rules unchanged. Old manifests must either retain their prior strict behavior or require explicit re-freeze into the new schema; migration cannot silently downgrade old entries to observed-only. This addresses L367's shipping question and L402's attribution interaction; it does not declare their unrelated historical residue resolved. Report any remaining items separately.

### Acceptance before implementation

| ID | Required result / neighbour |
|---|---|
| B1 Ordinary | Replay today's four DEWEY packets using frozen temporary fixtures. Verified unrelated packets absent from PROME's named delivery commit do not block; the inventory still lists them. A normal unchanged delivery passes. |
| B2 Overlap | A delivered file committed earlier and modified again pending is reviewed at the new bytes. A file that is also relied-on evidence satisfies both obligations; delivered deletions/renames remain explicit. |
| B3 Wrong owner | PROME-authored nested inbox/data files are not hidden; unrelated foreign work inside PROME is not claimed. Same Git author/path prefix is insufficient; mixed or ambiguous contribution remains explicit. |
| B4 Missing information | Missing baseline, malformed manifest, unavailable evidence version, empty path list and unresolved membership cannot promote REVIEWED or satisfy a required review gate. Preserve rc semantics or document the exact compatible change. |
| B5 Concurrent activity | Unrelated packet additions/edits and moving HEAD do not change the named delivery result. Changed current-state evidence, role tampering or unreviewed delivered additions block. Named historical evidence remains reproducible if its live pathname moves. |
| B6 Caller parity | Freeze/promotion, gate with no explicit paths, and post-commit verification enforce the same membership. Omitting a delivered root/shared path or passing a truncated explicit list cannot evade the actual-commit comparison. Existing consumed-move tests retain their outcomes. |

Candidate files: `PROME/tools/argus_scope.py`, its focused tests, gate integration and exact closeout caller instructions where necessary. No bypass switches, relaxed baseline rule, broad index operations or automatic concurrent-owner adoption. This is a consequential control repair: one plan read, one result read with an independently devised counterexample, within the existing episode budget. Record IMPLEMENTED, TESTED, INDEPENDENTLY VERIFIED and STILL UNRESOLVED separately.

## Relevant already-approved maintenance and execution boundary

The current order is still L675's in-flight regeneration → L628 calendar visibility → L676 JANUS, with the later slots as that row specifies. Helm encoding L665 remains already ruled, with its recorded L647 ordering and L594 integration. No fresh approval is requested for those repairs and no unrelated reporting backlog is made a prerequisite of A/B by this proposal.

The in-flight repair's concrete delta is the existing `python3 scripts/orch_log.py view` after spawn registration and after result consumption in COMPLETION_SPEC and the playbook recipe. The view reports recorded activity, never verified liveness. It is not implemented by generating a view once in this planning pass.

For the calendar repair, current source fails the bundle's exact before-hash precondition. Refresh against current source rather than applying the old patch blindly; preserve its independent review history/residue and add VIOLET-behind-VULCAN coverage from L628. Keep direct calendar reads until the refreshed implementation is accepted. A hash mismatch establishes staleness of the whole-file precondition, not that the patch's logic is wrong.

For Helm, encode the effective manual/spine-audit-only publication rule and hosted-build-date treatment under L665. Owed publication remains separately required and unavailable in this runtime; a passing build/gate does not publish it. Do not migrate hosting as a side effect.

This continuation follows a Standard closeout with two correction passes; the local late-session rule favors documentation/read-only work. This pass produces the bounded plan and readiness evidence, not another broad live edit. At the next eligible fresh session, recover this plan and the existing order; implement the next authorized maintenance item, then schedule A/B as separate process episodes. If moving A/B ahead of a named approved slot is desirable, present that specific priority adjustment rather than assuming one. Do not require completion of the entire backlog.

## Review and delivery

reads: 2

2026-10-14 read 1 — native helper `/root/closeout_repair_plan_1014`, explicitly selected `gpt-6.1-sol`, read-only: one blocking design omission, parse-old/hash-new concurrency. Corrected A and A5 to require parsing/fingerprinting identical captured bytes plus consistency/currentness validation. The independent counterexample parses five shares, then hashes a concurrently changed three-share file; later hash checks alone would incorrectly pass.

2026-10-14 read 2 — same helper, changed portion only: blocker resolved at PLAN level, zero remaining blocking plan findings; no further correction requested. Explicit closeout receipt confirms both reads were read-only, all findings delivered, no unsaved findings or remaining assigned work. Plan review is complete; implementation/result review is not performed or implied.

Declared residue: identify the selection consumer and complete current binding inventory before implementation; mechanically establish role-tamper invalidation, full-perimeter/actual-commit checks and legacy schema behavior in implementation/result review. Historical replay is not executable acceptance coverage or live certification. These are implementation prerequisites, not further planning audits or claims of completion.

This is not a full-system audit or an implementation result read. Existing CATO diagnosis is the source, not an independent read of this newly written design. No new financial conclusion, gate level or approval is established.

Implementation status: NOT IMPLEMENTED. Acceptance cases: SPECIFIED, not yet executable regression coverage. Historical reproduction: VERIFIED as limited above. Hosted delivery: unchanged/unavailable. Observe ordinary closeout correction passes, unrelated waits and available effort receipts after deployment; do not claim a percentage saving from total elapsed time alone.
