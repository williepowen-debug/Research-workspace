# PROME boot proposal review — September 21, 2026

## Current disposition

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
