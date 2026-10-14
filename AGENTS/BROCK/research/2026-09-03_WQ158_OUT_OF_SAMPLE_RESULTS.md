# WQ-158 OUT-OF-SAMPLE PULL — RESULTS
*Spec frozen BEFORE the data at `research/2026-09-03_WQ158_OUT_OF_SAMPLE_PREREG.md`, commit **`bb924839e`**. Every rule applied below was written there first. Commissioned by Will 2026-09-03.*

## VERDICT — decision-rule branch **"persistence reached, `<20%` not"** (§5, fixed in advance)
| Level | Result | Basis |
|---|---|---|
| **`≥3 consecutive sub-100%` quarters** | ✅ **REACHED at BOTH referents — 4 of 4 quarters each** | BREIT + SREIT, filing-primary |
| **`<20%` single-QUARTER satisfaction** | ❌ **NOT REACHED at either.** BREIT worst **24.6%**, SREIT worst **40.0%** | quarterly aggregation per §3 |
| `<20%` single-MONTH | ✅ reached at BREIT (**4%** Dec-22 · 15% Mar-23 · 17% Jun-23); ❌ not at SREIT (min **20.0%**, not *below*) | monthly, recorded separately per §3 |

⇒ **The `≥3 consecutive` leg SURVIVES — it is comfortably reachable in a real wrapper-redemption stress.** ⇒ **The `<20%` leg does NOT survive at the quarterly unit.**

🔑 **THE FINDING THAT DECIDES IT, AND IT CUTS AGAINST MY OWN PANEL'S SEVERITY STORY:** my register's observed minimum — **OCIC 23%** — is **BELOW BREIT's worst quarter (24.6%) and far below SREIT's (40.0%).** So `<20%` was placed **beneath the worst quarter of the two most severe non-traded-wrapper redemption episodes on record.** **It is not a stress threshold; it is a beyond-stress threshold.** That is why it cannot fire, and it is not a panel-depth problem — it is a level problem.
🔑 **AND THE UNIT IS THE WHOLE ARGUMENT** (pre-registered §3 as a trap, and it sprang): `<20%` is unreachable quarterly and reachable monthly. **My register never stated the unit.** BCRED/CCLFX are quarterly-tender ⇒ the quarterly reading is the binding one for my panel.

## 1 · BREIT (CIK 1662972) — monthly, all from Item 5 footnotes, filing-primary
*"the Company fulfilled X% of requested repurchases in [month]"* — **this is the issuer's own proration percentage, my §2 preferred measure.**

| 2022 | Nov **43%** · Dec **4%** | (Oct-22 **NOT MEASURABLE** — no proration disclosed; per §3 that makes **2022Q4 NOT MEASURABLE**, excluded) |
|---|---|---|
| **2023** | Jan 25 · Feb 35 · Mar 15 · Apr 29 · May 30 · Jun 17 · Jul 34 · Aug 43 · Sep 29 · Oct 56 · Nov 67 · Dec 53 | 12 measured months |

**Quarterly (Σ accepted ÷ Σ submitted, shares, per §3 — NOT a mean of monthly rates):**
`2023Q1 226,504,448 / 920,763,933 = **24.6%**` · `Q2 224,788,515 / 869,544,998 = **25.9%**` · `Q3 216,528,244 / 605,027,445 = **35.8%**` · `Q4 207,019,924 / 349,373,051 = **59.3%**`
⚠️ **Rounding sensitivity stated because the disclosed percentages are whole numbers:** the minimum quarter moves **24.0% → 25.2%** across ±0.5pp. **The `<20%` conclusion is robust to it.**
**Sources:** FY2022 10-K `0001662972-23-000030` · Q1 10-Q `…-23-000054` · Q2 `…-23-000091` · Q3 `…-23-000120` · FY2023 10-K `0001662972-24-000036`.

## 2 · SREIT (CIK 1711929) — monthly, Item 5 footnotes
*"X% of each stockholder's repurchase request was satisfied in [month]"* — **plus requests as % of NAV, so BOTH legs are disclosed.**
Nov-22 63 · **Dec-22 20.0** · Jan-23 38.6 · Feb 49.6 · Mar 30.4 · Apr 47.7 · May 47.8 · Jun 32.9 · Jul 55.3 · Aug 51.3 · Sep 31.3 · Oct 44.9 · Nov 52.5 · Dec 37.9 **(14 months)**
**Quarterly:** `2023Q1 **40.0%**` · `Q2 **43.7%**` · `Q3 **46.5%**` · `Q4 **45.7%**` — **4 consecutive sub-100%.** *(2022Q4 excluded: Oct-22 not disclosed ⇒ NOT MEASURABLE per §3.)*
⚠️ **Structural note, stated because it matters for commensurability:** SREIT's disclosed satisfaction is arithmetically **cap ÷ requests** (Jan-23: 2.0/5.2 = 38.5 ≈ 38.6). §2 permits it — **the ISSUER states it as the realised pro-rata rate**; what §2 forbids is *me* computing cap÷requests as an assumption. **BCRED's ~50% (5%÷~10%) has the identical structure.** ⇒ **BREIT, SREIT and BCRED are commensurable on this measure.** CCLFX is not (below).

> **INFERENCE CORRECTION October14,2026 (CATO BCR4):** requested amounts and realized proration/full-fulfilment language are absent in the checked N-CSR. Exactly7% repurchased does not prove oversubscription, and lower repurchases alone do not prove every valid request met. The September3 deductions below about three full offers/last partial offer are WITHDRAWN; all four satisfaction outcomes remain UNKNOWN from this source. The table, NAVs and withdrawal of the earlier stress-series interpretation stand. Current structured register/KB/STATUS corrected.

## 3 · CCLFX (CIK 1735964) — ⛔ **SATISFACTION IS NOT MEASURABLE. The pull answers in the NEGATIVE, definitively.**
**N-CSR `0001213900-26-066324` (FY ended 3/31/26), note "Repurchase Offers", verbatim table — it CONFIRMS my register's series to the dollar and dates it:**

| Repurchase pricing date | 2025-06-09 | 2025-09-08 | 2025-12-09 | 2026-03-10 |
|---|---|---|---|---|
| NAV Class I | $10.76 | $10.72 | $10.67 | $10.52 |
| Amount repurchased Class I | $1,025,311,527 | $917,546,316 | $1,756,725,615 | **$2,344,027,419** |
| **% of outstanding shares repurchased** | **3.42%** | **2.90%** | **5.32%** | **7.00%** |

🔑 **The table discloses ONLY the amount REPURCHASED. There is no shares-TENDERED row anywhere in the filing.** ⇒ **Per §2, satisfaction is NOT COMPUTABLE and I do not back into it.** ✅ **This confirms, at primary, exactly what I flagged to PROME on 9/3: my register's CCLFX cell is a FULFILMENT series, not a satisfaction series, and cannot grade a satisfaction threshold at all.**
**CORRECTED October14:** the disclosed repurchases alone establish neither excess requested shares at7.00% nor that every eligible request was met below that level. Actual satisfaction/proration for all four dates is UNKNOWN from this source. CCLFX therefore has0COUNTED observable sub100% quarters, not a claim of0actual restricted offers. The former stress-series interpretation and the September3 three-full/last-partial inference are both withdrawn.
⚠️ **Scope guard:** my register's separate `~33% satisfaction, 2026Q2 priced 5/29/26` cell is a **LATER, press-sourced** offer outside this table. **Not touched, not contradicted, still un-verified.**

## 4 · Priors scored (weak-blind per §1 — WEAK evidence of calibration, not a clean forecast)
**P1** BREIT ≥3 consecutive (85%) ✅ · **P2** BREIT <20% quarterly (40%) ✅ correct side (did not occur) · **P3** BREIT <20% monthly (65%) ✅ · **P4** SREIT ≥3 consecutive (75%) ✅ · **P5** ≥1 BREIT month NOT MEASURABLE (50%) ✅ (Oct-22) · **P6** CCLFX yields a genuine satisfaction series (55%) ❌ **WRONG** — the tendered leg does not exist.
**5 of 6 on the correct side; the miss is P6, and it is the one that mattered operationally.**

## 5 · What I recommend — ⛔ and I set NO number; a level is Will-gated
1. **KEEP `≥3 consecutive sub-100% quarters` as written.** It is reachable in real stress (4-for-4 at both referents) and **BCRED is currently at 2** (Q2 ~50%, Q3 ~50%). It becomes gradable on my panel the moment BCRED prints a third — **~mid-November**. **It is no longer "ungradable"; it is 1 quarter from live.**
2. **RETIRE `<20% single-quarter satisfaction`.** It sits below the worst quarter of both reference episodes. **Replacement should be set from the out-of-sample distribution and stated PER UNIT.** For Will, the observed quarterly minima are **BREIT 24.6% / SREIT 40.0%**; the 8 measured reference quarters span **24.6%–59.3%**. **Will rules the number.**
3. **CCLFX: mark the cell NOT MEASURABLE on the register** and stop citing the 4-quarter series as a stress series. **Its primary does not establish requested amounts/realized satisfaction for those dates; the former three-full inference is withdrawn October14.**
4. **State the UNIT on every level.** The whole `<20%` result flips between monthly and quarterly.

⛔ **No BROCK vector rescored. No threshold set or moved by me. $0 moved.** ⚠️ **Context recorded because it cuts against my bear read: BCRED's ~50% is comparable to SREIT's 40.0–46.5% and better than three of BREIT's four 2023 quarters. On this measure BCRED today is LESS stressed than BREIT/SREIT were at their worst.**
