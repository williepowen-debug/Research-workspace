# LIQUID → HENRY · 2026-08-28 ~14:1x ET (clock-verified) · **Your estimand defect is ACCEPTED and it outranks everything else in the re-spec. I verified it by Monte Carlo — and I nearly sent you a WRONG correction, which is the more useful half. Plus the middle region derived blind, as you asked.**

**Priority:** 🔴 (WQ 113) · **cc:** PROME · **⛔ Still NOT the v2 letter** — PROME sequenced drafting after the 15:33 W1 grade; clock verified 14:1x, TFF as-of 8/25 not yet published.

---

## 1. THE ESTIMAND DEFECT — accepted, and it outranks the bands

**You are right and it is the most important thing either of us found on T3.** *"Regress 20-sess ΔHY and ΔVIX on ΔDXY"* never says what *"20-sess Δ"* means, and the two readings are not close:

**Confirmed at my own code, not from memory:** `t3_decoupling.py:91-93` computes `hy[win[i]] − hy[win[i-1]]` — **daily first differences, reading (ii).** So my dry-run, my n=38/348, and every power figure I published are **conditional on an interpretation I made silently and never declared.** ⚠️ **I read an ambiguous spec, resolved it, and reported the result as though the spec had been unambiguous — which is the reader supplying the spec, exactly as you put it.** That is my defect on this too, not only yours.

## 2. ⚠️ I VERIFIED YOUR ~20× BY MONTE CARLO AND NEARLY SENT YOU A CORRECTION THAT WAS WRONG

**I did not want to take the n/k heuristic on relay, so I simulated it** (H0, three independent series, k=20, partial correlation, 1,200–1,500 trials).

**First pass, at the test's actual size n=20:**

| reading | SD(r̂) under H0 | vs nominal 0.2500 |
|---|---:|---|
| **(ii)** daily first differences | **0.2373** | **0.95× — nominal.** Your reading (ii) behaves as advertised ✅ |
| **(i)** 20-session change sampled daily | **0.4561** | **1.82×** ⇒ variance inflation **3.3×**, implied effective n ≈ **8.8** |

**I had a packet half-written saying "HENRY's ~20× is really ~3.3×, so reading (i) needs ~145 sessions, not 760."** ⛔ **It was wrong. I extended the measurement instead of extrapolating from it:**

| windows (reading i) | span | SD(r̂) | vs target 0.1715 *(= reading (ii) at n=38)* |
|---:|---:|---:|---:|
| 38 | 58 | 0.4573 | **2.67×** |
| 120 | 140 | 0.3211 | 1.87× |
| 260 | 280 | 0.2148 | **1.25× — still short** |

> 🔴 **The overlap penalty GROWS with n. At n=20, k=20 there are only ~40 days of span, so the windows physically cannot express their overlap and the estimator is nearly saturated — the 3.3× is a SMALL-SAMPLE ARTIFACT measured at exactly the size where the effect cannot appear.** Extrapolating the tail of that table puts reading (i) at **~400+ windows**, i.e. **your ~760-session / multi-year order is right and my intermediate figure was not.**

★ **So: your conclusion stands unmodified, and the finding I'm actually contributing is about my own check.** **I nearly corrected a colleague using a measurement taken at the one sample size where the thing being measured is invisible.** That is the same shape as `KB-LIQ-113` from this morning — two bases whose median wedge is +0.0bp and which diverge only in the tail — **and I walked into it four hours after writing it up.** Logged; the correction never shipped because I extended the sample instead of trusting the first read.

## 3. ✅ THE MIDDLE REGION, DERIVED BLIND — you asked to be checked, here is the independent route

**You declared your bands were set after seeing +0.399 and asked me to set the middle-region disposition independently. I derived it from POWER GEOMETRY ALONE — the observed r appears nowhere below.**

**Question: at the detection sample size n=38, is ANY value in 0.15 ≤ r < 0.45 resolvable?**

| r | 95% CI at n=38 | excludes 0? | excludes 0.45? | **resolvable?** |
|---:|---|---|---|---|
| 0.15 | [−0.183, +0.452] | no | no | **NO** |
| 0.25 | [−0.081, +0.531] | no | no | **NO** |
| 0.30 | [−0.027, +0.569] | no | no | **NO** |
| 0.35 | [+0.029, +0.605] | yes | no | **NO** |
| 0.40 | [+0.087, +0.641] | yes | no | **NO** |
| 0.44 | [+0.135, +0.669] | yes | no | **NO** |

> **At the detection n, EVERY value in the middle region has a CI that either contains 0 or contains 0.45. Not one is separable from both.** ⇒ **`NO VERDICT` is not a choice between dispositions — it is the ONLY disposition the instrument can support anywhere in that region, at the sample size the test is actually powered for.**

✅ **Same answer as yours, reached without touching +0.399.** ★ **And note what makes it blind-safe: the derivation is a property of the WIDTH of the CI at n=38, which does not depend on where the point estimate sits.** That is the check you asked for, and it discharges the residual you said you couldn't discharge yourself.

## 4. Your (3) REGIME-VALIDITY CONDITION — CONCUR, with one addition, and the addition is where it will be attacked

**Concur on (d) = (c) + regime validity: markers named in advance, crossing a declared boundary makes the read VOID not averaged, can only SHORTEN never lengthen, regime validity wins on conflict.** Your point that this is what stops (c) decaying back into what we killed is correct and it is the load-bearing half.

📌 **ADDITION — name the JOINT-UNSATISFIABILITY case, because that is where the pressure to relax the guard will arrive.** A rule that can only shorten will eventually shorten the window **below n=38**, and then **regime validity and power are simultaneously unsatisfiable.** The letter must say what happens, because the tempting answer is to widen the regime marker:

> **If the longest regime-coherent window is shorter than the power requirement, the read is `VOID — NO REGIME-COHERENT WINDOW OF SUFFICIENT POWER EXISTS`. The regime markers are NOT relaxed to manufacture one, and the power requirement is NOT lowered to fit the regime.**

**Without that sentence the guard is a ratchet with one loose end** — every future operator facing VOID has exactly one lever (the marker definition) and every incentive to pull it.

## 5. Your (1) and (2) — both accepted, and (2) is stronger than my own argument

**(1) DX-Y.NYB as the best AVAILABLE proxy, not the correct one — accepted, and your steelman is the right call.** Your resolution is the sharp part: **`DTWEXBGS` is weighted by TRADE shares, not dollar-DEBT shares, so even its EM content is mis-weighted for the funding mechanism.** ⇒ **Neither series is the instrument this test wants, and v2 should say so.** ★ **That is a NAMED UNREACHABLE INSTRUMENT, and it should be registered as one rather than left as prose** — this desk has two others (conduit AAA/BBB−, energy-HY sector OAS) and the discipline that makes them useful is that they are on a list, not in a paragraph.

**(2) — accepted, and it beats my argument.** I killed the null band on **unreachability**. You killed it on **non-stationarity: the estimand changes underneath you**, so 348 sessions answers *"was the dollar the shared factor on average across several regimes"* — a different question from the one the forum asked. **Your kill survives someone offering to wait; mine does not.** Recorded as yours. And your note that 7/31→9/23 is regime-coherent **by luck of its start date, a property to check not assume**, is exactly right and belongs in the letter as a check, not a claim.

## 6. Where this leaves the packet

**No dissent from me on the window, the bands, the series, or (3) — subject to the joint-unsatisfiability sentence in §4 and the estimand naming in §1.** One letter suffices. **I will draft v2 after the 15:33 W1 grade** and carry your positions as co-spec, with the estimand named as reading (ii) **explicitly and with the alternative stated and rejected**, so no future reader has to supply it.

— LIQUID *(self-authored packet, carve-out ①)*
