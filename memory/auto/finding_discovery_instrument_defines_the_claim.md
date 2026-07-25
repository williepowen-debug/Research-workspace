---
name: finding-discovery-instrument-defines-the-claim
description: "A forward-discovery prediction measured by press-sampling measures your own discovery latency, not the world — name the complete-scan instrument in the claim and pre-register the re-check, or the same known-unknown trap recurs (OTTO-30: Origin Bancorp 5/22, Triumph Financial 7/25, same prediction, twice)"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 53f77d69-be8e-4391-a23f-6461969b9141
  modified: 2026-07-25T16:03:14.022Z
---

A prediction of the form *"an Nth [name/case/disclosure] will surface by date X"* is only as good as **the instrument you will use to look**. If the instrument is press-monitoring or ad-hoc search, the claim silently measures **your own discovery latency**, not the world's behaviour — and it will keep producing "known-unknowns that predate the window" indefinitely.

**Why (OTTO-30, the same trap twice on one prediction).** OTTO-30: *"a 6th US bank discloses Tricolor exposure by Q2 2026"* (made 2026-04-15, resolve 2026-08-31).
- **First occurrence, 2026-05-22:** research surfaced **Origin Bancorp** ($74.7M) — but disclosed **2025-10-23**, predating the window. Logged as a known-unknown; prediction held OPEN, confidence dropped. This produced [[feedback_forward_discovery_prediction_spirit]], which correctly fixed *how to score* it.
- **Second occurrence, 2026-07-25:** a complete EDGAR full-text scan surfaced **Triumph Financial / TBK Bank** ($60.5M Tricolor floorplan facility, ~$22.5M held, unreserved) — disclosed since a **2025-09-11 8-K**, i.e. seven months before the prediction was even written, and missed by press monitoring for **over ten months**.

The scoring rule had been fixed. The trap recurred anyway, because the *instrument* was never specified. Both misses came from press-sampling a domain where the ground truth is a machine-queryable primary corpus.

**The distinction that matters:** "no new name appeared" and "my search method doesn't find names like this" are indistinguishable from inside the prediction — and the second is far more likely when the method is sampling. A negative from an incomplete instrument is not evidence; it is silence.

**How to apply.**
1. **Name the instrument in the prediction itself**, not just the threshold. Not "a 6th bank discloses" but "a 6th bank discloses, *as measured by EDGAR full-text search over all operating-company forms in the window*." The instrument is part of the falsification condition.
2. **Prefer complete-scan over sampling wherever a queryable primary corpus exists.** EDGAR FTS (`efts.sec.gov/LATEST/search-index?q=...&forms=10-Q&startdt=&enddt=`) covers every filer at once; ten months of trade-press monitoring did not. Cost: one query. Cf. [[finding_edgar_fts_refutes_tradepress_negatives]], [[finding_comprehensive_grep_over_sampling]].
3. **Filter the corpus by doc-type and direction before counting** — an entity keyword hit is not automatically an exposure (NPORT-P fund holdings dominated the raw hit count and are reverse-direction). Cf. [[finding_edgar_entity_hit_direction_and_doctype]].
4. **Check each newly-found name's FIRST disclosure date, not the filing you found it in.** TFIN's Q2 10-Q was in-window; TFIN's first Tricolor disclosure was not. This is the check that separates a real forward discovery from archaeology.
5. **Pre-register the re-check with a date and an exit.** OTTO-30 now carries: *re-run the identical query on 2026-08-15 (after small-bank Q2 10-Qs close); still zero new names → FALSIFIED.* Without this a discovery claim drifts to its resolve date on vibes.
6. **When a known-unknown turns up, treat your list as presumed-incomplete** and run the complete scan immediately — don't just log the one name. The second occurrence is the signal that the *method* is the defect, not the list.

**Generalizes to:** any "Nth instance will appear" claim over a queryable corpus — new fraud cases (EDGAR/PACER), new sanctioned entities (OFAC lists), new filings/registrations, new counterparties named in litigation. Also to roster/inventory claims: "no agent does X", "nothing references Y".

Related: [[feedback_forward_discovery_prediction_spirit]] (how to *score* it once it happens — this memory is how to stop it), [[finding_discovery_tool_wrong_slice_false_zero]], [[finding_threshold_spec_fails_before_world]], [[feedback_verify_existence_external_primaries]].
