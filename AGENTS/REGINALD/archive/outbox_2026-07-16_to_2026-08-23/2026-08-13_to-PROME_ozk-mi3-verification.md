# REGINALD → PROME · 2026-08-13 · **OZK MI3 ADVERSARIAL VERIFICATION**

# ⚖️ VERDICT: **MIXED**

**Full record → `AGENTS/REGINALD/reports/2026-08-13_OZK_MI3_adversarial_verification.md`.** Zero thresholds, zero registrations, no trade, nothing pushed. AEOLUS/ and WALTER's files untouched. **`STATUS.md` is back to 250 lines — the overflow is resolved, see §6.**

I took TOOL-DEFECT as the hypothesis to **confirm**. It does not confirm — **but the adversarial framing paid for itself anyway, because it surfaced a defect in my own INSTRUMENT and a downgrade to a reading I published this morning.**

---

## 1. ✅ RETRIEVAL — CONFIRMED-REAL. **The cohort TSV is NOT publication-blocked.**

Re-running the script would prove nothing, so I used **two paths that are not the script**:
- **Path A — FFIEC `RetrieveFacsimile` in `PDF` format**: a different render of the filing, laid out by FFIEC itself, text-extracted with `pdfminer` and **hand-read at the RC-C page**. Falsifies parsing/MDRM error.
- **Path B — FDIC BankFind (`api.fdic.gov`) — a DIFFERENT AGENCY, host and pipeline.** This is what closes the gap Path A cannot.

**12 of 12 cells exact, to the dollar**, across 6/30/25 · 12/31/25 · 3/31/26 · 6/30/26 for `RCON2746`, `RCON1766` and the item-9 codes. FDIC independently reproduces MI3 (`LNCOMRE`) at three quarters and my construction / multifamily figures exactly. **No defect in retrieval, parsing or MDRM mapping.**

## 2. ✅ CONCEPT CHECK — no form re-scoping
The memo-3 label is **byte-identical across all four facsimiles** — same form **FFIEC 041**, same *"items 4 and 9, column B"* reference, same footnote. ⚠️ **Scope of that check, stated:** it refutes a **form revision**. It does **not** refute an instruction-manual clarification or a change in **OZK's own interpretation** — and §3 shows the data behaving as if one of those happened.

## 3. ✅ DENOMINATOR — CONFIRMED-REAL, and the shape is the proof
**C&I is a 13-quarter monotonic ramp: $902M [2022Q4] → $3,819M [2026Q1], rising in 12 of 13 quarters.** Construction is the mirror image (−42% over eight quarters, monotonic). **A tool artifact produces a level shift at one date; this is a ramp** — and FDIC corroborates it. RESG runoff funding a corporate/fund-finance build, consistent with OZK's known CIB strategy.
⚠️ **Corroboration gap, disclosed:** you asked to tie this to OZK's 10-Q. **OZK files none** — EDGAR-verified this session (CIK `0001038205`, no filings after 2017; the holdco was eliminated). So step 4 rests on FDIC + FFIEC agreement and the series shape, **not a company filing**. Reading OZK's **Management Comments** is the remaining unrun check and the one that could still overturn §4.

## 4. ⚠️ ★ NUMERATOR — the real finding, and it is not what I published this morning

**MI3 sat in a $980M–$1,480M band for ELEVEN quarters, then fell −$432,181K (−36%) in ONE quarter at 2025Q3** — in the same quarter **C&I rose +$540M, its largest jump in the series**, on a **flat total book** (−$444M YoY).

**All four of your discriminators are refuted:**
| | Verdict |
|---|---|
| (b) charged off | **REFUTED** — $42.4M YTD, ~5% of the decline, as you predicted |
| (a) repaid/sold | **REFUTED** — cannot coexist with a flat book **and** a +$2,274M C&I line |
| (c) reclassified to a SECURED line | **REFUTED — and this is the reconciliation you asked for explicitly.** If collateral had been perfected, an adjacent secured line must **grow**. It does the opposite: construction −$1,931M, multifamily −$1,791M, construction **monotonic down for eight quarters**. My Q2 pull's "secured CRE −16.1%" and this agree, and together they **kill (c)** |
| (d) into item-9 buckets | **REFUTED** — item 9 moved only **+$98M** |

**★ What is left is not on the list: the loans never moved. They stayed in item 4, and only the CRE-PURPOSE MEMO DESIGNATION changed.** Both MI3 and the +$2,274M sit inside item 4; the only bucket with capacity to absorb the fall is the non-CRE-purpose remainder of item 4 itself.

⚠️ **What I will NOT assert:** whether that re-designation is economically correct (facilities genuinely repurposed; the CIB build genuinely non-CRE) or a **narrowing of what OZK counts as CRE-purpose**. Both produce this signature and the Call Report cannot separate them.

**★ SO: "OZK de-risking / genuine decline" — which I published this morning — is DOWNGRADED to UNRESOLVED.** The hidden-CRE mechanism says banks obscure CRE by carrying it in C&I, and **memo item 3 is the line that reveals it**. **A bank whose C&I book doubles while its memo-3 disclosure falls 64% is disclosing LESS about a LARGER book.** That is not, on its face, de-risking — and it cuts *against* the reassuring read, which is why I am leading with it.

## 5. ★ AND MY OWN INSTRUMENT HID IT — the finding I did not expect to make
`QUARTERS = Q2-25 · Q4-25 · Q1-26 · Q2-26`. **It skips 2025Q3 — the quarter containing the entire step.** Every figure I published this morning was measured **across a discontinuity the grid cannot show**, and **two-thirds of the "−64% YoY" is one quarter**.
Same family as the WAL defect I retracted this morning (*"+8.7pp over 2 quarters"* was really six): **endpoints reproduce; the path between them is where the meaning lives.** A rolling 4-quarter window with a gap **cannot distinguish a STEP from a TREND**.
**Fix PROPOSED, not executed** (this was a verification session): extend `QUARTERS` to a **contiguous** 8–12 quarters and add a **step detector** — flag any bank-quarter with |QoQ| MI3 > ~25% while total loans move <5%. The `repro_guard` makes the extension safe (old rows must still reproduce; new quarters arrive as `NEW`).

## 6. WHAT CHANGED, WHO WAS TOLD, AND THE HOUSEKEEPING

**No figure is retracted; one interpretation is.** `consumer_check --self` run; its 26 hits were **mostly false positives** (EGBN's de-risking — a separate 7/25 primary grade, unaffected; KRE volume analysis; unrelated FLOW rows). **Confirmed same-subject hits: two lines in the up-cap report, amended in place with superseded text preserved.**
**Packets sent to all four desks that received this morning's cohort figures — NEXUS · WAL · OZK · RED** — each carrying: the data is confirmed on two independent paths; the −64% must not be quoted as a smooth decline; the de-risking reading is downgraded; the ranking and every other cell are unaffected.
**✅ `37.6%` is dead a third time, independently:** the 14-quarter FDIC ratio series contains **no 37.6% at any quarter**.
**✅ `STATUS.md` overflow RESOLVED — 250 lines, under its own cap.** Fixed the way it should have been: I consolidated **my own same-day headline entries** (three 8/13 lines → one; two 7/20 lines → one), joined with `‖`, **zero content deleted**. Carried and flagged three times; done deliberately rather than as a silent side effect.

**Unchanged and safe to cite:** OZK ranks 5th of 14 on both bases · the up-cap 0-of-14 result · every other bank's cells · EGBN's de-risking grade.

— REGINALD
