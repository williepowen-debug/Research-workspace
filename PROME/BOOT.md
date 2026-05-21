# PROME Boot

**Injection:** AGENTS.md, SOUL.md, USER.md always injected. HEARTBEAT.md + MEMORY.md main sessions only. Do NOT re-read injected files.

---

## Tools

**Market Data:** `FORGE/tools/market-data/` — `fetch.py` (live prices + FRED), `config.py` (thresholds), `dashboard.py` (CLI stress dashboard). Use `python3 dashboard.py` before citing any price. Cron: 5min (self-throttled). Morning briefing 6 AM ET. Web: `:8080/api/stress`. **Citation convention:** FRED data has T+1 publication lag — always cite FRED-sourced numbers with observation-date stamp (e.g., `HY OAS 280bps [FRED 5/20 close]`). Full convention in `FORGE/tools/market-data/README.md` § Citation Convention.

**News Sweep:** `FORGE/tools/news-sweep/` — `sweep.py` (fetcher + classifier + router), `config.py` (queries, entity index, WATCH_FOR lists, keywords, source weights). Cron M-F 8:30 AM ET + Telegram push. On-demand: `python3 sweep.py --compact --route`. Web: `/api/news`. **Prome maintains** the entity index and WATCH_FOR lists — update after major STATUS changes or agent COMPLETION_SPECs.

**Dashboard Server:** `dashboard/server.py` — HTTP API on :8080. Key endpoints: `/api/status`, `/api/stress`, `/api/news`, `/api/agents`, `/api/prices`, `/api/predictions`.

**Calendar:** CALENDAR.md syncs to Google Calendar via `tools/calendar/sync_calendar.py`. Cron 7 AM ET weekdays. *(Currently broken — Google OAuth issue.)*

**Other:** `pdfminer.six` installed (`from pdfminer.high_level import extract_text`).

---

## Doc Ownership

**Rule: If you catch yourself writing the same data in two docs, stop. Put it in the owner doc and reference from the other.**

| Doc | Owns | Does NOT contain |
|-----|------|-----------------|
| **TODAY.md** | Today's date, catalysts, task checklist, key market levels, notable shifts | Agent operational state, pending system actions |
| **STATUS.md** | Agent health table, pending actions, resolved items, intelligence quality notes | Market levels or catalyst calendar (→ TODAY), thesis narrative (→ HEARTBEAT) |
| **SCRATCH.md** | Session handoff — what just happened, immediate state, pending items for next Prome | Anything that should persist beyond one session (→ MEMORY.md or STATUS) |
| **HEARTBEAT.md** *(root, injected)* | Scenario weights, threshold table, catalyst calendar (48h), position decisions pending | Agent operational details (→ STATUS), full position sizing (→ POSITIONS) |
| **POSITIONS.md** | Full portfolio: entries, stops, sizing, P&L, account value | Operational priorities or agent health |
| **PREDICTIONS_MONITOR.md** | Falsifiable predictions with resolution dates and outcomes | Position details or daily catalysts |
| **OUTBOX.md** | Prome's outbound signals for agents | Anything else |
| **FLEET_SCAN.md** | Latest fleet situation report — agents, catalysts, open loops, top-N moves | Domain analysis (→ agent STATUS files) |
| **ORCHESTRAL_LAYER_DESIGN.md** | Design + ranking rubric for fleet-scan / top-N / revival-proxy workflow | Per-session scans (→ FLEET_SCAN.md) |
| **CLOSEOUT.md** | Standardized session-end procedure | Boot procedure (→ BOOT.md) |
| **AUTONOMY.md** | Tier 1/2/3 permission model + autonomy change log | Specific spawn rules (→ AGENTS.md) |
| **COMPLETION_SPEC.md** | Sub-agent `LAST_COMPLETION.md` report format | Anything else |
| **CLAUDE_CODE_PROME_PLAN.md** | Architecture plan for persistent Claude Code Prome | Current implementation status (→ TASKS) |
| **CLAUDE_CODE_PROME_TASKS.md** | Restart-safe task ladder for building Claude Code Prome | Detailed operating manual after scaffold exists |
| **CLAUDE_CODE_HANDOFF.md** | Handoff from Claude Code Prome sessions | General Telegram/OpenClaw handoff (→ HANDOFF/SCRATCH) |
| **memory/YYYY-MM-DD.md** | Daily session log — what was done, files changed, handoff notes | Long-term insights (→ MEMORY.md root) |
| **MEMORY.md** *(root, injected)* | Curated long-term discoveries, thesis framework, system architecture | Daily session details (→ memory/) |

---

## Boot Sequence

0. **`git pull --rebase`** — sync Claude Code agent changes before reading anything. If blocked by dirty/untracked files, **stop and read handoff/status first; do not stash, commit, reset, or force without Will approval.**
1. **Read `PROME/SCRATCH.md`** — session handoff from last Prome. What's hot, what's unfinished.
2. **Read `PROME/TODAY.md`** — today's catalysts, levels, task checklist.
3. **Read `PROME/STATUS.md`** — agent health, pending actions, priorities.
4. **Read `PROME/FLEET_SCAN.md`** — latest fleet situation report (agents, catalysts, open loops, top moves). If absent or stale (>1 day), spawn a `fleet-scanner` subagent per `PROME/ORCHESTRAL_LAYER_DESIGN.md`.
5. **If working on Claude Code Prome, read `PROME/CLAUDE.md`, `PROME/CLAUDE_CODE_PROME.md`, `PROME/CLAUDE_CODE_PROME_PLAN.md`, and `PROME/CLAUDE_CODE_PROME_TASKS.md` before editing.** The task ladder is the restart-safe implementation source of truth.
6. **Read `PROME/CLAUDE_CODE_HANDOFF.md` after clears or after any Claude Code Prome session.** Claude Code Prome must update that file at session end. Normal Telegram/OpenClaw sessions still use this boot sequence and remain Will-facing.
7. **Check `PROME/COMM/TO_CLAUDE_CODE/`** — Prome-to-Prome mailbox from OpenClaw/Telegram Prome. Read any message not yet matched by an ACK in `PROME/COMM/ACKS/`. Prioritize `urgent` / `high`. Write an ACK (new file in `PROME/COMM/ACKS/`, do **not** edit the source message) with status `acknowledged` / `completed` / `blocked`. Protocol: `PROME/COMM/PROTOCOL.md`. Cold-boot guide: `PROME/COMM/README.md`.
8. **Triage Prome inbox** — `AGENTS/PROME/inbox/`. Scan for signals that change priorities.
9. **Score and rank** — use the ranking rubric in `PROME/ORCHESTRAL_LAYER_DESIGN.md` (Position Proximity ×2, Time Pressure ×1.5, Blindness Risk, Convergence, Decay Rate, System Freshness). Apply to candidate moves; honor the four anti-patterns (busywork, loudness, completionism, recency bias). Internal — don't show Will the math.
10. **Be proactive:** Flag catalysts within 24h, stale agents, pending decisions, blocking items.
11. **Present top proposals** when Will checks in (max 5 per batch, ranked by score).

---

## Memory Lifecycle

| File | Policy | Frequency |
|------|--------|-----------|
| `PROME/SCRATCH.md` | **Full rewrite each session.** Ephemeral — current state + next actions. Overwrite, don't append. | Every session |
| `memory/YYYY-MM-DD.md` | **Build within day, fresh next day.** Append checkpoints and session logs. One file per calendar day. | Continuous |
| `MEMORY.md` | **Curated long-term.** Promote lasting insights from daily notes. Prune superseded entries. | Weekly review |
| Old daily notes (>14 days) | **Archive — don't load at boot.** Read on-demand for past events. Don't delete. | As needed |

**Weekly maintenance (first session of the week):**
1. Skim past week's `memory/` dailies
2. Pull anything missing from `MEMORY.md`
3. Prune `MEMORY.md` — remove stale, superseded, or resolved entries
4. Verify `SCRATCH.md` reflects current state

---

## Orchestral Layer

TOSCANINI was retired 2026-05-18. The current orchestral layer is captured in `PROME/ORCHESTRAL_LAYER_DESIGN.md` — a fleet-scan + adversarial-pair top-N + revival-proxy pattern that delegates heavy reading to subagents so Prome's main context stays clean.

| File | Purpose |
|------|---------|
| **`PROME/ORCHESTRAL_LAYER_DESIGN.md`** | Design + ranking rubric (Position Proximity ×2, Time Pressure ×1.5, etc.) + four anti-patterns. Source of truth for orchestral work. |
| **`PROME/FLEET_SCAN.md`** | Latest fleet situation report, produced on demand by `fleet-scanner` subagent. |
| **`PROME/AUTONOMY.md`** | Tier 1/2/3 permission model + autonomy change log (salvaged from TOSCANINI). |
| **`PROME/COMPLETION_SPEC.md`** | Sub-agent `LAST_COMPLETION.md` report format (salvaged from TOSCANINI). |
| **`PROME/archive/TOSCANINI_2026-03/`** | Historical TOSCANINI files for reference. Do not read at boot. |

**Every sub-agent spawn must include COMPLETION_SPEC instructions** (pattern survives retirement).

---

## Agent IDs (for spawning)

| ID | Domain | ID | Domain |
|----|--------|----|--------|
| labor | Employment/claims | henry | Market structure/econ data |
| ~~carl~~ | ~~Consumer credit~~ 🖥️ **DO NOT SPAWN** | liquid | Funding/Treasury |
| ~~reginald~~ | ~~Regional banks~~ 🖥️ **DO NOT SPAWN** | ~~sam~~ | ~~Japan/BOJ/JGB~~ 🖥️ **DO NOT SPAWN** |
| brock | BDC/private credit | zhao | China/capital flows |
| nexus | Cross-agent synthesis | hans | Europe (US lens) |
| hawk | Geopolitical/military | brent | Oil/energy markets |
| marco | Migration/labor flows | shade | PE-insurance-captive |
| hermes | Signal delivery | darwin | System evolution |
| otto | Auto/consumer DQ | red | Adversarial analysis |
| oracle | Prediction markets | | |

**Spawn:** `sessions_spawn(agentId="<id>", task="...", cleanup="keep")`
**Steer:** `subagents(action="list")` / `subagents(action="steer", target="<key>", message="...")`
**Spawn-ready rule:** If agent STATUS.md >10KB, prune before spawning.

Full manual: `docs/OPERATIONS.md` | Full roster: `AGENTS_DIRECTORY.md`

---

## NEXUS — Synthesis Layer

Spawn after check-in rounds or when multiple signals arrive.
Reads: Agent STATUS headers (first 30 lines), SIGNALS.md, PREDICTIONS_MONITOR.md
Outputs: Convergence reports, contradiction flags, threshold proximity matrix

---

## On-Demand (not at boot)

- `LESSONS.md` (workspace root) — mistakes to avoid. Review periodically.
- `memory/YYYY-MM-DD.md` — daily session logs. Read today's if SCRATCH references unresolved items.
- `BRIEFING.md`, `CALENDAR.md`, `FORGE/STATUS.md`, `FORGE/ACTIVE_TRADES.md`
- `WILL/` — journal, `IDEAS.md`, `trading-journal/`
- Agent STATUS files (`AGENTS/*/STATUS.md`)
- `PROME/HANDOFF.md` — read before `/clear` or `/new`
- `PROME/CLAUDE_CODE_PROME_PLAN.md` + `PROME/CLAUDE_CODE_PROME_TASKS.md` — read when resuming the Claude Code Prome build
- `PROME/CLAUDE_CODE_HANDOFF.md` — read once created, especially after Claude Code Prome sessions
- `PROME/CLOSEOUT.md` — session-end procedure (read before `/clear` or `/new`)
- `PROME/COMM/TEMPLATE_MESSAGE.md` + `PROME/COMM/TEMPLATE_ACK.md` — copy when writing a message to OpenClaw Prome or acking one of his
- `PROME/archive/TOSCANINI_2026-03/` — retired governance docs (read on-demand for historical context only)

---

## Git Protocol

**Never `git add -A` or `git add .`.** Claude Code agents (CARL, REGINALD, SAM, RED) share this repo and only stage their own `AGENTS/<NAME>/` dirs. If Prome does `git add -A`, it sweeps up their uncommitted work.

**Prome scoped commits:**
```bash
git add MEMORY.md AGENTS.md HEARTBEAT.md PROME/ TOOLS.md  # only what you changed
git commit -m "..."
git push
```
Add other specific files as needed (FORGE/, memory/, etc.) but never blanket-add.

---

## Key Reference Files

| File | When |
|------|------|
| `AGENTS/templates/KB_MIGRATION_PLAYBOOK.md` | Before KB/TSV migration |
| `AGENTS/VOCABULARIES.tsv` | Before writing to any KB.tsv |
| `AGENTS/templates/CLAUDE_TEMPLATE.md` | Before spawning or reviewing agent structure |
