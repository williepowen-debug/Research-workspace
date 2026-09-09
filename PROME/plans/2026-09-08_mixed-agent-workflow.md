# Mixed manual and PROME-orchestrated agents — implementation handoff

Recorded: 2026-09-08, following the completed Codex owner catch-up. Owner: PROME. Status: Will requested work on all six improvement areas, starting in a fresh window. This file records the workstream and acceptance plan; the improvements are not implemented by this record.

## Start here next session

Boot as PROME using the normal root and local instructions. Read this plan and the current SCRATCH first-priority note. Refresh the actual machine/session inventory before any launch. Preserve time-sensitive market obligations from SCRATCH/DOCKET; this architecture work does not discharge them.

First deliverable: a verified capability matrix for the installed Codex and Claude runtimes and a bounded messaging/presence pilot. Begin with existing sessions when available. Do not repeat today's full owner catch-up or create another owner for a live desk. Build the smallest working integration before broad rollout. Follow the existing canon amendment procedure for any eventual shared-rule changes.

Will's instruction to carry forward verbatim:

> Okay I want to work on these all. But I want to close us out here and start it in a fresh window. Can you save this plan this out and save it for the next session and write it up in SCRATCH or whatever you rec

Treat this as authorization to pursue the six areas next session, including necessary reversible investigation and implementation. Do not ask Will to approve the same overall workstream again. Exact hardware limits, cross-runtime behavior and implementation choices remain to be established. This record does not activate Gate C, authorize trades/external sends or silently replace standing fleet rules.

## User requirements — preserve these corrections

- Will sometimes launches independent desk sessions manually from their own directories, in separate windows/Ubuntu terminals. He wants to talk directly to those agents AND have PROME orchestrate those same sessions using the doorbell.
- Direct conversation with Will does not reserve a desk exclusively or make it unavailable to PROME. Will need not go through PROME to assign an easy task, check in or offer a comment.
- The receiving desk reconciles both streams. Ordinary check-ins need no coordination broadcast. Changes to priority, scope, timing, dependencies or helper capacity are reported to PROME. Explicit Will direction takes precedence; ask only about an unresolved conflict.
- PROME discovers and uses an existing live owner before spawning. A manually launched WALTER and a PROME-launched WALTER are not two independent writing seats. Read-only helpers have separate scope.
- Inbox packets remain the durable content lane; doorbells provide timely coordination and point to artifacts. Preserve WALTER's signal-routing mandate. Delivery, execution, verification, Git persistence and downstream consumption are different states.
- Will reports roughly 8–10 instances have been comfortable recently. He has deliberately left headroom for desks to spawn helpers. This is operator experience, not a measured machine limit.
- Example standing group: PROME + WALTER + DAEDALUS + BRENT + SAM + RED + TERRY (seven sessions). Membership is flexible and remains subject to the roster; DAEDALUS is especially useful while doing architecture work.
- PROME's helpers and helpers spawned within independent desk windows must share the available capacity. Multiple terminal windows are not a reliable count of all work or memory use.
- Persistent identity and evidence live in the repository. Reuse useful conversations across related rounds; re-anchor to current files/data before follow-ups. Full closeout at final release; durable checkpoints between tasks. Do not assume an idle process is continuously reasoning or monitoring.

## Implementation sequence and acceptance criteria

### 1. Direct messaging and completion notifications

Test Claude-to-Claude and Codex-to-Codex separately, then establish whether and how Codex-to-Claude can work. A native collaboration handle is not proof of independent-session discovery. A tool advertised in CLI help is not proof of end-to-end message delivery.

For each supported transport, prove: correct recipient identity/directory, delivery while idle, delivery/steering while active, completion notice, unreachable-recipient behavior and recovery without a duplicate owner. Check input/approval handling without bypassing permissions. Retain small evidence receipts. Use harmless, bounded test tasks before domain writes. Read artifacts to verify work; an idle notification only proves a lifecycle event.

Claude's documented `notify_when_idle` is a promising immediate improvement: one-shot completion/exit notice from another local independent session, avoiding repeated status polls. Test its actual availability with the running provider/configuration. Do not assume it works from every subagent or across machines.

### 2. Complete session visibility and shared capacity

Create one generated operational view, preferably extending the existing Fleet-Ops dashboard. Suggested fields: desk, runtime, machine, session ID, working directory, parent, task reference, running/idle/blocked/closed/unknown, helper count, last confirmed activity and evidence source. Distinguish stale records from live discovery; missing observability means UNKNOWN, not DARK.

Cover manually launched sessions, PROME-owned workers and nested helpers. Keep historical orchestration provenance in the existing ORCH_LOG; avoid a competing task/decision source of truth. A runtime registry is an ephemeral operational index.

Measure actual host memory/CPU/process trees under normal use. The sandbox process namespace inspected in this discussion did not expose the desktop, so its memory snapshot cannot set a safe fleet limit. Separate retained sessions, active model work and expensive tools/browser processes. The current native collaboration concurrency limit is also distinct from host capacity.

Initial suggestion, not a ratified hard threshold: target eight concurrent workers/sessions and allow brief bursts toward ten when comfortable. Allocate helper capacity in advance rather than asking Will about every helper. Enforce reservation atomically so two desks cannot both claim the last slot. Release capacity on verified completion/death and reconcile stale reservations. Respect provider/runtime limits even with hardware headroom. Never close Will's active window automatically merely to make room.

Acceptance: inventory sees every pilot participant/helper; competing slot requests cannot overbook; a stale row cannot suppress recovery; a direct Will task can change priority without excluding PROME; no duplicate desk writer is created.

### 3. Lightweight hooks and lifecycle bookkeeping

Use ordinary scripts and available lifecycle events for registration, helper counts, task completion and exit. Claude documents SessionStart/SessionEnd/SubagentStart/SubagentStop; Codex App Server exposes thread/turn events. Inventory existing hooks before adding any. An exit hook may not run after a crash, so reconcile with actual liveness.

Acceptance: start/resume/normal exit/crash/reconnect scenarios produce correct state; failures are visible; bookkeeping does not create LLM polling loops or repeated inbox floods. No automatic inference of success from a process exit. Prefer a thin adapter around supported runtimes to a large replacement framework.

### 4. Compact task and handoff formats

Map to existing COMPLETION_SPEC, inbox and ORCH_LOG fields first. Suggested task content: unique reference, owner, objective, permitted scope, dated input paths, checkable done condition. Follow-up amendments should reference the same task when appropriate.

Maintain separate received/completed/verified/committed/consumed states only where the workflow needs them. Give messages stable task/message references for deduplication and retries; keep detailed evidence in files and completion summaries within the existing ten-line rule. Do not copy every conversation into PROME.

Acceptance: a task can be reconstructed from files after transcript loss; repeated doorbells do not repeat a write; a consequential direct-Will reprioritization reaches PROME; a downstream handoff is not called consumed merely because a packet was sent.

### 5. Context reuse and independent review

Boot each owner correctly once, use related multi-round tasks, refresh STATUS/inbox/changed evidence between rounds, checkpoint after each delivery, and explicitly request full closeout on final release. Respect the currently mandatory owner boot and whole-inbox rules; propose any optimization through their owner rather than silently skipping them.

Use a fresh, narrowly briefed reviewer for load-bearing challenges, including RED where appropriate, without automatically giving it the entire persuasive author transcript. Refresh/restart overloaded or stale conversations from durable state. Preserve unresolved questions, falsifiers, source gaps and approvals in handoffs.

Acceptance: useful follow-ups avoid unnecessary full reboot/closeout cycles, retain the correct prior task context and refresh changed facts. An independent reviewer can recover evidence and challenge a claim without the author's narrative. Measure correctness and operator intervention as well as latency/token usage.

### 6. Selective worktree isolation and Git delivery

Use separate worktrees for independent code/tooling changes when appropriate; retain a deliberate shared-file design for research desks whose inboxes and canonical state must be visible to peers. Keep one owner writer per desk and exact-path commits. Review how to serialize Git operations across manual and managed writers.

Claude background sessions default to worktree isolation before editing, which can break an assumption that a packet appeared in the shared checkout. Test the actual routing/file visibility before adopting that interface for desks; do not disable isolation globally as an unexamined convenience. A worktree is file isolation, not a host resource reduction or extra authority.

Acceptance: code branches integrate cleanly; research packets reach the intended canonical location; no worker commits another writer's staged paths; owner identity and boot instructions are correct in either checkout.

## Pilot and rollout

Start with two participating desks/sessions and a small temporary helper; WALTER + BRENT are suggested only if eligible and relevant after presence checks. Reuse manually opened sessions. Run three rounds: initial task, follow-up including a direct Will input, then controlled interruption/recovery. Simulate queue saturation and duplicate delivery with safe fixtures. Keep market decisions out of infrastructure tests.

Measure useful-result latency, follow-up latency, repeated boot/closeout work, successful/lost/duplicate messages, complete participant visibility, helper peak, memory pressure, recovery correctness and Will interventions. Report cached input, other input and output usage distinctly; aggregate input is neither unique context size nor a dollar bill. Today is an operational baseline, not a controlled benchmark.

Roll out proven components in that order. A fresh independent review is appropriate before changing shared orchestration rules. DAEDALUS can review/design or implement a bounded architecture task after PROME checks for Will's existing DAEDALUS session. Do not launch the entire roster for the pilot.

## Verified facts and open integration gaps as of this discussion

- Installed CLI inspection: Codex `0.153.4`; Claude Code `2.1.263`. Recheck at next boot; these are dated observations.
- Local Codex help exposes `agents`, `queue`, `resume`, `fork` and experimental `app-server`. Generated local App Server schemas include thread start/resume/read and turn start/steer; the steer contract includes the expected active turn ID. No queue message or App Server daemon activation was performed for this investigation.
- Claude documentation describes `/list-agents`, cross-session messages and one-shot idle notifications. Agent view (`claude agents`) lists background sessions; ordinary terminal sessions appear there only after backgrounding, and nested helpers are not separate rows. It is not a full fleet inventory by itself.
- Claude teams have experimental lifecycle limitations, including in-process teammate restoration when resuming the lead. Do not rely on a saved parent transcript to prove children are still alive.
- Codex-to-Claude messaging, shared discovery across runtime/provider variants, exact host limits, restart behavior and worktree/inbox compatibility are UNVERIFIED. Do not equate the existing Claude socket doorbell with Codex native collaboration.
- Existing worker model policy explicitly forbids accidental Fable inheritance for orchestrated owners and specifies Opus in its Claude lane. Today's authorized Astra owners are not a general pricing/model-policy migration. Select and record models deliberately within supported tools; benchmark a Codex policy rather than inventing equivalence.
- The earlier claim that independent Codex sessions could not be directed was too categorical. Local queue/App Server discovery corrected it; end-to-end behavior still needs the pilot.
- Unattended monitoring remains a possible later layer, not an established requirement or already running service. Live mixed sessions are the confirmed priority. Revisit scheduling/feed wakeups after the working-session loop is proven.

## Canonical local references

- `PROME/ORCHESTRATION_PLAYBOOK.md` — two-tier model, boot/re-ping, owner release, worker model policy.
- `MESSAGING/CROSS_SESSION_MESSAGING.md` — durable content versus doorbell coordination, recipient discovery, routing and authority.
- `PROME/COMPLETION_SPEC.md` — compact completion and durable delivery.
- `PROME/ROSTER.md` — launch eligibility; canonical ownership remains flat.
- `PROME/tools/fleet_dashboard.py`, `PROME/state/ORCH_LOG.tsv`, `scripts/orch_log.py` — existing generated view and provenance.
- `PROME/proposals/2026-09-08_codex-desk-presence-fallback-RULED.md` — prior catch-up-specific presence authorization, not a standing fleet-wide replacement.
- `PROME/reports/2026-09-08_owner-orchestration-completion.md` — completed owner catch-up and remaining source-limited items. That work must not be relaunched from stale September 7 prose.

## Primary documentation researched

- [Codex App Server](https://learn.chatgpt.com/docs/app-server): persistent thread operations, turn steering and lifecycle events.
- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents): delegation and context discipline.
- [Claude cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging): independent-session discovery, messaging, idle notices and availability constraints.
- [Claude agent view](https://code.claude.com/docs/en/agent-view): background session management, visibility scope and worktree defaults.
- [Claude agent teams](https://code.claude.com/docs/en/agent-teams): teammate interaction and lifecycle limitations.
- [Claude hooks](https://code.claude.com/docs/en/hooks): lifecycle automation interfaces.
- [Git worktrees](https://git-scm.com/docs/git-worktree): separate checkouts and indexes.
- [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): selective context, compaction and durable notes.

These sources establish product capabilities, not a proven integrated fleet. The implementation sequence and acceptance criteria above are PROME's proposed application to this repository.
