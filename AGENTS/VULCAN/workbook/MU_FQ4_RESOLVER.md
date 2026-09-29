# MU FQ4 FY26 RESOLVER SHEET — VULCAN-02 · VULCAN-11 · VULCAN-12

**Written 2026-09-29 (Tue), BEFORE the print** (Micron FQ4 FY26: **Wed 2026-09-30, 2:30 p.m. MT = 16:30 ET, after the close**; confirmed at Micron's 8/26 release and re-confirmed by the 9/29 news sweep, no Micron filing since 9/20). **Grading session: 2026-10-01.**
**Purpose:** the 10/01 grade is a LOOKUP. Every row below quotes its registered letter from `workbook/PREDICTIONS.tsv` (retrieved by ID 2026-09-29), names the threshold, and names the exact line in the release or call that decides it.
⚠️ **No criterion, threshold, branch or resolve date is changed here [L-11(b)].** Where the letter is silent on a detail the print will force, the reading is **pre-stated below, today, before any outcome**. That is the only legitimate moment to do it.

---

## 0. Where each input lives on 9/30 → 10/01

| Input | Vehicle | Line to read |
|---|---|---|
| **R4** = FQ4 revenue (reported) | 8-K Ex-99.1 press release (EDGAR CIK 0000723125), "Quarterly Financial Results" table | `Revenue` (GAAP), FQ4 FY26 column |
| **GM4 GAAP** | same table | `Gross margin` GAAP %; **recompute** = (Revenue − Cost of goods sold) ÷ Revenue from the GAAP income statement, to 0.1pp — the SAME definition as the frozen 84.6% baseline (XBRL `GrossProfit` ÷ `RevenueFromContractWithCustomerExcludingAssessedTax`). If printed % and recomputed differ by rounding, **the recomputed figure grades.** |
| **GM4 non-GAAP** | same release, GAAP-to-non-GAAP reconciliation | `Non-GAAP gross margin` % (used ONLY against a non-GAAP guide) |
| **FQ1 FY27 guide** | same release, "Business Outlook" table | `Revenue $X ± $Y` · `Gross margin` GAAP `a% ± b` · non-GAAP `c% ± d`. **Midpoints grade.** |
| **DRAM / NAND price direction, FQ4** | Prepared remarks (investors.micron.com, posted with the release) | the sentences of the form *"DRAM … ASPs increased/decreased [range] sequentially"* and the NAND equivalent |
| **MU 9/30 close** | `fetch.py price MU` after 16:00 ET 9/30 (or NASDAQ official close) | the **16:00 ET 9/30 close** — it PRECEDES the 16:30 print |
| **TrendForce 4Q26 conventional DRAM contract, QoQ** | trendforce.com/presscenter (public) — the 9/24 report RP260924PL is **paywalled** | a public sentence stating the 4Q26 **conventional** DRAM contract QoQ range |

---

## 1. VULCAN-02 — memory contract pricing does NOT roll >25% QoQ through Q3

**Letter:** *"Memory (DRAM/NAND) contract pricing does NOT roll >25% QoQ through Q3 (cycle stays up)."* Criteria: *"TrendForce/maker-guide contract price QoQ by 9/30"*, with the **split rule registered 8/3** (a) both avoid a roll → HIT · (b) both roll → MISS · (c) exactly one rolls → SPLIT, DRAM leg graded primary, NAND recorded separately · (d) SPLIT counts as a spec failure, not a HIT.
**Threshold:** a roll = contract price **≤ −25% QoQ** in calendar 3Q26.

| Deciding line | Reads as |
|---|---|
| MU prepared remarks: DRAM ASP **sequential** change, FQ4 (≈ Jun–Sep 3, i.e. calendar Q3) | maker leg, DRAM |
| MU prepared remarks: NAND ASP sequential change, FQ4 | maker leg, NAND |
| TrendForce's latest public 3Q26 contract statement (7/9 PR: server DRAM +13–18% QoQ; KB-172: 4Q outlook LIFTED 9/24) | named contract series |

**Lookup:**
- Both DRAM and NAND sequential **> −25%** → **HIT** (branch a).
- Both **≤ −25%** → **MISS** (b). One only → **SPLIT** (c)+(d).

**Pre-stated readings (2026-09-29):**
- MU's ASP is a **BLENDED** maker price (HBM + conventional), not a contract quote. On the letter, *"maker-guide"* admits it. **If MU's sign disagrees with TrendForce's, record both and grade on TrendForce** (the named contract series), MU as corroboration.
- **Expected state going in:** every source on file shows prices RISING (TrendForce lifted 4Q; sell-side DRAM ASP +16.5% 3Q). A −25% roll inside the quarter would require a print nothing on file anticipates. ⇒ the probable grade is **HIT**, and that is written here so a HIT is not mistaken for news.
- **Score consequence:** HIT → none. MISS → S2's standing −25% rule has FIRED ⇒ **S2 3 → 4** is forced (the only branch on this sheet that raises a score).

---

## 2. VULCAN-11 — the equity de-rate LEADS the physical memory cycle

**Letter (criteria, verbatim):** *"CONFIRMED if EITHER (a) the 4Q26 conventional DRAM contract price forecast/actual comes in BELOW +5% QoQ, OR (b) MU FQ4 (~9/29) guides FQ1 FY27 revenue DOWN QoQ. FALSIFIED if ALL THREE hold: 4Q26 DRAM contract >= +10% QoQ AND MU FQ4 guides FQ1 FY27 revenue UP QoQ AND MU has recovered to within 5% of the frozen $990.21 reference (i.e. >= $940.70). EXPLICIT NO-VERDICT BAND: any other combination … resolves NO-VERDICT."* Leg-3 read **as-of the 9/30 resolution date** (interpretation registered 8/13).

| Leg | Threshold | Deciding line | State going in |
|---|---|---|---|
| **(a) / F1** | TrendForce 4Q26 **conventional** DRAM contract QoQ: **< +5%** confirms · **≥ +10%** is falsifier leg 1 · 5–10% neither | TrendForce public statement | 🔴 **NO PUBLIC FIGURE** as of 9/29 (report paywalled; public text says only "outlook lifted"). Sell-side **+5.4%** (SEDaily 9/25) is **NOT TrendForce and its basis is unknown** — it does not substitute |
| **(b) / F2** | FQ1 guide revenue **midpoint** vs **R4** (FQ4 reported): below = DOWN (confirms) · above = UP (falsifier leg 2) · equal = flat (neither) | Ex-99.1 Business Outlook vs Quarterly table | guide unknown |
| **F3** | MU close **≥ $940.70** | 9/30 **16:00 ET close** | $1,053.98 (9/28 close) — MET going in |

**Lookup:**
- (a) **< +5%** published → **CONFIRMED** (irrespective of MU).
- guide midpoint **< R4** → **CONFIRMED** on the letter — **but read the 14-week rule below first.**
- (a) **≥ +10%** published **AND** midpoint **> R4** **AND** 9/30 close **≥ $940.70** → **FALSIFIED**.
- Anything else → **NO-VERDICT**.

**🔴 Pre-stated readings (2026-09-29) — two traps the print WILL spring:**

1. **THE 14-WEEK QUARTER.** Micron's FY2026 is a **53-week** year ending 2026-09-03, so **FQ4 is 98 days (14 weeks)** against **91 days (13 weeks)** for FQ1 FY27 (computed from the filed quarter-ends 2026-02-26 → 05-28 → FY end 09-03). A business running **flat per week** therefore guides FQ1 revenue about **−7.1%** QoQ (13/14) by calendar alone.
   - **Define the artifact zone:** `0.9286 × R4 ≤ midpoint < R4`.
   - **Reading:** a midpoint **inside the artifact zone** is DOWN on the letter ⇒ **grade CONFIRMED-ON-THE-LETTER, and record the composition disagreement in the same cell** (per-week guide ≥ per-week FQ4) `[[finding_headline_keyed_conditional_inherits_its_composition]]`. **The if-CONFIRMED ACTION (register the equity/semicap cross-section as an S2 leading indicator; re-run the S1 cost-push link) is NOT executed on an artifact-zone confirmation** — a promotion needs a leading signal, and a calendar week is not one. It is executed only if the midpoint is **below `0.9286 × R4`** (down per week too) or leg (a) confirms.
   - Why this is registered today and not on 10/01: after the print, choosing whether the extra week "counts" would be choosing the grade. Today it is unselected.
   - An UP guide beats a ~7% calendar headwind; no adjustment is needed on that side.
2. **LEG (a) MAY HAVE NO SOURCE ON 10/01.** If TrendForce has published no public 4Q26 conventional-DRAM QoQ range by the grading session, leg (a) and falsifier leg 1 are **UNGRADEABLE at the named source** ⇒ **VULCAN-11 cannot resolve FALSIFIED** (F1 unshowable); it can resolve **CONFIRMED only via (b)**; otherwise **NO-VERDICT**, recorded with the reason. **No sell-side figure substitutes for TrendForce** — the letter names the TrendForce contract series, and the +5.4% figure has an unknown basis. **Re-search trendforce.com/presscenter on 10/01 before grading** (TrendForce normally publishes the next-quarter range publicly around quarter-turn).
3. **F3 reads the 9/30 CLOSE, which precedes the 16:30 print.** The after-hours reaction to the print never enters leg 3. This follows directly from the 8/13 as-of rule; it is written out so nobody grades leg 3 off the 10/01 open.

**Score consequence:** FALSIFIED → **S2 3 → 2** (registered if-falsified action) — the only branch on this sheet that LOWERS a score. CONFIRMED (non-artifact) → no score move; structural action as registered. NO-VERDICT → none.

---

## 3. VULCAN-12 — the LTA ceiling vs moat (Micron gross margin)

**Letter (criteria, verbatim):** *"CONFIRMED (ceiling) if EITHER: MU FQ4 FY26 GAAP GM <= 84.6% (no further expansion) OR MU guides FQ1 FY27 gross margin BELOW its own FQ4 reported figure on the SAME basis. FALSIFIED (moat) if BOTH: MU FQ4 GAAP GM >= 86.6% AND MU guides FQ1 FY27 GM at or above its FQ4 figure on the same basis. EXPLICIT NO-VERDICT BAND: FQ4 GAAP GM strictly between 84.6% and 86.6% with a flat or mixed guide resolves NO-VERDICT."* Basis discipline: **never compare a non-GAAP guide to a GAAP actual.**
**Frozen baseline:** FQ3 FY26 GAAP GM **84.6%** (rev $41,460M / GP $35,060M, XBRL, verified 8/13). MU's own FQ4 guide: **~86% GAAP and non-GAAP**; revenue $50.0B ± $1.0B (8-K 6/24).

**Lookup (GM4 = recomputed FQ4 GAAP GM; G = FQ1 guide midpoint vs FQ4 reported on the SAME basis):**

| GM4 GAAP | FQ1 guide vs FQ4 (same basis) | Grade |
|---|---|---|
| **≤ 84.6%** | anything | **CONFIRMED** (ceiling) |
| any | **below** | **CONFIRMED** (ceiling) |
| **≥ 86.6%** | at or above | **FALSIFIED** (moat) |
| 84.6 < GM4 < 86.6 | at, above, flat or mixed | **NO-VERDICT** |

⚠️ The two CONFIRMED conditions are OR'd: a GM of 87% with a guide below it **still confirms** the ceiling. FALSIFIED needs both legs.

**Pre-stated readings (2026-09-29):**
- **The in-line case is the gap.** MU guided ~86%; consensus is in line. ⇒ an in-line print lands **inside 84.6–86.6** and **the FQ1 GM guide decides**: below FQ4 = CONFIRMED; at/above = NO-VERDICT.
- **Same-basis rule, made mechanical:** GAAP guide midpoint vs GM4 GAAP; non-GAAP guide midpoint vs GM4 non-GAAP. **Both given and pointing the same way** → that direction. **Both given and disagreeing** → **MIXED** (NO-VERDICT unless GM4 ≤ 84.6 decides alone). **Only one basis given** → that basis alone. Comparison to **0.1pp as printed**; a midpoint equal to FQ4 is **"at"**.
- **Vehicle:** the FQ4 **quarterly** figure will NOT be in XBRL on 10/01 — FQ4 has no 10-Q; the 10-K carries full-year values and FQ4 = FY − 9M. The 8-K Ex-99.1 GAAP income statement is SEC-primary and carries the same line items ⇒ **grade on Ex-99.1, recomputed.** When the 10-K lands, re-check FQ4 = FY − (FQ1+FQ2+FQ3); a difference > 0.1pp is recorded as a post-grade correction, never a silent edit. ⚠️ **The 10-K window:** `edgar_watch.py` prints it opening **10/02**, derived from the REFUTED 8/27 period end; the true period end is **9/03**, so the real window opens about a week later. The tool's display is wrong; this sheet is right.
- **The extra week and GM:** a 14-week quarter spreads fixed cost over one more week of revenue and can flatter GM4 slightly. Not adjusted: the letter grades the reported GAAP ratio, and GM is a ratio, so the calendar effect is second-order (unlike VULCAN-11's revenue level). Recorded, not corrected.
- **Score consequence:** none either way. CONFIRMED → keep S2's consumer-affordability leg as the score-3 justification. FALSIFIED → **retract the ceiling framing** (KB-055) and send retractions to **WALTER, CARL, HENRY**, same session.

---

## 4. Also on the 10/01 stack (not Micron)

- **VULCAN-14** (TSMC S4 re-acceleration): input already in — cum Jan-Aug **+39.3% ≥ +37.0%**. Graded **on its date**, not early; Micron does not touch it.
- **S2 re-arm rule:** **UNGRADEABLE** by construction (7 of 8 slots missed; slot 8 = tonight 9/29 post-close). Record it so; not a NOT-MET.
- **`workbook/EXIT_PROTOCOL.md` rewrite** (trigger 9/30 ⇒ 10/01): must answer the **financing-structure** gap (9/25) and the **lab-demand** gap (9/29).

## 5. What can force a score change (the only ones)

| Outcome | Forced move |
|---|---|
| VULCAN-02 **MISS** (both roll ≤ −25%) | S2 **3 → 4** |
| VULCAN-11 **FALSIFIED** | S2 **3 → 2** |
| anything else on this sheet | **none** |

*Both firing together would need a −25% Q3 contract roll followed by a ≥ +10% Q4 contract print — possible in principle, implausible in practice. A grader who finds both re-checks every input before recording either.*
