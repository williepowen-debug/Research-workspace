# PROME boot: recommendations for consideration

**Status: PROPOSED — no operating rule or implementation changed.**
**Author:** PROME / Codex · **Date:** 2026-09-21
**Requested by Will:** “Write out a plan/recommendations to consider.”
**Evidence basis:** one Codex boot, recorded in [the boot receipt](../reports/2026-09-21_codex-boot-1608.md), committed as `bbb8b8538`, plus inspection of the instruments below. This is not a fleet-wide performance study or an independent review.

## Recommendation

Improve the accuracy of the startup report first, then reduce the reading needed to reach it. Preserve the existing one-shot runner, digest-checked pagination, ownership boundaries, and explicit UNKNOWN states.

The main cost observed was reconstructing current state from overlapping summaries and historical records. The latest HANDOFF and SCRATCH entry supplied useful continuity; older work queues and long check logs then required considerable reconciliation. **Inference:** a smaller, reliably current read path would improve both speed and comprehension. This boot alone does not establish how much time or context it would save.

Start with two bounded repairs: accurately label calendar coverage, and make the budget report use the declared read perimeter. Evaluate broader document changes after those are verified.

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

For the calendar, establish two distinct contracts. A generated-view check compares the marked block with the current renderer output under the same declared date and options. The existing prose check assesses handwritten date claims. Zero handwritten claims can be legitimate; it must not certify the generated block. Eligible prose that could not be evaluated must remain distinguishable from an intentionally empty prose scope.

For budgets, reuse `read_cap_check.py` and `READS.tsv` rather than adding another maintained file list. Settle HANDOFF's read contract first. Preserve separate memory limits and existing advisory/blocking classifications unless explicitly changed.

**Acceptance:** stale generated text is detected even when there are no handwritten claims; an intentionally empty scope is accurately labeled; unreadable or malformed inputs cannot pass; a declared over-budget read appears in the boot summary; the summary and detailed log agree about coverage. Survey all consumers before changing a shared exit-code contract, per CHECK_STANDARD §9.

### 2. Put runtime requirements at the beginning of boot

**Priority: next. Owner: PROME.**

Extend the existing runner/presence evidence to record whether context injection, private Decision Deck access, native fleet preflight, and necessary data tools are available. Presence of credentials still does not prove authentication.

Select only the procedures supported by demonstrated capabilities. A missing Artifact tool leaves taps UNKNOWN. Missing native fleet visibility withholds desk launches. Neither blocks unrelated reading or maintenance. Report these limits before a session spends time preparing dependent work.

**Acceptance:** a runtime without the required tools reports PARTIAL and names the omitted steps; unavailable tools never become “no pending rulings” or “no live desks”; a failed authentication at point of use is not hidden by an earlier presence check. No new launch authority is introduced.

### 3. Give the existing startup documents distinct jobs

**Priority: after coverage repairs. Owner: PROME.**

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

**Priority: pilot after the document contracts are clear. Owner: PROME.**

Have existing checks produce a concise default report and retain complete logs. Show every current blocking item, unresolved actionable advisory, missing capability, and changed exception. Group unchanged historical evidence gaps separately, with identifiers and drill-down links.

Age alone must never hide an unresolved obligation. Determine whether an old record still requires action from its recorded state and owner, not from its date. If that cannot be determined, retain UNKNOWN visibly.

This requires an explicit amendment to BOOT's present instruction to read every named log in full. Until that amendment is adopted and tested, the full-log read remains required.

**Acceptance:** an old unresolved action remains visible; a new failure in a previously quiet check appears immediately; a summary cannot omit a blocking finding; missing summaries trigger full-log inspection; historical UNKNOWNs remain available and are never converted to receipts.

### 5. Make repeat boots incremental only after proving completeness

**Priority: later; optional. Owner: PROME.**

Consider extending the existing boot receipt with source digests and declared read scope. On a repeated boot, inspect changed sources and always reevaluate time-sensitive obligations. An unchanged file can still cross a deadline or become stale.

Preserve `boot_read.py`'s changed-source refusal and the one-shot BOARD guard. No fresh run directory to bypass an incomplete attempt. A missing or incompatible baseline falls back to the full read path.

**Acceptance:** advancing the clock without changing files still surfaces due work; concurrent source changes invalidate the affected read; changed policies force rereading; same-day rulings and corrections remain discoverable; interrupted attempts do not advance BOARD twice.

This is the highest-complexity recommendation. Defer it if simpler changes remove most of the burden.

## Implementation sequence and review

1. **Bound the first batch:** calendar coverage/reporting and declared-perimeter budget reporting only. Write acceptance conditions before edits. Preserve the relevant boot evidence and create fixtures in throwaway repositories.
2. **Verify that batch:** follow WQ-229's existing repair discipline. Consider ordinary, overlap, wrong-owner, missing-information and concurrent-activity cases; justify any N/A. An independent reader devises a counterexample before the repairs are called fixed.
3. **Reconcile the documentation:** propose exact manual/manifest amendments in the ruling record, obtain the applicable approval, then perform the existing plan/result reviews. Keep both skill copies aligned with the manual. Avoid a fleet-wide rewrite.
4. **Pilot the shorter path:** replay this boot's recorded states, then compare subsequent normal boots. Record time to a truthful boot report, context consumed where measurable, repeated reads, missed obligations and later corrections. Do not invent a token-savings percentage without measurement.
5. **Decide whether incremental boot is warranted:** adopt only if the simpler path still imposes material repeated work. Preserve a full-read fallback.

**Success criterion:** the shorter path surfaces the same obligations, caveats and missing capabilities with less repeated reading. A missed obligation or falsely complete report is a failed pilot, even if it runs faster.

**Rollback:** retain original artifacts and the full-read procedure. If the pilot loses information, return to that procedure and document the specific omission; do not relax a gate to improve the timing result.

## Scope, existing work and immediate disposition

Use the existing boot-hardening design (`PROME/plans/2026-09-09_boot-hardening.md`) and current carriers rather than start a parallel governance system. Related work includes L350/L380 (read scope and content floors), L378/L444 (orchestration evidence/session identity), L381 (instruction reconciliation), and L438 (obligations lost in rotation). L197 records the calendar renderer's original adoption. These are overlap pointers, not claims that those rows authorize every recommendation here; reread their full scope before implementation.

Agent-side improvements need no new rule: locate the known repo before broad filesystem searches, use bounded reads from the beginning, limit discovery output, and distinguish source facts from interpretation. This boot's initial broad search and truncated reads were execution mistakes, not evidence that another layer of process is needed.

**For consideration:** implement recommendations 1 and 2 first; prepare the bounded document cleanup in 3; pilot 4 only with a reviewed read-contract amendment; defer 5. This proposal creates no new deadline, WQ ruling request, or automatic workstream. No implementation or operating-rule amendment is claimed complete.
