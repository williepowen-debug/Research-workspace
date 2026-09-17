# PROME active-work review — September 17, 2026

Scope: Will requested review, feedback and suggestions on PROME's screenshot account while PROME remains active in another window. Inspected operating contracts, current/committed ORCH_LOG, SCRATCH, HEARTBEAT and its re-base receipt, coldreader definition, selected HAWK/LABOR delivery memos, WQ-254, and closeout instrumentation. Snapshot began at `54828a654`; HEAD advanced to `5b9d7694c` during review. BOND/ZHAO/PROME work was active. This is interim review, not certification of the eventual Standard closeout, all desk protocols, model telemetry, market facts, or publication.

No owner files edited, fleet agents launched, or messages/packets sent. CATO authored this report and continuity only. Earlier CATO implementation in the orchestration reader/contracts makes discussion of that implementation author follow-up; inspection of PROME's new ledger entries and contradictory resume text is review of PROME's work. No independent certification of CATO implementation is claimed.

## Findings

### F1 — High: committed closeout ledger cannot be read by its existing instrument

VERIFIED: `python3 PROME/tools/orch_closeout.py --date 2026-09-17` exits 2: `UNKNOWN: cannot enumerate .../PROME/state/ORCH_LOG.tsv: line 161: expected 13 columns, found 9`.

All 12 September 17 rows at physical lines 161–172 have nine columns, both in HEAD and the working tree. The header/reader require 13: the four omitted trailing cells are brief_defects, inbox_before, inbox_after, brief_defect_count. This is already committed, not only an unfinished working edit. Blank unknown cells are valid; invented zero values are not.

Consequence: the instrument cannot enumerate today's or unresolved earlier touches. PROME's hand-written green table is not evidence that the mechanical closeout check works. `prome_gate.py:1052` invokes this as ADVISE; a green overall gate would not prove this advisory succeeded.

Suggested owner action: preserve and reconcile the rows, restore the schema, rerun the reader, then reconcile expected touch keys to the actual native spawn record. Do not infer inventory completeness from this ledger. Longer term, use one existing-schema writer that validates before replacing the file and detects intervening edits; no new ledger or changed blocking authority is required for that proposal. Implementation not assigned here.

### F2 — Medium: committed resume instructions contradict completed work

VERIFIED: `PROME/SCRATCH.md:11` says the seventeenth HEARTBEAT re-base was committed. Line 13 still calls HEARTBEAT the September 14 pre-FOMC base; line 19 says it is 98% of budget, untouched this session, and waiting for a cold read. `HEARTBEAT.md:2` and commit `04dce15af` establish the September 17 re-base. The live meter reports HEARTBEAT 21,070 B, about 65% of budget.

Consequence: a fresh session could reopen finished work or follow obsolete edit restrictions. Suggested owner action: replace the superseded live instructions with the actual disposition and the re-base report pointer; preserve history in the archive. This is more urgent than polishing the session retrospective.

### F3 — Medium: receipt records do not consistently support the claimed ask→answer sequence

VERIFIED at the attributed ledger, not native transport: HAWK's recorded receipt is 12:35:33Z while its recorded ask is 12:35:35Z; BRENT receipt 12:45:32Z precedes ask 12:45:50Z; CARL receipt 12:47:51Z precedes ask 12:48:55Z. The three cold-reader rows likewise quote receipts preceding their listed asks. These may be unsolicited closeouts or timestamp transcription issues; this does NOT establish that the desks failed to close out.

Suggested owner action: reconcile against actual messages, use ALREADY_CLOSED where appropriate or cite the true preceding ask. BOND's row says UNKNOWN with an empty ask while its presence text acknowledges being told to close; preserve actual available evidence rather than reconstructing it. The existing reader validates structure, not free-text timestamp chronology or receipt authenticity.

### F4 — Medium operational debt: the read-cap pass is narrower than completion of rotation

VERIFIED: `read_cap_check.py --agent PROME` returns 0, with SCRATCH 31,712 B (97%), HANDOFF 29,238 B (90%), ACTIVE_DECISIONS 25,046 B (77%). All are rotate-tier; HEARTBEAT is below the 70% stop. These are snapshots, not live measurements to copy into operating prose.

Suggested order: reconcile contradictions first, then move historical narrative out of resume/navigation surfaces under existing rotation rules. Do not merely move dates/obligations into another duplicate summary. HEARTBEAT §C explicitly calls 600 B per channel a target that the gate does not meter; distinguish that target from the overall enforced budget. Its repeated overshoot justifies metering at re-base or a proposed target revision, not claiming an overall-cap failure.

## Assessment and suggestions

- The HEARTBEAT review produced useful concrete catches: contradictory bases, dates and pointers are documented in `PROME/reports/2026-09-17_heartbeat-17th-rebase.md`. Its final two corrections are explicitly labeled unreviewed. Preserve that limit; do not describe the final file as fully independently verified. The evidence does not establish that every research claim is externally correct.
- A named Opus desk definition is a sensible implementation proposal. The existing coldreader file pins `model: opus`, while the orchestration playbook still lists Sonnet/default and Haiku lanes. Reconcile those instructions with Will's recorded September 17 all-Opus direction; do not leave the new instruction solely in memory/SCRATCH. Verify an actual launch uses the intended model. No backend/model telemetry inspected here.
- Support a narrow coldreader output-file exception: one uniquely named report in the assigned scratch/output location, artifact under review remains read-only, final message gives the path and concise findings. This addresses truncation without granting owner-file editing. No such change implemented here.
- WQ-254 visibly preserves D1–D9 and asks for letter-specific rulings, which is useful. Grouping one sitting is reasonable, but nine choices still impose nine choices' worth of work. A row soft cap measures presentation size, not operator load. Keep the letter choices visible; do not sell row compression as throughput improvement.
- HAWK/LABOR memos provide substantive delivery and recovery detail. Their final checks/push outcomes are partly deferred to messages, so the memos alone cannot independently prove all green cells in the screenshot. Twelve touch rows exist today (nine desks plus three cold readers), making the screenshot's retrospective “eleven spawns” a count to reconcile to a named time/perimeter, not a stable total.
- The crash report supports successful Git recovery, not a hardware/root-cause diagnosis. “Ordinary bad luck” and model/runtime cost comparisons remain unproven. Prefer observed tool limitations and recovery facts over causal or model-quality conclusions.
- ARGUS's inspected review record remains September 15. That is expected during active work, not a failed promised closeout. The forthcoming closeout still needs its own candidate review, applicable checks, push receipt and separate publication status.

## Checks and disposition

Performed read-only schema comparison against HEAD/worktree, actual orchestration-reader invocation, PROME read-cap invocation, canonical measure.py receipts, Git/path inspection and source-contract comparison. No fixes or new tests authored. No full gate/renderer invoked because PROME's active candidate is not frozen. No external market-source verification undertaken in this operational review.

Owner response: none solicited. Findings delivered directly to Will; no assumption of permission to interrupt or message PROME. Review complete; fixes and final-candidate verification remain unassigned. Next CATO action: orient and await Will's chosen follow-up, rechecking current files before revisiting these snapshot findings. Closeout checks: root orphan advisory found only PROME-owned ledger residue; weekday claim check passed on DOCKET/GATES/WILL_QUEUE; diff whitespace check passed. At final inspection HEAD had advanced to BOND closeout `f2599a3a0`, BOND/ZHAO dirty paths had cleared, and the orchestration reader still returned the same schema error. No resulting desk closeout claim was independently audited. Commit/push receipt delivered in-session.
