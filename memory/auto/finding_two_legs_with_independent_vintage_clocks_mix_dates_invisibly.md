---
name: finding_two_legs_with_independent_vintage_clocks_mix_dates_invisibly
description: A derived value whose legs carry independent vintage clocks silently mixes dates while every leg is individually correct and current-looking; the contract-roll framing of this guard hides the non-roll instances.
metadata: 
  node_type: memory
  type: feedback
  symptoms: "the spread moved by exactly the size of the policy change · both legs are live and correctly labelled and the difference is still wrong · my pre-open value equals yesterday's close · the pull returned a number with no staleness signal · I stamped it \"last close\" · every sanity check passes and there is no error to notice · the level is right and the delta is not"
  originSessionId: 57755bd2-12ab-4274-91f6-9e080c74dde6
  modified: 2026-09-18T02:00:38.441Z
---

**A value and its true observation date must travel together, or the value is an assertion. The dangerous case is a DERIVED number whose two legs run on INDEPENDENT vintage clocks** — the derivation mixes dates, **every leg is individually correct, current and plausibly labelled, and there is no error to notice.**

🔑 **THE GENERALISATION IS THE FINDING. This guard already existed as "cross-series ROLL desync" — scoped to CONTRACT MONTHS** (WALTER `design/THRESHOLD_SCAN.md` axis (i), bought when `HO=F`/`RB=F` rolled Oct→Nov while `CL=F` did not and ~93% of a crack "collapse" was the roll). **That scoping is what made it miss every instance below.** ⇒ **It is not about contract months. Any event that re-dates ONE leg is a "roll":** a policy-rate change, a publisher's revision, a fill-forward, a different market calendar. **Ask what re-dates each leg independently — not whether either is a futures contract.**

**n=3 IN ONE EVENING, 2026-09-17/18, THREE DESKS, THREE MECHANISMS, ONE SHAPE:**

1. **WALTER — a SPREAD straddling a policy change.** `SOFR−IORB` published as **−28 bp**. It was SOFR 9/16 (3.62, pre-hike) minus IORB 9/17+ (3.90, post-hike): the FOMC hiked 25 bp on 9/16 and IORB re-dated a day before SOFR could. **Matched legs: 3.62 − 3.65 = −3 bp.** The entire 25 bp error *was* the hike. Both legs live, both correctly labelled, threshold far away in both readings — so nothing prompted a re-check.
2. **VIOLET — a pre-open state cell read as current.** Its cheap-tail alert published `DORMANT 2/4` computed off the **prior** close. `yfinance` `fast_info` **fill-forwards a prior-session close off-RTH with NO staleness signal**, so `^VIX3M`/`^VIX6M`/`^VVIX`/`^SKEW` return yesterday wearing today's label. The settle four hours later was `OPEN 4/4` — the opposite state. ⇒ **grade these series off the DATED publisher bar, never an intraday witness.**
3. **LIQUID — the date computed upstream and thrown away downstream (KB-LIQ-130).** Its `boot.py` stamped seven rows with the literal string `"last close"` while FORGE's `fetch.py` **already computes a verified as-of** by cross-checking `fast_info` against a dated `history()` bar. **The truth existed one layer up and was discarded in the act of consuming it.**

⚠️ **ALL THREE FAILED SILENT AND BENIGN** — no crash, no implausible number, no threshold crossed, so `[[finding_plausible_stale_value_evades_review]]` applies to every one. **The tell is never the value; it is that nobody can name the leg's observation date without going and looking.**

✅ **WHAT TO DO.** Resolve **BOTH** legs to a dated observation on **EVERY** pull and **state both dates beside any derived figure**. **If the dates differ, the figure is NOT GRADEABLE — report `VINTAGES MISMATCHED`, never a number.** Where one leg genuinely leads (FX and futures roll ahead of US cash equities), that is a **known** split to be **named**, not an alarm.

🔴 **AND THE GUARD YOU WRITE FOR THIS WILL FIRE WRONG ON ITS FIRST RUN.** LIQUID's did, minutes after writing it: it compared all seven tickers and raised on USD/JPY sitting at 9/18 against equities at 9/17 — **a real split, a wrong alarm**, and it would have cried wolf on every evening boot, which is when that desk boots. **Fixed by SCOPING it to one market calendar (cross-calendar renders neutral with both dates named) — NOT by loosening the bar.** See `[[finding_test_the_guard_not_just_the_guarded]]` and `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`.

📌 **Distinct from its neighbours:** `[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]` is one series against a threshold; `[[finding_agreement_at_one_date_can_be_cancelling_errors]]` is about agreement not validating a derivation. **This one is TWO LEGS, INDEPENDENT CLOCKS, and the mismatch is structurally invisible.** Related: `[[finding_instrument_reports_clean_against_the_wrong_reference]]` · `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]` · `[[finding_a_column_that_is_both_record_and_instrument_basis_fails_twice]]`

**Provenance:** WALTER (own defect, found at boot), VIOLET (owner-initiated cross-session correction), LIQUID (KB-LIQ-130/131, which named the common lesson: *"a value and its date must travel together or the value is an assertion"*). Canon for the contract-month form stays `AGENTS/WALTER/design/THRESHOLD_SCAN.md` § CROSS-SERIES ROLL DESYNC.
