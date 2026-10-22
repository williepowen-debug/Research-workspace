# WATT — D:L717 P1 de-escalation re-test (10/15–10/21) · D:L650 PJM 7/2 peak split · D:L770 carried acts

**Observed 2026-10-22 08:32–08:38 ET** (PROME-spawned subagent of session 84affa50, Claude Code; system-stated model Claude Opus 5.5, `claude-opus-5-5`, not independently verified). Raw captures + manifest: `sources/2026-10-22/`. Tape = PJM Data Miner 2 PJM-RTO (pnode 1) **unverified 5-minute** operational data, not settlement.

**Bottom line.** The October 15–21 window is **clear on every limb of the registered letter**, so **P1 de-escalates 5 → 3 today on the letter as executed (KB-118 / KB-133 / KB-149)** and the **composite moves 16/20 → 14/20**. This is the letter's evidence forcing a score change (item: D:L717), not judgment, and it is not early: the window closed 23:59 ET 10/21 and this is the first boot on/after 10/22. ⚠️ Watch fact, not a prediction: PJM's same-day outage forecast is **70.2 GW for 10/21 and 71.5 GW for 10/22** — above the ~61–62 GW on the 10/13–14 emergency days — and a Capacity Advisory ran for 10/19. A RED re-fire re-escalates on the letter (3 → 5), as on 10/7.

## D:L717 — grade on the letter

Letter (KB-149): (1) no PJM §202(c) order standing and none new; (2) seven clear calendar days with no EEA-class posting (calendar reading, L-51); (3) Hot Weather Alert lifted; a RED re-fire inside the window restarts it.

| Governing item (L717's words) | Evidence at the primary, read 10/22 | Result |
|---|---|---|
| DOE 202-26-50 lapses 23:59 10/16 UNRENEWED | DOE order page: "effective October 13, 2026, through October 16, 2026"; docket list ends with PJM's Updated Exhibit A of 10/14 1:41 PM; page `dateModified` 2026-10-14T14:44 (no edit after lapse). DOE 2026 index newest order = 202-26-50 (08:34 ET) | **MET** |
| No new PJM §202(c) | DOE 2026 index: no order numbered 202-26-51 or higher. Standing plant-specific retirement-deferral orders (202-26-40 Constellation, 202-26-25A Talen) stay outside limb 1, as at the 9/11 execution (KB-118) | **MET** (bounded to the public index) |
| No EEA-class posting 10/15–10/21 | Posting ids read one by one: **105575** Capacity Advisory (PJM-RTO, effective 10/16 09:08 → 10/19 23:59; "Advisory" priority, not EEA-class, KB-133); **105576** DOM post-contingency local load relief warning (10/16 14:10 → 10/17 00:06). Ids **105577–105640** all "no longer valid or no longer available". Dashboard shows one row (#105478, a 9/2 local warning). Independent second instrument: Inside Lines RSS feed newest operations update = "PJM Issues Capacity Advisory for Oct. 19" (10/16 18:29Z); nothing operational after it (next item 10/19 is a summit write-up) | **MET** |
| No P1 RED re-fire | Tape 10/15–10/21: 2,008 of 2,016 prints, **0 ≥ $1,000**, 0 ≥ $500; window max **$471.98 @ 08:20 10/16**. No two adjacent missing stamps, so no missing pair could hide a 2-consecutive RED run | **MET** |
| Limb 3 — Hot Weather Alert | None posted in the window | Not engaged / clear |
| No early 5→3 | Window closed 23:59 10/21; graded 08:3x ET 10/22 = first boot on/after 10/22 | Complied |

**Result: L717 MET → P1 5 → 3 executed 2026-10-22; composite 14/20 (5+3+4+2 → P1 3, P2 5, P3 4, P4 2).** Executed at the grade, not left graded-but-unexecuted (KB-118 note).

### Tape (DM2 rt_unverified_fivemin_lmps, pnode 1, pulled 08:36 ET 10/22)

| EPT date | Rows | Missing | Max $/MWh | ≥$150 | ≥$500 | ≥$1,000 | Mean | On-peak mean (HB08–23) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| 10/15 | 286 | 10:35, 22:20 | 268.62 @04:20 | 19 | 0 | 0 | 73.31 | 68.42 |
| 10/16 | 288 | — | 471.98 @08:20 | 19 | 0 | 0 | 65.34 | 59.25 |
| 10/17 | 288 | — | 387.92 @02:55 | 11 | 0 | 0 | 47.16 | 38.50 |
| 10/18 | 288 | — | 295.18 @19:10 | 9 | 0 | 0 | 32.86 | 36.19 |
| 10/19 | 288 | — | 380.98 @18:30 | 8 | 0 | 0 | 44.68 | 46.44 |
| 10/20 | 287 | 21:15 | 315.14 @08:00 | 15 | 0 | 0 | 50.96 | 40.49 |
| 10/21 | 283 | 12:05, 15:10, 15:20, 15:40, 22:00 | 257.81 @07:35 | 6 | 0 | 0 | 44.85 | 43.21 |

10/15–10/19 figures match the 10/20 pull (KB-157). Observed maxima do not certify missing stamps; the RED test is structurally unaffected (no adjacent missing pair). Today 10/22 through 08:25 EPT: latest $67.95, max $79.98 (boot).

### Outage watch fact (DM2 gen_outages_by_type, PJM RTO, pulled 08:36 ET 10/22)

| Executed | For 10/21 | 10/22 | 10/23 | 10/24 | 10/25 | 10/26 | 10/27 | 10/28 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 10/21 | 70,220 | 68,272 | 67,903 | 65,899 | 63,809 | 63,642 | 58,426 | — |
| 10/22 | — | **71,511** | 69,152 | 68,005 | 65,718 | 65,683 | 59,679 | 57,271 |

10/22 same-day: planned 48,385 · maintenance 12,698 · forced 10,428 MW. A supply snapshot with no load forecast beside it — a watch fact, not a call. EIA-930 PJM latest at boot 91,782 MW @ 10/20 22Z (97.3% of trailing 24h peak; feed ~34 h behind).

## D:L770 carried acts — done before the grade

| Act | Disposition |
|---|---|
| Reconcile dated clocks (Dec-2026 BRA among them) | All live WATT surfaces (STATUS, THESIS, TRADE, VX, NEXUS_BRIEF, KB-172) already carry **2029/30 BRA = December 2026, exact day unverified**; "mid-2027" survives only as the named correction and as the separate Cycle 3 interconnection clock. No live residue; no PROME DOCKET/GATES row carries a 2029/30 BRA date. Other clocks re-checked against STATUS's wake set: IRAS compliance ~11/8 (unadjusted), EL26-67 11/16 / 12/16, WATT-09 outer 11/30, WATT-08 2027-06-30, B1 T1 11/10–11, NERC 12/31, ERCOT 12/10 — unchanged. The 10/22 Special MC (RBP consultation, 09:00–12:00 EPT) is today and had not happened at this read — outcome unread, carried |
| Consume the PJM EEA2 9/17 correction (KB-160) | Consumed. It changes history, not this grade: the 9/26 de-escalation window was 9/19–9/25 (after 9/17) and the 9/11 execution predates it, so neither past grade moves; the 10/15–10/21 window is untouched. L717's carried flag "9/17 'no EEA-2' historical re-adjudication" is **discharged** by KB-160 (10/20). AEOLUS reconciled its side the same way (KB-AEO-208: EEA2 occurred 9/17 without a weather cause; C3 stays NOT FIRED). KILL_MEMO's obsolete "C1 never observed" sentence stays flagged, not edited (no authorized amendment) |

## D:L650 — PJM's 7/2/2026 peak, metered vs DR add-back (graded today, one day early on AEOLUS's packet)

| Basis | Figure | vs 8/2/2006 record 165,563 MW | Source / state |
|---|---:|---:|---|
| Preliminary unrestricted (DR add-back) | 168,158 MW | +2,595 | PJM OC 7/9 item 04, "Preliminary" (AEOLUS read 10/21) |
| Preliminary instantaneous metered | 162,713 MW @17:55 | −2,850 | same deck |
| **DM2 hourly metered, RTO row, HB 17:00 EPT** | **162,186.0 MW** | **−3,377** | DM2 `hrl_load_metered` 7/2, pulled 08:37 ET 10/22 by WATT; **`is_verified` = False** for the RTO row ~112 days on |
| EIA-930 hourly | ~162.6 GW | ≈ −2.96 GW | EIA Today in Energy 10/15 (AEOLUS) |

**Grade: the DR-verified figure the row waits on is NOT PUBLISHED.** AEOLUS checked OC 7/9, 8/6, 9/10, 10/8, the 10/8 Load Management Performance Report (DY 2025/26 only) and the October DR activity report; WATT closed the one leg AEOLUS could not (DM2) and found PJM's own RTO metered hour still unverified. **One figure, reconciled with AEOLUS (KB-AEO-206):** *PJM's 7/2/2026 peak set a record on PJM's preliminary unrestricted (DR-add-back) estimate only; metered load stayed below the 2006 record on every metered basis read.* KB-WATT-034's split is resolved on the available bases; its "PJM official ~early Sept" expectation is MISSED. Open: (1) unrestricted figure still preliminary; (2) 2006 comparator's DR basis unestablished, so even the unrestricted comparison may not be like-for-like. Recommendation to PROME: close L650 as graded; the residual verified-figure leg rides WATT's open set at the next P1 primary touch, no new dated wake (no monitor promised). No score depends on it.

## Inbox drain (whole inbox, every sender — 4 files)

| Item | Disposition | Record |
|---|---|---|
| AEOLUS 10/21 L650 C3 reconcile + answers | acted — L650 graded above; 10/13–14 supply attribution accepted both ways; 9/17 EEA2 leg reconciliation agrees with KB-160 | KB-175 |
| SIG-W-20261021-005 (DRAM newsroom ~20% Q4) | info-only — VULCAN's leg; no power channel | KB-176 |
| SIG-W-20261021-015 (Meta Q3: 2026 capex $135–145B, low end +$5B; FCF −$2.12B) | noted — P3 demand-side context: hyperscaler capex guide RAISED at the low end is not the P3 trigger (IPP load-growth guide RAISED or active queue >2× peak); P3 stays 4 | KB-176 |
| SIG-W-20261021-023 (AI-infra tape: SMCI pre-announce, NextDC power delay, CRWV 2031s ~79.5c) | noted — NextDC (Australia) power-supply delay is outside PJM and reported, not read; CRWV bond prices are VULCAN/LIQUID's; WATT's CoreWeave hedge share stays UNKNOWN; no score | KB-176 |

## Scores after this session

| Channel | Before | After | Forced by |
|---|---:|---:|---|
| P1 | 5 | **3** | D:L717 letter MET |
| P2 | 5 | 5 | — |
| P3 | 4 | 4 | — |
| P4 | 2 | 2 (DM2 same-vintage spark +$24.55/MWh, on-peak 10/16–10/21 $44.02 vs NG=F $2.782, 10/22 boot) | — |
| **Composite** | 16/20 | **14/20** | — |

No trade proposed or executed; no threshold, gate letter or prediction changed; $0. DM2 calls this session: 2 at boot + 3 deliberate (tape, outages, 7/2 metered load), spaced.
