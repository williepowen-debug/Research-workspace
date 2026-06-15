# MARCO — MAINTENANCE PUNCHLIST

**Purpose:** Standing list of stale / needs-attention items flagged for action at a later session. Flag-and-document only — items here are NOT yet fixed. Work them down at boot when not mid-event; check items off + date them.

**Created:** 2026-06-08 (session 12 — flag-and-document sweep while waiting on LABOR). Method: boot.py awareness layer + manual file read across all MARCO docs. Ranked by **behavioral impact** (does the agent DO something different?), not line count.

---

## TIER 1 — thesis-load-bearing (fix first)

### ✅ T1-A · FINDINGS.md points to the WRONG thesis version + carries a stale "Live state" block — DONE 2026-06-15
*(Resolved: bumped v2.0→v2.5; "Live state" block rewritten to pure pointers, no restated drifting values; header date refreshed.)*
- **What:** `FINDINGS.md` (the boot navigator) line 71 says "thesis/THESIS.md (**v2.0**, canonical)" — actual is **v2.4**. Lines 63-73 ("Live state — refreshed 2026-05-31") *restate* STATUS values that have since drifted: remittances "Mar +4.9% / count −3.6%" (now Apr +3.7% / count −1.7%), Canadian "Apr +1.4% headline" (pre-session-9 base-effect correction), produce "+6.1% (ag-labor stock loss)" (pre-v2.1 multi-causal resolution).
- **Why it matters:** FINDINGS is a navigator a fresh spawn may read to orient — a v2.0 pointer + drifted live-values misdirects. Violates single-source-of-truth (file even says "Not a synthesis — a navigator").
- **Action:** Bump v2.0→v2.4; prune the "Live state" block to pure pointers (no restated values — point to STATUS/thesis).
- **Effort:** small.

### T1-B · NOTES.md flags a data-quality tension under Channel 1's load-bearing 2.2M figure
- **What:** `NOTES.md` (deportation data discrepancy): DHS claims 2.5M departures (1.9M self-deported) vs independent deportation counts ~290-340K (MPI/Brookings/TRAC) — "DHS 7-8× higher, self-deportation methodology disputed." The thesis's durable Channel-1 driver is the **2.2M self-deportation stock shock (CBO)**.
- **Why it matters:** The spine of Channel 1 rests on a self-deportation magnitude that MARCO's own data-quality note flags as disputed. The *directional* claim survives at lower magnitude, but the headline number should be reconciled (CBO 2.2M vs DHS 1.9M self-deported vs the disputed methodology) — and a load-bearing figure shouldn't sit un-cross-referenced.
- **Action:** Reconcile the 2.2M source-of-record; add a one-line confidence/caveat to STATUS where 2.2M is cited (it's stated flat). Decide if the number needs a ±band.
- **Effort:** medium (judgment).

### ✅ T1-C · H-2A "requested vs certified" series ambiguity in MAR-11 — DONE 2026-06-15
*(Resolved: MAR-11 note now specifies threshold on CERTIFIED series, FY25 certified 398,059, '415K' was requested; cross-refs FINDINGS/OFLC. NEW flag found while editing → see T1-D below.)*
- **What:** Today's h2a_pull returned FY25 **certified = 398,059**. `FINDINGS.md` line 55 already resolves it: "prior '415K' was positions **REQUESTED**." But `PREDICTIONS.tsv` MAR-11 ("H-2A certifications >425K, FY2026") still carries the note "FY2025 was 415K" without the requested-vs-certified distinction.
- **Why it matters:** MAR-11 resolves at the ~Jun-30 OFLC Q3 window. If scored against 415K-requested baseline instead of 398K-certified, the threshold read is wrong. Canonical-measure discipline.
- **Action:** Edit MAR-11 note to specify certified-series (FY25 certified 398,059; prediction threshold = certified >425K). Cross-ref FINDINGS/OFLC_H2A_PULL.
- **Effort:** small.

### T1-D · PREDICTIONS.tsv has inconsistent column count (NEW — found 2026-06-15)
- **What:** Column-count distribution across `thesis/PREDICTIONS.tsv` = `{9-col: 3 rows, 8-col: 14 rows}` vs a 9-col header (Pred_ID…Outcome…Notes). Most data rows (14) are **missing the `Outcome` field** — Notes sits where Outcome should be positionally.
- **Why it matters:** `predictions_due.py` currently tolerates it (Timeframe is field 4, before the gap, so the due-scan parses fine), but any positional read of Outcome/Notes is wrong on 8-col rows, and a future schema-strict parse would misalign. Latent, not yet behavioral.
- **Action:** Normalize all rows to 9-col by inserting the empty `Outcome` field (verify `predictions_due.py` + any consumer reads by header-name, not position, before/after). Do in one pass — likely fold into the post-Jun-30 PREDICTIONS_ARCHIVE/calibration build (SCRATCH punchlist #2).
- **Effort:** small (but verify parser).

---

## TIER 2 — stale state / single-source-of-truth

### T2-A · STATUS.md internal stale blocks
- **What:** (1) "NEXT SESSION FOCUS (2026-05-31)" block — pre-Pull-Session-1; its Tier-1 item "resolve remittance paradox" already RESOLVED 6/2. Duplicates SCRATCH's NEXT SESSION (forward-planning should live in SCRATCH, not STATUS). (2) "CROSS-AGENT SIGNALS — NEEDS RE-SEND" block (Apr 21-23 signals) — deferred for ~7 weeks; **may now be superseded by NEXUS_BRIEF** as the cross-agent surface (built today).
- **Why it matters:** Two forward-planning sources drift apart; the re-send backlog may be obsolete under the new brief mechanism.
- **Action:** Prune STATUS "NEXT SESSION FOCUS" → pointer to SCRATCH. Decide whether the re-send backlog is now handled by NEXUS_BRIEF SENDING table (likely yes) and retire or convert it.
- **Effort:** small-medium.

### ✅ T2-B · RESEARCH_STATUS.md drift — DONE 2026-06-15
*(Resolved: remittance paradox + FLL-April → COMPLETE; ag-weather refreshed as open PROME loop; TOURISM row = SHELVE-sub-agent/KEEP-vector decision (was mislabeled "stalled"); StatCan Q1→Q2 gap re-dated; FL-airport gap → MCO-only/BTS-July. Header date refreshed.)*
- **What:** (1) "Remittance paradox" still under ACTIVE — RESOLVED 6/2 (paradox fading), should move to COMPLETE. (2) TOURISM listed DORMANT/"stalled, no commits since Apr 22" — **contradicts the session-11 finding** that TOURISM is NOT stalled (content current, refreshed session 9; ran a live World Cup pull 6/2). (3) "StatCan Q1 2026 BOP" GAP — superseded by Q2 (~Aug 28) per docket. (4) "Ag-weather/crop-disaster owner" — flagged to PROME 5/31; assignment status unknown (open loop).
- **Action:** Move remittance paradox → COMPLETE; correct/remove the TOURISM-stalled entry; re-date StatCan gap to Q2; chase the ag-weather-owner loop with PROME.
- **Effort:** small.

### T2-C · TRADE.md is Feb-14 vintage (pre-v2.1 framing)
- **What:** All figures Feb-vintage: Mexico remittances "−5%" (now +3.7%/count −1.7%), Central America "+18-25%", construction "−92.7% YoY growth", TX border DQ 7.92%. Whole file reflects the **acute-crisis framing the thesis has since walked back** (v2.1-v2.4 slow-structural-squeeze). IBOC-puts + ag-exposure ideas never actioned.
- **Why it matters:** Low direct behavioral impact (MARCO doesn't trade; feeds OTTO/LABOR/REGINALD) — but if read as current it misleads. The IBOC border-bank idea is arguably *more* relevant now (winter-$ hole → REGINALD), so don't just delete.
- **Action:** Reconcile to current thesis OR stamp clearly as "Feb-vintage watchlist, not current." Refresh the metrics table. Re-evaluate IBOC idea against the winter-2026-27 timing.
- **Effort:** medium.

---

## TIER 3 — dormant / cleanup

### T3-A · VX.tsv — 45/57 vectors are Jan-vintage (>60d, boot.py flags)
- **What:** 45 of 57 vectors last-updated Jan 20-22 (founding research): FL insurance index, net-migration, Sunbelt-Snowbelt differential, TX/FL housing, CA ag workforce, border vectors, etc.
- **Why it matters:** Some are genuinely stale and load-bearing (FL insurance, migration); some are deprecated/annual (can't refresh). Bulk staleness hides which.
- **Action:** Triage pass — per vector: refresh / mark `[STALE]` with date / archive-deprecated. Don't bulk-refresh; sort by whether the vector still drives a thesis claim.
- **Effort:** large (do in chunks).

### T3-B · RP-MARCO-MBS_BASELINE.md — never-executed + wrong VX refs
- **What:** Feb-9 baseline protocol for monitoring border-city **municipal-bond spreads** (EMMA). Status: "Awaiting initial spread data collection." Cross-refs use OLD VX numbering (VX-MARCO-01/03/06) that **doesn't match** current VX.tsv (1.01 / 2.02 / ELP-01 / etc.).
- **Why it matters:** **Latent opportunity:** ES-MARCO-04 (TX border fiscal stress) resolved today as a *counter-signal* on sales-tax revenue — but muni-bond spreads (EMMA) could be the cleaner, more forward-looking border-fiscal-stress instrument that sales-tax (a lagging, offset-able measure) isn't. This never-run protocol may be worth executing, not archiving.
- **Action:** Decide execute-vs-archive. If execute: pull EMMA spreads for the 5 target cities, fix VX cross-refs to current numbering, populate a real border-fiscal vector. If archive: move to `archive/` and note in FINDINGS.
- **Effort:** medium-large (if executed).

### T3-C · MARCO_SKELETON.md — historical artifact
- **What:** v1.0 thesis, explicitly superseded by `thesis/THESIS.md` (v2.4).
- **Action:** Archive to `archive/` (low priority; harmless where it is, but it's root clutter).
- **Effort:** trivial.

---

## Cross-references (already tracked elsewhere — not re-flagging)
- DEFERRED.md (4 open TOURISM cross-agent items: REGINALD ×2, HOUSING, CARL) — current as of 6/2, properly tracked. The CARL World-Cup item + REGINALD winter-$ items are now partly addressed via today's NEXUS_BRIEF SENDING + outbox; could cross-ref.
- ~~MCO/FLL April pax (PDF-blocked)~~ — **FLL RESOLVED 6/15** (pdfminer on Broward Monthly Statistical Summary PDF: +5.0% YoY / −4.7% 2-yr stack; intl −18.7% stack). MCO still blocked (flymco JS-rendered) → BTS T-100 ~Jul. Method: download+pdfminer w/ browser UA beats WebFetch for airport PDFs.
- Cross-agent re-sends — see T2-A (likely superseded by NEXUS_BRIEF).

---

*Maintained ad-hoc. Re-run the flagging sweep periodically (boot.py staleness + manual doc read). When an item is fixed, check it off with a date or delete the entry.*
