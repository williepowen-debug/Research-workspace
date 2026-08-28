# THE TREASURY BUYBACK INSTRUMENT — `RED-FT-11`, built 2026-08-27
**Will-directed ("build the treasury buyback instrument now"). Phase 2.5, Will-ruled 8/20 ahead of Phase 3. Displaced three sessions; built now.**

---

## 1. THE QUESTION — and it is not the one the fleet has been asking

The fleet question has been *"does the buyback move yields?"* **RED's question is narrower and it is about my own book:**

> **My strongest bear counter-signal row is `30Y 5.17 / 10Y real 2.32 — did NOT rally on a soft core print` at 30/70.** Since S29 cut Stagflation, **the real-rate grind is the bear's carrying mechanism and Managed Decline's defining one.**
> **A buyback is a yield-suppression operation landing directly on that instrument.**
> ⇒ **If the 10-30y sector rallies on FLOW rather than fundamentals, "the 30Y won't rally" stops being evidence about the economy and becomes partly a policy artifact — and I would have no way to tell.**

**That question survives regardless of whether the event is priced**, which matters because of §2.

## 2. ⛔ A PREMISE I WAS CARRYING IS UNSUPPORTED — corrected before building on it

I carried *"9 Sep is an UN-PRICED event, not a pre-priced one"* into SCRATCH, `board_log` and a packet to PROME. **TERRY had already ruled it:**

> *"Reading a net-zero level as zero flow is single-cause attribution on a multi-cause tape. **'UN-PRICED' is UNSUPPORTED — and not refuted. Nobody should size off it.**"*

**TERRY killed the 30Y-level framing in BOTH directions** (the announcement-day −3bp of 30Y−10Y flattening is 1.73sd of its own daily-change distribution and clears no bar ⇒ `UNDETERMINED`).

⇒ **This instrument is NOT built on an un-priced-event premise.** It is built on the attribution question, which stands either way. **Sixth instance today of RED carrying a claim another desk had already impeached** — recorded as such.

## 3. THE DESIGN — a CONDITIONAL CLASSIFIER, not a bare trigger

**My first design was a bare trigger and the base rate killed it: `30Y−5Y compresses ≥2sd over 5 sessions` fires 4 of 657 windows = 0.61%.** That is the `FT-03` problem — a line that carries no information until it fires and may never fire. **Struck before registration, not after.**

**The right object is a classifier that only asks the question when there is something to explain:**

| | Rule (all FRED officials, same 5-session window) |
|---|---|
| **PRECONDITION** | `Δ DGS30 ≤ −10.2bp` (1.0 sd, n=657) — **fires 12.2% of windows** |
| **FLOW** | `Δ(30Y−5Y) ≤ −3bp` **AND** `\|ΔBE10\| ≤ 4bp` **AND** `\|Δ2Y\| ≤ 6bp` |
| **FUNDAMENTAL** | `Δ2Y ≤ −8bp` **OR** `ΔBE10 ≤ −5bp` |
| **NO-VERDICT** | anything else — **a real outcome, recorded as one** |

**Branches verified DISJOINT: overlap 0 of 80 firings.**

### 🔑 Why 30Y−5Y and not 30Y−10Y — the mechanism sets the boundary
The 8/19 step-up covers the **10-30y** sector, so **10Y is INSIDE the bought bucket** and `30Y−10Y` compares two bought points against each other. On the announcement day:

| measure | move | in sd |
|---|---:|---:|
| `30Y−10Y` | −3bp | **1.67 sd** — does not clear *(TERRY got 1.73sd on a shorter window and correctly ruled UNDETERMINED)* |
| **`30Y−5Y`** | **−7bp** | **2.13 sd — clears** |

**The discriminator improves because the sector boundary is where the mechanism lives.** This is offered to TERRY as a refinement of an instrument choice, not a contradiction of their verdict — **their `UNDETERMINED` on `30Y−10Y` was correct on `30Y−10Y`.**

## 4. BASE RATES — and the prior runs strongly AGAINST the flow story

**Conditional on a 30Y rally ≥1sd (80 of 657 windows):**

| classification | n | share |
|---|---:|---:|
| **FUNDAMENTAL** | 71 | **88.8%** |
| **FLOW** | 5 | **6.2%** |
| NO-VERDICT | 4 | 5.0% |

**At ≥1.5sd, FLOW goes to 0 of 43.** ⇒ **Historically, a big 30Y rally has essentially always been fundamental.**

🔑 **That is what makes a FLOW verdict informative: it would be a ~6% event against its own reference class.** A trigger is only worth its slot if firing is surprising.

**Validation on the one labelled observation:** the 8/19 announcement day — `Δ30Y −9 · Δ(30Y−5Y) −7 · ΔBE 0 · Δ2Y 0` — **classifies FLOW.** The single day we know was announcement-driven lands in the right branch.

## 5. THE ACTION — and the important part is what does NOT move

**FLOW ⇒ the 30/70 real-rate-grind counter-signal row is DOWNGRADED TO 50/50, and Managed Decline is flagged MECHANISM-UN-INSTRUMENTED.**

> ⛔ **NO HYPOTHESIS WEIGHT MOVES ON A FLOW CLASSIFICATION. A FLOW verdict is a finding about MY INSTRUMENT, not about the world.** It does not say the economy is fine — **it says the 30Y stopped reading the economy.** Moving a weight on it would be scoring an instrument defect as evidence.

**This is the `ML-RED-144` class arriving in a second bucket.** At S29 I found Stagflation had been modal ~4 months **with no instrument for the mechanism its name refers to.** A FLOW verdict means **Managed Decline has just lost the instrument for its defining mechanism** — the same defect, and it must be recorded as that rather than traded.

**FUNDAMENTAL ⇒ the grind read is confirmed on its own terms. The row STANDS, no change** — it is already priced at 30/70, so confirmation banks nothing (Guard 6).

## 6. ⚠️ LIMITS — four, and the first is the one that matters

**(a) 🔴 THE BASE RATES ARE PRE-TREATMENT.** All 657 windows come from a period **without** a stepped-up buyback. **88.8%-fundamental is the prior for a world without the flow — it is a reference class for what a 30Y rally USED TO mean, not a prediction of what it will mean after 9/9.** That is precisely why the instrument exists, and it is why the prior must not be quoted as a forecast.

**(b) n=5 on the FLOW branch**, plus one labelled announcement day. **A flag to look, never a gate.** The FUNDAMENTAL branch (n=71) is far better supported than the branch I actually care about.

**(c) NOT MACHINE-GRADED — disclosed, because it cuts against my own `ML-RED-156`.** `boot.py` prints `⚪ unmapped metric, manual check`, correctly: a three-leg classification over a window cannot be expressed in the single-metric comparator. **ML-156 says a machine-consumed registration must carry its conjunction in the machine columns; this one cannot, so it is a MANUAL row and is labelled one.** Mitigation available later: the **precondition alone** (`Δ DGS30` 5-session) is mappable and would at least surface *when to look*.

**(d) Domain boundary.** **BOND owns `DGS30`/`DFII`/term premium and already runs `THREEFYTP10` daily and a buyback vector (`VX-16`, whose RED trigger fired 8/19). TERRY owns the position mechanics and `TRY-FIRE-004`.** **RED owns none of these instruments** — this is an attribution rule over their data, and if either desk says the leg choice is wrong, they are right and I re-spec.

## 7. WHAT WOULD MAKE ME RETIRE IT — written now

- The stepped-up 10-30y program **ends or is not renewed** — this is an instrument for a specific policy regime and means nothing outside it.
- The FLOW branch fires **3 times without the 30Y−5Y compression persisting beyond the operation window** — that would mean it is reading operation-day microstructure rather than a suppressed level.

⛔ **It does NOT exit on a classification. Classifying is what it is for.**

---

**Registered:** `registry/FALSIFICATION_TRIGGERS.tsv` → **`RED-FT-11`**, `ARMED-UNFIRED`, precondition live **2026-09-09**. `recipient_chain = BOND, TERRY, PROME` — **and routed at the write, not at closeout (the `FT-06` lesson from this morning: filling a routing column is not routing).**
