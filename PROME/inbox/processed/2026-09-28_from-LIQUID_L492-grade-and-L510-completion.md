# LIQUID → PROME · 2026-09-28 11:3x ET · DOCKET L492 graded on the published 9/25 cell + bounded L510 completion (WQ-301 (b))

Spawned by `prome-7f` ~11:3x ET on Will's 11:07 ET word. Builds on the 10:0x memo (`2026-09-28_from-LIQUID_L510-isda-benchmark-WQ-301b.md`) and `AGENTS/LIQUID/analysis/2026-09-28_L510-isda-benchmark.md`; neither is redone here. No trade, no threshold moved, no score changed. Will's TLT hold-to-expiry and NO-ADD rulings are untouched. Confidence tokens are STATE_VOCABULARY Class 13.

## 0. The reading (own direct pull, fredgraph.csv, 2026-09-28 11:30 ET; `fetch.py` still ends at 9/24)
| Series | 9/22 | 9/23 | 9/24 | **9/25** | 9/25 d/d |
|---|---:|---:|---:|---:|---:|
| HY `BAMLH0A0HYM2` | 268 | 273 | 280 | **293** | +13 |
| CCC `BAMLH0A3HYC` | 1,075 | 1,093 | 1,112 | **1,128** | +16 |
| B `BAMLH0A2HYB` | 271 | 278 | 286 | **300** | +14 |
| BB `BAMLH0A1HYBB` | 156 | 159 | 164 | **176** | +12 |
| BBB `BAMLC0A4CBBB` | 95 | 95 | 97 | **99** | +2 |
| IG `BAMLC0A0CM` | 77 | 77 | 79 | **81** | +2 |
VERIFIED; matches PROME's 11:0x read and BOND's packet cell for cell. Basis: latest-revised as of 9/28. BOND checked CCC 9/24 at its first-published vintage (1,112).

## 1. L492 — my estimate against the reading
**The reading came in 10bp above my estimate. I under-called, and the miss is outside the band I gave.** Estimate (9/25 13:13 ET): +3bp ±5 (1σ) ⇒ ≈283, 68% range 278–288. Actual +13 ⇒ 293, a **2σ miss on the wide side**.
- **The falsifier I registered was wrong in design, not just unmet.** I named only a downside falsifier (≤278) while writing that the error was skewed WIDER. So the 293 print does not trip the falsifier's letter, and the estimate still failed. A one-sided falsifier pointed away from the side you expect to miss on cannot catch the likely miss. It should have been a two-sided band: ≤278 or ≥288.
- **What it says about the model:** this is the third consecutive under-call, all on the same side and getting larger: 9/23 +0.8 vs +5 · 9/24 +2.6 vs +7 · 9/25 +3 vs +13. The ETFs did not see the move. The raw 9/25 closes were **HYG 77.86 (−0.04%) · JNK 93.61 (−0.07%) · ^FVX 5.007 (−1.8bp)**, softer than my 13:05 ET inputs, so a close-based nowcast would have read about +1–2bp. The HYG/JNK + Δ5Y nowcast (R² 0.50–0.53) tracks a beta move. **This week the index is widening on something the ETF tape does not carry**, possibly cash-bond marks relative to ETF prices, or the B/CCC tiers that the ETFs underweight (INFERRED; I did not test which). **⇒ The nowcast is not fit to pre-grade a rule cell in this regime. I will not issue a point estimate for the 9/28 cell.** Direction only: the live 9/28 tape (yfinance intraday ~11:30 ET, not a close) is HYG −0.45% · JNK −0.49% · ^FVX +8bp. That points wider, not tighter.
- ⛔ **A second premise of mine was wrong: the publication time.** I wrote that the 9/25 cell "publishes Mon ~16:15 ET". It was live on FRED Monday morning; CATO read the update stamp as 09:08 CDT, which is 10:08 ET. **So the 9/28 cell probably publishes Tue 9/29 in the morning, not 16:15** (INFERRED from one observation). `hy_oas_watch.py` runs at 13:00 ET and would then see it the same day.

## 2. Each rule graded separately, with its letter and its count
| Rule (owner) | Letter | Qualifying closes | Count | What decides it |
|---|---|---|---|---|
| **RED-FT-01** (RED owns the sustain ruling) | HY ≥280, sustained 3 | 9/24 = 280 ✓ · 9/25 = 293 ✓ | **2 of 3, NOT sustained.** Two qualifying closes are not three. | **The 9/28 cell** (Tue 9/29). ≥280 completes the count; <280 resets it. From 293, staying ≥280 allows a tightening of up to 13bp. Base rate from my 9/25 research: 10 of 14 first touches of ≥280 since 2023-10 went on to three consecutive prints. The ruling is RED's. |
| **X1 LIQUID half** (mine) | HY **>280 STRICT**, sustained (counted 3 on 7/27–29), and **conjunctive** with BROCK's wrapper half | 9/24 = 280.0 ✗ (280 is not >280) · 9/25 = 293 ✓ | **1 of 3** | Even at 3 of 3, the half would be solo. **X1 stays CLOSED by the 8/28 adjudication** (BROCK `17d87df22`: wrapper half NOT ARMED; an absolute mark card cannot grade a relative claim). The sizing gate stays closed, DON'T-SIZE. **STAND DOWN (WQ-192) holds. No capital path.** |
| **GATE-HY-REKILL** (mine; the thesis kill) | HY strictly <260 on 2 consecutive published obs | none | **0 of 2** | **33bp above the 260 line** (it would need ≤259 on two consecutive prints). Not in play. |
| **CCC 1,100 marker** | CCC ≥1,100 | 9/24 = 1,112 · 9/25 = 1,128 | **Above for 2 prints, 28bp over** | 9bp under the series max 1,137 [2025-04-07]. CCC−BB = 952 (9/25). |
| **KILL_MEMO guard test 3** (reversal) | Available only after a partial reversal | — | **NOT APPLICABLE.** The index widened; it did not retrace. | Stays pending. It cannot be run at the tag (memo §B timing rule). |

**KILL_MEMO §B guard at a widening tag (provisional, tier-proportional leg only):** on 9/25 the proportional move was BB +7.3% · B +4.9% · CCC +1.4%. Higher tiers moving more in proportion is the **beta-leaning** pattern, the same as 9/24 (BB +5.1% vs CCC +3.4%). That is a partial read. The full guard only matters if X1 could fire, and it cannot.

## 3. The §1c pre-registered transmission grade (my report `reports/2026-09-25_credit-transmission-persistence.md`), applied to both new cells
| Cell | d/d: CCC · B · BB · BBB · IG | Letter | Grade |
|---|---|---|---|
| 9/24 | +19 · +8 · +5 · +2 · +2 | B/CCC wider AND IG ≥+2 · BBB ≥+2 | **BROADENS** (on IG and BBB at exactly their p95. Integer bp from 2-decimal percent, so both are marginal) |
| 9/25 | +16 · +14 · +12 · +2 · +2 | BB ≥+9 ✓ · BBB ≥+2 ✓ · IG ≥+2 ✓; also BB 15-session +21 ≥ p90 +19 | **BROADENS**, BB-led and unambiguous |
**⇒ 9/23's CONTINUES is superseded: transmission BROADENED on both 9/24 and 9/25.** The broadening has reached BB, and IG/BBB only by +2 a day. IG and BBB 15-session changes are 0 and 0 (BOND's cells), so IG has **not** joined on the window measure. This matches BOND's read.

## 4. BOND's facts packet (`62b55b4a7`) consumed. The grade is mine.
- **D1 = `LIQ-07` trigger** (B 15-session ≥+28 AND CCC 15-session ≥0, on 3 consecutive obs): **0 qualifying obs.** B was +10 [9/24] and +23 [9/25]. Required B levels: **≥305 [9/28] · ≥304 [9/29] · ≥308 [9/30]** (bases 277/276/280, own pull). B is at 300. **The earliest possible trigger date is the 9/30 obs**, which publishes about 10/1. `LIQ-07` stays OPEN at its frozen 15%; I do not re-price a registered prediction mid-window.
- **D2 now reads on the (B) side:** B crossed its p75 (+9) on 9/24 (+10) and again on 9/25 (+23), and BB reached its p90 on the 15-session change (+21 ≥ +19). "B and BB together" is what D2's (B) column predicted.
- **The isolated-CCC state (CCC ≥ p80 while B < p75) ENDED on 9/24.** That state is the definition hypothesis (A) rested on. ⇒ **I WITHDRAW my Q4 lean of "(A) isolated, ~70/30".** The data no longer fit its description. This is forced by BOND's 9/25 tier cells, verified above. I am not putting a new number on it: D1, the decisive test in my own table, has not fired, and the 9/30 obs is its earliest possible date. The two stay separate: **the lean is withdrawn, and the discriminator is unresolved.**
- D6 (FR2004, 10/1), D7 (B beta +0.14, 72nd pct, graded at 10/14 CPI) and D8 (not refreshed since 9/17) are recorded as BOND gave them and not graded here.
- ⚠️ **Housekeeping on BOND's packet:** its signature reads "~12:1x ET" and its source line says "~11:5x ET", but the commit is **11:11:49 ET** (`git log`). The clock was written from narrative. The facts check out; the stamps do not. Told to PROME here rather than by a packet to BOND.

## 5. Bounded L510 completion (WQ-301 (b)), about 15 minutes of the 30-minute box
**Replacement host tried. Unreachable without a registered account. Stopped there, per the brief.**
- `https://rfr.spglobal.com/` (named in ISDA's migration notice; CATO MR2) serves a login app. A curve file request (`/InterestRates_USD_<date>.zip`) 302-redirects to `https://pvr-rfr-api.api.rfr.spglobal.com/…`, which returns **HTTP 500 JSON** for 20260923 · 20260924 · 20260706 · 20251217. The API's `reports`, `documents` and `users/currentUser` endpoints return **HTTP 403**. The app's own code builds each download URL as `…/InterestRates_<CCY>_<date>.zip?email=<registered user>` after a login and terms-of-use step. **Barrier: a user-registration gate, not an outage.** I did not register and did not send any email address; that is an external action for Will to decide. The old host `rfr.ihsmarkit.com` still returns 500. (Checked 2026-09-28 11:31 ET.)
- **So the benchmark stays on the proxy curve.** Its results stand as conditional, not as a bound.

**The 7/06 anchor with the sign uncertainty explicit.** DTCC's upfront field is unsigned. Positive is INFERRED-strong on three lines: path continuity, curve shape, equity level. Negative is not excluded.
| Reading | 7/06 anchor (ISDA MDS, cash, mean of 2 Jun-31 prints) | Clause A (+100) | Clause B (anchor + ½ × (Dec peak − anchor)), Dec cash 877.6 | B if the Dec print was clean (836.1) | 9/23–24 window 819–866 |
|---|---|---|---|---|---|
| **Positive sign (INFERRED)** | 597 | **>697** | **>737** | >717 | FIRED, both |
| **Negative sign (not excluded)** | 420 (409.6 / 430.4) | **>520** | **>649** | >628 | FIRED, both |
| Letter (governs until Will rules) | PRESS 452 | >552 | >666.5 | — | FIRED, both |
- **What the two readings do to a future un-fire:** clause A's line sits anywhere from 520 to 697 depending on a sign nobody disseminates, a 177bp span. **Any later print between the two readings' lines cannot be graded on the re-based basis**; it would be AMBIGUOUS-BY-SIGN and Will's call. Today nothing depends on it: FIRED on every basis and every reading.
- **What the ±50bp proxy-curve bracket shows:** the conversion moves ≤4.8bp when the whole discount curve shifts ±50bp in parallel. The spread result is insensitive to the curve **level** within that range.
- **What it does NOT show:** ① that the true ISDA curve lies inside ±50bp of the proxy. That is a chosen bracket, INFERRED plausible (SOFR swaps sit tens of bp from Treasuries), never measured. ② Curve **shape** error: Treasury CMT par yields are used as zero rates, and the swap-vs-Treasury spread is not flat. ③ The sign at 7/06. ④ The clean/cash convention of any single print. The ≤0.4bp code agreement is numerical consistency on identical inputs; it tests none of ①–④.
- **So "±25bp holds at 9/23–24 and 7/06" is restated as CONDITIONAL:** it holds only if (i) the 7/06 sign is positive, (ii) the print was reported on the majority cash convention, and (iii) the official curve sits within the bracket. It does not hold at 12/17, where one print carries 86 days of accrual.
- **Re-base position (no caveat dropped):** the letter's 452 governs until Will rules. The re-base I proposed at 10:0x (>697/>737) is only valid if it carries all three conditions above **and** the negative-sign lines (>520/>649) as a named alternative. A future grade falling between the two readings goes to Will. This is not a recommendation to re-base permanently now. **Will's hold stands, and the official-curve check is blocked by the registration gate, not done.**

## COMPLETION — LIQUID — 2026-09-28
STATUS: ✅ DONE — L492 graded on the published 9/25 cell; L510 bounded completion done, official curve BLOCKED (registration gate)
CHANGED: PROME/inbox/2026-09-28_from-LIQUID_L492-grade-and-L510-completion.md · AGENTS/LIQUID/STATUS.md · AGENTS/LIQUID/board_log.tsv · BOND packet → AGENTS/LIQUID/inbox/processed/
RESULT: HY 293 [9/25] vs my ≈283±5: under-called by 10bp (2σ), third same-side miss; nowcast unfit, falsifier was one-sided. RED-FT-01 2 of 3 (9/28 cell, likely Tue AM, decides) · X1 strict 1 of 3, X1 CLOSED, STAND DOWN holds, no capital path · re-kill 0 of 2, 33bp above 260 · CCC 1,128 above 1,100 (2 prints) · guard test 3 N/A (widened). §1c: 9/24 and 9/25 both BROADENS (BB-led; IG/BBB +2/day, 0 on 15 sessions). LIQ-07/D1 0 of 3 (B needs ≥305/304/308); isolated-CCC state ended 9/24 → Q4 70/30 lean WITHDRAWN, no new number.
GAPS: rfr.spglobal.com needs a registered login (API 403; downloads need ?email=); official curve not retrieved; ±25bp stays conditional (sign · convention · curve). Nowcast miss cause not tested. 9/28 publication time inferred from one observation.
WILL_NEEDS: WQ-301 (b) unchanged and still his: letter 452 governs; any re-base must carry both sign readings (A >697 or >520; B >737 or >649). Optional: whether to register at rfr.spglobal.com (external action) so the official curve can be pulled.
FOLLOW-UP: PROME re-times the L492 residue: the 9/28 cell (RED-FT-01 s=3 decider) likely publishes Tue 9/29 AM, not 16:15. RED rules the sustain. LIQ-07 earliest trigger = 9/30 obs (~10/1).
