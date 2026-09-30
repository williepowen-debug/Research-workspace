# WPSR wk-9/25 and the end-Q3 grades: BRT-29 · BRT-12 · F-b Cushing falsifier · F-a check

**2026-09-30, 10:56–11:0x ET by `date`, BRENT (brent-e1), Will-directed ("yes pull EIA at 10:30 and run the grades").** Pre-registration used: [`setups/2026-09-25_Q3-predictions-grade-PREP.md`](../../setups/2026-09-25_Q3-predictions-grade-PREP.md) and [`research/2026-09-28_phase-map-this-week.md`](../2026-09-28_phase-map-this-week.md). Before grading I read the full TSV row and prediction note for BRT-29 and BRT-12, plus the F-b source record (`archive/STATUS_dated_2026-09-02.md` row 17–18 and CHANGELOG 2026-09-02). **$0. No position, gate or capital authority touched.**

## 1 · Source

EIA WPSR primary spreadsheets, `ir.eia.gov/wpsr/psw0{1,2,4,9}.xls`, retrieved 10:56–10:58 ET 9/30. Last row in every table = **week ending 2026-09-25**. The EIA v2 API was still serving wk-9/18 at 10:56 (`eia_weekly.py`), and the WPSR highlights PDF was discontinued 9/23 (its own text). ⇒ **The spreadsheets are the primary here. The API lag is a retrieval-path fact, not a publisher delay.**

| File | Bytes | SHA-256 (first 16) | Series used |
|---|---|---|---|
| psw01.xls | 1,252,352 | `14b342db5651266d` | WCESTUS1, WCSSTUS1, WGTSTUS1, WDISTUS1, WGFUPUS2, WKJUPUS2, WDIUPUS2, WRPUPUS2, WCREXUS2, WCRFPUS2 |
| psw02.xls | 1,591,296 | `55b47b4943ed8a95` | WPULEUS3 |
| psw04.xls | 465,920 | `74015db9fcc7cdb6` | W_EPC0_SAX_YCUOK_MBBL (Cushing) |
| psw09.xls | 8,923,648 | `a9b6f71efd2dee67` | WDIEXUS2 |

The extracted series (every week, all 12 IDs) are in [`wpsr_series_through_2026-09-25.json`](wpsr_series_through_2026-09-25.json). **Reproduction check:** the same method reproduces the PREP's wk-9/11 gasoline 4-week YoY (−1.0119%) and wk-9/18 (−0.7798%) exactly.

## 2 · The print (wk-9/25) [CONF EIA WPSR primary]

| Series | wk-9/18 | **wk-9/25** | WoW |
|---|---|---|---|
| Commercial crude (M bbl) | 426.398 | **427.320** | **+0.922** |
| SPR (M bbl) | 284.552 | **283.767** | −0.785 |
| **Cushing (M bbl)** | 23.748 | **24.301** | **+0.553** |
| Gasoline stocks (M bbl) | 206.046 | 204.362 | −1.684 |
| Distillate stocks (M bbl) | 107.431 | 105.180 | −2.251 |
| Refinery utilization | 94.0% | **92.5%** | −1.5 pt |
| Crude production (kb/d) | 13,939 | 13,955 | +16 |
| Crude exports (kb/d) | 3,281 | 3,570 | +289 (9/11: 4,831) |
| **Distillate exports (kb/d)** | 1,331 | **1,529** | **+198** |
| Gasoline supplied (kb/d) | 8,847 | **8,689** | −1.79% |
| Jet supplied (kb/d) | 1,650 | 1,809 | +9.6% |
| Distillate supplied (kb/d) | 3,975 | 3,948 | −0.7% |
| Total product supplied (kb/d) | 21,050 | 21,500 | +2.1% |

**Four-week YoY (4-wk average vs the matching 4 weeks 52 weeks earlier):**

| | wk-9/11 | wk-9/18 | **wk-9/25** |
|---|---|---|---|
| Gasoline | −1.0119% | −0.7798% | **+0.2587%** (8,721.2 vs 8,698.8) |
| Jet | +4.4046% | +6.1997% | **+6.4531%** |
| Distillate | −3.3474% | +0.2758% | **+5.2184%** |

## 3 · BRT-29: **FAILED (MISS on T)**

- **Letter (T):** EIA gasoline 4-week YoY **≤ −3.0% by the wk-ending-9/25 print**.
- **Reading:** **+0.2587%** at wk-9/25. The single week needed to be ≤ 7,555 kb/d (PREP); it printed **8,689** (+2.0% vs the same week last year, 8,518).
- **Classification (per PREP):** failure on **T as written**. The "never reaches ≤ −1.5%" clause is not the operative path, because wk-8/28 printed −1.61%. **Do not write "never reached −1.5%".**
- **Premise:** MET 6/6 (9/7). **M:** INDETERMINATE and unresolved (9/15 second review; three eligible further named carriers never established). Per `[[finding_threshold_vs_mechanism]]`, the phenomenon was partly observed in aggregate seat-capacity data while the named-carrier form went unfilled. **The row needed T; T failed ⇒ the outcome is FAILED regardless of M.**
- **Direction at the end:** gasoline demand moved *above* year-ago. Jet runs +6.5% YoY, so aviation is **not** leading on this series now (context only; outside the elapsed M window).
- **Calibration:** confidence 55% on an outcome of 0 ⇒ **Brier 0.3025**.
- **Lesson:** a −3.0% gasoline-demand bar needed ~11 weeks of sustained $4+ pump prices to bite. The fall peaked at −1.61% (wk-8/28) and reversed while pump prices stayed above $4.40. Registration anchored on the prior cycle's −2.58% peak and the "EV-era inelasticity" caveat. The caveat was right and the bar was set past it. **For the P3 successor: a demand test needs a base rate conditioned on price level AND duration, not only an unconditional share of weeks.**

## 4 · BRT-12: **VOID** (pre-committed 8/13 rule; spec defects)

- **8/13 rule (written before the outcome):** *if by 2026-09-30 neither signal has appeared ⇒ VOID on the no-NEITHER-branch spec defect; if either appears ⇒ grade the ordering.*
- **Refiner leg (crack compression as the first Phase-2 credit warning): NOT APPEARED.** The one candidate (Nov ULSD crack 9/22 → 9/25) fully reversed [yfinance daily bars, NOT settles; 9/30 is intraday ~11:00 ET]:

| Date | Nov ULSD crack (HOX26×42 − CLX26) | Nov 3:2:1 vs BZX26 |
|---|---|---|
| 9/22 | 109.49 | 57.64 |
| 9/24 | 95.57 | 50.12 |
| 9/25 | **95.00** (trough) | 47.40 |
| 9/28 | 96.20 | 46.07 |
| 9/29 | 100.04 | 48.25 |
| **9/30 (intraday)** | **108.52** | 54.54 |

- **Second reader (LESSONS #27): HENRY, blind** (`inbox/…HENRY_BRT-12-blind-verdict.md`, written without opening this desk's PREP): **NO.** The crack is still ~6× its 2010–25 September median (~$16). Refiner equity rose, and the mechanism was the crude leg rising (the Phase-1 squeeze partly normalising), not an OPEC+ unwind or demand destruction. **My pre-registered lean was also NO; the reads agree.** That lean ran against my interest: calling it YES would have scored an 80% HIT.
- **E&P OAS leg: UNOBSERVABLE.** No instrument exists fleet-wide; FRED rejects `BAMLH0A0E2Y` (9/8). Broad HY OAS 3.02% (FRED `BAMLH0A0HYM2`, 9/28, +9 bp) is context only, not energy-specific. BOARD scan 9/20–9/30: no E&P downgrade or distress signal.
- ⇒ **Neither signal appeared ⇒ VOID, excluded from calibration.**
- ⚠️ **HENRY's carry item ②, stated as required:** "neither appeared" rests on **one measured leg (refiner) and one unmeasured leg (E&P OAS).** The VOID is reached partly through an instrument gap, not only through the world.
- **Two spec defects to record:** (1) no NEITHER branch (named 7/30, rule 8/13); (2) **an unobservable runner:** a race whose second leg had no working instrument at registration could never have been adjudicated even if both events occurred. **Registration lesson: every leg of a race needs a named, working instrument at registration.**

## 5 · F-b (v5.8 research falsifier): **FIRED on its letter**, with cause caveats that travel

**Letter** (source record `archive/STATUS_dated_2026-09-02.md`: *"Cushing building two more weeks while the draw pace keeps halving"*; THESIS short form *"Cushing building two more weeks on a halving draw pace"*). **"Draw pace"** = the 9/2 registration's **combined draw = commercial crude WoW + SPR WoW**, measured then at **−7.57 M/wk** (−4.45 commercial, −3.12 SPR; wk-8/28).

| Week | Commercial WoW | SPR WoW | **Combined** | Cushing | Cushing WoW |
|---|---|---|---|---|---|
| 8/28 (registration base) | −4.450 | −3.122 | **−7.572** | 22.508 | +0.080 |
| 9/04 | −0.391 | −1.244 | −1.635 | 21.824 | −0.684 |
| 9/11 | −0.640 | −0.403 | −1.043 | 21.482 | −0.342 |
| **9/18** | +2.969 | −0.405 | **+2.564** | **23.748** | **+2.266** |
| **9/25** | +0.922 | −0.785 | **+0.137** | **24.301** | **+0.553** |

- **Limb 1, "Cushing building two more weeks":** two build weeks since registration (9/18 and 9/25), consecutive. **MET** on any reading, whether consecutive or cumulative.
- **Limb 2, "draw pace keeps halving":** −7.57 → −1.64 → −1.04 → **+2.56 → +0.14**. In both Cushing build weeks the combined draw is not merely halved; it is a **net build**. **MET.** The one reading this is not robust to: the 9/04→9/11 step (−1.64 → −1.04) was not itself a halving. A strict "every week halves" reading is not what the text says ("keeps halving" of the pace, against the registration base) and was never specified. I have **not** invented a stricter persistence count after seeing the data (THESIS: "No new persistence count … is invented").
- ⇒ **F-b FIRED on the letter at the wk-9/25 print.** This is the direction that cuts against my own prompt-squeeze read, and I have graded it as such.

⚠️ **Caveats that must travel with the fire (they change what it MEANS, not whether it fired):**
1. **Base rate: two late-September Cushing builds happen in 6 of 20 years (2005–2025)** [same psw04 series]. It is a common seasonal pattern, not a rare signal.
2. **Refinery turnarounds:** utilization 96.8% → 94.0% → **92.5%** over the two build weeks. Lower runs leave crude in tanks. This is the seasonal channel, not demand destruction.
3. **Crude exports fell** from 4,831 kb/d (9/11) to 3,281 / 3,570 kb/d. Barrels that don't leave build at home. **EXPORT-SIGN WARNING (STANDING STATE) applies:** a US-balance loosening driven by export routing is not world-supply relief.
4. **The world curve disagrees.** Brent M1−M3 is still backwardated (Dec−Feb ≈ +$4.47 intraday; §6). Dated Brent last $114.89 (9/22) above futures. **F-b measures the US physical buffer only; it is not a Phase-2 declaration.**
5. **Research falsifier, not capital authority** (THESIS). It moves no gate, band or position.

**What it does mean:** the v5.8 race frame (*deficit closing vs buffers hitting floors*) has lost its US-inventory clock. Cushing is 4.3 M above the 20 M line and rising, and the combined commercial+SPR draw has stopped. The prompt-squeeze read now rests on the **world** legs (Brent structure, Dated premium, Gulf access) and not on US tanks. **THESIS v5.10 → v5.11 (minor):** a falsifier fire on one limb of the frame, not a phase transition; the two-phase framework is retained.

## 6 · F-a check (not crossed) and the first switch-day decomposition (WQ-331 P1)

- **Pinned month from today: BZZ26** (REGISTRY § BRENT GRADED-CONTRACT RULE). M1−M3 = BZZ26 − BZG27.
- **(i) Old pair last:** Nov−Jan 9/29 = 102.59 − 93.51 = **+$9.08**. **(ii) New pair first:** Dec−Feb 9/29 = 96.16 − 91.59 = **+$4.57** [yfinance daily bars, not settles]. **Calendar step = −$4.51. A calendar step is never a signal.** **(iii) Residual,** Dec−Feb 9/29 → 9/30 intraday (98.20 − 93.73 = **+$4.47**, 10:17 ET) = **−$0.10**.
- **F-a (< +$3.50): NOT crossed.** Distance ~$0.97 on the new pair, which is near. The level is intraday; the settle-window read belongs to the 14:28–14:30 proxy.

## 7 · Distillate exports (DOCKET L531): recorded, consistent-with only

Distillate exports rose **1,331 → 1,529 kb/d** (+198) with the export-ban talk live. This is **consistent with** front-running a possible restriction (Bloomberg 9/25: ban talk widened the export arb). **It is not proof:** one week, and a policy-driven flow is not a demand signal (WQ-331 P2). Distillate stocks −2.25 M; distillate supplied 4-wk YoY +5.2%.

## 8 · What did not change

No position, gate, band, probability or approval moved. BRT-30 (10/26), COT #8 (10/2) and the successor Saudi resolver (post-10/24) are untouched. **P3 (the Path-B successor draft) is owed next and is DRAFT ONLY.**
