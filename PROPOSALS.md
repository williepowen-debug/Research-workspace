# PROPOSALS.md — Agent Action Queue

*Agents propose actions here. Will approves/rejects via Telegram.*

---

## Pending Proposals

*None currently*

---

## Recent Activity

| ID | Agent | Action | Status | Timestamp |
|----|-------|--------|--------|-----------|
| — | — | System initialized | ✅ | 2026-02-07 |

---

## How This Works

1. **Agent wakes up** (scheduled or triggered)
2. **Agent reviews** its STATUS.md and data
3. **Agent proposes** action if needed (writes here or sends to Prome)
4. **Prome sends** proposal to Will via Telegram with [Approve] [Reject] buttons
5. **Will decides** — tap to approve/reject
6. **On approval** — Agent executes, logs result
7. **On reject** — Logged, no action taken

---

## Proposal Format

```
### [AGENT]-[DATE]-[SEQ]
**Agent:** [NAME]
**Trigger:** [What prompted this]
**Proposed action:** [What agent wants to do]
**Rationale:** [Why this matters]
**Urgency:** [Low/Medium/High/Critical]
**Status:** Pending / Approved / Rejected
```
