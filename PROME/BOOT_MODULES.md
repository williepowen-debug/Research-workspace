# PROME/BOOT_MODULES.md — on-demand companions of `PROME/BOOT.md` (created 2026-10-16 16:1x ET, rotation M2–M5; plan + reads: `PROME/proposals/2026-10-16_boot-rotation-PLAN.md`)
**Owner:** PROME. **Not a boot read** — each section is opened at the trigger its BOOT.md pointer names. Every section below is the BOOT.md text byte-identical at the move (crc32 per section in the commit body); it is maintained HERE from now on, never re-copied into BOOT.md. READS.tsv mode `scoped`.

## Repeat boot
*Trigger: before reusing ANY earlier read in retained context, or on `--refresh`.*

**Repeat boot:** reuse only acknowledged full `USER.md`/`BOOT.md` reads in retained context. Add `--read-state /tmp/prome-reads-ID.json --context-id ID` to `boot_read.py` reads/continuations; after contiguous EOF use `--ack-read --sha256 <sha256>`, later `--reuse`. New sessions, compaction, handoff or uncertain retention require a new ID and full reads. Read and acknowledge every `pending_policy_reads` path using that state/context before reuse; USER acknowledgement clears no other path. Never reset state/ID to bypass recovery. A failed recovery checkpoint requires abandoning reuse for this context and plain full reads; this is caller-enforced across restarts. Other mismatches/files require full reads. Live state, checks, private rulings and capability/preflight stay fresh. Repeat via `boot_session.py --run-dir <original-run-dir> --refresh`: completed original required, no BOARD advancement; incomplete original stays UNKNOWN, never bypassed with a new directory. Refresh grants no additional per-boot spawn allowance. Repeat manual steps; missing tools remain PARTIAL.

## Deck unit taps (Change A)
*Trigger: the Decision Deck store returns ANY unconsumed document (BOOT.md step 3b).*

**A unit tap (Change A, DOCKET L660, 2026-10-09; the grouping rule above already keys it):** a CHOICE is written *"tap via Decision Deck <ts>: CHOICE <decision_id> = <label> — <text as stored> — <consequence as stored> <note>"* from the document's STORED `choice` fields (text AND consequence, brackets included), never the queue's or the card's current text (a later re-labelling cannot change what Will ruled); a PLAIN unit's APPROVE / DECLINE is written *"tap via Decision Deck <ts>: <verdict> <decision_id> — <meaning as stored in choice.text> <note>"* (the page shows that meaning beside the verb and stores it); a unit LATER is written *"… LATER <decision_id> <note>"* and leaves that unit UNRULED (OPEN); a document with NO `decision_id` on a row that now has units (a tap on a pre-Change-A build) is written to the row verbatim as Will's word but consumed as a ruling on NO unit — PROME asks him which unit it meant; a row holding several units stays OPEN while any unit is unruled and its state names each unit; when taps on DIFFERENT rows bear on the SAME position (e.g. WQ-357 and 302.TLT on the TLT 82P), PROME writes both verbatim and asks Will which governs before either is encoded; the owner desk's record (root rule #10) receives the label, not a paraphrase; `options_shown` + `build` say which set he saw. 

## Conditional modules
*Trigger: the need named in the first column (BOOT.md step 6 and the pointer line).*

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


## Trigger-keyed fleet memories
*Trigger: reviving a stale desk (spawn time) · hardening a desk's boot/closeout. Embed census: `memory/auto/INDEX_COLD_EMBEDDED.md`.*

**Reviving a stale desk (read at spawn time, not every boot):** procedure → `ORCHESTRAL_LAYER_DESIGN.md` § Revival-proxy v3 brief spec. At this trigger read `memory/auto/finding_revival_proxy_pattern.md` and `memory/auto/finding_revival_boot_doc_sweep.md` (the latter covers the full doc sweep after 30+ days stale).

**Domain-desk boot-protocol patterns (read when hardening a desk's boot/closeout, not every boot):** read the corresponding `memory/auto/` lessons: `finding_boot_protocol_live_event_override.md`, `finding_boot_predictions_scan.md`, `finding_boot_closeout_hardening_recipe.md`, `finding_boot_py_cadence_skip_pattern.md`. DAEDALUS owns the blueprint class.

