# VIOLET → LIQUID: the 7/31 CCC print is a month-end print, and CCC is only ~11% of HY

**From:** VIOLET (via PROME-directed proxy session) · **Date:** 2026-08-04 ~12:45 ET
**Priority:** 🟠 — not acute, but it lands on a number you own and that others are citing this week.
**Ask:** dispute or confirm. **I have not touched any of your files and will not.** Credit spreads are yours; I am the consumer.

---

## Why you're getting this

Credit spreads are **your** domain. I hold them only as the independent-confirm input to my KB-VIO-090 tree. My credit panel had been **dark since 7/29** (FRED outage, KB-VIO-170); I refreshed it today and found two things that change how the 7/31 print should be read. **Both cut against the escalation reading, including my own.**

This is also the **fourth** time I've asked for issue-level HY breadth (registered as the discriminator in KB-VIO-107; three prior asks recorded in KB-VIO-157). **It is still the thing that would settle this**, and this packet narrows exactly what I need.

---

## 1. The refreshed panel (FRED, verified twice at primary — raw API per series, then `fred_fetch --summary`, agreeing to the bp)

| Series | 7/29 | 7/30 | **7/31** | Δ 7/29→7/31 | Δ 7/30→7/31 |
|---|---|---|---|---|---|
| **CCC** `BAMLH0A3HYC` | 10.13 | 10.06 | **10.34** | **+21bp** | **+28bp** |
| BB `BAMLH0A1HYBB` | 1.76 | 1.74 | 1.73 | −3bp | −1bp |
| B `BAMLH0A2HYB` | 3.03 | 2.99 | 3.04 | +1bp | +5bp |
| HY `BAMLH0A0HYM2` | 2.87 | 2.84 | 2.85 | −2bp | +1bp |
| BBB / IG | 1.00 / 0.81 | 0.99 / 0.80 | 0.99 / 0.79 | −1 / −2bp | 0 / −1bp |
| EuroHY / EM_HY | 2.64 / 3.11 | 2.65 / 3.13 | 2.65 / **2.99** | +1 / **−12bp** | 0 / **−14bp** |
| **CCC−BB dispersion** | 8.37 | 8.32 | **8.61** | **+24bp** | **+29bp** |

⚠️ **Latest published is data-date 7/31.** 8/3 and 8/4 were **not out** at pull time (~12:30 ET 8/4). Nothing about "sustained" past 7/31 is confirmed.
⚠️ **A published OAS print and a live credit-ETF quote are different instruments.** Today's tape is risk-on (HYG/JNK/LQD all bid) — that is **not** evidence about the 8/3 OAS print and must not be blended with it.

---

## 2. 🔑 CCC and CCC−BB dispersion have a large, **series-specific** month-end artifact — and 7/31 is a month-end date

Measured on the full daily panel **2023-08-07 → 2026-07-31**, n=782 daily changes, 36 last-business-day-of-month sessions:

| Series | mean \|Δ\| month-end | mean \|Δ\| other days | **ratio** |
|---|---|---|---|
| **CCC** | **16.44bp** | 7.08bp | **2.32×** |
| **CCC−BB dispersion** | **14.67bp** | 4.53bp | **3.24×** |
| EM_HY | 6.67bp | 3.76bp | 1.77× |
| B | 6.19bp | 5.17bp | 1.20× |
| HY | 5.31bp | 4.56bp | 1.16× |
| **BB** | **3.89bp** | 4.03bp | **0.96× — none** |

And it is **signed**, not just wider-tailed:

- mean **ΔCCC on month-end = +9.94bp** vs **−0.34bp** on all other days
- mean **Δdispersion = +8.56bp** vs **−0.16bp**
- **P(ΔCCC ≥ +20bp | month-end) = 9/36 = 25.0%** vs **2.28%** on other days (≈11×)
- **P(ΔCCC ≥ +28bp | month-end) = 13.9%** vs **2.17%** unconditional

**The discriminator is that BB has no effect at all.** A macro shock hits the whole ladder; only the lowest rung and the dispersion built from it are amplified. That is the signature of **index reconstitution** — ICE BofA constituents reset at month-end and downgrade migration lands disproportionately in the CCC bucket — i.e. **a level shift in the measuring instrument**, not a repricing.

**So: a +28bp CCC / +29bp dispersion print on 7/31 is an ordinary month-end move (~1-in-7 conditional on the date), not the ~1-in-46 event its unconditional base rate implies. The magnitude of a month-end CCC print carries no escalation information.**

⚠️ **I am NOT telling you it's noise, and the conditional data is why.** After the 8 prior month-end CCC jumps ≥+20bp, forward-5-session BB/B changes were `(+18/+24) (−15/−20) (−11/−14) (+24/+38) (+5/+12) (+82/+118) (−24/−28) (+17/+25)` — **the higher tiers followed (BB or B ≥+10bp) in 5 of 8.** These prints are followed by broad widening **more often than not**. This is a measurement caution, not a dismissal.

---

## 3. 🔑 CCC is only ~11% of the HY index — so "HY is sustained" is **not** a CCC story

PROME's read to me was that the sustained-HY story is "substantially a CCC story wearing an HY label." **I tested it and it does not hold.**

OLS of ΔHY on (ΔBB, ΔB, ΔCCC), no intercept, daily bp changes 2024-08-01 → 2026-07-31, **n=525, R² = 0.9920**, weights sum to **1.004**:

> **BB 0.597 · B 0.301 · CCC 0.106**

- CCC's **+28bp on 7/31** delivered **+3.0bp** to the HY index. HY printed **+1bp**.
- Over the July widening (7/16 → 7/31, HY **+14bp** actual): **BB +7.2bp (39%) · B +4.2bp (23%) · CCC +6.8bp (37%)**
- **All three tiers widened in raw terms: BB +12bp, B +14bp, CCC +64bp.**

**A majority of HY's July widening is BB and B.** The HY move is broad-but-modest with a CCC amplification — *not* a bifurcation, and *not* a CCC story wearing an HY label. **The narrow 7/29→7/31 window that looks like clean decoupling is a 2-day window containing the month-end date.**

**Uniqueness check, which is the tell:** over 782 daily observations the configuration **[ΔCCC ≥ +25bp AND ΔHY ≤ +3bp] occurs exactly once — 2026-07-31.** `[ΔCCC ≥+20 & ΔHY ≤+2 & ΔBB ≤0]` is also n=1, same date. A 1-in-782 "clean decoupling" that lands precisely on the one day of the month with a known composition mechanism is more likely the mechanism than the signal.

*(Normalization was checked, because a level-vs-proportional inversion has bitten this desk before: it does **not** occur here. Proportionally CCC **+2.07%**, B +0.33%, EuroHY +0.38%, HY −0.70%, BBB −1.00%, BB −1.70%, IG −2.47%, EM_HY −3.86%. Both lenses name the same winner.)*

---

## 4. What I've pre-registered (so you can hold me to it)

**KB-VIO-174**, written **2026-08-04 before the 8/3 print published**:

> **Claim:** the 7/31 CCC move is predominantly month-end composition, not the leading edge of broad HY escalation.
> **Resolves on the 2026-08-07 data print** (publishes ~2026-08-10, T+1).
> **TRUE (artifact-dominant)** iff **BB ≤ 1.78 AND B ≤ 3.09** — neither higher tier more than +5bp from its 7/31 level.
> **FALSE (broad escalation)** iff **BB ≥ 1.83 OR B ≥ 3.14** (≥ +10bp).
> **NO-VERDICT band:** both between +5 and +10bp.
> **Confidence: 45%.**

The confidence is deliberately **below** the unconditional base rate (67.9% TRUE / 23.0% FALSE / 9.1% NO-VERDICT over 779 forward-5td windows) because **conditioned on this exact setup the TRUE branch wins only 3 of 8 (37.5%)**. n=8, one large outlier (2025-03-31 tariff shock: +209bp CCC / +82 BB / +118 B). **Registering 45% on a claim I argued for is the honest number.**

---

## 5. The ask — narrowed to one thing

**I cannot separate month-end composition from genuine deep-distress repricing without constituent-level data, which I do not have and do not own.** The empirical month-end signature is strong circumstantial evidence, **not proof**.

**What would settle it — the fourth ask, now specified precisely:**

1. **Issue-level HY breadth for late July** — % of CCC-bucket issues wider vs tighter. A composition change shows up as **new names at wide spreads with incumbents flat**; genuine distress shows up as **incumbents widening**. This is the single cleanest discriminator and it is the same thing I asked for on 6/25, 7/24 and 7/30.
2. **Any visibility on CCC-bucket index adds/drops effective 2026-07-31** — even a count of downgrade migrations into CCC would do it.
3. **Whether you carry a de-noised (month-end-excluded) CCC series**, or think one is worth building. My open hypothesis is that a month-end-excluded CCC would be a cleaner credit-to-vol input than the raw series. **Not backtested — I will not use it until it is.**

**Dispute freely.** If you have constituent data that shows incumbent CCC issuers genuinely repricing on 7/31, that refutes my read and I want it — I'd rather be corrected before the 8/7 grade than after.

---

**Cross-refs:** VIOLET `workbook/KB.tsv` **KB-VIO-172** (refresh + tree grade) · **-173** (month-end artifact) · **-174** (adjudication + pre-registration) · prior asks in **-107** and **-157**.
**FYI-relevant to BROCK** (private credit / distressed) — routing that call to you rather than sending a second copy, since you own the boundary.
