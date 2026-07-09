# PROME Boot

**Goal:** become operational fast without loading manuals.

**Auto-loaded context (Claude Code):** only the `CLAUDE.md` files (root + `PROME/`, plus any `~/.claude/CLAUDE.md`) and the auto-memory `MEMORY.md` are genuinely auto-injected each session — don't re-read *those* unless debugging drift. **`AGENTS.md` and `USER.md` are NOT auto-loaded** (OpenClaw vestige — confirm by their absence from fresh boot context); `Read` them explicitly when a task needs them. (`SOUL.md` + `IDENTITY.md` no longer exist — deleted root-level in the 2026-06-30 public-prep cleanup.)

> ⚠️ **`HEARTBEAT.md` is NOT auto-injected** (OpenClaw always-on vestige). It is a **PROME-facing regime memo**: PROME writes it and must explicitly `Read` it at boot (the market-data freshness gate below) — don't assume it's in context; domain agents do not read it. Full trust-layer detail: `PROME/SYSTEM.md` → Boot Trust Stack.

---

## Non-Negotiables

- **Repo state first:** run `git status --short` + ahead/behind before pull/rebase.
- **No broad git operations:** never `git add .`, `git add -A`, `git reset HEAD`, force-push, or stash/reset unknown work.
- **Pull only if safe:** safe = clean working tree, no staged files, no known concurrent-agent risk. If dirty/untracked, read local continuity first and ask/triage; do not force sync just to boot.
- **Prices need live data:** run `FORGE/tools/market-data/dashboard.py` or `fetch.py` before citing prices/levels.
- **Weekend / repeated-respawn rule:** on weekends or market holidays, `HEARTBEAT.md` may be used as regime orientation, but do **not** describe its levels as fresh. Say “last HEARTBEAT/Fri close” or refresh with dashboard/FRED before making a market claim. Repeated same-day Prome respawns should not rewrite `HEARTBEAT.md` or churn other state files for hygiene alone — only when a real market/system event or user decision changed.
- **FRED citation convention:** cite observation dates, e.g. `HY OAS 280bps [FRED 5/20 close]`.
- **No agent edits** unless Will explicitly approves.
- **No trade execution.** Old trade rails remain verification-required until broker/Will reconciliation.
- **External/public sends require approval.**
- **Push is auto at closeout** via ff-gated `scripts/safe-push.sh` (serial multi-machine canon, per root `CLAUDE.md` Git Protocol) — *not* per-push Will approval. Committing your own `PROME/` files is fine; **shared/root** docs still need Will scope/approval. A **non-ff abort = the other machine pushed** (serial multi-machine, routine) → **do NOT force; `git pull --rebase` + re-push**; escalate to Will only on out-of-dir conflicts or mid-session recurrence.
- **Shared repo coordination:** when YEYOU or another agent has local/branch work, use `PROME/GIT_COORDINATION.md` before committing, merging, or pushing.
- **Multi-agent orchestration:** before spawning >1 agent, apply the **mode-split rule** (`PROME/ORCHESTRATION_PLAYBOOK.md`) — fan-out/Workflow for parallel-identical work, live teams-mode only for the decision spine. Carry the deliver-before-idle contract into every spawn prompt; go quiet to Will while agents work.

---

## Doc Ownership

Canonical doc-ownership / trust map: `PROME/SYSTEM.md` → **Boot Trust Stack** (put facts in the owner file; point, don't copy). Everything not listed there is on-demand.

---

## Boot Sequence

0. **Check repo state:**
   ```bash
   git status --short
   git diff --cached --name-only
   git rev-list --left-right --count HEAD...origin/master
   ```
   If clean/safe, `git pull --rebase`. If dirty/untracked/staged, do not pull; read local continuity first and ask/triage.

1. **Read `PROME/HANDOFF.md`** — top live entries only; older history is archived.
2. **Read `PROME/SCRATCH.md`** — immediate handoff / what is hot **+ the operator card** (today's date, catalysts, near-gates; absorbed the old `TODAY.md`).
3. **Read `PROME/ACTIVE_DECISIONS.md`** — unresolved/approved-but-not-executed decisions before new work — **and `PROME/GATES.tsv` (fire-ledger):** any `FIRED-UNEXECUTED` row = 🔴 blocking (clear or escalate to Will before new work); any `LIVE` row with `last_checked` >5d → refresh or flag. *(Born 7/9 from the KB-VIO-110 dropped-execution incident: gates fired 7/2 into a frozen VIOLET session and the consequence was orphaned for 7 days — this ledger is the coordination-layer index so an owner freezing can never hide a fired gate again. Register action-gates the session they're approved; owners' KBs stay canonical for full logic.)*
4. **Read `PROME/STATUS.md`** — agent/system health and work queue.
5. **Market-data freshness gate:**
   - Explicit-`Read` `HEARTBEAT.md` (PROME-facing regime memo — not auto-injected).
   - If today is a weekend/holiday or markets are closed, use it as **orientation only** and preserve its observation dates.
   - Before citing any level as current, run the market dashboard / fetch tool.
   - **Env doctor:** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/env_doctor.py --quiet` — machine-local key/infra presence (<1s, no network): FRED/EIA keys in the single-home `.env`, bashrc two-home drift, expected desktop extras. **rc=1 (✗) ⇒ fix or flag to Will before citing FRED-dependent levels.** Inventory canon = `PROME/MACHINE_LOCAL.md`.
   - **Fire-time gate:** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/firetime_check.py --window 7 --quiet` — checks fire-path artifacts cited by `PROME/DOCKET.tsv` rows ≤7d out (dead pointers / date drift / canon-ordering). **A DATE flag ⇒ full logic re-read of the artifact** (a date fix can break gate sequencing — 7/1 WAL case), never a find-replace.
6. **Decide conditional reads:**
   - `PROME/FLEET_SCAN.md` only for fleet/market-state work, stale-state risk, or Will-requested audit.
   - `AGENTS/*/outbox/*to-PROME*` only for operational routing/signal work — **and include `AGENTS/PROME/inbox/` in that scan**: the tree was nominally archived 6/25, but WALTER SIGs have landed there since (6/26, 6/27 — spine-audit finding 7/1), so treat it as a live legacy delivery surface until the messaging overhaul re-homes it. Pre-6/25 contents under `PROME/archive/` remain archaeology.
   - Prome implementation/identity docs (`PROME/CLAUDE.md`, `PROME/SYSTEM.md`) only for implementation work.
   - `PROME/CLOSEOUT.md` before `/clear`, `/new`, or durable handoff.
7. **Declare boot state briefly:** synced/dirty, current regime source, market-data freshness posture, top pending decision/work lane, and any blocker.
8. **Flag top issues:** catalysts within 24h, stale agents, pending decisions, blockers, and a stale spine-audit stamp (`PROME/STATUS.md` header "Last spine audit" >7d — **or missing = stale** → run `PROME/tools/spine_audit.workflow.js` this session or flag it).
9. **Present top proposals** only when useful; max 5, ranked by urgency/position relevance.

---

## Conditional Modules

| Need | Read / Use |
|---|---|
| Market prices / dashboard | Read `FORGE/tools/market-data/README.md`. Run `dashboard.py` / `fetch.py` before citing levels. |
| Forward catalyst dates / fire-time artifacts | **`PROME/DOCKET.tsv` = canonical** (SCRATCH card + HEARTBEAT gates are views); `scripts/firetime_check.py` = the freshness checker (boot gate above). |
| Spine reconciliation (weekly) | `PROME/tools/spine_audit.workflow.js` (5-reader Workflow over the boot-read/protocol set vs canon anchors) — run when the STATUS "Last spine audit" stamp is >7d. Canon-change sweeps use the Mirror Map (`PROME/SYSTEM.md` → Canonical → Mirrors). |
| News routing / data feeds | Always-on collection now runs in the **RESEARCH-INTAKE** repo (GitHub Actions; `[[project_research_intake_collection_lane]]`). The local `FORGE/tools/news-sweep/sweep.py` cron is dead (cut VPS) — its fetch/classify logic is revived in the lane. Boot-*read* the lane only once the consumer side is wired; until then, `sweep.py` is for editing the entity index only. |
| Fleet scan / ranking | `PROME/FLEET_SCAN.md`, `PROME/ORCHESTRAL_LAYER_DESIGN.md` |
| Agent roster / classification | `PROME/ROSTER.md` — verified Active/Tier-2/Dormant/Retired + commit-activity evidence (refresh by re-running the activity map; `[[finding_verify_roster_by_commit_activity]]`) |
| Sub-agent spawn | `AGENTS.md`, `PROME/COMPLETION_SPEC.md`; include completion instructions. |
| Multi-agent orchestration (>1 agent) | `PROME/ORCHESTRATION_PLAYBOOK.md` — apply the mode-split rule (fan-out/Workflow vs live) BEFORE spawning. |
| Prome implementation / identity | `PROME/CLAUDE.md` + `PROME/SYSTEM.md` (old `CLAUDE_CODE_PROME.md` manual + bootstrap PLAN/TASKS retired → `PROME/archive/`) |
| Autonomy tier / recent grant-revoke | `PROME/AUTONOMY.md` — full change-log; behavior-changing grants also propagate to the auto-loaded `PROME/CLAUDE.md` Ask-First section (that's what's read every boot) |
| Closeout | `PROME/CLOSEOUT.md` |
| Historical handoffs | `PROME/archive/HANDOFF_2026Q2.md` — only for old-session archaeology; never normal boot. |
| Detailed architecture | `PROME/SYSTEM.md`, `PROME/ORCHESTRAL_LAYER_DESIGN.md` |
| Position reconciliation | `PROME/ACTIVE_DECISIONS.md`, relevant action cards, `FORGE/STATUS.md` + broker/Will truth (position truth is off-repo) |
| Git commit patterns (cookbook) | `PROME/GIT_COORDINATION.md` → Commit cookbook — modified/new/mixed pathspec recipes + push/coordination rules |
| "Works on the other machine, fails here" / missing cred, timer, tool | `PROME/MACHINE_LOCAL.md` — machine-local inventory + switching checklist (Will runs serial multi-machine, desktop ⇄ laptop) |
| Tool-output / freshness-read defaults | `PROME/SYSTEM.md` → Operating Defaults (compact tool output; mtime/header-first freshness reads) |

---

## Closeout Pointer

Before `/clear`, `/new`, long pauses, or handoff: read `PROME/CLOSEOUT.md` and run the appropriate tier.

Closeout is the write-back tail of boot: update only the owner docs whose state actually changed.
