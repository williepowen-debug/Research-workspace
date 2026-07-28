---
name: finding_visibility_is_layered_not_binary
description: "Is it reported?" is rarely one question — decompose into independently binding layers, because a datum can clear layer 1 and fail layer 4, and one exclusion list cannot serve both a numerator and a denominator
metadata:
  type: feedback
---

A question shaped *"is X visible / covered / tracked?"* reads as binary and usually is not. **Decompose it into the layers that each independently bind, and name which layer your question actually turns on.**

Worked case (DEWEY C4, 2026-07-28, phantom consumer debt). "Is BNPL debt reported to credit bureaus?" turned out to be **four** separate gates:

1. **Furnished** to any bureau — Affirm: yes (Experian 2025-04-01, TransUnion 2025-05-01). Klarna: term loans only, explicitly **not** pay-in-4.
2. **In the core file** vs a *specialty* file — bureaus built separate BNPL files; CFPB: *"may not be reflected in traditional credit reports and credit scores."*
3. **In the specific bureau your statistic reads** — the NY Fed QHDC is built on **Equifax**. Affirm furnishes Experian + TransUnion. So the loan is furnished **and** absent from the aggregate.
4. **Scored** — Klarna, verbatim: *"will have no impact on your FICO / Vantage score and will only be visible to you at this time."*

**Essentially all BNPL clears layer 1 and fails layer 4.** So "furnished" and "visible to underwriting" are different facts, and the gap between them is exactly the thing being measured.

**Why this bites, concretely:** the task instruction said *"exclude anything now being furnished"* from the phantom total. Followed literally it deletes the single largest book (~$17B) from a total whose entire purpose is measuring what lenders cannot see. **The instruction silently conflated layer 1 with layer 4.**

**The operational rule that falls out:** ⚠️ **one exclusion list cannot serve both a numerator and a denominator.** "Invisible to the QHDC" needs the *Equifax-furnisher* list; "invisible to lenders/scores" needs a different one. Using one for both over- or under-counts depending on direction. Pick the frame explicitly and say which layer it targets.

**How to apply:** before accepting or writing a binary coverage claim, ask *"reported to whom, appearing where, and used by which decision?"* If the answer differs across those, the claim needs a layer named or it is ambiguous. Applies well beyond credit data — regulatory filing vs disclosure vs enforcement; logged vs indexed vs alerted; measured vs published vs revised.

**Corollary that also fired here:** a zero-hit grep for a term in a filing is **weak evidence, not a negative**, when the fact isn't the kind of thing that document discloses. Affirm's 10-Q has no "credit bureau" hits because furnishing practice is not a 10-Q disclosure item — not because it doesn't furnish. Check whether the source *would carry* the fact before reading its absence as an answer. See [[finding_verify_reader_before_source]], [[finding_declared_data_wall_needs_fleet_memory_check]].

Related: [[finding_count_measures_intake_not_domain]], [[finding_spread_metric_blind_to_common_mode]], [[finding_proxy_segment_masks_trigger_series]].
