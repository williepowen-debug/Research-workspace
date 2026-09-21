# CATO workflow and file review

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
