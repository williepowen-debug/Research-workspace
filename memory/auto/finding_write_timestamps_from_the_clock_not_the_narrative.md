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
