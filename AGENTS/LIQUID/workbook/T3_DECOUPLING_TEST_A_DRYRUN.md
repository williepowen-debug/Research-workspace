# T3 / Test A — DECOUPLING DRY-RUN (DOCKET 2026-09-01)
**Run:** 2026-08-28, data through **obs 2026-08-27** · **Owner:** LIQUID (test design) / HENRY (numeric bands, Phase 2) · **Tool:** `scripts/t3_decoupling.py` (built this session, reproducible)
**⛔ THIS GRADES NOTHING.** Dry-run only, as instructed. No verdict is recorded, no threshold moves, and the 9/1 read is pre-registered below rather than pre-empted.

---

## 0. The frozen letter, quoted before anything is computed

> **T3 · Test A — DXY-residual:** *"Regress 20-sess ΔHY and ΔVIX on ΔDXY; correlate residuals. **<0.15 ⇒ shared factor is the dollar; ≥0.45 ⇒ ~1.5 near the ceiling**"* — first read **~early Sept** · ⚠️ **UNDER-POWERED (~9 of 12 windows)**
> *(`FORUM/2026-08-10_financial-conditions/04_synthesis/06_HENRY_joint-synthesis-FINAL.md`, T3; DOCKET row 21.)*

## 1. THE HEADLINE, AND IT OVERTURNS THE DOCKET'S OWN PREMISE

> 🔴 **The test is NOT adequately powered on 20 sessions — and WAITING DOES NOT FIX IT.**
> **DOCKET row 21 reads *"UNDER-POWERED (~9 of 12 windows) until ~early Sept — register, do not act before."* That sentence treats power as a function of the CALENDAR. It is a function of the WINDOW LENGTH, and the window is always 20 sessions.** Arriving at 9/1 adds **zero** power to a 20-session statistic. ⇒ **At this spec the test is not "under-powered until early September." It is PERMANENTLY under-powered, and 9/1 was never the binding constraint.**

## 2. Interim value — reported with its uncertainty, never alone

**Basis, declared:** HY = FRED `BAMLH0A0HYM2` (EOD, T+1) · VIX = FRED `VIXCLS` (EOD **close**, not intraday) · Dollar = **`DX-Y.NYB`**, the ICE index the letter actually names, raw unadjusted closes. First differences on the **common trading-day index** of all three. Statistic = **partial correlation** of the two OLS residual series (k=1 control).

| | |
|---|---:|
| Window | **20 sessions of deltas, 2026-07-31 → 2026-08-27 (n=20)** |
| Raw corr(ΔHY, ΔVIX) | **+0.352** |
| **Partial corr of residuals on ΔDXY — the letter's statistic** | **+0.399** |
| 95% CI (Fisher-z, df = n−3−k = **16**) | **[−0.067, +0.722]** · width **0.790** |
| ΔDXY betas | ΔHY **−0.622** bp/unit · ΔVIX **+0.979** pts/unit |

**Band placement: +0.399 falls in 0.15–0.45 — the INTERMEDIATE zone for which the frozen letter names NO verdict.** Even taken entirely at face value and ignoring power, **the letter has no reading for the value actually observed.**

## 3. Power — the question PROME asked, stated as a test

**Test:** Fisher-z transform of a partial correlation, two-sided, α = 0.05, se(z) = 1/√(n−3−k) = 1/√16 = **0.250**.

| True ρ | Power to reject ρ=0 at n=20 |
|---|---:|
| **0.15** *(the letter's lower band)* | **9.3%** |
| 0.30 | 23.6% |
| **0.45** *(the letter's upper band)* | **49.2%** — worse than a coin flip |

> 🔴 **And the decisive one: the 95% CI [−0.067, +0.722] CONTAINS BOTH BANDS SIMULTANEOUSLY.** It contains values <0.15 **and** values ≥0.45. **A single 20-session read therefore cannot distinguish *"the shared factor is the dollar"* from *"~1.5 near the ceiling"* — the two conclusions the test exists to choose between.** That is not a marginal-power complaint; the instrument cannot separate its own two outcomes.

**What n would actually be required** *(same test, same α)*:

| Requirement | n |
|---|---:|
| 80% power to reject ρ=0 at true ρ=**0.45** | **38** |
| 80% power to reject ρ=0 at true ρ=**0.15** | **348** |
| CI at the observed r=0.399 excludes the <0.15 band | **≈60** |
| CI lands strictly *inside* 0.15–0.45 (excludes both) | **≈200** |

⇒ **The `<0.15 ⇒ shared factor is the dollar` band is the expensive one: establishing a near-null needs ~348 sessions (~17 months).** ⚠️ **You cannot demonstrate a null with 20 observations, and the letter's lower band asks for exactly that.**

## 4. ⚠️ A SECOND SPEC GAP: "ΔDXY" is ambiguous, and the ambiguity is worth almost the whole lower band

| Dollar series | Window | Partial r |
|---|---|---:|
| **`DX-Y.NYB`** (ICE DXY — what the letter names) | 7/31 → 8/27 | **+0.399** |
| **FRED `DTWEXBGS`** (Nominal Broad Dollar) | 7/27 → 8/21 | **+0.252** |

**Spread = 0.147 — almost exactly the full width of the `<0.15` band.** The letter says *"ΔDXY,"* which names the ICE 6-currency index, but nothing in the frozen text forbids the broad-dollar substitution and a grader reaching for FRED would land on `DTWEXBGS` by default. ⚠️ **They are not even the same window:** `DTWEXBGS` publishes with a lag, so its latest obs is **8/21** against DXY's **8/27** — a substitution silently changes the window as well as the series. **Returned to PROME as a definition item; I am not resolving it unilaterally on a frozen forum letter.**

## 5. PRE-REGISTRATION for the 2026-09-01 read — fixed now, before the number is known

1. **Dollar leg = `DX-Y.NYB`** (the letter's named index), raw unadjusted closes. *(Only if PROME/Will rule otherwise does this change; the alternative and its 0.147 effect are named above so neither can be chosen after the fact.)*
2. **HY = `BAMLH0A0HYM2`; VIX = `VIXCLS`** — both EOD closes. **The 8/31 and 9/1 HY observations publish T+1**, so a 9/1 read that needs 9/1 data is `UNGRADEABLE-PENDING-PUBLICATION`, never `NOT-FIRED` *(PROME lagged-series class ruling 8/27)*.
3. **20-session first differences on the common trading-day index of all three series.**
4. **Report `r`, its 95% Fisher CI, AND the power table. Never `r` alone.**
5. 🔴 **PRE-COMMITTED VERDICT RULE: if the CI spans both bands — which on n=20 it structurally will — the read is recorded `UNGRADEABLE-UNDERPOWERED`, with the point estimate shown and NO band verdict attached.** Registered **now**, with the interim r already known to be +0.399, so this cannot later look like an escape from an unwelcome number.
6. **The point estimate is reportable as colour; it is not a finding.** Nothing on any LIQUID surface may cite a T3 band verdict from a 20-session read.

## 6. What I am NOT claiming

⛔ Not that HY and VIX are decoupled. ⛔ Not that they aren't. ⛔ Not that the dollar is or isn't the shared factor. **The honest statement is that this instrument, at this window, cannot answer its own question — and that is a finding about the TEST, not about the market.**
**Successor options for the 9/1 sitting, offered not adopted:** (a) lengthen the window to ≥60 sessions and re-band; (b) keep 20 sessions but re-cast the bands as *decision* thresholds explicitly not claiming inference; (c) retire Test A and lean on Test B/C. **HENRY owns the numeric bands and should rule (b) vs (a).**

---

## 7. ⚠️ BLINDNESS DISCLOSURE for the v2 re-spec — filed 2026-08-28 13:5x ET, BEFORE any v2 drafting begins

**Will ruled ~14:0x ET that LIQUID leads a T3 v2 re-spec (WILL_QUEUE row 113; HENRY co-specs).** PROME's constraint (1) requires the v2 window be **sized by power analysis per band, written BLIND to where the known interim `r = +0.399` would land.**

🔴 **I cannot be literally blind — I computed r before the ruling existed, it is +0.399, and it is published above. Pretending otherwise would be the dishonest version of compliance.** So I am fixing the reasoning *now*, before drafting, and stating exactly what the n figures do and do not depend on:

> **`n = 38` (80% power at ρ=0.45) and `n = 348` (80% power at ρ=0.15) are functions of ONLY: the band value ρ, α = 0.05, two-sided, and the Fisher-z standard error `1/√(n−3−k)` with k = 1 control.** **The observed r appears nowhere in either calculation.** Substituting any other observed value — 0.0, 0.9, or an unknown — returns the identical 38 and 348. **They are blind by construction, not by discipline**, which is the only kind of blindness that survives the author already knowing the answer.

**What I must actively guard against, named in advance so it can be checked against the delivered letter:**
1. ⛔ **I must not choose the window so that 20-session-r ≈ +0.399 lands in a band.** The interim value sits in **0.15–0.45**, the zone v1 gives no verdict for — so **any v2 window that happens to make +0.399 "certify" as something is a red flag on my own work, not a result.**
2. ⛔ **I must not set the no-verdict band to bracket +0.399** for comfort. Constraint (3) already forbids a no-verdict band equal to the whole CI; I add that it must not be centred on the value I happen to hold.
3. ✅ **If the power-derived n does happen to certify the interim value, constraint (1) requires me to SAY SO and justify n from power alone.** Pre-committing: I will state it in the v2 letter with the arithmetic, not bury it.
4. ✅ **Sequencing honoured:** PROME instructed the re-spec be taken **after** the 15:33 W1 re-grade. **No v2 drafting has occurred and none will before that grade is filed.** This section is a disclosure, not a draft — it contains no proposed window, band, or series.

**Why this is filed rather than remembered:** the whole reason the v1 letter needs re-speccing is that its bands were set without a power calculation and nobody could later reconstruct what drove them. **A v2 whose provenance is undocumented would repeat that failure at a higher level of sophistication.**
