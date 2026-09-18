# Oil-in-yen re-benchmark — diagnosis and plan

**Written 2026-09-18 (SAM, Will-directed). Status: PLAN + a completed diagnostic. Nothing adopted; no threshold, gate or figure moved.**

---

## 0. THE HEADLINE, BEFORE THE DETAIL

The **+22% "Japanese crude premium" is not one defect. It is at least three superimposed**, and today's diagnostic separates them further than the original flag did:

| Component | Size | Status after this diagnostic |
|---|---|---|
| **Structural basis wedge** (CIF-vs-FOB freight/insurance + ME OSP premia to benchmark) | **~+7.7% / $5.45 per bbl** | 🟢 **MEASURED.** Present for 13 straight months *while Brent was the correct benchmark*. **Never a premium — a basis difference the instrument never modeled.** |
| **Slate change and/or war-risk, confounded** | **~+9.4pp / $10.7 per bbl** | 🟠 **REAL but NOT ATTRIBUTED.** See §2 — the two candidates are perfectly confounded in the available data. |
| **Lag-window error** (t−1..t−2 Brent average mis-timing the cargo) | — | 🔴 **ELIMINATED.** corr(deviation, Brent momentum) = **+0.07**, n=16. Not the driver. |

⛔ **The operative conclusion: re-benchmarking to the slate would "fix" the number while leaving the attribution wrong.** About 8 of the 21.5 points were never a mismatch at all, and the remaining ~9pp cannot yet be assigned between US-crude voyage economics and war-risk premia. A blind re-benchmark absorbs all three into one corrected constant and destroys the evidence that distinguishes them — the exact defect class in `[[finding_crosscheck_with_free_parameter_validates_nothing]]`.

---

## 1. WHAT THE DIAGNOSTIC DID

Instrument: `workbook/TRADE_BALANCE.tsv`, 17 deduped monthly observations (2025-04 → 2026-08). Columns used: `Crude_USD_bbl` (implied landed unit cost from customs value ÷ volume), `Brent_avg_lag` (the script's t−1..t−2 Brent average), `ME_Crude_Vol_kKL` / `Crude_Vol_kKL` (slate mix).

⚠️ **The raw table carries duplicate month rows** (revision re-pulls: 2026-04 ×3, 05 ×3, 06 ×2, 07 ×2). The first pass ran on the raw series and produced a momentum correlation of −0.10 that was an **artifact of duplicate ordering**. Deduped to latest-per-month, the true figure is **+0.07**. *Recorded because the corrupted version looked equally clean.*

**Three hypotheses, three different predicted shapes — this is why the test discriminates:**

| Hypothesis | Predicts | Observed | Verdict |
|---|---|---|---|
| Benchmark mismatch (US crude priced off Brent) | Deviation **steps up** when the slate changes | High-ME mean **+7.7%** → low-ME **+17.2%**, a **+9.4pp step** | **Consistent — but see §2** |
| Lag window wrong | Deviation **correlates with Brent momentum** | **+0.07** (n=16) | **REJECTED** |
| Fixed CIF freight charge | Wedge is a **constant $/bbl** | Wedge **$5.45 → $16.15**; corr(wedge$, Brent level) = **+0.84** | **REJECTED as *fixed*; the wedge is PROPORTIONAL to price** |

**The +0.84 correlation is the most useful single number here.** A fixed freight charge cannot produce it. A wedge that scales with the price level is the signature of **differential-priced components** — official selling prices set as a spread to benchmark, and ad-valorem insurance/freight — not a flat per-barrel cost.

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
reference = w_ME x Dubai + w_US x WTI + w_other x Brent      (all FOB)
          + basis_wedge                                       (measured, not assumed)
```
- `w_*` from **METI's monthly origin table** — already being read for the substitution work; it is the same source that produced the 37.0% US figure.
- **Dubai** is the correct benchmark for ME grades (Murban/DAS/Arab Light/Oman all price off Dubai/Oman, not Brent). Using Brent for ME barrels has been a standing error for the whole series, independent of everything else here.
- ⛔ **Freight is NOT to be fabricated.** AG–Japan and USG–Japan Worldscale rates are not freely available to this desk. Carry freight as a **named unquantified residual** inside `basis_wedge`, estimated empirically from the high-ME regime, never invented per-voyage.

**Data access is the gating question, not the maths.** Dubai and WTI-Midland assessments are Platts/Argus-licensed. Free proxies: WTI (`CL=F`) is usable for the US leg; for Dubai, the **Brent–Dubai EFS** is quoted in places but not reliably free. ⚠️ **If a clean Dubai series cannot be sourced, Phase 2 does not proceed on a substitute** — it stops, and Phase 1 plus the empirical wedge stands as the answer. A fabricated Dubai proxy would be worse than the current honest defect.

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
