# Refiner-vs-XLE decoupling distribution — the `TRY-BRENT-REFINER` falsifier series

**Built:** 2026-08-27 ~13:0x ET · **TERRY** (my half of the BRENT/TERRY co-build) · **Script:** `scripts/decoupling_series.py` (reproducible; re-run for fresh marks)
**Window:** `2026-02-27` → present. **Anchor is BRENT's**, verbatim from `AGENTS/BRENT/setups/2026-08-21_row58-shares-leg-thesis-break-observable.md:158` — *"pre-war n=2,770 to 2026-02-26; war n=117 from 2026-02-27"* — **verified at the artifact, not taken on relay.**
**Metric:** refiner 30-period % return **minus** XLE 30-period % return, in percentage points. Positive = refiner outperforming the energy sector = "decoupled."

> ⛔ **NO THRESHOLD IS REGISTERED HERE AND NONE IS PROPOSED. Threshold nomination is BRENT's half.** This file is the distribution he rules against.

---

## 🔴 THE HEADLINE IS NOT THE DISTRIBUTION — IT IS THAT **THE BASIS CHOICE FLIPS THE ANSWER**

**Same claim, same data, two defensible readings of "30d", opposite verdicts:**

| basis for "30d" | VLO today | percentile in the war window | reads as |
|---|---:|---:|---|
| **30 CALENDAR days** *(matches BRENT's own +8.9pp table)* | **+8.55pp** | **71.4%** | decoupling **healthy, above median** |
| **30 SESSIONS** | **+7.03pp** | **42.9%** | decoupling **below median, fading** |

★ **A 28.5-percentile swing produced by a definition, not by the tape.** `[[finding_normalization_choice_picks_opposite_winners]]` — **the disagreement IS the finding.**

⇒ ⛔ **THE BASIS MUST BE RULED BEFORE ANY THRESHOLD IS NOMINATED.** A threshold set on one basis and evaluated on the other is not conservative or aggressive — **it is measuring a different quantity.** *(My first build used 30 sessions and would have handed BRENT a distribution in which his own `+8.9pp` observation does not live — `[[finding_instrument_reports_clean_against_the_wrong_reference]]`, caught by reconciling his table against my output rather than assuming they matched.)*

**Reconciliation of BRENT's `+8.9pp`:** cal-30d **+8.53** · 21-session **+9.57** · 25-session **+9.38** · 30-session **+6.96**. ⇒ **his figure is a CALENDAR-30d measurement.** Recommend cal-30d as the ruled basis on that ground alone — it is the one already in the record — but **the ruling is his.**

## DISTRIBUTIONS — war window `2026-02-27 → 2026-08-27`, **n=126 sessions**, basis = **30 CALENDAR days**

| name | mean | median | sd | p05 | p25 | p75 | p95 | min | max | **today** | **pct** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **VLO** | +6.76 | +5.34 | 5.07 | +0.12 | +3.07 | +9.78 | +16.79 | −2.05 | +22.88 | **+8.55** | **71.4%** |
| MPC | +7.40 | +7.02 | 4.93 | −0.28 | +4.37 | +9.68 | +16.82 | −4.32 | +21.53 | +10.75 | 80.2% |
| PSX | +4.56 | +4.68 | 4.98 | −4.25 | +2.13 | +7.32 | +13.01 | −7.02 | +17.83 | +9.32 | **86.5%** |
| CVI | +6.43 | +4.70 | **13.31** | −10.54 | −2.77 | +12.62 | +35.91 | −14.50 | +45.90 | +10.26 | 68.3% |
| **DINO** | +7.16 | +5.94 | 9.98 | −8.35 | +0.27 | +13.64 | +26.66 | −13.38 | +31.07 | **+0.82** | **27.8%** |

**Three things worth BRENT's attention:**
1. ⚠️ **DINO is the outlier on BOTH bases** (27.8% cal / 25.4% session) — **its decoupling has faded hardest.** It is *not* in the approved position, but it was a named alternative and this is evidence against it.
2. ✅ **CVI's sd is 13.31 vs VLO's 5.07 — 2.6× the dispersion.** **BRENT predicted this before the pull** ("small-cap variance will show as a wider distribution, and that's a real property"). **Confirmed, and it is a genuine cost of the CVI-on-larger-sizing option** — a wider distribution means any threshold set on it fires later and noisier.
3. **PSX prints the highest percentile (86.5%) on the lowest mean (+4.56).** A high reading against a tight, low-mean distribution — **not the same signal as VLO's high reading against a wider one.**

## SUB-REGIME OVERLAY (VLO, cal-30d) — BRENT's requested split, boundaries revised to open at 2/27

| sub-regime | n | mean | median | min | max |
|---|---:|---:|---:|---:|---:|
| 2/27 – 3/31 | 23 | +8.99 | +10.02 | +0.16 | +13.67 |
| 4/01 – 5/31 | 41 | **+3.36** | +3.58 | −2.05 | +8.93 |
| 6/01 – 7/15 | 31 | +8.52 | +7.14 | +2.37 | +18.69 |
| 7/16 – 8/17 | 23 | **+9.01** | +5.58 | +0.83 | **+22.88** |
| **8/18 – now** | **8** | **+4.52** | +5.43 | −0.07 | +8.55 |

⚠️ **The nuance that a single percentile hides: today's `+8.55` is the MAXIMUM of its own sub-regime, and that sub-regime's mean (`+4.52`) is well BELOW the war-window mean (`+6.76`).** ⇒ **today is a strong print inside a softer recent stretch.** ⛔ **n=8 — that sub-regime cannot carry a verdict, and I am not drawing one.** This is exactly why BRENT specified the overlay: the split reaches Will as data rather than as a hidden modelling choice.

## CAVEATS, CARRIED NOT BURIED

- **n=126 here vs BRENT's n=117.** ✅ **Not a defect — different calendars.** His base rate runs on FRED-oil ∩ `BZ=F`; this runs on the US equity session calendar. ⭐ **The anchor is a DATE (`2026-02-27`), never a session count** — do not let a later reader "reconcile" 126 vs 117 as an error.
- **Marks are intraday 8/27**, not closes. Percentiles shift slightly on the settle.
- **`XLE` as the control is a CHOICE**, not a neutral fact: it is ~40% XOM+CVX, so this measures refiners vs *integrateds-plus-majors*, not vs crude itself. A `USO` or `BZ` control would answer a different question and could rank differently. **Named so the control is chosen, not defaulted into.**
- **Survivorship/listing:** all five names traded the full window; no reconstitution adjustment applied to XLE.
