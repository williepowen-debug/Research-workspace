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

### ✅ T1-B · Channel-1 "2.2M" magnitude data-quality tension — RESOLVED 2026-07-02
- **What (was):** NOTES.md flagged DHS 2.5M departures (1.9M self-deported) vs independent counts ~290-340K (MPI/Brookings/TRAC) as a disputed load-bearing figure under the "2.2M CBO" spine.
- **Resolution:** PROME Tier-2 verification (Workflow, vs CBO/NFAP-BLS-CPS/KC-Fed; inbox 6/26) confirmed the tension and re-marked it: "2.2M CBO" was a mis-attributed **disputed-DHS** claim (CBO removals ≈290K+30K — matching this flag's ~290-340K independent counts); realized = **~1.0M foreign-born LF / ~1.5M pop** (FRED LNU01073395). Re-marked across canonical + live surfaces (thesis v2.6, STATUS, VX-SDL-01, KB, FINDINGS, NEXUS_BRIEF); reconcile notes to LABOR+CORAL. Direction/mechanism unchanged; corroborated by June-2026 LF −1M+ YoY. MARCO's own NOTES.md flag was correct.

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

### ✅ T1-E · FL Citizens "$678.8B" was stale AND directionally backwards — RESOLVED 2026-07-02
*(Found in the 7/2 staleness hunt.)* The "$678.8B, growing toward $750B (MAR-17), systemic-risk BREACHED" was a **2024/near-peak** figure and the trajectory REVERSED: Citizens depopulated 585,432 policies + removed $235.6B exposure in 2025, entered 2026 **67% below peak**, 395,144 policies (was 936K). **Re-marked:** MAR-17 INVALIDATED (wrong direction); VX-SFE-03 BREACHED→DE-ESCALATED; thesis Channel-3 insurance leg (exposure-thermometer decoupled from the affordability crisis, risk shifted to private market); STATUS FL-triple-exposure; KB-MARCO-SFE-02. Cross-flag CORAL (whole-FL insurance owner). **Residual:** exact current-exposure $ = Citizens Dec-2025 board report (to verify); `sub_agents/HOUSING` + `CLAUDE.md` threshold table still carry $678.8B (see T3-D / open items).

### ✅ Doc-mirror · docket/CALENDAR.md re-synced to CATALYSTS.tsv — DONE 2026-07-02
*(CALENDAR.md had drifted 17d behind the TSV after the 6/8 update — listed June events as forward. Full rewrite to the current forward window this session.)*

---

## TIER 2 — stale state / single-source-of-truth

### ✅ T2-A · STATUS.md internal stale blocks — DONE 2026-07-02
*(Resolved in the 7/2 staleness hunt: "NEXT SESSION FOCUS (5/31)" block pruned → pointer to SCRATCH; "CROSS-AGENT NEEDS RE-SEND" block retired → pointer to NEXUS_BRIEF SENDING + outbox. Both were confirmed superseded.)*

### ✅ T2-B · RESEARCH_STATUS.md drift — DONE 2026-06-15
*(Resolved: remittance paradox + FLL-April → COMPLETE; ag-weather refreshed as open PROME loop; TOURISM row = SHELVE-sub-agent/KEEP-vector decision (was mislabeled "stalled"); StatCan Q1→Q2 gap re-dated; FL-airport gap → MCO-only/BTS-July. Header date refreshed.)*
- **What:** (1) "Remittance paradox" still under ACTIVE — RESOLVED 6/2 (paradox fading), should move to COMPLETE. (2) TOURISM listed DORMANT/"stalled, no commits since Apr 22" — **contradicts the session-11 finding** that TOURISM is NOT stalled (content current, refreshed session 9; ran a live World Cup pull 6/2). (3) "StatCan Q1 2026 BOP" GAP — superseded by Q2 (~Aug 28) per docket. (4) "Ag-weather/crop-disaster owner" — flagged to PROME 5/31; assignment status unknown (open loop).
- **Action:** Move remittance paradox → COMPLETE; correct/remove the TOURISM-stalled entry; re-date StatCan gap to Q2; chase the ag-weather-owner loop with PROME.
- **Effort:** small.

### 🟡 T2-C · TRADE.md is Feb-14 vintage (pre-v2.1 framing) — STAMPED 2026-07-02 (full refresh still pending)
*(7/2: added a prominent "FEB-VINTAGE — NOT CURRENT" banner listing the stale figures + the IBOC re-eval note, so it no longer misleads if read. A full metrics refresh + IBOC-vs-winter-$ re-evaluation is still open.)*

- **What:** All figures Feb-vintage: Mexico remittances "−5%" (now +3.7%/count −1.7%), Central America "+18-25%", construction "−92.7% YoY growth", TX border DQ 7.92%. Whole file reflects the **acute-crisis framing the thesis has since walked back** (v2.1-v2.4 slow-structural-squeeze). IBOC-puts + ag-exposure ideas never actioned.
- **Why it matters:** Low direct behavioral impact (MARCO doesn't trade; feeds OTTO/LABOR/REGINALD) — but if read as current it misleads. The IBOC border-bank idea is arguably *more* relevant now (winter-$ hole → REGINALD), so don't just delete.
- **Action:** Reconcile to current thesis OR stamp clearly as "Feb-vintage watchlist, not current." Refresh the metrics table. Re-evaluate IBOC idea against the winter-2026-27 timing.
- **Effort:** medium.

---

## TIER 3 — dormant / cleanup

### ✅ Dormant sub-agents FROZEN-bannered — DONE 2026-07-02
*(7/2 hunt: BORDER/HOUSING/MIGRATION/WORKFORCE STATUS files (untouched since Apr-21, carrying stale DHS-shutdown / 9.1mo-condo / $678.8B / 2.2M figures) each got a FROZEN banner pointing to canonical STATUS. TOURISM left live (recent). Will-approved freeze-not-archive.)*

### T3-A · VX.tsv — 46/57 vectors are Jan-vintage (>60d, boot.py flags)
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
