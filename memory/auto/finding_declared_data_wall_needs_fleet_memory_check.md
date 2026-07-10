---
name: finding-declared-data-wall-needs-fleet-memory-check
description: "A builder's honestly-verified 'data not retrievable' finding can be true for its system but false for the fleet — check the auto-memory index + the domain owner's dir for an already-solved door before accepting a declared wall (OZK/EDGAR vs FDIC API, 2026-07-09)"
metadata:
  type: feedback
---

**The pattern:** LABOR's Form-4 scanner build (2026-07-09) declared OZK insider data "not retrievable via SEC EDGAR by this or any similar tool" — verified against 4 independent SEC sources, hardened fail-loud, honestly reported. The finding was EDGAR-true but fleet-false: the FDIC securities-filings API ([[finding_fdic_securities_filings_api]], discovered in the OZK agent's session 3 days earlier) serves the same data through a different agency's door, and `AGENTS/OZK/INSIDERS/SELLING.md` was already tracking it, scored and current.

**Why:** rigorous within-system verification (N sources inside SEC) cannot detect a cross-system alternative (another agency, another agent's tooling). The builder's honesty made the wall *credible* — which is exactly what makes this class dangerous: a well-verified wall gets accepted and becomes a standing false blind spot. Sibling class: [[finding_asymmetric_records_need_reconciliation]] (one part of the fleet knows what another part re-discovers).

**How to apply:** when any agent (spawned builder, deep-research, or self) declares a structural data wall / "not retrievable" / "no source exists," the coordinator's acceptance step includes a fleet-memory check BEFORE the wall enters canon: grep the auto-memory index for the entity/data-type, and check the domain owner's dir (the agent that owns that name may already have the door). Also seed build-spawn prompts with the relevant `reference`-type memories for the entities in scope, not just technique memories. A declared wall is a claim requiring verification, same as a figure.
