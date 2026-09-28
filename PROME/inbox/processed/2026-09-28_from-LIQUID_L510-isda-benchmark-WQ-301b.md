# LIQUID → PROME · 2026-09-28 ~10:0x ET · DOCKET L510 done (WQ-301 (b) ready for Will) + WQ-301 (a)(c) encoded + inbox 7 → 0

Spawned `prome-7f` 09:45 ET (Tier-1 due-row). Full record: `AGENTS/LIQUID/analysis/2026-09-28_L510-isda-benchmark.md` (evidence scripts beside it in `analysis/2026-09-28_L510/`). Labels: **OBS-UF** = observed upfront (pt on the 500bp coupon, as DTCC disseminated) · **MDS** = model-derived spread (bp) · **PRESS** = press figure, basis unknown.

## 1. The validation (Will's four asks, answered)
| Ask | Answer | Token |
|---|---|---|
| Benchmark vs ISDA standard model / trusted implementation | QuantLib 1.43 `IsdaCdsEngine` (ISDA conventions: flat hazard, R 40%, CDS2015, ACT/360, step-in T+1, settle T+3, accrual rebate). Official ISDA USD curve file unreachable (rfr.ihsmarkit.com HTTP 500, every date); curve proxied by FRED Treasury CMT + SOFR, bracketed ±50bp. | VERIFIED run; curve = proxy |
| Measured gap per date (ISDA − our script, cash reading) | **9/23–24: +7.1 to +8.3bp** (script low) · **7/06: +0.2 to +0.4bp** · **12/17 Dec peak: −4.4bp**. Curve bracket ±1.0–4.8bp. On an identical flat curve the two codes agree **≤0.4bp at every date** ⇒ the 9/26 "UNMEASURED, INFERRED ≤±15bp" model gap is now MEASURED ≤0.4bp. | VERIFIED |
| Accrued-payment treatment | Tested on the whole DTCC tape at the 6/22 and 9/21 coupon dates vs no-coupon placebo windows: the reported upfront jumps by ≈ the accrued (bimodal ±0.24pt on 100bp names; 0 of 22 near zero at 6/22 vs 16 of 24 in the placebo). **DTCC's field is the CASH amount net of accrued** (majority convention; a minority of reporters look clean). Effect on the spread: +1.5–1.9bp [9/23–24] · +5.9–6.1bp [7/06] · **+41.5bp [12/17]**. | VERIFIED (majority); per-print UNKNOWN |
| Is ±25bp established? | **Yes at 9/23–24 (worst ≤13bp) and 7/06 (worst ≤8bp). No at the 12/17 Dec peak** — one print, 86 days of accrual; if its reporter used the clean convention, the reading overstates by ~46bp. | VERIFIED / UNKNOWN |

⛔ **Correction to my own 9/26 record, found in this pass: DTCC's upfront field is UNSIGNED** (0 negatives among 2,245 upfront rows on 9/23, though most IG names must carry negative upfronts). My 9/26 argument "a 452bp spread would need a NEGATIVE upfront, and none prints" is **WITHDRAWN** (grade record §2(d) struck through, KB-LIQ-069 annotated). The 7/06 sign is re-established **POSITIVE, INFERRED-strong**, on three other lines: no near-zero print on the path 7/06 → 7/29 (2.87–3.69 → 13.22–14.97pt OBS-UF); the same maturity-curve shape as September; CoreWeave shares $86.46 [7/06] vs $102–128 when the upfront sat near zero. Negative sign would put 7/06 at 410–430bp MDS. **The tape probably did print below 500bp in late April–May** (sign-ambiguous), so the PRESS 4.52 may be a May level; it is unreproducible on its stated date (7/06: 585–609bp MDS).

## 2. What it means for the anchor (WQ-301 (b))
| Basis | Anchor | Clause A | Clause B | 9/23–24 window, ISDA MDS | Leg 2 |
|---|---|---|---|---|---|
| Letter (governs now) | PRESS 4.52pp / 8.81pp | >552 | >666.5 | 819–866 | FIRED |
| **Re-based (recommended)** | MDS 597 [7/06 Jun-31, mean of 2 prints] / MDS 878 [12/17 Dec-30] | **>697** | **>737** | 819–866 | FIRED |
| 9/26 proposal — SUPERSEDED | 591 / 840 (script, clean reading) | >691 | >716 | — | — |
Limits that travel with the re-base: ① B rests on one Dec print — if clean-reported, B = **>717**; ② no single print with |OBS-UF| < ~1.5pt (spread within ~35bp of 500) may be graded alone. Both re-based lines sit at OBS-UF ≈ +4 to +6pt, clear of the sign fold. **Changes nothing today** (FIRED on every basis); later, the re-based leg un-fires below ~697/737, the letter's below 552.

## 3. Also done
- **WQ-301 (a) encoded:** grade record gets the RULED line + label legend + OBSERVED UPFRONT / MODEL-DERIVED SPREAD column headers; KB-LIQ-069 Fact annotated. **(c) encoded:** `AGENTS/LIQUID/CLAUDE.md` HY Energy OAS row → CANNOT-FIRE, *"energy-sector HY OAS: no reachable source, declared 2026-09-26"*, row and >300 letter kept.
- `scripts/crwv_cds_grade.py` docstring: the UNMEASURED band sentence replaced with the measured result + the unsigned-field rule (no logic change).
- **Inbox 7 → 0**, all logged in `board_log.tsv`: PROME WQ-301 packet acted · CREED 9/26 census noted (T-08b NOT fired, T-08a is a rate/refi fire on my duration channel, no LIQUID row moves) · SIG-W-20260927-002 acted: **the CCC/HY re-arm does NOT establish a new Will decision from my rows** (X1 >280 strict not met at 280.0; RED-FT-01 day 1 of 3, RED's; LIQ-07 not met) — it rides L492 · -004/-005/-006 Nano Banc info-only (REGINALD) · -008 UBS noted, unconfirmed.
- Corrections check: COR-20260927-05/-06 NO-OP, COR-20260925-13 DEFERRED (the `hy_oas_watch.py` stale-arbiter text repair is still owed by me). Now rc 0.

## 4. L492 — ARMED, not graded (PROME re-spawns at the print)
FRED BAMLH0A0HYM2 9/25 cell publishes ~16:15 ET today. My estimate **≈283 ±5; FALSIFIED by ≤278.** RED-FT-01 (≥280 sustain 3) at **day 1 of 3** (9/24 = 280) — RED owns the sustain ruling. **X1 letter is >280 STRICT: 280.0 is NOT met.** Re-kill (<260 ×2) 20bp away from 280. If the index retraces, run KILL_MEMO guard test 3 (does CCC stay wide?). The 9/28 cell (Tue 9/29) completes or breaks the sustain count.

## COMPLETION — LIQUID — 2026-09-28
STATUS: ✅ DONE (L510 + WQ-301 (a)(c) + inbox 7→0); L492 ARMED, not graded (print ~16:15 ET, not waited for)
CHANGED: AGENTS/LIQUID/analysis/2026-09-28_L510-isda-benchmark.md (+ 2026-09-28_L510/ 4 evidence scripts), analysis/2026-09-26_liq069-leg2-grade.md, workbook/KB.tsv, CLAUDE.md, STATUS.md, scripts/crwv_cds_grade.py (docstring), board_log.tsv, registry/corrections_receipts.tsv, inbox 7 files → processed/
RESULT: ISDA engine vs our script, per date: +7.1 to +8.3bp [9/23–24], +0.2 to +0.4bp [7/06], −4.4bp [12/17]; model conventions agree ≤0.4bp, so the gap is the discount curve. DTCC's upfront is cash net of accrued (measured at two coupon dates) and UNSIGNED — my 9/26 "no negative upfront" argument withdrawn; 7/06 sign re-established positive on three other lines. ISDA spreads: anchor 597bp [7/06], Dec peak 878bp [12/17], now 819–866bp [9/23–24]; ±25bp holds at 9/23–24 and 7/06, not at 12/17.
GAPS: Official ISDA USD curve unreachable (rfr.ihsmarkit.com HTTP 500) → Treasury-proxy curve, ±50bp bracket moves results ≤4.8bp. QuantLib's own ISDA reference suite not re-run here. Per-print clean/cash convention and the true sign are not disseminated. hy_oas_watch.py stale-arbiter repair still owed.
WILL_NEEDS: WQ-301 (b) — Will decides whether leg 2's anchor stays the press 4.52pp (lines >552/>666.5, not observable on its date) or is re-based to the same DTCC tape converted with the ISDA model (lines >697/>737, ±15bp measured, with two named limits). Rec: re-base. Today's FIRED 2-of-2 is unchanged either way.
FOLLOW-UP: PROME re-presents WQ-301 (b) with the >697/>737 numbers (not the 9/26 >691/>716); re-spawn LIQUID at ~16:15 ET for L492.
