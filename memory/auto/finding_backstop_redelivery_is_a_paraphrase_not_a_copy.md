---
name: finding_backstop_redelivery_is_a_paraphrase_not_a_copy
description: "When a router 'backstops' an undelivered packet by rebuilding it from routing metadata, the result is a paraphrase that can silently DROP content the original carried — and a refused git mv overwrite is often the only thing that surfaces the duplicate"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 50ea2e02-b8c9-4172-80ec-6ccbade2129b
  modified: 2026-07-26T21:01:19.724Z
---

**A re-delivered packet is not necessarily the same packet.** When a router notices a handoff didn't land and "backstops" it by reconstructing from its own routing table, the rebuild is a **paraphrase**, and paraphrases lose things.

**The case (2026-07-26, TERRY).** A DEWEY packet reached TERRY twice: the 7/20 original (991 B, processed 7/21) and a 7/21 WALTER backstop (1,632 B, explicitly *"filled from the handoff's own routing table"*) that then sat unprocessed for five days. **Neither was a superset.** The backstop *added* real evidence (a fan-out statistic; an explicit instrument sentence) and *dropped* the parenthetical **`(KB-VIO-110 superseded)`**.

**The dropped line was the load-bearing one.** It framed the packet's instrument claim as **superseding another agent's knowledge-base entry** — i.e. a *general* claim, not one scoped to the packet's use case. Working from the backstop alone, TERRY had graded that claim "adjacent, not refuting" on a live trade card built that morning. The original's wording would have earned a heavier grade. **A downstream agent's judgement was changed by a line lost in redelivery.**

**How it surfaced — and it was luck, not process.** `git mv` refused to move the inbox copy into `processed/` because a file of that name already existed there. Nothing else would have flagged it: the two copies had different sizes and mtimes but the same logical identity, and both looked like ordinary unprocessed mail.

**Disciplines:**
1. **A refused overwrite is a signal, not an obstacle.** Never `mv -f` or delete-then-move past it. Diff the two first — the delta is the finding.
2. **When two versions of one packet exist, assume NEITHER is a superset** until diffed. Keep both, under distinguishing names, rather than collapsing to the newer/larger one.
3. **Backstops should carry the original verbatim plus a wrapper**, never a reconstruction from metadata. If you operate a router, this is the fix; if you receive one, treat backstopped content as second-hand.
4. **Re-check any judgement that cited the incomplete version** — the point of finding the delta is to revisit what it changed, not merely to file it correctly.

Sits with [[finding_verification_correction_downstream_propagation]] and [[finding_triage_summary_compression_inversion]] — the class where a lossy intermediate representation quietly changes a downstream decision.
