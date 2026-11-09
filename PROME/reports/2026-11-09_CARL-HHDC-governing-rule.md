# Which kill rule governs CARL's Q3 household-debt grade (written before the print)

**Written** 2026-11-09 about 16:0x ET by PROME, on Will's instruction of 15:55 ET (`PROME/proposals/2026-11-09_wq656-657-658-RULED.md`). The NY Fed Q3 2026 release is due Tue 2026-11-10 11:00 ET and was not published when this was written (CARL's prep note records the file URL returning a redirect at 13:00 ET 11/9). No Q3 figure was seen.

## Finding: the governing rule is established. It is the RE-SPEC (THESIS v2.6.6).

| Dated record | What it establishes | Token |
|---|---|---|
| `PROME/proposals/2026-08-16_carl-row44-respec-optionA-RULED.md` | Will ruled Option (A) on 2026-08-16, verbatim "approved - go ahead with A as recommended": leg 2 re-keys to the credit-card transition rate into 90+ (NY Fed HHDC Page 14), 2 consecutive declines with cumulative decline of at least 100bp; the reset of the count from 1-of-2 to 0-of-2 accepted. Live only when two conditions clear | VERIFIED |
| Condition 1, CARL commit 7037178306 (2026-08-27) | The servicer-transfer caveat was read at the primary and is scoped to mortgage balances, not card reporting; the rule was encoded as THESIS v2.6.6 the same day, re-affirmed by Will in-session per the commit body | VERIFIED at the commit; the in-session re-affirmation is CARL's record |
| Condition 2, RED dissent | `AGENTS/CARL/thesis/CHANGELOG.md` records CHG-RED-045 answered in the spec text and RED's rider folded in; no later record reopening the choice was found | INFERRED (no reopening found; RED's files were not searched whole) |
| Same ruling, "What stands" | The as-written share rule (Page 12, direction only) is SUPERSEDED. It survives only as a mandatory shadow grade. If it fires while the re-spec has not, that divergence is written on the card in figures and escalated to Will the same session, "never absorbed" | VERIFIED |
| `AGENTS/CARL/thesis/HHDC_Q3_2026_GRADING_CARD_TEMPLATE.md` §1 (frozen 11/06) | Carries both rows as the ruling requires | VERIFIED |

## What follows for 11/10

1. **Official verdict:** the RE-SPEC only. At Q3 it fires only if Page 14 falls from 7.10 to 6.97 to 6.10 or lower (both moves down, cumulative at least 100bp). Any other print is NOT FIRED under the rule Will ratified.
2. **Shadow:** the as-written row is recorded beside it, both in figures, before any interpretation. If it shows decline 2 of 2 while the re-spec has not fired, that is a divergence reported to Will the same session as a fact. It is not a second official verdict and not a choice between rules: Will already made that choice on 8/16, before this print.
3. **No new rule.** Thresholds are those written in CARL's prep note before the print (`AGENTS/CARL/research/2026-11-09_HHDC_prep/PREP.md`), which match the ruling.
4. **What a divergence would mean:** only Will can reopen the 8/16 choice. A divergence report carries the figures and the note that CARL is the beneficiary of the reset; it proposes nothing.

## Limit
Condition 2 rests on the absence of a reopening record in the files read. If RED holds an unanswered post-8/16 objection to the re-spec, the choice would be open to Will under the 8/16 ruling's own clause, and the official verdict would then be unresolved. None was found.
