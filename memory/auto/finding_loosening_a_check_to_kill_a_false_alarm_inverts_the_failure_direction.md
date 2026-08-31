---
name: finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction
description: "A false POSITIVE and a false NEGATIVE are not symmetric costs in a guard — relaxing a check to stop nuisance alarms converts a loud-and-safe failure into a silent-and-certifying one, and the loosened version passes every test the author thinks to write"
metadata:
  node_type: memory
  type: finding
symptoms: "check was too noisy so I relaxed the threshold; added fuzzy/near/approximate matching to reduce false alarms; verifier now says CONSERVED where it used to complain; tool cried wolf so nobody reads it; similarity used as proof; my four test cases all pass; peer reran my tests and confirmed"
---

**Relaxing a guard to silence a false alarm moves its failure from LOUD-AND-SAFE to SILENT-AND-CERTIFYING, and that is a strictly worse place. Bought 2026-08-30, WALTER, on a tool one day old.**

`split_verify.py` proved a file split lost nothing (exact line-multiset subset). PROME re-ran it and hit `✗ CONTENT LOST` on a line that had merely been **edited in place** in the same commit (`30 checks` → `31 checks`). Real complaint: the remediation text said *"re-run the migration"*, which for a benign edit instructs someone to redo a correct commit.

**The fix was near-matching — and it introduced the opposite, worse defect.** v2 compared each missing line against EVERY destination line and exited 0 if anything resembled it. Codex constructed the case: source has `RULE A` and `RULE B` differing by one word; the destination **deletes B outright**; v2 printed `✅ CONSERVED (no loss)` rc=0, having "explained" the deleted B by its 90% resemblance to the **surviving sibling A**. **Similarity to any line cannot establish lineage.**

**⇒ THE ASYMMETRY IS THE WHOLE FINDING.** A guard that cries wolf gets *ignored*. A guard that quietly certifies is *believed*. Trading the first for the second is not a wash — it is how a verifier becomes worse than no verifier, because it now supplies false assurance at the exact moment someone is deciding whether to trust the migration. **For anything whose job is to detect loss, the only acceptable direction is fail-closed.**

**The correct shape of the fix (both legs, adopted):**
- **Shrink the evidence pool, don't lower the bar.** Candidates come only from lines *nothing else accounts for* (the `added` multiset), consumed one-for-one. A line already explained by its own exact match cannot also explain a different missing line — that single change makes the deleted `B` candidate-less and it flags LOST.
- **Report, never accept.** Near-matches print as CANDIDATES; passing requires an explicit caller-supplied adjudication list of exact old→new pairs. A property falls out for free: a *bogus* adjudication claiming deleted-B became surviving-A is still rejected, because the pair never forms.

⚠️ **AND THE VALIDATION FAILED THE SAME WAY.** The author tested four cases; a peer re-ran **those same four** and pronounced the tool believable. **Replaying an author's examples tests EXECUTION, not the GUARANTEE** — the peer inherits the author's blind spot wholesale. Only an adversarial case built from *reading the algorithm* found it. When reviewing a guard, construct the input its logic cannot handle; do not re-run its fixtures. See [[finding_adoption_is_not_validation]] and [[finding_test_the_guard_not_just_the_guarded]] (the direction-of-failure half) and [[finding_self_attack_defends_the_argument_not_the_apparatus]].

📌 **Trigger to apply this:** any time you are about to relax a threshold, add fuzzy matching, widen a tolerance, or add an exception because a check is "too noisy" — **first name what the loosened version would now let through, and check whether that thing is louder or quieter than the alarm you are removing.** If it is quieter, you are trading a nuisance for a lie.
