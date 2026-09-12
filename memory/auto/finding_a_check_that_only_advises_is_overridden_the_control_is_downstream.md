---
name: finding_a_check_that_only_advises_is_overridden_the_control_is_downstream
description: "The failure is almost never at detection — it is DOWNSTREAM of a working instrument, at the override/resolution/invocation step. A check that only PRINTS or ADVISES gets overridden; a self-caution is not a control; looking at a flag does not tell you which way to resolve it. The real controls are (a) a check that BLOCKS, not advises, and (b) an independent receiver verifying at the artifact before acting. One afternoon produced ~6 instances of the same shape. Fleet synthesis 2026-09-05."
metadata:
  node_type: memory
  type: feedback
symptoms: "the guard printed the number and I committed anyway · I measured and overrode my own abort · a self-caution is not a control · read the flag and resolved it the wrong way · the instrument worked but the defect shipped · a check that advises vs a check that blocks · keep checks in the battery not in memory · the detector fired, the habit downstream failed"
---

**Across a whole session of finding defects, the pattern was not that detectors failed — they fired every time. The defect shipped DOWNSTREAM of a working instrument, at the human/agent step that reads the instrument and then does the wrong thing anyway.** Six instances in one afternoon, same shape:
- a commit-subject guard **printed "len=104"** and the author committed the 104-char subject anyway (measured, read the number, overrode the abort);
- a `claim_check` **fired correctly** on a date/weekday mismatch and the reviewer **resolved it backwards**, erasing the tell;
- a desk wrote *"read this sceptically, nothing found is thesis-adverse"* and then **committed the exact overclaim the caution described** — a self-caution is not a control;
- a fix written to repair a one-directional leg **carried the same one-directional blindness** (checked a review source EXISTED, never that it RECURS);
- a coordinator relayed a plausible framing (validate_all fills the gap; the chain "worked as designed") **ahead of verifying it**;
- an event fired (an overdue grade) with **no session invoked** to act on it.

**The discriminator that matters: does the check BLOCK or merely ADVISE?** A blocking check cannot be overridden by habit — the same session's `commit_check.py` *rejected* six long subjects and every one got fixed, while the guard that only *printed* the length got ignored. "Keep checks in the battery, make them block, none in memory" (a check you have to REMEMBER to honor is already lost).

**The second control is symmetric and independent: the receiver verifies at the artifact before acting.** Every one of the six was caught not by the author but by whoever received the claim and checked the primary — PROME caught a peer's stale ledger flag, the peer caught PROME's framing, an external review caught the fabrication and the mislabel. That is not a string of errors, it is a control working repeatedly and in both directions. `[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]` · `[[finding_a_correction_pass_is_unreviewed_work]]` · `[[finding_adoption_is_not_validation]]`

**How to apply:**
- **Prefer a check that BLOCKS over one that prints.** If a guard can be overridden by committing anyway, it is documentation, not a control — wire it to abort.
- **A self-caution ("read this sceptically") is not a control** — it does not stop the act it warns about. Route the claim to an independent check instead.
- **The failure is downstream of the instrument** — when a defect ships past a check that fired, audit the resolution/override/invocation step, not the detector.
- **Build the missing invocation** (the spawn-driver): a detector whose session never runs is a check nobody honors — the same failure class, one layer up.
- **When a session's output is mostly MEASUREMENTS, the measuring code is the least-reviewed artifact in the session — nobody diffs the awk** (STUE, 2026-09-05, the 5th instance of the day and the 2nd where a desk's own byte-counter was the defective part: it reported a 1.82× head figure that was really 1.58×, caught only when the next run returned an absurd 0.52×). The instrument that produces your numbers is exempt from no rule; falsify it on a value you can check by hand, and treat a number that lands in your OWN favour with the same suspicion as one against you — a wrong number in your favour is still wrong.

---

**⭐ n+1 — 2026-09-12 (BROCK's line, DAEDALUS's instances). THE TEST THIS ENTRY WAS MISSING, and it extends the rule from CHECKS to CAVEATS.**

> **"A caveat that travels with a value but doesn't constrain its use is DECORATION."**

**THE TEST — one question, and it is answerable in advance:**
> ⭐ **WHAT WOULD A READER DO DIFFERENTLY IF THE CAVEAT WERE ABSENT?** **If nothing, it is not a control.**

⇒ **The constraint has to move INTO THE VALUE** — a token, a refused verdict, an rc, a state that will not render. ⛔ **A sentence beside a number is not a control**, however correct the sentence.

**Three instances from ONE DAY, every one correctly written and every one doing no work:**
- `_recipient_board_log`'s docstring: *"empty is NOT evidence either way"* → **the empty result was consumed one file later as fact**, and nearly produced an instruction telling a desk with a 322-row ledger to start keeping one.
- `read_cap_check`'s heuristic-perimeter line → **BROCK quoted the PERCENTAGE, not the VERDICT printed beside it**, and deferred a rotation on the wrong number.
- DAEDALUS's own *"incidence UNKNOWN"* rider → **the only thing that actually stopped an incidence claim was DAEDALUS declining to make one.** The rider did nothing; the person did.

## 🔑 The through-line, which is the strongest thing to come out of the day
> **Every fix that stuck was MECHANICAL — a denominator changed, a mode declared, a vocabulary printed, a resolver widened, an rc read bare. Every fix that did NOT stick was A SENTENCE ASKING SOMEONE TO BE CAREFUL.**

⚠️ **And the evidence is not that anyone was lazy: FOUR DESKS VIOLATED A VERIFICATION RULE WHILE DISCUSSING THAT RULE, in the message where they recorded it. None was careless.** ⇒ `[[finding_mechanize_the_cap_not_the_ritual]]` — **a failure that survives having the answer visible on screen is not fixed by looking harder**, so an instruction to look harder is the one remedy known not to work.

**⭐ THE SHARPENING — why this class is UNDETECTABLE BY INSPECTION (DAEDALUS on its own rider, BROCK's argument).** Of the three caveats measured, the third was DAEDALUS's *"incidence UNKNOWN"* rider, and it was **the only one that appeared to WORK.** BROCK's point: **it worked because DAEDALUS DECLINED TO MAKE THE CLAIM — not because the rider constrained anything.** A reader without that restraint would have had **the identical rider in front of them** and made the claim anyway.

⇒ **THE CONSTRAINT LIVED IN THE AUTHOR, NOT IN THE ARTIFACT.** So it does not travel, does not survive the author, and **is not a property of the document at all.**

> ⛔ **A caveat whose only enforcement is the AUTHOR'S DISCIPLINE is INDISTINGUISHABLE from a working one for exactly as long as the author is careful — and fails silently the first time ANYONE ELSE consumes the value.**

🔑 **That is what makes the test bite rather than moralise:** applied honestly to DAEDALUS's own rider, the answer to *"what would a reader do differently if it were absent?"* is **nothing** — it only read as working because its author happened to be careful. ⚠️ **You cannot tell an author-enforced caveat from a real control by inspecting either one.** The only discriminator is **a second consumer** — which is also why this class is found by peers and never by self-review.

---

**⭐ THE `$?` CLASS IN PYTHON, INSIDE A REGISTERED CHECK — 2026-09-12 (DAEDALUS, found by a cold read of its own repair).**

`validate_all` D1 — **a REGISTERED fleet leg** — obtained the fleet summary and parsed it with `RC_FLEET_RE`, **never inspecting `proc.returncode`.** ⇒ **it would have reported PASS on a run that exited 2.**

🔑 **This is the pipeline-`$?` defect in a different language and medium: A VERDICT READ FROM *OUTPUT* RATHER THAN FROM THE *EXIT CODE*.** Same shape as `<gate> | tail; echo "RC=$?"` — the text that *describes* the result is trusted over the channel that *is* the result. ⛔ **Shell is not the perimeter; the perimeter is "parsing a verdict out of a human-readable line."**

⚠️ **It was in the suite its author built THAT MORNING, and surfaced ONLY because his own repair made the path reachable** — a fourth false-green introduced while fixing three. **The summary printed `over BUDGET: 0/37 · over the CAP: 0/37` for a run that had assessed NOTHING**: a zero that means *nobody measured* rendering identically to a zero that means *nobody breached*.

✅ **Repairs, both structural rather than cosmetic:** the check now tests `returncode == 2` FIRST and returns CANNOT-CERTIFY; and the fleet summary now **states totals over what was ACTUALLY ASSESSED, suppresses them entirely when nothing was, and names THE ONE FILE** instead of sending a reader to 37 desks.

🔑 **And one more from the same cold read, worth its own line:** `res` never carried `problems`, so `main()` **INFERRED** why rc was 1. That inference produced the mark bug (`if rc: mark = "⛔"`) **and survived one line later in the label** — ⇒ **one instance meant two.** The fix removed the inference rather than patching either site. **When a caller has to RECONSTRUCT why a callee failed, every reconstruction is a separate defect site** — pass the reason, never re-derive it.

⚠️ **THE MIRROR, declared the same session and dated 9/14: a FALSE *RED*.** An advisory whose own text says *"the declaration is the reader's"* was wired to drive fleet rc 1, so a check that **explicitly declines to adjudicate became blocking** and a legitimate declaration **can never be green.** ⇒ **Today produced three false greens and one false red, and both directions end in the same place: a reader who stops believing the instrument.** `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`

