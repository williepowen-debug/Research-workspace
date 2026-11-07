# Sloane commit-review assessment — 2026-11-07

## Current assessment

Finish the existing research correction chain first. Sloane's material findings survive at the inspected revision, with two refinements: FLG also retains an explicitly withdrawn runway projection; and the ledger headers already explain the legacy reconciliation flags, so the remaining issue is column semantics for consumers that skip comments, not absent documentation. Recommend a bounded owner correction pass, then verification of the affected outputs. No new fleet audit, trial, checker or launch is recommended.

Will supplied Sloane's review of November 6–7 commits, initially at `364159994a`, while discussing review work. CATO checked selected current artifacts at `77d8849806147d19ce14f43e3ff19820c2a1cfcc`. The worktree and index were clean at entry. A later diff against that revision found no changes to the seven principal thesis/code/table/control files checked. Shared HEAD may advance; this is a named-revision assessment, not certification of later work.

Scope: REGINALD matrix, ledger builder, allowance/runway tables and November 7 ledger-refresh report; FLG thesis and correction packet; Git-guard acceptance record; BOND correction commit and current digest code. No primary-data refetch, full thesis assessment, financial recommendation, live hook test, BOND runner execution, fleet-owner discovery or external Iran-reporting verification. CATO did not recreate the ranking backtest or establish that PROME's autonomy has improved. Source consistency is not independent confirmation of external facts. Existing CATO involvement in BOND closeout repairs is visible in the code; this inspection is not an independent acceptance of that implementation.

## Findings and closure conditions

### S1 — High: FLG has not incorporated two withdrawn claims

`AGENTS/FLG/THESIS.md:188` still calls FLG's 6/12 reconciliation result an outlier and quotes 24.4% non-tying cohort quarters. REGINALD's report and committed packet `AGENTS/FLG/inbox/2026-11-07_from-REGINALD_ledgers-at-9-30-tie-claim-retired.md` (`22845c2970`) explicitly retire this conclusion: the incomplete formula omitted disclosed write-downs and adjustments.

Also, `THESIS.md:141` says runway is moving away from every cut at approximately +0.06 years/quarter and "On trend it never arrives." Packet ACTION 2 explicitly withdraws that extrapolation. Stored recent runway is 2.3618 → 2.2475 → 2.1520 → 2.1680 years. This is more consequential than a stale count because the paragraph uses it to justify the latency conclusion around K-3. It does not establish a replacement threshold or require changing K-3 automatically.

Owner: FLG; PROME coordinates existing handoff. Close when FLG incorporates both corrections in the active thesis, identifies whether the related latency reasoning survives, and preserves the still-valid basis/sample caveats. Packet delivery is demonstrated; incorporation is not. No inference of refusal or neglect, and no owner launch here.

### S2 — Medium: matrix retains contradictory causal wording

`AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md:156` correctly withdraws continuous lengthening; line 158 still attributes falling coverage to charge-offs as "the same mechanism lengthening the runway." A historical interval is not specified. This leaves conflicting interpretations beside the correction. Owner: REGINALD. Close with an explanation consistent with the numerator, denominator and stated period, avoiding an unsupported monotonic trend. No wrong ledger value established by this finding.

### S3 — Medium: allowance output is not chronological

`AGENTS/REGINALD/scripts/call_report_ledgers.py:178` sorts by ticker and raw M/D/YYYY strings. All 14 ticker groups in the saved allowance table are nonchronological. The header itself warns against this exact sort. Runway construction at line 104 and output at line 179 parse dates, so this check does not implicate published runway arithmetic.

Owner: REGINALD. Close by parsing dates in the allowance output sort and verifying order within each ticker while retaining the same records and values. No primary fetch is needed merely to establish or correct ordering.

### S4 — Medium: legacy flags remain easy to misinterpret

Read-only CSV parsing reproduced 182 allowance rows, 46 `identity_ties=NO`, all 46 with `full_identity=YES` in Notes, and 51 flagged runway windows among 126 populated windows. Recalculating the full identity from stored numeric cells and note fields produced zero failures across 182 rows. This confirms internal arithmetic, not primary-source authenticity; absent note adjustments were treated as zero for rows that already tie.

Both table headers explicitly explain the legacy formula and retire the unexplained-break interpretation. Thus Sloane's suggestion to clarify documentation is partly already satisfied. The useful remaining change is an explicit complete-reconciliation field and unambiguous historical-field naming/consumer semantics, with compatibility considered before renaming columns. Owner: REGINALD. Close when a consumer reading structured columns can distinguish an omitted-term historical test from a current unresolved discrepancy, and runway flags preserve that distinction. Do not erase the historical measurement or silently flip its meaning.

### S5 — Low: reproduction promise exceeds the implemented scope

Builder lines 10–11 promise to recompute every existing row. Lines 144–148 select only the latest existing NDFI quarter. On the first refresh that was all 26 prior NDFI rows; now the ledger has 52 rows, so the promise will not cover its accumulated history. ACL comparisons also deliberately omit recoveries and Notes. Owner: REGINALD. Prefer narrowing the promise to the actual coverage, rather than adding recurring primary fetches without a research need. Close when documentation accurately states the per-ledger and per-field checks.

### S6 — Deferred control work: known Git-guard and BOND limitations

`PROME/tools/tests/ACCEPTANCE_git_guard_reset_2026-11-06.md` explicitly leaves properties 1 and 2 incompletely met, including named branch resets and path forms. This is disclosed residue, not a newly hidden regression. Existing PROME docket entry schedules a decision at the next process slot; the record requires Will to name a further review after three reads. No additional counterexample review performed here. Owner: PROME. Closure remains at the existing acceptance record; do not silently describe installation or 82 passing tests as full acceptance.

BOND commit `c85c7b09c7` corrects a falsely claimed FREEZE MATCH: verify reported MOVED and its shell chain did not enforce the result. Current `AGENTS/BOND/monitors/closeout_run.py:156–180` hashes scoped status/diffs/untracked contents plus global HEAD. Consequently an unrelated commit changes the digest. Static code supports the concurrency mechanism; the historical incident is BOND's preserved record, not rerun here.

Owner: BOND, with existing CATO/DAEDALUS repair involvement consulted if tasked. A bounded repair needs both appropriate content coverage and enforcement of verification failure. Merely deleting HEAD is inadequate: committed changes within the checked scope must still invalidate the prior result. Closure cases should distinguish unrelated commits from scoped committed edits and failed Git reads. No repair or new review authorization inferred from Sloane's suggestion.

## Decision, limits and return

Recommend FLG incorporation first, REGINALD wording/schema/order/documentation alongside it, and retain the two control issues under existing owner work. These are recommendations, not assignments sent to owners. No messages, packets, launches, owner edits, installations or policy changes occurred. The local evidence check is complete; implementation and demonstrated benefit remain open with the owners identified above. WQ-607 and all unrelated approvals remain unchanged.

Sloane's favorable interpretation of REGINALD's willingness to preserve a failed ranking is supported by the report's explicit negative result and unchanged scores; that is one observed behavior, not proof of system-wide improvement. The L180 report explicitly distinguishes its literal BROADER result from weak substantive breadth evidence. Preserve those limits. PROME's next ordinary continuation decisions can supply useful observations when they arise; no new scheduled observation or formal trial is warranted here.

## Delivery checks

All inputs were verified present/readable before checking. Root orphan advisory: clean, no uncommitted files outside CATO. Weekday check: exit 0 for exactly `PROME/DOCKET.tsv`, `PROME/GATES.tsv`, `PROME/WILL_QUEUE.md`, this report and `AGENTS/CATO/CONTINUITY.md`. Optional CATO STATUS/calendar/catalyst files do not exist and were omitted. Explicit read-cap check: all six startup files below 32,550 bytes (`AGENTS/CATO/AGENTS.md`, `AGENTS/CATO/CHARTER.md`, `AGENTS/CATO/CONTINUITY.md`, root `CLAUDE.md`, `USER.md`, `AGENTS.md`); largest 24,405 bytes. No STATUS, shared numeric source, auto-memory or consumer value was changed, so ledger nudge, memory and consumer checks do not trigger. Exact-path commit and safe-push receipt are delivered in chat; no additional receipt-only commit.
