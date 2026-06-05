---
name: audit-packet-before-approval
description: "Before logging Will-approval on a consolidated multi-day decision packet, run an independent audit pass against source-of-truth files + live tape, asking \"what does this NOT cover?\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 27d4397e-ec03-41d2-99b4-ab1a8effed08
---

When presenting a Will-decision packet that consolidates multi-day work (e.g., default-pass deadlines absorbed, multiple domain agents weighed in, cross-line trade-offs locked), run an audit pass *before* Will approves. The audit should:

1. Verify load-bearing claims against source-of-truth files (FORGE/STATUS for positions; domain-agent STATUS for thesis weights; live dashboard for cushions).
2. Check stale data — packet tape snapshots are often hours-to-days old by approval time.
3. Ask "what does this packet NOT cover?" — adjacent decisions that look related but sit outside the rail's scope.
4. Surface findings as a refresh pass + explicit disclosure section *in the packet itself*, before approval.

**Why:** Validated 5/26 evening on v0.2 6/18-cluster approval. Will asked "any issues before we approve?" → audit pass surfaced (a) tape table 4 days stale; (b) WAL Q2-print rail blind spot (A4/A5 expire mechanically if WAL holds above $73 through 6/18, leaving no exposure for late-July REGINALD V2.2 catalyst — packet's own A5 rationale referenced the Q2 print but only inside the "if trigger fires" path); (c) AAL Jul 17 standalone characterized incorrectly. The default-pass discipline that gets a packet cleanly to PROPOSED also reduces per-line attention — cross-line gaps are easier to miss in consolidated artifacts than in piece-by-piece review. The audit asked questions the packet's own self-presentation didn't.

**How to apply:**
- Trigger when packet is `PROPOSED` and Will is about to mark `WILL_APPROVED`, especially after default-pass consolidation
- Always re-read live tape vs packet's snapshot; refresh table if stale
- Always ask "adjacent decisions" question: what could a reader mistake as covered that ISN'T covered?
- Surface findings as refresh-pass + new "Outside this rail" disclosure section *inside* the packet, not just verbally — see [[finding_outside_this_rail_disclosure]]
- Don't graft fixes into the packet (scope creep) — see [[feedback_refuse_rail_scope_creep]]
- Cross-references the inverse case from [[feedback_consolidate_domain_pressure]] — default-pass discipline produces clean packets, but the cleanliness itself creates the gap-detection blind spot
