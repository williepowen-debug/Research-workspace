# Prome System Map
**Created:** 2026-05-08 21:28 ET · **Updated:** 2026-07-01 (hygiene trim: dead `dashboard/server.py` row cut; OpenClaw spawn-prohibition → teams-mode reality; serial-multi-machine phrasing; HY-watch → intake-lane primary; FSK example marked historical; FORGE/STATUS caveat re-based). Prior: 2026-06-26 surgical refresh.  
**Owner:** Prome  
**Purpose:** Current architecture map for Prome’s operating system — what each file owns, what to trust, and where future Prome should look first.

---

## North Star

Prome’s system exists to turn public-data research into disciplined decisions without losing context, duplicating facts, or making ad hoc calls under pressure.

Core rule:

> Put facts in the owner file. Other files should point to it, not copy it.

---

## Boot Trust Stack

### Auto-loaded each session (Claude Code)

| File | Trust | Role |
|---|---|---|
| `CLAUDE.md` (root + `PROME/`) | High | Repo + PROME operating rules — the only docs Claude Code genuinely auto-injects. |
| `MEMORY.md` (auto-memory index — lives in-repo at `memory/auto/`, symlinked from `~/.claude`) | High for curated lessons; check freshness | Operating lessons / findings / feedback index — the genuinely-injected memory layer. |

*(`AGENTS.md` + `USER.md` are **explicit boot-reads**, not injected — see the next table. `SOUL.md` + `IDENTITY.md` were deleted root-level in the 2026-06-30 public-prep cleanup.)*

> ⚠️ **`HEARTBEAT.md` is NOT injected (OpenClaw vestige).** It was auto-loaded under the always-on VPS model; in Claude Code it is NOT in PROME's boot context — PROME must explicitly `Read` it. It is a **PROME-facing regime memo only**: PROME writes it, PROME reads it. Domain agents (incl. NEXUS) do **not** boot-read it (verified 2026-06-27: 19/20 agent CLAUDE.md have zero HEARTBEAT references). See `BOOT.md`'s market-data freshness gate.

### Read at boot / when resuming

| File | Cadence | Role |
|---|---|---|
| `USER.md` | Each fresh session (stable) | Will's operator model — communication/thinking style, edge, psychology. The operator manual for Will-facing work. |
| `AGENTS.md` | When roster/routing relevant | Agent roster, transmission chains, spawn restrictions. |
| `PROME/BOOT.md` | Maintained | Boot sequence + protocol reminders (trust/ownership map lives here). |
| `PROME/HANDOFF.md` | Refreshed each closeout (latest 3–5 entries) | Cross-runtime continuity. |
| `PROME/SCRATCH.md` | Full rewrite each closeout | Ephemeral session state + next-session entry point + **operator card** (date, catalysts, near-gates — absorbed `TODAY.md` 2026-07-01). |
| `PROME/STATUS.md` | Surgical at closeout | Operational status, work queue, agent/system health. |
| `PROME/ACTIVE_DECISIONS.md` | Surgical when a decision moves | Non-terminal decision safety index. |
| `PROME/FLEET_SCAN.md` | On-demand | Fleet/agent stale-state scan and ranked candidate moves. |
| `KERNELS.md` | On-demand reference | Thesis-spine: compressed transmission map + durable system lessons (renamed from root `MEMORY.md` 6/30; not injected). |
| `memory/YYYY-MM-DD.md` | On-demand (daily log) | Daily session activity detail; not root-memory insight. |

### Canonical → Mirrors map

*(Added 2026-07-01, seeded from the 24-file audit. When a **canonical** doc changes, walk its row and verify each mirror before commit — CLOSEOUT Chunk-3 trigger. Canonical wins on drift (`[[finding_doc_mirror_consistency_check]]`). The weekly spine audit (`PROME/tools/spine_audit.workflow.js`) checks the same rows as the catch-all.)*

| Canonical fact | Canonical home | Known mirrors (verify on canon change) |
|---|---|---|
| Git/push protocol (pathspec, auto-push, non-ff=routine, repo-root cwd) | root `CLAUDE.md` Git Protocol | `PROME/CLAUDE.md` (git-default ¶) · `PROME/BOOT.md` (non-negotiables) · `PROME/GIT_COORDINATION.md` (cookbook + Push Discipline) · `PROME/CLOSEOUT.md` (Chunk 4) · `PROME/AUTONOMY.md` (header note) · auto-memory `feedback_defer_push_coordinate` |
| Machine model (serial multi-machine, desktop ⇄ laptop) | root `CLAUDE.md` + `PROME/MACHINE_LOCAL.md` | `PROME/CLAUDE.md` (identity) · `SYSTEM.md` (Prome Runtime) · `ORCHESTRAL_LAYER_DESIGN.md` (open-questions bullet) · `public-prep/HISTORY_SCRUB_PLAN.md` (safety rail 5) |
| HY-watch mechanism (intake lane primary, desktop timer redundancy) | `HEARTBEAT.md` §Thresholds + intake repo | `PROME/STATUS.md` (Core State + HY lane row) · `SYSTEM.md` (Architecture Note 1) · `ACTIVE_DECISIONS.md` (RESEARCH-INTAKE + Post-FOMC rows) · bank-put proposal §F |
| Position truth (off-repo Will/broker; FORGE = stale mirror) | root `CLAUDE.md` + `FORGE/STATUS.md` banner | `SYSTEM.md` (Freshness Discipline + Note 3) · `ACTIVE_DECISIONS.md` (Current Mode) · `action-cards/TEMPLATE.md` (header) · bank-put proposal (inputs line) |
| Roster / classification | `PROME/ROSTER.md` | root `CLAUDE.md` (active list) · `AGENTS.md` (table + run-model note) · `README.md` · `AGENTS/_INDEX.md` + `_NETWORK.md` · `skills/walter/references/agent-directory.md` |
| Forward catalyst dates | **`PROME/DOCKET.tsv`** | `SCRATCH.md` (operator card) · `HEARTBEAT.md` (Near Gates) · `STATUS.md` (Next Best Action docket line) · fire-time artifacts (checked by `scripts/firetime_check.py`) |
| Trigger bands / levels | `FORGE/tools/market-data/config.py` + `AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md` + intake-lane alerts | `HEARTBEAT.md` §Thresholds · `skills/walter/references/agent-directory.md` (trigger-lines table) · fire-time artifacts |

---

## Prome Runtime

Prome runs as a Claude Code session on Will’s current box — **one identity, one machine *at a time* (serial multi-machine, desktop ⇄ laptop — `PROME/MACHINE_LOCAL.md`), shared files as source of truth.** (Historically Prome also ran an always-on OpenClaw/VPS surface; that platform was cut 2026-06-26 — see `AGENTS/WALTER/design/OPENCLAW_CUTOVER_PLAN.md`.)

Prome owns both halves of the work:

- **Will-facing:** conversational synthesis and check-ins (via Telegram), trade/portfolio decision prompts and approval rails, agent routing, proposal ranking, the “what changed / why it matters / what to do” framing.
- **Repo-native:** operating docs and system maps, tools/dashboards/scripts and verification gates, agent-folder audits and inbox/task packets, action-card scaffolds, handoffs.

Constant constraints: does **not** execute trades or external sends without Will approval, and does **not** fork memory into a private truth layer.

### Shared state / handoff

Primary shared files:

- `PROME/BOOT.md` — boot sequence and ownership map.
- `PROME/SYSTEM.md` — architecture map and trust layer.
- `PROME/HANDOFF.md` / `PROME/SCRATCH.md` — session continuity and current-session handoff.
- `PROME/STATUS.md`, `PROME/ACTIVE_DECISIONS.md`, `HEARTBEAT.md`, auto-memory `MEMORY.md` (index; the old root `MEMORY.md` is now `KERNELS.md`) — current-state and long-term context per their own rules.

Split-brain prevention: put facts in owner files and reference them elsewhere; update `PROME/HANDOFF.md` at the end of meaningful sessions when future-Prome continuity changes; update `PROME/SCRATCH.md` for the immediate next-session entry point.

Boot from `PROME/CLAUDE.md` (the bootstrap). Status: **operational** — persistent operating loop live since mid-May; original bootstrap PLAN/TASKS + the old `CLAUDE_CODE_PROME.md` manual archived to `PROME/archive/`.

---

## Decision-Support Layer (original design)

The original lightweight decision-artifact pattern. Live trade construction/risk now runs through **TERRY** (`AGENTS/TERRY/`, incl. the fire-card template + `grade_print.py`) and **FORGE**; the cards below (FSK_MAY11 etc.) are historical examples of the pattern.

```text
Event Pre-Build
→ Position Snapshot
→ Action Card
→ Live Event Read
→ Decision Log
→ HEARTBEAT update
```

| File / directory | Owner | Role |
|---|---|---|
| `PROME/archive/DECISION_FLOW.md` | Prome | Architecture/spec for the decision workflow *(archived 2026-06-30)*. |
| `PROME/action-cards/` | Prome | Event-specific branch-to-action cards. Temporary/current decision artifacts. |
| `PROME/archive/action-cards/FSK_MAY11_ACTION_CARD.md` | Prome | First concrete action card; maps FSK branches to allowed/forbidden actions. |
| `PROME/archive/TRADE_DECISIONS.md` | Prome | Historical log of Will’s trade/portfolio decisions *(archived 2026-06-30; live truth = FORGE/TERRY + broker)*. |
| `HEARTBEAT.md` | Prome/root | Current-state pointer layer. Should reference action cards, not contain full action logic. |

Design principle:

- Domain files classify events.
- Position files describe exposure.
- Action cards map event branches to allowed actions.
- Decision logs record what Will actually decided.
- HEARTBEAT orients future Prome.

---

## Domain / Research Layer

| Area | Owner | Role |
|---|---|---|
| `AGENTS/<NAME>/STATUS.md` | Domain agent | Agent current state, domain facts, pending work. |
| `AGENTS/<NAME>/domain/` | Domain agent | Durable domain research and frameworks. |
| `AGENTS/<NAME>/domain/sources/*_PREBUILD_*.md` | Domain agent / Prome when preparing catalyst | Event pre-builds with thresholds and read order. |
| `AGENTS/<NAME>/inbox/` | Domain signal routing | Incoming signals, should be triaged/processed. |
| `FORGE/research/` | Prome / domain-dependent | Thesis research outside a single agent. |
| `FORGE/timing/` | Prome / timing thesis | Timing frameworks, changelog-first thesis files. |

Historical example of the ownership split (FSK May-11 event; card archived):

- `AGENTS/BROCK/domain/sources/FSK_PREBUILD_MAY11.md` owned the event framework.
- `PROME/archive/action-cards/FSK_MAY11_ACTION_CARD.md` owned the portfolio/action mapping.

---

## Operational / Orchestration Layer

| File / directory | Role | Trust note |
|---|---|---|
| `PROME/AUTONOMY.md` | What Prome can do freely vs must propose/ask. | Use before ambiguous autonomy calls. |
| `PROME/COMPLETION_SPEC.md` | Required sub-agent completion format. | Use for spawns. |
| `PROME/ORCHESTRAL_LAYER_DESIGN.md` | Fleet scan, ranking rubric, orchestration design. | Use when triaging many tasks. |
| `PROME/ACTIVE_DECISIONS.md` | Open non-terminal decisions / Will blockers. | Check before proposing new decisions. |
| `PROME/FLEET_SCAN.md` | On-demand stale-state scan and ranked candidate moves. | Rebuild when Will asks for fleet/agent audit. |
| `PROME/archive/TOSCANINI_2026-03/` | Retired Toscanini queue/protocol archive. | Historical only; do not treat as live ops. |

---

## Tools / Data Layer

| Tool / path | Role | Rule |
|---|---|---|
| **`RESEARCH-INTAKE` repo** (clone `/home/willi/Research-Intake`) | **Always-on data-collection lane** — 6 feeds via GitHub Actions (EIA · EDGAR-8K · Treasury · CFTC-VIX · FRED · news-sweep), weekday-daily, agents read-only. | The autonomous collection surface: `liveness.json` + `SUMMARY.md` at root, `data/<UTC-date>/*.json`. Consumer-wiring is the open follow-up. [[project_research_intake_collection_lane]] |
| `FORGE/tools/market-data/dashboard.py` | Live stress dashboard. | Run before citing current market levels. |
| `FORGE/tools/market-data/fetch.py` | Live prices / FRED series. | Use for individual live data pulls. |
| `FORGE/tools/news-sweep/sweep.py` | Thesis-tagged news sweep + routing (entity index / WATCH_FOR lists). | **Local cron is dead** (cut VPS); the fetch+classify logic is **revived in RESEARCH-INTAKE** (routing dropped). Use this copy mainly to edit the entity index. |
| `FORGE/tools/filing-watch/` | EDGAR filing monitoring. | Useful for Qs/10-Q catalysts and Call Reports. |

Known current caveat:

- `FORGE/STATUS.md` (+`PORTFOLIO.md`) is the broker-export-refreshed structured position mirror — carries a STALE banner (last export 5/21); position truth is off-repo (Will/broker direct). Never cite its marks as current.

---

## Operating Defaults

Default to compact tool output so long sessions don't bloat the transcript. *(Relocated from `BOOT.md` 2026-07-01 — reference default, not a boot step.)*

- Inspect size/structure first: `wc`, `grep`, `find`, `git diff --stat`, `git diff --name-only`.
- Read targeted excerpts before whole files: prefer bounded `read`, `sed -n '1,120p'`, or focused greps.
- For large diffs, show stat/name-only first; print hunks only for files being actively reviewed.
- For generated reports/artifacts, write to file and summarize rather than pasting full content into chat.
- For agent freshness checks, use mtimes + headers/top sections first; deep-read only when decision-relevant.
- Escalate freely to full reads/diffs when correctness, safety, or editing requires it. This is a default, not a blind constraint.

---

## Freshness Discipline

Trust each file's own `Updated:` stamp over any table here (behavior-language beats date-pinning — stamps decay). At boot, refresh in order: `HEARTBEAT.md` (regime) → `PROME/SCRATCH.md` + `HANDOFF.md` (session continuity) → `STATUS.md` / `ACTIVE_DECISIONS.md` (state).

- **Live market levels:** always re-run `FORGE/tools/market-data/dashboard.py` / `fetch.py` before citing — never quote levels from state files.
- **Position / execution truth:** Will/broker direct (**off-repo**), not these docs — FORGE is only the stale structured mirror. The legacy `POSITIONS.md`/`TRADE_DECISIONS.md` decision-support docs were retired 2026-06-30 (POSITIONS deleted — held a broker balance; TRADE_DECISIONS → `PROME/archive/`), superseded by FORGE + **TERRY** (trade construction / risk). `FORGE/STATUS.md` refresh before use.
- **On-demand:** `PROME/FLEET_SCAN.md` — rebuild for the current question before trusting.

---

## Current Architecture Notes

1. **Detection/action layer is now automated (2026-06-26; re-based 2026-07-01).** Trigger detection runs unattended — the **RESEARCH-INTAKE lane is the machine-independent PRIMARY** for the HY OAS watch (GH Actions, weekday-daily, bands + named ≥280 X1-breach / <260 re-kill alerts); LIQUID's desktop `liquid-hy-watch` systemd timer is machine-local **redundancy** (dark when that box is off). The trigger→card path is tooled: `AGENTS/TERRY/scripts/{chain_fetch,grade_print}.py` + `TRADE_CARD_TEMPLATE_FIRE.md`. Standing rule: deploy fresh capital only on a fired trigger ([[feedback_deploy_on_trigger_not_calendar]]).

2. **File-based messaging is in use but being replaced.** Don't patch inbox/outbox/HERMES hygiene gaps — flag and let them ride ([[project_messaging_overhaul]]).

3. **Execution truth lives outside these docs.** Position truth is **off-repo** (Will/broker direct); `FORGE/STATUS.md`+`PORTFOLIO.md` is only the broker-export structured mirror (stale since 5/21) — never cite its marks as current. Retired Toscanini refs → `PROME/archive/TOSCANINI_2026-03/` (historical only).

4. **Always-on collection now lives in the RESEARCH-INTAKE repo (2026-06-29).** Built as **GitHub Actions in a dedicated private repo, NOT a VPS** — collectors write only there, agents read read-only (no working-branch divergence by construction). 6 feeds weekday-daily; replaces the dead `/home/moltbot` VPS crons (news-sweep / dashboard). Open follow-up: consumer-wiring (an agent reading the lane + its `liveness` staleness check). [[project_research_intake_collection_lane]].

---

## Maintenance Notes

- This is an **architecture map**, not a task list — the live work queue lives in `PROME/ACTIVE_DECISIONS.md` + `PROME/SCRATCH.md`.
- Keep `PROME/BOOT.md` aligned with the current decision-support layer.
- Run closeout per `PROME/CLOSEOUT.md` (boot↔closeout write-back symmetry).

---

## Safety / Autonomy Reminders

- Internal reads/organization/editing are generally okay when Will asks.
- External sends/posts/public actions require asking first.
- Trade proposals require Will’s explicit approval. Never execute.
- Use `trash` over `rm` for deletion.
- All agents are Claude Code sessions (no persistent/managed agents — OpenClaw vestige removed 7/1). PROME may spawn domain agents via teams-mode when orchestrating; apply the mode-split rule (`PROME/ORCHESTRATION_PLAYBOOK.md`) before spawning >1, and release/alias warm-parked agents at closeout.
- Before citing live prices, run the market-data dashboard or fetch tool.
