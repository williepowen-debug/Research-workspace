# FERT — L398 source disposition + G5 status + inbox drain
**Date:** 2026-09-22 (wall clock 16:55 Tue, boot.py) · **Session:** WQ-184 L0 due-row Tier-1 spawn by PROME · **DOCKET:** L398 (due 9/22) · **GATES:** GATE-FERT-G5 review 9/23

## 1. L398 — done-condition and verdict
Done-condition (DOCKET L398, verbatim): *"FERT names a reachable NOLA $/st source and a T12 second source — or records that it is running both watches on a single named source and states what that costs."*

**Verdict: DISCHARGED, with a stated cost on the NOLA leg.** Both watches now have a reachable, named, dated source other than the dead Advanced Turf PDF. The NOLA replacement gives urea **direction** weekly, not a free **$/st level**.

| Watch | Named source | URL (tested 2026-09-22 ~16:5x ET, curl + browser UA) | Result | Cadence | Basis | Authority | Free depth |
|---|---|---|---|---|---|---|---|
| **NOLA $/st (T5)** | Green Markets (Bloomberg) — Nitrogen Posts | `https://fertilizerpricing.com/nitrogen-posts/` | **HTTP 200, 40,660 B** | weekly, Fri-dated (latest 9/18/26) | NOLA barge US Gulf, $/st | PRIMARY headline · MIRROR-WALLED level | 9/18 urea: *"NOLA urea prices ratcheted up again this week"* — **direction only**. 9/18 UAN: *"$350–$362/st ($10.94–$11.31/unit)"* — **level quoted**. Urea post body `/urea-542/`: *"restricted to site members"* |
| NOLA phosphate (context) | Green Markets — Phosphate Posts | `https://fertilizerpricing.com/phosphate-posts/` | HTTP 200, 41,299 B | weekly | **Central Florida** DAP/MAP $/st (NOT NOLA) | PRIMARY headline | 9/18: *"Central Florida phosphate prices were unchanged at $840/st"* |
| **T12 second source (sulfur)** | Green Markets — Sulfur Posts | `https://fertilizerpricing.com/sulfur-posts/` | **HTTP 200, 38,783 B** | weekly | Tampa molten sulfur contract, **$/long ton CFR** | PRIMARY headline | 9/18: *"The Tampa molten sulfur contract continued at $705/lt CFR"* |
| T12 corroboration | Fertilizer Daily | `https://www.fertilizerdaily.com/20260715-tampa-sulfur-price-record/` | HTTP 200 | article (7/15/26) | Q3 Tampa $705/lt delivered, +$50 from $655 | MIRROR | also: Mosaic cut output at four US plants (July) |

**Tested and NOT usable:**
| Candidate | Result | Why it matters |
|---|---|---|
| Advanced Turf PDF 9/14, 9/21 editions | 404 (84 KB error page) | now **10 dated 404s** 8/17→9/21; 8/10 control still **200 / 190,176 B**; `wp-json` media index **403**. Retired as the instrument |
| CME urea FOB US Gulf futures settlements (the $/st futures on the NOLA basis) | CME **403** · Barchart page **202-empty**, API **403** · Yahoo chart API **429** | the only continuous $/st level series is **unreachable from this box** — Will can see it; an LLM session cannot |
| USDA AMS Illinois Production Cost Report (`ams.usda.gov/mnreports/ams_3195.pdf`) | **200**, bi-weekly, wk ending 9/18/26 | **Illinois distributor $/ton F.O.B.** — a retail-class series, **not NOLA**. Possible independent cross-check for G5 later; column mapping from pdfminer is ambiguous, so **no values cited** |
| hmndp.org fertilizer tracker | 200 | **rejected** — unsourced aggregator attributing NOLA $/st ranges to "USDA AMS weekly" reports I cannot locate |
| Fertilizer Daily NOLA coverage | 200 | **episodic only** (6/24 article, *"USD 350 per tonne"* — unit ambiguous, sourced to The Western Producer) |

**What it costs to run NOLA at direction depth (the cost L398 asks me to state):**
1. **No NOLA urea $/st level cell** can be refreshed; the 8/7 $385–410/st print is history. STATUS carries a direction cell instead.
2. **Any NOLA $/st threshold can't be graded from this box.** The assessment's §5B candidate *"NOLA barge >$550/st FOB"* stays unregistered for this reason as well as its own.
3. The NOLA→retail lead (international leads retail by weeks) is now read **by direction only**. The 9/18 headline says NOLA urea rose "again". DTN retail urea rose +$3 on 9/16. Those agree in sign; the size of either move can't be compared.
4. Mitigation: the weekly headline sometimes quotes a level (UAN did on 9/18). Record it when it appears, dated, and never infer it when it doesn't.

## 2. DTN 9/16 — first-party pull (closes the "first-party pull owed" item)
`curl` of `dtnpf.com/.../2026/09/16/fertilizer-prices-continue-lower-6-8` → **HTTP 200, 182,061 B**. On 9/17 the fetch tool failed on this page; the site itself is fine. US national average, $/ton, data week Sep 7–11 2026:

| DAP | MAP | Potash | Urea | 10-34-0 | Anhydrous | UAN28 | UAN32 |
|---|---|---|---|---|---|---|---|
| $923 | $962 | $494 | $658 | $717 | $938 | $430 | $457 |

- DAP and MAP **match DAEDALUS's MIRROR read exactly**, so the 9/16 G5 grade now rests on first-party authority. `KB-FERT-040`
- **Composition:** DTN's headline, *"continue lower for 6 of 8"*, compares against **a month ago**. Against the 9/9 cells, the week was flat or up on every product (urea +3, UAN28 +7, UAN32 +2, potash +1, anhydrous 0, 10-34-0 0, DAP +4, MAP +3). The headline and the week point opposite ways. One print; not scored.

## 3. GATE-FERT-G5 — review 9/23
- **Can't be graded today on its letter.** The review print is the 2026-09-23 DTN weekly, which publishes 9/23 around 03:50 CDT.
- **Current state:** NOT FIRED 5-of-5. MAP $962 (binding leg, $38 / +3.95% below $1,000); DAP $923 (+8.34%).
- **What grading needs:** a FERT touch on or after 9/23 ~05:00 ET. The method now works: curl the dtnpf.com article; its slug appears in a web search for "DTN retail fertilizer" once published.
- **Still owed at a full session, due 9/30:** the DAEDALUS OPERATOR-MISMATCH recomputation of the letter. The grade is unaffected.

## 4. Inbox drain
**0 items.** Top-level holds only `PROTOCOL.md` and `RECEIPT.md`; `WALTER/` is empty (`PROME/tools/inbox_census.py`: *top-level 2 · WALTER/ 0*, files only). Nothing needed a disposition or a `board_log.tsv` row. RECEIPT.md was overwritten with the zero-item run.

## 5. Files changed
`STATUS.md` · `workbook/KB.tsv` (+KB-FERT-040/041/042) · `workbook/TRIGGERS.tsv` (T5 re-pointed →9/25 · T12 consumed →10/16 · T4 method note) · `workbook/INSTRUMENT_GAPS.md` · `workbook/GATE_GRADES.md` (9/16 row) · `inbox/RECEIPT.md` · this memo.

**Not worked, not re-dated:** T1 (RCF award), T3 (Aug CPI food-at-home), T8 (NASS). They were outside this spawn's scope, and re-dating a row without working it is a false all-clear. FLOW.tsv is 32 days stale and not refreshed; it is outside scope.
