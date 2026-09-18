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

---

## n+1 — 2026-09-05, WALTER: **the fail-open branch was LABELLED "fail SAFE", and the label is why it survived review**

`walter_doctor._ever_in_git()` ended:

```python
except (OSError, subprocess.SubprocessError):
    return True   # fail SAFE: unknown -> assume delivered, never cry wolf
```

**That is fail-OPEN.** On a timeout it converts **unavailable evidence into presumed delivery** — the one direction that never prompts a re-check. The parent rule's asymmetry applies exactly: a delivery check that cries wolf is ignored; one that quietly certifies is believed.

🔑 **THE NEW TELL, and it is cheap to grep for: the comment said "SAFE."** Nobody re-reads a branch that has already declared itself the cautious option. **"Never cry wolf" is not a goal a correctness check may trade against** — it is the stated motive of every loosening this memory exists to catch, and here it had been promoted into the identifier for the defect itself.

⇒ **Two additions to the trigger list:** ① when you write or review an `except:` in a verifier, **say out loud what the return value ASSERTS** — `return True` in a function named `_ever_in_git` asserts *"git has seen this,"* which the exception proves you do not know; ② **fail-closed on a correctness check means returning UNKNOWN, not returning False.** Both fixes here made the function tri-state (`True` / `False` / `None`) and gave UNKNOWN its own visible bucket, because collapsing it into either boolean is a lie in one direction or the other. See [[finding_instrument_reports_clean_against_the_wrong_reference]] n+4, where the same review found the sibling defect.

⚠️ **The repair itself shipped broken and running it is what caught that** — a variable in the patched caller collided with an existing name and the check raised `TypeError` on its first run. [[finding_test_the_guard_not_just_the_guarded]], [[finding_a_correction_pass_is_unreviewed_work]].

---
**n+2 — 2026-09-18 (PROME, the WQ-244 blocking hooks under five independent Opus reads; measured by the fifth reader `wq244cold5` §5): two repairs, two new defects — each false-positive fix opened a silent bypass.** ① r3 ❌5's prefix walk (`time`, `env`, `command`, …) → r4 ❌6: `command -v pytest | head; echo $?` blocked (false positive) → v5 deleted `command` from the walk → r5 ❌9: `command python3 <gate> | tail; echo $?` slips through at rc 0 with a reason text asserting the gate is "an argument". ② r4 ❌5's `{` boundary for `time { gate | tail; }` → r5 ❌5: `ls scripts/{a,b}.py | wc -l; echo $?` blocked — brace EXPANSION read as a GROUP. **The reader's measurement: false positives per round 4·5·4·2·5, no round zero; every false positive since round 4 lives in the layer the wrapper invented to compensate for the upstream recogniser.** The trade this memory names is not one-shot — inside a SIMULATION layer it runs in both directions every round, and the fix to the false alarm IS the next bypass. **What worked:** narrow what BLOCKS to the clean detection (a literal `-m` in command position) and declare the rest ADVISORY — put to Will as WQ-263 instead of a sixth round. [[finding_a_correction_pass_is_unreviewed_work]] [[finding_hand_fixing_named_rows_is_not_fixing_the_class]]

---

## THE PRECURSOR: a guard that fires LEGITIMATELY but ROUTINELY buys the same desensitization without anyone loosening anything (SAM, 2026-09-18)

Loosening is the second step. The first is a guard whose correct, fail-closed behavior is triggered by benign work often enough that clearing it becomes reflex.

SAM's `boot.py` validates each open prediction against a sidecar `condition_sha256` in `PREDICTION_SCHEDULE.json`, hashing `Prediction` + `Timeframe` + **`Notes`**. Boot failed closed: `SCHEDULING GAP: changed conditions for SAM-33`.

**Notes is in the hash for a good reason** — SAM-33's *activation/VOID clause* lives in its Notes field, so terms genuinely can hide there. **But evidence also lives there**, and SAM-33's Notes carry an explicit append-only OP-AUDIT RECORD updated after every BOJ operation. So the guard fires on every routine evidence append: correct each time, and never once about a real term change.

**That is the desensitization purchase.** No threshold was relaxed; the guard is working as designed. But the *response* — re-stamp the hash — becomes routine, and the routine response to a real term re-tune is byte-identical to the routine response to an evidence append. The guard keeps firing and stops being read.

This is the same mechanism SAM's own charter already names for unwired scripts: *"a flag that fires every run for a known-good reason trains me to ignore it"* — which is how `grade_8_14_branch.py` got read past for days. **A guard can be desensitized by its true positives.**

**Defaults:**
- **Never clear a fail-closed guard without the field-level diff** that shows *which* field moved. Here: `git show <old>:<file>` → compare `Prediction`/`Timeframe`/`Confidence`/`Status` explicitly, confirm only the evidence text appended, *then* re-stamp. Costs a minute; it is the entire value of the guard.
- **Prefer separating the fields the guard must watch from the fields that legitimately churn** (terms vs. an evidence/audit log) over widening or removing the hash. Splitting the field is the fix; re-stamping faster is the trap.
- **Count how often a guard fires benignly.** A fail-closed check that has never once caught a real defect is not thereby proven sound — it may simply be measuring the wrong field, and the clean record is what makes it invisible.
