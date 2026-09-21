# PROME boot proposal review — September 21, 2026

## Current disposition

**Phase 1 follow-up at `fbfe85e36`: B2/B3 accepted within the inspected scope; B1 PARTIAL.** Generated freshness now detects changed deadlines and date advances; the HANDOFF contract and declared budget integration are present; capability disclosure stays within existing controls. CATO reproduced the reported 60-test pass and independently checked the corrected malformed source-date cases. One surviving B1 counterexample: an impossible handwritten slash date such as `9/31 Alpha earnings (L2)` is discarded before coverage counting, so the gate reports EMPTY and passes; in mixed input it silently omits the invalid claim. See the follow-up below. Recommend one bounded coverage correction, preserving the accepted repairs. HANDOFF budget and manifest-attestation residue remain separate. No owner edits or sends; await owner disposition or assigned recheck.

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
