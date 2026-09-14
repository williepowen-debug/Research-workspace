# HEN-44 — AUGUST CPI — **GRADE**

**Graded:** 2026-09-13 ~21:0x ET · **Print:** 2026-09-11 08:30 ET · **TWO DAYS LATE** — the desk was dark 9/11–9/13; the lateness is a discipline defect and is recorded as one.
**Letter:** `reports/2026-09-02_HEN-44_AUG-CPI_LETTER_FROZEN.md`, frozen 2026-09-02 ~20:4x ET, nine days before the print. **Not amended. Graded on the letter as written.**
**DOCKET L124.** Grading order pre-committed in §5 of the letter: **Leg C first**, then A, then B.

> **Every figure below was re-derived at the FRED primary by this session** (`fredgraph.csv`, pulled 2026-09-13 ~20:4x ET) from the 3-decimal index levels the letter named by series ID. **PROME's and CARL's relayed figures were treated as inputs, not as the grade**, and both reproduce exactly.

---

## VERDICT — **CONFIRM. 3 of 3 operative legs pass.**

| Leg | Registered bar (frozen 9/2) | Print, re-derived at the primary | Grade |
|---|---|---|---|
| **C — DISCRIMINATOR** | core MoM ≤ **+0.30%** **AND** core YoY ≤ **2.55%** = CONFIRM · MoM ≥ +0.35% **OR** YoY ≥ 2.60% = DENY | **+0.2898% MoM** (`CPILFESL` 336.789 → 337.765) · **+2.4460% YoY** (`CPILFENS` 329.970 → 338.041) | ✅ **CONFIRM** |
| **A — mechanism** | gasoline CPI `CUSR0000SETB01` MoM SA inside **+2.0% … +4.5%** | **+3.8993%** (332.215 → 345.169) | ✅ **PASS** (inside) |
| **B — aggregate** | headline CPI MoM inside **+0.25% … +0.45%** | **+0.3960%** (`CPIAUCSL` 332.813 → 334.131) | ✅ **PASS** (inside) |
| ~~B-YoY~~ | *demoted to decorative-context at registration (§4.1) — grades nothing* | +3.3965% NSA | — (not graded, as declared) |

**Meaning, stated at the letter's own scope:** the August oil shock is **CONTAINED TO THE ENERGY LINE**. First-round only. No second-round effects visible in core on this print.

---

## 1 · LEG C — the margins, because one of them is 1bp

| Term | Bar | Print | Margin inside CONFIRM | Distance to DENY |
|---|---|---|---|---|
| core MoM SA | ≤ +0.30% | **+0.2898%** | **+0.0102pp — ~1bp** | 0.060pp |
| core YoY NSA | ≤ 2.55% | **+2.4460%** | +0.104pp | 0.154pp |

**Leg C is an AND, so the binding term is MoM, and it clears by ~1 basis point.** That is genuinely marginal and it belongs on the grade rather than in a footnote. It is not, however, ambiguous: the bar is a number, the print is a number, and the print is below the bar.

### 1a · Did the rounding convention decide the verdict? **NO — and here is the proof, in both directions.**
The published BLS figure is **core +0.3% m/m**. The registered bar is **≤ +0.30%**.
- On the **unrounded** index arithmetic: **+0.2898% ≤ +0.30%** ⇒ CONFIRM.
- On the **published rounded** figure: **+0.3% ≤ +0.30%** ⇒ CONFIRM.

**Both readings give the same verdict, so the rounding convention is not load-bearing here.** CARL's flag (`PROME/inbox/processed/2026-09-11_from-CARL_…-legC-rounding-trap.md` §1) named the right *shape* and I am recording that the shape did not bite on this print.

⚠️ **But the latent defect CARL pointed at is REAL and I am registering it against the METHOD, not this grade.** Had the print landed in **(+0.300%, +0.305%)**, it would have published as "+0.3%" while *breaching* a ≤+0.30% bar — the rounded figure and the bar would have disagreed with no tell. **What saved this letter is that §1 named the series by ID (`CPILFESL`) and quoted 3-decimal index levels**, so the bar was resolvable at a precision the headline does not carry. ⇒ **Method rule adopted forward: a band edge stated at 2dp must be accompanied by the index series ID that can resolve it at 3dp. A bar written at the same precision as the published headline is unresolvable at its own boundary.**

### 1b · Basis robustness — the verdict does not depend on the SA/NSA choice
The letter named `CPILFESL` (SA) for the MoM term but did not name a basis for the YoY term. **It does not matter on this print:** core YoY on the NSA series (`CPILFENS`) is **+2.4460%**; on the SA series (`CPILFESL` 329.700 → 337.765) it is **+2.4462%**. **Agreement to 0.0002pp**, and both are ~0.10pp inside the bar. **Recorded because an unnamed basis is a defect even when it is harmless** — and CARL's own frame was scored NOT-DISCRIMINATING this week for exactly this omission on the gasoline leg.

### 1c · ⚠️ What the rounded consensus framing would have done
The figure in circulation on 9/11 was *"core +0.3%, 0.1pp above the Dow Jones consensus"* — an **adverse-sounding** framing. **Leg C is not keyed to consensus; it is keyed to a number, and on that number the print is on the CONFIRM side.** A grader who read "hot vs consensus" as "fails Leg C" gets the discriminator exactly backwards. ⛔ **KILL ON SIGHT: "August CPI was hot, so HEN-44 denies."**

---

## 2 · LEG A — mechanism, PASS, and the basis is the whole story
- **Letter's series, SA:** `CUSR0000SETB01` 332.215 → 345.169 = **+3.8993%** ⇒ **INSIDE +2.0/+4.5. PASS.**
- **NSA counterpart** (`CUUR0000SETB01` 350.846 → 359.738) = **+2.5344%** — also inside the band, so **Leg A passes on either basis**; the +1.37pp SA−NSA wedge is August's seasonal factor, not pass-through.
- Point estimate was **+3.2%** (the NSA pump monthly-average delta). Realised **+3.90%** SA — **0.70pp above the point estimate, comfortably inside the band.** The ±~1.3pp band set for n=1 method confidence was the right width and I am not narrowing it.
- ✅ **CARL independently reproduced the +3.20% pump input from `GASREGW` at +3.198%, before opening my letter, same 5-week perimeter, no fitted parameter.** That is a real two-desk cross-check on the one input both desks could corroborate.
- ⛔ **Declared limit stands (§4.3): Leg A cannot decompose crude premium from refining margin.** A +3.90% print against a +3.2% pump input leans toward the products/refining channel doing extra work, but the letter says that is **inferrable, never measured**, and I am not upgrading it.

## 3 · LEG B — aggregate, PASS
`CPIAUCSL` 332.813 → 334.131 = **+0.3960%** ⇒ **INSIDE +0.25/+0.45. PASS.** Published BLS headline +0.4% m/m.
⚠️ **Declared limit stands (§4.2): A and B are NOT independent.** Motor fuel is a component of headline, so **A and B agreeing is one observation wearing two hats.** The three-of-three tally above is honestly **two independent observations**, not three. Leg C is the only orthogonal leg and it is the one the letter was written for.

---

## 4 · THE BASE-EFFECT CALL WAS THE LETTER'S BEST WORK, AND IT VERIFIED
§1 of the letter warned, nine days early, that **the August-2025 bases are HARD, not easy**, and that a +0.35% headline would leave YoY unchanged.

| Claim in the frozen letter | Re-derived at the primary today | |
|---|---|---|
| Aug-2025 headline MoM **+0.35%** (322.169 → 323.291) | **+0.3483%** | ✅ |
| Aug-2025 core MoM **+0.31%** (328.682 → 329.700) | **+0.3097%** | ✅ |
| "a +0.35% Aug-2026 headline leaves headline YoY UNCHANGED at ~3.30%" | headline MoM printed **+0.3960%**, i.e. **+0.048pp above the base** ⇒ headline YoY NSA rose **+3.3648% → +3.3965% = +0.032pp** | ✅ **exactly the predicted mechanism** |
| *(corollary, not stated but implied)* core MoM **+0.2898%** printed **below** the +0.3097% base ⇒ core YoY **FELL** | **+2.4783% → +2.4460% = −0.032pp** | ✅ |

⇒ **The "+3.4% headline, inflation re-accelerating" read that travelled on 9/11 is reading a base, not a move** — precisely as the letter said it would be nine days before anyone could see the number. **The entire headline YoY increase is 3.2 basis points.**

⚠️ **One out-of-sample pass does not widen the method's band, and this is now n=2** (the July gasoline-sign call was n=1). Two passes are a reason to keep using the base-effect decomposition with a stated band. **They are not a reason to narrow it.**

---

## 5 · ⛔ THREE DESKS READ THIS PRINT THREE DIFFERENT WAYS AND ALL THREE ARE CORRECT

| Reading | Instrument | Verdict | Question it answers |
|---|---|---|---|
| **HENRY, HEN-44 Leg C** | core MoM/YoY **level** vs a bar frozen 9 days early | **CONFIRM** — contained to energy | *Did the oil shock reach core?* |
| **RED, `RED-FT-08`** | core CPI **3-month annualised** ≈ **2.04%** vs a ≥3.0 bar | **NOT MET** | *Is core momentum at a stress level?* |
| **The sell side** (Timiraos/WSJ table, `SIG-W-20260911-008`) | **surprise vs consensus** + reaction function | **16 of 20 shops flipped to a September hike ON this print** | *What will the Fed do?* |

**These do not contradict each other. They are a level, a rate, and a surprise.** `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]`
⛔ **KILL ON SIGHT, both directions:** *"RED-FT-08 NOT MET, so CPI was soft and hike risk is low"* · *"the Street flipped hawkish, so HEN-44 denies."* **Name the metric on either side or say neither.**

---

## 6 · WHAT A CONFIRM DOES **NOT** LICENCE — written against myself

1. ⛔ **It does not say inflation is low.** It says the shock has not reached **core**. The energy line it is contained to is **+16.28% YoY** (gasoline **+27.40%**, airline fares **+23.41%**), and the **headline−core wedge WIDENED 0.88 → 0.95pp**. *Contained ≠ small.*
2. ⛔ **It does not predict the Fed**, and the letter said so at registration (§4.6). **That is HEN-45**, frozen the same night and deliberately separate so a right call on inflation and a wrong call on the reaction cannot be netted. The Street read this same print as hawkish; **if the Fed hikes on 9/16 that does not retro-deny HEN-44.**
3. ⛔ **It is ONE MONTH.** Second-round effects have a lag measured in quarters. A single containment print is not containment. **The claim this CONFIRM supports is "no second-round effects VISIBLE IN AUGUST CORE," and nothing wider.**
4. ⚠️ **A falsifier that did not fire is not a confirmation of everything nearby.** The registered falsifier (core ≥+0.35% MoM or ≥2.60% YoY) did not fire, by 0.060pp and 0.154pp. That is what was tested. Nothing else was.
5. ⚠️ **~1bp is ~1bp.** Had core rounded a hair differently the MoM term fails CONFIRM and lands in the letter's **dead band** (0.30 < x < 0.35 = neither CONFIRM nor DENY). **The letter's two-sided construction has a gap, and this print landed 1bp from its edge.** A future letter should either close the dead band or say what it means.

---

## 7 · RESOLUTION
- **`workbook/PREDICTIONS.tsv` HEN-44: `ACTIVE` → `RESOLVED-CONFIRM`.** Outcome_Notes carries this grade.
- **No threshold on any HENRY surface moves on this grade.** A resolved letter is not a threshold change.
- **$0 moved. No card, no order, no trade proposed.**

*— HENRY, 2026-09-13, graded on the letter frozen 2026-09-02, two days late, at the FRED primaries the letter named.*
