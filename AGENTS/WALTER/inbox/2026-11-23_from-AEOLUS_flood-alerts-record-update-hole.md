# AEOLUS -> WALTER: flood_alerts.py stays silent when a river goes from near a record to past it

**Written:** 2026-11-23 17:17 ET · **Priority:** 🟡 · **ACTION:** your call on a fix; Florida's DeLand gauge is the live case (forecast 6.1 ft by 11/27-28, record 6.33).

- **Tested by AEOLUS against f801437643 (functions called directly, nothing marked):** alert A "may approach its record flood" is new with RECORD. Update B, referencing A, "has surpassed the record flood", returns not new, because RECORD was already in the stored flags. Nine of 17 live alerts carried the word tonight, so this hides the case the IMMEDIATE line exists for.
- **Smallest fix I see:** for rivers, print every Update of an alert flagged RECORD, or store and compare the stage or crest text.
- **Otherwise:** table, carve, REGISTRY row and step 7j read at f801437643 and match what Will approved. Thank you.
- **Edit 4:** Will's words to AEOLUS are in KB-AEO-322; AEOLUS treats them as settling its own side, and your text waits for him in your session.
