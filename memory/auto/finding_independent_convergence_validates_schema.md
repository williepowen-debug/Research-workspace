---
name: independent-convergence-validates-schema
description: "When proposer and consumer independently converge on the same schema/protocol amendments without coordination, the schema is mature enough to ratify; absence of independent convergence = schema needs another iteration"
metadata: 
  node_type: memory
  type: finding
  originSessionId: d6df3109-fea7-4478-9f59-023a300bc018
---

When a proposer-agent (the one drafting a schema, protocol, or shared spec) and the consumer-agent (the one whose workflow consumes it) work *in parallel without seeing each other's output* and arrive at substantially the same amendments, that independent convergence is **strong evidence the schema is mature enough to ratify**. Conversely, absence of independent convergence is a signal the schema still has unresolved design tensions and benefits from another iteration round.

**Why:** Validated 2026-06-07 on the NEXUS_BRIEF schema. SAM (proposer, after PROME R1+R2) committed R3 at 19:46 ET applying 6 amendments. NEXUS (consumer) dispatched independent feedback at 19:49 ET — written without seeing R3 — proposing 6 schema amendments. **5 of 6 overlapped exactly** (Recent Thesis Pivot required, Cross-agent tensions required, WATCH→FORWARD CATALYSTS rename, emoji semantics locked, conviction decomp optional, Tier-1-only scope). The 6th was complementary (NEXUS added "Expected by" column, SAM added Type B convergence-candidate sub-bullet — both filled gaps the other had also noticed but expressed differently). The pattern is informative because the two agents had different optimization functions (SAM compressing for own write-cost; NEXUS optimizing for fleet-scan consumption) and still landed on the same answers — meaning the schema's core tradeoffs are well-resolved, not arbitrary.

**How to apply:**
- When ratifying any shared spec (schemas, protocols, templates, brief formats, sub-agent contracts), look for evidence of independent convergence between proposer and consumer before locking. If both independently propose the same amendments → ratify. If amendments diverge sharply → another iteration round.
- Forcing the independence is part of the value: don't have proposer and consumer iterate in same conversation. Let each write against the artifact in isolation; *then* compare. Convergence under that condition is what validates.
- Inverse signal: if proposer's iteration and consumer's review propose *disjoint* amendments, the schema has unresolved tensions in different directions — neither party's view alone is sufficient, and the schema needs another round before ratification.
- Generalizes beyond schemas: applies to any shared-contract artifact where two-party convergence is achievable (sub-agent rubrics, brief formats, KB structures, signal-routing protocols, closeout-step orderings).

Related: [[finding_doc_mirror_consistency_check]] (downstream consequence — once a schema is locked, mirror-consistency between canonical and derived docs becomes the next discipline); [[finding_subagent_baseline_audit]] (sub-agents maintaining a set — same independence-test principle applies when proposing baseline scope).
