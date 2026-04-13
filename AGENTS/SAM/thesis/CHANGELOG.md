# SAM CHANGELOG

Tracks all changes to THESIS.md and TIMELINE.md. Reverse chronological. Each entry documents what changed, why, and the old → new view. This is the audit trail.

**Versioning convention:**
- THESIS: `vX.Y` — major (X) = structural thesis change (new channel, thesis break, conviction reversal). Minor (Y) = refinement (updated probability, new evidence for existing view, threshold adjustment).
- TIMELINE: not versioned numerically — entries are dated. Events are marked RESOLVED with outcomes when they pass.

---

## 2026-04-12 — HOUSEKEEPING: THESIS data sync + cross-file pruning

**Author:** SAM
**Action:** Synced stale THESIS.md fields to match current STATUS.md. No thesis-level change — this is a data freshness pass, not a view change. Also pruned stale content across CALENDAR, TIMELINE, MEMORY, and STATUS per doc ownership rules.

**THESIS.md changes (still v1.2, no version bump):**
- Header: `v1.0` → `v1.2` (header hadn't been updated with version field)
- Last Updated: Apr 5 → Apr 12
- Carry unwind 7d: 85% → 68% (oil headwind); 30d: 97% → 93%
- CFTC shorts: -67,800 (38%) → -93,742 (52%) — was one release stale
- Brent: ~$115 → ~$97 (post-ceasefire, blockade)
- Position: 4 shares → 8 shares (Tranche 1 was executed)
- BOJ trigger date: Apr 23-24 → Apr 28
- Catalyst sequence: removed 3 passed dates (Mar 31, Apr 1, Early Apr), added Apr 16 MOF + Apr 22 ceasefire expiry
- JGB 10Y threshold: BREACHED → NEAR (MOF Apr 9: 2.397%, 1.3bp below)
- Brent threshold: $115 → $97

**TIMELINE.md:** Fixed week labels (THIS WEEK/WEEK 2 → RESOLVED), Apr 23-24 → Apr 28, scenario rates updated from 0.75%/1.00% to 1.00%/1.25% (rate is already AT 0.75%).

**CALENDAR.md:** Pruned resolved Apr 7-11 week, migrated insurer plans to Apr 14 section.

**MEMORY.md:** Removed 5 script implementation findings (now baked into `scripts/` toolkit), trimmed stale MHLW date reference, updated References cross-link.

**STATUS.md:** Replaced 25-line narrative block with 2-line summary (narrative lives in TIMELINE per doc ownership), simplified carry unwind table (removed stale comparison column).

---

## 2026-04-11 — DATA ACCURACY AUDIT (STATUS refresh, no THESIS version bump)

### STATUS.md data corrections
**Author:** SAM
**Action:** First run of new SAM automation toolkit (`AGENTS/SAM/scripts/`) surfaced multiple data discrepancies between STATUS.md and authoritative sources. STATUS.md refreshed; THESIS.md version held at v1.2. Scenario weights unchanged pending Apr 16 MOF confirmation.

**What changed (STATUS only, not THESIS):**
1. **CFTC JPY non-commercial net: -72.9K → -93,742.** Prior STATUS was reading the Mar 31 CFTC release. The Apr 7 snapshot (released Fri Apr 10) shows shorts built +17K WoW. Now at 52.1% of Jul 2024 peak (was 38%). Source: `cftc.gov/dea/newcot/deafut.txt` parsed via `scripts/cftc_jpy.py`.
2. **JGB yields reconciled to MOF authoritative CSV.** STATUS had cited 10Y 2.41% / 40Y 3.92% for Apr 10. MOF `jgbcme.csv` through Apr 9 shows 10Y 2.397%, 40Y 3.678%; April peak was 10Y 2.429% / 40Y 3.747% (Apr 6). The 40Y 3.92% figure is 17bp above the MOF April peak and could not be reconciled — flagged as likely prior-session data source error. Apr 10 MOF data publishes Mon Apr 13. Until then STATUS uses MOF Apr 9 as baseline. 10Y NOT breached 2.40% stress threshold as previously claimed — actually sits 1.3bp below.
3. **MOF ITS weekly flow data refreshed.** Prior STATUS: "¥2,215.8B / 3 weeks, 2x base case." Corrected via `mof_flows.py` parsing 1,109-row history: 4-week rolling ¥-5.0T (~$-33B, $36B/mo run rate), squarely in THESIS Channel 1 stress-case range ($25-40B/mo). Latest single week (Mar 29-Apr 4) was ¥-2.46T — 2.5× prior weeks, by far the worst. Alert upgraded 🟡 → 🟠.
4. **FXY options positioning added to STATUS reference section.** Not a data correction — net-new visibility. Aggregate P/C 0.06x, 83.9% of call OI in $58-65 thesis zone, 19,014 Jun 18 $58 calls single-strike concentration.

**What did NOT change (intentional restraint):**
- Channel 1 scenario weights (Base 70% / Stress 25% / Crisis 5%). 4-week rolling is stress case but 12-week rolling is still base/stress boundary. One extreme week (Mar 29-Apr 4) is not enough to rebalance from the 70%-weighted base case. Will approved Option B (STATUS refresh + LIQUID signal) explicitly over Option C (scenario rebalance).
- THESIS version — this is a data audit, not a thesis change.
- Carry unwind probabilities (bumped 30d 90→92, 60d 95→96 in STATUS reflecting CFTC crowding + MOF flows; minor refinement not a thesis restructure).

**Signal sent:** 🟠 to LIQUID via `outbox/2026-04-11_to-LIQUID_mof-flows-stress-case-pace.md` — MOF stress-case pace + CFTC crowding + correction to prior understating.

**Decision gate:** Apr 16 MOF ITS release is decisive. If next week confirms another ¥2T+ weekly LT-debt outflow → rebalance to Option C (Base 70→55, Stress 25→37, Crisis 5→8) and bump THESIS to v1.3. If Mar 29-Apr 4 was a one-off → no thesis change.

**Source:** New SAM automation toolkit built today. Reference: `AGENTS/SAM/scripts/AUTOMATION_PLAN.md`, commits c44da1a1 / 5ed7bbfc / fe4628ad.

---

## 2026-04-05 — NORINCHUKIN RESEARCH + HEDGE RATIO COLLAPSE (THESIS v1.2)

### THESIS v1.1 → v1.2 (minor)
**Author:** SAM
**Action:** Integrated Norinchukin CLO contagion research. Added hedge ratio data, institutional exposure framing, GPIF non-risk finding, new thresholds.

**What changed:**
1. **Life insurer hedge ratio: 44.4% (Mar 2025) — 14-year low.** ~55% of foreign bonds ($370-550B) unhedged. Avg FX entry for unhedged: USD/JPY 135-145. Critical forced-selling threshold: below 130-135. This quantifies the exposure we knew existed but hadn't measured.
2. **Total institutional foreign portfolio: ~$3.0-3.5T.** Japan holds $1,185.5B in USTs (Dec 2025). Frames the larger pool beyond our $450-810B life insurer estimate.
3. **Norinchukin shrinking CLO book.** World's largest CLO investor (¥9.7T/$65B, 100% AAA). Reduced ¥500B in Q1 2026 — "fastest decline on record." Not forced selling yet but directional.
4. **GPIF confirmed NOT a forced-selling risk.** ±6-7% deviation bands cushion yen moves. Rebalances by BUYING foreign assets on yen appreciation. Through FY2029.
5. **New threshold added:** USD/JPY 130-135 (insurer forced systematic selling).
6. **Cross-agent link to LIQUID updated** with hedge ratio + UST holdings data.
7. **Outbox signal written** for LIQUID: hedge ratio collapse + Norinchukin + repatriation framing.

**Old view:** Channel 1 repatriation driven by ESR + hedge cost inversion + JGB yield attraction. Exposure estimated but hedge ratio not quantified.
**New view:** Same drivers, now with MEASURED hedge ratio (44.4%, 14yr low). System more exposed than modeled. Repatriation base case ($80-120B) may be conservative. Forced-selling FX threshold mapped (130-135). GPIF risk eliminated.

**Source:** Norinchukin CLO research package (Apr 2026). Full report: `research/outputs/NORINCHUKIN_CLO_CONTAGION.md`.

---

## 2026-04-03 — PRIVATE CREDIT AMPLIFIER INTEGRATED (THESIS v1.1)

### THESIS v1.0 → v1.1 (minor)
**Author:** SAM
**Action:** Added "Private Credit Amplifier" sub-section to Channel 1 (Life Insurer Repatriation). Adjusted flow scenario probabilities. New KB entries (160-162), new vector (VX-SAM-13.00).

**What changed:**
1. **Japan life insurers hold ~$40-53B ($45B central est.) in US private credit**, mostly unhedged (80-90%). Bottom-up verified: Sumitomo $10.7B, Nippon $3.25B, Meiji $4.2B, Dai-ichi $4.2B, plus listed insurers $14B. Morgan Stanley 1-3% AUM range applied to $2.6T industry.
2. **Double-hit vector identified:** BOJ hike (yen +5-8%) + US PC cascade ($10.1B Q1 redemptions) = $4-12B combined losses on illiquid, gated positions.
3. **Flow scenario probabilities adjusted:** Base case 75%→70%, stress case 20%→25%. PC amplifier makes orderly repatriation less likely.
4. **Inbox signal processed:** Prome/Eric Jackson (Pebbles II) cross-fund analysis. Also noted: Dutch pension DB→DC switch (Jan 2026), global pension PC exposure map (CPP, AustralianSuper, Korea NPS, UK).

**Old view:** Channel 1 repatriation driven by ESR + hedge cost inversion + JGB yield attraction. Base case 75%.
**New view:** Same drivers PLUS private credit amplifier — illiquid PC positions create correlated losses that make exits messier. Stress case probability nudged to 25%. Not a new channel — Channel 1's dark twin.

**Counterpoint noted:** Most CLO holdings are AAA/AA tranches (historically resilient). Severity depends on vintage and tranche quality. Direct lending more exposed than CLO senior tranches.

**Source:** Prome signal SIG-2026-04-02-001, Morgan Stanley estimates, SAM bottom-up verification. Full research: `research/outputs/JAPAN_INSURER_PRIVATE_CREDIT_EXPOSURE.md`.

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
