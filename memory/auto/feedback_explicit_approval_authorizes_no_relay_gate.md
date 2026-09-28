---
name: feedback_explicit_approval_authorizes_no_relay_gate
description: Will's standing instruction (2026-09-28) — his explicit approval authorizes the agreed work; a desk may check the committed wording of a relayed ruling, but PROME must not add another approval requirement merely because the ruling reached the desk by relay.
metadata:
  type: feedback
symptoms: "desk holding the install until Will confirms in its own session", "relayed ruling isn't enough on its own", "asked Will to re-confirm what he already ruled", "second approval step for a Will-gated surface after the word was committed", "messaging rule 3 hold on a ruling PROME already carries"
---

**Will, 2026-09-28 15:2x ET, verbatim:** *"Explicit approval from me authorizes the agreed work. Checking the committed wording is fine, but don't add another approval requirement merely because my ruling was relayed."*

**Context:** Will ruled WQ-241/WQ-321 in PROME's session (15:1x ET). PROME doorbelled CORAL with the verbatim ruling; CORAL held the install under messaging rule 3 because the Will-gated surfaces (a GATES letter, THESIS rails) had only a relayed word, and asked for the ruling in a committed artifact — which PROME had already committed (c0cfe7ba6) by the time the hold was raised. CORAL then verified at that commit and installed (8ce8ecb83). The hold was defensible; a SECOND gate on top of it would not have been.

**Why:** a ruling given to PROME and committed verbatim in `PROME/WILL_QUEUE.md` IS Will's word on the record. The relay chain is a delivery mechanism, not a dilution of authority. Adding "Will must confirm in your own window too" turns one decision into two and stalls the work he just authorized. This sits beside, not against, `[[finding_relayed_recommendation_is_not_an_approval]]`: that memory is about a REVIEWER's rec relayed through Will (a rec is still a rec); this one is about WILL's own ruling relayed through PROME (a ruling is a ruling once it is committed verbatim).

**How to apply:**
- On a Will ruling, PROME commits the verbatim text to the WQ row FIRST, then doorbells the owner with the commit hash. The owner's check is "does the committed row say this?" — never "has Will said it to me?".
- A desk that holds for the committed artifact gets the hash, not a lecture; a desk that asks for Will's separate confirmation after the hash is pointed at this memory.
- Reviewer findings (CATO etc.) relayed by Will remain recs until Will's own word — unchanged.
