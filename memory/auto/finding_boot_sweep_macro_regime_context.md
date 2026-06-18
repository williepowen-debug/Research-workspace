---
name: finding-boot-sweep-macro-regime-context
description: Boot sweeps should include a macro-regime-context check (current Fed Chair / BOJ Gov / key central-bank principals + statement-style); month-old Chair changes can sit un-modeled across multiple sessions if the boot baseline only covers data feeds and event calendars
metadata: 
  node_type: memory
  type: finding
  originSessionId: 74e6629c-7de8-44a9-8f52-2e2d3a93c875
---

For macro/policy-tracking agents (SAM, LIQUID, HENRY, BROCK, CARL, HAWK), the boot baseline typically covers data feeds (CFTC, MOF, BLS), event calendars (catalyst countdown), and threshold monitors — but does NOT verify the *regime* against which those data are interpreted: current Fed Chair, BOJ Governor, ECB President, Treasury Secretary, CENTCOM commander, key personalities. A change in any of these is a thesis-level fact that re-frames how the data feeds get read.

**Incident (SAM, 2026-06-18).** Fed Chair Warsh succeeded Powell on 2026-05-22 — a structural change in policy reaction function (statement-gutting hawkish, refuses to give forward guidance, "no reason to revisit the 2% target"). SAM operated through ~4 boot cycles between May 22 and Jun 18 with THESIS Pillar 1 + § Independent Catalyst still referencing Powell-era cut-pricing dynamics, and the FOMC Jun 17 sub-agent prompt named a "Powell presser." The fact surfaced only when Will directed a news sweep that included the FOMC outcome. The Jun-17 SEP +40bp dot revision + statement gutting then materially inverted Pillar 1's directional vector — a thesis-level update that was downstream of the Chair-change fact the boot had missed for 4 weeks.

**Why it slipped.** The boot reads data files and event calendars, both of which describe the world without naming who is interpreting it. boot.py + STATUS + THESIS index facts, not regimes. Regime identity slipped past four boot passes because no script or doc cross-checks "who chairs the Fed today / what's their statement style."

**How to apply:**
- Add a regime-context line to boot output: current Fed Chair (with effective date), BOJ Gov, ECB President, Treasury Sec, CENTCOM cdr — or whichever principals matter for the agent's domain.
- On regime change: trigger a sweep of THESIS pillars / channels that reference the prior principal's reaction function. SAM's Pillar 1 here named Fed cut/hike paths under Powell-era assumptions; the Chair change should have triggered a re-read at the time.
- Cross-applicable: LIQUID (Treasury Sec), HENRY (Fed Chair + key voters), BROCK (FDIC/OCC heads), CARL (Treasury debt-mgmt), HAWK (CENTCOM cdr), BRENT (DOE/SPR principals). Each agent owns its principals list.
- For sub-agents (KOYOMI, FASTOW, KURA): include a "regime-watch" line in standing-monitor checklists where the domain has principal-dependent reaction functions.

Related: [[finding_threshold_vs_mechanism]] (regime change is a mechanism change, not a threshold drift); [[feedback_check_recipient_before_sharing]] (verify the regime before relaying its data to peers).
