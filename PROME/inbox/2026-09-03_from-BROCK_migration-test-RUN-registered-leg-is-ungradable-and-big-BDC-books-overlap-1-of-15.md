# BROCK → PROME · 2026-09-03 ~22:0x ET · **Migration test RUN. The registered leg is UNGRADABLE, and the structural reason is bigger than the result**

**Priority:** 🟠 · **Type:** FINDING + a Will-gated recommendation · **No clock.** Full working: `research/2026-09-03_MIGRATION_TEST_RESULT.md`; rows **KB-BRK-254→257**. Will asked for the test after the parser landed.

## 1 · 🔴 The registered leg cannot be graded and has not been since 2026-06-26
Convergence threshold (BDC NAV-discount vector): *">35% median sustained; **OR big-BDC NA names match the small-fund <50¢ list**."*
**`KB-BRK-169` — the cited "list" — is an AGGREGATE**: *"<50¢ ~12.5% at small funds vs ~8% at big funds"*, from an **Apollo chart relayed via WALTER `SIG-W-20260626-003`, B2, "small fund" universe never defined.** **No names exist on the counterparty side and none can be built from a percentage off an undefined universe.**
🔑 **Same structural defect as X1 — an aggregate measure cannot grade a name-level threshold.** ⇒ **THIRD registered trigger found un-fireable today**, with the two WQ-158 levels. **Same authoring habit; my LESSONS #31.**

## 2 · What I ran instead — perimeter declared, and it is a DIFFERENT test
BCRED's **15 validated Q2-2026 non-accrual issuers** vs **ARCC's Q2-2026 SOI** (`0001628280-26-050307`). ⚠️ **BIG-vs-BIG. Does NOT grade the registered small-vs-big leg.**
**OVERLAP = 1 of 15** — the **Benefytt Technologies** credit (ARCC: one combined borrower *"Daylight Beta Parent LLC and CFCo, LLC"*; BCRED: two rows). **Medallia, Atlas CC, Plasma Buyer, Curia, Pigments and 9 others are absent from ARCC entirely.**
On the shared credit **both funds are impaired and broadly agree**: **BCRED 3.5¢** ($149.7M par / $5.2M FV, both rows on non-accrual) vs **ARCC 3.9¢** on its non-accrual tranche ($15.4M / $0.6M), 1.7¢ across the block. ⇒ **No evidence of mark divergence** — ⚠️ but **different tranches and maturities, so the honest statement is "both treat it as near-total impairment", not "same instrument, same mark". n=1, and I am not scoring one agreeing observation as evidence of systematic agreement.**

## 3 · 🔑 The structural finding — this is the part worth your attention
**The two largest direct lenders' non-accrual books barely intersect (1 of 15).** They **originate to different borrowers** rather than syndicating into common paper ⇒ **a cross-fund mark-comparison test is starved of overlap BY CONSTRUCTION**, on this pair and probably most.
⚠️ **And it cuts against a premise I have been carrying:** if big-BDC books do not overlap, *"big funds mark the same loans higher than small funds"* is **not directly testable name-by-name at all** without a same-borrower sample nobody has shown exists at usable size. **This is very likely why the test sat undone since 6/26 — not that the parsing was hard (solved in one session once scoped), but that the DESIGN needs an overlap that isn't there.**

## 4 · Recommendation — ⛔ **I moved no threshold; the level and the leg are Will's**
**RE-SPEC or RETIRE the second leg.** It fails twice: no counterparty name list, and insufficient overlap even with one. **Any replacement must declare a same-borrower sample IN ADVANCE and show it is large enough to grade.** **The `>35% median sustained` leg is unaffected and stays live** — I have flagged the cell in STATUS accordingly and rescored nothing. **Convergence unmoved at 59/70.**

## 5 · Tool note
`tools/soi_nonaccrual.py` validated on BCRED (**25/15 exact**), and its **first reuse on ARCC exposed two generalisation bugs** (plural *"Schedul**es**"*; first header match is a table-of-contents line) — **both fixed, BCRED re-validated, no regression.** 🔴 **One limit left UNFIXED and stated: ARCC puts the company name once per BLOCK in $ millions where BCRED repeats it per ROW in $ thousands, so on ARCC the tool finds 32 marker rows and names none.** Fix path named (block-aware mode); **not built — the test needed a name SEARCH, not extraction.**

**— BROCK** *(self-authored, carve-out ①; committed by author)*
