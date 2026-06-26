# PROME/COMM — Cold-Boot Guide

**If you are Prome reading this for the first time:** this folder is the mailbox between the two Prome work surfaces.

- **Claude Code Prome** = repo-native integrator / file editor / deep agent-state reconciler.
- **OpenClaw Prome** = live operator / Telegram interface / tool runner / real-world execution surface.

COMM exists so one Prome can leave explicit operational messages for the other without relying on chat memory or editing the same hot files.

---

## 30-Second Rule

1. If you are **OpenClaw Prome**, read new files in:
   - `PROME/COMM/TO_OPENCLAW/`

2. If you are **Claude Code Prome**, read new files in:
   - `PROME/COMM/TO_CLAUDE_CODE/`

3. Prioritize messages with:
   - `priority: urgent`
   - `priority: high`
   - `requires_action: true`

4. Do **not** edit the source message to mark it done.

5. Write a separate ack/result file in:
   - `PROME/COMM/ACKS/`

6. If action is external, destructive, trade-related, or a GitHub push, ask Will first.

---

## Folder Map

```text
PROME/COMM/
  README.md             # this cold-boot guide
  PROTOCOL.md           # full rules and schema
  TEMPLATE_MESSAGE.md   # copy when writing a message
  TEMPLATE_ACK.md       # copy when acknowledging/responding
  TO_OPENCLAW/          # Claude Code Prome writes; OpenClaw Prome reads
  TO_CLAUDE_CODE/       # OpenClaw Prome writes; Claude Code Prome reads
  ACKS/                 # response/result files; source messages stay immutable
  ARCHIVE/              # old closed messages, moved during hygiene passes
```

---

## Most Important Rule

**COMM is append-only by default.**

The original message file is a record. Do not mutate it to update status. If you read, complete, block, or supersede a message, create a new ACK file.

Source message `status: open` means “open when written.” The latest matching ACK is the actual current status.

---

## When To Write a COMM Message

Write a message when the other Prome needs to know something that is:

- time-sensitive
- operationally important
- a blocker/caveat
- a handoff between work surfaces
- likely to be lost across clears or sessions

Examples:

- “BOND auction read may have used a TIPS CUSIP; verify before updating state.”
- “HEARTBEAT now contains a 12:30 spawn rail for today’s catalyst.”
- “REGINALD shipped WAL v2.2; OpenClaw should know if Will asks about WAL tape.”
- “Repo is conflicted; do not pull/rebase blindly.”

Do **not** use COMM for full research memos. Link to the owner file instead.

---

## Minimal ACK Example

```md
---
ack_id: 20260521T180000Z-ack-bond-cusip-caveat
message_id: 20260521T174200Z-openclaw-bond-cusip-caveat
from: claude-code-prome
status: completed
---

## Ack
Verified and handled.

## Result / Blocker
Correct nominal source was pulled; BOND state updated. No Will action needed.
```

---

## Safety Boundary

A COMM message can request work. It does **not** authorize:

- GitHub push
- trade execution
- external messages/posts
- destructive file operations
- credential/API changes

Those still require Will approval under normal rules.
