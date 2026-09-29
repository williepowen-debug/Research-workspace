# LABOR LESSONS maintenance — CATO plan review, September 29, 2026

## Current assessment

**Implementation follow-up at `08008ad93`: accept the lesson rotation and fetch-guidance corrections.** LBR1's original coverage gap was addressed, LBR2/LBR3 close in the named scope. Two bounded actions remain with LABOR: fix false-fresh verdicts in the newly extended checker (LBR4), and correct the Challenger no-card exemption plus the stale October 2 calendar instruction (LBR5). Present readings are not challenged by these tests. Keep the gains; do not call the complete refresh control verified yet. No owner edits or messages by CATO.

## Original plan review — scope and evidence

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

## Original plan review — stop and delivery

Recommend the bounded owner pass; no new charter ruling or tool-build commission is needed for these documentation changes. CATO has not implemented LABOR's changes. Stop this review at the concrete recommendations above; an implementation follow-up should inspect the final diff, byte preservation, retained rules/links, active fetch-guidance copies and the repaired freshness/calendar disposition. No independent counterexample test suite is needed for this document-only plan. An actual refresh success remains future evidence.

`read_cap_check.py --agent LABOR` returned rc=0, **rotation_due=1**, LESSONS 32,285 and STATUS 13,970; its heuristic perimeter is only two detected whole reads, not fleet-wide certification. CATO delivery checks and publication receipt follow in-session.

CATO closeout: orphan advisory clean; weekday check clean on the three PROME files and this report; tracked whitespace check clean; no staged foreign work. CONTINUITY is 6,470 B, below the boot budget; the other CATO boot surfaces were not changed. No canonical figure, STATUS, shared memory or external packet changed, so consumer, ledger-nudge and memory checks are inapplicable. Exact report/continuity paths only will be committed; staged new-file whitespace is checked before delivery. Publication receipt and any shared push train are reported in-session.


## September 29 — implementation follow-up at 08008ad93

**Scope/concurrency:** Will supplied LABOR's completion receipt. Reviewed `d8ef31719` and brief re-pin `08008ad931873b7c9a0355285ae8599c0605fcd3`; HOMER STATUS/docket/ledger edits and an untracked archive were present initially and left alone. No pull, source fetch or owner edit. This follow-up examines the changed documents/code, archive retention, named consumer propagation and adjacent date/ownership failure cases. It does not reopen LABOR's labor-market grades or independently reproduce the reported 11:19 fetch probes.

**Accepted / closures.** LESSONS measures **22,125 B**, STATUS **14,399 B**; owner read-cap checker rc=0 and rotation_due=0 in its two-file heuristic perimeter. Thirty cold-index IDs are unique and descending; full IDs are 33/32/30; together all 1–33 appear. L-27 retains cross-product coverage and revised-input recomputation; L-28 retains forecast registration and conditional-base-rate assumptions; L-29 retains object-versus-value discipline. All six archive paths resolve. L-27/L-28 sections and old rotation banner occur byte-for-byte in the new archive; L-29's entire lesson text is identical, with only its trailing separator/blank lines omitted at archive EOF. This separator-only difference is immaterial and does not justify another rotation. The October 2/append re-trigger remains hot. LBR3 closes.

L-33, BD-35 and STATUS now agree on time-dependent route success, raw extraction, release-date verification and never grading from a summary. BD-35 remains openly unbuilt. LBR2 closes for these active surfaces. L-26 records the repeated JOLTS miss, corrects the missing-fetch diagnosis, and refers to an actual comparison now wired for JTSHIL and FLUR. The original plan defect LBR1 is addressed; new implementation limitations are LBR4 below. Challenger now has a dated modeled row; its exemption is reviewed separately in LBR5. NEXUS's STATUS pin correctly names `d8ef31719`. B3 remains required: the previous CATO report explicitly noted the skipped-read issue and recommended compliance without another boot gate. Automation covers these named comparisons, not all LESSONS content.

### LBR4 — Medium, open: newer mentions can mask stale live rows

`AGENTS/LABOR/scripts/spine_check.py` extends the series list but retains `status_obs_dates()`'s whole-file maximum over matching lines and all date tokens on each line. `main()` also treats any STATUS date ahead of FRED as FRESH while printing an equality sign. These are inherited mechanisms newly used for JOLTS/FLUR, not parser changes introduced by this commit.

Independent isolated checks execute the unchanged parser/main against temporary STATUS copies with explicitly stubbed FRED dates. [Replay](2026-09-29_1237_labor-lessons-plan-review_evidence/spine_probe.py) / [results](2026-09-29_1237_labor-lessons-plan-review_evidence/spine_probe_results.json): **11 cases, seven expected outcomes and four false passes.** Current STATUS passes; ordinary stale July JOLTS and FLUR fail rc=2; absent JOLTS/FLUR tokens and unavailable JOLTS source fail rc=2; unrelated history does not hide stale JOLTS. Thus the owner demonstrated a real improvement and the simple morning-date counterexample is independently reproduced under the specified source dates.

False-pass witnesses:

- Leave the live JOLTS row at July, append `JOLTS hires source retrieved: obs 2026-08-01; current table reconciliation still owed.` The gate returns **rc=0 / FRESH** while the live row remains stale. The equivalent Florida case also passes falsely.
- Put `JOLTS … obs 2026-07-01; FL UR obs 2026-08-01` on one line: the Florida date gets assigned to JOLTS and the stale row passes.
- Put unverified `obs 2026-09-01` on JOLTS while FRED says August: rc=0 and the final “matches FRED” claim, despite unequal dates and no verified primary override.

**Fix/closure:** bind each series to its canonical live row/date, keeping source/history notes from satisfying that row's freshness; treat conflicting, ambiguous or ahead-of-reference dates as separately unverifiable unless an explicit verified-primary override supports them. Do not blindly use either whole-file max or min, and do not let unrelated old history manufacture a stale alert. Keep the present valid/stale/missing/source-failure behavior. Close with independently expected tests for all listed failure families on both newly covered series. This is a freshness-control repair, not a claim that today's source values are wrong or a commission to redesign the whole boot.

### LBR5 — Medium, open: calendar exemption and carried instruction contradict the active rules/state

**New Challenger row, `docket/CATALYSTS.tsv:9`:** `NOCARD: no test can fire on this print` suppresses the card checker (actual classifier returns `NO-CARD`). Charter C2a requires a card whenever **at least two live tests ride a release**, not only when a trigger can complete on that release. The row names vector 2, vector 5 and T-09. Moreover, August is already **1 of 2** for vector 5's low-AI-share condition; September supplies both the second share observation and updated tech-YTD growth. August's +51.7% does not, by itself, prove September's conjunction impossible. No probability or forecast of that branch is claimed here.

**Correction:** remove the unsupported exemption and prepare the existing required form of grading card before the modeled October 1–2 report, or obtain an explicit ruling changing the applicability of C2a. A checker accepting `NOCARD:` is not authority to waive the rule. Name a `CARD:` target so the existing checker tracks the obligation. No new card mechanism needed.

**Pre-existing adjacent residue, `CATALYSTS.tsv:6`:** the active October 2 NFP row still says `LEG C cannot be met on 10/2 (JOLTS Aug prints ~Oct 6)`. STATUS and the amended card instead say LEG C was met September 29. This contradiction predates this rotation; it was encountered while checking the touched calendar, not caused by the rotation. Update the live row to the established grade/card amendment, retaining any historical statement as labelled history. No threshold change requested.

Closure: required Challenger preparation is represented and delivered before the print (or an actual overriding ruling is recorded), and the October 2 docket agrees with the already-graded LEG C disposition. These are the immediate calendar actions; the checker repair remains LBR4. Preserve the accepted rotation/fetch corrections and stop this review after the bounded findings; actual next-release behavior is still future evidence.

**Implementation-follow-up delivery checks:** owner read-cap check rc=0 / rotation_due=0; archive/index/link verification above; eleven isolated freshness cases retained; actual Challenger classifier returns NO-CARD; actual NFP card Amendment 1 confirms the calendar contradiction. Orphan advisory and weekday check clean; tracked whitespace clean; CONTINUITY 6,548 B, other CATO boot surfaces unchanged. Only CATO report, continuity and two reproduction files changed. No owner figure/STATUS/memory mutation or self-authored external packet; consumer/ledger/memory checks inapplicable. Exact staged/new-file checks precede commit; final fresh-fetch publication receipt remains in-session.
