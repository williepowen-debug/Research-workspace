# PROME/COMM Plan — Prome-to-Prome Mailbox

**Status:** Draft for Will review
**Created:** 2026-05-21
**Purpose:** Define a merge-safe, low-friction communication layer between Claude Code Prome and OpenClaw/Telegram Prome.

---

## 1. Design Goal

Create a small file-based mailbox that lets each Prome instance pass operationally important information to the other without relying on vague chat memory, overwriting shared state, or causing Git merge conflicts.

This should support the emerging architecture:

- **Claude Code Prome:** repo-native integrator, file editor, deep agent state reconciler.
- **OpenClaw Prome:** live operator, Telegram interface, tool runner, real-world execution surface.

The mailbox is not a replacement for `HEARTBEAT.md`, `TODAY.md`, or `SCRATCH.md`. It is a targeted message layer for items one Prome needs the other Prome to see or act on.

---

## 2. What Makes It Useful

A useful Prome-to-Prome system must be:

1. **Merge-safe** — no two agents edit the same live message file.
2. **Attention-efficient** — reader can scan priority/action fields without parsing prose.
3. **Durable** — messages survive clears, session restarts, and context loss.
4. **Auditable** — later we can reconstruct who said what, when, and why.
5. **Low ceremony** — writing a message should take under one minute.
6. **Action-oriented** — every message says whether action is required, optional, or informational.
7. **Non-duplicative** — detailed analysis stays in owner files; COMM messages point to it.
8. **Safe by default** — no pushes/external actions implied by a message; approvals stay with Will.

---

## 3. Proposed Directory Layout

```text
PROME/COMM/
  PROTOCOL.md                 # Rules, schema, examples
  TO_OPENCLAW/                # Claude Code Prome writes; OpenClaw Prome reads
  TO_CLAUDE_CODE/             # OpenClaw Prome writes; Claude Code Prome reads
  ACKS/                       # Acknowledgement/response files; originals never edited
  ARCHIVE/                    # Optional monthly archive of old/closed messages
  INDEX.md                    # Optional generated/maintained queue summary
```

### Ownership

| Path | Writer | Reader | Rule |
|---|---|---|---|
| `TO_OPENCLAW/` | Claude Code Prome | OpenClaw Prome | OpenClaw does not edit messages in-place |
| `TO_CLAUDE_CODE/` | OpenClaw Prome | Claude Code Prome | Claude Code does not edit messages in-place |
| `ACKS/` | Either | Either | Write new ack files; do not mutate source |
| `ARCHIVE/` | Prome during hygiene pass | Either | Move old/closed messages only when safe |
| `INDEX.md` | optional, Prome-owned | Either | Useful but can become conflict-prone; keep optional |

---

## 4. Message File Naming

Use unique timestamped filenames so writes are append-only and conflict-resistant.

Format:

```text
YYYYMMDDTHHMMSSZ_from-to_slug.md
```

Examples:

```text
20260521T173500Z_openclaw-to-cc_bond-cusip-caveat.md
20260521T181200Z_cc-to-openclaw_heartbeat-updated-10y-branch.md
```

Rules:
- UTC timestamp preferred for uniqueness.
- Slug should be short and human-readable.
- Never reuse filenames.
- Never edit another Prome's message file except typo-only before commit.

---

## 5. Message Schema

Each message starts with YAML front matter:

```md
---
id: 20260521T173500Z-openclaw-bond-cusip-caveat
from: openclaw-prome
to: claude-code-prome
priority: high            # low | normal | high | urgent
status: open              # open | acknowledged | closed | superseded
requires_action: true
response_requested: true
related_files:
  - AGENTS/BOND/research/TIPS_5_21_READ_2026-05-21.md
  - HEARTBEAT.md
due: 2026-05-21T20:00:00Z
---
```

Then body:

```md
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

## 6. Priority Semantics

| Priority | Meaning | Expected handling |
|---|---|---|
| `urgent` | Time-sensitive within minutes/hours; catalyst, blocker, safety issue | Check immediately on boot/heartbeat |
| `high` | Important today; affects decisions/state | Handle same session if possible |
| `normal` | Useful context or next-session task | Handle during normal boot/inbox sweep |
| `low` | Hygiene, nice-to-have, design note | Batch/archive later |

Hard rule: `urgent` should be rare. If everything is urgent, nothing is.

---

## 7. Status / Ack Model

To avoid merge conflicts, the original message file should generally remain immutable.

Instead of editing `status: open` in the source message, the reader writes an ack file:

```text
PROME/COMM/ACKS/20260521T193904Z_ack_bond-cusip-caveat.md
```

Ack schema:

```md
---
ack_id: 20260521T174200Z-ack-bond-cusip-caveat
message_id: 20260521T173500Z-openclaw-bond-cusip-caveat
from: claude-code-prome
status: acknowledged       # acknowledged | completed | blocked | superseded
---

## Ack
Received. I will verify nominal vs TIPS CUSIP before updating BOND state.

## Result / Blocker
Optional.
```

This keeps the system append-only and Git-friendly.

---

## 8. Boot / Heartbeat Integration

### OpenClaw Prome boot or heartbeat

1. Check `PROME/COMM/TO_OPENCLAW/` for unacknowledged `urgent` and `high` messages.
2. If action is internal and reversible, act.
3. If external/destructive/trade-related, ask Will.
4. Write ack/result to `ACKS/`.
5. Promote lasting state to `HEARTBEAT.md`, `TODAY.md`, or `SCRATCH.md` only when appropriate.

### Claude Code Prome boot

1. Pull/rebase per existing boot rules.
2. Check `PROME/COMM/TO_CLAUDE_CODE/` for unacknowledged `urgent` and `high` messages.
3. Act only within Claude Code Prome's allowed scope.
4. Write ack/result to `ACKS/`.
5. Update owner docs if needed.

---

## 9. What Belongs in COMM

Good COMM messages:

- “BOND post-auction used a possible TIPS CUSIP; verify before final state update.”
- “HEARTBEAT updated with 10Y auction branch; OpenClaw should spawn BOND around 12:30.”
- “REGINALD shipped WAL v2.2; Telegram Prome should surface tape-vs-fundamental read to Will if asked.”
- “Claude Code Prome found conflict in STATUS; OpenClaw should avoid pull until resolved.”

Bad COMM messages:

- Full research memos — put those in agent research folders and link them.
- Random thoughts without action or relevance.
- Trade instructions without Will approval.
- Anything requiring both agents to edit same file simultaneously.

---

## 10. Efficiency Features

### A. Minimal message template

For fast writes:

```md
---
id:
from:
to:
priority: normal
status: open
requires_action: false
response_requested: false
related_files: []
due:
---

## Summary

## Why it matters

## Requested action
```

### B. Optional index

`INDEX.md` can summarize open messages:

```md
# PROME COMM INDEX

## Open urgent/high
- [ ] 20260521T173500Z — BOND CUSIP caveat → Claude Code Prome

## Recently completed
- [x] ...
```

But `INDEX.md` is optional because it can become a merge hotspot. If used, update only during controlled hygiene passes.

### C. Archive policy

Monthly or weekly:
- Move acknowledged/completed messages older than 7 days to `ARCHIVE/YYYY-MM/`.
- Keep open messages in active folders.
- Do not archive unresolved blockers.

---

## 11. Safety / Git Rules

- COMM messages can request action; they do not authorize external actions, pushes, or trades.
- No GitHub push without Will approval.
- Local commits are okay as checkpoints if scoped and merge-safe.
- Subagents may write scratch/LAST_COMPLETION, but do not commit/push unless explicitly authorized.
- Message files should be additive; avoid editing existing messages.
- If a pull/rebase conflict touches COMM, preserve both sides and create a new reconciliation message if needed.

---

## 12. Initial Implementation Plan

Phase 1 — Scaffold:
1. Create `PROME/COMM/PROTOCOL.md` from this plan.
2. Create folders: `TO_OPENCLAW/`, `TO_CLAUDE_CODE/`, `ACKS/`, `ARCHIVE/`.
3. Add `.gitkeep` files so empty folders persist.
4. Add `TEMPLATE_MESSAGE.md` and `TEMPLATE_ACK.md` if useful.

Phase 2 — First real message:
1. OpenClaw Prome writes first message to Claude Code Prome: BOND CUSIP/TIPS caveat.
2. Claude Code Prome acks/handles later.

Phase 3 — Boot integration:
1. Add one line to `PROME/BOOT.md`: check COMM inbox after SCRATCH/TODAY/STATUS.
2. Add one line to Claude Code Prome boot docs if appropriate.

Phase 4 — Review after 1 week:
1. Count messages written/handled.
2. Identify friction/conflicts.
3. Decide whether `INDEX.md` is worth maintaining.

---

## 13. Recommendation

Build Phase 1 now, but keep it intentionally simple. Do **not** build automation or indexing yet. The first win is creating a safe, explicit mailbox where the two Prome surfaces can pass important operational context without competing over `HEARTBEAT.md` or `SCRATCH.md`.
