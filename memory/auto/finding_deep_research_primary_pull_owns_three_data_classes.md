---
name: finding_deep_research_primary_pull_owns_three_data_classes
description: "the deep-research workflow structurally CANNOT reach three data classes (paywalled/discontinued series, live current-readings, single-name secondary/filing detail) — the agent's own FRED/EDGAR pull must own them, which also upgrades the workflow's medium-confidence claims to primary-confirmed"
metadata: 
  node_type: memory
  type: finding
  originSessionId: fdac7b01-dbf6-4f06-84c6-20a6cea36d5c
---

The `/deep-research` workflow gives **breadth** (many sources, adversarial verify) but there are **three recurring data classes it structurally cannot reach** — and they are disproportionately where the decision hinges. When you run it, plan to own these yourself via your `scripts/` (FRED/EDGAR/pdf2text), *concurrently* in the background while the workflow fans out:

1. **Paywalled / discontinued series** — the workflow returns a stale republished proxy at best. *Ex (prompt 10, energy-HY-OAS):* the ICE energy sub-index is off free FRED; the workflow's only hard number was a **May-31 vintage republished in a Fidelity PDF**, five weeks stale vs the live question. DEWEY confirmed the 164 by pulling the source PDF directly AND supplied the broad-HY-OAS path *through* the event window from FRED — the workflow's data stopped before the event.
2. **Live "current readings" of a monitored series** — the workflow often returns ZERO current values even when named in scope. *Ex (prompt 07, funding gate):* it returned no current funding-microstructure readings at all; DEWEY's FRED pull (SOFR-IORB, SOFR 99th-pctile, RRP) supplied the entire "current readings" deliverable leg — plus a structural datum the episode papers predate (RRP drained to ~$6B, buffer gone).
3. **Single-name secondary/issuer detail** — bond spreads need a terminal; capital structure lives in filings the workflow reads via flaky newswires. *Ex (prompt 18, CoreWeave):* the EDGAR 10-Q pull (`edgar_doc.py`) gave the exact funded-debt table, the **effective-vs-stated coupon reconciliation** (10-Q "rate" col = effective; pricing-release = stated), and the customer-concentration figures the workflow's secondary sources garbled.

**Why it matters beyond filling gaps:** the primary pull also **upgrades the workflow's own confidence** — a claim it returns 2-1 "medium" (single republisher) becomes document-confirmed once you pull the source, and you catch reconciliations/misframings the fan-out can't.

**How to apply:** before launching the workflow, identify which load-bearing numbers fall in these three classes and queue your own FRED/EDGAR/PDF pulls to run while it works. Write the primary results to scratch so they survive to synthesis. Treat the workflow's "current readings / live level" legs as presumptively unmet — verify, don't assume. Note (workflow ops): if the run fails on its **first (scope) agent** with a StructuredOutput retry-cap error, resume-from-runId is effectively a clean restart (nothing cached) and usually succeeds — a transient entry-point failure, not systemic. Related: [[finding_deep_research_stale_vintage_headline]], [[finding_deep_research_slate_mining]], [[feedback_pull_live_primary_not_dashboard]], [[finding_edgar_403_user_agent_header]], [[finding_verify_loadbearing_before_trade]].
