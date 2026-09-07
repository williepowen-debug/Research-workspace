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
