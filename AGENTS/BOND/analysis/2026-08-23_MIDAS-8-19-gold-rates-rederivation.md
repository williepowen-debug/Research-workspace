# BOND — NON-AUTHOR RE-DERIVATION OF MIDAS'S 8/19 GOLD/REAL-RATE ATTRIBUTION

**Written:** 2026-08-23 (Sun ~12:0x ET, markets CLOSED — every figure is a final-for-week print, none live) · **Session:** PROME-spawned orch, full-owner · **Owner:** BOND
**Subject:** MIDAS published "≈89% of the 8/19 gold move unexplained by real rates," then SELF-RETRACTED to a two-factor 61–69% band. That retraction now sits on HEARTBEAT §8, a boot-loaded fleet surface, verified for EXISTENCE only. Nobody had re-run it. This is the re-run, at BOND's own instruments.
**Source read, not the précis:** `AGENTS/MIDAS/reports/2026-08-23_gld-rates-attribution.md` (180 lines, read in full).
**Scope fences honoured:** no MIDAS surface edited · HEARTBEAT untouched · MIDAS-06 (frozen letter, grades 8/28) out of scope · no threshold/band/gate registered · $0 · nothing trade-shaped.

---

## 0. THE THREE ANSWERS, UP FRONT

| # | Question | Verdict |
|---|---|---|
| **1** | Does the DXY-controlled re-base **REPRODUCE** at my pull? | **YES — every headline figure, to 1–3 decimal places, on an independent pull with an independently written estimator.** All eight coefficients, both R² lifts, the beta collapse, the event table, and the base rates reproduce. |
| **2** | Is the **SURVIVING VERDICT** sound, or does the co-symptom argument smuggle in the conclusion? | **SOUND — and the co-symptom claim is TRUE, but MIDAS asserted it without evidence and I have now tested it.** Strip the dollar *by construction* (price gold in the DXY basket / EUR / JPY) and gold still rose **+1.96% / +1.98% / +1.99%** on 8/19. The dollar is not a rival driver. ⚠️ **But the corollary runs the OPPOSITE way from MIDAS's own instruction:** if DXY is a co-symptom, then **61–69% is the wrong number to headline**, and MIDAS's *"every future citation must use the two-factor band"* installs the answer to a different question. |
| **3** | Anything **OVER-corrected**? | **YES — three ways, all measurable, all in the self-critical direction (PAT-122).** The chosen window is the single most self-damaging of five tested; the fitted dollar beta exceeds the arithmetic translation floor; and the mandated-citation instruction contradicts MIDAS's own mechanism argument. **One UNDER-correction too:** the rarity headline is instrument-asymmetric — banded for the residual, point-estimated on the more dramatic leg. |

---

## 1. METHOD — DECLARED BEFORE THE NUMBERS (L-22 compliance)

Independent pull, this session, 2026-08-23 ~11:5x–12:0x ET.

| Element | BOND's choice |
|---|---|
| Real yield | FRED `DFII10`, full series 2003-01-02 → **2026-08-20**, n=6,166 rows / 5,913 non-null. Direct API, cache-busted (`nocache=` param). |
| Gold | yfinance `GC=F` (n=6,518, from 2000-08-30) **and** `GLD` (n=5,473, from 2004-11-18) — both reported, never one. |
| Dollar | yfinance `DX-Y.NYB` (n=9,336, from 1990-01-01). |
| Returns | **log** returns ×100 (MIDAS used simple; the difference is ≤0.07pp on a 3.8% day and changes no verdict — both bases are shown where it matters). |
| **Missing-value convention** | **BOTH**, per L-22: **(a) holiday-bridged** — drop NaN yields, then diff, so a yield change may span >1 calendar day; **(b) interval-matched** — diff in place, then keep only pairs where the yield's prior observation date **equals** the price's prior trading date. |
| Estimator | OLS with intercept, written from scratch (`numpy.linalg.lstsq`), not a library wrapper. R² = 1 − var(resid)/var(y), ddof=0. |
| Window | MIDAS's registered 2024-01-01 → 2026-08-21 for reproduction; **plus 2023-01+, 5y, 10y and full-series for robustness** (§4). |

⚠️ **One instrument-integrity check I ran first, and it nearly produced a false finding of my own.** yfinance's FX pairs `EURUSD=X` / `JPY=X` are stamped **one session LATE** relative to `DX-Y.NYB`: cross-correlation of Δln(DXY) against −Δln(EURUSD) is **+0.820 at k=−1** and only **+0.136 at k=0** (JPY: +0.630 at k=−1, −0.000 at k=0; n=703). Read naively, the FX legs say the dollar was flat-to-stronger on 8/19 while DXY says −0.82% — which would have impeached MIDAS's dollar leg. It does not: shift the `=X` bars back one session and they reconcile exactly (EURUSD **+0.8115%**, USDJPY **−0.8017%** ⇒ DXY **−0.8263%**). **The DXY move is real.** *(`[[finding_instrument_reports_clean_against_the_wrong_reference]]` — caught inward this time. Logged as a fleet-relevant data note: any desk cross-checking a dollar move against yfinance `=X` pairs must date-correct first.)*

---

## 2. ANSWER 1 — IT REPRODUCES

### 2.1 The event table — exact

| Instrument | 8/18 | 8/19 | Δ (mine) | MIDAS | Match |
|---|---:|---:|---:|---:|:--:|
| GLD | 398.55 | 413.84 | **+3.8364%** | +3.8364% | ✅ |
| GC=F (GCQ26) | 4,366.00 | 4,489.40 | **+2.8264%** | +2.8264% | ✅ |
| DXY | 99.65 | 98.83 | **−0.8229%** (simple) / −0.8263% (log) | −0.82% | ✅ |
| DFII10 | 2.41 | 2.35 | **−6.0bp** | −6bp | ✅ |
| DGS10 | 4.71 | 4.65 | −6bp | −6bp | ✅ |
| T10YIE | 2.30 | 2.30 | 0bp | 0bp | ✅ |
| S&P 500 | 7,691.76 | 7,707.98 | +0.2109% | +0.21% | ✅ |
| SLV | 57.44 | 60.01 | +4.4742% | +4.47% | ✅ |

### 2.2 The coefficients — BOND's estimator vs MIDAS's registered table

**Univariate** (Δprice% ~ Δreal-yield bp), window 2024-01-01 → 2026-08-21:

| Series / convention | MIDAS β | **BOND β** | MIDAS R² | **BOND R²** | MIDAS n | **BOND n** |
|---|---:|---:|---:|---:|---:|---:|
| GLD, holiday-bridged | −0.0603 | **−0.0606** | 0.0325 | **0.0325** | 656 | 657 |
| GLD, interval-matched | −0.0691 | **−0.0699** | 0.0413 | **0.0418** | 627 | 625 |
| GC=F, holiday-bridged | −0.0481 | **−0.0483** | 0.0207 | **0.0205** | 657 | 658 |
| GC=F, interval-matched | −0.0563 | **−0.0564** | 0.0274 | **0.0271** | 628 | 627 |

**Two-factor** (+ ΔDXY%):

| Model | MIDAS b_rates | **BOND b_rates** | MIDAS b_usd | **BOND b_usd** | MIDAS R² | **BOND R²** | MIDAS unexpl | **BOND unexpl** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| GLD, interval | −0.0275 | **−0.0284** | −1.289 | **−1.2966** | 0.1648 | **0.1654** | 68.1% | **67.0%** |
| GLD, bridged | −0.0196 | **−0.0200** | −1.307 | **−1.3015** | 0.1626 | **0.1611** | 69.0% | **68.3%** |
| GC=F, interval | −0.0174 | **−0.0175** | −1.207 | **−1.2088** | 0.1354 | **0.1338** | 61.3% | **60.4%** |
| GC=F, bridged | −0.0102 | **−0.0105** | −1.217 | **−1.2088** | 0.1335 | **0.1311** | 62.5% | **61.9%** |

⇒ **Every claim in the retraction reproduces:** the 61–69% band (mine 60.4–68.3%), the R² lift 0.021–0.042 → 0.131–0.165 (a **4–6×** rise, MIDAS's "roughly quadruples" is if anything understated on the GC=F leg where it is 6.4×), and the beta collapse −0.0699 → −0.0284 (GLD) / −0.0564 → −0.0175 (GC=F).

**My n differs by 1–3 rows** from MIDAS's on every cell — log-vs-simple returns and my interval filter's exact tie-handling. **Neither the coefficients nor any verdict is sensitive to it.** MIDAS's L-22 finding stands and I confirm it independently: convention moves β by ~15–19% (bridged vs interval-matched) and n by ~30 rows. **MIDAS's registered −0.0514/−0.0634 remain ~9% off my reproductions in the same direction MIDAS reported** — flatter than interval-matched, steeper than bridged. I could not close that gap either, and I record it rather than paper over it.

### 2.3 The base rates — exact

| MIDAS claim | BOND re-derivation | Match |
|---|---|:--:|
| GLD +3.8364% = 17th-largest of 5,472, top 0.31% | **17th of 5,472 = top 0.311%** | ✅ |
| Days ≥+3.84% by year: 2008:5, 2009:1, 2012:1, 2013:1, 2014:1, 2016:2, 2020:2, **2026:4** | **identical, every cell** | ✅ |
| DFII10 largest 1-day declines: −62bp 2009-03-18, −45bp 2020-03-20, −35bp 2008-12-17 | **identical, and the ordering** | ✅ |
| P(decline ≥55bp) = 1 in ~5,900 | **1 of 5,659 = 0.018%** | ✅ |
| 8/19 DFII10 move = −6bp = 1.16σ | **−6bp = 1.17σ** (σ=5.133bp, n=5,659) | ✅ |

**⇒ ANSWER 1: REPRODUCES. I found no arithmetic, no data and no estimation error in the retraction.** The errors I did find are in **what the numbers were then instructed to mean** (§3) and in **which window and which instrument they were computed on** (§4).

---

## 3. ANSWER 2 — THE VERDICT IS SOUND; THE ARGUMENT FOR IT WAS NOT EVIDENCED, AND ITS COROLLARY IS INVERTED

**The tasking flagged this as the part most likely to be wrong and least likely to be checked, and told me to rule it rather than split it. Ruling it.**

### 3.1 The question, stated precisely

MIDAS's §3.1 argues USD weakness is a **co-symptom** of the same monetary root, not a rival driver. The tasking's framing is exactly right: *if it is a co-symptom it cannot reduce the residual; if it is a partially independent driver it must.* MIDAS **asserted** the co-symptom reading on mechanism grounds ("gold rose because the dollar fell" and "the dollar is being debased" are not competing hypotheses) and offered **no measurement.** A mechanism argument that decides which of two published numbers is authoritative is load-bearing, and it was carried on prose.

### 3.2 The test MIDAS did not run — price the metal in something other than dollars

If the dollar is the *driver*, gold's move is a currency-translation artifact and should largely vanish when gold is quoted against a non-dollar numéraire. If the dollar is a *co-symptom*, gold rose against everything and the move survives translation.

**8/19, log returns, FX date-corrected per §1:**

| Numéraire | Gold (GC=F) move |
|---|---:|
| USD | **+2.7872%** |
| **DXY basket** | **+1.9609%** |
| **EUR** | **+1.9756%** |
| **JPY** | **+1.9855%** |

**⇒ Roughly 70% of the gold move survives the removal of the dollar entirely.** And the three non-USD numéraires agree to within **2.5bp of each other** — this is not one currency's idiosyncrasy, it is broad. **The dollar cannot be the explanation of 8/19.**

**Base-rate the currency-stripped move so it is not just a number:** basket-gold daily returns, n=6,514 (2000-08-31 → 2026-08-21), σ=1.034%. **+1.96% = +1.90σ, the 383rd-largest |move| of 6,514 = top 5.9%; 181 up-days match or beat it = top 2.8%.** A gold day that is top-3% *after the dollar has been removed by arithmetic* is not a dollar story.

### 3.3 Regress the currency-stripped series on real yields — no variance-splitting convention required

This is the construction MIDAS's own §3.1 caveat asks for and does not build. It sidesteps the correlated-regressor problem entirely: strip the currency channel **by construction**, then ask what real rates explain of what is left. Interval-matched, intercept included:

| Series | window | n | b_rates | R² | rates explain | **unexplained** | residual | σ |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **GC=F in basket** | 2024-01+ | 627 | −0.0242 | 0.0057 | +0.145pp | **92.6%** | +1.723pp | 1.33σ |
| **GLD in basket** | 2024-01+ | 625 | −0.0379 | 0.0144 | +0.227pp | **92.3%** | +2.626pp | 2.06σ |
| GC=F in basket | 5y | 1,188 | −0.0309 | 0.0254 | +0.185pp | 90.6% | +1.704pp | 1.58σ |
| GLD in basket | 5y | 1,186 | −0.0393 | 0.0433 | +0.236pp | 92.0% | +2.631pp | 2.52σ |
| GC=F in basket | full | 5,626 | −0.0220 | 0.0116 | +0.132pp | 93.3% | +1.797pp | 1.73σ |
| GLD in basket | full | 5,190 | −0.0352 | 0.0298 | +0.211pp | 92.8% | +2.694pp | 2.63σ |

**⇒ 90–93% of the currency-stripped move is unexplained by real yields, on EVERY window and BOTH instruments.**

### 3.4 THE RULING

**(a) The surviving verdict — "rates-ASSISTED, not rates-EXPLAINED" — is SOUND, and it does not depend on the co-symptom argument at all.** It is robust across all three constructions and every one moves the rates share the SAME way:

| Construction | rates' share of 8/19 |
|---|---:|
| Univariate (MIDAS's original) | 8–15% |
| Two-factor with DXY (MIDAS's retraction) | **3–4%** |
| Currency-stripped (BOND, new) | **7.4%** |

No construction gets rates above 15%, and MIDAS's own retraction moves rates **down**, not up. **The verdict survives whichever frame you adopt — so the co-symptom argument is not load-bearing on the verdict and cannot be smuggling anything into it.**

**(b) The co-symptom CLAIM is TRUE — but MIDAS did not show it, and it happens to be right.** §3.2's translation test is the evidence. This is worth stating plainly because the pattern matters more than this instance: *an unevidenced argument that turns out correct is still an unevidenced argument, and the desk got no credit-worthy check out of it.* **It is now evidenced.**

**(c) 🔴 THE COROLLARY IS INVERTED, AND THIS IS THE FINDING.** MIDAS argues the dollar is a co-symptom — and then rules that **"the magnitude claim is re-based here and every future citation must use the two-factor band"** (§0), installing **61–69%** as the canonical number. **Those two statements contradict each other.** If DXY is a co-symptom of the same monetary root, then a model containing DXY has a **regressor on the causal path** — a mediator, not a control. Regressing an outcome on a co-outcome does not measure how much of the move is explained; it re-describes part of the move in the mirror's units and then reports the mirror as an explanation. **The 61–69% band answers "how much of 8/19 is unexplained by real rates AND a fitted dollar factor." It does not answer "how much of 8/19 is unexplained by real rates," which is the question the premium thesis actually asks.**

⇒ **The correct canonical figure for the debasement question is 87–93% (univariate) or 90–93% (currency-stripped) — i.e. materially CLOSER to MIDAS's ORIGINAL headline than to its retraction.** The 61–69% is a true number about a different question, and it should be published as such rather than as a supersession.

**What MIDAS should have retracted, and did not:** the original 89% was defective for the reasons MIDAS itself names — **R²=0.035, never flagged weak** (L-21 is exactly right, and it is the durable lesson of this whole episode). But the fix for a weak univariate instrument is **to say it is weak**, not to add a mediator and report the residual shrinkage as a correction. `[[finding_univariate_residual_is_a_claim_about_the_model]]` was applied correctly to diagnose and incorrectly to remedy.

---

## 4. ANSWER 3 — YES, OVER-CORRECTED. THREE WAYS, PLUS ONE UNDER-CORRECTION

### 4.1 🔴 The window is the single most self-damaging of five tested, and its extremity was never checked (PAT-122)

MIDAS's registered window is 2024-01-01 → 2026-08. It was inherited from KB-046, **so it was not picked after looking** — that defence holds and I record it. **But the retraction is a NEW claim published on that window with no robustness pass, and the window turns out to be the extreme of the set:**

| px | window | n | b_rates | **b_usd** | R² | **unexplained** | residual σ | rarity (top %) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| GLD | **2024-01+ (MIDAS)** | 625 | −0.0284 | **−1.2966** | 0.1654 | **67.0%** | **1.92σ** | **5.76%** |
| GLD | 2023-01+ | 863 | −0.0312 | −1.1571 | 0.1900 | 69.6% | 2.25σ | 3.82% |
| GLD | 5y | 1,186 | −0.0414 | −0.9267 | 0.2125 | 73.1% | 2.56σ | 2.70% |
| GLD | 10y | 2,380 | −0.0509 | −0.9282 | 0.2545 | 71.5% | 2.99σ | 1.81% |
| GLD | full | 5,190 | −0.0365 | −0.9380 | 0.2013 | 73.6% | 2.67σ | 2.33% |
| GC=F | **2024-01+ (MIDAS)** | 627 | −0.0175 | **−1.2088** | 0.1338 | **60.4%** | **1.23σ** | **14.83%** |
| GC=F | 2023-01+ | 865 | −0.0243 | −1.0636 | 0.1520 | 63.2% | 1.45σ | 10.75% |
| GC=F | 5y | 1,188 | −0.0348 | −0.8635 | 0.1715 | 66.9% | 1.66σ | 7.24% |
| GC=F | 10y | 2,380 | −0.0432 | −0.8567 | 0.1939 | 65.3% | 1.87σ | 5.38% |
| GC=F | full | 5,626 | −0.0238 | −0.9197 | 0.1764 | 67.6% | 1.78σ | 6.84% |

**MIDAS's window simultaneously produces the LARGEST |b_usd|, the SMALLEST unexplained share, and the SMALLEST residual σ of all five — on both instruments.** Every other window gives 63–74% unexplained (vs the published 61–69%) and a **2.25–2.99σ** residual on GLD (vs the published 2.00σ). ⇒ **The published band is the low edge of a 60–74% cross-window range, and the published σ is the low edge of a 1.9–3.0σ range.** *(`[[finding_asymmetric_rigor_counterparty_claims]]`, pointed INWARD: this is the number that makes MIDAS retract, and it got less scrutiny than the number it replaced.)*

### 4.2 🔴 The fitted dollar beta exceeds the arithmetic translation floor — so part of the "dollar" attribution is model, not currency

Pure currency translation has a beta of **exactly −1.000**. It is arithmetic, not an estimate: a 1% weaker dollar mechanically raises a dollar-quoted hard asset 1%, no behaviour required. MIDAS's fitted b_usd is **−1.207 to −1.307** — 21–31% **beyond** the translation floor.

| Instrument | dollar's **arithmetic** (translation) share of 8/19 | MIDAS's **fitted** share | gap |
|---|---:|---:|---:|
| GLD | +0.826pp of 3.765pp = **21.9%** | +1.065pp = **28.3%** | **6.4pp** |
| GC=F | +0.826pp of 2.787pp = **29.6%** | +0.997pp = **35.8%** | **6.2pp** |

**⇒ ~6pp of the 20–28pp MIDAS handed back to the dollar is a fitted amplification estimated on a window where gold and the dollar co-moved unusually strongly (|b_usd| −1.21/−1.30 vs −0.86/−0.94 on 5y/10y/full).** The defensible, assumption-free dollar contribution is the translation figure — and that is precisely §3.2's basket construction.

### 4.3 🟠 The mandated-citation instruction over-reaches its own evidence

*"Every future citation must use the two-factor band"* is a governance instruction, not a finding. §3.4(c) rules it wrong on the merits; separately, it is **over-broad even on MIDAS's own terms** — MIDAS's §3.1 says the two-factor split "is one defensible allocation, not the truth" and publishes both bands, then §0 mandates only one of them. **A caveat that survives in the body but is dropped in the instruction is not a caveat.** ⚠️ **It is now on HEARTBEAT §8 — a boot-loaded surface — where the body's caveat does not travel with it.**

### 4.4 ⚠️ …and one UNDER-correction: the rarity headline is instrument-asymmetric

MIDAS **bands** the unexplained share across both instruments (61–69%) but **point-estimates** the rarity on GLD alone: *"+2.00σ, 33rd of 627, top 5.3%."*

| Claim | on GLD | **on GC=F (the contract-named instrument)** |
|---|---|---|
| Two-factor residual, 2024-01+ | +2.44pp = **1.92σ**, top **5.76%** | +1.59pp = **1.23σ**, top **14.83%** |
| Raw session, all-history up-day rank | 17th of 5,472 = top **0.311%** | 72nd of 6,517 = top **1.105%** |

**The metal's own contract makes 8/19 a top-1% day with an ordinary 1.2σ residual. The ETF makes it a top-0.3% day with a 1.9σ residual.** Both are true; only one was headlined.

**Why the two disagree — and why §1.1's basis check missed it:** GLD rose **+0.978pp more than GC=F** on 8/19 (log), a **1.80σ** ETF-vs-futures gap. The mechanical cause is settlement timing (COMEX floor settle 1:30pm ET vs GLD's 4:00pm equity close) — gold **kept rallying into the New York afternoon**, which is a real market fact and arguably *reinforces* the premium read, but it is **not** a property of the metal's session. 🔴 **MIDAS's §1.1 "basis check" compared GCQ26/GCV26/GCZ26 to each other, found a 1.2bp spread, and concluded 8/19 is "basis-independent." The ETF-vs-futures gap on the very same day is 0.978pp — 81× larger than the spread the check measured.** The check was clean **against the wrong referent**: it validated the leg that did not need validating and never touched the one carrying the headline. `[[finding_instrument_reports_clean_against_the_wrong_reference]]`, n+1.

### 4.5 🟡 Minor: "explained" and "residual" are computed on two different models

MIDAS's *explained* = β·Δx with **no intercept**; MIDAS's *residual* (+2.52pp) **includes** it. On this window the intercept is **+0.082 to +0.114 %/session** (≈ +21–30%/yr — gold's realised drift over 2024–26, not noise). Including it on both sides moves unexplained from 67.0% to ~65.5% on my GLD fit. **Small (~1.5pp) and it does not change a verdict**, but the two published statistics are not from the same model, and a drift term that large deserves to be named rather than silently split.

---

## 5. WHAT I AM **NOT** SAYING

- **I am not defending the original 89%.** It was published off R²=0.035 with no weak-instrument flag. **L-21 is correct and is the durable lesson of this episode**; I endorse it and I would apply it to my own univariate work.
- **I am not re-litigating M1, the composite, MIDAS-06, or any MIDAS score.** Explicitly out of scope; nothing here touches them, and none of my findings would move them if it did — every one is about the *magnitude claim's basis*, not the channel read.
- **I did not verify MIDAS's positioning/COT leg** (§6 falsifier 3) — outside my instruments and outside this tasking.
- **The real-yield LEVEL is mine and it is unchanged by any of this.** For the record, since it is adjacent: **DFII10 published 8/20 at 2.35** (unpublished at my 8/21 close-out, when 8/19's 2.35 was the latest gradeable print). **The 2.50 add-gate distance stays 15bp; `BND-15` is unaffected.**

---

## 6. THE ONE-SENTENCE REPLACEMENT I WOULD PUT TO MIDAS

> **On 2026-08-19 gold rose +2.83% (GCQ26) / +3.84% (GLD) while the 10y real yield fell 6bp (−1.17σ, an ordinary day) and the dollar fell 0.82%. Priced against the dollar basket, against the euro and against the yen, gold still rose +1.96% / +1.98% / +1.99% — so the dollar is a co-symptom, not the driver, and that is now measured rather than argued. Real rates explain 7–15% of the currency-stripped move; 87–93% is unexplained by real rates, on every window and both instruments. The two-factor 61–69% figure is true and should be retained as the answer to a different question — "unexplained by rates AND a fitted dollar factor" — but it must not be cited as the magnitude of the premium, because a co-symptom on the causal path is a mediator, not a control.**

*(Offered as a recommendation to MIDAS via packet. **BOND does not encode it — MIDAS owns that surface.** The HEARTBEAT §8 line is PROME's and Will-gated; returned to PROME, not actioned.)*

---

## 7. WHAT I ROUTED, AND TO WHOM

| To | What | Where |
|---|---|---|
| **MIDAS** | Full finding set §3.4 / §4.1–4.5 + the §6 replacement sentence. **MIDAS encodes; BOND does not touch MIDAS surfaces.** | `outbox/2026-08-23_to-MIDAS_*.md` |
| **PROME** | HEARTBEAT §8 carries the mandated two-factor band without the body's own caveat (§4.3). **Will-gated surface — returned, not actioned.** | this file + SendMessage |
| **Fleet (data note)** | yfinance `EURUSD=X`/`JPY=X` daily bars are stamped **one session late** vs `DX-Y.NYB` (corr +0.82 at k=−1 vs +0.14 at k=0). Any dollar-move cross-check must date-correct first. | `workbook/KB.tsv` |

**Reproduction script:** `/tmp/bond_rederive/` (an3/an5/an6.py) — transient by design; every figure above is restated in-file with its window, n and convention so the file stands alone.
