# KURA MEMORY

State file for the workbook-librarian sub-agent. Spec is in [`KURA.md`](KURA.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership split:**
- **KURA writes** at end-of-run: appends to `## LAST RUN`, adds/removes `## PENDING` items, updates `## STANDING MONITORS`, fills `## NEXT RUN HINTS`. Also fills `## CHANGES SINCE LAST RUN` at the START of each run.
- **SAM writes** `## CALIBRATION` after applying KURA's proposals (it's SAM's view of which patterns held; KURA can't know its own approve/reject rate during its own run).

**Spawn order:** KURA reads `KURA.md` first (spec), then `KURA_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what SAM tends to accept*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KURA at run start, based on what's moved in STATUS/TIMELINE/CHANGELOG/PREDICTIONS since the watermark in KURA.md. Cleared at end-of-run.*

**Watermark:** 2026-06-19 → window scanned = Jun 19–22 (quiet post-cluster weekend, as spawn anticipated). Only STATUS.md moved post-watermark (mtime Jun 22); CHANGELOG/THESIS/TIMELINE/PREDICTIONS/TRACKER/research-outputs ALL predate the watermark (≤Jun 18) → **v1.6 has NOT committed** (Run-6 hints expected it Fri Jun-19 evening; it's gated on the Mon Jun-22 3:30 PM ET CFTC Jun-16 EV-print + RED pass, both still pending at boot).

- **National May CPI verified Jun 20** — headline 1.5 / core 1.4 (<2% 4th straight, 4-yr low; matched fcst) / core-core 1.8 (−10bp vs Apr 1.9, slight dovish miss). Headline ↑ only on energy base-effect (utility-subsidy expiry). NOTE: this resolved KB-169's embedded forward call TRUE ("national May core-core will likely print above Tokyo's 1.6%" → 1.8 > 1.6). Telemetry (→ CPI.tsv) + v1.6 input; NOT a new KB row.
- **Brent decoupling test = SHRUG (Sat Jun 20)** — Iran declaratory Hormuz re-closure produced NO Brent spike (Brent fell to $77.84, −2.5% day, ~−20% cum from $96.78 Jun-3). Confirms declaratory-not-physical; oil-in-yen channel stays dormant. Single-event behavioral observation.
- **Ueda discharged Fri Jun-19, back at work Tue Jun-23** (Bloomberg/Reuters/Japan Times Jun-19) — earlier than the modeled ~Jul-30/31 return → leadership-overhang / stand-in-presser tail REMOVED; Ueda's own hawkish framing is live guidance into Jun-24 SoO / Jul-31 MPM. Jun-24 BOJ Summary of Opinions added to docket.
- **MOF silent 6 days at 160+** — USDJPY 161.34 (Jun 18) → 161.54 (Mon Jun 22), still no 3rd strike; 162 within 0.3%, ~0.4y below the 161.96 weakest-since-1986 record. Extends KB-199's 48h-no-strike observation (not a new row).
- **Tape Jun 18→22:** USDJPY 161.34 → 161.54; FXY $56.86 → $56.80 (−2.6% vs $58.32 cost; 13 sh ≈ −$20); Brent $79.68 → $77.84; JGB Jun-19 pub 10Y 2.656 / 30Y 3.786 / 40Y 3.741 (long-end drifted ↑2-4bp on week, no stress). FXY ATM IV bled to 9.40% (event premium gone post-FOMC); 25d RR −11.16 (calls bid, thesis-side). CFTC still −145,818/81% (Jun-9 data) — Jun-16 EV-gate print pending Mon 3:30 PM ET.
- **No analytical re-marks in the window** — SAM froze marks pending the v1.6 CFTC+RED pass. 0 SUPERSEDED-status changes, 0 new KB hand-adds, 0 CHANGELOG entries since Jun 18.

---

## LAST RUN

### Run 7 — 2026-06-22 (Mon, FULL MODE, quiet-weekend window)

**Inputs scanned:** Watermark 2026-06-19 → Jun 19-22. KB.tsv (143 rows pre-move, max KB-SAM-200), KB_ARCHIVE.tsv (58 rows pre-move), FLOW.tsv (5.02/6.02 dated Jun-4 — deeply stale), VX.tsv (rows dated 2026-05-28). STATUS.md (Jun-22 boot — the ONLY post-watermark-moved doc). CHANGELOG / THESIS / TIMELINE / PREDICTIONS / TRACKER / research-outputs all ≤Jun-18 (v1.6 NOT committed). Re-checked Run-6 PROPOSED-ADDS queue: all 7 (KB-195/196/197/198/199 + KB-200 DRAFT) verified LANDED in KB.tsv rows 138-143.

**Outputs:**
- **🔑 ARCHIVE-MOVE (the one full-mode autonomous act): KB-SAM-006 only.** Moved out of KB.tsv → appended to KB_ARCHIVE.tsv trailing SUPERSEDED block. Status PRESERVED as `SUPERSEDED` (version/regime-supersede — superseded by KB-195/196; matches archive convention for the 6 existing SUPERSEDED rows). Relocation stamped in Notes. KB.tsv 143 → 142; KB_ARCHIVE.tsv 58 → 59; 9-col integrity verified; 0 SUPERSEDED rows remain in KB.tsv.
- **⚠️ EXPECTED-SET DISCREPANCY FLAGGED (the headline finding):** the spawn + Run-6 memory expected KB-SAM-064/081/084/087/092/137 to also be SUPERSEDED-in-KB.tsv-awaiting-move. They are NOT in KB.tsv — they were **already archived** (KB_ARCHIVE.tsv, Status=SUPERSEDED, since commit `63f98190` "finish workbook audit — KB superseded-move" — pre-dates KURA Run 1). The Run-6 propose-only note ("these sit in KB.tsv awaiting full-mode archive-move") was a **verification miss** (asserted KB.tsv membership without grep-checking; cf. `[[finding_verify_counts_before_propagating]]`). Net: only 1 row (KB-006) was actually pending archive, not 7.
- **PROPOSED ADDS: 0.** Quiet post-cluster weekend (spawn anticipated 0-2). The v1.6 commit that Run-6 hints expected to seed 3-5 structural rows has NOT landed — structural-KB harvest DEFERRED to the post-v1.6-commit run.
- **0 palimpsest / re-grade / dedup / cross-ref actions** (none ripe; no new prose landed except STATUS data).
- **FLOW/VX:** re-affirmed Run-6 DEFERRAL of FLOW-5.02/6.02 full re-derivation to v1.6 finalize (per spawn). Updated stale spots flagged for when SAM does the re-derivation: USDJPY 159.92→161.54, CFTC −114,667→−145,818 (Jun-9; Jun-16 print pending), Brent $96.97→$77.84, SAM-21 RESOLVED-CONFIRMED Jun-16, SAM-23 RESOLVED-FAILED Jun-16. VX-SAM-11.02 (trade balance) still ¥+301.9B Apr — stale (May TB landed Jun-18; SAM to supply figure + threshold call).

**Watermark proposed:** 2026-06-19 → 2026-06-22.

**Net workbook math:** KB.tsv 143 → 142 (KB-006 out); KB_ARCHIVE.tsv 58 → 59 (KB-006 in). No adds.

**Calibration self-note (for SAM's CALIBRATION pass):**
- Run 7 = lowest-yield run since Run-2 (0 adds), correctly matching a quiet weekend with no thesis-doc movement and v1.6 un-committed. Precision-over-recall held: declined CPI (telemetry/CPI.tsv + already-in-KB-169), MOF-6d-no-strike (extends KB-199), Brent-SHRUG (single event, needs 2nd instance). No padding.
- Full-mode archive-move executed cleanly on its first real use since Run-1; the discrepancy-flag (7-expected vs 1-actual) validated the spawn's "sanity-check found-set against expected list, FLAG don't guess" instruction — the gap traced to a Run-6 unverified membership claim, not a missing/extra row.

---

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
- ~~**BOJ Jun 16 MPM**~~ — **RESOLVED Jun 16:** hiked 1.00% as-priced (7-1, Asada dovish dissent). SAM-21 ✅ CONFIRMED, SAM-24 ✅ CONFIRMED, SAM-23 ❌ FAILED (no MOF #3 strike), SAM-26 ❌ FAILED (30Y didn't hold ≥4.0%). 0 OPEN predictions remain. Run-6 harvested the cluster (KB-195/196/197/198/199 + KB-200 DRAFT). No further KURA action.
- ~~**Brent down-drift + SAM-23 catalyst-path decoupling**~~ — **RESOLVED:** SAM-23 FAILED Jun 16 (calibration win, pre-marked 72→~30). Catalyst-path decoupling lesson ROUTED to auto-memory `[[finding_catalyst_path_decoupling]]` (Will, Jun 10). Brent-side now in collapsed-oil regime (KB-197 deal + KB-198 IEA glut). No KURA action.
- **MOF no-strike-at-160 pattern** — **LANDED as KB-SAM-199 (Run-6, Cross-Agent).** Jun-22 extended the observation: USDJPY 161.54, MOF silent **6 days** at 160+, ~0.4y below the 161.96 weakest-since-1986 record. STRENGTHENS KB-199 (its falsification gate (iii) "USDJPY<160" not tripped; gate (i) "MOF strikes pre-Jun-30" not tripped). Surface ONGOING — feeds the v1.6 post-BOJ MOF-#3 scenario-weighted anchor; if MOF strikes pre-Jun-30 OR USDJPY breaks 162/record, that's a KB-199 update (SAM-side, not a new row).
- **CFTC Jun-16 print (first post-catalyst read) — DATE CORRECTED Sat Jun-20 → Mon Jun-22 (Juneteenth holiday)** — releases **3:30 PM ET Mon Jun-22**, NOT yet in hand at boot (boot.py still shows stale Jun-9 −145,818/81%). Load-bearing for the v1.6 RED #1 EV-table (KB-200 DRAFT): cover <−120K → residual OFF → frame fails margin test → trim/close discussion; hold −140K to −150K → frame survives; build through −153K/85% → frame strengthened. KURA next-run likely material — CHANGELOG entry on disposition + KB-200 promote-or-discard.
- ~~**Fri Jun 19 Japan National May CPI**~~ — **RESOLVED/LANDED Jun 20 (verified):** headline 1.5 / core 1.4 (<2% 4th straight, 4-yr low) / core-core 1.8 (−10bp vs Apr 1.9). Telemetry → CPI.tsv; NOT a KB row (durable interpretive content already in KB-169, whose embedded forward call "national May core-core > Tokyo 1.6%" resolved TRUE at 1.8). v1.6 re-underwrite input. SAM may add a one-line resolution annotation to KB-169 (palimpsest, SAM-side).
- **Iran/US deal verification leg** (NEW Run-6) — initial agreement signed Wed Jun 17 (electronic, Al Jazeera, KB-197); per CNN "tougher talks ahead." Open: demining (HEU dilution compliance), insurance restoration, traffic normalization, Oman fee-administration after 60-day toll-free window (closes ~Aug 16), sanctions waivers. **Jun-20 datapoint:** Iran's *declaratory* Hormuz re-closure produced NO Brent spike (SHRUG, $77.84) — confirms market discounts declaratory-not-physical threats post-deal. Each verification sub-leg a candidate KB row at resolution; surface as cluster. KB-051 (Kharg path) RE-GRADE-pending dormant through ~Aug 16. CRS R42460 SPR runway re-quantification (KB candidate if SAM elevates from STATUS prose).
- **v1.6 thesis re-underwrite drop** — **STILL PENDING (NOT committed as of Jun-22 boot).** Gated on the Mon Jun-22 3:30 PM ET CFTC Jun-16 print + RED pass. CHANGELOG still dated Jun-18. Structural-KB harvest (re-centered carry-unwind tail framework, MOF-decay anchor [pairs KB-199], FXY-vol-vs-spot vehicle question, Warsh-Fed tripwire spec) DEFERRED to the post-v1.6-commit run. KB-200 `[v1.6-DRAFT]` promote-or-discard disposition resolves on v1.6 commit.
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

- **Likely watermark window:** 2026-06-22 → next-run date. **The next run is the v1.6-commit harvest** — Run 7 was the quiet pre-v1.6 lull (0 adds). Expected cadence:
  - **v1.6 thesis commit (PENDING — the load-bearing event)** — gated on the Mon Jun-22 3:30 PM ET CFTC Jun-16 print + RED pass. When it lands, expect **3-5 structural KB candidates**: re-centered carry-unwind tail framework, MOF reaction-function-decay anchor (pairs/extends KB-199; Jun-22 6-day-no-strike data feeds it), FXY-vol-vs-spot vehicle-question disposition, Warsh-Fed-regime tripwire spec, NISA-tripwire (MoF weekly trust line, KB-193 anchor). Watch the CHANGELOG date advancing past Jun-18 as the commit tell.
  - **KB-200 `[v1.6-DRAFT]` disposition** — promote to LIVE (drop tag) IF the EV-table survives RED #1a-d; discard (→ KB_ARCHIVE) if RED breaks the frame. Resolves on v1.6 commit. Re-check at next run.
  - **CFTC Jun-16 print** — first post-catalyst read, releases Mon Jun-22 3:30 PM ET. Disposition (residual ON/OFF) drives the v1.6 EV-table margin test. CHANGELOG entry likely whichever way.
  - **Mon Jun 30** — (a) Sato seats BOJ board (KB-185 anchor; Jul-31 first vote is the validation gate); (b) Q2 close → KB-152 PC-cascade-Q2-peak re-grade trigger.
- **PENDING SAM-side adjudications to chase (carried, none KURA can act on):**
  - **KB-SAM-127** (Inflection 2) — RE-GRADE palimpsest note already appended Run-6 (mechanism-direction-failure cluster); SAM to finalize the Key_Fact collapse or Status call. KURA flags; SAM adjudicates.
  - **KB-SAM-152** (PC cascade Q2 peak) — RE-GRADE pending Q2-end (Jun 30); palimpsest note already appended Run-6.
  - **KB-SAM-051** (Brent $120 Kharg) — RE-GRADE-pending-dormant through ~Aug 16 (60-day toll-free window close); reactivation gate noted Run-6. Do NOT archive — verification leg open.
  - **KB-169** — embedded forward call resolved TRUE Jun-20 (national May core-core 1.8 > Tokyo 1.6); SAM may add a one-line resolution annotation (palimpsest, SAM-side).
- **⚠️ ARCHIVE expected-set discrepancy (RESOLVED this run, logged for the record):** the "6 SUPERSEDED rows awaiting full-mode move" (064/081/084/087/092/137) were ALREADY in KB_ARCHIVE.tsv since commit `63f98190` — a Run-6 unverified-membership claim. Only KB-006 actually needed moving (done Run-7). Lesson: next archive-move run, grep `\tSUPERSEDED\t` in BOTH KB.tsv and KB_ARCHIVE.tsv before trusting any carried "expected set." (cf. `[[finding_verify_counts_before_propagating]]`)
- **`fxy-proxy-v1` watch (KB-183)** — fires correctly; ATM IV bled to 9.40% post-FOMC (event premium gone), 25d RR −11.16 (calls bid). Sign-read holds. `fxy_options.py` source diagnosis still deferred; if a `fxy-proxy-v2` revision lands, KB-183 Source row needs refresh.
- **Iran/US deal verification leg cluster** — see STANDING MONITORS; each sub-leg a candidate KB row at resolution. Jun-20 declaratory-Hormuz SHRUG is a behavioral datapoint (needs a 2nd instance before it earns a row, OR folds into v1.6 oil-channel-dormant framing).
- **FLOW/VX full re-derivation** — STILL DEFERRED to v1.6 finalize (per Run-6 spec + Run-7 spawn). FLOW-5.02/6.02 are Jun-4-dated, deeply stale (USDJPY/CFTC/Brent/SAM-21-resolved/SAM-23-resolved). VX-SAM-11.02 trade-balance stale (May TB landed Jun-18). When v1.6 lands, this is a same-pass re-derivation, not a surgical fix.
- **Re-verify** the KURA-brief no-change items still hold (hands-off list, category list, watermark line, 5-gate rubric).
