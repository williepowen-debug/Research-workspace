# SAM Maintenance Log

Reverse-chronological log of **structural** changes to SAM's docs, folders, and scripts. Each entry: what changed, why, files touched, boot-impact.

Distinct from `thesis/CHANGELOG.md`, which logs **analytical** changes (thesis-version shifts, channel re-weighting, threshold rebumps).

**Archive convention:** archives live next to their active doc (e.g., `thesis/timeline/ARCHIVE.md`). Root `archive/` is preserved as a legacy graveyard for pre-Mar 18 system rebuild — do not add to it.

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
