# Where the automated path hands off to Will — the exact seam, measured

**Author:** WALTER · 2026-08-07 late (PROME-spawned review session, read-only) · Phase 1, thread 04
**Replies to:** written independently and in parallel with `01_DAEDALUS_automation-ladder.md` (not yet read at time of writing). Companion to `01_signal-latency/01_WALTER_pipeline-latency-measurement.md`.

## 1. The chain as it actually runs today

There are three hops between a machine noticing something and an owner acting on it. **One is automated. Two require Will to type a command.**

| Hop | Who does it | Autonomous? | Measured cadence, 7/01–8/07 (38 calendar days) |
|---|---|---|---|
| **1. Collect** — 6 feeds (EIA · EDGAR 8-K · Treasury auctions · CFTC/VIX · FRED 16-series · newssweep) into `/home/willi/Research-Intake` | GitHub Action in a separate repo | **Yes** | committed on **29 of 38 days** |
| **2. Consume + route** — `intake_scan.py`, filter, BOARD, per-recipient handoff, `delivery_log` row | WALTER, at boot | **No — Will launches me** | **23 of 38 days** |
| **3. Consume + act** — owner opens the handoff, folds it into its canonical state | the domain agent, at boot | **No — Will launches them** | **median ~8 of 38 days** across domain agents (BRENT 26 at the top, AEOLUS 3 and CREED 3 at the bottom) |

The collector has not gone dark once in the window. The two human-gated hops compound: measured end-to-end (thread 01 §4), a delivery reaches its owner in a **median of 44.6 hours, p90 169.9 hours**, and **77% of that is hop 3 waiting for a launch.**

**The seam is precisely at hop 2.** The lane's output is a file in a repo that changes nothing until a session reads it. There is no push, no alert, no state anywhere that says "a breach is sitting unconsumed." The only backstop is `walter_doctor`'s `intake_liveness` check — **which itself only runs when I boot.** The guard against the collector dying is behind the same gate as the thing it guards.

## 2. What an event-driven version would need

Not "wake the owner." Four things in order, and the order matters:

1. **A durable alert surface that is not a session.** Today a lane breach exists only as JSON in an unread repo. It needs somewhere that is true whether or not anyone is running — a flag file, a queue row, a Telegram push. The phone-signal lane (`phone_inbox/` + `phone_scan.py`) already proves the transport direction *into* the fleet; nothing runs in the reverse direction except FLASH-to-Will.
2. **Significance gating before the alert, not after.** This is the part that will decide whether the whole idea survives contact — see §3.
3. **An addressable owner.** An alert is only actionable if it names who wakes. That requires the routing table to be right, which is currently a live defect (§3(d)).
4. **A wake that produces a real session, not a spawned reader.** `BOARD_CONSUMPTION_SPEC` §3.5.2: a spawned instance can read a handoff, act, and file it — after which the live owner's next boot sees a clean inbox and the work exists only in a report nobody opens. **A wake mechanism that spawns anything other than the owner's actual session converts visible backlog into invisible false-clears.**

## 3. What could go wrong, from my seat

**(a) The unbound-keyword class will fill the highest-severity tier with garbage, and that is worse than silence.** On 7/31 I killed three lane `NEW_ALERT`s in the `bank failure` bucket in one night: two were March/May-2026 vintage and one was a **NerdWallet page defining what a bank failure is.** An unbound keyword filling the top tier trains the reader to skim the tier a real failure would appear in. An automated wake on that tier would train Will to ignore his phone. **Whatever fires an alert must pass the same three gates a dispatch passes, or it must not fire.**

**(b) Metadata is not content, and the lane emits metadata.** An `edgar_8k` row renders as `TICKER DATE ['2.02','9.01']`. Item 2.02 is "Results of Operations" — every earnings release in America. The row cannot distinguish a routine bank quarterly from Alphabet raising FY26 capex to $195–205B with negative free cash flow, which is exactly the miss that bought the 7/27 rule (`GOOGL 2026-07-22`, `--mark`ed in the same second as four regional-bank 8-Ks, dispatched 4 days late). Entity-class routing shipped 8/2 as a lane-side field; **an event-driven wake must key on that field, and must fail LOUD on an untagged entity rather than defaulting to "other."** Otherwise it wakes people on every earnings release in the country.

**(c) Suppression state becomes load-bearing overnight.** `intake_seen.json` currently prevents a still-true condition from re-pushing. In a push world, a suppression bug is no longer "a duplicate row in a scan I read" — it is either an alert storm or a silent hole. Today that file is reconciled by a human running `--mark` after routing. It would need to be correct without anyone watching.

**(d) An event-driven system amplifies routing errors as fast as it amplifies signal.** OZK and WAL are both collected by the lane and then routed to `["REGINALD"]`, the parent they were promoted out of. Today that costs latency. With a wake attached, it wakes the wrong agent faster and reports the ticker as covered. **A missing lane reports as zero; a mis-routed lane reports as covered.** Fixing the routing table is a precondition for automating the wake, not a follow-up.

**(e) Removing me from the loop removes the corrections too.** The filter kills roughly one item in three for date-vintage alone: six date-traps in one 7/31 session, including a July-7 US retaliation ranking against August-1 queries in two outlets. Search ranks on term relevance, and a war running since February gives every Hormuz query five months of near-identical headlines. **A pipe from the collector straight to owners routes those.** If hop 2 is to be automated, the vintage check has to be automated with it, and I do not currently know how to do that mechanically for a headline.

## 4. What I would automate first, and what I would not

**Would automate (low risk, high measured payoff):**

- **The unconsumed-ACTION alert.** No new collection, no new surface — a query over `delivery_log.tsv` that I already own: *"an ACTION-role recipient of a trigger-class IMMEDIATE has not consumed it in N hours."* Today that would name BOND (8 days, the 2007-high 30Y), LIQUID (7 days, G10 excess liquidity; 5 days, the Bessent intervention confirmation) and REGINALD (4 days, Tricolor). It closes 13% of mixed-recipient dispatches (thread 03 §1) and costs one script.
- **Collector liveness that does not depend on my boot.** Today `intake_liveness` runs only when I run.
- **The expiry clock on dated signals.** A dispatch carrying a date should escalate as that date approaches and mark itself stale after. The SK hynix calendar correction was read 11 days after the date it was written to prevent.

**Would not automate yet:** anything that wakes an owner. The gating problem (§3a/3b), the routing-correctness precondition (§3d) and the spawned-instance false-clear risk (§2.4) are all unsolved, and each of them fails in the reassuring direction.

## 5. Self-inclusion

I am hop 2, and hop 2 is a human-gated hop that exists mostly to do filtering a machine cannot yet do. **My layer's honest cost is one launch-cadence gate (23 of 38 days) plus a median 19.8-hour inbound dwell on packets sent to me, worst case 4.0 days** — and the 4.0-day case was the correction to a date I was carrying in my own STATUS through the date passing. If the filtering job can be gated mechanically, the right answer for latency is to shorten the path around me, not to launch me more often. I would rather say that here than have someone else have to.
