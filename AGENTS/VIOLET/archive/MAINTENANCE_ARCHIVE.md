# VIOLET Maintenance Log — ARCHIVE

> **Archived 2026-07-30** from `MAINTENANCE.md` on its own ~300-line cap (it had reached 315).
> Contains every structural entry dated **2026-06-10 and earlier**, verbatim. The live log keeps 2026-06-11 onward.
> This file is **not boot-read** — it exists so the "why is VIOLET organized this way" trail survives the cap.

---

## 2026-06-10 (evening) — Two derivation scripts built (RED-sweep adjudication session)

**Trigger:** RED red-team sweep (CHG-RED-033/034) demanded empirical derivations: the close-and-hold sustain count and the first-fire-anchor ladder column. Both were one-off queries worth keeping rerunnable (the /tmp-loss lesson, SCRATCH carry-forward).

**What changed:**
- **`scripts/sustain_run_query.py` built** — max consecutive-close runs above each early40 episode's +50% line (n=5 derivation, KB-VIO-088). Reconciled exactly vs Orch answer key after one construction catch: **DIET-class-only clustering is canonical** (DIET∪STRICT shifts the 2024-12 anchor and admits the all-STRICT 2015-10 cluster).
- **`scripts/two_anchor_ladder.py` built** — first-fire-anchor ladder column + path-conditioned subset (KB-VIO-089). Every count reproduced exactly by Orch recompute.
- **Both scripts carry window/calendar conventions inline** (td-not-calendar, 61-closes-inclusive, closes-only, clustering rule) — KB-VIO-084/085 construction-note rule applied prospectively to tooling (Orch condition on the 034 green light).

**Files touched:** scripts/sustain_run_query.py (new), scripts/two_anchor_ladder.py (new), TRADE.md (falsification architecture + two-anchor corollary), workbook/KB.tsv (088/089), research/2026-06-10_red_sweep_response.md (new).

**Boot-impact:** none — both are on-demand derivation tools, not boot-sweep members.

**Lessons:** (1) A derivation can return "this instrument can't catch the failure class you're aiming at" — run-length had no discriminating power (dest-right and dest-wrong both ran 4); the register must state the *role* (tail-stop), not just the number. (2) Clustering construction is part of a number's identity, same family as anchor/unit — scripts should name it inline.

## 2026-06-10 (PM-5) — MEMORY.md subtraction pass (SCRATCH item 7a, pulled forward by Will; Orch-verified plan)

**Trigger:** Will pulled the queued MEMORY subtraction job forward (~3:30 PM). Plan reviewed by Orch with one hard correction (the "24-td gap" figure VIOLET was about to transcribe is a calendar/td mislabel — actual 17 td) and one approved decision (analogs → compressed lessons-only, not pure pointer, because MEMORY is boot-read and the thesis is not).

**What changed:**
- **~430 → ~200 lines.** Pointer-ized to thesis (canonical): REGIME DEFINITIONS (§ REGIME-DEPENDENT BEHAVIOR) and the ~50-line CREDIT-TO-VOL four-model synthesis (§ CENTRAL CLAIM + lag table). HISTORICAL ANALOGS compressed to a trigger-class/credit-lead/lesson table + **Jun 2026 NFP-shock episode added** (was missing — most decision-relevant analog).
- **Factual fixes, all verified against raw data before writing:** Principle 9 (R12 interrupted-and-resumed, 17-td gap) · Principle 10 ("sustained breaks have not occurred" was FALSE — daily-close runs 4 td 5/5-5/8 and 8 td 5/18-5/28, metric named) · TERM STRUCTURE section's "Inversion → Trade: Long vol" advice removed (contradicted own Prediction-#2 falsification, KB-VIO-034) · VVIX rare-trigger caveat (v3.4) + conditional-percentile discipline added.
- **Apr 12 "Open Questions for Will" retired** — all 3 resolved by events (boot.py automation; M1:M2 wired; messaging overhaul). Dispositions kept in session-notes intro.
- **Session notes reordered chronologically + compressed** (blow-by-blow → KB/research pointers; calibration takeaways kept) + **6/5-9 NFP-arc note added** (the scoped gap).
- **METRIC SEMANTICS gains calendar-vs-td rule** (KB-VIO-085).
- **By-catch fixes outside MEMORY:** thesis ×3 "24-td" → 17-td (24 calendar); KB-VIO-072 [COUNT CORRECTED] preamble (KB-VIO-051/058 pattern) + KB-VIO-085 logged; `scripts/convexity_read.py:43` comment re-pointed from MEMORY regime defs to the thesis section (Orch consumer-grep by-catch).

**Files touched:** MEMORY.md (rewrite), thesis/VIX_THESIS.md (3 count fixes), workbook/KB.tsv (072 preamble + 085), scripts/convexity_read.py (comment), MAINTENANCE.md (this entry).

**Boot-impact:** MEMORY.md is boot step 3 — boots now load ~230 fewer lines, with regime/transmission frameworks read from their canonical homes instead of drifting copies. No script behavior change.

**Lessons:** (1) A remediation plan is itself a transcription surface — the "24-td" error was upstream (thesis/KB) and got caught only because the verification pass recomputed rather than re-read; durations carry units like rates carry (threshold, tier, unit). (2) TSV edits via Python: plain string ops, NOT csv.writer (default quoting re-quoted 24 untouched rows on first attempt; caught by `git diff` before commit, reverted). (3) Boot-read vs write-back-read distinction decides pointer-vs-compress: the analogs stayed local *because* MEMORY is the only pattern library loaded every session.

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

## 2026-06-10 (PM-4) — CALENDAR.md fixes + FOMC day-count correction (housekeeping item 4 of 4)

**Trigger:** root-md audit item 5 (Data Refresh table stale, vix_options row wrong twice, footer drift) + the verify-item: CALENDAR's FOMC table disagreed with CATALYSTS.tsv on decision days.
**What changed:** FOMC day-counts corrected against the Fed's published calendar — **Jul 28-29** (was 29-30) and **Sep 15-16** (was 16-17); CATALYSTS.tsv decision-day rows (Jul 29, Sep 16) were already correct, so the canonical→mirror direction held (machine feed right, human twin drifted — KOYOMI/FASTOW date-verification class). "Sep expiry same day as FOMC+SEP" claim survives (both Wed Sep 16). Data Refresh table re-stamped to actual with automation framing fixed ("overdue" vix_options row → every-boot-auto + after-hours artifact note; "COT when wired" → wired; FRED-rates lag flagged with pointer to the diagnosis item); VIX9D added to the spot row; footer bumped.
**Files touched:** CALENDAR.md. **Boot-impact:** none (catalyst_countdown reads CATALYSTS.tsv, which was already correct).
**Lessons:** mirror-drift direction confirmed canonical-wins (auto-memory `[[finding_doc_mirror_consistency_check]]`); meeting-date ranges drift in human twins even when decision-day rows are right — verify day-counts at source before editing either file.

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

*Archived 2026-08-18 on the ~300-line cap (CLAUDE.md step 13a): the two 2026-06-11 entries below were the oldest still in the live log.*

## 2026-06-11 (late eve) — fred_fetch.py SERIES expanded: tree ladder + global-HY control groups

**Trigger:** Will query ("any additional useful FRED 6/10 data we can reach?") → extended pull found the June widening is US-local (KB-VIO-097: Euro HY/EM tightened while the US quality ladder ground wider). Wiring it up revealed the gap: `fred_fetch.py` SERIES carried only HY/IG/CCC — **the KB-VIO-090 tree's own conversion lines (BB ≥1.73, CCC−BB dispersion) weren't in the scripted fetch** and had been pulled ad hoc each session.

**What changed:** `SERIES` dict +2 groups: `credit_ladder` (BAMLH0A1HYBB BB, BAMLH0A2HYB single-B, BAMLC0A4CBBB BBB-rung) and `credit_global` (BAMLHE00EHYIOAS Euro HY, BAMLEMHBHYCRPIOAS EM HY corp — the KB-VIO-097 US-local-vs-global control pair). Verified: all 11 series fetch clean, caches current through 6/10 (correct T+1). Side-finding: DGS10/DGS2 current through 6/10 — the SCRATCH-7f rates-lag bug did NOT reproduce tonight.

**Files touched:** scripts/fred_fetch.py, workbook/fred_cache/ (11 fresh CSVs).

**Boot-impact:** none automatic — **boot.py does not call fred_fetch.py** (credit pulls remain a manual session step; the CALENDAR "per boot" row overstates this). Candidate future change: add a fred_fetch step to boot.py — defer to a deliberate protocol pass, not tonight.

**Lessons:** a registered decision tree's trigger lines should be in the scripted fetch the day the tree is registered — the tool lagged the framework by two days; caught only because a side-query walked the same ground.

---

## 2026-06-11 — Tick/settle mechanization: VX_DAILY schema v2 + convergence_score.py (CHG-RED-037 ship)

**Trigger:** The owed M1:M2 settle re-pull found the "+7.98% re-armed" 6/10 read was actually the **6/9 settlement** — `vix_futures.py` defaults to `date.today() − 1` and `thresholds.py` stamped the value with the row date. Every VX_DAILY m1m2 entry was systematically T-1 vs its row label (verified to 3 decimals on 6/8/6/9/6/10). Fourth settle-class error in 48h → RED's CHG-RED-037 mechanization proposal shipped same session, ahead of Packet #1 (ordering argument in the sweep response, dialogue Q5).

**What changed:**
- **`workbook/VX_DAILY.tsv` schema v2:** +`basis` (TICK/SETTLE by 16:15 ET pull time) and +`m1m2_settle_date` (carried from vix_futures' own `as_of`). All 140 rows migrated (padded; the three verified rows 6/9-6/11 populated [CONF], older rows documented-empty — semantics: m1m2 is T-1 vs row date by construction pre-schema-v2). Consumers (backfill.py DictReader, convexity_read.py pandas — column-name-based) verified parsing post-migration. Backup at `workbook/VX_DAILY.tsv.bak` (trash after a clean week).
- **`scripts/thresholds.py`:** prints "⚠️ BASIS: TICK" on pre-16:15 runs; labels M1:M2 "[settle DATE — T-1 vs row date]"; new `--supersede` flag (EOD SETTLE run replaces an intraday TICK row — previously the append skip baked ticks into the permanent record; TICK never overwrites SETTLE).
- **`scripts/convergence_score.py` built** — mechanical matrix sum from STATUS emoji rows, fails loud on mismatch with the declared score (the hand-sum erred twice in 48h, opposite directions). Write-back now runs it.

**Files touched:** workbook/VX_DAILY.tsv (+2 cols), scripts/thresholds.py, scripts/convergence_score.py (new), workbook/KB.tsv (090-093), TRADE.md (CCC tree pointer + LIQUID mis-attribution fix), research/2026-06-10_red_sweep_response.md (035/036/037/Q6 sections).

**Boot-impact:** boot.py unchanged (thresholds runs inside it; new labels appear in boot output). **New write-back habit: EOD `thresholds.py --supersede` after 16:15 ET on days with an AM boot row; run `convergence_score.py` whenever the matrix changes.**

**Lessons:** a tool default (`date.today()-1`) silently misaligned data-date vs row-stamp for the series' entire life; the fix is carrying the data's own as-of date through the pipeline, not vigilance. Same family as KB-VIO-085 (a number carries its unit) — a value also carries its *date*.

---

---

> **Second archival pass 2026-09-04** — `MAINTENANCE.md` hit **317 lines** against its ~300 cap (boot had been flagging it every session). Moved the three oldest live entries (**2026-06-13 · 06-14 · 06-23**) here verbatim; the live log now keeps **2026-07-11 onward**. Cap cleared to 300 with headroom for the entry that triggered the pass.

---

## 2026-06-23 — Credit-gate summary wired into boot.py (closes the boot/credit blind spot)

**Trigger:** At the 6/23 boot (after a 9-day dark gap spanning the BOJ/FOMC catalyst window), VIOLET mis-read the credit gate as "fred_fetch broken / gate UNCONFIRMED." The proximate bug was a read-side glob over a proliferated cache (KB-VIO-103→104, fixed same session), but the deeper gap was that **boot.py never surfaced the credit gate at all** — fred_fetch was a manual session step, so the load-bearing CCC/Bin-B verdict wasn't in the boot brief. Will-approved wiring it in. Also reconciles a doc drift: VIOLET's CLAUDE.md SPAWN step 5 already described boot.py as "live vol surface + **FRED credit** + catalyst countdown," but boot.py did not run FRED.

**What changed:**
- **`scripts/boot.py`:** added BOOT_SEQUENCE step `("Credit gate (FRED · KB-VIO-090/096)", "fred_fetch.py", ["--summary"], True)` after thresholds. Added markers to KEY_MARKERS (`CREDIT GATE`, `VERDICT`, `CCC`, `Bin-A`, `🟢`) so the gate verdict survives the collapse filter — the `🟢 BLOCK LIFTED` case wasn't a marker before and would have been hidden. Tested: collapsed boot now prints the CCC value, CCC-BB dispersion, and the `VERDICT: 🟢 BLOCK LIFTED / 🟠 BIN-B / 🔴 BIN-A` line; 2.1s cached, non-destructive (VX_DAILY 6/23 SETTLE row untouched).
- Relies on fred_fetch's `--summary` + freshness-aware cache (KB-VIO-104): boot serves credit from cache when fresh, fetches only when stale.

**Files touched:** scripts/boot.py, CALENDAR.md (Data Refresh row Manual→auto-in-boot + boot-sequence line), MAINTENANCE.md.

**Boot-impact:** boot.py now prints the credit-gate verdict every session (~+2s cached). The CALENDAR "boot.py does NOT call fred_fetch" note is SUPERSEDED; the CLAUDE.md SPAWN-step-5 "FRED credit" description is now accurate (code caught up to the doc). fred_fetch stays runnable standalone (`--force --summary`) for an authoritative refresh.

**Lessons:** a load-bearing input that isn't surfaced at boot is a latent blind spot — the 9-day-gap credit mis-read happened partly because the gate was never in the boot brief. Wire the load-bearing reads into the auto-boot, and keep the docs that *describe* boot in sync with what boot *runs* (the CLAUDE.md description had drifted ahead of the code; now reconciled). A new output line must also clear the output filter — adding the step without the KEY_MARKERS would have run it silently.

---

## 2026-06-14 — m1m2 backfill: warn-and-proceed → hard gate (Orc verification of 6/13 commit)

**Trigger:** Orc cross-container review of the pushed Friday-close work found one real gap: `backfill_m1m2()` printed the convention hazard then fell straight into the fill loop — no early return, no override gate. The skip-if-present guard only protects cells that ALREADY hold a value, so a future session running `backfill.py` (full, default) or `--m1m2-only` would still fill the ~79 blank m1m2 cells with same-day/unstamped values inconsistent with thresholds.py's T-1 series — the warning just scrolls past. The 6/13 docstring/commit said "BLOCKED"; the code only WARNED. Accident-proofing a session that never saw this thread was the whole point of the guardrail.

**What changed:**
- **`scripts/backfill.py`:** `backfill_m1m2()` now takes `allow: bool=False` and **early-returns (prints `⛔ REFUSING`, returns 0) unless `--allow-m1m2` is passed.** New `--allow-m1m2` CLI flag (default off). `main()` passes `allow=args.allow_m1m2`. Default `backfill.py` run now does spot only; the m1m2 path is genuinely blocked, not warn-only. Docstring + usage corrected to match. Tested: `backfill_m1m2(..., allow=False)` returns 0 and mutates no rows without any network call.
- **MAINTENANCE 6/13 entry:** "BLOCKED" claim corrected inline (it was aspirational as shipped that day).

**Files touched:** scripts/backfill.py, MAINTENANCE.md, STATUS.md (line-19 vestigial parenthetical dropped + 20d-SKEW-avg recompute — see below; analytical, not structural).

**Boot-impact:** none (backfill.py is not in boot.py). Behavioral: a default/`--m1m2-only` backfill no longer silently injects same-day values; recovery via `--spot-only` is unchanged and still the routine path. The #4 convention decision is still open — `--allow-m1m2` is the deliberate override to be used ONLY after it resolves.

**Lessons:** a documented hazard is not an accident-proof one — "BLOCKED" in a docstring while the code warns-and-proceeds is the gap between intent and enforcement; when the point of a guard is to protect a future unaware session, the guard must REFUSE, not narrate. (Reinforces the 6/13 lesson: surface — and here, *enforce* — the guard before it's relied on.)

---

## 2026-06-13 — Supersede limits surfaced: boot-time stale-TICK guard + m1m2 convention landmine pinned

**Trigger:** Weekend refresh found the VX_DAILY 6/12 row stuck as a stale morning TICK (VIX 19.04 vs 17.68 settle). Root cause (Orc): Friday's session closed 1:40pm, before the 16:15 ET settle, so the EOD `--supersede` never fired — and `--supersede` only ever targets *today's* row (stamps `et_now`), so it can NEVER reach back to repair a prior date; a stale row does not self-heal on re-run. The weekend-skip guard was a red herring (it only blocked the Saturday catch-up). Investigating the repair path surfaced a second landmine: **thresholds.py and backfill.py disagree on the m1m2 convention.**

**What changed:**
- **`scripts/thresholds.py`:** (a) `append_daily_log` now returns a STATUS CODE (appended/updated/skip-weekend/skip-exists/skip-tick-vs-settle/skip-no-file) instead of a bare bool — the old bool made every skip print the misleading "already has a row" line (which fooled VIOLET herself: the real reason was the weekend guard). Printer states the real reason + points to backfill.py. Bool back-compat preserved for `--json`. (b) New `check_stale_tick()` boot-time guard: emits a `⚠️` (surfaced by boot.py collapse) when the LATEST VX_DAILY row is a TICK dated before today — catches the missed-EOD case at next boot, which is the case that actually failed (a closeout checklist can't catch it; nothing is alive at 16:15 ET close). Tested both branches.
- **`scripts/backfill.py`:** m1m2 CONVENTION HAZARD pinned — docstring block + runtime `⚠️` print in `backfill_m1m2()`. This path writes SAME-DAY/unstamped m1m2; thresholds.py writes T-1 WITH `m1m2_settle_date`. The two disagree; the ~79 blank m1m2 cells are protected only by the skip-if-present guard. *(NOTE — corrected 6/14: as shipped this day the guard only WARNED-then-proceeded, NOT "BLOCKED" as this line originally claimed; a default `backfill.py` run would still have filled the blank cells. Hard gate added 6/14 — see entry below.)*
- **Data fixes (not structural, logged for trail):** VX_DAILY 6/12 spot row hand-backfilled to settle then m1m2 reverted to T-1 (6.49/settle_date 6/11) for series consistency; 6/10 skew fixed 141.97→143.08 via `backfill.py --spot-only` (was a dup of 6/09).

**Files touched:** scripts/thresholds.py, scripts/backfill.py, workbook/VX_DAILY.tsv (6/10 + 6/12 rows), MAINTENANCE.md.

**Boot-impact:** boot.py unchanged in structure (thresholds runs inside it); the new stale-TICK `⚠️` now appears in boot output whenever an EOD settle run was missed. **Open decision #4 (NOT done): m1m2 convention — migrate the whole series to same-day (Orc's lean: semantically correct for a "daily closes" ledger; KB-VIO-092-proof) vs document T-1 as canonical + align backfill. ~79-row migration touching both tools; needs the echo-back loop, not a snap. Until resolved: `--spot-only` only.**

**Lessons:** a tool whose write is keyed to "now" (not to the data's own date) cannot repair history — the recovery tool must be date-driven (backfill.py). Two tools touching one column under different conventions are safe only by an undocumented guard; surface the guard before it's relied on. And: a skip/error message must state *which* reason fired — a generic message cost a self-misread.

---
