# RAV maturity review — what CATO should inherit

**2026-09-15 · CODEX, at Will’s request.** Repository reference: `ba3756c48befe79a2399d782569c6040c0d49448`. Read-only review of RAV’s operation; this report does not create CATO, rename RAV, amend authority or close old findings.

## Verdict

**RAV demonstrated useful reviewing ability, but did not develop a reliably maintained persistent operating setup.** Reuse its strongest methods and historical evidence. Build CATO’s current instructions and continuity deliberately, rather than copying RAV wholesale or merely changing its name.

The recorded maturity is **Meta / L2 / medium confidence**, with a September 1 review date in `AGENTS/DAEDALUS/FLEET_MAP.tsv` and a September 5 status amendment. Its stated L3 condition is a charter-conformant run report. That is the existing architect’s grade, not a new grade assigned by this review.

## What it actually accomplished

| Evidence | What it establishes | Limit |
|---|---|---|
| July 29 commits `919446861`, `943a15df6`, `e3d19b75a`, `383bf5813`; [DAEDALUS review](../AGENTS/DAEDALUS/upgrades/RAV_CHANGE_REVIEW_2026-07-30.md) | Real repairs: a signal-ID regex could silently truncate an identifier; shared BOARD instructions carried superseded routing policy; an enforcer omitted checking its own registry; a WAL routing recipient was missing. The historical independent review verified the work and identified mistakes in its execution. | This pass inspected selected original diffs and the audit evidence; it did not rerun July market/operational state or recertify every patch today. |
| [August 5 preflight](../AGENTS/RAV/runs/2026-08-05_roster-phase0-preflight-addendum.md) | Substantive review of a roster migration; specific navigation and authority/cadence distinctions. A later correction explicitly preserves the original record and fixes TERRY’s classification. | One report in the canonical run directory does not establish sustained compliance with the run-report contract. |
| [August 21 operating feedback](../PROME/codex/2026-08-21_RAV_operating-improvements-feedback.md) and [design review](../AGENTS/DAEDALUS/upgrades/RAV_FEEDBACK_REVIEW_2026-08-21.md) | RAV was already addressing many of our concerns: delivery versus consumption, PASS limits, stale summaries, correction propagation and regression fixtures. Several ideas were adopted after refinement. | Some suggestions rediscovered existing rules; the central correction store and hand-maintained authority map were explicitly declined as specified. |
| [August 22 doorbell review](../PROME/codex/2026-08-22_RAV_dark-owner-doorbell-review.md) | Concrete evidence-based review continued after the last RAV-authored home-directory activity. It identified case-normalization risk and distinguished read-only receipt from actual integration. | The report explicitly says Will relayed the review and PROME preserved it; it did not originate as a run report in RAV’s home. |

A search of reachable Git history for author `rav-codex` finds work through August 5. **That is not RAV’s last activity date.** Later relayed reviews exist, and DAEDALUS’s own maturity record warns that home-directory activity metrics miss them. Counting only that email or directory would give the wrong verdict.

## Main findings

### 1. Persistent startup and continuity are underbuilt

`AGENTS/RAV/` contains a README, one run report and four inbox packets. It has no local `AGENTS.md`, current continuity file or launcher in that directory. The README explicitly relies on handing the session its context. Its inbox convention says everything present is unprocessed; old packets remain without a read-marker, so their presence alone cannot establish that their work remains owed.

This explains the difference between having a useful reviewer available and having a reviewer that reliably resumes its own work. CATO needs a short entry point and current continuity. Directory-specific startup instructions are supported by Codex’s [AGENTS.md mechanism](https://learn.chatgpt.com/docs/agent-configuration/agents-md); RAV’s blanket claim that there is nothing for a harness to load should not be inherited.

### 2. The review record does not consistently live at its declared home

The charter requires one run report per run in `AGENTS/RAV/runs/`. Later reviews live in `PROME/codex/` and the reviewee’s DAEDALUS tree; some depended on Will pasting text into PROME. Useful work survived, but discovery and follow-through depended on other people and agents.

There is also an instruction conflict: `RAV_QC_WORKFLOW.md:21` calls the run-report home reconciled, then still says small reviews go directly into the disposition ledger. That leaves a practical exception to the charter’s every-run requirement.

CATO should have one durable review-output home, with a brief report acceptable for a small task. Its continuity should link to owner records instead of becoming a second operational task ledger.

### 3. The disposition ledger is not reliable as current state

The ledger contains seven review rows; all seven Status cells say `Open`. Rows `RAV-QC-20260801-004` and `-005` have dispositions beginning `CLOSED`. This is a directly verified same-row contradiction. The other old open rows were not re-adjudicated in this review and must not be imported as confirmed active work.

The useful idea is sound: every finding needs an owner, disposition and evidence. The implementation was not maintained consistently enough to use as CATO’s current backlog. Preserve it as history and revalidate any item before carrying it forward.

### 4. Its instructions lag the system they describe

The RAV charter still says YEYOU has never run and discusses composing with it on revival. Current ROSTER and FLEET_MAP record YEYOU’s September 5 retirement and say that revival path is closed. The charter/README also describe navigation wiring as outstanding, while `_INDEX.md:64` and `_SYNTHESIS_OPS.md:34` already contain RAV entries.

These are stale instructions/status descriptions, not evidence that the wiring never happened. A successor should inherit current owner references, not transplant the charter’s incident history and outdated registration checklist.

### 5. Good diagnosis did not always produce the right fix or proposal

Historical evidence records two valuable cautions:

- RAV removed a meaningful `(re-route)` suffix after its newly stricter validator rejected it. The original diff confirms the removal. The historical audit explains why the validator should have understood the record instead. Preserve the principle: **a new check’s complaint does not by itself authorize changing the underlying facts or deleting annotations.**
- RAV’s August proposals included controls already present and a central correction store that collided with existing ownership decisions. DAEDALUS explicitly identifies both discoverability trouble and mirror-vintage differences; this is not all attributable to careless reading. CATO should establish the reviewed revision, locate existing controls and name the actual remaining gap before proposing another mechanism.

RAV also initially classified TERRY as a service role, then corrected the report. An outside reviewer can be wrong; a different model/vendor is not independent proof of correctness.

## What to reuse for CATO

| Inherit | Adapt or leave behind |
|---|---|
| Ask whether the artifact is correct and whether its claimed completion is evidenced | Broaden the written review remit to the whole system and workflow Will wants assessed; keep implementation authority separate from permission to suggest improvements |
| Concrete failing scenario, exact source and honest severity | Long historical narration embedded in startup instructions |
| Clearly bounded repairs supported by evidence; meaningful records are preserved | A blanket restriction against fixes involving a newly added check; preserve the protection against self-justifying data edits without obstructing legitimate regression-driven repairs |
| State what was checked, what was not, and what a PASS cannot establish | Any assumption that cross-vendor output is automatically correct |
| Owner notification and respect for concurrent work | Outage-era assumptions that quiet Git history proves nobody is editing |
| Durable reports and evidence-backed dispositions | The stale seven-row ledger as a ready-made active backlog |
| Recheck whether a correction reached its consumers | Dependence on Will relaying the reviewer’s only copy of its findings |
| Source links to valuable RAV cases | Wholesale copying of RAV’s files or bulk renaming its historical record |

## Recommended CATO design direction

**CATO: Will’s independent reviewer of agent work, system reliability and completion, running on Astra through Codex.** The model is a launch choice; the role’s continuity lives in maintained repository records.

Start with a small charter, an `AGENTS.md` entry point, one concise continuity file seeded from our handoff, and the existing concept of dated run reports. Recommendations go directly to Will. Owners/PROME can provide implementation dispositions, while CATO separately records whether it verified the evidence; an owner’s claim of closure is not CATO’s verdict.

CATO can also perform approved repairs, but must identify those as its own work. Its implementation cannot count as its independent verification. Use a separate reviewer where consequential changes require one.

Treat CATO as a **successor to the review function**, subject to Will choosing the transition. Preserve RAV’s name on historical work and reconcile live registry/launch references in one bounded migration if approved. Avoid creating two overlapping standing reviewers or claiming that RAV’s maturity automatically transfers to CATO.

**First practical proof:** a fresh CATO session should find the current task and approvals without Will re-explaining them, deliver a source-backed review in its own home, and leave a usable handoff. Start with the existing PROME work; no new recurring audit program is needed to establish this.

## Review limits and delivery

This is a source/history-based maturity assessment. It does not grade RAV’s underlying model, measure a finding hit rate, establish all-time usage or prove current hosted/market facts. No RAV, PROME operational, WALTER or DAEDALUS files were repaired. CATO has not been created, registered, launched or granted authority. The companion Codex handoff receives only a pointer to this assessment.
