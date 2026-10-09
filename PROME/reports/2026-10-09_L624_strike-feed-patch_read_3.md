COLDREADER · READ 3 (episode's LAST) · OSPREY fix pass 2 `4ea2b4539` (acceptance `88d715d03`) · AGENTS/OSPREY/scripts/strike_feed.py + tests/test_strike_feed_L624.py + feed/README.md vs ACCEPTANCE_L624 "Acceptance conditions (pass 2)" AC10–AC12 + "Completion states, pass 2" · 27 claims
Stamp: Fri Oct 9 13:11:56 EDT 2026 (`date`). Read-only. The script, the test file and the fixture were copied (`git show 4ea2b4539:…`; `cmp`-identical to the worktree) and run here under `-B`. The old versions are `git show 04d8f06be|46d6f6dea|46d6f6dea^:…/strike_feed.py`, run via STRIKE_FEED_PATH. Every counterexample ran through the test file's own `run()` harness (date and fetch injected, temp ledger and out_dir). Harness: `harness/cx.py`, `harness/cx2.py`, mutants in `mut/`. No network. `git status --short -- AGENTS/OSPREY/` was empty before and after.
SCORE: 20/27 ✅ · 6 ⚠️ · 1 ❌
READ-2 ❌8: **CLOSED in code** on the live page shape (newest-first). All four CX fail closed on 4ea2b4539, and all four fail open on 04d8f06be (table below).
VERDICT: **STILL UNRESOLVED (❌ = 1)**. The blocker is the README, the consumer surface, not the code: it claims a guarantee the acceptance itself declares false.

## ❌ (blocking)
❌1 README operator text launders the declared residue.
- **Claim:** "Any link that could be newer is named and fails closed." and "A date defect on the real newest (past-year typo, title year typo, format drift …) lands here, never silently."
- **Artifact:** AGENTS/OSPREY/domain/energy-strikes/feed/README.md:39 and :15 (written in 4ea2b4539).
- **The other side, in the same commit:** ACCEPTANCE:89 "A past-typo'd link BELOW the followed one looks the same as an honest older bulletin. That case is declared residue, not fixed." and :129 "a year-typo'd real newest placed BELOW the followed link … is still skipped."
- **Command:** `python3 -B harness/cx2.py new/tests new/strike_feed.py`, cases R3-Q and R3-B2.
- **Observed:**
  - R3-Q: a pinned "Most read" link to last week's 28 Sep–4 Oct bulletin sits on top, the real newest is past-year-typo'd ("5th - 11th October 2025") below it, run 10/13. Output: `BULLETIN — read manually`, NOT_READ=0, "position 1 of 3". The real newest appears nowhere.
  - R3-B2 (2 links, typo'd newest at the bottom) gives the same result.
  - The README's guarantee is false in exactly the declared-residue case. It is the surface a feed reader uses to decide whether a BULLETIN row can be trusted, and it drops the caveat.
- **Proposed change:** qualify README :15 and :39 ("on a newest-first index; a date-typo'd newest BELOW the followed link is silent — ACCEPTANCE residue ⚠️21"), or withhold those two sentences until fixed. Text only; the code is unchanged.

## ⚠️
⚠️2 The residue description says no signal exists to catch this case. There is one, and it is cheap.
- **Artifact:** ACCEPTANCE:129 "No order signal exists to catch it"; N1 :133 "makes every run `BULLETIN_NEWEST_UNSURE`".
- **Command:** R3-Q, plus a monotonicity check on the real fixture.
- **Observed:** in R3-Q the window ENDs down the page run 10-04, **2025-10-11**, 09-27. That is not monotone, so the order signal exists for every typo'd link except the last one on the page. `parse_html_index` dedup (:84) also keeps a featured duplicate's FIRST position, which throws away the list position that would have put the newest above it. The real fixture's 14 ENDs are monotone non-increasing (verified), so a "dated link below the followed one with an END later than an earlier link" doubt rule would not fire on the live page. N1's "every run" is false in the typo week (R3-Q is silent).
- **Why ⚠️ and not ❌:**
  - The silent case needs two things at once: the page stops being newest-first, AND the newest carries a date defect.
  - Under that same page structure, ordinary weeks fire UNSURE loudly (R3-A), so the structure change shows up first.
  - The live page is newest-first.
- **Proposed change:** register a DOCKET row for "monotonicity doubt below the followed link + dedup position". Correct :129 to "no signal for the LAST link; a fixable signal elsewhere".

⚠️3 The ⚠️16 property ("pub_date = window END") fails on the fallback path.
- **Artifact:** strike_feed.py:137 and :258/:275; ACCEPTANCE:48 (residue 2, "the TITLE does [parse]").
- **Observed:**
  - R3-I2: the title "29th December 2026 - 4th January 2027" (two years) does not parse. The code falls back to the slug date, giving window 2026-12-29..2026-12-29 and a note that says "pub_date = window END".
  - Read 2027-01-12, it shows `BULLETIN_STALE … publisher stopped` on an on-time bulletin.
  - R3-I3, the one-year title form, parses correctly.
  - The failure is loud (safe direction), and the residue claim holds only for the one-year title form.
- **Proposed change:** widen residue 2 to cover the two-year title form, and say the alarm can come about 6 days early.

⚠️4 A title-vs-slug year disagreement is resolved silently.
- **Observed:** R3-H (slug 2025, title 2026) gives the title's date, fresh, NOT_READ=0, with no note of the disagreement.
- This is a free tell, like the order tell read 2 flagged. It would catch CX1-shape typos (title typo, slug right) whatever the page order.
- **Proposed change:** add it to the ⚠️2 docket row.

⚠️5 Two AC10 clauses hold, but no test pins them.
- **Artifact:** ACCEPTANCE:78 ("up to 5, then +N more") and :81 ("UNDATED … note names the other unusable links").
- **Observed:** R3-S gives 5 named plus "+2 more" ✅, and R3-T gives UNDATED naming the other link ✅. But mutants M4 (`doubts[:5]` → `[:1]`) and M5 (doubt note dropped when UNDATED) both pass the suite: "Ran 32 … OK".
- **Proposed change:** add two tests.

⚠️6 AC12's original wording is left live beside its own correction.
- **Artifact:** ACCEPTANCE:94 "Every new pass-2 test FAILS" against :120 "AC12 as written over-claimed". The declared exception (`test_wrong_owner_non_follow_index_unchanged`) is labelled NON-DISCRIMINATING and passes on 04d8f06be, as stated.
- **Proposed change:** reword :94 in place.

⚠️7 A permanent loud false alarm on a non-newest-first page.
- **Observed:** R3-C (an oldest-first page with honest dates) gives UNSURE on every run, naming the 2 older links. R3-F/R3-G (a category URL matching `link_pattern`, above or below) give UNSURE. This is the declared N1 territory and fails safe. A standing UNSURE is still alarm-fatigue risk.
- **Proposed change:** none beyond N1's `link_pattern` repair note.

## ✅
1. Fixed code: `python3 -B -W error::ResourceWarning -m unittest test_strike_feed_L624` gives Ran 32, OK. `python3 -I -B <file>` gives OK.
2. 04d8f06be gives FAILED (failures=14): the 8 AC10 + 3 AC11 tests, plus X2, real_index and X3. This matches the memo.
3. 46d6f6dea gives 23 F. 46d6f6dea^ gives 20 F + 4 E. This matches the commit body.
4. ❌8 is closed on CX1, CX1b, CX2 and CX2b (table below).
5. AC10(a) is structural: the TOP matching link is always either the followed link or a doubt (:152, `i < followed["pos"]`). On a newest-first page, the real newest can never be silent.
6. AC10(b) applies anywhere on the page. Mutant M2 (rule b only above) is caught (2 F).
7. Mutant M1 (drop rule a) is caught (4 F). M3 (UNSURE not counted in NOT_READ) is caught (9 F). M6 (always UNSURE) is caught (2 F, must-not-fire). M7 (pub_date not END) is caught (1 F).
8. Must-not-fire holds: the real 10/9 fixture under `pick_newest` at 10/09, 10/12, 10/14 and 10/15 gives followed = 28 Sep–4 Oct, 0 doubts, 14 dated. The test asserts fresh, NOT_READ=0, "position 1 of 14".
9. Stale and doubt together give one row, UNSURE with "also BULLETIN_STALE", counted once (test, and R3-W).
10. Doubt + body failure + stale (R3-U) gives one `FETCH_FAILED (newest post)` row, note "BULLETIN_NEWEST_UNSURE + BULLETIN_STALE" plus the doubt URL, NOT_READ=1, summary "(followed: FETCH_FAILED (newest post))".
11. AC11 ⚠️17 holds (test, and R3-U).
12. AC11 ⚠️18 holds. R3-V (days 3): "days_back 3 < 10 … on-time … re-run", with no "publisher stopped".
13. The note never says "newest" for the followed item. It reads "latest window END of K dated … position P of N" (all runs).
14. Wrong owner: the doubt rule is gated on `follow_newest` (:249), and the non-follow `ww` source is unchanged (test).
15. R3-A (pinned older post on top, newest honest below) is LOUD: UNSURE naming the pinned June link, NOT_READ=1. N1's "loud" holds for the single-defect case.
16. R3-D (one link) is fresh, no doubt. R3-E (same END) follows the first in document order, no doubt.
17. R3-J (undated link on top) gives UNSURE. R3-K (forward year typo on top) gives UNSURE "FUTURE start". R3-M (same-year month typo on top) gives UNSURE. R3-O (a 30-day roundup above) gives UNSURE.
18. N2 is honest: no wrong window found. A digit inside a year that starts a match is rejected by the span check (`…2026-4th-january-2027`, span negative, gives None).
19. ⚠️22 and N3 are honest declarations. The row still says read manually. Vocabulary registration is DAEDALUS's.
20. Four states are reported unmerged. INDEPENDENTLY VERIFIED: NO pending READ 3 (ACCEPTANCE:124).

## Read-2 CX fixtures (harness/cx.py)
| CX | 4ea2b4539 | 04d8f06be |
|---|---|---|
| CX1 (run 2027-01-07) | UNSURE, NOT_READ=1, names the …-2027 link [above] | BULLETIN, NOT_READ=0, newest absent |
| CX1b (run 10/13) | UNSURE, NOT_READ=1, names the …-2025 link [above] | BULLETIN, NOT_READ=0 |
| CX2 (run 10/13) | UNSURE, NOT_READ=1, names "-oct-2026" [above, no parseable date] | BULLETIN, NOT_READ=0 |
| CX2b (run 10/13) | UNSURE, NOT_READ=1, names "week-41" [above, no parseable date] | BULLETIN, NOT_READ=0 |

## Own counterexamples (fixed code; old code gave BULLETIN, NOT_READ=0 on all except R3-P)
- **SILENT:**
  - R3-Q (pinned last week + past-typo'd newest below) gives BULLETIN, NOT_READ=0. → ❌1 / ⚠️2
  - R3-B2 (typo'd newest at the bottom) gives the same. Declared residue, no signal.
- **LOUD, correct:** R3-A, J, K, M, O, S, T, U, W.
- **LOUD, false alarm:**
  - R3-C (oldest-first page) and R3-F/G (category link): N1 territory.
  - R3-I2 (two-year cross-year title): early STALE. → ⚠️3
- **Correct and quiet:** R3-D, E, I3, L (newest not yet posted at 10/13 reads fresh: design tolerance per read 2), P.
- **Silent, information discarded:** R3-H (slug/title year disagreement). → ⚠️4

## Disposition (last read)
- **Blocking:** ❌1 only. Two README sentences overstate closure. It is a text fix; any fix made after this read is unreviewed.
- **Code:** the AC10–AC12 properties hold, and read-2 ❌8 is CLOSED on the live page shape.
- **Residue to the docket:** ⚠️2 (monotonicity and dedup-position doubt, a feasible fix) and ⚠️4 (title/slug disagreement), with ⚠️3, ⚠️5, ⚠️6 and ⚠️7 alongside.
POINTERS: 9/9 resolve (read-1 and read-2 ledgers, the OSPREY memo, ACCEPTANCE, the test file, the fixture, the README, commits 4ea2b4539 / 88d715d03 / 04d8f06be / 46d6f6dea); dead: none.
ONE-LINE VERDICT: STILL UNRESOLVED (❌ = 1, README :15/:39). The code closes ❌8 and holds as properties, but the operator README tells a reader "never silently" about a silent case the acceptance itself declares.
