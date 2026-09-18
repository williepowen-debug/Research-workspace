# Oil-in-yen re-benchmark — diagnosis and plan

**Written 2026-09-18 (SAM, Will-directed). Status: PLAN + a completed diagnostic. Nothing adopted; no threshold, gate or figure moved.**

> 🔧 **REVISED 2026-09-18, same day, on CATO findings R2 (HIGH) and R3 (MEDIUM), routed by PROME.** Two causal claims are **WITHDRAWN**: the lag-window hypothesis is **unresolved, not eliminated**, and the +0.835 wedge-level correlation **does not identify** proportional freight/insurance. **Every descriptive figure reproduces and none is disputed.** R3 replaced a wrong benchmark identity and, in doing so, supplied the mechanism that makes the R2 withdrawal correct — see **§3-bis**. *Corrections are written in place with the original claim named, so the change is auditable rather than silently overwritten.*

---

## 0. THE HEADLINE, BEFORE THE DETAIL

The **+22% "Japanese crude premium" is not one defect. It is at least three superimposed**, and today's diagnostic separates them further than the original flag did:

| Component | Size | Status after this diagnostic |
|---|---|---|
| **Structural basis residual** (CIF-vs-FOB freight/insurance + producer differentials) | **+7.73% / $5.45 per bbl** (n=13, sd 4.00) | 🟢 **MEASURED — and it is a RESIDUAL, not an attributed cause.** Present for 13 straight months *while Brent was a defensible benchmark*. **Not a premium**; the components named in this row's label are candidates, not findings. |
| **Slate change and/or war-risk, confounded** | **~+9.4pp / $10.7 per bbl** | 🟠 **REAL but NOT ATTRIBUTED.** See §2 — the two candidates are perfectly confounded in the available data. |
| **Lag-window / pricing-convention timing** | **unresolved** | 🟠 **OVERCLAIM WITHDRAWN 2026-09-18 (CATO R2).** This row read **ELIMINATED** on corr(deviation, Brent momentum) = **+0.07, n=16.** ⛔ **Absence of linear correlation at n=16 does not rule out a material timing contribution**, and the test was never specified well enough to. **Timing is UNRESOLVED, not excluded** — and see §3-bis: ADNOC priced a large share of these barrels **two months ahead of loading** over the whole sample, a documented convention this diagnostic never modeled. |

⛔ **The operative conclusion: re-benchmarking to the slate would "fix" the number while leaving the attribution wrong.** About 8 of the 21.5 points were never a mismatch at all, and the remaining ~9pp cannot yet be assigned between US-crude voyage economics and war-risk premia. A blind re-benchmark absorbs all three into one corrected constant and destroys the evidence that distinguishes them — the exact defect class in `[[finding_crosscheck_with_free_parameter_validates_nothing]]`.

---

## 1. WHAT THE DIAGNOSTIC DID

Instrument: `workbook/TRADE_BALANCE.tsv`, 17 deduped monthly observations (2025-04 → 2026-08). Columns used: `Crude_USD_bbl` (implied landed unit cost from customs value ÷ volume), `Brent_avg_lag` (the script's t−1..t−2 Brent average), `ME_Crude_Vol_kKL` / `Crude_Vol_kKL` (slate mix).

⚠️ **The raw table carries duplicate month rows** (revision re-pulls: 2026-04 ×3, 05 ×3, 06 ×2, 07 ×2). The first pass ran on the raw series and produced a momentum correlation of −0.10 that was an **artifact of duplicate ordering**. Deduped to latest-per-month, the true figure is **+0.07**. *Recorded because the corrupted version looked equally clean.*

**Three hypotheses, three different predicted shapes — this is why the test discriminates:**

| Hypothesis | Predicts | Observed | Verdict |
|---|---|---|---|
| Benchmark mismatch (US crude priced off Brent) | Deviation **steps up** when the slate changes | High-ME mean **+7.73%** → low-ME **+17.15%**, a **+9.4pp step** | **Consistent — but NOT selected; see §2** |
| Lag window wrong | Deviation **correlates with Brent momentum** | **+0.069** (n=16) | 🟠 **NOT REJECTED — verdict withdrawn (CATO R2).** No linear signal against *this* momentum variable, at n=16, against a window that matches no actual producer convention (§3-bis). **Unresolved.** |
| Fixed CIF freight charge | Wedge is a **constant $/bbl** | Wedge **$5.45 → $16.15**; corr(wedge$, Brent level) = **+0.835** | **A fixed $ charge cannot produce a wedge that triples — that much is arithmetic.** ⛔ **Positive attribution WITHDRAWN (CATO R2): +0.835 does NOT identify proportional freight/insurance**, because price level, war regime and slate regime all move together here. "Not fixed" is supported; "therefore proportional pricing" is not. |

**What the +0.835 correlation does and does not buy.** It rules out a *fixed* per-barrel charge as the whole story — arithmetic, not inference. ⛔ **It does NOT identify what replaced it.** Price level, war-risk regime and slate composition are collinear across these 17 months, so "scales with price ⇒ differential-priced OSPs and ad-valorem insurance" is a **hypothesis consistent with the data, not a finding the data selects.** *(Withdrawn as a finding 2026-09-18 on CATO R2; the figure reproduces and is not in dispute.)*

---

## 2. ⛔ THE CONFOUND, STATED PLAINLY

**The slate change and the war-risk period are the same months.** ME share fell below 85% in 2026-04 and Brent went from $67 to $103 on Hormuz/Iran escalation in exactly that window. Every low-ME observation is also a war-premium observation. **n=4.**

So the +9.4pp step is **consistent with** benchmark mismatch and **equally consistent with** war-risk freight and insurance on the surviving ME barrels — and with any mix. **This data cannot separate them**, and no amount of re-weighting inside this dataset will, because there is no month with a changed slate and no war premium.

**What would separate them** (the discriminating observation, registered now so it is not fudged later):
- **A month with the new slate and a decayed war premium.** Brent is now falling through $100 with Petroline still shut. If the wedge is **war-risk**, it compresses as the premium decays while the slate stays ~60% ME. If it is **benchmark mismatch**, the wedge **persists** at the new level regardless of Brent. → **First observation: September trade balance, Oct-21.** This is registered as a prediction candidate (§5).
- Alternatively, **Kuwait/Qatar returning from zero** (Oct-2 METI) would move the slate back without needing the war to end — the mirror-image test.

---

## 3. THE PLAN

### Phase 0 — ✅ DONE TODAY: decompose before rebuilding
Completed above. Deliverable: the three-way split, one hypothesis eliminated, one confound named.

### Phase 1 — Stop reporting a single misleading number (cheap, do first)
`trade_balance_japan.py:381-387` currently prints one deviation against Brent and warns *"OUTSIDE ±20% gross-error band — check FX/lag/parse"*. That message names three candidates and **omits the two that actually matter** (basis wedge, slate mismatch).

**Change:** report the deviation **net of the measured baseline wedge**, and print both numbers:
```
Implied unit cost: $103/bbl
  vs Brent t-1..t-2 avg $85           (+21.5% gross)
  vs Brent + measured basis wedge      (+13.8pp EXCESS over the $5.45/bbl · 7.7% high-ME baseline)
  ⚠️ EXCESS is UNATTRIBUTED — slate mismatch and war-risk are confounded (see rebenchmark plan §2)
```
Widen the band test to fire on the **excess**, not the gross. **This alone removes the false "22% premium" reading without needing any new data source.**

### Phase 2 — Build the slate-weighted reference (the real fix)
Replace the single Brent leg with:

```
reference(t) = SUM over grades g of  w_g(t) x P_g(convention_g(t), loading_month)
             + basis_residual                                  (measured, not assumed)
```
⚠️ **Written as a time-indexed sum deliberately.** The earlier draft had a static `w_ME x Dubai + w_US x WTI + w_other x Brent` identity; **that is wrong twice over** — it fixes a benchmark per region when the convention is per GRADE, and it holds the convention constant across a sample that contains a **2026-11-01 structural break** (R3).
- `w_*` from **METI's monthly origin table** — already being read for the substitution work; it is the same source that produced the 37.0% US figure.
- 🔧 **CORRECTED 2026-09-18 (CATO R3), verified at the producer primary.** The earlier blanket claim — *"Murban/DAS/Arab Light/Oman all price off Dubai/Oman"* — is **WRONG for this historical sample.** **ADNOC announced 2026-07-31 that Murban, Das, Umm Lulu and Upper Zakum move to prompt-month Platts Dubai (PCAAT00) plus an ADNOC differential — effective 2026-11-01.** Until that date they priced off the **ICE Futures Abu Dhabi Murban contract, set TWO MONTHS AHEAD of loading.** Source: [ADNOC press release](https://adnoc.ae/en/news-and-media/press-releases/2026/adnoc-announces-update-to-its-crude-pricing-methodology), fetched and read this session — **not taken on relay.**
- ⇒ **The reference cannot be a constant identity.** It must map **grade → loading month → destination → the pricing convention in force on that date**, and carry a **structural break at 2026-11-01**. Arab Light (Saudi OSP) and Oman are *not* on the same convention the ADNOC grades were. If a single Dubai series proxies the pre-November period, **that approximation must be stated and tested, not assumed.**
- ⛔ **Freight is NOT to be fabricated.** AG–Japan and USG–Japan Worldscale rates are not freely available to this desk. Carry freight as a **named unquantified residual** inside `basis_wedge`, estimated empirically from the high-ME regime, never invented per-voyage.

**Data access is the gating question, not the maths.** Dubai and WTI-Midland assessments are Platts/Argus-licensed. Free proxies: WTI (`CL=F`) is usable for the US leg; for Dubai, the **Brent–Dubai EFS** is quoted in places but not reliably free. ⚠️ **If a clean Dubai series cannot be sourced, Phase 2 does not proceed on a substitute** — it stops, and Phase 1 plus the empirical wedge stands as the answer. A fabricated Dubai proxy would be worse than the current honest defect.

### 🔑 3-bis — WHY R2 AND R3 ARE THE SAME FINDING (added 2026-09-18)

The two corrections arrived separately and interact. **ADNOC's pre-November convention priced a large share of Japan's ME barrels TWO MONTHS AHEAD OF LOADING.** This diagnostic compared landed cost against a **t−1..t−2 Brent average** chosen as a generic "cargo lag" — it never modeled any producer's actual pricing convention, and the dominant convention in the sample was neither Brent nor that window.

⇒ **The timing hypothesis I marked ELIMINATED now has a named, documented mechanism behind it.** That is a stronger argument for the R2 withdrawal than the n=16 objection alone. **A correlation run against the wrong timing variable is not evidence that timing does not matter.**

⇒ It also specifies the real Phase-2 test: build the reference on **convention-correct timing per grade**, then re-measure the residual. **If the residual collapses, timing was material after all** — and the original ELIMINATED verdict would have buried exactly that.

### Phase 3 — Separate the two instruments that are being confused
There are **two** oil-in-yen objects on this desk and they are not the same thing:
- **(a) the forward proxy** — Brent spot × USD/JPY = ¥/bbl. **This gates VECTOR-5 re-open leg (b) at ¥18,000/bbl.**
- **(b) the realized measure** — customs value ÷ volume, the actual landed cost.

**(b) is ground truth for (a).** The elegant fix: use the measured monthly wedge from (b) to **calibrate** (a), so the ¥18,000 gate is read against Japan's *actual* landed cost rather than a benchmark that has run 8–21% below it. ⚠️ **This means the ¥18,000/bbl threshold may be mis-scaled in the same direction** — it was set against a proxy that systematically **understates** the true landed cost. **Flagging, not moving it:** re-scaling a registered gate is a separate decision with its own pre-registration, and is not folded into an instrument repair.

### Phase 4 — Governance until the above lands
- The **+22% stays UNRESOLVED and uncitable** as a cost finding. Unchanged.
- The **~7.7% baseline wedge IS now citable** as a measured basis difference, with its n=13 and sd 4.0.
- **`[[finding_instrument_measures_a_superset_of_the_thesis_subject]]`** applies: the deviation is real, the label "premium" was wrong.

---

## 4. EFFORT AND ORDER

| Phase | Effort | Blocker | Value |
|---|---|---|---|
| 1 — report excess not gross | ~1 session | none | **High — kills the false reading immediately** |
| 2 — slate-weighted reference | 1–2 sessions | **Dubai series access** | High if unblocked; **STOP if not** |
| 3 — calibrate the forward proxy / flag the gate | ~1 session | needs Phase 1 | High — a registered gate depends on it |
| 4 — governance | continuous | none | — |

➡️ **Recommendation: do Phase 1 and Phase 3's flag now; treat Phase 2 as blocked-pending-data and say so, rather than substituting a proxy to make it look done.**

---

## 5. PREDICTION CANDIDATE GENERATED BY THIS WORK

Registered as a candidate, not yet on the board:

> **The September trade balance (Oct-21) shows the excess wedge COMPRESSING** — i.e. the unattributed component above the 7.7% baseline falls — **while ME share stays in the 55–70% band.** That outcome favours **war-risk** as the driver; a wedge that holds at ~+13pp excess with the slate unchanged favours **benchmark mismatch.**

This is the first observation that can break the §2 confound. **Terms must be frozen before Oct-21.**

---

*Diagnostic reproducible from `workbook/TRADE_BALANCE.tsv` with the dedupe-by-month step. Script under discussion: `scripts/trade_balance_japan.py` (`unit_cost_usd_bbl:255`, `market_context:229`, band print `:381-387`). No file was modified by this analysis.*
