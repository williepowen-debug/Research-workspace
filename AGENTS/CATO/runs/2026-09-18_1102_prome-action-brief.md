# PROME action brief — CATO's past-day system review

**Prepared for Will to share with PROME, September 18, 2026.** Original review commit: `c0ef59790`. Follow-up checked against HEAD `deb3b093306e1afe54166182c12da9244e2276ef`, including PROME hook v4 `249950463`. Active SAM/PROME work preserved. This is a review handoff, not a grant of new repair, spawn, trade, or cross-owner authority; use existing approvals and owner boundaries.

**PROME: please disposition each item separately at its existing owner/task record.** For each, record who owns it, whether it remains open, what changed, and the evidence for closure. A packet sent, a passing old selftest, or an implementation commit alone does not establish that the counterexample is fixed. If already repaired after this snapshot, link the newer revision and test instead of repeating the work.

The [full report](2026-09-18_1102_system-review.md) supplies reasoning, source links, limits, and the positive findings. [Historical probes](2026-09-18_1102_system-review-probe.py), [output](2026-09-18_1102_system-review-probe.txt), and [check output](2026-09-18_1102_system-review-checks.txt) are the evidence bundle. **The probe script deliberately loads the old reviewed Git revision and asserts that its defects reproduce. It will keep reproducing those historical defects after repairs. Build equivalent acceptance checks against the new candidate; do not use the pinned probe's exit 0 as evidence of a fix.**

## Recommended order and ownership

| ID | Priority / status at follow-up | Owner / coordinator | Required outcome |
|---|---|---|---|
| A1 | High — OPEN | WALTER + LIQUID; PROME coordinates shared-memory and consumer correction | Withdraw incorrect FRED provisional-cell rule while preserving valid date-alignment discipline |
| A2 | High — OPEN | BOND; PROME checks WQ-157-facing summaries | Correct standalone versus subgroup success-rate claim before relying on it for WQ-157 |
| A3 | High — OPEN | BOND | Fix BND-26's publication cutoff before the September 23 grading boundary |
| A4 | Medium — OPEN | BOND | Establish or explicitly withhold the grader's claimed first-publication basis |
| A5 | Medium — OPEN | DAEDALUS | A normal runner invocation must not invalidate its own receipt |
| A6 | Medium — OPEN | DAEDALUS | Receipts must detect changes to the inputs actually checked |
| A7 | Medium — OPEN | DAEDALUS | Unrecognized child failures must remain UNKNOWN, with their original return codes |
| A8 | Medium — OPEN in hook v4 | PROME | Blocking subject hook must distinguish a command from arguments describing one |
| A9 | Completed CATO correction | CATO; PROME already performed recovery | Preserve accurate recovery provenance; no repeat recovery needed |

## A1 — Shared FRED lesson rejects valid data

**Problem and consequence.** Shared memory says a derived FRED series newer than its FRED component pages is provisional/unsupported. T10YIE and T5YIFR use inputs obtained directly from Treasury; separate FRED page lag does not prove their inputs were unavailable. This lesson can cause desks to discard valid new data.

**Exact surfaces to start with:**

- `memory/auto/finding_two_legs_with_independent_vintage_clocks_mix_dates_invisibly.md`: “PROVISIONAL-CELL LIMB,” structural detection test, instance count, retrieval keywords, and claims of independent confirmation.
- `BOARD/SIG-W-20260917-011-two-red-ft-rows-grade-on-derived-fred-series-that-publish-provisional-cells-ahead-of-their-own-inputs.md` and its routed copies/consumers at BOND, HENRY, and RED.
- LIQUID's KB-LIQ-133 and related report/packets, already covered by the September 17 CATO review. PROME's existing delivery is `59b56f1c8`; do not treat it as repair confirmation.

**Evidence.** [FRED T10YIE notes](https://fred.stlouisfed.org/series/T10YIE) and [T5YIFR notes/formula](https://fred.stlouisfed.org/series/T5YIFR). Treasury September 17 nominal 5Y/10Y = 4.78/4.94; real 5Y/10Y = 2.46/2.61. Breakevens = 2.32/2.33. FRED's formula yields forward 2.34000098%, rounding to 2.34%. Full report links both Treasury tables.

**Action.** Retract the unsupported/provisional inference and correct its propagation. Retain the valid rule that calculations must use the actual inputs' stated observation dates. Require producer-lineage evidence before classifying a cell as unsupported. Correct shared retrieval cues and any example totals that still count these as proven defects; do not erase the dated correction history.

**Closure evidence.** Corrected source text plus a list of affected consumers and their dispositions; reproduced Treasury calculation; no remaining live instruction that automatically rejects a spread merely because separate FRED component pages lag. No actual changed grade or trade loss was established by this review.

## A2 — BOND's 68% is a subgroup, not the standalone signal

**Exact surface.** `AGENTS/BOND/analysis/2026-09-17_FR2004_WEEKLY_JOIN_WQ-157-leg-2.md`, §4 table versus §7 second bullet (snapshot line 141).

**Problem.** §7 says standalone I-prime fires are followed by rising yields 68% of the time. §4 assigns 68% to only 22 fires without the dealer leg; another 30 fires have 27% rising yields. All 52 comprise the standalone signal. The reported table implies 15 + 8 = 23 rising cases, or **23/52 = 44.2%**. CATO inferred those counts from the table's rounded rates; BOND must verify them against the joined rows before publishing an exact corrected rate.

**Action.** Recompute and display all three populations: all I-prime fires, fires with the dealer leg, fires without it. Correct §7 and any summaries that transferred the selected subset's result to the full signal. BOND STATUS already labels the 68% subgroup correctly; preserve that distinction. PROME should check WQ-157's decision-facing account before the September 19 sitting.

**Closure evidence.** Explicit numerators/denominators from the underlying rows, corrected summary, and consumer check limited to this misattribution. The paired/unpaired difference need not disappear. **This correction supplies no authority to loosen or otherwise change a trading condition.**

## A3 — BND-26 finalizes before publications are due

**Exact surfaces.** `AGENTS/BOND/analysis/2026-09-17_grade_BND-25_BND-26_on_the_9-16_H15_cells.py`, final branches; BND-26 in `AGENTS/BOND/thesis/PREDICTIONS.tsv`.

**Problem.** Observation window ends September 23; missing sessions are excluded at September 30, 17:00 ET. The code starts finalizing on September 23 based on a local date only. Fixtures with missing later publications produce TRUE with three non-breach sessions or VOID with only two. Both are premature while later publications can change the outcome.

**Action.** Use distinct observation-window and ET-aware publication-cutoff checks. Keep an unresolved row OPEN while still-eligible publications can alter its grade. Preserve the original universe, strict/inclusive boundaries, residual branches, and the valid earlier fixes. No policy threshold change is requested.

**Acceptance cases.** September 23 and September 30 at 16:59 ET with incomplete publications must not finalize a non-breach result. At/after the actual cutoff, apply the registered insufficient-publication and TRUE/FALSE rules. Test the inclusive 4.95 boundary, a later-published breach, and differing host timezones. Demonstrate that BND-25's ten-tenor completeness, straddling ties, and all-zero VOID branch still behave correctly.

## A4 — “AS FIRST PUBLISHED” is not implemented by a current CSV fetch

**Exact surfaces.** Same BOND grader and BND-25/BND-26 vintage clauses.

**Problem.** The script's label claims first-publication vintage while its fetch reads today's FRED CSV. It neither selects a historical vintage nor stores the first-published evidence. A revised historical cell can silently change the supposed fixed-basis verdict. No actual revision-driven wrong grade was demonstrated.

**Action.** Bind grading to evidence that supports the registered first-publication convention, or state that the required vintage cannot be established and withhold certification. A desk's first observation after being dark is not automatically the producer's first publication. Do not silently change the letter to latest-revised data.

**Closure evidence.** Show a fixture where an original cell and a later revision differ: the registered original remains authoritative, and unavailable original evidence remains visibly unknown. Record the evidence source, timestamp, and values actually used.

## A5 — Runner self-invalidates through its ordinary log write

**Exact surface.** `AGENTS/DAEDALUS/scripts/daedalus_gate.py`: `run`, `fingerprint`, `verify_receipt`; spec A3.

**Reproducer.** Run with default `log_row=True` in an isolated repo. The receipt fingerprints the tree before appending `runs/GATE_LOG.tsv`; that append changes a fingerprinted input. Immediate `verify_receipt` reports INVALIDATED. The author selftest suppresses the log append, so misses this production path.

**Action / acceptance.** Resolve the dependency between receipt identity and generated trace writes. A completed ordinary run must verify immediately with no unrelated edit; a genuine later checked-input change must still invalidate it. Include the real logging path in the regression, not only `log_row=False`. Do not solve this by dropping all of DAEDALUS from the fingerprint.

## A6 — Receipt omits dependencies it claims to check

**Exact surface.** Same runner's `fingerprint`; closeout C5 checks PROME/DOCKET, GATES, WILL_QUEUE and other paths outside its current fingerprint perimeter.

**Reproducer.** Change an uncommitted `PROME/DOCKET.tsv` input after a run: the fingerprint does not change. A HEAD change is detected, but an uncommitted dependency edit is not.

**Action / acceptance.** Bind the receipt to the actual checked inputs, including relevant external-owner files and conditional inputs, or narrow the verification claim explicitly. Changing a checked input must invalidate the receipt; unavailable required inputs must remain UNKNOWN. Account for changes during the check as well as after it. Preserve unrelated active files; this work needs reads/fingerprints, not owner-file edits.

## A7 — Compound wrapper converts child failure to CLEAN

**Exact surface.** Same runner, closeout C2 consumer wrapper. Review neighboring handwritten compound wrappers for the same return-code handling pattern; simple `child_step` already maps unexpected codes to UNKNOWN.

**Reproducer.** Return `(127, 'fixture child failed')` from the consumer child. C2 reports CLEAN and rc 0. Its mapping handles only `None`, 1, and 2 explicitly.

**Action / acceptance.** Preserve every constituent child's native code. Unknown codes, signals, missing commands and timeouts must not become clean. Test 0/1/2, an unexpected code such as 127, and a subprocess termination; assert the correct per-child class and overall UNKNOWN dominance. Preserve DUE as distinct from both CLEAN and BLOCKING. For multi-child steps, retain their individual receipts rather than replacing them with a synthetic success code.

## A8 — Subject hook blocks an echo

**Exact surface.** `PROME/tools/hooks/commit_subject_guard.py`, executable/token recognition.

**Current reproduction, including v4 `249950463`.** `diagnose('echo git commit -m "' + 'x' * 101 + '"')` returns `block`, although the shell only prints text. The recognizer treats argument tokens as an executable command. Actual long commit also blocks and short commit allows, so the defect is false-positive discrimination, not missing wiring.

**Action / acceptance.** Recognize command position and supported wrappers accurately; uncertain shell constructs follow the already-approved fail-open policy. A plain echo or printf describing a long commit must pass; an actual supported long commit must block; short commits must pass. Preserve heredoc/prose protections and existing approved unknown-subject behavior. A parsing refinement is not permission to alter root policy or extend rollout.

**Already fixed — do not reassign:** runtime `$MSG` now returns UNKNOWN with an advisory; earlier CATO notes referred to the old silent-allow behavior. The pipeline hook and per-desk deployment perimeter were not fully recertified by this focused v4 check.

## A9 — CATO closeout provenance is corrected

CATO's previous continuity claimed an in-session commit/push receipt that did not occur. PROME recovered the four files on Will's WQ-262 authorization in `14b60d68b`, then packeted LIQUID in `59b56f1c8`. CATO corrected its continuity/report in `c0ef59790`; that commit's push was actually confirmed by safe-push and a fresh origin ancestry check. **No repeated recovery or new operational rule is requested.** Preserve the distinction between delivered review content and completed Git closeout.

## Existing adjacent work and scope boundaries

- The September 17 LIQUID review remains the detailed source for hidden UNGRADEABLE rendering, HY watcher missed-reset/terminal-state defects, incomplete composite wiring and its other findings. Those were already sent by PROME; keep that existing workstream visible. A1 extends the source correction to shared memory/routing rather than replacing that packet.
- The new BOJ 1.25% guideline takes effect **September 24**, per the primary. Distinguish announcement from effective funding rate when updating rate spreads. This review did not establish a live SAM error; SAM was actively updating its desk.
- WQ-247/WQ-250 implementation advanced after the original review snapshot. The original report's “drafts, not encoded” wording describes its pinned cutoff, not the later commits. Their newer final implementations are **not reviewed here**.
- Good results already verified are in the full report: strict ORCH schema, BOND's venv selftests and corrected power wording, WALTER's version alignment, and sampled ORACLE selector behavior. They do not close the separate counterexamples above.

**Requested return to Will:** concise item-by-item dispositions with repair commit(s), counterexample results, remaining limitations, and owner consumer acknowledgments where propagation is required. Keep receipt correctness separate from substantive claim correctness. No CATO task beyond preparing this handoff is currently assigned.
