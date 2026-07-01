# PROME Boot

**Goal:** become operational fast without loading manuals.

**Auto-loaded context (Claude Code):** only the `CLAUDE.md` files (root + `PROME/`, plus any `~/.claude/CLAUDE.md`) and the auto-memory `MEMORY.md` are genuinely auto-injected each session — don't re-read *those* unless debugging drift. **`AGENTS.md` and `USER.md` are NOT auto-loaded** (OpenClaw vestige — confirm by their absence from fresh boot context); `Read` them explicitly when a task needs them. (`SOUL.md` + `IDENTITY.md` no longer exist — deleted root-level in the 2026-06-30 public-prep cleanup.)

> ⚠️ **`HEARTBEAT.md` is NOT auto-injected in Claude Code** (that was the OpenClaw always-on model — the line that used to claim it is removed). It is a **PROME-facing regime memo** that PROME must explicitly `Read` at boot (step 6). Don't assume it's already in context. Domain agents do not read it.

---

## Non-Negotiables

- **Repo state first:** run `git status --short` + ahead/behind before pull/rebase.
- **No broad git operations:** never `git add .`, `git add -A`, `git reset HEAD`, force-push, or stash/reset unknown work.
- **Pull only if safe:** safe = clean working tree, no staged files, no known concurrent-agent risk. If dirty/untracked, read local continuity first and ask/triage; do not force sync just to boot.
- **Prices need live data:** run `FORGE/tools/market-data/dashboard.py` or `fetch.py` before citing prices/levels.
- **Weekend / repeated-respawn rule:** on weekends or market holidays, `HEARTBEAT.md` may be used as regime orientation, but do **not** describe its levels as fresh. Say “last HEARTBEAT/Fri close” or refresh with dashboard/FRED before making a market claim. Repeated same-day Prome respawns should not rewrite TODAY/HEARTBEAT just for hygiene.
- **FRED citation convention:** cite observation dates, e.g. `HY OAS 280bps [FRED 5/20 close]`.
- **No agent edits** unless Will explicitly approves.
- **No trade execution.** Old trade rails remain verification-required until broker/Will reconciliation.
- **External/public sends require approval.**
- **Push is Will-coordinated:** committing may be okay when approved/scoped; pushing requires explicit Will approval.
- **Shared repo coordination:** when YEYOU or another agent has local/branch work, use `PROME/GIT_COORDINATION.md` before committing, merging, or pushing.
- **Multi-agent orchestration:** before spawning >1 agent, apply the **mode-split rule** (`PROME/ORCHESTRATION_PLAYBOOK.md`) — fan-out/Workflow for parallel-identical work, live teams-mode only for the decision spine. Carry the deliver-before-idle contract into every spawn prompt; go quiet to Will while agents work.

---

## Lean Tool Output

Default to compact tool output so long sessions do not bloat the transcript unnecessarily.

- Inspect size/structure first: `wc`, `grep`, `find`, `git diff --stat`, `git diff --name-only`.
- Read targeted excerpts before whole files: prefer bounded `read`, `sed -n '1,120p'`, or focused greps.
- For large diffs, show stat/name-only first; print hunks only for files being actively reviewed.
- For generated reports/artifacts, write to file and summarize rather than pasting full content into chat.
- For agent freshness checks, use mtimes + headers/top sections first; deep-read only when decision-relevant.
- Escalate freely to full reads/diffs when correctness, safety, or editing requires it. This is a default, not a blind constraint.

---

## Minimal Doc Ownership

If the same fact appears in two docs, put it in the owner doc and reference it elsewhere.

| Doc | Owns |
|---|---|
| `PROME/HANDOFF.md` | Cross-runtime continuity; latest 3–5 entries only. |
| `PROME/SCRATCH.md` | Immediate session state and next-session entry point. |
| `PROME/TODAY.md` | Operator card: today’s catalysts, tasks, notable shifts. |
| `PROME/ACTIVE_DECISIONS.md` | Non-terminal decision safety index. |
| `PROME/STATUS.md` | Agent/system health, work queue, quality notes. |
| `HEARTBEAT.md` *(PROME-facing regime memo; explicit-read, NOT injected)* | PROME's own regime / thresholds / near-gates orientation. PROME writes + reads it; domain agents do not. |
| `KERNELS.md` *(thesis-spine reference; explicit-read, NOT injected — renamed from root `MEMORY.md` 6/30)* | Compressed thesis/transmission map + durable system lessons. Consult on demand. |
| auto-memory `MEMORY.md` *(genuinely injected — off-repo `~/.claude/.../memory/`)* | Curated operating lessons / findings / feedback index. |
| `memory/YYYY-MM-DD.md` | Daily session log; activity detail, not root-memory insight. |

Everything else is on-demand.

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
2. **Read `PROME/SCRATCH.md`** — immediate handoff / what is hot.
3. **Read `PROME/TODAY.md`** — current operator card.
4. **Read `PROME/ACTIVE_DECISIONS.md`** — unresolved/approved-but-not-executed decisions before new work.
5. **Read `PROME/STATUS.md`** — agent/system health and work queue.
6. **Apply market-data freshness gate:**
   - If today is a weekend/holiday or markets are closed, use `HEARTBEAT.md` as **orientation only** and preserve its observation dates.
   - Before citing any level as current, run the market dashboard / fetch tool.
   - For repeated same-day respawns, avoid state-file churn unless a real market/system event or user decision changed.
7. **Decide conditional reads:**
   - `PROME/FLEET_SCAN.md` only for fleet/market-state work, stale-state risk, or Will-requested audit.
   - `AGENTS/*/outbox/*to-PROME*` only for operational routing/signal work. The old `AGENTS/PROME/` inbox tree is archived under `PROME/archive/` and is archaeology, not live intake.
   - Claude Code Prome docs only for Claude Code Prome implementation work.
   - `PROME/CLOSEOUT.md` before `/clear`, `/new`, or durable handoff.
8. **Declare boot state briefly:** synced/dirty, current regime source, market-data freshness posture, top pending decision/work lane, and any blocker.
9. **Flag top issues:** catalysts within 24h, stale agents, pending decisions, blockers.
10. **Present top proposals** only when useful; max 5, ranked by urgency/position relevance.

---

## Conditional Modules

| Need | Read / Use |
|---|---|
| Market prices / dashboard | Read `FORGE/tools/market-data/README.md`. Run `dashboard.py` / `fetch.py` before citing levels. |
| News routing / data feeds | Always-on collection now runs in the **RESEARCH-INTAKE** repo (GitHub Actions; `[[project_research_intake_collection_lane]]`). The local `FORGE/tools/news-sweep/sweep.py` cron is dead (cut VPS) — its fetch/classify logic is revived in the lane. Boot-*read* the lane only once the consumer side is wired; until then, `sweep.py` is for editing the entity index only. |
| Fleet scan / ranking | `PROME/FLEET_SCAN.md`, `PROME/ORCHESTRAL_LAYER_DESIGN.md` |
| Agent roster / classification | `PROME/ROSTER.md` — verified Active/Tier-2/Dormant/Retired + commit-activity evidence (refresh by re-running the activity map; `[[finding_verify_roster_by_commit_activity]]`) |
| Sub-agent spawn | `AGENTS.md`, `PROME/COMPLETION_SPEC.md`; include completion instructions. |
| Multi-agent orchestration (>1 agent) | `PROME/ORCHESTRATION_PLAYBOOK.md` — apply the mode-split rule (fan-out/Workflow vs live) BEFORE spawning. |
| Prome implementation / identity | `PROME/CLAUDE.md` + `PROME/SYSTEM.md` (old `CLAUDE_CODE_PROME.md` manual + bootstrap PLAN/TASKS retired → `PROME/archive/`) |
| Closeout | `PROME/CLOSEOUT.md` |
| Historical handoffs | `PROME/archive/HANDOFF_2026Q2.md` — only for old-session archaeology; never normal boot. |
| Detailed architecture | `PROME/SYSTEM.md`, `PROME/ORCHESTRAL_LAYER_DESIGN.md` |
| Position reconciliation | `PROME/ACTIVE_DECISIONS.md`, relevant action cards, `FORGE/STATUS.md` + broker/Will truth (position truth is off-repo) |

---

## Git Quick Reference

Modified tracked files — no staging step:

```bash
git commit -m "PROME: <subject>" -- PROME/<file> PROME/<file>
```

New files — add only explicit paths:

```bash
git add -- PROME/<newfile>
git commit -m "PROME: <subject>" -- PROME/<newfile>
```

Mixed modified + new files:

```bash
git add -- PROME/<newfile>
git commit -m "PROME: <subject>" -- PROME/<modified> PROME/<newfile>
```

**Option order matters:** put `-m` before `--`; everything after `--` is a pathspec.

Push only when Will approves/coördinates it.

---

## Closeout Pointer

Before `/clear`, `/new`, long pauses, or handoff: read `PROME/CLOSEOUT.md` and run the appropriate tier.

Closeout is the write-back tail of boot: update only the owner docs whose state actually changed.
