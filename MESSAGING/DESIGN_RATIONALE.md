# Messaging Control Plane v1 — Design Rationale

**Status:** PROPOSAL — NOT RATIFIED  
**Prepared:** 2026-07-13  
**Scope:** Phase 0.5 architecture rationale only; no delivery path, agent boot rule, receipt requirement, or canonical ownership has changed.

## Decision being considered

Whether to add a repository-native messaging control plane that observes the existing file-based messaging system, assigns stable identities, tracks one obligation per recipient, records recipient-owned dispositions, and generates open-obligation views without replacing current inbox, outbox, BOARD, gate, or WALTER routing behavior during the pilot.

The recommended design is a **shadow control plane around the existing system**, not a new transport.

## Authority and current repository constraints

This proposal follows the repository truth hierarchy: Will's current instruction, current repository rules, and canonical owner files outrank this document.

Current constraints found in the repository:

1. Root `CLAUDE.md` defines file-based inbox/outbox coordination and explicitly says not to build ad hoc new cross-agent send protocols or inbox boot auto-triage while the broader messaging overhaul is pending.
2. `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` v0.8 is the current owner specification for WALTER's narrow signal-delivery lane.
3. That WALTER specification already distinguishes published, delivered, and consumed; assigns delivery assertions to WALTER; assigns consumption assertions to recipients; uses one delivery row per signal × recipient; and treats `delivery_log.written_state` as a write-time stamp rather than maintained lifecycle state.
4. `PROME/ACTIVE_DECISIONS.md` assigns WALTER ownership of WALTER routing docs, tools, and spec tuning, while PROME owns operator-facing coordination and behavior review.
5. No root `MESSAGING/` implementation existed when this proposal was prepared.

Consequences:

- This proposal must not redefine WALTER's existing terms silently.
- A shadow adapter may read WALTER-owned records but must not edit or replace them.
- Any implementation that changes root messaging rules, boot behavior, or closeout behavior requires explicit ratification and corresponding canonical-rule updates.
- Research facts and judgments remain canonical in agent-owned files. Messaging metadata must not become a competing research truth surface.

## Repository evidence motivating the design

A retrospective cohort covering ledger dates 2026-07-06 through 2026-07-12 found:

- 47 WALTER messages.
- 103 WALTER recipient obligations: 46 ACTION and 57 INFO.
- 29 obligations involving the proposed seven-agent pilot.
- All 17 pilot ACTION obligations sent to recipients with board logs had a disposition.
- Only 5 of those 17 were labeled `acted`; several `noted` rows nevertheless described updates, citations, folding, or reconciliation.
- PROME received 6 INFO obligations but had no `board_log.tsv`, making missing acknowledgment an instrumentation gap rather than proof of non-consumption.
- Five WALTER rows contained invalid timestamps with minute values `60` through `64`.
- One direct PROME packet to BRENT contained five separable obligations mixing ACTION, INFO, and an appended qualification.
- Direct PROME packets generally lacked formal message IDs, uniform deadlines, and consistent disposition linkage.

The baseline supports two conclusions:

1. Existing delivery evidence is substantially stronger than existing integration evidence.
2. The next improvement should normalize identity and recipient obligations before attempting dashboards or fleet-wide workflow changes.

## External systems principles

The recommendation is not copied from one product. It combines several established patterns.

### 1. Delivery and processing are different events

Amazon SQS separates receiving a message from successfully processing and deleting it. If processing does not complete, the message can become visible again.

- <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html>

Internet messaging standards also distinguish delivery, processing, and display notifications.

- <https://www.rfc-editor.org/info/rfc5438>

**Repository implication:** a committed inbox handoff proves routing. It does not prove acknowledgment, disposition, or integration.

### 2. Stable identity enables correlation and deduplication

The CloudEvents specification requires an event `id` and `source` whose combination uniquely identifies an event; repeated delivery may retain the same identity so consumers can recognize duplicates.

- <https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md>

OpenTelemetry similarly propagates identifiers to correlate work across process and system boundaries.

- <https://opentelemetry.io/docs/concepts/context-propagation/>

**Repository implication:** file path and title are not sufficient identity. Moves, retries, summaries, and supersession must retain a stable message ID.

### 3. Multi-recipient delivery creates recipient-specific state

SMTP delivery-status standards identify both the transaction and the recipients for whom a status notification was issued.

- <https://www.rfc-editor.org/info/rfc3461>

**Repository implication:** one message fanning out to three recipients creates three obligations. One recipient cannot acknowledge or close another recipient's obligation.

### 4. At-least-once delivery requires idempotent processing

Amazon SQS standard queues document at-least-once delivery and possible duplicates. AWS transactional-outbox guidance recommends tracking processed messages so duplicate delivery does not create duplicate effects.

- <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html>
- <https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html>

Apache Kafka documents the distinction between at-most-once, at-least-once, and exactly-once processing semantics.

- <https://kafka.apache.org/41/design/design/>

**Repository implication:** the practical target is not a promise that a file will be encountered exactly once. The target is that repeating the same stable ID will not create duplicate obligations, gates, or canonical research effects.

### 5. Append-only events can generate current-state views

Event-sourcing systems preserve state changes in an append-only record and derive current projections by replaying those records.

- <https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing>

**Repository implication:** receipt history should remain append-only; `OPEN_MESSAGES.tsv`, overdue summaries, and per-agent inbox summaries should be regenerated views rather than independently maintained truth.

### 6. Control loops reconcile desired and actual state

Kubernetes controllers compare declared desired state with reported current state and repeatedly reconcile differences.

- <https://kubernetes.io/docs/concepts/architecture/controller/>

**Repository implication:** a generated control-plane view should compare the desired condition (recipient obligation dispositioned by its deadline) with repository evidence (receipt, board row, processed move, and target artifact).

### 7. Failure and blockage must remain visible

Queue systems use dead-letter handling for messages that repeatedly cannot be processed normally.

- <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-dead-letter-queue.html>

**Repository implication:** `BLOCKED`, `REJECTED`, and `EXPIRED` are observable outcomes. They are preferable to silent disappearance or endless pending state.

### 8. Alerts should be actionable

Google SRE guidance warns that non-actionable paging creates noise and alert fatigue.

- <https://sre.google/sre-book/being-on-call/>

**Repository implication:** ACTION and INFO are different obligation roles. INFO should not automatically create the same deadline and closeout burden as a critical requested action.

### 9. Agent tasks need lifecycle and artifacts

The Agent2Agent protocol distinguishes stateless messages from stateful tasks and models task states and resulting artifacts.

- <https://a2a-protocol.org/latest/topics/life-of-a-task/>

**Repository implication:** a research message may contain information, but an actionable recipient obligation should specify requested work, definition of done, and resulting artifact evidence.

### 10. Incremental replacement reduces migration risk

The strangler-fig pattern introduces new behavior around an existing system and cuts over incrementally rather than through a big-bang rewrite.

- <https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html>

**Repository implication:** observe current messaging first, preserve existing delivery, pilot a narrow priority class, and retain a simple rollback.

## Proposed conceptual model

### Message

The communication object created by a sender or routing owner.

Minimum concepts:

- Stable message ID.
- Created timestamp.
- Sender or routing source.
- Subject and provenance.
- Relationship to prior messages, gates, predictions, or artifacts.
- Immutable identity even if the human-readable title changes.

### Recipient obligation

One recipient-specific interpretation of the message.

Minimum concepts:

- Message ID.
- Recipient ID.
- Role: ACTION or INFO.
- Priority.
- Requested action and definition of done when ACTION.
- Acknowledgment and disposition expectations where applicable.
- Optional expected target artifacts.

A message with four recipients has four obligation rows even if all recipients read the same payload.

### Receipt

A recipient-owned assertion about one obligation.

Candidate states:

- `ACKNOWLEDGED` — received and owned; work may remain.
- `INTEGRATED` — target artifact and effect recorded.
- `NOTED` — read; no artifact change required.
- `BLOCKED` — owned but cannot proceed; blocker and next review recorded.
- `REJECTED` — read and declined with reason.
- `EXPIRED` — no longer actionable under ratified terms.
- `SUPERSEDED` — replaced by another stable message or obligation.

A receipt is evidence of the recipient's assertion. It is not automatically proof that the asserted target changed correctly.

### Artifact evidence

The repository evidence supporting an integration claim.

Minimum concepts:

- Target path or an explicit explanation of why no file change was appropriate.
- Description of the effect.
- Optional commit identifier.
- No duplication of the research fact itself in the messaging ledger.

### Projection

A generated current-state view derived from messages, obligations, receipts, and adapters.

Examples:

- Open ACTION obligations.
- Unacknowledged critical obligations.
- Acknowledged but undispositioned obligations.
- Blocked obligations and next review.
- Integration claims without target evidence.
- Duplicate or invalid routes.

Generated views must identify their generator and source records.

## Proposed state boundaries

Message-level and recipient-level state must not be collapsed.

### Message-level properties

- Created.
- Superseded.
- Globally expired only when all relevant obligations expire under the same terms.

### Recipient-obligation states

- Routed.
- Acknowledged.
- Integrated.
- Noted.
- Blocked.
- Rejected.
- Expired.
- Superseded.

A message must not be labeled globally `INTEGRATED` merely because one recipient integrated it.

## Shadow-mode source-of-truth boundaries

During shadow mode:

| Concern | Authoritative source |
|---|---|
| Research fact, thesis, gate logic, or current judgment | Canonical agent/owner file |
| WALTER signal content and routing decision | Existing BOARD, route log, delivery log, and WALTER-owned spec |
| Existing direct packet payload | Existing committed inbox/outbox artifact |
| Existing WALTER consumption evidence | Recipient board log plus processed-path evidence under v0.8 |
| Shadow normalized record | Generated adapter output, explicitly non-canonical |
| New recipient receipt, before ratification | Pilot evidence only; must not override owner research files |
| Open/overdue summaries | Generated projections only |

A future ratification may make new receipt files canonical for recipient-obligation disposition. That decision is not made by this document.

## Compatibility rules proposed from the baseline

- WALTER route-log row → message `CREATED`.
- WALTER delivery row plus git-derived handoff evidence → recipient obligation `ROUTED`.
- Board `acted` → `ACKNOWLEDGED` plus an integration claim; target evidence still required.
- Board `noted` or `info-only` → `NOTED`, unless separate target evidence shows an integration effect.
- Board `deferred` → `ACKNOWLEDGED` and open; use `BLOCKED` only with an explicit blocker.
- Board `skipped` → candidate `REJECTED` only when a reason is present.
- Processed move plus matching board row → consumed under WALTER v0.8; not necessarily integrated.
- Direct committed inbox packet → created and routed with a deterministic legacy ID.
- A mixed or numbered packet → one message with multiple recipient-obligation rows.
- Outbox/delivered copy → routing evidence only.
- Silence → unknown; never acknowledgment or integration.
- NEXUS topology rows or fired gates without a concrete packet → related control records, not messages by themselves.

## Alternatives considered

### A. Extend only the existing WALTER board-log system

Advantages:

- Smallest implementation.
- Proven in live use.
- Preserves WALTER ownership and current paths.

Limitations:

- Does not cover direct PROME and peer packets uniformly.
- Current dispositions conflate acknowledgment and integration.
- PROME and some agents lack equivalent instrumentation.
- Does not produce one cross-lane open-obligation view.

Use: retain as a canonical source and compatibility input, not the entire control plane.

### B. Root shadow control plane with adapters and recipient receipts

Advantages:

- Covers WALTER and non-WALTER lanes without replacing either.
- Keeps one recipient obligation per row.
- Permits generated views and validation.
- Can be rolled back by stopping generation.
- Supports incremental priority-class cutover.

Limitations:

- Risks creating a second source of truth if boundaries are unclear.
- Adds receipt and closeout burden.
- Requires explicit ownership ratification.

Recommendation: preferred, subject to the decision gates below.

### C. Use GitHub Issues as the primary task system

Advantages:

- Stable IDs, assignees, comments, and status.
- Existing user interface.

Limitations:

- Splits institutional memory between repository files and issue metadata.
- Weak fit for high-volume INFO traffic and agent-owned closeout.
- Requires network/API availability and different ownership rules.
- Encourages manual mirrors of canonical research state.

Recommendation: not for v1; potentially useful later for operator-approved implementation work.

### D. Introduce a database, broker, or workflow engine

Advantages:

- Mature querying, retry, concurrency, and operational features.

Limitations:

- Adds infrastructure and operational ownership disproportionate to the current serial, Git-native system.
- Creates synchronization and dual-write problems with canonical repository state.
- Makes rollback and forensic inspection more complex.

Recommendation: out of scope until the file-native pilot demonstrates a measured need.

### E. Treat file movement as the entire lifecycle

Advantages:

- Very simple and already partially implemented.

Limitations:

- Cannot reliably distinguish noted, integrated, rejected, blocked, or expired.
- Cannot express multiple recipient outcomes.
- Renames and directory conventions become overloaded as business state.

Recommendation: retain processed moves as evidence, not as the complete lifecycle.

## Primary risks and mitigations

| Risk | Mitigation |
|---|---|
| Duplicate source of truth | Keep research canon in owner files; label generated views; store pointers and effects, not copied research claims. |
| Receipt toil | Start with new IMMEDIATE/PRIORITY ACTION obligations; make INFO acknowledgment optional unless ratified otherwise. |
| PROME becomes a larger bottleneck | Recipients own dispositions; PROME receives generated exceptions rather than manually updating every record. |
| WALTER ownership is weakened | Adapter reads WALTER records; WALTER retains routing judgment and current tooling. |
| False overdue flags for dormant agents | Registry points to canonical roster state; use operating-time policy and explicit dormant handling. |
| Automatic inference overclaims integration | Separate recipient claim from verified target evidence; preserve confidence/evidence tier. |
| Duplicate routing creates duplicate effects | Stable IDs, alias mapping, and idempotent obligation keys. |
| Identifier conflicts | Use one ratified allocator under the repository's current serial-machine assumption; validator rejects duplicates. |
| Schema becomes too complex | Begin with the minimum fields needed to reproduce the baseline and open-obligation views. |
| Pilot corrupts existing workflow | Shadow-only generation; no redirect or deletion of existing inbox/outbox paths; rollback stops generation. |

## Pilot hypotheses

The following are hypotheses to test, not established facts:

1. Stable IDs will reduce duplicate and ambiguous routing enough to justify their maintenance cost.
2. One obligation per recipient will reveal open work more accurately than one message-level state.
3. Requiring target evidence for `INTEGRATED` will improve auditability without causing excessive closeout burden.
4. INFO messages can remain optional-receipt without hiding critical work.
5. A generated critical-overdue view will reduce PROME's manual chase workload.
6. The seven-agent cohort is representative enough to expose schema defects before fleet rollout.
7. A narrow priority-class pilot will produce useful latency and disposition metrics within one week.
8. File-native records and Git history are sufficient for v1 without a broker or database.

## Decisions required before implementation

This proposal requests explicit disposition of the following:

1. **Location:** approve or reject root `MESSAGING/` as the shadow control-plane location.
2. **Scope:** confirm PROME, WALTER, NEXUS, SAM, BRENT, VIOLET, and HOMER as the pilot.
3. **Canonical boundary:** confirm existing owner files and WALTER records remain canonical during shadow mode.
4. **Identifier policy:** approve `AGT-<NAME>`, `MSG-YYYYMMDD-NNNN`, and immutable legacy aliases.
5. **Obligation model:** approve one row/state per message × recipient.
6. **Integration evidence:** decide whether target path + effect is mandatory for `INTEGRATED`.
7. **Priority mapping:** decide whether WALTER `IMMEDIATE` maps to critical and `PRIORITY` maps to urgent; keep ACTION/INFO separate from priority.
8. **INFO policy:** decide whether INFO receipts are optional, sampled, or required.
9. **Clock policy:** define operating hours, dormant-agent handling, weekends, and deadline pauses.
10. **First live scope:** choose all pilot messages or only new IMMEDIATE/PRIORITY ACTION messages.
11. **Canonical rule reconciliation:** approve the necessary root-rule update before any boot/closeout or send-protocol change.
12. **Ownership:** designate the schema/validator owner and generated-view owner without changing WALTER's routing ownership.

## Recommended next gate

Do not begin boot/closeout changes or message-record writes merely because this document exists.

After Will reviews and dispositions the decisions above:

1. Record the ratified decisions in the canonical decision surface.
2. Add minimal schemas and an agent-ID mapping that points to `PROME/ROSTER.md` rather than duplicating roster status.
3. Build a read-only historical normalizer.
4. Require it to reproduce the fixed baseline: 47 messages, 103 obligations, 29 pilot obligations, five invalid timestamps, and the five-way BRENT packet split.
5. Review the generated output manually.
6. Only then consider recipient receipt files and live pilot hooks.

## Rollback

Before live hooks, rollback is deletion or abandonment of the proposal branch.

During a future shadow pilot, rollback means stopping shadow record generation and generated views while leaving existing inbox, outbox, BOARD, route, delivery, gate, and agent-owned files unchanged. Pilot evidence should be retained for evaluation rather than erased.

## Summary recommendation

Ratify a **root, file-native, shadow control plane** that wraps rather than replaces current messaging. Model a message separately from its recipient obligations, require stable identity, keep recipient assertions append-only, distinguish claimed from evidenced integration, and generate operator views from source records.

The design is intentionally conservative: no database, no broker, no fleet-wide migration, no silent override of WALTER, and no inference of consumption from delivery or silence.
