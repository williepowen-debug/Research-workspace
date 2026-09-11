---
name: finding_an_amendment_read_for_one_item_leaves_the_others_derived_from_the_original_live
description: "Consuming an amendment for the correction you were looking for does not update the OTHER decisions you derived from the original packet — they stay live on the queue as if the amendment never arrived"
symptoms: "a queue row for a question the desk already withdrew; a packet's row proven false by the time it was read; 'I read the amendment' beside a decision the amendment retracted; the coordinator registers what the amendment withdrew; DAEDALUS/NEXUS 'overtaken between authorship and delivery' in its consumption form"
metadata:
  type: feedback
---

An amendment is filed against a packet. The consumer reads it for the item it cares about (the correction it was told about), folds that in, and files the amendment as consumed. **Every other decision derived from the ORIGINAL packet is still on the rails, unreconciled** — the amendment withdrew or changed some of them, and nothing walked the list.

**Two instances in one day (2026-09-07):**
- PROME registered WQ-194 (LABOR's scoring-vintage question) from LABOR's charter packet AFTER LABOR's amendment §② had withdrawn it. PROME had read the amendment — for §① (the summons-gap correction), absorbed that into WQ-193, and filed it. Codex caught the stale row within minutes; PROME's rec on it would have published a book the amendment said was NOT AVAILABLE.
- DAEDALUS's packet to NEXUS carried a LABOR row that LABOR had already fixed between authorship and delivery; NEXUS re-measured the target before acting and 13 of 14 packets vanished.

**Why:** an amendment is read as a MESSAGE (what does it tell me?) not as a DIFF against the decisions already derived (which of MY rows does it touch?). The second question has no prompt: the queue rows do not know which packet they came from.

**How to apply:**
1. When an amendment arrives, list the queue/docket rows derived from the ORIGINAL packet and reconcile each one's disposition — before filing the amendment.
2. Authors: an amendment names the queue/docket items it affects (the packet-header rider Codex proposed 9/7; DAEDALUS 9/12 sitting + spine audit #13 candidate).
3. Re-measure the target before acting on any packet older than an hour (NEXUS's move).

Related: [[finding_directive_overtaken_between_authorship_and_delivery]] · [[finding_summary_section_merges_what_the_body_separates]] · [[finding_record_of_an_action_is_not_the_action]].

## ⭐ THE SELF-AUTHORED LIMB — nothing arrives to prompt the sweep (FALCON, 2026-09-11)

Every instance above has an **inbound** trigger: an amendment lands, and the failure is reading it narrowly.
This limb has **no trigger at all**, which makes it strictly harder to catch.

**The case.** FALCON ran a satellite analysis placing thermal hotspots on the Saudi East-West pipeline, then
ran its own population control, which **refuted the association** — the clusters sat at the population median.
It published that refutation at full strength, in the same report. Then, further down the same document, it
used **those same hotspots' persistence** to argue *"the outage is not a same-day reset"* — a claim about the
pipeline, resting on the link it had just killed. That inference went to BRENT as trade-relevant guidance and
sat there ~6 hours.

🔑 **A SELF-REFUTATION FILES AS A DISCHARGED OBLIGATION WHEN IT IS AN OPENED ONE.** Publishing the negative
result *feels* like the rigorous act — and it is — which is exactly the trap: **the rigour buys credibility
that the rest of the document then spends.** An inbound amendment at least announces itself and lands in an
inbox. Your own control announces nothing, creates no packet, and leaves no queue row. Both ends of the
sweep are you.

**How to apply — the addition:**
1. **When your own control kills an association, stop and GREP YOUR OWN DRAFT for every claim that depends on
   it** — before publishing, not at review. Write the refutation and the sweep as one act.
2. ⚠️ **The claims most likely to survive the sweep are the ones phrased about the SUBJECT rather than the
   instrument** ("the outage is not a same-day reset" does not contain the word *hotspot*). Search by
   DEPENDENCY, not by keyword.
3. **A disclaimed link is not a severed one.** Disclaiming it in §3 and reasoning across it in §5 leaves the
   inference live. If the link is dead, the downstream claim is dead — delete it or restate it on a surviving
   basis, and say which.
4. Four other claims in the same document failed the same way (a never-computed "36 hours" that was 25h21m
   sitting beside two real figures; non-detection read as proof of cause; a prediction state stated as a
   measurement). **A document that self-refutes once should be swept whole, not patched at the one spot.**

*Registered as FALCON LESSONS FAL-12. Found by external review (CODEX via Will), not by either desk's own
checks — neither the author's nor the recipient's. Encoded here rather than as a new slug: the load-bearing
structure is identical (a correction that does not travel to everything derived from it) and the difference is
the TRIGGER, which a named limb carries better than a split class would. Cousins:
[[finding_self_attack_defends_the_argument_not_the_apparatus]] (your attack list defends the ARGUMENT and is
blind to the APPARATUS — here the apparatus attack succeeded and the argument did not update),
[[finding_transfer_completes_only_when_the_receiver_encodes]].*
