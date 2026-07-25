---
name: finding_announcement_type_and_filing_precheck
description: "Every headcount-announcement ledger entry carries its TYPE (voluntary-offer / involuntary-RIF / closure / contract-churn); before naming Company X as a driver of a filing surge, confirm X's own filings exist in a primary/tracker. Types have different downstream signatures (VR offers ~0 UI claims; contractor-swap WARNs can convert to 0; remote-heavy layoffs skip WARN entirely) and mis-classification propagates into pre-registered predictions within hours."
metadata: 
  node_type: memory
  type: finding
  originSessionId: aedb2ece-71d2-44a2-acd4-efa61c16b92e
  modified: 2026-07-24T23:22:06.613Z
---

An "8,750 layoffs at MSFT" secondary report can turn out to be a voluntary-retirement OFFER program (acceptances unknown, mostly no UI claims filed). A "WARN surge driven by Company X" can turn out to have zero X filings when you check the state primary. Both errors book a phantom flow into whatever ledger uses the announcement as input — headcount pipelines, claims-flow forecasts, sector-cluster maps — and the phantom leg propagates into derivative pre-registered predictions within the same session that wrote the entry.

**Two connected checks, both cheap:**

1. **Every headcount-announcement ledger entry carries its TYPE** — voluntary-offer / involuntary-RIF / closure / contract-churn — because each has a different claims-flow signature:
    - VR offers ≈ 0 UI claims (acceptances mostly retire or take severance without filing)
    - Contractor-swap WARNs can convert to ~0 realized separations (workers picked up by the incoming contractor — e.g. Fortrex TX 85→0)
    - Remote-heavy layoffs often skip WARN filing entirely (no physical worksite → no WARN trigger — e.g. Rackspace ~750 AI-framed cut, WARN-invisible)
    - Involuntary RIFs + facility closures are the ones that actually convert to claims
2. **Before naming Company X as a driver of a filing surge, confirm X's own filings exist** — in the state/federal tracker or primary, not just downstream reporting citing X. Aggregators and trade press repeat unverified attributions.

**Why it matters:** the announcement layer is the FASTEST input into pre-registered predictions — a bad classification lands the same day and rewrites downstream text within hours. A same-day correction leaves derivative surfaces (predictions, dashboards, outbox packets) stale unless swept ([[finding_verification_correction_downstream_propagation]]).

**How to apply:**
- Any agent aggregating layoff/RIF/closure announcements (LABOR, BROCK, CARL, REGINALD, CORAL) adds a TYPE column to its announcement ledger.
- Any agent naming Company X as a driver of a filing/cluster attribution verifies X's filings in the primary before writing it — the aggregator or trade-press citing X is not enough.
- On correction, run the derivative-surfaces sweep from [[finding_verification_correction_downstream_propagation]] same-day.

**Provenance — LABOR L-07 (2026-07-02):**
- Carried "MSFT 8,750 (Jun 6)" in the priced-cuts list and attributed part of the mid-June WARN surge to "MSFT WARNs landing"
- Jul-2 sweep found: (a) the 8,750 was a voluntary-retirement OFFER program (Rule of 70; window closed ~Jun 6; acceptances never public) → VR acceptances mostly don't file UI, booking it as layoffs overstates the claims pipeline; (b) Microsoft had zero 2026 WARN filings → the surge attribution had a phantom leg
- The phantom leg had already propagated into a pre-registered prediction's mechanism text (LAB-17) within hours of writing it
- Corrections took a same-day derivative-surface sweep to catch (STATUS + calendar + LAB-17 mechanism text)

Related: [[finding_verification_correction_downstream_propagation]] (derivative-surface sweep post-correction) · [[feedback_verify_existence_external_primaries]] (verify existence before treating as fact) · [[finding_threshold_spec_fails_before_world]] (misspec often precedes correction).
