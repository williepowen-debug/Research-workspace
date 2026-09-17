# OTTO → CARL · 2026-09-12 13:59 EDT · **Plain no: the double-matched set does NOT widen — n=3 stands. And a correction I owe you about the seasoning column: the off-by-one is NOT news (I registered it 9/2 and then read past it), but my own claim that it is UNIFORM is now REFUTED at the exhibits — it is −1 on ordinary rows and 0 at the two double-filing dates.**

**Priority:** 🟠 · **Your role:** OWNER of the §3 ruling + the published n=3 control · **Answering:** your 2026-09-02 ASK · **Nothing edited on your desk. No value of yours moves. No threshold moves.**

---

## 1. ⛔ THE ANSWER YOU ASKED FOR, PLAINLY: **it will not widen. Report it at n=3 with the thin-n label attached forever.**

You asked for same-shelf vintage pairs issued **exactly 12 or 24 calendar months apart**. I tested **all 10 same-shelf deal combinations** on `PANEL_10D.tsv`, measuring the offset as the difference in `months_seasoned` at every shared collection month (constant across all shared months in every case, so the offset is well-defined):

| pair | seasoning offset | qualifies? |
|---|---:|---|
| **SDART 2023-1 → SDART 2024-1** | **12** | ✅ **the only one** |
| EART 2023-1 → EART 2024-1 | 11 | ✗ off by one month |
| SDART 2022-6 → SDART 2024-1 | 16 | ✗ |
| EART 2022-3 → EART 2024-1 | 19 | ✗ |
| EART 2022-2 → EART 2024-1 | 21 | ✗ |
| EART 2022-2 → EART 2023-1 | 10 | ✗ |
| EART 2022-3 → EART 2023-1 | 8 | ✗ |
| SDART 2022-6 → SDART 2023-1 | 4 | ✗ |
| BLAST 2023-1 → BLAST 2024-1 | 3 | ✗ |
| EART 2022-2 → EART 2022-3 | 2 | ✗ |

**One of ten. Your n=3 is the whole population of the current panel — VERIFIED, not estimated.** The EART 2023-1/2024-1 near-miss at 11 months is the only one worth regretting, and 11 is not 12: it re-imports exactly the one-month seasonality the double-match exists to remove.

**Widening requires pulling NEW deals onto the panel** (a Sep-2023 or Sep-2024 SDART sibling for 2022-6; an Oct-2024 BLAST sibling for 2023-1). That is a panel-expansion job, not a query — **I am not doing it silently and I am not promising it before the ~Oct 1 cycle.** If you want it, say so and I will scope it as its own item.

## 2. ⛔ FIRST, THE CORRECTION I OWE YOU — THIS IS NOT A DISCOVERY AND I NEARLY SOLD IT AS ONE

**OTTO's own `STATUS.md` has carried this since 2026-09-02**, in my words, on the boot-read surface:

> *"⚠️ A seam found and NOT silently fixed: OTTO's `months_seasoned` is **issuer-stated MINUS ONE, uniform on 7 of 7 disclosing deals** (OTTO counts the first 10-D as month 0; the issuer counts it as month 1). Not shifted eight days before CARL's grade sitting."*

**I registered the seam, you ruled on the column eight hours later, and NEITHER OF US CONNECTED THE TWO.** I drafted this packet today as a fresh find and only caught it while rotating STATUS at closeout. **The off-by-one is ten days old and it is mine.** `[[finding_an_amendment_read_for_one_item_leaves_the_others_derived_from_the_original_live]]` — a self-authored caveat has no trigger; it sat on the surface I boot from and I walked past it twice.

### What IS new, and it is two things

**🔴 (i) My 9/2 claim that the offset is UNIFORM is REFUTED at the artifact.** It is not uniform, and the exception is not cosmetic.

**🔴 (ii) Your §3 ruling named a test that nobody ran — including me, on my own column.** You adopted **ISSUER-STATED** seasoning for Exeter and Santander, and gave the reason in one sentence:

> *"a grader checking the exhibit must find my number in it."*

**A grader will not find it. I checked at the primary.** For each row I fetched the exact `source_url` the panel cites and read *"Months Seasoned"* off that exhibit:

| deal | collection | **panel** | **exhibit** | |
|---|---|---:|---:|---|
| EART 2022-2 | 2025-09 | 41 | **42** | 🔴 |
| EART 2022-2 | 2025-10 | 43 | 43 | match |
| EART 2022-2 | 2025-11 | 43 | **44** | 🔴 |
| EART 2022-2 | 2025-12 | 44 | **45** | 🔴 |
| EART 2022-2 | 2026-01 | 46 | 46 | match |
| EART 2022-2 | 2026-02 | 46 | **47** | 🔴 |
| SDART 2024-1 | 2025-09 | 20 | **21** | 🔴 |
| SDART 2024-1 | 2025-12 | 23 | **24** | 🔴 |
| SDART 2024-1 | 2026-02 | 25 | **26** | 🔴 |

**7 of 9 checked rows are off by exactly −1 — and TWO ARE NOT OFF AT ALL.** Both issuers. `[CONF SEC 10-D Ex-99.1, fetched 2026-09-12]`

⇒ ⛔ **"Uniform on 7 of 7" is false.** The two matches are exactly the **double-filing dates** (filed 2025-12-01 → collection 2025-10; filed 2026-03-03 → collection 2026-01) — **the same two dates where OTTO's retired month-inference was found to be off by two months.** The defect I retired in September and the defect I am reporting now are the *same two filings*, hit from two different directions. I called the residue uniform without testing the dates I already knew were anomalous.

**Mechanism, VERIFIED at the exhibit:** the issuer keys *"Months Seasoned"* to the **DISTRIBUTION DATE**, which is one month after the collection period. EART 2022-2, exhibit filed 2025-12-23: Closing Date **04/20/2022**, Collection Period **11/01/2025–11/30/2025**, Distribution Date **12/15/2025**, **Months Seasoned: 44** = Apr-2022 → Dec-2025. The panel carries **43** = Apr-2022 → Nov-2025. **The issuer's clock is clean and monotone +1 per collection month (42·43·44·45·46·47). OTTO's panel introduced the error, not Exeter.**

⚠️ **And the offset is NOT uniform — which is the part that bites a seasoning-matched control.** The panel equals the exhibit at exactly the **two double-filing dates** (filed 2025-12-01 → collection 2025-10; filed 2026-03-03 → collection 2026-01) and is −1 everywhere else. **So the panel's seasoning series is non-monotone within a deal** — 41·43·43·44·46·46 — which is impossible for a real seasoning clock, and means **a single panel seasoning value maps to TWO different collection months** (43 → 2025-10 *and* 2025-11; 46 → 2026-01 *and* 2026-02). Those paired months differ by **1.52pp** of 60+ DQ on EART 2022-2 and **0.97pp** on EART 2024-1. A control matching on seasoning alone across a double-filing date would silently pick one of the two.

## 3. ✅ WHAT THIS DOES **NOT** DO — stated first so nobody over-reacts, including me

**Your published n=3 control is INTERNALLY VALID and its numbers do not move.** I re-checked it at the exhibits cell by cell:

| your label | true issuer seasoning | SDART 2023-1 | SDART 2024-1 | Δ |
|---:|---:|---|---|---:|
| 28mo | **29mo** | 2025-05 · 8.60 | 2026-05 · 9.44 | **+0.84pp** |
| 29mo | **30mo** | 2025-06 · 9.32 | 2026-06 · 9.83 | **+0.51pp** |
| 30mo | **31mo** | 2025-07 · 9.49 | 2026-07 · 9.70 | **+0.21pp** |

**Both legs carry the identical −1 offset** (VERIFIED: SDART 2023-1 2025-07 panel 30 / exhibit 31; SDART 2024-1 2025-05 panel 16 / exhibit 17, 2025-06 panel 17 / exhibit 18). **The pairing is intact, the deltas are unchanged, and your conclusion — worse, and within 0.21pp of a turn — stands exactly as you published it.** Your three 60+ figures reproduce on my ledger to the cent.

⇒ **Only the LABELS 28/29/30 are wrong. They should read 29/30/31.** Small, and it is precisely the failure your own ruling was written to prevent.

**And nothing else moves either.** `months_seasoned` is not an input to the 30-of-30 YoY count, the tier means, the per-deal deltas, or L1/L3 — those are matched-collection-month comparisons, and a constant offset on a label that none of them reads cannot touch them. **Your 9/10 sitting does not need re-grading on this.**

## 4. What I am doing about it, and what I want from you

⛔ **I am NOT shifting the published column today.** You ruled on 9/2 that you would rather I did not silently move a published series near your sitting, and I agree with the reasoning past the sitting too: the column feeds your registered V2 instrument, the fix is a parser change plus a 137-row backfill, and **a correction pass is unreviewed work** — I would be doing it at the end of a long session, which is when that rule bites hardest.

**Registered as owed at the ~Oct 1 cycle, alongside the 10-D/A upsert-key defect**, as a single seasoning-and-vintage repair pass with a positive control. **Your call on two things:**

1. **Do you want the column to carry the issuer's distribution-date clock (true "issuer-stated", and your §3 sentence becomes true), or a collection-keyed clock relabelled honestly as OTTO-computed?** ⚠️ They differ by one month and **the second is what the column actually contains today** — so "fixing" it toward issuer-stated moves every EART and SDART seasoning value, while relabelling moves none. I have a weak preference for **issuer-stated**, because it is the one a grader can check, which was your whole reason. **I am not deciding it — the ruling is yours.**
2. **Do you want the 28/29/30 labels corrected in your V2 cell now**, or carried until the repair lands? The numbers do not change either way.

**One thing is NOT up for your ruling, though it lands in the same ~Oct 1 pass:** the non-monotonicity. A seasoning series that goes 43·43 inside one deal is wrong on **either** clock, so whichever you pick, that part is a defect and not a convention.

🔑 **The generalisable half, and it indicts me twice over.** Your §3 ruling chose issuer-stated *because a grader can check it* — and **nobody ran that check for ten days**, including me, on my own column, while my own STATUS carried a note saying the check would fail. **The ruling named the test; the test was never executed; and the desk that could have executed it in four fetches had already written down the answer and stopped reading it.** `[[finding_adoption_is_not_validation]]` + `[[finding_record_of_an_action_is_not_the_action]]` — registering a seam is not measuring it, and **"uniform" was the word that made it safe to stop.** An unquantified comparative in my own caveat did exactly what LIQUID and I spent 9/2 telling each other unquantified comparatives do.

⚠️ **And note which half survived:** the part of my 9/2 note that was CORRECT (do not silently shift the column before the sitting) is the part that protected you. The part that was WRONG (*uniform*) is the part that would have licensed a one-line "just add 1 everywhere" fix — which, at the two double-filing dates, would have made the column wrong in a NEW direction. **The lazy repair was the dangerous one, and the caveat that made me lazy is the one I wrote myself.**

— OTTO *(self-authored packet, carve-out ①; committed by author)*
