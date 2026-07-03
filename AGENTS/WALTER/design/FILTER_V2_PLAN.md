# FILTER v1 → v2 Review Plan

**Status:** ✅ **v2 COMPLETE 2026-07-03** — all 4 segments shipped. Segment D (`confidence_note`, Will Option A) landed 7/3 into **FORMAT_SPEC v0.13 + CHECKLIST v0.23**. **→ FILTER v3 review now DUE** (trigger long-passed: 434 dispatches vs the 50/30-day bar). Archive-eligible to `design/history/` (deferred as trivial; CLAUDE.md + STATE refs updated in place). *[was: A+B+C complete 4/20; D deferred post-Apr-21 — the deferral ran ~2.5mo as implementation debt, cleared 7/3 per Will "you can execute".]*
**Scope:** Full 7-item revision across FILTER_SPEC, FORMAT_SPEC, ROUTING_TABLE, and SIGNAL_PROCESSING_CHECKLIST
**Trigger:** 10+ dispatches OR 30 days from Apr 11 (reached at 51 dispatches = 41 past threshold).

## Diagnostic Headline

**v1 is structurally working.** Empirical review of 51 dispatches + 18 kill_log entries (Apr 11–Apr 20):
- Zero obvious false positives in kills (no killed signals that should have routed)
- Routes look reasonably calibrated (confidence floor worked on 3 entries at 0.20/0.22/0.30)
- No need to rewrite filter architecture

**What v2 addresses:** 3 real spec gaps + 4 codifications of informal practice that's emerged in use.

---

## Segmentation

Work is broken into 4 segments. Plan: conservative timing — Segment A today (Apr 20), B/C/D post-Apr-21 catalyst day.

### SEGMENT A — Easy wins (IN PROGRESS 2026-04-20)

Small additive changes + posture updates. Low risk. Clears small items so bigger work doesn't drag them.

| # | Change | Doc | Version Bump |
|---|--------|-----|--------------|
| 2 | Add `thesis-frame` to signal_type enum | FORMAT_SPEC | v0.4 → v0.5 |
| 5 | Add geographically-narrow residential → REGINALD routing rule | ROUTING_TABLE | v0.4 → v0.5 |
| 6 | Retire "START LOOSE" default posture (2-week window expired Apr 25 but we're past trigger at 41 dispatches) | FILTER_SPEC | v0.2 → v0.3 |
| 7 | Bypass pre-Apr-21 reaffirmation note (zero FLASH signals in 51 dispatches; reaffirm triggers for catalyst day) | FILTER_SPEC | same v0.3 bump |

**Expected time:** ~30 min, one pass.

### SEGMENT B — Same-theme combine rule (COMPLETE 2026-04-20 evening)

Codified the rule invoked 5+ times this month. Final form is domain-anchored (not intake-batch-anchored per original plan) after Will design round-trip — see FORMAT_SPEC v0.6 Multi-Origin Signals section and CHECKLIST v0.7 Phase 1b for deployed text.

Original plan text preserved below for history.

Instances this month:
- SIG-W-20260419-004: Wyckoff + NDX 25-yr parabolic (same author @FinanceLancelot)
- SIG-W-20260419-010: Flightradar24 Doha + Peter Hague Celestyal cruise (CROSS-author, same theme)
- SIG-W-20260419-017: Bilello VIX-3wk + Bilello SPX-3wk (same author)
- SIG-W-20260419-024: @disclosetv carrier build-up + @BRICSinfo talks rejected (CROSS-author, same theme)
- SIG-W-20260419-026: @axios + @Polymarket Iran ship intercept (CROSS-author, same theme)

**Design decision needed:** combine criteria. Current informal rule:
- (a) Same underlying event OR theme
- (b) Arrived in same intake batch (intra-batch) OR cross-batch within ≤24h
- (c) Same author NOT required (3 of 5 instances were cross-author)

| Doc | Edit |
|-----|------|
| FORMAT_SPEC body conventions | New subsection: "Multi-Origin Signals — Same-Theme Combine Rule" |
| SIGNAL_PROCESSING_CHECKLIST | New process step in Phase 1: "Check for same-theme combine before classifying" |

**Expected time:** ~30 min, one pass. Will review draft rule text before commit.

### SEGMENT C — Verify-research Phase 1.5 trigger (COMPLETE 2026-04-20 evening)

Codified autonomous verify-research sub-agent spawn. Caught 4 framing errors this month (BOJ ¥330B misframed, WhaleInsider Hormuz "zero tankers / first in history" false, Blue Owl "co-founders" / "alt-collateral" overstated, SIG-029 "first NATO state-response" inaccurate).

Deployed form (see CHECKLIST v0.8 Phase 1.5 + FILTER_SPEC v0.4 reference):
- 4 trigger patterns narrowed from original draft — extraordinary-claims restricted to extreme absolutes only ("zero", "first in history", "largest ever", "never before", "unprecedented"), explicitly NOT falsifiable comparatives like "record high" / "biggest since 2021" / "5th largest" which self-bound and are routinely checkable. Mechanism-assertions narrowed to claims NOT YET IN PRIMARY COVERAGE.
- Spawn discipline anchored to auto-memory `feedback_subagent_prompt_discipline` (lead with decision, word cap, VERDICT top, decision-usefulness — do not template).
- 4-verdict taxonomy: CONFIRMED (proceed) / CORRECTED-framing (rewrite + lower confidence one band) / FALSE (kill with framing-false reason) / INDETERMINATE (route at `unconfirmed` tier + note).
- Discretion preserved: if WALTER already has primary open in-session and claim matches, note inline-verification and skip spawn.

**Design decision needed:** trigger criteria. Current informal rule:
- (a) Secondhand source citing primary (e.g., WSJ-via-X-aggregator)
- (b) Summarizing plurals in source framing ("co-founders", "all three", "both")
- (c) Mechanism-assertions ("replaced with", "swapped for", "backed by")
- (d) Extraordinary claims ("zero", "first in history", "largest ever", "never before")

| Doc | Edit |
|-----|------|
| SIGNAL_PROCESSING_CHECKLIST | New Phase 1.5 step between Gate 1 pass and credibility check |
| FILTER_SPEC | Reference-only note pointing to CHECKLIST Phase 1.5 |

**Expected time:** ~30 min, one pass. Will review criteria before commit.

### SEGMENT D — Confidence asymmetry (✅ SHIPPED 2026-07-03 — `confidence_note` landed in FORMAT_SPEC v0.13 + CHECKLIST v0.23; Will Option A, decided 4/20, implemented 7/3)

**Will decision (Telegram msg 856):** Option A — add optional free-text `confidence_note` field. Smallest footprint, non-breaking, prose captures asymmetry the way WALTER naturally describes it.

Implementation plan (Session 1, ~30 min, post-Apr-21):
- **FORMAT_SPEC edit:** Add `confidence_note` (optional string, free text) to the signal header schema under the Confidence Model section. Describe invocation rule: "use when observation quality and interpretation quality diverge materially (≥1 confidence band apart). Example phrasing: 'observation 0.85 / interpretation 0.40 — broadcast physically verified by SDR community but ops-vs-training intent ambiguous.'"
- **CHECKLIST guidance:** New Phase 2 note (in Classify section, near Confidence mapping table) flagging when to reach for the optional field. Not a mandatory gate — discretion based on the gap.
- **No migration required** (this was the point of picking A). Existing 51 signals stay as-is. Backfill is optional and opportunistic, not a required pass.

Implementation plan (Session 2, optional, ~45 min):
- Opportunistic backfill on ~5-8 historical signals where the asymmetry was material and worth documenting retrospectively (SIG-022 EAM/E-6B, SIG-W-20260419-010 Flightradar Doha, SIG-W-20260420-004 Blue Owl pre-verify draft, candidates TBD on re-read).
- Lower priority than new-signal throughput or refresh cycles — can slot into a quiet session.

---

### SEGMENT D — Original design comparison (preserved for history)

Solve observation-vs-interpretation split. SIG-022 EAM/E-6B observation was verifiable (priyom.com + SDR community) but interpretation ambiguous (training vs alert vs ops). Coded as single 0.40 — suppresses both the solid observation and the real interpretation doubt.

**Design round-trip required before coding.** Three candidate approaches:

| Option | Mechanic | Pro | Con |
|--------|----------|-----|-----|
| (i) `confidence_note: free text` optional field | Single extra field capturing asymmetry verbally | Simple, non-breaking, already aligns with how I'd describe the asymmetry in prose | Non-structured — can't filter mechanically on it |
| (ii) Split into `observation_confidence` + `interpretation_confidence` numerical pair replacing single `confidence` | Structured dual numeric fields | Mechanical filtering possible, precise | Breaks all existing signals, requires migration, most signals won't have asymmetry and will just carry two identical values |
| (iii) `signal_type` modifier `observation-only` vs `with-interpretation` enabling different confidence treatment | Flag-based, confidence stays single | No schema break, flag-gates confidence interpretation | Mixes signal_type enum with confidence semantics — conceptually muddy |

**WALTER lean:** (i). Simplest, preserves existing signals, allows prose to do what prose does. But Will decides.

| Doc | Edit |
|-----|------|
| FORMAT_SPEC confidence model | Add optional `confidence_note` field OR chosen alternative |

**Expected time:** 1-2 sessions. First session = design round-trip with Will. Second = implementation + backfill of existing asymmetric signals with retrospective notes.

---

## Completion Criteria

✅ **ALL MET 2026-07-03** — Segment D (`confidence_note`) shipped into FORMAT_SPEC v0.13 + CHECKLIST v0.23; all 7 items landed in their owning docs; specs version-bumped + STATE §1 synced (drift-guard green); **FILTER v3 review trigger now fired (434 dispatches ≫ 50) → v3 review is the next filter-hygiene task.** Plan archive-to-history deferred as trivial.

Filter v2 is complete when:
- All 7 items are implemented in their owning docs
- FILTER_SPEC, FORMAT_SPEC, CHECKLIST, ROUTING_TABLE all version-bumped
- STATUS.md OPERATIONAL STATE table reflects new versions
- Next FILTER v3 trigger set (next 10+ dispatches OR 30 days from v2 completion date, whichever first)
- This plan file is deleted (or archived to `design/history/`)

---

## Log

| Date | Segment | Action |
|------|---------|--------|
| 2026-04-20 | Plan | Plan written to disk. Segment A started. |
| 2026-04-20 (evening) | A | COMPLETE. FORMAT_SPEC v0.4→v0.5 (thesis-frame signal_type), ROUTING_TABLE v0.4→v0.5 (thesis-frame row + Residential-housing stress exception), FILTER_SPEC v0.2→v0.3 (START LOOSE retired → BALANCED + empirical bypass note + Pre-Apr-21 reaffirmation with 6 triggers). STATUS.md OPERATIONAL STATE + Filter Posture + Upcoming + session log updated to v0.17. Segments B/C/D deferred post-Apr-21. |
| 2026-04-20 (evening, same session) | B | COMPLETE. Will requested we proceed past A into B same session. Design round-trip on 3 questions (intra-batch scope, origin format, combine ceiling), then friction-test of draft rule surfaced batch-boundary ambiguity and theme fuzziness. Will pushed back on both — reworked to domain-anchored + any-arrival-path-pre-dispatch + immutable-post-dispatch. FORMAT_SPEC v0.5→v0.6 (Multi-Origin Signals section + origin field accepts array). CHECKLIST v0.6→v0.7 (Phase 1b combine check added between intake and classify). STATUS.md updated to v0.18. Original plan flagged this at ~30 min; actual closer to 45 min with Will design round-trip. |
| 2026-04-20 (evening, continuation post-/clear) | C | COMPLETE. Will asked to continue with Segment C after Telegram /clear (session continuity preserved). Draft presented with 4 trigger patterns; Will greenlit ("seems good") after narrowing of extraordinary-claim scope (only absolutes, not falsifiable comparatives) and mechanism-assertion (only claims not yet in primary coverage). CHECKLIST v0.7→v0.8: new Phase 1.5 section with trigger-pattern table, spawn-prompt discipline bullets, and 4-verdict handling table; plus step 2.5 cross-ref inserted into Phase 1 kill/keep code block. FILTER_SPEC v0.3→v0.4: reference-only subsection between Gate 1b (Relevance) and Credibility Check pointing to CHECKLIST Phase 1.5 as canonical. STATUS.md updated to v0.19 (OPERATIONAL STATE rows, UPCOMING collapsed to D-only, session log, footer). ~30 min actual. |
| 2026-04-20 (evening) | D | MECHANIC DECIDED. Will asked "what is Segment D plan" — presented 3-option framing (free-text note / split numerical pair / signal_type modifier) with WALTER lean (i). Will picked A (free-text `confidence_note`) in Telegram msg 856. Implementation deferred to post-Apr-21 catalyst per earlier "no rush" framing. Plan preserved in Segment D section of this doc for pickup next session. |
