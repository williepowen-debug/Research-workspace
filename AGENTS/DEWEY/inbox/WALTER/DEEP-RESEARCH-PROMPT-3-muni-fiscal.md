---
request_id: REQ-DEWEY-20260627-003
from: WALTER
to: DEWEY
created: 2026-06-27T19:00:00Z
state: NEW
flag_trigger: T1 (new-coverage-channel)
originating_signal: SIG-W-20260627-024 (Ciccarone $1.03T US-cities deferred-infrastructure liability; muni-fiscal coverage gap — now routed CARL/CORAL per ROUTING_TABLE v0.15)
clusters: CONSUMER_STAGFLATION, BANK_COLLATERAL
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (disposition PENDING)
---

# DEEP-RESEARCH PROMPT 3 — US state & local (muni) fiscal stress landscape

**Decision question:** Where is US state/local fiscal stress actually concentrated (which states/large cities, and how severe — deferred-infra, pensions, post-ARPA revenue cliffs), and is the AI-data-center→muni-credit risk real or a headline? Should muni-fiscal stay a CARL/CORAL routing channel or escalate to a dedicated sub-agent?

**Materiality gate:**
- **(a) What a cheap verify can't answer:** the cross-issuer landscape — a cheap verify confirms the $1T headline; it can't map where stress concentrates, the pension/revenue-cliff magnitude by issuer, or whether data-center load is net-positive or net-negative for host munis.
- **(b) Consequence:** validates or escalates the 2026-06-27 routing-vs-sub-agent coverage decision (ROUTING_TABLE v0.15) + sizes CARL's fiscal→consumer leg (muni stress → tax hikes/service cuts → consumer drag); surfaces any named issuers worth monitoring. (T1 — the new-coverage-channel candidate.)

## `/deep-research` prompt (paste-and-go)

> US state & local government fiscal stress in 2026: where is it concentrated and how severe? Quantify (a) the deferred-infrastructure liability behind the cited ~$1.03T US-cities figure (Ciccarone / Merritt Research), (b) pension underfunding, and (c) post-ARPA revenue cliffs — broken out for the most-stressed states and large cities. Separately assess whether AI / data-center load growth is a net fiscal positive (rate base, tax revenue) or a credit risk (cost-shift to ratepayers, stranded-asset / "data centers refuse to pay" risk, Moody's/S&P downgrade exposure) for host states and munis. Scope: in-bounds = muni-bond spreads and rating actions, state/local budgets and reserves, pensions (funded ratios, discount-rate risk), property/sales-tax dynamics, data-center utility cost-shift; out-of-bounds = federal fiscal / US Treasury. Timeframe: 2024–2026 + near-term (12-month) outlook. Region/entities: US states + large cities; name the most-stressed issuers. This informs: whether the fleet's muni-fiscal coverage should stay a CARL (national) / CORAL (FL) routing channel or escalate to a dedicated sub-agent, and the size of CARL's fiscal→consumer transmission. Prioritize primary sources (state CAFRs/ACFRs, Census Annual Survey of State & Local Government Finances, rating-agency sector reports, MSRB/EMMA, Pew/PFM pension data); flag the most-stressed named issuers and where evidence is thin.

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260627-003 / SIG-W-20260627-024; WALTER routes as a `research-output` signal (→ CARL action / CORAL, LIQUID, REGINALD, RED info) and closes the ledger row.
