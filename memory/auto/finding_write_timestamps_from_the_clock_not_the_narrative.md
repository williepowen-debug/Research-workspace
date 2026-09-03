---
name: finding_write_timestamps_from_the_clock_not_the_narrative
description: "A busy session's narrative clock drifts FAST (~2.5h in one morning); every written stamp comes from `date`, never from felt elapsed time"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f1c92371-68f1-4c6c-b922-9cbd6e8cc42c
  modified: 2026-08-20T15:01:19.038Z
---

**The failure (PROME 2026-08-20, BOND-caught; n=2 after the 8/17 "evening" mislabel):** PROME ran a 7-desk coordination morning on an estimated clock and drifted ~2.5 hours FAST — told a live desk "it's past 1PM" at 10:36 EDT, and stamped four committed ruling records with times progressively more wrong (~11:xx/~12:xx/~13:0x vs true commit times 09:16/09:29/10:17). The drift COMPOUNDS with activity density: each burst of work inflates felt elapsed time, and nothing inside the narrative ever corrects it.

**Why it matters more than a wrong label:** time-anchored instructions become false event claims. BOND's BND-17 carried a residual branch — "VOID if components don't publish within 24h of the auction" — and a grader taking "past 1PM" at face value could have resolved a live prediction VOID on the absence of data that was never due. The absence of a result is only evidence once the event has occurred ([[finding_record_of_an_action_is_not_the_action]] pointed at a clock).

**How to apply:** run `date` before writing ANY timestamp into an artifact (ruling records, packet stamps, session labels) and before issuing any "it's now past X" instruction to a peer. When correcting a wrong stamp already committed, anchor the correction to the artifact's own git commit time — it's ground truth that survives the narrative. Time-gate peers on EVENTS (the print publishing) rather than clock claims wherever possible.

**n+1, SAME SESSION AS A FLAGGING — the drift resumed within 90 minutes of being caught (PROME, 2026-08-23):** DAEDALUS's pilot review flagged F5(c): a commit git-stamped **11:25:59** cited Will's word at *"~11:4x"* — 20 minutes into its own future, on a **Will-gated provenance line where the timestamp IS the authorization record**. PROME acknowledged it, corrected the durable surface, and then **drifted again in the same session**: at a real clock of **12:21** it wrote "~13:2x" into a SCRATCH header and had already stamped two owner packets and a ruling record ~40-60 minutes fast. Caught only because the next `date` call happened to run before the closeout commit.

**Why acknowledging it does not fix it:** the drift is not a belief about the time, it is the *absence* of a reading — under load the narrative supplies a plausible-feeling stamp and nothing contradicts it. **A session that has just been told it drifts will drift again unless it re-reads the clock at each write.** Direction is consistently FORWARD (the felt duration of dense work exceeds the elapsed time), so stamps run early-to-late and a reader reconstructing sequence from them gets the ORDER wrong, not just the offset.

**Apply:** run `date` immediately before writing ANY stamp — not once per session, not "recently enough," per stamp. Commit messages cannot be amended (root Git Protocol 4b), so a drifted stamp there is permanent: the correction goes on the durable surface with the git timestamp named as the truth. **And check internal consistency across a batch** — 8/23's ruling record said rows were "registered ~12:1x, ruled minutes later" while its own header said ruled ~12:0x, i.e. registration after the ruling. Two drifted stamps in one document can invert a causal sequence that actually happened in the right order.


**n+1 — the peer's clock is narrative too (PROME, 2026-09-02 EVE):** twelve spawned desks reported in with `2026-09-03T00:xxZ` idle stamps; PROME wrote "~22:0x / ~22:1x / ~22:3x ET" on a HEARTBEAT amendment header, ORCH_LOG delivery cells, the WILL_QUEUE reconcile line and five packets — all ~1h ahead of the `NOW:` line (21:16 ET). The UTC stamp was *read*, so it felt like a clock reading; it was a conversion the session never did. Fixed on PROME surfaces at closeout (a second correction commit on HEARTBEAT — the two-correction stop tripped); packets stand as written. **Apply:** the only clock is the `NOW:` hook line or `date`; a timestamp arriving inside a message — a peer's, a tool's, a `Z`-suffixed idle notice — is data about the sender, never the time you write.
