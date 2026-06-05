---
name: refuse-rail-scope-creep
description: "When a new decision could fit an existing rail by stretching scope, prefer a new rail + clean candidate row over scope creep on a working rail."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 27d4397e-ec03-41d2-99b4-ab1a8effed08
---

When the temptation arises to graft an adjacent decision into an existing Will-approval packet ("efficient — one approval covers both"), resist. The "efficiency" is illusory; it conflates decision types, expands the approval contract, makes the rail harder to reason about, and breaks the rail's own self-description.

**Why:** Validated 5/26 evening on v0.2 6/18 cluster. Pre-approval audit surfaced the WAL Q2-print gap (A4/A5 expire mechanically if WAL holds above $73 through 6/18 → no late-July exposure). Two paths to fix: (a) approve v0.2 clean and route Q2-print exposure to its own action card; (b) graft a time-trigger into v0.2 that auto-spawns the fresh-open decision on 6/13. Path (b) was seductive but wrong because: (1) v0.2's own self-description was "no threshold edits, no new trigger IDs, no positions added or removed" — adding a time-trigger violates that; (2) the cluster card is loss-management of dying premium; fresh-open with $1000-1400 cost is a new-exposure category — different decision; (3) compound packets are harder to reason about now and harder to debug post-hoc; (4) embedding doesn't actually save a Will-touch (sizing/IV still need eyes at decision time) — it just bundles two unrelated decisions.

Chose (a): v0.2 stays clean, Q2-print becomes its own candidate row. Same principle as [[feedback_consolidate_domain_pressure]] — stable-scope rails are how decision quality compounds; scope creep erodes it.

**How to apply:**
- When auditing or amending a Will-decision packet, if a new decision could "fit" by stretching scope, ask: does it belong to the same decision category (loss-management vs new exposure vs sizing vs roll target)? Same time horizon? Same domain agent? Same cost order-of-magnitude?
- If any answer is "no" → it's a new rail. Add as candidate row in `ACTIVE_DECISIONS.md`; surface as its own action card when concrete.
- If all answers are "yes" but the existing rail says "no new trigger IDs" or similar self-discipline → still a new rail. Respect the artifact's own self-description.
- Default position: new rail. Scope creep is the easy mistake; new rails require slight extra plumbing but preserve decision-quality across iterations.
- Cross-references: [[feedback_audit_packet_before_approval]] (the audit is where this temptation first arises) and [[finding_outside_this_rail_disclosure]] (how to disclose the resulting scope-limit in the packet)
