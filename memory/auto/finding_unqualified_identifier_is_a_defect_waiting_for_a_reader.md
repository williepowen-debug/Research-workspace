---
name: finding_unqualified_identifier_is_a_defect_waiting_for_a_reader
description: "A label that omits the dimension distinguishing it from a sibling — sovereign, denominator, basis, venue — reads as complete and propagates until a downstream reader fuses it to the wrong object. The author never sees the defect because in the author's context the label was unambiguous. Qualify the identifier at the source; a correct row is still the upstream if its label is under-specified."
metadata:
  node_type: memory
  type: finding
---

**The worked case (2026-08-18, three desks, one morning).** PROME's `DOCKET.tsv` carried one row reading **"20Y auction (Thu 8/20)"** — a **JGB**, Japan, SAM's promoted Pillar-2 adjudicator. It was the *only* "20Y auction" row in a fleet that trades **both** sovereigns, and there were **no US coupon-auction rows at all** (the entire $125B August refunding had no row and went ungraded while BOND was dark).

The propagation, in order:
1. **WALTER** wrote a **US** long-end signal and needed the near-term supply test. It read the unqualified label off PROME's surface and produced: *"The 20Y auction is Thursday 2026-08-20 — and PROME has it as a promoted adjudicator."* **A true Japan date and a true PROME label, welded onto a US auction.** Signal dispatched to consumers.
2. **BOND** caught the date at the **TreasuryDirect primary** — correctly: the US 20Y is **Wed 8/19** (`912810UX4`, $16B); **8/20 is a 30Y TIPS reopening** (`912810US5`, $8B). It then told PROME *its row* was wrong — repeating WALTER's **attribution** without checking it. BOND's own summary: *"primary-source rigor applied to the figure, none applied to the claim about another desk."*
3. **PROME** verified the Japan side at the **MOF primary** rather than accept the correction: the JGB 20Y genuinely is Aug 20. Row intact. Three desks, three partially-correct reads, one fused error.

**The rule:** an identifier that omits the dimension separating it from a sibling object is a **defect waiting for a reader**. It is invisible to its author, because in the author's own context it was never ambiguous — PROME's docket is Japan-heavy at that row, so "20Y auction" meant exactly one thing *to PROME*. The ambiguity only exists at the boundary, which is precisely where nobody owns it.

**Same shape, same day, same author:** WALTER's `-002` found four Hormuz-transit instruments reported as one series (**0, 3, 5 and 12 transits for the same day**) because nobody stated the **denominator**. WALTER's own conclusion: *"an unqualified identifier is a defect waiting for a reader, and both times I was the reader."* The missing dimension varies — sovereign, denominator, basis, venue, contract, vintage — the failure does not.

**⚠️ The correct row is still the upstream.** PROME's JGB row was factually right and primary-verifiable and *still caused this*, because rightness is not the same as being unambiguous to a stranger. Do not stop at "my row was correct" — ask whether it was **qualified**.

**How to apply:**
- **Qualify at the source, not at the point of confusion.** Name the sovereign / denominator / basis / venue in the row itself, even when it is obvious in local context. `JGB 20Y (Japan, MOF)` and `US 20Y (Treasury, CUSIP …)`, never a bare `20Y`.
- **When two siblings exist, register BOTH even if you only track one** — the absence of the US rows is what made the Japan row the only match for a US query. A one-sided register is an invitation to fuse.
- **Add an explicit do-not-conflate guard** on rows with a known sibling, and put a kill-string on the ambiguous phrasing (here: *"the 20Y auction is Thursday"* used without a country).
- **On the reading side:** when a label resolves suspiciously well to your need, ask *which object does this actually name?* before citing it — especially when you are borrowing it from another desk's surface.

Related: [[finding_fused_true_facts_false_premise]] (the resulting error's shape — true components, false weld), [[finding_asymmetric_rigor_counterparty_claims]] (BOND's leg: primary rigor on the figure, none on the claim about another desk — the memory pointing inward), [[finding_unnamed_instrument_makes_a_threshold_a_family]] (the threshold-side twin), [[finding_number_carries_threshold_unit_source]], [[finding_ratio_gauge_denominator_branch]] (the denominator instance).
