# VIOLET Maintenance Log

Reverse-chronological log of **structural** changes to VIOLET's docs, folders, scripts, and SPAWN/write-back protocol. Each entry: **Trigger / What changed / Files touched / Boot-impact / Lessons**. Answers *"why is VIOLET organized this way?"*

**Distinct from:**
- `thesis/CHANGELOG.md` — **analytical** changes (thesis version bumps, POV pivots, conviction shifts, prediction resolutions).
- `SCRATCH.md` — **ephemeral** per-session handoff (overwritten every write-back; structural changes noted there do NOT persist — they persist HERE).

Log material structural changes only — not routine content edits. Template adopted from OTTO (2026-06-10), incl. the cap: **archive to `archive/` if this grows past ~300 lines** (SAM cautionary tale: 636).

---

## 2026-06-10 (PM) — SIGNAL_INTAKE.md rebuilt as WALTER subscription spec (orchestrator-verified; housekeeping item 1 of 4)

**Trigger:** Root-md audit flagged SIGNAL_INTAKE.md as the worst behavioral-risk doc (unqualified-94% sizing, falsified inversion-as-leading-indicator, pre-Episode-17 vehicle default, HERMES-era protocol). Orchestrator packet superseded the rehab plan with a decisive fact neither reviewer caught by reading: **the file is WALTER's per-agent subscription spec** (template `AGENTS/WALTER/design/SIGNAL_INTAKE_TEMPLATE.md` v0.1; STATE.md §8 rollout VIOLET ✅). VIOLET pushed back twice, both accepted amended: (1) ROUTING_TABLE.md `MARKET_VOL` row routes nothing to VIOLET (HENRY|LIQUID|LIQUID,RED — predates the HENRY/VIOLET vol-ownership split) → flag-to-WALTER promoted to load-bearing deliverable, row-split proposal; (2) Prome's "perishable live levels" ACTIVE THRESHOLDS instruction contradicted CARL's post-5/31 reference pattern (section deleted as drift hazard) → lines-only middle path adopted, HY/CCC episode-gates cut.

**What changed:**
- Old file (Apr 12 structure — never template-conformant; STATE.md's ✅ meant "exists") → `archive/SIGNAL_INTAKE_2026-04-12_pre_template.md` via git mv. Episode database + watch tables preserved there; canonical homes are MEMORY/thesis.
- New `SIGNAL_INTAKE.md`: CARL-pattern "how to read" header (live-source map + boot-self-pull rule: route news/events/reads, not raw data) + 3 priority tiers + keyword confidence tiers + WHAT-NOT-TO-SEND with redirects + **4 durable threshold lines only** (VVIX 120; VIX3M/VIX <1.0 labeled peak-marker/exit-timing per KB-VIO-034; 20d-SKEW <140 sustained 4+td; VIX 30/40) with CARL-divergence + self-destruct condition documented inline + outbound pointer to step 12. No sizing/94%/vehicles anywhere (owner docs: TRADE/thesis, KB-VIO-079).
- `[verify with owner]` flags preserved on other agents' vocabulary (Scenario D, SOFR-IORB >0.25, gold margin cascade) — never invented replacements.
- CLAUDE.md FILES row added (consumer + template review triggers). Draft + 3-part WALTER flag at `research/2026-06-10_signal_intake_REWRITE_DRAFT.md` Appendix A (MARKET_VOL split proposal / spec-rebuilt notice / BOARD consumption unwired — relay via Will; VIO-T-NN registry end-state named, not built).

**Files touched:** SIGNAL_INTAKE.md (rebuilt), archive/SIGNAL_INTAKE_2026-04-12_pre_template.md (new via git mv), CLAUDE.md (FILES row), research/2026-06-10_signal_intake_REWRITE_DRAFT.md (draft, committed earlier), MAINTENANCE.md (this entry), auto-memory finding promoted.

**Boot-impact:** none — SIGNAL_INTAKE.md is not in the boot read-set; WALTER consumes it at its design passes (runtime routing is ROUTING_TABLE.md, which is why the flag matters more than the rewrite).

**Lessons:** (1) **Grep for consumers outside your own directory before restructuring/retiring any file** — two reviewers graded this file by reading it; the decisive fact was only visible by searching for who reads it. (2) **Check the current reference implementation, not just the template** — CARL had evolved past the template's own instructions (dropped ACTIVE THRESHOLDS as a drift hazard); conforming to the spec doc alone would have rebuilt the disease. Both promoted to auto-memory (`finding_external_consumer_check_before_restructure`).

---

## 2026-06-10 (PM-3) — CLAUDE.md residue pass (housekeeping item 3 of 4; Will-reviewed draft, approved)

**Trigger:** root-md audit item 3 + full condition report (`research/2026-06-10_claude_md_condition_report.md`). Spine was healthy; lines ~95-168 were April-bootstrap residue with two self-contradictions (HERMES boundary rule vs MAIL/step 12; dangling "Outbox Protocol" ref in step 13) and one falsified teaching (KEY THRESHOLDS "inversion = leading indicator" vs v3.1/KB-VIO-034).

**What changed (fixes 1-10 + decisions A/B; draft + diff summary at `research/2026-06-10_claude_md_REWRITE_DRAFT.md`):**
- Boundary rule + step-13 tail → NEXUS_BRIEF CROSS-DOMAIN / outbox-🔴-acute (HERMES + dangling ref killed).
- KEY THRESHOLDS table (TBD column since April, falsified inversion framing, weak single-day SKEW-140 line) → 3-pointer THRESHOLDS block, zero values restated (SIGNAL_INTAKE lines / STATUS live / thesis logic).
- CROSS-AGENT SIGNALS: send-table kept (VIOLET-owned trigger definitions; inversion row re-framed peak-marker broadcast); delivery-mechanism line added; receive table → SIGNAL_INTAKE pointer (inbound owner; kills the drift-twin).
- CONVERGENCE MATRIX: 5-point scale + STATUS-must-include requirement kept; 5 template rows (⚪/TBD/"Never") deleted; N/(5×vectors) scoring note added.
- RESEARCH PRIORITIES (April list, all done/falsified/tooled) → pointers to STATUS queue + thesis.
- OUTPUT RULES: nonexistent `domain/sources/` path → `research/ or archive/`.
- DOMAIN SCOPE: VIX1Y (never tracked) out; VIX9D+ratios, M1:M2 curve shape, SKEW 20d-avg, COT in; BRENT/HAWK-oil + SAM-carry NOT-own rows with transmission-read carve-outs.
- Header network line aligned to both surfaces (NEXUS_BRIEF out / SIGNAL_INTAKE in) + SAM/BRENT edges.
- **Decision A (Will-approved): `workbook/VX.tsv` RETIRED** → `archive/VX_2026-04-15_threshold_dashboard.tsv` via git mv (dead since 4/15; VX_DAILY owns the daily series, SIGNAL_INTAKE/STATUS/thesis own threshold lines). Step 8 + FILES table updated.
- **Decision B (Will-approved): `workbook/FLOW.tsv` RE-SCOPED** to formal sends only; 5/21 HENRY LIAISON row backfilled + dated rescope-note row added (no other formal sends 4/15→6/10).
- **Decision C (BOARD consumption boot step): DEFERRED** until WALTER answers the MARKET_VOL routing flag. **Decision D (boot predictions-due scan): named as future build item.**

**Files touched:** CLAUDE.md (rewrite), workbook/VX.tsv → archive/ (git mv), workbook/FLOW.tsv (2 rows), MAINTENANCE.md (this entry), research/ draft + condition report (committed earlier).
**Boot-impact:** none mechanical (boot.py untouched; no script read VX.tsv — verified by SAM-pattern precedent and grep). Behavioral: fresh spawns no longer get contradictory routing guidance or the falsified inversion teaching; MEMORY-subtraction session will need a touch on boot step 3's description when it runs.
**Lessons:** template residue survives because protocol files get amended at the top (spawn steps) and never re-read at the bottom; a full-file condition report before editing catches self-contradictions that section-level edits keep missing. By-catch class repeated: STATUS "1 pending inbox signal" was stale propagation — the 5/14 signal was dispositioned 6/6 (fix at EOD re-stamp).

---

## 2026-06-10 (PM-2) — README.md refreshed (housekeeping item 2 of 4)

**Trigger:** root-md audit item 2 (front door pointed at retired `LAST_COMPLETION.md`; quoted the unqualified 94%; map omitted SCRATCH/NEXUS_BRIEF; network section was messaging-era).
**What changed:** directory map rebuilt (LAST_COMPLETION out; SCRATCH/NEXUS_BRIEF/MAINTENANCE/thesis-CHANGELOG/COT_VIX/CATALYSTS in; archive note updated for pre-template SIGNAL_INTAKE); Core Thesis re-stated as 3 durable pillars with the threshold-indexed L1 rates (KB-VIO-079 usage rule inline) + inversion-marks-peaks (KB-VIO-034) added as pillar 3; cross-agent section rewritten to current surfaces (NEXUS_BRIEF primary / outbox 🔴-acute / WALTER-routed inbound per subscription spec / VIOLET-owned vol broadcast).
**Files touched:** README.md. **Boot-impact:** none (not in boot read-set; first-orientation doc for fresh spawns/external readers).
**Lessons:** none new — this was execution of the audit finding (README is now covered by the same drift fix as SIGNAL_INTAKE: pillar rates point at the canonical table instead of carrying their own copy).

---

## 2026-06-10 — MAINTENANCE.md created + root .md audit (the trigger for the upcoming housekeeping wave)

**Trigger:** Will-directed audit of all 9 root .md files, then "do you have a MAINTENANCE.md?" — VIOLET didn't (SAM/OTTO/RED/MARCO do). Audit root cause made the case: the rot was concentrated in UNOWNED docs (README.md + SIGNAL_INTAKE.md appear in no maintenance table), and VIOLET's structural record lived only in overwritable SCRATCH + git archaeology.

**What changed:**
- **New `MAINTENANCE.md`** (this file) — OTTO template (Trigger/What/Files/Boot-impact/Lessons, ~300-line archive rule). Backfill below is condensed (5 waves, dated from git); full detail stays in git log.
- **`research/2026-06-10_root_md_audit.md`** — audit findings, ranked by behavioral impact. Headline items queued (in order): 🔴 SIGNAL_INTAKE.md rehab (unqualified-94% sizing [KB-VIO-079 class] + falsified inversion-as-leading-indicator + pre-Episode-17 vehicle default + HERMES-era protocol); 🟠 README.md refresh (points at retired LAST_COMPLETION.md; unqualified 94%); 🟠 CLAUDE.md residue pass (KEY THRESHOLDS all TBD, convergence template rows, HERMES boundary rule vs MAIL section contradiction, outbox-for-🟠 vs NEXUS_BRIEF-primary contradiction, April research priorities); 🟡 CALENDAR small fixes (+ verify Sep FOMC day-count vs CATALYSTS.tsv before editing); 🟡 MEMORY.md subtraction job (separate session — footer drift, chrono order, 6/5-6/9 trajectory gap, duplication→pointers).
- **`CLAUDE.md`** — MAINTENANCE.md row added to FILES YOU MAINTAIN; write-back step 13a added (log structural changes here at write-back).

**Files touched:** MAINTENANCE.md (new), CLAUDE.md (FILES table + step 13a), research/2026-06-10_root_md_audit.md (committed earlier same session).

**Boot-impact:** none directly — MAINTENANCE.md is not in the boot read-set (reference doc, read on demand / when asking "why is X organized this way"). Write-back gains step 13a.

**Lessons:** Unowned docs rot silently; an ownership row + a structural log are the cheap fix. Adopt the log BEFORE a housekeeping wave so the wave gets recorded from entry one.

---

## CONDENSED BACKFILL (pre-2026-06-10; dated from git; full detail in git log + research/)

## 2026-06-09 — Orchestrator full-tree review executed (items #1-3) + Packet #2 build + thresholds.py date-bug fix

- **`scripts/convexity_read.py` v0 built** (Packet #2 — convexity-pricing rubric: dual percentile windows 1yr/5yr, VIX-bucket-conditional VVIX, CC+Parkinson realized, event-premium curve location, mandatory carry flag). First live run KB-VIO-078 overturned 2 of 3 answer-key verdicts. Same session: IV-RV positional-join bug fixed → date-keyed join; SPX fetch 320d→450d for honest 1yr percentile. (`3d9df85c`, `35298c3e`)
- **L1 base-rate canonicalized (KB-VIO-079):** threshold×tier×unit table added to VIX_THESIS § OPERATIONAL LAYER STACK; 7 surfaces re-pointed. *(Known incomplete sweep: README.md + SIGNAL_INTAKE.md still carry the unqualified 94% — caught by the 6/10 audit, queued above.)*
- **`TRADE.md` rehabbed:** Episode-17 closed out (had sat OPEN 3 weeks past expiry); Event-Premium Fade framework pre-registered ahead of the 6/10 CPI decision; short-premium sizing column added.
- **`scripts/thresholds.py` UTC→ET date-stamp bug fixed** (evening boot at 20:29 ET wrote a next-day row); VX_DAILY.tsv 6/8 gap backfilled (KB-VIO-076 process lesson: gap-check the ledger after any skipped trading day). (`ca464bc3`)
- **Packet #1 (abstain-gate → v3.6) spec accepted** + refinements → `research/2026-06-09_packet1_abstain_gate_spec.md`; wiring deferred to post-CPI.
- **Boot-impact:** boot.py unchanged; thresholds.py rows now ET-stamped; convexity_read.py is a manual post-print tool (not in boot sweep).

## 2026-06-07 — NEXUS_BRIEF stood up (fleet rollout) + wired into write-back

- **`NEXUS_BRIEF.md` created** per ratified schema (R3 + amendment 7; SAM-drafted fleet template); write-back step 12 added to CLAUDE.md — mandatory every session, minimum As-of stamp + STATUS-commit hash refresh. NEXUS reads this in place of raw STATUS; outbox demoted to 🔴-acute only. (`e5b1d967`)
- Same session: fleet date-fix swept in (May CPI 6/12→6/10 per BLS) across brief + state files. (`b9616991`)
- **Boot-impact:** write-back gained a mandatory step; boot read-set unchanged.

## 2026-06-01 — Closeout protocol codified + SCRATCH replaces LAST_COMPLETION + thesis/CHANGELOG + COT pipeline

- **`SCRATCH.md` created** as canonical next-boot handoff (SAM/CARL/BRENT fleet pattern); **`LAST_COMPLETION.md` retired**. (`ac376e9f`)
- **CLAUDE.md SPAWN PROTOCOL rewritten** as read→write paired boot/write-back spine (BRENT closeout-as-write-back-tail pattern); **`thesis/CHANGELOG.md` added** (old view → new view at each version bump). (`7d8f8fb2`)
- **`scripts/cftc_cot.py` built** (CFTC TFF VIX-futures positioning + 3yr percentiles → `workbook/COT_VIX.tsv`, 178 weeks backfilled; `--boot` freshness-gated, wired into boot.py). (`5446b64e`)
- **Boot-impact:** boot.py now runs thresholds + vix_options + cftc_cot + catalyst_countdown; SCRATCH is boot read #2.
- *(Later refinement, validated 6/5: neutral "Write-back" framing + live-event override clause in EXECUTE — aggressive closeout framing was pulling sessions toward premature closeout mid-event; auto-memory `finding_boot_protocol_live_event_override`.)*

## 2026-04-15/16 — Tooling wave 1 (agent created 2026-04-12)

- **`scripts/boot.py`** (orchestrator), **`scripts/thresholds.py`** (live vol surface + VX_DAILY append), **`scripts/vix_options.py`** (OI snapshots → VIX_OPTIONS.tsv), **`workbook/CATALYSTS.tsv`** + countdown. (`ee293319`, `c51cc1f2`, `72774d88`)
- **`scripts/fred_fetch.py`, `analog_pull.py`, `analog_timeline.py`** (4/16, Phase 2 cluster-analog work).
- Root doc set established: STATUS / MEMORY / CALENDAR / TRADE / README / SIGNAL_INTAKE + thesis/ + workbook/ + research/.
- **Boot-impact:** established the ~10s scripted boot that replaced manual data pulls.

---

*Created: 2026-06-10. Log structural changes at write-back (CLAUDE.md step 13a). Cap ~300 lines — archive overflow to `archive/MAINTENANCE_ARCHIVE.md`.*
