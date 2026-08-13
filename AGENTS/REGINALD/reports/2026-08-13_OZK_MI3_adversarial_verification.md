# OZK MI3 COLLAPSE — ADVERSARIAL VERIFICATION

# ⚖️ VERDICT: **MIXED**

> **RETRIEVAL: CONFIRMED-REAL, no tool defect.** 12 of 12 cells reproduce **to the dollar** on an independent render path, and MI3 plus every denominator reproduce **again at a different agency** (FDIC, different host, different pipeline). Nothing in my parser, MDRM mapping or SDF handling is wrong. **The cohort TSV is NOT publication-blocked.**
> **DENOMINATOR LEG: CONFIRMED-REAL.** OZK's C&I book really did roughly double — and it is a **13-quarter monotonic ramp** ($902M Q4-2022 → $3,819M Q1-2026), not a jump. A tool artifact cannot produce that shape.
> **⚠️ NUMERATOR LEG: NOT a tool defect — but NOT a clean economic decline either, and this is the finding.** MI3 oscillated $980M–$1,480M for **eleven quarters**, then fell **−$432,181K (−36%) in ONE quarter at 2025Q3**, while C&I *rose* $540M in that same quarter — its largest quarterly increase in the series. **Loans did not leave the balance sheet; the memo-item-3 label did.** That is the signature of a reporting/classification change, and the Call Report alone cannot adjudicate whether it was justified.
> **★ AND MY OWN INSTRUMENT HID IT.** The screen's `QUARTERS` list is `Q2-25 · Q4-25 · Q1-26 · Q2-26` — **it skips 2025Q3, which is the single most informative quarter in the series.** My published **"−64% YoY"** is arithmetically correct and **straddles the step**, so it presents a possible definitional break as an economic trend.

**Date:** 2026-08-13 · **Agent:** REGINALD · **Authority:** Will-directed adversarial verification, TOOL-DEFECT as the hypothesis to *confirm*.
**Entity:** BANK OZK · `ID_RSSD 107244` · FDIC cert **110** · filing form **FFIEC 041**.

---

## 1. INDEPENDENT RETRIEVAL — two paths, neither of them the script's

**Path A — FFIEC `RetrieveFacsimile` in `PDF` format** (a different render of the filing; the numbers are laid out by FFIEC, not parsed by my MDRM code), text-extracted with `pdfminer` and **hand-read** at the RC-C page.
**Path B — FDIC BankFind API** (`api.fdic.gov`, **different agency, different host, different pipeline**), which exposes the same concepts under its own field names.

| Quarter | Cell | Script TSV | **Path A — FFIEC PDF** | **Path B — FDIC** | Match |
|---|---|---:|---:|---:|---|
| 6/30/2025 | RCON2746 (MI3) | 1,202,101 | **1,202,101** | **1,202,101** (`LNCOMRE`) | ✅ |
| 12/31/2025 | RCON2746 | 721,546 | **721,546** | **721,546** | ✅ |
| 3/31/2026 | RCON2746 | 489,284 | **489,284** | **489,284** | ✅ |
| 6/30/2026 | RCON2746 | 430,277 | **430,277** | *(not yet in FDIC index)* | ✅ |
| 6/30/2025 | RCON1766 (item 4) | 2,330,142 | **2,330,142** | **2,330,142** (`LNCI`) | ✅ |
| 12/31/2025 | RCON1766 | 3,431,585 | **3,431,585** | **3,431,585** | ✅ |
| 3/31/2026 | RCON1766 | 3,818,846 | **3,818,846** | **3,818,846** | ✅ |
| 6/30/2026 | RCON1766 | 4,603,672 | **4,603,672** | — | ✅ |
| 6/30/2025 | item 9 (J454+J464) | 3,177,436 | **3,163,310 + 14,126** | — | ✅ |
| 12/31/2025 | item 9 | 2,755,752 | **2,742,514 + 13,238** | — | ✅ |
| 3/31/2026 | item 9 | 3,071,157 | **3,057,519 + 13,638** | — | ✅ |
| 6/30/2026 | item 9 | 3,275,845 | **3,264,019 + 11,826** | — | ✅ |

**12 / 12 exact.** FDIC additionally reproduces construction (`LNRECONS` 8,684,947 = my 1.a.1+1.a.2) and multifamily (`LNREMULT` 4,336,103 = RCON1460) to the dollar.

⚠️ **Stated limit:** Path A is a different *render* of the same filing, so it falsifies **parsing/mapping** error, not **filing** error. Path B is a genuinely different agency — that is what closes the gap. **Two independent paths, one of them a different institution: the retrieval is sound.**

## 2. CONCEPT CHECK — no instruction or form change in the window

The memo-item-3 label was extracted from **all four PDF facsimiles** and compared character-for-character:

> *"3. Loans to finance commercial real estate, construction, and land development activities (not secured by real estate) included in Schedule RC-C, part I, items 4 and 9, column B"* — **byte-identical at 6/30/2025, 12/31/2025, 3/31/2026 and 6/30/2026**, same footnote marker, same form **FFIEC 041** throughout.

**So the FORM did not re-scope the cell.** ⚠️ **What this does NOT rule out:** an *instruction-manual* clarification (the FFIEC instructions are a separate document from the form face) or a change in **OZK's own interpretation** of an unchanged instruction. §3 shows the data behaving as if one of those happened. **This check refutes the form-revision hypothesis; it does not refute the reporting-change hypothesis.** (`finding_verification_zero_is_ambiguous` — it certifies its scope.)

## 3. ★ NUMERATOR DECOMPOSITION — and the 14-quarter series changes the question

FDIC `LNCOMRE`, 14 quarters, independent of my tooling:

| Quarter | MI3 $K | QoQ | C&I $K | Construction $K | MI3/C&I |
|---|---:|---:|---:|---:|---:|
| 2022Q4 | 1,479,154 | — | 902,321 | 8,287,936 | 163.9% |
| 2023Q2 | 1,364,503 | +72,725 | 1,268,787 | 9,446,030 | 107.5% |
| 2023Q4 | 1,241,457 | +143,513 | 1,269,610 | 11,653,487 | 97.8% |
| 2024Q2 | 1,229,202 | +58,704 | 1,499,489 | 11,491,194 | 82.0% |
| 2024Q4 | 1,055,957 | +76,946 | 1,728,801 | 9,522,678 | 61.1% |
| 2025Q1 | 1,133,405 | +77,448 | 2,066,290 | 9,208,619 | 54.9% |
| **2025Q2** | **1,202,101** | +68,696 | 2,330,142 | 8,684,947 | 51.6% |
| **2025Q3** | **769,920** | **−432,181** ⚠️ | **2,870,535** *(+540,393, largest in series)* | 8,489,956 | 26.8% |
| 2025Q4 | 721,546 | −48,374 | 3,431,585 | 7,778,411 | 21.0% |
| 2026Q1 | 489,284 | −232,262 | 3,818,846 | 7,112,891 | 12.8% |

**Eleven quarters in a $980M–$1,480M band with no trend, then a −36% single-quarter drop.** That is a **step**, not a runoff.

**Answering the "where did ~$770M go?" discriminators directly:**
- **(b) charged off — REFUTED.** Known debt-on-debt charge-offs are **$42.4M YTD**, ~5% of the decline. Confirmed as impossible-to-be-the-story.
- **(a) repaid/sold — REFUTED as the main story.** Total loans & leases were **essentially flat** across the window: 33,005,054 [Q2-25] → 32,560,970 [Q2-26], **−$444M**, against a $772M MI3 fall plus a $2,274M C&I rise. **A $772M repayment cannot coexist with a flat book and a doubling C&I line.**
- **(c) reclassified into a SECURED line — REFUTED, and this is the reconciliation Will asked for explicitly.** If MI3 loans had perfected collateral and become secured-by-RE, an adjacent **secured** line must grow by a matching amount. **It does the opposite:** construction 1.a.2 **−$1,931M**, multifamily 1.d **−$1,791M**, and construction falls **monotonically for eight straight quarters**. **The secured book is shrinking, not absorbing.** This is the explicit reconciliation against my own Q2 pull (secured CRE −16.1%): the two findings agree, and together they **kill hypothesis (c)**.
- **(d) moved into item-9 buckets — REFUTED.** Item 9 total moved **3,177,436 → 3,275,845 = +$98M**, nowhere near $772M.
- **★ (e) — WHAT IS LEFT, and it is not on Will's list: the loans stayed exactly where they were, in item 4, and only the MEMO LABEL changed.** Item 4 **rose $2,274M** while MI3 **fell $772M**. Both are inside item 4. **The only bucket with the capacity to absorb the decline is the non-CRE-purpose remainder of item 4 itself.** In 2025Q3 specifically, MI3 fell $432M in the same quarter C&I rose $540M — its biggest jump ever. **Loans did not move between schedules; the CRE-purpose designation moved.**

⚠️ **What I cannot determine from the Call Report, and will not assert:** whether that re-designation was **economically correct** (facilities genuinely repurposed, or the CIB/fund-finance build genuinely non-CRE) or a **narrowing of what OZK counts as CRE-purpose**. Both produce this signature. **Resolving it requires OZK's own disclosure, which §4 shows is unusually thin.**

**★ The direction matters for the thesis, and it cuts against the reassuring read.** My hidden-CRE discovery says banks obscure CRE by carrying it in C&I — and memo item 3 is the line that *reveals* it. **A bank whose C&I book doubles while its memo-item-3 disclosure falls 64% is disclosing less about a larger book.** That is not, on its face, de-risking. **I published "OZK de-risking / genuine decline" this morning. That claim is now DOWNGRADED to UNRESOLVED.**

## 4. DENOMINATOR LEG — real, and the shape is the proof

**C&I: 902,321 [2022Q4] → 3,818,846 [2026Q1] — up 4.2× across 13 quarters, rising in 12 of them.** Smooth, monotonic, no step. **A tool defect produces a level shift at one date; this is a ramp.** Independently confirmed at the FDIC. Construction runs the mirror image: **−42% over eight quarters, monotonic.** Together: **RESG runoff funding a corporate/fund-finance build** — consistent with OZK's publicly-known CIB and lender-finance strategy.

⚠️ **Corroboration gap, disclosed rather than papered over.** Will asked to tie this to OZK's own 10-Q. **OZK files none.** Verified at EDGAR this session: CIK `0001038205` ("BANK OF THE OZARKS INC") has **no filings after 2017** — the holding company was eliminated that year. This **confirms the standing note in my `CLAUDE.md`** ("OZK files NO SEC 10-Q — primary = FDIC Call Report + Mgmt Comments"). **So step 4's corroboration is FDIC + FFIEC agreement plus the series shape — not a company filing.** Reading OZK's quarterly **Management Comments** for the CIB/fund-finance narrative is the remaining, unrun check, and it is the one that could still overturn §3.

## 5. ★ THE INSTRUMENT FINDING — my own quarter list hid the step

`QUARTERS = ["6/30/2025", "12/31/2025", "3/31/2026", "6/30/2026"]`. **2025Q3 — the quarter containing the entire −36% step — is not in it.** Every figure I published this morning was measured across a discontinuity I could not see, on a grid too coarse to show it.

- **A rolling 4-quarter window with a gap cannot distinguish a STEP from a TREND.** My "−64% YoY" is arithmetically right and **interpretively wrong-by-omission**: two-thirds of it is one quarter.
- Same family as the defect I retracted this morning at WAL — *"+8.7pp over 2 quarters"* was really six. **Endpoints reproduce; the path between them is where the meaning lives.** (`finding_new_pin_needs_trajectory_before_level_read`.)
- **Proposed fix, not executed** (verification session, zero changes to the instrument): extend `QUARTERS` to a **contiguous** 8–12 quarter run, and add a **step detector** — flag any bank-quarter where |QoQ| in MI3 exceeds ~25% while total loans move <5%. The existing `repro_guard` makes the extension safe: old rows must still reproduce, new quarters simply arrive as `NEW`.

## 6. WHAT CHANGES, AND WHAT DOES NOT

| Claim published 2026-08-13 AM | Status after verification |
|---|---|
| Every cohort cell / the TSV as a data artifact | ✅ **CONFIRMED — 12/12 exact on two independent paths, one at a different agency. NOT publication-blocked.** |
| OZK item-4 denominator ~doubled | ✅ **CONFIRMED-REAL** — 13-quarter monotonic ramp, FDIC-corroborated |
| OZK MI3 dollars −64% YoY | ✅ **arithmetically CONFIRMED** — ⚠️ **but it spans a −36% single-quarter step at 2025Q3 and must not be quoted as a smooth economic decline** |
| **"OZK de-risking / genuine decline"** | ⚠️ **DOWNGRADED to UNRESOLVED.** The loans stayed in item 4; only the CRE-purpose designation moved. Disclosure shrank while the book grew. |
| **"OZK ranks 5th of 14, not the most concentrated"** | ✅ **unchanged** — a ranking of reported values, and the reported values are confirmed |
| `37.6%` kill-on-sight | ✅ **CONFIRMED a third time, independently** — the FDIC series runs 163.9 · 118.5 · 107.5 · 87.4 · 97.8 · 86.4 · 82.0 · 65.1 · 61.1 · 54.9 · 51.6 · 26.8 · 21.0 · 12.8. **37.6% appears at no quarter in fourteen.** |
| Up-cap decomposition (0/14 relabel signatures) | ✅ **unaffected** — OZK classified BOOK-EXPANSION on both legs falling, which this verification confirms as *reported*; the §3 step is a **memo-label** event the co-movement test was never built to see |

**Owed:** a packet to the four desks that received this morning's cohort figures (**NEXUS · WAL · OZK · RED**) carrying the qualification in row 3 and the downgrade in row 4. **No figure is retracted; one interpretation is.**

*— REGINALD, 2026-08-13. Paths: FFIEC CDR `RetrieveFacsimile` PDF (pdfminer, hand-read) · FDIC BankFind `api.fdic.gov` · SEC EDGAR submissions API. All pulled 2026-08-13.*
