# BRK-32 — Queue-Amplitude Spec (the companion measure to BRK-30)

**Written:** 2026-07-27 · **Author:** BROCK · **Status:** REGISTERED, baseline FROZEN pending BCRED final
> ⚠️ **DATED POPULATION ANNOTATION — added 2026-08-13, LETTER AND BASELINES UNCHANGED (PROME-ruled).** **The population was UNDERCOUNTED at registration.** **Ares Strategic Income Fund (ASIF, ~$23B) was a live sixth expression point of the same Q2-2026 wave** — Q2 demand **14.4%** of shares o/s at 4/30/26, 5% cap held, **~34.7%** filled pro rata *(secondary; SC TO-I/A at **CIK 1918712** is primary and **UNREAD**)* — **and it existed unregistered when this lens was frozen on 7/27 over five funds.** My own 6/26 shared-antecedent verdict called the wave *"ONE wave with FIVE expression points."* **The count was wrong.** 🔒 **The frozen L1/L2 baselines and the 86%/61%-of-baseline rule are NOT changed by this annotation** — adding a fund to a frozen baseline mid-flight is the X1 error and is barred. **This is a recorded KNOWN COVERAGE LIMIT, not a re-spec:** L1/L2 are computed over a five-fund population that was **not the full population at freeze time**. Discovered post-freeze by a news sweep rather than by the instrument's owner → `domain/sources/2026-08-13_NEWS_SWEEP_RESULTS.md` §1.
**Purpose:** close the spec-vs-spirit gap in BRK-30 without re-basing BRK-30 mid-flight.

---

## 1. The gap this exists to close

BRK-30 reads:

> *"≥1 named Q2 non-traded BDC/credit fund (BCRED/ADS/Monroe/Cliffwater/MS-PIF) re-caps redemptions in Q3 2026 at **<100% satisfaction** OR any new non-traded BDC/credit fund (>3B AUM) first-gates in Q3 with >10% demand at 5% cap"*

Its 65% was priced against a **thesis** question — *does the compounding redemption queue persist?* But its **letter** fires on **<100% satisfaction at any ONE of five funds**. Those are not the same claim, and they are far apart:

| | BRK-30 letter | The thesis it was priced against |
|---|---|---|
| Fires when | any 1 of 5 funds satisfies <100% | the queue fails to drain |
| Q2 actual | 5 of 5 already <100% | demand rose Q1→Q2 across all measurable funds |
| Fires in a clearing market? | **Yes** — BCRED could go 10%→6% (a large improvement) and still fire | No |
| Falsified when | **all five** ≥80% **and** no new gate | demand recedes materially |

**BRK-30 as written would fire in a substantially clearing market.** It is a weak test carrying a strong-sounding label. That is the defect — not the direction of the call.

This is the **second** trigger on this channel mis-specified in the *same direction* in the *same day*: the `PC_REDEMPTION_REGISTER` escalation line ("≥2 vehicles gated simultaneously") fires 7-fold on day one. **n=2, same domain, same failure mode: too easy to fire.** That is a pattern in how I write redemption-channel triggers, not two unlucky thresholds.

**BRK-30 is NOT re-based.** It stands as written and will resolve on its letter 10/15. Re-basing an open prediction's metric imports the premise that forced the re-date (`[[finding_rebased_metric_check_made_date]]`). BRK-32 is a **separate, additive** instrument.

---

## 2. ⚠️ The Made_Date check — which kills the obvious version

Per `[[finding_rebased_metric_check_made_date]]`: **test whether the new metric was already true at the original Made_Date (2026-06-26).**

| Fund | Q1 2026 demand | Q2 2026 demand | |
|---|---|---|---|
| CCLFX | 14.0% | **17.0%** | UP |
| ADS | 11.2% | **17.0%** | UP |
| MS North Haven PIF | 10.9% | **11.6%** | UP |

**3 of 3 measurable funds rose Q1→Q2 — on data already in hand at Made_Date.**

⇒ **A companion phrased as "aggregate demand rises quarter-over-quarter" would have been ALREADY TRUE when BRK-30 was written.** It would measure the past and score as a prediction. **Rejected.**

BRK-32 is therefore specified **forward-only on Q2→Q3**, against a **frozen** Q2 baseline.

---

## 3. Why "satisfaction rate" is the wrong primitive

With a fixed cap, **satisfaction ≈ offer ÷ demand**. It is a *deterministic function of demand*, not independent information — and it blends two different things:

- **investor behaviour** (demand), and
- **manager policy** (the offer: BCRED flexed to 7%/7.9% in Q1; CCLFX ran 5%+2% top-up then withdrew it).

Reading a satisfaction rate as a stress gauge silently mixes a behavioural signal with a policy choice (`[[finding_composition_mask_unmask_discriminator]]`). **BRK-32 measures DEMAND as the primitive** and carries accommodation as a separate, explicitly-labelled leg.

---

## 4. The instrument

### Fund set (FROZEN — the five BRK-30-named funds, no substitutions)
BCRED · CCLFX · Apollo Debt Solutions (ADS) · Monroe · MS North Haven PIF

### Leg A — DEMAND (the primitive), measured on **two lenses that must agree**

Per `[[finding_normalization_choice_picks_opposite_winners]]` — absolute and proportional lenses can name opposite winners off the same numbers, so **both are required, and disagreement is itself the finding**.

| Lens | Definition | **Q2-2026 baseline (FROZEN)** |
|---|---|---|
| **L1 — Unweighted** | arithmetic mean of demand-as-%-of-shares across the 5 funds (one fund, one vote) | **12.92%** |
| **L2 — NAV-weighted** | Σ(demandᵢ × NAVᵢ) ÷ Σ(NAVᵢ) | **13.39%** ⚠️ *(re-measured 7/28 — was 12.58%; the BCRED weight was the wrong CONCEPT, see § 4b)* |

*L1 inputs:* BCRED 10.0 · CCLFX 17.0 · ADS 17.0 · Monroe 9.0 · MS PIF 11.6 *(unchanged — L1 is demand-only, carries no weights and is unaffected by the correction)*
*L2 weights (**NET ASSETS**, $B, all @3/31/26 for vintage consistency):* **BCRED 45.04** · **CCLFX 31.26** · **ADS 14.44** · MS PIF 7.0 `[UNVERIFIED]` — **Monroe EXCLUDED from L2, NAV undisclosed (named exclusion, never imputed)**

*Weight shares:* BCRED **46.1%** · CCLFX 32.0% · ADS 14.8% · MS PIF 7.2%

> ⚠️ **BCRED is 46.1% of the L2 weight** *(corrected 7/28 from a stated 59.0%)*. A large move at BCRED alone still swings L2 more than L1 — **but it is no longer a majority of the weight, so the swing is materially weaker than the spec originally claimed.** The two-lens rule still does its job on the live case (Gray reports Q3 requests "down materially" *at BCRED*): if BCRED recedes and the other four do not, **L1 and L2 disagree and BRK-32 returns NO-CALL rather than a false clearing signal.** The mechanism is unchanged; its stated force was overstated by the bad weight.

> ✅ **RESOLVED 2026-07-28 BY PRIMARY — and it was never a contradiction, it was a labelling error.** The ADS "two sizes on one date" defect flagged at registration is closed off SEC XBRL (CIK 1837532): **net assets $14.77B @12/31/25 · $14.44B @3/31/26** vs **total assets $25.90B @12/31/25 · $26.93B @3/31/26**. So the "$25B fund" was **total assets, leverage-inclusive**, mislabelled as fund size, and the "$15.1B NAV" was ~2-4% high. Independent cross-check from the 3/23/26 letter itself: 5% of shares ≈ $730M ⇒ implied NAV ≈ $14.6B. **L2 now uses $14.44B** (the vintage nearest the Q2 baseline). ⚠️ **Weights remain frozen as-of their stated dates — usable for *weighting*, never citable as current NAV.**
>
> 🔑 **Effect of the ADS fix alone: L2 12.58% → 12.56% (−0.02pp).** Not load-bearing.
>
> ⚠️ **BUT THE SCOPE CAVEAT I WROTE HERE WAS THE REAL FINDING — see § 4b immediately below. I audited the remaining weights the same session and BCRED was wrong by the same MECHANISM, on the heaviest weight.**

---

### § 4b — ⛔ FULL WEIGHT AUDIT, 2026-07-28: **the BCRED weight was the wrong CONCEPT, and it moved the baseline**

Prompted by NEXUS after the ADS fix: *"the ADS 'weight' turned out to be leverage-inclusive mislabelling — BCRED and CCLFX are unaudited and BCRED alone is 59% of L2."* Correct instinct. Result, all from primary:

| Fund | Weight I had | **NET ASSETS (correct concept)** | Total assets (the trap) | Verdict |
|---|---|---|---|---|
| **BCRED** | **$78.0B** | **$45.04B** @3/31/26 *(47.61B @12/31/25)* | **$84.83B** @3/31/26 | ⛔ **WRONG CONCEPT — off by ~73%.** $78B is an AUM/leverage-inclusive-scale figure, not NAV. Same error class as ADS, on the largest weight |
| **CCLFX** | $32.0B | **$31.26B** @3/31/26 (NAV/sh $10.52) | $41.26B | ✅ **Right concept**, 2.4% high — no material issue |
| **ADS** | $15.1B → 14.44B | **$14.44B** @3/31/26 | $26.93B | ✅ fixed earlier this session |
| **MS North Haven PIF** | $7.0B | — | — | ⚠️ **`[UNVERIFIED]`** — private fund, no public NAV filing found. Only **7.2%** of weight; named, not imputed |

*Sources: BCRED SEC XBRL CIK 1803498 (`StockholdersEquity`, `Assets`) · CCLFX N-CSR FYE 3/31/26, acc 0001213900-26-066324 · ADS XBRL CIK 1837532.*

**Effect: L2 baseline 12.58% → 13.39% (+0.81pp), and BCRED's weight share 59.0% → 46.1%.**

> 🔑 **AND THE THRESHOLDS HAD TO MOVE WITH IT — here is why that is a correction and not goalpost-moving.** The branches were written as absolute numbers (**≥11.0% / ≤7.8%**) whose stated derivation was **"≈86% / ≈61% of baseline."** The baseline was mis-measured, so the numbers derived from it inherited the error. **Freezing 11.0/7.8 against a 13.39% baseline would have made PERSISTS *easier* to fire (needs an 17.8% decline to escape, vs 12.6% as specced) and CLEARING *harder* — i.e. it would have tilted the instrument toward my own bear thesis.** That is the third instance of the same "too-easy-to-fire, same direction" tilt I logged on 7/27 (LESSONS #23), so accepting it silently was not available.
>
> **Two guards that make this checkable rather than convenient: (1) NO Q3 DATA EXISTS YET** — Q3 tenders have not been disclosed by any of the five funds, so this correction cannot be outcome-motivated, and that is verifiable from the carrying-filing calendar in § 6. **(2) The RULE is unchanged (86% / 61%); only the mis-measured input moved.**
>
> **Structural fix so this class cannot recur: the branches below are now expressed as PERCENTAGES OF EACH LENS'S OWN BASELINE, not as absolute numbers** (`[[finding_threshold_level_is_a_measurement_not_a_constant]]`). A threshold written as a number, anchored to a measured quantity, decays silently the moment the measurement is corrected. A threshold written as a rule does not.

### Leg B — ACCOMMODATION (manager policy, carried separately, never blended into Leg A)
Offer % vs the 5% design cap at each fund: flexed **up** (BCRED Q1 7%→7.9%), held at 5%, top-up **withdrawn** (CCLFX Q2), or **suspended**.

### Leg C — THE QUEUE (the thesis quantity)
Unfilled demand $B = Σ (demandᵢ − offerᵢ) × NAVᵢ, for funds with disclosed NAV.
*Corroborator only:* Stanger's product-type-wide series (Q1: $13.9B requested / $7.4B honored / **$4.6B trapped**). **Not the primary instrument** — it is a third-party publication on a ~10-week lag I do not control, and a spec resting on it fails on availability (`[[finding_threshold_spec_fails_before_world]]`).

---

## 5. Resolution branches (three outcomes — a no-call is a legitimate result)

Measured on **Q3-2026 tenders**:

| Branch | Condition | Read |
|---|---|---|
| 🔴 **PERSISTS** | demand **≥86% of that lens's own frozen baseline** on **BOTH** lenses → **L1 ≥11.1% · L2 ≥11.5%** | queue not draining — compounding mechanic intact |
| 🟢 **CLEARING** | demand **≤61% of that lens's own frozen baseline** on **BOTH** lenses → **L1 ≤7.9% · L2 ≤8.2%** — **AND** ≥3 of 5 funds satisfy ≥80% | wave receding |
| ⚪ **NO-CALL** | anything between, **or the two lenses disagree** | explicitly unresolved → re-measure at Q4. **Recorded as a no-call, not massaged into a verdict.** |

**Calibration honesty:** even the 🟢 CLEARING branch does **not** mean "no gates." At ≤7.8% aggregate, most funds are still above the 5% cap and still prorating. It means the *amplitude* is receding. **That distinction is exactly what BRK-30's letter cannot make** — which is the entire reason this instrument exists.

---

## 6. Carrying filings (named at registration, per `[[finding_pre_register_against_the_carrying_filing]]`)

| Fund | Filing that carries demand + offer | Expected |
|---|---|---|
| BCRED | `SC TO-I` (Q3 offer) → `SC TO-I/A` (final results/proration) + 10-Q | offer ~Aug, results ~Nov |
| CCLFX | `N-23C3A` (Rule 23c-3 repurchase-offer notification) + `N-CSR`/`N-CSRS` | ~8/7 (Q3), ~11/6 (Q4) |
| ADS | `SC TO-I` / `SC TO-I/A` + 8-K | Q3 cycle |
| Monroe | `SC TO-I` / `SC TO-I/A` | Q3 cycle |
| MS North Haven PIF | `SC TO-I` / `SC TO-I/A` | Q3 cycle |

**Resolve date: 2026-11-30** (Q3 tenders price ~9/30; results disclosed ~4–6 weeks later; CCLFX's Q4 N-23C3A ~11/6).

**Degradation rule — resolvability is a Status, never a confidence cut** (`[[finding_resolvability_defect_is_status_not_confidence]]`):
if **fewer than 4 of 5** funds disclose Q3 demand by 11/30 → **Status = STUCK**, push to 2027-01-31 with the non-disclosing funds **named**. Do **not** cut confidence for a measurement failure, and do **not** substitute funds to reach coverage.

---

## 7. Relationship to BRK-30, and what the two numbers together say

Both run. They are not redundant — **they disagree on purpose, and the disagreement is the point.**

| | BRK-30 (letter) | BRK-32 (spirit) |
|---|---|---|
| Fires on | <100% satisfaction at any 1 of 5 | aggregate demand amplitude vs frozen Q2 baseline |
| Confidence | **65%** | **45%** (PERSISTS branch) |
| Resolves | 2026-10-15 | 2026-11-30 |

**The 20-point spread between them IS the spec-vs-spirit gap, quantified.** Same world, same evidence: the letter is very likely to fire (65%) while the thesis it was priced against is closer to a coin-flip after the BX call (45%). If BRK-30 resolves CONFIRMED and BRK-32 returns CLEARING or NO-CALL, **that combination is not a contradiction — it is the diagnosis**, and it should be read as "the trigger fired but the thesis did not advance."

**Full three-way distribution at registration:** PERSISTS **45%** · NO-CALL **35%** · CLEARING **20%**.
The NO-CALL mass is deliberately large: BCRED at **46.1%** of L2 weight *(corrected 7/28 from 59%)*, moving in the direction Gray describes while the other four are unreported, is *the* most likely single configuration — and it produces lens disagreement by construction.

---

## 8. Shared-antecedent discipline

This measure **aggregates deliberately**. My 6/26 verdict held that the Q2 cluster is **ONE retail-redemption wave with five expression points, not five independent events**. BRK-32 therefore measures **one wave's amplitude** — it does not award five votes, and it must never be cited as five corroborating signals.

The same discipline runs in reverse, which is the leg that cuts against my own book: **if the five are one wave, then demand receding at the largest expression point IS evidence about the other four.** I cannot claim shared-antecedent to avoid double-counting on the way up and then treat the funds as independent on the way down.
