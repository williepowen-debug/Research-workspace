# PROME CLOSEOUT — conditional procedures
**Owner:** PROME · **Created 2026-09-12 (WQ-240, Will-directed).** ⛔ **NOT a boot read and NOT a routine read.** `PROME/CLOSEOUT.md` is the routine sequence; this file holds the procedures that run only when their trigger fires. Every section below is reached by an explicit pointer from there — **if nothing points here, it is dead text, not canon.**

**Why this file exists:** `CLOSEOUT.md` sat at ~95% of its read cap, so the routine sequence a session actually executes was buried in procedures most closeouts never run. The sizing decision owed at DOCKET L338 is **hot/cold split, not rotation** — rotation would have archived live procedure. Implementation record: `PROME/proposals/2026-09-12_wq240-closeout-simplification-RULED.md`.

---

## Byte-flow and rotation recipes (trigger: a state file at/over its line)

- **`STATUS.md` surgical:** stamp, work-queue table, decision-layer freshness. **Next Best Action is FROZEN:** pointer banner only; forward directives belong in SCRATCH. **Current state only (WQ-233, Will-approved 2026-09-11).** STATUS carries the scoped PROME queue, owner lanes, restrictions, live surfaces, the spine-audit date and completion-evidence notes — **not session accounts.** The session's account goes to its **existing** destinations, `PROME/HANDOFF.md` (continuity) and `memory/YYYY-MM-DD.md` (the day's log); **this rule adds no third recap.** **At closeout, update STATUS for what actually changed in current state:** add or amend a queue row when a PROME priority or follow-up starts, moves or completes — give it an actor, a trigger and a done-condition, and leave registered detail at its canonical record. **The queue is selected, not an exhaustive inventory:** a live obligation already carried by DOCKET, GATES, WILL_QUEUE, SCRATCH or an owner's artifact does not need a row here. **Byte flow:** `python3 PROME/tools/measure.py PROME/STATUS.md`; **≥24,412 B (75% of the 32,550 B budget) ⇒ move superseded current-state material verbatim into `PROME/archive/STATUS_HISTORY.md` until <22,785 B (70%)**; record it in the commit. Never trim history in place. Prior headline rotations → `PROME/archive/STATUS_HEADLINES_<range>.md` (frozen; do not append).

- **`ACTIVE_DECISIONS.md` surgical** if a decision moved. **Byte flow:** `python3 PROME/tools/measure.py PROME/ACTIVE_DECISIONS.md`; ≥24,412 B ⇒ rotate verbatim, crc32-verified round-trip to `PROME/archive/ACTIVE_DECISIONS_ROTATION_<date>.md` until <22,785 B; record in the commit. Order: whole terminal rows → header prior-stamp chain → snapshot-then-rewrite live rows (archive the full original row; rewrite current-state-only with dated pointer, NEVER clause-splice). **Standing guards never rotate:** manifest `guard-bytes retained: N`; grep dropped text for directive markers and disposition every hit. Rising N triggers guard-retirement review, discharge by ruling. Target ≤~2 KB per row; resolutions REPLACE pending language. **If found >100% of budget at ANY BOOT, script the check (rc-keyed, MEMORY pattern), without re-litigation.** Design: `PROME/proposals/2026-08-22_active-decisions-flow-rule-DESIGN.md`. **Every PROME rotation** (STATUS, WILL_QUEUE, HANDOFF, and GATES history when its redesign lands) uses verbatim blocks between markers and archive-header crc32. Recompute crc from archived bytes; the banner alone proves nothing. Header/`**Last reconciled:**` carries ONE stamp; prior stamps rotate.

- **Blind-reader verification:** every byte-flow rotation and HEARTBEAT re-base gets a fresh-context read-only Explore-class reader before commit. It starts with ONLY the rewritten surface and answers ground-truth questions covering changed state, at least one rotated-content question (follow the pointer), and one anchor-recovery walk; grade its answers. ⛔ **WITHHELD (Will 2026-09-26 20:16 ET, L511): the "Stop and budget" wording below was edited after the final independent read and is UNVERIFIED — do not rely on it; `PROME/CLAUDE.md` § Review budget governs.** **Stop and budget:** a rotation or re-base is one episode under `PROME/CLAUDE.md` § Session Process Controls → Review budget — WQ-165's early stop runs inside WQ-178's reads; at an early stop or at the limit, any unresolved defect that could materially change a decision or instruction is withheld per that bullet (pointer to source + last reliable version, or UNAVAILABLE), never shipped as live guidance; declare ⚠️ and unreviewed fixes as residue in the commit — except that any ⚠️ or unreviewed fix that could materially change a decision or instruction is withheld, whatever its grade. Basis/pointer-class: right figure missing basis/vintage/unit/perimeter or wrong pointer/item destination. Action-class: executed order listed live, dead calendar event, wrong position count, or wrong unit against a bar. Runner: `/coldread` step 4.

- **`HANDOFF.md` (Standard/Heavy):** concise entry: landed work, Will's decisions, decisions needed, risks, next pointer, rules held. Keep 3–5 live entries. Rotate to `PROME/archive/HANDOFF_<date>_<name>.md` with archive-header crc. HANDOFF's Archive line stays ONE pointer; `PROME/archive/HANDOFF_ARCHIVE_POINTERS_2026-08-28.md` is frozen, never append; `ls` is the archive index.

---

## Chunk 3 — Optional residuals (trigger-gated)

- **Doc retired/created** → update Boot Trust Stack (`SYSTEM.md`).
- **Canonical doc changed** → walk its Mirror-Map row (`SYSTEM.md` → Canonical → Mirrors) BEFORE commit; mechanized: `python3 scripts/consumer_check.py --mirror-map --old <OLD-TOKEN>`.
- **DOCKET row changed** → `firetime_check.py` on citing artifacts (DATE flag ⇒ full logic re-read).
- **Spine-audit stamp >7d** (STATUS header) → run `PROME/tools/spine_audit.workflow.js` or hand it to next boot in SCRATCH.
- **Autonomy change** → AUTONOMY.md log + propagate to `PROME/CLAUDE.md` Ask-First (the surface boot actually reads).
- **Named teams-mode spawns** → **release at closeout** per the two-tier model (Pre-closeout step 3 above; single home = `PROME/ORCHESTRATION_PLAYBOOK.md` §Two-tier) — never park warm across the boundary (`[[feedback_warm_parked_agent_collision]]`).
- **Sub-agents ran** → diff their outputs against PROME owner docs; promote unpropagated facts before commit (`[[feedback_subagent_propagation_gap]]`).
- **New external surface discovered** → `reference` auto-memory.

---

## Skip rules

- **Operator card:** part of SCRATCH's targeted update (WQ-240 — never a mandated full rewrite); `TODAY.md` is retired.
- **`AGENTS/<other>/` files:** owners own their state. Exceptions: root's four self-authorship carve-outs ①–④ (④ activation-gated; PROME-only Gate C custody is separate), plus Will-approved per-instance apply-on-behalf for named files, with authorization in the commit body. Follow root Git Protocol for the full scope, including mandatory self-authored packet and auto-memory commits.
- **Root `CLAUDE.md` / shared files** — flag to Will; Will-approval gates the change.

---

## Cross-session behavioral rules

- **Behavior-language over hash-pinning** in state files (hashes decay within 48h).
- **Verify state before propagating** — ground truth, not prior surface text.
- **Chunked updates** with checkpoints, not 4-5-file batches.
- **`trash` over `rm`.**

---

---

## Closeout-class fleet memories (fleet-memory embeds — migrated 2026-07-31, Phase-2 restructure)
*Embedded hooks from `memory/auto/`; index pointers live in `memory/auto/INDEX_COLD.md`.*

- finding_closeout_as_writeback_tail — "Codify session closeout as the write-back tail of the auto-loaded CLAUDE.md SPAWN PROTOCOL, not a standalone doc; auto-load is the decisive factor" `[[finding_closeout_as_writeback_tail]]`
- feedback_intra_day_closeout_discipline — Run WALTER closeout (spawn-protocol steps 12-15) at every session end, not just end-of-day; multi-session-days must honor intermediate closeout to prevent STATUS-staleness gap `[[feedback_intra_day_closeout_discipline]]`
- feedback_handoff_cadence — Will prefers clean handoffs at natural breakpoints over riding a long session into degradation `[[feedback_handoff_cadence]]`
- finding_state_token_sweep_all_surfaces — "When a gate/decision state flips (e.g. FIRED-UNEXECUTED → RESOLVED), sweep the state-token across ALL surfaces — live ledgers (VX/KB.tsv) and live templates/setups too, not just STATUS/SCRATCH; scope the verification grep from repo root." `[[finding_state_token_sweep_all_surfaces]]`
- finding_completion_stamp_skip_reads_as_current — "a file whose NAME promises currency (LAST_COMPLETION) that SKIPS a closeout doesn't read as stale — it reads as current and wrong; detect by mtime vs STATUS.md" `[[finding_completion_stamp_skip_reads_as_current]]`
