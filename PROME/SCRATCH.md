# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-03 ~10:45 PM ET

---

## RIGHT NOW — Chunk 2: Template + OUTBOX/INBOX Push

**Task:** Update CLAUDE_TEMPLATE.md with OUTBOX.md protocol, then push updated instructions to all 11 agent CLAUDE.md files. Create OUTBOX.md for all agents.

### What to add to CLAUDE_TEMPLATE:
- OUTBOX.md in spawn protocol: "If findings are relevant to another agent's domain, write a signal to OUTBOX.md with target agent name."
- OUTBOX.md signal format (FROM, TARGET, signal summary, timestamp)
- OUTBOX.md in FILES table
- Keep it minimal — HERMES handles delivery, agents just drop signals

### Agents to update (11):
LABOR, CARL, SAM, HENRY, LIQUID, REGINALD, HAWK, MARCO, HANS, ZHAO, DARWIN

Each needs:
1. OUTBOX.md created in agent workspace (`/home/moltbot/.openclaw/agents/*/workspace/`)
2. CLAUDE.md updated with OUTBOX instruction + workbook logging rules (from template)

### Already done:
- CLAUDE_TEMPLATE.md has workbook logging rules (added tonight)
- INBOX.md exists for all agents (fixed tonight)
- HENRY and LIQUID workbooks repaired (audit + fill)

### Agent workspace paths:
- Agent CLAUDE.md: `/home/moltbot/.openclaw/agents/{name}/workspace/` (some have CLAUDE.md, some have AGENTS.md — check each)
- Domain symlink: `domain` → `/home/moltbot/.openclaw/workspace/AGENTS/{NAME}/`

---

*This file is disposable. Rewrite freely. No preservation guilt.*
