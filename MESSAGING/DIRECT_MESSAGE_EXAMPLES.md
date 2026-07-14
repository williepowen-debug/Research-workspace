# Direct Message v1 Examples

These examples normalize patterns observed in committed PROME packets. They are illustrative; they do not retroactively replace the source messages.

## Example 1 — NEXUS correlation update: one ACTION

```yaml
schema: direct-message/v1
message_id: MSG-PROME-20260711-001
created_at: "2026-07-11T12:00:00-04:00"
from: PROME
subject: Refresh Packet-A correlation inputs before the July 14 print
supersedes: null
related:
  - AGENTS/LIQUID/KB-LIQ-071.md
  - HEARTBEAT.md
obligations:
  - obligation_id: MSG-PROME-20260711-001#NEXUS-01
    to: NEXUS
    role: ACTION
    urgency: SCHEDULED
    requested_action: "Reconcile the HYG/Brent non-correlation datum and corrected MOVE reversal in Packet A."
    definition_of_done: "Packet A reflects the current correlation evidence or records a sourced NO_CHANGE decision."
    due: "2026-07-14T09:00:00-04:00"
    receipt_required: true
    expected_targets:
      - AGENTS/NEXUS/STATUS.md
```

Why this helps: the original packet mixed a useful datum with a stale-read correction but did not state a formal role or completion condition. V1 makes the implied action explicit.

## Example 2 — SAM seam proposal: conditional ACTION

```yaml
schema: direct-message/v1
message_id: MSG-PROME-20260711-002
created_at: "2026-07-11T12:10:00-04:00"
from: PROME
subject: Decide the proposed SAM/VIOLET yen-vol seam
supersedes: null
related:
  - AGENTS/VIOLET/STATUS.md
obligations:
  - obligation_id: MSG-PROME-20260711-002#SAM-01
    to: SAM
    role: ACTION
    urgency: SCHEDULED
    requested_action: "Accept the proposed seam and record it, or send PROME a counter-proposal. No analytical work is required before the condition is reviewed."
    definition_of_done: "SAM records acceptance in its seam authority surface or returns a specific counter-proposal to PROME."
    due: "2026-07-16T09:00:00-04:00"
    receipt_required: true
    expected_targets:
      - AGENTS/SAM/STATUS.md
```

Why this helps: “if this works, note it; if not, counter” is still an obligation. V1 makes the two permitted outcomes visible without pretending immediate work is due.

## Example 3 — BRENT packet split into five obligations

One readable message can remain a single research packet, but its envelope expands into independently trackable obligations:

| Obligation | Role | Requested outcome |
|---|---|---|
| `#BRENT-01` | ACTION | Grade whether the KOC platform hit changes the current re-arm/kinetic ladder |
| `#BRENT-02` | ACTION | Reconcile the approximately 6.7 Mbpd GCC curtailment figure against BRENT's book |
| `#BRENT-03` | INFO | Receive the superseding 4.22M bpd Russia crude-export datum |
| `#BRENT-04` | INFO | Receive the WATT spark-spread context; no action requested |
| `#BRENT-05` | ACTION coupled to `#BRENT-01` | Apply the war-long versus current-cycle base-rate caveat to the KOC grade |

Recommended normalization: combine `#BRENT-01` and the caveat into one obligation because the caveat changes how the same decision must be made. Keep the other three independently dispositionable items separate. The result is four obligations, not five:

```yaml
obligations:
  - obligation_id: MSG-PROME-20260712-001#BRENT-01
    to: BRENT
    role: ACTION
    urgency: NEXT_BOOT
    requested_action: "Grade the KOC platform hit against the current-cycle production-infrastructure ladder while incorporating the war-long base-rate caveat."
    definition_of_done: "BRENT records the grade, rationale, and whether the re-arm condition changed."
    due: next_boot
    receipt_required: true
    expected_targets: [AGENTS/BRENT/STATUS.md]
  - obligation_id: MSG-PROME-20260712-001#BRENT-02
    to: BRENT
    role: ACTION
    urgency: NEXT_BOOT
    requested_action: "Reconcile the approximately 6.7 Mbpd GCC curtailment figure against the current BRENT book."
    definition_of_done: "The figure is adopted with source/date, corrected, or rejected with sourced reason."
    due: next_boot
    receipt_required: true
    expected_targets: [AGENTS/BRENT/STATUS.md]
  - obligation_id: MSG-PROME-20260712-001#BRENT-03
    to: BRENT
    role: INFO
    urgency: ROUTINE
    requested_action: null
    definition_of_done: null
    due: null
    receipt_required: false
    expected_targets: []
  - obligation_id: MSG-PROME-20260712-001#BRENT-04
    to: BRENT
    role: INFO
    urgency: ROUTINE
    requested_action: null
    definition_of_done: null
    due: null
    receipt_required: false
    expected_targets: []
```

Why this helps: BRENT can complete the KOC judgment while deferring the GCC reconciliation. The system does not falsely label the entire packet done or undone.

## Example 4 — Peer-to-peer INFO without central routing

VIOLET may write directly to SAM:

```yaml
schema: direct-message/v1
message_id: MSG-VIOLET-20260713-001
created_at: "2026-07-13T14:30:00-04:00"
from: VIOLET
subject: Yen-vol transmission gauge selected
supersedes: null
related: [MSG-PROME-20260711-002]
obligations:
  - obligation_id: MSG-VIOLET-20260713-001#SAM-01
    to: SAM
    role: INFO
    urgency: ROUTINE
    requested_action: null
    definition_of_done: null
    due: null
    receipt_required: false
    expected_targets: []
```

PROME and WALTER do not need to relay this message. Generated views can still correlate it with the earlier seam decision through `related`.

## Example 5 — `NO_CHANGE` is a real completed result

If BRENT reviews the KOC hit and determines the existing status remains correct, the receipt may close the obligation without a content change:

```text
event = NO_CHANGE
target_path = AGENTS/BRENT/STATUS.md
effect_or_reason = Reviewed FALCON baseline and current-cycle conditions; KOC remains below the registered production-infrastructure threshold, so the existing re-arm grade remains valid.
evidence_tier = POINTED
```

This prevents the system from rewarding unnecessary file edits merely to prove activity.
