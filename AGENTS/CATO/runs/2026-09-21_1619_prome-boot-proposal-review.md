# PROME boot proposal review — September 21, 2026

## Current disposition

**October 4 boot-friction investigation complete; recommend a bounded owner repair, not another boot framework.** The reported mechanical PASS / overall PARTIAL distinction is supported by saved evidence. Replaying the actual orchestration log found 478 repeated historical evidence gaps; 193 do not match the compact reader's single-token desk pattern. Compact output still requires 14 pages. Nine required cold-start documents total 194,890 bytes at this snapshot, before logs/conditional reads; the charter's amendment-history header alone is 5,327 bytes. The read-budget result excludes the charter as injected even though the explicit-read runtime path applies. Private Artifact/native fleet capabilities remain unverified in PROME's separate session and absent from CATO's exposed tools; the existing bridge pilot does not grant a replacement. [October 4 findings and proposed sequence](#october-4--boot-friction-in-ordinary-use), [reproduction](2026-10-04_prome-boot-evidence/). No PROME edits, live boot, BOARD advancement, sends or launches. Await Will's direction; prior unrelated approvals survive.

### September 21 disposition retained

**Phase 4 mechanically accepted at `24960e563`, with two confirmed owner-declared advisories (B6/B7); no additional blocker found in the inspected scope.** Independently reproduced 98 passing tests and isolated interruption/policy-change counterchecks. Read reuse remains limited to acknowledged USER/BOOT in caller-asserted retained context; checks run fresh without BOARD advancement. B1–B5 remain closed. Older manifest completeness remains UNKNOWN. This phase adds meaningful state-management complexity; faster boots and net token benefit are unmeasured. Recommend small advisory corrections and ordinary-use measurement before further expansion. No owner edits/sends/live boot; await Will's next scope.

## Initial proposal disposition (historical)

**Support the direction; tighten the first implementation batch before work begins.** Will requested help with PROME's concurrent boot-improvement work and supplied its conversation and proposal receipt. Reviewed proposal `7c8fcd566`, boot receipt `bbb8b8538`, and the specific read/calendar contracts below. This is proposal feedback, not implementation approval or certification of PROME's complete boot. No owner files, operating rules, messages, or BOARD state changed.

The first useful batch is calendar coverage and read-budget reporting. Put HANDOFF contract reconciliation before budget implementation. Move runtime capability disclosure earlier using the existing capability model; a new generic capability framework is not established as necessary. Leave archival restructuring, shortened-log execution, and incremental boots for later bounded work. Existing stopped PROME/WALTER reviews are not reopened.

## Evidence and findings

### B1 — Medium: the calendar needs separate prose and generated-view results

**VERIFIED:** `scripts/docket_view.py::segments` deliberately skips the generated markers; `check_view` returns zero with a zero-match caveat. The saved boot log `15-docket-view-drift-scratch-calendar-prose-vs-docket-.txt` records exactly that. `PROME/tools/prome_gate.py:1251` labels the result “docket_view drift (SCRATCH calendar prose vs DOCKET).” It names prose, but does not establish generated-view freshness. PROME's proposal correctly diagnoses this; zero matches alone are not a parser defect or proof of a stale live calendar.

**Reviewer-designed reproduction, executed:** loaded `scripts/docket_view.py` from Git revision `7c8fcd566` into an isolated temporary directory, with a six-column docket containing one PENDING event, `REVIEW_TEST deadline`, owned by PROME, dated 2026-09-22. Rendered a marked calendar under `## Catalyst calendar` as of 2026-09-21. Its prose check returned rc=0 and ZERO claims. Changed only the docket date to 2026-09-23, leaving the generated block untouched. The expected render changed, while the prose check again returned rc=0 and ZERO claims. This demonstrates the coverage boundary, not an observed missed operational deadline.

**Correction / closure:** retain the prose check and add the proposed generated-block comparison. Report their scopes separately. Define freshness against a declared evaluation date and rendering options; comparing only against the block's old as-of date can certify reproducibility while leaving today's obligations stale. Test a clock advance without a file edit in this first batch, not only in a later incremental-boot pilot. The isolated renderer also produced different output for unchanged source on consecutive dates. Missing/duplicate markers and unevaluable source must not pass. Use one stable source snapshot or detect changes during comparison.

### B2 — Medium: settle HANDOFF's read contract before wiring budget coverage

**VERIFIED:** `PROME/BOOT.md:53` requires top live entries; `PROME/registry/READS.tsv:108` declares whole-file reading and explicitly says the 3–5-entry retention bound is not read scope. `check_byte_budgets` has a separate fixed list omitting HANDOFF. A read-only execution of `python3 scripts/read_cap_check.py --agent PROME` returned:

`READ-CAP-RESULT v1 mode=agent rc=1 assessed=1 desk=PROME reads=7 over_budget=1 over_cap=0 manifest_defects=0 advisories=0 generated_flagged=0`

Its named over-budget file was HANDOFF. This is a declared-perimeter result; the zero manifest-defect count does not reconcile the manual disagreement.

**Correction / closure:** the proposal itself says “settle HANDOFF's read contract first,” but places documentation reconciliation after the first verified batch. Move this small contract decision into that batch's prerequisites; broader cleanup can remain later. Keep the current disagreement visible until resolved. If scoped reading is intended, identify an addressable region that carries every live obligation, rather than merely relabeling the file. READ_CAP rules 8 and 16 still apply. Consume the existing structured result, preserving rc=0/1/2 and `assessed`; distinguish size findings, manifest defects, and inability to evaluate. Preserve separate auto-memory limits and advisory/blocking classifications.

### B3 — Low: keep runtime disclosure a bounded extension of existing controls

**VERIFIED:** BOOT already specifies AVAILABLE / UNAVAILABLE / UNKNOWN capability semantics, permits unrelated work, and says credential presence is not authentication. The new boot receipt explicitly discloses absent private Artifact access and native fleet preflight. These disclosures support the proposal's direction; this review did not authenticate tool availability in PROME's separate session.

**Recommendation / closure:** expose the relevant tool requirements early and record evidence from the actual session. A shell credential probe cannot establish that a private connector is callable. Keep session visibility distinct from thread-local collaboration tools and recheck at point of use. Narrow the proposal's final “recommendations 1 and 2 first” wording so it does not accidentally commission a general capability subsystem alongside the explicitly bounded first batch.

## Verification and limits

- **Implemented:** this CATO report and its continuity pointer only; no proposed repairs implemented.
- **Tested:** isolated calendar counterexample with pinned source, `python3 -B -W error::ResourceWarning`; assertions passed. Read-cap check executed read-only; rc=1 was its expected finding, not a test crash. Full boot gate was not rerun.
- **Independently checked:** proposal evidence for the calendar exclusion, budget-list omission, and manual/manifest mismatch. This does not independently certify earlier CATO-authored boot-hardening or instruction work.
- **Unresolved:** owner disposition, exact implementation scope/text, implementation and independent result review. Speed savings, complete preservation of historical duties, tool availability in the separate runtime, actual live generated-calendar freshness, and full boot compliance were not established here.

Entry Git state: master at `7c8fcd566`, two local PROME commits ahead of the existing tracking ref, nothing staged, foreign `PROME/state/argus_baseline.json` modified. Preserve that file; no pull or stash. Some discovery output was truncated; the specific source clauses used above were recovered through targeted reads and execution. No completeness claim is made over the broader logs or manifests.

Closeout checks: scoped whitespace check passed; weekday check passed on DOCKET, GATES, WILL_QUEUE and the two authored CATO files; orphan advisory identified only the preserved foreign ARGUS baseline. No threshold, STATUS, ledger, or auto-memory edits trigger the corresponding conditional checks.

**Resume:** feedback delivered for Will's ongoing PROME conversation. Await the next proposed change or assigned bounded review; do not implement, send, launch, or reopen old residue automatically. Final exact-path commit and fresh-fetch push receipt are delivered in-session. Any shared push of PROME's already-committed work is separate from CATO's authored changes.

## September 21 Phase 1 implementation follow-up — fbfe85e36

**Scope:** Will supplied PROME's Phase 1 completion receipt while the support assignment remained active. Read the implementation plan, committed code/instruction changes, complete focused test file, and the two new ORCH_LOG review receipts. Git entry was master at `fbfe85e36`, no staged paths, only PROME's foreign ARGUS baseline modified. Source files inspected were clean against that revision. No production boot/closeout rerun, owner mutation, peer message, or new helper launch. Review-receipt contents are owner-recorded; native helper transcripts were not authenticated here.

**Accepted portions:**

- B1 generated freshness: the new CLI checks generated output separately using the caller's ET date/options, snapshots and identity checks. My own temporary fixture returned FRESH for a matching block, STALE after changing only the docket deadline, and STALE on a date advance without changing source or view. A handwritten edit does not stand in for generated freshness. Existing strict markers and snapshot failure cases are covered by the reproduced suite.
- B2: BOOT and READS now both require whole-file HANDOFF reading; both boot skill copies carry the opening-disclosure pointer. The gate calls read-cap with `--require-manifest`, parses the structured assessment/rc/counts, and keeps memory separate. The reproduced suite exercises missing/absent manifests, wrong desk, contradictory results, size/manifest overlap and memory execution despite manifest failure. Accepted as declared-perimeter reporting, not proof the manifest is complete or HANDOFF is within budget.
- B3: the opening instructions require actual-session tool evidence, distinguish native fleet from thread-local visibility, retain point-of-use authentication and allow unrelated work. No general capability subsystem was added. This accepts the instruction change, not execution in every subsequent boot.

### B1 surviving instance — Medium: invalid handwritten dates disappear from coverage

**Exact source:** `scripts/docket_view.py:363` (`md_date`) returns None for an impossible M/D date; `segments` removes None values. At lines 461–464, a segment with no surviving date is skipped before `eligible` is incremented. `PROME/tools/prome_gate.py:376` then labels dated=0 as EMPTY and accepts rc=0/unassessed=0.

**Reviewer-designed counterexample, executed through the public CLI and gate summary:** create a temporary six-column docket with L2 = `2026-09-22 / Alpha earnings / ALPHA / PENDING / - / -`. Create a view headed `## Catalyst calendar` containing one generated marker pair plus the handwritten line `9/31 Alpha earnings (L2)`. Render with `--write`, `--docket <fixture>`, and `--as-of 2026-09-21`. Invoke both checks with the same source/date; prose also uses the production section and ignore options. Results:

| Input/result | Observed |
|---|---|
| Generated block next to the malformed prose | rc=0; gate accepts FRESH, assessed=1 |
| Handwritten `9/31 Alpha earnings (L2)` | rc=0; gate accepts EMPTY, matched=0, assessed=0, unassessed=0 |
| Valid handwritten `9/22 Alpha earnings (L2)` control | rc=0; gate accepts assessed=1 |
| Invalid and valid claims on one line, separated by a middle dot | rc=0; gate accepts assessed=1, unassessed=0; invalid claim disappears |
| ISO-form impossible date `2026-09-31` | parser raises ValueError; unlike the slash-date case, the failure remains detectable |

**Consequence:** the new coverage summary cannot distinguish a genuinely empty handwritten scope from recognized date-shaped text that failed validation. This violates the intended separation between empty and unevaluable prose. The older M/D parser behavior predates this batch; the new summary inherits that blind spot. This is not evidence of a missed live deadline or a defect in the generated block's comparison.

**Concrete correction / completion condition:** preserve date-recognition/validation failure through the prose path and explicitly surface it as malformed or unassessed; do not silently drop it or label its scope empty. No new date vocabulary or broad parser rewrite is requested. Add the invalid-only and mixed-valid/invalid cases, plus a truly empty control, at the producer and gate-summary boundary. Respect the declared shared exit contract; if retaining prose rc=0, an unassessed/malformed count must make the advisory fail visibly. The generated freshness verdict remains independent. B1 stays PARTIAL until this case is corrected or its coverage limitation explicitly dispositioned by Will.

### Verification receipt and remaining limits

**Implemented by owner:** code and instruction changes in `fbfe85e36`; CATO changed only this report and continuity.

**Tested by CATO:** `python3 -B -W error::ResourceWarning -m unittest PROME/tools/tests/test_boot_coverage.py PROME/tools/tests/test_prome_gate_gates.py PROME/tools/tests/test_capability_class_WQ239.py` passed 60 tests. Independent temporary fixtures reproduced the surviving counterexample, the generated positive/negative controls, and rc=2 rejection of dotted, Unicode-dash and compact numeric docket dates. The latter independently checks the final owner correction that the earlier result reader had not reread. No live state inputs were changed by these experiments.

**Independent verification boundary:** acceptance above covers this owner implementation and named conditions only. It does not recertify prior CATO-authored boot hardening or instruction work. Owner-reported selftest totals and disposable full-gate runs were not repeated because no new concern required broadening beyond the executed suite and counterexamples.

**Still unresolved:** B1 malformed handwritten-date coverage; owner-declared HANDOFF size breach and older manifest attestation; unavailable private/native tools remain capability limits. Structural cleanup, shortened-log execution and incremental boot remain deferred. No claim of faster boots, complete manifest coverage, all-green operational health, or production adoption follows.

**Resume:** recommend the small B1 correction before calling Phase 1 fully accepted. Await Will/owner disposition or an assigned bounded recheck; do not repair active PROME files, reopen earlier reviews or begin Phase 2 automatically. Exact-path commit and fresh-fetch push receipt follow in-session; foreign ARGUS baseline remains preserved.

## September 21 bounded acceptance — 0d104a775

Will supplied the correction receipt and reported that PROME is now working on Phase 2. Reviewed the committed date-parser/test diff and `PROME/plans/2026-09-21_prose-invalid-date-correction.md`. The proposal and dated plans inspected still carry the original deferred cleanup directions; no concrete Phase 2 change was assessed. Will's current report establishes active work, overriding historical “deferred” language as a session-status description, without establishing its precise scope or completion.

**B1 CLOSED within the agreed coverage conditions.** Invalid M/D sentinels now survive segmentation, including header context, and are counted as unassessed before matching. Existing gate logic flags that result. CATO's public-CLI temporary fixtures observed: invalid-only unassessed=1; mixed valid/invalid assessed=1 and unassessed=1; invalid header with two claims unassessed=2; empty/valid controls correctly pass. An invalid claim beside a genuine date divergence retains rc=1 and unassessed=1. Generated blocks remain FRESH independently in each case. This closes the surviving instance recorded above; no expanded date vocabulary or whole-calendar correctness certification follows.

**Checks:** reran the same three-suite strict ResourceWarning command; 63 tests passed. The independent closure fixtures above also passed. Inspected inputs were clean against `0d104a775`; tests changed only temporary fixtures. No production boot rerun, owner edits, messages or helper launches. The owner's independent-reader receipt remains an owner report; CATO's own fixture results establish the bounded acceptance here.

**Remaining:** HANDOFF budget breach and older manifest attestation are not repaired by this correction. Phase 1 improves coverage reporting; it does not establish shorter boots, complete manifest coverage, tool availability or completion of Phase 2. Next review should use Phase 2's exact preservation conditions and changed artifacts, retaining every live obligation, approval and material caveat if documents are shortened. This is a review criterion, not a new build or standing rule.

**Custody / resume:** update only this report and its continuity entry; preserve PROME's foreign ARGUS baseline and concurrent work. Await the Phase 2 artifact or Will's next scoped request. Whitespace, weekday and orphan checks apply; no conditional threshold, ledger, STATUS or memory checks are triggered. Exact-path commit and fresh-fetch push receipt follow in-session.

## September 21 Phase 2 review — dd9d0bfc7

**Scope and result:** Will requested analysis of completed Phase 2, following his concern about bloat. Read the plan, current three startup surfaces, pre-change HANDOFF/SCRATCH narrative, changed STATUS queue/header, and named ledger dispositions. Compared protected regions mechanically. Accept the document-size and conservation work with the advisory residue below; this is not certification of every inherited domain claim or owner completion. No new mandatory companion, read-contract change, or code framework landed in this commit.

### Independently verified preservation

Archive payloads extracted strictly between PHASE2 markers match `git show 0d104a775:PROME/<surface>.md` byte-for-byte. `measure.py` recomputation:

| Surface | Before bytes | After bytes | Archived CRC32 |
|---|---:|---:|---:|
| HANDOFF | 41,296 | 10,003 | 3032627484 |
| SCRATCH | 25,943 | 18,455 | 2236125182 |
| STATUS | 26,468 | 17,573 | 136530883 |

Total 93,707 → 46,031 bytes; all three finish below the existing 22,785-byte stop. The prior STATUS_HISTORY is an exact prefix of the appended file. SCRATCH's DOCKET/WILLQ blocks and caution block are identical. STATUS from Owner lanes through Completion evidence is identical, preserving restrictions and unresolved KERNEL siblings. DOCKET, GATES, WILL_QUEUE, ACTIVE_DECISIONS, HEARTBEAT, BOOT, READS, both boot skill copies, and committed ARGUS baseline are unchanged between the source and result revisions. The foreign working-tree baseline remains dirty; this comparison does not authenticate PROME's historical transient handling of it.

**Live-state recovery:** WQ-274's incomplete book and separate resolving inputs remain explicit; VLO mirror completion is supported by L424, with staged shares/account/time still unresolved. L395's terminal disposition correctly retains L400 residue. L438's pending confirms remain on both HANDOFF and STATUS despite the closed parent. L381 NOT RUN is still available outside the PENDING-only calendar. L423 F3/F4, presence warnings, publication limits, owner/registrar disagreements, historical UNKNOWNs, and unverified consumer reads survive. The OSPREY vintage/operator/clock caveats and L432 unread-primary limit remain visible. Archived dated prices and old cap-slot counts no longer masquerade as fresh orientation. These are conservation checks, not regrades of those underlying claims.

**Read-only checks executed:** table check passed all three files; generated calendar FRESH at supplied 2026-09-21 date; Will-queue block agreed. Read-cap rc=0, seven declared cap-bearing reads, zero over-budget/over-cap, one rotation-tier surface (HEARTBEAT, outside this batch). `reads_check.py --agent PROME` returned rc=2/UNKNOWN because the 2026-08-31 attestation predates BOOT changes. This confirms the stated distinction between size compliance and complete read enumeration. No production boot/closeout gate or unrelated code suites were rerun.

### B4 — Low: historical WALTER installation error remains in the shortened summary

`PROME/HANDOFF.md` Owner work first bullet attributes “checklist installation unfinished” to the prior session. That is faithful to the old report but preserves a known incorrect status on the current startup path. `8d2c9b8ef` actually changes `AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` FALSE/INDETERMINATE rows; the current rows retain the correction, and `b1d6ff592` contains the later U1/U2 change. CATO's earlier stopping receipt already distinguished those implementations from acceptance. This is inherited stale wording, not a new lost obligation or an instruction to duplicate implementation; the current “read the owner's artifact” guard reduces the risk.

**Recommended replacement:** “WALTER consumed the packet at cb43e637f; S2 was implemented at 8d2c9b8ef and U1/U2 at b1d6ff592, with subsequent corrections. Independent acceptance is separate; check the current owner record before closing it.” Close B4 when HANDOFF explicitly supersedes the unfinished-installation claim, retaining the independent-acceptance limit. Do not reopen WALTER's full review or commission implementation again.

### B5 — Low: disclosed STATUS archive-navigation advisory confirmed

STATUS History reaches the existing archive, and the Phase 2 source snapshot is present, but the detailed rotation pointer still names September 18. Nothing is lost; recovery takes an extra search. Close at the next relevant maintenance edit by pointing directly to `archive/STATUS_HISTORY.md#phase-2-source-snapshot--2026-09-21`. This is the owner's existing advisory, not a second archival defect.

**Disposition / resume:** accept the cleanup; retain B4/B5 as low-impact wording/navigation residue and the unrenewed attestation as a separate unresolved control. Prefer these small existing-file corrections and ordinary use over Phase 3/incremental machinery. No measured latency or token savings, fresh financial facts, complete operational boot, or whole-fleet clean-state claim. Owner helper-review narratives were read, not authenticated at native transcripts; the independent checks above are CATO's evidence. Save this report/continuity only, run scoped closeout checks, commit exact paths, and fresh-confirm the push. Await Will's next request; no owner repair, sends or automatic expansion.

## September 21 Phase 3 review — b693a7efe

**Scope / disposition:** Will requested a check of completed Phase 3. Reviewed the implementation record, complete reader and new tests, producer output contract, BOOT exception and matching skill indices. Accept the bounded presentation change: only consecutive exact duplicate-reason UNKNOWN rows are grouped; all identities remain, other text stays verbatim. No new registry, cache, gate or recurring process. The added reader option is modest complexity with demonstrated text savings. Recommend ordinary use before further expansion; this does not commission incremental boot.

**Independent verification:** reran `python3 -B -W error::ResourceWarning -m unittest PROME/tools/tests/test_boot_log_view.py PROME/tools/tests/test_orch_closeout.py`: 29 tests passed. Read the saved `/tmp/prome-boot-codex-20260921-1608/checks/00-orchestrated-touch-closeout-evidence-wq-249-.txt` through every compact page, then independently expanded grouped rows back to their original lines. Reconstruction equals the original bytes exactly; all 201 full keys retain order and multiplicity. Full mode also reproduces the original. `measure.py`: 33,180 bytes / CRC32 1765509790 → 22,536 bytes / CRC32 3861198606, 32.1% reduction, two groups, four compact pages. JSON envelopes are excluded. Original source remained unchanged.

**Reviewer-designed counterexample:** a multi-page run of repeated identical identities, followed by a near-identical reason with an added action and Unicode, another group, CRLF row and unterminated final row, reconstructed exactly. Serialized-text page limits held. Same-size source mutation and view-switch continuation refused. BOM/unfamiliar-header inputs returned full-text fallback; invalid UTF-8 raised an error. These tests used disposable fixtures, not operational state.

**Instruction / custody checks:** BOOT still requires all pages, full logs elsewhere, original-log fallback and UNKNOWN for missing evidence; one-shot execution remains intact. Both skill copies match. Gate, one-shot runner, producer, BOARD cursor and committed ARGUS baseline have no changes in this commit. Foreign working-tree ARGUS changes were preserved; this is not a claim about historical transient handling. No live boot/closeout was rerun. Owner helper-review descriptions were inspected, not authenticated against native transcripts; acceptance rests on CATO's independent checks above.

**Prior residue:** B4 CLOSED: HANDOFF now expressly supersedes the WALTER unfinished-installation claim and retains separate pending independent acceptance. B5 CLOSED: STATUS directly links the existing Phase 2 archive heading. Both corrections are in `bef8fe23e`. Older manifest completeness remains unresolved; this review does not renew it, resolve operational UNKNOWNs or establish whole-boot speed/token savings.

**Delivery / resume:** only this report and its continuity entry authored. Scoped whitespace, weekday and orphan checks precede exact-path commit; fresh-fetch push receipt delivered in-session. No owner edits, messages or launches. Orient and await Will; no additional work assigned.


## September 21 Phase 4 review — 24960e563

**Scope / result:** reviewed the complete receipt helper, reader integration, refresh runner, gate dispatch/check inventory, new tests, instruction/manifest-note changes and owner review record. Mechanically accept within the declared retained-context limits, retaining B6/B7 below. Context identity is an assertion, not authentication. Fresh sessions/compaction cannot reuse instructions under the written contract; this code does not prove cognition or whole-boot completion.

**Independent checks:** strict ResourceWarning run of `test_repeat_boot.py`, `test_boot_log_view.py`, `test_boot_coverage.py`, `test_prome_gate_gates.py` and `test_capability_class_WQ239.py`: **98 tests passed**. Includes fresh time-sensitive/BOARD fixtures and check-inventory equality except `--advance`. Own disposable counterchecks confirmed: changing another policy input mid-pagination prevents acknowledgement; losing saved EOF state prevents acknowledgement; a completed rc1 original can receive a fresh rc2 observation without altering its original files; an inconsistent rc2 original never launches a refresh child. No live boot, refresh or BOARD mutation was run. Both skill copies match; committed BOARD cursor/ARGUS baseline unchanged. Foreign dirty ARGUS file preserved.

### B6 — Advisory: changed canon is invalidated but not delivered

Confirmed the owner's result-review advisory with an independent fixture: acknowledge USER, change root CLAUDE to a new rule, then request USER reuse. The result correctly returns FULL, but says only `page recorded; acknowledge after EOF`. Consume/re-acknowledge USER and reuse succeeds without the new CLAUDE text ever being delivered. `boot_reuse.py::read_with_state` detects a changed policy digest but discards the incompatibility reason. BOOT's opening says auto-loaded CLAUDE need not be reread except when debugging drift. Thus invalidating USER/BOOT reuse alone does not refresh changed canon in retained context. This is not a false cache hit or a newly undisclosed defect; it is the documented reconciliation limitation, now independently reproduced.

**Bounded correction / closure:** expose policy-basis invalidation and direct a read/reconciliation of current governing instructions before reuse resumes. A generic canon-change notice plus explicit reread rule can suffice; no new registry or framework is needed. Verify changed root/PROME CLAUDE becomes visible to the caller before treating retained instructions as current. Until then, do not equate successful re-acknowledgement with refreshed canon.

### B7 — Low advisory: refresh does not explicitly preserve the consumed spawn allowance

Confirmed the owner's plan-review advisory. Existing per-boot caps remain in PROME/CLAUDE and gate guidance; no executable launch allowance was added. However, BOOT's repeat paragraph does not say the refresh shares the original allowance. Close with one sentence that refresh creates no new per-boot spawn allowance; keep existing native preflight and authorization requirements. No fleet launches or cap changes are authorized by this review.

**Complexity / usefulness:** unlike Phase 3's presentation change, this adds persistent receipts, explicit acknowledgement, invalidation, locking/atomic writes and refresh directories. It is bounded but materially more machinery. `measure.py` over pinned Git snapshots: BOOT 23,887 → 24,402 bytes; PROME/CLAUDE 23,809 → 24,081; one skill index 3,168 → 3,370. USER stays 4,126 bytes. Eligible USER+BOOT text totals 28,528 bytes before page envelopes, a potential avoided repeat read only when receipts/context qualify. No measured latency or net token benefit; acknowledgement/tool overhead and mandatory fresh work remain. Prefer the two small corrections and observing ordinary repeats before expanding caching.

**Limits / delivery:** older manifest completeness remains unresolved; private-ruling/native-tool availability and carried operational obligations remain separate. Owner helper review is an artifact claim, not native-transcript authentication. Only CATO's report/continuity authored; scoped closeout checks and exact-path commit, with fresh-fetch push receipt delivered in-session. Await Will; no automatic advisory implementation or further phase.

## October 4 — boot friction in ordinary use

**Assignment:** Will supplied PROME's boot report and self-assessment and asked CATO to investigate. **Pin:** `5f7233fb7c5c1473d232ded65c1320affd3d06ea`; foreign BRENT/WALTER/PROME work remained dirty. This is changed-evidence follow-up to the accepted September boot changes, not a claim those changes were never useful. No owner edits or operational boot were run. Eighteen source identities and saved outputs are retained in [evidence](2026-10-04_prome-boot-evidence/). Read scope: boot/runner requirements, relevant charter clauses, PROME READS rows, saved receipt and check output, compact-reader implementation/tests, existing session-pilot boundary and Decision Deck storage references. Not a complete review of every gate, owner-source flag, financial claim or actual prior-session tool transcript.

### Supported behavior and verification limits

The saved `completed.json` has returncode 0/incomplete false; saved `gate.txt` reports 10 blocking and 25 advisory checks, with all blocking checks passing. That is **mechanical success**, not a full boot or healthy-fleet certificate. PROME's receipt correctly reports PARTIAL, unavailable tools, deferred source re-reads, unchanged Friday market context and no desk launch. The quoted 4m46s is user-supplied session elapsed time; this review does not attribute a precise fraction of that time to reading or tools.

The receipt says initial truncated reads were recovered, and that all check logs were read to EOF. Their existence does not independently establish what the other session consumed. CATO accepts those as owner reports, not a reconstructed execution trace. The existing BOOT and runner already require one bounded document page per output and offer `orch-compact-v1`; adding another reader or repeating the same instructions would duplicate a control.

### B8 — concrete presentation-cost gap in the existing compact reader

**VERIFIED:** `PROME/tools/boot_read.py:GAP_ROW` uses `\S+` for the desk label. `orch_closeout.py` emits the recorded label, including spaces/parenthetical roles. In this real log, 478 lines end with the exact repeated missing/duplicate-evidence reason; 285 match the pattern, 193 do not. For example, `VIOLET (Will's session, directed)` is preserved verbatim rather than grouped. The unrecognized text is not lost or falsely resolved: this is an efficiency limitation, not corrupted evidence.

`measure.py` on the saved log and replay: **93,391 bytes original → 78,159 compact**, a 16.3% reduction; **16 full pages → 14 compact pages**. All 478 repeated gaps are dated before October 4, spanning September 1–October 3. The same output separately reports 12 attributed receipts, four asks still working, 11 dark-before-ask records and inventory UNKNOWN. Those classes must not be conflated or dropped as history. All **29 existing log-view/orchestration tests pass**. A new isolated two-row counterexample groups `VIOLET` but not the otherwise identical role-qualified label, retaining both identities in each case. [Probe/results](2026-10-04_prome-boot-evidence/probe-results.json).

**Bounded remedy:** extend the existing presentation matcher to preserve and group the producer's valid full labels. Acceptance: spaces, parentheses, repeated identities and labels containing delimiter-like words preserve the complete identity/key/order; altered reasons and novel failures remain verbatim; digest/paging/fallback protections still hold. No receipt fabrication, ledger regrading or new registry. This is worth fixing but will not by itself eliminate the historical reading cost.

### B9 — the mandatory reading contract, not just execution, is expensive

**VERIFIED:** BOOT step 5 requires every named log to EOF and explicitly retains every identity in the compact exception. Therefore PROME was following the current rule by reading historical unknowns. Phase 3 removed repeated words, not repeated historical obligations. The old 33,180-byte September 21 log was reduced to four pages; the present log is materially larger. Phase 4 reuse is limited to retained-context USER/BOOT; it does not help a genuinely fresh session recover all the other live state.

`measure.py` over the current nine explicit cold-start documents gives **194,890 bytes** (root CLAUDE/USER; PROME CLAUDE/BOOT/HANDOFF/SCRATCH/ACTIVE_DECISIONS/STATUS; HEARTBEAT), before logs and conditional sources. This measures text, not tokens or latency. The charter alone is 34,340 bytes; its long Created/Updated amendment-history paragraph is 5,327 bytes. Saved read-budget output already names BOOT and SCRATCH as rotation-due. Existing size controls have detected part of the burden; another detector is unnecessary.

**Recommendation:** finish the already-detected current-state/history separation and move dated charter provenance behind its existing ruling-record pointers, retaining the current stamp, all live authority and unresolved conditions. Shorter line counts are not a success criterion: these files contain very long lines. A proposed future log-read contract could read current touches, outstanding asks, changed/new errors and inventory uncertainty in full, while carrying unchanged historical gaps as explicitly UNKNOWN totals by reason/date with an exact full-evidence pointer. This would be a **change to the read contract**, not a license to skip under today's instructions. Before adopting it, specify how a previously unseen old gap, changed reason, missing baseline, identity collision or source change forces full disclosure; preserve every original record. Do not simply classify old as irrelevant or backfill invented receipts to make the output quiet. No such change was implemented or approved here.

### B10 — runtime-specific read coverage is not represented by the green budget result

**VERIFIED:** the saved read-budget output grades seven whole reads and explicitly excludes PROME/CLAUDE as harness-injected. BOOT's non-injected-runtime branch explicitly requires reading that charter. The current checker perimeter therefore does not represent that explicit-read path. Root's whole-read rule and READ_CAP rule 20's harness-injection rationale need to be reconciled for this mode; do not treat the unconditional charter label as proof that an explicit read is free of cost or truncation exposure. This review establishes the perimeter mismatch, not that the bounded reader actually lost charter text.

**Correction/closure:** make the existing read declaration/report distinguish injected context from explicitly read documents, or visibly state the unassessed runtime branch until the owner reconciles it. The current 34,340-byte charter exceeds the root 32,550-byte whole-read budget if that branch is assessed as a whole read. Reduce stale provenance while preserving rules rather than raising a budget. The older manifest-attestation uncertainty remains; this is not a re-attestation of the whole fleet manifest.

### Capability limitation — B3's disclosure works, access remains separate

The Decision Deck uses a private Claude-hosted Artifact `rulings` store. Repository HTML and WILL_QUEUE are not a read of its unconsumed taps. CATO's exposed tool metadata contains no native Artifact read_db/write_db or fleet ListAgents/SendMessage; similarly named Pages/Sites/document tools serve different surfaces. CATO did not authenticate PROME's separate tool inventory or the private store. Thread-local collaboration is not fleet discovery.

The existing `PROME/tools/SESSION_PILOT.md` describes an opt-in bridge with scoped inventory and delivery evidence, unresolved global coverage and no fleet-wide activation. It expressly does not turn an empty inventory into owner-launch permission. A new bridge build or migration is not implied by this investigation. Full coordination requires a session where the actual required tools are exposed and verified, or a separately authorized equivalent; a model-name change or successful mechanical gate does not establish that. Until then, repo work can proceed with dependent ruling pickup/doorbells/preflight visibly withheld. Preserve legitimate committed ruling-relay pickup under the existing C2 grant; it does not replace querying all private taps.

### Existing noisy advisories and priority

The saved fire-time output repeatedly treats multi-path citation cells as single filenames. This is already registered to DAEDALUS at **DOCKET L593, October 9**, not a new CATO discovery requiring another instrument. Its real owner-source findings remain separate. L358 already carries boot-manifest/procedure residue; L378 carries the unresolved runtime closeout-consumer boundary. Retain those owners instead of starting competing cleanups.

**Recommended sequence:** first keep immediate domain/position obligations ahead of process work; for the next authorized boot-maintenance slot, repair the compact matcher and complete the existing text rotations, preserving all live conditions. Then decide whether the all-history log-read contract deserves a bounded current/changed-evidence replacement. Separately settle the operating runtime for private ruling pickup and fleet coordination. Do not add more caching or another boot framework on the strength of this one complaint. Success is an ordinary cold boot that recovers the same obligations with less mandatory historical reading, not just another passing unit suite.

**Disposition:** useful continuity was recovered; PROME's self-criticism is fair but underexplains the structural cost. Its initial batching was avoidable; the mandated historical reading and missing runtime access were not solved by reading more carefully. No owner fixes, sends, launches, hook changes or new monitoring were performed. CATO's earlier boot authorship limits remain: these are bounded follow-up findings and independent counterexamples to the later compact-view behavior, not independent recertification of all prior CATO-authored infrastructure. Stop at delivered diagnosis and proposed owner corrections; resume on Will's direction.

**October 4 verification/delivery checks:** 29 targeted log-view/orchestration tests passed under strict ResourceWarning; frozen-log replay and the role-label counterexample reproduced. Weekday check passed on five existing/readable paths: PROME/DOCKET.tsv, PROME/GATES.tsv, PROME/WILL_QUEUE.md, CATO/CONTINUITY.md and this report. CATO's absent STATUS/CALENDAR/workbook CATALYSTS were omitted. Direct startup bytes: CATO AGENTS6,465 / CHARTER9,921 / CONTINUITY19,520; root CLAUDE24,199 / USER4,626 / AGENTS4,991, all below32,550. Generic CATO read-cap remains rc2 CANNOT-EVALUATE because no local CLAUDE.md exists; not a pass. Orphan advisory found foreign BRENT/WALTER/PROME work only, preserved; no self-authored outside packets. Scoped whitespace passed. No STATUS, ledger, memory or governing-figure replacement triggered conditional nudge/memory/consumer checks. Only the continuing review, continuity and seven evidence files are CATO delivery; exact-path commit and fresh-fetch publication receipt will be given in-session.
