# PROME boot proposal review — September 21, 2026

## Current disposition

**Phase 2 cleanup accepted with disclosed advisory residue at `dd9d0bfc7`; Phase 1 B1/B2/B3 remain closed within scope.** Independently reproduced 93,707 → 46,031 bytes (50.9% reduction), exact archive payloads, unchanged generated/guard sections and protected committed files. HANDOFF's budget breach is closed; the older manifest completeness attestation remains UNKNOWN. No blocking conservation defect found in the compared surfaces. Additional B4 advisory: the condensed HANDOFF repeats the historically incorrect WALTER “checklist installation unfinished” report; implementation is established, independent acceptance remains separate. B5 is the owner's disclosed imprecise STATUS archive pointer. Recommend short maintenance corrections and ordinary use, not another framework or broad cleanup cycle. No owner edits/sends or full boot rerun; await Will's next scope.

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
