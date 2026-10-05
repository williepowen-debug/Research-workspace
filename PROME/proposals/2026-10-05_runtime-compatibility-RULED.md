# Runtime compatibility correction — RULED WQ-385

## Will ruling — WQ-385, October 5, 2026

Received directly in this PROME session, verbatim:

> Approve WQ-385 for the eight-file scope in the proposal and the supervised Claude, Codex and mixed-runtime tests. Approve one additional process change for this session only; the standing limit remains unchanged. Preserve existing research approvals and installed permissions.
>
> Complete the required independent result review, including verification that both plan-review blockers are resolved. Distinguish instructions implemented from compatibility demonstrated. If a test is blocked or fails, report the specific limitation and retain the last working method. Return with the review result, test outcomes and any remaining action
> for me.

Disposition: authorized encoding and tests; no new standing permission, process limit, unattended launch or owner replacement grant. The approved candidate below is retained as the plan history. Implementation and test evidence: `PROME/reports/2026-10-05_runtime-compatibility-results.md`.

reads: 1
- Plan read: October 5, 2026, `PROME/reports/2026-10-05_runtime-plan-independent-review.md`; B1/B2 corrected by author before ruling. Required result read pending; no second plan read.

# Approved proposal snapshot

Prepared October 5, 2026 by PROME for Will, incorporating CATO's advice supplied by Will in this session. This is a bounded continuation of `PROME/plans/2026-09-08_mixed-agent-workflow.md`, not a new orchestration system. Status: proposed scope and candidate wording; one independent plan review received and its two blockers addressed by the author as recorded below. Not encoded or compatibility-tested. Preparing this correction is authorized; the concrete encoding scope is registered as WQ-385. This document does not itself amend the mandatory spawn preflight or authorize unattended mixed-runtime launching.

## Outcome and boundaries

One desk keeps the same identity, research assignment, evidence standards, file ownership, delivery obligations and closeout when its model or runtime changes. Runtime-specific instructions cover only instruction loading, discovery, launch/resume, messaging, permissions and lifecycle mechanics. Record model and runtime separately; neither implies the other or proves capabilities. Will's additional direction in this drafting turn is incorporated: boot should explicitly allow OpenAI or Anthropic models and select the appropriate operational methods for how the agent was launched. The selection uses the actual runtime and available tools, not the provider name alone.

Keep the installed Codex script rules at `/home/willi/.codex/rules/prome-research-fetch.rules`. Their installation and prefix checks are established; live permission inheritance and a complete owner handoff remain unverified. They authorize selected script invocations outside the sandbox, not network-only access, and do not grant Claude Code permissions. No further permission expansion is part of this correction.

Preserve existing assignment approvals and their conditions across runtimes. A technical permission request is not a request to reapprove the research. A missing or ambiguous approval record must be resolved at its source; changing runtime cannot revive revoked authority, expand scope, move capital or waive a technical permission boundary.

Excluded: new scheduler, daemon, registry, dashboard, hook system, task database, concurrency manager, directory migration, model pricing policy, roster rewrite, fleet-wide charter sweep, Gate C activation, and unattended rollout. Existing inboxes, ORCH_LOG and completion records remain the coordination surfaces. Local instruction conflicts discovered by a pilot are named and bounded before any further edit is proposed.

## Exact instruction scope

Only the following eight existing instruction files are proposed for operational edits. Root/shared edits retain their current Will-gated scope; the draft must receive the existing independent plan review before encoding and a result review afterwards. Update affected document stamps in the same edits. Historical records and archived examples are not globally rewritten.

Single homes are explicit: detailed runtime methods live only in `PROME/ORCHESTRATION_PLAYBOOK.md`; the short boot selection contract lives in `PROME/COMPLETION_SPEC.md`; launch eligibility/preflight remains in `PROME/CLAUDE.md`; messaging governance remains in `MESSAGING/CROSS_SESSION_MESSAGING.md`. The remaining edited paragraphs are pointers or corrections of conflicting assumptions, not additional Claude/Codex procedure tables.

| File and section | Surgical change | Governing boundary |
|---|---|---|
| Root `CLAUDE.md`, opening, How The System Works and Data Hygiene Direct Messaging v1 bullet | Replace the assertion that all agents are Claude Code sessions; describe shared desk identity and explicit instruction loading. Replace the teams-only delivery sentence with a pointer to COMPLETION_SPEC. Replace the messaging bullet's claim that native Claude tools are available to every session with the exact pointer correction below. Keep Claude launch behavior as a labeled runtime example. | Root shared-file scope and Git Protocol; numbered Critical Rules unchanged. Preserve the DM-v1 allowlist and routing boundaries. |
| Root `AGENTS.md`, Operating model and source table | Replace Claude-only launch assumption with the shared identity rule and pointer to runtime mechanics in ORCHESTRATION_PLAYBOOK. Qualify auto-loading by runtime; preserve flat canonical paths and roster authority. | Navigation mirror only; no new substantive policy home. |
| `PROME/CLAUDE.md`, registered-dated-row paragraph and Desk-spawn preflight | Replace literal-tool eligibility with the explicit coverage-aware rule drafted below. Keep same-minute freshness, whole-inbox obligations, launch grants, caps and read-only exemption. | WQ-184/206/221 grants and WQ-178 preflight; the replacement requires explicit reconciliation, not inference from a tool name. |
| `PROME/AUTONOMY.md`, Tier 1 follow-up-spawn bullet | Replace its repeated `ListAgents`/`SendMessage` mechanics with a pointer to the canonical PROME preflight. | Preserve all tiers and grants. No duplicate preflight definition. |
| `PROME/ORCHESTRATION_PLAYBOOK.md`, mode table, hybrid step 2, launch/delivery templates, Concurrency / git hygiene, anti-patterns, quick checklist, coordination, two-tier model and failure path | Add one compact runtime-mechanics table; point discovery to PROME/CLAUDE and messaging to MESSAGING. Replace operative unconditional tool names and serialization guarantees with the exact pointer corrections below. Distinguish own-window Codex tasks from thread-local helpers and the historical Codex review-only lane. Qualify lifecycle assertions by observed runtime. | Same substantive mode selection and delivery contract. Existing Claude Opus/Fable cost constraint stays in its applicable lane; no implied OpenAI equivalent or new model grant. |
| `PROME/COMPLETION_SPEC.md`, required brief, handoff checkpoint and delivery methods | Preserve the explicit root/desk reads. Add runtime/capability identification and separate saved, notified, consumed and closed evidence. Replace the blanket transport sentence with a pointer to the verified runtime mechanics. | L399 explicit loading and WQ-249 ask/receipt semantics; existing ledger schema and completion block stay intact. |
| `PROME/BOOT.md`, pre-boot Multi-agent orchestration bullet, step 0 and step 5 presence sentence | Replace the operative Workflow/teams-only mandate with the exact mode/mechanics pointer below. Report discovery coverage and actual runtime tools; preserve AVAILABLE/UNAVAILABLE/UNKNOWN and point to the canonical preflight. Keep snapshots as evidence rather than substitute authority. | Existing boot receipt, one-shot gate and read requirements unchanged. |
| `MESSAGING/CROSS_SESSION_MESSAGING.md`, section 1, rule 6 and section 4 | Label historical Claude socket observations by runtime; apply content/coordination principles across verified transports. Make UNKNOWN distinct from dark before rule 6b. Preserve per-session technical permissions and approval provenance. | Rules 1–7 keep their numbering. WALTER retains signal-routing semantics; peer messages cannot grant technical permissions. |

`PROME/CLOSEOUT.md` already points to the preflight/closeout owners and distinguishes committed work from an actual ask. No edit is proposed. `PROME/tools/SESSION_PILOT.md` already states that partial inventory is UNKNOWN and its pilot is not fleet-wide authority; no tool or pilot activation is proposed. Reuse its acquisition methods only within their verified scope. The September 8 fallback ruling was session-bounded and cannot authorize today's standing replacement.

## Candidate shared wording

For the root operating model:

> A desk may run with an OpenAI or Anthropic model. Its identity, responsibilities, evidence standards, owned paths and approved work remain the same. At boot, identify the actual model/provider when exposed, the runtime, session identity and available operational tools; do not infer tool availability from the model name. Load the root rules and the desk's own instructions explicitly as required by PROME/COMPLETION_SPEC.md; do not assume a runtime auto-loads another runtime's instruction files. Select the matching runtime mechanics in PROME/ORCHESTRATION_PLAYBOOK.md and report unavailable capabilities. Existing approvals retain their scope and conditions across runtimes; technical permissions remain enforced by the receiving runtime and do not constitute a new research approval.

Add this short boot selection sequence to the existing required brief in COMPLETION_SPEC, with PROME/BOOT pointing to it rather than defining a second sequence:

1. Identify the desk, actual model/provider when exposed, runtime, session ID and repository/worktree. Mark unavailable identity information UNKNOWN; never invent a model label.
2. Load the same root and desk instructions and recover the existing assignment/approval basis.
3. Inspect the tools actually exposed for discovery, execution, messaging and closeout; select the applicable playbook mechanics. Claude Code selects its verified Claude Code methods; Codex selects its verified Codex methods. A provider label alone does not select a tool.
4. Record the selection and capability gaps in the existing boot receipt or completion notes. Recheck a capability when it is needed; a startup declaration is not a lasting permission grant. Apply the playbook's capability-specific consequence; continue only independent authorized work.

This adds no new boot file, schema, provider-specific desk charter or operator approval request. The three compatibility tests below must observe correct method selection and a truthful missing-tool report, in addition to instruction loading.

For `PROME/CLAUDE.md` Desk-spawn preflight, replacing rather than adding beside the current mandatory `ListAgents` clause:

> Before spawning a domain owner that writes its desk directory, obtain same-minute, same-host evidence identifying the desk's possible writers across every runtime in use. Use supported native discovery, direct checks of known session IDs, and the existing host inventory where its coverage is established. Record identity, runtime, repository/worktree, canonical desk scope, observation time and coverage in the existing task receipt/ORCH_LOG notes. A matching live owner, including an idle or approval-blocked owner, receives the existing assignment through its verified channel; do not duplicate it. A partial, stale, unreachable or unmapped result is UNKNOWN, never absence. Unknown ownership withholds a new writing launch; resolve it by probing the existing owner or obtain Will's explicit, bounded preflight ruling. Quiet files, clean Git, a saved database row, thread-local helper discovery, or omission from one task list cannot independently clear the launch. Preserve the read-only verification exemption, inbox-census rule, roster eligibility, launch grants and caps. No automatic cross-runtime replacement or unattended launch is authorized by this correction.

This is an explicit proposed replacement of the current tool-specific requirement, not a claim that Codex `list_threads` already satisfies it. A positive identity can establish a known owner; negative evidence must cover all relevant runtimes and session classes. Coverage that cannot be established remains UNKNOWN. File activity and host PIDs corroborate identity or expose conflict; they do not prove absence of an idle owner.

For MESSAGING rule 6b P0, replace the current operative precondition and operative-form sentences, including “An UNCORROBORATED IN-FLIGHT row means DARK,” with:

> **P0: establish owner absence before taking the DARK branch.** An IN-FLIGHT row alone establishes neither liveness nor absence and never suppresses an uncertainty report. Resolve owner identity and discovery coverage under PROME/CLAUDE.md's canonical desk-spawn preflight. A corroborated live owner, including an idle or approval-blocked owner, is not DARK; use rule 6's existing-owner coordination branch through a verified channel. Uncorroborated liveness with incomplete discovery is UNKNOWN, not DARK. Keep the committed packet available and report the unresolved recipient or coverage to PROME through a verified channel; do not assert a dark-owner spawn recommendation. Rule 6b's DARK branch applies only when absence is established, and all its existing action, timing, authority and sender-does-not-launch conditions still apply. The ledger records PROME's open touch; it is not a liveness instrument.

Preserve rule 6b's other legs and stable numbering. Retain prior P0 incident history only as explicitly superseded historical wording; it must not remain labeled “Operative form.” No new WALTER routing semantics or permission grant is introduced.

## Exact corrections to conflicting mirrors

Root `CLAUDE.md`, Data Hygiene Direct Messaging v1 bullet: retain its opening DM-v1 allowlist and exclusions verbatim through “WALTER is unchanged under its BOARD/inbox spec.” Replace the remainder with:

> Cross-session coordination follows MESSAGING/CROSS_SESSION_MESSAGING.md; read it before first use and select a verified available method from PROME/ORCHESTRATION_PLAYBOOK.md. Messages carry coordination and artifacts carry content; verify peer claims at artifacts, preserve the rule on relayed operator words, and never route signals around WALTER. At packet commit, apply messaging rule 6; apply its rule 6b only when that branch's owner-status condition is established. Tool availability and incomplete discovery follow those canonical references, not an assumption that every session exposes Claude tools.

`PROME/BOOT.md`, pre-boot Multi-agent orchestration bullet, replace with:

> Before spawning more than one agent, apply the substantive mode-split rule in PROME/ORCHESTRATION_PLAYBOOK.md and select the available mechanism from its Runtime mechanics section. Carry the shared delivery contract from PROME/COMPLETION_SPEC.md into each spawn brief. Launch preflight and authority remain governed by PROME/CLAUDE.md.

`PROME/ORCHESTRATION_PLAYBOOK.md`, make these exact operative substitutions while retaining the dated June 26 examples as history:

- Mode table Tool row: label it **Runtime mechanism**; Mode A cell becomes “Verified mechanism for independent batch work; select under Runtime mechanics.” Mode B cell becomes “Verified mechanism for iterative coordination; select under Runtime mechanics.”
- Mode table Concurrency row: both cells point to “Verify actual execution and commit concurrency under Runtime mechanics; mode alone grants no serialization or isolation.”
- Hybrid step 2 becomes: “Fan out the independent part (Mode A), using the selected verified runtime mechanism; collect artifacts and synthesize.”
- Concurrency / git hygiene first bullet becomes: “Mode A describes work independence, not a serialization guarantee. Verify the chosen mechanism's execution and commit behavior under Runtime mechanics. Other live sessions may still share the Git index; apply root Git Protocol regardless of mode.” The second bullet retains its existing race warning and deferred worktree decision; runtime-specific `isolation: worktree` syntax is a labeled example, not a universal supported option.
- Anti-pattern directive “Use a Workflow” becomes “Use a verified Mode-A mechanism selected under Runtime mechanics.” Directive “Serialize (Workflow) or worktree-isolate” becomes “Verify commit serialization or approved isolation under Runtime mechanics and root Git Protocol; never assume either from the mode name.”
- Quick checklist item 2 becomes: “Mode selected by the decision test, and its mechanism selected under Runtime mechanics?” Item 5 becomes: “Actual execution/commit concurrency checked under Runtime mechanics and root Git Protocol?”

Add one sentence beside the authoritative runtime table: “Workflow/teams tool names and their historical serialization behavior are Claude-runtime examples; for every selected mechanism, establish its actual concurrency and file visibility before relying on those properties. Missing evidence does not authorize concurrent owner writes or a worktree migration.” Other operative unconditional SendMessage wording in the named delivery/coordination templates is replaced with a pointer to the same table and COMPLETION_SPEC, not another transport recipe.

For delivery in COMPLETION_SPEC:

> Save the required owned artifact and dated delivery packet, and complete the existing Git persistence steps. Then use a verified available channel for the coordination notice. A tool acknowledgment establishes notification acceptance only. PROME reads the exact artifact version and records its acknowledgment/disposition in the existing receipt before claiming consumption or a completed handoff. Saved work with interrupted messaging remains pending delivery/consumption. Recover the same task by reconciling the artifact version and existing acknowledgment before retrying a notice; do not repeat the research or spawn another owner merely because the notice failed. Acknowledged delivery is separate from the explicit closeout ask and the owner's closeout receipt required by WQ-249.

Retain the two-delivery intent: durable artifact plus reported result. When live transport is unavailable, an existing durable coordination packet and actual recipient read/acknowledgment may demonstrate a supervised handoff; merely writing the packet cannot. Missing live closeout transport remains explicitly unverified until the ask is received and the owner answers through an evidenced channel. No replacement state tokens or ledger columns are needed.

## Runtime mechanics within the existing playbook

| Mechanic | Claude Code lane | Codex lane | Shared constraint |
|---|---|---|---|
| Load identity | Verify root and local instructions for actual launch directory and available instruction loader. | Explicit root/local reads; today's create_thread inherited PROME cwd, so task identity cannot be inferred from cwd alone. | Same files and substantive owner contract. |
| Discover | Use native Claude discovery when exposed and document its actual coverage. | Use exposed list/read tools and returned task IDs; current list omitted our spawned tasks, while direct reads found them. | Neither lane alone establishes cross-runtime absence. |
| Start or resume | Use supported owner-session mechanism after canonical preflight; respect existing Claude worker model rule. | Use a supported task/owner-session mechanism after preflight; follow actual schema and approved model choice. | Record actual identity/model and observe successful start; unsupported settings are not silently substituted. |
| Notify and receive | Native messaging when verified for the exact pair. | Native task messaging when verified for the exact pair. | Save content first; distinguish send acknowledgment from recipient consumption. No raw socket guesses or permission bypass. |
| Permissions | Claude Code session permissions. | Codex session permissions, including only installed applicable rules. | Assignment approval persists; technical grants do not transfer automatically. |
| Close | Explicit ask and owner receipt, with actual lifecycle evidence. | Explicit ask and owner receipt, with actual lifecycle evidence. | Do not infer closeout from idle, clean files, or a process exit. |

The table is a runtime selection guide, not a certification of every tool/provider combination. For models, keep the existing applicable selection authority. A supported tool that requires inheritance must have its inherited choice identified and checked against that authority; do not invent an Opus-to-OpenAI mapping or silently inherit a prohibited model. Owner sessions and read-only review helpers remain distinct roles regardless of provider.

Add these consequences beside the table, in this single methods reference:

- **Messaging unavailable or awaiting technical approval:** an already-authorized owner may continue independent research and save its artifact under existing permissions. Notification and recipient consumption remain unverified until the actual read and acknowledgment. Do not bypass the pending technical approval by changing transport to perform the denied action.
- **Owner discovery incomplete:** withhold a potentially duplicate writing launch. Continuing independent work does not authorize launching or taking over that desk. Resolve ownership under the canonical preflight before launch; do not infer inactivity from a blocked message.
- **Required source access unavailable:** continue unrelated authorized work, but identify the missing source and withhold conclusions that depend on it. A prior quote is not a replacement for required current evidence.
- **Persistence or closeout unavailable:** preserve the useful permitted output, report the exact incomplete step, and keep delivery/closeout pending. An idle task or saved file is not completion.

## Smallest compatibility tests

Use eligible Claude Code and Codex desk owners with PROME as coordinator. Each single-runtime test has two launch-path cases: an existing owner manually launched by Will and an owner started through PROME's intended operational mechanism. Reuse existing sessions where their launch origin is evidenced. If a fresh spawn is necessary for the same desk, first obtain the previous owner's explicit closeout/release, resolve its liveness and repeat the preflight; never create two owners to compare launch paths. Confirm current assignments and avoid delaying expiry/release work. If a runtime or launch path is unavailable, mark that case NOT RUN and limit any compatibility claim to the cases actually tested. An operator-supervised test window must identify all participants and avoid concurrent manual launches; this is not proof of unattended race safety.

Each owner performs one tiny already-authorized research check: fetch one required public source through its normal approved data path, preserve source/vintage, write one owned artifact and dated completion packet, persist it under the existing Git rules, and deliver it to PROME. No new forecast, trade, threshold, registry or synthetic consumed inbox entry. Capture evidence in the existing owner artifact and ORCH_LOG notes: exact instruction paths read, model/runtime/session identity, effective permission mode, fetch result, artifact path/version, receiver acknowledgment, closeout ask and receipt. Count human interventions and elapsed time; do not set an invented performance threshold.

| Test | Minimal exercise | Pass condition |
|---|---|---|
| Claude Code owner | Run the small check in the manually launched case and the actual PROME-spawned case, sequentially for a single desk if needed. Record launch origin, initial cwd, loaded instructions, effective permissions and exposed tools for each. | Instruction loading, required data access, owned persisted artifact, PROME read/acknowledgment and explicit closeout receipt evidenced separately for both launch paths. A manual-session success does not pass the spawned case. |
| Codex owner | Run the same-sized check in the manually launched case and the actual PROME-spawned case. Use already-created eligible tasks if possible, preserving evidence of their original startup and reloading the corrected instructions before the test. | Same five obligations evidenced separately for both launch paths; inherited cwd/permissions/tools and exact script invocation recorded. A standalone CLI test, parser success or installed rules alone does not pass the PROME-spawned case. |
| Mixed-runtime handoff and interruption | Reuse those two owners. A sends a committed artifact pointer to B, B reads it and returns an acknowledgment/artifact; reverse the direction with the same bounded evidence. In one leg, simulate loss of the coordination notice after saving the artifact, using a disposable test notice rather than disrupting production work. Recover the same task and record the recipient read before resending. | Both runtimes identify the correct peer and exchange acknowledged work. Recovery produces one substantive result, no duplicate owner and no duplicate application. Explicit asks/closeout receipts complete both owners. If only durable packets work, label the result supervised durable-handoff PASS and native cross-runtime messaging UNVERIFIED. |

Within the mixed test, exercise the existing preflight decision without launching: (a) the other runtime has a live owner; (b) that owner is approval-blocked; (c) its discovery source is omitted or stale; (d) its cwd differs from its verified desk assignment. Expected: reuse the identified owner in (a)/(b); withhold a new writer in (c) and any unresolved (d). No live duplicate is deliberately created. This checks the safety decision; it does not establish an atomic launch reservation or unattended concurrency safety.

## Review and implementation order

1. Review this candidate wording against the eight named source sections, including one reviewer-devised case involving a hidden idle owner or a saved-but-unreceived delivery. CATO's advice informed the draft; it is not an independent review of this resulting text.
2. Reconcile the explicit governing-rule changes, especially mandatory native preflight, root/shared scope and worker-model selection. Existing research grants are not resubmitted for approval. Use the current canon proposal/review procedure; no standing rule changes by installing a local permission file.
3. Encode the bounded paragraphs once in their current homes and align the named mirrors. Check for contradictory operative requirements within this perimeter, broken pointers, unchanged schema/path/authority invariants, and required read caps. Keep historical examples labeled historical. Apply the existing result-review budget.
4. Run the three supervised tests, preserving any missing capability as an explicit limit. If a needed supported transport is absent, stop at that named gap and propose a separately bounded implementation; do not grow this edit into a bridge service.
5. Report separately: instruction changes implemented, text checks passed, independent review obtained, and compatibility demonstrated or still unverified. Passing these tests does not enable unattended mixed-runtime spawning.

Today's installed permission rule was the session's process implementation. This drafting pass installs no further process control and does not silently exceed the existing process-change ceiling. Schedule any later encoding under the applicable limit or an explicit bounded ruling.

## Independent plan review and disposition

One independent read completed October 5, 2026 at 14:14:21 UTC, against draft SHA256 `20b4860ae36d3858e6d4f03302d660a44ddc63368fa327a0a14d694bacfb7b83`. Review artifact: `PROME/reports/2026-10-05_runtime-plan-independent-review.md`. The reviewer devised a hidden, approval-blocked owner counterexample and a saved-but-unreceived delivery case. The preflight and delivery wording passed those textual cases; no runtime compatibility was tested.

- B1 BLOCKING: omitted operative root/BOOT/playbook mirrors. Addressed in this draft by expanding the named sections within the same eight files and supplying exact replacements above.
- B2 BLOCKING: rule 6b's uncorroborated-IN-FLIGHT-to-DARK inference conflicted with UNKNOWN. Addressed in this draft by the explicit replacement of both operative P0 passages above; other gate legs and numbering stay unchanged.
- Review status: one independent review received; B1/B2 corrections are author-checked and have not received a second independent plan read. No live instruction has been encoded, and this is not a clean independent verification of the corrected result. The existing required result review still applies after any authorized encoding.

Declared residue, October 5, 2026: R1 — whole-inbox/full owner boot duties may make a nominally small test larger; participant selection and recorded effort must expose that constraint, and no synthetic inbox exemption is granted. R2 — the October 5 runtime-table observations are dated experiment evidence, not permanent capability guarantees; their date/context must survive any transplantation. These warnings remain declared rather than prompting additional process design or a further review round.

## Evidence and unresolved limits

- Existing approved workstream: `PROME/plans/2026-09-08_mixed-agent-workflow.md`; bounded prior exception: `PROME/proposals/2026-09-08_codex-desk-presence-fallback-RULED.md`.
- Current experiment: `PROME/reports/2026-10-05_morning-orchestration.json`; permission diagnosis and installed-rule checks under `PROME/reports/2026-10-05_approval-diagnosis/`.
- CATO's additional permission analysis: `AGENTS/CATO/runs/2026-10-05_0940_codex-approval-advice.md`; its suggested auto-review trial remains a separate untested option, not activated by this draft.
- Today's Codex launches verified returned IDs and later active status, but did not establish Claude-side owner absence. They are not evidence that the current literal ListAgents rule was satisfied and are not precedent for a standing mixed-runtime preflight.
- No compatibility test has passed in this proposal. No shared instruction file or desk charter was edited by this preparation. Existing assignments, position deadlines and approval conditions continue independently.
