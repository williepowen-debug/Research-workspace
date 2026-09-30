# BRT-31 — Path-B successor to BRT-29: DRAFT for Will (WQ-331 P3)

> ⚠️ **SUPERSEDED 2026-09-30 12:2x ET by [v2](2026-09-30_BRT-31-path-B-successor-DRAFT-v2.md)** after CARL's blind read (❌1 base rate did not grade the letter; ❌2 no outcome precedence). Kept verbatim below as the record; **do not register from this file.**

**Status: DRAFT. NOT REGISTERED.** Written 2026-09-30 11:4x ET by BRENT, Will-directed ("go ahead and draft the Path-B successor"), under WQ-331 P3 (Will 9/28 18:36: a DRAFT after the 9/30 grade, returned to Will before the next print). **It enters `thesis/PREDICTIONS.tsv` only on Will's own word.** No row, gate, band or approval exists until then. $0.

**Why it exists:** BRT-29 FAILED today ([grade](../research/2026-09-30_wpsr-grades/REPORT.md) §3). Without a successor, Path B (demand weakening) has no registered test and becomes unfalsifiable by default (phase map §3, P3).

## 1 · The letter (proposed)

| Field | Proposed text |
|---|---|
| **Claim** | US gasoline demand weakens measurably under the sustained price shock: **EIA gasoline product supplied, 4-week average vs the same 4 weeks a year earlier, prints ≤ −1.5% on two consecutive weekly prints** within the window. |
| **Named series** | EIA WPSR `WGFUPUS2` (psw01.xls "Data 2"; the EIA primary spreadsheet, not the v2 API, which lagged on 9/30). **Method:** 4-wk avg of the latest 4 weeks ÷ 4-wk avg of the 4 weeks 52 weeks earlier − 1. It reproduces EIA's published figures: wk-9/11 −1.0119%, wk-9/18 −0.7798%, wk-9/25 +0.2587% (EIA prose "+0.3%"). |
| **Window** | **The first 8 weekly prints whose data week ends after Will's ruling.** If ruled before Wed 10/7 10:30 ET: data weeks ending **10/2 → 11/20** (releases 10/7, **Thu 10/15**, 10/21, 10/28, 11/4, **Thu 11/12**, 11/18, 11/25; the Thursdays come from EIA's holiday schedule). **Anchor type: DATA WEEK, never release date**, so a delayed release does not move the window. |
| **MET** | Any two **consecutive** window prints ≤ −1.5%. |
| **NOT MET** | **Every** window print > −1.0%. |
| **NO-VERDICT (a real answer)** | Everything else: a single print ≤ −1.5% without a consecutive second, or prints between −1.5% and −1.0%. |
| **Precondition (regime)** | The base rate below is conditioned on retail gasoline (`GASREGW`) ≥ +20% vs a year earlier. **If GASREGW YoY is below +20% on 3 or more of the 8 window weeks ⇒ NOT-FIRED-PRECONDITION** (price relief came first: record it for Path A; excluded from calibration). Today: +23.2% at its 12-week minimum; $4.465 on 9/28 vs ~$3.1 a year ago. |
| **Contamination (asymmetric; can only refuse)** | If a **federal or state fuel-tax cut** or other **policy action that lowers US pump prices** takes effect inside the window, **NOT MET cannot be graded from prints after its effective date** (a policy wedge, per WQ-331 P2). MET still grades, because demand falling despite a policy price cut is stronger evidence. **A US diesel-export restriction does not touch this series** (gasoline only). |
| **Excluded weeks** | **None.** Every exclusion is grader discretion. Holiday alignment was checked: Thanksgiving 2026 (11/26) and 2025 (11/27) fall in the year-aligned weeks. |
| **Mechanism (recorded, NOT a leg)** | Via sustained pump prices, not via a macro/income shock or supply outage. Recorded at grade for the lesson; **it does not gate the outcome.** BRT-29 failed partly on over-specified legs. |
| **Proposed confidence** | **30%** (§3). |

## 2 · Base rate [CONF EIA WPSR `WGFUPUS2` 1993–2025 + FRED `GASREGW`; reproducible: `research/2026-09-30_path-b-successor/baserate.py`]

Sample: weekly 4-wk YoY 1993–2025, excluding 2020-03 → 2021-12 (COVID) and **all of 2026 (the period under test)**. "High-price" = GASREGW YoY ≥ +20% in **every** one of the prior 12 weeks. **"Start ≥ −0.5%" matches today's starting point (+0.26%).** Each window start's next 8 prints are classified.

| Bar (two consecutive prints) | High-price, start ≥ −0.5% (n=88) | Ordinary, start ≥ −0.5% (n=1058) | MET separates signal from noise? |
|---|---|---|---|
| **≤ −1.5% (proposed)** | **MET 36% · NOT MET 35% · NV 28%** | MET 16% · NOT MET 64% · NV 20% | **Yes, ~2.3×** |
| ≤ −2.0% | MET 22% · NOT MET 35% · NV 43% | MET 12% · NOT MET 64% · NV 24% | Weakly, ~1.8× |
| ≤ −2.5% | MET 6% · NOT MET 35% · NV 59% | MET 8% · NOT MET 64% · NV 28% | **No** (worse than noise) |

**Reading the table:**
- **Why −1.5% and not BRT-29's −3.0%:** from a positive start over 8 weeks, a −2.5% or −3.0% bar is **no more likely in a price shock than in ordinary times.** It would have been a test that could only fail. This is the BRT-29 lesson, now measured.
- **What each outcome is worth:** MET is ~2.3× likelier under a price shock than in ordinary times, which is moderate evidence, not proof. **NOT MET is the more informative outcome:** 35% in shocks vs 64% in ordinary times. Demand that never even reaches −1% for 8 weeks during a +20% price shock is resilient.
- ⚠️ **Effective sample is ~5 price episodes, not 88 weeks:** 1999–2000, 2003–04, 2006–08, 2010–11, 2022. Window starts overlap and weeks are autocorrelated. **Treat every percentage here as ±10–15 points.**
- ⚠️ **One more cut by the noise floor:** a **16% MET rate in ordinary times** means a hit at −1.5% can be weekly noise. That is why the bar needs two consecutive prints, and why MET is labelled "weakening measured", **never "demand destruction confirmed"**.

## 3 · Proposed confidence: 30% (below the 36% base rate)

- **Base:** 36% (high-price, start ≥ −0.5%).
- **Down:** L12 (EVs lengthen demand adjustment). The current trend is rising: 4-wk YoY −1.61% (8/28) → +0.26% (9/25), and the single week of 9/25 is **+2.0% vs a year earlier**. BRT-29's 55% was over-confident on this same channel.
- **Up:** diesel retail $6.38 (9/28 [FRED GASDESW]) keeps freight and consumer budgets under pressure; +23% gasoline price YoY is persistent.
- ⇒ **30%.** Calibration anchor: consumer transmission, direct (one step: price → gallons), not the third-order chains where BRENT runs over-confident.

## 4 · Pre-flight (PREDICTIONS.tsv header)

1. **Can it fail to fire entirely?** No. Each outcome has a numeric band and a non-trivial base rate (≥20%). The precondition is the only non-grading exit, and it is itself a Path-A fact worth recording.
2. **True for wrong reasons?** A macro/income shock or a hurricane-driven supply week could print a fall. The 4-wk average plus two consecutive prints damp single-week events. The mechanism is recorded at grade. **False while the thesis holds?** Yes: demand can stay resilient while Phase 1 persists, which is exactly what NOT MET measures.
3. **Mechanism attribution:** "via sustained pump prices" is recorded, not graded (above).

## 5 · Governing lessons (`lessons_check.py --concept` run 2026-09-30 11:3x ET)

- **L09** (product supplied misleads in shock weeks 1–4): **honoured.** The shock is ~7 months old; no early-week read.
- **L12** (longer demand timeline): **honoured** in the confidence mark.
- **L21** (a threshold fails on its spec first; base-rate it before registering): **honoured.** §2 is the base rate, and it is what rejected −2.5%/−3.0%.
- **L22** (a trading/printing instrument, a number, frozen bands, verification run): **honoured.** WPSR prints weekly; bands are numeric; the method reproduces EIA's published figures; the script re-runs.
- **L06** (cracks tell the real story): **not applicable, deliberately.** This is a volume test. Cracks stay graded on their own lines (F1, TERRY's); a crack move never grades BRT-31.
- **L08** (storage data has reporting lag): **honoured.** The window keys on the DATA WEEK, so the ~5-day WPSR publication lag and holiday shifts cannot move it.
- **L23** (continuous `=F` tickers re-point at the roll): **not applicable.** No futures instrument is used.
- **L25** (a source that hangs is not down): **honoured, with a rule:** if the EIA spreadsheet or API fails or lags (the API served wk-9/18 at 10:56 ET on 9/30), retry by the other path. **A failed retrieval never grades or skips a print.** The print is graded when read.
- **L27** (a desk cannot review its own support): **not yet satisfied.** ⇒ **Recommend a blind second reader (HENRY or CARL) of §1–§2 before Will rules.** They would be sent the letter and the script, not this recommendation.
- ⚠️ **My own error in drafting, caught before any file:** a first base-rate pass joined gasoline to jet fuel, whose weekly series has gaps. That silently dropped 1994–2004 and produced MET 19% vs 14% at −2.5%. The saved script uses gasoline alone on the full sample. **I had reported the truncated figure to Will in chat, and corrected it the same session.**

## 6 · What Will decides

1. **Register as written** (−1.5%, two consecutive prints, 8 prints, 30%), **or adjust** the bar or window. §2 gives the cost of each alternative.
2. **Second reader first (recommended), or rule now.** If he rules after Wed 10/7 10:30 ET, the window simply starts one print later (data-week anchor).
