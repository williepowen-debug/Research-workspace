---
name: finding_banner_is_a_warning_not_a_fix
description: "A SUPERSEDED/FROZEN banner makes a rotting doc feel handled and can extend its life for months — banners buy time, they don't stop the clock; pair every banner with a dated rewrite trigger"
metadata: 
  node_type: memory
  type: finding
  originSessionId: fc3e71c7-82d9-4929-bc1c-b5c4f3b21422
  modified: 2026-07-27T23:22:53.796Z
---

Putting a `⚠️ SUPERSEDED — do not action from this file` banner on a stale document is the correct *first* move and a poor *only* move. The banner converts an urgent problem into a comfortable one: every future reader sees the warning, concludes the situation is known and managed, and moves on. **The banner becomes the reason the rot survives.**

**FALCON, 2026-07-27.** `THESIS.md` and `TIMELINE.md` carried "SUPERSEDED, rewrite is an open backlog item" banners from **2026-04-20**. They were re-banner-stamped at an agent spinout, carried in handoff notes, and listed as a backlog item — and went **98 days** unrewritten while every other surface stayed current. Nobody was ever misled, because the banner worked. Nobody fixed it either, for the same reason.

**The concrete cost was not abstract staleness.** The stale thesis carried a **4-tier A/B/C/D scenario ladder** while every live surface had moved to **3-tier B/C/D** — so any new reader, or any *spawned sub-agent* reading the thesis document first (a common boot path), inherited a framework the agent no longer used. A banner saying "superseded" doesn't tell you *which parts* are superseded or what replaced them.

**How to apply:**
- **Pair every banner with a dated trigger**, not an open-ended "backlog" label: *"rewrite when X resolves / by DATE."* An item with no trigger is an item with no owner.
- Say **what specifically is wrong** in the banner, not just that it is old — *"this file's scenario ladder is 4-tier; the live one is 3-tier"* is actionable in a way *"superseded"* never is.
- Treat **structural contradictions with live surfaces** (a different taxonomy, ladder, or ID scheme) as a higher class than ordinary staleness — those actively mis-teach a reader who lands there first, and banners don't neutralise them.
- When a banner has survived two or three sessions, that's the signal to **either rewrite or delete the file**, not to re-stamp the banner. Re-stamping is how 98 days happen.
- Same shape for executables: a "frozen, do not use" designation on a script that is still wired into a live boot sequence is documentation, not enforcement ([[finding_stale_executable_exits_clean]]).

Related: [[finding_governance_doc_stale_default_drift]], [[finding_completion_stamp_skip_reads_as_current]], [[finding_passive_surface_rot_push_not_dashboard]], [[finding_mechanize_the_cap_not_the_ritual]].
