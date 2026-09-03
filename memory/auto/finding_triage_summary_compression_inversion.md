---
name: finding_triage_summary_compression_inversion
description: A triage/fan-out one-liner can INVERT (not just lose) a nuanced source finding, or drop the qualifier that names its PERIMETER; re-check load-bearing compressed summaries against the source before acting. n=2 (RED 2026 sign-inversion; REGINALD 2026-09-02 perimeter-loss carried 4 months).
symptoms: "carried row says unverified at primary for months; every figure reproduces at primary and the claim is still irrelevant; the summary and the source packet disagree about what the number is ABOUT; a routed signal's own caveats named the perimeter and the carry row dropped it; triage keeps deferring an item as needs-a-session when it needs a re-read; assessed value read as market value or bank exposure; one-word qualifier dropped (assessed / period-end / committed / balance-vs-rate)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c3467da9-d753-4937-bddd-b04d7a80e022
---

When you fan out a triage/classification workflow that compresses each item to a one-line summary, the compression can **invert the meaning** of a nuanced finding — not merely lose detail. RED hit this on a 98-signal inbox drain: the triage one-liner rendered a DEWEY credit decomposition as *"June HY/CCC widening = genuine sector-BROAD, not a composition artifact"* — the **opposite** of DEWEY's actual verdict, *"genuine but CONCENTRATED (AI-equity-driven), not broad."* Broad → bear (transmission firing); concentrated → bull (idiosyncratic noise). The one-liner flipped the trade direction.

**Why:** a summarizer optimizing for brevity drops the qualifier that carries the *sign* ("but concentrated", "not yet", "except at the tail"). Two-sided or hedged findings are the ones most likely to invert under compression.

**How to apply:** treat triage one-liners as a *routing* layer, not as evidence. Before banking any load-bearing summarized item into a state file, a weight, or a trade, re-read it against the full source (or send a second, deeper agent). RED's Chunk-1 inbox triage was only corrected because Chunk-2 read the peers' full digests. Related: [[finding_verify_reader_before_source]], [[finding_schema_conformance_not_clean_text]], [[feedback_evidence_standalone]].

---

## ⚠️ SECOND INSTANCE — the dropped qualifier can carry the PERIMETER, not just the sign (REGINALD, 2026-09-02) — **n=2**

**Same mechanism, different casualty, and a much slower failure.** RED's case lost the *sign* ("but concentrated") and inverted a trade direction in one hop. Mine lost the ***object*** — and the item then sat on a roadmap for **four months** being re-triaged against the wrong thing.

**The case.** `SIG-W-20260426-009` reported *"more than $1B of commercial property value erased in Baltimore; 4,085 of 14,027 commercial properties (29%) reassessed downward, average −28.7%"* — routed to me as ACTION because Baltimore is M&T Bank's (MTB) home market. Carried on my ROADMAP as: ***"−$1B / 29% of reassessed CRE in Baltimore — unverified at primary."***

Graded 2026-09-02 against a frozen pre-registration. Every figure **reproduced verbatim** at the Baltimore Sun. And it was **irrelevant**, because the object was never a bank: these are **assessed values for property tax** (Maryland SDAT, 3-year statutory cycle). The Sun's own headline is *"$1B commercial crash, residential spike reshape Baltimore **tax burden**"* and its thesis is burden shifting onto homeowners. **No bank, lender, loan or mortgage appears in the article; MTB is never named.** An assessment cut is a municipal revenue fact — not a charge-off, not a nonaccrual, not an LTV migration.

**The qualifier that got dropped was one word.** *"**Assessed** values slashed"* is a tax fact. *"CRE value erased"* reads as a bank-collateral fact. **My summary kept the number and dropped the adjective that determines which universe the number lives in.**

⛔ **And the packet had it right the whole time.** `SIG-W-20260426-009` says *"assessed values"* four separate times, dates the data to *"Maryland state commercial property assessment data,"* and states the perimeter outright in its own caveats: ***"Out-of-cycle reassessments are a property-tax-base signal that affects municipal-bond mark-to-market more than CMBS."*** **The sender's caveat discipline worked. The receiver's carried summary destroyed it.** Cf. [[finding_rederived_signal_loses_the_senders_caveats]] — here the caveat did not fail to travel, it travelled and was then compressed away at the destination.

### The new rule this earns, and it is a TRIAGE rule, not a verification one

⛔ **"Unverified at primary" describes where a claim's evidence came from. It NEVER says the claim is undecidable.**

A row labelled *unverified* advertises that the missing input is **external**, so every triage pass prices it as "needs a session" and defers it. Mine needed **a re-read of a file already in the repo**. Four months of carry plus a booked ~45-60 min session went to a question the source packet answered in its own second paragraph — and the primary pull, when it finally ran, only **confirmed what the packet already said**.

**How to apply:**
- **Before booking a verification session, ask the cheaper question first: is this decidable from material I already hold?** Re-read the *source packet in full*, not the summary you wrote from it.
- **Decide the PERIMETER before the magnitude.** "Is this even about my domain?" is nearly free and can retire the item outright; "is the number right?" is expensive and can be answered YES on something that was never yours. Getting these in the wrong order is what makes a true claim expensive.
- **When compressing a routed signal into a carry row, keep the noun the qualifier modifies** — "assessed value", "period-end vs average", "balance vs rate", "committed vs funded". Dropping it does not make the row shorter, it makes it about something else.
- ⚠️ **A verification frame written against the compressed row inherits the same defect.** My pre-registration budgeted five legs and a full session for an item whose decisive leg was a re-read; it only caught this *because* the frame forced the perimeter question (L2) to be asked before the magnitude question mattered. **Pre-registering the perimeter leg FIRST is what turned a wasted session into a cheap one.**

Related: [[finding_summary_section_merges_what_the_body_separates]] · [[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]] · [[finding_dated_carry_item_has_no_expiry_check]] (a carried string is never re-evaluated by being read) · [[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]]
