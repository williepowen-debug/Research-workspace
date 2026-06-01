# BRENT CHANGELOG

Tracks all changes to THESIS.md and TIMELINE.md. Reverse chronological. Each entry documents what changed, why, and the old view to new view. This is the audit trail.

**Versioning convention:**
- THESIS: `vX.Y` — major (X) = structural thesis change (phase transition, thesis break, conviction reversal). Minor (Y) = refinement (updated levels, new evidence, threshold adjustment).
- TIMELINE: not versioned numerically — entries are dated. Events marked RESOLVED with outcomes when they pass.

---

## 2026-06-01 — PHASE 1 RE-ARMED (intra-version POV pivot; THESIS v3.0 framing inverted, no v-bump yet)

### Phase 2 PRICING dominant → PHASE 1 RE-ARMED in <24 hours on MOU suspension
**Author:** BRENT
**Action:** STATUS.md 3-chunk rewrite (header, diplomatic/kinetic sections, verdict, Path A, catalyst calendar, price dashboard, convergence matrix, two-phase thesis, KEY OPEN ITEMS, Summary for Will, POSITIONS). Per [[finding_pov_changelog_pattern]] this is an intra-version POV pivot documented here without bumping THESIS to v3.1 — the structural thesis (two-phase, kinetic-diplomatic clocks, storage-tightening, demand-destruction-lagging) is unchanged; the WHICH-CLOCK-WINS read inverted at the Mon open. A formal THESIS.md rewrite is deferred to next session pending Trump/Rubio response (which gates dead-vs-on-ice on the MOU).

**What changed:** 
- Iran (Tasnim, IRGC-aligned) announced Jun 1 SUSPENSION of indirect (Pakistan-mediated) US talks citing Israel's Lebanon incursion. Statement invokes "complete closure of Hormuz + activate Bab al-Mandab" — NEW chokepoint vector. MOU framework went rumor → "mostly agreed" → walked in <7 days.
- CENTCOM intercepted 2 Iranian ballistic missiles targeting Kuwait bases overnight Sun→Mon May 31 — second Kuwait-targeted volley in 4 days.
- Brent gapped **+4.40% to $95.13** at Monday open (from Fri $92.05 close). WTI +5.15%. Tanker complex +2.4% on war-risk re-pricing (STNG $76.33 / DHT $16.72). VG (Hormuz-LNG-arb) +6.60%, the largest mover. Natgas −3.62% — tape pricing this as oil-specific not broad energy-systemic.

**Old view (5/31, v3.0 published):** Phase 2 PRICING DOMINANT via diplomatic channel. Tape pricing near-certainty of MOU signature; flat-price asymmetry inverted in May toward $75-85 downside; kinetic gap-up was the tail risk. "Asymmetry that favored holding longs in May has inverted."

**New view (6/1):** PHASE 1 RE-ARMED. Apr-17-rhyme (LESSONS #18) resolved toward snapback. Asymmetry RE-INVERTED back toward kinetic/squeeze tail. Open question is *depth*: walkout-as-bargaining (Iran re-engages 48-72hr) caps bounce at $95-100; full collapse + Bab al-Mandab operational + Cushing floor prints $105-115. Convergence matrix recalc: **46/65 (was 42/60)** — added Bab al-Mandab 🟡 NEW vector; upgraded Brent price 🟠3→4 + Tanker 🟠3→4; Kinetic+Ceasefire 🔴5 reinforced.

**Position frame:** XLE $65C Sep 30 = now THE live scenario, not a tail (Brent +4.4% gap is what the call insures). CF $130C Jun 18 HOLD-with-pop-re-eval tested intraday — pop was modest (+1.62% vs USO +4.30%); fertilizer chain not catching the bounce. Tanker BRT-15 channel-mix-shift: original ton-mile-on-Iranian-return gate temporarily dead, but war-risk-premium channel firing — entry gating may be wrong-sided. Decisions pending Will.

**New predictions:** BRT-27 (Iran walkback within 14d, 55%), BRT-28 (Bab al-Mandab operational within 30d, 45%).

**STATUS section reference:** lines 15-34 (PHASE 1 RE-ARMED section). Predictions: thesis/PREDICTIONS.tsv BRT-07, 15, 16, 17, 21, 26 updated for Jun 1; BRT-27/28 new.

---

## 2026-06-01 — PREDICTIONS ARCHITECTURE REHAB (SAM-aligned Tier 1)

**Author:** BRENT
**Action:** Restructured BRENT predictions per SAM-style architecture. Three-chunk rehab (T1-A status renames; T1-B archive build + Notes condensation; T1-C scoreboard preamble + relocation + reference updates).

**What changed:**
- **Location:** `workbook/PREDICTIONS.tsv` → `thesis/PREDICTIONS.tsv` (sibling of THESIS.md; SAM-aligned). git mv preserved history.
- **Status nomenclature:** NOT-FIRED → FAILED for direction errors (BRT-23, BRT-24); → NOT-FIRED-PRECONDITION for unfired conditionals (BRT-20, BRT-25); CONFIRMED-MECHANISM → RESOLVED — MECHANISM-CONFIRMED / THRESHOLD-UNTESTABLE for BRT-22 (SAM-25-style split).
- **Notes condensation:** All 17 closed-row Notes condensed to ≤265 chars + `→ PREDICTIONS_ARCHIVE.md#BRT-XX` anchor links. Full blow-by-blow moved to archive.
- **Archive created:** `thesis/PREDICTIONS_ARCHIVE.md` with 17 post-mortems by Pred_ID (CONFIRMED + FAILED + NOT-FIRED-PRECONDITION + PARTIAL + RESOLVED-special + RETIRED). Reference-only, not boot-loaded.
- **Scoreboard preamble:** 26 comment lines at top of PREDICTIONS.tsv with tally, directional failures, resolved-special, calibration findings, pre-flight check.
- **2 new predictions:** BRT-27 (Iran walkback within 14d, 55%), BRT-28 (Bab al-Mandab operational within 30d, 45%).
- **Reference updates:** CLAUDE.md (2 paths + closeout discipline note for closed-row condensation), thesis/THESIS.md, handoff_WALTER/README.md.

**Calibration findings surfaced:**
- BRENT systematically **UNDER-confident** on direct-supply / chokepoint / storage predictions (BRT-06 @ 55% overshot threshold by ~2000%). Anchor 80-95% next time storage math binds.
- BRENT systematically **OVER-confident** on industrial-transmission (third-order) predictions (BRT-23 @ 70% + BRT-24 @ 65% both FAILED). Anchor 40-55% when chain has 2+ intermediating actors.
- No FAILED above 70% — high-conviction predictions are reliable.

**Cross-agent:** [[finding_threshold_vs_mechanism]] auto-memory refreshed with BRT-23 as first non-SAM case — pattern now 3-of-3 cross-agent confirmed (SAM-25, SAM-26, BRT-23). Memory edit was additive evidence, not new rule.

**Why no THESIS v-bump:** This rehab is *infrastructure/process* (how BRENT tracks predictions), not thesis content. THESIS.md untouched.

---

### THESIS v2.0 → v3.0 — Regime shift: Phase 2 arrived via the diplomatic/supply-relief channel
**Author:** BRENT
**Action:** Major rewrite. v2.0 (May 6) framed "Phase 1 DEEPENING, Conviction HIGH on Phase 1 longs." Over the following 25 days the flat price decoupled from the physical squeeze on diplomatic-relief pricing: Brent $116.55 (May 5 peak) → $92.05 (May 29), −19% on the month (worst since Mar 2020), −21% from peak. This is a phase-transition-in-pricing + a flat-price conviction reversal — both qualify for a major (X) bump per the versioning convention.

**What changed (7 numbered items):**

1. **Phase 2 PRICING has arrived — via SUPPLY RELIEF (diplomacy), not demand destruction.** A 60-day US-Iran MOU ("mostly agreed": Hormuz reopens, mines cleared, US lifts blockade + sanctions waivers) drove the −21% move as the market priced Iranian barrels returning seaborne.
   - Old view (v2.0): Phase 2 "more remote than 24hr ago"; Path A 1/4 partial, prob 10%
   - New view: Phase 2 is what the tape is pricing; Path A prob raised to ~40%. The demand-destruction path (Path B) is NOT the channel — supply relief is.

2. **Flat-price conviction REVERSED to cautious-neutral.** The v2.0 "HIGH on Phase 1 longs, kinetic gap-up is the live risk" call is retired.
   - Old view: hold Phase 1 longs; paper relief is a slow grind, kinetic event is the gap risk
   - New view: position the binary — signature → $75-85; collapse/kinetic → $100+. No new flat-price longs. Cleanest expression = tanker ton-mile (BRT-15) + XLE gap-up insurance, not flat-price longs.

3. **LESSONS #18 is now the central discipline — the Apr 17 false-reopening rhyme, louder.** The reopening is PRICED but NOT operational: deal unsigned and fraying on all terms (Iran/Fars contradicts uranium, no-tolls, adds a $12B frozen-asset precondition); Trump "not to rush"; Rubio floating military "Plan B"; physical strait trickle-flow (~10 vessels/day; UBS "little evidence" of improvement); kinetic continued through the peace week (US strikes May 25-26, Iranian missiles at Kuwait + drones at strait).
   - Old view: Path A 4-hour exit on fire; gates mostly moving away
   - New view: gates are the live scorecard; tape is pricing ahead of all of them; snapback ($100+) is the re-widened tail, not just a 10% risk

4. **Storage is now the truest Phase-1 read — and it screams the OPPOSITE of price.** Cushing −2.794M (week May 22) → ~23.0M = biggest single-week draw since Aug 2023; 20M floor ~early-mid June. SPR 365.1M (−9.1M; lowest since Apr 2024); ~350M floor ~1.5-2 wks. The physical squeeze is intensifying even as flat price falls.
   - Old view (v2.0): Cushing 29.8M, ~12-week trajectory; SPR release "failed to dent tape"
   - New view: Cushing draw accelerated ~2× and is weeks (not months) from the operational floor — a WTI-dislocation / kinetic-resolution forcing function independent of the deal

5. **BRT-04 (shale non-response) downgraded 75% → ~60%; RED-19 FALSIFIED.** Rigs 429 (May 29; +22 from 407 trough; 7 consec weekly gains; >415 upper bound). RED's own prediction (rigs 400-415 through Jun) falsified, confirming the BRT-04 downgrade direction.
   - Old view (v2.0): BRT-04 75%, "first weakness" (FANG/COP)
   - New view: shale response is a persistent uptrend; capex AND rig-count layers both creeping; BRT-04 materially weakened

6. **Demand destruction still NOT visible — Path B is the dog that didn't bark.** Gasoline +0.5% YoY (May 15); the anticipated first-negative print didn't materialize; util ramped to 94.5% (summer driving). Only Trigger #1 (curve <$3) is at/near firing; Trigger #3 fired May 5 then reversed (May 26 COT due Jun 5 is the re-fire watch).
   - Old view: Path B 0/3, first clean signal window May 7+
   - New view: Path B 1/3; demand inelastic so far; Phase 2 is arriving on the supply axis ahead of the demand axis

7. **LIAISON/BOARD/FLOW infra detail collapsed out of THESIS** per messaging-system-overhaul direction. `demand_destruction/TRACKER.md` named as the operational dashboard (kept current through May 29 while STATUS lagged).
   - Old view (v2.0): heavy LIAISON architectural layer in-thesis (FORMAT_SPEC, BURST_WINDOW, enums, dispatch lists)
   - New view: thesis carries thesis; messaging infra lives in its own files and is being replaced

**Provenance:**
- STATUS refreshes: May 20 (Phase 1 contested), May 31 (Phase 2 pricing dominant + weekend deal-fray sweep)
- demand_destruction/TRACKER.md + data files (May 22/25/27/29) — operational dashboard, current
- Weekend news sweep May 31: Axios/PBS/The Hill (MOU terms), CNBC (Brent $92.05, −19% month), Fars via Iran Intl/Al Jazeera (Iran contradicts terms, $12B), CNN (Hegseth combat-ready; Kuwait missiles), CNBC (Trump "not to rush"; Rubio "Plan B")
- RED CHG-RED-024 closure (RESOLVED-CONVERGED-SILENT); RED-19 falsification noted
- HAWK routing May 22 ("armed pause / controlled grind")

**Cache refresh trigger:** v2.0 → v3.0 version-string change. (LIAISON dual-trigger cache mechanism deprecated per messaging-overhaul; noted for audit continuity only.)

---

## 2026-05-06 — THESIS v2.0 (Major version bump — Project Freedom + bypass-pair + BRT-04 weakness + LIAISON layer)

### THESIS v1.1 → v2.0 — Structural deepening + architectural integration
**Author:** BRENT
**Action:** Comprehensive rewrite reflecting May 4-5 structural changes since v1.1 (Apr 16). Triggers a `design/CROSS_REFS/BRENT.md` cache refresh on WALTER's side per LIAISON Turn 3 Q6 dual-trigger mechanism (THESIS.md version-string changed).

**What changed (8 numbered items):**

1. **Project Freedom narrow channel (May 4)** — US Navy escort active 100+ aircraft / 15K personnel; >1,500 vessels still trapped per CENTCOM; commercial transit NOT restored, only US-flagged. Replaces v1.1 "naval blockade active" framing — escort is a different kinetic posture than blockade, with different supply implications.
   - Old view: US naval blockade = full supply lockdown
   - New view: US-flagged narrow channel + ongoing kinetic events on non-US-flagged commercial; bypass-route security premium repricing across structure

2. **Bypass-pair pattern confirmed** — Iran systematically targeting BOTH workaround corridors: Petroline (Apr 9 drone-hit) + Fujairah (May 4). Bypass-route security now structural risk, not just Strait-specific.
   - Old view: bypass routes "impaired" but available as fallback
   - New view: bypass routes are themselves contested kinetic targets; cannot be assumed available in resolution scenarios

3. **Day-2 UAE strikes (May 5) + admin "ceasefire not over" framing** — Iran attacked UAE 2 consecutive days; admin holding Apr 8 ceasefire framing for War Powers Resolution reasons. Diplomatic narrative diverges from kinetic reality. STATUS retro-tagged with `BRENT-placeholder-narrative pending REQ-NEXUS-20260505` per LIAISON Q3 substance-vs-narrative line.
   - Old view: Apr 8 ceasefire = pre-blockade equilibrium
   - New view: Ceasefire kinetically broken; admin framing is War Powers Resolution legal cover, not kinetic reality

4. **172M SPR + 400M IEA coordinated release failed to dent tape (running since Mar 11)** — strong squeeze confirmation; Hormuz outage is structurally larger than coordinated paper supply can offset.
   - Old view (v1.1): "SPR 409.2M bbl, no large release despite crisis. Policy tools constrained."
   - New view: largest coordinated release in IEA history is RUNNING, and failed to bend the curve. Confirms Phase 1 outage is structurally larger than any sustainable reserve drawdown.

5. **BRT-04 first weakness (May 4) — FANG + ConocoPhillips capex break** — FANG raised oil guide 510 → 520+ MBO/d, capex $3.75B → $3.9B; COP raised CapEx + adding Permian rig H2. **First major Permian operator broke capital discipline.** BRT-04 confidence downgraded 95% → 75%. Earnings season runs May; if 2-3 more break, BRT-04 materially weakened — Phase 2 supply-side path opens earlier than expected.
   - Old view (v1.1): "BRT-04 upgraded 95%" — shale non-response confirmed
   - New view: rigs still 408 (May 1, new low) but capex layer cracking — rig count proxy alone insufficient; watch CXO/OXY/EOG/MRO Q1 calls

6. **Curve structure as new analytical dimension (NEW v2.0)** — Spot $108-116 vs Dec26 $80 vs Jun27 $76. Back end pricing "severe but temporary." Tempers v1.1's implicit sustained-high duration view. Drives curve-aware sizing rule (don't initiate beyond Sep without explicit duration thesis).
   - Old view (v1.1): no curve-structure analysis
   - New view: positioning beyond ~6mo fights the curve; XLE Sep $65C is right window

7. **Position view refresh** — v1.1 carried USO 2 shares (+42.7%) and STNG 2 shares (+6.2%). STATUS confirms book is now XLE Sep $65C (2x) + CF Jun $130C (1x); USO $120C May 1 closed +$1,700; **no USO/STNG/DHT shares on book**. Tanker thesis BRT-15 has no current equity expression.
   - Old view (v1.1): USO+STNG shares + USO call expressions
   - New view: longer-dated XLE call (energy beta, 5mo expiry) + CF (sulphur/nitrogen adjacent, 6wk); cash from USO call realization

8. **LIAISON architectural layer integration (NEW v2.0)** — BRENT participates in 3-way joint proposal with CARL+WALTER. New protocol elements:
   - FORMAT_SPEC v0.8 cosign (4 fields: consumer_transmission + signal_role + consumer_lens + cluster_secondary)
   - lng_substitution enum addition (BRENT contribution)
   - BRENT-IMMEDIATE 8-threshold dispatch list (Q4)
   - BURST_WINDOW_OPEN protocol for Phase 2 trigger events (Q5)
   - energy_transmission + regime_state v0.9 candidate enums (Q11; separate Will-surface from v0.8)
   - 47-signal back-disposition pass complete (commit bf8c2c9e); 5 Post_Hoc_Conf deltas surfaced for WALTER calibration
   - FLOW.tsv outbound expansion (5 new rows + FLOW-BRT-02 refresh; commit 1a3c691c)
   - Substance/narrative line: workbook-citable = authoritative; cross-cluster narrative = pending-NEXUS placeholder

**Provenance:**
- STATUS refreshes: Apr 17 (Hormuz reopen retracted), Apr 29 (Brent +$4 d/d clean threshold), May 4 (Project Freedom Day 1), May 5 (Day-2 UAE + post-dig findings)
- LIAISON Turns 1-3 (`AGENTS/BRENT/handoff_WALTER/LIAISON.md`)
- Commits: 707a2f79 (channel + Turns 1-3 + STATUS retro-tag), bf8c2c9e (back-disposition), 8f2331f1 (joint proposal sections), 1a3c691c (FLOW.tsv expansion)
- BOARD signals integrated: 47 unique signals Apr 14 → May 5 (per `board/BOARD_LOG.tsv`)

**Cache refresh trigger:** v1.1 → v2.0 version-string change fires WALTER's `design/CROSS_REFS/BRENT.md` cache refresh per LIAISON Q6 dual-trigger mechanism. WALTER picks up updated FLOW.tsv outbound paths, refreshed PREDICTIONS.tsv statuses, and v2.0 thesis structure on next dispatch cycle.

---

## 2026-04-07 — INITIAL CREATION (THESIS v1.0)

### THESIS v1.0 — Established
**Author:** BRENT + Will
**Action:** Extracted and formalized standalone thesis from STATUS.md, PREDICTIONS.tsv (25 entries), VX.tsv (13 vectors), LESSONS.md (17 lessons), PHASE2_SHORT_PLAYBOOK, and demand_destruction/ research.

**Core thesis (v1.0):** Two-phase oil crisis. Phase 1 (supply squeeze) is active and deepening on Day 39 with ~9-11M bpd disrupted, physical Brent at $141, SPR exhausted. Phase 2 (demand destruction / OPEC+ unwind) not yet visible in data — earliest summer 2026. Alpha is in the sequencing.

**Structure defined:**
1. Two phases with entry/exit criteria for each
2. Four transmission channels (supply→price, price→consumer, price→inflation, supply chain)
3. Two exit protocols (PATH A binary resolution, PATH B gradual demand destruction)
4. Phase 2 confirmation rule (3 signals x3 readings = top 4-6 weeks away)
5. Short playbook reference (bear put spreads, not outright puts at 100th IV percentile)

**Position view:** USO 2 shares (+42.7%), STNG 2 shares (+6.2%). USO $118C closed +$534.83.

**Key thresholds:** 11 thresholds defined. 5 currently breached (Brent >$100, gas >$4, VLCC >WS200, dated-futures >$20, Brent >$100 Scenario C).

**Conviction:** HIGH

---

### TIMELINE v1 — Established
**Author:** BRENT + Will
**Action:** Created forward-looking expected progression from STATUS.md catalyst tracking, ECON_CALENDAR.md, and demand_destruction/TRACKER.md.

**Key branch points defined:**
- Apr 7 8PM ET: Trump Hormuz deadline (THE binary event)
- Apr 9: EIA weekly petroleum (first post-Kharg data)
- Apr 11: Baker Hughes rig count
- Apr 15: Feb TIC data (Japan UST flows — cross-agent with SAM)
- Weekly: EIA petroleum status, demand destruction indicator tracking
- June 7: Next OPEC+ meeting
- Ongoing: Phase 2 leading indicator monitoring (airline cuts, ATA tonnage, M1-M3 structure)

---

## PRIOR THESIS EVOLUTION (reconstructed)

These entries are reconstructed from git history and research outputs to establish the audit trail pre-CHANGELOG.

### ~2026-02-18 — THESIS SEEDED (Pre-war)
**What changed:** Initial oil thesis established around Hormuz risk. HAWK provided military scenario framework (A/B/C/D).
**Old view:** Standard oil supply monitoring
**New view:** Two-phase thesis framework created: Phase 1 squeeze → Phase 2 destruction/unwind

### ~2026-03-01 — WAR BEGINS / HORMUZ CLOSED
**What changed:** Iran-Israel/US war breaks out. Hormuz closed and mined. Phase 1 activates immediately.
**Old view:** Hormuz closure was a scenario to model
**New view:** Hormuz closure is reality. Gulf producers begin filling storage. Price surge underway.

### ~2026-03-06 — MAJOR RESEARCH BUILDOUT (Batches 1-3)
**What changed:** Comprehensive data ingestion. 25 predictions created. 13 vectors established. OPEC+ spare capacity verified (4.35M bpd true, 90% trapped). US shale non-response confirmed. HY energy credit benchmarked. Sulphur/copper chain and Taiwan LNG/semiconductor chains discovered.
**Old view:** Directional thesis with rough estimates
**New view:** Quantified thesis with sourced data, formal predictions, and cross-domain supply chain analysis

### ~2026-03-07 — SUPPLY CHAIN EXTENSIONS
**What changed:** Sulphur chain (Gulf → DRC copper), Taiwan LNG/semiconductor, and Iran food stress vectors added. Expanded BRENT's scope beyond crude oil into second/third-order supply chain effects.
**Old view:** Oil-centric thesis
**New view:** Multi-commodity supply chain thesis with semiconductor and agricultural dimensions

### ~2026-03-08 — GULF STORAGE CRISIS MODELED
**What changed:** Day-by-day storage models for Kuwait, UAE, Iraq, Qatar. Curtailment dates predicted.
**Old view:** "Gulf storage is filling" (qualitative)
**New view:** Kuwait tank tops ~Mar 20. UAE ~Mar 31. Iraq weeks behind. Quantified timeline.

### ~2026-03-15 — PHASE 2 FRAMEWORK ESTABLISHED
**What changed:** Demand destruction research completed (HAMILTON.md, ANALOGS.md, TRACKER.md). Phase 2 short playbook written. Exit protocols formalized.
**Old view:** "Phase 2 happens eventually"
**New view:** Phase 2 has specific leading indicators, a confirmation rule (3 signals x3 readings), and a short playbook (bear put spreads). Minimum 20-24 weeks to -5% YoY gasoline.

### ~2026-03-20 — DATED BRENT PHYSICAL CRISIS
**What changed:** Dated Brent physical premium emerged (~$20+ over futures). North Sea all-bid, no-offer.
**Old view:** Futures price tells the story
**New view:** Physical market is in a separate, more severe crisis. Dated-futures spread is the true scarcity signal.

### ~2026-03-27 — SPR FAILURE / POLICY EXHAUSTION
**What changed:** 400M bbl SPR release (largest ever) fails to contain prices. Brent $107 post-release.
**Old view:** Government has policy tools to dampen Phase 1
**New view:** Policy tools exhausted. Market is on its own. Phase 1 ceiling removed.

### ~2026-04-01 — OPEC+ SYMBOLIC / KHARG THREAT EMERGES
**What changed:** OPEC+ Apr 5 meeting produced symbolic "paper" increase only. Kharg Island emerged as military target.
**Old view:** OPEC+ might respond with real supply
**New view:** OPEC+ response is cosmetic. Real supply decisions are military, not economic.

### ~2026-04-06/07 — IRAN EXPORT INFRA UNDER ATTACK
**What changed:** Kharg Island struck (90% Iran exports). South Pars struck. Ceasefire rejected. Trump 8PM deadline set. Iran threatens to target regional oil infra.
**Old view:** War was about Hormuz chokepoint control
**New view:** War is now destroying Iran's own export capacity. Iran may retaliate against Saudi/UAE facilities. Phase 1 has no ceiling until resolution.

---

*Future entries: Add above the PRIOR section. Include: date, which doc changed, what changed, why, old view to new view. Tag THESIS changes with version number.*
