# FILTER v1 → v2 Review Plan

**Status:** Segment A COMPLETE 2026-04-20 evening. Segments B/C/D scheduled post-Apr-21 catalyst day.
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

### SEGMENT B — Same-theme combine rule

Codify the rule invoked 5+ times this month: if 2+ images/posts surface the same underlying event/theme in the same intake batch, combine into one signal with multiple origin attributions, not duplicate signals.

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

### SEGMENT C — Verify-research Phase 1.5 trigger

Codify autonomous verify-research sub-agent spawn. Caught 4 framing errors this month (BOJ ¥330B misframed, WhaleInsider Hormuz "zero tankers / first in history" false, Blue Owl "co-founders" / "alt-collateral" overstated, SIG-029 "first NATO state-response" inaccurate).

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

### SEGMENT D — Confidence asymmetry (design-heaviest)

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
