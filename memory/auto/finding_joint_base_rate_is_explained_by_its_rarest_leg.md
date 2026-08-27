---
name: joint-base-rate-is-explained-by-its-rarest-leg
description: "A conjunction's small joint base rate ('both happened in only 1.7% of weeks') feels like strong association and usually is not — it is small because ONE leg is rare. Always compare the observed joint rate to the PRODUCT of the marginals before calling co-occurrence evidence."
symptoms: "both legs point the same way · adding a second leg changed nothing · one leg wearing a two-leg label · P(B|A) is 90-something percent · the conjunction fires whenever the first leg fires · only N of M periods show both · joint base rate 1.7% · mutually corroborating · two independent confirmations · the second leg confirms the first · rare co-occurrence"
metadata:
  node_type: memory
  type: finding
---

A small joint base rate is intuitively read as "these two things going together is rare, therefore their co-occurrence is meaningful." **That inference is invalid without the marginals.** If one leg is rare on its own, EVERY conjunction containing it will look rare — including conjunctions with a leg that happens more than half the time.

**Worked instance (SAM, 2026-08-27, caught by RED the same session):**
- Claim published: *"both duration legs pointed at JGBs — joint base rate **19/1,129 = 1.68%** of weeks"*, offered as corroboration that two instruments confirmed one mechanism.
- The test: P(leg A: outward flow trips a ¥1.5T bar) = **2.48%** · P(leg B: inward flow > 0) = **57.22%** · product if independent = **1.42%** · observed joint = **1.68%**.
- ⇒ **lift = 1.19×**; conditional P(B|A) = 67.9% vs 57.2% unconditional; one-sided binomial **p = 0.172**.
- **The 1.68% was small almost entirely because leg A is rare. Leg B fires in a majority of all weeks. The conjunction added ~nothing to its own legs and the "corroboration" was withdrawn.**

**The symmetric corollary, which is the part that surprises people.** Near-independence also refutes the *opposite* reading — that the two legs are **one underlying impulse observed at both ends**. A single shared cause predicts co-occurrence FAR above chance. So a lift near 1.0 kills both stories at once:
- **"Two independent witnesses corroborating"** — needs lift > 1 to mean anything.
- **"One witness double-counted"** — needs lift >> 1 to be true.
- Lift ≈ 1 ⇒ **neither**. Report the co-occurrence as a DESCRIPTION, never as evidence, in either direction.

**The simpler kill, and it needs no joint arithmetic at all (RED, same session).** Look at the marginals FIRST and ask whether either leg is the **modal state**. Here P(leg B) = **57.22%** — "non-residents bought JGBs this week" is true in more than four of every seven weeks. **A leg that fires >50% of the time is a descriptor of the regime, not a detector of an event, and cannot corroborate in ANY conjunction regardless of what the lift comes out at.** That kills the claim off one number, before any product or binomial is computed. Check it first; the lift calculation is the backstop, not the front line.

**The constructive half — a sign leg can often be repaired into a magnitude leg.** Re-specify the weak leg with a bar **base-rated to the same rarity as the strong leg**, then re-test:
- outward leg 28/1,129 = **2.48%** ⇒ inward bar set at **≥¥1.376T** (top 28 of 1,129) = **2.48%**
- joint at comparable bars: **3/1,129 = 0.27%** vs **0.062%** if independent ⇒ **lift 4.32×** (vs 1.19× at the sign spec)
- ⇒ **the IDEA survived; the SPECIFICATION was what died.** ⚠️ And the instance that prompted all this **fails the repaired test** — that week's inward leg was ¥0.435T (73rd percentile), nowhere near the bar. **A properly-specified conjunction can have real association AND still not be tripped by the observation that made you look.** ⚠️ n=3 at the tight bar: lift 4.32× is not significant either. A flag to look, never a gate.

**SECOND FAILURE MODE — a leg can be non-modal, non-independent, AND STILL INERT (RED, 2026-08-27, found by running this memory against its own registry).** The modal test above catches a leg that fires *too often to mean anything*. It is **blind** to a leg that is **implied by the other leg**:
- RED-FT-08 = core CPI MoM ≥0.4% **AND** 3-mo annualised ≥3.0%. n=435. Leg A 10.80%, leg B 25.29% — **both pass the modal test, both non-modal, lift 3.70×.**
- But **P(B|A) = 44/47 = 93.6%.** Leg B removes **3 of leg A's 47 firings.** The joint rate is essentially leg A's rate. **It is one leg wearing a two-leg label, and the test as first written CLEARS it.**

**⇒ The covering question is not "are the legs independent?" but "DOES ADDING THIS LEG CHANGE THE FIRING SET?"** Compare P(joint) to **P(each leg alone)**, not only to the product. Run it **in both directions** — the answer is usually asymmetric and tells you which leg is doing the work:

| Spec | P(B\|A) | leg B removes | verdict |
|---|---|---|---|
| RED FT-08 | 93.6% | 3 of 47 (6%) | **INERT** — one leg in disguise |
| SAM sign spec (withdrawn) | 67.9% | 9 of 28 (32%) | **weak** — and killed by the modal test anyway |
| SAM magnitude re-spec | 10.7% | 25 of 28 (89%) | **discriminating** — the leg earns its place |

🔑 **And the part that should sting: I had computed P(B|A) = 67.9% and published it — as an INPUT to the lift.** The same number is simultaneously the direct answer to "does this leg change the firing set?" **I read one of its two meanings and not the other.** The number that answers the covering question is often already on the page, doing a different job.

⚠️ **Regime-split it too.** RED's FT-08 post-2021 (n=66): leg A 39.4%, leg B 69.7% (now modal), **joint 26 = identical to leg A** — leg B removed **exactly zero** firings in the very inflation episode the trigger exists to detect. **A conjunction can be inert precisely in the regime it was built for**, while looking fine on the full sample.

⚠️ **How it survived a base-rate audit (the transferable governance point):** RED's audit base-rated all nine registry rows **as whole rows and never split a conjunction into legs** — *an audit inherits the granularity of its own unit of analysis.* Compounding it, an earlier fix had deliberately expressed conjunctions as ONE quantity so no consumer could fire half a test — correct for the consumer, and it **made the two-leg structure invisible to a row-level auditor.** **The repair that protected the consumer concealed the defect from the auditor.**

**Why:** the error is asymmetric and flattering. A small joint number always reads as a strong finding, so it survives review while the marginals — which are one query away — go uncomputed. It is especially dangerous when the rare leg is the one you just measured and are excited about, because the conjunction then looks like independent confirmation of your own new result.

**How to apply:**
- Before writing "both X and Y occurred, base rate k/N," compute **P(X), P(Y), and P(X)·P(Y)**, and report the **lift** and a significance figure alongside the joint rate. If lift ≈ 1, say so in the same sentence.
- **State which CUT built each number.** The 2026-08-27 prose quoted "this week ranks 10th most negative" and "joint base rate 19" — two DIFFERENT cuts (a top-10 rank and a threshold bar) — without saying so, which invited a reviewer to reconstruct the joint set wrongly. RED's premise about the cut was in fact wrong, and **the charge landed anyway** because the underlying test was the right one. Name the cut per number.
- ⚠️ **If the inference is wired into a script, fix the SCRIPT, not just the prose.** The bad reading here was one line of console output that would have printed "corroborates a relative-value read" at every boot. A bad inference in prose is a mistake; the same inference inside an instrument is a machine for repeating it.
- Relates to [[finding_crosscheck_with_free_parameter_validates_nothing]] (a test with an unpinned parameter validates nothing), [[finding_overlapping_window_inflates_the_base_rate]] (the other way a base rate flatters), [[finding_shared_antecedent_independence_test]] (the QUALITATIVE twin — signals that share a latent antecedent), and [[finding_base_rate_the_instrument_before_its_event_table]].
