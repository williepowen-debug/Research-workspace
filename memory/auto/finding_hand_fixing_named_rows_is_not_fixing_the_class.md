---
name: finding_hand_fixing_named_rows_is_not_fixing_the_class
description: "When a reviewer names N defective instances, fixing those N by hand leaves the class intact — and you cannot tell, because the named ones are now clean. Mechanize the fix instead; the check routinely finds instances the reviewer never named."
symptoms:
  - "I fixed the three rows they flagged"
  - "addressed all review comments"
  - "the reviewer's findings are all resolved"
  - "corrected at the headline but the ledgers lag"
  - "my own audit reported clean over the same tree"
  - "how many more like this are there"
metadata:
  node_type: memory
  type: feedback
---

A review hands you a **sample**, not a census. Fixing exactly the instances a reviewer named produces a tree where **every named instance is clean and the class is untouched** — and the evidence that would tell you otherwise is precisely what the review did not look at.

**The instance (HANS, 2026-09-05).** Codex, via PROME, named **three** `KB.tsv` rows still ACTIVE asserting figures already corrected at the headline surfaces. Fixing those three by hand would have closed the packet. Instead the fix was mechanized as a check (`doc_audit.py` C8: *no ACTIVE knowledge row may assert a value retired for a metric it declares*). **On its first run it found a fourth row the reviewer never named.** The reviewer's sample was 75% of the class, and nothing in the packet could have revealed the remainder.

**The compounding detail:** the desk's own audit had reported **CLEAN over that same tree the same hour**, because its perimeter covered two ledgers and stopped. A checker's perimeter is itself a claim `[[finding_instrument_reports_clean_against_the_wrong_reference]]`.

**The rule:**
> **Treat every named defect as one draw from a population. Ask "what query would have found this one?", run it, and fix what it returns.** If that query is cheap to keep, it becomes the check; if it isn't, at minimum record the count you found so the sample-vs-census gap is visible.

**Two traps on the way there, both seen in the same session:**
1. **The mechanized check will produce false positives, and the tempting fix is to suppress the row.** The right fix makes the check able to *name what it is looking at* — declare the series, the surface, the marker — so it can tell an assertion from a quote. A check that punishes correct documentation trains you to document less.
2. **A reviewer's ADDRESS can be stale even when the DEFECT is real** — a cited line number rots the moment a row is inserted above it. Resolve by content/ID, never by the cited coordinate `[[finding_directive_overtaken_between_authorship_and_delivery]]`.

Related: `[[finding_a_correction_pass_is_unreviewed_work]]` (the fix pass itself carries a higher defect rate), `[[finding_mechanize_the_cap_not_the_ritual]]` (a remembered "remember to also update X" is not a control), `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` (pair every rule with a retroactive sweep).
