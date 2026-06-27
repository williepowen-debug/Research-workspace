---
request_id: REQ-DEWEY-20260627-002
from: WALTER
to: DEWEY
created: 2026-06-27T19:00:00Z
state: NEW
flag_trigger: T3 (load-bearing-but-thin) + T4 (position/thesis-pivot)
originating_signal: SIG-W-20260627-017 (ex-AI Q1 economy contracted −1.1%; AI capex +23% masking; the ~+1.6% headline flagged as superseded 2nd-estimate)
clusters: CONSUMER_STAGFLATION
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (disposition PENDING)
---

# DEEP-RESEARCH PROMPT 2 — Ex-AI-capex real economy ⭐ WALTER recommend

**Decision question:** Is the "US real GDP ex-AI-capex contracted ~−1.1% in Q1-2026 while headline stayed positive" decomposition robust, and what does private final demand ex-AI-capex actually show over the last 4 quarters?

**Materiality gate:**
- **(a) What a cheap verify can't answer:** the full decomposition across BEA NIPA components — a cheap verify confirms one number, not whether the ex-capex contraction is robust to method/classification or a one-quarter artifact.
- **(b) Consequence:** CARL's stagflation/consumer-deterioration thesis + RED/HENRY recession-timing confidence + bear-position sizing — if the real economy ex-capex is already contracting, the "resilient consumer/economy" bull-counter weakens materially.

## `/deep-research` prompt (paste-and-go)

> Ex-AI-capex US real economy: decompose US real GDP and private final demand for the last four available quarters to isolate the contribution of AI / data-center capex (and the broader tech-capex + directly-related construction/equipment/electrical) from the rest of the economy. Test the specific claim that US real GDP excluding AI-capex contracted ~1.1% annualized in Q1-2026 while headline GDP stayed positive (~+1.6%). Quantify the AI/data-center capex contribution to headline growth and show what private final demand / real final sales to domestic purchasers look like net of it. Scope: in-bounds = BEA NIPA components (nonresidential fixed investment in intellectual property, structures, equipment tied to data centers; the capex multiplier into construction, electrical, employment), Census construction-spending + durable-goods, the data-center share of structures investment; out-of-bounds = equity-market AI valuation / stock prices. Timeframe: Q2-2025 through the latest available quarter (Q1-2026). Region/entities: US national accounts. This informs: CARL's stagflation/consumer-deterioration thesis and the fleet's recession-timing confidence — whether "the economy ex-AI is already contracting" is a load-bearing fact or a fragile decomposition artifact. Prioritize primary sources (BEA NIPA tables, BLS, Census); flag where the result is sensitive to method, classification of data-center spend, or estimate vintage.

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260627-002 / SIG-W-20260627-017; WALTER routes as a `research-output` signal (→ CARL action / HENRY, RED, BROCK info) and closes the ledger row.
