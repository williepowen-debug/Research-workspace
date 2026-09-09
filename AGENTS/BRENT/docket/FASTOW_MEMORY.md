# FASTOW MEMORY

State file for the docket-steward sub-agent. Spec is in [`FASTOW.md`](FASTOW.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership:** FASTOW writes this file directly at end-of-run (consistent with FASTOW's other write privileges — full-edit mode by default, busy-work-only). BRENT may pre-edit between runs to seed `## NEXT RUN HINTS`, `## PENDING`, or `## CALIBRATION`.

**Spawn order:** FASTOW reads `FASTOW.md` first (spec), then `FASTOW_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last synced*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by FASTOW at run start: what's moved in STATUS / THESIS / TIMELINE / CHANGELOG since the previous sync. Cleared at end-of-run.*

*(cleared end-of-Run-2)*

---

## LAST RUN

### Run 2 — 2026-06-07 ~21:08 ET (Sun, pre-Globex, post-Run-1 retro integration)

**Trigger:** Normal sync. Monthly baseline-audit trigger does NOT fire (Run 1 was Jun 7 same day — no calendar-month rollover; next monthly trigger Jul 1+). Post-miss trigger did not fire. **No audit trigger this run.**

**Read-set scan:**
- STATUS.md timestamp 2026-06-07 ~17:38 ET (unchanged since Run 1; fresh).
- THESIS / TIMELINE / CHANGELOG unchanged since Run 1.
- CATALYSTS.tsv: 24 forward rows post-Run-1 BRENT application of light-convention delta. Date-sorted.
- Run 1 retro produced 2 BRENT-side edits to STANDING MONITORS (OPEC+ Jun 7 outcome ingestion watch + NEW pre-fire date verification monitor for cadence-derived rows).

**Pruned:** none. No `— FIRED` rows. OPEC+ Jun 7 still TODAY/PENDING.

**Added:** none. (Run 2 is rolling-light per CALIBRATION; no new events surfaced from sources within rolling window.)

**Refreshed (framing):** none. Spot-checked all forward rows against unchanged STATUS — all framing current.

**Modeled-date revisions:** none. SPR 350M Jun 10 + Cushing 20M Jul 1 both still match STATUS storage section (no new EIA data since Jun 3 to shift either).

**Pre-fire date verification (NEW STANDING MONITOR per BRENT post-Run-1 retro):** scanned TSV for rows whose `notes` contain "best-estimate" / "verify against" / "cadence-derived" / "typical" / "customary" language AND date within next 7 calendar days. **Hits:** 1 row.
- **OPEC MOMR (June) — Jun 13 → Jun 11 REVISED.** Pre-Run-2 row dated 2026-06-13 with notes "Best-estimate mid-month (typical 11th-13th)". 6 days out (within 7d gate). WebSearch + WebFetch (investing.com OPEC calendar) confirmed source-locked **Jun 11 2026 10:00**. Revised date Jun 13 → Jun 11, notes upgraded to "Source-locked Jun 11 2026 10:00 per investing.com OPEC calendar (revised from Jun 13 best-estimate per FASTOW Run 2 pre-fire verification)". TSV re-sorted to preserve ascending order (Jun 11 now sits between SPR ~Jun 10 and Jun 12 COT/BH).
- Rows skipped (date >7d out, not in pre-fire window): EIA STEO Jul 8 ("customary Tue early-month"), OPEC MOMR Jul 11 ("best-estimate date"), US CPI Jul 15 ("verify against BLS schedule"). Will fire when within 7d.

**Live-spot scan:** clean. No live price/level leaked into TSV cells.

**BASELINE AUDIT:** no audit trigger this run (Run 1 was same calendar day; monthly trigger next fires Jul 1+).

**STATUS ↔ TSV event-SET parity check:** **DIVERGENCE FOUND** — see ESCALATIONS below. STATUS § CATALYST CALENDAR (lines 202-218) shows ~13 events vs TSV's 24. Missing from STATUS: OPEC MOMR Jun (Jun 11), IEA OMR Jun (Jun 17), EIA WPSR Jun 17 / Jun 24, BH Jun 19 / Jun 26, COT Jun 19 / Jun 26, EIA STEO Jul 8, OPEC MOMR Jul 11, US CPI Jul 15, OPEC JMMC Jul 28. **All 12 of the Run-1 BRENT-applied additions are absent from STATUS.** This is the structural divergence Run 1 was supposed to surface — flagging now as Run-2 ESCALATION since the gap persists post-Run-1 close. (Possible BRENT explanation: STATUS calendar is a curated "load-bearing-only" view, not a 1:1 TSV mirror — if so, the TRUTH MODEL's "must not diverge in event SET" rule needs nuancing; see META-REVIEW Finding #4.)

**1-week retention check on FIRED rows:** none — OPEC+ Jun 7 still TODAY/PENDING.

**Runway:** 24 forward events; furthest is Sep 30 (XLE expiry, 115d). Healthy. Events in next 14d: 14 (dense pre-OPEC+ outcome week).

**Cost:** ~4 min (within Run 2 budget of 3-5 min for normal sync; Part A only).

**Notes:**
- Pre-fire date verification monitor caught a 2-day error on first invocation (OPEC MOMR Jun 13 → Jun 11) — same magnitude class as Run-1 STEO catch (Jun 11 → Jun 9). **Monitor validates: cadence-derived rows do drift, and 7-day pre-fire window is the right pre-emptive cadence.** Findings codified to MEMORY (auto-memory) candidate.
- Part B Meta-Review follows below (separate budget; see PENDING § Run 2 META-REVIEW).

---

### Run 1 — 2026-06-07 ~17:40 ET (Sun, pre-Globex, pre-OPEC+ outcome)

**Trigger:** First FASTOW run ever. Monthly baseline-audit trigger fires by definition.

**Read-set scan:**
- STATUS.md timestamp 2026-06-07 ~17:38 ET (fresh tonight) — Brent $94.66 Fri close; OPEC+ Vienna meeting TODAY with outcome PENDING; SPR ~350M floor Jun 10; Cushing 20M floor pushed to ~Jul 1; macro-transmission firing Jun 5 (VIX +40%, Fed-hike pricing).
- THESIS.md / TIMELINE.md not re-read in full (no thesis-version bump since Jun 3 intra-version POV pivot per CHANGELOG); STATUS holds the current operative framing.
- CHANGELOG last entry Jun 3 (catalyst baton-pass Cushing → SPR + PADD-3 export-pull + MD contamination discipline).
- CATALYSTS.tsv: 12 rows; date-sorted; no FIRED rows pending prune.

**Pruned:** none. No `— FIRED` rows in TSV. OPEC+ Jun 7 is TODAY with outcome PENDING — keep (will be FIRED post-tonight; eligible to prune after Jun 14 per 1-week retention).

**Added:** none — Run 1 is baseline-audit propose-only; all delta written to `## PENDING` for BRENT review.

**Refreshed (framing):** none. Spot-checked all 12 forward rows:
- Jun 10 EIA WPSR row already carries the directional-not-symmetric framing (`SPR throttle at ~350M = bullish; drain-through past 350M = near-term BEARISH + medium-term bullish (DIRECTIONAL, not symmetric)`) consistent with the Jun 3 Will-call correction. ✓
- Jun 12 CFTC COT row references the May 19 baseline (98,219, +25,418) which still matches STATUS. ✓
- BRT-27 / BRT-28 / OPEC+ / position-expiry framings match current STATUS. ✓

**Modeled-date revisions:** none. SPR ~350M floor row dated 2026-06-10 (modeled) matches STATUS storage section ("~350M operational floor ~1 wk out — Jun 10 EIA print is the floor-touch"). Cushing 20M floor row dated 2026-07-01 (modeled, REVISED) matches STATUS ("20M operational floor pushed to ~Jul 1"). EIA Jun 3 synthesis (`demand_destruction/data/eia_2026-06-03.md`) confirms both projections — no new data has landed since Jun 3 to shift either floor date.

**Live-spot scan:** clean. No live price/level leaked into TSV `what_to_check` or `threshold_signal` cells. All cells hold structural thresholds + significance only per TRUTH MODEL.

**BASELINE AUDIT (monthly trigger fired by definition — Run 1):** see `## PENDING` for full proposed delta. **Summary:** audited all 10 release classes vs source-of-truth. Window: today (Jun 7) through end-of-July (Jul 31). Found **~28 candidate gaps** (mostly recurring weekly releases beyond the first one in TSV, plus 5 monthly events not in TSV). Proposed delta written to PENDING for BRENT to apply selectively. None auto-added.

**Cost:** ~9 min (within 10-12 min budget for Run 1).

**Notes:**
- BRENT's GitHub modeled-date convention is working: `~` prefix renders in countdown for the 2 modeled rows. ✓
- STATUS § CATALYST CALENDAR matches TSV event SET. ✓ (1 date-divergence flagged in ESCALATIONS — see below.)
- Furthest event in TSV is Sep 30 (XLE expiry), 115 days out — healthy runway.

---

## PENDING

*Items FASTOW has surfaced for BRENT to act on. FASTOW adds; BRENT clears when resolved. Do NOT auto-clear from FASTOW — BRENT owns the close.*

### September 9 maintenance disposition (BRENT)

Historical decisions below remain a record, not current instructions. #1's curated-subset solution was superseded September 7 by full-set calendar generation (FASTOW.md § TRUTH MODEL, reconciled September 8). #9 now means BRENT regenerates and checks STATUS after every TSV change. #3/#5/#6 retain their recorded applied dispositions. #2 (third date tier), #4 (extra archive convention), #7 (additional release classes) and #8 (KOYOMI comparison) remain DEFERRED; no new schema, cadence, automatic archive threshold or cross-agent work adopted. This closes the stale-hints ambiguity, not the deferred research/design tasks. Current rules win over June run examples.

### Run 2 META-REVIEW (2026-06-07 ~21:08 ET) — propose-only findings

*BRENT requested a meta-review of FASTOW operation. All findings are propose-only escalations. FASTOW did NOT edit FASTOW.md or any other spec file. BRENT applies / declines / defers each finding. Sorted by impact.*

**✅ BRENT DISPOSITION (2026-06-07 retro applied):**
- **#1 APPLIED** — FASTOW.md § TRUTH MODEL clarified: STATUS calendar = curated load-bearing subset, NOT 1:1 mirror; inclusion rules set; FASTOW return block now flags "STATUS sync needed?" when changes require propagation.
- **#3 APPLIED** — FASTOW.md § BASELINE AUDIT now pre-declares default convention as light.
- **#5 APPLIED** — STANDING MONITOR § Pre-fire date verification now carries explicit halt-vs-continue rule (leave row + escalate on ambiguity/failure; do NOT silent-revise).
- **#6 APPLIED** — Run-1 PENDING delta condensed to one-liner above (~45 lines saved).
- **#9 APPLIED** — Return-block template now includes "STATUS sync needed?" line (closes #1's propagation gap).
- **#2 DEFERRED** — date_class third tier (cadence-derived) is sound but lower-urgency; notes-language heuristic is working (caught 2 errors on consecutive runs). Revisit if heuristic misses or if schema changes warranted by other reasons. Touches countdown.py code + spec + retag rows; not worth tonight.
- **#4 DEFERRED** — PENDING archive convention; revisit when FASTOW_MEMORY.md > 400 lines or PENDING > 150 lines. Currently fine.
- **#7 DEFERRED** — EIA MER + ad-hoc OPEC+ classes. Low impact for current Phase-1 thesis. Ad-hoc meetings are runtime watch (not pre-schedulable rows) — wrong mechanism. Revisit if Phase-2 activates.
- **#8 DEFERRED** — KOYOMI parity check. Read-only cross-agent task; next session.

**Auto-memory promoted:** Pre-fire date verification monitor on cadence-derived sub-agent rows codified as transferable lesson (`finding_subagent_prefire_date_verification`) — 2 consecutive runs catching 2-day errors is strong evidence; applies to any sub-agent maintaining date-keeping sets (SAM/KOYOMI, future).

#### ⚠️ ESCALATION-PROPOSE #1 (HIGH) — TRUTH MODEL ambiguity: is STATUS calendar a 1:1 TSV mirror or a curated load-bearing subset?
**Finding:** Run 2 STATUS↔TSV parity check found 12-event divergence (STATUS shows ~13 events; TSV holds 24). All 12 Run-1 BRENT-applied additions are absent from STATUS calendar. FASTOW.md § TRUTH MODEL says "STATUS's 📅 CATALYST CALENDAR section mirrors the TSV. Forward-event SET must match." Two reads possible: (a) STATUS calendar should be re-synced to TSV (Run-1 close left STATUS stale); (b) STATUS calendar is intentionally curated to load-bearing-only events and the "must not diverge in event SET" rule applies only to load-bearing rows, not full TSV.
**Recommended action:** BRENT clarifies in FASTOW.md § TRUTH MODEL. Either (a) STATUS calendar is a full mirror → BRENT re-syncs STATUS to TSV (add 12 missing rows); OR (b) STATUS calendar is a curated subset → FASTOW.md § TRUTH MODEL adds the curation rule: "STATUS holds the load-bearing subset; full event SET lives in TSV; FASTOW's parity check verifies STATUS subset ⊆ TSV (no STATUS row that's missing from TSV), not equality." Without clarification, FASTOW will keep firing this ESCALATION every run.
**Impact:** Every run produces a false-positive divergence flag → noise floor → BRENT desensitization to a real divergence when one fires.

#### ⚠️ ESCALATION-PROPOSE #2 (HIGH) — date_class binary undersells cadence-derived rows
**Finding:** Confirmed in Run 2 by OPEC MOMR Jun 13 → Jun 11 catch (2-day error, same magnitude as Run-1 STEO Jun 11 → Jun 9). Current schema has `confirmed` (source-locked) and `modeled` (projection that revises). But Run-1 added several rows tagged `confirmed` whose dates were actually cadence-derived best-estimates ("typical mid-month", "customary Tue"). The `confirmed` tag overstates verification state and silently bypasses pre-fire scrutiny. BRENT's post-Run-1 STANDING MONITOR (pre-fire date verification on notes-language heuristic) is a workaround, not a schema fix.
**Recommended action:** Add a third `date_class` value: `confirmed` (source-locked, verifiable URL+date) | `cadence-derived` (release class is known + cadence rule is established, but specific date is interpolated from cadence — e.g., "OPEC MOMR is mid-month") | `modeled` (data-driven projection that revises with new data, e.g., storage floors). Render in countdown with distinct prefix (proposal: `?` for cadence-derived, `~` for modeled, no prefix for confirmed). FASTOW's pre-fire monitor then keys off `date_class=cadence-derived` (deterministic) rather than notes-language heuristic (fragile to phrasing drift). Migration: Run-2 rows OPEC MOMR Jul 11, EIA STEO Jul 8, US CPI Jul 15 reclassify to `cadence-derived`. Requires `catalyst_countdown.py` to accept the new tier; ~5-line change.
**Impact:** Schema clarity + monitor reliability. Removes ~30s/run of notes-string scanning.

#### ⚠️ ESCALATION-PROPOSE #3 (MEDIUM) — Spec doesn't specify default audit convention (heavy vs light)
**Finding:** Run-1 surfaced this gap implicitly — FASTOW had to ask BRENT "did you want full-window expansion or rolling-light?" mid-run. Spec § BASELINE AUDIT specifies the universe + execution rubric but doesn't pre-declare a default convention. Run-1 chose heavy default ("first-run baseline value is to surface the full set"), BRENT chose light, CALIBRATION codified light. But next month's baseline audit will face the same choice again unless spec encodes the default.
**Recommended action:** Add to FASTOW.md § BASELINE AUDIT execution rubric: "**Default convention:** light (next-rolling-1 per weekly release class). Heavy expansion (full forward window) only on (a) first-ever baseline audit, (b) post-thesis-bump audit where forward planning matters, or (c) explicit BRENT request via NEXT RUN HINTS. The light default is preserved across BRENT-CALIBRATION-declined classes." Removes the recurring convention call from monthly audits.
**Impact:** Eliminates one decision round-trip per monthly audit.

#### ⚠️ ESCALATION-PROPOSE #4 (MEDIUM) — Memory-file PENDING section will accumulate; needs archive convention
**Finding:** PENDING currently holds Run-1 baseline-audit delta (28 rows, ~50 lines) marked ✅ RESOLVED. Each subsequent audit will add similar block. By Run 6-12 the file will be dominated by historical PENDING noise. Spec says "BRENT clears when resolved" but no archive destination specified.
**Recommended action:** Add to FASTOW.md a § MEMORY HYGIENE subsection: "Resolved PENDING items >30 days old condense to one-liner ✅ resolved entry + archive link to `docket/FASTOW_PENDING_ARCHIVE.md`. FASTOW prunes during normal sync (not just baseline audits); BRENT may pre-prune. Threshold: when FASTOW_MEMORY.md >400 lines OR PENDING section >150 lines, force a prune pass." Mirrors BRENT's own thesis/PREDICTIONS_ARCHIVE.md convention.
**Impact:** Keeps boot-read fast; memory file stays scan-friendly.

#### ⚠️ ESCALATION-PROPOSE #5 (MEDIUM) — Pre-fire monitor needs explicit halt-vs-continue rule on source-fetch failure
**Finding:** Pre-fire monitor (BRENT post-Run-1 addition) fetches sources for cadence-derived rows within 7d. Run 2 hit cleanly (investing.com confirmed Jun 11 within 2 tool calls). But if source returned ambiguous data (e.g., investing.com showed Jun 11 AND Jun 13 in conflicting calendars; or fetch failed with 404), no behavior spec. Apply best-guess? Halt and flag? Use original date?
**Recommended action:** Add to STANDING MONITOR § Pre-fire date verification: "On source-fetch ambiguity or failure: leave original date, flag ⚠️ ESCALATION-PROPOSE in return block + PENDING, do NOT silent-edit. Three-source rule: if two independent sources agree, accept; if disagree or only one source available, flag." Removes silent-failure risk.
**Impact:** Prevents the pre-fire monitor itself from becoming a silent data-corruption vector.

#### ⚠️ ESCALATION-PROPOSE #6 (LOW) — Run 1 PENDING entry contains the full 28-row proposed delta even after resolution; could be condensed
**Finding:** Lines ~67-113 hold the full Run-1 proposed-delta table even though the ✅ RESOLVED entry at lines ~59-66 summarizes which rows were applied. Information is now redundant; the TSV itself is the source of truth for what was applied.
**Recommended action:** BRENT condense the resolved-delta block to one-liner: "✅ Run-1 baseline audit: 12 events applied + 16 declined; full proposal-table archived to `FASTOW_PENDING_ARCHIVE.md#run-1-baseline-audit` (proposed path, never created) for audit trail." (Implements #4 above by demonstration.)
**Impact:** ~45 lines saved in FASTOW_MEMORY.md.

#### ⚠️ ESCALATION-PROPOSE #7 (LOW) — Recurring-release universe missing two BRENT-relevant classes
**Finding:** Spec § BASELINE AUDIT universe table (~10 classes) is missing: (a) **EIA Monthly Energy Review / Petroleum Supply Monthly** (monthly, deeper than WPSR; relevant to refinery margins / production by PADD) — could be in-scope if Phase-2 demand-destruction tracking ramps; (b) **OPEC+ ad-hoc / emergency / video meetings** (irregular, but historically common during high-volatility periods like current MOU regime; surfaced via OPEC press releases not the JMMC schedule). Both omitted from Run-1 audit by default.
**Recommended action:** BRENT decides whether to add. If yes, append rows to universe table. If no, codify the decision in CALIBRATION so future spec readers know it was considered.
**Impact:** Small now (Phase-1 thesis); larger if Phase-2 activates.

#### ⚠️ ESCALATION-PROPOSE #8 (LOW) — KOYOMI parity check: FASTOW heavier than KOYOMI?
**Finding:** Could not directly compare KOYOMI spec without reading it (out of scope for FASTOW). But Run-1 spec auto-memory note `[finding_subagent_naming_identity_over_functional]` + `[finding_subagent_memory_split]` suggest KOYOMI and FASTOW are intentionally parallel. FASTOW.md is 17KB / ~160 lines; spec includes 5-job-step rubric + baseline-audit universe + decline-memory + TRUTH MODEL + retention rules. If KOYOMI is lighter (e.g., no decline-memory), FASTOW may have over-evolved relative to peer. If KOYOMI is heavier (e.g., has explicit cadence-derived tier already), FASTOW may be under-evolved.
**Recommended action:** BRENT cross-checks against KOYOMI spec (SAM owns) once and either (a) confirms parity is intentional asymmetry, or (b) ports any KOYOMI improvements that BRENT wants. Out-of-scope for FASTOW to do directly (no SAM directory read in WRITE-SET).
**Impact:** Coordination-level; not blocking.

#### ⚠️ ESCALATION-PROPOSE #9 (LOW) — Spec ambiguity: who owns the human-readable STATUS calendar refresh after FASTOW TSV edits?
**Finding:** Spec says BRENT owns STATUS edits. Run-1 left a known divergence (Jun 11 STEO date corrected in TSV; BRENT applied to STATUS via Run-1 retro). Now Run-2 produces Jun 11 MOMR correction; STATUS doesn't list MOMR at all (so no update needed). But the pattern shows: every cadence-derived correction FASTOW makes potentially requires a downstream BRENT STATUS edit. No explicit cadence rule for "when does BRENT sync STATUS post-FASTOW run?"
**Recommended action:** Add to FASTOW.md DONE checklist: "FASTOW return block includes 'STATUS sync needed?' line (Y/N + which fields). BRENT applies during own next-session closeout." Closes the propagation loop without requiring real-time coordination.
**Impact:** Prevents the very divergence Finding #1 surfaced.

#### Workflow friction observations (not escalations)

- **Run 2 was budget-clean** at ~4 min. Pre-fire monitor was the only non-trivial step (1 WebSearch + 1 WebFetch). All other steps were no-ops (no FIRED rows, no thesis movement, no modeled-date shifts).
- **The TSV re-sort step** after a date revision is manual (bash sort). Could be `catalyst_countdown.py --sort-check` returning non-zero if unsorted. Not urgent.
- **CALIBRATION-read** before audits is critical and was honored Run 2 (no audit fired so no read needed). No friction.

### ✅ RESOLVED 2026-06-07 — Run-1 BASELINE AUDIT (BRENT applied)

**Resolution summary:**
- STEO date correction applied (Jun 11 → Jun 9 in TSV + STATUS) ✓
- 12-row light-convention delta applied to CATALYSTS.tsv: OPEC MOMR Jun 13, IEA OMR Jun 17, EIA WPSR Jun 17 + Jun 24, CFTC COT + Baker Hughes Jun 19 + Jun 26, EIA STEO Jul 8, OPEC MOMR Jul 11, US CPI Jul 15, OPEC JMMC Jul 28 ✓
- 16 weekly rows declined per CALIBRATION light-convention (see Declined release classes below) ✓
- CPI Jul 15 INCLUDED per BRT-16 macro-transmission firing visibly Jun 5 (BRENT call) ✓

### Run-1 BASELINE AUDIT proposed delta — historical, condensed 2026-06-07

Run-1 baseline audit proposed 28 additions + 1 date-correction (STEO Jun 11 → Jun 9). BRENT applied 12-row light-convention delta + 1 STEO fix; 16 weekly forward-expansion rows declined per CALIBRATION. Full delta table preserved in git history at commit `5c06ac5c` (FASTOW_MEMORY.md pre-condense). Condensed here per Run-2 META-REVIEW Finding #6 (avoid PENDING bloat). If future audit/review needs the original delta, recover from git history.

---

## STANDING MONITORS

*Recurring watches FASTOW should check every run (in addition to baseline-audit triggers). Seed list — extend as patterns emerge.*

- **Modeled-date rows** — every run, check CATALYSTS.tsv rows with `date_class=modeled` against current STATUS storage section. Currently active: SPR 350M floor (Jun 10), Cushing 20M floor (Jul 1). Update dates if STATUS projection has shifted. *(Run 1: both confirmed against STATUS, no revision.)*
- **STATUS ↔ TSV event-SET divergence** — every run, verify STATUS § CATALYST CALENDAR section matches TSV event set. Surface divergence as ESCALATION; don't edit STATUS. *(Run 1: event SET matches; but Jun 11 STEO date is wrong in BOTH — flagged for BRENT.)*
- **1-week retention on `— FIRED` rows** — every run, prune any `— FIRED` row whose date is >7 days past today. *(Run 1: no FIRED rows; OPEC+ Jun 7 will become first candidate after Jun 14.)*
- **NEW (post-Run-1) — OPEC+ Jun 7 outcome ingestion:** OPEC+ Vienna row currently `2026-06-07 ... — TODAY` with outcome PENDING. After tonight's outcome is known (Mon AM integration), BRENT should rename the event to `OPEC+ Regular Meeting (Vienna 41st) — FIRED [outcome summary]` and the 1-week retention clock starts. Next FASTOW run prunes if >7 days past.
- **NEW (added by BRENT post-Run-1 retro 2026-06-07) — Pre-fire date verification for cadence-derived rows.** Every run, scan TSV rows whose `notes` column contains "best-estimate," "verify against," "cadence-derived," "typical," or "customary" language. For any such row whose projected date is within the next **7 calendar days**, re-fetch source-of-truth (per § BASELINE AUDIT release-class table) and revise the date if shifted. **Rationale:** Run 1 produced 12 net additions of which several were cadence-derived (OPEC MOMR Jun 13, OPEC MOMR Jul 11, US CPI Jul 15, EIA STEO Jul 8) — the `date_class=confirmed` tag overstates their verification state. STEO Jun 11 was a 2-day error caught by source-check; same risk applies to these. Cost ~1 min per row (single source fetch). Surface revisions in LAST RUN entry as "Pre-fire date verification: ROW X-Y-Z confirmed source-locked / revised old→new." If a row's notes have NO such uncertainty language, skip it (already trusted source-locked). **Halt-vs-continue rule (per Run-2 META-REVIEW Finding #5):** if source fetch on a candidate row returns AMBIGUOUS or NO clear date, **do NOT revise the row** — leave the existing date in place AND log to ESCALATIONS in the return block as "Pre-fire verification ambiguous: ROW X-Y-Z, source returned [no result / multiple candidates / unreachable]; manual check needed." Silent revert or speculative revision can corrupt the docket; explicit escalation lets BRENT triage. **Run 2 validation:** monitor caught OPEC MOMR Jun 13 → Jun 11 (2-day error) on first invocation; same error magnitude as Run-1 STEO catch. Monitor is earning. See PENDING Finding #2 for proposed schema-level fix (`date_class=cadence-derived` tier) that would replace the notes-language heuristic with a deterministic key.

---

## CALIBRATION

*BRENT-owned section. FASTOW reads but never writes here. Records which release classes BRENT has declined to track under the current thesis lens — prevents baseline-audit from re-proposing the same classes every month.*

### Declined release classes

- **Weekly recurring releases (EIA WPSR / CFTC COT / Baker Hughes) — forward expansion past rolling next-2** — declined 2026-06-07. Reason: routine telemetry releases, not action-forcing decision gates beyond the next 1-2 of each class; full forward-window expansion bloats the docket without adding decision value (countdown shows them anyway). Per FASTOW Run 1 baseline audit; matches KOYOMI/SAM light-convention precedent. Re-evaluate if: thesis shifts to require quarterly forward planning, or a specific weekly print becomes structurally load-bearing (e.g., a particular Cushing print being the WTI-dislocation forcing event).

**Format when added:**
```
- {class name} — declined YYYY-MM-DD. Reason: {one-line — what about the current thesis lens makes this class out-of-scope}. Re-evaluate if: {condition that would bring it back in scope}.
```

---

## NEXT RUN HINTS

**BRENT seed, September 9 maintenance; no new FASTOW run claimed.** Re-read FASTOW.md before using historical run notes. Prior hints are preserved verbatim in [archive](../archive/FASTOW_HINTS_2026-09-09.md).

- Current state is CATALYSTS.tsv plus ../SCRATCH.md. September STEO is published; comparison remains pending. Next WPSR is September 10 noon ET / later files 14:00, observation September 4; Friday COT requires September 8 as-of. Release occurrence alone does not complete the associated analysis.
- STATUS calendar uses the entire TSV event set, generated by BRENT with ../scripts/render_calendar.py --write then --check. The June curated-subset convention is superseded. No hand-edited calendar and no third date_class: retain confirmed/modeled.
- Expired dates are not grades. Keep unresolved rows; prune only graded/fired rows after the existing retention period. Historical June/July examples in run history and STANDING MONITORS do not establish current catalyst dates or levels.
- USO October call is closed; no October 9 management action survives. XLE receipt remains pending; no execution inference. TRADE owns holdings and action state.
- Apply current monthly/pre-fire audit triggers from FASTOW.md, not the old Run-3 countdown. Deferred meta-review items remain optional backlog under the disposition below, not mandatory next-session changes.
