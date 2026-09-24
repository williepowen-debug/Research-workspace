# PROME file sweep — September 23, 2026

**Current disposition: owner corrections rechecked at `01bb6a9b0`; principal decision and task-state repairs accepted locally, with partial findings and two new bounded defects below.** PF2, PF3 and PF7 close within their stated scope; PF4's principal directions are corrected with a minor pointer residue. PF1 retains declared sizing/guard-summary residue; PF5 and PF6 remain partial. PF8 identifies a newly broken SYSTEM table row; PF9 corrects a false VLO-parser warning in the owner's receipt. No PROME files or hosted pages changed by CATO. Next: bounded owner corrections, retaining the disclosed deferrals; this CATO assignment is delivered, orient and await Will.

**Original audit disposition (preserved):** Will assigned a sweep/audit of PROME's files after startup orientation. CATO found seven actionable findings: six medium and one low. Existing review limits and deferred defects remain separate below. At that snapshot, current summaries could not consistently answer what was already approved, delivered, or still owed. The strongest finding was propagation: correct records and controls existed, but competing live summaries kept older instructions in circulation.

**Revision:** `1d8bf4e3570ae90cfa7e18e564f6183b6879d930`, clean `master` at audit entry and before report creation. Startup pull in this session confirmed up to date. No PROME/owner files, live state, cursors, receipts, rulings, or publications changed. No fleet sessions launched or messages sent. This audit does not reopen the accepted September 23 C1–C3 closeout corrections or HEARTBEAT correction loop; their bounded acceptance stands. This is a newly assigned, broader file sweep.

## Scope and evidence limits

Examined the active continuity/decision surfaces (HANDOFF, SCRATCH, STATUS, ACTIVE_DECISIONS), bootstrap/boot/closeout manuals and runners, SYSTEM, BRIEF and HANDBOOK. Inspected relevant sections of AUTONOMY, ROSTER, GIT_COORDINATION, COMPLETION_SPEC, CLOSEOUT_PROCEDURES, GATES_README, MACHINE_LOCAL and the cold/projection references. Traced selected current rows through WILL_QUEUE, DOCKET, WQ_EXPLAINERS, READS, WQ_LEDGER, ORCH_LOG, linked plans/reports and FORGE/TERRY evidence. Inspected the corresponding parser/gate code and generated local Helm/Deck previews.

The filesystem inventory covers 1,779 PROME files excluding `__pycache__` (including ignored files). **Inventory is not content coverage.** Archives, processed inbox history, research corpora, every proposal, every gate letter and every tool were not read in full. Large ledgers were read by selected complete records after structural enumeration. Truncated exploratory output was not treated as a complete read or absence proof; material cited records were subsequently read in bounded excerpts. The top-level Markdown relative-link scan found no missing targets within its stated syntax perimeter; it did not validate backticked paths, anchors or arbitrary inline references.

No external market facts, current positions, hosted page contents, private ruling-store state, native fleet presence or old runtime transcripts were independently verified in this sweep. Historical prices below identify contradictory record states; they are not current quotes or trading guidance. Owner publication/review receipts remain owner evidence unless explicitly stated otherwise.

**Authorship:** earlier Codex/CATO implemented parts of L381, L393 and the boot/review tooling. Checks of those changes are **author follow-up**, not independent acceptance. The original independent receipts retain their original scope. This report and its evidence have no separate independent reviewer.

Machine-readable measurements, 21 source hashes, diagnostic outputs, render excerpts and test results: [evidence](2026-09-23_1953_prome-file-sweep-evidence.json).

## Findings and concrete closure conditions

### PF1 — Medium: the live decision index still directs a completed VLO fill and omits it from the sleeve description

**Claim / artifact:** `PROME/ACTIVE_DECISIONS.md:38`, the live TERRY 004 row, still says `WQ-213 VLO ×3 = Will's hands Fri 9/18` and that the fill receipt closes WQ-213. The same row says `ENERGY = USO 37 sh ONLY` in its sleeve-sizing instruction, while acknowledging a VLO receipt vintage elsewhere in that cell.

**Verification / observed result — VERIFIED at local artifacts:** `PROME/WILL_QUEUE.md:64` records one of three VLO shares filled, two STAGED for Will's chosen day, approval already covering three, account/time unknown, and L412 resolved. `FORGE/STATUS.md:99` carries the one-share receipt with those limits. STATUS's VLO row already says the mirror pass is complete. A fresh `decision_reference.html` renders both obsolete ACTIVE_DECISIONS instructions verbatim. This is not just an old sentence in an archive: it is the In-flight view's current State/Next material.

**Consequence:** the next session can re-present the completed three-share task or use an incomplete sleeve inventory. No observed repeat order or sizing error is established; live-broker verification and no-execution guards remain binding. This audit does not certify the present book or decide the economic treatment of the refiner exposure.

**Proposed correction:** replace the pending fill instruction with the receipted one-of-three state and the remaining two-share authorization, preserving account/time uncertainty and owner-card conditions. Replace the `USO ... ONLY` scope with the owner-confirmed sleeve perimeter or a pointer to its current inventory; do not invent a fresh total or correlation assumption. Preserve all genuine standing guards.

**Close when:** ACTIVE_DECISIONS and the rebuilt In-flight card agree with WQ-213 and the owner receipt, distinguish filled from staged, retain current-book uncertainty, and no longer assert an incomplete current sleeve as exhaustive. Hosted delivery, if undertaken, requires its own receipt.

### PF2 — Medium: current Deck choices contain expired timing and a misleading no-add consequence

**Claim / artifacts:** `PROME/registry/WQ_EXPLAINERS.tsv:51,61,65`; WILL_QUEUE WQ-246/259/264 (`:37,30,27`); `PROME/HANDBOOK.md` Top priorities and `PROME/BRIEF.md` QUESTION.

**Verification / observed result — VERIFIED at sources and local render:**

| Row | Current rendered statement | Conflict or limit |
|---|---|---|
| WQ-259 | Approve publishes “tonight” and is stale again “in six days”; decline promises “One redeploy on 9/23”; recommendation remains HOLD for 9/23. | HANDBOOK/BRIEF now recommend waiting for the last owner grade at the **9/24 boot**. The raw queue also retains the September 17 framing. The fresh September 23 Deck therefore disagrees with the freshly corrected priorities. |
| WQ-264 | Approve starts a shadow run **Monday 9/21**. | The September 23 build offers a start already in the past. The raw queue explicitly says approval before 9/21 was needed to start that clock. No record inspected establishes that the trial began or allows backdating it. |
| WQ-246 | Decline means the position keeps its size “by default rather than by decision”; headline calls it the only add-gate on the position. | The same queue records a standing **Will-ruled NO-ADD**, and explicitly distinguishes BOND's underspecified thesis gate from TERRY's valid level-based entry card. The explainer drops that distinction and misstates why size is held. Its yes branch does retain NO-ADD, so the guard is not absent everywhere. |

All 23 open rows have explainers; the coverage check passes. Presence does not establish that the choice is current or accurately scoped. These are outside the earlier C1 correction's bounded priority/QUESTION edits; they are not grounds to withdraw that acceptance.

**Consequence:** the button's explanation can describe an impossible start or a different consequence from the authoritative ruling. Generic publication will reproduce the defects.

**Proposed correction:** reconcile WQ-259's current recommendation and timing at the queue and explainer together. For WQ-264, preserve the originally proposed start as history, state whether any observation has actually occurred, and obtain the owner's prospective start/end interpretation before promising one. Scope WQ-246 to BOND's thesis qualifier, preserving TERRY's separate entry card and Will's existing NO-ADD. No threshold, ruling or retrospective clock is set by this audit.

**Close when:** each raw row, explanation, recommendation and rendered choice agrees on the present decision, preserves the controlling guard, and promises no past-dated action. Local correction and hosted publication remain separate states.

### PF3 — Medium: the publication task still reports the pre-delivery state

**Claim / artifacts:** `PROME/STATUS.md:20` presents the two September 17 failed publications and “hosted versions ... 9/15” in its current operational queue. DOCKET L393 still says production publishing pending, native reference URL unavailable and WQ-253 explainer missing.

**Verification / observed result — VERIFIED discrepancy, owner-reported publication:** WILL_QUEUE `:56` records Will's September 22 instruction that WQ-265 is done because the Deck was refreshed, with a v35 publication and reference-page creation receipt. Current HANDOFF/SCRATCH separately record Deck-only publication and dashboard/Helm at September 14 vintage. The fresh Deck reports no missing explainer rows. STATUS and L393 did not integrate this later delivery evidence.

**Consequence:** a new session can restart the initial publication/URL-establishment task or describe the wrong hosted vintage. The standing per-closeout publication-cost instruction remains valid; WQ-265's closure explicitly grants no blanket future publication authority.

**Proposed correction:** update STATUS and L393 to distinguish the implemented split and owner-reported initial publication from any outstanding native link/store verification and subsequent unpublished changes. Use the actual surviving delivery condition; do not close L393 merely from an inference that all hosted prerequisites were tested.

**Close when:** current summaries point to the latest receipt and name only evidence/delivery still owed. A hosted freshness claim requires an actual hosted inspection; this audit supplies none. No new layout approval is required.

### PF4 — Medium: task titles and leading status still commission superseded work

**Artifacts and observed results — VERIFIED local contradictions:**

| Carrier | Stale direction | Evidence of actual remaining work |
|---|---|---|
| DOCKET L381; STATUS `:29`; SCRATCH continuity; HANDOFF older carries | `NOT RUN`; fix the wave-approval line first. | Current ORCHESTRATION_PLAYBOOK `:93`, COMPLETION_SPEC `:61–64` and CLOSEOUT pre-closeout item 3 contain the implemented reconciliation. The September 15 plan/result record and L381's own trailing addendum say implementation verified; **two ordinary-session observations** remain owed. The fresh reference page leads with NOT RUN. CATO author follow-up. |
| DOCKET L423 | Fourth parser review still pending. | ORCH_LOG **physical line 232**, `coldreader/l423`, records its delivery and F3/F4 unresolved. This is owner evidence of a delivered review, not independent verification that its repairs are correct. HANDOFF already acknowledges delivery. Its older row-233 pointer is off by one at this revision. |
| DOCKET L444 title; generated SCRATCH calendar; fresh Helm clock item | `ADD A session_id COLUMN` because the field is absent. | L444's own current explanatory state retracts this premise: the field already exists in `closeout_v1`; the remaining gap is **cap-bearing/exempt classification**, with no schema widening. SCRATCH's live carry says the same, but the generated headline still advertises the rejected build. |

**Consequence:** visible queues reward redoing implementation while hiding the actual observation, verification or classification work. A trailing correction does not repair the leading instruction consumed by a summary renderer.

**Proposed correction:** replace current titles/leading states with the actual remaining work and retain old descriptions in clearly identified history. Keep L381 partial pending observations, L423 partial pending its specific review tails, and L444's existing cap/authority/schema constraints. Do not infer completion of any residual leg.

**Close when:** source rows and both generated calendar/reference consumers direct only the surviving task. No repeat implementation or new approval gate should follow from the historical wording.

### PF5 — Medium: secondary instructions still conflict with the live procedure and custody rules

**Artifacts / verification / observed result — VERIFIED:**

- `PROME/SYSTEM.md:40` says **Full rewrite each closeout** for SCRATCH; CLOSEOUT's targeted-update rule applies at every tier and requires a no-op when nothing changed. CLOSEOUT_PROCEDURES Skip rules also retains “SCRATCH's rewrite.” Following the map can recreate the duplication the maintenance rule was designed to prevent.
- `PROME/SYSTEM.md:171` advertises `prome_gate.py closeout` **without a tier**. CLOSEOUT step 9 explicitly requires the actual tier. A mocked missing-review input through the production `check_review_manifest` records **advisory / ok=True / UNKNOWN** without a tier and **BLOCKING / ok=False** at `standard`. This tests the review leg, not the whole gate: the correct manual/runner still requires review and later content verification. No observed unreviewed push is inferred.
- `PROME/ROSTER.md:204` tells each desk to declare cadence by **editing its own row here**, while saying PROME will not populate the table. Root Git grants do not authorize domain desks to commit ROSTER changes. The inspected cadence design says PROME applies owner-declared cadence; it grants no general cross-directory commit exception. The table has only a default placeholder, not per-desk writable rows. This creates an incomplete delivery route, not evidence a desk violated custody. READS already demonstrates the existing alternative: owner declares, PROME transcribes with attribution.

**Proposed correction:** make SYSTEM and the remaining rewrite phrase point to the targeted closeout procedure; remove the tierless shortcut in favor of the canonical command/sequence. Clarify that cadence is the owner's declaration and PROME's attributed registration, using the existing packet route. Do not expand desk commit authority. ROSTER's same-session two-correction stop remains binding; this report does not authorize a third edit.

**Close when:** following each secondary pointer yields the same write scope, review requirement and declaration delivery path as its owner rule. Test missing-review behavior and one owner-declaration handoff; no new ledger or framework is needed.

### PF6 — Medium, existing unresolved control debt: the declared read perimeter is stale and contradicts the boot instruction

**Artifacts / verification:** `PROME/registry/READS.tsv:105–117,174–189,274`, BOOT step 3/3b, and both read checkers.

**Observed result — VERIFIED:** `read_cap_check.py --agent PROME --require-manifest` returns **0** within the declared perimeter; `reads_check.py --agent PROME` returns **2 / UNKNOWN**, identifying the August 31 attestation as stale after boot-defining changes. The manifest's GATES row itself declares that BOOT says “Read” while actual practice is bounded summary. BOOT still says Read; the registry header still says `read_cap_check` does not consume it, contradicted by the current run. PROME's rows do not enumerate the explicit WALTER LAST_COMPLETION §WILL_NEEDS read added to BOOT 3b. This is a concrete missing read in the declaration, not just an aged timestamp.

**Consequence:** a passing size verdict cannot certify complete boot coverage, and a fresh reader receives competing instructions about GATES. This was already disclosed in earlier boot work and DOCKET L358; it is **reverified existing debt**, not a newly discovered failure of the accepted Phase 4 correction. No observed missed Will request is claimed.

**Proposed correction:** re-enumerate the actual current boot dependencies, reconcile GATES' verb with the intended bounded operation, correct the obsolete registry header, and re-attest only after that review. Do not lower declared modes to make sizes pass or treat summaries as evidence that full inputs were read.

**Close when:** every mandatory read is represented with its honest mode, the manual and runner agree, and the coverage checker can assess the current attestation. The current capacity check's narrower pass remains valid.

### PF7 — Low: the L393 regression fixture no longer satisfies the parser's input contract

**Artifact:** `PROME/tools/tests/test_decision_deck_split.py:25–33,48–52`; current `decision_deck.py:189–204`.

**Verification / observed result — TESTED, CATO author follow-up:** the selected suites ran **50 tests: 49 passed, one failed**, no errors. `test_partition_retains_full_content_and_actions` fails because its temporary OPEN table has no header. The current parser treats the first data row as its header, dropping the row containing `Full what`. Reproduced the failure directly; inserted only the required seven-column header/separator in the **temporary fixture**, and the same complete test passed. Production sources/tests stayed unchanged.

**Consequence:** a regression check intended to protect content preservation now fails on invalid setup. It does not establish a production content-loss defect with valid input; other split tests with weak content assertions may not reveal the malformed setup.

**Proposed correction / close when:** repair the fixture to the current contract, retain every content/action/navigation assertion, and pass the split suite. Do not weaken the production header check. This small test repair is lower priority than PF1–PF5.

## What passed, and what remains outside the recommendation

- WQ ledger check: 373 event rows, 14-column schema and append-only seal/order checks pass. Table check: no over-celled rows in seven declared whole-read inputs. Synthetic queue-parser parity: 26/26. These are structural tests, not factual or choice-semantic certification.
- Nine root/PROME agent/skill definitions compare identical. The inspected boot/closeout runners retain the required manual pointers. Parity does not prove agreement with every secondary map.
- Selected gate checks found no FIRED-UNEXECUTED row, no invalid leading GATES token across 20 rows, and no overdue live INSTRUMENT review. They do retain an overdue CORAL JUDGEMENT review advisory. This audit did not regrade it.
- Dashboard receipt/panels checks pass for the local September 23 build; **NEXUS split EMPTY** remains an advisory. It was not diagnosed to root cause here. Existing Brent/missing-tile and caveat-truncation residue remains deferred; no new dashboard repair is commissioned by this receipt.
- BOOT measures **24,398 B**, ACTIVE_DECISIONS **24,269 B** (`measure.py`); both are below the documented 24,412 B rotation trigger, with **14 B / 143 B** remaining. None of the seven measured cap-bearing inputs exceeds budget. This is fragility at the next edit, not an order to rotate now.
- Existing L455 owner-commit matching, L450 buried-state detection, L458 post-closeout baseline handling and historical helper/reader-evidence limits remain at their existing records. The accepted HEARTBEAT and C1–C3 correction loops stay closed. No broker reconciliation, hosted publication, fleet-wide census, new policy, trade or owner grade follows from this audit.

## Reproduction and delivery

Local previews (all outputs under `/tmp`, no feed/snapshot advancement):

```text
python3 -B PROME/tools/will_handbook.py --no-feed -o /tmp/cato-prome-sweep-20260923-helm.html
python3 -B PROME/tools/decision_deck.py --today 2026-09-23 -o /tmp/cato-prome-sweep-20260923-deck.html --reference-out /tmp/cato-prome-sweep-20260923-reference.html
python3 -B -W error::ResourceWarning -m unittest PROME.tools.tests.test_repeat_boot PROME.tools.tests.test_decision_deck_split PROME.tools.tests.test_dashboard_marks_L409
```

The diagnostic run invoked named read-only gate functions, **not** the operational boot/closeout runner. One exploratory probe used the wrong module attribute (`RESULTS` instead of `results`) and failed before executing a check; the corrected probe ran and its outputs are saved. The one test failure is diagnosed above, not reported as a passing suite. Temporary previews are reproducible; their relevant text is preserved in the evidence JSON, so this receipt does not depend on Will relaying temporary files.

**Recommended order:** reconcile PF1/PF2 decision content, PF3/PF4 current task/delivery states, then PF5 instruction mirrors. Address PF6 through the existing boot-perimeter work and PF7 at the next test maintenance touch. Use the existing owner records and required review discipline; no new process layer is proposed. A bounded repair should verify the rendered consumer, not merely the edited Markdown.

**Implemented:** CATO report, evidence and continuity only. **Tested:** structural diagnostics, local previews, selected suites and isolated counterexamples described above. **Independently verified:** bounded local content comparisons where CATO was not the implementer; no independent acceptance of CATO-authored machinery or this report. **Still unresolved:** PF1–PF7; proposed repairs and publication not undertaken. No owner response obtained or communication authorized.

Closeout checks: all 21 recorded source hashes still match after the audit; evidence JSON parses; report finding IDs and its evidence link checked. Git whitespace check, CATO orphan advisory and weekday check across DOCKET/GATES/WILL_QUEUE/this report pass. No auto-memory or published figure was changed, so the conditional memory/figure-consumer checks do not apply.

**Resume:** audit complete; orient and await Will's choice of a bounded correction or review. Do not automatically implement these recommendations. Exact-path CATO commit and fresh-fetch push verification follow in-session; no extra commit is needed solely to record its hash.

## September 23 follow-up — PROME's correction response

**Scope / revision.** Will relayed PROME's statement that all seven findings were verified and six corrected. CATO checked correction commit `01bb6a9b05209e96ed7d02caf79a40b9a3741168`, its parent diff, current source records, freshly rebuilt local Deck/reference/Helm, and the actual `catopf-result` ledger. The tree was clean on entry. This is a bounded follow-up, not another full sweep, owner takeover, operational boot, publication or assignment to clear PROME's other closeout tasks. Evidence is appended under `followup_2026_09_23_owner_corrections` in the existing JSON; the original audit evidence is preserved.

### Disposition of the original findings

| Finding | CATO verification at the correction revision | Disposition / remaining condition |
|---|---|---|
| PF1 | ACTIVE_DECISIONS and the local reference now distinguish one VLO share filled from two staged, retain account/time UNKNOWN and current-book uncertainty, include VLO in the sleeve, and restore the scaling/stand-down clause. The principal TLT guard values survive the diff. | **Principal defect repaired; disclosed residue remains.** The sleeve instruction still does not explicitly separate held exposure from staged proposed exposure, and the summary dropped TERRY's duty to record remaining fills and state the day-colour condition. The owner acknowledges these in its receipt. Clarify at the next authorized owner touch; do not invent current marks, an exit rule or a new approval. The old USO disposal history removed from this row is historical context, not itself a new trading guard. |
| PF2 | Both the raw WQ rows and explainers now present a prospective WQ-264 window, distinguish the September 15 candidate read from a shadow run, scope WQ-246 to BOND's thesis qualifier while retaining Will's July 16 no-add, and condition WQ-259 refresh on the recorded final grade. The local Deck matches. | **Closed for these local decision corrections.** Reviewer counterexample: if VIOLET does not record a grade on September 24, the yes-branch still says publication waits until the record exists; arrival of the date alone is not permission to publish. Dated historical phrases remain visible and labelled; a zero-hit claim about every old substring would be wrong. No broader satellite-evidence census or hosted inspection performed. |
| PF3 | STATUS and L393 now lead with the September 22 v35/reference receipt and distinguish later unpublished sources from native link/store verification still owed. | **Closed for publication-state descriptions.** Counterexample checked: WQ-265 being closed does not mark the native attachment check complete or authorize future publication. Actual hosted contents and the reported receipt remain externally unverified here. Earlier split implementation remains CATO author-follow-up, not newly independent certification. |
| PF4 | L381 leads PARTIAL with two observations owed; STATUS/SCRATCH/HANDOFF agree. L423 leads with the delivered fourth read and remaining F3/F4. L444 and the fresh Helm headline direct classification, not a new session-id column. | **Principal directions repaired, minor residue disclosed.** HANDOFF's L423 reference still says ORCH_LOG row 233; the named `coldreader/l423` is physical row 232. Correct the pointer on the next owner touch. Old docket descriptions are retained behind current state/history labels; no outstanding parser repair or ordinary-session observation is certified complete. |
| PF5 | SYSTEM and CLOSEOUT_PROCEDURES now require targeted SCRATCH updates; SYSTEM names the tiered gate and points to CLOSEOUT step 9. | **Partial.** ROSTER's owner-edit cadence instruction remains unchanged. The new SYSTEM row also has PF8 below. The owner-declares/PROME-transcribes route remains the proposed correction; no new cross-directory authority. |
| PF6 | READS adds WALTER's scoped WILL_NEEDS read and correctly says the capacity checker consumes the manifest. Coverage still returns rc=2 / UNKNOWN; capacity rc=0 within seven declared cap-bearing inputs. | **Partial.** READS lines 9–10 still say the heuristic convention REMAINS LIVE for every verdict until the checker consumes this file, contradicting corrected lines 3–8 and the actual declared-manifest run. Reconcile that current header as well as the GATES verb and full dependency census before re-attestation under L358. Adding one row is not full coverage. |
| PF7 | The diff adds only the missing seven-column fixture header/separator; assertions remain. The split suite passes all seven tests. | **Closed as tested fixture repair.** This is author follow-up to CATO's earlier split/test implementation, not an independent certification of all parser behavior. The broader original 50-test set was not rerun. |

**Deferral rule precision.** PROME's receipt says ROSTER had two correction commits that day and voluntarily applies the stop across the day's sessions. `PROME/CLAUDE.md:78` actually says the same file **in one session**. This review does not establish that a third edit was forbidden in the current session merely from daily commit counts, nor require overriding an owner's chosen stopping point. The proposed custody correction remains owed; no fresh Will approval is implied solely by the date of earlier commits. Existing read-budget and same-session conditions still apply.

### PF8 — Low: the tier correction breaks SYSTEM's Markdown table

**VERIFIED:** `PROME/SYSTEM.md:171` now embeds `--tier <bounce|light|standard|heavy>` in a three-column Markdown table without escaping the pipes. `python3 -B PROME/tools/table_check.py PROME/SYSTEM.md` returns rc=1: six cells under the three-column header at line 166. The checker identifies three dropped cells, including the remainder of the tier/review requirement. This is newly introduced by `01bb6a9b0`, separate from the original tierless instruction finding.

**Consequence:** a rendered reader loses part of the procedure that the correction intended to expose. The correct canonical manual remains available; this is not proof of an unreviewed closeout or a whole-gate bypass.

**Concrete correction / closure:** escape the option separators or use a plain pointer to the actual-tier command in CLOSEOUT step 9. Close when the explicit SYSTEM table check passes and its rendered rule retains the complete instruction. No new checker or operational gate run is necessary. CATO has not edited the active owner's file.

### PF9 — Low: the correction receipt carries a false parser-absence warning

**VERIFIED:** the owner's correction report at line 54 and the reader's warning 7 say the VLO row does not reach `positions_from_forge.py`, making it absent from the dashboard. The current parser already has the account-section support added September 20 (`AGENTS/TERRY/scripts/positions_from_forge.py:58–64`). A direct current extraction, `python3 -B AGENTS/TERRY/scripts/positions_from_forge.py --json --asof 2026-09-23`, includes VLO in `live`, quantity 1, group UNATTRIBUTED, account UNKNOWN. The recorded dated mark is not a live broker quote. This disproves the stated parser-absence premise; it does not certify a hosted dashboard's freshness.

**Consequence:** deferring this as a fresh TERRY/ANVIL parser repair would recommission work that is already done—the same propagation problem found in the original audit. The VLO approval-date mismatch is a separate provenance issue and remains deferred, not resolved by parsing.

**Concrete correction / closure:** add a correction to PROME's current receipt withdrawing the parser-absence claim and cite the existing parser behavior; preserve the historical reader ledger as evidence of what it actually said. Do not task another parser repair from this warning. Close when the active receipt separates actual remaining VLO uncertainties from this disproved premise.

### Independent-review scope and delivery limits

The actual `coldread_catopf_ledger.md` is preserved in the evidence JSON. It reviewed **PF1/PF2**, returned PF1 with caveats and **PF2 NO**, and found five blocking defects with its own counterexamples. PROME then fixed those in one pass and performed its own post-fix render check. CATO's fresh artifact checks above establish the inspected final corrections now; the earlier reader's negative verdict is not a positive review of the final bytes. This does not demand another same-session reader or waive WQ-178's stop: report review, author correction, final author test and remaining residue separately.

The user's relayed blanket statement that the corrections were cold-read before being called fixed is broader than the record. The report's PF3 row explicitly has no independent review and calls it non-consequential because it is a state description. That rationale does not match `PROME/CLAUDE.md` WQ-229, which explicitly includes a **Will-facing surface**. PF4–PF7 also have no independent-review receipt in that table; not every small edit requires one. Narrow the completion claim to the actual reader scope and the current CATO check, retaining the authorship limits above. Do not retroactively describe a missing pre-completion review as having occurred.

Local Deck/reference/Helm generation completed successfully; the split suite passed; the explicit SYSTEM table check failed; read coverage remains UNKNOWN while declared capacity passes. No operational boot/closeout gate, current broker check, native publication or fleet launch was run. No PROME source file, owner packet, approval or ruling was changed. The corrected hosted Deck remains a separate publication decision under Will's existing instruction; its current contents and the quoted token cost were not independently inspected.

**Recommendation / resume:** accept the principal local decision corrections, make the small SYSTEM/header/receipt corrections through PROME, and retain the named PF1/PF4 residue, cadence correction and L358 dependency work at their existing owner homes. This is not an assignment to clear overdue docket rows, change the firetime checker or prepare the spawn slate. CATO has delivered this follow-up; orient and await Will. Commit/push receipt is supplied in-session after exact-path closeout.
