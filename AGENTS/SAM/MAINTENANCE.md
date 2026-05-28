# SAM Maintenance Log

Reverse-chronological log of **structural** changes to SAM's docs, folders, and scripts. Each entry: what changed, why, files touched, boot-impact.

Distinct from `thesis/CHANGELOG.md`, which logs **analytical** changes (thesis-version shifts, channel re-weighting, threshold rebumps).

**Archive convention:** archives live next to their active doc (e.g., `thesis/timeline/ARCHIVE.md`). Root `archive/` is preserved as a legacy graveyard for pre-Mar 18 system rebuild — do not add to it.

---

## 2026-05-28 (PM, live session #2) — workbook FLOW.tsv refresh-split (v1.5 consistency)

Second-pass workbook cleanup, triggered by Will's "get the workbook caught up" review. FLOW.tsv (14 transmission-flow vectors) was ~7 weeks stale (last touched Mar 4 – Apr 7) and actively **contradicted v1.5** — most dangerously logging carry-unwind probs at 80/95/95 (vs current 12/62/80) and Channel 1 as "CRITICAL-CONFIRMED, $10-15B/mo selling active NOW" (v1.5 demoted Channel 1 to deferred after 3-of-3 benign Big 3 ESR prints). Pre-step confirmed **no script reads FLOW.tsv** (boot.py only auto-pulls data feeds) — edit is boot-safe. Mirrors the May-28 KB.tsv live-vs-archive split pattern.

**Split 14 rows → 10 live (`FLOW.tsv`) + 4 archived (new `workbook/FLOW_ARCHIVE.tsv`).**

- **Archived (resolved point-in-time telemetry):** `5.03` Path D (Apr 23-24/May 1 BOJ hike window — resolved by Apr 28 hold), `6.01` Energy→JGB Supply (March QatarEnergy/LNG crisis — abated), `6.03` War Escalation (Apr-7 8pm Hormuz deadline — passed, Brent $110→$92), `7.01` Taiwan LNG→TSMC (Mar-15 inflection — passed, cross-domain non-core). Each preserved verbatim with a `[RESOLVED YYYY-MM-DD: …]` prefix in Key Insight + Status → `ARCHIVED (was …)`.
- **Refreshed to v1.5 (5 live vectors):** `5.02` Carry Unwind (probs 80/95/95→12/62/80; CFTC -72.9K→-93,905; USDJPY→159.21; repointed to Jun 16 single-path); `2.03` J-SOLV (CRITICAL-CONFIRMED→DEFERRED; 3-of-3 benign ESR, foreign books growing; J-ICS long-end leg kept INTACT); `5.01` Floating Mortgage (repointed to Jun 16 collision); `3.01` CLO/Norinchukin (flagged Jun FY2025 print as the data-refresh gate; Apr-7 figures marked PENDING REFRESH); `1.06` Fiscal Doom Loop (re-pointed from stale "Feb 19 20Y auction" to current super-long auction softness + Jun 16).
- **Reaffirmed (5 structural, date-touch + "(Reaffirmed 2026-05-28, v1.5)" tag):** `1.05` Rural Political, `3.02` Desperation Swap, `3.03` Private Market Contagion, `4.01` BDC Latent, `6.02` USD-vs-Yen Safe-Haven (spot refreshed to 159.21).

**Files:** `workbook/FLOW.tsv` (14→10 rows, all v1.5-consistent); `workbook/FLOW_ARCHIVE.tsv` (new, 4 rows, same 10-col schema). Both verified 10-col clean. **Boot-impact: none.** **FILES-table note:** CLAUDE.md line ~236 lists FLOW under hand-maintained workbook tsvs — add FLOW_ARCHIVE alongside it on the next CLAUDE.md pass.

**Deferred workbook passes remaining (unchanged):** VX.tsv keep-vs-retire (decide-after-review pending); KB.tsv 4 SUPERSEDED rows → KB_ARCHIVE + v1.5 consistency scan; archive/ scaffolding cleanup (KB_STAGING_*, KB_BACKUP_10rows, ML.tsv + VX_HISTORY.tsv, SAM_WORKBOOK.xlsx).

---

## 2026-05-28 (PM, live session) — KOYOMI first run + `RELEASES.md` + spec hardening (prototype validated)

Operationalized the KOYOMI prototype created earlier today (entry below). Will spawned KOYOMI for the first time as a **named/persistent teammate** for a shakedown run. Outcome: prototype validated — Will likes the pattern; KOYOMI is now operational.

**First run earned its keep immediately:** KOYOMI caught a real **CALENDAR↔CATALYSTS.tsv divergence** — CALENDAR was missing 6–7 forward events the TSV already had (FOMC Jun 17, US CPI Jun 10, both JGB auctions, GDP revision Jun 8, National May CPI Jun 19, Tokyo June CPI Jun 26). She reconciled CALENDAR up to the TSV, then surfaced 3 design questions instead of guessing. Will decided all 3.

**Three decisions encoded into `docket/KOYOMI.md`:**
1. **TRUTH MODEL (split ownership)** — new spec section. `CATALYSTS.tsv` = source-of-truth for the dated-event SET (which events, dates, priority); `CALENDAR.md` = source-of-truth for narrative/routing/threshold prose; **neither carries live spot.** Resolves the "which file wins" ambiguity that made KOYOMI second-guess.
2. **Prune by the >1-week retention rule, not on sight** — codified in JOB step 1. A resolved event leaves the *forward* views when its date passes but stays in RECENTLY RESOLVED until >1 week old. (KOYOMI's own round-1 instinct; my spawn-prompt instruction to prune May 26 early was wrong — she correctly held it.)
3. **Strip live spot from CALENDAR** — executed by KOYOMI round 2.

**New file — `docket/RELEASES.md`:** recurring-releases reference. Cadence rules (CFTC=Fri/data-as-of-Tue, Tokyo CPI=last Fri, GDP 2nd prelim=~3wk after 1st, BOJ/FOMC/JGB-auction cadence) + official schedule links (ESRI, MIC, BOJ, MOF, CFTC, Fed, BLS) + a "Confirmed dates" scratchpad. Now KOYOMI's first stop for date verification (WebSearch only if this can't resolve). Holds **schedules only — no analysis, no live data.**

**`KOYOMI.md` spec changes:** added TRUTH MODEL section; read-set expanded to include RELEASES.md + both docket files (they were listed only under write-set); JOB step 1 (prune rule) + step 3 (no spot refresh) rewritten; granted a narrow write-set exception (append-only to the RELEASES.md "Confirmed dates" table when a date is verified at source).

**`docket/CALENDAR.md` — spot stripped (KOYOMI):** removed all live levels from INTERVENTION WATCH, PHASE 2 WATCH, STRUCTURAL CHANNEL 1 MONITORS, GEOPOLITICAL WATCH, and the May 29 CFTC / Jun 10 JGB auction rows — kept structural thresholds + significance, replaced bare-level cells with "see STATUS". **Historical levels in RECENTLY RESOLVED left intact** — they're resolved-event *outcome records* (what printed), not live monitors duplicating STATUS, and age out under the 1-week rule. SAM-confirmed convention: the strip rule applies to forward monitors, not outcome records.

**Jun 8 GDP date:** web-verified cadence-consistent (Q1 1st prelim May 19 + ~3wk → Mon Jun 8); logged ⚠️ in RELEASES.md pending ESRI schedule confirmation. Row kept in CALENDAR + TSV, noted "(date cadence-derived; confirm at ESRI)".

**Git:** SAM stages all docket changes (KOYOMI does not commit, per agent-git-isolation). **Boot-impact:** none — `catalyst_countdown.py` runs clean; CALENDAR is slimmer (one less divergence surface, no daily spot treadmill). **Eval note:** today's CLAUDE.md SPAWN PROTOCOL change (docket path + KOYOMI step 10) is a standing eval re-baseline trigger — flagged to Will.

---

## 2026-05-28 (AM) — new `docket/` folder + KOYOMI sub-steward (delegation prototype)

Created `AGENTS/SAM/docket/` to co-locate the forward-calendar layer and give a future maintenance sub-agent a single, enforceable ownership boundary. Outcome of a design conversation with Will: SAM stays sole orchestrator + analyst; bounded *busy-work* (calendar/catalyst upkeep) gets delegated to an ephemeral, SAM-internal sub-steward so SAM's context stays free for judgment.

**Moves (git mv, history preserved):**
- `CALENDAR.md` → `docket/CALENDAR.md`
- `workbook/CATALYSTS.tsv` → `docket/CATALYSTS.tsv`

**Repaths (verified both scripts resolve the new path + parse correctly):**
- `catalyst_countdown.py` — CATALYSTS path → `docket/`; docstring updated.
- `jgb_auctions.py` — added `DOCKET` const; CATALYSTS path → `docket/` (AUCTIONS_TSV stays in workbook/). Confirmed `load_catalyst_auction_dates()` still finds the 2 JGB auctions.
- `boot.py` untouched (invokes scripts by name).

**CLAUDE.md updated:** boot step 3 (`docket/CALENDAR.md`); write-back step 10 (sync CALENDAR + CATALYSTS, prefer spawning KOYOMI for sizeable refresh); doc-ownership table (added CATALYSTS row); FILES table (docket/CALENDAR + docket/CATALYSTS + docket/KOYOMI rows); corrected the old line-233 inaccuracy (CATALYSTS/FLOW/VX were wrongly listed as "auto-pulled" — now split auto-pulled vs hand-maintained). Forward-pointing CALENDAR refs updated in TRADE/STRATEGY/THESIS; historical mentions + CHANGELOG history left as-is.

**KOYOMI brief — `docket/KOYOMI.md`:** SAM-internal sub-steward (暦, "almanac"), spawned on command, NOT a network peer. Read-set: STATUS / THESIS§CATALYST / TIMELINE + run catalyst_countdown.py. Exclusive owned write-set: `docket/` only. Job: prune resolved, add upcoming, refresh stale content, keep CALENDAR↔CATALYSTS in sync + ISO/auction-name format rules. **Escalate-don't-act clause** is the load-bearing guardrail: anything analytical goes back to SAM, never edited inline. Does not commit (git is SAM's). Returns a tight summary.

**Status: command-first prototype.** KOYOMI runs only when SAM/Will invokes it — evaluate-mode until Will decides he likes the pattern. **Deferred (graduation rungs):** boot-time staleness *tripwire* in catalyst_countdown.py (runway < ~10d → auto-nudge SAM to spawn KOYOMI) → weekly scheduled run (needs an external firer — PROME/cron; `/loop` only runs within a live session). Boot-impact: none.

**Remaining deferred workbook passes (unchanged):** VX.tsv keep-vs-retire; FLOW.tsv refresh-vs-archive; archive/ scaffolding cleanup.

---

## 2026-05-28 (later) — CATALYSTS.tsv refresh + live-search additions + countdown holiday-skip (deferred-pass #1: KEEP, not retire)

Resolved the first deferred next-pass item from the KB cleanup entry below. The deferred note read "CATALYSTS.tsv retire (dup of CALENDAR)" — **corrected after gap-check: the file is not a free delete.** `scripts/catalyst_countdown.py` (runs at boot) READS CATALYSTS.tsv as its structured countdown feed. CALENDAR.md's dates are freeform ("Thu-Fri May 28-29", "🔴🔴 Tue Jun 16", "Early Jun", "Ongoing" triggers) and can't be parsed reliably into the strict `%Y-%m-%d` the script needs. Re-plumbing the script to read CALENDAR is fragile/intrusive.

**Decision: KEEP CATALYSTS.tsv as the machine-readable forward-event feed; CALENDAR.md remains the human-readable narrative/routing doc.** Different consumers. The root problem was drift (hand-maintained, ~6 weeks stale — still listed resolved May 1/14/15/20/22 events, Jun 16 BOJ row stale at SAM-21 70% / swap 74%), not duplication per se.

- Rewrote forward-only: dropped 6 resolved May events; refreshed to current v1.5 forward set — Tokyo May CPI (5/29), CFTC weekly (5/29), BOJ MPM base case (6/16, SAM-21 ~57% / market 55-65%, SAM-24 25bp @85%), Sato board (6/16), BOJ interim QT (6/16), May trade balance Phase 1 lag-test (6/18). who_cares + threshold_signal columns synced to current routing.
- Verified `catalyst_countdown.py` runs clean against refreshed file: imminent Tokyo CPI + CFTC (1 trd), upcoming Jun 16 cluster + Jun 18 TB. Boot-impact: none (positive — countdown was previously showing only stale Jun 16 with wrong probabilities).

**Live-search catalyst additions (Will-approved):** ran web research (MOF / Fed / BLS / Stats Bureau / Cabinet Office) for missing forward catalysts; added 7 rows, all dates verified at source. **FOMC Jun 17 (🔴)** — the rate-differential half of the carry trade, was absent (file tracked only the BOJ side); lands 24h after BOJ Jun 16 and now co-headlines the HIGH-PRIORITY summary. Also: US CPI May (Jun 10, 🟠, feeds FOMC dots); JGB 30Y auction (Jun 10, 🟠, direct J-ICS long-end / SAM-26 demand test); Japan Q1 GDP 2nd est (Jun 8, 🟡); JGB 20Y auction (Jun 25, 🟡); National May CPI (Jun 19, 🟡 — verified off Stats Bureau raw table, NOT Jun 26); Tokyo June CPI (Jun 26, 🟡). File now 13 forward events, date-sorted.

**Script fix — catalyst_countdown.py holiday-skip:** `trading_days_between` previously counted all weekdays; now skips a HOLIDAYS frozenset (Japan national holidays + US market holidays, 2026). Market-agnostic union (errs ~1 day toward "more urgent" near a single-market holiday — documented in-code). Verified: Jun 18→Jun 25 now 4 trd not 5 (skips Juneteenth); July 4 week skips correctly. Extend the set each calendar year.

**Anti-drift recommendation (NOT yet done — needs Will sign-off):** tie CATALYSTS.tsv refresh to CALENDAR.md maintenance so it can't drift again — either (a) add a one-line reminder to CLAUDE.md write-back step 10 ("update CALENDAR.md → also refresh workbook/CATALYSTS.tsv dates for catalyst_countdown.py"), or (b) leave as-is and refresh CATALYSTS opportunistically at boot when stale. Also: CLAUDE.md FILES table (line ~233) inaccurately lists CATALYSTS among tsvs "auto-pulled by boot.py" — it is hand-maintained and READ by boot, not written. Flag for the CLAUDE.md pass.

**Remaining deferred workbook passes:** VX.tsv keep-vs-retire (STATUS dup; ~6wk stale); FLOW.tsv refresh-vs-archive (Feb-Apr war/LNG content); archive/ scaffolding cleanup (KB_STAGING_*, KB_BACKUP_10rows, ML.tsv + VX_HISTORY.tsv merge, SAM_WORKBOOK.xlsx).

---

## 2026-05-28 — workbook KB.tsv cleanup: split + recategorize + internal backfill

Two-batch cleanup of `workbook/KB.tsv` (was 167 rows, frozen at 2026-04-07). Triggered by Will's workbook-staleness review. Pre-step verified **no script reads KB.tsv** (boot.py only auto-pulls the data feeds) — schema change is boot-safe.

**Batch 1 — split + recategorize:**
- Split 167 rows → 116 live (`KB.tsv`) + 51 historical (new `workbook/KB_ARCHIVE.tsv`). Historical = resolved point-in-time operational telemetry (SK-refiner saga, Mar-27 USD/JPY-160 intervention sequence, dated carry-probability snapshots, FY2025-end window timing).
- Consolidated 32 inconsistent Category values → 9 (Insurer / Regulatory / Repatriation / BOJ-Wages / Carry-FX / Energy / Household / Framework / Cross-Agent). Live rows grouped by category, sorted by ID within.
- Added `Status` column (LIVE / SUPERSEDED / HISTORICAL).
- Flagged 4 insurer assessments contradicted by v1.5 actuals as SUPERSEDED **in place** (KB-081/084/087/092) with actual outcomes appended — preserves the threshold-vs-mechanism calibration lesson rather than burying it.

**Batch 2 — dedup + internal backfill (no web; sourced from STATUS / TIMELINE / TRACKER):**
- Merged duplicate KB-148 into KB-137 (identical +50bp→ESR-200% calc, DEEP_DIVE §1B).
- Added 7 LIVE rows (KB-168..174) closing the Apr-7 → May-28 sync gap: BOJ Apr 28 hold + 3-way dissent; April CPI dovish miss; MOF interventions Apr 30 + May 6; Big 3 FY2025 ESR actuals (3-of-3); FY2026 plan outcomes (zero clean foreign-bond cuts); current vol/positioning; and **SYNTHESIS KB-172** resolving the KB-164 (active-at-stress-pace) vs KB-081 (deferred) Channel-1 contradiction in favor of deferral.
- KB-166/167 left archived as superseded forecasts; their outcomes captured in new LIVE rows instead of un-archiving.

**Batch 3 — numeric-conflict reconciliation (Notes-only appends, rows stay LIVE):**
- **RESOLVED — JGB losses → ¥13.2T** ($86B, Jun 2025; FY2025 prints confirm worsening: Nippon -¥5.73T, Meiji -¥2.16T). Annotated KB-063/064; the ¥9T DEEP_DIVE figure was earlier/lower.
- **RESOLVED — hedge ratio → 44.4%** (Mar 2025, 14-yr low; STATUS/TRACKER). Annotated KB-065/066; DEEP_DIVE's ~30% was too low, RP-SAM-4's 45-50% range was right.
- **STANDING GAP — per-insurer UST split** ($450-810B) not closeable from FY2025 disclosures (no clean UST line). Annotated KB-061/062/139/140 with the Japan all-inst TIC total ($1,239.3B Feb 2026) + rotation-within reframe.

**Net: KB.tsv 167 → 122 live rows. Boot-impact: none.** Calibration framing: the "blind spot" was a sync gap, not lost intelligence — current state was already in STATUS/TIMELINE/TRACKER; KB had drifted.

**Deferred to next workbook passes:** CATALYSTS.tsv retire (dup of CALENDAR); VX.tsv vs STATUS owner decision; archive scaffolding cleanup (KB_STAGING_*, SAM_WORKBOOK.xlsx, ML.tsv + VX_HISTORY.tsv merge).

---

## 2026-05-27 evening — v1.5 propagation sweep (STRATEGY, TRADE, TRACKER, RED, all 7 insurer profiles)

Same-day evening follow-up to the morning v1.5 thesis bump. Will flagged STRATEGY.md + TRADE.md as likely stale; I confirmed and asked to expand to a full doc-stack audit. Outcome: 12 docs refreshed across decision layer, RED counter-thesis layer, and per-insurer reference layer. Triage discipline: ranked by behavioral impact per [[feedback_audit_behavioral_ranking]] before touching files.

**Triggering trail:** Morning STATUS+THESIS+CHANGELOG resolved Position A (Sep $60 OTM) as NOT WARRANTED under v1.5 single-path. But STRATEGY.md + TRADE.md still presented full entry rules + ranked entry windows for the same Position A — a behaviorally-active contradiction (future SAM or Will reading those would get conflicting guidance from STATUS vs decision docs). The Sep-$60-NOT-WARRANTED reframe is the load-bearing edit that drove the whole sweep.

**Files touched (12 total):**

1. **`STRATEGY.md`** — v1.4 → v1.5; Stage 3 reframed multi-channel → single-path; hard trigger table refreshed (SAM-21 70%→~57%, ESR row ✅ resolved 3-of-3 benign, JGB 30Y retracement noted, Channel 3 dormant); **Position A flipped AUTHORIZED → NOT WARRANTED** with 4 explicit re-activation conditions; When-to-HOLD refreshed; Key Check Dates pruned forward-only; new CHANGELOG entry. Live data references redirected to STATUS.md.

2. **`TRADE.md`** — header v1.5; Tranche 2 Hard-Trigger Status table SAM-21 + ESR row + Channel-3-dormant + JGB-30Y-retracement; Position A NOT WARRANTED with re-activation conditions; Carry Unwind Probability synced to v1.5 (12/62/80); Risk Factors restructured (BOJ-delay 10%→25% single-path elevation; oil 20%→15%; intervention-fails 15%→12%; new Channel-1-reactivation row at 10%); "Bigger Hike" section anchored to SAM-24 @85%; Watchlist EWJ + Japan Banks SAM-21 refs; Key Dates pruned forward-only; Catalyst Sequence collapsed to TIMELINE pointer.

3. **`insurers/TRACKER.md`** — header 5/26 PM → 5/27 v1.5; Channel 1 banner "🟡 DOWNGRADED, NOT DEAD (Day 1)" → "🟡 DEFERRED STRUCTURAL BACKSTOP (3-of-3 confirmed)" with 5 explicit reactivation conditions; Sumitomo row in ESR table fully populated (197% ↑+19pt, foreign book +¥1.11T detail, Symetra/Dearborn); "Reading the Big 3 mutual prints" closed out as 3-of-3 RESOLVED with v1.5 signature table (insurer × ESR × mechanism × foreign book × US direction); "Wed Sumitomo pattern-confirmation test" section retired; Industry aggregates JGB row updated (30Y 3.866% / 40Y 3.836% / 10Y 2.713%); "What we're waiting for" pruned + added H2 FY2026 plans as next structural re-test; Key Dates Sumitomo ✅; Phase 2 inception extended to May 27 with Brent $93.13 + MOU framework hardening.

4. **`red/COUNTER_THESIS.md`** — full rewrite v1.0 → v1.5. New one-liner: single-path narrowing = thinner not stronger; June BOJ is most-priced event of cycle. Explicit calibration credit for CH-002 (FY2025 net buying) and CH-003 (intervention spike-and-reverse) wins driving v1.5 demotion. New narrative builds on threshold-vs-mechanism trap potentially repeating on Channel 2 (BOJ stress absorbed via targeted long-end op, not rate hike). "What world looks like if I'm right" / "What would prove me wrong" re-spec'd for v1.5. Explicit "what I'm NOT challenging" section preserves [[feedback_red_edge]] discipline. v1.0 counter-thesis archived below for historical record.

5. **`red/CHALLENGES.md`** — full rewrite. Resolved CH-002 + CH-003 (CONFIRMED) and CH-006 (DISMISSED) removed and logged. Retargeted CH-001 (severity 🟠→🟡 under v1.5 — Channel 1 demoted), CH-004 (severity 🟠→🟡 — lower probabilities, less false-precision risk), CH-005 (unchanged under v1.5), CH-007 (severity 🟡→🟠 — single-path makes consensus risk worse). **NEW CH-008 — Fiscal-Dominance Frame (BOJ Frozen, Not Hike-Ready) from eval Case 02 baseline runner; resolves Jun 16.** This formalizes the v1.5.x candidate finding logged in morning MEMORY into an active RED challenge with counter-evidence and resolution criteria.

6. **`red/LOG.md`** — new calibration scoreboard at top (2 CONFIRMED, 1 DISMISSED, 4 RETARGETED, 1 NEW). 5/27 resolution rows for CH-002, CH-003 (CONFIRMED) and CH-006 (DISMISSED) with full evidence trails. Retarget rows for CH-001 / CH-004 / CH-005 / CH-007 with v1.5 reasoning. New CH-008 entry. Original 3/31 rows preserved with cross-references — full audit trail intact. Major calibration call surfaced: **RED's CH-002 (FY2025 was net buying) was correct in substance 8 weeks before v1.5 demotion landed** — durable evidence that RED earns its keep.

7-13. **`insurers/<7 profiles>.md`** — all 7 refreshed under v1.5 (decision point in CLAUDE.md "retire-vs-refresh deferred post-Sumitomo" resolved as REFRESH after Will pushed back on the retire recommendation):
   - **nippon-life.md** — FY2025 ESR 195% section with Resolution Life decomposition; canonical threshold-vs-mechanism trap example; Stancorp attribution error fixed (Stancorp is Meiji's, not Nippon's)
   - **meiji-yasuda.md** — FY2025 ESR 208% manageable; pre-FY2025 "ESR NOT DISCLOSED red flag" resolved; cleanest base-case datapoint of Big 3
   - **sumitomo.md** — FY2025 ESR 197% ↑+19pt with full asset-composition table (foreign book +¥1.11T); Symetra/Dearborn detail; explicit cross-ref to RED CH-002 confirmation; most narrative-rich of the three
   - **dai-ichi.md** — FY2025 ESR ~220% +10pp equity-rally-driven; framed as least-representative of Big 4 / US-PC-stress amplifier via Canyon Partners
   - **norinchukin.md** — positioned as standalone independent Channel 1 reactivation gate (Jun FY2025); CEO Kitabayashi public risk-off concern preserved; ¥500B Q1 "fastest on record" decline
   - **fukoku.md** — first-mover historical-marker; J-ICS DOMESTIC mechanism precedent case (preserved in v1.5)
   - **japan-post.md** — clean-read JGB seller (zero PC); CEO Sahara Mar-3 directional-right / timing-wrong (April expectation missed); v1.5 sentiment confirmation for BOJ hike thesis

**Pattern preserved across all 7 profile refreshes:** durable per-insurer narrative (executive quotes with attribution, specific deal commitments by amount/counterparty, source attributions, historical trajectory) kept intact. The refresh added FY2025 ESR data + v1.5 framing on top, didn't strip the depth layer. Per Will's pushback: "TRACKER's table form can't hold executive quotes / PC deal specifics / source attributions" — refresh-not-retire was the right call.

**Net behavioral fix:**
- Position A NOT WARRANTED resolution now coherent across STATUS, STRATEGY, TRADE (was split before this sweep)
- RED has a functional counter-thesis targeting v1.5 again (was targeting v1.0, useless for v1.5 single-path decisions)
- Per-insurer reference layer + TRACKER aggregator layer now both reflect 3-of-3 Big 3 ESR window resolution
- Future SAM boots will load consistent v1.5 framing across all 12 docs

**Boot impact:** None directly — STRATEGY/TRADE not in boot sequence; TRACKER not in boot sequence; RED not in boot sequence; per-insurer profiles not in boot sequence. All are reference docs read on demand. Boot.py + boot docs (THESIS, STATUS, CALENDAR, TIMELINE, MEMORY) untouched.

**Cross-session lesson promoted to auto-memory:** `finding_refresh_not_retire_perentity_profiles.md` — when a thesis bump leaves per-entity profiles stale, refresh-with-trajectory-preservation beats archive-and-rely-on-aggregator. Aggregator files (TRACKER-style table) cannot hold executive quotes / source attributions / deal specifics / historical trajectory. Transferable to CARL (per-bank profiles?), REGINALD (per-name?), HENRY (per-vol-product?), BROCK (per-spread-pair?), HAWK (per-belligerent?).

---

## 2026-05-27 afternoon — eval suite v1 → v1.1 (split-file redesign after baseline contamination)

Same-day follow-up to the v1 scaffold below. Will ran the baseline against v1 single-file cases and reported both responses showed near-verbatim phrase echo from EXPECTED criteria. Diagnosed by a sister model (Prome / external session) and confirmed: v1 design had INPUT + EXPECTED + DO-NOT in a single file, README told operator to paste only the INPUT block, but file-design discipline is stronger than operator-instruction discipline. Will pasted the whole file (or selection scrolled past rubric), and rubric language leaked into the runner's prompt.

**Smoking gun:** Case 02 response contained "super-long duration adds proportionally more solvency-capital strain than the yield pickup compensates for" — that exact phrase was in v1's EXPECTED list, NOT in the INPUT. Near-verbatim echo confirms contamination source.

**Substantive finding (positive):** Both responses also contained reasoning that was NOT in EXPECTED — positioning recommendations, BOJ-tactical paths, FX rate-diff decoupling explanations. Real reasoning was happening alongside the rubric echo. v1 just couldn't measure how much.

**v1.1 fix (same-session ship):**
- Split each case into TWO files. `case_NN_<topic>_INPUT.md` is pasteable (scenario data + questions only). `case_NN_<topic>_RUBRIC.md` is scorer-only with a prominent "⚠️ SCORER ONLY — DO NOT PASTE INTO RUNNER" header. Makes contamination physically harder.
- Re-shaped EXPECTED criteria from quote-form to assertion-form. Case 02 J-ICS solvency-strain criterion rewritten as "Explains why super-long is structurally unattractive under J-ICS — beyond just citing J-ICS by name. Must connect duration repricing to solvency capital impact AND explain why this dominates yield-pickup motivation. Wording is flexible. The test is whether the response articulates the structural disincentive, not whether it uses any particular phrase." Tests concept, not phrasing match.
- Added contamination self-check at multiple points in INPUT file headers ("Does your selection contain `EXPECTED`, `DO NOT`, or `RUBRIC`? → too much"). README repeats the check. RUBRIC files include a post-response contamination-signature check.
- Added `PASS-CAVEATED` and `FAIL-CONTAMINATED` result categories to scoring rubric.

**Files in v1.1 (active):**
- `evals/README.md` — rewritten for v1.1 split-file workflow, includes v1 → v1.1 baseline-finding note
- `evals/case_01_nippon_esr_INPUT.md` + `evals/case_01_nippon_esr_RUBRIC.md`
- `evals/case_02_jgb30y_jics_INPUT.md` + `evals/case_02_jgb30y_jics_RUBRIC.md`
- `evals/results.tsv` — 2 baseline rows logged as PASS-CAVEATED with contamination diagnosis
- `evals/baseline_artifacts/` — preserved v1 response transcripts (docx) for audit trail

**Files removed:**
- `evals/case_01_nippon_esr_mechanism.md` (v1 combined-file)
- `evals/case_02_jgb30y_jics_direction.md` (v1 combined-file)

Both files were never committed to git in their v1 form, so deletion is clean (no rewrite-history issue).

**Recommendation for next session:** re-baseline against v1.1 once. Pick Case 02 — the harder of the two to derive unprompted (structural-inversion call against pre-J-ICS muscle memory) — for the higher-diagnostic-value clean run.

**Boot impact:** None. `evals/` remains operator-only infrastructure.

---

## 2026-05-27 morning — eval suite v1 (scaffold) [SUPERSEDED — see v1.1 above]

Ship-day for the SAM eval suite. New top-level `evals/` directory with 2 frozen-scenario test cases. Origin: design-doc review session with Will (Ideas.docx walked through 4-part infra menu; eval suite picked as highest-ROI item; scoped to 2 cases not 5 per discipline-of-cap-on-first-ship).

**v1 artifacts (now superseded by v1.1):**
- `evals/README.md` — runner protocol (skip-boot pattern), pass/fail scoring rubric, re-run cadence, retire policy, failure-protocol diagnostic buckets.
- `evals/case_01_nippon_esr_mechanism.md` — combined INPUT + EXPECTED + DO-NOT in one file. **Contamination flaw discovered same-day; redesigned in v1.1.**
- `evals/case_02_jgb30y_jics_direction.md` — same structure, same flaw. **Redesigned in v1.1.**
- `evals/results.tsv` — header row only initially; v1.1 added 2 baseline-PASS-CAVEATED rows.

**CLAUDE.md update:** FILES table entry added for `evals/` between `red/` and `research/outputs/`. Explicit note: SAM does NOT auto-load eval files at boot — eval scoring happens in a separate fresh skip-boot session that Will runs.

**Runner pattern (skip-boot):** Will opens a fresh Claude Code session in `AGENTS/SAM/`, pastes ONLY the INPUT block (which contains explicit "DO NOT RUN BOOT" framing), scores the response against EXPECTED + DO-NOT, appends to `results.tsv`. CLAUDE.md + auto-memory auto-load (that's correct — they contain the lesson surface; the test is application not derivation). STATUS / THESIS / PREDICTIONS / TIMELINE do NOT load (they contain answer keys for resolved cases — would contaminate the test).

**Cap discipline:** v1 holds at 2 cases. No case 3 until either (a) one of the first 2 catches a regression, OR (b) a new lesson emerges that neither covers. Per README.md retire policy: cases retire when their lesson migrates to script-enforcement.

**Boot impact:** None. `evals/` is operator infrastructure, not agent context.

---

## 2026-05-26 evening (continued) — MEMORY restructure + CLAUDE.md audit + scripts fixes + cpi_japan.py build

Same-evening continuation of the folder cleanup logged below. Five additional workstreams, six commits total.

**MEMORY.md restructure (commit 0e58c525):** 87→44 lines. Promoted threshold-vs-mechanism lesson (SAM-25/26) + audit-behavioral-ranking lesson to auto-memory (`finding_threshold_vs_mechanism.md`, `feedback_audit_behavioral_ranking.md`). Compressed Session Notes to template (terse LAST SESSION + numbered NEXT SESSION); retired PENDING + INFRASTRUCTURE STATUS sub-sections. Findings 7→2 (kept SAM-operational items; retired 2 stale — PROME SCRATCH contradicts `project_openclaw_prome_degraded`, EUR/JPY operationalized in boot.py). References collapsed 5→2 lines.

**CLAUDE.md audit (commit 20da4862):** 228→233 lines but net more accurate. Phase A (SPAWN PROTOCOL): fixed broken "All mail lives in removed:" line; added ⚠️ messaging-overhaul status note pointing to `[[project_messaging_overhaul]]`; boot step 6 now references PREDICTIONS calibration scoreboard + `[[finding_threshold_vs_mechanism]]`; boot step 14 captures auto-memory promotion path. Phase B: deleted WAR — TWO-PHASE JPY DYNAMIC section (contradicted THESIS v1.4 supply-destruction-inverted Phase 1 framing); removed stale "Current" column from KEY THRESHOLDS table; added 4 thresholds (USDJPY <130-135, JGB 10Y >2.40%, MOF weekly >¥1.5T). Phase C: added Big 3 ESR <200% via market stress row to CROSS-AGENT SIGNALS (mechanism-aware per TRACKER); retired Shunto row (annual reactivation note); cleaned blank-section debris; FILES table now lists MAINTENANCE.md, SIGNAL_INTAKE.md (with stale warning), expanded workbook breakdown beyond just VX.tsv.

**Scripts fixes (commit a4572223):**
- `jgb_auctions.py` — TSV-append bug fixed. Climate Transition uniform-price auctions lack weighted-average column, causing `TypeError: unsupported format string passed to NoneType.__format__` at append time. Added `_fmt()` helper handling None gracefully. Verified by appending May 25 5-Year Climate Transition (BTC 4.622x). Boot 7/8 → 8/8 green.
- `usdjpy.py` — added `TOUCH_TOLERANCE = 0.10` constant; modified `days_since_level()` to use tolerance band. May 6 low 155.05 now correctly registers as touching 155 (was n/a previously). Added intraday-range alert as third summary line — `INTRADAY_RANGE_WARN = 2.5` 🟠, `INTRADAY_RANGE_CRIT = 4.0` 🔴, calibrated against Apr 30 (5.15y) + May 6 (2.84y) intervention events. Would have correctly flagged Apr 30 as INTERVENTION-GRADE.
- `AUTOMATION_PLAN.md` — status banner DRAFT → ✅ EXECUTED with verification line.

**cpi_japan.py — net new boot script (commit bdca2519):** 9th script in boot sequence; closes the Japan CPI observability gap that was previously hand-pulled via web search. Architecture: e-Stat API v3 (`api.e-stat.go.jp/rest/3.0`), statsDataId `0003427113` (2020-base CPI), pulls headline + core + core-core YoY for National (area 00000) + Tokyo Ku-area (13A01). `ESTAT_APPID` loaded from repo-root `.env` (gitignored). Two-table threshold scheme per Will's `Thresholds.md` note — separate buckets for Core (BOJ target series) and Core-core (trend gauge), plus cross-series divergence flag (≥0.5pp = energy/subsidy driven; ≤0.2pp = broad-based softening), plus Tokyo-vs-National comparison note with CALENDAR `<1.95%` Tokyo trigger adjustment. Idempotent `workbook/CPI.tsv` append on (Series, Reference_Month). Today's read: 🟠 National Apr 2026 core 1.4 Soft band + 0.5pp divergence (energy/subsidy-driven softness BOJ can look through); Tokyo gap to National 0.0pp vs typical -30-40bp (softness may be closing). Boot 9/9 green, 9.9s total. Will registered the AppID; one-time setup. Pattern carries forward to future Japan-stats scripts (BOJ, trade balance, employment).

**Boot impact:**
- `boot.py` BOOT_SEQUENCE: 8 → 9 entries (added "Japan CPI" between MOF Weekly Flows and Catalyst Countdown).
- `MAINTENANCE.md` and `SIGNAL_INTAKE.md` (with stale warning) now listed in CLAUDE.md FILES table.
- `KEY THRESHOLDS` in CLAUDE.md no longer carries stale Current values; STATUS.md is the canonical live values doc.
- `workbook/CPI.tsv` — new file, 12 rows seeded (Nov 2025 → Apr 2026 × National + Tokyo).
- Repo-root `.env` — new file, gitignored, holds `ESTAT_APPID`.

**Auto-memory entries created:**
- `finding_threshold_vs_mechanism.md` — falsifiable-prediction discipline pattern (SAM-25/26 both fired the same trap)
- `feedback_audit_behavioral_ranking.md` — rank doc-cleanup findings by behavioral impact, not line-count

---

## 2026-05-26 evening — Folder cleanup Pass 1a/1b/2a/2c (Will-directed audit response)

**Trigger:** Will asked for folder-structure audit (post-Sumitomo pre-watch session). Audit surfaced ~6 weeks of accumulated dead-ends at SAM's edges; Will approved Pass 1a + 1b + 2a + 2c (deferred 2b insurer per-name files until post-Sumitomo; deferred Pass 3 research/ reorg).

**Pass 1a — dead top-level dirs trashed:**
- `recon/` (single Mar 15 file) — `git rm`
- `domain/` (single Mar 17 file, superseded by `research/outputs/LIFE_INSURER_UST_DEEP_DIVE.md`) — `git rm`
- `sources/` (3 Mar 17 files) — `git rm`
- `session_archive/` (single Mar 3 STATUS archive) — `git rm`

**Pass 1b — stale top-level files:**
- `LAST_COMPLETION.md` (Apr 11 stale; absorbed by MEMORY.md "LAST SESSION" block) — `git rm`
- `SIGNAL_INTAKE.md` (Apr 8 stale; thesis now v1.4) — added top-banner `⚠️ STALE` note pointing readers to THESIS/STATUS as canonical; file preserved for WALTER routing reference pending messaging-system overhaul decision

**Pass 2a — workbook staging moved to workbook/archive/:**
- `KB_STAGING_A.md`, `KB_STAGING_A_FORMATTED.tsv`, `KB_STAGING_B.md`, `KB_STAGING_B_FORMATTED.tsv` (Mar 30 unresolved staging)
- `KB_BACKUP_10rows.tsv` (Mar 30)
- `ML.tsv` (Mar 17), `VX_HISTORY.tsv` (Mar 17)
- Live `workbook/` now shows only the 10 active tsvs (CATALYSTS, CFTC_JPY, FLOW, FXY_OPTIONS, JGB_AUCTIONS, JGB_YIELDS, KB, MOF_FLOWS, USDJPY, VX) + archive/

**Pass 2c — inbox/outbox bankruptcy (one-time sweep per `project_messaging_overhaul`):**
- *Inbox* — 7 files trashed after read-review. None held uncaptured signal: 2 info-only WALTER routes (IMF GFSR, Baker Hughes), 2 absorbed-into-thesis claims (Hormuz exposure, oil products inventory), 1 falsified claim (Japan UST-selling — Feb TIC contradicts), 1 tangential (equity rotation), 1 sweep superseded by Apr 30 + May 6 intervention integration.
- *Outbox* — 2 Apr-era files trashed (6+ weeks stale, undelivered, superseded); 3 May 21 files moved to `delivered/` (recent, content preserved); current May 26 PROME tracker_cleanup_complete left in `outbox/`.

**Files touched (`AGENTS/SAM/` only):**
- Trashed: `recon/`, `domain/`, `sources/`, `session_archive/`, `LAST_COMPLETION.md`, 7 inbox files, 2 Apr-era outbox files
- Moved: 7 workbook staging files → `workbook/archive/`; 3 May 21 outbox files → `outbox/delivered/`
- Edited: `SIGNAL_INTAKE.md` (banner), `MAINTENANCE.md` (this entry)

**Boot impact:**
- `ls AGENTS/SAM/` now shows 7 top-level docs (was 9) + 9 subdirs (was 12 incl. dead). Cleaner orientation surface.
- `ls workbook/` now shows live tsvs only; archive subdir holds the staging graveyard.
- `inbox/` empty (processed/ unchanged); `outbox/` shows only current session's work.
- No boot-sequence file path changes — all paths in CLAUDE.md boot steps unaffected.

**Deferred:**
- Pass 2b (insurers/<name>.md per-insurer profiles) — wait for post-Sumitomo Wed AM when Big 3 mutual state is fully resolved; then retire-vs-refresh decision is cheaper.
- Pass 3 (research/ reorg into outputs/+archive/) — cosmetic, low behavioral impact, defer indefinitely.
- SIGNAL_INTAKE full refresh — pending messaging-system overhaul direction.

**Rationale (per [[feedback_audit_behavioral_ranking]] / 2026-05-26 lesson):** Cuts ranked by behavioral impact, not line-count. HIGH-impact dead dirs and stale top-level files cleared first; MED-impact workbook staging + inbox/outbox cleared because user opted in; LOW-impact research/ reorg deferred.

---

## 2026-05-26 PM — TRACKER.md mechanism-aware routing + Channel 1 banner + staleness fixes (PROME cleanup ask + follow-up audit)

**Trigger:** PROME signal `prome_2026-05-26_insurer_tracker_cleanup_request.md` — Will + PROME walked SAM domain to understand Channel 1; flagged stale alert rule ("ANY ESR <200% → 🔴") and missing mechanism-vs-threshold discrimination. Independent finding from same root as MEMORY 2026-05-26 (threshold-vs-mechanism trap on SAM-25). Follow-up audit (post-PROME-reply) caught two additional actively-wrong sections.

**Change (single-file structural cleanup, two passes):**

*Pass 1 — PROME ask:*
- Added top-level **🟡 CHANNEL 1 STATUS** banner ("downgraded, not dead") above the J-ICS Key Insight. Captures: what's intact, what's deferred (not dead), why the old rule is too crude.
- **Signal routing replaced** — old 5-bullet rule list collapsed; new 5-row mechanism-aware table discriminating market-loss-driven vs M&A-driven sub-200% prints. New row for J-ICS-cited super-long avoidance.
- **"What's confirmed"** — re-ranked by mechanism evidence weight. Oct 2025 50% planned-cut survey explicitly down-weighted as superseded by Apr 2026 actuals (zero clean cuts). Old "Nippon 222% → if drops <200% → tone changes" assertion stripped as superseded by May 26 Nippon 195% (M&A) outcome.
- **"What we're waiting for"** — refreshed: Sumitomo Wed May 27, mid-tier Late Jun, Norinchukin Jun, any explicit reduction target (Fukoku-2023-style), MOF ITS sustained selling.
- **KEY DATES** — added Apr 14-25 FY2026 plans (✅) and May 22 CPI (✅ dovish miss) with outcomes. Refreshed Sumitomo row to call out M&A-vs-stress pattern test explicitly.
- **MONITORING CHECKLIST** — section header retired (week mostly resolved); extract-checklist preserved inside the new SIGNAL ROUTING section. Added US-subsidiary direction-of-travel row (Resolution Life, Stancorp).
- **Last Updated + Purpose** banners refreshed.

*Pass 2 — follow-up staleness fixes (Will-approved after Pass 1 audit):*
- **Industry Aggregates JGB rows refreshed.** JGB 30Y was claiming "4.000% ✅ BREACHED" as if durable; STATUS already showed 3.931% (May 22, retraced -7bp). Replaced with breach-and-retrace narrative + footnote treating 4.000% as structural stress level, not durably-held floor (SAM-26 lesson). JGB 10Y refreshed 2.770% May 20 → 2.749% May 22. JGB 40Y row added (3.921%).
- **Oil-yen section replaced.** "Apr 12 Hormuz blockade context" was v1.3-era framing ("oil spike → trade deficit widens → yen weakens → FX gains paper over bond losses") — actively wrong post-v1.4. April trade balance posted ¥+302B SURPLUS (blockade collapsed import volumes); CPI missed on fuel subsidies; Brent has since collapsed -12% on MOU optimism. Replaced with tight v1.4 oil-yen note flagging Phase 1 inversion + Phase 2 inception + insurer FX-cushion fading, pointing to `thesis/THESIS.md` § OIL-IN-YEN as single source of truth.

**Files touched:**
- `insurers/TRACKER.md` (+58 / -51 net across both passes; structural replacement, not accumulation)

**Boot impact:** None on the standard 7-step read sequence. TRACKER is read on insurer-specific spawns. Behavioral impact is twofold: (1) alert-routing correctness — future ESR-threshold breaches won't auto-trigger 🔴 if the mechanism is capital action; (2) cross-doc consistency — TRACKER no longer reports JGB stress facts in conflict with STATUS, and no longer carries an obsolete mental model of the oil-yen channel.

**Convention transferable (Pass 1):** Threshold-based alert rules across SAM (and other agents) should be audited for mechanism qualifier — the "level breach → route as stress" reflex mis-fires when capital actions, M&A, or sub-debt drives the breach. Apply when calibrating BROCK HY OAS triggers, REGINALD KRE bear-line, HENRY VIX regime triggers — any level-based signal where the same level can be reached by multiple mechanisms.

**Lesson reinforced (Pass 2):** Doc-cleanup asks benefit from a follow-up audit pass after executing the explicit scope — the PROME ask covered the rule + Channel 1 banner + key dates, but the two highest-impact remaining issues (cross-doc fact conflict on JGB 30Y; obsolete oil-yen mental model) were *adjacent* to the ask, not in it. Catching them required a fresh end-to-end read once the requested edits were in. Behavioral-impact ranking (per MEMORY 2026-05-26): only proposed top-2 of 11 noticed items; deferred cosmetic and duplicative items. Validates "rank by behavioral impact first, line count second" lesson in practice.

**Not changed (per PROME scope):**
- `STATUS.md` — Channel 1 demotion already reflected on May 26 AM (line 14)
- `thesis/THESIS.md` — v1.5 reframe deferred to post-Sumitomo
- `thesis/CHANGELOG.md` — no analytical version change; this is rule calibration + staleness, not thesis update

**Completion note:** filed to `outbox/2026-05-26_to-PROME_tracker_cleanup_complete.md` (Convention B own-outbox routing).

---

## 2026-05-26 — TIMELINE archive split + `thesis/timeline/` folder

**Trigger:** Boot-doc audit found `thesis/TIMELINE.md` at 555 lines / 56KB — 45% of total boot context. Resolved entries going back to Mar 31 + obsolete v1.3-era forward-looking sections were padding the read.

**Change:**
- Created `thesis/timeline/` folder.
- Split content at cut date 2026-05-11 (v1.4 era inception, Bessent-Katayama meeting).
- Active post-May-11 narrative + pending branch points → `thesis/timeline/TIMELINE.md`.
- Pre-May-11 resolved events + obsolete v1.3 forward sections + historical Branch Point rows → `thesis/timeline/ARCHIVE.md` (reverse-chron, prepend-newest pattern).
- Trashed old `thesis/TIMELINE.md`.

**Files moved/created:**
- NEW `thesis/timeline/TIMELINE.md` (~220 lines)
- NEW `thesis/timeline/ARCHIVE.md` (~190 lines)
- NEW `MAINTENANCE.md` (this file)
- REMOVED `thesis/TIMELINE.md` (trashed)

**Path refs updated:**
- `AGENTS/SAM/CLAUDE.md` — 3 path references (boot step 4, write-back step 12, Files table)
- `AGENTS/SAM/red/CLAUDE.md` — 1 path reference (boot step 2)

**Boot impact:** TIMELINE read 555 → ~220 lines (-60%). Total boot context ~1,230 → ~890 lines (-28%).

**Convention established (per Will):** archives co-locate with active docs; root `archive/` is legacy-graveyard only.

**Next maintenance candidates (audit findings from 2026-05-26):**
1. ~~PREDICTIONS archive split~~ → **REVISED + EXECUTED** (see PREDICTIONS entry below)
2. ~~THESIS de-dupe (core)~~ → **EXECUTED** (see THESIS entry below)
3. ~~STATUS narrative compress~~ → **EXECUTED** (see STATUS entry below)
4. ~~THESIS Forward catalyst table refresh~~ → **EXECUTED** (see THESIS residuals entry below)
5. ~~THESIS KEY THRESHOLDS — strip Status column~~ → **EXECUTED** (see THESIS residuals entry below)
6. ~~THESIS POSITION VIEW — collapse to pointer~~ → **EXECUTED** (see THESIS residuals entry below)

All 6 candidates executed in one sitting on 2026-05-26.

---

## 2026-05-26 — PREDICTIONS.tsv restructure-in-place (calibration-preserving)

**Trigger:** Original audit recommendation was to archive CONFIRMED/FAILED rows. Will pushed back: closed predictions are calibration gold — 6 high-confidence failures (90% / 75% / 65% / 65% / 60% / 55%) are the strongest available signal against overconfidence in future prediction-writing.

**Change (lighter than original plan — no file split):**
- Rows reordered: **OPEN → RESOLVED → FAILED → CONFIRMED**, by Pred_ID within each.
- Added `#`-prefixed preamble block at top with:
  - Calibration scoreboard (7 CONFIRMED / 6 FAILED / 1 RESOLVED-special / 6 OPEN)
  - High-confidence failures listed with one-line lesson each
  - Failure-pattern synthesis (political ceiling, flow-data interpretation, intervention prob-weighting, threshold-vs-mechanism)
  - SAM-25 called out as the threshold-vs-mechanism trap
- No rows removed. No file split. Boot step 6 still scans single file.

**Files touched:**
- `thesis/PREDICTIONS.tsv` (in-place restructure; 20 data rows preserved + 20-line `#`-preamble added)

**Boot impact:** Negligible line increase (~22 preamble lines), but boot step 6 now leads with calibration-warning instead of arbitrary historical first row.

**Convention established:** TSV files can carry `#`-prefixed comment preambles for calibration / context that humans scan but parsers skip. Use sparingly; keep under ~25 lines.

---

## 2026-05-26 — STATUS.md narrative compress (candidate #3)

**Trigger:** STATUS.md at 203 lines carried ~70 lines of prose narrative that duplicated TIMELINE (event narratives) and THESIS (channel/v1.5 framing). Per CLAUDE.md doc-ownership rule, STATUS is "snapshot format — tables and levels, minimal prose."

**Change (4 sub-edits):**
- **STATE OF PLAY (lines 5-44)** — compressed 40-line prose block to 10-line bullet headlines + pointer to `timeline/TIMELINE.md` May 26 section. Preserved the "what's TOP OF MIND today" hook.
- **REFERENCE DATA (lines 169-188)** — collapsed 8 channel-by-channel narrative sub-summaries to one-line-per-channel + BOJ QT data point. Stripped duplicates of CPI / Brent / GDP / trade balance (all in TIMELINE). Retained unique data: hedge ratio 44.4%, MOF intervention ¥10T total, BOJ QT pace.
- **Bottom THESIS section (lines 192-203)** — stripped entirely. The refreshed THESIS.md status banner already owns this; bottom STATUS restate was pure duplication. Replaced with one-line pointer.
- **In-section narratives** — light wordiness trim: probability footnote, stale "Decision-eve Tue" note (Tue had already happened), redundant "No position change May 22-25" recap.

**Files touched:**
- `STATUS.md` (203 → 153 lines, -25%)

**Boot impact:** Total boot context 1,230 → **815 lines (-34% from baseline)** across all 6 candidates.

**Discipline reinforced:** STATUS = snapshot (tables, current values, decision context). TIMELINE = narrative. THESIS = structural. Going forward: paragraphs of event-narrative in STATUS should auto-route to TIMELINE; STATUS keeps bullet headlines + pointer.

---

## 2026-05-26 — THESIS.md de-dupe

**Trigger:** Boot-doc audit found THESIS.md duplicated content owned by other files: Catalyst Sequence "Resolved" table (~25 rows narrating events that live in TIMELINE) + CONFIRMED/FALSIFIED PREDICTIONS tables (duplicating PREDICTIONS.tsv).

**Change:**
- Stripped Catalyst Sequence "Resolved (Apr 13 → May 21)" subsection (~25 rows). Replaced with one-line pointer to `timeline/TIMELINE.md` + `timeline/ARCHIVE.md`.
- Stripped CONFIRMED PREDICTIONS + FALSIFIED PREDICTIONS tables (14 rows total). Replaced with one-line pointer to `PREDICTIONS.tsv` and its preamble calibration record.
- Refreshed version banner from May 21 framing ("THESIS STRENGTHENED") to May 26 framing ("MIXED — Channel 1 weakened post-ESR, Channel 2 dominant, Channel 3 dormant"). Did NOT bump version — v1.5 reframe deferred to post-Sumitomo per MEMORY guidance.

**Files touched:**
- `thesis/THESIS.md` (276 → 235 lines, -15%)

**Boot impact:** Total boot context now 1,230 → ~846 lines (-31% from baseline) after all three 2026-05-26 cleanups (TIMELINE split + PREDICTIONS restructure + THESIS de-dupe).

**Doc-ownership reinforced:** THESIS = structural argument + thresholds + channels + conviction. TIMELINE = event narratives. PREDICTIONS.tsv = falsifiable record. Each doc now contains only what it owns; cross-doc references replace duplication.

**Forward-table staleness flagged (not executed in this pass — surfaced as candidates #4-#6 above):**
- Forward catalyst row "Fri May 22 Japan April CPI" is resolved (left in place — pointer-only de-dupe was the locked scope)
- Duplicate "Mid-June BOJ" rows
- KEY THRESHOLDS table has stale May 21 "Status" column
- POSITION VIEW says 8 shares; actual is 13

---

## 2026-05-26 — THESIS.md residual cleanups (batch #4-#6)

**Trigger:** Three staleness/duplication issues surfaced during #3 (core de-dupe) but were out of locked scope. Batched as a single follow-up pass.

**Change:**
- **#4 Forward catalyst table refresh** — dropped resolved May 22 CPI row; updated Big 3 ESR row to reflect Sumitomo-only Wed May 27 (Nippon/Meiji done); added Tokyo May CPI Thu-Fri May 28-29; merged duplicate Mid-June BOJ rows into one with SAM-21 + SAM-24 references; added pointer to CALENDAR.md for operational tracking.
- **#5 KEY THRESHOLDS — Status column stripped** — table now 2 cols (Level, Significance), purely structural. Current values + breach status redirected to STATUS.md. Removed JGB 40Y row (was definitional placeholder with no significance).
- **#6 POSITION VIEW — collapsed to thesis-level statement** — kept one-line "what we hold + why" (FXY long, target $60-62, stop $55.05). Removed stale share count (8 vs actual 13). Pointed to STATUS.md / TRADE.md / STRATEGY.md for operational details.

**Files touched:**
- `thesis/THESIS.md` (235 → 235 lines — net flat; pointer text added back what stale-content cuts removed. Win is in structural clarity, not line count. Cumulative day total: 276 → 235, -15%.)

**Doc-ownership reinforced again:** THESIS = structural (thresholds as definitions, position as thesis-level statement, forward catalysts as thesis-dependent events). STATUS = current snapshot (values, sizes, fills). CALENDAR = operational forward tracking. TRADE = position details. STRATEGY = decision playbook.

---

*Each new structural change prepends above. Older entries below.*
