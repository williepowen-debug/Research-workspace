# FASTOW MEMORY

State file for the docket-steward sub-agent. Spec is in [`FASTOW.md`](FASTOW.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership:** FASTOW writes this file directly at end-of-run (consistent with FASTOW's other write privileges — full-edit mode by default, busy-work-only). BRENT may pre-edit between runs to seed `## NEXT RUN HINTS`, `## PENDING`, or `## CALIBRATION`.

**Spawn order:** FASTOW reads `FASTOW.md` first (spec), then `FASTOW_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last synced*.

---

## CHANGES SINCE LAST RUN

*FASTOW run field; no new run claimed. Current reads are STATUS/THESIS/CHANGELOG/CATALYSTS; TIMELINE is frozen history.*

*(cleared end-of-Run-2)*

---

## LAST RUN

Last recorded steward run: Run2, June7,2026; no new FASTOW run claimed. Full dated run history is preserved verbatim in [before-image](../archive/2026-10-14_operational-followups/FASTOW_MEMORY.md#last-run), 27634 UTF-8 bytes, crc32 `effaa330`; payload rule whole file. Pending material/calibration below remains retained, not resolved by this rotation. Current owner guidance is NEXT RUN HINTS.

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

**BRENT owner reconciliation October14; no new FASTOW run.** Last recorded steward run remainsJune7. Older run results/standing monitors above retain their dates, not current completion or action state. The previousSeptember9hints are preserved in [whole-file before-image](../archive/2026-10-14_operational-followups/FASTOW_MEMORY.md); [manifest](../archive/2026-10-14_operational-followups/manifest.json) gives exact bytes/CRC/SHA.

- Read FASTOW.md, current CATALYSTS and ../SCRATCH.md. October14OMR public read complete; October15Board/WPSRweekOctober9 future. Existing VLObasis transition, October16COT, October26BRT30 and November1DST remain at their owners. Do not reuse September dates or old position/receipt labels from historical hints.
- STATUS calendar is the generated full TSV event set: BRENT runs render_calendar.py --write then --check. No hand edits, new date_class or automatic forward expansion beyond retained CALIBRATION scope.
- Expired dates are not grades; retain unresolved rows. TIMELINE remains frozen. Current holdings/outcomes/approval are read from ../TRADE.md; no cached USO/XLE statement here.
- June meta-review proposals remain dated optional backlog; current adopted FASTOW.md/rulings win where they already resolved an issue. Do not turn them into a new monitoring/research commission or mandatory protocol.
