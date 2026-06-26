# Prome System Map
**Created:** 2026-05-08 21:28 ET · **Updated:** 2026-06-26 (surgical refresh — de-date-pinned to behavior-language; CC-Prome status → operational; stale May action-items cleared)  
**Owner:** Prome  
**Purpose:** Current architecture map for Prome’s operating system — what each file owns, what to trust, and where future Prome should look first.

---

## North Star

Prome’s system exists to turn public-data research into disciplined decisions without losing context, duplicating facts, or making ad hoc calls under pressure.

Core rule:

> Put facts in the owner file. Other files should point to it, not copy it.

---

## Boot Trust Stack

### Always injected in main sessions

| File | Trust | Role |
|---|---|---|
| `AGENTS.md` | High | Agent roster, transmission chains, spawn restrictions. |
| `SOUL.md` | High | Prome identity/tone. |
| `USER.md` | High | Will preferences and operating style. |
| `MEMORY.md` | High for curated long-term facts; check freshness | Long-term discoveries, thesis framework, system architecture notes. |
| `HEARTBEAT.md` | High for current state if recently updated | Cold-boot current-state orientation. |

### Read at boot / when resuming

| File | Cadence | Role |
|---|---|---|
| `PROME/BOOT.md` | Maintained | Boot sequence, doc ownership, protocol reminders. |
| `PROME/HANDOFF.md` | Refreshed each closeout (latest 3–5 entries) | Cross-runtime continuity. |
| `PROME/SCRATCH.md` | Full rewrite each closeout | Ephemeral session state + next-session entry point. |
| `PROME/TODAY.md` | Refreshed when date/catalysts move | Daily catalysts/checklist + regime pointer. |
| `PROME/STATUS.md` | Surgical at closeout | Operational status, work queue, agent/system health. |
| `PROME/ACTIVE_DECISIONS.md` | Surgical when a decision moves | Non-terminal decision safety index. |
| `PROME/FLEET_SCAN.md` | On-demand | Fleet/agent stale-state scan and ranked candidate moves. |

---

## Prome Runtime Split

Prome now has two work surfaces, not two identities.

Core rule:

> One Prome, two work surfaces. Shared files are the source of truth.

### Telegram / OpenClaw Prome

Owns the Will-facing interface:

- Conversational synthesis and check-ins with Will.
- Trade/portfolio decision prompts and approval rails.
- Agent routing, proposal ranking, and external-message discretion.
- Final “what changed / why it matters / what to do” framing.

### Claude Code Prome

Owns repo-native implementation when scoped:

- Prome operating docs, system maps, and handoffs.
- Tools, dashboards, scripts, and verification gates.
- Agent-folder audits and inbox/task packet preparation.
- Action-card scaffolds and decision-artifact buildout.

Claude Code Prome does **not** replace Telegram/OpenClaw Prome as Will-facing operator, does **not** execute trades or external sends, and does **not** fork memory into a private truth layer.

### Shared State / Handoff

Primary shared files:

- `PROME/BOOT.md` — boot sequence and ownership map.
- `PROME/SYSTEM.md` — architecture map and trust layer.
- `PROME/HANDOFF.md` / `PROME/SCRATCH.md` — cross-runtime Prome continuity and current session handoff.
- `PROME/TODAY.md`, `PROME/STATUS.md`, `PROME/ACTIVE_DECISIONS.md`, `HEARTBEAT.md`, `MEMORY.md` — current-state and long-term context as their own rules define.

Split-brain prevention:

- Put facts in owner files; reference them elsewhere.
- Claude Code Prome must update `PROME/HANDOFF.md` at the end of meaningful sessions when future Prome continuity changes.
- If Claude Code work changes the next Telegram/OpenClaw session, also update `PROME/SCRATCH.md` as appropriate.
- Telegram/OpenClaw Prome should read `PROME/HANDOFF.md` after clears or after known Claude Code Prome work.

## Claude Code Prome

Persistent **Claude Code Prome** is the repo-native work surface for the same Prome identity.

Boot/operating files:

| File | Role |
|---|---|
| `PROME/CLAUDE.md` | Claude Code bootstrap file. |
| `PROME/CLAUDE_CODE_PROME.md` | Longer operating manual. |
| `PROME/HANDOFF.md` | Single live handoff for OpenClaw + Claude Code Prome sessions. |

Current status: **operational** — the persistent operating loop is live (bootstrap complete since mid-May; original PLAN/TASKS archived to `PROME/archive/`). Boot from `PROME/CLAUDE.md` + `PROME/CLAUDE_CODE_PROME.md`.

Design rule:

> One Prome, two work surfaces. Telegram/OpenClaw Prome owns Will-facing synthesis and approvals; Claude Code Prome owns repo-native implementation, tooling, audits, and handoffs when scoped.

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
| `PROME/DECISION_FLOW.md` | Prome | Architecture/spec for the decision workflow. |
| `PROME/action-cards/` | Prome | Event-specific branch-to-action cards. Temporary/current decision artifacts. |
| `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` | Prome | First concrete action card; maps FSK branches to allowed/forbidden actions. |
| `PROME/TRADE_DECISIONS.md` | Prome | Permanent log of Will’s trade/portfolio decisions and outcomes. |
| `PROME/POSITIONS.md` | Prome | Current position snapshot, sizing, P/L, OCR caveats. |
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

Important current example:

- `AGENTS/BROCK/domain/sources/FSK_PREBUILD_MAY11.md` owns the FSK event framework.
- `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` owns the portfolio/action mapping.

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
| `FORGE/tools/market-data/dashboard.py` | Live stress dashboard. | Run before citing current market levels. |
| `FORGE/tools/market-data/fetch.py` | Live prices / FRED series. | Use for individual live data pulls. |
| `FORGE/tools/news-sweep/sweep.py` | Thesis-tagged news sweep + routing. | Prome maintains entity index and WATCH_FOR lists. |
| `dashboard/server.py` | Local web/API dashboard on `:8080`. | Use API endpoints if CLI is inconvenient. |
| `FORGE/tools/filing-watch/` | EDGAR filing monitoring. | Useful for Qs/10-Q catalysts and Call Reports. |

Known current caveat:

- `FORGE/STATUS.md` was flagged stale by inbox signal; do not use it as fresh source until refreshed.

---

## Freshness Discipline

Trust each file's own `Updated:` stamp over any table here (behavior-language beats date-pinning — stamps decay). At boot, refresh in order: `HEARTBEAT.md` (regime) → `PROME/SCRATCH.md` + `HANDOFF.md` (session continuity) → `STATUS.md` / `TODAY.md` / `ACTIVE_DECISIONS.md` (state).

- **Live market levels:** always re-run `FORGE/tools/market-data/dashboard.py` / `fetch.py` before citing — never quote levels from state files.
- **Position / execution truth:** Will + FORGE, not these docs. `PROME/POSITIONS.md` + `PROME/TRADE_DECISIONS.md` are superseded by FORGE + **TERRY** (trade construction / risk). `FORGE/STATUS.md` refresh before use.
- **On-demand:** `PROME/FLEET_SCAN.md` — rebuild for the current question before trusting.

---

## Current Architecture Notes

1. **Detection/action layer is now automated (2026-06-26).** Trigger detection runs unattended — LIQUID's `liquid-hy-watch` systemd timer (Mon–Fri 13:00 ET) classifies HY OAS against `config.py` bands and writes transitions to `AGENTS/LIQUID/alerts/`. The trigger→card path is tooled: `AGENTS/TERRY/scripts/{chain_fetch,grade_print}.py` + `TRADE_CARD_TEMPLATE_FIRE.md`. Standing rule: deploy fresh capital only on a fired trigger ([[feedback_deploy_on_trigger_not_calendar]]).

2. **File-based messaging is in use but being replaced.** Don't patch inbox/outbox/HERMES hygiene gaps — flag and let them ride ([[project_messaging_overhaul]]).

3. **Execution truth lives outside these docs.** `FORGE/STATUS.md` + broker = ground truth; refresh before use. Retired Toscanini refs → `PROME/archive/TOSCANINI_2026-03/` (historical only).

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
- Do not spawn persistent/managed agents: CARL, REGINALD, SAM, RED, BRENT.
- Before citing live prices, run the market-data dashboard or fetch tool.
