# L510 — ISDA benchmark of the CoreWeave 5Y upfront→spread conversions (WQ-301 (b)) · 2026-09-28 ~10:0x ET · LIQUID

**Task (DOCKET L510, Will 2026-09-26 15:54 ET):** one targeted validation before any anchor re-base — benchmark the current (9/23–24) and anchor (7/06) conversions against the ISDA standard model or a trusted implementation, INCLUDING accrued-payment treatment; state the measured gap per date; keep OBSERVED UPFRONT distinct from MODEL-DERIVED SPREAD. Spawned by PROME `prome-7f`. No trade, no threshold moved, no anchor changed. Confidence tokens = STATE_VOCABULARY Class 13.

**Labels used on every figure below:** **OBS-UF** = observed upfront, points on the 500bp coupon, as DTCC disseminated it (`Other payment amount` ÷ notional, type UFRO) · **MDS** = model-derived conventional spread, bp (R 40%, flat hazard) · **PRESS** = press figure, basis unknown. A cell never carries two of these.

## 1. Answer in five lines
1. **Model gap, measured:** QuantLib 1.43 `IsdaCdsEngine` (the trusted implementation) vs our `scripts/crwv_cds_grade.py`, same inputs, same reading: **9/23–24: script LOW by 7.1–8.3bp · 7/06: 0.2–0.4bp · 12/17: script HIGH by 4.4bp.** On an identical flat 4% curve the two codes agree to **≤0.4bp at every date** — the whole gap is the discount curve, not the model conventions. The 9/26 "structural gap UNMEASURED, INFERRED ≤±15bp" is now **MEASURED ≤0.4bp**.
2. **Accrued treatment, measured on the whole tape:** DTCC's upfront is **predominantly the CASH amount net of accrued**, not the clean upfront (§3). ⇒ the 9/26 "dirty" column was the right reading. It moves the spread **+1.5–1.9bp at 9/23–24, +5.9–6.1bp at 7/06, +41.5bp at 12/17.**
3. **New structural fact — the field is UNSIGNED** (0 negative values among 2,245 UFRO rows on 9/23, though most IG names on a 100bp coupon must carry negative upfronts). ⛔ This **invalidates my 9/26 argument** (§2(d) of the grade) that "a 452bp spread would need a NEGATIVE upfront, and none prints" — none CAN print. The 7/06 sign is re-established by three independent lines (§4): **positive, INFERRED-strong.** A negative sign would put 7/06 at **410–430bp MDS**.
4. **The ±25bp bound:** **HOLDS at 9/23–24 (worst ≤13bp) and 7/06 (worst ≤8bp)**, curve uncertainty included. **NOT established at the 12/17 Dec peak**: if that one print was reported clean (a minority convention on the tape), the cash reading overstates it by ~46bp.
5. **Leg 2 stays FIRED on every basis** (letter >552/>666.5; re-based >697/>737; window low 819 MDS). The re-base changes nothing today.

## 2. The benchmark (ISDA column = QuantLib `IsdaCdsEngine`, Taylor/HalfDayBias, flat hazard, R 40%, CDS2015 schedule, ACT/360, step-in T+1, cash settle T+3, accrual rebate on)

| Print (DTCC PPD SEC-regime) | OBS-UF | Script MDS clean / cash | ISDA MDS clean / cash | Gap ISDA−script (cash) | Curve ±50bp (cash) | Both codes, flat 4% (cash) |
|---|---|---|---|---|---|---|
| 12/17/25 Dec-30 14:45Z $1M (Dec peak) | 11.29 | 840 / 882 | 836.1 / 877.6 | **−4.4** | ±4.8 | 881.6 vs 882 |
| 7/06 Jun-31 14:06Z $750k (CORR) | 3.69 | 603 / 609 | 602.9 / 609.0 | **+0.3** | ±1.3 | 608.6 vs 609 |
| 7/06 Jun-31 20:18Z $2M | 2.87 | 579 / 585 | 579.4 / 585.3 | **+0.2** | ±1.0 | 585.0 vs 585 |
| 7/07 Jun-31 18:45Z $3M | 3.66 | 602 / 608 | 602.2 / 608.7 | **+0.4** | ±1.3 | 608.2 vs 608 |
| 9/23 Q2 Dec-31 12:45Z $3M | 11.46 | 835 / 836 | 842.7 / 844.2 | **+7.7** | ±4.5 | 836.2 vs 836 |
| 9/23 Q3 Dec-31 19:16Z $3M (low) | 10.72 | 811 / 812 | 817.6 / 819.0 | **+7.1** | ±4.1 | 811.7 vs 812 |
| 9/23 Q4 Dec-31 17:54Z $3M (high) | 12.08 | 856 / 857 | 864.1 / 865.6 | **+8.2** | ±4.8 | 857.0 vs 857 |
| 9/24 Q1 Dec-31 19:22Z $3M | 11.82 | 847 / 849 | 855.5 / 857.4 | **+8.3** | ±4.7 | 848.8 vs 849 |

Accrued (pt) computed by both codes: 1.208 [12/17] · 0.208 [7/06] · 0.222 [7/07] · 0.042 [9/23] · 0.056 [9/24] — identical to 3 decimals.
**Discount curve (the one input I could not get at the source):** the ISDA-standard USD curve file (Markit/S&P, `rfr.ihsmarkit.com`) returned HTTP 500 for every date tried incl. 2020/2023 (2026-09-28 09:5x ET). Proxy = FRED H.15 Treasury CMT 1M–10Y + SOFR O/N at the front [same date], log-linear discount (= ISDA flat-forward interpolation). SOFR swaps sit below Treasuries at 5Y (INFERRED, not measured here), so the true ISDA figure is probably 2–3bp BELOW my ISDA column in September. The ±50bp bracket covers it.
⚠️ QuantLib's ISDA engine is validated against ISDA reference outputs by its own test suite; I did not re-run that suite (UNVERIFIED here). The independent check I did run: two separately written codes agree ≤0.4bp on identical inputs.

## 3. Accrued-payment treatment — which number does DTCC disseminate? (`2026-09-28_L510/accrued_test2.py`)
Test: at a coupon date the accrued resets from ~c×90/360 to ~0. A CLEAN upfront does not jump; a CASH amount net of accrued jumps by the accrued (up for names paying upfront, down for names receiving it, since the field is unsigned). Same name + maturity + coupon, USD, standard, same-day executions, |OBS-UF| clear of zero.

| Window | Coupon? | 100bp-coupon names | Signed median Δ | In the ±0.05pt bin |
|---|---|---|---|---|
| 9/16 → 9/18 | no (placebo) | 54 | +0.017pt | **24 of 54** |
| 9/18 → 9/22 | **yes (9/21)**, accrued reset 0.242pt | 55 | −0.118pt | **8 of 55**; 20 in [−0.35,−0.15] |
| 9/22 → 9/23 | no (placebo) | 58 | −0.000pt | 24 of 58 |
| 6/18 → 6/23 | **yes (6/22)**, reset 0.247pt | 22 | −0.254pt | **0 of 22**; bimodal at ±accrued |
| 6/23 → 6/24 | no (placebo) | 24 | −0.005pt | 16 of 24 |

IG OAS was flat across 9/18→9/22 (77/77/77bp, FRED BAMLC0A0CM), so the bimodal jump is not a market move. 500bp-coupon names: median |Δ| 0.95–1.41pt across the coupon windows vs 0.47–0.86pt placebo, against an accrued reset of 1.18–1.24pt. **⇒ VERIFIED at the tape (majority convention): the field is the cash amount net of accrued.** ⚠️ Not every reporter: the 9/18→9/22 window still has 8 names in the zero bin. **The per-print convention is not observable**, so a single print read far from a coupon date (12/17: 86 days of accrual) carries a one-sided clean-vs-cash risk of up to 41.5bp.

## 4. The sign at the 7/06 anchor (the field is unsigned) — `2026-09-28_L510/crwv_scan.py`, all 500 CoreWeave prints 12/01/2025–9/25/2026
| Line of evidence | Reading |
|---|---|
| **Path continuity** | OBS-UF near zero **only** in 4/10–6/24 (lows 0.04 [6/11], 0.10 [5/05, 6/10], 0.36 [4/23]) — the window where the sign could flip. From 7/06 it rises **2.87–3.69 → (2.56 [7/09]) → 3.80–4.46 [7/13–14] → 7.14 [7/17] → 11.74 [7/28] → 13.22–14.97 [7/29]** with no print near zero, and stays ≥4.28 on Jun-31 through 9/24. A sign change 7/06→7/29 would have to happen between prints and move ~150–280bp in 2–3 sessions. |
| **Curve shape** | Jun-31 ÷ Dec-30 OBS-UF on the same day: 2.1 [7/07] · 1.6 [7/13] · 1.6 [7/17] · 1.4 [7/21] · 1.2 [7/24] — the same upward-sloping pattern as September (~1.3), when the sign is certain. The negative reading on 7/07 inverts the curve (Dec-30 455 over Jun-31 ~420 MDS). |
| **CoreWeave shares** (fetch.py raw closes) | $102–128 [4/10–5/05] while OBS-UF ≈ 0 (MDS ≈ 500) · **$86.46 [7/06]** · $60.82 [7/29] at the OBS-UF peak · $107.73 [8/12] as OBS-UF fell to 3.2–5.7. Lower equity on 7/06 than in the ≈500bp window ⇒ wider credit ⇒ positive sign. A 410–430bp MDS at $86 would be tighter than at $128. |

**⇒ 7/06 sign POSITIVE, INFERRED-strong (three independent lines, none of them the tape's own sign).** MDS if negative: 409.6 / 430.4 [7/06 Jun-31] and 455.4 [7/07 Dec-30] (`isda_neg.py`).
⛔ **Correction to my 9/26 record** (§2(d) of `2026-09-26_liq069-leg2-grade.md`): *"DTCC printed no standard CoreWeave 5Y below ~500bp on any day from 5/04 to 7/10 … every standard print carried a positive upfront"* is **not supportable** — the sign is not disseminated. In 4/10–6/24 several prints are sign-ambiguous, and on 5/05 the curve is only upward-sloping if Dec-30 (1.15pt) is negative (≈470bp MDS, INFERRED). **So the tape probably did print below 500 in late April–May.** The correct statement is narrower: **the PRESS 4.52pp cannot be reproduced from the tape ON ITS STATED DATE (7/06: 585–609bp MDS, positive sign).** It may be an April–May level, a model mid or a different tenor (INFERRED; the article's own basis is unknown).

## 5. What it means for the anchor (WQ-301 (b), for Will)
| Basis | Anchor | Clause A line | Clause B line | 9/23–24 window (ISDA MDS, cash) | Result |
|---|---|---|---|---|---|
| **LETTER (governs until Will rules)** | PRESS 4.52pp [7/06]; PRESS Dec peak 8.81pp | >552 | >666.5 | 819.0–865.6 | FIRED, both |
| **Re-based, ISDA + cash reading (this memo)** | MDS 597.2 = mean(585.3, 609.0) [7/06 Jun-31]; MDS 877.6 [12/17 Dec-30] | **>697** | **>737** (597.2 + ½×280.4) | 819.0–865.6 | FIRED, both (window low − 13bp worst error = 806) |
| 9/26 proposal (script, clean reading) — **SUPERSEDED** | 591 / 840 | >691 | >716 | — | — |

- The PRESS Dec peak 8.81 **does** reproduce from the tape (877.6 MDS cash, −3bp); the PRESS 4.52 does not on 7/06 (597, +145bp). Same article, one number reproducible and one not.
- Both re-based lines sit at OBS-UF ≈ +4 to +6pt on the on-the-run contract, **clear of the sign fold** (|OBS-UF| < ~1.5pt ≈ MDS within ~35bp of 500). The letter's 552 line sits at ≈ +2pt, close to it — an un-fire read on the letter basis is the harder grade.
- **Two limits that travel with any re-base:** ① the B line rests on ONE Dec print; if it was reported clean, B falls to **>717**. ② no single print with |OBS-UF| < ~1.5pt may be graded alone (sign unknowable).
- **Recommendation: re-base (A >697bp, B >737bp; conversion = ISDA standard model on the cash-net-of-accrued reading; stated error ±15bp at the anchor and grading dates, with limits ① and ②).** Reason: the letter's 452 cannot be observed on its date, so any future re-tightening grade on the letter basis depends on a number nobody can see. What it changes today: nothing — FIRED on every basis. What it changes later: on re-base the leg un-fires below ~697/737; on the letter it stays fired down to 552.
- **Owner of the call: Will.** Until he rules, the letter's 452 governs. Not applied here.

## 6. Reproduce
`python3 -m venv qlenv && qlenv/bin/pip install QuantLib` (1.43) · `fetch.py fred <SERIES> --json --periods 220` for SOFR, DGS1MO…DGS10 into a dir · DTCC ZIPs via `scripts/crwv_cds_grade.py CACHE DAY…` · then `analysis/2026-09-28_L510/{isda_bench,isda_neg}.py FRED_DIR`, `{accrued_test2,crwv_scan}.py ZIP_DIR`. Evidence scripts kept with this memo — not a tool, not wired anywhere.
