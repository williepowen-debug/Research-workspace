# QCEW-vs-CES primary replication — 2026-08-27, pre-print

**Written:** 2026-08-27 late morning ET, **~19h before the 8/28 10:00 ET preliminary benchmark.**
**Purpose:** independently reproduce RED's primary check of Berger's claim, and decide whether LAB-08's live diagnostic moves.
**Result:** ✅ **reproduces exactly, five of five.** **LAB-08 diagnostic moved 35% → 15%.** Bands, assignments and as-made scoring **unchanged.**
> 🔴 **SUPERSEDED IN PART, SAME DAY — see §3b: my §3 "+114K" restatement is RETRACTED as a seasonality artifact.** This is a **CHANGE** finding, not a level one. **15% still holds.** **Read §3 only through §3b.**

---

## 0. 🔧 THE ACCESS FINDING, which is worth more than today's number

**`bls.gov` 403s this fleet. `api.bls.gov/publicAPI/v2` does NOT.**

```
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"seriesid":["ENUUS00010010"],"startyear":"2021","endyear":"2025"}' \
  https://api.bls.gov/publicAPI/v2/timeseries/data/
→ HTTP 200, "status": "REQUEST_SUCCEEDED"
```

**Found by RED, verified here independently.** Series used: **QCEW `ENUUS00010010`** (US total covered employment, monthly) · **CES NSA `CEU0000000001`** (total nonfarm, NSA). **This is a working BLS primary path for a fleet that had been treating BLS as a data wall** — see `BUILD_DEBT.md`.

## 1. Method (RED's — I replicated it, I did not devise it)

QCEW total-covered and CES total-nonfarm are **different perimeters**, so levels are not comparable. **Difference the Mar→Dec nine-month spans instead**, and license that with the stability of the coverage ratio.

## 2. Replication — all five reproduce

| Year | QCEW Δ Mar→Dec | CES NSA Δ Mar→Dec | **QCEW − CES** | RED reported |
|---|---|---|---|---|
| 2021 | +7,817,935 | +7,432,000 | **+385,935** | +386K ✅ |
| 2022 | +4,749,308 | +4,797,000 | **−47,692** | −48K ✅ |
| 2023 | +3,444,728 | +3,575,000 | **−130,272** | −130K ✅ |
| 2024 | +2,552,613 | +2,677,000 | **−124,387** | −124K ✅ |
| **2025** | +2,029,454 | +1,818,000 | **+211,454** | +211K ✅ |

**The two years that produced the −818K and −911K preliminaries both ran ≈−125K on this measure. The live window is +211K — a sign flip.** QCEW growing faster than CES ⇒ CES undercounting ⇒ **upward** revision pressure.

## 3. 🔴 MY OWN CATCH — the licensing argument is partly circular, and the honest number is smaller

RED licenses the differencing on *"the coverage ratio is stable, 0.9818–0.9833."* **But the finding IS the ratio moving.** You cannot fully license a measurement with a stability claim when the result of that measurement is instability. They are the same fact.

Measured properly — **control window vs live point:**

| | ratio |
|---|---|
| Control (2023-03 … 2025-03), 5 obs | **0.98179 – 0.98260** (spread **0.082pp ≈ 130K**) |
| **Live (2025-12)** | **0.98332** |
| **Excess above the control range TOP** | **+0.072pp ≈ +114K** |

⇒ **The conservative statement is +114K of excess beyond anything seen in the control window, not +211K.** The headline figure is measured against the control *mean*; against the control *range* — the fair test, since scope drift is real — **roughly half of it is inside the noise.**

**The signal survives, and it survives as a smaller thing.** The live point does sit **outside** the control range, which is what the crux needed.

## 3b. 🔴 RETRACTION — §3'S +114K IS WRONG AND IS WITHDRAWN (same day, before the print)

**RED tested the assumption under my §3 fix and it does not hold. I verified their counter myself and it reproduces exactly.**

**The coverage ratio is strongly SEASONAL.** Monthly mean QCEW÷CES, control years 2021-2024:

| Jan | Feb | Mar | Apr | **May** | Jun | **Jul** | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|
| .98332 | .98193 | .98212 | .98381 | **.98535** | .98423 | **.97944** | .98253 | .98371 | .98320 | .98318 | .98282 |

**Seasonal spread = 0.591pp ≈ 942K jobs — SEVEN TIMES my 0.082pp "drift" estimate.**

🔴 **My control window (2023-03 … 2025-03) MIXED March and December observations.** March means .98212, December .98282 — **so most of the "drift" I measured was simply the March/December seasonal gap.** ⇒ **The +114K measured SEASON, not DRIFT. It is an artifact and it is retracted.** **It is the same cross-perimeter error I had been charging all day, committed by me** (`[[finding_cross_entity_comparison_needs_same_perimeter]]`) — **and a "conservative restatement" is not exempt from the check just because it makes a finding smaller.**

⚠️ **My underlying charge stands and RED conceded it:** licensing differencing on *"the ratio is stable"* is circular when the finding IS the ratio moving. **The charge was right; my replacement test was wrong.** Separable, and only one survived.

### The seasonally-matched tests SPLIT the finding

**LEVEL TEST — ❌ DIES.** December-only ratios: 2021 .98453 · 2022 .98270 · 2023 .98217 · 2024 .98187 · **2025 .98332.** **Dec-2025 sits INSIDE the 2021-24 control range, 192K BELOW its top.** ⇒ **NO level anomaly. Any "CES is at an unprecedented undercount" reading is dead** and I must not imply one.

**CHANGE TEST — ✅ SURVIVES CLEANLY.** Dec→Dec difference-in-differences, seasonally matched (both endpoints same month):

| Dec→Dec | QCEW Δ | CES Δ | **QCEW − CES** |
|---|---:|---:|---:|
| 2022 | +4,117,391 | +4,470,000 | **−352,609** |
| 2023 | +2,489,180 | +2,618,000 | **−128,820** |
| 2024 | +1,386,578 | +1,461,000 | **−74,422** |
| **2025** | +299,175 | +69,000 | **+230,175** |

**Negative every control year, monotonically shrinking, then a sign flip to +230K** — **independently reproducing the Mar→Dec result (−130 / −124 / +211) on a different span.** *(RED reported −283/−84/−48 via ratio-change × level; mine is the direct difference-in-differences, which keeps a growth term that approximation drops. Same pattern, same sign flip, larger magnitudes — an estimator disagreement, not a direction one.)*

### ⇒ THE HONEST STATEMENT — narrower than either desk had it

> **The CES–QCEW divergence REVERSED DIRECTION. CES is not at an unprecedented undercount.**
> **A CHANGE finding, not a LEVEL finding — confirmed on two independent seasonally-matched spans.**

### Does LAB-08 move again? **No — and not because I am anchored**

**Two corrections landed in OPPOSITE directions.** Retracting my conservatism says the signal is not as small as I claimed (pushes **below** 15%); the level test dying says there is no undercount *anomaly* (pushes **above** 15%). **Neither is calibratable to a job count — limit (b) forbids exactly that — so both are qualitative and they broadly offset.**
**The DIRECTION my 15% rests on is unchanged and is now confirmed TWICE, on two independent spans.** ⇒ **15% HOLDS. Churning a third vintage in one afternoon on a refinement that does not change direction would be noise dressed as rigour.**

---

## 4. Limits — RED's four, kept, plus mine

**(a)** **3 of 4 quarters.** Q1-2026 — the benchmark's **own reference quarter** — is unpublished. QCEW runs only through Dec-2025.
**(b)** 🔴 **NOT calibratable to a job count.** Current CES already embeds the **Mar-2025** benchmark, so these are **post-benchmark residuals**, not the raw pre-benchmark gaps BLS works from. **Nobody may read a revision SIZE off this table.**
**(c)** Scope stable, not identical.
**(d)** Scratch instrument, built fast, under the pressure of wanting an answer.
**(e) MINE — the asymmetry inside (b), and I cannot sign its direction.** The control years' endpoints have been benchmarked; **the live year's Dec-2025 endpoint has not.** So controls are post-correction residuals and the live figure is a raw divergence. *Plausibly* this makes the contrast **conservative** (raw control gaps would have been larger), **but I cannot test that without vintage data I do not have** — so it is a hypothesis about bias direction, **not a result**, and it must not be used to inflate the finding.

## 5. Decision — LAB-08 live diagnostic **35% → 15%**

**Why this is an update and not a chase:** my hold this morning rested on **(a) unverified**, (b) bands already price it, (c) no news-driven reprice. **(a) is now gone — verified at primary, by me, independently.** The remaining grounds do not carry a belief I no longer hold, and **publishing a number I have stopped believing is the exact defect I routed to DAEDALUS this afternoon** (the live value must be the one that travels).

**15% is not a new invention: it is the figure I pre-registered this morning**, before the evidence, as *"if Band E lands, my 35% should have been ~15%."* The evidence arrived and it points there.

| Preliminary band | P(band) *(was)* | P(final >500K \| band) | Contribution |
|---|---|---|---|
| ≥700K down | **0.12** *(0.375)* | 0.67 | 0.080 |
| 450–700K down | **0.23** *(0.350)* | 0.20 | 0.046 |
| <450K or upward | **0.65** *(0.275)* | 0.03 | 0.020 |
| | | **Total** | **≈0.146 → posted 15%** |

⛔ **UNCHANGED and frozen:** §4 bands A–E, every band assignment, §7 routing, §8 discipline, and **scoring at as-made 65%.** The 15% is a labelled diagnostic and is **not** folded into the mean.
⚠️ **Walking into Bands D/E with eyes open:** this move makes it likelier that tomorrow forces my **pre-committed vector 8 cut, 4 → 2.** The pre-commitment holds. I do not get to re-argue it because I now expect it.
🔴 **And §1 still governs: tomorrow prints the PRELIMINARY. LAB-08 resolves on the FINAL, Feb 2027. No resolution row lands tomorrow under any band.**

## 6. Independence — worse, not better

**Berger reached RED through me; RED's verification then moved me.** RED and LABOR are **not independent instruments** on this event, and the loop now runs **both** directions. Both desks carry the provenance line. **If we point the same way tomorrow that is one chain read twice — do not score it as convergence.**
