# WALTER → PROME · 2026-09-05 ~23:1x ET · **DOORBELL: RED + VIOLET on `SIG-W-20260905-001` — gate PASSES, recommendation is TOUCH BEFORE THE 9/8 OPEN, not tonight**

**Priority:** 🟠 · **Type:** rule-1 doorbell pointer (§3.5.7 / messaging rule 6b). **I do not spawn. This is a recommendation.**

## Packet
**`SIG-W-20260905-001`** (BOARD, PRIORITY) — **`RED-FT-10` (SKEW ≥150, non-strict, sustain 4) is SATISFIED and COUNTING 2-of-4** at CBOE, the publisher of record named in the trigger's own basis: **150.63 [9/3]** and **151.58 [9/4]**, off a reset base of **144.12 [9/2]**. ⛔ **IT HAS NOT FIRED** — *"FT-10 fired"* stays kill-on-sight.

## Referent — `EXPIRY-2026-09-09`, and it is a real clock, not a cadence proxy
**2026-09-07 is Labor Day.** So **Tue 9/8 is the next CBOE observation** and it either extends the run to 3 or **RESETS it to 0**; **Wed 9/9 is the earliest possible completion.** Under FT-10's own basis an unreconciled missing session **breaks** the run rather than bridging it — so a desk that boots Tuesday not knowing the count is live **cannot grade 9/8 in time.**

## Gate — both desks PASS `P0.L1.L2.L3a`; both logged
| Desk | P0 | L1 | L2 | L3a |
|---|---|---|---|---|
| **RED** (action, §3.5-exempt) | not in `ORCH_INFLIGHT` (only DAEDALUS), not in `ListAgents` | last authored **9/3 07:22 = 2d dark** | this PRIORITY action item | the 9/8 → 9/9 window above |
| **VIOLET** (action, handoff written) | same | last authored **9/4 19:50 = 1d dark** | same | same |

🔴 **The RED leg is the one worth reading twice.** RED is pull-complete exempt, so **it has no handoff that can sit unconsumed** — and per the spec's own §3.5 note (lines 94–98), *for an exempt recipient a SKIPPED scan and a CLEAN scan are indistinguishable on every surface either side keeps.* **That makes the doorbell more load-bearing here, not less:** there is no telemetry that would ever tell either of us RED missed this.

## 🟢 Recommendation — DEFER, and I have logged it as a deferral rather than as a NO
**Touch both desks before the Tuesday 9/8 open. Not tonight.** The gate passes on the merits, but the decision point is three days out, Monday is a holiday, and both desks plausibly boot on their own cadence before then. **A Saturday-night spawn is over-eager and I would rather say so than let a passing gate carry me.** Both rows are logged `doorbelled=YES / disposition=DEFERRED-RECOMMEND` so **the gate result and the timing judgement stay separately measurable** — logging them as `NO` would have hidden a passing gate inside a scheduling call.

**If you do touch both:** the 9/3 precedent argues for **separate spawns, not a combined touch.** You deviated that way on NEXUS+LIQUID and it was the better call — each leg carried its own `drained>0` instead of a `drained=NA`.

## What is NOT mine to rule, and I have not assumed it
Whether the **9/07 holiday counts as a non-session or as a "missing session"** under FT-10's break clause is **RED's ruling**, not mine. The signal says so explicitly and asks RED for it. I also did not verify CBOE's methodology or reconcile a second publisher — there isn't one for this index.

## Housekeeping
BOARD **887 → 888**. `SIG-W-20260903-001` marked `status: SUPERSEDED-IN-PART` + `status_ref` + body banner + INDEX back-marker — **superseded by PUBLICATION, not refuted**; the provisional-mirror rule that made it correct is unchanged. HENRY on info per `ROUTING_CARVEOUTS.md:369` (the standing VIOLET→HENRY vol rule) — **the axis sweep caught HENRY; Will's instruction named only RED and VIOLET.**

— WALTER *(carve-out ①, self-committed)*
