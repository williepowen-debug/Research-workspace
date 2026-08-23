---
name: finding_transfer_completes_only_when_the_receiver_encodes
description: "A hand-off of OWNERSHIP has two halves and only the sender's half is self-motivated — the sender encodes TRANSFERRED and correctly stops, while the receiver has no trigger at all, so the item is owned by NOBODY and BOTH desks' own ledger checks pass clean because each correctly audits only its own book."
symptoms: "I routed it to the right owner · handed it off · registered it under their name · the row names them as owner · docketed it for them · both desks' checks passed clean · my ledger is correct, why is anyone still waiting · the date is right but nobody gets woken · I grepped my own desk and found no read-path · routing owed"
metadata:
  node_type: memory
  type: finding
---

**When ownership of a tracked item moves between agents, the transfer can silently fail to complete — and the gap is invisible to both parties, because both behaved correctly.**

The asymmetry is structural:

- **The sender's half is self-motivated.** It is holding a row it has been told is no longer its own. Encoding `TRANSFERRED-TO-X` and ceasing to score is the natural, immediate action, and it usually happens the same day.
- **The receiver's half has no trigger whatsoever.** *Nothing in the receiver's own files changed.* The row is not in their ledger — that is the entire problem, and its absence looks identical to "this row was never mine." The only prompt is a packet sitting in an inbox they may not open for days.

**Then the detection gap closes over it.** Each desk audits *its own* book, and on each book the state is CORRECT: the row is rightly absent from the sender's live set, and rightly not-yet-present at the receiver's. **No single-agent check can see it.** Catching it needs an instrument that spans both ledgers, or a third party holding the ruling.

**Measured (2026-08-20, REGINALD → WAL, prediction REG-15):** ruled 8/12, sender encoded `TRANSFERRED-TO-WAL` 8/13 and stopped scoring, receiver encoded **8/20**. **Seven days owned by nobody**, on a row whose resolving data was already available. Found by the *coordinator's* boot sweep — neither desk's own check flagged it, and neither could have.

**How to apply**

1. **Say "a transfer completes when the RECEIVER encodes."** Not when the ruling lands, not when the sender marks it transferred, not when the packet is committed. If you are the receiver, the transfer is *your* open obligation from the moment you learn of it.
2. **Receiving an ownership hand-off is mechanical-before-creative work** — encode the row into your book at the boot you learn of it, even if you cannot yet score it. An encoded-but-unscored row is owned; an un-encoded one is not.
3. **Senders: state the completion condition in the packet** — "this closes on YOUR encode, not mine." Cheap, and it converts the receiver's silent no-op into a named obligation.
4. **Coordinators: this is a class you must own**, because it is the one both endpoints are structurally blind to. Diff the ruling record against the receiver's ledger, never against the sender's.
5. **Generalizes past predictions** — any single-owner artifact that moves between agents (a gate, a watch row, a threshold, a catalyst, a card) has the same two-halves shape and the same one-sided trigger.

Related: [[finding_ownership_claim_is_last_to_move]] (stale ownership *declarations* surviving a move — the inverse: there the claim persists and is wrong; here no claim exists at all) · [[finding_record_of_an_action_is_not_the_action]] · [[finding_delivery_check_is_not_a_knowledge_check]] · [[finding_imperfect_level_to_the_right_owner_beats_a_perfect_one_to_nobody]]

**n+1, THE RESOLVED-NOT-DELIVERED FORM (SAM, 2026-08-23, self-reported at its orch-session closeout):** BOND asked SAM (8/18 packet) to verify the MOF monthly release date. SAM did the work — re-dated its OWN docket 8/31 → ~Fri 8/28 on 8/20, cadence-derived, correctly — **and the fix landed on SAM's surfaces and stopped there: the answer was never sent TO BOND.** Three days of a correct docket beside an unanswered ask. Harder to spot than the usual unverified-date miss because the owner's own record looked right throughout — every self-audit passes while the counterparty still holds the stale date. Delivered 8/23 with the re-confirmation (MOF publishes no forward schedule; n=2; 8/31 = likely slip). **Apply:** resolving an ASKED question on your own surfaces is the sender-half only; the transfer completes when the ANSWER reaches the asker (packet, not just your docket cell). At any ask-driven fix, the last step is addressed delivery — same two-halves shape as the parent finding, presenting as "my ledger is correct, why is anyone still waiting."

---

**n+2, THE ROUTED-AWAY FORM (BOND ↔ PROME, 2026-08-23) — and it inverts the parent finding's own assumption about who is at risk.**

BOND returned an ungradeable threshold to PROME with the words *"routed to PROME rather than left dormant."* PROME docketed it, mis-dated it, was corrected by BOND, and re-dated it correctly. **Then BOND grepped its OWN desk for a read-path to the corrected row and found none** — the row lived on `PROME/DOCKET.tsv` alone. **The date was now right and would have woken nobody on the owner side.** Both desks' checks passed clean, exactly as the parent finding predicts.

⚠️ **Two things make this sharper than the parent case.**

1. **The party who lost it was the RETURNER** — the one who most needed the wake-up, who knew precisely what it depended on, and who had written the words about not leaving it dormant. The parent finding frames the receiver as passively un-triggered; here the *sender* was the one left un-triggered, because routing an item away feels like discharging it. **Routing something to the right owner is the START of the transfer, not the end of your part in it.** Sibling: `[[finding_imperfect_level_to_the_right_owner_beats_a_perfect_one_to_nobody]]` — getting it to the right owner is necessary and still not sufficient.
2. **The registrar half is a real gap, not just inattention.** PROME registered a DOCKET row **naming a different desk as owner and routed nothing to that desk.** The W4 hand-off rule covers DOCKET → WILL_QUEUE (a catalyst producing a *Will*-action); **there is no symmetric rule for a DOCKET row whose owner is a domain desk.** "Routing owed by PROME" exists only as a prose habit inside the provenance field of some rows — a note, never an enforced step.

**Why no instrument caught it:** `docket_check.py` is **auction-only** (TreasuryDirect coupon auctions, CUSIP-keyed), so its `rc=0` is silent about every non-auction catalyst. **A clean auction check is not a clean calendar** — the same scope correction BOND had made to its own boot step 5 two days earlier, biting again on a neighbouring class.

## How to apply (n+2 additions)

- 🔴 **If you route an item away, build the receiver-side row in your OWN book before you consider it discharged** — a pointer, explicitly labelled a mirror, naming whose copy is authoritative. Un-owned beats double-owned only until the wake-up date; then both fail.
- 🔴 **Registrars: a ledger row naming a NON-SELF owner is an un-delivered packet until that owner has a read-path.** Registering under someone's name is not routing to them. The check is one grep of the owner's own docket/catalyst surface — run it at the touch that creates the row, not at the touch that discovers the gap.
- **Label the mirror at birth.** BOND wrote *"PROME's row is authoritative; if they disagree, mine is the copy to fix"* — which is what stops a receiver-side pointer becoming a second source of truth (`[[finding_owner_of_record_means_authoritative_not_correct]]`).
- **Three fields on one item, three independent ways to lose it** — this row lost the *quantity* (a threshold family with no instrument), the *schedule* (a date keyed to the wrong artifact, `[[finding_instrument_reports_clean_against_the_wrong_reference]]` n=10), and the *delivery* (no receiver-side row). Each was guarded by someone and none by everyone. **When an item passes between desks, audit all three; guarding the hard one predicts nothing about the other two.**
- ★ **The unifying shape across all three, worth carrying on its own: A CORRECT ACTION ON THE WRONG SURFACE READS AS A COMPLETED ONE.** The release ping was correct and stale; the date was correct and keyed to the wrong artifact; the row was correct and lived in one place. Every one of them looked done.
