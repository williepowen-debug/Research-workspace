# PROME Boot

**Owner:** PROME · **Updated:** 2026-10-05 (WQ-385 runtime compatibility; ruling: `PROME/proposals/2026-10-05_runtime-compatibility-RULED.md`). Prior: 2026-10-05 — maintenance; prior text and dated provenance: [boot snapshot](archive/BOOT_MAINTENANCE_2026-10-04/BOOT.md).

**Goal:** become operational fast.

**Auto-loaded context (Claude Code):** root/local/user-level `CLAUDE.md` and auto-memory `MEMORY.md`; re-read only for drift. `USER.md` must be explicitly read, subject only to the retained-context exception below; `AGENTS.md` is on-demand for roster/routing. Neither is auto-loaded. `SOUL.md` / `IDENTITY.md` do not exist.

On a runtime without confirmed context injection, explicitly read root `CLAUDE.md`, `PROME/CLAUDE.md` and `USER.md`. Do not assume Claude hooks ran. The gate defaults to `--charter-mode explicit`, assessing both charters in addition to declared reads. Only confirmed injection permits `--charter-mode injected`; pass the mode through `boot_session.py` (also on refresh). Saved verdicts retain their original coverage, never re-grade on retry. Standalone `scripts/read_cap_check.py --agent PROME --require-manifest --charter-mode explicit` checks that perimeter without a boot.

> **HEARTBEAT.md must be explicitly read at boot.** PROME owns this regime memo; domain agents do not read it. Trust map: `PROME/SYSTEM.md` → Boot Trust Stack.

---

## Non-Negotiables

- **Repo state first:** run `git status --short` + ahead/behind before pull/rebase.
- **No broad git operations:** never `git add .`, `git add -A`, `git reset HEAD`, force-push, or stash/reset unknown work.
- **Pull only if safe:** safe = clean working tree, no staged files, no known concurrent-agent risk. If dirty/untracked, read local continuity first and ask/triage; do not force sync just to boot.
- **Prices:** run `FORGE/tools/market-data/dashboard.py` or `fetch.py` before citing current levels.
- **Weekend / repeated-respawn rule:** on weekends or market holidays, `HEARTBEAT.md` may be used as regime orientation, but do **not** describe its levels as fresh. Say “last HEARTBEAT/Fri close” or refresh with dashboard/FRED before making a market claim. Repeated same-day Prome respawns should not rewrite `HEARTBEAT.md` or churn other state files for hygiene alone — only when a real market/system event or user decision changed.
- **FRED citation convention:** cite observation dates, e.g. `HY OAS 280bps [FRED 5/20 close]`.
- **No agent edits** unless Will explicitly approves.
- **No trade execution.** Trade rails are verification-required at every fire-time — root rule #4 (live prices, never STATUS marks) **plus** root position-truth canon (live broker book; FORGE is the stale mirror).
- **External/public sends require approval.**
- **Push auto at closeout:** ff-gated `scripts/safe-push.sh`, no per-push ask for own PROME work; shared/root docs need Will scope/approval. Non-ff is routine, never force; recovery/escalation → root Git Protocol.
- **Shared repo coordination:** when another agent has local/branch work, use `PROME/GIT_COORDINATION.md` before committing, merging, or pushing.
- **Multi-agent orchestration:** before spawning more than one agent, apply the substantive mode-split rule in `PROME/ORCHESTRATION_PLAYBOOK.md` and select the available mechanism from its Runtime mechanics section. Carry the shared delivery contract from `PROME/COMPLETION_SPEC.md` into each spawn brief. Launch preflight and authority remain governed by `PROME/CLAUDE.md`.

---

## Doc Ownership

Ownership/trust map: `PROME/SYSTEM.md` → **Boot Trust Stack**. Facts live at their owner; everything else is on-demand.

---

## Boot Sequence

**Bounded reads:** from repo root, use `python3 PROME/tools/boot_read.py <path>` for one document page per tool output. Follow each `next_offset` using `--offset <next_offset> --sha256 <sha256>` until `eof: true`; a changed-source refusal means restart that document. Truncated output is an incomplete read, never evidence of EOF. The manual's selected sections still determine read scope.

**Repeat boot:** reuse only acknowledged full `USER.md`/`BOOT.md` reads in retained context. Add `--read-state /tmp/prome-reads-ID.json --context-id ID` to `boot_read.py` reads/continuations; after contiguous EOF use `--ack-read --sha256 <sha256>`, later `--reuse`. New sessions, compaction, handoff or uncertain retention require a new ID and full reads. Read and acknowledge every `pending_policy_reads` path using that state/context before reuse; USER acknowledgement clears no other path. Never reset state/ID to bypass recovery. A failed recovery checkpoint requires abandoning reuse for this context and plain full reads; this is caller-enforced across restarts. Other mismatches/files require full reads. Live state, checks, private rulings and capability/preflight stay fresh. Repeat via `boot_session.py --run-dir <original-run-dir> --refresh`: completed original required, no BOARD advancement; incomplete original stays UNKNOWN, never bypassed with a new directory. Refresh grants no additional per-boot spawn allowance. Repeat manual steps; missing tools remain PARTIAL.

0. **Check repo state (and take the clock):**
   At the opening report, apply the runtime selection sequence in `PROME/COMPLETION_SPEC.md` and disclose private Artifact ruling access plus actual discovery, execution, messaging and closeout capabilities using AVAILABLE / UNAVAILABLE / UNKNOWN. Cite this session's tool evidence and discovery coverage; a shell probe cannot establish connector availability. Record gaps and dependent skipped steps in the existing boot receipt, and recheck at use. Apply the capability-specific consequences in `PROME/ORCHESTRATION_PLAYBOOK.md` § Runtime mechanics and canonical launch preflight in `PROME/CLAUDE.md`. Thread-local helpers do not establish fleet presence. Credential presence remains distinct from authentication.
   Use the prompt hook's `NOW: <day> <date> <time> ET` as clock (`PROME/.claude/settings.json`), never narrative. Without it, run `date` before any timestamp.
   The SessionStart banner (`scripts/session_banner.sh`, local settings wiring) reports fetch, ahead/behind, dirty tree and env_doctor. No banner ⇒ flag to Will and run these checks manually; otherwise confirm them. Subdirectory hooks need local wiring.
   ```bash
   git status --short
   git diff --cached --name-only
   git fetch origin   # FETCH FIRST — ahead/behind reads the LOCAL tracking ref; a fetch-less 0/0 hides a machine-switch gap ([[finding_fetch_before_trusting_boot_sync]])
   git rev-list --left-right --count HEAD...origin/master
   ```
   If clean/safe, `git pull --rebase`. If dirty/untracked/staged, do not pull; read local continuity first and ask/triage.

1. **Read `PROME/HANDOFF.md` in full using the bounded reader.** The declared read mode is `whole`; the retention target does not limit read scope. Preserve any read-budget finding until the file is brought within its existing budget or a separately reviewed scoped read is adopted.
2. **Read `PROME/SCRATCH.md`** — immediate handoff / what is hot **+ the operator card** (today's date, catalysts, near-gates).
3. **Read `PROME/ACTIVE_DECISIONS.md`** — unresolved/approved-but-not-executed decisions before new work — **and `PROME/GATES.tsv` (fire-ledger):** any `FIRED-UNEXECUTED` row = 🔴 blocking (clear or escalate to Will before new work); LIVE-row staleness keys on the **`consumed_by`** field (flag rows whose consumer date passed or whose cell is empty). Register action-gates the session they're approved; owners' KBs stay canonical for full logic.
   - **3b. Decision Deck pickup (WQ-202):** the hosted deck (`PROME/tools/decision_deck.py`; `DECK_URL` in `PROME/tools/will_handbook.py`) accepts Approve / Decline / Later. Read its store via Artifact: `action: read_db`, `db_op: query`, `collection: rulings`, `where consumed == false`. **GROUP BY WQ FIRST:** one tap is one document; latest `ts` is the ruling, earlier taps remain history. Record the consumed document `<id>` in the row; if several exist, record that fact and the earlier verdicts. Write each tap verbatim into `WILL_QUEUE.md` as *"tap via Decision Deck <ts>: <verdict> <note>"*, preserving the latest ruling. **A CHOICE tap (Change A, DOCKET L660, 2026-10-09):** group by `decision_id` (a decision UNIT such as `302.TLT`; absent ⇒ the WQ) and write *"tap via Decision Deck <ts>: CHOICE <decision_id> = <label> — <text as stored> <note>"* from the document's STORED `choice` text, never the queue's or the card's current text (a later re-labelling cannot change what Will ruled); a unit LATER is written the same way with LATER; a row holding several units stays OPEN while any unit is unruled and its state names each unit; the owner desk's record (root rule #10) receives the label, not a paraphrase; `options_shown` + `build` say which set he saw. Mark EVERY tap in that group consumed with `write_db` / `update`, `consumed: true` and pickup stamp, so superseded taps do not return next boot. A tap is Will's word only while the artifact is private (no viewer identity); **never share it**. Trade/spend consequents keep their own rails. Regenerate and republish at closeout (`PROME/CLOSEOUT.md`). **Deck feed (WQ-206):** Read `AGENTS/WALTER/LAST_COMPLETION.md` §WILL_NEEDS in this step; register Will-actionable items as WQ rows (WALTER never registers; PROME numbers).
4. **Read `PROME/STATUS.md`** — agent/system health and work queue.
   - **4b. Read § Boot-class fleet memories** (the last section of this file) — its FIRST group is the every-boot read; the other three groups are keyed to their own moments (mechanized step · desk revival · desk-hardening) and are there so the embed contract holds, not to act on now. The boot-class lessons have no other carrier; a runner that skips them re-learns a solved failure.
5. **Market-data freshness gate:**
   - Explicit-`Read` `HEARTBEAT.md` (PROME-facing regime memo — not auto-injected).
   - If today is a weekend/holiday or markets are closed, use it as **orientation only** and preserve its observation dates.
   - Before citing any level as current, run the market dashboard / fetch tool.
   - **Machine capabilities:** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/env_doctor.py --quiet` (machine-local presence, no network). Gate class CAPABILITY withholds only dependent work: AVAILABLE = present, not authenticated (point of use decides); UNAVAILABLE = absent; UNKNOWN = crash/unreadable/unrecognised rc, establishes nothing. Report until RESTORED. A WILL_QUEUE follow-up past needed-by becomes URGENT for escalation, never a gate on unrelated work. Canon: `PROME/MACHINE_LOCAL.md`.
   - **Position-agreement gate (whenever live capital exists):** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/position_agreement_check.py --all --quiet`. rc=1 ⇒ flag disagreement to the owner; STATUS is canonical and the trade surface gets fixed. Scope: TRY-* cards. This tests agreement, not merely age (`[[finding_freshness_check_cannot_catch_a_fresh_lie]]`).
   - **⚡ ONE-SHOT GATE:** `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_session.py --run-dir /tmp/prome-boot-<session-id>` runs the mechanical stack in `prome_gate.py boot`. Choose the run directory ONCE per boot and reuse it on retry. The receipt prevents another BOARD-advancing attempt through that directory; it is not a global lock. Completed retries return the saved verdict and observation time; incomplete attempts return UNKNOWN without rerunning. Inspect saved logs and independently runnable checks; never invent another directory or call the raw boot gate to bypass the guard. Read `gate.txt` and every named log to EOF using the bounded reader. Only the WQ-249 orchestration log may use `--view orch-compact-v1`: identical UNKNOWN reasons are grouped, every full identity and all other text retained, never converted to receipts. Continue with the same view and returned offset/digest; source/view changes require restart. `full-fallback`, missing view or rendering errors require full-text inspection; an unreadable original remains UNKNOWN. Originals remain drill-down evidence; previews never suffice. The gate's verdict block owns the check list and severity; rc=1 means blocking failure, rc=2 unknown execution. **New fleet-wide checks get added to the SCRIPT, not to this prose.** Optional `--sessions-json <path>` takes a fresh same-host `session_bridge.py` snapshot; otherwise presence is collected in the caller's visible namespace. A snapshot is scoped evidence; record its runtime/namespace coverage and observation time. It never alone proves a desk absent or replaces the canonical same-minute Desk-spawn preflight in `PROME/CLAUDE.md`. Acquisition details: `PROME/tools/SESSION_PILOT.md`.
   - **5b. R1 corrections check (fleet-wide — FORUM-6 ruling ①, Will-approved 2026-08-17):** `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" PROME` — rc 0/1/2 per `AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md` §9; **rc=1 = a NAMED correction is unreceipted:** read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` and commit `PROME/registry/corrections_receipts.tsv`. *(Also runs inside `prome_gate.py boot`.)*
   - **Fire-time gate:** `cd "$(git rev-parse --show-toplevel)" && python3 scripts/firetime_check.py --window 7 --quiet` — checks fire-path artifacts cited by `PROME/DOCKET.tsv` rows ≤7d out (dead pointers / date drift / canon-ordering). **A DATE flag ⇒ full logic re-read of the artifact** (a date fix can break gate sequencing), never a find-replace. **rc=1 always means act** — known-benign flags are suppressed by the **expiry-dated allowlist** (`scripts/firetime_allowlist.tsv`): expired rows re-flag themselves, so a clean quiet run = genuinely clean.
6. **Decide conditional reads:**
   - Fleet-state reads (`PROME/ROSTER.md` classification + DAEDALUS `FLEET_MAP.tsv` maturity) only for fleet work, stale-state risk, or Will-requested audit. *(`FLEET_SCAN.md` = superseded snapshot, historical only.)*
   - **BOARD diff-scan (every boot, ALREADY inside `prome_gate.py boot`):** run standalone ONLY if the gate was skipped: `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/board_scan.py --advance`. A bare scan never writes the cursor; `--advance` writes `PROME/state/board_cursor.txt` ONLY with no undispositioned ACTION/unreadable lines. A held cursor is expected: disposition those lines, never use `--ack-actions` just to restore advancement. Scan the whole INDEX, every signal since cursor, never a tier/sample. **rc=1 ⇒ PROME is on an ACTION line; disposition before proceeding.** If the scan stops, the pull-complete exemption (`AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` §3.5) is void and must be handed back to WALTER.
   - `AGENTS/*/outbox/*to-PROME*` reads are conditional on routing/signal work. **`PROME/inbox/` is PROME's SOLE delivery surface** (`MESSAGING/DIRECT_MESSAGING_V1_SPEC.md`). If `AGENTS/PROME/` reappears, read its contents, migrate to `PROME/inbox/`, and flag the sender; never service it in place.
   - Prome implementation/identity docs (`PROME/CLAUDE.md`, `PROME/SYSTEM.md`) only for implementation work.
   - `PROME/CLOSEOUT.md` before `/clear`, `/new`, or durable handoff.
7. **Declare boot state briefly:** synced/dirty, current regime source, market-data freshness posture, top pending decision/work lane, and any blocker.
8. **Report, then continue.** **Report:** catalysts within 24h · stale agents · pending decisions · blockers · **UNAVAILABLE or UNKNOWN capabilities** · a stale spine-audit stamp (`PROME/STATUS.md` header "Last spine audit" >7d — **or missing = stale** → `/spineaudit` this session or flag it) · **and a ranked one-line digest of owed prior-session work with the first action stated** (*"owed: A · B · C — starting A"*). **Then start it.** If Will directed no task, select the highest-priority authorized work and start it — announced as a statement, never offered as a menu.
   - **Interrupt test — ONE question: _is Will's ANSWER necessary for PROME's next action?_** Necessary = the next action **cannot be completed without it**: a decision only Will can make (a trade or spend consequent; a Will-gated surface the lane must edit; a ruling the lane's next step consumes), or a dependency PROME **can name** that blocks the directed lane. **YES ⇒ ask, and stop on that item only. NO ⇒ surface it and keep working.**
   - ★ Work that needs Will's **hands** but not his **answer** — a token to paste, a key to supply, a trade only he can place — is **surfaced, never asked**: PROME's own next action does not depend on it.
   - ⛔ **Urgency is not an interrupt.** Surface dated/overdue items, urgent risks and missing capabilities prominently; urgency never decides whether work proceeds.
   - ⛔ **Anti-scoping:** if ANY authorized next action on the same subject needs Will's answer, the item is an ask, whichever action PROME elects.
   - **Absent a YES, routine authorized maintenance is PROME's to run, not to ask about** — the tier is `PROME/AUTONOMY.md`'s, and Tier 1 already covers follow-up work inside an approved workstream.
   - A dated owed item reaching its third boot unrun leaves SCRATCH for a DOCKET `COVERED:` annotation or a WQ row.
   - Ruling record + acceptance tests: `PROME/proposals/2026-09-12_wq239-boot-interrupt-contract-RULED.md`.
9. **Present top proposals** only when useful; max 5, ranked by urgency/position relevance.

---

## Conditional Modules

| Need | Read / Use |
|---|---|
| Market prices / dashboard | Read `FORGE/tools/market-data/README.md`. Run `dashboard.py` / `fetch.py` before citing levels. |
| Forward catalyst dates / fire-time artifacts | **`PROME/DOCKET.tsv` = canonical** (SCRATCH card + HEARTBEAT gates are views); `scripts/firetime_check.py` = the freshness checker (boot gate above). |
| Spine reconciliation (weekly) | `/spineaudit` → `PROME/tools/spine_audit.workflow.js`: 8 paired spine readers (including runners vs manuals) + 1 anchor reader sampling DOCKET's >7d PENDING tail at source; `firetime_check` covers ≤7d. Run when STATUS's stamp is >7d. Fix by delete-and-point, not accumulating correction tags; canon sweeps follow SYSTEM's Mirror Map. |
| News routing / data feeds | Always-on collection runs in the **RESEARCH-INTAKE** repo (GitHub Actions; `[[project_research_intake_collection_lane]]`). **WALTER owns lane consumption; PROME never boot-reads the lane.** `FORGE/tools/news-sweep/sweep.py` = entity-index edits only (no cron). |
| Roster / classification / fleet scan | `PROME/ROSTER.md` (activity and responsibility classes; refresh via commit-activity map, `[[finding_verify_roster_by_commit_activity]]`) + `AGENTS/DAEDALUS/FLEET_MAP.tsv` (maturity, DAEDALUS-owned) + `PROME/ORCHESTRAL_LAYER_DESIGN.md`. `PROME/FLEET_SCAN.md` is historical, never boot-read. |
| Sub-agent spawn | `AGENTS.md`, `PROME/COMPLETION_SPEC.md`; include completion instructions. |
| **FORGE reconcile (new broker export) / FORGE mechanical follow-ups** | **Spawn agent type `anvil`** (skeleton = `.claude/agents/anvil.md`, Will-directed 2026-07-30) — the standing reconcile-clerk contract; supply the export transcription + post-snapshot events in the spawn prompt. Flow: ANVIL edits → PROME verifies at artifact → ANVIL commits (operator OK retired 9/30; AUTONOMY change log). *(FORGE owner = PROME, root canon.)* |
| Prome implementation / identity | `PROME/CLAUDE.md` + `PROME/SYSTEM.md` |
| Autonomy tier / recent grant-revoke | `PROME/AUTONOMY.md` — full change-log; behavior-changing grants also propagate to the auto-loaded `PROME/CLAUDE.md` Ask-First section (that's what's read every boot) |
| Position reconciliation | `PROME/ACTIVE_DECISIONS.md`, relevant action cards, `FORGE/STATUS.md` + broker/Will truth (position truth is off-repo) |
| Git commit patterns (cookbook) | `PROME/GIT_COORDINATION.md` → Commit cookbook — modified/new/mixed pathspec recipes + push/coordination rules |
| "Works on the other machine, fails here" / missing cred, timer, tool | `PROME/MACHINE_LOCAL.md` — machine-local inventory + switching checklist (Will runs serial multi-machine, desktop ⇄ laptop) |
| **Is surface X a WHOLE read or instrument-covered?** | **`PROME/registry/READS.tsv` — PROME's own attested read manifest: mode, protocol-mismatch and owed fix per surface.** ⚠ **Added 2026-09-12 because the answer to the GATES whole-vs-grep question was ALREADY RECORDED there and nothing on this boot path pointed at it** — PROME re-derived it by judgment and commissioned a sitting to settle what the registry already said (DAEDALUS, L209). `read_cap_check.py` now consumes this file. |
| Tool-output / freshness-read defaults | `PROME/SYSTEM.md` → Operating Defaults (compact tool output; mtime/header-first freshness reads) |

---

## Closeout Pointer

Before `/clear`, `/new`, long pauses, or handoff: read `PROME/CLOSEOUT.md` and run the appropriate tier.

Closeout is the write-back tail of boot: update only the owner docs whose state actually changed.

---

## Boot-class fleet memories (fleet-memory embeds — migrated 2026-07-31, Phase-2 restructure; per-item review 2026-08-29 EVE)
*Memory hooks; the `INDEX_COLD.md` pointers resolve here. Only the first group is every-boot; other groups apply at their named trigger. Full lessons: `memory/auto/<slug>.md` (on-demand).*

**PROME's own boot (unpredictable-trigger — read every boot):**
- finding_boot_sweep_macro_regime_context — a month-old Fed-Chair/BOJ-Gov change can sit un-modeled if boot covers only feeds + calendars; check principals
- finding_inbound_lane_is_the_falsification_channel — a lane that can carry a falsifier for a thesis you own is boot-MANDATORY, never spawn-optional (HAWK 9d unread)
- finding_gitignored_private_drop_boot_surfaced — gitignored drops (broker exports) are invisible to `git status`; a boot-card line is the only discovery path
- feedback_front_load_planning — multi-step deterministic work: surface every decision in ONE planning pass, let Will batch-approve, then execute mechanically
- finding_display_filter_gating_safety_net — a forward-section display filter silently gates the past-due safety net too (OTTO 7/25: 3-of-4 fired items hidden)

**Already mechanized on PROME's boot path (pointer only — the step is the carrier):**
- finding_fetch_before_trusting_boot_sync → step 0 (`git fetch` before ahead/behind) · feedback_scan_agent_outboxes_at_boot → step 6 (the every-boot carrier is the BOARD diff-scan inside the gate; the raw `outbox/*to-PROME*` read stays conditional — WALTER routes, the scan is the pull) · finding_freshness_audit_vs_caught_up → `prome_gate.py boot` (step 5) check "agent freshness (ground-truth vs narrative)", ADVISORY class — never stops boot (mtime-fresh ≠ caught-up on inbox backlog)

**Reviving a stale desk (read at spawn time, not every boot):** procedure → `ORCHESTRAL_LAYER_DESIGN.md` § Revival-proxy v3 brief spec. At this trigger read `memory/auto/finding_revival_proxy_pattern.md` and `memory/auto/finding_revival_boot_doc_sweep.md` (the latter covers the full doc sweep after 30+ days stale).

**Domain-desk boot-protocol patterns (read when hardening a desk's boot/closeout, not every boot):** read the corresponding `memory/auto/` lessons: `finding_boot_protocol_live_event_override.md`, `finding_boot_predictions_scan.md`, `finding_boot_closeout_hardening_recipe.md`, `finding_boot_py_cadence_skip_pattern.md`. DAEDALUS owns the blueprint class.
