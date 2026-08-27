---
name: finding_level_published_in_narrative_can_vanish_from_an_edition
description: "A threshold keyed to a figure that lives in a report's NARRATIVE or a CHART — rather than a standing table cell — can become unquotable in an arbitrary period, because the publisher may simply not print that figure that time. The defect presents as 'the registered number is wrong/unreproducible', which sends you hunting for a transcription error that does not exist. Worse: the obvious fix (re-point the row at the source document) RECREATES the original defect, since the named source does not contain the value either. And a conjunctive spec hides all of it — the trigger grades correctly by luck whenever another leg is decisive."
metadata: 
  node_type: memory
  symptoms: "registered threshold value not found in the source document; grep the PDF and the number is not there; zero occurrences of the level anywhere; cannot reproduce the band's own figure; source_of_truth points at a report that lacks the cell; the chart number does not exist in this edition; trigger graded fine but the level leg was never checked; two independent claims in one row fail together"
  type: finding
  originSessionId: 758cd0a0-6a17-45b2-9f18-b56f71d1fe00
  modified: 2026-08-27T19:34:34.337Z
---

**Worked case (CREED ↔ REGINALD, 2026-08-27).** `CREED-T-03` — the desk's *most decision-relevant* trigger — registered as `FDIC-NONOWNER-CRE-PDNA-LARGEBANK > 3.40`, sourced to *"FDIC Q1 2026 QBP."* That document's `>$250B` nonfarm-nonresidential cell reads **2.73%**. Not 3.40, at any vintage: the combined series prints Q3-25 3.20 / Q4-25 3.23 / Q1-26 2.73 / Q2-26 2.48.

**The tell that it was a PERIMETER error and not a typo:** the row made *two* independent claims — the level (3.40) and *"improved 6 straight quarters"* — and **both failed together** on the same basis (Q4-25 is a **+3bp rise**). One wrong number is a transcription slip. Two unrelated claims failing on one basis is a **wrong parent series**.

**Resolution.** The FDIC publishes *two* different CRE PDNA objects:
- **(i) non-owner-occupied-SPECIFIC, `>$250B`** — the worse-credit subset, ~67bp above the combined cut. Q3-24 peak **4.99**, Q4-25 **4.06** (*"fifth consecutive quarter"* of decline).
- **(ii) COMBINED nonfarm-nonresidential** — a standing table cell.

The level came from **(i)**; the grading was being done against **(ii)**. The parent was identified when the consuming desk found the FDIC's own sentence in a five-month-old analyst note — and it was **decisive because it contained `4.99` verbatim**, one of the two disputed figures. *Identify a parent series by finding one of its disputed numbers inside it, not by plausibility.*

## The load-bearing part: (i) lives in a CHART + one narrative sentence

Not in a table. Consequences, in order of how badly each bites:

1. **A full-text grep returns ZERO** and reads as "the number was invented." It wasn't.
2. **An edition can omit the series ENTIRELY.** The Q1-2026 QBP has **eight charts** — there is no Chart 11, the number appears nowhere, and the only non-owner mention is qualitative and numberless. *A chart can hide a number from a text extractor; a chart that does not exist cannot.* So this is **absence, not an extraction artifact**.
3. **The chart NUMBER is edition-specific.** "Chart 11" is an address in one edition and meaningless in the next. Never register a level's location as a chart number.
4. ⇒ **The level leg is gradeable in some periods and not others, and nothing announces which.**

## ⛔ The obvious fix recreates the defect

The natural repair — *"name the true source and re-point the row"* — is a `source_of_truth` correction, executable in the owner lane without a band ruling. **It was wrong.** Re-pointing at the Q1-2026 QBP would have named a source **that does not contain the value**, which *is* the original defect, rebuilt by its own remedy.

**It died only because the owner EXECUTED the fix and looked at the result** rather than reasoning about whether it would work. Same desk, same day, second instance of that shape.
→ related: `finding_a_fix_can_relocate_a_constraint_and_report_it_removed`, `finding_verify_recommended_fix_not_just_finding`

## Why nobody noticed for months: a conjunctive spec hides a dead leg

`T-03` is three conjunctive legs. It graded **NOT FIRED** correctly on 2026-08-27 — but **only because reserve coverage (166.8% → 172.7%, improved) is basis-independent and decisive on its own.** Had coverage deteriorated and direction turned, the owner would have had to fire, or refuse to fire, **on a level it could not source.**

> **A trigger that grades by luck reads exactly like one that works.**

**In an AND-spec, a decisive leg means the other legs are never exercised.** Their defects are invisible for as long as the decisive leg keeps deciding. This is the conjunctive twin of `finding_registered_gate_captures_attention`.

## What to do

- **Registering a level: ask where the number physically lives** — a standing table cell that prints every period, or narrative/chart prose that may not? If the latter, it is a **weak instrument regardless of how good the number is**, and that belongs on the row.
- **Cannot reproduce a registered level at its named source?** Check whether the row makes a *second* claim (a count, a direction, a streak). If both fail on the same basis, stop hunting for a typo — **you have the wrong parent series.**
- **Before re-pointing a `source_of_truth`, open the target and confirm the value is in it.** A pointer fix is only cheap when the pointer lands.
- **Re-basing onto the reproducible standing series is the honest road** when the parent is episodic — and it is a *band* decision (operator-gated), not an owner-lane pointer fix. **Never move a band to fit the number you can currently see; that silently re-positions the trigger.**
- **Periodically exercise the non-decisive legs of a conjunctive spec on their own**, or you are not testing them.
- ⚠️ **Consuming desks: a level with no reference is not a signal, and a level whose parent you cannot name is not one either.** Both ends here behaved correctly and the defect still propagated — see `finding_inherited_defect_propagates_though_both_ends_act_correctly`.

Related: `finding_banded_threshold_with_no_metric_surface_is_untrippable` (metric absent from any *internal* surface — this is its *external-publication* sibling) · `finding_registry_names_a_concept_tool_resolves_an_instrument` · `finding_unnamed_instrument_makes_a_threshold_a_family` · `finding_impeachment_must_be_scoped_to_the_claim_not_the_source` (the level and count died; the counter-direction substance survived on the reproducible series)
