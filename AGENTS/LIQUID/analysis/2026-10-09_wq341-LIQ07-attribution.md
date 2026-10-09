# WQ-341 OBSERVED branch — LIQUID's `LIQ-07` attribution read of the B-tier quiet-session widening (9/29, 10/7; 10/8 out-of-letter)

**LIQUID · Fri 2026-10-09 ~10:2x ET · PROME `prome-75` (Tier 1, pre-authorized by Will 10/3, WQ-341) · ask: `PROME/inbox/2026-10-09_from-NEXUS_wq341-observed-branch-attribution-asks.md` (`4994ec168`).** Attribution only. This read does not grade `LIQ-07`'s S1/S2 funding verdict, which stays separate (§5). It installs no root and no "non-root". No trade words.

**Data:** FRED ICE BofA OAS `BAMLH0A1HYBB` / `BAMLH0A2HYB` / `BAMLH0A3HYC` / `BAMLH0A0HYM2` / `BAMLC0A0CM`, LATEST-REVISED, pct×100 rounded to integer bp. Rates are FRED H.15 `DGS10` / `DFII10`. Everything was pulled via FORGE `fetch.py` on 10/9 ~10:1x ET; history runs 2023-10-10 → 2026-10-08 (FRED's rolling ~3 years, a calm window).
- ⚠️ FRED had no 10/8 `DGS10` / `DFII10` cell at pull time, so the 10/8 rates are NEXUS's Treasury early copy (−6 / −5). **10/8 is OUT-OF-LETTER throughout.**
- **Every model is fitted on 2023-10-10 → 2026-09-23 only**, so the graded window sits out of sample. The models are mine and unreviewed.

## 1. Tier decomposition (bp, d/d; percentile of the d/d against its own 2023-10 → 2026-09-23 history)

| Session | BB | B | CCC | HY | IG | ΔDGS10 / ΔDFII10 |
|---|---|---|---|---|---|---|
| **9/29 (W)** | +6 (p91) | **+7** (p89) | +11 (p90) | +6 | +1 (p83) | +2 / +1 |
| **10/7 (W)** | +4 (p84) | **+6** (p86) | +15 (p93) | +6 | −1 (p22) | +1 / +1 |
| 10/8 (OUT-OF-LETTER) | +5 (p88) | **+7** (p89) | +23 (p97) | +6 | 0 (p54) | −6 / −5 (early copy) |
| *context 10/6* | −8 | −12 | +3 | −9 | −1 | −4 / −4 |
| *context 9/28* | +7 | +9 | +18 | +9 | +2 | +7 / +7 |

- **The move is graded by credit quality across the WHOLE HY ladder (CCC > B > BB), with IG flat.** On each of the three sessions BB moved at its 84th–91st percentile, so B did not move alone.
- **B shows no excess over its usual relation to BB.** Fitted B = 1.25 × BB (no intercept; residual sd 2.38bp). B's excess over that was **−0.5bp [9/29] · +1.0bp [10/7] · +0.7bp [10/8]**, at the 24th–34th percentile of |residual|, i.e. ordinary.
- **What this says about the named mechanism:** at TIER level the B widening is what BB's widening predicts. A cause concentrated in B-rated incumbents would show B moving out of line with BB, and on these three sessions it does not.
- ⚠️ **What it does NOT say:** tier data cannot see issuer composition. The same picture appears if AI-exposed names sit in BB and CCC as well, or if any economy-wide risk-off moves every tier by its beta. VULCAN's issuer read (named B incumbents vs the index) is the composition test, and this does not replace it.

## 2. Sector attribution — **NO_INSTRUMENT (not read)**
NEXUS's ask was to attribute sectors "from verified constituent or sector data, never from memory". I have no verified constituent or sector series reachable from this box:
- ICE BofA sector sub-indices are terminal-only, and FINRA TRACE is gated (standing caveat, STATUS §5).
- FRED carries tiers, not sectors.

So **no sector is attributed here.** My 9/29 "CCO Holdings" attribution was from memory and is withdrawn as evidence. The issuer-level test (bonds, CDS or equities of named B incumbents against the index) is VULCAN's half.

## 3. A1 — lagged rates (prior-session ΔDGS10 / ΔDFII10): the fit, not a verdict

| Model (OLS on daily ΔB, n = 737, fitted to 9/23) | R² | 9/29 fitted → resid | 10/7 fitted → resid | 10/8 fitted → resid (OUT-OF-LETTER) |
|---|---|---|---|---|
| M0 same-day ΔDGS10, ΔDFII10 | 0.065 | −1.1 → **+8.1** | −0.3 → **+6.3** | +1.1 → **+5.9** |
| **M1 = A1: prior-session ΔDGS10, ΔDFII10** | **0.020** | +1.6 → **+5.4** | −1.3 → **+7.3** | +0.0 → **+7.0** |
| M2 = A1 + prior-session ΔB (rebound) | 0.034 | +2.8 → **+4.2** | −2.8 → **+8.8** | +0.8 → **+6.2** |
| M3 = same-day + prior rates + prior ΔB | 0.097 | +1.8 → **+5.2** | −2.8 → **+8.8** | +2.1 → **+4.9** |

Residual sd is 7.6–7.9bp in every model. The 9/29–10/8 residuals sit at the 56th–84th percentile of |residual|.

- **A1 fits poorly.** Prior-session rates explain 2.0% of the daily variance in B. Its fitted values on the two W cells are +1.6 and −1.3bp, against +7 and +6 actual.
- **The "retrace" reading of 10/7 runs the wrong way in history.** The prior-session ΔB coefficient is **+0.12**: B's daily changes show slight momentum, not reversal. After 10/6's −12, the model expects a further *tightening* on 10/7 (fitted −2.8), not +6.
- **10/8 (OUT-OF-LETTER):** B widened +7 on a rates rally. Every rates model fits between 0 and +2bp, so a rates reading leaves +5 to +7 unexplained there too. On the same day CCC moved +23 (p97).
- ⚠️ **What the poor fit does NOT establish:** that rates played no part. Daily OAS is noisy (resid sd ~8bp), a linear two-day model is a weak test, and the fitting history is calm. The statement is narrower: **lagged rates do not account for the two W cells in this model.**

**Base rate (same fit window):**
- On rates-quiet sessions (|ΔDGS10| ≤ 3 AND |ΔDFII10| ≤ 3; 331 days), B widened ≥ +5 on **14.5%** of days and tightened ≤ −5 on **19.0%**.
- The probability of ≥ 2 of 4 such sessions at that rate is **10.3%** (binomial, independence assumed).
- My quiet definition may differ at the margin from NEXUS's letter. NEXUS's letter governs the grade.

## 4. A3 — supply / flows: **UNREAD**
- **HY new-issue calendar 9/29 and 10/7:** no free primary source reachable. Only an anecdote exists: WALTER SIG-W-20261008-049 named two BDC bond deals on 10/8 (Bain Capital Private Credit $350M 5-yr at 7.60%; Hercules $400M 3-yr at 6.70%). They are not an index-supply measure.
- **HY fund flows** (Lipper / EPFR) are paywalled.
- **HYG/JNK shares outstanding** have no free history (STATUS §3, RED context row).
- **A3 is neither supported nor excluded.**

## 5. Kept separate — `LIQ-07` S1/S2 (funding), not graded here
Through 10/8 the funding legs read **0 of 3**:
- SRF max $0.003B;
- SOFR99−IORB max +8 [10/6], so GATE-079 is not armed;
- `sofr_dispersion.py` SOFR75 z −1.1 [10/8].

6 of 10 look-forward sessions have elapsed, and the verdict is due 10/15–16 on the letter.

**NEXUS T-30 — discount-window primary credit:**
- First read: **$9,965M Wednesday level, as-of 10/7** [FRED `WLCFLPCL`]; weekly average $7,701M. That is five straight rising Wednesdays from $5,282M [9/2] and the highest since at least Jan-2024.
- **Second read armed:** as-of Wed 10/14, published Thu 10/15 ~16:30 ET, beside the `LIQ-07` verdict.
- No threshold applies, and the series is not a `LIQ-07` funding leg by the letter.

## 6. What this read hands NEXUS / PROME (attribution, not a grade)

| Question | LIQUID's answer | Confidence |
|---|---|---|
| Is the B move B-specific? | **No, at tier level.** B = 1.25 × BB with ordinary residuals on all three sessions. The whole ladder repriced by quality, and IG did not move. | VERIFIED (FRED, latest-revised) |
| Do lagged rates (A1) explain the W cells? | **Poorly.** R² 0.020; residuals +5.4 and +7.3bp. Rebound runs against the sign in history. | VERIFIED as a fit; INFERRED as to cause |
| Sector composition (A2)? | **Not read.** No verified source; VULCAN's issuer test is the one that can decide it. | NO_INSTRUMENT |
| Supply / flows (A3)? | **UNREAD.** | — |
| The named mechanism (AI disruption at B incumbents)? | Not shown by tier data, and not refuted. Tier data cannot see composition. | UNKNOWN pending VULCAN |

**Vintage guard (NEXUS's):** all cells are latest-revised. If either W cell revises under +5.0, NEXUS re-grades at the 10/13 L554 wake; this read stands against the logged values (+7 / +6).
