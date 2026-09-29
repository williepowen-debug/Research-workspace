# LABOR LESSONS maintenance — CATO plan review, September 29, 2026

## Current assessment

Recommend proceeding with the rotation, with bounded changes to the plan: preserve both operational rules in each demoted lesson; correct fetch guidance at its active consumers; amend the existing L-26 recurrence instead of adding a duplicate L-34; and require reconciliation of fetched observations with live STATUS. A fetch or calendar entry alone is insufficient. No new monitor, charter rewrite or research project is needed for this lesson maintenance. This is advice to Will, not approval or an owner-file edit.

## Scope and evidence

Will requested review of LABOR's work and proposed LESSONS edits while LABOR is active. Shared HEAD at the final inspection: `963a0cfd996f9be24822a73c9f114ab4a3cc999d`; latest LABOR commit initially `09ad752f6`. LESSONS remains the unedited 32,285-byte version, SHA-256 `7b3bbafa76565e0095cb32e0d8fd19c136986a3a0925b842447b30a111ddafe8`. No post-edit artifact was available to certify. HOMER's rent script was concurrently dirty at the initial inspection; later committed by its owner. No pull, owner edits, messages or fleet launches.

Read the full LESSONS in bounded parts, relevant LABOR charter boot/closeout rules, archived L-26 case, current catalyst calendar, pertinent STATUS/BUILD_DEBT entries, full claims freshness checker and the data-fetch series list. Compared the pre-FLUR-change series list at `acaa1cd3f`. Broad combined output truncated; needed rules, original L-26 case and code were retrieved separately. Read READ_CAP rules 1–13 governing this rotation and ran its owner checker. Did not audit LABOR's labor-market figures, grade changes, full charter or the whole STATUS consolidation. The reported 11:19 HTTP probes and boot omission are owner reports; their execution was not independently replayed. This review does not claim which HTTP recipe works now.

## Findings

### LBR1 — Medium: proposed freshness rule would still permit the JOLTS failure

`labor_data.py:52–55` fetches JOLTS openings, hires, quits and layoffs, and did so before today's FLUR addition (same list at `acaa1cd3f`). `spine_check.py:70–73` covers only ICSA/CCSA. Archived L-26 explicitly says the landed July JOLTS observation was in the September 1 boot output but went unrecognized. Its existing remedy is to check for a landed observation before trusting a modeled countdown; the current hot index preserves the diagnosis but omits that action. Today's JOLTS lack of a CATALYSTS row is an additional routing gap, not evidence that JOLTS had no fetch. Florida lacked a fetch until today's FLUR addition; Challenger is still absent from the current eight-line CATALYSTS file. STATUS carries its next release as approximately October 1–2.

**Recommendation:** retain L-26 and append a short, dated recurrence explaining these different causes. Restore its actionable rule in the hot index. Suggested live rule: **Every decision-bearing STATUS series needs a refresh route and a check of the newest available reference period against its carried period; a newer observation triggers reconciliation regardless of the estimated calendar date. An unavailable source means explicitly stale/unknown with a next check. Calendar-only series need a dated source check, rolled forward after consumption.** Existing B2a/B5/C2 are the workflow homes; this does not commission automation or require a charter edit. Add the missing Challenger next-check row during the owner pass. Frozen/historical figures need not acquire live refresh obligations.

Closure for this plan concern: corrected lesson distinguishes missing ingestion from failure to consume fetched evidence, points at the existing workflow, retains the modeled-date early-arrival check, and the named calendar-only Challenger gap has a dated live row. No claim that actual next-release performance has already improved.

### LBR2 — Medium: L-33-only edit leaves the obsolete fetch prescription in live instructions

`LESSONS.md` L-33 says curl always fails and the fetch tool is the only route. **`BUILD_DEBT.md:62` BD-35 repeats that prescription**, while `STATUS.md:113` broadly states BLS/DOL HTML returns a denied stub. The plan should address these active copies rather than only L-33. Preserve the original September 17 incident as dated evidence; current reachability is an observation at a moment, not a permanent property. L-24's own successful recipe should likewise be labelled observed, not guaranteed.

A bounded sequence of fetch methods is reasonable. **`file` is a type check, not verification of a release.** Preserve L-33's stronger chain: save raw response → check expected type/parseability → extract raw text → verify publisher, release/reference dates, series and units → take figures from that text. Summaries are not evidence for missing figures; inability to obtain or validate the artifact means UNKNOWN. A real but stale PDF must fail the date check. For structured BLS API results, use the corresponding series/period/schema checks. Use the exact retained timestamped probe details if available; do not turn today's successful route into another universal rule. BD-35 remains open unless its actual build is delivered; rewriting the lesson does not complete that code.

Closure: revised LESSONS and these two active consumers agree, raw-artifact/date guards remain explicit, and no summary-only fallback can grade a print. No fresh network experiment or new fetch tool is needed to approve this documentation plan.

### LBR3 — Low: the budget is correctly measured but misdescribed as the truncation boundary

Independent byte count is **32,285**, leaving **265** to the **32,550-byte operating budget**. Canon READ_CAP rule 1 sets that budget at 60% of its estimated 54,250-byte read ceiling; it does not establish that the next 266 bytes immediately truncate this file or that L-27 is already missing. Rotation is nevertheless already due (trigger at 75% of budget). The required stop is **strictly below 22,785**, hence a net reduction of **at least 9,501 bytes**, after replacement index/banner/new prose. The proposed final 21.5–22.5 KB is an estimate to measure, not an acceptance receipt.

## Rotation acceptance and concrete retained rules

L-27 (3,570 bytes) plus L-28 (5,804) frees 9,374 bytes before index replacements. The 1,684-byte first section includes the introduction as well as the rotation log; not all of it is disposable log. Moving history is reasonable, but measure the finished file. Preserve original contiguous bytes in a named archive, independently compare archived payloads to the pre-edit Git blob, and check every new link. Recompute the checksum rather than trusting the archive banner. Keep all lesson IDs findable; sort the cold index descending by lesson ID and remove the stale “8 most recent in full” claim.

The index entries must retain both rules per lesson, not just their headlines:

- **L-27:** enumerate the cross-product of grading axes, explicitly assigning every reachable cell; freeze formulas and recompute values when their input series are revised. Point to the archive and the existing October 2 card, frozen September 24, rather than the fulfilled September 25 task.
- **L-28:** register, gate and score outcome expectations even when phrased as threshold sensitivity; name the regime and what invalidates it alongside any conditional base rate. Keep the archive pointer.

A two-line banner can hold the archive pointer and the already-docketed **October 2 recheck, or any append/edit first**, with rotation trigger/stop sizes. Do not move the operational re-trigger into cold history. B3 already requires reading LESSONS; the self-reported skipped read needs compliance with that rule, not a new duplicate boot gate.

## Stop and delivery

Recommend the bounded owner pass; no new charter ruling or tool-build commission is needed for these documentation changes. CATO has not implemented LABOR's changes. Stop this review at the concrete recommendations above; an implementation follow-up should inspect the final diff, byte preservation, retained rules/links, active fetch-guidance copies and the repaired freshness/calendar disposition. No independent counterexample test suite is needed for this document-only plan. An actual refresh success remains future evidence.

`read_cap_check.py --agent LABOR` returned rc=0, **rotation_due=1**, LESSONS 32,285 and STATUS 13,970; its heuristic perimeter is only two detected whole reads, not fleet-wide certification. CATO delivery checks and publication receipt follow in-session.

CATO closeout: orphan advisory clean; weekday check clean on the three PROME files and this report; tracked whitespace check clean; no staged foreign work. CONTINUITY is 6,470 B, below the boot budget; the other CATO boot surfaces were not changed. No canonical figure, STATUS, shared memory or external packet changed, so consumer, ledger-nudge and memory checks are inapplicable. Exact report/continuity paths only will be committed; staged new-file whitespace is checked before delivery. Publication receipt and any shared push train are reported in-session.
