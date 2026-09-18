# AEOLUS · HURRICANE — run report ADDENDUM: ENSO-conditioned residual ACE

```
run_date:     2026-09-18 (Friday)
parent:       RUN_REPORT.md (same run, not superseded — this ADDS the conditioning to P8)
task:         AEOLUS follow-up — condition the post-Sep-18 residual accrual on ASO ONI
constraint:   MEASUREMENT ONLY. No probability is computed here. AEO-01 is not re-priced,
              not graded, not resolved. That is AEOLUS's, and it is why the ask was made.
writes:       5 rows -> workbook/LOG.tsv. NO rows to SERIES.tsv (see "Why no SERIES rows").
              SOURCES.md and AGENT.md NOT touched, per instruction.
```

---

## 0. THE HEADLINE — YOU WERE RIGHT ABOUT 1998, AND THE CONDITIONING DOES WHAT YOU EXPECTED

**`ASO 1998 ONI = −1.02` — La Niña, and not marginally so.** Confirmed at the primary (`oni.ascii.txt`), not from memory. Neighbours for context: `ASO 1997 = +2.04` (the strong El Niño that preceded it), `ASO 1999 = −1.00`. The 1997-98 El Niño had indeed collapsed and La Niña was in place by ASO 1998.

**So the single year in the entire record that accrued ≥105.931 ACE after September 18 did it under the opposite ENSO state from 2026.**

**And the conditional cells are empty — in every El Niño cell, at every ONI cut, in both windows:**

| Class | 1991-2020 | 1966-2024 |
|---|---|---|
| **El Niño** (ASO ONI ≥ +0.5) | **0 of 8** | **0 of 15** |
| **Strong El Niño** (≥ +1.5) | **0 of 2** | **0 of 3** |
| Neutral | 0 of 15 | 0 of 30 |
| La Niña | **1 of 7** *(1998)* | **1 of 14** *(1998)* |

**The one qualifying year in 59 seasons is La Niña.** ⚠️ **This is a count of zero, not a rate of zero** — see §5 for what the cells will and will not bear.

---

## 1. METHOD

- **Classification instrument:** ASO ONI from CPC `oni.ascii.txt`, pulled with **`regime/SOURCES.md` item ①'s verified command** — I used the owner's command rather than reconstruct a URL.
  ```bash
  curl -s "https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt"
  ```
  **ONI is `regime/`'s instrument. It was READ for a computation, not adopted.** No ONI row was written into `hurricane/workbook/` — per your instruction and the SHARED-INPUT RULE. ENSO values reconcile at `regime/`.
- **Cuts:** El Niño ASO ONI ≥ +0.5 · Neutral −0.5 < ONI < +0.5 · La Niña ≤ −0.5 · **strong El Niño ≥ +1.5** reported separately.
- **Residual:** post-Sep-18 accrual = full-season ACE − **inclusive**-to-date(09-18) ACE — **identical to the P8 definition**, so the unconditional and conditional figures are like-for-like.
- **Thresholds:** `NEED = 105.931` (what AEO-01 requires from 4.3950) · `AEO-01 line = 110.3257`.
- **ACE:** computed by the `SOURCES.md` method from HURDAT2; same parse, re-validated this run at 14.40 mean NS / 7.20 mean HU vs NOAA's published 14 / 7.

---

## 2. WINDOW 1 — 1991-2020 *(like-for-like with the normals period AEO-01's denominator is defined on)*

| Class | n | mean | median | max | min | **≥105.931** | full season **<110.3257** |
|---|---:|---:|---:|---:|---:|---:|---:|
| **El Niño** | **8** | 30.319 | 30.877 | **60.672** (2004) | 2.242 (1997) | **0 of 8** | **6 of 8 = 75%** |
| Neutral | 15 | 48.928 | 45.935 | 104.533 (2005) | 4.863 (1993) | **0 of 15** | 6 of 15 = 40% |
| **La Niña** | 7 | 62.237 | 58.213 | **119.905** (1998) | 13.205 (2007) | **1 of 7** — 1998 | 1 of 7 = 14% |
| **Strong El Niño** ≥+1.5 | **2** | 19.145 | 19.145 | **36.047** (2015) | 2.242 (1997) | **0 of 2** | **2 of 2 = 100%** |

**El Niño members** (yr, ASO ONI, full, residual): 1997 +2.04 / 40.93 / **2.242** · 2015 +2.02 / 62.69 / 36.047 · 2002 +0.78 / 67.43 / 49.550 · 1991 +0.72 / 35.54 / 8.275 · 2009 +0.66 / 52.58 / 11.303 · 2004 +0.58 / 226.88 / 60.672 · 2006 +0.54 / 78.54 / 25.707 · 2018 +0.52 / 132.58 / 48.752

**La Niña members:** 2011 −0.76 / 126.30 / 48.442 · 2020 −0.77 / 180.37 / 92.875 · 1995 −0.81 / 227.38 / 58.215 · 1999 −1.00 / 176.53 / 58.213 · **1998 −1.02 / 181.16 / 119.905** · 2007 −1.05 / 73.89 / 13.205 · 2010 −1.43 / 165.48 / 44.805

---

## 3. WINDOW 2 — 1966-2024 satellite era

⚠️ **Requested as 1966-2025. HURDAT2 currently ends 2024, so the window is 1966-2024.** Not smoothed, not back-filled. **Containment: `ASO 2025 ONI = −0.43` → Neutral**, so 2025's absence **cannot move the El Niño, strong-El Niño or La Niña cells at all** — it can only touch Neutral, where the finding is already 0 of 30. **No pre-1966 data was pooled**, so no pre-satellite ACE low-bias enters any figure here.

| Class | n | mean | median | max | min | **≥105.931** | full season **<110.3257** |
|---|---:|---:|---:|---:|---:|---:|---:|
| **El Niño** | **15** | 26.454 | 16.030 | **72.985** (1969) | 2.242 (1997) | **0 of 15** | **11 of 15 = 73%** |
| Neutral | 30 | 41.452 | 40.078 | 104.533 (2005) | 2.050 (1979) | **0 of 30** | 16 of 30 = 53% |
| **La Niña** | 14 | 54.728 | 53.328 | **119.905** (1998) | 13.205 (2007) | **1 of 14** — 1998 | 6 of 14 = 43% |
| **Strong El Niño** ≥+1.5 | **3** | 26.087 | 36.047 | **39.972** (2023) | 2.242 (1997) | **0 of 3** | **2 of 3 = 67%** |

**El Niño members:** 1997 +2.04 / 40.93 / 2.242 · 2015 +2.02 / 62.69 / 36.047 · **2023 +1.50 / 148.21 / 39.972** · 1972 +1.49 / 35.61 / 2.855 · 1987 +1.49 / 34.36 / 13.523 · 1982 +1.45 / 31.50 / 5.100 · 2002 +0.78 / 67.43 / 49.550 · 1991 +0.72 / 35.54 / 8.275 · 2009 +0.66 / 52.58 / 11.303 · 1986 +0.64 / 35.79 / 3.800 · **1969 +0.61 / 148.31 / 72.985** · 1976 +0.60 / 84.17 / 16.030 · 2004 +0.58 / 226.88 / 60.672 · 2006 +0.54 / 78.54 / 25.707 · 2018 +0.52 / 132.58 / 48.752

---

## 4. THE THREE YOU ASKED ME TO SETTLE

### ① 1998's ASO ONI — **you were right. −1.02, La Niña.**
Confirmed at the primary, not inferred. **The more valuable answer would have been "you're wrong," and it isn't available — the record says what you said it says.**

### ② El Niño years finishing the full season <110.3257
**6 of 8 = 75%** (1991-2020) · **11 of 15 = 73%** (1966-2024). Strong subset: **2 of 2 = 100%** (1991-2020) · **2 of 3 = 67%** (1966-2024).

🔑 **The structure of the exceptions is the more useful finding.** The four El Niño years that finished *above* the line were **already far above 2026's pace on September 18**:

| Year | ASO ONI | **to-date 9/18** | residual | full |
|---|---:|---:|---:|---:|
| 1969 | +0.61 | **75.328** | 72.985 | 148.312 |
| 2004 | +0.58 | **166.208** | 60.672 | 226.880 |
| 2018 | +0.52 | **83.830** | 48.752 | 132.583 |
| 2023 | +1.50 | **108.237** | 39.972 | 148.210 |
| **2026** | *(+1.80 JJA)* | **4.3950** | — | — |

**None of them got there from a quiet September.** More generally: **the lowest to-date-9/18 ACE of ANY 1966-2024 season that finished ≥110.3257, in any ENSO class, is 2022 at 49.433** (La Niña, finished 110.450 — barely over). **2026 stands at 4.3950, roughly one eleventh of the lowest starting point from which that line has ever been reached.**

### ③ Worst case the regime has actually produced from this point
| | max post-Sep-18 accrual | shortfall vs the 105.931 needed |
|---|---:|---:|
| **Any El Niño year, 1966-2024** | **72.985** (1969) | **32.9 units short** |
| **Any strong El Niño year, 1966-2024** | **39.972** (2023) | **65.9 units short** |
| Any El Niño year, 1991-2020 | 60.672 (2004) | 45.3 short |
| Any strong El Niño year, 1991-2020 | 36.047 (2015) | 69.9 short |

---

## 5. 🔴 WHERE THIS IS THIN, AND THE P7 TRAP ONE CONDITIONING VARIABLE OVER

**You asked me not to let you repeat P7. Here is where it could happen.**

### 2023 sits EXACTLY on the strong-El-Niño boundary — and that one choice moves a headline by 33 points

`ASO 2023 ONI = +1.50`, precisely the threshold.

| "strong" defined as | n | max residual | **full season <110.3257** |
|---|---:|---:|---:|
| **ONI ≥ +1.5** (2023 in) | 3 | 39.972 | **2 of 3 = 67%** |
| **ONI > +1.5** (2023 out) | 2 | 36.047 | **2 of 2 = 100%** |

**An inclusive-vs-exclusive choice on a single boundary year takes the strong-El-Niño full-season statistic from 67% to 100%.** I am not picking. **It is your definitional call.**

**2023 also matters on the merits:** it finished at **148.210, above the line** — the **only strong-El-Niño counterexample on the full-season criterion in the whole record.** A record-warm-Atlantic season that overrode the El Niño signal. **It did not, however, do it after September 18** (residual 39.972); it arrived at 9/18 already at 108.237.

### Full cut sensitivity, 1966-2024

| El Niño defined as | n | max residual | mean residual | **≥105.931** | full <110.3257 |
|---|---:|---:|---:|---:|---:|
| ONI ≥ +0.5 | 15 | 72.985 | 26.454 | **0** | 11/15 = 73% |
| ONI ≥ +0.75 | 7 | 49.550 | 21.327 | **0** | 6/7 = 86% |
| ONI ≥ +1.0 | 6 | 39.972 | 16.623 | **0** | 5/6 = 83% |
| ONI ≥ +1.5 | 3 | 39.972 | 26.087 | **0** | 2/3 = 67% |
| ONI > +1.5 | 2 | 36.047 | 19.145 | **0** | 2/2 = 100% |

> 🔑 **The "≥105.931" column is ZERO at every cut, in both windows. That is the one finding that does not depend on the conditioning choice — and it is the only one that doesn't.** Every percentage in the rightmost column moves with the cut. **Quote the zero; treat the percentages as cut-dependent.**

### The strong cell is too thin to carry a headline alone — say so, don't smooth it

**n=2 (1991-2020) and n=3 (1966-2024).** **A zero count at n=3 is not a zero rate and must not be read as one.** I am reporting it because you asked for it, and flagging that **the weight actually sits in the larger cells that say the same thing** — all-El-Niño **n=15, zero**; Neutral **n=30, zero**. The strong cell corroborates; it cannot carry.

### 🔴 2026's own ASO ONI does not exist yet

**CPC's latest published season is `JJA 2026 +1.80`.** ASO requires a complete Aug-Sep-Oct and has not been issued. **2026 is being placed in the El Niño / strong-El Niño class by FORECAST, not by an observed ASO value, and every conditional figure in this addendum inherits that assumption.** Your +1.80 JJA figure is exactly right and is the latest that exists. **When ASO 2026 publishes, re-check the class before re-using these cells.**

### Other borderlines whose class flips on rounding (1966-2024)
1967 −0.40 · 1974 −0.47 · 1976 +0.60 · 1977 +0.45 · 1978 −0.44 · 1983 −0.43 · 1994 +0.47 · 2000 −0.42 · 2004 +0.58 · 2006 +0.54 · 2016 −0.42 · 2018 +0.52.
**Reported as ambiguity, not resolved.** Note that **2004 (+0.58) and 2018 (+0.52)** are two of the four El Niño exceptions on the full-season criterion — **both are weak-El-Niño boundary cases, and both drop out of the El Niño cell at a +0.75 cut**, which is what takes 73% to 86% in the table above.

---

## Why no SERIES.tsv rows

`AGENT.md` fixes the `SERIES.tsv` controlled vocabulary and says **a new instrument needs AEOLUS's approval — do not invent one.** An ENSO-conditioned base rate is a **derived statistic, not a dated instrument observation**, and there is no approved instrument name for it. It is therefore recorded in `LOG.tsv` (5 rows) and here. **If you want it as a standing series it needs a name from you** — same posture as the cat-bond spread proposal in P5.

---

## What I did NOT do

- **No probability.** No conversion of any count into a rate, a likelihood or a confidence interval.
- **No AEO-01 re-price, grade or resolution.**
- **No ONI row written into `hurricane/workbook/`.**
- **`SOURCES.md` and `AGENT.md` untouched** — yours this session.
- **No commits.**
