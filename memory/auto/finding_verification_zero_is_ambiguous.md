---
name: finding_verification_zero_is_ambiguous
description: "A check reporting no problems is consistent with two worlds — it read everything and found nothing, or it read nothing; and N surfaces agreeing is consistent with correct AND with uniformly stale. Both are invisible by construction."
metadata:
  type: feedback
---

**A clean result from a verification is ambiguous, and the ambiguity is invisible by construction.** Two distinct forms, both bit TERRY on 2026-07-30:

**① "No findings" = found nothing wrong, OR read nothing.** Adding a two-clock banner to `SIGNALS.tsv` made line 1 a one-column banner. `boot.py` assumed `lines[0]` was the header, so `csv.DictReader` keyed every row off the *banner* — the boot card printed **"active rows: 0 of 15" with no regime PIN for an entire session, and its own author read past it at boot.** A quiet ledger and a dead parser render identically. A second layer sat underneath: the active-row filter matched an **exact set** `{LIVE, LIVE-WEAK, DECAYING}` while that morning's decay sweep had introduced `LIVE-RECONFIRMED` and `SHAPE-LIVE / LEVELS-STALE`, so it silently dropped the load-bearing row. **A reader whose vocabulary lags the file it reads fails false-negative, and quietly.**

**② "All surfaces agree" = correct, OR uniformly stale.** A card's verdict moved to NO AT THIS PRICE in its body while its header *and all three ledgers* still said CONDITIONAL. Every state field agreed — so a cross-surface consistency check passed, having compared four copies of the same stale value. **Consistency checks are structurally blind to unanimous staleness**, which is exactly the state a correction pass produces when it updates prose and forgets the fields.

**Why:** absence of evidence is being read as evidence of absence, at the level of the *instrument* rather than the data. Every guard has a silent-success path, and it is the same output as real success. The failure direction is the dangerous one: a wrong value invites challenge, a *missing* one closes the question.

**How to apply:**
- **Make zero a finding, not a pass.** If a surface a check depends on parses to zero rows, report it as a parser defect. Never let "0 of N" print without asserting N was actually read.
- **Test the guard with the bug put back.** Re-introduce the defect and confirm the alarm fires. Selftests that only exercise the happy path certify nothing.
- **Break unanimity with an outside witness.** When N surfaces agree, compare against something *outside* the agreeing set — a card's body vs its own header, a hand-computed number vs the tool's. Agreement among copies is not corroboration ([[finding_circular_corroboration_via_state_file]]).
- **Match on shape, not an exact enumeration**, wherever a reader's vocabulary can drift behind the file's.
- **Expect the guard to inherit your blind spot.** The first version of the anti-drift checker matched bare numerics and reproduced the exact false-positive defect its author had diagnosed hours earlier.

Related: [[finding_test_the_guard_not_just_the_guarded]] · [[finding_silent_blank_evades_review]] · [[finding_fail_loud_on_incomplete_data]] · [[finding_ledger_drift_behind_narrative]] · [[finding_state_token_sweep_all_surfaces]]
