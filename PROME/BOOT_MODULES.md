# PROME/BOOT_MODULES.md — on-demand companions of `PROME/BOOT.md` (created 2026-10-16 16:1x ET, rotation M2–M5; plan + reads: `PROME/proposals/2026-10-16_boot-rotation-PLAN.md`; M6 Resume after a restart moved 2026-10-29; M7 rotation #3 (log-read contract · fleet memories · Non-Negotiables · banners) 2026-10-30 — plan PROME/proposals/2026-10-30_boot-rotation-3-PLAN.md; M6's plan `PROME/proposals/2026-10-29_boot-rotation-PLAN.md`)
**Owner:** PROME. **Not a boot read** — each section is opened at the trigger its BOOT.md pointer names. Every section below is the BOOT.md text byte-identical at the move (crc32 per section in the commit body); it is maintained HERE from now on, never re-copied into BOOT.md. READS.tsv mode `scoped`.

## Repeat boot
*Trigger: before reusing ANY earlier read in retained context, or on `--refresh`.*

**Fresh-context continuation:** § Resume after a restart (this file; pointer at BOOT.md's § heading) may reuse the completed original mechanical run via `--refresh`, but never its instruction-read acknowledgements. Its explicit fresh-read, live-check and carried-obligation requirements replace the full manual sequence for that branch only. The retained-context read-reuse contract below is unchanged.

**Repeat boot:** reuse only acknowledged full `USER.md`/`BOOT.md` reads in retained context. Add `--read-state /tmp/prome-reads-ID.json --context-id ID` to `boot_read.py` reads/continuations; after contiguous EOF use `--ack-read --sha256 <sha256>`, later `--reuse`. New sessions, compaction, handoff or uncertain retention require a new ID and full reads. Read and acknowledge every `pending_policy_reads` path using that state/context before reuse; USER acknowledgement clears no other path. Never reset state/ID to bypass recovery. A failed recovery checkpoint requires abandoning reuse for this context and plain full reads; this is caller-enforced across restarts. Other mismatches/files require full reads. Live state, active checks and capability/preflight stay fresh; private Deck rulings and Deck-specific access probes remain PAUSED BY WILL (WQ-460), with unseen taps UNKNOWN. Repeat via `boot_session.py --run-dir <original-run-dir> --refresh`: completed original required, no BOARD advancement; incomplete original stays UNKNOWN, never bypassed with a new directory. Refresh grants no additional per-boot spawn allowance. Repeat active manual steps; unavailable tools needed by active duties remain PARTIAL. Paused Deck access alone does not make a repeat boot PARTIAL.

## Deck unit taps (Change A)
**PAUSED BY WILL (WQ-460, 2026-10-19):** this module is dormant; no hosted-store pickup or consumption during the pause. Resume requires Will's word and reconciliation under `PROME/proposals/2026-10-19_wq460-decision-deck-paused-RULED.md`. After resume, trigger: the Decision Deck store returns ANY unconsumed document. Group by `decision_id` first (absent ⇒ WQ); the latest `ts` governs that group and earlier taps remain history. Full pre-pause pickup procedure remains in BOOT.md git history; restore the reviewed procedure before using this module.

**A unit tap (Change A, DOCKET L660, 2026-10-09; the grouping rule above already keys it):** a CHOICE is written *"tap via Decision Deck <ts>: CHOICE <decision_id> = <label> — <text as stored> — <consequence as stored> <note>"* from the document's STORED `choice` fields (text AND consequence, brackets included), never the queue's or the card's current text (a later re-labelling cannot change what Will ruled); a PLAIN unit's APPROVE / DECLINE is written *"tap via Decision Deck <ts>: <verdict> <decision_id> — <meaning as stored in choice.text> <note>"* (the page shows that meaning beside the verb and stores it); a unit LATER is written *"… LATER <decision_id> <note>"* and leaves that unit UNRULED (OPEN); a document with NO `decision_id` on a row that now has units (a tap on a pre-Change-A build) is written to the row verbatim as Will's word but consumed as a ruling on NO unit — PROME asks him which unit it meant; a row holding several units stays OPEN while any unit is unruled and its state names each unit; when taps on DIFFERENT rows bear on the SAME position (e.g. WQ-357 and 302.TLT on the TLT 82P), PROME writes both verbatim and asks Will which governs before either is encoded; the owner desk's record (root rule #10) receives the label, not a paraphrase; `options_shown` + `build` say which set he saw. 

## Conditional modules
*Trigger: the need named in the first column (BOOT.md step 6 and the pointer line).*

| Need | Read / Use |
|---|---|
| Market prices / dashboard | Read `FORGE/tools/market-data/README.md`. Run `dashboard.py` / `fetch.py` before citing levels. |
| Forward catalyst dates / fire-time artifacts | **`PROME/DOCKET.tsv` = canonical** (`PROME/state/CALENDAR.md` = the generated calendar view, read at BOOT step 2; SCRATCH card + HEARTBEAT gates are views); `scripts/firetime_check.py` = the freshness checker (boot gate above). |
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


## Trigger-keyed fleet memories
*Trigger: reviving a stale desk (spawn time) · hardening a desk's boot/closeout. Embed census: `memory/auto/INDEX_COLD_EMBEDDED.md`.*

**Reviving a stale desk (read at spawn time, not every boot):** procedure → `ORCHESTRAL_LAYER_DESIGN.md` § Revival-proxy v3 brief spec. At this trigger read `memory/auto/finding_revival_proxy_pattern.md` and `memory/auto/finding_revival_boot_doc_sweep.md` (the latter covers the full doc sweep after 30+ days stale).

**Domain-desk boot-protocol patterns (read when hardening a desk's boot/closeout, not every boot):** read the corresponding `memory/auto/` lessons: `finding_boot_protocol_live_event_override.md`, `finding_boot_predictions_scan.md`, `finding_boot_closeout_hardening_recipe.md`, `finding_boot_py_cadence_skip_pattern.md`. DAEDALUS owns the blueprint class.


---

## Runtime disclosure

Mandatory at BOOT.md step 0 on every boot.

At the opening report, apply the runtime selection sequence in `PROME/COMPLETION_SPEC.md` and disclose actual discovery, execution, messaging and closeout capabilities; private Artifact ruling access is PAUSED BY WILL (WQ-460), with no Deck-specific probe required using AVAILABLE / UNAVAILABLE / UNKNOWN. Cite this session's tool evidence and discovery coverage; a shell probe cannot establish connector availability. Record gaps and dependent skipped steps in the existing boot receipt, and recheck at use. Apply the capability-specific consequences in `PROME/ORCHESTRATION_PLAYBOOK.md` § Runtime mechanics and canonical launch preflight in `PROME/CLAUDE.md`. Thread-local helpers do not establish fleet presence. Credential presence remains distinct from authentication.

---

## Resume after a restart (WQ-526, 2026-10-26)
*Trigger: Will's words “pick up PROME” (the bounded continuation of an unfinished working session). Step numbers inside cite PROME/BOOT.md's steps; "this BOOT.md" in its step 1 and "the full sequence below" mean PROME/BOOT.md.*


“pick up PROME” (Will 2026-10-29 13:23 ET; the former trigger “Resume PROME” is RETIRED, not an alias — it collided with Claude’s `--resume` and the launcher’s Resume button) selects this bounded continuation of an unfinished working session. “Checkpoint for restart” selects CLOSEOUT's Bounce checkpoint. Ordinary “boot” remains the full sequence below; end-of-day/machine-switch closeout is not a checkpoint. Same date or unchanged HEAD is neither necessary nor sufficient for validity. This branch replaces the full boot's execution order only when the following eligibility and steps are satisfied; other restrictions remain binding.

1. **Fresh context and eligibility.** Resolve root/cwd, take the clock, and read current root/local instructions and USER.md afresh (confirmed injection may satisfy the charters, never saved read acknowledgements). Read this BOOT.md, CLOSEOUT.md § Restart checkpoint, HANDOFF and SCRATCH using the existing bounded reader. Locate the original working-session identity, original boot run directory, unresolved controls, consumed process/spawn/review allowances and task/artifact pointers. A valid completed mechanical original (boot_session.py's existing validation) is required; an overall PARTIAL boot may continue only with every unresolved obligation carried and dependent work still withheld. Missing identity/baseline/limits, incomplete mechanical original, uncertain repository/host continuity, or lost work requires recovery/full boot; never invent a new baseline to bypass failure or reset allowances. A relevant instruction change requires reading and reconciling its consequences; unrelated commits alone do not invalidate continuation. The departing PROME must have yielded write ownership; no two PROME writers.
2. **Fresh checks.** Run step0's runtime disclosure and Git/fetch checks; do not pull over foreign work. Read STATUS restrictions and the active-decision digest (ACTIONABLE and touched GUARD rows whole), WALTER WILL_NEEDS, and the current calendar against canonical DOCKET/GATES for elapsed/newly due obligations. Regenerate the existing calendar view if stale; do not trust its saved date. Run `python3 PROME/tools/boot_session.py --run-dir <original-run-dir> --refresh` from the repository root, with the actual charter mode. Read its full verdict/log under step5's existing contract. This is the existing mechanical refresh, not a cheaper new checker; it does not advance BOARD. All blocking/ACTION obligations retain their existing disposition rules; a quiet refresh cannot discharge an earlier manual gap.
3. **Arrivals, ownership and task.** Census and disposition the current PROME inbox under step6, including arrivals after the checkpoint, corrections, Will rulings and any gitignored private-drop check required by the boot memories. Read the spawn-slate top block and source rows relevant to action; review deadlines against the fresh clock even if Git is unchanged. Re-establish identity/reachability before coordinating any saved assignment; saved IDs are leads, not presence. Unknown owner survival forbids a replacement writing launch; apply the existing same-minute preflight at launch. Preserve approved assignments, owner scopes and all consumed session allowances. An interrupted worker resumes only after its prior writer is verified stopped; do not infer completion from a delivery or idle state. Follow CLOSEOUT's checkpoint rule for session-bound workers.
4. **Targeted context, then act.** Read the research/HEARTBEAT sections and boot-memory guidance needed by the resumed task, changed decisions, arrivals or flagged checks. Unlike full step5/4b/9, no automatic whole HEARTBEAT reload, broad boot-memory recital, unrelated historical report reload, dashboard pull or new top-proposals exercise is required. A changed-source/task/market requirement triggers its relevant read or refresh; current-price tasks still require fresh observations. Step8's book line, decision/critical-blocker, ACTION/SKIPPED/PARTIAL and research-first rules remain, expressed as a concise delta; explicitly name carried unresolved controls. Say which task is resumed and take its next authorized action. A valid checkpoint is research navigation, not retained conversational memory or a completed boot verdict.

This mode adds no spawn allowance, closes no assignment and changes no grade or trade authority. Day boundaries and new events trigger fresh due-work checks, not automatic clearance. The actual end-of-day Standard closeout and its duties remain owed. If no new arrival/deadline occurred, report that observation rather than claiming that detection was experimentally demonstrated.

---

## Gate log-read contract
*Moved verbatim from `PROME/BOOT.md` 2026-10-30 under WQ-552 A (rotation #3); crc32 3869686084 over the moved text as stated in the plan; plan `PROME/proposals/2026-10-30_boot-rotation-3-PLAN.md`.*

**Log-read contract (change 2026-10-16, Will's word 16:04 ET; acceptance `PROME/tools/tests/ACCEPTANCE_gate_log_summary_2026-10-16.md`): read `gate.txt` to EOF with the bounded reader — it carries every check's verdict, its named flags and, for the WQ-249 orchestration check, the four closeout-state counts with today's touch names read from the log itself. A named log is read (bounded reader, to EOF) ONLY when its gate line is ⚠️/❌ AND the line's preview does not name the item PROME must act on, or when PROME drills into one named flag; the WQ-249 log's UNKNOWN rows older than today are legacy and are never a boot read. A WQ-249 line that names every touch dated today (the four states and the UNKNOWN rows) is COMPLETE — its standing sentence *spawn inventory coverage UNKNOWN* is printed on every run and alone never requires the log; UNKNOWN rows older than today are the standing WQ-249 backlog, worked at closeout (Pre-closeout 3), not re-read at boot. The spawn-list line carries the class counts and every DARK and ACTIVE row id; ACTIVE rows take their consumer read at the owner's artifact (the slate's read-first list, step 6), never from the log. A gate line reading `UNKNOWN: counts UNKNOWN — read the log` means exactly that. Only the WQ-249 log may use `--view orch-compact-v1` when it IS read: identical UNKNOWN reasons are grouped, every full identity and all other text retained, never converted to receipts; continue with the same view and returned offset/digest; `full-fallback`, missing view or rendering errors require full-text inspection; an unreadable original remains UNKNOWN. The gate's verdict block owns the check list and severity; rc=1 means blocking failure, rc=2 unknown execution. **New fleet-wide checks get added to the SCRIPT, not to this prose.** Optional `--sessions-json <path>` takes a fresh same-host `session_bridge.py` snapshot; otherwise presence is collected in the caller's visible namespace. A snapshot is scoped evidence; record its runtime/namespace coverage and observation time. It never alone proves a desk absent or replaces the canonical same-minute Desk-spawn preflight in `PROME/CLAUDE.md`. Acquisition details: `PROME/tools/SESSION_PILOT.md`.

---

*Moved verbatim from `PROME/BOOT.md` 2026-10-30 under WQ-552 A (rotation #3); crc32 2981797587 over the moved text as stated in the plan; plan `PROME/proposals/2026-10-30_boot-rotation-3-PLAN.md`.*

## Boot-class fleet memories (fleet-memory embeds — migrated 2026-07-31, Phase-2 restructure; per-item review 2026-08-29 EVE)
*Memory hooks; the `INDEX_COLD.md` pointers resolve here. Only the first group is every-boot; other groups apply at their named trigger. Full lessons: `memory/auto/<slug>.md` (on-demand).*

**PROME's own boot (unpredictable-trigger — read every boot):**
- finding_boot_sweep_macro_regime_context — a month-old Fed-Chair/BOJ-Gov change can sit un-modeled if boot covers only feeds + calendars; check principals
- finding_inbound_lane_is_the_falsification_channel — a lane that can carry a falsifier for a thesis you own is boot-MANDATORY, never spawn-optional (HAWK 9d unread)
- finding_gitignored_private_drop_boot_surfaced — gitignored drops (broker exports) are invisible to `git status`; a boot-card line is the only discovery path
- feedback_front_load_planning — multi-step deterministic work: surface every decision in ONE planning pass, let Will batch-approve, then execute mechanically
- finding_display_filter_gating_safety_net — a forward-section display filter silently gates the past-due safety net too (OTTO 7/25: 3-of-4 fired items hidden)

**Already mechanized on PROME's boot path (pointer only — the step is the carrier):**
- finding_fetch_before_trusting_boot_sync → step 0 (`git fetch` before ahead/behind) · feedback_scan_agent_outboxes_at_boot → step 6 (the every-boot carrier is the BOARD diff-scan inside the gate; the raw `outbox/*to-PROME*` read stays conditional — WALTER routes, the scan is the pull) · finding_freshness_audit_vs_caught_up → `prome_gate.py boot` (step 5) check "agent freshness (ground-truth vs narrative)" (advisory, per-agent staleness) plus the ACTION OWED check "PROME/inbox drained" (every unfiled file; 2026-10-21) — neither stops boot (mtime-fresh ≠ caught-up on inbox backlog)

**Trigger-keyed groups** (desk revival · desk hardening) → `PROME/BOOT_MODULES.md` § Trigger-keyed fleet memories (read at the spawn or hardening moment, never at boot).

---

## Rotated Non-Negotiables (2026-10-30)
*Verbatim prior text of `PROME/BOOT.md` § Non-Negotiables before rotation #3 (crc32 816980847); the live, tightened block is in BOOT.md — this is history, not instruction.*

## Non-Negotiables

- **Repeated same-day respawns:** do not rewrite HEARTBEAT or churn state for hygiene alone; require a real market/system event or user decision.
- **FRED citations:** name observation dates, not retrieval dates.
- Root `CLAUDE.md` Critical Rules #4/#5, position-truth canon and Git Protocol bind; PROME/CLAUDE.md Ask-First governs external sends and shared/root edits. Use live prices and the broker book at trade fire-time; FORGE is a stale mirror, never execution authority.
- **No trade execution.**
- **No agent edits** unless Will explicitly approves.
- **Shared repo coordination:** when another agent has local/branch work, use `PROME/GIT_COORDINATION.md` before committing, merging, or pushing.
- **Multi-agent orchestration:** before spawning more than one agent, apply `PROME/ORCHESTRATION_PLAYBOOK.md`'s substantive mode split and Runtime mechanics. Each brief carries `PROME/COMPLETION_SPEC.md`; launch preflight and authority remain in `PROME/CLAUDE.md`.


---

## Rotated banners (2026-10-30)
*Verbatim prior text of `PROME/BOOT.md` lines 6 and 8 before rotation #3 (crc32 3574064564); the rulings are carried at BOOT.md step 3b — history, not instruction.*

**Helm RETIRED (WQ-461, 2026-10-19).** No routine dashboard generation, presentation upkeep, hosted reads or publication. Historical BRIEF/HANDBOOK/HTML and change-feed records are frozen; use canonical owner records and the direct conversation. The boot book line, WALTER intake and decision checks remain active. Authority: `PROME/proposals/2026-10-19_wq461-helm-retired-RULED.md`.

**Decision Deck PAUSED BY WILL (WQ-460, 2026-10-19).** Deck-specific pickup, upkeep, builds and publication are suspended until explicit resume and reconciliation. Decisions continue in chat + WILL_QUEUE; WALTER intake still runs at step 3b. Scope: `PROME/proposals/2026-10-19_wq460-decision-deck-paused-RULED.md`. The hosted page has not been disabled; unseen taps remain UNKNOWN.
