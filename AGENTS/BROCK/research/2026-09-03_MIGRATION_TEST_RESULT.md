# SIZE-BIFURCATION MIGRATION TEST — RUN 2026-09-03. **The registered test is NOT RUNNABLE; a substitute was run and labelled**

## 1 · 🔴 THE REGISTERED TEST CANNOT BE GRADED, AND HAS NOT BEEN SINCE 2026-06-26
**Registered form** (`STATUS.md` convergence matrix, BDC NAV discount vector): *">35% median sustained; **OR big-BDC NA names match the small-fund <50¢ list**."*
**The counterparty side does not exist.** `KB-BRK-169` — the cited "small-fund <50¢ list" — is an **AGGREGATE, not a list**: *"loans marked <50¢ ~12.5% at SMALL private-credit funds vs ~8% at BIG funds."* Source: **an Apollo chart relayed via WALTER (`SIG-W-20260626-003`), confidence B2, and the "small fund" universe is never defined.**
⇒ **There are no names on the small-fund side, and none can be constructed from that source** — a percentage off an undefined universe cannot be resolved into constituents. **The leg is ungradable by construction and has been for ~10 weeks, sitting on the board looking merely un-fired.**
🔑 **Same structural defect as X1: an ABSOLUTE/aggregate measure cannot grade a RELATIVE/name-level threshold.** `[[finding_relative_threshold_cannot_be_graded_by_a_one_sided_instrument]]` · `[[finding_banded_threshold_with_no_metric_surface_is_untrippable]]`
⛔ **This is the third registered trigger found un-fireable today** (with the two WQ-158 levels). **Same authoring habit — LESSONS #31.**

## 2 · The substitute I ran instead — **perimeter DECLARED, and it is a DIFFERENT test**
**BCRED's 15 Q2-2026 non-accrual issuers** (`research/2026-09-03_BCRED_Q2_NONACCRUAL_NAMES.md`, validated 25/15 exact) searched against **ARCC's Q2-2026 Consolidated Schedules of Investments** (acc `0001628280-26-050307`, current-period segment only).
⚠️ **This is BIG-vs-BIG. It is NOT the registered small-vs-big test and does not grade it.**

## 3 · Result — **overlap is 1 of 15**
| | |
|---|---|
| BCRED NA issuers found in ARCC's SOI | **1 of 15** |
| The shared credit | **Benefytt Technologies** — ARCC lists it as one combined borrower *"Daylight Beta Parent LLC and CFCo, LLC"*; BCRED splits the same credit across two rows |
| Absent from ARCC entirely | Atlas CC · Cast & Crew · ES Group · AEC Parent · Hoya Midco · Curia Global · Material Holdings · **Medallia** · Mitnick · Newfold Digital · Paramount Global Surfaces · Pigments Services · Plasma Buyer · WHCG Purchaser |

**On the one shared credit — both funds are impaired and they broadly AGREE:**
| | par | cost | fair value | FV/par | non-accrual? |
|---|---:|---:|---:|---:|---|
| **BCRED** (2 rows) | $149.7M | $62.1M | $5.2M | **3.5¢** | ✅ both rows |
| **ARCC** NA tranche (09/2033) | $15.4M | $12.0M | $0.6M | **3.9¢** | ✅ footnote (8) |
| **ARCC** whole block (+09/2038 + Class B units) | $36.2M | $12.5M | $0.6M | 1.7¢ | second loan carries no (8) |

⇒ **NO EVIDENCE OF MARK DIVERGENCE.** Both mark it in the **low single digits of par**, both have a tranche on non-accrual. ⚠️ **They are not identical instruments** (different maturities/tranches), so this is *"both funds treat this credit as near-total impairment,"* **not** *"the same instrument at the same mark."* ⛔ **n=1. One agreeing observation is not evidence of systematic agreement, and I am not scoring it as one.**

## 4 · 🔑 THE STRUCTURAL FINDING, which matters more than the result
**The two largest direct lenders' non-accrual books barely intersect — 1 of 15.** BCRED's distressed names are almost entirely credits ARCC does not hold.
⇒ **A cross-fund mark-comparison test on non-accruals is STARVED OF OVERLAP BY CONSTRUCTION on this pair**, and will be on most pairs: these funds originate to different borrowers rather than syndicating into the same paper. **That is very likely why this test has sat undone since 6/26 — not because the parsing was hard, but because the design needs an overlap that does not exist.**
⚠️ **It also cuts against a premise I have carried:** if big-BDC books do not overlap, then "big funds mark the same loans higher than small funds" is **not directly testable name-by-name** at all — it needs a same-borrower sample that nobody has shown me exists.

## 5 · Recommendation — ⛔ **and I move no threshold; that is Will's**
**RE-SPEC or RETIRE the second leg of the BDC NAV-discount vector's next-level threshold.** It fails twice over: no name list exists on the small-fund side, and even with one, overlap is structurally too thin to grade. **A workable replacement would need a same-borrower sample declared in advance** — e.g. broadly syndicated credits held by both a large and a small fund — and I have not established that such a sample exists at usable size. **The >35% median leg is unaffected and remains the live half.**

## 6 · Tool limitation found on first reuse — recorded, not papered over
`tools/soi_nonaccrual.py` **validated on BCRED (25/15 exact) and FAILED to name-extract on ARCC.** Two generalisation bugs were fixed (ARCC writes *"Consolidated Schedul**es** of Investments"* — plural — and its first header match is a **table-of-contents line** ~126k chars before the real schedule; the tool now matches singular/plural case-insensitively and requires ≥2 schedule column-words after the header). **BCRED re-validated 25/15 after the patch — no regression.**
🔴 **What remains UNFIXED and is stated as a limit:** ARCC's SOI puts the **company name once per block** with multiple instrument rows beneath and the marker on each row, and reports **$ millions**; BCRED repeats the name on every row in **$ thousands**. **The tool's name extraction assumes the BCRED layout, so on ARCC it finds 32 marker rows and names none.** **Fix path: a block-aware mode that assigns each marker row to the nearest preceding name-block header.** **Not built today. The migration test did not need it — a name SEARCH answered the question.**
