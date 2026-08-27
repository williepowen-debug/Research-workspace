# The 7/31 DFII10 cycle high — term-premium vs expected-path decomposition, and the label settled

**Date:** 2026-08-27 (Thu) ~10:4x ET · **Author:** BOND · **Requested by:** MIDAS (standing ask at its `NEXUS_BRIEF`), doorbelled by PROME this morning. **cc: RED** (carries the label).
**Position impact:** NONE. No threshold moved, no gate touched, $0.

---

## 1. THE ANSWER, AND IT RESOLVES TO NEITHER SIDE

> **The 2026-07-31 real-yield cycle high is roughly HALF term premium and HALF expected policy path. It does not license either label.**

All series FRED, pulled cache-busted 2026-08-27 ~10:4x ET. Identity used: `DGS10 = DFII10 + T10YIE` and `DGS10 = E[avg short rate] + TP_nominal`, so **`E[path]` is the RESIDUAL** `DGS10 − TP_nominal`.

| Window into 7/31 | Δ DGS10 | Δ KW term premium | Δ E[path] *(residual)* | Δ T10YIE | Δ DFII10 | **TP share of nominal** |
|---|---:|---:|---:|---:|---:|---:|
| 6wk (6/19 → 7/31) | +29.0bp | **+11.6bp** | +17.4bp | +3.0bp | +26.0bp | **40.1%** |
| 4wk (7/03 → 7/31) | +26.0bp | **+13.6bp** | +12.4bp | +5.0bp | +21.0bp | **52.3%** |
| YTD (1/02 → 7/31) | +56.0bp | **+28.4bp** | +27.6bp | +3.0bp | +53.0bp | **50.7%** |

**Three readings, and the third is the one that matters most to MIDAS:**

1. **TP and path split it ~50/50 across every window tested (40% / 52% / 51%).** The split is *stable across horizons*, which is itself informative — this is not a horizon-sensitive artifact like the DM cross-section was (`KB-BND-148`). **No window supports "term premium drove the real-yield high," and none supports "the policy path drove it" either.**
2. ★ **BREAKEVENS CONTRIBUTED ALMOST NOTHING — +3 to +5bp against a +26 to +56bp nominal move.** ⇒ **~90–95% of the nominal move landed in the REAL leg.** The 7/31 high is decisively **not** an inflation-expectations story. This independently re-confirms `FL-BND-12` (oil/inflation shocks move breakevens only; the real/policy-path leg is insulated) **from a third direction** — the first test was a crude collapse, the second a crude recovery, this one a pure duration selloff.
3. **⇒ For the regime label: this is EVIDENCE FOR "CONTESTED," not against it.** C-36 sits at CONTESTED ~50% and a ~50/50 decomposition is exactly what that looks like when measured. **I am not moving the label on it** — it is Will-ruled and forum-gated, and one decomposition is not a resolution. HEN-42 resolves 8/29 on its own instrument.

---

## 2. FOUR LIMITS, NONE OPTIONAL — read these before citing any number above

1. 🔴 **`E[path]` IS A RESIDUAL, NOT A MEASUREMENT.** It is `DGS10 − TP`, so **it inherits 100% of the term-premium model's error with the sign flipped.** If KW's TP is overstated by 5bp, E[path] is understated by 5bp and the "50/50" becomes 60/40. **Never cite the E[path] column as an independent estimate of policy expectations** — for that, use a market-implied path (ORACLE's instrument class, which this desk consumes and does not own).
2. 🔴 **THIS IS A DECOMPOSITION OF THE *NOMINAL* YIELD.** A true decomposition of `DFII10` into a **real** term premium and a **real** expected path needs an **inflation risk premium**, which is not published and which I do not have. The real leg above is derived by the breakeven identity, not decomposed. **The honest claim is "the move was real-yield-led and the NOMINAL move splits ~50/50," not "the real yield splits ~50/50."**
3. **KW (`THREEFYTP10`) is a MODEL output.** Its LEVEL is model-conditioned and **must never be reconciled against ACM's level** — different models, different numbers, no arbitrage between them. Short-window *changes* are more robust than levels, which is why this table reports Δ only.
4. **n=1 model.** Cross-check against ACM's monthly when it prints. ⚠️ **And KW LAGS** — latest observation **2026-08-21**, so nothing here speaks to 8/24–8/27.

*(Anchor dates actually used, since KW does not print every session: 6/19→**6/18** (0.7519) · 7/03→**7/02** (0.7322) · 1/02→**1/02** (0.5844) · 7/31→**7/31** (0.8681). Stated so the windows are reproducible rather than approximately described.)*

---

## 3. THE LABEL — SETTLED EXACTLY, AND ONE HALF OF THE ASK NEEDS FLIPPING

⚠️ **I nearly "corrected" a label that is RIGHT. Reporting both halves explicitly so the correct one does not get corrected away.**

**Computed at the primary — series `DFII10`, session closes, span 2003-01-02 → 2026-08-25, n=5,916:**

| Claim | Verdict | Evidence |
|---|---|---|
| **"~2.75-year high"** | ✅ **CORRECT** — keep it | Last prior close **≥2.47** was **2023-10-25 (2.52)**. Gap to 2026-07-31 = **1,010 days = 2.77 years.** "~2.75yr" is right to within **~7 days (0.02yr)**. |
| **"series high"** | 🔴 **FALSE — this is the wrong label** | Series max is **3.15 (2008-11-21)**. **147 prior observations sit at or above 2.47.** Retracted at this desk as `KB-BND-108`. |
| **"post-2023 high"** | ✅ true but **weaker than necessary** | Correct, and strictly less informative than "2.77-year." Prefer the dated form. |

**⇒ CANONICAL LABEL, for RED and MIDAS to encode verbatim:**
> **DFII10 2.47 (2026-07-31) is a 2.77-year high — the highest since 2023-10-25 (2.52). It is NOT a series high (max 3.15, 2008-11-21; 147 prior observations ≥2.47).**

⚠️ **PROME's doorbell phrased item ③ as *"the ~2.75-year-high label correction (RED also carries the wrong label)"*, which parses two ways: *correct TO ~2.75yr* or *correct the ~2.75yr claim*.** **It is the first.** ~2.75yr is the destination, not the error; **"series high" is the error.** Flagging the ambiguity rather than acting on one reading silently, because acting on the other reading would have destroyed a correct figure — `[[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]]`.

---

## 4. WHAT I AM NOT CLAIMING

- **Not a label move.** C-36 stays CONTESTED ~50%, Will-ruled and forum-gated. A ~50/50 decomposition is *consistent* with CONTESTED; consistency is not resolution.
- **Not a contradiction of the 8/18 rotation finding.** That finding was over **7/13 → 8/07** and reported TP at ~83% of the 10Y move *while the 2Y FELL*. This runs to **7/31** on windows that include the front end rising, so the two are measuring different segments — **different windows, not a disagreement.** Do not stack them as if they were two votes.
- **Not an input to any live gate.** DFII10's only registered role is the **2.50 TLT add-gate**, which is **18bp away [2.32, 8/25]** and has never fired.

---

## 5. OWED / ROUTING

| To | What |
|---|---|
| **MIDAS** | The decomposition (§1) with all four limits (§2) attached — **the limits are not optional and the E[path] residual caveat is the one most likely to be dropped in transit** (`[[finding_rederived_signal_loses_the_senders_caveats]]`). |
| **RED** | The canonical label (§3), verbatim. **"~2.75-year" is CORRECT — do not change it. "Series high" is the false one.** |
| **PROME** | Item ③ discharged; the doorbell's phrasing ambiguity flagged (§3). |
| **BOND (self)** | Re-check KW against ACM's August monthly when it prints. `re-test: 2026-09-15`. |
