# PROME response and retired-claim sweep proposal

September 20, 2026. Bounded review of Will's relayed response, proposal `25648708c`, docket correction `74089738c`, and existing CATO receipts. Initial HEAD `25648708c`, clean working tree and index. This is a context-aware follow-up, not the proposed fresh cold read. No policy, owner-file, communication, registration or implementation authority inferred.

## Disposition

Support advancing the draft to a bounded cold read before Will's ruling. The requested calendar distinction is now present, and the handoff reconciliation avoids duplicate delivery. The proposal correctly extends an existing consumer-check obligation, preserves history, and separates candidate discovery from semantic verification. Two design gaps should be explicit inputs to the cold read, rather than deferred until implementation.

## F1 — MEDIUM: trigger omits standalone task completion

The proposal's “proposed extension” triggers on retiring/superseding a claim or registering a prediction/commitment. Its acceptance condition 3 also requires completed checkboxes to reflect completion. A session can finish reading a document without registering anything or explicitly retiring a thesis; the stale UNREAD checkbox is then precisely the defect, but the trigger need not fire.

Suggested clarification: include completing or correcting a tracked task/state that changes an own consulted summary. Test a completed-document case with no new registration or thesis retirement. Do not depend on treating every task completion as an implicit “claim retirement.”

## F2 — MEDIUM: concurrency wording confuses review scope with commit ownership

The concurrent-activity neighbour says the sweep binds the authoring session's own commit set, not the live tree. If this limits the read set to edited paths, it misses untouched summaries carrying the retired claim—the motivating failure. If it means snapshot binding, it needs to say how the full named surface set is captured and how later edits invalidate the receipt. Git custody alone does not provide that guarantee.

Suggested clarification: inspect all enumerated own consulted surfaces, including untouched files, against an identified snapshot; recheck affected surfaces when they change before completion. Keep exact-file authorship and commit permissions separate. A concurrent edit should qualify/reopen the affected inspection, never justify committing another session's work. Test a source-only correction with an untouched stale STATUS, plus a summary altered after inspection.

## Additional drafting precision

- The tool is not wholly incapable of prose matching: `scripts/consumer_check.py` lines 956–963 already document literal nonnumeric tokens in `--mirror-map`, using PROME's canonical-mirror list plus own surfaces. That is not yet generic per-desk semantic coverage. Identify the actual scope/input gap before mandating code changes; reuse the existing capability where it fits.
- A labelled retraction may legitimately appear as a discovery candidate. Acceptance condition 6 should prohibit misclassifying it as a live defect, not prohibit discovery. Human verification is still necessary, especially where a retraction and a live contradiction share a paragraph.
- The “four evidence cases” list currently has three substantive numbered entries and a fourth restatement. SAM's two distinct surfaces could become separate fixtures, but enumerate them before claiming four test cases. Also retire the unsupported funding-gap claim, not the useful scenario model itself.
- Preserve the actual funding limitation: missing interim cash trough, financing-draw schedule, minimum reserves and availability assumptions. The proposal's deposits/trailing-OCF description is related but narrower than [F1](2026-09-19_2034_cruise-followup.md). Carrying it is appropriate; modelling it remains unassigned.

## Response verification and limits

`74089738c` changes DOCKET to distinguish eligible holiday-traded derivatives from closed cash markets and excluded futures. [JPX's dated notice](https://www.jpx.co.jp/english/news/2040/20260918-01.html) confirms holiday trading on September 21–23; [JPX eligibility](https://www.jpx.co.jp/english/derivatives/rules/holidaytrading/) excludes JGB and interest-rate futures. [BOJ's holiday schedule](https://www.boj.or.jp/en/about/outline/holi.htm) lists the same three dates for its offices. This verifies the requested JPX distinction and office holidays, not a comprehensive OTC JGB trading restriction or all possible BOJ operations. Direct primary links would improve the docket's current SAM-packet provenance.

SAM's docket explicitly maps ADDENDUM to CATO's `2137` ruling review and ADDENDUM 2 to the `2205` recheck. Existing CATO records also cover the R6 correction and TERRY withdrawal. No additional consolidated handoff is needed on the supplied inventory. This does not close the separate research limitations preserved in those records.

Only this report and CATO continuity were authored. No executable change or new tests were needed for this documentary design review. Closeout checks and exact-path commit/push receipt are delivered in-session. Next: orient and await Will; the suggested cold read is not launched and no canon change is approved.
