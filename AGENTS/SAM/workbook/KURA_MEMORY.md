# KURA MEMORY

State file for the workbook-librarian sub-agent. Spec is in [`KURA.md`](KURA.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership split:**
- **KURA writes** at end-of-run: appends to `## LAST RUN`, adds/removes `## PENDING` items, updates `## STANDING MONITORS`, fills `## NEXT RUN HINTS`. Also fills `## CHANGES SINCE LAST RUN` at the START of each run.
- **SAM writes** `## CALIBRATION` after applying KURA's proposals (it's SAM's view of which patterns held; KURA can't know its own approve/reject rate during its own run).

**Spawn order:** KURA reads `KURA.md` first (spec), then `KURA_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what SAM tends to accept*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KURA at run start, based on what's moved in STATUS/TIMELINE/CHANGELOG/PREDICTIONS since the watermark in KURA.md. Cleared at end-of-run.*

**Watermark:** 2026-06-02 → window scanned = Jun 2 PM + Jun 3 (full day, AM + PM sessions).

- **Run 2 KB-SAM-183 landed:** SAM approved Run-2 proposal; KB.tsv now 126 rows. Routing call (KB vs auto-memory vs scripts/README) resolved in favor of Framework KB. Pattern logged in `## PROPOSED ADDS` Run-2 entry for SAM's CALIBRATION pass.
- **Jun 3 AM — CH-004 carry-unwind decomposition close** (commit `1d643418`): MEASUREMENT CORRECTION not view change. Carry-unwind probs decomposed 15/70/80 → 14/37/49 (7/30/60d). New METHOD in THESIS § CARRY-UNWIND PROBABILITY METHOD. CFTC-amplifier/residual conditionals defined. Outbox signals to LIQUID/HENRY/RED. CHANGELOG 2026-06-03 measurement-correction entry.
- **Jun 3 PM — three material moves** (commits `1122060a`, `96a37dd1`):
  - **USDJPY tagged 160.03 Wed 15:29 ET** — first print above hard trigger this cycle. Yen STRONGER on crosses (USD-driven). FXY $57.37. Brent $97.70 (+1.77%, 4th up day).
  - **Polymarket BOJ hike repriced 87.6% → 94.8%** (+7pp/24h). SAM-21 HELD 70%. Pre-registered mechanical trigger in STATUS: "if Polymarket ≥90% on Jun 9 re-check AND no Takaichi pushback → +5pp to 75%."
  - **MOF intervention authoritative ¥11.73T verified** (vs prior STATUS ~¥10T two-op back-out). STATUS INTERVENTION table + REFERENCE DATA now lead with authoritative monthly aggregate, footnote named-op estimates.
  - **Stop-spec harmonization** (Will-decided pure event-cap mode A): 5-file pass across STRATEGY / STATUS / TRADE / THESIS / CHANGELOG. Resolves real contradiction (STRATEGY two-part AND-rule vs STATUS/THESIS/TRADE flat "$55.05"). Operative rule: pre-Jun-16 = no mechanical price stop, event-capped by sizing; post-Jun-16 = exit if BOTH (BOJ dovish) AND (USDJPY 167+/no MOF).
  - **METSUKE Run 2** (commits `6945a39e`, `a5729593`): 8 flags / 8 applied / 100% apply rate. SAM had judged "not warranted on operational discipline" — Will overrode, lesson codified in METSUKE_MEMORY CALIBRATION.
- **Jun 3 data refresh:** FXY ATM IV proxy still broken (1.17% Wed AM, vs 1.56 Tue, vs 10.52 Mon) — KB-183 caveat continues to fire. CFTC -114,667 unchanged (next print Sat Jun 6).
- **No TIMELINE / PREDICTIONS / TRACKER / insurer-profile updates Jun 3.** Two CHANGELOG entries (CH-004 close + stop-spec harmonization). THESIS surgically updated (POSITION VIEW + 2 RISK FACTORS rows for stop-spec).

---

## LAST RUN

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
- **KB-SAM-185 placement call** (NEW Run-3) — thin-liquidity prediction-market discipline proposed as Framework KB row. Borderline; alt routing = auto-memory (rule may generalize beyond Japan-macro probability marks). SAM call. Same borderline as KB-183 resolved in favor of KB — flagging in case the rule reads more universal than tool-specific.
- ~~**KB-SAM-183 placement call**~~ — **RESOLVED Jun 3:** approved as Framework KB row (KB.tsv row 126). Routing precedent established for tool-specific methodology caveats.

---

## STANDING MONITORS (surface each run until resolved)

- **JICPA finalization** (KB-108, KB-125) — STATUS CHECK still pending; no FINAL standard reported post comment-close (Mar 17). Base case approval; tail risk neither confirmed nor cleared. *(No update Run-2.)*
- **Norinchukin Jun FY2025 print** — only remaining near-term Channel 1 reactivation gate. Will trigger FLOW-3.01 refresh + KB-160 PC exposure update if Kitabayashi commentary lands. CLO book reportedly ¥8.2T (was ¥9.7T in thesis) — verify. *(No update Run-2; print date not yet announced.)*
- **Mid-tier ESR window** — T&D, Sony Life, Daido, Taiyo prints (late-Jun); consistency check vs Big 3 v1.5 pattern. Explicit foreign-bond reduction language would partially reactivate Channel 1. *(No update Run-2.)*
- **May TB print Jun 18-19** — Phase 1 inversion diagnostic per THESIS v1.4 (queues against KB-176). *(No update Run-2.)*
- **FY2026 hedge ratio** — Mar-2026 full-year aggregate not yet released per KB-065/066. Surface when next industry hedge ratio prints. *(No update Run-2.)*
- **`fxy-proxy-v1` recalibration** (NEW Run-2) — **Third consecutive anomaly print Jun 3 AM (1.17% Jun-18 IV)** after Jun 2 (1.56%) and Jun 1 baseline (10.52%). Now firmly persistent, not transient. KB-183 covers the read-discipline; what's still owed is the `fxy_options.py` source diagnosis (SAM NEXT SESSION #6). Surface each run until either recalibration lands or anomaly resolves spontaneously.
- **MOF intervention quarterly per-op release** (NEW Run-3) — resolves the ~¥1.95T residual classification (70% slippage / 30% possible late-May smoothing op prior, per Jun 3 PM verification). Next quarterly release expected ~Aug. If late-May op confirmed: marginally hawkens reaction-function read. Park; no current action. If KB-184 lands, this monitor pairs with it for next-quarter close-out.
- **Polymarket Jun 9 re-check** (NEW Run-3) — SAM-21 mechanical trigger watch: if Polymarket BOJ-hike ≥90% on Jun 9 re-check AND no Takaichi/cabinet pushback → mechanical +5pp to 75% (per pre-registered trigger in STATUS § BOJ ASSESSMENT). If KB-185 lands, this is the first real-time application of the rule. Surface Jun 9 + each run until BOJ Jun 16 resolves.

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

- **Likely watermark window:** 2026-06-03 → next-run date. Expected harvest cadence:
  - **Jun 6 (Sat) CFTC weekly** — first scheduled CFTC-amplifier/residual re-check under new METHOD (per SAM NEXT SESSION #5). If short covers below ~-108K (60% cycle-peak line) → amplifier drops, 30d carry-unwind mark slips ~5-8pp. Worth a small harvest run if CFTC moves materially.
  - **Jun 9 (Mon) Polymarket re-check** — first real-time application of KB-185 mechanical trigger (if approved). If pricing ≥90% + no Takaichi pushback → SAM-21 +5pp to 75% with CHANGELOG entry — durable workbook fact (SAM-21 mark trajectory) but lives in PREDICTIONS not KB.
  - **Jun 13-15 pre-BOJ cabling window** — MOF/Bessent/Katayama verbal density up; possible POV pivot if cabling tone shifts. METSUKE Run 3 likely fires here.
  - **Jun 16 BOJ + Jun 17 FOMC + Jun 18-19 May TB / National CPI cluster** — heaviest expected harvest. KURA Run 4 post-cluster (Jun 20-21) likely material.
  - Smaller intervening moments: Jun 8 Q1 GDP 2nd estimate, Jun 10 US CPI + JGB 30Y auction (SAM-26 mechanism diagnostic).
- **Re-check `## PROPOSED ADDS` queue** against newly-landed rows — Run-3 queue has 2 candidates (KB-SAM-184 MOF measurement scope, KB-SAM-185 prediction-market discipline). KB-184 high-conviction A1; KB-185 borderline placement (Framework vs auto-memory). If SAM routes KB-185 elsewhere, delete and log in CALIBRATION.
- **Re-verify** the no-change items in KURA brief still hold (hands-off list, category list, watermark line, the 5-gate rubric).
- **`fxy-proxy-v1` watch** — proxy now broken 3 consecutive sessions. If `fxy_options.py` source fix lands (SAM NEXT SESSION #6), KB-183 may need refresh from `fxy-proxy-v1` to `fxy-proxy-v2` provenance. If proxy still broken Run 4, surface more loudly.
- **MOU walk-back scenario** — if Trump-Khamenei reset → Brent collapse → Phase 2 re-engages → new POV pivot in CHANGELOG worth harvesting. (Conversely, further MOU escalation → CHANGELOG POV pivot the other direction.)
- **THESIS NARRATIVE RECONCILIATION pass** (SAM NEXT SESSION #1) — when SAM lands this (probably v1.5.1 minor bump): the demoted-to-tail "Aug-2024-speed unwind" framing, promoted structural pillars (J-ICS, rate-diff, hedge-ratio, positioning), and decomposed HIGH conviction may surface 1-2 durable thesis-backbone KB candidates. Watch for this CHANGELOG entry as a high-yield harvest trigger.
- **Norinchukin Jun FY2025 print date** — still TBD; material Channel 1 re-test gate.
- **METSUKE Run 3 cadence:** per SAM's MEMORY NEXT SESSION #14, METSUKE Run 3 = pre-BOJ Jun 9-15 window OR next material POV pivot (or per Run 2 lesson: spawn after every material multi-file edit pass). KURA Run 4 likely follows METSUKE Run 3 if the pre-BOJ window produces a thesis-narrative-reconciliation pass.
