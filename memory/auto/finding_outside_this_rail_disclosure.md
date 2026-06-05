---
name: outside-this-rail-disclosure
description: "Will-decision artifacts with non-trivial scope boundaries should include an explicit \"Outside this rail\" subsection naming adjacent decisions the artifact does NOT cover."
metadata: 
  node_type: memory
  type: project
  originSessionId: 27d4397e-ec03-41d2-99b4-ab1a8effed08
---

New artifact subsection format for Will-facing decision packets. When a packet's scope boundary is non-obvious — i.e., reasonable adjacent decisions could be mistaken as covered — add an "Outside this rail (no [vX] coverage)" section that enumerates what the artifact deliberately does NOT cover, with a one-line note on where each adjacent decision routes instead.

**Why:** First instance 5/26 evening on v0.2 6/18 cluster approval packet. v0.2 was scoped to *theta-killer loss-management at 6/18 expiry*. But two adjacent decisions could look embedded: (a) WAL Sep $67.5P × N fresh-open for the late-July REGINALD V2.2 Q2 print catalyst; (b) AAL Jul 17 standalone (orphan, no rail). Without disclosure, Will could approve v0.2 believing his Q2-print exposure was preserved, when in fact A4/A5 mechanically expire if WAL holds above $73 through 6/18 → unhedged for the actual late-July catalyst. The disclosure makes the gap an explicit acknowledged design choice, not a silent hole.

**How to apply:**
- Trigger: any Will-decision packet whose scope is narrower than the "obvious" set of related decisions
- Section location: after design discussion (e.g., "What changed from vN-1 → vN"), before the live-tape table
- Format: 1-2 bullet items per scope-limit. Each bullet states what's NOT covered + where the adjacent decision routes (separate action card, future review window, etc.) + any timing constraint
- Cross-reference: log adjacent decisions as candidate rows in `ACTIVE_DECISIONS.md` so they stay boot-surfaced
- Companion to [[feedback_audit_packet_before_approval]] — the audit pass surfaces gaps; this is how to disclose them inside the artifact
- Companion to [[feedback_refuse_rail_scope_creep]] — once gaps are disclosed, RESIST the temptation to graft adjacent decisions into the existing packet
