# MTB — Baltimore CRE reassessment + the largest absolute MI3 book in the cohort
## ⚑ FROZEN PRE-REGISTRATION — written 2026-09-02, BEFORE any data is pulled

**Status:** ⚑ **FROZEN — GRADED 2026-09-02 (2nd session, post-close). Thresholds untouched; RESULT column and §6 filled, nothing else edited.** VERDICT: **L2 = MUNICIPAL ⇒ TRUE AND IRRELEVANT; L5 = NO ROW.** ⛔ **Do not edit the thresholds below after reading data.** Fill the RESULT column only. If a threshold turns out to be badly specified, say so in §6 and grade against it anyway — a frame rewritten after the fact grades nothing. *(Same construction as the 7/18 watch-cards, which scored 4-of-4 and whose value was that the bar was set first.)*

---

## 1. Why this, why now

Two independent things point at MTB and neither was chased:

**(a) An unverified claim, carried 4 months.** `SIG-W-20260426-009` (Will signal, 2026-04-26, Baltimore Sun-sourced): **−$1B / 29% of reassessed CRE in Baltimore.** Never taken to primary. It has sat as an aged ROADMAP row since April.

**(b) My own instruments now say something the claim would fit.** Verified at `workbook/MI3_COHORT.tsv` on 2026-09-02:

| Quarter | MI3 book | v1a % | YoY |
|---|---|---|---|
| 6/30/2025 | $4.28B | 9.17 | **−18.9%** |
| 9/30/2025 | $4.61B | 9.81 | −13.4% |
| 12/31/2025 | $4.54B | 9.33 | −7.1% |
| 3/31/2026 | $5.07B | 10.05 | **+9.6%** |
| 6/30/2026 | **$4.95B** | 9.69 | **+15.7%** |

★ **The trajectory INVERTED monotonically over five quarters — from double-digit contraction to double-digit growth.** And **$4.95B is the largest absolute MI3 book in the cohort by ~1.9×** (next: WAL $2.55B · HBAN $2.21B · CFG $2.14B).

⚠️ **The tension that makes this worth a session:** my rebuilt Convergence Matrix scores **MTB 1** — near-clean on both instrumented channels — while MTB carries the cohort's largest absolute hidden-CRE-class book, growing. **My own 8/13 report flags exactly this as invisible to a ratio screen**, and leaves the question open in writing: *"whether MTB's $4.95B absolute book warrants a Matrix row"* (`reports/2026-08-13_MI3_cohort_rerun.md` §Owed next).

⛔ **A `1` on the matrix means clean on TWO SCORED CHANNELS, never a clean bill of health** — the same caveat already carried for CFG (scores 0 holding ~$44.5B committed PC-NDFI).

---

## 2. What I am NOT claiming going in

- **MI3 growth is not deterioration.** A bigger CRE-purpose-C&I book can be origination, an acquisition, or a reclassification. **The whole point of the mechanism finding is that the BUCKET moves; the ratio alone never says why.**
- **The Sun figure may be wrong, stale, or about a different perimeter** (city vs MSA; assessed value vs loan exposure; a reassessment cycle vs a credit event). **Assessed-value reassessment is a MUNICIPAL TAX event and is NOT a bank charge-off** — conflating them would be the headline error available here.
- MTB is **not** on the watchlist and this frame does **not** propose adding it.

---

## 3. Pre-registered legs (thresholds SET BEFORE DATA)

| # | Test | Source | Threshold set 9/2 | RESULT |
|---|---|---|---|---|
| **L1** | Does the Sun claim reproduce at primary? | Baltimore Sun piece + whatever it cites (city assessment record / SDAT) | **REPRODUCES** = the −$1B and the 29% both trace to a named, dated primary. **PARTIAL** = one half traces. **FAILS** = neither, or the perimeter is not MTB's book | ✅ **REPRODUCES — all four figures, verbatim.** Baltimore Sun **2026-04-19** (ZH picked it up 4/26, so the signal's own date is the aggregator's, not the source's): *"More than $1 billion in commercial property value has been erased from Baltimore since 2020… according to **city assessment data**"*; *"about 29% of the city's commercial properties — **4,085 out of 14,027** — saw their **assessed values** slashed on average by **28.7%**"*; Downtown **−$496.3M**, Inner Harbor **−$363.4M**, Downtown West **−$214.6M** = **>$1.07B**; out-of-cycle reassessments vs Maryland's standard 3-year review ✓. ⚠️ Article is paywalled past the lede; figures verified via search-index excerpts of the Sun's own text + the visible lede, **not** a full-text read. |
| **L2** | Is the object a BANK exposure at all? | The claim's own perimeter | **BANK** = MTB loan/collateral exposure. ⛔ **MUNICIPAL** = assessed-value reassessment → **the claim is TRUE AND IRRELEVANT to my thesis**; say so plainly and stop | ⛔ **MUNICIPAL. The stop rule fires: TRUE AND IRRELEVANT.** The measured object is **assessed value for property-tax purposes** (Maryland SDAT / city assessment data) on a 3-year statutory cycle. The Sun's own headline names the subject — ***"$1B commercial crash, residential spike reshape Baltimore TAX BURDEN"*** — and its thesis is a burden **shift onto homeowners**, not a credit event. **No bank, lender, loan or mortgage appears anywhere in the piece**; MTB is never mentioned. An assessment cut is a municipal revenue fact; it is not a charge-off, not a nonaccrual, not an LTV migration, and it does not touch MTB's book. |
| **L3** | What drives the MI3 reversal? | FFIEC RC-C item 4 → item 9.a per-quarter; MTB 10-Q (CIK **0000036270**) | **ORIGINATION** = item 4 and 9.a both grow · **MIGRATION** = 9.a grows while 4 falls (the mechanism this desk discovered) · **M&A** = a named acquisition dates the step | ✅ **ORIGINATION — and by a margin that is not close.** Across the inversion window 6/30/2025 → 6/30/2026, **BOTH parents grow**: item 4 (C&I) $32.75B → **$34.22B (+4.51%)**, item 9.a (NDFI) $10.80B → **$13.65B (+26.46%)**, total loans $136.06B → **$143.22B (+5.26%)**. No quarter in the window shows the migration signature on a YoY basis. *(One single quarter, Q3-2025, has item 4 −2.1% against item 9.a +9.9% — a QoQ migration shape that does **not** survive into the annual comparison.)* ★ **The sharper read, and it cuts AGAINST a row: MI3 grew +15.70%, SLOWER than the +26.46% of item 9.a, the very parent it sits in — so MI3 is gaining dollars while LOSING share of its own bucket. That is the inverse of the relabelling signature.** Answered off `workbook/MI3_COHORT.tsv` (already-captured `item4_k`/`item9a_k`); **no new pull and no 10-Q needed** — the ledger carried L3's inputs. |
| **L4** | Does the step-detector fire on MTB? | `scripts/mi3_cohort_screen.py` step_flag column | Already computed — **read it, do not re-derive**; a flagged step is a reporting/classification change, not growth | ✅ **DOES NOT FIRE — `step_flag` is empty on all 12 MTB quarters** (9/30/2023 → 6/30/2026). Read, not re-derived, as instructed. So the book move is **not** a reporting/classification step. ⚠️ Note the direction of this result: a clean step_flag **removes** an innocent explanation as well as a guilty one — it says the move is real balances, which is what makes L3 the deciding leg rather than this one. |
| **L5** | **Does MTB earn a Matrix row?** (the registered open question) | Above + `BANK_EXPOSURE_MATRIX.md` method | **YES** only if L3 = MIGRATION **or** (L1 REPRODUCES **and** L2 = BANK). **NO** if the book grows by origination/M&A with clean credit — *large is not stressed* | ⛔ **NO ROW.** Graded strictly against the pre-registered condition: L3 = **ORIGINATION** (not MIGRATION) ✗ · L1 REPRODUCES ✓ **but** L2 = **MUNICIPAL** (not BANK) ✗ ⇒ **neither disjunct is satisfied.** Credit is the counterweight the frame demanded be quoted and it holds: MTB graded **GENUINE** on NCO at the 6/8 decomposition (0.34%→0.31%, reserve **BUILD +$35M**). **Large is not stressed.** ⚠️ **The `CRE ACL −31% vs loans −10% "optimistic into the wall" flag from 6/8 is NOT retired by this** — it was never a hidden-CRE claim and this frame did not test it; it stays where it is. **The registered open question from the 8/13 report is now CLOSED: MTB does not earn a Matrix row on this evidence.** |

---

## 4. The discriminator I must not skip

**Every instrument built on 8/20 needed a SECOND instrument to tell two opposite stories apart** (de-risking vs deterioration; cure vs charge-off; disposition vs release). **A level scores a state; only the series says which direction produced it.** Here the second instrument is **L3's item-4 → item-9.a split**: absolute book size alone cannot distinguish a bank originating more CRE-purpose C&I from a bank relabelling existing exposure into it.

⚠️ **MTB's own credit line is the counterweight and it must be quoted, not omitted:** the 6/8 cohort decomposition graded MTB **GENUINE** on NCO (0.34%→0.31%, reserve **build** +$35M) — with one flag: **CRE ACL −31% against loans −10%, "optimistic into the wall."** If L3 comes back ORIGINATION and credit is still clean, **the honest answer is NO ROW**, and I should expect to write that.

---

## 5. Budget and stop rule

**~45-60 min.** ⛔ **Stop at L2 if the object is municipal** — that is a complete answer and the cheapest possible one. ⛔ **Do not weight the Sun figure before L1 returns**; it has been carried unverified for 4 months, which is exactly how an aggregator figure hardens into a "precise" claim.

## 6. Post-hoc notes on the frame itself — filled 2026-09-02 (2nd session)

### 6.1 ⛔ THE FINDING THAT OUTRANKS THE GRADE: the decisive leg needed no primary work, and never did.

**L2 — the leg that killed the claim — is answerable from `SIG-W-20260426-009` itself.** That packet has been on disk since April. Its own Signal section says **"assessed values"** four separate times, dates the data to *"Maryland state commercial property assessment data,"* and names the named-property figures as *"assessed value."* Its own Caveats and its BROCK relevance block go further and state the perimeter outright: ***"Out-of-cycle reassessments are a property-tax-base signal that affects municipal-bond mark-to-market more than CMBS."***

⇒ **The row sat for four months labelled *"unverified at primary"* when what it actually needed was a re-read of the packet already in the repo.** The primary pull (L1) confirmed exactly what the packet had said all along; it added provenance, not perimeter.

**Why it survived four months, and this is the transferable part:** the carried ROADMAP row held the **headline** — *"−$1B / 29% of reassessed CRE in Baltimore"* — and **a headline drops the qualifier that does the work.** *"CRE value erased"* reads as a bank-collateral fact. *"**Assessed** values slashed"* is a tax fact. **The summary and the body disagreed about the object, and only the summary travelled.** `[[finding_summary_section_merges_what_the_body_separates]]` · `[[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]]`

⛔ **The rule this earns: *"unverified at primary"* describes where a claim's evidence came from. It never says the claim is undecidable.** Before scheduling a verification session, ask the cheaper question first — **can this be decided from material I already hold?** Four months of carry and a booked session went to a question the source packet had answered in its own second paragraph.

### 6.2 A threshold WAS mis-specified — and it was mine, in §1(b), not in the leg table.

§1(b) presents the MI3 trajectory as *"INVERTED monotonically over five quarters — from double-digit contraction to double-digit growth"* and treats that as the thing needing explanation. **It priced the window but not the window's start.** `6/30/2025 = $4.276B` is **the minimum of the entire 12-quarter series** — so the alarming `+15.7% YoY` is a change measured off the series low, which is the one anchor that guarantees a large positive number.

**Priced against the series start instead: $6.240B [9/30/2023] → $4.947B [6/30/2026] = −20.7%.** MTB's MI3 book is still **a fifth smaller than when the series opens**; the "inversion" is a book that stopped shrinking. Both statements are true, and the frame carried only the one that motivates a session. `[[finding_window_start_at_an_extremum_inverts_the_move]]`

⚠️ **Graded against the frame as written anyway, per its own rule** — this note does not change any RESULT. But it would have lowered the frame's own priority had it been written on 9/2 morning, and **the frame was authored by the desk that then graded it**, which is exactly the case where a window-start check is not optional.

### 6.3 Did a leg go unexercised because another decided first? — No, and the conjunctive-spec worry does not land here.

The frame's §5 stop rule (*"stop at L2 if municipal"*) would have ended the session after two legs. **All five ran anyway**, for reasons worth recording:
- **L1** was run *after* L2 was already decided, deliberately — the stop-rule branch asserts the claim is *"TRUE and irrelevant,"* and **I am not entitled to the word TRUE without checking.** Irrelevant-and-unverified and irrelevant-and-verified are different dispositions to leave behind.
- **L3 and L4 were free.** Both were answerable from `workbook/MI3_COHORT.tsv` — `item4_k`/`item9a_k`/`step_flag` were already captured columns. ⚠️ **The frame named MTB's 10-Q and CIK 0000036270 for L3 and neither was needed**, which is a small credit to the 8/13 instrument: it had already banked the discriminator.

★ **On the frame's own sharp question — *"a conjunctive spec whose decisive leg always fires reads exactly like one that works"*: L5 is a DISJUNCTION, and BOTH disjuncts failed INDEPENDENTLY.** L3 returned ORIGINATION on evidence with no reference to the Sun claim; L2 returned MUNICIPAL on evidence with no reference to the MI3 series. **Two unrelated instruments, two independent failures, same verdict.** That is the shape a spec has when it is genuinely exercised rather than decided by one dominant leg — so the NO ROW is better supported than a single-leg stop would have been.

### 6.4 Basis check — does this grade depend on anything the 8/28 v1a redefinition disturbs? **No.**

Every load-bearing figure here is **absolute dollars** (`mi3_k`, `item4_k`, `item9a_k`), which are measured, not derived, and are **untouched by the denominator ruling.** The `$4.95B largest-in-cohort by 1.94×` claim is a **dollar** rank, re-verified directly at the ledger this session (MTB $4.947B · WAL $2.555B · HBAN $2.207B · CFG $2.136B) — **not** a ratio rank, so `MEMORY` 6i's `DO-NOT-CITE-until-11/07` flag on *ratio* ranks does not reach it. ⚠️ **Naming the distinction because the flag is easy to over-apply**: it exists because each name's ratio recomputes by its own unknown 9.b, and dollars have no such dependency.

**Recorded, NOT applied:** under the ruled v1a (÷ item 4 + item 9.a, dropping 9.b), MTB 6/30/2026 recomputes **9.69% → 10.33% (+64bp)**. ⛔ **Do not write this into the ledger** — the redefinition lands with the whole cohort at the **2026-11-07** run (MEMORY 6i); applying it to one name mid-cycle is precisely the non-comparable-basis defect the re-run existed to fix.
