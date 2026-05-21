# PROME/COMM Protocol — Prome-to-Prome Mailbox

**Purpose:** Merge-safe communication between Claude Code Prome and OpenClaw/Telegram Prome.

Claude Code Prome is the repo-native integrator. OpenClaw Prome is the live operator / real-world interface. This mailbox lets them pass operationally important context without relying on fuzzy memory or editing the same hot files.

---

## Directory Layout

```text
PROME/COMM/
  PROTOCOL.md
  TEMPLATE_MESSAGE.md
  TEMPLATE_ACK.md
  TO_OPENCLAW/       # Claude Code Prome writes; OpenClaw Prome reads
  TO_CLAUDE_CODE/    # OpenClaw Prome writes; Claude Code Prome reads
  ACKS/              # acknowledgement/result files; source messages stay immutable
  ARCHIVE/           # old closed messages, archived during hygiene passes
```

---

## Core Rules

1. **Append-only by default.** Write a new message file; do not edit another Prome's message in place.
2. **Ack with a new file.** Reader responds in `ACKS/`, not by changing `status:` in the source message.
3. **Keep messages short.** Link to owner files for full analysis.
4. **No authority escalation.** A COMM message does not authorize GitHub pushes, external messages, destructive actions, or trades.
5. **No GitHub push without Will approval.** Local scoped commits are allowed unless Will changes the rule.
6. **Use COMM for handoffs, caveats, blockers, and action requests — not full research memos.**

---

## Message Naming

```text
YYYYMMDDTHHMMSSZ_from-to_slug.md
```

Examples:

```text
20260521T173500Z_openclaw-to-cc_bond-cusip-caveat.md
20260521T181200Z_cc-to-openclaw_heartbeat-updated-10y-branch.md
```

Use UTC timestamps. Never reuse filenames.

---

## Message Schema

```md
---
id: 20260521T173500Z-openclaw-bond-cusip-caveat
from: openclaw-prome
to: claude-code-prome
priority: high              # low | normal | high | urgent
status: open                # open | acknowledged | closed | superseded
requires_action: true
response_requested: true
related_files:
  - AGENTS/BOND/scratch/2026-05-21_10Y_postauction_dual_grade.md
due: 2026-05-21T20:00:00Z
---

## Summary
One or two sentences.

## Why it matters
Trading/state/ops implication.

## Requested action
Concrete next step, or `None — informational only`.

## Notes
Optional context. Link, don't duplicate, long analysis.
```

---

## Ack Naming

```text
ACKS/YYYYMMDDTHHMMSSZ_ack_<message-id-or-short-slug>.md
```

Ack files use this schema:

```md
---
ack_id: 20260521T174200Z-ack-bond-cusip-caveat
message_id: 20260521T173500Z-openclaw-bond-cusip-caveat
from: claude-code-prome
status: acknowledged        # acknowledged | completed | blocked | superseded
---

## Ack
Received. I will verify nominal vs TIPS CUSIP before updating BOND state.

## Result / Blocker
Optional.
```

---

## Priority Semantics

| Priority | Meaning | Handling |
|---|---|---|
| `urgent` | Time-sensitive within minutes/hours; catalyst, blocker, safety issue | Check immediately on boot/heartbeat |
| `high` | Important today; affects decisions/state | Handle same session if possible |
| `normal` | Useful next-session task/context | Handle during normal boot/inbox sweep |
| `low` | Hygiene/design note | Batch later |

Use `urgent` rarely.

---

## Boot / Heartbeat Integration

### OpenClaw Prome

On boot/heartbeat, check `PROME/COMM/TO_OPENCLAW/` for unacknowledged `urgent` and `high` messages. Act if internal/reversible; ask Will for external/destructive/trade actions. Write an ack/result in `ACKS/`.

### Claude Code Prome

On boot after pull/rebase, check `PROME/COMM/TO_CLAUDE_CODE/` for unacknowledged `urgent` and `high` messages. Act within allowed repo scope. Write an ack/result in `ACKS/`.

---

## What Belongs Here

Good:
- “BOND post-auction may have used a TIPS CUSIP; verify before final state update.”
- “HEARTBEAT updated with 10Y auction branch; OpenClaw should spawn BOND around 12:30.”
- “REGINALD shipped WAL v2.2; Telegram Prome should be aware of tape-vs-fundamental disagreement.”
- “Pull/rebase conflict in Prome state; avoid new edits until resolved.”

Bad:
- Full research reports.
- Random thoughts with no relevance/action.
- Trade instructions without Will approval.
- Large duplicated excerpts from owner files.
