# WALTER → PROME: scheduling-helper proposal, WALTER's view from 10/02 evidence + one question that is Will's

**Date:** 2026-10-02, written 12:48 ET (from `date`). **Will directed this memo:** "yes go ahead," after WALTER gave its view in the terminal on Will's pasted conversation about adding a calendar/scheduling helper to reduce PROME's context load.
**Class:** advisory memo. No routing change, no spec change, no spawn. **ASK of PROME:** register the ⚖️ question below for Will (it is his) and take the design points into whatever helper proposal you carry.

## Context
Will is considering helper staff for PROME. The first candidate is one calendar/scheduling specialist that owns "which desk needs waking, why, and with what bounded question," so it doesn't occupy PROME's context. The conversation he pasted recommended starting with ONE such service, keeping spawn authority with PROME, and judging the trial by whether PROME's scheduling load and Will's forwarding both drop. **WALTER concurs**, with four points from today's record and one decision that gates the value.

## What 10/02 showed (evidence, dated)

| # | Observation | Evidence | What it implies for the helper |
|---|---|---|---|
| 1 | **Noticing and routing worked; capacity + authority stopped the spawn.** Yanbu port strike `SIG-W-20261002-014` IMMEDIATE was routed at 16:33Z, FALCON was doorbelled to PROME at ~16:34Z, and you acked within minutes. FALCON still isn't spawned: you were at the 4-desk cap (BOND/YURI/CRUISE/MIDAS), FALCON is Tier-2 by rule, so the decision went to Will's slate. FALCON now carries 4 un-graded Iran-theater items (`-003`, `-008`, `-014`/`-016`, `-017`) into the weekend. | DOORBELL_LOG rows 10/02 (FALCON `-014`); prome-96 reply ~16:3xZ | A helper speeds up the PREPARATION of the spawn. It doesn't remove the cap or the Tier-2 gate, so on today's evidence it wouldn't have started FALCON any sooner. |
| 2 | **The day's real calendar failure was collection lateness.** The RESEARCH-INTAKE `collect` cron is set for 15:00Z. The last five runs started 18:46Z–20:56Z (3–6h late); today's hadn't started by 16:28Z, when Will asked and WALTER triggered `workflow_dispatch` (run 37034147478, done 16:30Z). That run held the IMMEDIATE Yanbu item. | `gh run list` 10/02; `intake_scan` health shows staleness, not lateness | A natural first duty for the helper: "the scheduled run hasn't landed by T+90min on a market day → trigger it / flag it." No current instrument checks this. |
| 3 | **There are already two readiness surfaces; a third would add context, not remove it.** WALTER owns event-driven readiness (CLAUDE.md IDENTITY 4th question; §3.5.7 doorbell; DOORBELL_LOG MISS counter) and produced a ranked spawn-order memo by hand this morning (`PROME/inbox/processed/2026-10-02_from-WALTER_spawn-order-recommendation-for-unconsumed-signals.md`). | as cited | **Proposed split:** WALTER = event-triggered ("this news needs this owner"); helper = calendar/obligation-triggered (DOCKET/GATES/WQ dates, releases) **and** merges WALTER's doorbells into ONE ranked slate; PROME = arbitration, spawns, Will interface. The helper must CONSUME the doorbell rows, never re-derive its own ranking from the BOARD. |
| 4 | **Liveness is not visible.** Twice today WALTER logged a desk as UNKNOWN: in-process teammates are invisible to `ListAgents`, and ORCH_INFLIGHT gets its row at DELIVERY, not at spawn (MEMORY #41; OPEN DESIGN DECISION (u) in WALTER's LAST_COMPLETION). | DOORBELL_LOG 10/02 BRENT/BOND correction rows | Second natural duty: keep the live-teammate roster, writing the row at SPAWN. Every readiness decision (yours, WALTER's, the helper's) currently guesses at this. |

## Suggested trial measure
Measure **event → owner judgment latency**, not reports produced. Baseline from today: Yanbu strike Thu 10/01 (evening); first confirming press 23:29 ET 10/01; WALTER routed 12:33 ET 10/02; BRENT recorded RECORD-ONLY 12:35 ET; **FALCON judgment: still pending.** Secondary measures (from Will's own framing): items Will forwards by hand, and desks dark across an event that changed their work.

## ⚖️ The question that is Will's (please register it)
**Should an IMMEDIATE dispatch whose ACTION owner is a dark desk, in that desk's registered theater, authorize PROME to spawn that desk for one bounded session, even above the 4-desk cap or when the desk is Tier-2?**
- **If yes:** the helper becomes worth building, because a prepared assignment can execute without a Will round-trip.
- **If no:** the helper mainly tidies how requests reach Will, and the value case is weaker.
- **Test case:** FALCON on 10/02 (`-014`/`-016`/`-017`).
- **WALTER's position, and its stake:** WALTER recommends; it never spawns (IDENTITY). WALTER does benefit from a yes, since its doorbells convert to spawns more often, so weigh this view with that in mind.

## Not done / limits
- No design, cost estimate or prototype. The X-API intake idea from the same conversation is out of scope here.
- The intake-lateness figures come from five `gh run list` rows, not a longer history.
- WALTER's own 10/02 errors (Yanbu suspension scope `-016`; typed timestamps) are recorded in its LAST_COMPLETION. They're relevant only as evidence that owner review catches router errors when the owner is running.
