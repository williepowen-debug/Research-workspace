# Direct Agent Messaging v1 Specification

**Status:** DEFAULTS RATIFIED FOR IMPLEMENTATION — NOT YET LIVE  
**Version:** 1.0-rc2  
**Prepared:** 2026-07-13  
**Owner proposed:** PROME for operations; Will for ratification; WALTER retains exclusive ownership of WALTER routing semantics.

## 1. Purpose

Direct Messaging v1 makes agent-to-agent inbox work traceable without replacing the repository's file-native workflow.

It answers six questions reliably:

1. What was sent?
2. Who sent it and who owes a response?
3. Is it information or an assignment?
4. Has the recipient reviewed and dispositioned it?
5. What result was produced?
6. Did that result change a canonical artifact?

The system is a control plane around readable Markdown messages. It is not a broker, database, autonomous supervisor, or new research authority.

## 2. Scope and non-goals

### In scope

- PROME-to-agent direct packets.
- Agent-to-PROME requests.
- Peer-to-peer agent messages.
- One message copied to multiple recipients.
- Multiple distinct obligations contained in one readable packet.
- Recipient-owned acknowledgments, dispositions, and outcome evidence.
- Generated open-work and diagnostics views.
- Read-only compatibility with legacy direct messages and WALTER signals.

### Out of scope for v1

- Replacing inbox directories.
- Routing all messages through PROME or WALTER.
- Changing WALTER's filtering, BOARD, route log, delivery log, signal IDs, priorities, or ownership.
- Making messaging records canonical for research facts, theses, positions, or gates.
- Autonomous escalation, task reassignment, or research judgment.
- A database, queue service, GitHub Issues workflow, or external orchestration service.
- Backfilling every historical inbox file.

## 3. Two-lane architecture

| Lane | Purpose | Native authority | v1 treatment |
|---|---|---|---|
| WALTER signal lane | External news, images, research returns, alerts, and threshold signals | WALTER's BOARD, routing specifications, route/delivery logs, and recipient board evidence | Read-only adapter; preserve `SIG-W` identity and semantics |
| Direct message lane | PROME tasking, peer coordination, questions, corrections, handoffs, and contextual notes | Sender's delivered message plus recipient-owned receipt | New v1 contract |

No v1 component may require WALTER to carry an ordinary direct message. No adapter may write into WALTER-owned records.

## 4. Authority and ownership

| Object | Owner | Rule |
|---|---|---|
| Message payload | Sender | Immutable after delivery; corrections supersede |
| Recipient obligation | Sender at creation | Recipient may disposition but not rewrite the request |
| Receipt and event history | Recipient | Sender cannot assert receipt or completion for recipient |
| Research artifact | Existing domain owner | Messaging metadata only points to it |
| Generated projection | Generator | Rebuildable, non-canonical view |
| WALTER signal/routing record | WALTER | Read-only to direct-messaging components |
| Schema and validator | PROME operationally, after Will ratification | WALTER-specific mappings require WALTER-compatible review |

The sender may create files only in the recipient's established delivery area. After delivery, the recipient owns processing and receipt records inside the recipient's directory.

## 5. Identity

### 5.1 Message ID

Format:

`MSG-<SENDER>-<YYYYMMDD>-<NNN>`

Example:

`MSG-PROME-20260713-001`

Rules:

- `SENDER` is the canonical uppercase agent ID from `PROME/ROSTER.md`; `WILL` is allowed for operator-authored packets.
- `NNN` is a zero-padded sender-local sequence for that UTC date.
- The combination must be repository-unique.
- The ID never changes when a file moves, is copied to another recipient, or is summarized.
- Retrying delivery reuses the same message and obligation IDs.
- The sender tool allocates the next sequence; the validator rejects collisions.

### 5.2 Obligation ID

Format:

`<MESSAGE-ID>#<RECIPIENT>-<NN>`

Example:

`MSG-PROME-20260713-001#BRENT-02`

Each distinct requested operation or independently dispositionable INFO item receives its own obligation ID. A message sent to three recipients creates at least three obligations. One recipient cannot close another recipient's obligation.

### 5.3 Legacy identity

Historical direct files may be assigned deterministic adapter IDs beginning `LEGACY-`. These are compatibility aliases, not retroactive edits to source files.

WALTER signals retain their `SIG-W...` IDs. The adapter must not allocate parallel `MSG-...` identities for them.

## 6. Delivery location and filename

V1 preserves the existing recipient inbox transport:

`AGENTS/<RECIPIENT>/inbox/<optional-sender-subdirectory>/`

Recommended filename:

`<MESSAGE-ID>__<PRIMARY-ROLE>__<short-slug>.md`

Example:

`MSG-PROME-20260713-001__ACTION__koc-platform-grade.md`

For messages addressed to PROME, the implementation must use PROME's ratified incoming-message location rather than assume an `AGENTS/PROME/` directory.

A committed file at the correct inbox path proves `ROUTED`. An uncommitted local file proves only `CREATED_LOCAL` and must not appear as delivered in network views.

## 7. Message envelope

Messages are Markdown with a small YAML front matter envelope followed by human-readable content.

Required message fields:

| Field | Requirement |
|---|---|
| `schema` | Exactly `direct-message/v1` |
| `message_id` | Valid stable ID |
| `created_at` | ISO 8601 timestamp with timezone |
| `from` | Canonical sender ID |
| `subject` | Short human-readable subject |
| `supersedes` | Empty or prior message ID |
| `related` | Zero or more message, signal, gate, prediction, or artifact references |
| `obligations` | One or more structured recipient obligations |

Required obligation fields:

| Field | ACTION | INFO |
|---|---:|---:|
| `obligation_id` | Required | Required |
| `to` | Required | Required |
| `role` | `ACTION` | `INFO` |
| `urgency` | Required | Required |
| `requested_action` | Required and operational | Empty |
| `definition_of_done` | Required | Empty |
| `due` | Required unless `ROUTINE` | Optional |
| `receipt_required` | Always `true` | Default `false` |
| `expected_targets` | Optional | Empty |

The Markdown body may be as detailed as necessary, but it must not contradict the envelope. When they conflict, the validator reports an error and no automated lifecycle inference is allowed.

## 8. Roles and urgency

### Roles

- `ACTION`: the recipient owes a decision or operation.
- `INFO`: the recipient is being informed; no work is implied.

Questions requiring a response are ACTION. Conditional requests are ACTION with the condition stated in `requested_action`. An INFO item must not hide phrases such as “update,” “reconcile,” “decide,” or “report back.”

### Direct-message urgency

| Urgency | Meaning | Due rule |
|---|---|---|
| `URGENT` | Review at the next safe opportunity; may justify operator attention | Explicit timestamp required |
| `NEXT_BOOT` | Review during the recipient's next normal session | `next_boot` allowed |
| `SCHEDULED` | Review or finish by a known date/time | Explicit timestamp required |
| `ROUTINE` | Context or work with no immediate clock | Due may be empty |

Urgency is independent of ACTION/INFO. These terms belong to the direct lane and do not redefine WALTER's FLASH/IMMEDIATE/PRIORITY/ROUTINE semantics.

## 9. One packet, many obligations

A readable file may contain multiple numbered items, but every independently decidable item must appear as a separate obligation in the envelope and eventual ledger.

Use one obligation when several facts jointly support one requested decision. Use multiple obligations when the recipient could complete, reject, defer, or integrate the items separately.

An appended caveat that materially changes an existing obligation should normally supersede the message. It must not be silently added after delivery.

## 10. Receipt location and form

Proposed recipient-owned location:

`AGENTS/<RECIPIENT>/messages/receipts/<MESSAGE-ID>__<RECIPIENT>.md`

Each receipt covers all obligations for that recipient in one message. It contains immutable identifying metadata and an append-only event table. Existing event rows are never rewritten; corrections append a new event that cites the mistaken row.

The receipt file is authoritative only for the recipient's assertions. It cannot establish that the underlying research conclusion is correct.

## 11. Lifecycle events

### Transport events

- `CREATED_LOCAL`: source file exists locally but is not yet committed.
- `ROUTED`: committed inbox delivery exists.
- `SUPERSEDED`: a later message explicitly replaces this message or obligation.
- `CANCELLED`: sender withdraws an open obligation through a new signed message/event; history remains.

### Recipient events

| Event | Meaning | Open afterward? |
|---|---|---:|
| `ACKNOWLEDGED` | Reviewed, but no disposition yet | Yes |
| `ACCEPTED` | Recipient accepts responsibility | Yes |
| `DEFERRED` | Intentionally postponed; next review required | Yes |
| `BLOCKED` | Cannot proceed; blocker and owner required | Yes |
| `REJECTED` | Declined with reason | No |
| `NOTED` | INFO consumed; no artifact change required | No |
| `COMPLETED` | Requested work performed; result/evidence recorded | Depends on integration requirement |
| `INTEGRATED` | Result applied to the identified canonical target | No |
| `NO_CHANGE` | Review completed and evidence supports no artifact change | No |

Rules:

- `ACCEPTED`, `DEFERRED`, `BLOCKED`, `REJECTED`, and `NOTED` all imply acknowledgment; a separate `ACKNOWLEDGED` event is needed only when the recipient has not decided.
- ACTION requires a disposition. INFO requires a receipt only when `receipt_required: true`; otherwise silence remains unknown and creates no overdue alert.
- `COMPLETED` is not automatically `INTEGRATED`.
- If integration is required, `COMPLETED` remains open until `INTEGRATED` or `NO_CHANGE` is recorded.
- `DEFERRED` requires `next_review_at`; `BLOCKED` requires blocker, blocker owner, and next review.
- `REJECTED` requires a reason and may recommend a correct recipient.

## 12. Evidence tiers

| Tier | Meaning | Example |
|---|---|---|
| `ASSERTED` | Recipient states an outcome | “Updated STATUS” with no pointer |
| `POINTED` | Exact target path and effect supplied | `AGENTS/BRENT/STATUS.md`, revised KOC grade |
| `CORROBORATED` | Target inspection agrees with the claim | Generated validator finds the message ID or expected change |
| `COMMIT_LINKED` | Commit identifier also supplied | Commit containing the target change |

`INTEGRATED` requires at least `POINTED`: exact target path plus a concise description of the effect. The messaging system does not copy the research finding into its ledger.

`NO_CHANGE` requires an explanation of what was checked and why the current canonical artifact remains valid.

## 13. Supersession and correction

- Delivered message content is immutable.
- A material correction creates a new message with `supersedes: <old-id>`.
- The replacement states which obligations are replaced and whether any old obligation remains valid.
- Generated views close superseded obligations only when the replacement relationship is valid.
- Minor typographical corrections that do not change meaning may be fixed before commit; after commit, preserve history and prefer a correction message.
- Duplicate delivery with the same IDs is idempotent and must not create duplicate obligations.

## 14. Generated views and diagnostics

Generated outputs are rebuildable and non-canonical. Minimum views:

- Open ACTION obligations.
- ACTION obligations routed but undispositioned.
- Deferred and blocked obligations with next review.
- Completed work awaiting integration evidence.
- Recently closed obligations.
- Optional INFO receipt coverage.
- Legacy and WALTER adapter records labeled by provenance.

Minimum validation errors:

- Duplicate or malformed IDs.
- Invalid sender or recipient.
- Invalid timestamp or timezone.
- ACTION missing requested action, definition of done, or due rule.
- INFO containing a structured requested action.
- Obligation recipient inconsistent with delivery path.
- Receipt owned by the wrong recipient.
- Receipt referencing a nonexistent obligation.
- Invalid lifecycle transition.
- `INTEGRATED` without target path and effect.
- Broken supersession reference.
- Multiple obligation rows collapsed into one lifecycle state.

Diagnostics report; they do not rewrite research or reassign work automatically.

## 15. Compatibility behavior

### Legacy direct messages

- Source files remain untouched.
- Adapter derives `LEGACY-...` message identities and one row per recipient obligation.
- Committed inbox presence proves routing only.
- Processed moves and board rows are evidence of consumption, not automatic integration.
- Silence is unknown.

### WALTER

- Preserve native `SIG-W` identity.
- Preserve WALTER ACTION/INFO role and native priority as source fields.
- BOARD/route/delivery records remain WALTER authority.
- Recipient board disposition and processed move remain consumption evidence under WALTER's current spec.
- Map into shared generated views only through a labeled read-only adapter.
- Do not require new direct-message receipt files for WALTER signals in v1.

### Live team messages

Ephemeral `SendMessage` coordination is not independently durable. Any decision, assignment, or result that must survive the session must still be written to a repository artifact. V1 may later provide a helper to convert a live team instruction into a direct message.

## 16. Ratified implementation defaults

Will approved the following defaults on 2026-07-13. They authorize implementation and testing on the design branch, not live activation.

| Decision | Recommended v1 choice |
|---|---|
| Location | Root `MESSAGING/` for shared specification, tooling, schemas, adapters, and generated views |
| Primary implementation scope | All new direct agent-to-agent messages after cutover; no long pilot |
| Message format | Markdown plus constrained YAML front matter |
| Message ID | `MSG-<SENDER>-<YYYYMMDD>-<NNN>` |
| Obligation unit | One state per message × recipient × independently decidable item |
| ACTION receipts | Required |
| INFO receipts | Optional unless sender explicitly requires one |
| Integration proof | Exact target path plus effect required |
| Receipt storage | Recipient-owned `messages/receipts/` directory |
| WALTER treatment | Native read-only adapter; no duplicate identity or receipt lane |
| Historical backfill | Baseline and on-demand only |
| Operational schema owner | PROME, with Will ratification and WALTER boundary protection |
| Automatic escalation | Disabled in v1; dashboards report exceptions to Will/PROME |
| Time policy | Explicit due timestamps use ISO 8601; `NEXT_BOOT` remains a first-class due value |

## 17. Acceptance criteria for implementation

V1 is ready to activate when:

1. Templates validate and remain readable without tools.
2. Sender tool allocates unique IDs and writes only to allowed inbox locations.
3. Validator reproduces the fixed baseline compatibility cases, including the five-way BRENT packet split.
4. Recipient receipts cannot disposition another recipient's obligation.
5. Generated views distinguish routed, acknowledged, completed, and integrated.
6. WALTER fixtures ingest without altering `SIG-W` IDs or native files.
7. Duplicate processing is idempotent.
8. Rollback can stop v1 generation while leaving existing inboxes and WALTER intact.
9. Root and agent instructions are reconciled in the same activation change.
