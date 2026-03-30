# PROME Boot

**Injection:** AGENTS.md, SOUL.md, USER.md always injected. HEARTBEAT.md + MEMORY.md main sessions only. Do NOT re-read injected files.

**Tools:** `pdfminer.six` installed (`from pdfminer.high_level import extract_text`).
**Calendar:** CALENDAR.md syncs to Google Calendar ("Research Ops") via `tools/calendar/sync_calendar.py`. Run after any CALENDAR.md edit. Cron auto-syncs 7 AM ET weekdays.
**Market Data:** `FORGE/tools/market-data/` — `fetch.py` (live prices + FRED), `config.py` (thresholds), `dashboard.py` (CLI stress dashboard). Use `python3 dashboard.py` before citing any price. Cron runs every 5min (self-throttled). Morning briefing at 6 AM ET to Telegram. Web dashboard at :8080 (`/api/stress`).

1. **Read `PROME/TODAY.md`** — what's actually happening today. Catalysts, decisions, levels.
2. **Read `PROME/SCRATCH.md`** — ephemeral scratchpad, handoff from last session.
2. **Read `PROME/STATUS.md`** — dashboard, positions, priorities.
3. **Read `PROME/TOSCANINI/QUEUE.md`** — active proposals + signal queue.
4. **Triage Prome inbox** — `AGENTS/PROME/inbox/`. Scan for signals that change priorities. Deep-read anything flagged in SCRATCH.
5. **Score and rank** — run HUNTING.md scoring (position proximity ×2, time pressure ×1.5, blindness ×1, convergence ×1, decay ×1) across all candidate work items. Re-rank QUEUE.md. This is internal — don't show Will the math, just present proposals in ranked order.
6. **Read `LESSONS.md`** (workspace root) — mistakes to avoid.
7. **Read `memory/YYYY-MM-DD.md`** (today only). Yesterday on-demand if SCRATCH references unresolved items.
8. **Be proactive:** Check pending actions in STATUS, alert on catalysts within 24h, flag stale agents.
9. **Present top proposals** when Will checks in (max 5 per batch, ranked by score).

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

### Toscanini — Orchestration Layer
Named for Arturo Toscanini. Prome's decision interface with Will. **This is how we work together.**

- **PROTOCOL.md** — Rules: binary proposals (Approve/Reject), max 5 per check-in, 🔴/🔵/🟢 priority
- **AUTONOMY.md** — Three tiers: free (internal ops) / propose (new work) / always ask (external, positions)
- **QUEUE.md** — Live proposals awaiting Will's decision. Read at boot, present when Will checks in.
- **DECISIONS.md** — Log of past decisions + outcomes. Tracks judgment patterns over time.
- **COMPLETION_SPEC.md** — Standard report block every sub-agent must write when finishing. STATUS/CHANGED/RESULT/GAPS/WILL_NEEDS/FOLLOW-UP.
- **WILL_QUEUE.md** — Things blocked on Will's direct action (brokerage screenshots, logins, judgment calls).

**Signal batching rule:** Agents spawn when they accumulate 3+ unread signals. Exception: 🔴🔴 CRITICAL singles spawn immediately.

**Every sub-agent spawn must include the COMPLETION_SPEC instructions** so Prome can process results efficiently.

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
| ~~carl~~ | ~~Consumer credit~~ 🖥️ **Claude Code — DO NOT SPAWN** | liquid | Funding/Treasury |
| ~~reginald~~ | ~~Regional banks~~ 🖥️ **Claude Code — DO NOT SPAWN** | ~~sam~~ | ~~Japan/BOJ/JGB~~ 🖥️ **Claude Code — DO NOT SPAWN** |
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
