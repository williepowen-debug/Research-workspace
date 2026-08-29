# PROME CLOSEOUT

**Created:** 2026-05-18 · **Updated:** 2026-08-22 (stamp bump, audit #10 — n=2 of the ride-under class this stamp's own history records: covers the 8/21 HELM/brief-retirement row + the 8/22 ACTIVE_DECISIONS flow rule + blind-reader rule, each dated inline at site). Prior: 2026-08-16 S4 (stamp re-based, DAEDALUS sweep-1 item 9 — the 8/9 stamp's "zero rule-content changes except as named" had ridden over FOUR later material rule-adds: 8/12 hot-index flow rule [step 1d-bis] · 8/16 STATUS byte flow rule [Chunk 1] · 8/16 S4 STATUS headline convention [Chunk 1] · 8/16 S4 will_brief mandatory rebuild row [Write-Back table, Will-ruled]. Each is dated inline at its own site; this stamp now covers them.) Prior: 2026-08-09 (**T2-a spine prune, Will-approved batch: 287→~160 lines.** Scope manifest: Chunk-4 git prose demoted to root-canon pointers [root `CLAUDE.md` is auto-injected — the full protocol is always in context]; File-ownership table MERGED into the Write-Back Contract; claim-check narrative compressed; mention-registry block retired [`check_symmetry()` v1 anchors on `Read`-directive lines now — one `TODAY.md` one-way row survives because it rides BOOT step 2's Read line]; auto-push rationale de-triplicated. ADDED: stamp canon + deferred-decision write-back row [governance batch]. Zero rule-content changes except as named. Prior stamp history → `git log` on this file.)
**Owner:** Prome
**Purpose:** Repeatable session-end procedure. Run before `/clear`, `/new`, or session handoff.

> Companion to `PROME/BOOT.md` (session start) + `PROME/CLAUDE.md` (bootstrap). **Git protocol canon = root `CLAUDE.md` (auto-injected; not restated here).**

---

## When to run

Before `/clear` or `/new` · before stepping away from a long session · after any session that produced state changes worth persisting. Skip for casual one-off exchanges with no artifacts.

---

## Pre-closeout (~1 min)

1. `git status --short` — review what changed.
2. **Foreign uncommitted work does NOT block closeout** — pathspec commits + `safe-push.sh` never touch another agent's tree. The real check: you are about to commit only your own `PROME/` scope (+ the standard closeout set: daily `memory/YYYY-MM-DD.md` and self-authored `memory/auto/` files — carve-out ③ makes the latter MANDATORY; recipes in Chunk 4). If `AGENTS/PROME/` reappears, that's a sender-routing regression: migrate contents to `PROME/inbox/`, flag the sender (BOOT step 6).
3. **Orchestrated-desk release (2026-08-23, Will-ruled two-tier model — ANY tier, including Bounce; PAT-112 hook):** if this session spawned named subagent desks, send each live one the final **"run your closeout per your own protocol"** ping, then verify **idle + last delivery committed** (`git log` the desk's `(orch)` commits; desk-dir residue = in-flight, integrate-never-sweep on respawn). Log the final touch in `PROME/state/ORCH_LOG.tsv`. A desk released without its own closeout leaves a stale header over its newest content — the exact PAT-112 failure. Single home: `PROME/ORCHESTRATION_PLAYBOOK.md` §Two-tier.
4. List this session's artifacts; check transcript hygiene (preserve durable results in files, not restated dumps); pick the tier:

| Tier | When | Touches | Commit? |
|---|---|---|---|
| **Bounce** | Mid-day restart; back within the hour | SCRATCH addendum (3-5 lines) | Optional 1-line checkpoint |
| **Light** | Short session paused for hours; 1-2 artifacts | SCRATCH full rewrite + STATUS surgical | Optional |
| **Standard** *(default)* | End-of-thread / end-of-day | Chunk 1 + Chunk 2 (+ auto-memory if earned) + Chunk 4 + auto-push | Yes |
| **Heavy** | Pattern-discovery session | Standard + design docs + Chunk 3 full sweep | Yes |

End-of-day always runs at least Standard. **Chunk 3 is trigger-gated at ANY tier** — a fired trigger (spawned-agent release, autonomy change, …) runs its step even on a lighter closeout. **Bounce procedure:** append 3-5 lines to `PROME/SCRATCH.md` (what happened / what's pending / next entry point); recommended checkpoint commit from repo root: `git commit -m "PROME: bounce checkpoint" -- PROME/SCRATCH.md`.

---

> **⚡ Mechanical tail in one shot (T2-b):** `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout` — the scripted checks + printed reminders for the two MANUAL root steps (1c consumer_check, 1d memory_index_check). rc=1 only on BLOCKING failures. The judgment writes below are not replaced. **New mechanical checks go in the SCRIPT, not this prose.**

## Boot↔Closeout symmetry

Closeout is the **write-back tail** of boot (`[[finding_closeout_as_writeback_tail]]`): what BOOT reads, this writes back; a boot-read surface with no closeout write goes stale silently. *(Machine-checked every boot: `check_symmetry()` anchors on BOOT's `Read`-directive lines since 8/9 — a mandatory boot read carries the word `Read` on its BOOT.md line and must appear in this section.)*

| Surface | Boot (read) | Closeout (write-back) |
|---|---|---|
| `HANDOFF.md` | boot: continuity read | Chunk 1 — append/rotate concise continuity entry when session affects future Prome state |
| `SCRATCH.md` | boot: hot-state + operator card | Chunk 1 — full rewrite (incl. operator card: date/catalysts/near-gates). **Format contract (7/11):** the cautions "Pending Will:" line is parsed by the Fleet-Ops dashboard — keep the exact label `Pending Will:` and `·`-separated items, one line |
| `ACTIVE_DECISIONS.md` | boot: decisions read | Chunk 1 — surgical if a decision moved |
| `PROME/GATES.tsv` | boot: fire-ledger gate (step 3) | Chunk 1 — surgical: register any action-gate approved this session; flip state on any landed verdict; refresh `last_checked` on rows touched. **A row must never leave a session `FIRED-UNEXECUTED` without an escalation note** |
| `STATUS.md` | boot: health/queue read | Chunk 1 — surgical |
| `HEARTBEAT.md` | boot: market-data / regime gate (step 5) | per Write-Back Contract — update after a regime-level change or >48h stale (market week); **byte flow rule = the read-cap budget (32,550 B; split/rotate ≥75%, stop <70% — `prome_gate` meters it since 8/29)**, remedy = re-base with hot/cold split, history → `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_*`; **commit PROME-standard since 2026-08-23** (Will "free it"; record `PROME/proposals/2026-08-23_heartbeat-gate-RULED.md` — this row carried "Will-gated" 4 days past the grant, n=3 of the ungating-leaves-mirror-behind class root canon records; synced 8/27 closeout) |
| `memory/YYYY-MM-DD.md` | on-demand | Chunk 2 — create/append |
| `PROME/DOCKET.tsv` | boot: fire-time gate input (step 5) | Chunk 1 — paired with the operator card: any catalyst date that moved/resolved updates its DOCKET row (canonical; SCRATCH/HEARTBEAT are views) |
| **Fleet-Ops dashboard** | not a boot read — Will's comprehension surface | **Standard+ closeouts:** regenerate `python3 PROME/tools/fleet_dashboard.py -o <scratchpad>/fleet_dashboard.html` → republish via Artifact **to the recorded URL** (in the script header — pass `url=`, else it orphans Will's tab) |
| **THE HELM** *(renamed from Operator Handbook, Will's word 8/21)* (`will_handbook.py` + `PROME/HANDBOOK.md` + `PROME/BRIEF.md`) | not a boot read — Will's ONE page (Will-requested 2026-08-21; absorbed the Desk brief as a tab same day, standalone RETIRED on Will's word) | **Standard+ closeouts, MANDATORY:** ① if the picture changed, REWRITE `PROME/BRIEF.md` narrative (STORY = one plain-language paragraph, every claim dated; refresh `## WRITTEN`) — unchanged = leave it, the tab shows its age ② refresh `PROME/HANDBOOK.md` §Top priorities if the curated list changed (manual sections change only when a CONVENTION changes) ③ ALWAYS regenerate `python3 PROME/tools/will_handbook.py -o <scratchpad>/handbook.html` → republish via Artifact to the recorded URL in its header (favicon 📖). **This run OWNS the change-feed baseline (write=True since the retirement commit)** — `will_brief.py` is a parser/state LIBRARY now, never run as a page |
| ~~**Will's briefing page**~~ **RETIRED 2026-08-21** (Will: "run that through the handbook and retire the standalone") | — | Folded into the Handbook row above; the old URL carries a retirement banner. Former directive text → `git log -p -- PROME/CLOSEOUT.md` (removed 8/29 audit #11, delete-and-point — a skimming reader could have republished the retired page). |

**Intentionally one-way (no closeout write-back, by design):**
- `FLEET_SCAN.md` — superseded historical snapshot; no refresh (fleet state = `ROSTER.md` + DAEDALUS `FLEET_MAP.tsv`).
- COMM mailbox / inbox / agent-outbox scans — ACKed/routed *inline during the session*, never deferred to closeout.
- OPEN-predictions resolution / forward-catalyst firing — domain-agent-owned (NEXUS/ORACLE/LABOR). PROME's only forward-state write-back is the operator-card catalyst list in SCRATCH.
- `TODAY.md` — **retired 2026-07-01; the file does not exist.** It appears on BOOT step 2's Read line only inside its own retirement note (correct historical reference; reword a flagged quote only to stop a pattern-match, never to erase the record).

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
| Regime / thresholds / near gates | `HEARTBEAT.md` | PROME owns content; **commit PROME-standard since 2026-08-23** (Will "free it") — still commit it EXPLICIT-PATH, never swept blind into a batch (synced 8/27; the discipline survived the ungating, per the ruling record) |
| Forward catalyst date moved / resolved | `PROME/DOCKET.tsv` | Update the row **and run `scripts/firetime_check.py` on citing artifacts** — DATE flag ⇒ full logic re-read, never find-replace |
| Daily activity | `memory/YYYY-MM-DD.md` | Append durable session log; **commit at closeout** (outside `PROME/` — Chunk 4 recipe) |
| Durable insight / lesson | auto-memory (`memory/auto/`) | Promote sparingly; index row in `MEMORY.md`; **self-commit mandatory** (root carve-out ③, step 1d) |
| Boot sequence / conditional modules | `PROME/BOOT.md` | Only if they changed |
| Architecture / Boot Trust Stack / doc ownership | `PROME/SYSTEM.md` | Only if a file was retired/created or ownership moved (Chunk-3 trigger) |
| Autonomy grant/revoke | `PROME/AUTONOMY.md` **+ `PROME/CLAUDE.md` Ask-First** | Change-log alone never reaches the next boot — propagate to the auto-loaded surface |
| Prototype learnings | `PROME/ORCHESTRAL_LAYER_DESIGN.md` or SCRATCH v_next | Pick one home, not both |
| `PROME/FLEET_SCAN.md` | — | Don't touch (superseded snapshot) |
| Root `CLAUDE.md`, other shared/root docs | — | Flag to Will; never auto-edit *(HEARTBEAT removed from this row 8/27 — PROME-standard since the 8/23 ruling; root-doc HEARTBEAT LINES stay Will-gated per root canon)* |

**Default:** if no owner state changed, do not write back — state bloat is worse than a quiet closeout.

**Stamp canon (adopted 8/9, governance batch):** an `Updated:` stamp carries a **scope manifest** — what this update covers, not only when. Material section-adds bump the stamp by default (two consecutive stamp misses on material adds, 7/28 + 8/3). A peer-facing surface synced only **partially** carries a **mixed-vintage banner** naming which sections are current (HENRY `LAST_COMPLETION` block = the adopted pattern).

---

## Chunk 1 — State files (Light/Standard/Heavy; Bounce = SCRATCH addendum only)

- **`SCRATCH.md` full rewrite:** what happened · git state in behavior-language (never hashes — they decay) · next-session entry point · cautions.
- **`STATUS.md` surgical:** stamp, work-queue table, decision-layer freshness. ~~Next Best Action~~ **FROZEN 2026-08-08 (Will-ruled): pointer banner only — do NOT write directives into it** (the duplicated-surface rot class; forward moves live in SCRATCH). **Flow rule (Will-approved 2026-08-16, BYTE-keyed per PAT-086 — a line-keyed bound gets walked around, LABOR precedent):** `wc -c < PROME/STATUS.md` ≥ **24,412 B** (75% of the **32,550 B read-cap budget** — root Data Hygiene P1 / `READ_CAP.md` rule 5, Will-approved 8/28, binds above any owner number; re-keyed 8/29 audit #11 from the retired 51,200 B pair) ⇒ this closeout rotates the oldest history blocks (session headlines first, then oldest spine-audit *Prior:* records) **verbatim, crc32-verified round-trip,** into `PROME/archive/STATUS_HEADLINES_<range>.md` until **< 22,785 B** (70%), recorded in the commit. Mirrors the MEMORY.md ≥75%→<70% flow rule (8/12): rotation-not-deletion, history never trimmed in place. First pass 2026-08-16 (76,581→35,172 B, 17 entries, crc `3608023976`). **Headline convention (8/16 S4, RAV rec, Will-approved "go on all four"):** the STATUS session headline is a POINTER-WEIGHT record — outcomes, counts, ruling names, and where the narrative lives (SCRATCH/HANDOFF), target **≤ ~1.5 KB**; the ~5.1 KB/day narrative headlines are what consumed the 8/8 cut in 8 days. Narrative belongs to SCRATCH (session spine) and HANDOFF (continuity); STATUS should never be the third copy. The flow rule still backstops overruns — this convention is what makes rotation rare instead of per-closeout.
- **`ACTIVE_DECISIONS.md` surgical** if a decision moved (boot pairs with it — unwritten = silently stale). **Flow rule (Will-approved 2026-08-22, BYTE-keyed):** `wc -c < PROME/ACTIVE_DECISIONS.md` ≥ **24,412 B** (75% of the 32,550 B read-cap budget — same canon as the STATUS rule above) ⇒ this closeout rotates **verbatim, crc32-verified round-trip** into `PROME/archive/ACTIVE_DECISIONS_ROTATION_<date>.md` until **< 22,785 B** (70%), recorded in the commit. Rotation order: terminal rows WHOLE → header prior-stamp chain → **snapshot-then-rewrite** on live rows (full pre-edit row archived verbatim, live row rewritten current-state-only + dated pointer — NEVER clause-splicing). **Standing guards (clauses carrying live directives) never rotate** — the manifest counts `guard-bytes retained: N` per pass, and the sweep is grep-assisted (dropped text grepped for directive markers, every hit dispositioned); rising N ⇒ guard-retirement review (discharge by ruling). Row-weight convention ≤ ~2 KB; resolutions REPLACE pending language. **Declared revisit trigger: file found >100% of budget at any BOOT ⇒ the check gets scripted (rc-keyed, MEMORY pattern) — no re-litigation.** Design = `PROME/proposals/2026-08-22_active-decisions-flow-rule-DESIGN.md`. **Same recipe for every PROME rotation** (STATUS work-queue/headlines · WILL_QUEUE stamp-chain/roll-offs/>7d DONE · HANDOFF entries · GATES history when that redesign lands): verbatim block between markers, crc32 in the archive header. ⚠️ **Verify a rotation by RECOMPUTING the crc from the archived bytes — never by reading the banner that claims it** (SHADE ③ 8/28; a banner is a claim about the file, the crc is the file). The `**Last reconciled:**` / header stamp lines carry ONE stamp — prior stamps rotate with the pass, never chain in place.
- **Blind-reader verification (Will-approved 2026-08-22, rec-2 — verbatim "ok approve both to your recs" ~11:47 EDT):** any rotation pass under a byte flow rule AND any HEARTBEAT re-base closes with a **blind cold-reader check** — spawn a fresh-context read-only agent (Explore-class) that reads ONLY the rewritten surface, answers a short ground-truth question set (state questions whose answers the rewrite touched + at least ONE rotated-content question so pointer-following is exercised + one anchor-recovery walk), and is graded before the commit ships. Rationale: the author is contaminated — they know the answers, so only a cold reader can detect a dropped guard or lost state. First run 2026-08-22: 10/10 correct AND caught the author's chars-vs-bytes unit mislabel. Cost ~60s/one small agent.
- **`HANDOFF.md` (Standard/Heavy):** concise entry — what landed, Will's decisions, decisions needed, risks, next pointer, rules held. Keep 3-5 entries live. Rotated entries → `PROME/archive/HANDOFF_<date>_<name>.md` with the crc in that file's header; **HANDOFF's own Archive line stays ONE pointer** — the pre-8/28 pointer paragraph is a FROZEN snapshot at `PROME/archive/HANDOFF_ARCHIVE_POINTERS_2026-08-28.md` — nothing appends to it; `ls` is the index.
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

**Root session-end steps 1b-1e** (root `CLAUDE.md` owns the full text):
- **1b orphan check:** `bash scripts/orphan_check.sh PROME` — `[likely YOURS]` → commit per carve-out ① (⚠️ `memory/auto/` files PROME wrote are path-classified `[not yours]` but carve-out ③ makes committing them MANDATORY).
- **1c consumer check** (if a published number was superseded): `python3 scripts/consumer_check.py --agent PROME --old <old> --new <new>` → packet each 🔴 owner, never edit their files.
- **1d memory-index check** (if auto-memory written): `python3 scripts/memory_index_check.py --strict --slug <slug>` — the `--slug` form, never bare `--strict`.
- **1d-bis hot-index flow rule (Will-approved 2026-08-12, PROME-only):** if `check_memory_length.sh` reads **≥75% of bytes** at closeout, demote (never delete) settled/predictable-trigger rows from `MEMORY.md` to `INDEX_COLD.md` until **under 70%**, in the same sitting — slug-conservation proven in the commit (union count before == after; the 8/12 pass's script pattern is the template). Agents still only flag (7/28 ruling); this step is why the flag now has a standing consumer instead of an emergency every ~8 days.
- **1e claim check** (canon scope, root 1e): `python3 scripts/claim_check.py --check weekday PROME/DOCKET.tsv PROME/GATES.tsv PROME/WILL_QUEUE.md PROME/STATUS.md` — the measured decision-class scope; a bare no-args run is a *different*, broader check (changed-files, all classes) and fine as an extra, not a substitute *(scope drift fixed 8/9, audit #8)*. **rc=1 means LOOK, not find-replace** (its first live flag was a *correct* prior-year date). Known limits: can't tell mention from use; cross-repo hashes read `missing`; placeholders flag.

```
cd "$(git rev-parse --show-toplevel)"                    # ⚠️ STEP 0: ALL git ops + safe-push from repo root —
                                                         #    from PROME/'s cwd, `git status -- PROME/` SILENTLY false-passes
git status --short
git status -- PROME/ memory/                             # mandatory pre-commit check (root item 5): no dangling deletions,
                                                         #    no forgotten new files, nothing staged outside scope
# modified files — path-scoped commit, no staging step (never `git reset HEAD`):
git commit -m "PROME: <subject>" -- PROME/<file> PROME/<file>
# new untracked files — atomic add+commit of EXPLICIT paths (never `git add PROME/` as a directory):
git add -- PROME/<newfile> && git commit -m "PROME: <subject>" -- PROME/<newfile>
# Chunk 2 outputs live OUTSIDE PROME/ — commit them too (first session of a day: daily log is new-untracked, add it):
git add -- memory/auto/<slug>.md memory/YYYY-MM-DD.md && git commit -m "PROME: <subject>" -- memory/YYYY-MM-DD.md memory/auto/<slug>.md memory/auto/MEMORY.md
./scripts/safe-push.sh
git status --short --branch                              # final: clean tree + "ahead 0, behind 0" BEFORE reporting synced
```

**Auto-push:** `safe-push.sh` is the closeout tail — ff-gated, fails safe, sweeps the push-train. **POST-PUSH VERIFY:** the literal `Pushed.` line ("Nothing to push" when you expected commits = you forgot to commit). Non-ff abort = **routine** → `git pull --rebase --autostash` + re-push; escalation rules = root canon (out-of-dir conflicts, or non-ff persisting through a completed rebase→re-push cycle). Commit style: `PROME: <short one-liner>`; **`-m` before `--`** (everything after `--` is a pathspec).

**Session summary to Will:** what landed (1-2 lines) · what's pending · next-session entry point (points at SCRATCH).

---

## Skip rules

- **Operator card** — part of SCRATCH's rewrite (standalone `TODAY.md` retired 2026-07-01).
- **`AGENTS/<other>/` files** — default **never** (owners own their state). Exceptions = root canon's **three self-authorship carve-outs ①–③ (+ the PROME-only Gate C custody carve-out ④ when activated)** (① self-authored inbox packets — must commit · ② self-authored shared-log rows · ③ `memory/auto/` self-commit mandatory; full text root `CLAUDE.md` Git Protocol) + **Will-approved per-instance apply-on-behalf** (specific files, authorization named in the commit body).
- **Root `CLAUDE.md` / shared files** — flag to Will; Will-approval gates the change.

## Cross-session behavioral rules

- **Behavior-language over hash-pinning** in state files (hashes decay within 48h).
- **Verify state before propagating** — ground truth, not prior surface text.
- **Chunked updates** with checkpoints, not 4-5-file batches.
- **`trash` over `rm`.**

---

## Closeout-class fleet memories (fleet-memory embeds — migrated 2026-07-31, Phase-2 restructure)
*One-liners embedded from memory/auto/ (files unchanged); index rows now in memory/auto/INDEX_COLD.md.*

- finding_closeout_as_writeback_tail — "Codify session closeout as the write-back tail of the auto-loaded CLAUDE.md SPAWN PROTOCOL, not a standalone doc; auto-load is the decisive factor" `[[finding_closeout_as_writeback_tail]]`
- feedback_intra_day_closeout_discipline — Run WALTER closeout (spawn-protocol steps 12-15) at every session end, not just end-of-day; multi-session-days must honor intermediate closeout to prevent STATUS-staleness gap `[[feedback_intra_day_closeout_discipline]]`
- feedback_handoff_cadence — Will prefers clean handoffs at natural breakpoints over riding a long session into degradation `[[feedback_handoff_cadence]]`
- finding_state_token_sweep_all_surfaces — "When a gate/decision state flips (e.g. FIRED-UNEXECUTED → RESOLVED), sweep the state-token across ALL surfaces — live ledgers (VX/KB.tsv) and live templates/setups too, not just STATUS/SCRATCH; scope the verification grep from repo root." `[[finding_state_token_sweep_all_surfaces]]`
- finding_completion_stamp_skip_reads_as_current — "a file whose NAME promises currency (LAST_COMPLETION) that SKIPS a closeout doesn't read as stale — it reads as current and wrong; detect by mtime vs STATUS.md" `[[finding_completion_stamp_skip_reads_as_current]]`
