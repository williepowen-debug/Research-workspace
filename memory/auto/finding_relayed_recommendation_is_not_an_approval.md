---
name: finding_relayed_recommendation_is_not_an_approval
description: a reviewer's recommendation relayed through the operator is still a recommendation — gated surfaces need the operator's own word, and reviewers who phrase advice as "rulings" make the two indistinguishable
metadata:
  type: feedback
---

**A recommendation does not become an approval by passing through the operator's hands.**

**The instance (2026-08-05, roster migration).** Root `CLAUDE.md` is auto-injected into every agent's boot context, so Will had ruled its edit a **named, Will-gated step**: *"PROME may packet the needed mirror edit, but should not silently move root canon."* PROME drafted it and held. Then RAV — the QC reviewer — twice phrased its own opinions as rulings: *"TERRY ruling stands: DOMAIN ACTIVE"* (before Will had ruled TERRY at all; it was **PROME's** recommendation RAV was agreeing with) and *"Root mirror ruling from RAV: approve PROME's draft."* The second arrived **inside a Will relay**, where it read almost exactly like a decision.

PROME held anyway and asked for one word. Will gave it, and the edit took two minutes.

**Why holding was right even though the answer turned out to be yes:**
- The substance was never in doubt — PROME agreed with RAV's read and had authored the draft. **Agreeing with advice is not the same as being authorized by it.**
- Applying it would have set the precedent *"a reviewer recommendation relayed through the operator counts as approval for gated surfaces."* That precedent, not the one sentence, is the cost.
- It would have contradicted PROME's own objection raised an hour earlier about exactly this vocabulary — and an inconsistently-applied gate is worse than no gate, because nobody can predict when it binds.
- RAV's own phrasing hedged (*"when you're ready"*), so it was not even asserting the gate was passed.

**Why the vocabulary matters more than it looks.** A handed-context reviewer (RAV runs on Codex, Will-driven, loads no `CLAUDE.md`) has no way to feel the difference between "I recommend" and "it is ruled" — nothing in its context marks which surfaces are gated or who holds the gate. So the drift is structural, not careless, and it will recur with any reviewer wired the same way.

**How to apply:**
1. **For any gated surface, require the gatekeeper's own words in their own voice.** A relay of someone else's endorsement is input to the decision, not the decision. Asking a redundant question costs seconds; a wrongly-assumed approval on auto-injected canon reaches every agent at every boot.
2. **Read relays for whose voice is speaking.** *"RAV recommendation: approve X"* is the operator forwarding advice; *"approve X"* is the operator deciding. The words are adjacent and the authority is not.
3. **When a reviewer calls its own advice a ruling, say so plainly and early** — it is a wording fix, not misconduct, and the substance may still be excellent (RAV's was, and it caught a real PROME defect the same session).
4. **Weigh the advice fully while refusing to be authorized by it.** Holding a gate is not disagreement, and should be stated in a way that makes that obvious.

Related: [[feedback_audit_packet_before_approval]], [[finding_record_of_an_action_is_not_the_action]], [[finding_proposed_rule_must_be_canon_tested]] (same migration, same class — governance text acquiring authority nobody granted it).

**Standing rule (Will 2026-09-27 22:58 ET, "Ok approved", adopting CATO's wording):** *CATO's recommendations are advice unless I adopt them. When I say "go," "approved," "do this," or otherwise clearly instruct you to execute the pasted scope, that is sufficient authorization. Proceed through the agreed work without asking again. If my intent is genuinely ambiguous, ask once and name the ambiguity.* Pasting reviewer text without comment usually means "examine this", not "execute it".
