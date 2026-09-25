# End-Q3 prediction grades — PREP (BRT-26 · BRT-29 · BRT-12)

**Written:** 2026-09-25 10:3x–10:5x ET by BRENT (Will-directed "Yes do it"). **This file PRE-STAGES; it grades nothing.** Each grade lands in `thesis/PREDICTIONS.tsv` + its `thesis/prediction_notes/` note + `thesis/CHANGELOG.md` on the date shown. I read all TSV fields and all three notes in full before writing this. Claims, confidences and falsifiers are untouched: retro-editing them is a calibration sin.

| Row | Grades on | When | Modal outcome (pre-registered here, before the data) |
|---|---|---|---|
| **BRT-26** | Baker Hughes US **oil** rigs, 9/25 print, vs frozen **457** | **Today, after ~13:00 ET** | **HIT** unless oil ≥457 (needs **+5** from 452) |
| **BRT-29** | EIA gasoline 4-wk YoY at the **wk-ending-9/25** print, needs **≤ −3.0%** | **Wed 9/30, ~10:30 ET** | **MISS on T.** It needs a ≥14.6% one-week collapse, seen since 2010 only in holiday or winter-storm weeks (below) |
| **BRT-12** | Pre-committed 8/13 rule: neither signal by 9/30 ⇒ **VOID** (spec defect); either signal ⇒ grade the ordering | **9/30**, after a second reader | **VOID** is modal, but one candidate (the 9/22–24 diesel-crack drop) must be adjudicated first |

---

## BRT-26 — rig count stays below 457 (conf 85% [9/6 window-shrink mark])

- **Last reading:** US Oil **452** [9/18 print, BH primary workbook, live reader]. Needs **+5** to reach 457. Recent pace: +1, +2, +2.
- **The 9/25 print is the last one inside the window.** Baker Hughes' next print is Fri 10/2, after end-Q3. The alternative trigger ("before a genuine Hormuz operational resolution") has not occurred: no resolution, and Petroline was only partially restarted 9/22.
- **Decision tree at the print:**
  1. Oil ≤ 456 ⇒ **HIT** (final observation inside the window). Record `Date_Resolved 2026-09-25`, final print date, and **witness count = ONE Baker Hughes lineage**. Trading Economics / Investing.com are retrieval paths, not independent measurements (9/15 note).
  2. Oil ≥ 457 ⇒ **MISS**. Two retrievals of the primary workbook plus one aggregator; the breach is PROVISIONAL until the primary's OIL cell is read (8/21 note).
  3. Primary unreachable ⇒ **do not grade off an aggregator alone.** Record NOT-YET-GRADED with the aggregator figure and retry. The window has closed on observations, not on reading them.
- **Procedure:** `instrument_check.py --id BRT-26-RIGS` (live reader) → open the NAM Summary cell → confirm the print date is 2026-09-25 → second retrieval.
- **Brier input:** 0.85 on the outcome. Also report the 60% first-call mark separately (WQ-112 convention).

## BRT-29 — aviation-led demand destruction (conf 55%)

**Legs and state:**

| Leg | Letter | State |
|---|---|---|
| Premise | GASREGW ≥$4.00 in ≥4 of 6 prints 7/27–8/31 | **MET 6/6** (9/7, two lineages) |
| M | ≥3 further named carriers cut capacity citing fuel/war economics by 8/31, AND jet 4-wk YoY below gasoline in the lead window | **INDETERMINATE** (9/15 second review); jet below gasoline only intermittently, 8/14 and 8/21 |
| **T** | EIA gasoline 4-wk YoY **≤ −3.0% by the wk-ending-9/25 print** | **Not reached; out of reach** |

**T arithmetic** [CONF EIA WPSR `WGFUPUS2`, v2 API, pulled 2026-09-25 ~10:40 ET; reproduces the 9/16 note's −1.0119% for wk-9/11 and the 9/23 routine's −0.78% for wk-9/18]:

| Week ending | Weekly (kb/d) | 4-wk avg | Year-ago 4-wk | 4-wk YoY |
|---|---|---|---|---|
| 8/21 | 9,043 | 8,931.8 | 9,030.5 | −1.09% |
| **8/28** | 8,922 | 8,904.5 | 9,049.8 | **−1.61%** (deepest in the window) |
| 9/04 | 8,551 | 8,801.2 | 8,926.8 | −1.41% |
| 9/11 | 8,798 | 8,828.5 | 8,918.8 | −1.01% |
| 9/18 | 8,847 | 8,779.5 | 8,848.5 | **−0.78%** |

- **To print ≤ −3.0% at wk-9/25, the single week-ending-9/25 number must be ≤ 7,555 kb/d.** The last print was 8,847 and the same week last year was 8,518, so that is a **−14.6% week-on-week** fall. **Base rate** [CONF EIA `WGFUPUS2` weekly, 2010–2026, 873 weeks; checked 2026-09-25]: outside Mar–Jun 2020, WoW falls of ≥14.3% occurred only in **holiday or weather weeks**: 12/30/2022 −19.4% · 12/31/2021 −16.0% · 7/08/2022 −14.4% (post-July 4) · 2/19/2021 −14.3% (Winter Storm Uri). The week ending 9/25 has no holiday. *(An earlier draft of this line said no such week had occurred outside COVID; the check refuted that before commit.)*
- **Modal = MISS on T.** Once T fails, M does not matter for the outcome: the row needs T. Record M as INDETERMINATE for the lesson, per `[[finding_threshold_vs_mechanism]]`: premise met, phenomenon partly observed in aggregate capacity data, named-carrier form unfilled.
- ⚠️ **Which failure clause applies:** the falsifier's "never reaches ≤ −1.5%" path is **not** the operative one, because wk-8/28 printed −1.61%. The failure is on **T as written** (≤ −3.0% by the named print). Per the 9/8 note, −1.5% is a sufficient failure only, never an alternate success bar. **Classify MISS on T; do not write "never reached −1.5%".**
- **Jet now runs ABOVE gasoline:** jet 4-wk YoY **+6.2%** at wk-9/18 against gasoline −0.78%. Aviation is not leading on this series now. This is outside the elapsed M window and is recorded as context only.
- **Grade at the 9/30 print only.** The letter names that print; no early final grade even at this distance.

## BRT-12 — first Phase-2 credit warning shows in refiner spreads before upstream E&P OAS (conf 80%)

**Pre-committed rule (8/13, Will-approved slate; written before the outcome):** *if by 2026-09-30 neither signal has appeared ⇒ VOID on the no-NEITHER-branch spec defect; if either appears ⇒ grade the ordering normally.*

**Evidence state at 2026-09-25:**

| Leg | Instrument | Reading |
|---|---|---|
| Upstream E&P OAS widening | **None exists.** FRED rejects `BAMLH0A0E2Y` (9/8); LIQUID carries HY-Energy OAS as **permanently unmeasured** | **Unobservable.** Broad HY context only [CONF FRED `BAMLH0A0HYM2`]: 265bp (9/1) → **280bp (9/24)**, +15bp in the last week. CCC: 1,049 → **1,112bp**. Not energy-specific. |
| Refiner-spread compression as a *Phase-2 credit warning* | Crack series, named contracts | **One candidate to adjudicate:** Nov ULSD crack 109.49 (9/22) → **95.57 (9/24)**; Nov Brent 3:2:1 57.64 → **50.12** |

**Adjudication question for 9/30: is the 9/22–24 compression "the first Phase-2 credit warning"?** My lean is **NO**, for three reasons:
1. **Wrong phase.** The compression is crude-led under a Phase-1 supply shock: Brent +$7.35 over the two sessions, with the Petroline and Yanbu outage live. Phase 2 per THESIS is OPEC+ unwind or demand destruction, and neither is underway.
2. **Level.** Cracks remain historically extreme. The 3:2:1 is still ~$50 against a 2010–25 September spot median of about $14 (`research/2026-09-25_crack-seasonality/`), so this is a narrowing of a record margin, not margin stress.
3. **No credit symptom.** VLO equity rose (+1.9% 9/23→24, TERRY's correlation read); no refiner credit spread series exists.

**This lean runs against my own interest.** Calling the compression the signal would score BRT-12 a HIT at 80%, since no E&P OAS widening can be shown. Classifying it as not-the-signal forgoes that HIT. It is still my call on my own support, and LESSONS #27 applies: a desk cannot review its own support. ⇒ **Ask HENRY (crack co-owner) for a blind read of the classification before 9/30.** Send the letter and the evidence table, not my lean (messaging rule 7: blind first).

**A second spec defect to record with a VOID:** the race has an **unobservable runner**. The E&P OAS leg has no instrument fleet-wide, so the ordering could never have been adjudicated even if both events happened. Record both defects (no NEITHER branch; one leg unmeasurable) in the note. The lesson is a registration check: *every leg of a race must have a named, working instrument at registration.*

**Grading procedure 9/30:**
1. Re-pull the crack path through the 9/29–30 settles.
2. Check for any new energy-credit event (E&P downgrade or distress headline) via WALTER.
3. Get HENRY's blind classification.
4. Apply the 8/13 rule.
5. VOID ⇒ excluded from calibration; write both defects and the lesson.
