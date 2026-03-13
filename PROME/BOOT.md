# PROME Boot

**Injection:** AGENTS.md, SOUL.md, USER.md always injected. HEARTBEAT.md + MEMORY.md main sessions only. Do NOT re-read injected files.

**Tools:** `pdfminer.six` installed (`from pdfminer.high_level import extract_text`).

1. **Read `PROME/SCRATCH.md`** — ephemeral scratchpad. Read FIRST.
2. **Read `PROME/STATUS.md`** — dashboard, positions, priorities.
3. **Read `LESSONS.md`** (workspace root) — mistakes to avoid.
4. **Read `memory/YYYY-MM-DD.md`** (today only). Yesterday on-demand if SCRATCH references unresolved items.
5. **Be proactive:** Check pending actions in STATUS, alert on catalysts within 24h, flag stale agents.

### Memory Lifecycle

| File | Policy | Frequency |
|------|--------|-----------|
| `PROME/SCRATCH.md` | **Full rewrite each session.** Ephemeral only — current state + immediate next actions. Not a log. Overwrite, don't append. |  Every session start or handoff |
| `memory/YYYY-MM-DD.md` | **Build within day, start fresh next day.** Append checkpoints and session logs throughout the day. One file per calendar day. | Continuous |
| `MEMORY.md` | **Curated long-term.** Promote insights from daily notes that have lasting value (discoveries, corrections, framework shifts). Remove entries that are fully superseded or no longer relevant. | Weekly review |
| Old daily notes (>14 days) | **Archive — don't load at boot.** Read on-demand only if investigating a specific past event. Don't delete — they're the audit trail. | As needed |

**Weekly maintenance (fold into first session of the week):**
1. Skim past week's `memory/` dailies
2. Pull anything missing from `MEMORY.md`
3. Prune `MEMORY.md` — remove entries that are stale, superseded, or fully resolved
4. Verify `SCRATCH.md` reflects current state (not last week's handoff)

### On-Demand (not at boot)
- `BRIEFING.md`, `CALENDAR.md`, `FORGE/STATUS.md`, `FORGE/ACTIVE_TRADES.md`
- `WILL/` — journal, `IDEAS.md`, `trading-journal/`
- Agent STATUS files (`AGENTS/*/STATUS.md`)
- `PROME/HANDOFF.md` — read before `/clear` or `/new`

---

## Agent IDs (for spawning)

| ID | Domain | ID | Domain |
|----|--------|----|--------|
| labor | Employment/claims | henry | Market structure/econ data |
| carl | Consumer credit | liquid | Funding/Treasury |
| reginald | Regional banks | sam | Japan/BOJ/JGB |
| brock | BDC/private credit | zhao | China/capital flows |
| nexus | Cross-agent synthesis | hans | Europe (US lens) |
| hawk | Geopolitical/military | brent | Oil/energy markets |
| marco | Migration/labor flows | shade | PE-insurance-captive |
| hermes | Signal delivery | darwin | System evolution |
| otto | Auto/consumer DQ | red | Adversarial analysis |

**Spawn:** `sessions_spawn(agentId="<id>", task="...", cleanup="keep")`
**Steer/check:** `subagents(action="list")` / `subagents(action="steer", target="<sessionKey>", message="...")`
**Follow-up:** `sessions_send(sessionKey="agent:<id>:subagent:...", message="...")`
**Spawn-ready rule:** If agent STATUS.md >10KB, prune before spawning.

Full manual: `docs/OPERATIONS.md` | Full roster: `AGENTS_DIRECTORY.md`

---

## NEXUS — Synthesis Layer

Spawn after check-in rounds or when multiple signals arrive.
Reads: Agent STATUS headers (first 30 lines), SIGNALS.md, PREDICTIONS_MONITOR.md
Outputs: Convergence reports, contradiction flags, threshold proximity matrix

---

## Key Reference Files

| File | When |
|------|------|
| `AGENTS/templates/KB_MIGRATION_PLAYBOOK.md` | Before KB/TSV migration |
| `AGENTS/VOCABULARIES.tsv` | Before writing to any KB.tsv |
| `AGENTS/templates/CLAUDE_TEMPLATE.md` | Before spawning or reviewing agent structure |
