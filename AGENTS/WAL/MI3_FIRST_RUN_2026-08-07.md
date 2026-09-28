# V1a MI3 — FIRST-EVER RUN AND GRADE

**Date:** 2026-08-07 · **Session:** WAL #2 (PROME-directed spawn), scope extension after Will cleared the FFIEC CDR blocker same day.
**Instrument:** FFIEC CDR Public Web Service, **REST + JWT**, `RetrieveFacsimile` / SDF. Entity **ID_RSSD 3138146** (Western Alliance Bank; FDIC cert 57512). Recipe from `AGENTS/DAEDALUS` packet, commit `f32f2fb8a`.
**Spec graded against:** the **FROZEN v2.1 MI3 calibration table** (`THESIS.md` §"Outstanding V1 PRIMARY TEST", lines 210-223) and the **Bear-fast KILL** exit rule in `STATUS.md`. No spec text was edited before or after grading.
**Series data:** `workbook/MI3_SERIES.tsv` (12 quarters, machine-readable).

> ## 🔨 HEADLINE
> **The V1a primary falsifier has run for the first time in the thesis's life — on BOTH available 2026 quarters — and it comes back DISCONFIRMING, concordantly, with room to spare.**
> **Q1-2026 MI3 = 23.88% · Q2-2026 MI3 = 21.20%.** Both land in the frozen table's **`<24%` → "V1 PLATEAUED"** band. The **Bear-fast KILL** rule (MI3 <25%) **FIRES**, on the exact instrument it named.
> **The ~Sep 1 bear-fast time-box is DISSOLVED** — it existed only to force a disposition call if the falsifier never ran. It ran.
> ⚠️ **The KILL firing is the pre-registered grade and is recorded as executed. The re-allocation of bear-fast's 10% weight is NOT pre-registered and was NOT executed — it is a v2.4 proposal to Will (§6).**

---

## 0. SPEC-EXECUTABILITY CHECK (run BEFORE grading, per the WAL-01/Schedule-O defect class found earlier today)

| Question | Answer |
|---|---|
| Does the Call Report actually carry the numerator? | ✅ **Yes.** `RCON2746` present in every quarter pulled, schedule `RCCI`, line `M3`, full FFIEC label: *"Loans to finance commercial real estate, construction, and land development activities (not secured by real estate) included in Schedule RC-C, part I, items 4 and 9, column B."* |
| Does it carry the denominator the spec names ("Item 4")? | ✅ **Yes.** `RCON1766`, schedule `RCCI`, line **`4`**, label *"Commercial and industrial loans."* The spec's "Item 4" resolves unambiguously. |
| Does the historical baseline reproduce on this basis? | ✅ **Yes, exactly — see §2.** This is the decisive check. |
| **Verdict** | ✅ **SPEC IS EXECUTABLE. No `NO-VERDICT-SPEC-DEFECT`.** The grade proceeds. |

**★ This is the first WAL rule tested today that named an instrument which could actually carry its datum** — after MI3-is-not-a-10-Q-line (correctly routed here), the void *"Q3 10-Q Schedule O"*, and v2.3.1 leg (a). The rule that was hardest to *run* turned out to be the best-*specified* one.

⚠️ **One basis caveat — flagged, NOT improvised around.** RCON2746's own FFIEC definition says its balance sits in **items 4 AND 9**, while the frozen spec's denominator is **item 4 only**. The numerator therefore includes dollars the denominator excludes, which **inflates** the printed ratio. I graded on the **frozen basis (item 4)** because that is what the spec says and what the 24.2% baseline was built on — changing the basis mid-grade is exactly the improvisation PROME's instruction rules out.

**The verdict is ROBUST to that choice, which is why the caveat changes nothing:**

| Basis | Q1-2026 | Q2-2026 | vs 25% trigger |
|---|---|---|---|
| **Frozen spec — MI3 ÷ item 4** | **23.88%** | **21.20%** | both **below**, both falling |
| Fuller — MI3 ÷ (item 4 + item 9a) | 10.34% | 9.17% | far below |

Repair proposed in §6 (**P8**), not applied.

---

## 1. THE PULL — provenance, and what makes it trustworthy

| Step | Result |
|---|---|
| `RetrieveReportingPeriods` (`dataSeries: Call`) | 200 — periods through **6/30/2026** confirmed available |
| `RetrieveFacsimile`, RSSD 3138146, SDF, **3/31/2026** | **200**, 244,178 bytes → **1,797 SDF rows** |
| `RetrieveFacsimile`, RSSD 3138146, SDF, **6/30/2026** | **200**, 246,442 bytes → **1,814 SDF rows** |
| Plus 10 historical quarters, 9/30/2023 → 12/31/2025 | all **200** |

**Two independent confirmations that this is the right entity and the right data:**
1. **`RCON2170` (total balance-sheet assets) at 3/31/2026 = $98,766,387K** — matches DAEDALUS's independently-pulled spot value **to the dollar**.
2. **`RCONJ454` (item 9a, loans to nondepository financial institutions) ties to the 10-Q to the dollar** — see §4.

⚠️ **One live gotcha worth recording:** the base recipe is correct, but **`python-urllib`'s default User-Agent is 403'd by the Azure Application Gateway** in front of `ffieccdr.azure-api.us`. `curl` succeeds with identical headers. Same class as the EDGAR-403 finding. The failure is a **WAF/UA block, not an auth failure** — do not debug the token when a 403 appears with an Azure-Application-Gateway HTML body (auth failures return 401, or 500 with codes 5001/5003).

---

## 2. ★ THE BASELINE REPRODUCES EXACTLY — and the trajectory claim does not

`THESIS.md:212` states: *"WAL's MI3 ratio (RCON2746 / Item 4) was **24.2%** per prior screen and growing (**15.5% → 24.2% — +8.7pp over 2 quarters**, fastest in cohort…)."*

| Claim | Computed from primary | Verdict |
|---|---|---|
| MI3 = **24.2%** ("prior screen") | **12/31/2025 = 24.24%** | ✅ **REPRODUCES** |
| MI3 = **15.5%** (start of the run) | **6/30/2024 = 15.51%** | ✅ **REPRODUCES** |
| **+8.7pp** | 24.24 − 15.51 = **+8.73pp** | ✅ **REPRODUCES** |
| **"over 2 quarters"** | 6/30/2024 → 12/31/2025 = **SIX quarters** | ❌ **WRONG BY 3×** |

**Both endpoints are right; the interval is wrong by a factor of three.** That single error made the trend look **3× steeper than it was**: the claimed +4.37pp/quarter is actually **+1.46pp/quarter** — and, as §3 shows, not even a steady climb.

This is why the baseline check had to run before the grade. Had the levels *not* reproduced, the correct output would have been a basis dispute, not a verdict. They did, so the grade stands on the identical basis to the number the thesis was built on.

---

## 3. THE FULL SERIES — 12 quarters, and it changes the shape of the question

MI3 = `RCON2746` ÷ `RCON1766` (item 4), the frozen basis. Machine-readable → `workbook/MI3_SERIES.tsv`.

| Quarter | MI3 $K | C&I item 4 $K | **MI3** | QoQ pp | Frozen band |
|---|---:|---:|---:|---:|---|
| 2023-09-30 | 907,244 | 8,327,780 | 10.89% | — | <24 |
| 2023-12-31 | 899,159 | 8,850,297 | 10.16% | −0.73 | <24 |
| 2024-03-31 | 1,481,601 | 8,816,860 | 16.80% | **+6.64** | <24 |
| **2024-06-30** | 1,494,563 | 9,633,571 | **15.51%** ⬅ *the "15.5%"* | −1.29 | <24 |
| 2024-09-30 | 1,609,970 | 10,059,406 | 16.00% | +0.49 | <24 |
| 2024-12-31 | 2,047,935 | 9,371,561 | 21.85% | **+5.85** | <24 |
| 2025-03-31 | 2,307,710 | 9,589,515 | 24.06% | +2.21 | 24.0-24.9 partial |
| 2025-06-30 | 2,245,837 | 9,990,574 | 22.48% | −1.59 | <24 |
| 2025-09-30 | 2,252,290 | 10,253,572 | 21.97% | −0.51 | <24 |
| **2025-12-31** | 2,729,877 | 11,262,949 | **24.24%** ⬅ *the "24.2%" screen · **all-time high*** | +2.27 | 24.0-24.9 partial |
| **2026-03-31** | **2,722,527** | **11,399,418** | **23.88%** | −0.35 | **<24 → PLATEAUED** |
| **2026-06-30** | **2,554,610** | **12,047,671** | **21.20%** | **−2.68** | **<24 → PLATEAUED** |

**★★ Four structural findings the level alone would have hidden:**

1. **MI3 has NEVER reached 25% in twelve quarters.** All-time high **24.24%**. The bear-fast trigger (≥25%) has never once come within **76bps** of firing; the ≥27% "hard-confirm" band sits **276bps above the all-time high**. *The falsifier was not merely un-run — on the actual data it was never close to firing at any point in the observable record.*
2. **Since Q1-2025 the series OSCILLATES with no trend:** 24.06 → 22.48 → 21.97 → 24.24 → 23.88 → 21.20. Six quarters, ~3pp range, no direction. **"Growing" is not a property of this series.**
3. **The rise the thesis was built on was two discrete step-changes in 2024** (+6.64pp in Q1-24, +5.85pp in Q4-24), not an ongoing acceleration. Everything since has been flat-to-down.
4. **Q2-2026 is the lowest print in six quarters — and the numerator FELL in absolute dollars.** $2,729,877K (Q4-25) → $2,722,527K (Q1-26) → **$2,554,610K** (Q2-26): **−$175M / −6.4%** over two quarters, while C&I *grew* +$785M. Both moves push the ratio down, but **the numerator decline is the substantive one** — the hidden-CRE book is genuinely contracting, not just being diluted by denominator growth.

---

## 4. ★ INDEPENDENT CROSS-VALIDATION — the Call Report ties to the 10-Q to the dollar

`RCONJ454` (Schedule RC-C item 9a, *loans to nondepository financial institutions*) against this morning's 10-Q read:

| Date | Call Report `RCONJ454` | Q2 10-Q p.76 "Total loans to NDFIs" | Match |
|---|---:|---:|---|
| 2026-03-31 | **$14,927,699K** | **$14,928M** | ✅ exact |
| 2026-06-30 | **$15,812,034K** | **$15,812M** | ✅ exact |

**Two independent regulatory filings, prepared for different regulators on different schedules, agreeing to the dollar.** This is a genuine independent confirmation of this morning's NDFI finding — not a second reading of the same source.

**And the Call Report extends it from 2 data points to 12.** NDFI as a share of total loans (`RCONJ454 ÷ RCON2122`):

**15.7% → 15.9% → 16.8% → 18.3% → 18.8% → 21.0% → 21.5% → 21.8% → 22.4% → 23.6% → 23.6% → 24.1%**

**Rising in 11 of 12 quarters and monotonic non-decreasing since 2024-03-31.** This is a **multi-year structural trend**, not a one-quarter blip.

**→ This materially strengthens proposal P1 (V3 under challenge).** V3 was cut 2/5 → 1/5 on 7/25 on the premise that the NDFI/warehouse book is *"SHRINKING by management choice."* That premise is now contradicted by **two independent primary sources across twelve quarters.** *(Score still NOT moved — P1 remains Will's call.)*

---

## 5. THE GRADE — strictly off the frozen table, no improvisation

**Frozen v2.1 calibration table** (`THESIS.md` lines 216-221), reproduced verbatim in its four bands:

| MI3 print | V1 status |
|---|---|
| ≥27% | V1 hard-confirmed; multiple-hiding-places thesis active |
| 25.0-26.9% | V1 acceleration confirmed |
| 24.0-24.9% | V1 trajectory bending; partial confirmation |
| **<24%** | **V1 plateaued** |

### Verdicts

| Quarter | MI3 | Band | **GRADE** | Margin to the nearest boundary |
|---|---:|---|---|---|
| **Q1-2026 (3/31/26)** | **23.88%** | **<24%** | **V1 PLATEAUED** | ⚠️ **12bps** below the 24.00% boundary — *a near-boundary call, but unambiguously below* |
| **Q2-2026 (6/30/26)** | **21.20%** | **<24%** | **V1 PLATEAUED** | **280bps** below — unambiguous |

**The two quarters are CONCORDANT.** No split verdict, no tie-break needed. Had they split, this document would say so rather than picking the convenient one; they did not.

### The pre-registered exit rule

> **Bear-fast KILL** — *"MI3 <25% — carried **ONLY** by the FFIEC Q2 Call Report PDD (~Aug window; it is NOT a 10-Q line, DEWEY 7/16)."* State at session start: **⬜ UNRUN.**

**Q1-2026 = 23.88% <25% ✓ · Q2-2026 = 21.20% <25% ✓ — and the Q2 print is the exact carrying instrument the rule names.**

> ## ✅ **BEAR-FAST KILL — FIRED, 2026-08-07.**

### The time-box

> **⏱ Bear-fast TIME-BOX** — *"If the ~Aug FFIEC window ALSO passes unintegrated, that is the 3rd consecutive miss. Forced disposition call, no third deferral."* State at session start: **⬜ ARMED — trips ~Sep 1.**

The window did **not** pass unintegrated. The falsifier ran, on the named instrument, on both available quarters, and returned a verdict.

> ## ✅ **TIME-BOX — DISSOLVED, 2026-08-07. Purpose discharged, not deferred, not waived.**

**The forced-disposition machinery is no longer needed** because the thing it was built to compensate for — a weight carried on an untestable premise — is now tested. *(The time-box worked exactly as designed: it created the pressure that got the blocker cleared four weeks before it would have tripped.)*

---

## 6. WHAT WAS **NOT** DONE — the re-weight is a proposal, not a grade

> **Rider 2026-09-28:** P7 **EXECUTED** 8/20 (v2.4: bear-fast 10%→2%); P8/P9 self-ruled 8/20. THESIS line references in this file are 8/7 vintage — the calibration table now sits in THESIS §"EXECUTED V1 PRIMARY TEST"; anchor on the section name, not a line number.

**The 10% bear-fast weight was NOT moved, and no thesis version was bumped.** Reasons, stated so the restraint is auditable:

1. **The pre-registered grade is the band verdict plus the KILL rule's firing.** Both are recorded above. **Where the freed 10% goes is nowhere in any frozen spec.**
2. **The frozen table's *implication* column is stale-vintage and cannot be mechanically applied.** For the `<24%` band it reads: *"bear shifts back toward 30%; V2.2 demotes V1."* That is written against **v2.1→v2.2**, when "the bear" was a single weight. The live thesis is **v2.3**, where the bear is **split** into Bear-fast 10% + Bear-medium 16% = 26%. *"Shift the bear back toward 30%"* is **incoherent under v2.3's structure** — and mechanically applying it would **raise** total bear weight on a **disconfirming** result, which is plainly the wrong sign. **The status column graded cleanly; the implication column did not survive the version change.** → repair proposal **P9**.
3. PROME's instruction was explicit: *zero threshold moves outside the pre-registered MI3 grade itself.*

### Proposals — Will-gated, nothing executed

| # | Proposal | Basis |
|---|---|---|
| **P7** | **★ v2.4 re-mark owed: retire or fold bear-fast.** Its primary falsifier has now run and disconfirmed on two concordant quarters, and the series has never approached the trigger in 12 quarters. Options: **(i)** retire bear-fast to 0% and redistribute; **(ii)** fold its 10% into bear-medium (making one CRE-tail bear at ~26%); **(iii)** cut it materially and keep a residual. **Recommend (ii) or (iii), not a mechanical read of the stale implication column.** Total bear weight should **not rise** on a disconfirmation. |
| **P8** | **Repair the MI3 denominator spec.** RCON2746 sits in items **4 and 9**; the spec divides by item 4 only, inflating the ratio. Either restate as MI3 ÷ (item 4 + item 9a) with a re-based threshold, or keep item 4 and **document that it is a deliberately conservative (over-stating) basis**. ⚠️ **Re-basing changes the LEVEL, not this verdict** — both bases are far below 25% in both quarters. |
| **P9** | **Retire the v2.1 calibration table's *implication* column.** Its *status* column graded cleanly and should be kept as the calibration record; its implication column is written against a thesis structure that no longer exists. |
| **P10** | **Correct `THESIS.md:212`'s trajectory claim.** "+8.7pp over **2 quarters**" is **6 quarters** on the primary. Levels reproduce; the interval does not. *(Corrected in place this session as a factual fix with a CHANGELOG entry — no weights touched.)* |

---

## 7. WHAT THIS DOES AND DOES NOT SETTLE

**Settles:**
- V1a is **disconfirmed on its own pre-registered terms**, on two concordant quarters, with a reproducible baseline.
- MI3 is **not a rising series** and has never been near the trigger. The "fastest in cohort / growing" premise was a two-endpoint artifact spanning a mis-stated interval.
- The bear-fast time-box is discharged; the ~Sep 1 forcing date is gone.

**Does NOT settle:**
- **Nothing about V1b.** MI3 measured *hidden* CRE — CRE-purpose lending **not secured by real estate**. The **$99M life-science credit, the office book, the classified balance and the appraisal are all in the SECURED book and are untouched by this result.** ⚠️ **Do not read "V1a disconfirmed" as "V1 disconfirmed."** V1b-magnitude remains 4/5 and this morning's 10-Q added evidence for it (OREO office property count 15 → 22).
- **Cohort position.** This is WAL standalone. Whether 21.20% is high or low *versus peers* needs the same pull for the comparison set — REGINALD's lane, now unblocked and cheap.
- **Whether the metric ever mattered.** A falsifier that never came within 76bps of its trigger in 12 quarters raises a fair question about how the 25% line was chosen. Out of scope here; flagged.

---

*Graded 2026-08-07 off the frozen v2.1 calibration table and the STATUS Bear-fast KILL rule, with no spec text edited before or after. All figures A1 primary from FFIEC CDR PWS, RSSD 3138146. Series → `workbook/MI3_SERIES.tsv` · evidence rows KB-WAL-164..170 · Q2 10-Q companion read → `Q2_10Q_READ_2026-08-07.md`.*
