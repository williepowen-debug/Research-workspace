# Agent Profile — RED

> ⚠️ **STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01):** all three file-readable legs: ML-RED-205 > 165 · CHG-046 present · RED-FT-10/11/12 present · body 8/12. Read the FLEET_MAP row (re-cut 2026-09-01) and `upgrades/PRODUCTION_REVIEW_2026-09-01.md` before this body. Refresh checkpoint: **2026-09-08**. *(Bannered by `scripts/profile_clock_check.py` + the PR#5 readers; a banner is a warning, not a fix — PAT-085.)*

**Built by:** DAEDALUS · **Full rewrite: 2026-08-12** (supersedes the 7/4 profile + its 7/22 Δ-banner) · **Method:** 3-reader Mode-A fan-out (spine / workbook+registry / comms+working-dirs) run as the Will-directed architecture audit (`upgrades/RED_AUDIT_2026-08-12.md` = the evidence store; this profile = the durable comprehension), synthesized with each reader's explicit not-read list honored below.
**Read vintage:** RED tip `4b3bb1b55` (S29c, 12:16 ET) for all measurements; **live-updated through `67e31cc7d` (S29e, 14:28 ET)** where marked — RED consumed the audit mid-day across two addendum sessions (S29d closed 3 time-critical findings in 66 minutes; S29e closed R17 and adopted all three PROME amendments), so several audit defects are already CLOSED and marked so here.
**Staleness triggers (file-readable, per PAT-089 fix-form):** refresh §2/§3b when `workbook/ML.tsv` max ID exceeds **ML-RED-165** OR `workbook/CHALLENGES.tsv` contains **CHG-RED-046** OR `registry/FALSIFICATION_TRIGGERS.tsv` contains **RED-FT-10** (all greppable from RED's own ledgers); refresh §4-§6 when RED's dedicated hygiene session lands (the audit batch — grep MAINTENANCE.md for `audit` entries after 2026-08-12). **Hard floor: 2026-09-26** (45d) regardless.

> Durable understanding — section-tasks read THIS, not the raw (heavy, ~240-file) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity
The fleet's **adversarial analyst** — the honesty mechanism. Steelman the strongest "we're wrong" case first, then issue honest odds: hypothesis weights, counter-signal weights, falsification triggers. **Class: Utility** (grade vs `BLUEPRINTS/utility-agent.md`) — owns no domain data, generates no original research. **PULL_COMPLETE since 2026-07-09**: BOARD scan (boot 1.5) is its SOLE WALTER-signal channel; the `inbox/WALTER/` delivery lane is NO-OP by design. Writes challenge packets to `challenges/` (by target), numbered dispatches to `OUTBOX.md` (PROME pickup), loose packets to `outbox/` (read-in-place by recipients). Registry rows in `registry/FALSIFICATION_TRIGGERS.tsv` are consumed by WALTER's boot-6c auto-fire scan. **Grade story: L4 conf-H (8/12 audit: HOLD).** The analytical layer is the strongest DAEDALUS has audited — every 8/12 finding was structural/contract-layer. **Audit-absorption datum: 5 findings spot-checked, 5 verified, 3 closed in 66 min, each with the defect owned in its own ledger row.**

## 2. File anatomy (where the richness lives) — MEASURED 8/12

| File | Size/rows | State | Notes |
|---|---|---|---|
| `CLAUDE.md` | 321 ln | governing | CONTRACT block :22-28 · BOOT 0-9a / WRITE-BACK W1-W10 :36-82 · discipline overlay :84 (stamp = TRIGGER not shield) · FILES tables :195-250 (⚠️ carries the dead-path cluster, §4-D6) |
| `STATUS.md` | 171 ln / 205 B-ln | live, ≤200 local cap | weights table :51-58 · bull steelman :66-74 (BEFORE counter — load-bearing order) · falsification table :99-114 · BOTTOM LINE :165-167 |
| `SCRATCH.md` | — | **sole canonical handoff** | full rewrite each W5 from in-file template |
| `MEMORY.md` + `MEMORY_ARCHIVE.md` | 157 ln / 260 B-ln | boot step 1 | densest spine file; Calibration Record shows its own corrected miscounts — exemplary. ⚠️ :9 carries a dead archive/ link (§4-D6) |
| `MAINTENANCE.md` | 285 ln | structural log | loop-closer rule :10 (fires on SELF-made changes only — PAT-097) |
| `NEXUS_BRIEF.md` | **100/100 ln AT CAP**, 272 B/ln | fleet-facing | Amendment-10 fold-LAST rule :100. ⚠️ chronic addendum casualty (§4-D1); byte-growth PAT-086 shape (lines :21+:100 = 20% of file) |
| `OUTBOX.md` | 24 entries | PROME dispatch ledger | `RED-TO-<AGT>-YYYYMMDD-NNN`, sequence 001-011 unbroken (IDs verified, bodies not read) |
| `outbox/` (dir) | 8 files | ⚠️ UNREGISTERED lane | absent from FILES table; no `delivered/` (25-of-36 fleet convention); **read-in-place by recipients — never grade aging by recipient-copy test, false orphans by construction** |
| `workbook/ML.tsv` | **153 rows**, 14-col, LF | LIVE — crown jewel | zero ID gaps 001-153; self-critical findings log; where RED's learning lives |
| `workbook/KB.tsv` | 85 rows, 13-col, LF | LIVE | Admiralty conf; `Stale_By` date col (the good stamp form). ⚠️ D2 case-split |
| `workbook/CHALLENGES.tsv` | 45 rows, 11-col, LF | LIVE | grade+finding+resolution frozen per row; all 5 ACTIVE rows dated (W2 rule holding since 7/31) |
| `workbook/VX.tsv` | 25 rows, 12-col, LF | ⚠️ **LIVE-STALE — the one rotting ledger** | 13 of 16 live-strength rows unreviewed ≥51d; VX-RED-013 @129d; `Last_Reviewed` is a real date col, unused |
| `workbook/VX_HISTORY.tsv` | 71 rows, 7-col, LF | LIVE audit trail | name-exempt from ledger_staleness (right reason) |
| `workbook/PREDICTIONS.tsv` | 21 rows, 10-col, LF | LIVE | 8W/12C/1A (RED-04 → 9/30); boot.py parses fuzzy Timeframe |
| `workbook/FLOW.tsv` | 7 rows + banner | **FROZEN 7/5 — exemplary banner** | names successors + do-not-cite; W6's FLOW leg dead by design |
| `workbook/SCHEMA.tsv` | 84 rows, 5/6 | ⚠️ **stale contract** | last touched 5/6; documents 8 registry cols of 12; no CATALYSTS/WATCHLINES coverage; 4 value domains drifted (§4-D3) |
| `registry/FALSIFICATION_TRIGGERS.tsv` | **9 rows** (FT-01..09), 12-col | LIVE, WALTER-consumed | high content / low machine-legibility (§4-D4); FT-08 machine form CORRECTED S29d |
| `docket/CATALYSTS.tsv` | 64 rows, 9-col | LIVE canonical | CALENDAR.md = narrative twin, canonical-wins; WAL V4 8/13 row added S29d |
| `docket/WATCHLINES.tsv` | 12 rows, 11-col, **CRLF (sole CRLF file)** | LIVE | **best-specified surface RED owns** — fully machine-evaluable Source/Op/Threshold/Sustain |
| `board_log.tsv` | 119 rows | ⚠️ dormant-by-orphaned-obligation | see §4-D5 |
| `challenges/` (21) `research/` (16) | bimodal | LIVE tail | Feb-Apr dead cohort + Jul/Aug live accrual |
| `reports/` (5) `counter-evidence/` (1) `design/` (1) | dead cohorts | unbannered-historical | reports/ nothing since 6/11; counter-evidence superseded by VX.tsv but KRE_BULL_CASE.md is MEMORY-referenced — keep |
| `thesis/` | 4 files, **four clocks** | mixed | CHANGELOG 93KB LIVE (S27/28/29 ✓) · TIMELINE 51d claims-current · FRAMEWORK 132d (stable rubric, fine) · PREDICTIONS_README ❌ dead preservation claim (§4-D6) |
| `handoff_WALTER/` | 3 files | HISTORICAL, presents live | README false on two counts (§4-D7); LIAISON open Turn-8 67d |
| `scripts/boot.py` | 242 ln | read-only tooling | registry+WATCHLINES+CATALYSTS+PREDICTIONS+CHALLENGES eval; docstring verified accurate against code; METRIC_MAP **6 metrics as of S29e** (T5YIFR wired → 8 of 9 triggers auto-evaluate). ⚠️ **`CORE-CPI-3MO-ANN` is DELIBERATELY unmapped — a release-derived 3-month compound has no FRED series and failing loud is correct. Recorded as a DECISION, not an omission — do not "fix"** |

**Line-ending reality (replaces the old profile's CRLF table — that table is WRONG):** there is NO stable convention. Two silent whole-file flips in 5 days (LF→CRLF 8/7, CRLF→LF 8/12; VX/CATALYSTS/CHALLENGES). Current: **everything LF except WATCHLINES.tsv (CRLF).** A section-task must re-measure, never trust a stated convention. The 6/23 binary-mode edit guard still applies to whatever is CRLF at read time.

### 2b. BOOT ↔ WRITE-BACK step map (the symmetric spine — read this instead of re-opening `CLAUDE.md:36-82`)

**Every named path verified to resolve, 8/12.** `boot.py`'s docstring checked against its code, not assumed.

| BOOT | Target | ↔ | W-step | Touches |
|---|---|---|---|---|
| 0 | `git pull` (root protocol) | | **W1** | `STATUS.md` — weights (every weight dated), challenges, counter-signals, FT statuses; ≤200 ln local cap, overflow → `reports/` |
| 1 | `MEMORY.md` | ↔ W7 | **W2** | `PREDICTIONS.tsv` + `CHALLENGES.tsv` — resolve every DUE row; **ACTIVE rows MUST carry a resolution date** (ML-RED-125 rule) |
| **1.5** | `/BOARD/INDEX.md` b1-b4 + cross-ref `WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` vs own registry — **SOLE WALTER channel; carries NO ledger obligation (§4-D5)** | | **W3** | `thesis/CHANGELOG.md` — old view → new view |
| 2 | `STATUS.md` | ↔ W1 | **W4** | `docket/CATALYSTS.tsv` (canonical) + `CALENDAR.md` (narrative twin) — **doc-mirror check, canonical wins** |
| 3 | `CALENDAR.md` + CATALYSTS (`pending`, ~14d) + DUE-scan PREDICTIONS/CHALLENGES | ↔ W2/W4 | **W5** | `SCRATCH.md` full rewrite from in-file template |
| 4 | `thesis/CHANGELOG.md` (last 2-3) | ↔ W3 | **W6** | `workbook/` — ML (append-only) · KB · VX + VX_HISTORY · CHALLENGES · ~~FLOW~~ (**dead leg by design, frozen**) |
| 5 | `SCRATCH.md` | ↔ W5 | **W7** | `MEMORY.md` + auto-memory promotion scan; verbose → `MEMORY_ARCHIVE.md` |
| **5.5** | `inbox/WALTER/` — **NO-OP since 7/9; holds the ONLY board_log mandate (the orphan)** | | **W8** | `reports/` · `challenges/` · `OUTBOX.md` · **`NEXUS_BRIEF.md` whenever state moved** ⚠️ *sits late — the addendum casualty (§4-D1)* |
| 6 | mode select (Targeted / Sweep / Ad Hoc) | | **W9** | `MAINTENANCE.md` (structural only) |
| 7 · 8 | target agents' STATUS (first 50 ln) · `PROME/STATUS.md` | | **W10** | git, pathspec `AGENTS/RED/` + `safe-push.sh` |
| 9 · 9a | `scripts/boot.py` (cwd-proof) · `scripts/ledger_staleness.py RED --quiet` (cwd-proof) — **separate steps; boot.py does NOT call 9a, correctly** | | | |

**Addenda truncate from the bottom:** W1/W2/W5/W6 survive a re-closeout; **W3/W7/W8/W9 do not.** That ordering is why NEXUS_BRIEF and OUTBOX are the chronic casualties and MEMORY loses its one-liners (§4-D1).

## 3. Per-dimension (utility floor) — all conformant or better

CONTRACT :22-28 ✓ · role rubric `thesis/FRAMEWORK.md` applied visibly every session ✓ · structured record = best-in-fleet (7 TSVs, RED-unique adversarial schema — VX bull/bear+Flip_If, FLOW break-pathways, CHALLENGES dispute ledger; **NOT DARWIN debt, do not generic-ize**) · calibration loop = PREDICTIONS 8W/12C + CHALLENGE_IMPACT_LEDGER (2/24=8.3% harmful-revision rate, arithmetic verified; ⚠️ population stops at CHG-043, stamp 7/31) · authority = no cross-fleet write power, conformant · boot cwd-proof ✓ (9/9a verified live).

### 3b. Invalidation-surface inventory (sweep form: surface / where / stamp-type / vintage)

| # | Surface | Where | Stamp form | Vintage @8/12 |
|---|---|---|---|---|
| 1 | Hard triggers FT-01..09 | `registry/FALSIFICATION_TRIGGERS.tsv` | ⚠️ **free-text notes col 12** (`FIRED <date> (S<n>)`), no date column | 8/12 S29d. FT-06 FIRED 8/11, exit ≥18 s=5; FT-01 RE-FIRED 8/7 |
| 2 | Trigger exits | same, cols 9-11 | literal `UNDEFINED` token = HONEST (S26 ruling, do not auto-fill) | 2 of 9 defined (FT-01, FT-06) |
| 3 | Soft watchlines WL-01..12 | `docket/WATCHLINES.tsv` | ⚠️ notes-col prose (`RE-ARMED <date>`) | 7/31 relabel; WL-03 RE-ARMED 8/7, 8bps out |
| 4 | SKEW <140 kill (RED owns the line, Will 8/10) | STATUS :106 | ⚠️ **prose-only, no machine vintage** | FIRED S28; 135.59 [8/11] |
| 5 | DIET guard (Acute protection) | STATUS :10/:88 | ⚠️ **prose-only; precondition state VOLATILE** | precondition ABSENT (SKEW sub-140) |
| 6 | Challenge resolution dates | `CHALLENGES.tsv` col 7 | ISO date / dated event (W2 rule enforced) | all 5 ACTIVE dated; CHG-043 → 8/15 |
| 7 | Prediction windows | `PREDICTIONS.tsv` Timeframe | fuzzy-date, boot.py-parsed | RED-04 → 9/30, sole ACTIVE |
| 8 | STATUS falsification table | STATUS :99-114 | narrative mirror, registry-canonical declared | 8/12 |
| 9 | Forward catalysts | `CATALYSTS.tsv` → CALENDAR | date + status enum | 8/12 |
| 10 | CALENDAR watch/backstop sections | CALENDAR.md lower sections | dated blocks — FROZEN whole 7/31 (canonical = TSVs) | header 8/12; bodies unread ⚠️ |
| 11 | VX Flip_If + Last_Reviewed | VX.tsv / VX_HISTORY.tsv | **dedicated date column — RED's best stamp form** | see D-VX staleness |
| 12 | KB Stale_By | KB.tsv | dedicated date column | KB-067 corrected 8/12 |
| 13 | Position/expiry mismatch | thesis/TIMELINE.md | header stamp | ⚠️ 51d, unread bodies |
| 14 | Harmful-revision ledger | CHALLENGE_IMPACT_LEDGER.md | dated rubric + ⚑ rows | ⚠️ 7/31, 12d, 3 challenges moved since |

**⚠️ REPRESENTATION-LAYER WARNING (RED's own S29e finding, PAT-098 — the sharpest thing to carry from this profile):** on this agent the *content* is reliably right and the *machine representation* is where defects live — FT-08's machine columns carried one leg while its prose carried two; boot.py's threshold formatter printed `.0f` so FT-09 rendered "live 2.31 vs >3" (24bps from firing, displaying as 69bps away) on the very line the fix existed to protect; the registry's fire-state is prose a parser cannot read. **Evaluation was correct in every case; only the representation was wrong — and the representation is what a consumer acts on.** When grading or consuming RED, read the authoritative field, never the rendered one.

**Sweep warnings:** (a) rows 1-3 stamp in NOTES columns — a scan keyed on date *columns* reads them as unstamped (`finding_scan_keyed_on_naming_reads_local_form_as_absence`); (b) rows 4-5 have NO machine-readable vintage and both moved this week — the sweep's blind spots; (c) rows 10-14 schemas verified but bodies unread — prioritize 14 (fleet-cited by NEXUS).

## 4. Known defects & deviations — audit-adjudicated, DO NOT RE-DISCOVER

- **D1 · ADDENDUM-CLOSEOUT SEAM (PAT-096 type specimen — the root structural defect).** Write-back specified for a session that ends once; S29 ended FOUR times (S29/b/c/d). Addenda ran only W1/W2-partial/W5/W6; W3/W7/W8/W9 never fire. Chronic casualty = NEXUS_BRIEF (three addenda behind at 13:50: FT-06 exit absent, 2 unmarked basis instances, Rescue re-mark missing) + OUTBOX (PROME untold of exit/basis/Rescue) + MEMORY (ML-RED-150..154 one-liners). Amendment-10 fold-LAST rule currently self-refuted — **the rule is correct; it is the evidence, don't delete it.** Spec gap, not discipline failure. Fix = named addendum-closeout subset in CLAUDE.md (in RED's audit packet).
- **D2 · KB Status case-split:** `ACTIVE`×31 (Apr-era) vs `Active`×18 (every row since 7/5). **Case-fold before counting anything in KB** — exact-match drops the 18 newest live rows.
- **D3 · SCHEMA drift:** 4 value domains richer than the 5/6 contract (PREDICTIONS 20/21 non-canonical incl. RED-21's singleton `CORRECT`; CHALLENGES 12 values; KB 17; VX.Strength 11/25). **The vocabularies carry real information — the schema is the stale artifact; never "fix" data toward it.** Registry: SCHEMA says 8 cols, file has 12 (`exit_*` undocumented) — and WALTER's own CROSS_REFS/RED.md:25 + CLAUDE.md:204 carry the same stale "8-col". Dangling links: CHG-024/027 → VX-RED-022 (never existed, sole ID gap); one KB_Links → KB-RED-041.
- **D4 · Registry machine-layer lag (R7; fleet context below §7):** no instrument-basis column (basis prose on FT-06/08/09 only — both BRENT-PAPER rows bare; ML-RED-153 self-marked, unpropagated); no state column (FIRED lives mid-prose in `exit_source`, ~1,900 chars on FT-06 — substring state reads are FALSE); FT-08 was a half-registration (one leg machine, AND-leg prose) — **CORRECTED S29d** (now CORE-CPI-3MO-ANN ≥3.0, defect owned in notes). **R17 CLOSED S29e** (T5YIFR wired). Re-spec direction ruled 8/12 (PROME amendments), **DEFERRED by RED to its hygiene session**: basis / state / **pre-registered action-magnitude** columns — with R2/R7b/R8/R9/R4, per PROME's sequencing that absorbing an 18-finding list into a live catalyst day IS the D1 failure mode.
- **D5 · board_log obligation orphaned:** the ledger duty lives in boot 5.5 (NO-OP lane since 7/9); boot 1.5 (sole live channel) has none. All 119 rows are VOLUNTARY logging. Last row 8/07 while 8/11-8/12 BOARD consumptions went unlogged. **Grade as unregistered voluntary ledger, NOT non-compliance.** Two-state fix owed: obligation → 1.5, or FROZEN banner.
- **D6 · Dead archive/ cluster (PROME 6/30 prune `1cb18fbc3`, PAT-097 instance):** CLAUDE :232-235 (FILES table) + :77 + :316 + `competing-hypotheses/` :224 (never existed) + MEMORY:9 live link + MAINTENANCE:8 + **PREDICTIONS_README:5 false preservation claim** (target recoverable at `63dca04ef^`). RED's own 6/2 audit flagged part, closed "(Not done)", 71d. Fix template = CORAL CLAUDE.md:5 (documented-loss form). Also LAST_COMPLETION contradiction: :209 (reconciled truth — live spawn-contract surface, expected stale, never boot-read) vs :77/:202 ("retired" residue — **amend those two, never delete the file**).
- **D7 · handoff_WALTER misdocumentation:** README (6/2) denies the board_log (119 rows since 7/5) and labels RED's live inbox lane "degraded HERMES — don't use." LIAISON:233 cites retired `thesis/PREDICTIONS.tsv` as WALTER's boot-read. Historical dir presenting as live; wants a closed-banner.
- **D8 · Misc:** KRE_EXECUTIVE_SUMMARY basename collision — **two different documents, opposite verdicts (45% vs 75%); fix is RENAME, never merge** (sole duplicate basename in tree) · 4 misfiled Feb/Mar .md in workbook/ (TSV-only dir per CLAUDE:239-246; unique content, no challenges/ counterparts — relocate/archive) · ~30 archive candidates >60d (5-of-5 oldest UNREFERENCED; 20 unchecked) — **blocked: no archive/ dir exists to receive them** · NEXUS_BRIEF/STATUS byte-growth under line caps (PAT-086).

## 5. DO-NOT-TOUCH (load-bearing; verified in-file 8/12)

1. **KB/VX/FLOW/CHALLENGES/PREDICTIONS are RED's own adversarial schema** — the role, not DARWIN debt. Never strip toward generic-utility.
2. **`registry/FALSIFICATION_TRIGGERS.tsv` = WALTER's auto-fire surface; `docket/WATCHLINES.tsv` = RED's soft display.** Never add a display row to the registry. **Registry `UNDEFINED` exit cells are HONEST, not empty** — never auto-fill mirrored thresholds (WALTER refused exactly that on FT-06; the June FT-01 mirror was wrong).
3. **Steelman-before-attack ordering is semantic** (CLAUDE :167/:26/:14/:321; executed at STATUS:66-74). Any restructure that moves COUNTER-SIGNALS above BULL CASE STEELMAN breaks the discipline.
4. **Discipline overlay (CLAUDE:84): a dated section stamp is a TRIGGER, not a shield.** The stamp IS the mechanism — never "tidy" old stamps off headers; removing one disarms the re-read trigger.
5. **Amendment-10 fold-LAST rule (NEXUS_BRIEF:100)** — correct rule, currently the D1 evidence. Keep.
6. **LAST_COMPLETION dual-role (CLAUDE:209)** — spawn-contract surface, expected stale between spawns, never boot-read. Older-than-SCRATCH is NORMAL. Fix direction for the residue: amend :77/:202.
7. **Dated historical records stay uncorrected** (STATUS:40 principle; e.g. CALENDAR:45's $100.19 in a RESOLVED row). Only LIVE surfaces get dispute-marks/fixes.
8. **FLOW.tsv stays FROZEN**; W6's FLOW leg is dead by design.
9. **Canonical predictions = `workbook/PREDICTIONS.tsv` ONLY** (thesis/ fork retired 6/2 — and its README breadcrumb is D6, fix the claim not the retirement).
10. **CRLF/binary-mode edit guard** applies to whatever is CRLF at read time (currently WATCHLINES only — re-measure first).

## 6. Maturity snapshot
**L4 conf-H, HOLD (8/12 audit; FLEET_MAP row re-cut same day — not restated here).** L5 path: (a) addendum-closeout subset defined + one clean multi-ending day; (b) registry machine-layer completed (basis/state/leg-2 ✓ S29d/magnitude); (c) currency legs (VX pass, D6 dead paths). YEYOU leg STRUCK (8/7, unsatisfiable-leg class). Strongest L5-class evidence on record: 7/31 twenty-of-twenty closeout sweep; the 66-minute audit absorption with defects owned in-ledger; pre-registered rubrics before grading (impact ledger); ML-RED-144/151/153 self-marked spec defects.

## 7. Open questions / fleet context
- **The registry defect is FLEET-WIDE, not RED-local** (workbook reader Task B, 8/12): WALTER's 6c array = 18 conditions / 17 registered / 16 distinct; basis 3/17 (all RED, all 8/12); state 0/17 in-registry; REG-T (REGINALD, 8 rows) has NO exit columns at all; the Cushing trigger is registered nowhere and auto-dispatches IMMEDIATE; WALTER's FIRED_LOG is fire-only and two events behind on FT-01 (missed the 7/31 un-fire AND 8/7 re-fire). **Root cause: step 6c is a human read-loop — no code on either side parses the registry**, so RED's good-faith exit columns improved the document, not the surface. Routed 8/12 (WALTER packet + PROME for REGINALD's queue).
- **Does RED's dedicated hygiene session land the structural batch** (PROME sequencing: R2/R3-post-BRENT-ruling/R7/R8/R9 in their own session)? That session closing clean = L5 leg (a)'s test.
- Post-BRENT-ruling: does the $100 basis relabel propagate through all ~13 live instances in one pass (the D1 mechanism's first test under the new addendum awareness)?
- VX.tsv review-or-banner: does RED grade the 13 stale vectors or freeze the file? (Either is two-state-legal; silent middle is not.)
- CHALLENGE_IMPACT_LEDGER population (stops at 043) + 12d stamp — re-grade windows 025 (~8/15) and the passed 027 (8/4-8/6).
