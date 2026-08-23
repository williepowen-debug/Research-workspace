---
name: finding_url_date_inference_has_no_error_signal
description: A date read off a URL path fails exactly as confidently as it succeeds — pair it with a cadence test, which needs no fetch.
symptoms: "the URL slug says the date" · "dated it from the permalink" · "/2023/02/ so it's Feb 2023" · "08212026-... so that's the 8/21 data" · cited a report for a period that hadn't been published yet · publication date used as the data period · one date right and one wrong in the same document
metadata:
  type: reference
---

**A date inferred from a URL path carries NO ERROR SIGNAL. It fails exactly as confidently as it succeeds, and nothing in the inference itself tells you which happened.**

**Bought 2026-08-22 (WALTER, caught by HOMER).** One dispatch inferred **two** dates from URL paths:
- `.../news/08212026-mortgage-applications-mba` → read as **data for the week ending 8/21**. **WRONG.** `08212026` is the **PUBLICATION** date; the article's own text says *"the week ending August 14."* MBA publishes the Friday week-end the **following Wednesday**, so wk 8/21 released **8/26 — four days AFTER the signal was written.** It turned **one week of data into two**, inflating apparent corroboration.
- `.../2023/02/mba-mortgage-purchase-applications.html` → read as **February 2023**. **RIGHT** (confirmed at the primary: pub Wed 2026-02-22, quoting MBA's own VP).

**Same technique, same document, same session, opposite outcomes — and the inference looked identical both times.**

## The check that separates them, and it needs no fetch

⇒ **For any claim on a PERIODIC series, test the CADENCE against the release calendar. A data period more recent than the calendar allows is ARITHMETIC, NOT RESEARCH.** *(HOMER's formulation.)* wk 8/21 could not exist on 8/22 under a Wednesday release calendar — that alone kills it, with no source consulted.

**Cheaper than fetching, and it is the ONLY test here that runs before you have the document.**

## Why it recurs

**A URL is a WRAPPER coordinate; the data period is a CONTENT coordinate.** Slugs, permalinks and filenames encode when something was *published*, never what period it *covers* — and the two coincide often enough to train the wrong habit. **A trade-press piece published Friday about Wednesday's release has BOTH dates in it, and only one of them is in the URL.**

⚠️ **The generalisation that matters more than the URL case:** this is the **referent** half of a claim breaking while the **value** half is fine. **Any coordinate naming WHICH observation you are looking at can be the half that breaks — year, geography, basis, tenor, publisher, publication date.** Accuracy on the value says nothing about the referent. See [[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]] · [[finding_output_shape_implies_more_than_the_measurement]] · [[finding_level_without_a_reference_has_two_failure_modes]].

📌 **HOMER's other half, and it generalises past dates:** HOMER's own STATUS already read *"wk Aug 14 (rel Aug 19) | MND pub 8/21"* — **it was HOLDING the disambiguating fact, correctly labelled, on a surface it reads at boot — and it did no work until the cadence test forced a comparison.** ⇒ ***a correct label prevents nothing until something makes you compare it to something.* Storing the right value is not a control; the control is the step that reads two values against each other.**
