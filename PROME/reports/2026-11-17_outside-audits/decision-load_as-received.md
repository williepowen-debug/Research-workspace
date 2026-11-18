# How much of William's time the system takes: the decision queue, 30 July to 17 November 2026

Follow-up question 3 of 7. Read-only. Repository pinned at master `62d7a184` (17 Nov 2026, 19:28 ET), full history.
Sources: every committed version of `PROME/WILL_QUEUE.md` (1,381 versions since the queue was created on 30 July) and the queue's event ledger `PROME/registry/WQ_LEDGER.tsv` (1,905 events covering 680 numbered items). Decisions made before 30 July lived in other files and are not counted here.

## The short version

- **The queue puts about 40 items a week in front of you, and about 55 a week at its peak from mid-October to mid-November.** Since 30 July, 680 numbered items have been registered, and you ruled on 577 of them. The rest were receipts, items that were overtaken, or items the system closed itself.
- **You answer fast.** Half of your rulings came within about 2 hours of the item being registered, and three quarters within about a day. Only 41 items (7%) waited more than a week, and most of those were chores for your own hands or trade cards. In November the typical wait was under an hour.
- **You almost always take the recommendation.** In about 300 rulings where both PROME's recommendation and your choice can be read mechanically, you picked a different option 6 times (about 2%). Half of your replies are five words or fewer, and about a third of your recorded rulings came in a message that settled several items at once ("694 A, 693 A, 697 A approved").
- **So the cost to you is mostly reading, not deciding.** The median item is about 210 words. At roughly 40 to 55 items a week, that is something like an hour or two of reading a week just for the asks. That figure is my rough estimate, not a measurement: nothing in the repository records how long you spend.
- **My judgment: roughly one in five to one in three of your decisions could have been settled under rules you had already given.** This held in every period I checked, including the week after you granted four new permissions on 11 November. The examples are in section 4. On 30 September you asked for this yourself: *"Lets look at the WQ and see if there are other simple or no brainer decisions you can just move forward with and assume I approve?"*

## 1. How many items come to you each week

Week starting Monday. "Registered" is every new numbered item. "Ruled by you" is items where your word closed it. "Closed by the system" is receipts, items overtaken, or items PROME closed itself. Full table: [weekly_load.tsv](weekly_load.tsv).

| Week of | Registered | Ruled by you | Closed by the system | Typical wait (median) | Slowest 10% waited at least | Ruled within 24 hours |
|---|---|---|---|---|---|---|
| 3 Aug | 16 | 4 | 2 | 6.4 days | 98 days | 22% |
| 10 Aug | 13 | 12 | 11 | 1.2 days | 11 days | 38% |
| 17 Aug | 29 | 20 | 8 | 2.6 hours | 0.6 days | 94% |
| 24 Aug | 52 | 44 | 7 | 4.6 hours | 0.6 days | 94% |
| 31 Aug | 47 | 33 | 2 | 1.4 hours | 7.7 days | 68% |
| 7 Sep | 54 | 45 | 6 | 5.6 hours | 12 days | 71% |
| 14 Sep | 30 | 21 | 3 | 4.0 days | 10 days | 32% |
| 21 Sep | 39 | 45 | 5 | 2.0 hours | 3.9 days | 64% |
| 28 Sep | 71 | 44 | 24 | 10 hours | 12.6 days | 57% |
| 5 Oct | 36 | 17 | 16 | 21 hours | 6.6 days | 54% |
| 12 Oct | 36 | 36 | 5 | 3.8 hours | 5.9 days | 58% |
| 19 Oct | 70 | 63 | 3 | 2.4 hours | 6.5 days | 72% |
| 26 Oct | 62 | 71 | 2 | 1.0 hour | 0.6 days | 95% |
| 2 Nov | 68 | 64 | 3 | 0.4 hours | 1.4 days | 89% |
| 9 Nov | 31 | 38 | 3 | 0.7 hours | 0.6 days | 100% |
| 16 Nov (Mon and Tue only) | 22 | 20 | 1 | 0.2 hours | 0.1 days | 100% |

- **Across the whole period: 680 items, about 42 a week.** In the four weeks from 19 October to 15 November it was 231 items, about 58 a week, of which you ruled 220.
- **The week of 9 November was the first real drop** (31 items, down from 60 to 70). Your 11 November grants of four new permissions (WQ-673, classes C10 to C13) fall in that week. One quiet week is not yet a trend.
- **You ruled on 77 different days, about 6 items on a typical ruling day.** The busiest days had 22 or 23 rulings (10 Sep, 15 Oct, 29 Oct, 31 Oct, 5 Nov). In most weeks since late August you ruled on 5 to 7 days of the week.
- **When you rule:** of the 213 rulings with a recorded clock time, the busiest hours are 10:00 to 17:00 ET and 21:00 ET; 15 (7%) came between 22:00 and 06:00, and 33 (15%) on a weekend.

## 2. How long items wait for you

| Measure | All 577 rulings |
|---|---|
| Median wait | about 2.2 hours |
| Within 1 hour | 212 (37%) |
| Within 24 hours | 430 (75%) |
| More than 3 days | 103 (18%) |
| More than 7 days | 41 (7%) |
| More than 14 days | 11 (2%) |

| Kind of item | Rulings | Median wait | Slowest 10% |
|---|---|---|---|
| Decisions (rules, designs, gates, research) | 528 | 1.9 hours | 5.7 days or more |
| Trade items | 31 | 12 hours | 6.9 days or more |
| Chores for your own hands (keys, broker exports, launches) | 18 | 33 hours | 20 days or more |

- **The long waits are mostly not decisions.** The slowest were a "stay silent until mid-October" placeholder (WQ-31, 98 days), a phone-signal setup chore (WQ-204, 41 days), and two trade cards (WQ-357 and WQ-302, about 25 to 28 days). Waits have fallen steadily: the median was about 9 hours for items registered in August, 2.4 hours in October and under an hour in November.
- ⚠️ **What "wait" measures here.** The clock starts when PROME writes the item into the queue, and PROME usually does that minutes before it shows you the question in a session. So a short wait means you answer quickly once asked. It does not show how long the underlying issue sat before PROME asked. November is also slightly flattered because its newest items have had less time to wait, though only 2 items are still open.
- **Method note.** Where the ledger records your words with a clock time (213 rulings), I used that time. Otherwise I used the ledger's ruling date or the first queue commit where the item left the open list, whichever came first. Registration is the first queue commit that shows the item. Waits are therefore accurate to the day for about 60% of rulings, and to the minute for the rest.

## 3. What the rulings look like

- **You take PROME's recommendation almost every time.** In 300 rulings where both the recommended option and your option can be read from the record, they differ 6 times: WQ-441, 518, 556, 656, 662 and 667. PROME's own review on 11 November, which read the rows more carefully, found you changed or declined 29 of 174 recommendations in its window (17%). Most of those changes were to system proposals rather than research or trades, and they mostly removed steps.
- **Your replies are short.** Of the 426 rulings that record your words, the median is 6 words, and half are 5 words or fewer. 139 of them were settled by a single message that covered more than one item.
- **More than once you handed the call back.** *"lets have you approve with your recs"* (WQ-513 to 516), *"approve with your recs all four"* (WQ-614 to 617), and on WQ-458: *"Walter is handling this and progressing through. Does not need a WQ for me to approve."*

## 4. Items the system could have settled under rules you had already given (my judgment)

⚠️ **Everything in this section is my judgment, not a measurement.** For each item I named the earlier rule I think already covered it. Where the rule only arguably applied, I marked it "plausible", not "clear". I judged each item against the rules in force when it was asked, not against later ones.

### 4a. Re-asks of rulings you had already given

These are the clearest cases. The system asked you again about something you had already decided.

| Item | What was asked | The earlier ruling that already settled it |
|---|---|---|
| WQ-151, 159, 162, 164, 196 to 199 (1 to 8 Sep) | Eight items registered for decisions you had already made | The original rulings. PROME's 9 Sep reconciliation closed them all: *"Decision already RULED/EXECUTED on the original row; no fresh operator approval owed."* |
| WQ-179 (4 Sep) | LABOR's write-mode question | Your *"Go ahead with the batch"* in DAEDALUS's window on 7 Sep. You then had to say *"close 179"* to PROME as well. |
| WQ-235 (12 Sep) | Which measurement basis BROCK's gate uses | Your 13 Aug ratification of that gate's specification already fixed it as amortized cost. PROME later wrote "Not a new ruling." |
| WQ-177 (4 Sep) | Stand down VIOLET's 1 July hedge framework | The framework had already been retired and replaced on 31 July by the rising-volatility design. |
| WQ-570 and WQ-565 (Oct) | Ruled in CATO's and NEXUS's windows, then asked again by PROME | Your word in the desk window. Recording that word without asking again became class C2 on 1 October. |

### 4b. A random sample of 40 items from 7 August to 3 October

This is the period PROME's own 11 November review did not read. The full judgment for each item is in [sample40_judgment.tsv](sample40_judgment.tsv).

- **Clear (6 of 39 decisions, 15%):**
  - **WQ-102:** whether the root rule or OTTO's local rule wins. The root rulebook already said the root rule overrides.
  - **WQ-121:** the HEARTBEAT re-base, six days after HEARTBEAT was made PROME's own to edit (23 Aug).
  - **WQ-177, 179 and 235:** the re-asks in 4a above.
  - **WQ-305:** ORACLE editing its own charter to drop a check that had never found anything. This passed all five tests of the 7 Aug delegation rule (`AGENTS/DAEDALUS/BLUEPRINTS/DELEGATION_TIER.md`), and today it is exactly class C4.
- **Plausible (6 more, which would bring it to 12 of 39, 31%):** WQ-84, 85, 88, 100 and 332 were each a desk's question about its own specification that looks self-rulable under the 7 Aug delegation rule. WQ-335 was a "not now" that both PROME and the desk recommended.
- **Not avoidable (25):** trades, spending, root rulebook changes, gate levels, new process, or items where you changed the answer.
- **Not counted:** two items were queue clutter you never had to answer (WQ-151 and WQ-197), and one was a hands chore (WQ-210).
- **Your answer to WQ-305, 332 and 335 on 30 September was the request quoted at the top.** It led directly to the 1 October approval inventory (WQ-348, classes C1 to C9).

### 4c. 4 October to 11 November: PROME's own count

PROME's report `PROME/reports/2026-11-11_queue-review-by-decision-type.md` read 209 items from this window. It found 52 avoidable repeats (25%), rising to about 89 (43%) if agreed research answers count as delegable. I checked its method and the class definitions it used, but not each of its 209 rows. Its eight repeat groups led to your WQ-673 grant on 11 November (classes C10 to C13).

### 4d. 11 to 17 November, after the new grants

There were 36 new items in this window. Six were receipts PROME recorded without asking you, and two were hands chores, which leaves 28 real asks. I read all 28.

| Item | What you were asked | Rule already in force | My call |
|---|---|---|---|
| WQ-706, 707 (17 Nov) | Add the "last 7 days" limit to 46 free news searches, and split two long searches | **C7**: add or remove a free feed in the news-collection lane. PROME's own 11 Nov review counted WQ-598 (two free "last 7 days" searches) as already covered by C7. | Clear |
| WQ-705 (17 Nov) | Test and fix one free Gulf news search | **C7** | Clear |
| WQ-697 (16 Nov) | HENRY drops a slow start-up scan from its own boot | **C4**: a desk editing its own charter, including "how often it runs one of its own checks" | Clear |
| WQ-708 (17 Nov) | Retire WALTER's blocked-page reader | Your 16 Nov blocked-sites rule (WQ-701, fix G), which bars exactly this tool, together with **C11** (the next step inside work you already approved). PROME also offered "name it as an exception", which only you could grant. | Plausible |
| WQ-694 (16 Nov) | Add a second daily news collection run | **C7** covers "change a schedule time"; a second run is a little more than that | Plausible |
| WQ-681 (12 Nov) | WALTER runs the free news collector at session start | **C7** | Plausible |
| WQ-691 (16 Nov) | CORAL's 3.5 score: does a half point round up? | Your WQ-690 ruling 50 minutes earlier, where a half did not round up. PROME's own recommendation said it "matches the 690 ruling". | Plausible |

- **That is 4 clear and 4 plausible out of 28 (14% to 29%), in the week after the new grants.** The other 20 were genuinely yours: trades, gate changes, the Decision Deck's retirement, GIBBS (where you overruled the recommendation), ownerless puts, new research for four desks (beyond C9's two-per-boot cap), and changes to root files.
- **The pattern is that the classes exist but are not applied at the moment of asking.** Free news-search edits and a desk trimming its own checks are plain cases of C7 and C4, and they still came to you as ⚖️ blocks.

## 5. What this means

- **Your direct decision time is small per item and the items are rarely contested.** The load comes from volume (40 to 70 a week) multiplied by reading.
- **About one in five to one in three of those items should never have reached you under rules you had already written.** That share did not shrink much as rules were added (the 7 Aug delegation tier, the 1 Oct classes C1 to C9, the 11 Nov classes C10 to C13). Each round removed some kinds of question, but PROME kept asking in cases the rules already covered.
- **The fix that fits your 16 Nov limit on new process is to use the grants already written, not to write new ones.** The paste block below asks for no new rule, checker or queue row.

## 6. Caveats that could change the reading

- **The minutes are not recorded anywhere.** "An hour or two of reading a week" is my estimate: about 210 words per item at ordinary reading speed, times 40 to 55 items. It also leaves out the in-chat explanation blocks and the time sessions take.
- **The "could have settled" share is judgment.** It rests on 4 strong re-ask groups, a 40-item random sample, PROME's own 209-row review, and my reading of the 28 most recent asks. A stricter reader could put it nearer 15%, and a looser one nearer 40%.
- **Waits start when PROME registers the item, not when the issue first appeared** (see section 2).
- **Before 30 July the queue did not exist,** so this report says nothing about February to July.

## Files

- [weekly_load.tsv](weekly_load.tsv): the weekly table.
- [decision_rows.tsv](decision_rows.tsv): one row per item, with registered and ruled times, wait, who closed it, verdict, and your words (first 200 characters).
- [sample40_judgment.tsv](sample40_judgment.tsv): the 40-item sample with my call on each.
- `scripts/`: `history.py` walks every queue version; `build.py` builds the per-item rows; `aggregate.py` computes the weekly table and the wait figures. Run them against a full clone at `62d7a184`.

---

## Paste block for PROME

```
From Will, after an outside read-only review of the decision queue (decision-load report, 2026-11-18, repo pin 62d7a184). No new rule, checker, ledger or queue row is wanted from this. It asks you to use permissions I have already given.

1. Before you register any ⚖️ item for me, check it against the "Done without asking" classes C1 to C13 in PROME/CLAUDE.md and against my earlier rulings on the same subject. If one already covers it, do it, record it as a receipt under that class, and name it in the day's "Done without asking" list. Do not ask me.

2. Cases from last week that should have gone that way (the reviewer's judgment; check each one against the class text before you agree):
   - WQ-705, 706, 707: free news-search edits, including the "last 7 days" limit. This is C7, and your own 11/11 review already counted WQ-598 (the same kind of edit) as C7.
   - WQ-697: HENRY dropping its own start-up scan. This is C4 ("how often it runs one of its own checks").
   - Arguable: WQ-708 (follows from my WQ-701 G blocked-sites rule, plus C11), WQ-694 and WQ-681 (news-lane schedule, C7), and WQ-691 (follows from my WQ-690 ruling 50 minutes earlier).
   If you disagree with any of these, tell me which and why in one line. Do not open a queue row about it.

3. When your own recommendation text says "you already ruled", "matches the NNN ruling" or "your standing rule", treat that as the sign the item is a receipt, not a question.

4. A ruling I give in a desk's window is recorded under C2. Do not ask me again in your window. This happened with WQ-179, 565 and 570.

5. Nothing changes for trades, money, keys, accounts, root CLAUDE.md, your own charter, gate levels, seats, or security and privacy. Those still come to me.

At your next scheduled autonomy review (due 2027-02-11), report how many items reached me per week since 11/18 and how many you recorded as receipts. Do not add a new measurement before then.
```
