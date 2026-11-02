# November 2 morning changes — targeted error review

## Assessment

Two confirmed integration/policy mismatches warrant bounded corrections: restrict Fable to PROME in the launcher, and preserve launcher warnings when the session-view writer groups old unresolved touches. No owner implementation changed by this review; no agents launched or packets sent. Review complete; no CATO repair assigned. Do not treat this review as certification of all morning research or later commits.

## Scope and evidence

Will asked for analysis of this morning's edits/errors. Initial inventory at 10:18 EST: 87 commits and 435 committed changed paths from `d8fd813c6a1e18dc319ea9a0f2ba63c0233e73b7` through `f28fc8021`; uncommitted owner work also inspected as a snapshot. Selected higher-impact executable/instruction changes and their consumers: launcher Python/helper/PowerShell/tests/guide, USER model ruling, PROME gate/spawn-list changes, ledger-nudge wording, orchestration-view writer/tests, DAEDALUS owner-relative clock implementation/tests/acceptance, and selected DOCKET, queue, BOND/HENRY/NEXUS and ORACLE changes. Many research/raw-data paths were inventoried rather than read. No external financial evidence, live position, every arithmetic assertion or every dated record was revalidated. No claim of exhaustive 435-file coverage.

This is CATO author follow-up for launcher code, not independent acceptance. Other owners are active; their uncommitted code/results may change after this snapshot. Earlier DAEDALUS clock HOLDs are superseded by its final accepted source hash; they are not reopened here. Read current owner contracts relevant to behavior; no owner edits undertaken.

## M1 — P2: launcher permits Fable outside PROME despite the new standing ruling

Evidence: `USER.md` Fable-only paragraph (WQ-590, November 2 09:49) says desks/readers/every other spawn never use Fable. `scripts/agents.py` build_plan accepts runtime fable for all non-CATO entries; `scripts/agents_gui.ps1` Sync-Editors still offers it and Apply-Group accepts it. `scripts/tests/test_agents_launcher.py` explicitly expects CYPHER Fable on new and resume.

Read-only reproduction using actual configuration: build_plan(entries['CYPHER'], 'fable', 'new') returns `claude --dangerously-skip-permissions --model fable ...`; resume also succeeds. No CLI/model launched. The older launcher behavior predates the new ruling; the morning omission is failure to reconcile it with the new policy, not proof every previous launch was unauthorized. No actual forbidden launch established.

Consequence: the operator can launch a desk in the model he has just prohibited, and a passing suite currently preserves that mismatch. Correction owner CATO under a bounded implementation assignment: enforce the model restriction in the common plan builder, limit GUI choices and saved-group handling consistently, replace contrary test expectations while preserving PROME Fable and CATO policy. Closure: non-PROME new/resume/direct/group paths refuse Fable before opening a terminal; PROME still accepts it. This review does not initiate that repair.

## M2 — P2: grouped unresolved touches disappear from the launcher's warning

Producer: current uncommitted `scripts/orch_log.py` render_view groups touches older than seven days by base desk. Consumer: `scripts/agents_gui.py:80` unresolved_touches only reads table rows beginning `| 20`, then touch_for returns state available with dates from those detailed rows. `scripts/agents_gui.ps1:1306` only warns when dates is nonempty. Grouped rows beginning with a desk are silently ignored. Thus representation-only producer change alters downstream behavior despite preserving canonical debt.

Read-only real-producer reproduction: validate the production ORCH_LOG ledger, render its rows into a disposable directory with today November 2, compare horizon 10000 versus default seven days through actual unresolved_touches/touch_for. Full-detail render: 30,024 bytes, 178 visible unresolved rows, HANS dates ['2026-10-21']. Default grouped render: 19,295 bytes, 39 visible rows, HANS dates [], state still available. This loses 139 touch records from launcher consumption without declaring missing coverage. The ledger remains unchanged; grouping does not actually close any debt. No claim that a duplicate owner launch occurred.

Current producer SHA256 `0e77438e350270ae0c4807e3dd3c2d6dff2471d360ae0405815f4c13bf0f2b7f`; consumer `72f8049278694420915c779e20a45d84bcddc502953d666205f2ea7c5ed63fd0`. DAEDALUS L911 acceptance says grouping is presentation only and preserves unresolved touches. Production-view regeneration is explicitly still PROME's action; this is a pre-release consumer defect, not proof of an already-installed false launcher status.

Correction: DAEDALUS/PROME retain the view compression, but coordinate with the launcher owner to read canonical exact unresolved identities or explicitly interpret grouped unresolved evidence. Do not restore unbounded startup output, infer closure by age or invent exact dates/identities from summary ranges. Closure: preserved real-ledger case still warns for HANS and every other desk represented only in old grouped debt, while retaining correct empty/unavailable handling and compact view size. No new checker or recurring audit is needed; add the producer/consumer case to existing tests if repair is commissioned.

## Verification and limits

- Launcher author suite: 42/42 pass; this does not close M1/M2.
- Orchestration focused suites: 46/46 pass with PYTHONPATH=scripts. First invocation without PYTHONPATH failed imports and evaluated no behavior; corrected invocation passed. Existing ResourceWarnings concern unclosed reads; no new functional failure inferred from them.
- DAEDALUS clock suite: 17/17 pass at final accepted source SHA256 `e6f1003671d8a38b39b0843fa5f32dbbd0ff1e67c83d2be1816eea59e8285beb`. Review of prior counterexamples/final disposition and current parser found no additional confirmed error in that bounded repair; this does not certify profile contents refreshed.
- Scoped committed-code whitespace check passed for launcher and PROME gate/spawn-list changes. ORACLE's +52pp label is the current difference between its two stored legs (88.5 minus 36.5), not by itself a 52pp daily jump; no defect asserted from its commit headline.
- CATO Kimi token/permission patch retains its earlier authenticated remote MCP initialization evidence; no token printed or persisted by this review. Completed WAL boot remains outside this review's certification.

Remaining actions: M1 launcher policy repair and M2 consumer compatibility before production use of grouped output. Both are recommendations with reproduced evidence, not newly delegated work or implementation. Do not reopen other accepted repairs without changed evidence. Review stops here; orient and await Will. Durable report/index/continuity only; no owner files altered. Delivery checks recorded below.

Delivery checks: weekday passed on the six readable named inputs (PROME DOCKET/GATES/WILL_QUEUE, CATO continuity/index/this report); read-cap evaluated all six required startup files, all below cap, root CLAUDE 76% rotation advisory only. Orphan advisory read; no CATO-authored shared residue from this review. Owner files and never-sent Decisions exports preserved. Exact CATO paths only for delivery. No memory/ledger/consumer-figure change conditions.
