# Independent plan review — runtime compatibility correction

Review completed 2026-10-05T14:14:21Z. Reviewed proposal: `PROME/proposals/2026-10-05_runtime-compatibility-PROPOSAL.md`, SHA-256 `20b4860ae36d3858e6d4f03302d660a44ddc63368fa327a0a14d694bacfb7b83`.

Conclusion: **WITHHOLD encoding as currently scoped.** The candidate shared rules are sound on incomplete discovery, persistent approvals, delivery evidence and supervised tests. Two consequential holes remain in the concrete transplant perimeter: conflicting operative mirrors outside the named sections, and the exact replacement of messaging rule 6b's contradictory DARK inference. Resolve these within the same eight files; no additional architecture, launch, permission expansion or fleet charter sweep is needed.

This was a read-only independent review. I read the eight named source files' relevant operative sections, plus `PROME/CLOSEOUT.md`, `PROME/tools/SESSION_PILOT.md`, `PROME/tools/tests/README.md`, the September 8 workstream and its bounded fallback ruling. I did not read CATO's advice or consult another agent. Commands below are run from `PROME/` unless specified. Observed source text is VERIFIED; counterexample consequences are reasoned, not live runtime tests.

## Assertion ledger

### B1 — BLOCKING: the exact perimeter omits live clauses that still impose Claude-only mechanics

**Claim →** Encoding only the listed root/BOOT sections and the candidate runtime table leaves mutually inconsistent operational instructions, so the promised common workflow is not yet reviewably encodable.

**Exact artifact →** Proposal lines 17–30 restrict root `CLAUDE.md` edits to opening/How The System Works and `PROME/BOOT.md` edits to step 0/step 5 presence. Root `CLAUDE.md:123` separately asserts that `SendMessage`/`ListAgents` are a “standing tool for every session” and commands `ListAgents` at packet commit. `PROME/BOOT.md:28` mandates fan-out/Workflow and “live teams-mode only.” The playbook's unqualified mode table (`PROME/ORCHESTRATION_PLAYBOOK.md:13–16`), hybrid sequence (`:38`), serialization instruction (`:152`), anti-pattern commands (`:167–171`) and quick checklist (`:178–181`) also prescribe these mechanisms outside the named launch-template/coordination/two-tier/failure sections.

**Verification command/read →** `rg -n 'standing tool for every session|Workflow|teams-mode only' ../CLAUDE.md BOOT.md ORCHESTRATION_PLAYBOOK.md`; read proposal lines 17–30, 61–79 and 95–101 alongside the matches.

**Observed result →** VERIFIED: the conflicting clauses are operative, not merely archived examples. Root line 123 is especially conclusive: the new opening would require selection from actual tools, while the retained root instruction still orders a specific unavailable tool. The playbook also supplies a runtime-specific serialization guarantee that must not become an assumed property of an arbitrary Codex mechanism. Proposal line 99's later contradiction check cannot authorize edits outside the proposal's own exact section perimeter.

**Proposed change →** Add these exact live clauses to the surgical manifest within the existing eight files. Draft the root messaging correction as a pointer to MESSAGING rule 6 and verified playbook transport, preserving the DM-v1 allowlist and WALTER/approval boundaries verbatim. Draft the BOOT clause as a pointer to mode-split plus the playbook mechanics. In the playbook, retain substantive independent-versus-dependent work selection, but label Workflow/teams tool names and serialization guarantees as applicable Claude mechanics; require the selected mechanism's actual concurrency behavior to be verified. This is alignment of conflicting mirrors, not an additional procedural home. Historical lessons may remain labeled historical.

### B2 — BLOCKING: the rule-6b change names an intention but does not supply the consequential replacement text

**Claim →** “Make UNKNOWN distinct from dark before rule 6b” does not explicitly dispose of the current P0 clause that commands exactly the opposite inference; the resulting canon text cannot yet be reviewed as a single unambiguous rule.

**Exact artifact →** Proposal `:30` is the only specific messaging amendment instruction. Proposed preflight `:51–53` says partial/unreachable/unmapped discovery is UNKNOWN and cannot establish absence. `MESSAGING/CROSS_SESSION_MESSAGING.md:35–36` currently says P0 fails only on corroborated liveness and, expressly, “An UNCORROBORATED IN-FLIGHT row means DARK: doorbell normally.” The paragraph labels this its “Operative form.” The draft contains no replacement quotation for that operative form.

**Verification command/read →** `nl -ba ../MESSAGING/CROSS_SESSION_MESSAGING.md | sed -n '27,59p'`; `nl -ba proposals/2026-10-05_runtime-compatibility-PROPOSAL.md | sed -n '21,59p'`.

**Observed result →** VERIFIED: the draft safely withholds a writing launch, but the existing messaging rule would still classify an unobservable idle owner as DARK and issue the dark-owner recommendation. This is not a request to rewrite historical provenance: the exact currently operative inference must be superseded. Merely inserting an UNKNOWN sentence before 6b leaves two competing instructions and a false absence report upstream of the safe launch gate.

**Proposed change →** In the proposal, name and quote replacement wording for the P0 operative sentences, for example: “An IN-FLIGHT row alone establishes neither liveness nor absence. Resolve owner identity and discovery coverage under the canonical PROME preflight. Uncorroborated liveness with incomplete discovery is UNKNOWN, not DARK. Keep the committed packet available and report the unresolved recipient/coverage to PROME through a verified channel; do not assert a dark-owner spawn recommendation. Rule 6b's DARK branch applies only when absence is established. An IN-FLIGHT row alone never suppresses an uncertainty report.” Preserve rule numbering, all existing action/time-sensitive gate legs, WALTER's lane and the no-launch-by-sender boundary. Historical prior P0 wording can remain only if explicitly marked superseded.

### R1 — RESIDUE: the tiny owner exercise needs an explicit selection constraint to remain tiny

**Claim →** The test workload can exceed one small check because full owner-session and whole-inbox duties remain binding.

**Exact artifact →** Proposal `:51` preserves whole-inbox obligations; `:83–85` directs a tiny research check without delaying existing work. `PROME/ORCHESTRATION_PLAYBOOK.md:216` and `MESSAGING/CROSS_SESSION_MESSAGING.md:59` require a writing owner touch to drain the whole inbox.

**Verification command/read →** Read those passages together with proposal `:89–93`.

**Observed result →** VERIFIED: no rule is actually waived, which is correct. Nevertheless a fresh owner with a large backlog cannot truthfully be presented as a tiny exercise if the intended operational launch must run that desk's full protocol. This affects participant choice and test scheduling, not the proposed safety rule.

**Proposed change →** Declare as residue and operationalize participant selection: prefer eligible already-caught-up owners; include any unavoidable owner boot/inbox/closeout work in the recorded elapsed time and intervention count. If that work would delay a position or release obligation, defer the case and report NOT RUN. Do not create a synthetic inbox-consumption exemption.

### R2 — RESIDUE: dated observations should stay dated when the table is transplanted

**Claim →** “Today's create_thread” and “current list omitted our spawned tasks” are experiment evidence, not enduring runtime mechanics.

**Exact artifact →** Proposal runtime table `:65–66`; evidence pointers `:108–111`.

**Verification command/read →** Read the table and its evidence section; compare root `CLAUDE.md` Output Canon's source-and-date requirement.

**Observed result →** VERIFIED: the proposal is dated, so the statements are adequately contextualized here. Transplanted without that date/context, they could describe a future tool installation inaccurately. The surrounding capability checks contain the operational risk, so this is residue rather than a blocking redesign request.

**Proposed change →** Keep the imperative mechanics general and retain the observation as an explicitly dated October 5 example pointing to the existing report. No new compatibility registry is needed.

## Independently devised consequential counterexample

A manually launched Codex owner has a verified desk assignment but inherited PROME cwd. It is idle at a technical approval prompt. The available native list is thread-local and omits it. Its desk tree is clean. Its old ORCH_LOG touch is still IN-FLIGHT. A due registered row requests new work for the desk.

Under candidate preflight `:51–53`, the cwd mismatch/list omission/quiet tree do not establish absence; discovery coverage is UNKNOWN and a new writing owner is withheld. If direct ID evidence identifies the owner, the existing task is routed to that same owner through a verified channel. The candidate passes this safety case without treating the pending technical approval as a withdrawn assignment approval. Under current messaging P0 `:36`, however, an uncorroborated IN-FLIGHT row is expressly DARK. That counterexample exposes B2's consequential text collision; it does not justify a new registry or launch-reservation system.

Second interruption check: an owner commits the result and dated packet, the notification call receives a transport acknowledgment, and PROME loses context before reading. Candidate `:57–59` permits only notification acceptance, not consumption or closeout. Recovery reconciles the same artifact version and existing acknowledgment before retry; a missing owner closeout response remains pending. This passes the saved-versus-received distinction at the text level. No live failure injection was performed.

## Preserved obligations and limits

- One substantive workflow and owned paths remain invariant; provider/model are separate from runtime and exposed capabilities.
- Root/local explicit reads, roster eligibility, preflight freshness, existing launch grants/caps and read-only-review exemption are preserved. The September 8 fallback is correctly treated as session-bounded.
- Existing assignment approval remains distinct from technical escalation; neither peer transport nor a local rules file grants new authority. Root/shared scope and WQ-299 process ceiling remain explicit gates, not implicitly satisfied by this draft.
- Runtime detail has one proposed home in the playbook; discovery authority remains PROME/CLAUDE and messaging content/approval governance remains MESSAGING.
- Saved artifact, notification acceptance, recipient consumption and owner closeout evidence are explicitly separate. CLOSEOUT itself need not change for this purpose.
- Both manual and actual PROME owner launch paths are tested separately; unavailable cases remain NOT RUN. Durable supervised handoff cannot certify native cross-runtime messaging. The tests correctly do not certify unattended race safety.
- The Opus/Fable constraint remains applicable to its existing Claude lane; no OpenAI price/model equivalence or silent inheritance grant is proposed. Actual inherited model selection must still be identifiable and authorized for the intended launch; unavailable evidence cannot certify that case.

No runtime, launch, domain script, native messaging or compatibility test was executed. No repository or runtime configuration file was edited. The only authored artifact is this `/tmp` review. **No owned repository files or commits remain.** Findings are delivered in full before idle; separate closeout acknowledgment awaits PROME's explicit ask.
