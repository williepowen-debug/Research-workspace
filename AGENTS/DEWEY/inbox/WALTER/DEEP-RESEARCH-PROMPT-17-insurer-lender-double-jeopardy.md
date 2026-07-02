---
request_id: REQ-DEWEY-20260702-013
from: PROME (Will-directed batch 2026-07-02 — fleet-mined slate; WALTER logs + routes, see AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md)
to: DEWEY
created: 2026-07-02T04:00:00Z
state: NEW
flag_trigger: T3 (load-bearing-but-thin)
originating_evidence: "trade-relevance depends on specific entity+fund mapping — which insurers hold AND lend to which of the 5 named gated funds. That mapping is not yet complete." (AGENTS/SHADE/research/INSURER_LENDER_DOUBLE_JEOPARDY_2026-06-26.md — map cells all Unknown/NOT CONFIRMED). BROCK+SHADE independently queued the identical filing-mining task.
clusters: M-08 insurer nexus / gate cascade / double-jeopardy (vector-7)
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (WALTER logs row at next boot, disposition QUEUED)
run_order: 13 of 13
deliver_by: 2026-07-22 (before BDC Q2 marks 7/25-28; the paired wrapper-decoupling trigger sits ~5bp away)
governance_note: SHADE pre-registered its own dig as trigger-gated ("no dig absent a trigger", SHADE STATUS §10 item 6). Will sanctioned this DEWEY pre-stage as part of the 7/2 all-13 batch approval — the exception covers DEWEY's fact-finding only; SHADE's own escalation/dig discipline stays trigger-gated and SHADE decides what to do with the map when it lands.
---

# DEEP-RESEARCH PROMPT 17 — Insurer-lender double-jeopardy map of the 5 gated funds

**Decision question:** If wrapper-decoupling fires (HY>280 AND wrapper-led), which named insurer takes the synchronized holder-plus-lender hit — and does the Q2 gate wave create double-exposed insurer-lenders escalating the Athene vector?

**Materiality gate:**
- **(a) What a cheap verify can't answer:** the map requires mining SEC credit-agreement exhibits/8-K signature pages across 5 funds for the lender side, PLUS public shadows of NAIC Schedule BA statutory data for the holder side, then cross-referencing — too broad for either SHADE's or BROCK's single session, which is why both queued it.
- **(b) Consequence:** converts double-jeopardy from mechanism-watch to named-entity exposure; escalates BROCK's Athene/insurance vector (🟠3) on confirmation; unlocks SHADE mapping and pre-stages the TERRY target the moment the trigger fires.

## `/deep-research` prompt (paste-and-go)

> Insurer-lender double-jeopardy map of the Q2-2026 gated funds. IN-BOUNDS: (1) LENDER SIDE — for each of: Blackstone BCRED, Apollo Debt Solutions BDC (ADS), Monroe Capital Income Plus, Cliffwater Corporate Lending Fund (CCLFX), and Morgan Stanley North Haven Private Income Fund, enumerate named lenders on revolving/subscription/NAV credit facilities from SEC credit-agreement exhibits and 8-Ks (10-K/10-Q exhibit indexes, signature pages, amendments), N-CEN Part C line-of-credit disclosures, and SAI borrowings sections; flag every life insurer or insurer-affiliated lender (Athene, Global Atlantic/KKR, Corebridge, F&G, Brighthouse, MassMutual, TIAA, etc.). (2) HOLDER SIDE — which of those insurers simultaneously hold equity/Schedule-BA positions in the same funds, using public shadows of NAIC statutory data: insurer 10-K related-party and investment notes (esp. Athene/Apollo), state-DOI-accessible statutory filings, NAIC Capital Markets special reports, Moody's/Barclays/Clearwater analyses. (3) Adjudicate the Athene↔ADS pair explicitly: does Athene hold ADS equity AND does Athene or an Apollo affiliate lend to ADS facilities? (4) Prioritize confirmed holder+lender overlaps by insurer RBC-buffer fragility (F&G > Brighthouse > Corebridge > GA > Athene). DISCIPLINE: where Schedule BA is not publicly obtainable for an insurer, state so per fund/insurer explicitly — do not infer holdings. OUT-OF-BOUNDS: gate mechanics re-derivation (BROCK canonical); Athene balance-sheet totals (covered by the 6/27 DEWEY report); re-litigating the WSJ/Clearwater ~25% aggregate stat; re-opening the BCRED-Athene direct pair (ruled out in-repo) absent new primary evidence; trade construction. TIMEFRAME: latest available filings (FY2025 statutory, Q1-2026 SEC).

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260702-013; WALTER routes as a `research-output` signal (→ SHADE action [insurer side] / BROCK co-owner [fund side] / REGINALD, NEXUS info, TERRY downstream) and closes the ledger row.
