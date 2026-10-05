# Codex approval stalls — advice on PROME's diagnosis

**October 5, 2026, 09:40 ET.** Will requested judgment and suggestions on PROME's quoted approval diagnosis. Advice only: no installation, permission change, owner edit, message or launch authorized or performed in this review. Earlier in this conversation CATO supplied WALTER/BRENT/BOND Astra launch commands and answered PROME's requested launch-status coordination; none was a CATO launch.

## Recommendation and stop condition

PROME's separation of shell/network and messaging blockers is useful. Resolve the existing requests through their task approval controls for today's work. Before maintaining permanent script exceptions, propose one bounded trial of built-in **Approve for me** (installed CLI exposes `--approve-for-me`; docs use `approvals_reviewer = "auto_review"`). It can review both shell escalations and eligible MCP approvals; it can also deny or time out. Availability and inheritance in PROME's actual spawned-task path remain untested. Preserve on-request approvals and the workspace sandbox; do not replace the reviewer policy.

Success is an assigned owner's source fetch, saved useful result, handoff received by PROME and closeout receipt, with repeat human interventions counted. Test the actual spawned-task path; a standalone CLI success does not prove inheritance. Stop after that bounded result or a named remaining blocker. No fleet permission redesign or new tracking tool is proposed.

If ordinary network fetches remain the recurring cost, evaluate a research-session network grant while retaining workspace filesystem limits. It broadens network access for that session; scoped command rules instead grant selected script invocations execution outside the sandbox. Neither is universally narrower. Official documentation supports both mechanisms, not their activation in the current managed tasks. Any activation remains a separate user decision.

## Evidence and limits

Local HEAD at inspection: `53d4ee6cb5627543ed702bd89a63c6ba7cbb233e`. Foreign WALTER/PROME changes and untracked reports were present; no pull or owner changes. PROME's three diagnosis files were untracked working artifacts, not a committed or remote-verified delivery:

| File under PROME/reports/2026-10-05_approval-diagnosis/ | SHA256 |
|---|---|
| diagnosis.json | 34ce2f3eb1a6545a6da062bdafdcd7b1a92e5d2813bb65af8bb6b91423497f3e |
| proposed-research-fetch.rules | 092ae0df2f6986656b75edc5660ecbd5655d2bff1f1ba8f3180e0c1f92bef94b |
| rule-checks.json | e982d69c6e2601f0d38b28a2b7af891af645417b73e40f8416d1ddd14c623665 |

Read PROME's latest three reply summaries through native `read_thread`, the three full artifacts and current PROME owner rules. Exact pending commands remain PROME's rollout-based diagnosis; CATO did not independently reopen those rollout files or see approval modal text. Separate immediate `wait_threads` snapshots verified all three task IDs still reported `waitingOnApproval` during this review: HENRY `01a10c34-b664-7021-b85f-5338a1bfcebe`, VULCAN `01a10c3a-235c-7f50-a5bb-63d8ec008fdb`, TERRY `01a10c3a-f6e1-7320-a5c0-38e73e993296`. An initial combined call returned HENRY only, so the others were checked separately; no monitoring loop installed.

## Bounded findings/advice

- **CA1 — operational gap, already disclosed by PROME:** draft rules do not match the pending relative-path commands. CATO independently ran `codex execpolicy check --rules <draft> <argv>` against HENRY `../../.venv/bin/python3 scripts/boot.py` and VULCAN `python3 tools/edgar_watch.py`: both returned no matched rules. Absolute HENRY interpreter/script matched allow. An installed draft therefore would not itself clear those pending requests. If rules are chosen, standardize/test actual future invocations and verify a fresh-session run; installation and parser checks alone are insufficient.
- **CA2 — material permission tradeoff, already disclosed in the artifact:** these are prefix grants outside the sandbox, not network-only approvals or exact immutable programs. Counterexample devised by CATO: absolute VULCAN invocation plus `--cato-review-unused-argument` still matched allow. This was a policy-parser probe only; the script was never executed and whether that argument is accepted by the script was not tested. Rules do not constrain script revisions or destinations. Script internals/dependencies were not audited, and this review does not approve their unsandboxed execution. Owner report already notes EDGAR may append a seen ledger.
- **CA3 — causal wording:** network-disabled shell settings do not by themselves explain a built-in MCP approval. Keep two separate diagnoses. Generic MCP configuration exists, but an effective persistent override for injected `codex_tui` remains UNKNOWN. User config had no explicit approval/sandbox/network keys or configured MCP server entries in a key-only inspection; that does not exclude runtime/managed layers. Native `create_thread` schema exposes prompt/model/title and inherits cwd; it exposes no per-child permission override. Actual child inheritance needs observation.
- **CA4 — practical alternative, not a verified fix:** installed help and current official docs expose built-in auto-review. Try the existing facility on one authorized owner workflow before growing a script-rule collection. No guarantee that it clears this injected messaging prompt; denial, timeout, effective child settings and useful delivery are the acceptance evidence. Discovery omissions remain PROME-reported, not independently reproduced here; retain exact returned IDs and never equate a list omission with an idle owner.

Earlier launch commands CATO supplied deliberately selected workspace-write/on-request without enabling shell networking. They therefore leave routine network escalation possible. This is a property of that launch choice; CATO does not attribute PROME's independently created tasks to those commands.

## Sources and verification

Official pages opened October 5: [rules](https://learn.chatgpt.com/docs/agent-configuration/rules), [sandbox/network approvals](https://learn.chatgpt.com/docs/agent-approvals-security), [MCP](https://learn.chatgpt.com/docs/extend/mcp?surface=cli), [auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review). Local CLI help corroborates the exposed flags and policy checker. Four independent parser probes above completed successfully; they establish matching behavior only. No source fetch, script execution, runtime permission change, MCP setting mutation or completed owner cycle tested. No independent review of CATO's own advice record claimed.

## Delivery checks

Five weekday inputs verified readable and checked clean: PROME/DOCKET.tsv, PROME/GATES.tsv, PROME/WILL_QUEUE.md, CATO/CONTINUITY.md and this report. Optional CATO STATUS/CALENDAR/CATALYSTS absent and omitted. Direct startup bytes: CATO AGENTS 6,465 / CHARTER 9,921 / CONTINUITY 20,042; root CLAUDE 24,199 / USER 4,626 / AGENTS 4,991, all below 32,550. Generic CATO read-cap remains rc2 CANNOT-EVALUATE for missing local CLAUDE.md, not a pass. Orphan advisory found only preserved WALTER batch manifest and PROME briefs/reports/ORCH_LOG; no CATO-authored outside paths in this assignment. Staging was empty before exact-file delivery. No auto-memory, STATUS, ledger or authoritative figure replacement triggered conditional checks. Publication receipt is delivered in-session, not presumed here.

Current resume point is discussion with Will. Existing unrelated approvals and assignments survive untriggered.
