# FROZEN GRADING CARD — QCEW Preliminary Benchmark, Fri 2026-08-28, 10:00 ET

**Written:** 2026-08-07 ~17:45 ET, **21 days before the print** · **Status: FROZEN.**
**Author:** LABOR · **Card class:** C2a benchmark/quarterly gauge (quarterly-card rule, Will-ruled 7/31) · **Enumerated at boot by B5b.**

> **Why this card is written three weeks early.** The last two prints I graded without a card cost **0.64** and **0.5625** of Brier between them. This one carries **LAB-08 (65%)** — the only OPEN row ≥60% — and **vector 8**, which is one of only two 🔴s left in the book. It is the largest scheduled item I own.

---

## 0. §C gate #15 declaration — the source and the arithmetic, named before any band

**Source:** BLS *Current Employment Statistics Preliminary Benchmark Announcement*, `bls.gov/news.release/prebmk.htm` (+ `prebmk.nr0.htm`), **10:00 a.m. ET Friday 2026-08-28**. Date and time [CONF] verbatim in **USDL-26-1291**: *"At 10:00 a.m. (ET) on August 28, 2026, the Bureau of Labor Statistics (BLS) will publish the preliminary estimate of the upcoming annual benchmark revision to the establishment survey data."* Q1-2026 QCEW issues the same day. ⚠️ **bls.gov 403s to WebFetch — use the BD-18 UA-header curl.**
**The figure:** the **preliminary estimate of the benchmark revision to the March-2026 total nonfarm employment level**, in thousands and as a percent, headline and private/government split.
**The arithmetic that settles each band:** the printed preliminary figure `P`, converted to a percent of the **published March-2026 CES level (158,650K)**, and mapped to an **implied final** via §2's ratio band. **No other computation is required and none may be substituted at grade time.**

---

## 1. 🔴 THE STRUCTURAL FACT THIS CARD EXISTS TO PIN DOWN — **Aug 28 does NOT resolve LAB-08**

**LAB-08 = *"BLS benchmark revision >500K downward,"* due Q1 2027.** Per USDL-26-1291: *"The final benchmark revision will be issued with the publication of the January 2027 Employment Situation news release in February 2027."*

**So the instrument that RESOLVES LAB-08 is the FINAL, in Feb 2027. Aug 28 prints the PRELIMINARY.** They are different numbers, and **publication lag decides membership** — the same principle that froze LAB-06's N at 5 draws. **Aug 28 is a confidence gate, not a resolution. Anyone (including me) who reads a preliminary ≥500K as "LAB-08 confirmed" is wrong on the letter.**

---

## 2. 🔴 AND THE FINAL HAS COME IN **SMALLER** THAN THE PRELIMINARY, THREE YEARS FOR THREE

| Benchmark (March ref) | **Preliminary** | **Final** | Final ÷ Prelim |
|---|---|---|---|
| March 2023 | −306K | **−187K** | **0.61** |
| March 2024 | −818K | **−598K** | **0.73** |
| March 2025 | −911K | **−862K** | **0.95** |

**Mean ratio ≈ 0.76; observed range 0.61–0.95; direction 3-for-3 toward a smaller final.** Mechanistically expected: the preliminary uses QCEW through Q1 only, and BLS refines with later QCEW quarters, reconstructions and updated birth-death estimates before the final.

⚠️⚠️ **n = 3. This is a TENDENCY, not a calibrated relationship, and all three are post-COVID years with unusual dynamics.** I am using it as a **band**, never as a point estimate, and the card states the implied-final range rather than a single number every time.

**Implied final from a preliminary `P`:** `0.61P` to `0.95P`, centre `≈0.76P`.
**Inverting it — what LAB-08's >500K bar actually requires of the preliminary:**

| Ratio assumption | Preliminary needed for a >500K final |
|---|---|
| Favourable (0.95) | **≥ 526K** |
| Central (0.76) | **≥ 658K** |
| Unfavourable (0.61) | **≥ 820K** |

🔴 **Therefore: a preliminary of 500–650K does NOT make LAB-08 likely.** It maps to an implied final of roughly **305K–620K, centred ~380–495K — mostly BELOW the bar.** **LAB-08 at 65% has been implicitly asserting a preliminary near 700K+, and no surface of mine ever said so.**

## 2b. The other calibration input: BLS's own dispersion

BLS states that over the prior 10 years the **absolute** percentage benchmark error averaged **0.2%**, range **<0.05% to 0.4%**. On a March-2026 level of **158,650K**: average ≈ **317K**, range ≈ **79K to 635K**.
**LAB-08's 500K bar = 0.315% — above the 10-year average and in the upper part of the historical range.** *(The 2024 and 2025 finals — 598K and 862K — both exceeded it, and 862K exceeds even the stated 0.4% top, which is why those years are correctly described as exceptional rather than typical.)*

---

## 3. 🔧 PRE-PRINT REPRICE OF LAB-08 — **65% → 35%**, declared now, 21 days before the print

**This is a re-registration under §C gate #14, and it is legitimate only on that gate's terms — which are met:**
- **Declared BEFORE the print, with this commit as the receipt.** Never claimable retroactively.
- **Unforced.** No new data has landed; the trigger is arithmetic I had never done — §2's prelim→final ratio and §2b's dispersion.
- **Symmetric.** If the preliminary prints ≥820K, this same 35% scores *badly* where the original 65% would have scored well. It cuts both ways or it does not count.
- **Scoring is unchanged: LAB-08 resolves at its as-made 65%** (§A convention). The 35% is a separate labelled diagnostic and is **not** folded into the mean.

**The arithmetic behind 35%,** decomposed so it can be checked rather than asserted — P(preliminary band) × P(final >500K | that band):

| Preliminary band | My P(band) | Implied final range | P(final >500K \| band) | Contribution |
|---|---|---|---|---|
| ≥700K | 0.375 | 427–665K | 0.67 | 0.251 |
| 450–700K | 0.350 | 275–665K | 0.20 | 0.070 |
| <450K | 0.275 | <428K | 0.03 | 0.008 |
| | | | **Total** | **≈ 0.33 → posted 35%** |

**Why the cut is this large.** Three things compound: **(a)** the bar sits above BLS's own 10-year average revision; **(b)** the final has been smaller than the preliminary in every observed year; **(c)** **LABOR is 0-for-4 at ≥60% on threshold calls and 3-for-3 on mechanism calls at the same confidence** — a 65% *threshold* call is in the exact category the record says I get wrong.
**What is NOT the reason:** the mechanism is intact and I am not conceding it. Downward monthly revisions are compounding (−74K → −103K), the Oct-2025 collection hole is real, and the immigration/birth-death dynamic that produced the 2024–25 revisions is still operating. **The mechanism supports a large downward revision; the THRESHOLD at 500K on the FINAL is what I was overpricing** (`[[finding_threshold_vs_mechanism]]`).

---

## 4. BANDS — committed assignments on the PRELIMINARY

| Band | Preliminary (downward) | % of level | Implied final (0.61–0.95) | LAB-08 | Vector 8 | Assignment |
|---|---|---|---|---|---|---|
| **A** | **≥900K** | ≥0.57% | 549–855K | **→ 75%** | **holds 4** | Exceeds even 2025's preliminary. Measurement layer confirmed as the dominant bearish leg. **Route 🔴.** |
| **B** | **700–899K** | 0.44–0.57% | 427–854K | **→ 60%** | **holds 4** | The band LAB-08's original 65% implicitly assumed. Above the historical range top. |
| **C** | **500–699K** | 0.32–0.44% | 305–664K | **→ 30%** | **holds 4** | ⚠️ **The trap band. A headline "half a million jobs revised away" that does NOT make LAB-08 likely** — implied final centres ~380–495K, below the bar. **Say that explicitly the same day**; it will be reported as a huge number and my own prediction still probably fails. |
| **D** | **300–499K** | 0.19–0.31% | 183–474K | **→ 12%** | **4 → 3** | Around BLS's 10-year average. The exceptional-revision regime is normalising. |
| **E** | **<300K** or **upward** | <0.19% | <285K | **→ 4%** | **4 → 2** | 🔴 **Vector 8 was upgraded to 4 on 8/7 specifically on the compounding-revision premise. This band refutes that premise and the vector must fall — say so plainly.** |

**Band D/E force a cut to a vector I upgraded three weeks earlier. That is deliberate: the upgrade was made on a premise this print can refute, and the card commits the reversal now so it cannot be argued away later.**

**Also record, in every band (they cost nothing and are the actual content):** the **private vs government split** (2025: −880K private / −31K government); the **implied revised monthly average** for the 12 months to March 2026; and whether BLS names the **birth-death model** or the **Oct-2025 collection gap** in its own text.

---

## 5. Mechanism vs threshold — pre-stated (§C gate #3)

**A LAB-08 miss falsifies the 500K THRESHOLD ON THE FINAL. It does NOT falsify:** that CES overstates employment in this regime; that the birth-death model is mis-calibrated to a shrinking-immigration labour force; or that vector 8's measurement-layer read is right. **Those are mechanism claims and this print does not test them at the 500K line.**
Conversely **a LAB-08 hit does not validate my sizing** — it would mean the mechanism was strong enough to clear a bar I could not justify from the base rates. **Say which one happened.**

## 6. Attribution discipline — what I will NOT do

- **Not treat the preliminary as the resolution.** LAB-08 resolves **Feb 2027**. If I catch myself writing "LAB-08 confirmed" on Aug 28, that is the error this card exists to prevent.
- **Not quote a single implied-final point estimate.** The ratio is n=3. Quote the **range**, always.
- **Not attribute the revision to any single cause** — birth-death, immigration, the Oct-2025 hole and QCEW coverage are entangled and I cannot separate them from this release.
- **Not read a large revision as new information about the CURRENT labour market.** It restates **March 2026**. The 8/7 print already told me the count is negative *now*; a benchmark tells me the *level* was wrong *then*.
- **Not let this leak into the demand-vs-supply attribution I declared unresolved on 8/7.** A benchmark revision speaks to measurement, not to which side of the market moved.
- **Not re-cut the bands after seeing the print.** If it lands outside A–E, that is a card defect to record (§6 discipline) — but A–E are exhaustive by construction, so an unlisted outcome would mean I mis-specified the axis, not the levels.

## 7. Routing — pre-committed

| Outcome | Route | Priority |
|---|---|---|
| Band A or B | **REGINALD + CARL + HENRY + PROME/NEXUS** — the payroll level has been materially overstated all year, which re-bases every trailing average anyone is using | 🔴 |
| Band C | **PROME/NEXUS only**, with the trap explicitly flagged: **big headline, LAB-08 still probably fails** | 🟠 |
| Band D or E | **NEXUS + PROME — calibration record.** Vector 8 cut; no thesis packet | 🟡 |
| Any band | `PREDICTIONS.tsv` + `PREDICTIONS_SCOREBOARD.md` (confidence move only — **no resolution row until Feb 2027**) + `PUBLISHED.tsv` | — |

## 8. Grading discipline

1. **Grade off the BLS primary** (`prebmk.nr0.htm` via UA-curl), not a wire summary — L-12.
2. **Grade off THIS card**, band by band. A band written here outranks whatever seems obvious on print morning.
3. **Spine sweep after the print** (C1): every surface carrying vector 8, LAB-08 or a trailing-average figure.
4. **`PUBLISHED.tsv`** row for the LAB-08 confidence move, ISO-timestamped.
5. **LAB-08 scores AS-MADE at 65%** whenever it finally resolves — the 35% is a labelled diagnostic only.
6. **Re-read §1 before writing anything.** The single most likely error on the day is treating the preliminary as the final.

---

*Frozen by LABOR 2026-08-07, 21 days before the print. Consume at B5b. Grade off this card, not off the tape.*

---

# ADDENDUM — 2026-08-23 ~18:5x ET, **5 days before the print**

> ⛔ **THIS ADDENDUM CHANGES NO BAND, NO ASSIGNMENT, AND NO CONFIDENCE.** §4's bands A–E, §3's 35%, §7's routing and §8's discipline are **exactly as frozen on 2026-08-07**. Written **before** the print, Will-approved, as a record of what moved in the card's *information model* — not in its content. **If this addendum has moved a number, it is a defect and the frozen text wins.**

## A. Verified: the card's denominator is intact

§0 and §4 convert the printed preliminary `P` to a percent of the **published March-2026 CES level, 158,650K.** **Re-pulled 2026-08-23: PAYEMS March-2026 = 158,650K — unrevised.** [CONF FRED/BLS PAYEMS, obs 2026-03-01, pulled 2026-08-23]. **Every percentage in the §4 band table therefore still holds as written.** *(Checked because a revised denominator would silently shift all five band boundaries while the card still read correct — the card's own arithmetic is the thing most likely to rot between freeze and grade.)*

## B. The two external inputs this card was written expecting have BOTH now failed to arrive

The card was frozen on 8/07. Two things have happened since, and **neither touches a band** — but together they change what the 35% is standing on.

1. **The 8/19 FOMC minutes: branch D-2 ABSENT.** Graded 8/20. `data quality` / `response rate` / `benchmark` = **0 occurrences each.** The branch-(c) watch closed with **no Fed corroboration of the data-degradation premise.**
2. 🔧 **Jackson Hole is NOT a pre-print input — my ledger was wrong by 7 days.** The card was written while `CATALYSTS.tsv` carried JH as **Fri Aug 21**, i.e. a week *before* this print. **Corrected 2026-08-23: the symposium is Aug 27–29 and Warsh's keynote is Fri Aug 28 10:00 ET — the SAME MORNING as this release.** It therefore **cannot inform this card at all**; it arrives simultaneously. *(Date is PROME-verified-at-primary + MNI wire 8/20 + weekday check; recorded as relayed, **not** `[CONF]` — kansascityfed.org returns HTTP 403 to this fleet.)* And per the same-day finding, the keynote theme is reported as *"Financial Innovation: Implications for Payments and Policy"* `[2ND]` — **neither branch of the watch** — so it would most likely close **uninformative, not negative**.

⇒ **The consequence, stated plainly: LAB-08 walks into this print with ZERO external input having arrived — not from the minutes, not from Jackson Hole.** The 35% stands **entirely** on §2's prelim→final ratio band, §2b's BLS dispersion, and §3's decomposition. **That is not a weakening of the reprice — it is the reprice being exactly what it declared itself to be: unforced arithmetic, not a response to news.** §3's "unforced" claim is *strengthened* by this, not undermined.

## C. 🔴 NEW GUARD, bought by the collision — pre-committed now, before the print

The 8/07 card could not have written this, because on 8/07 the two events were believed to be a week apart.

**Warsh speaks at 10:00 ET. This release publishes at 10:00 ET. They are simultaneous.**

⛔ **I will NOT let same-morning Jackson Hole language move the band assignment, vector 8, or LAB-08's confidence.** Specifically, and in both directions:

- **If Warsh names payroll reliability, QCEW, the benchmark or CPS response rates:** that is the branch-(c) tell firing **late**, it is **testimony, not measurement**, and it is **not** an input to which band this print lands in. Log it as its own item; **do not fold it into the QCEW grade.**
- **If Warsh says nothing about labour data** (the likely case given the reported theme): that is **UNINFORMATIVE, not negative** — silence under an off-topic program is not evidence about the Fed's data priorities, and it must **not** be read as refuting vector 8.
- **The band is a function of the printed figure `P` and nothing else** (§0: *"No other computation is required and none may be substituted at grade time."*).

**Why this guard is needed:** two events landing in the same minute is the exact condition under which a same-day narrative gets built across both. §6 already forbids attributing the revision to a *cause*; this extends it to forbid attributing it to a *speech*. **It also fails safe: if I catch myself citing Warsh anywhere in the QCEW grade, that is the defect this addendum exists to prevent.**

## D. Unchanged and re-affirmed

- **§1 stands and is still the single most likely error on the day:** Aug 28 prints the **PRELIMINARY**; **LAB-08 resolves on the FINAL, Feb 2027.** No resolution row is written on 8/28 under any band.
- **§4 Band C remains the trap band** — a "half a million jobs revised away" headline that still leaves LAB-08 probably failing.
- **LAB-08 scores AS-MADE at 65%.** The 35% is a labelled diagnostic and is not folded into the mean.
- **Bands D/E still force the vector-8 cut** I pre-committed on 8/07.

*Addendum written 2026-08-23 by LABOR, 5 days before the print, Will-approved. **The frozen card above is unamended.** Grade off §4, not off this addendum and not off the tape.*
