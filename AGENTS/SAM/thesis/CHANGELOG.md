# SAM CHANGELOG

Tracks all changes to THESIS.md and TIMELINE.md. Reverse chronological. Each entry documents what changed, why, and the old → new view. This is the audit trail.

**Versioning convention:**
- THESIS: `vX.Y` — major (X) = structural thesis change (new channel, thesis break, conviction reversal). Minor (Y) = refinement (updated probability, new evidence for existing view, threshold adjustment).
- TIMELINE: not versioned numerically — entries are dated. Events are marked RESOLVED with outcomes when they pass.

---

## 2026-04-02 — TRUMP REVERSAL + WEAK 10Y AUCTION + SAM-06 RESOLVED

### PREDICTION Resolved: SAM-06
**Author:** SAM
**Prediction:** "Life insurers announce more JGB selling" (75% confidence, Q1 2026)
**Result:** CONFIRMED — TRUE
**Evidence:** Fukoku Mutual stopped buying 30Y/40Y JGBs (Jan 2026, first to break). Nippon Life realized ¥220B JGB losses (active selling, not paper). Feb MOF data showed ¥3.42T foreign bond selling — largest since Oct 2024. Multiple independent confirmations across Q1.
**Calibration note:** 75% confidence on a TRUE outcome — well-calibrated.

### TIMELINE Updated
**Author:** SAM
**Action:** Marked Apr 2 RESOLVED (10Y auction + Trump speech). Updated Apr 6 assessment. Added to branch point table.

**What changed:**
1. **10Y JGB auction RESOLVED — WEAK.** BTC 2.56x (well below 12mo avg 3.24), tail 0.36 (widest since Aug 2024). Coupon 2.4% (28-year high). Not a failure but a clear warning for Apr 7 30Y.
2. **Trump speech REVERSED de-escalation.** No exit plan, no Hormuz reopening. Brent surged $102→$109. De-escalation probability dropped to ~25-30% (was 40-50%).
3. **Phase 1 dynamics reasserting.** USD/JPY back to 159.68. Oil up = yen weak. MOF intervention risk re-engaging.
4. **Apr 6 branch point updated.** Bear fork (strikes resume) now more likely after Trump speech.

**Old view:** De-escalation possibly emerging, oil headwind lifting, smooth policy path. 10Y auction routine.
**New view:** De-escalation crumbling, oil back as headwind, Phase 1 reasserting. 10Y auction weak = Apr 7 30Y now THE critical event. Path to FXY target bumpier but destination unchanged.

**Note on THESIS:** No version bump. Thesis structure unchanged — all 3 channels intact. What changed is PATH (bumpier) not DESTINATION. April BOJ hike prob slight downgrade (45-50% → 40-45%) on renewed "uncertainty" excuse. May unchanged.

### NEW FILES CREATED
**Author:** SAM + Will
1. **STRATEGY.md** — Decision playbook at SAM root. When to add/hold/exit FXY, vol signals mapped to position decisions, 5-stage trade framework, asymmetry table. Not part of boot — read when position decisions are on the table.
2. **research/outputs/VOL_OPTIONS_FRAMEWORK.md** — Full technical reference for vol/options monitoring. CME CVOL (JPVL) regimes, UpVar/DnVar decomposition, FXY OI structure, USD/JPY risk reversal interpretation, convergence signal logic, traffic light dashboard. Source: Perplexity deep research, validated by SAM.
3. **4 new workbook vectors** (VX-SAM-12.00 through 12.03) — vol convergence signal, CVOL, FXY P/C OI, risk reversals. All marked MANUAL UPDATE REQUIRED.

### PROCESS IMPROVEMENT
**Author:** SAM + Will
**Action:** Boot process audit and 6 structural fixes to CLAUDE.md:
1. Boot order changed: THESIS → STATUS → CALENDAR → TIMELINE → MEMORY (was MEMORY first)
2. Market refresh step added (step 7) — fetch live prices before analysis
3. Doc ownership rules added — prevents STATUS/TIMELINE/MEMORY redundancy
4. Session notes template added (CHANGES SINCE / LAST SESSION / NEXT SESSION)
5. PREDICTIONS.tsv added to boot sequence (step 6)
6. STATUS.md trimmed ~34 lines of narrative that duplicated TIMELINE

---

## 2026-04-01 — TANKAN RESOLVED (BULL FORK) + OIL CRASH + TIMELINE EXPANSION

### TIMELINE Updated
**Author:** SAM
**Action:** Major update — marked 2 events RESOLVED, added 5 new branch points, added oil de-escalation scenario.

**What changed:**
1. **Tankan RESOLVED — BULL FORK.** Large mfg 17 (beat cons 16), non-mfg 36 (beat cons 33), biz inflation expectations 2.6% (above BOJ 2% target). April 23-24 hike probability: ~45-50% (up from ~35%).
2. **FY-end RESOLVED.** No outsized flows. Window closed.
3. **Oil crash added.** Trump ceasefire talk → Brent ~$102 (from $115). De-escalation fragile — Iran rejected 15-point plan. Apr 6 strike pause expiry added as branch point.
4. **JGB auctions added.** Apr 7 (30Y) and Apr 14 (20Y) — not in original TIMELINE. These are cross-agent 🔴 triggers if BTC <2.0x.
5. **New tail scenario: oil de-escalation (25%).** War ends → Brent $80-90 → yen strengthens on fundamentals → FXY target faster with less volatility. Reduced "oil dominates" from 20% → 15%.
6. **Branch point table expanded** from 7 to 10 entries, with status tracking column added.

**Old view:** 7 branch points, Tankan pending, no auction dates, oil $115 headwind active
**New view:** 10 branch points, Tankan resolved bull, auctions tracked, oil headwind possibly lifting, de-escalation path emerging

**Note on THESIS:** No version bump. Thesis structure unchanged — all 3 channels intact, conviction HIGH. The shift is in TIMING (accelerating) and RISK CHARACTER (crisis → policy-driven). If April hike probability exceeds 60% or oil de-escalation firms up, consider v1.1 to update probabilities.

---

## 2026-03-31 — MIMURA ESCALATION + MARKET PRICING UPDATE

### TIMELINE Updated
**Author:** PROME
**Action:** Updated "Mon Mar 31" section with Mimura "decisive measures" escalation and market pricing shift.

**What changed:**
- Mimura (top currency diplomat) used "decisive measures" — strongest verbal signal this cycle, first time this language. Final step before actual USD-selling.
- Ueda coordinated messaging: "keeping close eye on yen moves." MOF-BOJ alignment is the pattern that precedes intervention (same as July 2024 sequence).
- Market now pricing 65% May hike to **1.00%** (above our prior base case of 0.75%). Equiti: oil above $110 could force emergency April move.

**Old view:** MOF intervention "still on alert" based on Katayama warning at 159.5
**New view:** Mimura escalation = intervention is the NEXT step, not a possibility. Verbal sequence complete.

**KB entries added:** KB-SAM-157 (Mimura), KB-SAM-158 (Ueda-Mimura coordination), KB-SAM-159 (65% May 1.00% pricing)

**Note on THESIS:** No version bump — intervention was already tracked in THESIS v1.0. This is confirming evidence, not a structural change. If market pricing of 1.00% holds and our terminal rate view needs revising from 0.75%, that would warrant v1.1.

---

## 2026-03-31 — INITIAL CREATION

### THESIS v1.0 — Established
**Author:** PROME + Will
**Action:** Extracted and synthesized standalone thesis from STATUS.md, KB (156 entries), Deep Dive, Mortgage Bomb analysis, and RP-SAM-4.

**Core thesis (v1.0):** Multi-channel convergence — BOJ forced to hike into oil shock while life insurers exit USTs and carry trades hit record crowding. All paths lead to yen appreciation and carry unwind within 60 days.

**Three channels defined:**
1. Life insurer repatriation (ESR regime change makes losses visible → forced UST selling)
2. Carry unwind (85% 7d / 97% 30d; CFTC shorts tripled; intervention paradox)
3. BOJ policy divergence (0.75% political ceiling from floating mortgage constraint)

**Independent catalyst added:** Fed cut path via private credit cascade (HANS/BROCK)

**Position view:** FXY long, 4 shares starter, entry decision card issued Mar 27 at USD/JPY 160.

**Conviction:** HIGH

---

### TIMELINE v1 — Established
**Author:** PROME + Will
**Action:** Created forward-looking expected progression from research, KB, and STATUS.md.

**Key branch points defined:**
- Apr 1: Tankan (strong → April hike live; weak → May only)
- Apr 15: Feb TIC data (large selling → thesis confirmed; mixed → slower)
- Apr 23-24: BOJ meeting (hike → carry unwind fires; hold → wait May 1)
- May 1: BOJ meeting (BASE CASE HIKE)
- Mid-May: ESR disclosures (first real MTM damage visible)
- Late May: April CPI (oil shock + SK disruption reflected)
- June: Sato joins board (hawk→dove swap), Takaichi-Ueda collision window

**Horizon:** Through Q3 2026

---

## PRIOR THESIS EVOLUTION (reconstructed from research history)

These entries are reconstructed from git history and research outputs to establish the audit trail pre-CHANGELOG. Not as detailed as future entries will be.

### ~2026-02-08 — Channel 1 Established (Life Insurer Deep Dive)
**What changed:** First comprehensive mapping of Japan life insurer → UST transmission mechanism. Quantified Big 4 exposure, built scenario framework (base/stress/crisis), identified ESR as binding constraint.
**Old view:** "Japan might sell Treasuries" (vague, headline-level)
**New view:** Specific mechanism with quantified flows ($80-500B range), identified actors (Meiji most vulnerable), defined triggers (ESR thresholds, auction failures)

### ~2026-02-12 — Channel 3 Reshaped (Floating Mortgage Bomb)
**What changed:** Discovered 75% floating rate mortgage structure. Identified hard political ceiling on BOJ at 0.75%.
**Old view:** BOJ terminal rate 1.25-1.5% (market consensus); Takaichi-Ueda collision "possible"
**New view:** Terminal rate 0.75% (political ceiling); collision "inevitable"; D2 (YCC return) probability 30-35% → 32-40%

### ~2026-02-22 — Channel 1 Deepened (RP-SAM-4)
**What changed:** ESR regime change quantified (SMR 933% → ESR 219%). Hedged UST returns confirmed negative vs JGBs. Individual insurer hedge ratios mapped.
**Old view:** Repatriation thesis directionally correct but timing uncertain
**New view:** Timing anchored to April 2025 ESR implementation + FY-end March 2026 disclosures

### ~2026-03-17 — Oil-in-Yen Structural Added (SK Refiner Crisis)
**What changed:** SK refiner feedstock crisis tracked. Run cuts confirmed 12 days ahead of initial April 7 estimate. Force majeure declared.
**Old view:** Oil impact on Japan = generic "energy importer" narrative
**New view:** Specific transmission: SK cuts → Asia-Pacific product shortage → Japan CPI upward surprise → BOJ hike MORE urgent. Two-phase yen dynamic (weak then strong).

### ~2026-03-24 — Independent Catalyst Added (HANS/BROCK Fed Path)
**What changed:** Private credit cascade signal from HANS. 9 funds gated (APO, ARES). Fed cut path identified as independent carry unwind trigger.
**Old view:** Carry unwind requires BOJ action or intervention
**New view:** USD/JPY sub-145 possible on U.S. credit deterioration alone, without BOJ

### ~2026-03-27 — Entry Decision Issued (USD/JPY 160 Breach)
**What changed:** USD/JPY breached 160.106. Intervention paradox formalized. FXY entry decision card issued.
**Old view:** Waiting for catalyst hierarchy (BOJ > oil resolution > intervention > repatriation)
**New view:** Buy now in tranches. Oil scenario analysis shows FXY wins in all 3 scenarios. Asymmetric setup.

### ~2026-03-30 — BOJ Summary of Opinions + Board Stacking
**What changed:** Most hawkish Summary of Opinions in normalization cycle. Takata dissented for 1.00%. "Raise without hesitation" language. Separately, Takaichi nominated 2 dovish academics to board.
**Old view:** BOJ debate is "when to hike"
**New view:** BOJ debate is "how much to hike." But medium-term political risk rising — dovish majority forming by 2027.

---

*Future entries: Add below the most recent dated entry, above the PRIOR section. Include: date, which doc changed, what changed, why, old view → new view. Tag THESIS changes with version number.*
