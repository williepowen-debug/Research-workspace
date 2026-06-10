---
name: finding_external_consumer_check_before_restructure
description: "Before restructuring/retiring any agent file, grep for consumers OUTSIDE the agent's directory AND check the current reference implementation, not just the template/spec doc"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: de6bdaa1-59b8-4ef3-a048-32bc7fc5487b
---

Before restructuring or retiring any file in an agent's directory, run two checks that reading the file cannot answer:

1. **Grep for consumers outside the agent's own directory.** VIOLET's SIGNAL_INTAKE.md was graded "unowned, rot, rehab-or-retire" by two independent reviewers (VIOLET root-audit + orchestrator first pass) who both read the file. The decisive fact — it is WALTER's per-agent subscription spec (`AGENTS/WALTER/design/SIGNAL_INTAKE_TEMPLATE.md`, STATE.md §8 rollout tracker) — was only visible by searching for who reads it. "Unowned" was half right: the file had a consumer that nothing in the owner's docs recorded. Record the consumer in the maintenance/ownership table when found.

2. **Check the current reference implementation, not just the template.** The orchestrator's rewrite instruction ("ACTIVE THRESHOLDS = perishable section, current live levels") followed template v0.1 — but CARL, the designated reference, had evolved past the template on its 5/31 hygiene pass (deleted Active Thresholds + dated catalysts as drift hazards; file became "scope-of-attention only" with live-source pointers). Conforming to the spec doc alone would have rebuilt the stale-copy disease the rework was curing.

**Why:** file-level rot diagnoses and conformance instructions both default to reading the artifact in front of you; consumers and pattern-evolution live elsewhere in the tree.

**How to apply:** before any restructure/retire/conform job: `grep -r <filename> --include=*.md` outside the owning dir; if a template names a reference implementation, read the reference's CURRENT state and diff it against the template's instructions — divergence is signal (the reference learned something). Validated VIOLET/WALTER 2026-06-10 (ROUTING_TABLE MARKET_VOL gap found the same way: the live routing table didn't route vol to VIOLET at all). Pairs with [[finding_number_carries_threshold_unit_source]] (same class: the artifact in front of you is not the ground truth) and [[feedback_check_existing_design_docs]].
