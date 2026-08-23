---
name: finding_grading_a_disposition_on_a_book_you_do_not_own
description: "A position's disposition inferred from the tape is a claim about a book you cannot see — the close tells you what an option was WORTH at expiry, never whether it was still held; flag the expiry, never grade it, and the failure is invisible because a fabricated $0 on a lapsed put looks exactly like the truth"
symptoms: "peer says my position lapsed worthless; expiry passed so I marked it $0; the strike finished OTM so the outcome is zero; graded a position off the closing price; a P&L of zero that nobody entered; ledger says LAPSED but the position was sold; both desks' records look internally consistent"
metadata:
  type: finding
---

**A disposition derived from the tape is an inference about a book the inferring desk cannot see.** The close tells you what a contract was *worth* at expiry. It tells you **nothing about whether it was still held** — and those are different questions that produce the same-looking answer.

**The instance (WAL desk, 2026-08-23).** A peer flagged that `WAL $77.5P Aug-21 ×1` had expired, computed correctly that WAL closed **$79.67 [Fri 2026-08-21]** so the strike finished **2.72% OTM**, and concluded: **LAPSED WORTHLESS**. The arithmetic was right. **The position had been SOLD on 2026-08-18, three sessions earlier**, on the operator's own in-session word — recorded in a relayed exchange and a discrepancy row on the position-mirror surface, **neither of which is a surface the flagging desk reads.**

**★ Why this class survives: both desks' own checks pass clean.** The peer's tape read is correct. The owner's ledger is correct. **Only the join is wrong**, and neither side owns the join. Cf. [[finding_transfer_completes_only_when_the_receiver_encodes]] and [[finding_inherited_defect_propagates_though_both_ends_act_correctly]].

**★★ Why it is worse than an ordinary wrong number: the error is invisible forever after.** Accepting the grade would have written *LAPSED, P&L $0* for a leg **sold at an unknown price on an unknown date**. **A $0 on a lapsed OTM put is exactly what the truth looks like** — no reviewer, reconciliation or staleness check flags it, because nothing about it is anomalous. A fabricated zero standing where an honest unknown belongs is unrecoverable without a broker record. *(Cf. [[finding_partial_record_written_as_final_never_heals]].)*

**How to apply:**
- **Flag the expiry; never grade the disposition, on a book you do not own.** "Your dated leg passed its expiry, please dispose it" is the whole message. Adding "⇒ it lapsed" converts a correct flag into a defect. *(The flagging packet here said, verbatim, "I have NOT marked it and I will not — this is a flag, not a write-back," one paragraph below the LAPSED verdict. The right rule was already written; it just wasn't applied to the sentence above it.)*
- **As the OWNER receiving such a flag: resolve it at your own canonical file BEFORE accepting the packet's conclusion.** Reading your own ledger first is what separates a correct record from a fabricated one, and it costs one file read.
- **Grade disposition and P&L SEPARATELY — they resolve on different instruments.** `DISPOSITION RESOLVED = SOLD (operator's word) / P&L UNRESOLVED — pending broker confirm` is a complete, honest row. **Never infer one half from the other**, and never let "the position is closed" quietly become "the P&L is zero."
- **An honest UNRESOLVED beats a plausible guess.** A row that says *pending broker confirm* gets reconciled; a row that says *$0* never gets looked at again.
- Position truth is off-repo: **the operator's word about his own book outranks any tape-derived inference** — no matter how clean the arithmetic.

Distinct from [[finding_record_of_an_action_is_not_the_action]] (there the record and the action diverge; here two correct records answer different questions). Related: [[finding_exact_level_authenticates_a_wrong_direction]] — an exact, verifiable figure ($79.67, 2.72% OTM) stops anyone checking the claim attached to it.
