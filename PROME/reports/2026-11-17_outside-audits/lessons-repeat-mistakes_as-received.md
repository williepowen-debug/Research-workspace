# Do written lessons stop repeat mistakes?

**Date:** 2026-11-17 (evening ET). **Repository state read:** origin/master `78ed22bb9d` (2026-11-17 18:44 ET), full history (25,626 commits). Read only; nothing in the repository was changed.
**Question (follow-up 5 of 7):** when a desk writes down a lesson, does the same kind of mistake stop, or does it come back?

## The short answer

Mostly it comes back. I traced 15 lessons through history. The 5 that a script checks automatically all held, in the files the script checks. Of the 9 that rely on an agent remembering, 7 came back, usually within days and in several cases at a *rising* rate. The other 2 held only at the desk that wrote them (BRENT, TERRY) while the same mistake kept happening elsewhere. The last one held because the desk removed the thing that caused the error (a duplicate list), not because anyone remembered.

The earlier finding (rules hold when a script enforces them, lapse when someone must remember) holds up, with three refinements that matter for what to do next:

1. **A script only protects the files it is pointed at.** The weekday checker keeps the six files it scans clean (59 of 59 clean today), but wrong weekdays keep shipping in WALTER's signal cards and inbox packets, which it does not scan. The latest one went out today: a card dated 11/17 calls Friday November 13 a "Thu".
2. **A script that supplies the right answer is not the same as one that checks what was written.** Since 8/29 every prompt gets the real clock stamped onto it, yet commits fixing hand-typed clock times went *up*: 6 in August, 16 in September, 22 in October, 18 so far in November, across 25 desks.
3. **A lesson written at one desk rarely reaches the others.** BRENT stopped reporting intraday prices as closing prices after its fourth repeat; WALTER then made the same mistake on 10/2 and 10/22.

The system already knows this about itself. The header of `scripts/claim_check.py`, written 7/27, says: *"A lesson that requires you to remember to remember, at the moment you are confident and moving fast, is not a control."* TERRY wrote the same thing in its trade postmortems: *"detection was never the gap; invocation was, for the third time."* The gap is not awareness. It is that only a handful of the repeating mistake types were ever turned into checks, and the fleet's usual response to a repeat is to append "n+1" to the memory file and move on.

## What was read

| Source | Count |
|---|---|
| Desk `LESSONS.md` files | 16 desks |
| Desk `MAINTENANCE.md` files | 12 desks |
| Fleet auto-memory files (`memory/auto/`), mostly "finding_" and "feedback_" lessons | 604 |
| Correction packets and correction signals in history (unique file names containing "correct") | 749 |
| WALTER signal cards on `BOARD/` | 2,230 |
| Commit subjects, all history | 25,626 |

**How a lesson was judged.** For each lesson I found the date it was first written down, then searched later commits, correction packets, signal cards and the lesson files themselves for the same kind of mistake after that date. "Held" means no later instance found; "came back" means at least one dated, verifiable later instance. A search can miss instances, so "held" is weaker evidence than "came back".

**How the sample was chosen.** I took every lesson type that appears at two or more desks or in fleet memory with a recorded repeat, plus every lesson that has a dedicated check script, plus TERRY's trade lessons. That leans toward lessons that matter, not toward ones that failed: the 5 script-checked lessons are all included.

## The 15 lessons

### Lessons a script checks: all held where the script runs

| # | Lesson | First written | How it is enforced | Result |
|---|---|---|---|---|
| 1 | Commit subjects no longer than 100 characters | before July | Claude hook 9/18, then git commit hook 10/05 that rewrites long subjects | **Held.** Share over 100 characters: 81% in August, 23% September, 3% October, 0% November. |
| 2 | The boot-loaded fleet memory index stays under 25,600 bytes | 6/05 | `check_memory_length.sh` at closeout | **Held.** 18,868 bytes today (73% of cap). |
| 3 | Files read whole at boot stay under 32,550 bytes | 8/28 | `read_cap_check.py` | **Held where checked:** 0 of 41 desks over the cap. **Lapsed where exempted:** desk charters are excluded, and LABOR's is 55,603 bytes, above the ~54,250-byte point where a single read gets cut off. |
| 4 | Every desk sees corrections that name it | 8/26 | `corrections_boot_check.py` blocks a desk's boot until it answers | **Held:** 41 of 41 desks wired. |
| 5 | A weekday written next to a date must be that date's weekday | 7/27 (after three wrong weekdays in one week, one of which raised a false "collector is dead" alarm) | `claim_check.py --check weekday`, advisory, run at closeout on six named files | **Held on those files** (59 of 59 clean today). **Came back everywhere else**, see below. |

On lesson 5, here is the rate of weekday-date mismatches in dated files (packets, signal cards, reports), by the month in the file name, using the repository's own checker today:

| Month | Dated files | Files with a mismatch | Per 1,000 files |
|---|---|---|---|
| July | 2,421 | 50 | 20.7 |
| August | 3,242 | 57 | 17.6 |
| September | 4,367 | 65 | 14.9 |
| October | 7,802 | 53 | 6.8 |
| November (to 11/17) | 3,557 | 28 | 7.9 |

The rate fell by about half but did not reach zero. Some flags are false (the checker guesses the year), so I hand-checked the October and November ones. Real errors that went out to other desks include: CPI release day given as "Tue 10/14" when it was a Wednesday (10/8, corrected the same day); "Thursday, October 2" for a Friday (BOARD card 10/2); "Fri 2026-10-10" for a Saturday (10/15); "Wednesday October 22" for a Thursday (10/23); a PROME pre-CPI brief draft calling Friday 11/6 "Monday" (11/10); and "Thu Nov 13" for a Friday (11/17). None of those files is on the checker's list.

### Lessons that rely on memory: these came back

| # | Lesson | First written | Later instances found | Result |
|---|---|---|---|---|
| 6 | **Take clock times from the computer clock, never type them from a sense of elapsed time** | 7/02 fleet memory; reinforced 8/20 and 9/24 | 64 commits fixing typed times, across 25 desks. By month: June 1, July 1, August 6, September 16, October 22, November 18 (to 11/17). VULCAN recorded it 5 times in 7 days (lessons L-107, L-108, L-110, L-111, L-113, 11/10 to 11/16), each time writing the lesson again. | **Came back, and rising.** A clock hook added 8/29 gives every prompt the true time; it does not check what gets typed into a file. |
| 7 | **Quote shell heredocs so "$8B" does not become "B"** | 9/24 to 9/25 fleet memory | 12 commits fixing or recording heredoc damage after the lesson was written (9/25 to 11/16), at PROME, WALTER, SAM, BRENT, DEWEY, NEXUS, LABOR, LIQUID. Memory file counts it to n=5 by 10/10 and keeps adding. | **Came back.** WALTER's new `dispatch_card.py` (11/16) now refuses signal cards that show this damage; too new to judge, and it covers only WALTER's cards. |
| 8 | **Read release dates from the official schedule; do not infer them** | 7/24 fleet-wide CPI date correction (July CPI was 8/12) | 10/8: CPI weekday wrong in a WALTER card. 10/26: CARL's calendar had October CPI on November 12, marked "(inferred)"; the BLS schedule said November 10. | **Came back.** |
| 9 | **An article's date is not today's date; last year's story is a decoy** | 7/31 memory ("anniversary article is a consensus decoy"); 8/21 memory ("publication date is not the event date"); OZK lesson 9/27 says "now seen 5×" | 10/12: an October article reprinting August shipping-transit figures was read as current. 10/16: an August 2023 KBRA article was routed as "the fourth US bank failure of 2026" (false; FDIC lists six, latest 9/25). 11/17: a September 17 settlement was routed again as new. | **Came back.** |
| 10 | **An intraday price is not the closing or settlement price** | BRENT, 7/29; BRENT's 8/12 commit calls its own mistake "4th instance of the class, committed inside the ruling that bans it" | At BRENT: no instance found after a 9/25 variant. At other desks: WALTER 10/2 (post-settlement Brent price used as the settle, caught by BRENT); WALTER 10/22 (SoftBank intraday ¥4,505 called the close; real close ¥4,305). | **Held at the desk that wrote it, came back at others.** |
| 11 | **A record that an action happened is not the action** (a disposition row, a commit message or a log line is not proof the thing was done) | 7/27 fleet memory | The memory file itself numbers its repeats: n=14, 15 and 16 by 9/06, at PROME, WALTER, DAEDALUS, REGINALD; later entries to 10/29. | **Came back.** |
| 12 | **A correction is new work and needs its own check** | 8/21 fleet memory | CARL 9/01, FERT 9/05, VIOLET 9/06, PROME 9/10, and "three instances in about two hours, two desks" on 9/11; entries to 10/14. | **Came back.** |
| 13 | **A pre-written checklist only helps if something triggers it** (TERRY) | TERRY postmortem 8/07 ("invocation was the gap, for the third time") | TRY-RESHAPE-BC sat as "decision-ready" for 13 days after every leg had expired; the checklist written to prevent exactly that, naming that trade, was never run (written up 9/03). | **Came back.** TERRY's fix was to change the form (a dated re-trigger on the file), not to promise harder. |
| 14 | **A manual stop that never fires is a note, not a rule; match option expiry to the view's horizon** (TERRY, QQQ put cluster, about −$4,341) | 8/04 postmortem; construction rule #16 | TERRY's postmortem: the hard stop was "specified in four consecutive reviews and executed zero times." TERRY then changed the form (resting orders at entry, loss capped by structure). On TERRY's own cards, no repeat found. Short-dated QQQ puts did come back in the account from late September, on lines Will opened himself: QQQ 730P (Sep 30 expiry) closed at −$2,229.54 and was rolled into a one-day Oct-01 740P, followed by Oct-02, Oct-05, Oct-09 and Oct-15 lines. TERRY's management cards on those lines cite rule #16 ("a 2-session put is a timing trade"). | **Held for the desk the rule binds.** The rule governs TERRY's proposals, not trades Will places himself. The decision on those is Will's; it is reported here only because the pattern repeated. |

### A lesson that held without a script

| # | Lesson | First written | Result |
|---|---|---|---|
| 15 | **Do not re-list option strikes and expiries in summary files; point to the one position file** (REGINALD, after a phantom position on 5/08 and again on 6/19 that nearly wrote off a live put) | 6/19 | **Held at REGINALD**: no later instance found. The fix removed the duplicate lists, so there was nothing left to drift. The same class came back at other desks: WAL and OZK on 8/20, TERRY 8/21 to 9/03. |

## What works and what does not

| Kind of lesson | Example | Did it stop the mistake? |
|---|---|---|
| A script that blocks or rewrites, on every commit | subject length; account-number guard; docket line numbers | Yes, from the day it was installed |
| A script that runs at a set step on named files | weekday check, read cap, memory length | Yes on those files; the same mistake continues in files it does not see |
| A script that gives the right answer but checks nothing | prompt clock stamp | No; typed-time fixes rose after it was added |
| Removing the copy that goes stale | REGINALD strike lists | Yes, at that desk |
| A lesson in the desk's own LESSONS file | BRENT intraday, VULCAN clock, OZK article dates | Sometimes, after several repeats at that desk; it does not reach other desks |
| A fleet memory file with an "n+1" log | clock, heredoc, record-is-not-action, correction-is-new-work | No. The repeat log grows; the error rate does not fall |
| A changed form instead of a firmer wording | TERRY: resting orders instead of manual stops; dated re-trigger instead of a checklist | Yes for that desk, as far as the record shows |

**One partial success inside the failures.** Many repeats are now caught *before* commit by the author (VULCAN's five clock slips were all fixed before they left the desk). So memory lessons work somewhat as a review prompt, not as prevention. That catches the error but costs a re-check on every write, and it fails exactly under time pressure, which is when VULCAN says the slips happen.

**One measurement caveat.** Rising counts of fixes and corrections can mean more mistakes or better catching. WALTER's share of cards that are corrections rose from 1% in May to 8% in October and 13% in November, but from 10/08 every correction must be logged in a register, so some of that rise is bookkeeping. The clearest evidence of repeat mistakes is therefore not the counts but the dated repeats the desks wrote down themselves. A rough scan found 183 of 604 fleet memory files mention a repeat dated after the file was created; I hand-checked four and all four were real repeats.

## What to do

The fleet does not need more lessons. It needs a short list of the mistakes that keep coming back, each with a decision: turn it into a check, remove the thing that causes it, or accept it. Five of the repeating types are mechanical enough to check with a script in an afternoon each; the instructions below name them.

## Copy-paste block for PROME

```
PROME: findings from an outside read-only audit of lessons vs repeat mistakes
(origin/master 78ed22bb9d, 2026-11-17). Full report: lessons/2026-11-17_do-lessons-stop-repeat-mistakes.md
in the audit project files. Please verify each point at the repository before acting, then bring Will one
decision list. Nothing here is approved yet; items 1 to 5 change shared tooling and need Will's OK.

Finding: lessons that a script checks held (subject length, memory cap, read cap, corrections boot leg,
weekday on the six closeout files). Lessons that rely on memory came back, several at a rising rate:
typed clock times (64 fix commits, 25 desks, 22 in October and 18 in November so far), unquoted heredocs
eating dollar figures (12 fix or record commits 9/25 to 11/16), inferred release dates (CPI 7/24, again 10/26),
old articles read as current (10/12, 10/16, 11/17), intraday prices as closes (WALTER 10/2, 10/22 after
BRENT stopped). The response to a repeat is usually an "n+1" line in a memory file, which has not lowered
any of these rates.

Proposed actions, for Will's decision:
1. Weekday check where errors still ship: add claim_check's weekday test to WALTER's dispatch_card.py
   refusals and run it on every staged new file in BOARD/ and any AGENTS/*/inbox/ at commit. Test case:
   SIG-W-20261117-014 says "Thu Nov 13" (a Friday) and went out today.
2. Typed clocks: add a commit-time check that flags any clock stamp in staged text that is later than the
   commit time, and any "~HH:MM" or "HH:Mx" stamp; ship a one-line stamp helper desks call instead of
   typing. The 8/29 prompt clock gives the time but does not check what is written.
3. Heredocs: extend the PreToolUse Bash hook (git_guard.py already parses heredocs) to warn on an
   unquoted <<EOF whose body contains $ or a backtick, for every desk, not only WALTER's cards.
4. Old articles: require a source publication date on every external claim in a WALTER card; refuse a card
   whose source is older than the event window unless it is marked historical. Test cases: 10/16 KBRA
   2023 article; 10/12 transit copy; 11/17 Credit Acceptance duplicate.
5. Release dates: one fleet schedule file for BLS/BEA/Fed releases, filled from the official schedules;
   a check that flags any calendar row marked "inferred" within 30 days of the date. Test case: CARL's
   October CPI row "November 12 (inferred)", actual November 10.
6. Make repeats trigger a decision, not a memory line: keep a short register of mistake types with 3 or
   more repeats after they were written down (start with the five above plus "record of an action is not
   the action" and "a correction is new work"). For each, Will rules one of: build a check, remove the
   cause, or accept the risk. Review monthly by counting repeats after the ruling date, not by counting
   lessons written.
7. Close the read-cap exemption: desk charters are excluded from read_cap_check; LABOR's charter is
   55,603 bytes, above the single-read cutoff. Either include charters in the check or record why not.
8. Spread single-desk lessons: when a desk writes a lesson about a data trap that other desks also handle
   (BRENT's intraday-vs-settle rule is the example), route it through WALTER or the fleet memory index so
   other desks get it, and prefer a check in the shared fetch tool over a rule in one desk's file.

Report back to Will in plain words: which of 1 to 8 you agree with, the cost of each, and anything you
found that contradicts these numbers.
```

## Files

- `data/weekday_flags_at_78ed22bb9d.txt`: the repository's own weekday checker run over 27,321 files today (raw output; includes false flags from year guessing).
- `data/typed_clock_fix_commits.txt`: the 64 commit subjects fixing hand-typed times, June to November.
- `data/correction_packets_first_seen.tsv`: the 749 correction files with the date each first appeared.
