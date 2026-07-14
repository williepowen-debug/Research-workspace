# Direct Message v1 Templates

These templates are proposed and are not live until ratified.

## ACTION message

```markdown
---
schema: direct-message/v1
message_id: MSG-SENDER-YYYYMMDD-NNN
created_at: "YYYY-MM-DDTHH:MM:SS-04:00"
from: SENDER
subject: Short decision-oriented subject
supersedes: null
related:
  - PATH-OR-ID
obligations:
  - obligation_id: MSG-SENDER-YYYYMMDD-NNN#RECIPIENT-01
    to: RECIPIENT
    role: ACTION
    urgency: NEXT_BOOT
    requested_action: "Specific operation or decision the recipient owes."
    definition_of_done: "Observable condition that closes the request."
    due: next_boot
    receipt_required: true
    expected_targets:
      - AGENTS/RECIPIENT/STATUS.md
---

# Short subject

## Why you are receiving this

Explain the routing reason and relevant context.

## Evidence or inputs

- Source, date, and exact datum.
- Relevant repository path or native signal ID.

## Requested action

Restate the request in natural language. Clarify judgment boundaries and caveats.

## Definition of done

State what the recipient must produce, decide, update, or explicitly leave unchanged.
```

## INFO message

```markdown
---
schema: direct-message/v1
message_id: MSG-SENDER-YYYYMMDD-NNN
created_at: "YYYY-MM-DDTHH:MM:SS-04:00"
from: SENDER
subject: Short informational subject
supersedes: null
related: []
obligations:
  - obligation_id: MSG-SENDER-YYYYMMDD-NNN#RECIPIENT-01
    to: RECIPIENT
    role: INFO
    urgency: ROUTINE
    requested_action: null
    definition_of_done: null
    due: null
    receipt_required: false
    expected_targets: []
---

# Short subject

## Why you are receiving this

Explain why the datum is relevant to the recipient.

## Information

Provide the sourced information and related paths.

**No action is requested.**
```

## Recipient receipt

```markdown
---
schema: direct-receipt/v1
message_id: MSG-SENDER-YYYYMMDD-NNN
recipient: RECIPIENT
obligations:
  - MSG-SENDER-YYYYMMDD-NNN#RECIPIENT-01
---

# Receipt — MSG-SENDER-YYYYMMDD-NNN — RECIPIENT

Append events. Never rewrite or remove an earlier event row.

| event_at | obligation_id | event | next_review_at | target_path | effect_or_reason | commit | evidence_tier |
|---|---|---|---|---|---|---|---|
| YYYY-MM-DDTHH:MM:SS-04:00 | MSG-SENDER-YYYYMMDD-NNN#RECIPIENT-01 | ACCEPTED |  |  | Accepted for next session |  | ASSERTED |
| YYYY-MM-DDTHH:MM:SS-04:00 | MSG-SENDER-YYYYMMDD-NNN#RECIPIENT-01 | INTEGRATED |  | AGENTS/RECIPIENT/STATUS.md | Updated the named judgment and cited the source | abc1234 | COMMIT_LINKED |
```

## Blocked event example

Use `effect_or_reason` to name the blocker and blocker owner:

```text
Waiting for the 2026-07-16 TIC release; blocker owner: external publication.
```

`next_review_at` is mandatory for `BLOCKED` and `DEFERRED`.

## Superseding correction

Create a new message rather than editing the delivered file:

```yaml
message_id: MSG-PROME-20260713-004
supersedes: MSG-PROME-20260713-001
related:
  - MSG-PROME-20260713-001
```

The body must say exactly which prior obligations are replaced.
