# VIOLET Maintenance Log

Reverse-chronological log of **structural** changes to VIOLET's docs, folders, scripts, and SPAWN/write-back protocol. Each entry: **Trigger / What changed / Files touched / Boot-impact / Lessons**. Answers *"why is VIOLET organized this way?"*

**Distinct from:**
- `thesis/CHANGELOG.md` — **analytical** changes (thesis version bumps, POV pivots, conviction shifts, prediction resolutions).
- `SCRATCH.md` — **ephemeral** per-session handoff (overwritten every write-back; structural changes noted there do NOT persist — they persist HERE).

Log material structural changes only — not routine content edits. Template adopted from OTTO (2026-06-10), incl. the cap: **archive to `archive/` if this grows past ~300 lines** (SAM cautionary tale: 636).

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
