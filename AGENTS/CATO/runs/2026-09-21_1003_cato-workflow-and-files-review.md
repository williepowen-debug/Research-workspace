# CATO workflow and file review

**Current disposition — September 21, after Will's explicit implementation approval:** C1–C4 are implemented and author-checked as detailed in the implementation addendum below. This is CATO's own repair, not independent certification. Git delivery is reported in-session after verification. No further repair is assigned by this record; other CATO instances are unaffected.

## Original assessment — before implementation approval

September 21, 2026. Will requested assessment of CATO's performance, file structure and possible guideline changes while PROME completes its own work. This is CATO's self-assessment, not independent certification. Scope: this conversation's SAM/PROME review cycle, local governing files/continuity and earlier relevant proposals. No overall accuracy, token-cost or time-savings estimate is claimed. Proposed guideline text below is **not installed**. PROME's active files and other CATO sessions are untouched.

## Assessment

CATO's most useful work today followed a claim to its actual consumer: the BROCK coverage annotation that suppressed the promised wake-up, the shell pipeline that converted failure into apparent success, and regenerated output that retained a completed task. Pinning commits and checking native receipts also distinguished real repairs from the owner's summary. Those concrete findings are valuable; owner acceptance and a different model family do not establish CATO's general reliability.

CATO also contributed to the correction loop. The shared-memory scope finding originally included both a universal measurement claim and an estimate/residual qualification, but subsequent short answers stressed only a quoted sentence. A later reply narrowed the ask to two copies while a second paragraph in one of those files remained part of the finding. The detailed record was more complete than the actionable summary. These were real owner omissions, but I should have made the remaining scope stable and unmistakable rather than repeatedly announcing an almost-final pass.

Likewise, “stop the broad review” repeatedly sat beside “not fully fixed.” Both can be true, but I did not consistently distinguish stopping the assignment from clearing its findings. The PROME verifier case further shows why output defects, procedure deviations and checker scope problems must be separated: committed content can match while a required verifier fails on foreign state. CATO eventually made that distinction; it should lead the finding from the first pass.

## Findings and bounded recommendations

| ID | Evidence and consequence | Proposed change / done when |
|---|---|---|
| C1 — Startup memory is a history file | `measure.py` at entry: CONTINUITY **46,327 B**, versus the root **32,550 B** whole-read budget; 40 paragraphs labelled Latest. CHARTER already calls it a short resume map. The September 19 proposal already identified the same failure; we continued adding history. | Preserve the old file verbatim, compact the live map to current task dispositions/approvals/links, then verify preservation and links. Roughly 500–700 words is a design target, not another binding cap. |
| C2 — Repair scope drifts between report and reply | SAM verification-scope finding, successive 08:06/08:42/08:53/09:00/09:07 receipts. The full scope and the final actionable list diverged. | Stable finding IDs and one list of active copies/consumers within the existing task report. Each unresolved item gets a concrete completion condition. Follow-ups update those same IDs; explicitly identify new scope. |
| C3 — Verdict language conflates different questions | SAM stop-versus-clear wording; PROME content-hash pass versus verifier/procedure failure. | State what is correct now, what did not happen, what remains unknown, and whether any further work is actually assigned. Link a procedural objection to the applicable rule and its consequence; do not imply corrupt output merely because a check failed. |
| C4 — Follow-up documentation grows faster than navigation | At entry, `runs/` contains 170 files / 90 Markdown reports across concurrent CATO instances; five separate September 21 SAM reports in this closeout sequence. Count is not itself a defect or a cost estimate. CHARTER already says one report per substantive task. | Preserve existing evidence paths; use dated addenda and a current disposition in one task report for a continuing correction chain. New report for a new assignment/scope, not automatically every pasted receipt. Keep individual probes/excerpts only when they materially substantiate a finding. |

The existing read-cap checker returns **rc=2, CANNOT-EVALUATE**, because it expects `AGENTS/CATO/CLAUDE.md`. It assesses zero files. This is a coverage gap, not a clean result. Direct `measure.py` results establish C1 without adding a fake CLAUDE file. Any shared-checker adaptation belongs in a separately scoped owner change; it is not necessary to compact CATO's memory.

## Concrete guideline replacement draft

This refines the [September 19 proposal](2026-09-19_1540_closeout-and-upstream-plan.md), rather than creating a competing methodology. Keep CHARTER's authority, independence and repair-acceptance rules. Replace its general opening Review method paragraph with:

> Begin from the assigned claim and the decision it affects. Pin the revision, distinguish pending work, and state the bounded conditions for closing the review. Follow the evidence through the authoritative record to the output or instruction its consumer actually uses. Separate observation, inference and recommendation.
>
> In the task report, give each finding a stable ID, practical consequence, concrete correction and completion condition. For propagated claims, name the active copies and consumers in scope, including shared memory and rendered output; retain clearly labelled history. A search result establishes only the stated search perimeter. Record any uninspected surface as a limit.
>
> On follow-up, check the agreed conditions at the new revision. Keep surviving instances under their original finding; identify newly introduced defects separately. Close repaired items explicitly. Distinguish content correctness, required process completion, checker limitations and delivery. Do not waive a binding control, infer failure from an advisory, or imply bad content solely from a procedure deviation.
>
> End with what can be relied on, the remaining actionable findings, and a recommendation to proceed, make a bounded correction, or stop with disclosed residue. Stopping a review does not certify every claim. Do not expand the audit merely because another example might exist; a user-directed stop closes the assignment. Do not use reviewer agreement or owner concessions as a performance score.

Replace CHARTER's “One dated report per substantive task” paragraph and findings/repair bullets with the same requirements plus:

> Keep one report per continuing assigned task, with a current disposition and dated follow-up sections. Preserve earlier observations and corrections; never silently rewrite history. A new assignment or materially different scope may get a new report. Use separate evidence files where they add reproducibility or preserve a necessary source. The short reply must name every material action still needed to close the agreed findings, or explicitly say which lower-impact residue is deferred.

AGENTS.md needs only two small changes; it should point to CHARTER instead of restating this method:

- Startup step 4: append “For a follow-up, read the task report's current disposition and existing closure conditions before extending scope.”
- Closeout step 3: replace with “Update the relevant task entry in CONTINUITY, replacing its superseded disposition and linking the report. Preserve other sessions' entries and existing approvals. Put history in the report or a linked archive. If nothing remains assigned to this instance, say to orient and await Will.”

## Proposed file structure

Keep `AGENTS.md` as the short entry point, `CHARTER.md` as the single method/authority owner, `README.md` as navigation, `launch.sh` unchanged, and `runs/` as on-demand evidence. No new KB, skill, scorecard, mandatory reviewer agent or closeout checker.

For the continuity cleanup, preserve a dated **verbatim copy alongside CONTINUITY.md**, e.g. `CONTINUITY_2026-09-21_ARCHIVE.md`. Keeping it at the same directory depth preserves its existing relative links. Mark it cold/history-only in README and the live map; it is not a new boot read. Do not reorganize existing run files or break their external links.

The live continuity should contain only:

1. Current task/instance scope and whether work is assigned. Multiple CATO sessions can run concurrently; one instance closing does not stop the others.
2. One latest disposition per relevant task, with its report link. Today that includes SAM **closed by Will**, PROME's latest reviewed revision with owner actively correcting, and pointers to other instances' latest CRUISE/OSPREY records without taking them over.
3. Still-valid authority/provenance constraints: manual-only registration, RAV transition unfinished, earlier CATO implementations remain author-follow-up, and no implicit owner-send/spawn/publication grants.
4. Older approvals or unresolved references that would otherwise be lost: L393's existing layout approval/publication restriction, L333 evidence limits, L381 observation obligations, foundation/authorship and recovery references. They are dated references to recheck, not new work orders.
5. The archive pointer and next action.

Before replacing live continuity: inventory active tasks and approvals from its current bytes, re-read for concurrent edits, retain the complete original, verify retained links and directly measure the compact result. Preserve another instance's in-flight status rather than inferring closure from Git inactivity. This is a bounded documentation change, not a license to grade or re-open any historical owner task.

## What I recommend doing first

Adopt the existing continuity cleanup with the compact method/output replacements above as **one CATO-only change**. Replace prose rather than adding another checklist. Judge the result on the next normally assigned review: does the first response state the full repair scope, does a follow-up address the same findings, and can the next CATO instance find the real resume point? Do not commission a benchmark or claim improved efficiency in advance.

This turn delivers assessment and concrete draft wording only; no governing guidance or continuity archive has been installed. Only this report and a short pointer replacing the older proposal's continuity paragraph are authored. PROME's active repair work and other sessions remain independent. No implementation is self-starting from this proposal. Next: continue only on Will's direction.

## Follow-up — implementation plan requested September 21

Will requested a plan to address these issues. Current disposition: plan prepared; implementation remains pending. This addendum continues the same task. The existing continuity pointer already identifies the proposal and implementation resume point.

Execute as one bounded CATO documentation repair, in this order:

1. **Preserve and map current state.** Re-read current CATO instructions and continuity, inspect the branch/index/worktree, and inventory each active task, approval, restriction and unresolved condition. Record where each will remain accessible in the compact map. Preserve other instances' entries; do not infer they are idle from clean tracked files. If another instance is editing a target, defer that file until its work can be preserved. Snapshot the exact continuity bytes immediately before replacement; if they change during preparation, refresh the snapshot and proposed map.
2. **Repair C1 in CONTINUITY.** Create a uniquely named dated verbatim archive alongside the original, then replace the live file with a roughly 500–700-word resume map. Retain current dispositions and material authority constraints in the live map, linking detailed historical evidence. Do not turn unresolved historical items into assignments. Verify archive byte equality with the captured pre-edit file, account for every inventory item, and measure the resulting live file against the root budget. Word count is a target, not permission to drop a restriction.
3. **Repair C2/C3 in CHARTER.** Apply the replacement review method above, preserving existing authority, independence and consequential-repair acceptance provisions. Require stable finding IDs, inspected revision, affected consumers, practical impact and a concrete closure condition. Follow-ups retain IDs for surviving instances and distinguish newly introduced defects. Final replies carry the complete material repair list and separate content, procedure, checker limits and delivery. A stopping recommendation must state any unresolved residue.
4. **Repair C4 and navigation.** Update CHARTER's durable-output wording to one report per continuing task, with a current disposition and dated addenda. Apply the two small AGENTS edits above. Update README to distinguish the live resume map, cold archive and on-demand task evidence. Keep existing reports and links in place; no retrospective report consolidation. The touched implementation paths are CHARTER.md, AGENTS.md, CONTINUITY.md, README.md, the new continuity archive and this task report, all within AGENTS/CATO/.
5. **Validate and deliver.** Check relative links, archive equality, preservation inventory, whitespace and direct file sizes. Read the edited guidance together for contradictions and duplicated authority. Walk the proposed wording against two existing cases without reopening either owner's work: SAM's surviving shared-memory copies should remain within the original finding's scope; PROME's foreign-file verifier failure should be distinguished from verified delivered content without waiving the required control. These are author checks of the wording, not independent certification or proof of future performance. Inspect exact commit paths, run applicable root closeout checks and obtain the safe-push fresh-fetch receipt. State any remaining checker limitation explicitly.

Completion means the compact continuity preserves the inventoried authority and resume points; the archive matches its captured original; every C1–C4 change above is installed and linked; and the checks/receipt are recorded. The shared read-cap checker still cannot evaluate CATO's AGENTS-based entry point: direct measurement validates this documentation repair, while changing that shared tool remains a separate proposal. No new recurring audit, mandatory reviewer or fleet work is part of the plan. Assess whether the method helps on the next normally assigned review; do not claim improved reliability merely because instructions were edited.

Recovery is a new exact-path commit restoring only this implementation's changes after checking for intervening edits. Preserve the archive and other sessions' contributions; do not reset or rewrite shared history.

## Implementation — approved September 21

Will said “okay approved. Go ahead and do it.” Starting revision: `e57f824d9ce668f6b7f56f7f6eb52cbac9fbf535`. Implemented only the six planned CATO paths: AGENTS, CHARTER, CONTINUITY, README, the new archive and this continuing report. The earlier assessment/plan above remains dated history; its pending/proposed wording no longer describes the current disposition.

| Finding | Installed repair | Acceptance result |
|---|---|---|
| C1 | Replaced cumulative continuity with a compact resume map; preserved its exact prior bytes in [the cold archive](../CONTINUITY_2026-09-21_ARCHIVE.md). | Archive byte comparison passed. Live map retains the inventory below and links detailed limits. Direct size measurement is below the root whole-read cap. |
| C2 | CHARTER requires stable finding IDs, named active copies/consumers, explicit scope limits and completion conditions; AGENTS starts follow-ups from that disposition. | SAM walkthrough below keeps both shared-memory residues within the same finding and makes the material repair list explicit. |
| C3 | CHARTER separates content, process, checker limits and delivery, and distinguishes stopping from clearing findings. | PROME walkthrough below preserves the failed-control disposition while accepting the scoped content evidence. Authority and consequential-control acceptance provisions are unchanged. |
| C4 | CHARTER uses one continuing task report with current disposition and dated addenda; AGENTS replaces superseded continuity entries; README identifies cold history and on-demand evidence. | This implementation continues this report. Prior evidence paths were not moved; all live Markdown links resolve. |

### Preservation inventory

The archive is the complete 143-line pre-edit continuity file, **46,053 bytes**, SHA-256 `3dae6b2da31b4a0501fdb710acf0a1ff8d14b23fc3b0796634dea9175914e8e3`. It was captured after the earlier proposal-pointer edit, so it is 274 bytes smaller than the assessment's initial 46,327-byte snapshot. Equality was checked against a separate pre-edit copy and the Git revision above. The archive stays at the same directory depth. The table accounts for source paragraphs by their archive line numbers; dated unresolved findings remain accessible without becoming new work orders.

| Source lines / subject | Retained location and disposition |
|---|---|
| 1–5 dated header | Replaced by current date/scope; original header retained only in archive. |
| 7 OSPREY | Live OSPREY entry retains the closed instance, narrow acceptance, C1/C2 approval gates, C3 HAWK dependency and owner obligations. |
| 9 PROME completion | Live PROME entry links the exact partial review and revision; later active owner work is not re-certified. WQ-265 publication deferral retained. |
| 11 PROME direction | Same live entry links the separate discussion and retains WQ-273/274 owner-report limits and Robinhood/expiry caveats. |
| 13–25, 29–35 CRUISE/PROME proposals and reviews | Live CRUISE entry plus general instance boundary; full chronological design, funding, yield, grading and options limits remain in archive/report links. Sweep/registration advice remains advice. |
| 27 SAM | Live SAM entry records Will's later stop and links the bounded receipt with unresolved qualifications. No automatic reopening. |
| 37 CATO proposal | Superseded by approved implementation and this report; original proposal retained in archive. |
| 39–67 prior SAM/PROME/system reviews and Carta investigation | Dated history remains in archive with its original report links and unresolved dispositions. Live historical-residue/instance boundaries prevent these from becoming assignments; Carta disable recommendation remains unexecuted history. |
| 71–91 system, LIQUID, DAEDALUS, PROME reviews | Archive retains limits and proposals. Live historical-residue entry directly links LIQUID's corrected recovery authorship and September 17 disposition index. |
| 93–107 standing remit, crash recovery, CARL/PROME and BRENT/WALTER repairs | Live closing paragraph retains the review remit; historical-residue entry links recovery; authorship entry covers prior implementations. Historical dirty counts are not current custody instructions. Detailed findings/receipts remain in archive. |
| 109–117 foundation, prior repairs and checklist recovery | Live foundation/authorship links retain manual-only registration, unresolved RAV transition and author-follow-up boundary; original verification/publishing limits remain linked. |
| 119–123 relationship/repository | Existing CHARTER/AGENTS/root sources remain authoritative; live map states owner/authority and review-scope boundaries. |
| 125–136 older approvals and obligations | Live L393, L333, L381 and sample entries preserve existing approval, publication limits, evidence limitations, observations owed, separate L378 and unapplied PROME sample. Detailed historical receipts retained in archive. |
| 138–143 constraints | Live foundation/publication/closing paragraphs preserve tool rediscovery, private artifact/ruling-store protection, concurrent custody, no imported RAV backlog and limits of startup testing. |

The separate CRUISE closeout discovered during this inventory is local `runs/2026-09-21_0822_cruise-cato-closeout_4c97a2.md`. It explicitly records no-Git/no-CONTINUITY restrictions and four uncommitted reports awaiting integration under separate authorization. The live map identifies this local-only condition rather than treating the files as delivered. All four files and the foreign pending shared-memory file remained byte-identical to their entry snapshots. They are outside this commit.

**Inherited archive link limitation:** 93 of the archive's 94 relative links resolve at their original paths. Its old `PROME/inbox/2026-09-15_from-CATO_manual-integration-proposal.md` target moved to [the processed inbox](../../../PROME/inbox/processed/2026-09-15_from-CATO_manual-integration-proposal.md). This is the same missing link present in the captured original. The archive remains verbatim; this navigation correction supplies the current location. The original proposal remains a proposal, not an activation grant.

### Author validation and method walkthrough

- Archive bytes equal the captured original; relative path bases are unchanged. All relative Markdown links in the four live guidance/navigation files resolve. CHARTER's entire purpose/authority/independence prefix and consequential-control acceptance paragraph compare byte-identically with the starting version.
- Direct `measure.py` checks cover all four live files; each is below 32,550 bytes. The archive is intentionally larger, cold and excluded from startup reads. The final live-continuity measurement is recorded below after its closeout wording update.
- `read_cap_check.py --agent CATO` still returns **rc=2, CANNOT-EVALUATE**, assessed zero: it expects CATO/CLAUDE.md. No shared tool was changed and no clean result is claimed. Direct measurement supplies the file-size check for this repair.
- **SAM example:** read the existing September 21 09:07 receipt, without touching owner files. Both the line-96 universal measurement claim and line-91 allocation qualification belong to its existing verification-scope finding. Under the installed method, a reply must retain both completion conditions, keep shared memory inside the declared consumer scope, and distinguish stopping from certification. No new owner review or correction was commissioned.
- **PROME example:** read the existing September 21 09:53 report, without rerunning operational closeout. Its eight committed-file matches establish scoped delivery evidence; the foreign uncommitted-versus-committed mismatch explains the verifier failure; neither waives CLOSEOUT's required zero exit or retroactively supplies independent review. Structured dispositions and stale consumer instructions are separate content work. The installed wording preserves these distinctions without reopening later owner revisions.
- These walkthroughs check the instruction text against recorded cases; they do not establish future adherence or independent verification. No new executable behavior was introduced, so code tests or a new recurring audit were unnecessary.

No substantive finding in this bounded CATO repair remains open. The shared checker coverage limitation and other sessions' custody are disclosed limits outside the implementation. Future performance can be assessed on the next normally assigned review. Resume: orient and await Will; no standing owner task, publication or fleet launch created.

Final pre-commit checks: CONTINUITY **5,244 bytes / 547 whitespace-delimited words** (from 46,053 bytes); AGENTS 3,788 B; CHARTER 8,529 B; README 2,078 B. All 29 relative links across those live files and all three links in this report resolve. Archive equality passed against both the pre-edit copy and `git show e57f824d9:AGENTS/CATO/CONTINUITY.md`; its one inherited moved link is dispositioned above. The five other-session pending files remain byte-identical. `git diff --check` passed. Root weekday claim check passed across DOCKET, GATES, WILL_QUEUE, live continuity and this report. Orphan advisory identified only the other session's shared-memory file outside CATO; preserved. No canonical research figure, STATUS/ledger or auto-memory was changed, so consumer-supersession, ledger-nudge and memory-index conditions did not trigger. Exact-path commit and fresh-fetch push receipt follow in-session; no retrospective independent-review claim is made.
