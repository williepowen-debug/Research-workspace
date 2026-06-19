# KURA MEMORY

State file for the workbook-librarian sub-agent. Spec is in [`KURA.md`](KURA.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership split:**
- **KURA writes** at end-of-run: appends to `## LAST RUN`, adds/removes `## PENDING` items, updates `## STANDING MONITORS`, fills `## NEXT RUN HINTS`. Also fills `## CHANGES SINCE LAST RUN` at the START of each run.
- **SAM writes** `## CALIBRATION` after applying KURA's proposals (it's SAM's view of which patterns held; KURA can't know its own approve/reject rate during its own run).

**Spawn order:** KURA reads `KURA.md` first (spec), then `KURA_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what SAM tends to accept*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KURA at run start, based on what's moved in STATUS/TIMELINE/CHANGELOG/PREDICTIONS since the watermark in KURA.md. Cleared at end-of-run.*

**Watermark:** 2026-06-09 → window scanned = Jun 10–18 (Jun 16 BOJ HIKED 1.00% as-priced; Jun 17 FOMC Warsh-chaired hawkish SEP +40bp dot; Jun 17 Iran/US deal SIGNED electronic; Jun 18 Step 1.5 HAWK-Iran reconcile; Jun 18 stop re-arm single-leg $55.05; v1.6 DRAFT EV-table; KB hand-adds 186-194 by SAM Jun 10-15).

- **Run 3 outcomes applied** (commit `eaf6c218` "KOYOMI+KURA Run 5/3 apply bundle"): KB-SAM-184 (MOF measurement scope, A1, Framework) PROMOTED to KB.tsv (now 127 rows; max KB-SAM-184). KB-SAM-185 (thin-liquidity prediction-market discipline) RE-ROUTED to auto-memory `[[finding_thin_liquidity_prediction_market_discipline]]` by Will — cross-agent transferable, not Japan-domain-only. KB-183 routing precedent NARROWED to "tool-specific AND SAM-domain-only" per Run-3 CALIBRATION. FLOW-5.02 + 6.02 spot-stale fixes applied.
- **Jun 3 evening — v1.5.1 narrative reconciliation** (commit `39639b06`): minor version bump v1.5 → v1.5.1. New STRUCTURAL PILLARS section in THESIS promotes rate-differential, J-ICS lifer abandonment, hedge ratio 14-yr low, CFTC positioning to explicit thesis backbone. Channel 2 prose reconciled with CH-004 METHOD (Aug-2024-speed demoted expectation → upside-tail conditional on hawkish-of-pricing + at-peak positioning). Intervention paradox replaced with "structural pillars + asymmetric option on Jun 16" honest framing. Conviction split: direction/level HIGH vs near-term timing MEDIUM. No probability re-rates; position unchanged.
- **Jun 3 evening — v1.5.1 propagation completion** (commit `693f4e65`): 3-line fix (HENRY cross-agent link Aug-2024-speed demotion + STATUS Channel 2 ref + header v1.5 → v1.5.1).
- **Jun 3 evening — Open Flags rail Phase A + B** (commit `72220937`): eval re-baseline scoped & scheduled Jun 7-8 with operator packet at `evals/REBASELINE_v1.5.1_RUN_PROMPT.md`. SAM-23 mechanical mark-DOWN/UP trigger discipline pre-registered (conjunction-based, mirrors SAM-21 Jun-9 pattern).
- **Jun 4 AM — Jun 3-4 cabling-window news ingest + OS.1 closure + Sato corrections** (commit `079e46ca`): Bloomberg sources-leak ("BOJ Is Said to Mull June Rate Hike With Another Possible in 2026") + Ueda Kisaragi-kai (Jun 3 hawkish-of-pricing) + Polymarket built 94.8% → 96.9% (3rd sequential build) + Takaichi verbal Jun 3 at 160 reads as intervention-permission NOT pushback. SAM-21 HELD 70% per pre-registered Jun-9 discipline. OS.1 (fiscal-dominance counter-frame) CLOSED largely-falsified for SAM-21 binary; live for post-June PATH/CEILING story. Sato BOJ entry date corrected Jun 16 → Jun 30 + framing UPGRADED (Nakagawa was active 1.00% Apr-28 dissenter, so bloc drops 3 → 2 unless Sato surprises) — UNVERIFIED, KOYOMI quarantine in flight this same run.
- **Tape since Run 3:** USDJPY 160.03 (Jun 3 PM tag) → 159.92 (Jun 4 Asia). Brent $97.70 (Jun 3 close) → $96.97 (Jun 4, 2nd down session). JGB 30Y +3bp to 3.85% (Jun 4) curve steepening on hike anticipation. CFTC -114,667 still on May-26 reference (next print Sat Jun 6).
- **No TIMELINE / PREDICTIONS / TRACKER / insurer-profile structural updates Jun 4.** One new CHANGELOG entry (v1.5.1 follow-on, three-part: news ingest + OS.1 + Sato). STATUS substantially refreshed (banner + STATE OF PLAY + market data + BOJ ASSESSMENT table).

---

## LAST RUN

### Run 6 — 2026-06-19 (Fri AM, propose-only, post-BOJ + post-FOMC + Iran-deal cluster)

**Inputs scanned:** Watermark 2026-06-09 → 2026-06-19 window covers the densest 10d in v1.5.1's life. Read: KB.tsv (135 rows incl. SAM hand-adds 186-194 between Jun 10 & Jun 15; max ID KB-SAM-194), KB_ARCHIVE.tsv (58 rows unchanged), FLOW.tsv (last touched Jun 4 — stale on USDJPY/Brent/CFTC/Channel-1 status), VX.tsv (rows dated 2026-05-28), THESIS.md (banner Jun-18 fact strip + Pillar 1 RE-WIDENING; § INDEPENDENT CATALYST updated; Iran row Step 1.5 reconcile; structural-counter-flow NISA addition Jun-15), STATUS.md (new § FOMC JUN 17 RESOLVED + § BOJ JUN 16 RESOLVED blocks; Step 1.5 stop re-arm single-leg $55.05), STRATEGY.md, CHANGELOG (2026-06-18 + 2026-06-16 + Jun-10/PM/AM entries), THESIS_v1.6_DRAFT.md (EV-table inputs — flagged as DRAFT, not v1.5.1 fact).

**Outputs:**
- **6 proposed KB adds** (Fed-Chair, FOMC SEP, Iran-deal-signing-electronic, Iran-deal-toll-free-then-Oman, IEA-glut-warning, MOF-decay-48h-no-strike-at-161), **1 v1.6-DRAFT-tagged add** (EV-table inputs as v1.6 working assumptions). See § PROPOSED ADDS in KURA.md (this run appends Run-6 block).
- **9 palimpsest/SUPERSEDED proposals** — old Powell-Fed-Chair implicit anchors (in CHANGELOG/STATUS prose only — no dedicated KB row to flip; flag for cleanup-not-archive); KB-SAM-006 (HANS Fed-cut path) needs SUPERSEDED-pending-v1.6 marker (Fed-cut regime FLIPPED to Fed-HIKE); KB-SAM-008/010/036/044/045/046/151 already HISTORICAL; KB-SAM-127 (Inflection 2 FX hedge crisis BOJ surprise hike) — POV pivot fired Jun 16 *without* the modeled 10y move; mark resolved-against-mechanism; KB-SAM-152 (PC cascade Q2 peak) ages out — Q2 closed Jun 30; PROPOSE re-grade not archive.
- **0 archive-moves** (no rows already marked SUPERSEDED in KB.tsv as of run; KB-SAM-081/084/087/092/137/064 already SUPERSEDED per Jun-1 sweep — these sit in KB.tsv awaiting full-mode archive-move; KURA is propose-only this run so they stay).
- **2 FLOW spot-stale flags** (FLOW-JPN-5.02 + 6.02 — material) + 1 FLOW-JPN-3.01 sanity check (Norinchukin gate already resolved Jun-10 PM but row dated Jun-10 — fine).
- **1 VX threshold spot flag** (VX-SAM-11.02 trade balance: May TB due ~Jun 18-19 — not yet in workbook; mid-yield update window open).
- **2 dedup candidates** (KB-187 Japan oil reserves cluster — three rows KB-187/188/189/190 added Jun-15 to "Energy" category but cluster covers tightly-overlapping ground; recommend NO merge, instead surface as deliberately-decomposed cluster).
- **3 KB rows landed in window already (SAM hand-adds Jun 10-15):** KB-SAM-186 (Norinchukin FY2025), 187-190 (Japan oil/energy cluster), 191-194 (SoftBank-OpenAI/NISA/Bank-stress). These all entered KB.tsv directly via SAM; format pass to verify: schema OK; KB-SAM-186 has multi-line Notes (escaped quotes); slot KB-SAM-186 RE-USED from KURA Run-5 routing (was the catalyst-path decoupling row routed to auto-memory; SAM used the slot for Norinchukin) — per Run-4 precedent on slot re-use, this is CLEAN.

**Watermark proposed:** 2026-06-09 → 2026-06-19.

**Net workbook math (if SAM approves the 6 NEW + 1 DRAFT-tagged):** KB.tsv 135 → 142 rows; KB_ARCHIVE.tsv unchanged at 58 (propose-only).

**Notable non-promotes / route-elsewhere:**
- **Step 1.5 comprehensive-grep discipline** — PROME named SAM's comprehensive-grep as the correct verifier standard; transferable across the fleet. Per Run-3 narrowed routing (cross-agent transferable → auto-memory), → auto-memory candidate `[[finding_comprehensive_grep_vs_sample_verification]]` (or fold into existing `finding_doc_mirror_consistency_check` / `finding_followup_audit_pass`).
- **Risk-control re-arm ≠ sizing decision** (Will-decided 2026-06-18 stop re-arm) — operational discipline lesson, cross-agent transferable (any agent re-deriving an AND-stop-spec after one leg goes permanently FALSE faces this). → auto-memory candidate.
- **Boot-sweep gap on Warsh Chair change** — already promoted to `finding_boot_sweep_macro_regime_context` per the Jun-18 CHANGELOG. Confirm landed; no KB action.

**Calibration self-note (for SAM's CALIBRATION pass):**
- Run 6 = highest-yield run since inaugural (6 strong + 1 DRAFT-tagged). BOJ + FOMC + Iran-deal triple-resolution cluster justified the bump; precision-over-recall held — declined the cross-agent transferable items (comprehensive-grep / risk-control-re-arm).
- v1.6 DRAFT-TAGGED routing pattern is NEW. Recommend SAM/Will rule on a status convention — `LIVE-v1.6-DRAFT` or a separate Status column value — so the row promotes into KB.tsv but doesn't read as v1.5.1 fact. Default proposed: tag in Notes as `⚠️ v1.6 DRAFT input — not v1.5.1 fact; finalize-or-discard on v1.6 commit`.
- ID slot KB-SAM-186 re-use (SAM hand-added Norinchukin) — clean per Run-4 precedent. Next KB ID continues KB-SAM-195+.
- SAM-side direct KB adds (Jun 10-15, 9 rows) bypassed KURA — workflow note: when SAM has session bandwidth and the harvest is in-session, direct-add is fine; KURA's role contracts to format-check + dedup-sanity + watermark-advance. No process change needed.

---

### Run 5 — 2026-06-09 (Tue 12:35 PM ET, propose-only, intra-day in-session)

> **⚠️ SAM POST-RUN CORRECTION (Jun 9 PM, OHLC-verified — run-log below preserved as written):** Two midday premises this run ingested were corrected in SAM's evening pass (commit `cd9f23cd`): (1) **"Brent breach $90"** — actual: intraday tag $89.59 (~12 PM ET) that did NOT hold ($92.40 by evening, no closing breach); Mon Jun 8 closed UP +1.2%, so NOT 4 consecutive down sessions (Thu-Fri down / Mon up / Tue down; cum −4.5% not −7%). (2) **"USDJPY 4 days above 160"** — actual: 2 distinct tags (Fri + Tue) with Mon dip between; this premise-fail is why **KB-187 was DECLINED midday** (see Outputs annotation below). Next KURA run: treat evening-pass STATUS/TIMELINE language as current; the corrected facts are also a worked example for the OHLC-verify finding in SAM MEMORY.

**Inputs scanned:** Watermark 2026-06-04 → window = Jun 5 NFP shock + Jun 6 CFTC METHOD gate test + Jun 7 NEXUS_BRIEF rollout + Jun 8 (JST) Q1 GDP revised + Jun 9 noon SAM-21 mechanical fire + Brent breach $90. Read: STATUS (Jun 9 12:35 PM ET refresh, SAM-21 fire propagated), MEMORY (Sun Jun 7 closeout + NEXT SESSION rolling), CHANGELOG (newest = Jun 4 v1.5.1 follow-on; no Jun 5-9 entries yet — SAM-21 mechanical fire not yet logged as CHANGELOG entry), TIMELINE (newest = Jun 8-9 RESOLVED block: SAM-21 fire, Q1 GDP revised, Brent breach $90; Jun 5-6 RESOLVED block: NFP + CFTC), THESIS v1.5.1 (unchanged structure, version unchanged), PREDICTIONS (SAM-21 row updated 70→75, scoreboard preamble updated "1 RESOLVED-special / 4 OPEN" → notes the SAM-21 mark move), TRACKER (no change), KB.tsv (128 rows; max KB-SAM-185 post Run-4 promote after KOYOMI clearance), KB_ARCHIVE.tsv (58 rows), FLOW.tsv (lines 10-11 dated 2026-06-04 — STALE vs Jun 9 spots), VX.tsv (all 2026-05-28 — no new prints affect bands). Re-checked Run-4 `## PROPOSED ADDS` queue: KB-SAM-185 PROMOTED via KOYOMI clearance (KB.tsv row 128), queue clear before adding Run 5.

**Outputs:**
- **2 proposed adds:**
  - **KB-SAM-186 (Framework)** — Catalyst-path decoupling: level-reads vs path-reads, two-window empirical decoupling. **BORDERLINE — flagged for cross-agent-transferability re-route call.** This is conceptually the `finding_catalyst_path_decoupling` SAM has flagged for auto-memory. Per Run-3 narrowed routing (cross-agent transferable → auto-memory), this PROBABLY routes to auto-memory not KB. Surfaced as KB candidate at SAM's spawn-prompt request, with explicit routing flag.
  - **KB-SAM-187 (Framework)** — MOF intervention reaction-function: 4 days at USDJPY 160+ without strike under Bessent-Katayama-Himino cabling-aligned posture. Empirical datapoint on intervention reaction-function timing — durable mechanism observation (cabling-aligned vs not), pairs with KB-040 (intervention paradox) and KB-184 (measurement scope). ~~**CLEAR PROMOTE candidate**~~ **→ DECLINED Jun 9 (same day, Will-caught premise-fail):** USDJPY did NOT sustain 4 days above 160 — 2 distinct tags (Fri 160.20 + Tue 160.37) with Mon dip between; also the `usdjpy.py:73` "May26" label = apostrophe-stripped "May'26" for the May-6 op, not a May-26 intervention. The underlying observation (no MOF strike despite repeated 160+ tags under cabling-aligned posture) may re-form as a candidate with corrected framing post-Jun-16; do not re-propose on the "4 sustained days" premise.
- **0 archive-moves** (no SUPERSEDED rows in KB.tsv).
- **2 FLOW spot-stale flags:** FLOW-JPN-5.02 (USDJPY 159.92 Jun 4 → 160.37 Jun 9; CFTC -114,667 May 26 → -129,567 Jun 2 data 5th-build amplifier ON; SAM-21 70 → 75) + FLOW-JPN-6.02 (USDJPY 159.92 → 160.37; Brent $96.97 → $90.16, 4th down session, breach $90 line; Israel-Lebanon ceasefire context still accurate but oil thesis-side legs deeply met now).
- **1 VX staleness flag (informational):** VX.tsv all rows dated 2026-05-28 — no May Tokyo CPI / Apr trade balance / Mar wage data updates Jun 5-9. Next VX update window = Jun 18-19 May TB + Jun 19 National CPI.
- **0 cross-ref fixes, palimpsest collapses, dedup candidates, re-grades.**
- **3 add-candidates declined / re-routed** (see escalations below).

**Watermark proposed:** 2026-06-04 → 2026-06-09.

**Net workbook math (if SAM approves KB-187 and re-routes KB-186 to auto-memory):** KB.tsv 128 → 129 rows; KB_ARCHIVE.tsv unchanged at 58. If SAM keeps both as KB rows: KB.tsv 128 → 130. If SAM re-routes both: KB.tsv unchanged at 128.

**Notable non-promotes (the spawn-prompt-flagged candidates that did NOT clear):**
- **Mechanical-trigger-fire discipline pattern** (auto-memory candidate `finding_pre_registration_discipline_through_corroboration`) — held SAM-21 across 5 sequential ≥90% Polymarket reads, fired clean per spec Jun 9. Calibration-flavored cross-agent transferable lesson (any agent using pre-registered triggers + earned-discount calibration would apply this). Per Run-3 narrowed routing rule → auto-memory, not KB. **Route to auto-memory; don't propose as KB row.** Worked example anchor: STATUS § BOJ ASSESSMENT Jun 9 mechanical-trigger eval + PREDICTIONS SAM-21 narrative.
- **Earned-discount widening with conviction-direction-match** (75% vs Polymarket 98.2% = 23pp gap) — same family of calibration discipline as the above; also cross-agent transferable. Per Run-3 narrowing → auto-memory if anywhere. Furthermore, existing PREDICTIONS scoreboard preamble + SAM-21 narrative ALREADY encode this pattern (failed-twice Takaichi-ceiling discount). Routing: live in PREDICTIONS, no new KB row needed. **Decline as duplicate.**
- **KB-183 expiry-roll update** — Tue boot.py rolled to Jul-17 (9.64% IV, 25d RR -3.34) vs Fri's earlier expiry (11.08%, -14.53). This is an expiry-cycle artifact, NOT a broken-read or a calibration recurrence. KB-183 STILL FIRES correctly as a read-discipline anchor. **No row update needed; STANDING MONITOR carries forward, no action.**

**Calibration self-note (for SAM's later CALIBRATION pass):**
- Run 5 watermark advance 5 days as Will flagged in spawn prompt; mid-yield run as expected (1 clear add + 1 borderline). Discipline held — declined the SAM-flagged mechanical-discipline / earned-discount candidates as cross-agent-transferable per Run-3 narrowed rule rather than padding the KB roster.
- KB-186 (catalyst-path decoupling) tests the Run-3 narrowed routing rule one more time. SAM has already flagged this for auto-memory under `finding_catalyst_path_decoupling`. KURA's read: the rule applies to LIQUID (UST flows), HENRY (carry unwind), BROCK (treasury auctions) anywhere they ANCHOR a probability mark on an assumed catalyst path that a different path can hit. Probably auto-memory. But surfaced as KB candidate to give Will/SAM the routing call. If SAM accepts as KB, the rule generalizes to "tool-specific Japan-macro mechanism observation goes KB even when partially cross-agent." If SAM re-routes, the Run-3 rule holds firm.
- The intra-day in-session spawn (KURA fired during SAM's own active session, not at closeout) is a new spawn pattern. Worked because SAM-21 mechanical fire is a session-natural KB harvest moment (clear before/after, single trigger). Track whether this pattern reduces post-session subagent cadence pressure or just shifts it.
- Workbook signal density: 5-day window, 1 clear add + 1 borderline → mid-yield (Run 1 inaugural = 7; Run 2 = 1; Run 3 = 2; Run 4 = 1; Run 5 = 1-2). Consistent precision-over-recall discipline; no padding observed.

---

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
- ~~**KB-SAM-185 (Run 4) — Sato BOJ entry, PENDING_KOYOMI**~~ — **RESOLVED Jun 4 PM:** KOYOMI Run 6 cleared all 4 sub-claims; SAM promoted KB-SAM-185 to KB.tsv row 128 (BOJ-Wages, A1).
- ~~**ID-slot convention question**~~ — **RESOLVED Jun 4:** Will confirmed re-use the never-promoted KB-185 slot. Pattern: never-promoted-due-to-rerouting ≠ archived; ID slot is clean for re-allocation.
- ~~**KB-SAM-186 routing (cross-agent-transferable test)**~~ — **RESOLVED Jun 10 (Will ruled, Orch-concurred): ROUTED TO AUTO-MEMORY** as `finding_catalyst_path_decoupling` (with two-way sibling cross-refs to `threshold_vs_mechanism`). Run-3 narrowed rule HOLDS firm (cross-agent transferable → auto-memory). **Drop the KB draft row — do NOT add to KB.tsv.** ⚠️ ID collision note: the ID **KB-SAM-186 is now TAKEN** by SAM's Norinchukin FY2025 row (hand-added Jun 10, unrelated content); KURA's next proposed row starts at KB-SAM-187+ after re-checking max ID.
- ~~**Standing pre-registration discipline auto-memory candidates**~~ — **RESOLVED Jun 10 (Will ruled on all 3):** `finding_catalyst_path_decoupling` PROMOTED; `finding_pre_registration_discipline_through_corroboration` was already promoted Jun 10 AM; `finding_script_label_apostrophe_strip` FOLDED into existing `finding_number_carries_threshold_unit_source` (label-format extension — amend-don't-multiply); `finding_counter_frame_3_question_disposition` **DEFERRED to post-BOJ** for its second worked instance (two-instance standard; post-BOJ disposition wave — Branch-C scoring, CH-005, Channel-1 retire — supplies it). Drop from carry-state except the deferred item.
- ~~**KB-SAM-185 placement call**~~ — **RESOLVED Jun 3:** RE-ROUTED to auto-memory `[[finding_thin_liquidity_prediction_market_discipline]]` by Will. KB-183 routing precedent narrowed (tool-specific AND SAM-domain-only → KB; cross-agent transferable → auto-memory).
- ~~**KB-SAM-183 placement call**~~ — **RESOLVED Jun 3:** approved as Framework KB row (KB.tsv row 126). Routing precedent established for tool-specific methodology caveats.

---

## STANDING MONITORS (surface each run until resolved)

- **JICPA finalization** (KB-108, KB-125) — STATUS CHECK still pending; no FINAL standard reported post comment-close (Mar 17). Base case approval; tail risk neither confirmed nor cleared. *(No update Run-2.)*
- ~~**Norinchukin Jun FY2025 print**~~ — **RESOLVED Jun 10 (SAM direct, Will-directed pull):** results were out May 21 (IR HTML 403s hid them; direct PDFs work). CLO book **record ¥10.1T Mar 2026 (+¥1.8T YoY)** — BOTH prior figures wrong (¥8.2T was Dec 2024; "¥9.7T shrinking" falsified — never declined). Gate NOT reactivated; net income ¥121.4B beat. SAM already did: FLOW-3.01 refresh (→ ARMED-DORMANT), FLOW-3.03 note, **KB-SAM-186** (hand-added — KURA verify format next run), TRACKER/THESIS/STATUS/TIMELINE sweep, norinchukin.md canonical refresh. **Residual for KURA Run 6:** KB-160 cross-ref check (its CLO mentions are insurer-side, likely fine) + KB-186 format/dedup pass.
- **Mid-tier ESR window** — T&D, Sony Life, Daido, Taiyo prints (late-Jun); consistency check vs Big 3 v1.5 pattern. Explicit foreign-bond reduction language would partially reactivate Channel 1. *(No update Run-2.)*
- **May TB print Jun 18-19** — Phase 1 inversion diagnostic per THESIS v1.4 (queues against KB-176). *(No update Run-2.)*
- **FY2026 hedge ratio** — Mar-2026 full-year aggregate not yet released per KB-065/066. Surface when next industry hedge ratio prints. *(No update Run-2.)*
- **`fxy-proxy-v1` recalibration** (NEW Run-2) — **Third consecutive anomaly print Jun 3 AM (1.17% Jun-18 IV)** after Jun 2 (1.56%) and Jun 1 baseline (10.52%). Now firmly persistent, not transient. KB-183 covers the read-discipline; what's still owed is the `fxy_options.py` source diagnosis (SAM NEXT SESSION #6). Surface each run until either recalibration lands or anomaly resolves spontaneously. *(No Jun 4 update — boot.py output not refreshed Jun 4 AM per STATUS data table footnote; carry forward.)*
- **MOF intervention quarterly per-op release** (NEW Run-3) — resolves the ~¥1.95T residual classification (70% slippage / 30% possible late-May smoothing op prior, per Jun 3 PM verification). Next quarterly release expected ~Aug. If late-May op confirmed: marginally hawkens reaction-function read. Park; no current action. Now paired with the landed KB-184 (MOF measurement scope) for next-quarter close-out.
- ~~**Polymarket Jun 9 re-check**~~ — **RESOLVED Jun 9:** SAM-21 mechanical trigger FIRED 70 → 75% per pre-registered spec (Polymarket 98.2% / Takaichi pushback NONE / Q1 GDP composition non-blocking). PREDICTIONS + TIMELINE + STATUS updated. Discipline-credibility lesson tracked separately as auto-memory candidate.
- **Sato Jun 30 BOJ board entry** (Run-4) — KB-185 PROMOTED. Now tracking Sato's first MPM (Jul 31) for dissent-vote validation of the 3 → 2 framing. If Sato dissents WITH Takata/Tamura on the dovish side, row's consequence chain is confirmed; if Sato unexpectedly votes hawkish, row's "unless Sato surprises" caveat fires. Surface until Jul 31 MPM resolves.
- ~~**CFTC Sat Jun 6 print**~~ — **RESOLVED Jun 6:** METHOD residual-gate test resolved AGAINST cover (-129,567 = 72% of cycle peak; amplifier +5pp ON, residual ON). No 30d bucket re-mark (within ±5pp discipline band). Now tracking Sat Jun 13 print (last pre-blackout read; -153K/85% line is next escalation gate to +8-10pp amplifier).
- **CFTC Sat Jun 13 print** (NEW Run-5) — last pre-blackout CFTC read. If shorts build through -153K (85% line) → amplifier escalates +5pp → +8-10pp → 30d bucket may bump +3-5pp. If shorts cover below -108K (60% line) → amplifier+residual OFF → 30d 37% → ~29-32%. Either path produces auto-CHANGELOG entry worth scanning at next KURA run.
- **BOJ Jun 16 MPM** (NEW Run-5) — heaviest expected harvest window across the agent network. KURA Run 6 (post Jun 16-17) likely 5-10 candidates depending on outcome. Hike-delivered: SAM-21 RESOLVES, SAM-24 (25bp not 50bp) RESOLVES; CHANGELOG entry on hike + Ueda presser + statement language. Hike-skipped (tail): SAM-08/SAM-20 lesson cluster triple-FAILED — calibration entry to PREDICTIONS_ARCHIVE. Either outcome triggers full thesis re-balance pass.
- **Brent down-drift + SAM-23 catalyst-path decoupling** (NEW Run-5; **corrected Jun 9 PM**) — Brent tagged $89.59 intraday Tue Jun 9 but did NOT hold ($92.40 by evening; no closing breach of the "$90 = headwind resolved" line; Mon was an up session — choppy drift, cum −4.5%). SAM-23 mark-DOWN conjunction has legs (i) MET (Thu-Fri consecutive + cum ≥−2% — not "deeply") but USDJPY-leg INVERTED (160+). Empirical decoupling of MOU → oil → yen path still observed across 2 distinct micro-windows (Fri NFP-route + Tue oil-down-under-stable-USDJPY). CHANGELOG re-anchoring entry warranted post-Jun-16 settle per MEMORY NEXT SESSION. KURA Run 6 likely has a method-execution KB candidate if SAM-23 framework re-anchors.
- **MOF no-strike-at-160 pattern** (Run-5; **EVOLVED post-Jun-16 — corrected-framing candidate now RIPE — Run-6 PROPOSED ADD):** Post-BOJ-hike Wed-Thu (Jun 17-18), USDJPY ran 160.78 → **161.34** with **48h+ no strike** and Bloomberg's "Markets Alert for Japan Intervention" surfaced Wed — first reaction-function-decay observation under cabling-aligned posture in v1.5.1's lifetime. PROPOSED as new KB row (KB-SAM-196 in Run-6 PROPOSED ADDS, Cross-Agent category, paired with KB-040/170/184). Surface ONGOING — MOF decay window is the load-bearing input to the post-BOJ MOF-#3 scenario-weighted anchor.
- **Sat Jun 20 CFTC print (Jun 16 data — first post-catalyst read)** (NEW Run-6) — load-bearing for v1.6 RED challenge #1 EV-table. If covers below -120K (~67% peak) → residual term OFF → frame fails margin test → v1.6 may trigger trim/close discussion. If holds at -140K to -150K (~78-83%) → residual ON → frame survives. KURA Run 7 likely material — CHANGELOG entry on disposition.
- **Fri Jun 19 Japan National May CPI** (NEW Run-6) — first national print post-BOJ-hike; the trade-balance print landed Wed; CPI now is the input for v1.6 re-underwrite (per CHANGELOG "v1.6 triggers tonight after Fri CPI"). KURA Run 7 will harvest v1.6 commit if it lands.
- **Iran/US deal verification leg** (NEW Run-6) — initial agreement signed Wed Jun 17 (electronic, Al Jazeera); per CNN "tougher talks ahead." Open sub-questions: demining (Iran HEU dilution compliance), insurance restoration (London market re-rating), traffic normalization (Day 110 initial 4 supertankers; backlog "weeks to clear"), Oman fee-administration after 60-day toll-free window (closes ~Aug 16), sanctions waivers rollout. Each is a candidate KB row at resolution; surface as cluster. CRS R42460 SPR runway re-quantification (KB candidate if SAM elevates from STATUS prose).
- **v1.6 thesis re-underwrite drop** (NEW Run-6) — drafting tonight per CHANGELOG. KURA Run 7 likely harvests structural KB rows (re-centered carry-unwind tail framework, FXY-vol vs spot vehicle question, MOF-decay anchor) if v1.6 commits.
- **NISA retail outward flow ¥6T-total / ¥1T/mo subset reconciliation** (NEW Run-6) — THESIS structural-counter-flow paragraph flags figures as needing reconciliation; KB-SAM-193 ALREADY ADDED Jun 15 with the reconciliation flag in Notes. Surface until reconciliation resolves; do not re-propose.
- **Sato Jun 30 BOJ board entry** — KB-SAM-185 anchors. Sato's first MPM is Jul 31 — validation watch (post-Asada-dovish-dissent at Jun 16, "3 → 2 unless Sato surprises" framing now has the freshest evidence cluster). Surface until Jul 31 MPM resolves.
- **CFTC weekly post-catalyst series** — METHOD residual gate is now load-bearing for the EV-table. Each Sat print until cover OR EV-frame fails.

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

- **Likely watermark window:** 2026-06-19 → next-run date. Expected harvest cadence (Run 7):
  - **Fri Jun 19 evening — v1.6 thesis commit** (post Fri National CPI per Will-named gate). Likely 3-5 structural KB candidates: re-centered carry-unwind tail framework, MOF-decay reaction-function anchor (paired with KB-187 post-Jun-16 corrected-framing if KURA Run-6 KB-SAM-196 lands), FXY-vehicle question disposition, Warsh-Fed-regime tripwire spec, NISA-tripwire (MoF weekly trust line).
  - **Sat Jun 20 CFTC print (Jun 16 data)** — first post-catalyst CFTC; load-bearing for v1.6 EV-table; CHANGELOG entry likely whichever way.
  - **Mon Jun 22 KB.tsv mass-archive opportunity** — Run-6 propose-only run flagged ~6 already-SUPERSEDED KB.tsv rows awaiting full-mode archive-move (KB-SAM-064/081/084/087/092/137). If SAM grants `full` mode on Run 7, these move out in one pass.
  - **Mon Jun 30 Sato seats BOJ board** — KB-185 anchors; Jul 31 first vote is the validation gate.
- **Re-check `## PROPOSED ADDS` queue (Run-6)** — six new KB candidates + one v1.6 DRAFT-tagged. SAM rules on routing convention for DRAFT-tagged rows (Notes-tag default vs new Status column value); Will may have stronger view. Drop after disposition.
- **PENDING resolutions to chase down before Run 7:**
  - **KB-SAM-006 SUPERSEDED proposal** (Fed-cut path FLIPPED to Fed-HIKE under Warsh) — if accepted, archive on Run 7 `full` mode.
  - **KB-SAM-127 (Inflection 2 BOJ surprise hike → 10y move in 2 weeks)** — fired Jun 16 *without* the modeled mechanism; either re-grade to mechanism-direction-failure (cluster with SAM-14/19/25/Norinchukin pattern) or mark SUPERSEDED.
  - **KB-SAM-152 PC cascade Q2 peak** — Q2 closes Jun 30; if Q3 redemptions surface, refresh row, otherwise re-grade.
  - **Cross-agent transferable lessons** (Step 1.5 comprehensive-grep, risk-control re-arm) — Will rules auto-memory yes/no.
- **`fxy-proxy-v1` watch** — KB-183 fires correctly under v1.5.1 still. Jun 15 boot showed +24.05 RR sign-flip on Sun → reverted to -8.37 on Mon = exactly the KB-183 sign-impeachment pattern; row holds. `fxy_options.py` source diagnosis still deferred.
- **MOU walk-back vs further escalation** — SUPERSEDED by Iran-deal-SIGNED-Jun-17. Verification-leg watch replaces MOU-binary watch (per STANDING MONITORS).
- **Intra-day in-session spawn pattern** — Run 5 fired in-session (SAM-21 trigger); Run 6 fired between sessions (Will-directed at the v1.6-pre-draft inflection). Both patterns work for different content shapes. Run 7 likely closeout-spawn after v1.6 commits.
  - **Wed Jun 10 US CPI + JGB 30Y auction** — SAM-26 mechanism diagnostic (30Y back above 4.0% or auction softness signals Phase-1 fiscal-supply driver). Possible mechanism/diagnostic KB candidate if 30Y auction prints with explicit tail or cover-ratio breakdown.
  - **Sat Jun 13 CFTC Jun 9 data** — last pre-blackout CFTC read; -153K/85% line is METHOD next escalation gate. If amplifier flips to +8-10pp on a build OR amplifier+residual OFF on a cover, the METHOD's second real-world application produces a durable execution-pattern note ("amplifier-escalation gate fired week-of vs week-prior-of catalyst" type rule).
  - **Jun 13-15 pre-BOJ blackout window** — MOF/Bessent/Katayama verbal density continuing; possible POV pivot if cabling tone shifts (e.g., dovish Ueda last-minute leak or Bessent rate-gap pushback). METSUKE pre-BOJ run likely fires here.
  - **Tue Jun 16 BOJ MPM + Wed Jun 17 FOMC + Thu Jun 18-19 May TB / National CPI cluster** — heaviest expected harvest. KURA Run 6 post-cluster (Jun 20-22) likely material; could be 5-10 candidates depending on BOJ outcome. Cluster resolves SAM-21, SAM-24, potentially SAM-26, and the SAM-23 catalyst-path decoupling either way.
  - **Mon Jun 30 Sato seats BOJ board** — KB-185 anchors here; the consequence chain validates / falsifies at Sato's first MPM (Jul 31).
- **Re-check `## PROPOSED ADDS` queue** against newly-landed rows — Run-5 queue now holds only the borderline KB-186 (catalyst-path decoupling, routing-pending → auto-memory call with Will). **KB-187 was DECLINED same-day (Jun 9, premise-fail — see Run 5 Outputs annotation): the "4 days at 160+" claim was wrong (2 distinct tags with Mon dip).** Do not re-propose on that premise; a corrected-framing no-strike-at-160 candidate may re-form post-Jun-16. If KB-186 routes to auto-memory, drop from queue and propose anew at Run 6 only if the mechanism produces a fresh Japan-macro datapoint.
- **Re-verify** the no-change items in KURA brief still hold (hands-off list, category list, watermark line, the 5-gate rubric).
- **`fxy-proxy-v1` watch** — KB-183 fires correctly Jun 9 (expiry-roll behavior, not broken read). `fxy_options.py` source diagnosis (SAM MEMORY NEXT SESSION #6) still deferred; KB-183 holds. If post-BOJ a `fxy-proxy-v2` revision lands, KB-183 needs Source-row refresh.
- **MOU walk-back vs further escalation** — Brent tagged $89.59 intraday Jun 9 but didn't hold ($92.40 evening; no closing breach of $90 — corrected Jun 9 PM; rumor-tier Trump-Iran walk-back + China demand weakness drove the drift). If Tehran fully resumes message exchange OR Trump-Khamenei reset → SAM-23 mark-DOWN trigger may fire (still gated on USDJPY-leg falling below 159.50). If Tehran further escalates (Hormuz block, additional grievance) → SAM-23 mark-UP gates conjunction-evaluate. New POV pivot in CHANGELOG worth harvesting either direction; pair with SAM-23 catalyst-path decoupling CHANGELOG entry SAM has flagged.
- **Norinchukin Jun FY2025 print date** — still TBD; material Channel 1 re-test gate.
- **Cross-agent transferable lesson candidates parked under PENDING** (Run 5) — if SAM/Will rule on any as auto-memory, KURA can drop them from carry-state:
  - `[[finding_catalyst_path_decoupling]]` — when a framework anchors mark-up/down conjunction on an assumed catalyst path (MOU → oil → yen), a different path (NFP → USD → USDJPY) hitting the same level invalidates path-dependency but not level read. Discriminate level-driven vs path-driven triggers. Worked example: SAM-23 Jun 5 NFP-route + Jun 9 Brent-decoupled. (Also surfaced as KB-186 candidate this run; routing call pending.)
  - `[[finding_pre_registration_discipline_through_corroboration]]` — pre-registered trigger value comes from holding through multi-source-corroboration pressure (SAM-21 Jun 3-9 worked example, 5 sequential Polymarket ≥90% reads + Bloomberg sources leak + Ueda hawkish speech, fired clean per spec).
  - `[[finding_counter_frame_3_question_disposition]]` — 3-question rubric for closing counter-thesis hypotheses (market repriced THROUGH? inside the discount or un-priced? path/ceiling vs binary?). Worked example: OS.1 fiscal-dominance closure Jun 4.
- **Intra-day in-session spawn pattern** (NEW Run-5) — Run 5 fired during SAM's own active session on a session-natural KB harvest moment (SAM-21 mechanical trigger fire). Track if this pattern recurs post-Jun-16 BOJ resolution (another session-natural moment). If yes, the subagent-trio cadence may bifurcate to: "intra-session for clear trigger fires" + "closeout for multi-file edit passes."
