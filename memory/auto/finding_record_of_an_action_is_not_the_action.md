---
name: finding-record-of-an-action-is-not-the-action
description: "A record ABOUT an action is not evidence the action happened — including your OWN record. A commit message saying 'routed to X', or a requester's note that an ask is 'still pending', both read as fact and both can be false. Check the TARGET artifact: the recipient's inbox, the asked-for file. n=2 in one session, both self-inflicted."
metadata:
  node_type: memory
  type: finding
---

**A record about an action is not the action.** This holds for other agents' records *and for your own* — the second is the one that gets through, because you trust your own commit messages.

**Two instances, 2026-07-27, both PROME's, ~5 hours apart.**

1. **Someone else's record.** CREED's memo said a REGINALD freeze-banner ask was *"still pending"* — 23 days open. PROME relayed it to Will and cited the root Data Hygiene rule at it. **REGINALD had satisfied it 18 days earlier** (`da82a095`, 7/09), and the banner was *better* than the ask required. The stale claim lived in **CREED's own records** (`LAST_COMPLETION.md`, `STATUS.md`), written 7/4 and never refreshed. Three hops, one unchecked predicate.
2. **My own record.** The HEARTBEAT re-base commit stated a VIX-COT decay finding was **"Routed to VIOLET."** No such packet existed. I had written the intent in a commit body and never created the artifact. Found only because I checked VIOLET's inbox before writing a follow-up — **while VIOLET was booting to mark a live position with a mandatory exit two days out.** The two available framings of that datum pointed in *opposite* directions, so the missing half was decision-relevant, not cosmetic.

**Why it survives every reader:** both records are *assertions in the voice of the system of record.* A commit message is written by the person who would have done the thing, at the moment they intended to; a requester's status file is written by the person who wanted it. Neither is updated by the event that would falsify it. Nothing in the pipeline re-checks them, so they propagate at full confidence.

**How to apply:**
- **Before re-raising an aged cross-agent ask:** `git log` the **target path**, not the requester's note. The requester's record of an ask is not evidence the ask is open.
- **Before citing your own routing/delivery as done:** `ls` the **recipient's inbox**. "Routed", "flagged to", "notified" in a commit body are intents until an artifact exists at the destination.
- **Highest-risk moment:** a *crashed or interrupted session*. Intent-language survives in commits; the artifact-creating step is what gets lost. After any unclean shutdown, re-verify every delivery the dead session claimed.
- **Cheap tell:** if the only evidence for X is a sentence written by whoever was supposed to do X, it is unverified.

Related: [[finding_never_received_is_not_doesnt_hold]] (a zero handoff count measures your routing history, not the other agent) · [[finding_dirty_path_means_in_flight_not_orphaned]] (the inverse error — absence of a commit is not absence of delivery) · [[finding_terminated_notice_can_precede_delivery]] · [[feedback_behavior_language_over_hash_pinning]] · [[finding_completion_stamp_skip_reads_as_current]] (CREED's complement, same session: a file whose NAME promises currency reads as current-and-wrong, not stale).
