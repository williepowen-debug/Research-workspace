# PROME CLOSEOUT

**Created:** 2026-05-18 · **Updated:** 2026-09-11 (Will-directed simplification: remove historical explanations; retain procedures, thresholds, exceptions, section names and runner interfaces). Amendment history: `git log -p -- PROME/CLOSEOUT.md`; pre-simplification text: `git show 4a0757370074f1a5ed48353894298b465f842047:PROME/CLOSEOUT.md` (on-demand).
**Owner:** Prome
**Commit-pipeline approval/review:** `plans/2026-09-09_boot-hardening.md` (on-demand).
**Purpose:** Repeatable session-end procedure. Run before `/clear`, `/new`, or session handoff.

> Companion to `PROME/BOOT.md` (session start) + `PROME/CLAUDE.md` (bootstrap). **Git protocol canon = root `CLAUDE.md` (auto-injected; not restated here).**

---

## When to run
*(Execution wrapper: the `/closeout` skill — `PROME/.claude/skills/closeout/SKILL.md` — runs this file's order with the exact commands; this file stays the canon for rules and tiers.)*

Before `/clear` or `/new` · before stepping away from a long session · after any session that produced state changes worth persisting. Skip for casual one-off exchanges with no artifacts.

---

## Pre-closeout (~1 min)

1. `git status --short` — review what changed.
2. **Foreign uncommitted work does NOT block closeout:** commit only your authored scope using exact pathspecs and safe-push. Include daily memory and self-authored auto-memory under the root grants; never sweep the tree. Non-ff recovery requires root step 3's dirty-path overlap check before autostash. If `AGENTS/PROME/` reappears, migrate its contents to `PROME/inbox/` and flag the sender (BOOT step 6).
3. **Orchestrated-desk release (ANY tier):** tell each named desk spawned this session to run its own closeout; verify idle + last delivery committed (desk `(orch)` commits). Desk-dir residue is in-flight; never sweep it on respawn. Log final touch in `PROME/state/ORCH_LOG.tsv`. Single home: `PROME/ORCHESTRATION_PLAYBOOK.md` §Two-tier.
4. List this session's artifacts; check transcript hygiene (preserve durable results in files, not restated dumps); pick the tier:

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-day restart; back within the hour | SCRATCH addendum (3-5 lines) | Optional 1-line checkpoint |
| **Light** | Short session paused for hours; 1-2 artifacts | SCRATCH full rewrite + STATUS surgical | Optional |
| **Standard** *(default)* | End-of-thread / end-of-day | Chunk 1 + Chunk 2 (+ auto-memory if earned) + Chunk 4 + auto-push | Yes |
| **Heavy** | Pattern-discovery session | Standard + design docs + Chunk 3 full sweep | Yes |

End-of-day runs at least Standard. Standard+ includes the MANDATORY dashboard and THE HELM symmetry rows, plus the Decision Deck row. Chunk 3 triggers apply at ANY tier. **Bounce:** append 3–5 SCRATCH lines (what happened, pending, next entry point); optional wrapper checkpoint from repo root with message-file subject `PROME: bounce checkpoint` and exact path `PROME/SCRATCH.md`.

---

> **⚡ Mechanical tail in one shot — RUN IT LAST**, after every state write and after the two Will-facing pages regenerate, immediately before the commit: `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout`. An early run is optional preflight, not the final verdict. rc=1 means BLOCKING failures. The script also prints reminders for manual root steps 1c (consumer check) and 1d (memory index); it does not replace judgment writes. New mechanical checks go in the SCRIPT, not this prose.

## Boot↔Closeout symmetry

Closeout is the **write-back tail** of boot (`[[finding_closeout_as_writeback_tail]]`). `check_symmetry()` checks BOOT's case-sensitive `Read` directives against this section: register each mandatory boot-read surface here as paired-write or intentionally one-way.

| Surface | Boot (read) | Closeout (write-back) |
|---|---|---|
| `HANDOFF.md` | boot: continuity read | Chunk 1 — append/rotate concise continuity entry when session affects future Prome state |
| `SCRATCH.md` | boot: hot-state + operator card | Chunk 1 — full rewrite (incl. operator card: date/catalysts/near-gates). **Format contract (7/11):** the cautions "Pending Will:" line is parsed by the Fleet-Ops dashboard — keep the exact label `Pending Will:` and `·`-separated items, one line |
| `ACTIVE_DECISIONS.md` | boot: decisions read | Chunk 1 — surgical if a decision moved |
| `PROME/GATES.tsv` | boot: fire-ledger gate (step 3) | Chunk 1 — surgical: register any action-gate approved this session; flip state on any landed verdict; refresh `last_checked` on rows touched. **A row must never leave a session `FIRED-UNEXECUTED` without an escalation note** |
| `STATUS.md` | boot: health/queue read | Chunk 1 — surgical |
| `HEARTBEAT.md` | boot: market-data / regime gate (step 5) | Update after a regime-level change or >48h stale (market week). Byte flow: 32,550 B budget, split/rotate ≥75%, stop <70% (`prome_gate` meters it). Re-base with a hot/cold split; history → `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_*`. Commit PROME-standard, explicitly pathed. |
| `memory/YYYY-MM-DD.md` | on-demand | Chunk 2 — create/append |
| `PROME/DOCKET.tsv` | boot: fire-time gate input (step 5) | Chunk 1 — paired with the operator card: any catalyst date that moved/resolved updates its DOCKET row (canonical; SCRATCH/HEARTBEAT are views) |
| `PROME/WILL_QUEUE.md` | boot: step 3b Decision Deck pickup (taps → rows) + the WALTER §WILL_NEEDS feed (WQ-206) | Chunk 1 — paired: every ruling taken this session (tap or word) written to its row verbatim with the stamp; new asks registered BEFORE they are presented; DONE rows ≥7d rolled to `PROME/archive/WILL_QUEUE_ROWS_<date>_rolloff.md`; then `willq_view.py --write PROME/SCRATCH.md` regenerates the Pending-Will block and the Decision Deck is republished (its own row below) |
| **WQ LEDGER** (`PROME/registry/WQ_LEDGER.tsv` + `.crc` seal; `PROME/tools/wq_ledger.py`; WQ-203) | not a boot read — the deck's Decided tab reads it programmatically | After the WILL_QUEUE paired write and before deck regeneration: `python3 PROME/tools/wq_ledger.py sync` then `python3 PROME/tools/wq_ledger.py check` (rc 0 required). Sync appends changed rows as REGISTERED · RULED · DECLINED · CLOSED · UPDATED; a second unchanged sync appends nothing. **Read the specific failure before acting:** `SEAL BROKEN` ⇒ sync refuses; restore committed truth with `git checkout -- PROME/registry/WQ_LEDGER.tsv PROME/registry/WQ_LEDGER.crc`, re-run sync, flag tamper. SCHEMA/VOCABULARY (`event not in vocabulary`, `at does not parse`, `written_at goes backwards`) ⇒ fix the cause, do not restore merely to hide it. `duplicate event — identical payload` ⇒ investigate the repeated write; distinct same-day changes are valid. Never hand-edit or rotate the ledger; corrections append UPDATED events. |
| **Fleet-Ops dashboard** | not a boot read — Will's comprehension surface | **Standard+ mandatory, AFTER the last state write:** `python3 PROME/tools/fleet_dashboard.py -o <scratchpad>/fleet_dashboard.html` → republish via Artifact **to the recorded URL** in the script header (`url=`). `<scratchpad>` is the session scratch directory or another writable temp directory. |
| **THE HELM** (`will_handbook.py` + `PROME/HANDBOOK.md` + `PROME/BRIEF.md`) | not a boot read — Will's handbook/briefing page | **Standard+ mandatory, AFTER the last state write:** ① if the picture changed, rewrite BRIEF narrative (STORY: one plain-language paragraph, every claim dated; refresh `## WRITTEN`); otherwise preserve its age ② refresh HANDBOOK §Top priorities if changed; manual sections change only with a convention ③ ALWAYS run `python3 PROME/tools/will_handbook.py -o <scratchpad>/handbook.html` → republish via Artifact to the recorded header URL (favicon 📖). This run owns the change-feed baseline (`write=True` by default). `will_brief.py` is a parser/state library; never run it as a page. |
| **DECISION DECK** (`PROME/tools/decision_deck.py` + `PROME/registry/WQ_EXPLAINERS.tsv`; WQ-202, Will 2026-09-10) | not a boot read — Will's decision surface (its `rulings` store IS a boot read: BOOT.md step 3b) | **Standard+ closeouts, MANDATORY, AFTER the last WILL_QUEUE/DOCKET/ACTIVE_DECISIONS write:** ① every OPEN queue row has a `WQ_EXPLAINERS.tsv` line (write it at registration; a missing one renders "explainer owed") ② `python3 PROME/tools/decision_deck.py --selftest` rc 0, then `python3 PROME/tools/decision_deck.py` → republish `PROME/artifacts/decision_deck.html` via Artifact to `DECK_URL` (in `will_handbook.py`; favicon ⚖️; capabilities carried forward) ③ never share the artifact — privacy is the tap's authentication |
| ~~**Will's briefing page**~~ **RETIRED** | — | Folded into THE HELM; never republish the retired standalone page. |

**Intentionally one-way (no closeout write-back, by design):**
- `PROME/CLOSEOUT.md` — procedure reference; read before closeout, maintained when the procedure changes, not rewritten every session.
- `FLEET_SCAN.md` — superseded historical snapshot; no refresh (fleet state = `ROSTER.md` + DAEDALUS `FLEET_MAP.tsv`).
- COMM mailbox / inbox / agent-outbox scans — ACKed/routed *inline during the session*, never deferred to closeout.
- OPEN-predictions resolution / forward-catalyst firing — domain-agent-owned (NEXUS/ORACLE/LABOR). PROME's only forward-state write-back is the operator-card catalyst list in SCRATCH.

---

## Prome Write-Back Contract *(File-ownership reference merged in, 8/9)*

Update only the owner doc whose state actually changed:

| If this changed | Write back to | Rule |
|---|---|---|
| Next-session state + operator card | `PROME/SCRATCH.md` | Full rewrite (Standard/Heavy); Bounce appends 3-5 lines |
| Cross-runtime continuity / Will's decisions | `PROME/HANDOFF.md` | Concise top entry only if future Prome needs it; keep latest 3-5, archive the rest |
| Non-terminal decision state | `PROME/ACTIVE_DECISIONS.md` | Surgical row; if state unknown, mark `DEFERRED`/reconcile, never infer execution |
| Action-gate approved / fired / resolved | `PROME/GATES.tsv` | Register the session it's approved; resolve the session the verdict lands (`[[finding_fired_gate_needs_owner_independent_ledger]]`) |
| **Decision DEFERRED this session** | `PROME/DOCKET.tsv` | **Register a dated row at creation** (deferral class, reconsider-by date) — a deferral without a ledger row has no read-path (the 46-day-limbo class; governance batch 8/9) |
| Agent/system health or work queue | `PROME/STATUS.md` | Surgical; no market narrative (that's SCRATCH/HEARTBEAT) |
| Regime / thresholds / near gates | `HEARTBEAT.md` | Commit PROME-standard, explicitly pathed; root-doc HEARTBEAT lines stay Will-gated. |
| Forward catalyst date moved / resolved | `PROME/DOCKET.tsv` | Update the row **and run `scripts/firetime_check.py` on citing artifacts** — DATE flag ⇒ full logic re-read, never find-replace |
| Daily activity | `memory/YYYY-MM-DD.md` | Append durable session log; **commit at closeout** (outside `PROME/` — Chunk 4 recipe) |
| Durable insight / lesson | auto-memory (`memory/auto/`) | Promote sparingly; index row in `MEMORY.md`; **self-commit mandatory** (root carve-out ③, step 1d) |
| Boot sequence / conditional modules | `PROME/BOOT.md` | Only if they changed |
| Architecture / Boot Trust Stack / doc ownership | `PROME/SYSTEM.md` | Only if a file was retired/created or ownership moved (Chunk-3 trigger) |
| Autonomy grant/revoke | `PROME/AUTONOMY.md` **+ `PROME/CLAUDE.md` Ask-First** | Change-log alone never reaches the next boot — propagate to the auto-loaded surface |
| Prototype learnings | `PROME/ORCHESTRAL_LAYER_DESIGN.md` or SCRATCH v_next | Pick one home, not both |
| `PROME/FLEET_SCAN.md` | — | Don't touch (superseded snapshot) |
| Root `CLAUDE.md`, other shared/root docs | — | Flag to Will; never auto-edit. HEARTBEAT is the exception above. |

**Default:** if no owner state changed, do not write back — state bloat is worse than a quiet closeout.

**Stamp canon:** an `Updated:` stamp names what the update covers. Material section additions bump it. A partially synced peer-facing surface carries a mixed-vintage banner naming which sections are current.

---

## Chunk 1 — State files (Light/Standard/Heavy; Bounce = SCRATCH addendum only)

- **`GATES.tsv` + `DOCKET.tsv` surgical, FIRST:** before editing, enumerate every gate/catalyst touched this session; each gets a row edit or a stated no-op. Register approved action-gates, flip landed verdicts, never leave `FIRED-UNEXECUTED` without escalation. Update moved/resolved DOCKET dates. Then regenerate the view: `cd "$(git rev-parse --show-toplevel)" && python3 scripts/docket_view.py --write PROME/SCRATCH.md`. It writes ONLY between `<!-- DOCKET-VIEW BEGIN/END -->`; **rc 2 ⇒ fix DOCKET or markers, never bypass**. After END, the hand line is editorial only (★ items; no dates already in the block). The gate's `--check` detects drift in remaining prose. See the symmetry-table rows for the paired writes.
- **`SCRATCH.md` full rewrite:** what happened · git state in behavior-language (never hashes — they decay) · next-session entry point · cautions.
- **`STATUS.md` surgical:** stamp, work-queue table, decision-layer freshness. **Next Best Action is FROZEN:** pointer banner only; forward directives belong in SCRATCH. **Byte flow:** measure with `python3 PROME/tools/measure.py PROME/STATUS.md`; ≥24,412 B (75% of the 32,550 B budget) ⇒ rotate oldest session headlines, then oldest spine-audit *Prior:* records, verbatim with crc32-verified round-trip into `PROME/archive/STATUS_HEADLINES_<range>.md` until <22,785 B (70%); record in the commit. Never trim history in place. **Headlines:** pointer-weight outcomes, counts, ruling names and narrative pointers; target ≤~1.5 KB. Narrative belongs in SCRATCH/HANDOFF, not a third STATUS copy.
- **`ACTIVE_DECISIONS.md` surgical** if a decision moved. **Byte flow:** `python3 PROME/tools/measure.py PROME/ACTIVE_DECISIONS.md`; ≥24,412 B ⇒ rotate verbatim, crc32-verified round-trip to `PROME/archive/ACTIVE_DECISIONS_ROTATION_<date>.md` until <22,785 B; record in the commit. Order: whole terminal rows → header prior-stamp chain → snapshot-then-rewrite live rows (archive the full original row; rewrite current-state-only with dated pointer, NEVER clause-splice). **Standing guards never rotate:** manifest `guard-bytes retained: N`; grep dropped text for directive markers and disposition every hit. Rising N triggers guard-retirement review, discharge by ruling. Target ≤~2 KB per row; resolutions REPLACE pending language. **If found >100% of budget at ANY BOOT, script the check (rc-keyed, MEMORY pattern), without re-litigation.** Design: `PROME/proposals/2026-08-22_active-decisions-flow-rule-DESIGN.md`. **Every PROME rotation** (STATUS, WILL_QUEUE, HANDOFF, and GATES history when its redesign lands) uses verbatim blocks between markers and archive-header crc32. Recompute crc from archived bytes; the banner alone proves nothing. Header/`**Last reconciled:**` carries ONE stamp; prior stamps rotate.
- **Blind-reader verification:** every byte-flow rotation and HEARTBEAT re-base gets a fresh-context read-only Explore-class reader before commit. It starts with ONLY the rewritten surface and answers ground-truth questions covering changed state, at least one rotated-content question (follow the pointer), and one anchor-recovery walk; grade its answers. **Stop rule (WQ-165):** re-run until ❌=0 OR two consecutive reads return only basis/pointer-class ❌ and no action-class ❌; then fix the last read's ❌, declare them and every ⚠️ as residue in the commit, and ship. Basis/pointer-class: right figure missing basis/vintage/unit/perimeter or wrong pointer/item destination. Action-class: executed order listed live, dead calendar event, wrong position count, or wrong unit against a bar. Runner: `/coldread` step 4.
- **`HANDOFF.md` (Standard/Heavy):** concise entry: landed work, Will's decisions, decisions needed, risks, next pointer, rules held. Keep 3–5 live entries. Rotate to `PROME/archive/HANDOFF_<date>_<name>.md` with archive-header crc. HANDOFF's Archive line stays ONE pointer; `PROME/archive/HANDOFF_ARCHIVE_POINTERS_2026-08-28.md` is frozen, never append; `ls` is the archive index.
- **Doc-ownership separation:** SCRATCH = narrative + entry point · STATUS = state tables only · HANDOFF = concise continuity. If two restate a fact, keep it in SCRATCH and cross-reference.

## Chunk 2 — Memory (Standard/Heavy)

- **`memory/YYYY-MM-DD.md`:** bullet log of the day (append if it exists).
- **Auto-memory (`memory/auto/`), trigger-gated any Standard+:** save only surprising/non-obvious lessons, pattern validations/invalidations, things not derivable from code — never activity recaps or derivable conventions. Frontmatter + **Why/How-to-apply** for feedback/project types; one-line `MEMORY.md` index row (append, never rewrite). No lesson → skip; memory bloat hurts more than absence.

## Chunk 3 — Optional residuals (trigger-gated)

- **Doc retired/created** → update Boot Trust Stack (`SYSTEM.md`).
- **Canonical doc changed** → walk its Mirror-Map row (`SYSTEM.md` → Canonical → Mirrors) BEFORE commit; mechanized: `python3 scripts/consumer_check.py --mirror-map --old <OLD-TOKEN>`.
- **DOCKET row changed** → `firetime_check.py` on citing artifacts (DATE flag ⇒ full logic re-read).
- **Spine-audit stamp >7d** (STATUS header) → run `PROME/tools/spine_audit.workflow.js` or hand it to next boot in SCRATCH.
- **Autonomy change** → AUTONOMY.md log + propagate to `PROME/CLAUDE.md` Ask-First (the surface boot actually reads).
- **Named teams-mode spawns** → **release at closeout** per the two-tier model (Pre-closeout step 3 above; single home = `PROME/ORCHESTRATION_PLAYBOOK.md` §Two-tier) — never park warm across the boundary (`[[feedback_warm_parked_agent_collision]]`).
- **Sub-agents ran** → diff their outputs against PROME owner docs; promote unpropagated facts before commit (`[[feedback_subagent_propagation_gap]]`).
- **New external surface discovered** → `reference` auto-memory.

## Chunk 4 — Git + report (Standard/Heavy; Light optional)

**PROME commit form:** every commit uses `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/commit_check.py commit --stage --push -F <msgfile> -- <exact paths>`. The wrapper checks intent, refuses no-change, stages literal file paths, verifies committed paths, then pushes only on success; directories and symlinks are refused. For multiple batches, omit `--push` until the final successful batch. On failure inspect state; never reset, sweep or amend. **Message text:** use the Write tool or a quoted heredoc (`cat > <file> <<'EOF'`) to a file; never inline prose in Bash arguments, including packet/row text quoting git commands (the PreToolUse guard can interpret it as a command). **Include authored Chunk 2 outputs in the batch:** first daily log may be untracked (`--stage` adds it); touched `memory/auto/<slug>.md` travels with its MEMORY index row, gated by `python3 scripts/memory_index_check.py --strict --slug <slug>` (root 1d). **Renames:** `git mv` first; name BOTH old and new paths. The wrapper skips a vanished already-staged source at staging and records the rename in the pathspec commit.
**Subject drafting target ≤70 chars:** measure (`head -1 <msgfile> | wc -c`) before the wrapper; ≥101 means STOP and rewrite. The wrapper refuses subjects >100 chars. Plain `git commit` bypasses its intent manifest and post-commit verification; the wrapper is the only PROME commit form.

**Root session-end steps 1b-1e** (root `CLAUDE.md` owns the full text):
- **1b orphan check:** `bash scripts/orphan_check.sh PROME`; commit self-authored packets under carve-out ①. Its path-based `[not yours]` label does not override mandatory self-authored auto-memory commits under ③.
- **1c consumer check** (if a published number was superseded): `python3 scripts/consumer_check.py --agent PROME --old <old> --new <new>` → packet each 🔴 owner, never edit their files.
- **1d memory-index check** (if auto-memory written): `python3 scripts/memory_index_check.py --strict --slug <slug>` — the `--slug` form, never bare `--strict`.
- **1d-bis hot-index flow (PROME-only):** if `check_memory_length.sh` reads ≥75% of bytes, demote (never delete) settled/predictable-trigger MEMORY rows to `INDEX_COLD.md` until <70%, in the same sitting. Prove slug conservation in the commit (union count before == after; the 8/12 pass is the template). Domain agents only flag.
- **1e claim check:** `python3 scripts/claim_check.py --check weekday PROME/DOCKET.tsv PROME/GATES.tsv PROME/WILL_QUEUE.md PROME/STATUS.md` (root 1e). No-args checks changed files/all classes: useful as an extra, never a substitute. **rc=1 ⇒ LOOK, never find-replace.** Limits: cannot distinguish mention from use; cross-repo hashes read `missing`; placeholders flag.

- **1f ARGUS closeout audit (Standard/Heavy; WQ-226; trial DOCKET L333, graded 9/19):** after Chunks 1–3 writes and **BEFORE committing**, run `python3 PROME/tools/argus_scope.py`. It reports committed AND pending changes against `PROME/state/argus_baseline.json`, classified by `PROME/state/AUDIT_PERIMETER.tsv` as OWNED · SHARED · UNATTRIBUTED; do not infer ownership from subjects or filenames. **UNATTRIBUTED >0 ⇒ add the required manifest row.** Scope rc 0 ⇒ spawn read-only agent type `argus` (Opus, `.claude/agents/argus.md`) with the scope; rc 3 (<3 paths) ⇒ skip and report it; rc 2 ⇒ audit everything since HEAD~50 and report the fallback. Under the WQ-178 read budget, consume its five-field ledger: fix ❌ only, declare every ⚠️ in the closeout commit body. Append a RUN-LOG row to `PROME/argus/MEMORY.md`; put declined flag classes in CALIBRATION. This is ARGUS's one whole-file read; PROME writes it, ARGUS never does. Check `python3 scripts/read_cap_check.py PROME/argus/MEMORY.md`; **roll at ≥24,412 B.** ⚠️ Do NOT roll off that tool's `% of cap` — it divides by the 54,250 B token ceiling, not by the 32,550 B read budget, so a "≥75%" read off that line fires 8,138 B PAST the cap (ARGUS P1, 2026-09-11). ARGUS is the allowed result read, not an additional one. **AFTER the closeout commit:** `python3 PROME/tools/argus_scope.py --record-baseline HEAD`; commit the baseline file with the next commit. Trial metric: defects caught BEFORE vs AFTER commit (baseline 0 vs 7). Trial/approval record: `PROME/reports/2026-09-11_sam-subagent-system-assessment.md` §4; scope contract: `PROME/proposals/2026-09-11_L336-argus-redesign-ACCEPTANCE-CONDITIONS.md`.

```bash
cd "$(git rev-parse --show-toplevel)"  # all git operations from repo root
git status --short
git status -- PROME/ memory/  # no dangling deletions, forgotten files or out-of-scope staging
# Exact reviewed paths, including authored memory; BOTH paths for git-mv renames:
python3 PROME/tools/commit_check.py commit --stage --push -F <msgfile> -- <exact paths>
git status --short --branch  # clean tree, ahead 0 / behind 0 before reporting synced
```

**Auto-push:** `safe-push.sh` is the ff-gated closeout tail and sweeps the push-train. **Verify the exact receipt:** `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` A bare `Pushed.`, log tail, or unexpected `Nothing to push` is not confirmation. Non-ff is routine: follow root Git Protocol session-end step 3 IN FULL. Compare incoming paths against dirty paths BEFORE any `--autostash` (whole-tree); overlap ⇒ stop and flag. Use root step 3's escalation test. Message first line: `PROME: <short one-liner>`; exact paths follow `--`. Root ledger nudge 1c-bis is N/A: no `PROME/workbook/LEDGER_GLOB`.

**Session summary to Will:** what landed (1-2 lines; commit hashes belong HERE, never in state files — they decay) · what's owed at next boot · open `PROME/WILL_QUEUE.md` rows by number · the push receipt line verbatim · next-session entry point (points at SCRATCH).

---

## Skip rules

- **Operator card:** part of SCRATCH's rewrite; `TODAY.md` is retired.
- **`AGENTS/<other>/` files:** owners own their state. Exceptions: root's four self-authorship carve-outs ①–④ (④ activation-gated; PROME-only Gate C custody is separate), plus Will-approved per-instance apply-on-behalf for named files, with authorization in the commit body. Follow root Git Protocol for the full scope, including mandatory self-authored packet and auto-memory commits.
- **Root `CLAUDE.md` / shared files** — flag to Will; Will-approval gates the change.

## Cross-session behavioral rules

- **Behavior-language over hash-pinning** in state files (hashes decay within 48h).
- **Verify state before propagating** — ground truth, not prior surface text.
- **Chunked updates** with checkpoints, not 4-5-file batches.
- **`trash` over `rm`.**

---

## Closeout-class fleet memories (fleet-memory embeds — migrated 2026-07-31, Phase-2 restructure)
*Embedded hooks from `memory/auto/`; index pointers live in `memory/auto/INDEX_COLD.md`.*

- finding_closeout_as_writeback_tail — "Codify session closeout as the write-back tail of the auto-loaded CLAUDE.md SPAWN PROTOCOL, not a standalone doc; auto-load is the decisive factor" `[[finding_closeout_as_writeback_tail]]`
- feedback_intra_day_closeout_discipline — Run WALTER closeout (spawn-protocol steps 12-15) at every session end, not just end-of-day; multi-session-days must honor intermediate closeout to prevent STATUS-staleness gap `[[feedback_intra_day_closeout_discipline]]`
- feedback_handoff_cadence — Will prefers clean handoffs at natural breakpoints over riding a long session into degradation `[[feedback_handoff_cadence]]`
- finding_state_token_sweep_all_surfaces — "When a gate/decision state flips (e.g. FIRED-UNEXECUTED → RESOLVED), sweep the state-token across ALL surfaces — live ledgers (VX/KB.tsv) and live templates/setups too, not just STATUS/SCRATCH; scope the verification grep from repo root." `[[finding_state_token_sweep_all_surfaces]]`
- finding_completion_stamp_skip_reads_as_current — "a file whose NAME promises currency (LAST_COMPLETION) that SKIPS a closeout doesn't read as stale — it reads as current and wrong; detect by mtime vs STATUS.md" `[[finding_completion_stamp_skip_reads_as_current]]`
