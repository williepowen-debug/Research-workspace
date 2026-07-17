---
name: finding_fused_true_facts_false_premise
description: A false premise most often arrives as TWO separately-true facts about different entities/dates welded into one causal claim — and it arrives pre-framed as a high-priority routing item. Decompose every relayed premise into its atomic facts and date-stamp each one BEFORE building on it.
metadata: 
  node_type: memory
  type: finding
  originSessionId: 04cf38c5-5603-446b-bb9d-12a9d5cf55cf
---

**The pattern:** the premises that waste the most work are not fabrications. Every atomic fact in them is **true and primary-sourceable**. The failure is in the **weld** — two facts about *different entities* or *different dates* get fused into one causal claim, and the causal claim is the part nobody sourced because it was never in a source at all. It is created by the juxtaposition.

**It fired twice in one week in one domain (private credit, 2026-07-16/17):**

| | Fact A (true) | Fact B (true) | The weld (false, unsourced) |
|---|---|---|---|
| **BRK-25** | **MFIC** — listed BDC, ~$3B portfolio, shopped per WSJ 5/10 | **ADS** — non-traded, had an **11.05%** redemption quarter | *"Apollo shopping a captive listed BDC @ **$0.85/NAV** with an 11% redemption quarter."* The $0.85 was **MFIC's May price ÷ NAV** (11.68/13.82=0.845) — a market quote read as a bid. Two Apollo vehicles, ~1 month apart. |
| **CCLFX** | **Gate** — Q2 5% cap vs ~17% requested, priced 5/29/26, reported 6/2/26 | **$1B secondary** — PitchBook **3/10/26**, GP-led sell-down into a 2:1-levered vehicle, *"portfolio management **rather than forced liquidity**"* | *"CCLFX gating **and force-selling $1B to meet redemptions**."* B **pre-dates** A by ~3 months and cannot be a response to it. |

**Third instance within 24h, different domain (AI-capex, 2026-07-17 — VULCAN):** *"AMZN 6→5y useful-life shortening / $920M charge"* rode in PROME's DOCKET row and VULCAN's own tasking. Fact A (true): AMZN shortened server life 6→5y eff. 1/1/25 (impact ~−$0.7B FY25 op income). Fact B (true): a **$920M Q4'24 early-retirement accelerated-depreciation charge** — a SEPARATE disclosure that does **not** count toward the useful-life gate [AMZN FY24 10-K]. The weld put B's dollar figure on A's event. **VULCAN's corollary (its L-10): the canon you inherit from yourself gets the least scrutiny — the weld had cycled through several of our own surfaces, and repetition laundered it.** Also missed by the weld: AMZN had *extended* 5→6y eff. 1/1/24 first — the round trip is the real signature.

**Why it survives review:** every fact checks out. An agent verifying "is MFIC being shopped?" or "did CCLFX gate?" gets YES and moves on. **Nobody verifies the connective tissue**, because the connective tissue does not look like a claim — it looks like context. And once welded, each re-citation of the fused form counts as "seen before" rather than "needs sourcing."

**Why it is dangerous:** it arrives **pre-framed as the highest-priority item of the day**, with the urgency attached to the weld rather than the facts. The CCLFX spec was routed 🔴 *because* the fusion made it look like a live forced sale; a downstream audit then re-rated a separate research prompt "the hottest" **for the same reason**. False premises propagate *faster* than true ones because the weld is what makes them interesting.

**How to catch it — the check is cheap and mechanical:**
1. **Decompose the premise into atomic facts.** Each noun phrase that carries a number or an entity is one fact.
2. **Date-stamp each fact independently.** Not the date it was *routed* to you — the date of the **underlying event**. `[[finding_designation_date_lags_event_date]]`
3. **Check the entities are the same entity.** Manager-family names ("Blue Owl", "Apollo") routinely stand in for 3-4 distinct registrants. `[[finding_insurer_entity_scope_trap]]`
4. **Ask what source states the CAUSAL link.** If the answer is "none — it's implied by the ordering," the link does not exist. Chronology alone refutes it more often than not.
5. **Read the original source's own framing.** PitchBook explicitly said *"rather than forced liquidity"*; the fusion inverted the source's own verdict.

**The honest-caveat discipline:** having found the weld, do not over-swing. The CCLFX sell-down *was* contemporaneous with the repurchase escalation, so *"wholly unrelated to redemptions"* would have been a second false claim replacing the first. The defensible statement is narrower and sufficient: **vintage and structure are settled; motivation is ambiguous.** Correcting a premise does not license asserting its inverse. `[[finding_refuted_claim_citation_vs_fact_failure]]`

**Related:** `[[finding_deep_research_stale_vintage_headline]]` (one leg of the weld is usually a stale vintage) · `[[finding_catalyst_vs_consequence_conflation]]` (the probability-structure cousin) · `[[finding_asymmetric_rigor_counterparty_claims]]` (you grep your own claims and infer about relayed ones)
