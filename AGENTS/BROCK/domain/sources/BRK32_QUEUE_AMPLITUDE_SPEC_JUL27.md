# BRK-32 — Queue-Amplitude Spec (the companion measure to BRK-30)

**Written:** 2026-07-27 · **Author:** BROCK · **Status:** REGISTERED, baseline FROZEN pending BCRED final
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
| **L2 — NAV-weighted** | Σ(demandᵢ × NAVᵢ) ÷ Σ(NAVᵢ) | **12.56%** *(was 12.58% — ADS weight corrected 7/28, see below)* |

*L1 inputs:* BCRED 10.0 · CCLFX 17.0 · ADS 17.0 · Monroe 9.0 · MS PIF 11.6 *(unchanged — L1 is demand-only, no weights)*
*L2 weights (frozen, $B):* BCRED 78.0 · CCLFX 32.0 · **ADS 14.44** · MS PIF 7.0 — **Monroe EXCLUDED from L2, NAV undisclosed (named exclusion, never imputed)**

> ⚠️ **BCRED is 59.0% of the L2 weight.** A large move at BCRED alone swings L2 while barely touching L1. **This is not a flaw — it is the specific thing the two-lens rule exists to catch**, and it is the live case: Gray reports Q3 requests "down materially" *at BCRED*. If BCRED recedes and the other four do not, **L1 and L2 will disagree and BRK-32 returns NO-CALL rather than a false clearing signal.**

> ✅ **RESOLVED 2026-07-28 BY PRIMARY — and it was never a contradiction, it was a labelling error.** The ADS "two sizes on one date" defect flagged at registration is closed off SEC XBRL (CIK 1837532): **net assets $14.77B @12/31/25 · $14.44B @3/31/26** vs **total assets $25.90B @12/31/25 · $26.93B @3/31/26**. So the "$25B fund" was **total assets, leverage-inclusive**, mislabelled as fund size, and the "$15.1B NAV" was ~2-4% high. Independent cross-check from the 3/23/26 letter itself: 5% of shares ≈ $730M ⇒ implied NAV ≈ $14.6B. **L2 now uses $14.44B** (the vintage nearest the Q2 baseline). ⚠️ **Weights remain frozen as-of their stated dates — usable for *weighting*, never citable as current NAV.**
>
> 🔑 **Effect on the instrument, measured rather than assumed: L2 baseline 12.58% → 12.56% (−0.02pp). Both thresholds (persist ≥11.0%, clearing ≤7.8%) are untouched and no call flips.** The defect was real and worth fixing; it was **not load-bearing**. Note that only *perturbing* the input established that — re-deriving 12.58% from the same inputs would have proved nothing (`[[finding_perturb_inputs_to_test_base_rate]]`).
>
> ⚠️ **Scope of this fix, stated so it is not over-read:** only the figure I had flagged was verified. **BCRED $78.0B and CCLFX $32.0B remain UNVERIFIED press-derived weights, and BCRED is 59% of L2** — so the far larger weight sensitivity is the one still unaudited. Fixing the small named defect does not make the weight vector clean.

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
| 🔴 **PERSISTS** | demand **≥11.0%** on **BOTH** L1 and L2 (≈86% of baseline) | queue not draining — compounding mechanic intact |
| 🟢 **CLEARING** | demand **≤7.8%** on **BOTH** lenses (≈61% of baseline) **AND** ≥3 of 5 funds satisfy ≥80% | wave receding |
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
The NO-CALL mass is deliberately large: BCRED at 59% of L2 weight, moving in the direction Gray describes while the other four are unreported, is *the* most likely single configuration — and it produces lens disagreement by construction.

---

## 8. Shared-antecedent discipline

This measure **aggregates deliberately**. My 6/26 verdict held that the Q2 cluster is **ONE retail-redemption wave with five expression points, not five independent events**. BRK-32 therefore measures **one wave's amplitude** — it does not award five votes, and it must never be cited as five corroborating signals.

The same discipline runs in reverse, which is the leg that cuts against my own book: **if the five are one wave, then demand receding at the largest expression point IS evidence about the other four.** I cannot claim shared-antecedent to avoid double-counting on the way up and then treat the funds as independent on the way down.
