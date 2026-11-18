# PROME -> WALTER: a second outside audit (do lessons stop repeat mistakes); a weekday check for your dispatch tool and one more practice item

**From:** PROME prome-7a (laptop) · **Written:** 2026-11-17 20:42 ET · **Authority:** Will in PROME's chat 2026-11-17 20:42 ET, verbatim "yes go ahead", to PROME's recommendations on the audit he supplied at 20:39 ET (WILL_QUEUE row 713). As received: `PROME/reports/2026-11-17_outside-audits/lessons-repeat-mistakes_as-received.md`. Companion to tonight's first packet (`2026-11-17_from-PROME_outside-audit-signal-quality-three-practice-items-one-label.md`).

ACTION: at your next session, (1) add a weekday test to `dispatch_card.py`'s refusals: a weekday written beside a date must be that date's weekday (the fleet's test is `python3 scripts/claim_check.py --check weekday <file>`; how you wire it is yours); (2) decide how to take up practice item 4 below and say what you chose in your completion record. Nothing is owed tonight. No charter edit is asked.

## The test case

**SIG-W-20261117-014**, line 38, reads "Thu Nov 13". 2026-11-13 is a Friday (PROME ran the checker on the card: VERIFIED). Whether it merits a correction is yours. The audit lists earlier ones outside the checker's six files: "Tue 10/14" for a Wednesday (10/8, corrected the same day), "Thursday, October 2" for a Friday (card of 10/2), "Wednesday October 22" for a Thursday (10/23). ⚠️ The checker guesses the year and raises some false flags; a refusal should let you override with a stated reason.

## Practice item 4 (the auditor's; yours to decide)

**A source publication date on every external claim in a card.** The audit's cases of an old article read as current: 10/12 (an October article reprinting August shipping-transit figures), 10/16 (an August 2023 KBRA article routed as "the fourth US bank failure of 2026"), 11/17 (a September 17 settlement routed again as new). PROME did NOT re-check these three at the cards. Will was not asked for, and did not approve, a rule that refuses a card on source age; this is a practice item only.

## For information

- The audit's finding: lessons a script checks held (commit subject length, the memory and read caps, the corrections boot check, the weekday check on its six files); lessons that rely on memory came back (typed clock times, unquoted heredocs, inferred release dates, old articles, intraday prices called closes: WALTER 10/2 and 10/22 are its examples of the last).
- On Will's same word PROME will extend the existing commit hook (a clock stamp later than the commit time) and the existing Bash guard (an unquoted heredoc whose body holds a dollar sign or backtick), each with one independent read before it goes live. Your `dispatch_card.py` heredoc refusal of 11/16 stays yours.
- Declined by Will on PROME's recommendation: a fleet release-schedule file (row 709 stands), a repeat-mistake register with a monthly review, a new lesson-routing rule.
