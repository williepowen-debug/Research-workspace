# PROME Boot

**Owner:** PROME · **Updated:** 2026-08-29 (step 8 owed-items-as-a-choice rule — the rule lives HERE; `/boot` carries only the sequence). Prior: 2026-08-28 (step-provenance trim, PROME slim-down 6/6 — incident histories and adoption dates that rode inside boot steps now live in `git log -p -- PROME/BOOT.md`; the steps carry the RULE only. Fleet-memory embeds untouched pending per-item review.)

**Goal:** become operational fast without loading manuals.

**Auto-loaded context (Claude Code):** only the `CLAUDE.md` files (root + `PROME/`, plus any `~/.claude/CLAUDE.md`) and the auto-memory `MEMORY.md` are genuinely auto-injected each session — don't re-read *those* unless debugging drift. **`AGENTS.md` and `USER.md` are NOT auto-loaded** (OpenClaw vestige — confirm by their absence from fresh boot context). **`USER.md` = every-boot explicit `Read`** (Will's operator model; `PROME/CLAUDE.md` step 1 owns this — the old "when a task needs it" line here contradicted it, reconciled 2026-07-10 doc-audit). `AGENTS.md` stays on-demand (roster/routing tasks only). (`SOUL.md` + `IDENTITY.md` no longer exist — deleted root-level in the 2026-06-30 public-prep cleanup.)

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
- **No trade execution.** Trade rails are verification-required at every fire-time — root rule #4 (live prices, never STATUS marks) **plus** root position-truth canon (live broker book; FORGE is the stale mirror).
- **External/public sends require approval.**
- **Push is auto at closeout** via ff-gated `scripts/safe-push.sh` — *not* per-push Will approval. Committing your own `PROME/` files is fine; **shared/root** docs still need Will scope/approval. Non-ff abort = **routine, never force**; the full recovery + escalation protocol lives in root `CLAUDE.md` Git Protocol.
- **Shared repo coordination:** when YEYOU or another agent has local/branch work, use `PROME/GIT_COORDINATION.md` before committing, merging, or pushing.
- **Multi-agent orchestration:** before spawning >1 agent, apply the **mode-split rule** (`PROME/ORCHESTRATION_PLAYBOOK.md`) — fan-out/Workflow for parallel-identical work, live teams-mode only for the decision spine. Carry the deliver-before-idle contract into every spawn prompt; go quiet to Will while agents work.

---

## Doc Ownership

Canonical doc-ownership / trust map: `PROME/SYSTEM.md` → **Boot Trust Stack** (put facts in the owner file; point, don't copy). Everything not listed there is on-demand.

---

## Boot Sequence

0. **Check repo state:**
   A **SessionStart banner** (`scripts/session_banner.sh`) should already have printed fetch/ahead-behind/dirty-tree/env_doctor at launch. Live wiring = `PROME/.claude/settings.json` (the root-level hook never fires for subdir launches — CC bug #10367, `finding_subdir_launch_hooks_dont_fire`). **No banner = flag it to Will**, then run the checks below manually. (Banner present ⇒ the checks below are confirmation, not discovery.)
   ```bash
   git status --short
   git diff --cached --name-only
   git fetch origin   # FETCH FIRST — ahead/behind reads the LOCAL tracking ref; a fetch-less 0/0 hides a machine-switch gap ([[finding_fetch_before_trusting_boot_sync]])
   git rev-list --left-right --count HEAD...origin/master
   ```
   If clean/safe, `git pull --rebase`. If dirty/untracked/staged, do not pull; read local continuity first and ask/triage.

1. **Read `PROME/HANDOFF.md`** — top live entries only; older history is archived.
2. **Read `PROME/SCRATCH.md`** — immediate handoff / what is hot **+ the operator card** (today's date, catalysts, near-gates; absorbed the old `TODAY.md`).
3. **Read `PROME/ACTIVE_DECISIONS.md`** — unresolved/approved-but-not-executed decisions before new work — **and `PROME/GATES.tsv` (fire-ledger):** any `FIRED-UNEXECUTED` row = 🔴 blocking (clear or escalate to Will before new work); LIVE-row staleness keys on the **`consumed_by`** field (flag rows whose consumer date passed or whose cell is empty; the old >5d raw-age rule is RETIRED). Register action-gates the session they're approved; owners' KBs stay canonical for full logic.
4. **Read `PROME/STATUS.md`** — agent/system health and work queue.
5. **Market-data freshness gate:**
   - Explicit-`Read` `HEARTBEAT.md` (PROME-facing regime memo — not auto-injected).
   - If today is a weekend/holiday or markets are closed, use it as **orientation only** and preserve its observation dates.
   - Before citing any level as current, run the market dashboard / fetch tool.
   - **Env doctor:** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/env_doctor.py --quiet` — machine-local key/infra presence (<1s, no network): FRED/EIA keys in the single-home `.env`, bashrc two-home drift, expected desktop extras. **rc=1 (✗) ⇒ fix or flag to Will before citing FRED-dependent levels.** Inventory canon = `PROME/MACHINE_LOCAL.md`.
   - **Position-agreement gate (whenever live capital exists):** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/position_agreement_check.py --all --quiet` — the POSITIVE check `ledger_staleness.py` cannot be (age ≠ agreement — a fresh file can lie, `[[finding_freshness_check_cannot_catch_a_fresh_lie]]`). rc=1 = a trade surface disagrees with its STATUS's live cards ⇒ flag to the owner (STATUS is canonical; the trade surface gets fixed). v1 scope = TRY-* card class only.
   - **⚡ ONE-SHOT GATE:** `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py boot` runs THIS WHOLE MECHANICAL STACK (env_doctor · position-agreement · board-scan · firetime · GATES vocabulary/fired/ages · DOCKET overdue · dashboard-state nonempty/vintage · boot↔closeout symmetry · read-cap byte meter [STATUS · AD · HEARTBEAT · SCRATCH vs 32,550 B]) in one verdict block — rc=1 only on BLOCKING failures; advisory class preserved. Each check stays independently runnable below. **New fleet-wide checks get added to the SCRIPT, not to this prose** (the missed-1c/1d class). ⚠️ It runs `board_scan --advance` — one invocation per boot, not per retry.
   - **5b. R1 corrections check (fleet-wide — FORUM-6 ruling ①, Will-approved 2026-08-17):** `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" PROME` — §9 rc 0/1/2; **rc=1 = a NAMED correction is unreceipted:** read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` and commit `PROME/registry/corrections_receipts.tsv`. *(Also runs inside `prome_gate.py boot`.)*
   - **Fire-time gate:** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/firetime_check.py --window 7 --quiet` — checks fire-path artifacts cited by `PROME/DOCKET.tsv` rows ≤7d out (dead pointers / date drift / canon-ordering). **A DATE flag ⇒ full logic re-read of the artifact** (a date fix can break gate sequencing — 7/1 WAL case), never a find-replace. **rc=1 always means act** — known-benign flags are suppressed by the **expiry-dated allowlist** (`scripts/firetime_allowlist.tsv`): expired rows re-flag themselves, so a clean quiet run = genuinely clean.
6. **Decide conditional reads:**
   - Fleet-state reads (`PROME/ROSTER.md` classification + DAEDALUS `FLEET_MAP.tsv` maturity) only for fleet work, stale-state risk, or Will-requested audit. *(`FLEET_SCAN.md` = superseded snapshot, historical only.)*
   - **BOARD diff-scan (every boot, ~1s — ALREADY RUN inside `prome_gate.py boot`; run standalone ONLY if the gate was skipped — the cursor advances on every invocation):** `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/board_scan.py --advance`. This is PROME's **pull**, and it is what makes the §3.5 pull-complete exemption sound — WALTER stops writing info-cc handoffs *only because* this scan is complete (whole-INDEX, every signal since the cursor, never a tier or a sample). **If this scan stops running, the exemption is void and must be handed back** — a BOARD-diff cannot surface what nobody scans. **rc=1 = PROME is on an ACTION line ⇒ disposition before proceeding** (genuinely exceptional, never routine). Cursor: `PROME/state/board_cursor.txt`.
   - `AGENTS/*/outbox/*to-PROME*` only for operational routing/signal work — **and `PROME/inbox/` is the SOLE PROME delivery surface** (Will-ruled 2026-07-24; matches `MESSAGING/DIRECT_MESSAGING_V1_SPEC.md`). **If `AGENTS/PROME/` ever reappears, that is a sender-routing regression, not a delivery surface** (removed 7/24, re-grew twice since) — read anything found there, migrate it to `PROME/inbox/`, then flag the sender; servicing it in place is what feeds the cycle.
   - Prome implementation/identity docs (`PROME/CLAUDE.md`, `PROME/SYSTEM.md`) only for implementation work.
   - `PROME/CLOSEOUT.md` before `/clear`, `/new`, or durable handoff.
7. **Declare boot state briefly:** synced/dirty, current regime source, market-data freshness posture, top pending decision/work lane, and any blocker.
8. **Flag top issues:** catalysts within 24h, stale agents, pending decisions, blockers, and a stale spine-audit stamp — **and put OWED prior-session work to Will as a choice, not a mention** (one line: *"owed from <date>: A · B · C — first, or after the <directed lane>?"* with a rec; a dated owed item reaching its third boot unrun leaves SCRATCH for a DOCKET `COVERED:` annotation or a WQ row — three consecutive boots 8/28–8/29 mentioned T6/HEN-42/NEXUS and let the directed lane absorb them) (`PROME/STATUS.md` header "Last spine audit" >7d — **or missing = stale** → run `PROME/tools/spine_audit.workflow.js` this session or flag it).
9. **Present top proposals** only when useful; max 5, ranked by urgency/position relevance.

---

## Conditional Modules

| Need | Read / Use |
|---|---|
| Market prices / dashboard | Read `FORGE/tools/market-data/README.md`. Run `dashboard.py` / `fetch.py` before citing levels. |
| Forward catalyst dates / fire-time artifacts | **`PROME/DOCKET.tsv` = canonical** (SCRATCH card + HEARTBEAT gates are views); `scripts/firetime_check.py` = the freshness checker (boot gate above). |
| Spine reconciliation (weekly) | `PROME/tools/spine_audit.workflow.js` — 8 paired readers over the 16-file boot-read/protocol spine set vs canon anchors (**the `/boot` + `/closeout` skill runners joined 8/29** — the root↔PROME parity gate compares the two COPIES, never a copy to its MANUAL, so it read green while `/boot` omitted five BOOT.md steps; the CANON block carries the layering rule, both directions), **+ 1 anchor reader sampling DOCKET's >7d PENDING tail at source artifacts** (added 8/16 audit-#9 review, Will-approved: the spine is checked AGAINST DOCKET, so a DOCKET error is self-sealing without it; `firetime_check` covers only ≤7d). Run when the STATUS "Last spine audit" stamp is >7d. **Fix rounds: prefer delete-and-point over annotate-and-accrete** — dated correction tags are themselves stale-able claims. Canon-change sweeps use the Mirror Map (`PROME/SYSTEM.md` → Canonical → Mirrors). |
| News routing / data feeds | Always-on collection runs in the **RESEARCH-INTAKE** repo (GitHub Actions; `[[project_research_intake_collection_lane]]`). **WALTER owns lane consumption** (wired 7/2, proven live 7/4 — see ACTIVE_DECISIONS row); **PROME never boot-reads the lane.** `FORGE/tools/news-sweep/sweep.py` = entity-index edits only (its cron died with the VPS). |
| Fleet scan / ranking | `PROME/ROSTER.md` (verified classification) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (maturity/state, DAEDALUS-owned) + `PROME/ORCHESTRAL_LAYER_DESIGN.md` (layer design). *`PROME/FLEET_SCAN.md` = superseded historical snapshot (its own banner says so) — don't boot-read it (doc-audit 7/10).* |
| Agent roster / classification | `PROME/ROSTER.md` — verified Active/Tier-2/Dormant/Retired + commit-activity evidence (refresh by re-running the activity map; `[[finding_verify_roster_by_commit_activity]]`) |
| Sub-agent spawn | `AGENTS.md`, `PROME/COMPLETION_SPEC.md`; include completion instructions. |
| **FORGE reconcile (new broker export) / FORGE mechanical follow-ups** | **Spawn agent type `anvil`** (skeleton = `.claude/agents/anvil.md`, Will-directed 2026-07-30) — the standing reconcile-clerk contract; supply the export transcription + post-snapshot events in the spawn prompt. Flow: ANVIL edits → PROME verifies at artifact → Will OK → ANVIL commits. *(FORGE owner = PROME since 2026-07-30 — root `CLAUDE.md`, position-truth paragraph in Key Directories/How-The-System-Works; section cite, line numbers rot [audit #10].)* |
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

---

## Boot-class fleet memories (fleet-memory embeds — migrated 2026-07-31, Phase-2 restructure)
*One-liners embedded from memory/auto/ (files unchanged); index rows now in memory/auto/INDEX_COLD.md. Read the linked file for the full lesson.*

- finding_display_filter_gating_safety_net — "A boot-summary keyword/priority filter written for forward sections silently gates the past-due safety net too — low-priority FIRED items vanish, and a fixed look-back window ages out unswept ones. Audit compact-mode filters against every section they touch (OTTO boot 7/25: 3 of 4 fired catalysts hidden, a 5th aged out)" `[[finding_display_filter_gating_safety_net]]`
- finding_boot_protocol_live_event_override — "SPAWN PROTOCOL framing pulls agents toward CLOSEOUT after boot even mid-event; the fix is neutral \"Write-back\" framing + explicit live-event override in EXECUTE step. Validated on VIOLET 2026-06-05 mid-VIX-spike." `[[finding_boot_protocol_live_event_override]]`
- finding_boot_predictions_scan — A cheap boot-time PREDICTIONS due/stale scan catches silently-stale OPEN predictions; caught a 24d-stale MISS on first run. Transferable to any agent with a predictions TSV. `[[finding_boot_predictions_scan]]`
- finding_boot_closeout_hardening_recipe — "Phased recipe for hardening an agent's boot/closeout protocol — mirror, strip live-state, audit-produce doc-ownership + deferred punch-list" `[[finding_boot_closeout_hardening_recipe]]`
- finding_boot_py_cadence_skip_pattern — "For monthly/low-frequency-data agents, the mature boot.py pattern is SAM/BRENT run-at-boot-defensively + mtime cadence-skip on fetchers — NOT a read-only/--pull opt-in split" `[[finding_boot_py_cadence_skip_pattern]]`
- finding_boot_sweep_macro_regime_context — Boot sweeps should include a macro-regime-context check (current Fed Chair / BOJ Gov / key central-bank principals + statement-style); month-old Chair changes can sit un-modeled across multiple sessions if the boot baseline only covers data feeds and event calendars `[[finding_boot_sweep_macro_regime_context]]`
- finding_revival_proxy_pattern — Step 4 of PROME/ORCHESTRAL_LAYER_DESIGN.md — foreground general-purpose subagent briefed as revival proxy for a stale persistent domain agent. Produces decision-grade catch-up + inbox-deposited revival packet for target agent to integrate on next boot. `[[finding_revival_proxy_pattern]]`
- finding_revival_boot_doc_sweep — "When reviving an agent stale 30+ days, sweep boot docs (CLAUDE.md, MEMORY.md, CALENDAR.md, STRATEGY.md, IDENTITY.md, USER.md) alongside STATUS — staleness compounds across all of them, not just the dashboard" `[[finding_revival_boot_doc_sweep]]`
- feedback_scan_agent_outboxes_at_boot — "When booting PROME, scan AGENTS/*/outbox/ for PROME-targeted signals — not just the PROME inbox — to close the outbox-resident signal discovery gap" *(quoted path modernized 8/3: the memory's original text said `AGENTS/PROME/inbox/`, a tree removed 2026-07-24 — delivery surface is `PROME/inbox/` per step 6; the directive half is unchanged)* `[[feedback_scan_agent_outboxes_at_boot]]`
- feedback_front_load_planning — "For multi-step deterministic work, surface all decisions in a pre-execution planning pass; let Will batch-approve defaults; then execute mechanical with proceed-pacing at step boundaries" `[[feedback_front_load_planning]]`
- finding_freshness_audit_vs_caught_up — mtime/STATUS-freshness ≠ caught-up; a fresh agent can still be behind on inbox backlog AND on a pending test in its own STATUS that already resolved `[[finding_freshness_audit_vs_caught_up]]`
- finding_gitignored_private_drop_boot_surfaced — "User-private data drops (broker/account exports) should be gitignored AND boot-surfaced — gitignore keeps them off the shared repo but also hides them from git status, so a boot-card line is the only discovery path. Privacy and discoverability are a matched pair; do one without the other and you either lose the data or leak it." `[[finding_gitignored_private_drop_boot_surfaced]]`
- finding_fetch_before_trusting_boot_sync — At boot, git ahead/behind reads the LOCAL remote-tracking ref and is stale until you `git fetch` — a `0/0` can hide a large gap (53 commits here), especially right after a serial-multi-machine switch; fetch before declaring "synced" or reading state. `[[finding_fetch_before_trusting_boot_sync]]`
- finding_inbound_lane_is_the_falsification_channel — "If a signal lane can carry a falsifier for a thesis you own, it is boot-mandatory not spawn-optional — HAWK's 9-day-unread WALTER signal contained the exact correction to its own canonical thesis" `[[finding_inbound_lane_is_the_falsification_channel]]`
