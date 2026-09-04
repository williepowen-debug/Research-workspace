# PROME profile refresh — Mode-A READER REPORT (2026-09-03)

**Reader:** DAEDALUS fork (read-only; this file is the only write) · **Subject:** PROME, repo-root `PROME/` · **Basis:** working tree at HEAD `658e6cd3b` (clean), measured with `wc -c` / `du -sb` on 2026-09-03 ~21:xx ET · **Prior profile body:** `profiles/PROME.md` (2026-07-28, 37 d) · **Commits touching `PROME/` since 7/28:** 1,491 (`git log --since=2026-07-28 -- PROME | wc -l`) · **Budget constant:** 32,550 B (`BLUEPRINTS/READ_CAP.md`; `prome_gate.py:586`).

Confidence tokens per `PROME/CLAUDE.md:77`: **VERIFIED** = checked at the artifact · **INFERRED** · **SEARCH-NOT-FOUND** · **UNKNOWN**.

---

## 1. File anatomy, measured today

### 1a. Top-level `PROME/` (du -sb; 38 entries)

| Path | Bytes | Class | What it is (one line) |
|---|---:|---|---|
| `archive/` | 10,199,624 | ARCHIVE | 168 entries: 66 `HANDOFF_*` rotations · 17 `HEARTBEAT_PREREBASE_SNAPSHOT_*` · 12 `STATUS_HEADLINES_*` · 4 `WILL_QUEUE_ROWS_*` · 3 `ACTIVE_DECISIONS_ROTATION_*` · 2 `GATES_STATE_HISTORY_*` · `GATES_TERMINAL_ROWS_2026-09-03.tsv` · `DOCKET_HISTORY_2026-08-30.md` · legacy (`HANDOFF_2026Q2.md` 247,167 B, last touched 8/7; network PNGs; `DECISION_ARTIFACTS_INDEX.md` 7/1) |
| `inbox/` | 2,857,299 | LIVE flow | sole PROME delivery surface (root `CLAUDE.md:18`); 4 unprocessed top-level packets (all DAEDALUS, 9/3 20:18–20:41) · `processed/` 471 files |
| `proposals/` | 797,491 | LIVE record | 76 files — ruling records (`*-RULED.md`), build records; newest `2026-09-03_wq170-and-163-item6-RULED.md` |
| `tools/` | 618,822 | PROTOCOL (code) | 12 scripts + `hooks/` (3) + `tests/` (2) + state JSON; see §1c |
| `DOCKET.tsv` | 255,948 | LIVE rail | 251 data rows (104 PENDING · 9 PENDING(OVERDUE-annotated) · 92 RESOLVED · …); canonical forward catalysts; cited by PHYSICAL LINE NUMBER, append-only (`DOCKET.tsv:1`) |
| `state/` | 145,776 | LIVE state | `ORCH_LOG.tsv` 114,667 B (born 861e72699 8/23) · `board_cursor.txt` · `brief_changes.jsonl` · `brief_snapshot.json` |
| `research/` | 112,035 | record | 14 files |
| `WILL_QUEUE.md` | 71,327 | LIVE rail | operator ledger, born 090b28389 7/30; OPEN 14 rows · RECENTLY DONE 24 rows |
| `codex/` | 61,823 | record | RAV/Codex cross-vendor lane: CHARTER 7/9, QC ledger/workflow 8/7, 4 review records 8/21–8/23 |
| `HEARTBEAT_COLD.md` | 55,776 | LIVE cold register | born 9/2 at the tenth HEARTBEAT re-base (4948f6d9b); grep-mode, never boot-read |
| `GATES.tsv` | 51,849 | LIVE rail | fire-ledger, 20 data rows (18 LIVE · 2 RESOLVED); born 49b87964d 7/9; two-step split 9/3 (a0b34e041, b0e36d039) |
| `ORCHESTRATION_PLAYBOOK.md` | 43,558 | PROTOCOL | mode-split, model tiering, two-tier orchestrated-desk model (§L203, 8/23); stamp 8/10 |
| `ROSTER.md` | 34,725 | LIVE classification truth | 5-class taxonomy (8/5), Authority column w/ DESCRIPTIVE-ONLY fence (`:29`, `:31`), cadence posture (`:19`) |
| `packets/` | 30,741 | flow | 4 files |
| `CLOSEOUT.md` | 30,038 | PROTOCOL spine | 174 ln; tiers + symmetry table + write-back contract + Chunks 1–4; stamp 8/29 |
| `.claude/` | 29,896 | PROTOCOL (harness) | `settings.json` (4 hooks) · `agents/{anvil,coldreader}.md` · `skills/{boot,closeout,coldread,reconcile,spineaudit}/SKILL.md` (all born 8/29 except anvil 7/30) |
| `registry/` | 29,366 | LIVE registry | `READS.tsv` 29,284 B (born 85a158c03 8/31) · `corrections_receipts.tsv` 82 B (1 receipt, 8/28) |
| `SYSTEM.md` | 24,596 | PROTOCOL (governance) | Boot Trust Stack + Mirror Map (`:46–65`); stamp 8/22 |
| `STATUS.md` | 24,171 | LIVE (pointer-weight) | 66 ln; header + spine-audit stamp (`:17`) + Core State + Live Surfaces + Work Queue + frozen Next Best Action (`:64`) |
| `HANDOFF.md` | 22,503 | LIVE continuity | 5 entries (`:11,:21,:31,:41,:52`), rotation-bounded to 3–5 |
| `reports/` | 19,946 | record | 2 files |
| `MACHINE_LOCAL.md` | 18,592 | PROTOCOL | machine inventory + switching checklist; stamp 8/29 |
| `BOOT.md` | 17,890 | PROTOCOL spine | 124 ln; steps 0–9 + Conditional Modules table + boot-class memory embeds; stamp 8/29 NIGHT-2 |
| `data/` | 17,671 | record | 3 files |
| `ACTIVE_DECISIONS.md` | 17,325 | LIVE rail | non-terminal decision index; stamp 9/1; byte flow rule since 8/22 (cff011ef6) |
| `SCRATCH.md` | 16,432 | LIVE session state | ★ NEXT SESSION · errors #81–84 · cautions · operator card · catalyst view · git state; stamp 9/3 ~21:0x |
| `ORCHESTRAL_LAYER_DESIGN.md` | 15,653 | PROTOCOL (decaying) | stamp 2026-07-01 — oldest protocol vintage in the dir |
| `cluster/` | 12,972 | record | 2 files |
| `public-prep/` | 12,307 | record | 2 files |
| `GIT_COORDINATION.md` | 12,234 | PROTOCOL | commit cookbook; no `**Updated:**` stamp form found (SEARCH-NOT-FOUND on the regex, not necessarily unstamped) |
| `artifacts/` | 11,812 | record | 1 file |
| `drafts/` | 11,132 | flow | 1 file |
| `HANDBOOK.md` | 11,119 | LIVE Will-facing source | THE HELM manual canon (born db9b4503f 8/21) |
| `CLAUDE.md` | 11,012 | PROTOCOL (auto-injected) | 95 ln; Boot steps 1–2 · Ask-First · Spawn tiers · Git default · **Session Process Controls (WQ-140, 8/30)** · Handoff Requirement |
| `AUTONOMY.md` | 10,086 | PROTOCOL | Tier 1 / 2 / 3 (`:11,:31,:45`) + Gray Zone + change-log; stamp 8/29 |
| `BRIEF.md` | 8,401 | LIVE Will-facing source | narrative fed to THE HELM (`will_brief.py`) |
| `COMPLETION_SPEC.md` | 8,329 | PROTOCOL | spawn contract; stamp 8/13 |
| `action-cards/` | 4,701 | record | 1 file |
| `FLEET_SCAN.md` | 1,193 | ARCHIVE-in-place | superseded 2026-06-16 snapshot, banner on `:1–4`; never boot-read (`BOOT.md:64,:83`) |

### 1b. Boot reads — what a PROME session loads whole, vs the 32,550 B budget

Sources: `PROME/CLAUDE.md:25–26` (steps 1–2), `PROME/BOOT.md:49–58` (steps 1–5), `PROME/registry/READS.tsv` PROME rows (data rows 2–14, 44–54).

| Surface | Mode (READS.tsv) | BOOT step | Bytes | % of 32,550 | Metered by `prome_gate check_byte_budgets` (`:587–590`)? |
|---|---|---|---:|---:|---|
| `USER.md` | whole | CLAUDE.md-Boot-1 | 4,126 | 12.7% | no |
| `PROME/BOOT.md` | whole | CLAUDE.md-Boot-2 | 17,890 | 55.0% | no |
| `PROME/HANDOFF.md` | whole | BOOT-1 | 22,503 | **69.1%** | **no** — only the "3–5 entries" maintenance bound (`HANDOFF.md:3`) |
| `PROME/SCRATCH.md` | whole | BOOT-2 | 16,432 | 50.5% | yes |
| `PROME/ACTIVE_DECISIONS.md` | whole | BOOT-3 | 17,325 | 53.2% | yes |
| `PROME/STATUS.md` | whole | BOOT-4 | 24,171 | **74.3%** | yes — 241 B under the 24,412 B rotation trigger (`CLOSEOUT.md:97`) |
| `HEARTBEAT.md` | whole | BOOT-5 | 23,799 | **73.1%** | yes |
| **Σ whole reads** | | | **126,246** | **388%** (3.9 budgets) | |
| root `CLAUDE.md` | auto-injected (BASIS row 40) | — | 22,347 | 68.6% | n/a |
| `PROME/CLAUDE.md` | auto-injected (BASIS row 39) | — | 11,012 | 33.8% | n/a |
| `memory/MEMORY.md` (auto-memory index) | auto-injected | — | 18,982 | 58.3% (vs its own 25,600 B cap: 74.1%) | yes (via `harness_caps.env`) |
| **Σ context before any conditional read** | | | **≈178,587** | | |

Programmatic / summary / scoped (declared, NOT cap-bearing — `READS.tsv` header rulings 3, `:25–33`):

| Surface | Declared mode | Bytes | % | Note |
|---|---|---:|---:|---|
| `PROME/GATES.tsv` | summary (BOOT-3) | 51,849 | 159.3% | READS.tsv row 8 self-declares the PROTOCOL/PRACTICE mismatch: BOOT.md:51 says "Read … `PROME/GATES.tsv`" over a script consume. After the 9/3 two-step split it sits AT the ~50 KB practical read ceiling (DOCKET L256, PENDING 9/4 = step-3 design) |
| `PROME/DOCKET.tsv` | summary (BOOT-5) | 255,948 | 786% | consumed by `check_docket_overdue`; the VIEW read is SCRATCH's calendar |
| `PROME/WILL_QUEUE.md` | summary (BOOT-5) + scoped OPEN table (BOOT-8) | 71,327 | 219% | two rows, two operations (READS.tsv rows 13–14) |
| `PROME/CLOSEOUT.md` | summary (BOOT-5, symmetry input) | 30,038 | **92.3%** | ⚠️ but it is read WHOLE by the session at closeout (`BOOT.md:68`, `/closeout` SKILL step 7 "Chunk 4 in full") — a closeout-time whole read has no manifest row (READS.tsv is a BOOT manifest) — see §6 D-6 |
| `PROME/ROSTER.md` | **not declared** (conditional, `BOOT.md:64,:83`) | 34,725 | **106.7%** | over budget; no PROME row in READS.tsv (SEARCH-NOT-FOUND: `grep -P '^READ\tPROME\tPROME/ROSTER'` = 0) — see §6 D-5 |
| `PROME/state/ORCH_LOG.tsv` | scoped by **WALTER** (READS.tsv row 31, WALTER:9b) | 114,667 | 352% | READS.tsv:31 recorded 58,230 B on 8/31 → **+97% in 3 days**; no rotation/cap rule found in PLAYBOOK/CLOSEOUT/BOOT (grep null) — see §6 D-3 |
| `PROME/HEARTBEAT_COLD.md` | grep (row 11) | 55,776 | 171% | correct class; grows at every re-base by design |

Cross-check with the fleet instrument (read-only run, `scripts/read_cap_check.py --agent PROME`, rc=0): **it finds 1 whole-read file (STATUS.md, 24,171 B)** and prints "heuristic — READS.tsv replaces it". The manifest declares **7**. The FLEET_MAP row's "every STATUS-relative instrument under-measures it" is VERIFIED and quantified: 1 of 7.

### 1c. Tools (`PROME/tools/`, bytes; birth hash)

| Tool | Bytes | Born | Invoked from |
|---|---:|---|---|
| `fleet_dashboard.py` | 58,660 | 4bf31bc4c 7/11 | CLOSEOUT symmetry row `:52` (Standard+) |
| `reads_check.py` | 45,998 | 85a158c03 8/31 | **WALTER `CLAUDE.md` only**; not BOOT/CLOSEOUT/skills of PROME (grep 0/0/0) |
| `will_handbook.py` | 43,304 | db9b4503f 8/21 | CLOSEOUT `:53` (THE HELM, Standard+ MANDATORY) |
| `prome_gate.py` | 42,160 | 72d130881 7/28 | BOOT `:60` (boot) · CLOSEOUT `:36` (closeout) · both skills |
| `will_brief.py` | 35,428 | d933e41d0 8/3 | CLOSEOUT `:53` (via handbook) |
| `spine_audit.workflow.js` | 13,586 | pre-7/28 | `/spineaudit`; GROUPS = 8 pairs / 16 files incl. the two runners (`:66–88`) |
| `gates_step2_rotation_2026-09-03.py` | 11,953 | b0e36d039 9/3 | one-shot (dated filename) |
| `commit_check.py` | 10,125 | c78a1efdf 8/29 | CLOSEOUT `:121,:137–141` + closeout skill step 7 |
| `recurrence_rate.py` | 8,612 | 0784e9e00 8/23 | no protocol invocation site found (BOOT/CLOSEOUT/CLAUDE/skills/SYSTEM all 0) |
| `agent_freshness.py` | 7,796 | 219516625 8/14 | inside `prome_gate.py:654` (`--gate`) |
| `board_scan.py` | 6,812 | b7e48bc10 7/27 | inside gate (`:646`) + BOOT `:65` standalone rule |
| `measure.py` | 6,229 | b14f7b6f7 8/30 | `PROME/CLAUDE.md:76` (rule) only — no step invokes it |
| `queue_parser_selftest.py` | 5,365 | 6c3d893fc 8/16 | inside gate closeout (`:702`) |
| `hooks/git_guard.py` · `hooks/prompt_clock.sh` · `hooks/forge_validate.py` | 5,374 · 466 · 3,768 | e67992c34 / 909921438 8/29 | `.claude/settings.json` PreToolUse · UserPromptSubmit · PostToolUse |
| `tests/test_prome_gate_gates.py` · `hooks/test_git_guard.py` | 2,659 · 1,909 | 8/28 · 8/29 | selftests |

---

## 2. The spine since the re-base

### 2a. What the "8/20 spine re-base" trigger actually was — UNKNOWN in git

`git log --since=2026-08-19 --until=2026-08-21 -- PROME/BOOT.md PROME/CLOSEOUT.md PROME/CLAUDE.md PROME/SYSTEM.md` returns **nothing**. The only 8/20 re-base is **HEARTBEAT** (cf3a0d5bf, chain reset). The protocol-spine restructures that DID happen, by hash:

| Date | Hash | Spine change |
|---|---|---|
| 8/8 | 5b5fd31da · 84cfe5a0b | STATUS Next Best Action FROZEN to pointer (50,550→35,775 B); symmetry advisory cleared |
| 8/9 | b2ada2fa0 | **CLOSEOUT spine prune 287→165 ln** (git prose → root-canon pointers; tables merged; stamp canon + deferral row added) — `CLOSEOUT.md:3` scope manifest |
| 8/16 | 5ae4f2fee · 27c98aaf1 | STATUS byte flow rule ENCODED; spine-audit anchor leg (8th reader samples DOCKET) |
| 8/17 | e01259478 | "boot spine single-Read-able" (self-audit batches) |
| 8/22 | cff011ef6 · 0dcc11cd7 | ACTIVE_DECISIONS flow rule + blind-reader rule adopted |
| 8/23 | 861e72699 | two-tier orchestrated-desk model → PLAYBOOK §L203 + `state/ORCH_LOG.tsv` born |
| 8/28 | a4dde8fdb · d3915f75d · a52b641f8 | slim-down 6/6 (BOOT step provenance → git pointers); R1 corrections check wired (BOOT 5b) |
| **8/29** | e2bffc961 · 5e1081f8d · e0186278c · de9b2c62a · 570ba689f · f6fdb6767 · 6923e56d3 · 38470d237 | **THE RUNNER DAY:** manual-vs-skill layering rule; `/boot` + `/closeout` built as ordered indexes; runners cold-tested (6 FAILs fixed); spine audit gains the runners; closeout gate moved LAST; BOOT.md provenance out of step bodies (19,756→17,871 B); memory embeds regrouped by trigger; 3-blind-reader fix round |
| 8/29 | c78a1efdf · e67992c34 · 909921438 | `commit_check.py` wrapper; 4 harness hooks (banner/clock/git_guard/forge_validate) |
| 8/30 | b14f7b6f7 | WQ-140: `measure.py` + Session Process Controls → `PROME/CLAUDE.md:74–80` |
| 8/31 | 85a158c03 · 7d079e523 | `registry/READS.tsv` + `reads_check.py` |
| 9/2 | 4948f6d9b | HEARTBEAT structural split (hot + `HEARTBEAT_COLD.md`) |
| 9/3 | a0b34e041 · b0e36d039 · 7c864f271 | GATES two-step split; WQ-165 cold-read STOP rule into CLOSEOUT |

**INFERRED:** the profile's own trigger clause ("any re-base of the protocol spine, or ±2 surfaces added/removed from BOOT.md's read list") was fired by the 8/9 prune and re-fired by the 8/29 runner day; the "8/20" label in the FLEET_MAP row most plausibly points at HEARTBEAT (a boot-read surface), not the manual spine. See §8 Q1.

### 2b. Current boot chain (`PROME/BOOT.md`, one line per step; executed via `/boot` SKILL)

| Step | Line | Content |
|---|---|---|
| CLAUDE-1 | `PROME/CLAUDE.md:25` | explicit `Read USER.md`; `AGENTS.md` on demand |
| CLAUDE-2 | `:26` | follow BOOT.md in full via `/boot`; **layering rule:** manuals own rules, skills own sequence; a manual step absent from its runner is a defect (both directions) |
| 0 | `BOOT.md:38–47` | clock from the `NOW:` hook line (`prompt_clock.sh`); SessionStart banner (`session_banner.sh`, flag-not-force); `git status`/`fetch`/`rev-list`; pull only if clean |
| 1 | `:49` | Read `HANDOFF.md` (top live entries) |
| 2 | `:50` | Read `SCRATCH.md` + operator card |
| 3 | `:51` | Read `ACTIVE_DECISIONS.md` **and `GATES.tsv`** — FIRED-UNEXECUTED = 🔴 blocking; LIVE staleness keys on `consumed_by` |
| 4 / 4b | `:52–53` | Read `STATUS.md`; read § Boot-class fleet memories (first group every boot) |
| 5 | `:54–62` | market-data gate: explicit-Read `HEARTBEAT.md` · env_doctor · position-agreement · **⚡ ONE-SHOT `prome_gate.py boot`** (13 check families, rc=1 only BLOCKING; runs `board_scan --advance` once) · 5b R1 corrections · firetime ≤7d w/ expiry-dated allowlist |
| 6 | `:63–68` | conditional reads: ROSTER/FLEET_MAP only for fleet work; BOARD scan already inside gate; `PROME/inbox/` sole delivery surface / `AGENTS/PROME/` regression rule; CLOSEOUT before `/clear` |
| 7 | `:69` | declare boot state |
| 8 | `:70` | flag top issues incl. spine-audit stamp >7d **or missing = stale**; **owed items as a choice to Will**; **third-boot rule** (owed item leaves SCRATCH for DOCKET `COVERED:`/WQ row) |
| 9 | `:71` | ≤5 proposals |
| — | `:75–91` | Conditional Modules table (11 rows) |
| — | `:103–124` | 14 memory embeds in 4 trigger groups |

### 2c. Current closeout chain (`PROME/CLOSEOUT.md`; executed via `/closeout` SKILL)

| Block | Line | Content |
|---|---|---|
| Pre-closeout 1–4 | `:20–23` | git status; foreign dirty work does NOT block; **orchestrated-desk release** (8/23 two-tier, ANY tier); tier pick |
| Tiers | `:25–32` | Bounce / Light / **Standard (default)** / Heavy; Standard+ MANDATORY = Fleet-Ops dashboard regen + THE HELM; Chunk 3 trigger-gated at any tier |
| ⚡ Mechanical tail | `:36` | `prome_gate.py closeout` **RUN LAST** (REV 8/29) — after every write and after the two pages regenerate |
| Symmetry table | `:38–54` | 11 rows: HANDOFF · SCRATCH (`Pending Will:` parse contract) · AD · **GATES** · STATUS · HEARTBEAT (byte flow, re-base w/ hot/cold) · memory · **DOCKET** · Fleet-Ops dashboard · THE HELM · retired brief; one-way list `:56–60`; machine-checked by `check_symmetry` on `Read`-directive lines |
| Write-Back Contract | `:64–87` | 16-row "if this changed → write back to" table incl. **AUTONOMY → CLAUDE.md Ask-First propagation**; stamp canon `:89` |
| Chunk 1 | `:93–101` | GATES + DOCKET surgical FIRST (added 8/29) · SCRATCH full rewrite · STATUS surgical + **byte flow rule ≥24,412 B → rotate to <22,785 B** · AD flow rule (same figures) · **blind-reader verification on any rotation/re-base** · HANDOFF 3–5 entries w/ crc rotation |
| Chunk 2 | `:103–106` | daily memory + auto-memory (trigger-gated) |
| Chunk 3 | `:108–117` | residuals: SYSTEM trust stack · Mirror-Map walk (`consumer_check --mirror-map`) · firetime on DOCKET change · spine audit >7d · AUTONOMY propagate · release spawns · subagent propagation |
| Chunk 4 | `:119–148` | **`commit_check.py commit -F <msgfile> -- <paths>` for every commit** · root 1b/1c/1d/1d-bis/1e by name · command block · `safe-push.sh` receipt line `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` · Will summary format |
| Skip / cross-session rules | `:152–163` | carve-outs ①–④ mirror; behavior-language over hashes |
| Embeds | `:167–174` | 5 closeout-class memory one-liners |

### 2d. Delta vs the 7/28 profile §2/§6

| Profile (7/28) said | Today |
|---|---|
| `CLAUDE.md` 76 ln, thin, lagging mirror | 95 ln / 11,012 B; now carries the **Spawn-tier block** (`:57–61`, 8/22) and **Session Process Controls** (`:74–80`, 8/30) — a rule-bearing surface, not thin; explicitly justified as "AUTONOMY is not boot-read and this file is" (`:61`) |
| `BOOT.md` 96 ln · `CLOSEOUT.md` 260 ln | 124 ln / 17,890 B · **174 ln / 30,038 B** (8/9 prune 287→165, then re-grew +9 ln); BOOT "the FAST surface" now fenced: "new fleet-wide checks get added to the SCRIPT, not to this prose" (`BOOT.md:60`, `CLOSEOUT.md:36`) |
| STATUS ~88 KB, no BOTTOM LINE | 24,171 B / 66 ln, pointer-weight by rule (`CLOSEOUT.md:97`); still no labeled BOTTOM LINE (`grep -c 'BOTTOM LINE' STATUS.md` = 0); Next Best Action FROZEN `:64` |
| Protocol ~1,200 ln / 12 docs; no runners | + 5 skills (`.claude/skills/`, 8/29) as ordered indexes; layering rule is a spine-audit CANON anchor (de9b2c62a) |
| `spine_audit` GROUPS = 10 files, blind to HANDOFF/AUTONOMY/MACHINE_LOCAL/COMPLETION_SPEC | 16 files / 8 pairs — the four blind spots joined 8/9 (`:72–76`) + the two runners 8/29 (`:88`); anchor reader samples DOCKET's >7d tail |
| Archive contains LIVE boot-read `HANDOFF_2026Q2.md` | **GONE as a boot read:** `grep 2026Q2 BOOT.md HANDOFF.md CLOSEOUT.md CLAUDE.md` = 0; file frozen at 8/7; HANDOFF rotation now one file per block with crc (`HANDOFF.md:7`) |
| Tools: board_scan · fleet_dashboard · spine_audit | + prome_gate (7/28 night) · will_brief · agent_freshness · will_handbook · recurrence_rate · commit_check · measure · reads_check · 3 hooks · gates_step2 (one-shot) |
| Reading protocol §6: "STATUS head + SCRATCH + DOCKET/GATES" | still right, but add: `WILL_QUEUE.md` OPEN table (Will's actor ledger) · `state/ORCH_LOG.tsv` (who is in flight) · `registry/READS.tsv` (what boot actually loads); GATES/DOCKET are now cited by physical line number, so quote `L<n>` |

---

## 3. What changed since 7/28 — the 12 most structurally important (sampled)

| # | Hash | Date | Change |
|---|---|---|---|
| 1 | 72d130881 (born) → fd4acad51 · a52b641f8 · ea5c501a9 · c2ccf0d1d | 7/28 → 9/2 | **`prome_gate.py` becomes the enforcer** — 13 check families; review_by BLOCKING (8/28); R1 corrections (8/28); BD-02 summons (8/20); WQ roll-off clock fix (9/2) |
| 2 | b2ada2fa0 | 8/9 | CLOSEOUT spine prune 287→165 + stamp canon + deferral write-back row |
| 3 | 861e72699 | 8/23 | Two-tier orchestrated-desk model + `state/ORCH_LOG.tsv` (touch ledger; feeds DAEDALUS coordination scorecard, DOCKET L239) |
| 4 | 85f006d37 … 582600d5c · 78d8b5b37 | 8/25 → 9/2 | **Kernel / Gate C custody:** 94 commits on `KERNEL/`; decisions 1–15 ratified 8/25; Gate C C1–C8 8/26–8/27; Sitting 2 convened+closed 9/2 [14:00:15Z–14:13:08Z], six activations LIVE-2026-0007…, `revoked_at` set; root `CLAUDE.md` Gate C custody paragraph (PROME sole acceptance custodian) |
| 5 | db9b4503f → 25910ade4 | 8/21 | **THE HELM** (`will_handbook.py` + `HANDBOOK.md` + `BRIEF.md` as a tab); standalone Desk-brief RETIRED (11c96b695) |
| 6 | 6a6294059 · 0843ee3a1 | 8/5 · 8/30 | ROSTER five-class taxonomy + Authority column w/ DESCRIPTIVE-ONLY fence; root CLAUDE.md roster paragraph retired to a pointer (WQ-120, 8/29) |
| 7 | e2bffc961 · 5e1081f8d · de9b2c62a · 570ba689f | 8/29 | `/boot` + `/closeout` runners + layering rule; closeout gate LAST; runners in spine audit |
| 8 | c78a1efdf · e67992c34 · 909921438 | 8/29 | `commit_check.py` wrapper + 4 harness hooks (`git_guard` lint layer — its own docstring retracts "impossibilities", `git_guard.py:8–10`) |
| 9 | b14f7b6f7 | 8/30 | WQ-140 Session Process Controls: `measure.py` sole byte source · confidence tokens · two-correction stop · pre-edit cold read |
| 10 | 85a158c03 · aa15e2831 · 7d079e523 | 8/31 | `registry/READS.tsv` declared boot-read manifest (per Will's 5 perimeter rulings) + `reads_check.py`; ATTESTATION/BASIS row kinds |
| 11 | 4948f6d9b · 140aa8924 · 32f4b62be | 8/31 → 9/3 | HEARTBEAT: ninth re-base (8/31), **tenth = STRUCTURAL SPLIT** hot/cold (9/2), Am.#1–#4 chain 4, eleventh docketed 9/4 (DOCKET L257) |
| 12 | 39d07304d · a0b34e041 · b0e36d039 · f59290aa2 | 8/29 → 9/3 | GATES.tsv: state-cell split 98,116→51,502 B (WQ-131, ≤220-char cells + `hist→GATES_STATE_HISTORY`); step 1 terminal rows → archive (14 rows, crc 829548738); step 2 `Prior:` chains → `GATES_STATE_HISTORY_2026-09-03_step2.md` under 2 pre-edit + 3 post-edit blind reads; step 3 = design owed 9/4 (L256) |

Also structural, not in the top 12: `WILL_QUEUE.md` born 7/30 (090b28389) and now the single Will-actor ledger (row-before-the-ask rule, 8/29); `coldreader` agent + `/coldread` (8/29) as the standing second reader (T3 from the 7/28 profile — LANDED); `codex/` RAV lane 8/21–8/23; `DOCKET_HISTORY` tombstone compaction + line-number citation convention (WQ-138, 8/30).

---

## 4. L5 CONFIRM raw material — self-authored rules naming a mechanical step, and where each is invoked

Condition under test (FLEET_MAP row, Next_upgrade): *"full 21d window, ZERO new unexecuted-own-rule"*. This section enumerates; it does not grade. "Invocation site" = a script that runs it or a protocol step that names it in execution order. ✔ = scripted · ◐ = doc step / skill only · ✗ = no invocation site found.

### 4a. Covered by `prome_gate.py` (`mode_boot` `:641–674`, `mode_closeout` `:676–703`)

| Rule (home) | Check | Class | boot | closeout |
|---|---|---|---|---|
| env keys present (`MACHINE_LOCAL.md`) | `env_doctor` | BLOCK | ✔ | — |
| trade surface agrees w/ STATUS cards | `position_agreement` | BLOCK | ✔ | ✔ |
| BOARD pull complete (WALTER §3.5 exemption) | `board_scan --advance` | BLOCK | ✔ | — |
| firetime ≤7d artifacts (`BOOT.md:62`) | `firetime_check --window 7` | ADVISE | ✔ | — |
| agent freshness ground-truth (8/14) | `agent_freshness --gate` | ADVISE | ✔ | — |
| R1 corrections receipted (`BOOT.md:61`) | `corrections_boot_check PROME` | ADVISE | ✔ | — |
| GATES FIRED-UNEXECUTED never standing (`GATES.tsv:4–5`, `CLOSEOUT.md:47`) | `check_gates_tsv` | BLOCK | ✔ | ✔ |
| GATES state cell leads w/ enumerated token | same | BLOCK | ✔ | ✔ |
| GATES `consumed_by` consumer passed/empty (8/7 ruling) | same | ADVISE | ✔ | ✔ |
| GATES `review_by` passed, LIVE INSTRUMENT (8/28) | same | BLOCK | ✔ | ✔ |
| DOCKET PENDING overdue unannotated (`DOCKET.tsv:2` "the boot-time overdue check is the enforcement") | `check_docket_overdue` | BLOCK | ✔ | ✔ |
| DOCKET today-rows undispositioned before going dark | `check_docket_today` | BLOCK | — | ✔ |
| BD-02 desk catalyst summons (`ea5c501a9`) | `check_desk_catalyst_summons` | ADVISE | ✔ | ✔ |
| WILL_QUEUE: ISO needed-by passed / DUE TODAY; reconcile stamp ≤2d; actionable cap; DONE roll-off ~7d; MISFILED close-in-place (`WILL_QUEUE.md:6–8`) | `check_will_queue` | ADVISE | ✔ | ✔ |
| HEARTBEAT chain ~5 → re-base (`HEARTBEAT.md:75`) incl. header cross-check | `check_heartbeat_chain` | ADVISE | ✔ | ✔ |
| Dashboard panels nonempty (PAT-105) / vintage | `check_dashboard_state` | BLOCK/ADVISE | ✔ | ✔ |
| Boot-read surface needs a symmetry row (`CLOSEOUT.md:40`) | `check_symmetry` | ADVISE | ✔ | — |
| root↔PROME `.claude/` parity (8/29) | `check_claude_dir_drift` | ADVISE | ✔ | ✔ |
| Byte flow ≥75% on STATUS · AD · HEARTBEAT · SCRATCH · MEMORY (`CLOSEOUT.md:49,:97,:98`) | `check_byte_budgets` | ADVISE | ✔ | ✔ |
| orphan check (root 1b) | `orphan_check.sh PROME` | ADVISE | — | ✔ |
| gate↔brief WQ parser agreement (8/16) | `queue_parser_selftest` | ADVISE | — | ✔ |
| memory_index_check (root 1d) · consumer_check (root 1c) | `record(ADVISE, "MANUAL: …", True, …)` (`:689–695`) | reminder | — | prints ✅ unconditionally — a reminder, not a check |

### 4b. Self-authored mechanical rules with NO scripted enforcement (doc-step or skill only, or nothing)

| # | Rule | Home (file:line) | Named mechanical step | Invocation site | Status |
|---|---|---|---|---|---|
| R1 | GATES state cell ≤220 chars (WQ-131) | `GATES.tsv:6` | length check | none (`grep -c 220 prome_gate.py` = 0) | ✗ **and currently breached: `GATE-LIQ-079` state cell = 350 chars** (VERIFIED, awk length) |
| R2 | GATES terminal rows ≥7d rotate to `GATES_TERMINAL_ROWS_<date>.tsv` (WQ-166) | `GATES.tsv:8` | recurring rotation | one-shot script only; CLOSEOUT mentions "terminal" 2× but no step; closeout skill 0 | ✗ no recurring site |
| R3 | DOCKET append-only / cite by physical line number / tombstone compaction (WQ-138) | `DOCKET.tsv:1` | row-order invariant | none (no reorder guard; `claim_check` checks weekdays only) | ✗ |
| R4 | Every reported byte/line/crc figure comes from `measure.py` (WQ-140) | `PROME/CLAUDE.md:76` | measurement source | rule text only; BOOT/CLOSEOUT/skills 0 hits | ✗ — live instance §6 D-1 |
| R5 | Two-correction stop per file per session | `PROME/CLAUDE.md:78` | correction count | none (gate's "correction" hits are R1 receipts) | ✗ judgment; observed applied (35b6d3f3b; fa5e2604a "two-correction stop") |
| R6 | Confidence tokens on audit claims | `PROME/CLAUDE.md:77` | vocabulary | none | ✗ |
| R7 | Pre-edit cold read for registry-wide transformations / archival splits | `PROME/CLAUDE.md:79` | `/coldread` | skill exists; applied on GATES step 2 (b0e36d039 "TWO pre-edit blind reads") | ◐ |
| R8 | Blind cold-reader after any rotation / HEARTBEAT re-base, before commit | `CLOSEOUT.md:99`, `HEARTBEAT.md:75` | `/coldread` | skill; WQ-165 two-read stop (7c864f271) | ◐ |
| R9 | Third-boot rule: owed item leaves SCRATCH → DOCKET `COVERED:` / WQ row | `BOOT.md:70` | boot counter | none (`grep -c third prome_gate.py` = 0); applied by hand (WQ row 133) | ✗ |
| R10 | Spine audit >7d **or missing** = stale → `/spineaudit` | `BOOT.md:70`, `CLOSEOUT.md:113` | stamp age | none scripted (gate "spine" hits are comments `:121,:583`); STATUS `:17` = 8/29 (5 d) | ✗ |
| R11 | HANDOFF keep 3–5 live entries; rotate w/ crc | `HANDOFF.md:3`, `CLOSEOUT.md:100` | entry count | none; currently 5 (compliant) | ✗ |
| R12 | HANDOFF whole-read byte budget | (no rule exists) | — | — | GAP: 22,503 B = 69.1% with no meter, no rule |
| R13 | STATUS headline ≤~1.5 KB pointer-weight | `CLOSEOUT.md:97` | headline bytes | none | ✗ |
| R14 | HEARTBEAT >48h stale in a market week → update | `HEARTBEAT.md:75`, `CLOSEOUT.md:49` | age | none (gate meters chain + bytes only) | ✗ |
| R15 | HEARTBEAT hot paragraphs ≤600 B each | `HEARTBEAT.md:75` | per-§ bytes | "a TARGET the gate does not yet meter" — self-declared; §1 627 · §3 763 · §5 641 · §7 809 B over | ✗ self-declared breach |
| R16 | Stamp canon: `Updated:` carries a scope manifest; material adds bump it | `CLOSEOUT.md:89` | — | spine audit (judgment); ride-under class recurs (`CLOSEOUT.md:3` records n≥3) | ◐ |
| R17 | Every commit through `commit_check.py` wrapper | `CLOSEOUT.md:121` | wrapper | CLOSEOUT + skill step 7; `git_guard.py` does NOT require it (grep 0) | ◐ — slip recorded SCRATCH error #82 (9/3) |
| R18 | Root 1e `claim_check` in closeout | `CLOSEOUT.md:128` | script | doc step only; not in `mode_closeout` (grep 0) | ◐ |
| R19 | READS.tsv attestation validated by `reads_check.py` | `READS.tsv` header `:46–53` | script | **WALTER's boot only**; PROME BOOT/CLOSEOUT/skills 0 | ✗ PROME never runs its own manifest checker |
| R20 | ORCH_LOG one row per touch (8/23) | `ORCH_LOG.tsv:1` | — | no cap / rotation rule anywhere (PLAYBOOK/CLOSEOUT/BOOT grep null) | GAP (114,667 B, WALTER scoped-reads it every boot) |
| R21 | HEARTBEAT split re-check "on 2026-10-02" | `HEARTBEAT.md:2` | dated re-trigger | not on DOCKET/WQ/SCRATCH (grep 0); moot if L257 re-base runs 9/4 | 🟡 undocketed date |
| R22 | Standard+ regenerate the two Will-facing pages LAST | `CLOSEOUT.md:36,:52` | order | gate detects only via `dashboard_state` vintage; order itself unchecked | ◐ |
| R23 | Orchestrated-desk release ping + idle verify at ANY tier | `CLOSEOUT.md:22` | — | judgment; ORCH_LOG records | ◐ |
| R24 | Push receipt = exact `Pushed. CONFIRMED…` line | `CLOSEOUT.md:146` | receipt | `safe-push.sh` prints it; no PROME `verify_push`-class check by subject (grep 0) | ◐ |

Net: 22 scripted families (§4a) vs **10 self-authored rules with no invocation site (✗)** and 8 doc/skill-only (◐). Two ✗ rules are **currently breached** (R1, R15). Whether any of these is a "new unexecuted-own-rule inside the 21d window" is the sweep's call — R1 (rule 8/29, breach 9/3), R4 (rule 8/30, instance 9/3), R19 (rule 8/31) are all inside the window.

---

## 5. DO-NOT-TOUCH — re-verification of profile §4 + new load-bearing quirks

| # | 7/28 quirk | Today | Evidence |
|---|---|---|---|
| 1 | Root-level placement | **PRESENT** | `PROME/` at repo root; root `CLAUDE.md:18` "AGENTS/PROME/ does not exist and must not be recreated"; `ls AGENTS/PROME` → no such dir; regression regrew twice (5d447c207 8/28) |
| 2 | DOCKET-wins-on-drift | **PRESENT, strengthened** | `DOCKET.tsv:1` "canonical … cited by PHYSICAL LINE NUMBER; never insert, delete or reorder rows"; `BOOT.md:80` "DOCKET = canonical (SCRATCH card + HEARTBEAT gates are views)"; `CLOSEOUT.md:51` |
| 3 | AUTONOMY.md tiers | **PRESENT + mirrored** | `AUTONOMY.md:11/:31/:45`; tier block ALSO in auto-injected `PROME/CLAUDE.md:57–61` with the reason (`:61`); write-back rule `CLOSEOUT.md:82` |
| 4 | HEARTBEAT re-base + amendment ritual | **PRESENT, now hot/cold + crc + cold-read** | `HEARTBEAT.md:2–3` (Base/Chain header), `:75` (re-base rule, blind read), 17 `HEARTBEAT_PREREBASE_SNAPSHOT_*` in archive; block format `> **AMENDMENT #N` is what `check_heartbeat_chain` counts (`:3`) |
| 5 | `archive/HANDOFF_2026Q2.md` boot-read | **GONE (fixed)** | no reference in BOOT/HANDOFF/CLOSEOUT/CLAUDE (grep 0); file last changed 8/7; rotation now per-block files w/ entry-crc32 (`HANDOFF.md:7`) |
| 6 | codex lane dormant, needs trigger line | **CHANGED — now the RAV cross-vendor lane, live** | `PROME/codex/` 4 review records 8/21–8/23 + `RAV_QC_LEDGER.md`; `PLAYBOOK.md:119` §Codex lane; WQ-140 born from Codex review (b14f7b6f7); BOOT/SYSTEM carry no "codex" line (grep: only `CLAUDE.md:74`) |

**New load-bearing quirks (do not "fix"):**

| # | Quirk | Why it is design | Evidence |
|---|---|---|---|
| N1 | GATES/DOCKET cited by **physical line number**; DOCKET append-only, terminal rows compact IN PLACE to tombstones | every consumer (WQ rows, SCRATCH, packets, this report) carries `L<n>` refs; reordering breaks the fleet | `DOCKET.tsv:1`; `WILL_QUEUE.md:85`; GATES uses `gate_id` not line — different key |
| N2 | GATES state cell = lead token + ≤220 chars + `· hist→GATES_STATE_HISTORY`; `will_handbook.py:468` string-searches the state text | consumers read the LEAD token; the dashboard renders ≤220 | `GATES.tsv:6` |
| N3 | `BOOT.md` `Read`-directive lines ARE the symmetry contract | `check_symmetry` harvests `` `X.md` `` on lines containing the word `Read` — rewording a step can silently drop a surface from the check | `prome_gate.py:519–522`; `CLOSEOUT.md:40` |
| N4 | HEARTBEAT amendment heading regex | `> **AMENDMENT #N` or `> ## AMENDMENT #N`; a style change disarmed the check once (8/4) — header `Chain: N` is cross-checked | `prome_gate.py:396–420`; `HEARTBEAT.md:3` |
| N5 | SCRATCH `Pending Will:` label + `·`-separated items parsed by the dashboard | | `CLOSEOUT.md:45` |
| N6 | `board_scan --advance` runs INSIDE `prome_gate boot`; a second gate run advances the cursor twice | not a bug — nothing skipped, but rule "one invocation per boot" | `BOOT.md:60,:65`; SCRATCH error #81 (9/3) |
| N7 | Kernel accepted events / rejected receipts are **additions-only**; views generated only via the registered renderer; exact pathspecs | root `CLAUDE.md` Gate C custody paragraph; 94 `KERNEL/` commits | `KERNEL/GATE_C_C4_CUSTODY.md`, `..._C7_RUNBOOK.md` |
| N8 | `PROME/.claude/` SHADOWS root `.claude/` for launches from `PROME/` — parity is a gate check, not a symlink | | `prome_gate.py:619–623` |
| N9 | STATUS Next Best Action is FROZEN pointer banner — re-enabling is a Will ruling | | `STATUS.md:64–66` |
| N10 | READS.tsv has NO byte column on purpose; stored bytes rot within hours | | `READS.tsv:35–38` |
| N11 | `HANDOFF.md` Archive line stays ONE pointer; pre-8/28 pointer paragraph frozen in archive | | `CLOSEOUT.md:100` |
| N12 | `git_guard.py` is a lint layer, NOT a boundary (five bypasses passed selftest) — never cite it as enforcement | | `git_guard.py:8–10` |

---

## 6. Defects found (flag, never fix)

| ID | Sev | file:line | Finding | Suggested fix |
|---|---|---|---|---|
| D-1 | 🟠 | `PROME/SCRATCH.md` §5 · `PROME/DOCKET.tsv` L257 | HEARTBEAT re-base trigger claimed "24,448 B = 75.1%, crossed by 36 B". **No committed vintage of `HEARTBEAT.md` has that size**: b0ff3fc32 22,779 · a0b34e041 22,819 · edd164e1c 22,923 · 32f4b62be (HEAD) **23,799 B = 73.1%** — BELOW the 75% trigger. The figure is not reproducible from git; it did not come from `measure.py` at receipt time (R4). | Re-measure at closeout with `measure.py`; if the re-base is still wanted 9/4, re-state the basis (the ≤600 B/§ breaches on `HEARTBEAT.md:75` are a sufficient reason); memory `finding_loadbearing_number_must_be_reproducible` |
| D-2 | 🟠 | `PROME/GATES.tsv` row `GATE-LIQ-079` col 6 | State cell **350 chars** vs the ≤220 contract (`GATES.tsv:6`, WQ-131); no check exists (R1). Registered 9/3 (owner-declared UNGRADEABLE-until-banded). | Cut to summary+pointer; add a length assertion to `check_gates_tsv` (`prome_gate.py:148`) |
| D-3 | 🟠 | `PROME/state/ORCH_LOG.tsv` | 114,667 B, +97% since 8/31 (READS.tsv:31 recorded 58,230 B); WALTER scoped-reads it at every boot (WALTER:9b); no cap/rotation rule in PLAYBOOK/CLOSEOUT/BOOT (grep null). Silent-rot middle state the root Data Hygiene rule forbids. | Rotate touches whose desk has CLOSED OUT to `archive/ORCH_LOG_<range>.tsv` w/ crc; add to `check_byte_budgets` at the physical-ceiling constant; or generate WALTER's "who is in flight" view |
| D-4 | 🟡 | `PROME/HANDOFF.md` (22,503 B) · `PROME/BOOT.md` (17,890 B) · `USER.md` | Three of seven declared whole boot reads are outside `check_byte_budgets` (`prome_gate.py:587–590`). HANDOFF is at **69.1%** with only an entry-count bound; 5 entries × ~4.4 KB will cross 75% on the next long entry. | Add HANDOFF.md + BOOT.md to the meter list (one line each); consider an entry-byte target like STATUS's 1.5 KB |
| D-5 | 🟡 | `PROME/ROSTER.md` 34,725 B (106.7%) | Conditional whole read (`BOOT.md:64,:83`) over budget and absent from PROME's READS.tsv rows (SEARCH-NOT-FOUND). READ_CAP applies to "any surface a boot protocol tells a session to READ WHOLE"; conditional reads are declared for WALTER (CONDITIONAL row_kind) but not here. | Declare a `scoped`/CONDITIONAL row; or split the taxonomy narrative (`:29–31` block) from the table |
| D-6 | 🟡 | `PROME/CLOSEOUT.md` 30,038 B (92.3%) | Read whole at every Standard closeout (`/closeout` step 7 "Chunk 4 in full"; `BOOT.md:68`) but declared only `summary` (READS.tsv row 44 — as the symmetry check's INPUT). The boot manifest has no closeout leg, so a 92% surface is invisible to both instruments. | Either a CLOSEOUT-read row class in READS.tsv or a note that closeout reads are out of perimeter; the file re-grew +9 ln since the 8/9 prune |
| D-7 | 🟡 | `PROME/WILL_QUEUE.md` OPEN table rows 159, 162 | Both lead with `**RULED 2026-09-02 …**` yet sit in OPEN (the close-in-place "silent middle state" `prome_gate.py:329–336` is built to flag — whether it fires on the bold-wrapped token is UNKNOWN; not run). | Move to RECENTLY DONE at next reconcile; confirm the MISFILED regex strips `**` |
| D-8 | 🟡 | `PROME/tools/prome_gate.py:689–695` | `MANUAL: memory_index_check` / `MANUAL: consumer_check` are `record(ADVISE, …, True, …)` — they print ✅ unconditionally. A reader of the verdict block sees two green checks that checked nothing (PAT-074 class). | Print as `REMINDER` lines outside the pass/fail tally, or gate on `git diff --cached --name-only memory/auto/` |
| D-9 | 🟡 | `PROME/tools/reads_check.py` | PROME built the manifest checker and gave itself no invocation site (only WALTER's `CLAUDE.md` runs it). Its own attestation row (READS.tsv row 2) can drift unnoticed — exactly the "nothing aged the attestation" risk row 41 names. | One line in `mode_boot` or BOOT step 5: `python3 PROME/tools/reads_check.py --agent PROME` (ADVISE) |
| D-10 | 🟡 | `PROME/tools/recurrence_rate.py` | No invocation site in any protocol doc/skill (grep 0 across BOOT/CLOSEOUT/CLAUDE/skills/SYSTEM). Decorative vs deliberate — UNKNOWN. | Register in `AGENTS/DAEDALUS/CHECKS.tsv`-style ledger (PROME-local) or name its trigger |
| D-11 | 🟡 | `PROME/BOOT.md:51` | "Read … **and `PROME/GATES.tsv`**" over a script consume — the protocol-verb mismatch READS.tsv row 8 declares but the manual still carries. | Reword to "the gate consumes GATES.tsv; read any flagged row" (keeps the surface in `check_symmetry` only if the word `Read` survives — N3) |
| D-12 | 🟡 | `PROME/HEARTBEAT.md:2` | Dated re-check "2026-10-02" lives only in the file header; not on DOCKET/WQ/SCRATCH. | Docket it, or strike it once L257 runs |
| D-13 | 🟡 | `PROME/ORCHESTRAL_LAYER_DESIGN.md` (stamp 2026-07-01) · `ORCHESTRATION_PLAYBOOK.md` (8/10, but §Two-tier added 8/23 → ride-under) | Oldest protocol vintages; PLAYBOOK stamp predates its own L203 section (stamp-canon ride-under class, `CLOSEOUT.md:89`). | Stamp reconcile at next spine audit; ORCHESTRAL_LAYER_DESIGN retirement-eligible test (>60 d, referenced from BOOT.md:83 only as a pointer) |
| D-14 | 🟡 | `AGENTS/DAEDALUS/FLEET_MAP.tsv` PROME row (own desk) | Gaps cell says STATUS "63 ln / 17.4 KB" (9/1); today 66 ln / 24,171 B — the cell is a stale mirror of a live number. | Re-cut at the 9/6 sweep; state the rule not the number |

No 🔴 silent-failure defect was found in the enforced path: `prome_gate` BLOCK families all have a live invocation site, GATES has 0 FIRED-UNEXECUTED and 20/20 rows lead with an enumerated token (awk col 6), DOCKET has 0 rows with NF≠6, HANDOFF has 5 entries, `AGENTS/PROME/` absent.

---

## 7. Maturity read — Meta class, per leg

| Leg | Verdict | Evidence |
|---|---|---|
| L0 Skeleton (dir + CLAUDE.md) | **MET** | `PROME/` + `PROME/CLAUDE.md` (95 ln) |
| L1 Live (STATUS + BOTTOM LINE) | **MET (BOTTOM LINE in its own form)** | `STATUS.md` updated 9/3 ~21:0x; no labeled "BOTTOM LINE" (grep 0) — substance = header + Core State (`:19–27`), a grandfathered local form since the 7/28 grade |
| L2 Logging (structured record, valid schema, accruing) | **MET** | GATES 20 rows × 12 cols, tokens valid 20/20; DOCKET 251 rows NF==6 (0 short); WILL_QUEUE 38 rows w/ ISO dates; ORCH_LOG 85 ln; READS.tsv; corrections_receipts; 76 proposal records |
| L3 Meta: conformance checks run; fleet map current | **MET** | `prome_gate` boot+closeout with 22 scripted families; spine audit #11 8/29 (5 d, inside 7-d cadence; STATUS `:17`); `.claude` parity; the fleet map is DAEDALUS's, and PROME's ROSTER (its half) was re-cut 8/30 (0843ee3a1) |
| L4 Meta: builds/retirements executed clean; patterns accruing | **MET** | Builds: THE HELM (8/21), READS.tsv (8/31), commit_check + hooks (8/29), runners (8/29), Kernel Sitting 2 convened+closed clean 9/2; retirements: Desk-brief (11c96b695), root LESSONS.md (671a3f4c8), TODAY.md, Next Best Action; 40 PATTERNS rows since 8/1 cite PROME; 4 memory promotions in 30 d |
| L5 Meta: clean closeouts, zero YEYOU flags (waivable), current | **MET on closeouts; CONFIRM condition NOT YET TESTABLE** | Closeouts: 9/3 EVE (fa5e2604a), 9/3 AM (42202174a), 9/2 EVE (79dbfe69f), 9/2 (95e104c30), 9/1 ×2 — each a STANDARD with gate PASS recorded in the message; one **un-closed afternoon session 9/3** (`prome-d6`, 12:0x→18:22) folded into the evening closeout (STATUS `:2`) — a session that ended without closeout is a closeout-discipline miss, self-reported. YEYOU: zero findings all-time (waived). Currency: every rail stamped 9/3. |

**Recommendation on Conf M → H:** **HOLD at M until the 9/6 sweep**, and the single deciding fact is **§4b R1 — GATE-LIQ-079's 350-char state cell against PROME's own ≤220 rule (8/29), registered 9/3 with no check**: it is a *new* own-rule-unexecuted instance inside the 21-d window, of exactly the class the 8/17 grade named as the L5 blocker ("the CLASS (rules unexecuted)", FLEET_MAP_HISTORY 8/17). If the sweep rules that class must be ZERO, the condition fails on this row alone (with R4/D-1 and R19/D-9 as second and third instances). If the sweep rules on *scripted-family* execution only, every family fired and the grade lifts. That is the sweep's adjudication, not this reader's.

---

## 8. Open questions for PROME (phrased for DAEDALUS to ask)

| # | Question | Why it matters |
|---|---|---|
| Q1 | What does "spine re-base 8/20" (FLEET_MAP row, the profile's named refresh trigger) refer to? No commit on 8/20 touches BOOT/CLOSEOUT/CLAUDE/SYSTEM; only HEARTBEAT re-based that day (cf3a0d5bf). Was the trigger the 8/9 CLOSEOUT prune (b2ada2fa0) or the 8/29 runner day? | Fixes the profile's trigger clause so `profile_clock_check.py` fires on a real event |
| Q2 | Where did 24,448 B (HEARTBEAT, DOCKET L257 / SCRATCH §5) come from — `measure.py` on an uncommitted intermediate, or a char count? | D-1; decides whether L257's re-base premise stands |
| Q3 | Is GATE-LIQ-079's 350-char cell a knowing exception (owner-declared UNGRADEABLE needs the prose) or a miss? Should `check_gates_tsv` enforce ≤220? | D-2 / R1 — the L5 deciding fact |
| Q4 | ORCH_LOG: is there a rotation intent (e.g., closed-out desks' touches roll to archive), and who is its byte owner given WALTER reads it every boot? | D-3 |
| Q5 | Should `reads_check.py --agent PROME` run inside `prome_gate boot`? PROME wrote the manifest and the checker but never invokes it for itself. | D-9 / R19 |
| Q6 | Are closeout-time whole reads (CLOSEOUT.md 92%) inside the READ_CAP perimeter, or is READS.tsv boot-only by ruling? | D-6 |
| Q7 | `recurrence_rate.py` (8/23): what invokes it, or is it a one-off analysis? | D-10 |
| Q8 | The 9/3 afternoon session `prome-d6` ended without a closeout (STATUS `:2`); is that a Bounce that was never re-entered, or a harness crash? Does the L5 "clean closeouts" leg count it? | L5 leg evidence |
| Q9 | WILL_QUEUE rows 159/162 sit RULED-in-OPEN — does the MISFILED regex see a `**RULED` lead token? | D-7 |
| Q10 | Is the ≤600 B/§ HEARTBEAT paragraph target (four §§ over at Am.#4) going into `check_byte_budgets` with the 9/4 re-base, or staying prose? | R15 |

---

*Measured 2026-09-03; every byte figure is `wc -c` at HEAD 658e6cd3b; nothing outside this file was written.*
