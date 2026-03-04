# AGENTS.md — OTTO Workspace

## Every Session (Boot Sequence)

0. **Check `INBOX.md`** — Process pending signals from other agents (INTEGRATE, LOG, or DISCARD). **For each signal, log a one-line entry to ML.tsv:** `ML-XXX-NNN | [date] | INBOX: [sender] re: [topic] → INTEGRATED to VX-XXX-NN / DISCARDED ([reason])`
1. **Read `STATUS.md`** — signal dashboard, active vectors, priorities
2. **Read `SOUL.md`** — who you are
3. **Read `USER.md`** — who you're helping
4. **Read `LESSONS.md`** — mistakes to avoid
5. **Read `CLAUDE.md`** — domain instructions
6. **Check `inbox/`** folder — new signals from other agents

## Memory

- **Files > Brain** — write it down or lose it
- Daily notes: `memory/YYYY-MM-DD.md`
- Long-term: `MEMORY.md` (main session only)

## Safety

- Private things stay private. `trash` > `rm`.
- Internal actions (read, organize, search): do freely
- External actions: ask first

## Signal Routing

| Agent | Domain | How to Send |
|-------|--------|-------------|
| BROCK | Private credit / BDC exposure | Drop file in `AGENTS/BROCK/inbox/` |
| REGINALD | Bank exposure / regional stress | Drop file in `AGENTS/REGINALD/inbox/` |
| CARL | Consumer stress / macro | Drop file in `AGENTS/CARL/inbox/` |
| LIQUID | Market liquidity / ABS | Drop file in `AGENTS/LIQUID/inbox/` |

**Receiving:** Check `AGENTS/OTTO/inbox/` for inbound signals.

## Session End (Handoff)

1. Update `STATUS.md` dashboard
2. Write `memory/YYYY-MM-DD.md` with "Last context:" opener
3. Commit and push

## Heartbeats

Follow `HEARTBEAT.md`. Use for periodic checks on fraud cases, earnings dates, court filings.

---

## OUTBOX — Cross-Agent Signals

When you discover something relevant to another agent's domain, append it to `OUTBOX.md`. Don't deep-dive it yourself.

HERMES (mail carrier) delivers signals to target agents twice daily.

**Sending to WILL (the human):** Use `To: WILL` for items that need human decision-making — trade ideas, position changes, threshold breaches requiring action, or time-sensitive approvals. Don't send routine analysis; only things Will needs to see or act on.
 You just drop them in OUTBOX.md.

## WORKBOOK RULES

| File | What goes in | Test |
|------|-------------|------|
| `ML.tsv` | New data points with sources. Timestamped facts. | "Is this new evidence?" |
| `VX.tsv` | Vector state changes (GREEN→RED, new vector, threshold crossed) | "Did a risk indicator move?" |
| `FLOW.tsv` | Transmission channels confirmed, changed, or newly identified | "Did we learn HOW stress travels?" |
| `FL.tsv` | Upcoming dated catalysts. Archive passed events. | "Is there a date to watch?" |

**Log significant findings to workbook, not just STATUS.md.** STATUS gets rewritten; workbook is permanent.
