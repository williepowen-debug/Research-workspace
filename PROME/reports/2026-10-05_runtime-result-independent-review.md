# WQ-385 independent RESULT review

Completed: 2026-10-05T14:35:21.255947+00:00. Review 2 of this amendment: one earlier plan review, this result review. Independent read-only pass; no additional reviewer or agent, no substantive contact with the author before findings were formed.

**Verdict: instruction implementation PASSES WITH DECLARED RESIDUE; no BLOCKING implementation defect found. Both plan blockers B1 and B2 are independently VERIFIED resolved. Runtime compatibility is NOT CERTIFIED.** At the reviewed evidence snapshot, the Claude manual/spawned cases, Codex spawned case and mixed handoff/interruption case remain BLOCKED / NOT RUN; Codex manual BOND remains pending. No test PASS follows from this review.

## Scope and review method

Reviewed the approved ruling and acceptance conditions in `PROME/proposals/2026-10-05_runtime-compatibility-RULED.md:5–16,26–49,124–156`, the earlier independent plan review, and the actual eight-file working differences against `/tmp/wq385-before/`. Explicitly read applicable root Critical Rules/Git Protocol and PROME authority/review controls, plus relevant current boot, completion, playbook and messaging sections. Read-only helper exemption is explicit at `PROME/COMPLETION_SPEC.md:10`; no domain boot or inbox-consumption exemption was invented. Runtime here is Codex with shell reads and thread-local collaboration; this review does not establish fleet discovery or an owner launch path.

Compared author-recorded instruction hashes to the actual eight files: all match. Independently compared root Critical Rules and Git Protocol sections with before-images: byte-identical text. Independently ran `git diff --check -- CLAUDE.md AGENTS.md PROME/CLAUDE.md PROME/AUTONOMY.md PROME/ORCHESTRATION_PLAYBOOK.md PROME/COMPLETION_SPEC.md PROME/BOOT.md MESSAGING/CROSS_SESSION_MESSAGING.md` from repo root: no whitespace finding. Ran `python3 scripts/read_cap_check.py --agent PROME`: rc=0, with its declared-manifest perimeter and explicit-runtime/injection limitations retained. This does not prove every possible runtime context fits or auto-loads correctly.

No repository edits, commits, launches, model calls or runtime configuration changes were performed by this reviewer. Only this `/tmp` artifact was authored. Review claims concern the snapshotted working text, not Git persistence of the implementation.

## Assertion ledger

### B1 — prior BLOCKING finding RESOLVED / VERIFIED

**Claim:** The identified root, BOOT and playbook operative mirrors no longer mandate unavailable Claude-only transports or assume Mode A serialization.

**Exact artifact:** Root `CLAUDE.md:13–23,125`; `AGENTS.md:9–19`; `PROME/BOOT.md:28,45,68`; `PROME/ORCHESTRATION_PLAYBOOK.md:13–16,38,64–85,130,163–165,177–178,192–206,213–226,234–248,252`; `PROME/AUTONOMY.md:24`.

**Verification:** Compared the corresponding eight-file hunks to before-images and the ruling's exact corrections; searched these files for `standing tool for every session`, `teams-mode only`, `ListAgents`, `SendMessage`, serialization and runtime pointers; read each consequential surviving match in context.

**Observed result:** VERIFIED. Root's universal native-tool claim is replaced while its DM-v1 route allowlist/exclusions through WALTER remain intact. BOOT points to mode selection and selected runtime mechanics. The mode table, hybrid step, git/concurrency discipline, anti-pattern directives and checklist no longer guarantee serialization or worktree support from a mode name. Current delivery templates point to the same runtime/completion homes. Surviving historical examples and Claude/Fable-specific lanes are bounded by their headings/context and `ORCHESTRATION_PLAYBOOK.md:85`; they do not establish universal tool support. Codex review helpers are explicitly distinguished from desk owners (`:144–150`).

**Disposition:** No correction required. This verifies text alignment, not successful launch or delivery.

### B2 — prior BLOCKING finding RESOLVED / VERIFIED

**Claim:** Rule 6b no longer converts uncorroborated IN-FLIGHT into DARK or suppresses uncertainty reporting.

**Exact artifact:** `MESSAGING/CROSS_SESSION_MESSAGING.md:31–43`, especially P0 at `:40`; canonical preflight `PROME/CLAUDE.md:67` and due-row pointer `:48`; playbook failure path `:252`.

**Verification:** Compared both replaced P0 passages with their before-images and the ruling; searched the full eight-file perimeter for the old uncorroborated-to-DARK instruction.

**Observed result:** VERIFIED. Both old operative P0 formulations are replaced, not left competing with an added UNKNOWN sentence. P0 now requires established absence for the DARK branch, treats idle/approval-blocked owners as live, and routes unresolved identity/coverage as uncertainty without a dark-owner spawn recommendation. The prior formulations are expressly superseded. Rule 6b's action/time/referent conditions and sender-does-not-launch boundary remain unchanged. A ledger row establishes neither absence nor liveness.

**Disposition:** No semantic correction required; minor P0 formatting residue is recorded below.

### I1 — retained authority, ownership, model and method boundaries / VERIFIED

**Claim:** This implementation preserves substantive approval/ownership limits while changing runtime selection and mechanics in the approved scope.

**Exact artifact:** Root `CLAUDE.md:13,32–50,71–108`; `AGENTS.md:13–21` and Coordination and authority; `PROME/CLAUDE.md:31–72`; `PROME/AUTONOMY.md:24`; playbook `:64–85,234–248`; messaging `:26–30,77–80`; completion `:10–21,25–40`.

**Verification:** Eight-file hunk inspection, exact unchanged root-section comparison, author-hash comparison, and inspection of the ruling's eight-file manifest and verbatim permission.

**Observed result:** VERIFIED. Root Critical Rules/Git Protocol, launch grant tiers/caps, roster authority, whole-inbox obligation, canonical desk paths and standing process ceiling are preserved. Gate C is not activated. Opus/Fable restriction remains in its applicable Claude worker lane; no OpenAI mapping or implied grant is created. Inherited model choice must be identified and checked, not silently accepted. Research approval persists in its original scope; runtime technical permission does not transfer or bypass a pending prompt. Read-only helpers retain their exemption and are not fleet-presence evidence.

Detailed runtime methods have one home in the playbook; short boot selection is in COMPLETION_SPEC; launch coverage/authority is in PROME/CLAUDE; messaging governance is in MESSAGING. Other edited surfaces point to these homes rather than adding alternative Claude/Codex procedures. Completion ledger keys/state tokens and completion block are unchanged. Eight instruction files are the implementation perimeter; evidence/ruling records are not a new operational system.

**Disposition:** No blocking scope/authority defect found. Retain the session-only nature of the extra process change; do not infer unattended rollout or new ownership rights.

### E1 — implementation evidence does not establish compatibility / VERIFIED limitation

**Claim:** None of the required complete runtime cases can be certified from the reviewed report and probes.

**Exact artifact:** `PROME/reports/2026-10-05_runtime-compatibility-results.md:3,11–31`; `PROME/proposals/2026-10-05_runtime-compatibility-RULED.md:126–136`; JSON locations below.

**Verification:** Read the report and decoded the nested JSON strings in `runtime-compatibility-probes.json`; checked `initialProbe`, `henry`, `vulcan`, `terry`, `bond`, and tools metadata; read host inventory and instruction-checks JSON. Compared all instruction hashes to current files.

**Observed result:** VERIFIED at the recorded times. The initial list is `truncated:true`; it omits the known HENRY/VULCAN/TERRY IDs. Direct known-ID results report all three active with `waitingOnApproval`. BOND's direct record reports active, Codex, and BOND cwd. These support limited positive identity/status observations, not complete absence, approval inheritance, or completed tests. BOND's cwd/status alone does not prove its original manual launch origin or all required startup reads. HENRY's reviewed probe is a status poll, not an end-to-end owner-run receipt.

Host inventory declares visible-PID-namespace-only coverage and UNKNOWN Codex endpoint coverage. The stored Claude record has null PID and blocked state; it cannot establish a currently live, identified Claude participant. No reviewer upgrade of that record to liveness or absence is warranted. Instruction-check booleans/hashes demonstrate text checks, not permission inheritance or runtime delivery.

**Disposition:** Preserve the reviewed outcomes: Claude manual = BLOCKED / NOT RUN; Claude spawned = BLOCKED / NOT RUN; Codex manual BOND = pending, not PASS; Codex spawned HENRY = BLOCKED / NOT RUN; mixed bidirectional/interrupted handoff = BLOCKED / NOT RUN. Native cross-runtime messaging and supervised durable mixed handoff are both unverified. The report is candid about these limitations. Later evidence may support a narrower claim, but it is not certified by this snapshot review.

## Independently devised counterexamples

**Hidden alternate-runtime owner after a known session exits.** PROME confirms that one known Codex owner ID has exited. Another manually launched Claude owner of the same canonical desk is idle in a different worktree/PID namespace, with no recent desk writes; its session is absent from the available native list. An old ledger touch is uncorroborated, and a due registered row invites replacement. This case adds a second possible writer after positive death evidence for the first; it is not just an empty-list case. Under current `PROME/CLAUDE.md:67`, confirming one ID's exit does not establish absence across all relevant runtimes/classes. Missing namespace/assignment coverage is UNKNOWN, so neither a new writing launch nor messaging rule-6b DARK recommendation is cleared. `ORCHESTRATION_PLAYBOOK.md:252`'s opening canonical-preflight requirement governs the later “Exit confirmed” phrase. If the hidden owner's actual identity is resolved, reuse it; if the approved transport is unavailable, keep the assignment/delivery pending. **INFERRED textual PASS; no live duplicate was created.**

**Lost notice followed by an artifact-version change.** Owner saves/commits V1. Its notice is lost. Before recovery, an authorized owner correction produces V2 at the same path, while an old receiver acknowledgment names V1. Recovery must reconcile the exact artifact version and existing acknowledgment under `COMPLETION_SPEC.md:38`, so a path-only match or V1 acknowledgment cannot certify consumption of V2. Read/ack V2 before claiming that handoff; retain the same owner/task and do not repeat research merely because the notice failed. A send acknowledgment still is not recipient consumption, and either acknowledgment is separate from an explicit closeout ask/receipt (`:19–21,38–40`). **INFERRED textual PASS; this does not prove idempotent application or crash recovery in the live runtime.**

These cases address wrong identity/worktree, incomplete discovery, concurrency overlap and saved-versus-consumed delivery independently of the author's tabletop examples. They establish expected safe decisions only. No atomic owner reservation, exactly-once mechanism or unattended race safety is claimed.

## Declared residue and outstanding work

- **R1 retained:** Full owner boot, whole-inbox and closeout duties can make the nominally tiny test larger (`RULED.md:156`; playbook `:241–243`). The report preserves these duties and prioritizes production work (`results.md:11`). When an eligible case runs, record actual launch origin, instruction reload, effective model/permissions, exact source invocation/vintage, committed artifact version, receiver acknowledgment, closeout ask/receipt, elapsed time and human interventions. Until then the case stays pending/NOT RUN.
- **R2 retained and contained:** October 5 create_thread/list observations remain dated and linked (`playbook:68–69,85`). They are not enduring capabilities and cannot select future tools without rechecking.
- **R3 cosmetic, nonblocking:** Messaging P0 at `MESSAGING/CROSS_SESSION_MESSAGING.md:40` begins with nested `**` markers and ends with an extra pair. The plain rule is unambiguous, so this is formatting residue, not authority to spend an additional canon correction/read.
- **Evidence limit:** Runtime outcomes remain unresolved as E1 states. Retain existing owner sessions and their last working approved methods, the installed script rules, durable artifacts and pending delivery/permission status (`results.md:29–31`). Do not repair an unavailable Claude lane by guessing sockets, launching duplicate owners, bypassing prompts or adding an unapproved bridge. Any later implementation expansion needs its own bounded scope.

No BLOCKING instruction finding requires a result-correction edit. The result-review obligation is met for the hashed instruction text below; the approved live-test acceptance obligations are not thereby met. This report is delivered before idle. Separate closeout receipt awaits PROME's explicit ask.

## Reviewed version identifiers

All paths below are relative to repository root. SHA-256 values identify the reviewed bytes, not a commit or a compatibility certification.

| Artifact | SHA-256 |
|---|---|
| `AGENTS.md` | `aecdda8cfa113f1161d74abd78d3e8fa0e460a03c2e890ffd1f7321b92a0d5ae` |
| `CLAUDE.md` | `609e423d7ea3cee6395854304f2b36a7d2f831061dbf02e29bbd1021aba43e9e` |
| `MESSAGING/CROSS_SESSION_MESSAGING.md` | `ba606c7260bf0c3831888f071a3605db38a3edd81095c20e4242657544b2c0e2` |
| `PROME/AUTONOMY.md` | `d39b18c842529b9a605084b608b00f7c73cda566ecb8507de984727b1b2d8771` |
| `PROME/BOOT.md` | `3a75d0ccb5387fe2f40c6ae96c720224b17b2870f724d4fa6ae454f5dcb2e6e0` |
| `PROME/CLAUDE.md` | `07efbb4c175965342a4fb4e47d8dbc1e9eb7cc4196926444b23452a5ddc20c6f` |
| `PROME/COMPLETION_SPEC.md` | `d213e20eb75f65ab6953ec99d6430c56500744ea4fad8efd01d968228288a6ff` |
| `PROME/ORCHESTRATION_PLAYBOOK.md` | `22c0750a022d7211fd017a94efe1db6f2525380db526972a2ee03b62b85b6d20` |
| `PROME/proposals/2026-10-05_runtime-compatibility-RULED.md` | `9f1e3c97f5a97c2f08466fbfdcb270ab977802958cdbfbcccc5e17acfd5ae0d3` |
| `PROME/reports/2026-10-05_runtime-plan-independent-review.md` | `10e806b8a11e11a60dc9ce642421b9dab17e5cffc0a0c0f09c915e59ef471dae` |
| `PROME/reports/2026-10-05_runtime-compatibility-results.md` | `1a6c7c3f26d9fbd90b74f7d93eba72558fe2289f412c71e45497a6c4f4b5b7ef` |
| `PROME/reports/2026-10-05_runtime-compatibility-probes.json` | `bf55da9983e6fb40daf272ab0091ff94fbd0dc8c2367bcdf08f2fa30879c92cc` |
| `PROME/reports/2026-10-05_runtime-host-inventory.json` | `84d3fd026eb3987f4849edc58eb212a887637233c3ccf60128ec4fdfc13e22df` |
| `PROME/reports/2026-10-05_runtime-instruction-checks.json` | `3d0f195e6906a8406421d0ce35307dd3b80c0813b197aae5a32407c6797a0244` |
