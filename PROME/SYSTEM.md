# Prome System Map
**Created:** 2026-05-08 21:28 ET · **Updated:** 2026-08-22 (stamp reconcile, audit #10 — the 8/16 FORGE/timing row re-sync rode under the 8/09 stamp; covered). Prior: 2026-08-09 (architecture second wave + deletion pass, Will-approved batch — scope manifest: T1-a census-executed record added under the Mirror Map · filing-watch row TOMBSTONED + cron-scripts trash note [FORGE audit M2/M3] · nothing else touched; FORGE corpus banners + education/auction-data archive moves live in FORGE itself.) Prior: 2026-08-03 EVE (spine-audit #7: Note-3 hardcoded "reconcile 7/20" STRIPPED — 2 reconciles stale AND the PAT-068 restated-vintage class root canon killed 7/30, while line 167 had already been corrected; RESEARCH-INTAKE table row synced to Note 4 [consumer wiring DONE 7/2, row said "open follow-up" for a month]; HY band wording aligned to config.py/KILL_MEMO [>280, <260×2closes]. Stamp note: body edits 7/28 [FLEET_SCAN retirement, generate-at-n≥3] and 7/30 [WILL_QUEUE mirror row, FORGE caveat] rode under the 7/11 stamp — covered now.) Prior: 2026-07-11 (spine-audit minors: stamp caught up — mirror-map rows carried 7/6 edits under the 7/01 stamp; auto-memory link wording symlink→hardlink [`[[finding_automem_hardlink_inplace_edit]]`]; scrub-plan pointer PROME-prefixed). Prior: 2026-07-01 (hygiene trim: dead `dashboard/server.py` row cut; OpenClaw spawn-prohibition → teams-mode reality; serial-multi-machine phrasing; HY-watch → intake-lane primary; FSK example marked historical; FORGE/STATUS caveat re-based). Prior: 2026-06-26 surgical refresh.  
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
| `MEMORY.md` (auto-memory index — lives in-repo at `memory/auto/`; `~/.claude/.../memory/` is a **directory symlink** to it, so normal Write/Edit tools are safe — `[[finding_automem_hardlink_inplace_edit]]` [superseded-hardlink slug, current model inside]) | High for curated lessons; check freshness | Operating lessons / findings / feedback index — the genuinely-injected memory layer. |

*(`AGENTS.md` + `USER.md` are **explicit boot-reads**, not injected — see the next table. `SOUL.md` + `IDENTITY.md` were deleted root-level in the 2026-06-30 public-prep cleanup.)*

> ⚠️ **`HEARTBEAT.md` is NOT injected (OpenClaw vestige).** It was auto-loaded under the always-on VPS model; in Claude Code it is NOT in PROME's boot context — PROME must explicitly `Read` it. It is a **PROME-facing regime memo only**: PROME writes it, PROME reads it. Domain agents (incl. NEXUS) do **not** boot-read it (verified 2026-06-27: 19/20 agent CLAUDE.md had zero HEARTBEAT references — ⚠️ a ~20-agent-era census; the 2026-07 cohort [WATT/VULCAN/MIDAS/OSPREY/FALCON/HOMER/WAL] was never censused. The rule stands by design, but re-verify the count before citing it as evidence — flagged 8/9, audit #8). See `BOOT.md`'s market-data freshness gate.

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
| `PROME/FLEET_SCAN.md` | **Superseded snapshot — do not rebuild** | Historical only (its own banner). Fleet stale-state/maturity is **DAEDALUS territory**: `PROME/ROSTER.md` (classification) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (maturity/state). *(Rebuild advertisement retired 7/28 — DAEDALUS objection, PROME-ratified: a vestigial design doc is the re-entry path for a duplicate surface.)* |
| `KERNELS.md` | On-demand reference | Durable cross-domain market mechanisms + research principles — no live levels, positions, roster or tool config (re-shaped 8/29 WQ-129; topology lives at `AGENTS.md` / `AGENTS/_NETWORK.md`; renamed from root `MEMORY.md` 6/30; not injected). |
| `memory/YYYY-MM-DD.md` | On-demand (daily log) | Daily session activity detail; not root-memory insight. |

### Canonical → Mirrors map

*(Added 2026-07-01, seeded from the 24-file audit. When a **canonical** doc changes, walk its row and verify each mirror before commit — CLOSEOUT Chunk-3 trigger. Canonical wins on drift (`[[finding_doc_mirror_consistency_check]]`). The weekly spine audit (`PROME/tools/spine_audit.workflow.js`) checks the same rows as the catch-all.)*

> **Generate-at-n≥3 rule (adopted 2026-07-28, Will-approved — DAEDALUS T1-c):** any hand-maintained mirror row that has rotted **3×** gets **generated from its source or reduced to a countless pointer** — hand-mirroring has empirically failed for that row class; stop re-committing to it. First application: the STATUS.md HEARTBEAT base/amendment-count rows (rotted at 3 consecutive re-bases → countless pointers, 7/28).
> **Mechanized walk:** `python3 scripts/consumer_check.py --mirror-map --old <OLD-TOKEN>` greps the retired token across every file named in **this table** (parsed at runtime — the tool carries no copy of the list) **plus PROME's own surfaces**. Run it on any canon/threshold change *(adopted 2026-07-28, Will-approved — DAEDALUS T1-b; born from the 7/28 PORTFOLIO miss, where the publisher checked its consumers and not itself).*
> **Census axis (for the 8/6-8/9 pass):** classify each mirror **declared-view-with-canonical-wins-rule** (SCRATCH operator card, HEARTBEAT Near-Gates — correct design, keep) vs **silent duplicate** (the debt class — every rot incident of 2026-07 was one). The census hunts the second class.
> **★ Census EXECUTED 2026-08-09 (T1-a, Will-approved batch).** Declared-view class, KEEP: SCRATCH operator card · HEARTBEAT §Thresholds/Near-Gates · WILL_QUEUE views in SCRATCH/HANDOFF · GIT_COORDINATION cookbook (owner of recipes, not a mirror) · root `CLAUDE.md:26` roster line (named Will-gated mirror, reconciled 8/5). Silent-duplicate class found → demoted same day: CLOSEOUT Chunk-4 git prose (pruned to command-block + root pointer — root canon is auto-injected, the restatement could only drift) · CLOSEOUT File-ownership table (merged into the Write-Back Contract — same table twice) · BOOT Non-Negotiables non-ff paragraph (demoted to pointer; its restated copy had rotted once already, re-based 8/3). Generate-class: none new (STATUS amendment count already converted 7/28). No other silent duplicates found in the Map's mirror lists.

| Canonical fact | Canonical home | Known mirrors (verify on canon change) |
|---|---|---|
| Gate C Kernel custody / carve-out ④ (PROME sole acceptance custodian; additions-only paths; desk submission carve-out) | root `CLAUDE.md` Git Protocol ④ + custody ¶ (reconciled 8/27 C8) | `PROME/GIT_COORDINATION.md` (carve-out ④) · `PROME/AUTONOMY.md` · `PROME/CLOSEOUT.md` Chunk 4 · `KERNEL/` runbooks |
| Root-canon provenance (incidents, dates, counts behind every root rule) | `docs/CANON_PROVENANCE.md` (keyed `key:` + `root-anchor:` per block; anchors must survive verbatim in root) | root `CLAUDE.md` header pointer · `PROME/CLOSEOUT.md` (canon-change trigger) |
| Git/push protocol (pathspec, auto-push, non-ff=routine, repo-root cwd) | root `CLAUDE.md` Git Protocol | `PROME/CLAUDE.md` (git-default ¶) · `PROME/BOOT.md` (non-negotiables) · `PROME/GIT_COORDINATION.md` (cookbook + Push Discipline) · `PROME/CLOSEOUT.md` (Chunk 4) · `PROME/AUTONOMY.md` (header note) · auto-memory `feedback_defer_push_coordinate` |
| Machine model (serial multi-machine, desktop ⇄ laptop) | root `CLAUDE.md` + `PROME/MACHINE_LOCAL.md` | `PROME/CLAUDE.md` (identity) · `SYSTEM.md` (Prome Runtime) · `ORCHESTRAL_LAYER_DESIGN.md` (open-questions bullet) · `PROME/public-prep/HISTORY_SCRUB_PLAN.md` (safety rail 5) |
| HY-watch mechanism (intake lane primary, desktop timer redundancy) | `HEARTBEAT.md` §Thresholds + intake repo | `PROME/STATUS.md` (Core State + HY lane row) · `SYSTEM.md` (Architecture Note 1) · `ACTIVE_DECISIONS.md` (RESEARCH-INTAKE + Post-FOMC rows) · bank-put proposal §F |
| Position truth (off-repo Will/broker; FORGE = stale mirror) | root `CLAUDE.md` + `FORGE/STATUS.md` banner | `SYSTEM.md` (Freshness Discipline + Note 3) · `ACTIVE_DECISIONS.md` (Current Mode) · `action-cards/TEMPLATE.md` (header) · bank-put proposal (inputs line) |
| Roster / classification | `PROME/ROSTER.md` | root `CLAUDE.md` (pointer only since 8/29 WQ-120 — the re-listed roster was removed) · `AGENTS.md` (table + run-model note) · `README.md` · `AGENTS/_INDEX.md` + `_NETWORK.md` *(skills/walter mirror retired — dir archived 7/6 → `archive/skills-openclaw/`)* |
| Forward catalyst dates | **`PROME/DOCKET.tsv`** | `SCRATCH.md` (operator card) · ~~`HEARTBEAT.md` (Near Gates)~~ **mirror RETIRED 2026-08-29 (WQ-121 eighth re-base: the section is gone; HEARTBEAT is pointer-only for dates — RAV caught this row still listing it, 8/29 PM)** · ~~`STATUS.md` (Next Best Action docket line)~~ **mirror RETIRED 2026-08-08 — that section is frozen to a pointer banner (Will-ruled); it carries no catalyst dates and must not be re-added as a mirror** · fire-time artifacts (checked by `scripts/firetime_check.py`) |
| Will's open items (operator queue) | **`PROME/WILL_QUEUE.md`** *(added 2026-07-30 at birth — DAEDALUS W6: register the mirror in the existing walk, never build a new grep)* | `SCRATCH.md` (operator-card 3-line pointer view — declared-view class) · `HANDOFF.md` "Open for Will" (dated history, not live) · any agent packet restating a Pending-Will list (regrow class — repoint to the queue on sight) |
| Trigger bands / levels | `FORGE/tools/market-data/config.py` + `AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md` + intake-lane alerts | `HEARTBEAT.md` §Thresholds · fire-time artifacts *(skills/walter trigger-table mirror retired — archived 7/6)* |

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
| `FORGE/timing/` | Prome / timing thesis | **FROZEN 2026-08-09** (banner in `FORGE/timing/README.md`; root `CLAUDE.md` Key Directories row concurs) — historical timing/convergence corpus; cite as history, never current. *(Row re-synced 8/16 audit #9 — it had described the corpus as live.)* |

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
| `PROME/FLEET_SCAN.md` | Superseded historical snapshot — never rebuild. | Fleet/agent audit → `PROME/ROSTER.md` + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (DAEDALUS-owned). |
| `PROME/archive/TOSCANINI_2026-03/` | Retired Toscanini queue/protocol archive. | Historical only; do not treat as live ops. |

---

## Tools / Data Layer

| Tool / path | Role | Rule |
|---|---|---|
| **`RESEARCH-INTAKE` repo** (clone `/home/willi/Research-Intake`) | **Always-on data-collection lane** — 6 feeds via GitHub Actions (EIA · EDGAR-8K · Treasury · CFTC-VIX · FRED · news-sweep), weekday-daily, agents read-only. **CI posture of THIS repo (stated 8/29 on RAV's review): ZERO GitHub workflows — `.github/workflows/` was removed with the SENTRY retirement (WQ-127); there is NO repository-wide automated verification; every check runs at boot/closeout gates on the operator's box. The August audit's finding moved from 'only a non-validator workflow exists' to 'no workflow exists' — a posture, not a cleanup.** | The autonomous collection surface: `liveness.json` + `SUMMARY.md` at root, `data/<UTC-date>/*.json`. **Consumer wiring DONE** (WALTER 7/2, proven live 7/4 — matches Note 4 below; this row had carried "open follow-up" for a month after completion). [[project_research_intake_collection_lane]] |
| `FORGE/tools/market-data/dashboard.py` | Live stress dashboard. | Run before citing current market levels. |
| `FORGE/tools/market-data/fetch.py` | Live prices / FRED series. | Use for individual live data pulls. |
| `FORGE/tools/news-sweep/sweep.py` | Thesis-tagged news sweep + routing (entity index / WATCH_FOR lists). | **Local cron is dead** (cut VPS); the fetch+classify logic is **revived in RESEARCH-INTAKE** (routing dropped). Use this copy mainly to edit the entity index. *(The 3 VPS-era cron scripts — `cron_sweep.sh`, `cron_dashboard.sh`, `morning_briefing.sh` — trashed 2026-08-09, FORGE audit M3: no crontab existed, one sourced a nonexistent `.env`.)* |
| `FORGE/tools/filing-watch/` | **DEAD — tombstoned 2026-08-09** (FORGE audit M2: data vintage 2026-05-07; superseded by RESEARCH-INTAKE's `edgar_8k` feed). | Do not use; the lane's EDGAR feed is the live path. |

Known current caveat:

- `FORGE/STATUS.md` **alone** is the broker-export-refreshed structured position mirror — **the reconcile vintage lives in ITS OWN header, deliberately not restated here** *(hardcoded-date mirror removed 2026-07-30, DAEDALUS FORGE-audit H2 — this line carried "7/20" for hours after the 7/30 reconcile; a date in an always-loaded doc that mirrors a file header is a PAT-068 machine)*; it **stales between exports** (its own banner governs); position truth is off-repo (Will/broker direct). **FORGE owner = PROME (Will-ruled 2026-07-30, DAEDALUS audit S1)** — reconciles run as PROME-directed spawns (ANVIL model). Never cite its marks as current. *(`FORGE/PORTFOLIO.md` = **FROZEN Feb-2026 snapshot, historical only, never half the live mirror** — pairing retired here 2026-07-28 per the Will-approved root `CLAUDE.md` correction; the stale pairing was the cause of VIOLET's position-missing symptom.)*

---

## Operating Defaults

Default to compact tool output so long sessions don't bloat the transcript. *(Relocated from `BOOT.md` 2026-07-01 — reference default, not a boot step.)*

- Inspect size/structure first: `wc`, `grep`, `find`, `git diff --stat`, `git diff --name-only`.
- Read targeted excerpts before whole files: prefer bounded `read`, `sed -n '1,120p'`, or focused greps.
- For large diffs, show stat/name-only first; print hunks only for files being actively reviewed.
- For generated reports/artifacts, write to file and summarize rather than pasting full content into chat.
- For agent freshness checks, read **content vintage first** — the file's own `Updated:`/two-clock header — never mtime-first (git sync restamps mtimes toward false-fresh, `[[finding_mtime_is_corrupted_by_git_sync]]`; bullet re-based 8/9, audit #8); deep-read only when decision-relevant.
- Escalate freely to full reads/diffs when correctness, safety, or editing requires it. This is a default, not a blind constraint.

---

## Freshness Discipline

Trust each file's own `Updated:` stamp over any table here (behavior-language beats date-pinning — stamps decay). Boot-refresh order is owned by `PROME/BOOT.md` — follow its sequence; don't maintain a competing order here (spine-audit 7/1: this paragraph had drifted from the owner doc).

- **Live market levels:** always re-run `FORGE/tools/market-data/dashboard.py` / `fetch.py` before citing — never quote levels from state files.
- **Position / execution truth:** Will/broker direct (**off-repo**), not these docs — FORGE is only the stale structured mirror. The legacy `POSITIONS.md`/`TRADE_DECISIONS.md` decision-support docs were retired 2026-06-30 (POSITIONS deleted — held a broker balance; TRADE_DECISIONS → `PROME/archive/`), superseded by FORGE + **TERRY** (trade construction / risk). `FORGE/STATUS.md` refresh before use.
- **Fleet state:** `PROME/ROSTER.md` (classification) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (maturity, DAEDALUS-owned) — `FLEET_SCAN.md` is a superseded snapshot, never rebuild it.

---

## Current Architecture Notes

1. **Detection/action layer is now automated (2026-06-26; re-based 2026-07-01).** Trigger detection runs unattended — the **RESEARCH-INTAKE lane is the machine-independent PRIMARY** for the HY OAS watch (GH Actions, weekday-daily, bands + named >280 X1-breach / <260-two-consecutive-closes re-kill alerts — band definitions per `config.py`/KILL_MEMO canon); LIQUID's desktop `liquid-hy-watch` systemd timer is machine-local **redundancy** (dark when that box is off). The trigger→card path is tooled: `AGENTS/TERRY/scripts/{chain_fetch,grade_print}.py` + `TRADE_CARD_TEMPLATE_FIRE.md`. Standing rule: deploy fresh capital only on a fired trigger ([[feedback_deploy_on_trigger_not_calendar]]).

2. **File-based messaging is in use but being replaced.** Don't patch inbox/outbox hygiene gaps — flag and let them ride ([[project_messaging_overhaul]]). *(7/14 delta: Direct Messaging v1 first cohort is LIVE — PROME→BRENT + PROME→SAM `MSG-*` routes under `MESSAGING/`, both proven 7/16; HERMES's folder was removed entirely in the 6/30 prune. All other routes: still let-ride.)* *(8/22 audit-#10 add: cross-session harness messaging — `SendMessage`/`ListAgents`, live 8/16, Will-ruled — is a third live lane; rules = `MESSAGING/CROSS_SESSION_MESSAGING.md`, root-canon pointer auto-injected.)*

3. **Execution truth lives outside these docs.** Position truth is **off-repo** (Will/broker direct); `FORGE/STATUS.md` alone is the broker-export structured mirror (**reconcile vintage lives in its own header, deliberately not restated here** — PAT-068 class-kill, root `CLAUDE.md:30`; stales between exports) — never cite its marks as current. *(`PORTFOLIO.md` = frozen Feb-2026 snapshot, historical only — pairing retired 7/28.)* Retired Toscanini refs → `PROME/archive/TOSCANINI_2026-03/` (historical only).

4. **Always-on collection now lives in the RESEARCH-INTAKE repo (2026-06-29).** Built as **GitHub Actions in a dedicated private repo, NOT a VPS** — collectors write only there, agents read read-only (no working-branch divergence by construction). 6 feeds weekday-daily; replaces the dead `/home/moltbot` VPS crons (news-sweep / dashboard). Consumer wiring DONE (WALTER 7/2, proven live 7/4); lane-side coverage doctor added 7/17 (`scripts/lane_coverage_check.py`, INFO-severity). [[project_research_intake_collection_lane]].

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
