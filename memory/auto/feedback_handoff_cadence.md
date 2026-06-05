---
name: Session Handoff Cadence
description: Will prefers clean handoffs at natural breakpoints over riding a long session into degradation
type: feedback
originSessionId: 1c71cf68-1772-4e62-a2be-566f76ade21d
---
Will would prefer to stay in one session for continuity, but knows long context windows cause problems — so he proactively initiates handoffs at natural breakpoints rather than pushing through until degradation.

**Why:** Apr 20 2026 session — after commit+push closeout, Will's message: "to be clear I would love to stay in one session, but I just know that the longer these windows go the more problems we have." He times handoffs at plumbing-clean moments (closeout done, memory written, commit pushed) so the next session boots from disk not from a compacted summary.

**How to apply:**
- Don't push back on handoff requests as "premature" — respect his intuition that the window's getting tight, especially if the session already saw one compaction.
- **Proactively surface handoff-good moments:** after any closeout, after 7+ sub-agent spawns, after a session shape-change (routing → architecture Q&A, or investigation → implementation), after a compaction notice.
- Make the pre-handoff closeout thorough — STATUS/MEMORY/LAST_COMPLETION are designed so the next session picks up from disk, not from context. If those are stale or thin, the next session starts with less than it should.
- When Will signals "handoff now", do STATUS → MEMORY → LAST_COMPLETION → commit+push in sequence without asking whether each step is needed. These are the plumbing he relies on.
- The spawn protocol's boot sequence (read STATUS, MEMORY, LAST_COMPLETION, REGISTRY, COP, ROUTING_TABLE, scan BOARD) was designed for exactly this. If the closeout is tight, boot recovery is tight.

**Corollary:** if he says "let's keep going" after a handoff offer, that's also valid — he's asking because he'd like to stay in flow. Don't force a handoff on him; offer it and let him choose.
