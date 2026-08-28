# Does the German→US manufacturing lead depend on WHAT drives the German move?
**HANS · 2026-08-28** · Reproducible: `.venv/bin/python AGENTS/HANS/scripts/pmi_ism_lead_test.py`
**Commissioned by Will** after I flagged this as the untested assumption inside this desk's highest-value signal.

---

## THE CLAIM UNDER TEST
Sent to HENRY 2026-08-28, flagged by me as untested:
> *"A fiscal/capex-driven German PMI is a WEAKER ISM lead than a demand-driven one, because the US ISM is not receiving the German fiscal impulse."*

## ⚠️ PROXY PAIR — READ BEFORE QUOTING ANY NUMBER
**The literal series pair is not obtainable free.** ISM was pulled from FRED for licensing; the OECD German confidence series ends 2024-01. So this tests the **mechanism** on the nearest current proxies:

| Role | Series | Source |
|---|---|---|
| **Leader** | German industrial confidence (BS-ICI, SA) | Eurostat / DG-ECFIN BCS |
| **Follower** | US manufacturing industrial production | FRED `IPMAN` |
| **Regime classifier** | German capital-goods **minus** consumer-goods production, YoY | Eurostat `sts_inpr_m` MIG |

**This is not HCOB PMI and not ISM.** A regime *difference* here is evidence the mechanism is real; it is not a measurement of the literal lead.

---

## FINDING 1 — THE CLAIM IS SUPPORTED, BUT THE RIGHT STATEMENT IS SHARPER

**Correlation of German confidence (YoY chg) with US mfg IP (YoY), by lag and regime** — 2000–2026, n≈100 months per regime:

| Lag | CAPEX-LED | DEMAND-LED | Difference |
|---:|---:|---:|---:|
| 0 mo | +0.761 | +0.797 | +0.036 |
| 1 mo | +0.712 | +0.818 | +0.106 |
| **2 mo** | **+0.621** | **+0.801** | **+0.180** |
| 3 mo | +0.555 | +0.776 | +0.222 |
| 4 mo | +0.514 | +0.737 | +0.223 |
| 5 mo | +0.492 | +0.699 | +0.207 |
| 6 mo | +0.457 | +0.661 | +0.203 |

**Decay over 6 months: capex-led 0.304 · demand-led 0.137 → the capex-led lead decays 2.2× faster.**
**Mean gap across lags 2–6mo: +0.207, consistent over five consecutive lags.**

### ⇒ The precise claim, which is NOT what I originally told HENRY
**Contemporaneously the two regimes are equivalent (0.761 vs 0.797). The difference is entirely in FORWARD content.**
> **A capex-led German print is an equally good COINCIDENT indicator and a materially weaker LEAD.**

That is a sharper and more useful statement than *"a capex-led PMI is a weaker signal,"* and it is the version that should travel. **At lag 2 — the exact horizon this desk advertises — the capex-led relationship is 0.62 against 0.80.**

⚠️ **A method note against myself:** the first version of my own script compared only the **best lag** in each regime, found a +0.06 gap, and printed **"NO MATERIAL DIFFERENCE."** That was wrong — **a lead is about forward content, so the question is decay, not peak.** The summary statistic hid the structure `[[finding_output_shape_implies_more_than_the_measurement]]`.

---

## FINDING 2 — 🔴 AND IT CUTS AGAINST MY OWN ATTRIBUTION

**I told HENRY today the current German expansion is capex/fiscal-driven. The hard production data does not show that.**

| German production, YoY | Mar | Apr | May | **Jun 2026** |
|---|---:|---:|---:|---:|
| Capital goods | −5.69% | −3.89% | −2.69% | **−2.49%** |
| Consumer goods | −5.22% | −2.76% | −0.47% | **+1.55%** |
| **Intensity (capex − consumer)** | −0.47 | −1.13 | −2.22 | **−4.04pp** |

**Six-month mean intensity −0.53pp → Germany sits in the DEMAND-LED tercile** (capex-led requires ≥ +4.80pp). **Capital-goods output is still contracting; consumer goods has turned positive.**

**⇒ If that classification is right, my caveat to HENRY is the WRONG caveat for this episode — and the lead is at its STRONGER setting (r≈0.80 at lag 2), making the ISM read MORE reliable than I told them, not less.**

---

## FINDING 3 — THE PARTIAL RECONCILIATION, AND WHAT IT DOESN'T RESOLVE

**German order books are improving sharply while capital-goods output is still falling** — consistent with an order pipeline not yet converted to production:

| Balance | Dec-25 | Mar | Jun | **Aug-26** | Δ |
|---|---:|---:|---:|---:|---:|
| Order books (BS-IOB) | −40.9 | −29.3 | −26.1 | **−24.4** | **+16.5** |
| **Export** order books (BS-IEOB) | −35.7 | −28.3 | −25.8 | **−22.5** | **+13.2** |

**Production data runs only to June; the PMI surge is July–August.** So a defence/data-centre impulse could sit in orders and not yet in output.

⚠️ **But export order books improved nearly as much as total (+13.2 vs +16.5).** **A purely German-domestic fiscal impulse should widen that gap far more than 3.3pp.** That argues the improvement is **broad-based rather than domestic-fiscal** — which weakens the capex attribution further rather than rescuing it.

**Unresolved, and I could not close it:** German capital-goods **new orders** would settle this directly. I could not locate the series on the Eurostat API (`sts_neworders_m` and variants return no value block). **That is the single highest-value follow-up.**

---

## WHAT THIS MEANS FOR HENRY — the correction

| I told HENRY (this morning) | What the test says |
|---|---|
| Expansion is capex/fiscal-driven | 🔴 **Not visible in hard data.** Capital-goods output −2.49% YoY; consumer goods **+1.55%** |
| Therefore a **weaker** ISM lead | 🔴 **Probably the wrong caveat for this episode.** Germany classifies **demand-led**, where the lead is **stronger** |
| Lead is **~2 months** | 🟡 **Proxy pair peaks at lag 1**, not 2. My charter's "~2 months" may be a month long |
| Caveat is untested | ✅ **Now tested. The regime effect is REAL** — 2.2× faster decay, +0.207 mean gap over five consecutive lags |

**Net: the mechanism I warned about is real, but I applied it to the wrong episode.** The caveat should stay in the toolkit and come **off** this particular print until capital-goods orders say otherwise.

---

## LIMITS — the honest ones, not decorative
1. **AUTOCORRELATION IS THE BIGGEST.** YoY series on overlapping 12-month windows: n≈100 monthly observations is **not** ~100 independent ones — effective df is closer to **8–10**. Confidence intervals are far wider than n suggests. **The evidence is the DIRECTION and the CONSISTENCY across five consecutive lags, never the r itself.**
2. **Multiple comparisons:** 7 lags × 2 regimes = 14 correlations. A single-lag gap is noise.
3. **Look-ahead in the split:** terciles use full-sample information not available in real time. Mild, but real.
4. **Proxy pair** (restated): not PMI, not ISM.
5. **Correlation, not causation** — both series load on the global manufacturing cycle, and a common driver could produce the regime difference without German activity causing anything in the US.
6. **Survey vs hard data conflict is unresolved**, see Finding 3.
