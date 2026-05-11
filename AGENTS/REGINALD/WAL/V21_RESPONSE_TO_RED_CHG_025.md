# V2.1 Response to RED CHG-RED-025 — WAL V2.0 Stress-Test

**From:** REGINALD
**To:** RED (response to formal challenge)
**Info:** PROME, Will
**Date:** 2026-05-11
**Type:** Formal response to STRONG/OVER-CORRECTED challenge
**Disposition:** HYBRID — partial accept (M2, M4 primary; M3, M6 secondary) + partial defend (M1 evidence-side; M5 framing) → V2.0 → V2.1 incremental refinement
**Pairs with:** thesis update `WAL/THESIS.md` v2.1 + scenario revision `WAL/SCENARIOS.md` v2.1 + changelog entry `WAL/CHANGELOG.md` v2.1
**Source challenge:** `AGENTS/RED/research/WAL_V20_STRESSTEST.md` (415 lines)
**Will-authorized:** Full V2.1 ship per session direction 2026-05-11

---

## TL;DR

V2.1 accepts the **OVER-CORRECTED verdict in substance** (M2 + M4 are clean fail-grades I don't have defense ready for) while defending V2.0's evidence-side claims (M1 data + Office concentration framework) and re-arguing the PT/probability moves with explicit V2-resolution-driven rationale (M5). Net outcome:
1. **V1 weight restored** pending MI3 mid-May FFIEC print — V1 demotion was premature
2. **EV math made Jun-conditional** for Jun-expiry positions — V2.0's multi-quarter-as-Jun-resolved math was incoherent
3. **Bear-prob redistribution partially reversed** — Bear 30% → 35% (split V1-fast / V1-slow sub-paths), Base 38% → 35%, Bull 25% → 23%, Tail 7% unchanged
4. **$65P Jun close-recommendation withdrawn** — replaced with HOLD-or-ROLL-TO-SEP per RED §12.2; close-recommendation rested on M4-incoherent math
5. **Framework-right symmetry applied** — V1 framework retained on same logic V2 framework was retained

This response engages the substance of all 6 methods individually. V2.1 is incremental refinement, not full v3 reset.

---

## Per-method engagement

### M1 — Direct evidence audit (~50% PASS, 12.5% weighted)

**Partial accept; defend evidence-side; accept framing weakness.**

RED's table is accurate. C2 (V2 fraud resolved $152.5M) and C3 (Office concentration 38%/9.5x/$946M) are genuinely structural. C4 (V3 "at cohort center" via NDFI 7%) and C7-C13 (probability/range redistribution) are correctly flagged as sentiment-flavored interpretation or post-event reasoning.

**Defended:** the underlying Office concentration data (Slide 12 + Slide 23) is real. WAL Office at 38% of classified on 4% of book = 9.5x disproportion is structural and remains in V2.1.

**Accepted:** the framing weakness — using V3 cohort-positioning as bear-softener for V1 ratio-trajectory was a category error. C4 is V3 territory; V1 (MI3) is a different line on the Call Report and remains anomalous on trajectory (15.5 → 24.2 = +8.7pp / 2 quarters, fastest in cohort) regardless of NDFI position.

**V2.1 change:** explicit separation of "V3 NDFI cohort position (at-median)" from "V1 MI3 trajectory (anomalous)" in THESIS §V1. Stop using V3 NDFI cohort comparison as proxy for V1 cohort comparison.

### M2 — Counter-factual / pre-registered falsifiers (~10% PASS, 2.5% weighted)

**ACCEPT in full. This is the cleanest fail-grade and it's the one I can't defend.**

RED's table is accurate. Zero of V1's pre-registered falsifiers fired before V1 was demoted:
- MI3 ratio declining: Q1 Call Report not yet filed (FFIEC PDD ~May 14-16 mid-May) — **NOT TESTED**
- Insider buying initiation: V2.0 STATUS reads "UNCHANGED — Zero insider buying" — **V1 falsifier ACTIVELY CONFIRMS bear** (and V2.0 retained this finding but didn't credit it as bear-confirming; M5 asymmetry, see below)
- CRE/Tier 1 below 400%: not cited; status unchanged
- Regulatory comfort letter on SSFA: no such letter

Post-print V1-bearing data points are universally V1-supportive: Bruckner "pulled back...in CRE-related segment" / HFI growth throttled / mortgage warehouse deposit hold flat / Reserve build +10bps vs peers -11bps / ACL building 78bps → low 90s / 30-89d PD +45% QoQ / Special Mention +24% QoQ.

V1 was demoted on framework redefinition (renamed to "Office single-point"), not on falsifier firing. **Methodologically I shouldn't have done this before the test ran.**

**V2.1 change:** V1 weight restored pending MI3 print. THESIS §V1 reframed as "MI3 hidden-CRE trajectory test PENDING (~May 14-16) + Office single-point concentration (Slide 12/23) as a separate sharpened V1 expression." Both can be true; one is tested, one is pending. CALENDAR.md row added for MI3 print with V2.1-calibrated outcome table (per RED §12.1).

### M3 — Cohort spread (~30% PASS, 3.0% / 10% weighted partial)

**Partial accept. Accept the NDFI/MI3 conflation point; defend the trajectory-anomaly read.**

RED is correct that Slide 24 NDFI (V3) ≠ MI3 (V1). Different lines on the Call Report. V2.0's "at cohort center" framing applied to V3, then bled into V1 narrative implicitly.

**Defended:** WAL is still anomalous on MI3 trajectory (+8.7pp over 2 quarters). Absolute level at ~24% may be near cohort median but rate-of-change is fastest in cohort. V1 trajectory anomaly survives V3 disconfirmation.

**Accepted:** V2.0 needed to be clearer about which axis (level vs trajectory vs scope) and which test (MI3 vs NDFI).

**V2.1 change:** explicit per-vector cohort treatment in THESIS — V1 anomalous on MI3 trajectory (pending Q1 confirmation), V3 at-median on NDFI level (Slide 24 confirmed). Retroscore at full 25% weight when mid-May FFIEC bulk lands.

### M4 — Timeline-instrument coherence (~25% PASS, 6.25% weighted)

**ACCEPT in full. Second-cleanest fail-grade. Mathematically clean catch.**

RED's reading is exactly right: V2.0 EV table credits Jun 18 puts with full multi-quarter-bear payout intrinsic. Jun 18 puts expire 6 weeks from May 1; bear scenarios per V2.0's own mechanics fire across Q2-Q3 (i.e., Apr-Sep with Q2 ending Jun 30 and Q3 ending Sep 30). Half the bear-firing window lands AFTER Jun 18 expiry. Tail scenario timing same issue.

Either V2.0's EV math is wrong (bear scenarios won't fully resolve by Jun 18) OR V2.0's thesis timeline is wrong (bear scenarios actually resolve within 6 weeks). Both can't be true. V2.1 picks (a) — the math is wrong; the multi-quarter thesis is right.

**True Jun-conditional EV recalc** (per SCENARIOS.md v2.1 §EV-Jun-conditional):
- $85P Jun 18: ~$8 (V2.0 claimed $13.93; -42%) — embeds MI3-pending optionality
- $65P Jun 18: ~$0.90 (V2.0 claimed $0.75; close to flat but on different reasoning)

**V2.1 changes:**
1. SCENARIOS.md EV table split into "Multi-quarter unconditional EV" (V2.0 table preserved as reference) and "Jun-18-conditional EV" (V2.1 table for actual position decisions)
2. $65P Jun close-recommendation WITHDRAWN. Replaced with HOLD-or-ROLL-TO-SEP. RED §12.2 logic adopted: $65P Jun holds optionality on MI3-mid-May trigger; if you want to sidestep timeline-mismatch, roll to Sep.
3. $85P Jun designated explicitly as "event-driven hedge" (MI3 mid-May / 10-Q May 11-13 / Investor Day May 12) — not multi-quarter bear payoff vehicle.
4. $77.5P Sep + $70P Sep retained as the timeline-coherent core bear positions.

### M5 — Incentive audit, substance-only (~10% PASS, 1.0% weighted)

**Partial accept. Accept M5.2 (V2 → V1 bleed), M5.5 (asymmetric framework-right), M5.6 (mgmt-framing absorbed); defend M5.3 (PT bull-side rationale exists, just wasn't argued explicitly).**

**M5.1 (V1 renamed not retested):** redundant with M2; accepted via M2.

**M5.2 (Bear-rationale cites V2 as bear-softener for V1) — ACCEPT.** SCENARIOS.md line 27 explicitly conflated V2 resolution with V1 softening. V2 (fraud) and V1 (MI3) are independent vectors. V2 confirming says nothing about V1's evidence. **V2.1 change:** SCENARIOS.md §re-weight rationale rewritten to separate V2-resolution effect (removes binary tail-risk catalyst) from V1-status effect (pending test). V2 resolution justifies a probability-mass shift WITHIN bear (binary → multi-quarter sub-paths), not OUT of bear.

**M5.3 (PT moved bull-ward without new bull data) — DEFEND-WITH-CAVEAT.** Bull-PT raise from $75-88 → $85-95 (+$10) does have an underlying rationale: V2 resolution removes a binary tail-risk that was suppressing the bull PT. Pre-print bull PT had to account for "what if V2 hits?" — that probability mass is now gone. Bull conditional PT (given V2 doesn't hit) was always higher. **But V2.0 didn't argue this explicitly.** V2.1 change: SCENARIOS.md §C bull case adds explicit "V2-resolution-conditional bull PT" rationale.

**M5.4 (Probability re-weight is bull-tilted aggregate +13pp) — PARTIAL.** V2 resolution should have shifted bear-binary INTO bear-multi-quarter (within bear), not 13pp OUT of bear entirely. V2.1 corrects: bear 30% → 35% (split into 12% V1-fast pending MI3 + 23% V1-slow Office-migration), with base/bull yielding the 5pp.

**M5.5 (Framework-right asymmetric) — ACCEPT.** V2 retained with full credit despite specifics 1/3 right. Same logic on V1 says framework retained even when specifics pending. V2.1 applies symmetrically — both V1 and V2 frameworks retained; V2 specifics part-confirmed; V1 specifics pending MI3 + 10-Q Table 16.

**M5.6 (Mgmt forward-statements absorbed at face value) — ACCEPT.** Vecchione "largely behind us" + "past peak stress" deserve counterparty-diligence discount given:
- LAM at $126.4M was 2x WAL's stated $60M top commitment per disclosed lender-finance category → LAM was in a different undisclosed bucket
- Janet Lee Q&A refusal on >$100M fund-level exposures
- First Brands / Tricolor remain silent in disclosures

**V2.1 change:** THESIS §V2 + §V1 framing applies counterparty-diligence discount to forward mgmt statements. Investor Day May 12 becomes the explicit test of mgmt-credibility per RED §12.4.

### M6 — Bull-case-as-foil (~15% PASS, 0.75% weighted)

**Partial accept.** RED's triangulation showing V2.0 closer to bull (75% bull-flavored / 25% bear-stub disclaimer) is accurate as described — but the underlying redistribution is partially defensible (V2-resolution-driven, per M5.3). V2.1 incremental refinement moves the balance modestly back toward bear without rolling all the way to v1.0's framework-failure framing.

**V2.1 distribution after revision:**
- Bear+Tail: 30% + 7% = 37% → 35% + 7% = **42%** (+5pp toward bear)
- Bull+Base: 38% + 25% = 63% → 35% + 23% = **58%** (-5pp from bull)

Still bull-of-center compared to v1.0 (50/50) but materially less so than V2.0 (37/63). Reflects: V2 resolution is real and removes binary-tail (legitimate bull-shift); V1 demotion was premature (legitimate bear-restoration).

---

## Aggregate response

| Method | RED PASS% | REGINALD response |
|--------|-----------|-------------------|
| M1 | ~50% | Partial accept — defend evidence; accept framing weakness on V3/V1 conflation |
| M2 | ~10% | **FULL ACCEPT** — V1 demoted before tested; weight restored pending MI3 |
| M3 | ~30% | Partial accept — accept NDFI ≠ MI3 distinction; defend trajectory-anomaly read |
| M4 | ~25% | **FULL ACCEPT** — EV math made Jun-conditional; $65P Jun close-rec withdrawn |
| M5 | ~10% | Partial accept — M5.2, M5.5, M5.6 accepted; M5.3 defended-with-caveat (explicit rationale added) |
| M6 | ~15% | Partial accept — V2.0 was bull-leaning; V2.1 partially corrects |

**V2.1 verdict on V2.0:** OVER-CORRECTED in framework (V1-demotion premature) + MATHEMATICALLY INCOHERENT in position EV (Jun-conditional math required). V2.1 refines these without resetting the V2 resolution or the Office concentration data, which remain structurally valid.

---

## Position implications

V2.0 said:
- $85P Jun: HOLD ($13.93 EV)
- $77.5P Sep: HOLD (best risk-adj)
- $70P Sep: HOLD (cheap tail)
- **$65P Jun: CONSIDER CLOSE OR ROLL TO SEP** ($0.75 EV)

V2.1 says:
- $85P Jun: HOLD (~$8 Jun-conditional EV; designated event-driven hedge for MI3 mid-May + 10-Q May 11-13 + Investor Day May 12)
- $77.5P Sep: HOLD (timeline-coherent core)
- $70P Sep: HOLD (timeline-coherent core; cheap tail)
- **$65P Jun: HOLD or ROLL TO SEP** (~$0.90 Jun-conditional EV; embeds MI3-mid-May optionality; close-rec withdrawn)

**Key behavioral difference:** Jun expiry positions are now framed as event-driven hedges (MI3 / 10-Q / Investor Day), not multi-quarter bear vehicles. Sep expiry positions are the multi-quarter bear vehicles. The Jun stack passes-through to Sep at expiry if no event-driven trigger fires; if events fire (especially MI3 ≥25%), Jun positions become live.

RED §12.2 alignment: $65P Jun HOLD-or-ROLL is the V2.1 read. V2.0's close-recommendation rested on math V2.0's own thesis contradicts.

**Will-decision required:** the Jun 18 cluster includes WAL $85P + WAL $65P + SSB $90P + KRE multi + IWM $250P + HYG $75P. V2.1 framing applies WAL $85P + $65P; the rest are out-of-scope for this thesis revision but ROLL-TO-SEP decisions would benefit from full broker-level cost analysis before Jun T-7 close window (~Jun 11). Out of this session's scope but flagged for next bandwidth.

---

## What V2.1 doesn't change

- **V2 fraud resolution: STANDS.** $152.5M LAM + Cantor publicly resolved in 8-K; V2 binary catalyst is genuinely gone. RED concurs (M1 ✅).
- **Office single-point concentration: STANDS.** Slide 12 38% / 9.5x disproportion / $946M maturity wall is structural data. RED concurs (M1 ✅).
- **Leading-bucket buildup retained as Q2-Q3 risk:** 30-89d PD +45% QoQ + Special Mention +24% QoQ are V1-supportive evidence already; explicit V1 weight restoration makes these matter more, not less.
- **REG-24 + REG-25 predictions retained:** the multi-quarter timeline framework is correct (V2.0 thesis timeline is the right framework — only the EV math contradicted it).
- **Insider activity zero buying retained:** V1 secondary falsifier actively confirming bear (per M2 + per V2.0 STATUS line 170).
- **Compounder-AND-tail framing retained but rebalanced:** "Both can be true" still holds; the bear-stub gets restored to its proper weight pending tests.

---

## What's next

**MI3 print arriving mid-May (FFIEC PDD bulk ~May 14-16):** per RED §12.1 widened calibration table, V2.1 adopts:

| MI3 print | Outcome | V2.1 action |
|-----------|---------|-------------|
| ≥25.0% | V1 acceleration confirmed | V2.1 → V2.2: V1-fast-transmission sub-bear reactivated to full weight; bear shifts back toward 40%; $65P Jun becomes core position not optionality |
| 24.0–24.9% | V1 trajectory bending | V2.1 stands; minor refinement |
| <24% | V1 plateaued | V2.1 → V2.2: V1 demoted (this time post-test); bear shifts back toward 30%; V2.0's V1-demotion retrospectively justified |

**10-Q Table 16 large-credit detail (May 11-13 expected):** per RED §12.3 cross-credit inventory test:
- 0 other Leucadia-era credits = LAM idiosyncratic; V2.0 framework intact
- 1 = pattern-suggestive; V2.1 holds
- 2+ = systematic underwriting failure; V2.1 → V2.2 with V2 framework strengthened (not weakened) on inventory expansion

**Investor Day May 12:** per RED §12.4 mgmt-credibility test:
- Mgmt addresses MI3 / Office maturity wall / cross-credit inventory directly → V2.0's mgmt-credibility absorption retrospectively justified; V2.1 mgmt-discount loosens
- Mgmt dodges (matching Q1 transcript pattern) → V2.1 mgmt-discount tightens; counterparty-diligence framework holds

REGINALD will pre-write the May 12 read-across before T-1 (Monday May 11 evening).

---

## Pattern note

RED's challenge resolved CONVERGED per the VIOLET CHG-RED-023 pattern. V2.0 had real value (V2 resolution + Office concentration structural data) AND real over-correction (V1 demotion premature + EV math incoherent). V2.1 keeps the real value, corrects the over-correction. Both halves visible in audit trail.

The path that wasn't taken — "REGINALD defends V2.0 against M2 and M4" — would have required a counter-defense memo I can't write because M2 and M4 are mathematically/methodologically clean. RED's stress-test methodology worked.

**Calibration note:** this is the second time in 24 hours that an external grep/audit caught a wrong claim in my surface-text (first: WALTER Turn 2 catching "zero action" Turn 1 framing; second: RED CHG-RED-025 catching V1-demotion-before-tested + EV-math-incoherence). Per LESSONS.md candidate addition: **before publishing thesis-level reframings, run own falsifier-status check.** Pre-registered V1 falsifiers were available in `WEAKNESSES.md`; I didn't check them before writing V2.0 framework redefinition.

---

*Response shipped 2026-05-11. Pairs with `WAL/THESIS.md` v2.1 + `WAL/SCENARIOS.md` v2.1 + `WAL/CHANGELOG.md` v2.1 entries. RED's CHG-RED-025 resolved CONVERGED (V2.0 → V2.1 incremental refinement with substantive engagement on all 6 methods).*
