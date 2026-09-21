# PROME boot: recommendations for consideration

**Status: PROPOSED — no operating rule or implementation changed.**
**Author:** PROME / Codex · **Date:** 2026-09-21
**Requested by Will:** “Write out a plan/recommendations to consider.”
**Evidence basis:** one Codex boot, recorded in [the boot receipt](../reports/2026-09-21_codex-boot-1608.md), committed as `bbb8b8538`, plus inspection of the instruments below. This is not a fleet-wide performance study or an independent review.
**Revision:** incorporates CATO's [independent proposal review](../../AGENTS/CATO/runs/2026-09-21_1619_prome-boot-proposal-review.md), commit `94fa87e5e`. CATO checked specific coverage contracts and executed an isolated calendar counterexample; it did not approve implementation or certify the full boot. This revised proposal has not yet received a result review.

## Recommendation

Improve the accuracy of the startup report first, then reduce the reading needed to reach it. Preserve the existing one-shot runner, digest-checked pagination, ownership boundaries, and explicit UNKNOWN states.

The main cost observed was reconstructing current state from overlapping summaries and historical records. The latest HANDOFF and SCRATCH entry supplied useful continuity; older work queues and long check logs then required considerable reconciliation. **Inference:** a smaller, reliably current read path would improve both speed and comprehension. This boot alone does not establish how much time or context it would save.

The first batch is coverage reporting only: separate calendar checks, resolve the HANDOFF read contract, then make budget reporting consume the declared-perimeter result. Earlier disclosure of missing tools is a small presentation change within existing controls. Document restructuring, shorter log reads and incremental boot are deferred until this batch is independently verified and separately scoped.

## CATO review disposition

| Item | Disposition in this revision |
|---|---|
| B1 — calendar coverage | Accepted. Preserve the prose check and add a separate generated-block comparison. Test a deadline change, a clock advance with unchanged files, invalid markers, unevaluable input and concurrent source changes in the first batch. |
| B2 — HANDOFF contract | Accepted. Move the scope decision ahead of budget implementation. Recommend whole-file reading for the first batch; exact proposed text and its cost are below. The live disagreement remains unresolved until the amendment is adopted. |
| B3 — capability scope | Accepted. Move existing disclosures earlier using actual session evidence. No general capability framework, new registry or launch adapter is proposed for this batch. |

CATO's counterexample changed an isolated docket deadline while leaving its generated calendar unchanged; the prose check continued returning rc=0 with zero matches. This establishes a coverage boundary, not an observed missed live deadline. CATO also found different renders on consecutive evaluation dates with unchanged source. These are reviewer-executed results, not tests rerun by PROME in this revision.

## Observations and their limits

| Finding | Evidence and verification | Observed result | Proposed response |
|---|---|---|---|
| **VERIFIED: the budget summary has a smaller perimeter than the declared read check.** | `PROME/tools/prome_gate.py::check_byte_budgets`; `python3 scripts/read_cap_check.py --agent PROME`; `PROME/registry/READS.tsv` | The gate's fixed list excludes HANDOFF. The separate declared-perimeter check flags HANDOFF over budget. | Reuse the existing read-cap result and state its perimeter. Keep auto-memory's separate cap distinct. |
| **VERIFIED: calendar success was reported with zero matched claims.** | `scripts/docket_view.py::segments` and `check_view`; boot log `15-docket-view-drift-scratch-calendar-prose-vs-docket-.txt` | Generated blocks are intentionally excluded. The log says “0 dated claim(s)” and “all covered,” followed by a warning that this proves nothing. The gate displays a passing drift check. | Separate generated-view freshness from coverage of handwritten date claims. Do not call this proof that the generated calendar is correct. |
| **VERIFIED: current and historical summaries coexist on required reads.** | `PROME/STATUS.md` Current Work Queue; `PROME/SCRATCH.md` NEXT and Operator card; latest HANDOFF | Newer completion statements coexist with older “owed” descriptions. The operator card was still labeled pre-open during an afternoon boot. | Retain one current summary per subject; preserve historical accounts outside the default read path. |
| **VERIFIED: full-log reading includes extensive historical exceptions.** | `BOOT.md` step 5 and the saved `00-orchestrated-touch-closeout-evidence-wq-249-.txt` | Current receipts are followed by many older UNKNOWN records. Those records remain unresolved evidence, not proof of an active failure today. | Present current obligations and historical exceptions separately, with complete evidence still retained. |
| **VERIFIED: runtime capability affects completion.** | Boot receipt; session-presence log; available tool inventory in this session | Private Artifact ruling pickup and native fleet preflight were unavailable. Disk observations could not establish current fleet absence. | Declare capabilities and their dependent steps at the start, then report completion against that declaration. |
| **VERIFIED: two read instructions disagree.** | `BOOT.md` step 1 versus the HANDOFF row in `registry/READS.tsv` | The manual says “top live entries only”; the manifest declares a whole read. | Decide the intended read and reconcile both surfaces. Do not reduce the declared perimeter merely to clear a size warning. |

The saved logs are under `/tmp/prome-boot-codex-20260921-1608/`. That is local, temporary evidence. Preserve the relevant logs with any implementation review before relying on them as durable fixtures. The committed boot receipt and source files are the durable entry points.

**Interpretation guard:** nine blocking checks passed. Neither read-cap nor complete runtime capability coverage was established by that headline. The passing blocking verdict was not itself false; treating it as a complete boot would have been.

## Prioritized changes

### 1. Make coverage visible in every completion claim

**Priority: first. Owner: PROME, coordinating shared-script changes with their owner.**

Use the existing check contracts and receipt files. Distinguish:

- The checks that executed and their findings.
- The scope actually assessed, including an explicitly empty scope.
- Required steps that were skipped or could not certify their scope.
- Capabilities unavailable to the runtime and the actions that depend on them.

For the calendar, establish two distinct contracts. A generated-view check compares the marked block with the current renderer output under the caller's declared evaluation date and rendering options. Normal boot uses today's ET date; historical replay must explicitly declare its historical date. Never infer the evaluation date solely from the old block's stamp: that proves reproducibility while potentially hiding today's obligations. The existing prose check assesses handwritten date claims. Zero handwritten claims can be legitimate; it must not certify the generated block. Eligible prose that could not be evaluated must remain distinguishable from an intentionally empty prose scope. Use a stable source snapshot or detect changes during comparison, including changes to the destination block and relevant rendering configuration.

**HANDOFF prerequisite — proposed decision, not an enacted rule:** use whole-file reading for the first batch, retaining the manifest's existing `whole` declaration. `HANDOFF.md` currently has no designated live-section heading; this revision has not proved an addressable subset carries every live obligation. Whole-file reading is the conservative interim scope, with a real context cost and an over-budget warning that remains visible. It is not the desired long-term compression mechanism. Do not relabel the manifest to remove the warning.

Proposed replacement for BOOT step 1, to be reviewed in this proposal before any transplant:

> Read `PROME/HANDOFF.md` in full using the bounded reader. The declared read mode is `whole`; the retention target does not limit read scope. Preserve any read-budget finding until the file is brought within its existing budget or a separately reviewed scoped read is adopted.

If scoped reading is chosen instead, first identify an addressable region, demonstrate that every live obligation and material caveat has a carrier within it, and apply READ_CAP rules 8 and 16. Budget integration waits for that decision; calendar work can proceed independently. This batch does not rotate HANDOFF or weaken its budget.

For budgets, consume the existing structured `READ-CAP-RESULT` from `read_cap_check.py` and `READS.tsv` rather than adding another maintained list. Preserve rc=0/1/2 and `assessed`; distinguish size findings, manifest defects and inability to evaluate. Preserve separate auto-memory limits and existing advisory/blocking classifications.

**First-batch acceptance cases:**

| Case | Required result |
|---|---|
| Unchanged source, evaluation date, rendering options and generated block | Generated comparison passes; prose scope is separately reported. |
| Docket deadline changes; generated block stays stale | Generated comparison detects drift even if the prose check has zero matches. |
| Evaluation date advances; source files do not change | Compare against the new date's output. A stale prior-day block cannot pass on its own old as-of stamp. |
| Missing/duplicate/malformed markers, unreadable or malformed source | Cannot certify the generated view; never clean. |
| Source, destination or rendering configuration changes during comparison | Use one stable snapshot or refuse the inconsistent result; never certify mixed revisions. |
| Intentionally empty prose scope versus eligible but unevaluable prose | Label the coverage distinction; neither certifies the generated view. |
| HANDOFF/manual/manifest scope | Approved text and declaration agree before budget integration; an alternative scoped region must satisfy its conservation conditions. |
| Read-cap ordinary result, over-budget result, manifest defect, unassessed or missing structured result | Preserve each outcome and assessment status through the gate summary; a missing result is not zero findings. Auto-memory remains separately assessed. |

Survey all consumers before changing a shared exit-code contract, per CHECK_STANDARD §9. Use the existing neighbour-case discipline; in particular, a scope omission and a concurrent edit are different failure cases. Do not claim implementation complete from these written acceptance cases.

### 2. Put runtime requirements at the beginning of boot

**Priority: small disclosure adjustment alongside coverage reporting. Owner: PROME.**

Move the relevant existing capability disclosures to the opening boot report and existing receipt. Use the actual session's callable-tool evidence for private Artifact access and native fleet preflight, and the existing presence/credential controls for what they genuinely assess. A shell probe cannot establish that a private connector is callable. Presence of credentials still does not prove authentication. Do not build a general capability framework, a new registry, or a runtime launch adapter in this batch.

Select only the procedures supported by demonstrated capabilities. A missing Artifact tool leaves taps UNKNOWN. Missing native fleet visibility withholds desk launches. Neither blocks unrelated reading or maintenance. Report these limits before a session spends time preparing dependent work.

**Acceptance:** a runtime without the required tools reports PARTIAL and names the omitted steps; unavailable tools never become “no pending rulings” or “no live desks”; a failed authentication at point of use is not hidden by an earlier presence check. Recheck at point of use. Native fleet visibility remains distinct from thread-local collaboration tools. No new launch authority is introduced.

### 3. Give the existing startup documents distinct jobs

**Priority: DEFERRED until the coverage batch is independently verified and this work separately scoped. Owner: PROME.**

Proposed division, to be reconciled with the existing ownership map:

| Surface | Default content |
|---|---|
| HANDOFF | Latest session outcome, unfinished work, decisions and material caveats needed to resume. |
| SCRATCH | Immediate next action and generated views of registered obligations. |
| STATUS | Current operational health and selected live work, with source pointers. |
| ACTIVE_DECISIONS | Non-terminal decision state and all standing guards. |
| HEARTBEAT | Dated regime synthesis, with freshness limits explicit. |
| Archives / owner artifacts | Historical narrative, full evidence and canonical domain logic. |

Remove superseded “owed” summaries from the default path once their current disposition is verified at the owner artifact. Replace duplicate current counts and dates with generated values or pointers. Preserve unresolved clauses even when their parent task completed; L438 is an existing example of why moving an apparently finished row can lose an obligation.

**Acceptance:** a reader can identify the current next action without comparing competing session narratives; every unresolved duty and decision-changing caveat retains a live carrier; old states remain retrievable; rotation meets the existing stop rule or explicitly records why the permanent content cannot fit. No authority, threshold, or owner grade changes through compression.

### 4. Shorten the default check output without losing exceptions

**Priority: DEFERRED until the coverage batch is independently verified and a separate read-contract amendment is reviewed. Owner: PROME.**

Have existing checks produce a concise default report and retain complete logs. Show every current blocking item, unresolved actionable advisory, missing capability, and changed exception. Group unchanged historical evidence gaps separately, with identifiers and drill-down links.

Age alone must never hide an unresolved obligation. Determine whether an old record still requires action from its recorded state and owner, not from its date. If that cannot be determined, retain UNKNOWN visibly.

This requires an explicit amendment to BOOT's present instruction to read every named log in full. Until that amendment is adopted and tested, the full-log read remains required.

**Acceptance:** an old unresolved action remains visible; a new failure in a previously quiet check appears immediately; a summary cannot omit a blocking finding; missing summaries trigger full-log inspection; historical UNKNOWNs remain available and are never converted to receipts.

### 5. Make repeat boots incremental only after proving completeness

**Priority: DEFERRED; optional, separately scoped work after the coverage batch is independently verified. Owner: PROME.**

Consider extending the existing boot receipt with source digests and declared read scope. On a repeated boot, inspect changed sources and always reevaluate time-sensitive obligations. An unchanged file can still cross a deadline or become stale.

Preserve `boot_read.py`'s changed-source refusal and the one-shot BOARD guard. No fresh run directory to bypass an incomplete attempt. A missing or incompatible baseline falls back to the full read path.

**Acceptance:** advancing the clock without changing files still surfaces due work; concurrent source changes invalidate the affected read; changed policies force rereading; same-day rulings and corrections remain discoverable; interrupted attempts do not advance BOARD twice.

This is the highest-complexity recommendation. Defer it if simpler changes remove most of the burden.

## Implementation sequence and review

1. **Resolve the prerequisite:** review and adopt the exact HANDOFF amendment and its declaration together before budget implementation, using the applicable authorization and plan/result review procedure. Whole-file is this proposal's recommendation, not a recorded Will ruling. Keep the existing mismatch visible until adopted. The independent calendar leg does not depend on this choice.
2. **Build only the coverage batch:** implement the separate generated/prose calendar results and consume the existing structured read-cap result after prerequisite adoption. Include clock-advance freshness in this batch. Earlier tool disclosure uses existing controls only. Preserve relevant boot evidence and create fixtures in throwaway repositories. Reconcile touched instructions in the same batch: exact amendments stay in the proposal/ruling record for plan review, then receive result review after transplant; both skill copies remain aligned with the manual.
3. **Verify that batch:** follow WQ-229's existing repair discipline. Consider ordinary, overlap, wrong-owner, missing-information and concurrent-activity cases; justify any N/A. An independent reader devises a counterexample before the repairs are called fixed. Report IMPLEMENTED, TESTED, INDEPENDENTLY VERIFIED and STILL UNRESOLVED separately.
4. **Stop at the verified coverage result:** document restructuring, shorter-log execution and incremental boots are not automatic successors. Consider them separately against the remaining measured burden. A later pilot would record report latency, context where measurable, missed obligations and later corrections; no savings percentage is claimed now.

**Success criterion:** the shorter path surfaces the same obligations, caveats and missing capabilities with less repeated reading. A missed obligation or falsely complete report is a failed pilot, even if it runs faster.

**Rollback:** retain original artifacts and the full-read procedure. If the pilot loses information, return to that procedure and document the specific omission; do not relax a gate to improve the timing result.

## Scope, existing work and immediate disposition

Use the existing boot-hardening design (`PROME/plans/2026-09-09_boot-hardening.md`) and current carriers rather than start a parallel governance system. Related work includes L350/L380 (read scope and content floors), L378/L444 (orchestration evidence/session identity), L381 (instruction reconciliation), and L438 (obligations lost in rotation). L197 records the calendar renderer's original adoption. These are overlap pointers, not claims that those rows authorize every recommendation here; reread their full scope before implementation.

Agent-side improvements need no new rule: locate the known repo before broad filesystem searches, use bounded reads from the beginning, limit discovery output, and distinguish source facts from interpretation. This boot's initial broad search and truncated reads were execution mistakes, not evidence that another layer of process is needed.

**For consideration:** proceed with the coverage batch only, with HANDOFF scope resolved before its budget leg and a small early-disclosure change using existing controls. Defer recommendations 3–5 until independent verification and separate scoping. This proposal creates no new deadline, WQ ruling request, or automatic workstream. No implementation or operating-rule amendment is claimed complete. CATO's review was incorporated; the revised proposal remains available for its next review, and no message has been sent on Will's behalf.
