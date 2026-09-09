# PROME Boot

**Owner:** PROME · **Updated:** 2026-09-09 (explicit runtime context, bounded reads and guarded gate; approval and review: `plans/2026-09-09_boot-hardening.md`). Prior scope and provenance: `git log -p -- PROME/BOOT.md`.

**Goal:** become operational fast without loading manuals.

**Auto-loaded context (Claude Code):** only the `CLAUDE.md` files (root + `PROME/`, plus any `~/.claude/CLAUDE.md`) and the auto-memory `MEMORY.md` are genuinely auto-injected each session — don't re-read *those* unless debugging drift. **`AGENTS.md` and `USER.md` are NOT auto-loaded.** **`USER.md` = every-boot explicit `Read`** (Will's operator model; `PROME/CLAUDE.md` step 1 owns this). `AGENTS.md` stays on-demand (roster/routing tasks only). `SOUL.md` / `IDENTITY.md` do not exist.

On a runtime without confirmed context injection, explicitly read root `CLAUDE.md`, `PROME/CLAUDE.md` and `USER.md`. Do not assume Claude hooks ran.

> ⚠️ **`HEARTBEAT.md` is NOT auto-injected** It is a **PROME-facing regime memo**: PROME writes it and must explicitly `Read` it at boot (the market-data freshness gate below) — don't assume it's in context; domain agents do not read it. Full trust-layer detail: `PROME/SYSTEM.md` → Boot Trust Stack.

---

## Non-Negotiables

- **Repo state first:** run `git status --short` + ahead/behind before pull/rebase.
- **No broad git operations:** never `git add .`, `git add -A`, `git reset HEAD`, force-push, or stash/reset unknown work.
- **Pull only if safe:** safe = clean working tree, no staged files, no known concurrent-agent risk. If dirty/untracked, read local continuity first and ask/triage; do not force sync just to boot.
- **Prices need live data:** run `FORGE/tools/market-data/dashboard.py` or `fetch.py` before citing prices/levels.
- **Weekend / repeated-respawn rule:** on weekends or market holidays, `HEARTBEAT.md` may be used as regime orientation, but do **not** describe its levels as fresh. Say “last HEARTBEAT/Fri close” or refresh with dashboard/FRED before making a market claim. Repeated same-day Prome respawns should not rewrite `HEARTBEAT.md` or churn other state files for hygiene alone — only when a real market/system event or user decision changed.
- **FRED citation convention:** cite observation dates, e.g. `HY OAS 280bps [FRED 5/20 close]`.
- **No agent edits** unless Will explicitly approves.
- **No trade execution.** Trade rails are verification-required at every fire-time — root rule #4 (live prices, never STATUS marks) **plus** root position-truth canon (live broker book; FORGE is the stale mirror).
- **External/public sends require approval.**
- **Push is auto at closeout** via ff-gated `scripts/safe-push.sh` — *not* per-push Will approval. Committing your own `PROME/` files is fine; **shared/root** docs still need Will scope/approval. Non-ff abort = **routine, never force**; the full recovery + escalation protocol lives in root `CLAUDE.md` Git Protocol.
- **Shared repo coordination:** when another agent has local/branch work, use `PROME/GIT_COORDINATION.md` before committing, merging, or pushing.
- **Multi-agent orchestration:** before spawning >1 agent, apply the **mode-split rule** (`PROME/ORCHESTRATION_PLAYBOOK.md`) — fan-out/Workflow for parallel-identical work, live teams-mode only for the decision spine. Carry the deliver-before-idle contract into every spawn prompt; go quiet to Will while agents work.

---

## Doc Ownership

Canonical doc-ownership / trust map: `PROME/SYSTEM.md` → **Boot Trust Stack** (put facts in the owner file; point, don't copy). Everything not listed there is on-demand.

---

## Boot Sequence

**Bounded reads:** from repo root, use `python3 PROME/tools/boot_read.py <path>` for one document page per tool output. Follow each `next_offset` using `--offset <next_offset> --sha256 <sha256>` until `eof: true`; a changed-source refusal means restart that document. Truncated output is an incomplete read, never evidence of EOF. The manual's selected sections still determine read scope.

0. **Check repo state (and take the clock):**
   Every prompt in a PROME session carries a `NOW: <day> <date> <time> ET` line injected by the UserPromptSubmit hook (wiring `PROME/.claude/settings.json`) — **that line is the clock; stamp from it, never from narrative.** No `NOW:` line ⇒ run `date` before writing any timestamp.
   A **SessionStart banner** (`scripts/session_banner.sh`) should already have printed fetch/ahead-behind/dirty-tree/env_doctor at launch. Live wiring = `PROME/.claude/settings.json` (root-level hooks never fire for subdir launches — `finding_subdir_launch_hooks_dont_fire`). **No banner = flag it to Will**, then run the checks below manually. (Banner present ⇒ the checks below are confirmation, not discovery.)
   ```bash
   git status --short
   git diff --cached --name-only
   git fetch origin   # FETCH FIRST — ahead/behind reads the LOCAL tracking ref; a fetch-less 0/0 hides a machine-switch gap ([[finding_fetch_before_trusting_boot_sync]])
   git rev-list --left-right --count HEAD...origin/master
   ```
   If clean/safe, `git pull --rebase`. If dirty/untracked/staged, do not pull; read local continuity first and ask/triage.

1. **Read `PROME/HANDOFF.md`** — top live entries only; older history is archived.
2. **Read `PROME/SCRATCH.md`** — immediate handoff / what is hot **+ the operator card** (today's date, catalysts, near-gates).
3. **Read `PROME/ACTIVE_DECISIONS.md`** — unresolved/approved-but-not-executed decisions before new work — **and `PROME/GATES.tsv` (fire-ledger):** any `FIRED-UNEXECUTED` row = 🔴 blocking (clear or escalate to Will before new work); LIVE-row staleness keys on the **`consumed_by`** field (flag rows whose consumer date passed or whose cell is empty). Register action-gates the session they're approved; owners' KBs stay canonical for full logic.
4. **Read `PROME/STATUS.md`** — agent/system health and work queue.
   - **4b. Read § Boot-class fleet memories** (the last section of this file) — its FIRST group is the every-boot read; the other three groups are keyed to their own moments (mechanized step · desk revival · desk-hardening) and are there so the embed contract holds, not to act on now. The boot-class lessons have no other carrier; a runner that skips them re-learns a solved failure.
5. **Market-data freshness gate:**
   - Explicit-`Read` `HEARTBEAT.md` (PROME-facing regime memo — not auto-injected).
   - If today is a weekend/holiday or markets are closed, use it as **orientation only** and preserve its observation dates.
   - Before citing any level as current, run the market dashboard / fetch tool.
   - **Env doctor:** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/env_doctor.py --quiet` — machine-local key/infra presence (<1s, no network): FRED/EIA keys in the single-home `.env`, bashrc two-home drift, expected desktop extras. **rc=1 (✗) ⇒ fix or flag to Will before citing FRED-dependent levels.** Inventory canon = `PROME/MACHINE_LOCAL.md`.
   - **Position-agreement gate (whenever live capital exists):** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/position_agreement_check.py --all --quiet` — the POSITIVE check `ledger_staleness.py` cannot be (age ≠ agreement — a fresh file can lie, `[[finding_freshness_check_cannot_catch_a_fresh_lie]]`). rc=1 = a trade surface disagrees with its STATUS's live cards ⇒ flag to the owner (STATUS is canonical; the trade surface gets fixed). v1 scope = TRY-* card class only.
   - **⚡ ONE-SHOT GATE:** `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_session.py --run-dir /tmp/prome-boot-<session-id>` runs the mechanical stack in `prome_gate.py boot`. Choose the run directory ONCE per boot and reuse it on retry. The receipt prevents another BOARD-advancing attempt through that directory; it is not a global lock. Completed retries return the saved verdict and observation time; incomplete attempts return UNKNOWN without rerunning. Inspect saved logs and independently runnable checks; never invent another directory or call the raw boot gate to bypass the guard. Read `gate.txt` with the bounded reader, then the full check logs it names; previews are not complete evidence. The gate's verdict block owns the check list and severity; rc=1 means blocking failure, rc=2 unknown execution. **New fleet-wide checks get added to the SCRIPT, not to this prose.** Optional `--sessions-json <path>` takes a fresh same-host `session_bridge.py` snapshot; otherwise presence is collected in the caller's visible namespace. A snapshot is scoped evidence, never proof a desk is absent or a substitute for the native same-minute spawn preflight. Acquisition details: `PROME/tools/SESSION_PILOT.md`.
   - **5b. R1 corrections check (fleet-wide — FORUM-6 ruling ①, Will-approved 2026-08-17):** `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" PROME` — rc 0/1/2 per `AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md` §9; **rc=1 = a NAMED correction is unreceipted:** read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` and commit `PROME/registry/corrections_receipts.tsv`. *(Also runs inside `prome_gate.py boot`.)*
   - **Fire-time gate:** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/firetime_check.py --window 7 --quiet` — checks fire-path artifacts cited by `PROME/DOCKET.tsv` rows ≤7d out (dead pointers / date drift / canon-ordering). **A DATE flag ⇒ full logic re-read of the artifact** (a date fix can break gate sequencing), never a find-replace. **rc=1 always means act** — known-benign flags are suppressed by the **expiry-dated allowlist** (`scripts/firetime_allowlist.tsv`): expired rows re-flag themselves, so a clean quiet run = genuinely clean.
6. **Decide conditional reads:**
   - Fleet-state reads (`PROME/ROSTER.md` classification + DAEDALUS `FLEET_MAP.tsv` maturity) only for fleet work, stale-state risk, or Will-requested audit. *(`FLEET_SCAN.md` = superseded snapshot, historical only.)*
   - **BOARD diff-scan (every boot, ~1s — ALREADY RUN inside `prome_gate.py boot`; run standalone ONLY if the gate was skipped — the cursor advances on every invocation):** `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/board_scan.py --advance`. This is PROME's **pull**, and it is what makes the `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` §3.5 pull-complete exemption sound — WALTER stops writing info-cc handoffs *only because* this scan is complete (whole-INDEX, every signal since the cursor, never a tier or a sample). **If this scan stops running, the exemption is void and must be handed back** — a BOARD-diff cannot surface what nobody scans. **rc=1 = PROME is on an ACTION line ⇒ disposition before proceeding** (genuinely exceptional, never routine). Cursor: `PROME/state/board_cursor.txt`.
   - `AGENTS/*/outbox/*to-PROME*` only for operational routing/signal work — **and `PROME/inbox/` is the SOLE PROME delivery surface** (`MESSAGING/DIRECT_MESSAGING_V1_SPEC.md`). **If `AGENTS/PROME/` ever reappears, that is a sender-routing regression, not a delivery surface** — read anything found there, migrate it to `PROME/inbox/`, then flag the sender; servicing it in place is what feeds the cycle.
   - Prome implementation/identity docs (`PROME/CLAUDE.md`, `PROME/SYSTEM.md`) only for implementation work.
   - `PROME/CLOSEOUT.md` before `/clear`, `/new`, or durable handoff.
7. **Declare boot state briefly:** synced/dirty, current regime source, market-data freshness posture, top pending decision/work lane, and any blocker.
8. **Flag top issues:** catalysts within 24h, stale agents, pending decisions, blockers, and a stale spine-audit stamp (`PROME/STATUS.md` header "Last spine audit" >7d — **or missing = stale** → `/spineaudit` this session or flag it) — **and put OWED prior-session work to Will as a choice, not a mention** (one line: *"owed from <date>: A · B · C — first, or after the <directed lane>?"* with a rec; a dated owed item reaching its third boot unrun leaves SCRATCH for a DOCKET `COVERED:` annotation or a WQ row).
9. **Present top proposals** only when useful; max 5, ranked by urgency/position relevance.

---

## Conditional Modules

| Need | Read / Use |
|---|---|
| Market prices / dashboard | Read `FORGE/tools/market-data/README.md`. Run `dashboard.py` / `fetch.py` before citing levels. |
| Forward catalyst dates / fire-time artifacts | **`PROME/DOCKET.tsv` = canonical** (SCRATCH card + HEARTBEAT gates are views); `scripts/firetime_check.py` = the freshness checker (boot gate above). |
| Spine reconciliation (weekly) | `/spineaudit` → `PROME/tools/spine_audit.workflow.js` — 8 paired readers over the boot-read/protocol spine set (incl. the `/boot` + `/closeout` runners vs their manuals) + 1 anchor reader sampling DOCKET's >7d PENDING tail at source (the spine is checked AGAINST DOCKET; `firetime_check` covers only ≤7d). Run when the STATUS "Last spine audit" stamp is >7d. **Fix rounds: delete-and-point over annotate-and-accrete** — dated correction tags are themselves stale-able claims. Canon-change sweeps use the Mirror Map (`PROME/SYSTEM.md` → Canonical → Mirrors). |
| News routing / data feeds | Always-on collection runs in the **RESEARCH-INTAKE** repo (GitHub Actions; `[[project_research_intake_collection_lane]]`). **WALTER owns lane consumption; PROME never boot-reads the lane.** `FORGE/tools/news-sweep/sweep.py` = entity-index edits only (no cron). |
| Roster / classification / fleet scan | `PROME/ROSTER.md` (verified Active/Tier-2/Dormant/Retired + responsibility class; refresh by re-running the commit-activity map — `[[finding_verify_roster_by_commit_activity]]`) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (maturity/state, DAEDALUS-owned) + `PROME/ORCHESTRAL_LAYER_DESIGN.md` (layer design). ⛔ `PROME/FLEET_SCAN.md` = superseded snapshot, never boot-read. |
| Sub-agent spawn | `AGENTS.md`, `PROME/COMPLETION_SPEC.md`; include completion instructions. |
| **FORGE reconcile (new broker export) / FORGE mechanical follow-ups** | **Spawn agent type `anvil`** (skeleton = `.claude/agents/anvil.md`, Will-directed 2026-07-30) — the standing reconcile-clerk contract; supply the export transcription + post-snapshot events in the spawn prompt. Flow: ANVIL edits → PROME verifies at artifact → Will OK → ANVIL commits. *(FORGE owner = PROME — root `CLAUDE.md` position-truth paragraph.)* |
| Prome implementation / identity | `PROME/CLAUDE.md` + `PROME/SYSTEM.md` |
| Autonomy tier / recent grant-revoke | `PROME/AUTONOMY.md` — full change-log; behavior-changing grants also propagate to the auto-loaded `PROME/CLAUDE.md` Ask-First section (that's what's read every boot) |
| Position reconciliation | `PROME/ACTIVE_DECISIONS.md`, relevant action cards, `FORGE/STATUS.md` + broker/Will truth (position truth is off-repo) |
| Git commit patterns (cookbook) | `PROME/GIT_COORDINATION.md` → Commit cookbook — modified/new/mixed pathspec recipes + push/coordination rules |
| "Works on the other machine, fails here" / missing cred, timer, tool | `PROME/MACHINE_LOCAL.md` — machine-local inventory + switching checklist (Will runs serial multi-machine, desktop ⇄ laptop) |
| Tool-output / freshness-read defaults | `PROME/SYSTEM.md` → Operating Defaults (compact tool output; mtime/header-first freshness reads) |

---

## Closeout Pointer

Before `/clear`, `/new`, long pauses, or handoff: read `PROME/CLOSEOUT.md` and run the appropriate tier.

Closeout is the write-back tail of boot: update only the owner docs whose state actually changed.

---

## Boot-class fleet memories (fleet-memory embeds — migrated 2026-07-31, Phase-2 restructure; per-item review 2026-08-29 EVE)
*Every slug embedded 7/31 is still named here (the embed contract: `INDEX_COLD.md` rows point at this section); hooks trimmed 8/29 (embeds, not index rows — the ≤80-char canon does not apply) and the 14 regrouped by WHEN they trigger: only the first group is an every-boot read; the other three are keyed to their own moments. Memory FILES unchanged — read `memory/auto/<slug>.md` for the full lesson.*

**PROME's own boot (unpredictable-trigger — read every boot):**
- finding_boot_sweep_macro_regime_context — a month-old Fed-Chair/BOJ-Gov change can sit un-modeled if boot covers only feeds + calendars; check principals
- finding_inbound_lane_is_the_falsification_channel — a lane that can carry a falsifier for a thesis you own is boot-MANDATORY, never spawn-optional (HAWK 9d unread)
- finding_gitignored_private_drop_boot_surfaced — gitignored drops (broker exports) are invisible to `git status`; a boot-card line is the only discovery path
- feedback_front_load_planning — multi-step deterministic work: surface every decision in ONE planning pass, let Will batch-approve, then execute mechanically
- finding_display_filter_gating_safety_net — a forward-section display filter silently gates the past-due safety net too (OTTO 7/25: 3-of-4 fired items hidden)

**Already mechanized on PROME's boot path (pointer only — the step is the carrier):**
- finding_fetch_before_trusting_boot_sync → step 0 (`git fetch` before ahead/behind) · feedback_scan_agent_outboxes_at_boot → step 6 (the every-boot carrier is the BOARD diff-scan inside the gate; the raw `outbox/*to-PROME*` read stays conditional — WALTER routes, the scan is the pull) · finding_freshness_audit_vs_caught_up → `prome_gate.py boot` (step 5) check "agent freshness (ground-truth vs narrative)", ADVISORY class — never stops boot (mtime-fresh ≠ caught-up on inbox backlog)

**Reviving a stale desk (read at spawn time, not every boot — the procedure is `ORCHESTRAL_LAYER_DESIGN.md` § Revival-proxy v3 brief spec):**
- finding_revival_proxy_pattern — foreground subagent briefed as revival proxy → decision-grade catch-up + inbox-deposited packet for the desk's next boot
- finding_revival_boot_doc_sweep — 30+ days stale: sweep CLAUDE/MEMORY/CALENDAR/STRATEGY/USER alongside STATUS; staleness compounds across all of them

**Domain-desk boot-protocol patterns (not PROME's boot — read when hardening a desk's boot/closeout; DAEDALUS blueprint class):**
- finding_boot_protocol_live_event_override — SPAWN framing pulls a desk to CLOSEOUT mid-event; neutral "write-back" framing + explicit live-event override (VIOLET 6/5)
- finding_boot_predictions_scan — a cheap boot-time PREDICTIONS due/stale scan; caught a 24d-stale MISS first run
- finding_boot_closeout_hardening_recipe — phased: mirror → strip live-state → audit doc-ownership → deferred punch-list
- finding_boot_py_cadence_skip_pattern — low-frequency-data desks: run-at-boot-defensively + mtime cadence-skip on fetchers, not a read-only/--pull split
