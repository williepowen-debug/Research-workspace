# GRADE — the 2026-09-01 synchronised sovereign selloff

**BOND · 2026-09-01 ~22:4x ET · all figures BOND's own cache-busted pulls at the FRED / ECB / BoE / MOF primaries this session**
**Trigger:** WALTER `SIG-W-20260901-006`, which put **BOND on ACTION** and stated explicitly that *"BOND owns the decomposition."* This is that decomposition.

---

## 0. THE HEADLINE: it is not one move. It is TWO, and they have OPPOSITE signatures.

| | window | character |
|---|---|---|
| **Leg 1 — the week INTO 9/1** | 8/26 → 8/31, **fully published** | **100% REAL, monotonically FRONT-LED, bear-FLATTENING** ⇒ policy-path |
| **Leg 2 — the 9/1 session itself** | 8/31 → 9/1, **breakeven leg only** | **BREAKEVENS JUMPED** (+4 to +6bp) ⇒ inflation-expectations |

**Treating them as one "global bond selloff" merges the two things this desk exists to keep apart.** The week into 9/1 was a *policy* event. The 9/1 session has a live *inflation-expectations* component the preceding week did not — and the driver named by the wires (oil +5.2%, Brent BZX26, **BRENT owns the level**) is exactly the shock this desk has a registered channel for.

---

## 1. ⛔ WHAT CANNOT BE GRADED TONIGHT, STATED FIRST

**The H.15 partial split is live right now** (`KB-BND-168`), and it is the binding constraint:

| Series | Reaches | |
|---|---|---|
| `T5YIE` · `T10YIE` · `T5YIFR` | **2026-09-01** | ✅ published |
| `DGS2` · `DGS5` · `DGS10` · `DGS30` | **2026-08-31** | ❌ 9/1 publishes 9/2 |
| `DFII5` · `DFII10` · `DFII30` | **2026-08-31** | ❌ 9/1 publishes 9/2 |

⇒ **The 9/1 session cannot be decomposed into real + breakeven tonight. I have one of the three legs.** **`re-test: 2026-09-02`** — the H.15 split resolves on the next publication and `BND-21` is registered against it. **This is a same-day publication lag, NOT a data wall.**

🔴 **AND I AM NOT INFERRING THE REAL LEG FROM A WIRE NOMINAL.** The wires put the 10Y at ~4.798–4.80 against `DGS10` 4.75 [8/31], which would imply nominal ≈ +5bp and therefore real ≈ +1bp against the published breakeven +4bp. **That arithmetic is basis-mixed** — a wire benchmark quote differenced against a FRED constant-maturity close — and **this desk has already paid for exactly that construction once**: T6's `>5.28` leg graded a `^TYX` intraday against a `DGS30` close and was unreachable by construction. **The number is quoted here as the reason for a confidence, never as evidence.**

---

## 2. LEG 1 — the week into 9/1 (8/26 → 8/31). Fully published, fully gradeable.

| Tenor | nominal | real | breakeven | **real share** |
|---|---:|---:|---:|---:|
| 5Y | **+12.0bp** | **+12.0bp** | +0.0bp | **100%** |
| 10Y | **+9.0bp** | **+10.0bp** | −1.0bp | **111%** |

*(identity `nominal = real + breakeven` closes to 0.0bp residual at both tenors — the decomposition is exact, not fitted)*

**Term structure — monotonically front-led:** `DGS2` **+15.0** > `DGS5` +12.0 > `DGS10` +9.0 > `DGS30` **+7.0**.
**Every curve measure flattened:** 2s10s **47 → 41** (−6.0bp) · 5s30s **81 → 76** (−5.0bp) · 2s30s **99 → 91** (−8.0bp).
**The long-end real did NOT lead:** `DFII30` **+7.0** vs `DFII5` **+12.0** — the real curve flattened 5s30s by **−5.0bp**.
**Breakevens fell:** `T10YIE` −1.0 · `T5YIFR` −2.0.

### ⇒ This is a textbook POLICY-PATH move and it is NOT a term-premium move
A term-premium expansion requires the **long-end real to LEAD** — this desk's own v2 discriminator. It did the opposite, by 5bp. Rising real yields, falling breakevens, monotonic front-leadership and a bear flattener on all three measures is the signature of the market taking **more near-term tightening and less terminal/growth**.

★ **This is an OUT-OF-SAMPLE corroboration of the C-36 ruling made earlier tonight, on data that had not been decomposed when the label was ruled.** C-36 was ruled **two-part** — *policy-path channel ALIVE AND TRANSMITTING · term premium drove the July delta* — on the single 8/28 session. **The full 8/26→8/31 window now says the same thing over five sessions and with the real/breakeven split behind it.** The label was not fitted to this evidence; the evidence arrived after.
★ **And it is the same signature LIQUID registered independently in June** — *"credible-hawkish Fed rallies the long end"* (`KB-LIQ-060`, re-fired as `KB-LIQ-112`). **Two desks, different instruments, same mechanism.**

---

## 3. LEG 2 — the 9/1 session (8/31 → 9/1). Breakeven leg only, and it INVERTS leg 1's character.

| | 8/31 | 9/1 | Δ |
|---|---:|---:|---:|
| `T5YIE` | 2.31 | **2.37** | **+6.0bp** |
| `T10YIE` | 2.31 | **2.35** | **+4.0bp** |
| `T5YIFR` | 2.31 | **2.33** | **+2.0bp** |

**In the week into 9/1 breakevens were flat-to-DOWN. On 9/1 they jumped.** The front (`T5YIE` +6.0) moved more than the 10Y (+4.0), which moved more than the 5y5y forward (+2.0) — **a near-dated inflation impulse that DECAYS with horizon**, i.e. the market is pricing a shock it does not expect to persist. That is the shape an energy shock makes.

### 🔑 This is a LIVE TEST OF `FL-BND-12` — and it is registered, not invented tonight
`FL-BND-12` / `KB-BND-091` is a standing registered channel: **an oil shock is a BREAKEVEN event, and the real / policy-path leg is structurally INSULATED.** It was promoted from INFERRED to TESTED on the ~11% crude collapse, which moved `T10YIE` −7bp with **`DFII10` exactly flat**.

**9/1 is the mirror-image test: a ~+5.2% oil move in the other direction.** The breakeven leg has printed and it behaved as the channel predicts. **The insulation half cannot be checked until `DFII10` [9/1] publishes on 9/2** — so the test is **OPEN, and pre-registered below rather than left to be graded after the fact.**

---

## 4. INTERNATIONAL — like-for-like, and the UK leg is unusable

**8/26 → 8/31, endpoints matched where the primary allows:** EA AAA 10Y **+9.1bp** ≈ US 10Y **+9.0bp** · JP 10Y **+5.1bp** · ~~UK **+1.3bp**~~ **UNUSABLE — the BoE endpoint is 8/27, four days stale.** ⚠️ **`re-test: 2026-09-03`. This is a PUBLICATION LAG, not an unavailable source** — BoE IADB republishes daily and the leg pulled cleanly; saying "unusable" without the re-test would make it self-sealing, which is the class this desk has shipped three times.

⛔ **The min-across-legs bound is NOT quoted here**, because it would be **+1.3bp taken from the stale UK leg** — precisely the coverage artifact documented tonight in `KB-BND-207`. **A bound computed on mixed endpoints is a statement about publication calendars, not about markets.**

**What survives:** **the US and euro-area 10Y moved by the same amount to within 0.1bp** over the fully-published window. That is a real common-factor observation and it is consistent with HANS's independent European read (`FLOW-HANS-9`, ECB QT >€500bn, EZ HICP 3.3%). **It is NOT evidence that Europe is a passenger — over the longer 8/13→8/27 like-for-like the EA leg *led* the DM cross-section at +12.2bp, rank 1/4.**

---

## 5. CREDIT AND FUNDING

| | 8/28 | 8/31 | Δ |
|---|---:|---:|---:|
| HY OAS | 260 | **263** | +3.0bp |
| IG OAS | 79 | **80** | +1.0bp |
| **CCC OAS** | 1026 | **1042** | **+16.0bp** |

**CCC/HY ratio 3.95x → 3.96x.** ★ **The tail widened 5.3× the index.**

⚠️ **Superlative COMPUTED at write time, four parameters stated** (`BAMLH0A3HYC` · daily closes · 2023-09-04 → 2026-08-31 · **n=785**): **1042bp is a FRESH 2026 HIGH.** It is **NOT a series high** — series max **1137bp on 2025-04-07** — and **13 observations sit at or above 1042**, distributed **2023: 1 · 2024: 1 · 2025: 10 · 2026: 1 (this one)**. ⇒ **Elevated and unremarkable against 2025, not unprecedented.**
**Read unchanged: a widening tail against an inert index with zero pulled deals is a repricing of the worst credits, NOT a market-function event.**

**SOFR − IORB flipped POSITIVE: +3bp [8/31]**, from −2/−1/0/+1 all week. ⚠️ **8/31 is month-end and month-end SOFR firmness is routine — this is NOT called as funding stress.** But it is a named input to `DEALER_CAPACITY`'s forced-de-risking discriminator, so **it must be re-read on 9/1–9/2: if it does not normalise, the FR2004 11-21Y re-build re-reads as forced rather than benign.**

---

## 6. GATE CHECK — **the selloff fired NOTHING NEW**

| Gate | Current | Threshold | Distance | State |
|---|---:|---:|---:|---|
| **DFII10 ≥2.50** — the only live TLT-put add-gate | 2.44 [8/31] | 2.50 | **6bp** | **NOT FIRED** |
| T5YIFR >2.50 | 2.33 [9/1] | 2.50 | 17bp | NOT FIRED |
| HY OAS >300 | 263 [8/31] | 300 | 37bp | NOT FIRED |
| CCC/HY >1100 | 1042 [8/31] | 1100 | 58bp | NOT FIRED |
| DGS30 >5.00 | 5.25 [8/31] | 5.00 | — | **already breached, 40-session run** |
| DGS10 >4.50 | 4.75 [8/31] | 4.50 | — | **already breached** |

**The two "fired" rows were already breached long before 9/1 and are not news.** ⇒ **A multi-decade-high tape across four sovereigns moved NO pre-registered line on this desk.** That is the disciplined finding and it is the one most likely to be lost in the noise: **the levels are historic and the thesis is exactly where it was.**

**Position UNCHANGED: TLT puts HOLD, no add.** Will's standing 7/16 NO-ADD governs; root rule #5 means no add executes without [Approve].

---

## 7. 🔴 THE CROSS-DESK PROBLEM — "gold fell, so it's real rates" is NOT safe for 9/1

WALTER's `consumer_lens` reads: *"they moved TOGETHER on a real-rate/inflation-expectations story, not a flight-to-quality — gold fell with bonds."*

- **For LEG 1 that inference is exactly right** — the week was 100% real, and gold falling is what that produces.
- **For the 9/1 SESSION it is in tension with the published data.** Breakevens rose **+4 to +6bp** on 9/1, which is **gold-POSITIVE**. Gold fell **−2.35%** anyway (relayed via WALTER/REGINALD; **MIDAS owns the level**).

**Candidate resolution, and it is MIDAS's own finding rather than mine:** MIDAS's pre-registered positioning falsifier **fired against their own read on 8/28** — gold COT **net/OI 56.86%** [as-of 8/25], composition **CHASED** (non-commercial longs **+20,257**, shorts −888, OI +21,697). **A measurably crowded spec long unwinds hard on any adverse move, with or without a real-rate impulse.**

⇒ **Routed to MIDAS, not ruled here.** Gold is their instrument class and the debasement tell is their call. **What this desk asserts is only the rates half: the 9/1 breakeven leg rose, which does not sit comfortably beside a real-rate reading of gold's fall on the same session.**

---

## 8. WHAT THIS CHANGES

- **Composite: 12/35, UNCHANGED.** No vector moved. Nothing crossed a pre-registered line.
- **C-36: no change — and CORROBORATED** on out-of-sample data the ruling did not use.
- **`FL-BND-12`: under live test**, open until 9/2, pre-registered as `BND-21`.
- **`FL-BND-11`: untouched.** Nothing here bears on the intervention funding channel.
- **Position: UNCHANGED.** $0.

**The honest one-line grade: a historic-looking tape that decomposes into an ordinary policy-path repricing followed by an energy-driven breakeven bump, firing no gate — with the one genuinely open question (whether the real leg stayed insulated on 9/1) not answerable until tomorrow, and registered rather than guessed.**
