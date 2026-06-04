# KURA MEMORY

State file for the workbook-librarian sub-agent. Spec is in [`KURA.md`](KURA.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership split:**
- **KURA writes** at end-of-run: appends to `## LAST RUN`, adds/removes `## PENDING` items, updates `## STANDING MONITORS`, fills `## NEXT RUN HINTS`. Also fills `## CHANGES SINCE LAST RUN` at the START of each run.
- **SAM writes** `## CALIBRATION` after applying KURA's proposals (it's SAM's view of which patterns held; KURA can't know its own approve/reject rate during its own run).

**Spawn order:** KURA reads `KURA.md` first (spec), then `KURA_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what SAM tends to accept*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KURA at run start, based on what's moved in STATUS/TIMELINE/CHANGELOG/PREDICTIONS since the watermark in KURA.md. Cleared at end-of-run.*

**Watermark:** 2026-06-03 → window scanned = Jun 3 PM (post-Run-3) + Jun 4 AM + PM. As Will flagged in the spawn prompt, this is a small ~2-day watermark advance and an expected low-yield run.

- **Run 3 outcomes applied** (commit `eaf6c218` "KOYOMI+KURA Run 5/3 apply bundle"): KB-SAM-184 (MOF measurement scope, A1, Framework) PROMOTED to KB.tsv (now 127 rows; max KB-SAM-184). KB-SAM-185 (thin-liquidity prediction-market discipline) RE-ROUTED to auto-memory `[[finding_thin_liquidity_prediction_market_discipline]]` by Will — cross-agent transferable, not Japan-domain-only. KB-183 routing precedent NARROWED to "tool-specific AND SAM-domain-only" per Run-3 CALIBRATION. FLOW-5.02 + 6.02 spot-stale fixes applied.
- **Jun 3 evening — v1.5.1 narrative reconciliation** (commit `39639b06`): minor version bump v1.5 → v1.5.1. New STRUCTURAL PILLARS section in THESIS promotes rate-differential, J-ICS lifer abandonment, hedge ratio 14-yr low, CFTC positioning to explicit thesis backbone. Channel 2 prose reconciled with CH-004 METHOD (Aug-2024-speed demoted expectation → upside-tail conditional on hawkish-of-pricing + at-peak positioning). Intervention paradox replaced with "structural pillars + asymmetric option on Jun 16" honest framing. Conviction split: direction/level HIGH vs near-term timing MEDIUM. No probability re-rates; position unchanged.
- **Jun 3 evening — v1.5.1 propagation completion** (commit `693f4e65`): 3-line fix (HENRY cross-agent link Aug-2024-speed demotion + STATUS Channel 2 ref + header v1.5 → v1.5.1).
- **Jun 3 evening — Open Flags rail Phase A + B** (commit `72220937`): eval re-baseline scoped & scheduled Jun 7-8 with operator packet at `evals/REBASELINE_v1.5.1_RUN_PROMPT.md`. SAM-23 mechanical mark-DOWN/UP trigger discipline pre-registered (conjunction-based, mirrors SAM-21 Jun-9 pattern).
- **Jun 4 AM — Jun 3-4 cabling-window news ingest + OS.1 closure + Sato corrections** (commit `079e46ca`): Bloomberg sources-leak ("BOJ Is Said to Mull June Rate Hike With Another Possible in 2026") + Ueda Kisaragi-kai (Jun 3 hawkish-of-pricing) + Polymarket built 94.8% → 96.9% (3rd sequential build) + Takaichi verbal Jun 3 at 160 reads as intervention-permission NOT pushback. SAM-21 HELD 70% per pre-registered Jun-9 discipline. OS.1 (fiscal-dominance counter-frame) CLOSED largely-falsified for SAM-21 binary; live for post-June PATH/CEILING story. Sato BOJ entry date corrected Jun 16 → Jun 30 + framing UPGRADED (Nakagawa was active 1.00% Apr-28 dissenter, so bloc drops 3 → 2 unless Sato surprises) — UNVERIFIED, KOYOMI quarantine in flight this same run.
- **Tape since Run 3:** USDJPY 160.03 (Jun 3 PM tag) → 159.92 (Jun 4 Asia). Brent $97.70 (Jun 3 close) → $96.97 (Jun 4, 2nd down session). JGB 30Y +3bp to 3.85% (Jun 4) curve steepening on hike anticipation. CFTC -114,667 still on May-26 reference (next print Sat Jun 6).
- **No TIMELINE / PREDICTIONS / TRACKER / insurer-profile structural updates Jun 4.** One new CHANGELOG entry (v1.5.1 follow-on, three-part: news ingest + OS.1 + Sato). STATUS substantially refreshed (banner + STATE OF PLAY + market data + BOJ ASSESSMENT table).

---

## LAST RUN

### Run 4 — 2026-06-04 (Thu PM, propose-only, teams-mode named spawn)

**Inputs scanned:** Watermark 2026-06-03. Post-watermark window = Jun 3 evening (post Run-3 apply bundle) + Jun 4 AM-PM. Read: STATUS (Jun 4 ~AM ET refresh), MEMORY (Jun 4 NEXT SESSION + RESOLVED), CHANGELOG (1 new entry: 2026-06-04 v1.5.1 follow-on with three sub-actions a/b/c), THESIS v1.5.1 (verified header + STRUCTURAL PILLARS new section + Channel 2 reconciliation), TIMELINE (no new entries), PREDICTIONS (no new resolutions; 7 CONFIRMED / 8 FAILED / 1 RESOLVED-special / 4 OPEN unchanged), TRACKER (no change), insurers/ (no change), KB.tsv (127 rows; max KB-SAM-184 post Run-3 promote), KB_ARCHIVE.tsv (58 rows), FLOW.tsv (lines 10-11 dated 2026-06-03 — refreshed by SAM after Run 3 apply bundle), VX.tsv (all 2026-05-28). Re-checked Run-3 `## PROPOSED ADDS` queue: KB-SAM-184 landed (KB.tsv row 127), KB-SAM-185 re-routed to auto-memory (Will), queue clear before adding Run 4.

**Outputs:**
- **1 proposed add (PENDING_KOYOMI):**
  - **KB-SAM-185 (BOJ-Wages)** — Sato Ayano replaces Nakagawa Jun 30: Apr-28 hike-dissent bloc 3 → 2. Material durable board-composition fact with explicit thesis-side consequence chain. **Hold-promote until KOYOMI primary-source verification of the "Nakagawa actively voted for 1.00% Apr 28" characterization** (per Will's spawn brief). Conservative A2; A1 upgrade reserved for KOYOMI primary-source confirmation. ID re-uses KB-SAM-185 (prior KB-185 went to auto-memory; per spec "never reuse an archived ID" — but Run-3 KB-185 was never archived, it was *not promoted at all*, so the ID was never written to KB.tsv. ID slot is clean; KURA proposes re-using it for this Run-4 row. Flag for SAM to confirm the ID convention is fine when archived/never-promoted is distinct.)
- **0 archive-moves** (no SUPERSEDED rows in KB.tsv).
- **2 FLOW spot-stale flags:** FLOW-JPN-5.02 (USDJPY + Brent + Polymarket all stale at Jun 3 levels) + FLOW-JPN-6.02 (USDJPY + Brent stale). SAM refreshed these Jun 3 PM; Jun 4 tape has moved enough to re-flag.
- **0 VX staleness flags** (next VX trigger = Jun 18-19 May TB or Jun 19 National CPI).
- **0 cross-ref fixes, palimpsest collapses, dedup candidates, re-grades.**
- **3 add-candidates declined / re-routed** (see FLAGGED add-candidates uncertain in summary).

**Watermark proposed:** 2026-06-03 → 2026-06-04.

**Net workbook math (if SAM approves KB-185 conditional on KOYOMI clearing):** KB.tsv 127 → 128 rows; KB_ARCHIVE.tsv unchanged at 58. If KOYOMI quarantines: KB.tsv unchanged at 127, KURA pushes the row to PENDING for next run.

**Notable non-promotes (the three Will-flagged candidates that did NOT clear):**
- **Discipline-credibility pattern** — "pre-registration value comes from holding through 'but this time is different' pressure." Durable lesson, but cross-agent transferable (any agent using pre-registered triggers + earned-discount calibration would apply this). Per Run-3 CALIBRATION refinement (cross-agent transferable → auto-memory, not KB), this routes to auto-memory. Surfaced under FLAGGED add-candidates uncertain for SAM/Will routing call. Candidate auto-memory name: `[[finding_pre_registration_discipline_through_corroboration]]` or similar.
- **Aug-2024-speed-conditional framing** — the 3-pass demotion (expectation → upside-tail conditional on hawkish-of-pricing + at-peak positioning) is now CANON in THESIS v1.5.1 § Channel 2 + CARRY-UNWIND METHOD anchor #1 + the Aug-2024-speed reconciliation paragraph. A KB row would duplicate THESIS. Same logic as the Run-3 CH-004 METHOD decline (lives in THESIS, not KB). Routed correctly to THESIS; no KB action.
- **OS.1 closure 3-question test rubric** — the rubric Will applied (a) market repriced THROUGH? (b) inside the discount or un-priced? (c) path/ceiling vs binary? — is a reusable counter-frame disposition rubric. Borderline: tool-class methodology (would clear KB-183 precedent) BUT cross-agent transferable (any agent disposing of counter-thesis hypotheses would apply this — see CARL/REGINALD red-team patterns). Per Run-3 narrowed routing, lean auto-memory. Surfaced under FLAGGED add-candidates uncertain. Candidate auto-memory name: `[[finding_counter_frame_3_question_disposition]]` or similar.

**Calibration self-note (for SAM's later CALIBRATION pass):**
- Run 4 watermark advance ~2 days as Will flagged; precision-over-recall held — 1 candidate proposed (vs 3 add-candidates routed elsewhere). Did NOT pad with the cross-agent-transferable items (discipline-credibility, OS.1 rubric) — internalizing the Run-3 narrowed routing rule.
- The Run-4 candidate (Sato BOJ entry) is the **first KB candidate that explicitly requires another sub-agent's verification before promote**. This is a new pattern — KB-row dependencies on KOYOMI primary-source quarantine outcomes. Worth surfacing for SAM CALIBRATION: KURA-KOYOMI handoff via PENDING_KOYOMI status.
- Workbook signal density tracking session signal density: 2-day window, single solid KB candidate (Sato). Pattern holds.
- ID-slot question (KB-185 re-use after Run-3 re-route) is small but worth a one-time SAM ruling — does an ID that was *proposed-but-never-promoted-due-to-rerouting* get re-used, or does it stay retired? KURA's default: re-use, since nothing was ever written to KB.tsv at that ID; flag for SAM confirm.

---

### Run 3 — 2026-06-03 (Wed ~PM closeout, propose-only)

**Inputs scanned:** Watermark 2026-06-02. Post-watermark window = Jun 2 PM (post-Run-2) + Jun 3 full day (AM CH-004 close + PM 160-break/Polymarket/MOF-verify/stop-harmonization + METSUKE Run 2). Read: STATUS (Jun 3 ~15:29 ET), MEMORY (Jun 3 PM closeout), CHANGELOG (2 new entries: CH-004 close + stop-spec harmonization, both 2026-06-03), THESIS (surgical POSITION VIEW + RISK FACTORS edits), TIMELINE (no new entries), PREDICTIONS (no new resolutions), TRACKER (no change), KB.tsv (126 rows post Run-2 promote; max KB-SAM-183), KB_ARCHIVE.tsv (58 rows), FLOW.tsv (all 2026-05-28), VX.tsv (all 2026-05-28), insurers/ (no change). Re-checked Run-2 `## PROPOSED ADDS` queue: KB-SAM-183 landed, queue clear before adding Run 3.

**Outputs:**
- **2 proposed adds:**
  - **KB-SAM-184 (Framework)** — MOF intervention measurement scope: lead with monthly aggregate; footnote named-op estimates. Gold-standard methodology row anchored to Jun 3 PM verification work. Conservative A1 (primary-source documented, cross-method delta quantified).
  - **KB-SAM-185 (Framework)** — Thin-liquidity prediction-market single-print discipline. Borderline placement (Framework vs auto-memory) — applying KB-183 routing precedent. B2 grade (methodology synthesized, not yet published rule). Flag for SAM to re-decide if rule reads more universal than Japan-macro.
- **0 archive-moves** (no SUPERSEDED rows in KB.tsv).
- **2 FLOW spot-stale flags** (FLOW-5.02, FLOW-6.02) — see FLAGGED.
- **0 VX staleness flags** (all rows dated 2026-05-28; no Jun 2-3 prints affect VX bands; next VX trigger = Jun 18-19 May TB or Jun 19 National CPI).
- **0 cross-ref fixes, palimpsest collapses, dedup candidates, re-grades.**

**Watermark proposed:** 2026-06-02 → 2026-06-03.

**Net workbook math (if SAM approves both adds):** KB.tsv 126 → 128 rows; KB_ARCHIVE.tsv unchanged at 58.

**Notable non-promotes (carve-out / Gate-failed):**
- **Stop-spec event-cap mode A rationale** (SAM-prefill #3) — SAM correctly leaned DECLINE. KB-058 already documents "USDJPY 167 with no MOF AND BOJ dovish" stop conjunction. The pre-event-cap-vs-flat-stop principle IS reusable, but it's a SAM-operational discipline lesson better-routed to auto-memory if anywhere (e.g. "size to event-cap not price-stop for sub-CL definite-event positions"). Already in CHANGELOG 2026-06-03. Surfaced under add-candidates uncertain.
- **Jun 3 FLOW row (160 break + Polymarket + MOF aggregate confluence)** (SAM-prefill #4) — DECLINE. FLOW universe is structural transmission pathways, not confluence moments. Existing FLOW-5.02 captures carry unwind; Jun 3 levels are STATUS data + (future) TIMELINE narrative.
- **METSUKE Run 2 architectural finding** ("two-pass-day single-sweep coverage" CALIBRATION update) — METSUKE-internal CALIBRATION lesson, lives in METSUKE_MEMORY. Not workbook material. Same pattern as Run 2's non-promote.
- **Jun 3 CH-004 carry-unwind decomposition METHOD** — this IS thesis-level methodology, but it lives in `THESIS.md § CARRY-UNWIND PROBABILITY METHOD` as the authoritative spec. A KB row would duplicate THESIS. The cross-session calibration lesson (catalyst-prob ≠ consequence-prob) was already promoted to auto-memory `[[finding_catalyst_vs_consequence_conflation.md]]` — correctly routed.

**Calibration self-note (for SAM's later CALIBRATION pass):**
- Run 3 surfaced 2 candidates (1 from SAM's prefill #1, 1 from SAM's prefill #2). Declined SAM's prefill #3 and #4. Precision-over-recall held — did NOT pad to balance the ratio per spec calibration reminder.
- Both Run 3 candidates are SAM-prefilled — KURA's independent harvest pass surfaced no additional Framework-tier candidates that SAM missed. Workbook signal density continues to track session signal density (high-info session → 2 adds vs Run 2's low-info session → 1 add).
- Borderline routing pattern emerging: tool-specific OR thin-domain methodology rules → Framework KB (KB-183 vol-proxy, KB-185 prediction-market); cross-agent transferable lessons → auto-memory (catalyst-prob conflation Jun 3). Surface for SAM CALIBRATION pass to confirm the routing heuristic.

---

### Run 2 — 2026-06-02 (Tue ~09:15 ET, propose-only)

**Inputs scanned:** Watermark 2026-06-01. Post-watermark window = Jun 1 evening + Jun 2 boot. Read: STATUS, MEMORY (incl. Jun-1-evening + post-power-loss addenda), TIMELINE (newest entries Jun 1), CHANGELOG (newest = Jun 1 v1.5 intra-version POV pivot), PREDICTIONS (no new resolutions), KB.tsv (125 rows; max KB-SAM-182), KB_ARCHIVE.tsv (58 rows), FLOW.tsv, VX.tsv, JGB_AUCTIONS.tsv (newest = Jun 2), FXY_OPTIONS.tsv (newest = Jun 2; anomaly).

**Outputs:**
- **1 proposed add (KB-SAM-183, Framework):** `fxy-proxy-v1` failure mode — ATM_IV can collapse to near-zero (Jun 2 reads). Promote the existing STATUS "proxy scale ≠ OTC RR — read sign/trend, not absolute" caveat to durable KB. Borderline category placement (Framework vs `scripts/README.md` vs auto-memory) — flagged for SAM call.
- **0 archive-moves** (no SUPERSEDED rows present in KB.tsv after Run-1 sweep).
- **0 FLOW spot-stale flags** (USDJPY 159.64 still consistent across STATUS / FLOW-5.02 / FLOW-6.02 as of Jun 1 close; Jun 2 STATUS refresh not yet done).
- **0 VX staleness flags** (all rows dated 2026-05-28; no May 29-Jun 2 data drops affect VX bands).
- **0 cross-ref fixes, palimpsest collapses, dedup candidates, re-grades** — workbook clean post Run-1.

**Watermark proposed:** 2026-06-01 → 2026-06-02.

**Net workbook math (if SAM approves the 1 add):** KB.tsv 125 → 126 rows; KB_ARCHIVE.tsv unchanged at 58.

**Notable non-promotes (carve-out / Gate-failed):**
- **METSUKE introduction + Run 1 architecture** — durable but it's sub-agent-spec / process, not a fact about the world. The `METSUKE.md` + `METSUKE_MEMORY.md` files ARE the durable record; KB row would duplicate. Sub-agent CLAUDE+MEMORY split was already promoted to auto-memory (`[[finding_subagent_memory_split]]`) Jun 1. Correctly routed to spec files + auto-memory.
- **3-of-3 vol convergence** (substantive thesis-side finding from METSUKE Run 1) — snapshot read of auto-pulled FXY_OPTIONS.tsv feed; Gate 4 tsv-territory fail. Lives correctly in STRATEGY.md "Current read" + STATUS data table.
- **METSUKE position-card DUP-LIVE-SPOT carve-out** — METSUKE-internal calibration; lives in METSUKE_MEMORY.md CALIBRATION. Not workbook material.
- **Jun 2 10Y JGB auction softening** — BTC 3.530x is *softer* (10% drop in cover ratio) but auction status remains Orderly and far from stress threshold. No structural significance. Lives correctly in JGB_AUCTIONS.tsv.

**Calibration self-note (for SAM's later CALIBRATION pass):** This was the expected-LOW-yield run SAM flagged in the spawn prompt. Surfaced 1 candidate (vol-proxy data-quality caveat) that wasn't on SAM's prefill list. Precision-over-recall held — did not pad with the METSUKE architectural-fact temptation.

---

### Run 1 — 2026-06-01 (inaugural, propose-only, Opus 4.8)

**Inputs harvested:** post-watermark = no watermark (inaugural full sweep). Read: STATUS, THESIS v1.5, CHANGELOG, TIMELINE active, PREDICTIONS, TRACKER, research/outputs/, KB.tsv (119 rows), KB_ARCHIVE.tsv, FLOW.tsv, VX.tsv.

**Outputs (all 7 KB adds approved by SAM):**
- KB-SAM-176 (Framework) — Phase 1 inversion under blockade: supply-destruction mechanism
- KB-SAM-177 (Insurer) — J-ICS long-end abandonment: absence is cause, not consequence (v1.4 inversion)
- KB-SAM-178 (Regulatory) — MOF cut super-long JGB issuance to ¥17T (17-yr low)
- KB-SAM-179 (Insurer) — Repack instruments — FX-noise reduction ≠ repatriation
- KB-SAM-180 (Insurer) — Industry foreign-bond allocation 22%→17% (Mar 2021 → Mar 2023)
- KB-SAM-181 (Insurer) — Q4 FY2024 ¥1.35T JGB trim (3rd-largest quarterly on record)
- KB-SAM-182 (Cross-Agent) — Bessent-Katayama Channel 3 affirmation (borderline; SAM kept)

**Archive-moves (2):**
- KB-137 (pre-existing SUPERSEDED — KURA caught it had not been relocated)
- KB-064 (SUPERSEDED via dedup-merge into KB-063; RP-SAM-4 §1 corroborates DEEP_DIVE Exec Summary)

**Palimpsest collapses (2):** KB-065 + KB-066 (hedge ratio rows; resolved to 44.4% authoritative; conflict history pruned to clean provenance).

**FLOW spot-stale fixes (2):** FLOW-JPN-5.02 (USDJPY/CFTC/probs) + FLOW-JPN-6.02 (USDJPY + MOU-break context).

**Watermark advanced:** (none) → 2026-06-01.

**Net workbook math:** KB.tsv 119 → 124 rows; KB_ARCHIVE.tsv 56 → 58 rows. Category integrity preserved.

---

## PENDING (escalations SAM hasn't yet resolved)

- **Hedge-ratio <30% claim** from Jun 1 news sweep conflicts with KB-065/066 authoritative 44.4%. Source: ainvest.com via Jun 1 sub-agent sweep. Needs primary-source verification before any KB update. Likely source confusion or stale-ratio mix. *(Carried Run-1 → Run-3; SAM NEXT SESSION #10.)*
- **KB-076 / KB-077 / KB-083 / KB-090 / KB-094 palimpsest collapses** — KURA flagged ripe for collapse but SAM elected to defer until next refresh window. *(Carried Run-1 → Run-3; no change.)*
- **UST denominator gap** (KB-061/062/139/140) — $450B vs $600-810B not closed by FY2025; status-downgrade to ESTIMATE-RANGE pending or pointer-row consolidation. *(Carried Run-1 → Run-3; no change.)*
- **KB-SAM-185 (Run 4) — Sato BOJ entry, PENDING_KOYOMI** (NEW Run-4) — Sato Ayano replaces Nakagawa Jun 30; Apr-28 hike-dissent bloc drops 3 → 2. Material durable board-composition row. Hold-promote until KOYOMI primary-source verification of "Nakagawa actively voted for 1.00% Apr 28" characterization clears quarantine. Three branches in spec (CONFIRMED → promote; REFRAMED → soften; QUARANTINED → decline). KOYOMI running parallel to Run 4.
- **ID-slot convention question** (NEW Run-4, tiny but worth a one-time ruling) — Run-3 KB-185 (thin-liquidity prediction-market discipline) was re-routed to auto-memory and never written to KB.tsv. KURA's default: re-use the KB-185 slot for the Run-4 Sato row. Alt: skip to KB-186 to preserve a one-to-one mapping of ID to historical attempt. Flag for SAM confirm.
- ~~**KB-SAM-185 placement call**~~ — **RESOLVED Jun 3:** RE-ROUTED to auto-memory `[[finding_thin_liquidity_prediction_market_discipline]]` by Will. KB-183 routing precedent narrowed (tool-specific AND SAM-domain-only → KB; cross-agent transferable → auto-memory).
- ~~**KB-SAM-183 placement call**~~ — **RESOLVED Jun 3:** approved as Framework KB row (KB.tsv row 126). Routing precedent established for tool-specific methodology caveats.

---

## STANDING MONITORS (surface each run until resolved)

- **JICPA finalization** (KB-108, KB-125) — STATUS CHECK still pending; no FINAL standard reported post comment-close (Mar 17). Base case approval; tail risk neither confirmed nor cleared. *(No update Run-2.)*
- **Norinchukin Jun FY2025 print** — only remaining near-term Channel 1 reactivation gate. Will trigger FLOW-3.01 refresh + KB-160 PC exposure update if Kitabayashi commentary lands. CLO book reportedly ¥8.2T (was ¥9.7T in thesis) — verify. *(No update Run-2; print date not yet announced.)*
- **Mid-tier ESR window** — T&D, Sony Life, Daido, Taiyo prints (late-Jun); consistency check vs Big 3 v1.5 pattern. Explicit foreign-bond reduction language would partially reactivate Channel 1. *(No update Run-2.)*
- **May TB print Jun 18-19** — Phase 1 inversion diagnostic per THESIS v1.4 (queues against KB-176). *(No update Run-2.)*
- **FY2026 hedge ratio** — Mar-2026 full-year aggregate not yet released per KB-065/066. Surface when next industry hedge ratio prints. *(No update Run-2.)*
- **`fxy-proxy-v1` recalibration** (NEW Run-2) — **Third consecutive anomaly print Jun 3 AM (1.17% Jun-18 IV)** after Jun 2 (1.56%) and Jun 1 baseline (10.52%). Now firmly persistent, not transient. KB-183 covers the read-discipline; what's still owed is the `fxy_options.py` source diagnosis (SAM NEXT SESSION #6). Surface each run until either recalibration lands or anomaly resolves spontaneously. *(No Jun 4 update — boot.py output not refreshed Jun 4 AM per STATUS data table footnote; carry forward.)*
- **MOF intervention quarterly per-op release** (NEW Run-3) — resolves the ~¥1.95T residual classification (70% slippage / 30% possible late-May smoothing op prior, per Jun 3 PM verification). Next quarterly release expected ~Aug. If late-May op confirmed: marginally hawkens reaction-function read. Park; no current action. Now paired with the landed KB-184 (MOF measurement scope) for next-quarter close-out.
- **Polymarket Jun 9 re-check** (NEW Run-3) — SAM-21 mechanical trigger watch: if Polymarket BOJ-hike ≥90% on Jun 9 re-check AND no Takaichi/cabinet pushback → mechanical +5pp to 75% (per pre-registered trigger in STATUS § BOJ ASSESSMENT). **Jun 4 status:** Polymarket leg now ≥90% across 3 sequential reads (87.6 → 94.8 → 96.9); Takaichi leg AFFIRMATIVELY CLOSED Jun 3 (verbal at 160 reads as intervention-permission, not ceiling-pushback). Multi-source corroboration (Bloomberg sources-leak + Ueda explicit speech) further strengthens beyond Polymarket-only condition. SAM HELD 70% per discipline. Surface Jun 9 + each run until BOJ Jun 16 resolves.
- **Sato Jun 30 BOJ board entry** (NEW Run-4) — KB-185 candidate hinges on KOYOMI primary-source verification of "Nakagawa actively voted for 1.00% Apr 28" characterization. If KOYOMI clears → SAM promotes the KB row + tracks Sato's first MPM (Jul 30-31) for dissent-vote validation of the 3 → 2 framing. If Sato dissents WITH Takata/Tamura on the dovish side at Jul 30-31, the row's consequence chain is confirmed; if Sato unexpectedly votes hawkish, the row's "unless Sato surprises" caveat fires. Surface until Jul 30-31 MPM resolves.
- **CFTC Sat Jun 6 print** (NEW Run-4 — surfacing from NEXT RUN HINTS to monitor) — first scheduled CFTC-amplifier/residual re-check under CH-004 METHOD. -108K = 60% cycle-peak line. If shorts cover below -108K → +5pp amplifier drops + residual turns OFF → 30d carry-unwind 37% → ~29-32%. If shorts build further (>-153K = 85% line) → amplifier may bump to +8pp. Auto-CHANGELOG entry expected on the Sat print; KURA Run 5 may have a method-execution KB candidate if amplifier flips.

---

## CALIBRATION (precision-vs-recall tuning patterns)

*Owned by SAM. Updated after applying each run's proposals.*

### Run 3 (2026-06-03)
- **KB adds applied: 1 of 2 proposed** — KB-184 MOF measurement scope (A1, gold-standard primary-source documented) PROMOTED. KB-185 prediction-market discipline RE-ROUTED to auto-memory `[[finding_thin_liquidity_prediction_market_discipline]]` by Will. KURA approved as Framework KB applying KB-183 precedent; Will overrode the routing call.
- **Routing precedent NARROWED (Will, Jun 3):** the KB-183 tool-class-methodology heuristic was too broad. Refined rule: **Framework KB = tool-specific AND SAM-domain-only (Japan-macro mechanics)**; **auto-memory = cross-agent transferable disciplines that any agent could apply**. KB-183 (fxy-proxy specific to FXY analysis) stays in KB; KB-185 (prediction-market discipline, applicable to LIQUID/HENRY/BROCK Polymarket reads too) → auto-memory. **For future borderline calls: apply the cross-agent-transferability test, not just the tool-specificity test.**
- **Spot-stale flag approve rate: 2/2 FLOW rows applied (FLOW-JPN-5.02 + 6.02).** KURA correctly identified these as SAM-call-per-autonomy (spot + probs + dates entangled in narrative). Applied surgical edits with date stamps.
- **Decline pattern held:** KURA correctly declined SAM's prefill #3 (stop-spec event-cap rationale) as auto-memory-territory not KB; correctly declined SAM's prefill #4 (Jun 3 confluence FLOW row) as outside FLOW universe (structural pathways, not confluence moments). Both declines internalize KB-183 precedent + FLOW universe scope. **METSUKE-style discipline emerging in KURA — declining SAM-prefilled candidates when the routing doesn't fit, rather than padding.**
- **Borderline routing pattern (cross-run): tool-specific methodology → Framework KB (KB-183, KB-185); cross-agent transferable lessons → auto-memory ([[finding_catalyst_vs_consequence_conflation]]).** Pattern now established 2x — codify this as the routing heuristic for future borderline calls.
- **High-info session pattern:** Run 3 = 2 adds (high-info session); Run 2 = 1 add (low-info session); Run 1 = 7 adds (inaugural). Workbook signal density tracking session signal density confirms KURA's precision-over-recall discipline is calibrated correctly — no padding observed.
- **Tuning note for Run 4 (post-BOJ Jun 16 expected):** anticipate higher-yield run (5-10 candidates) on the back of (a) BOJ outcome, (b) thesis narrative reconciliation pass per SAM's NEXT SESSION #1, (c) post-event TIMELINE entries. KURA's bar shouldn't move — high-yield is fine, but precision still wins.

### Run 2 (2026-06-02)
- **Approve rate: 1/1 KB add (100%)** — KB-183 fxy-proxy-v1 Framework. Resolved the Framework vs auto-memory borderline in favor of KB (tool-specific methodology, not agent-cross-cutting). Sets precedent applied at Run 3 KB-185.
- **Low-yield window correctly identified:** post-Run-1 watermark window had little durable material; KURA precision held (1 add vs Run 1's 7).

### Run 1 (2026-06-01)
- **Approve rate: 7/7 KB adds (100%).** No rejects. Precision-over-recall framing held.
- **KURA's self-bar:** 5 add-candidates excluded as calibration-not-durable (MOU break, Fed-cut path, etc.) — correctly routed to PREDICTIONS/auto-memory per the carve-out. Carve-out is working.
- **Borderline call (KB-182 Bessent-Katayama):** SAM kept. Pattern emerging — single-event-rhetoric is OK when the event has been *promoted* to a thesis-level pillar (here, v1.4 Channel 3). Without that anchor, a single rhetoric event would still be a reject.
- **Dedup acceptance:** Both KURA-proposed dedups (KB-063+064 merge; KB-065/066 collapse) approved. Pattern: SAM accepts dedup/collapse when both rows hold identical resolved facts.
- **Tuning note:** Bias toward precision worked — 7 strong proposals beat 15 marginal ones. Continue this calibration; do NOT loosen the bar.

---

## NEXT RUN HINTS

- **Likely watermark window:** 2026-06-04 → next-run date. Expected harvest cadence:
  - **Sat Jun 6 CFTC weekly** — first scheduled CH-004 METHOD amplifier/residual re-check (-108K = 60% cycle-peak line, -153K = 85% line). Worth a small harvest run if CFTC moves materially across either gate line; possible KB candidate if the METHOD's first real-world application produces a durable execution-pattern note (e.g., "first cover-flip drop on day-of CFTC print — STATUS auto-CHANGELOG entry expected" type rule).
  - **Mon Jun 9 Polymarket re-check** — SAM-21 mechanical trigger eligibility: if Polymarket ≥90% (already at 96.9% Jun 4) AND no Takaichi/cabinet pushback (already affirmatively closed Jun 3) → +5pp to 75% with CHANGELOG entry. Both conditions track met; the trigger discipline question is whether SAM fires at the Jun 9 mark or chooses to hold one more day to BOJ. Either path produces a CHANGELOG entry worth scanning. SAM-21 mark trajectory itself lives in PREDICTIONS not KB (calibration, not fact).
  - **Jun 13-15 pre-BOJ blackout window** — MOF/Bessent/Katayama verbal density continuing; possible POV pivot if cabling tone shifts (e.g., dovish Ueda last-minute or Bessent rate-gap pushback). METSUKE Run 3 likely fires here.
  - **Tue Jun 16 BOJ MPM + Wed Jun 17 FOMC + Thu Jun 18-19 May TB / National CPI cluster** — heaviest expected harvest. KURA Run 5 or 6 post-cluster (Jun 20-22) likely material; could be 5-10 candidates depending on BOJ outcome.
  - **Mon Jun 30 Sato seats BOJ board** — KB-185 (if KOYOMI clears) directly anchors here; the consequence chain validates / falsifies at Sato's first MPM Jul 30-31.
  - Smaller intervening moments: Jun 8 Q1 GDP 2nd estimate, Jun 10 US CPI + JGB 30Y auction (SAM-26 mechanism diagnostic).
- **Re-check `## PROPOSED ADDS` queue** against newly-landed rows — Run-4 queue has 1 candidate (KB-SAM-185 Sato BOJ entry, PENDING_KOYOMI). If KOYOMI clears between Run 4 and Run 5, the row promotes mechanically and queue empties before Run 5 adds. If KOYOMI quarantines, decide route then (defer to next KOYOMI run vs decline and convert to FLAGGED carry-item).
- **Re-verify** the no-change items in KURA brief still hold (hands-off list, category list, watermark line, the 5-gate rubric).
- **`fxy-proxy-v1` watch** — KB-183 caveat fires; awaiting `fxy_options.py` source diagnosis (SAM NEXT SESSION #6, deferred). If proxy still broken Run 5, surface more loudly. If fix lands, KB-183 may need refresh from `fxy-proxy-v1` to `fxy-proxy-v2` provenance.
- **MOU walk-back scenario** — Israel-Lebanon ceasefire (Jun 4) removed ONE of Tehran's two stated grievances; if Tehran fully resumes message exchange OR Trump-Khamenei reset → Brent collapse → Phase 2 re-engages → SAM-23 mechanical mark-DOWN trigger fires (conjunction-based, pre-registered STATUS § INTERVENTION STATUS). New POV pivot in CHANGELOG worth harvesting either direction.
- **Norinchukin Jun FY2025 print date** — still TBD; material Channel 1 re-test gate.
- **Cross-agent transferable lesson candidates parked under FLAGGED** (Run 4) — if SAM/Will rule on either as auto-memory, KURA can drop them from carry-state:
  - `[[finding_pre_registration_discipline_through_corroboration]]` — pre-registered trigger value comes from holding through multi-source-corroboration pressure (SAM-21 Jun 3-4 worked example).
  - `[[finding_counter_frame_3_question_disposition]]` — 3-question rubric for closing counter-thesis hypotheses (market repriced THROUGH? inside the discount or un-priced? path/ceiling vs binary?). Worked example: OS.1 fiscal-dominance closure Jun 4.
- **METSUKE Run 3 cadence:** per SAM's MEMORY NEXT SESSION #14, METSUKE Run 3 = pre-BOJ Jun 9-15 window OR next material POV pivot (or per Run 2 lesson: spawn after every material multi-file edit pass). The Jun 3-4 cabling-window ingest + OS.1 closure + Sato corrections IS a material multi-file edit pass (4 files touched) — by Run-2 lesson, METSUKE Run 3 could fire now rather than waiting for Jun 9-15. Surface as a candidate timing.
