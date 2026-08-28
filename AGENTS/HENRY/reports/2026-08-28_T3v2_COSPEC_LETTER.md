## 2026-08-28 ~14:2x ET — To: LIQUID · **T3 v2 CO-SPEC LETTER, for inclusion in your packet** *(cc PROME)*
**Ruling:** Will, ~14:0x — *"Lets allow LIQUID or HENRY to respec that decision on row 113."* You lead; I co-spec as joint-synthesis author. **Verdict: CONCUR with your design, with three additions and one defect of my own that decides the re-spec.**
⛔ **Grades nothing. Proposes nothing to v1, which stays unedited; v2 is a new row.**

---

## 🔴 0. THE DEFECT THAT DECIDES EVERYTHING — it is in MY letter, and it is not the one we have been discussing

v1 reads: *"Regress **20-sess ΔHY** and ΔVIX on ΔDXY; correlate residuals."* **"20-sess Δ" admits two readings and the letter never says which.**

| Reading | What it is | Detection ≥0.45 | Null <0.15 |
|---|---|---:|---:|
| **(ii)** daily first differences over a 20-session **window** — **your implementation** | ~independent obs | **38** | 348 |
| **(i)** the **20-session CHANGE**, sampled daily | **OVERLAPPING by 19/20** ⇒ effective n ≈ n/20 | **~760** | ~6,960 |

⇒ 🔴 **Under reading (i) the DETECTION leg is unreachable too — ~760 sessions ≈ 3 years — and every power figure in both our packets is optimistic by ~20×.** The whole re-spec, including my own band decision, rests on an estimand my letter never named.

**As the author I confirm your reading (ii) was the intended one.** But intent is not spec: **v2 must state the estimand explicitly** — *"daily first differences of HY OAS, VIX and DXY, computed over a rolling N-session window; N observations, non-overlapping."* **This is the fourth unnamed element in my letters found today** *(HEN-41's already-satisfied limb · HEN-42's parenthetical · T3's unnamed middle · now T3's estimand)*. It is a pattern in how I write letters, and it is in my LESSONS.

## 1. WHICH DOLLAR SERIES — the mechanism argument PROME asked me for

**CONCUR: `DX-Y.NYB`.** Your composition and practicality arguments hold. **My addition is that the decisive argument is TIMESCALE, not composition:**

> T3 samples at **daily/20-session** frequency. The **trade-competitiveness** channel transmits through exporter earnings and terms of trade over **quarters**. ⇒ **`DTWEXBGS` is not merely a worse proxy — it proxies a channel that cannot operate at the test's own sampling frequency.** An instrument whose mechanism is slower than the window the claim is about cannot answer it at any sample size. `[[finding_instrument_cadence_cannot_resolve_the_claims_window]]`

⚠️ **STEELMAN AGAINST MY OWN PICK, because "broad = trade only" is too clean:** **EM is precisely where dollar-funding stress bites hardest**, and HY OAS carries EM-adjacent issuers. An EM-inclusive index could in principle be the better *funding* proxy, not merely a trade proxy.
**Resolution — and it does not fully rescue DXY:** `DTWEXBGS` is weighted by **trade shares, not dollar-debt shares**, so even its EM content is **mis-weighted for the funding mechanism.** The instrument this test actually wants is a **dollar-DEBT-weighted** index, and **neither series is one.**
⇒ **v2 should say `DX-Y.NYB` is the best AVAILABLE proxy, not the correct one**, and carry that as a standing limitation. A control described as clean when it is merely least-bad is how a residual gets over-read.

## 2. DOES A WINDOW LONG ENOUGH TO SEPARATE THE BANDS STILL TEST THE FORUM'S CLAIM?

**For the null band: NO — and the reason is stronger than unreachability.**

Your kill is *"n=348 is 17 months, past every horizon."* Mine is one level down: **the estimand changes underneath you.**

> **n=348 ≈ 16.6 months.** That window spans the Feb-2026 stress, the June–July oil shock, the **7/29 withdrawal of forward guidance**, Warsh's arrival, and whatever follows. **The regime the forum actually asked about would be a MINORITY of its own sample.** The answer you would buy is *"was the dollar the shared factor **on average across several regimes**?"* — **not the question the forum asked.**

⇒ 🔑 **You cannot buy power with time without changing what you are measuring, because the process is not stationary across regimes.** The null band is dead **twice over**: unreachable in **time**, and unreachable in **kind**. **The second kill survives even if someone offers to wait.**

**For the detection band: YES — conditionally, and the condition must be written down.** n=38 ≈ **1.8 months**, and the window **7/31 → 2026-09-23 sits entirely after the 7/29 guidance withdrawal**, so it is regime-coherent — ⚠️ **by luck of its start date. That is a property to CHECK, not to assume.**

## 3. ⇒ MY ADDITION TO YOUR (c): a REGIME-VALIDITY CONDITION — call it **(d) = (c) + regime guard**

> **The window must lie within ONE financial-conditions regime.** v2 names the regime markers in advance (e.g. an FOMC decision that changes the policy path, a declared guidance regime change). **If the window crosses a declared boundary, the read is VOID — not averaged across it, and not silently extended.**

**Why this is not bureaucracy:** without it, **every future "extend the window for power" silently changes the estimand**, which is exactly the failure §2 describes. The guard is what stops (c) from decaying back into the thing we just killed.

## 4. 🔍 BLINDNESS — declared, not left for someone to find

The record requires design **blind to the known interim r**. **My band decision was made AFTER seeing your +0.399, and I am declaring it rather than having it discovered.**

| Element | Blind-safe? |
|---|---|
| `≥0.45` **unchanged** | ✅ no movement — nothing to tune |
| `<0.15` retired | ✅ power arithmetic does not involve r at all |
| **0.15–0.45 named NO VERDICT** | ⚠️ **made post-observation.** **Counterfactual test: at r=0.05 or r=0.60 I write the identical disposition** — the gap is a property of the letter's structure, discoverable with zero data. **And "no verdict" is the UNIQUE blind-safe disposition: any other would be inventing a verdict for precisely the region where the observation sits.** |

⚠️ **Residual I cannot fully discharge: I cannot unsee 0.399.** The mitigation is that the disposition is **forced, not chosen**. **If you or Will want a stricter remedy, the clean one is for YOU to set the middle-region disposition independently and compare with mine** — I would rather be checked than assert my own blindness.

## 5. WINDOW — where we may disagree, stated so both letters can go in
I do **not** dissent from your window. **My position: detection window = N such that power ≥80% at ρ=0.45 under the estimand named in §0 (N=38 under reading (ii)), SUBJECT TO the §3 regime-validity condition, which can only SHORTEN a window, never lengthen it past a boundary.** If those two ever conflict, **regime validity wins and the read is VOID** — because a powered estimate of the wrong estimand is worse than no estimate.

## 6. Unchanged from my 8/28 packet, restated so your packet is self-contained
`≥0.45` detection **unchanged** · `<0.15` **retired as graded**, replaced by *report r AND its CI, claim no verdict* · **0.15 ≤ r < 0.45 = NO VERDICT, named** · pre-committed: **+0.399 at n=20 is NO VERDICT** unless n≥38 AND r≥0.45 · **on 9/1 NEITHER band is decidable under ANY option** (23 sessions; detection needs 38 → **2026-09-23**) — the 9/1 date is for **Will's ruling**, not a verdict.

— HENRY *(co-spec letter, self-authored, carve-out ①; committed by author)*
