# Owner-unconsumed boot line (S1): desks dark 7 days or more that hold inbox items 7 days or older

Written before the edit, 2026-11-16 12:38 ET (session prome-6f). DOCKET line 730. Authority: WQ-401 RULED APPROVE 2026-10-15 (the build; the hit set keys on dark at PROME's boot, reading (b)); WQ-577 "577 Yes." 2026-10-31 (kept as ONE advisory boot line, nothing more); Will in PROME's chat 2026-11-16 12:29 ET, "Okay go with this", on PROME's stated order of work. Design: `AGENTS/NEXUS/research/2026-10-08_S1_owner-unconsumed-line_DESIGN.md` (definitions §2, acceptance cases §5). `reads: 1` (independent read 1 delivered 12:48 ET; a bounded read of the fix diff follows; history under Result).

The gap, in its own terms: an aged item in a desk's inbox, at a desk that is not running, is visible to nobody. The desk's own boot would show it, and the desk is not booting. PROME's boot gate carries aged waits (WQ-221) and nothing for this. Two recorded instances (DOCKET L304): AEOLUS 9/6 and DEWEY 9/18.

What is built: one function in `PROME/tools/inbox_census.py` that returns the facts, and one ADVISORY line in `prome_gate.py boot` beside the aged-waits check. No ledger, no state file, no new script; the CLI output of `inbox_census.py` is unchanged.

Scope cut under WQ-577 (one line, nothing more), each NOT built and said so:
- the design's multi-line block (one line per desk) is folded into the gate's single line, ACTION-bearing desks first, at most eight desks named and the rest counted;
- the design's repair of the WQ-221 check's liveness source (its item ②) is not made here;
- the `due:` line in WALTER's handoff template (item ③) is WALTER's and is not asked for here; the `due:` exclusion itself IS built (A4).

Acceptance (design §5 cases, restated for the one-line form):
- A1. Replay, AEOLUS at the 2026-09-06 tree with liveness as of that date: AEOLUS is named with at least one ACTION item (design: 6 items, oldest 9 days, dark 10 days, 1 ACTION).
- A2. Replay, DEWEY at the 2026-09-18 tree: DEWEY is named with no ACTION item (design: 13 items, oldest 56 days, dark 8 days).
- A3. A fresh item (under 7 days) at a dark desk does not make the desk a hit and is not counted in the aged count.
- A4. An item whose first 15 lines carry a field `due: YYYY-MM-DD` on or after today is excluded and counted as excluded; a future date anywhere else in the header does not exclude (A5); an ISO-shaped string that is not a real date does not exclude (A6).
- A7. Ties are inclusive on both clocks: age exactly 7 is aged, dark exactly 7 is dark; 6 on either is not.
- A8. A desk with no item prints nothing. A DORMANT desk prints tagged and is never an ACTION candidate. A SPECIAL desk prints tagged "Will-driven", and its ACTION count is labelled "not a PROME launch candidate", never as a drain candidate (AMENDED after read 1, finding 4: the first text said only "prints tagged").
- A9. A desk with a self-commit inside 7 days is not named, however old its items.
- A10. Scaffolding (`README*`, dotfiles, `*MANIFEST*.md`) is skipped and counted as skipped; a file with no date in its name is counted in the desk's item count and never sets the oldest age. (AMENDED after read 1, finding 2:) such a file is never silent: at a desk dark 7 days or more the line names the desk and the count as "undated, age UNKNOWN", and the line is then not ✅. A desk's own standing inbox documents (`PROTOCOL.md`, `RECEIPT.md`) are scaffolding.
- A11. A directory under `AGENTS/` that is not on the roster's ACTIVE, TIER-2, DORMANT or SPECIAL lists is never a hit; if it holds aged items it is named once as outside the perimeter.
- A12. A git failure for a desk reads UNKNOWN for that desk, named on the line; it is never dark and never clean. If every desk is UNKNOWN the line is not ✅.
- A13. Item age: a file in the `WALTER/` lane takes its date and its ACTION or INFO role from WALTER's delivery log when the log has its path; otherwise from the file name (`YYYY-MM-DD` prefix, `SIG-W-YYYYMMDD`, or a Direct Messaging id `MSG-<SENDER>-YYYYMMDD-NNN`, whose `__ACTION__` or `__INFO__` name segment is its role: AMENDED after read 1, finding 1) and, for the role, its `action:` front matter naming the desk. A top-level packet is ACTION-typed when a line in its first 4,000 bytes starts with `**ACTION`, `ACTION:`, `## ACTION` or `## Requested action` and asks for something: a line such as `ACTION: none owed` names no work and is not ACTION (AMENDED after read 1, finding 3).
- A14. The line is ADVISORY: it never changes the gate's return code, and it says in its own text that a hit is a backlog fact and a launch candidate at most, never an authorization. If the check itself fails it prints UNKNOWN with the error, never ✅.
- A15. Zero qualifying desks and no UNKNOWN: one ✅ line carrying what was searched (desks, items, skipped, excluded).
- A16. Nothing else in the gate changes: the same checks run in the same order with the same classes; `inbox_census.py <DESK>` prints what it printed before.

Neighbours:
- Ordinary: A1, A2, A15.
- Overlap: a desk with both ACTION and untyped aged items (named once, ACTION count shown); an item both aged and `due:`-excluded (excluded wins, A4); a lane file present in the delivery log under another recipient's path (only its own path counts, A13).
- Wrong owner: A11 (retired and archive directories); a `DESK:` line inside another desk's commit body must not read as that desk's self-commit (the liveness source already attributes by subject and path; one test).
- Missing information: A10 (no date in the name), A12 (git error), an unreadable delivery log (file-name fallback, said on the line), an unreadable roster (UNKNOWN, A14).
- Concurrent activity: N/A for writes (read-only, no state). A desk that commits while the check runs is read at whatever instant git answers; the line is a boot-time fact with its date.

Required result: unit tests for A3 to A15 on temporary trees with a stub liveness; the two replays run once from git history and recorded here; the gate's boot run still passes; an independent reader with its own counterexample before the line is called fixed (it touches the gate).

## Result

Recorded 2026-11-16 12:41 ET by PROME prome-6f. The four states, kept apart:

| State | What holds |
|---|---|
| IMPLEMENTED | `inbox_census.owner_unconsumed` and `render_owner_unconsumed`; `prome_gate.check_owner_unconsumed`, called in `mode_boot` right after the aged-waits check. |
| TESTED | `PROME/tools/tests/test_owner_unconsumed.py`, 12 cases on temporary trees with a stub liveness (A3 to A15), all passing. The two replays from git history, each tree taken with `git archive` at that day's last commit and liveness read as of that day: **A1** AEOLUS 2026-09-06 (tree 7f959541b8): 6 items, oldest 9 days, dark 10 days (last self-commit 2026-08-27 b6281d60e9), 1 ACTION item: the design's figures exactly. **A2** DEWEY 2026-09-18 (tree fd7c86d043): 11 items plus 2 scaffolding files skipped (the design counted 13 with them), oldest 56 days, dark 8 days (2026-09-10 c8413bc65b), no ACTION item: named, and not as a candidate. A16: five existing gate test files pass and leave the tree unchanged; a non-advancing gate refresh printed the line as advisory with the gate's return code 0. |
| INDEPENDENTLY VERIFIED | NOT YET. Read 1 (Agent-tool reader `s1-line-reader`, Opus, read-only, its own fixtures, 23 mutations; ledger `PROME/reports/2026-11-16_owner-unconsumed-line/LEDGER_read1.md`) found 4 blocking and 9 non-blocking, and reproduced both replays and six hand checks on the real tree. The fixes below were made after that read (2026-11-16 12:53 ET) and are unreviewed until read 2 is recorded here. |
| STILL UNRESOLVED | The scope cuts listed above (the WQ-221 check still uses its own, weaker liveness source). The ACTION recogniser for top-level packets is a four-form match over free text, the design's own declared weak leg: a packet that asks for work in other words is counted as backlog and not as ACTION. |

What the line printed on today's tree (2026-11-16 12:41 ET): RAV [SPECIAL] 6 items, oldest 104 days, dark 103 days, 2 ACTION · BARON [DORMANT] 1 item, oldest 96 days, dark 277 days · outside the roster perimeter with aged items: YEYOU 4 · searched 44 desks, 191 items, 14 scaffolding files skipped, 0 excluded by a due date. No ordinary desk qualifies today: the five desks holding unread packets since 11/11 are 5 days in, under the 7-day line on both clocks.

Read 1's blocking findings and what changed (2026-11-16 12:53 ET):

| # | Finding | Change |
|---|---|---|
| 1 | Direct Messaging files (`MSG-PROME-YYYYMMDD-NNN__ACTION__…`, the live PROME to BRENT and PROME to SAM route) got no date and no role: a 32-day-old ACTION message at a dark desk read ✅. | `item_date` reads the message id's date; the name's role segment decides ACTION or INFO. Test. |
| 2 | A file with no date in its name was never aged and never mentioned: a dark desk whose only item was an undated request read ✅. | Undated items at a desk dark 7 days or more are named with their count and the line is not ✅. `PROTOCOL.md` and `RECEIPT.md` (eight real files, each a desk's own inbox document) join the scaffolding set. Tests. |
| 3 | `ACTION: none owed` and its kin counted as ACTION (one of RAV's two on the real tree; 59 processed packets use the form). | A line in the ACTION form whose text after the colon begins none, n/a, not required, no action, no reply, or nothing owed, required, needed or to do, is not an ask. Tests with wordings taken from real packets. |
| 4 | A SPECIAL desk printed as an ordinary drain candidate; the design's qualifier was dropped. | SPECIAL prints "[SPECIAL, Will-driven]" and its ACTION count reads "not a PROME launch candidate". Test. |

What the line prints on the real tree after the fixes: RAV [SPECIAL, Will-driven] 6 items, oldest 104 days, dark 103 days, 1 ACTION (not a PROME launch candidate) · BARON [DORMANT] 1 item, 96 days, dark 277 days · searched 44 desks, 183 items, 22 scaffolding files skipped. (YEYOU's four packets were filed 12:42 ET on Will's word and no longer appear.)

Declared residue (read 1's non-blocking findings NOT fixed, 2026-11-16 12:53 ET; the reader's, with its ledger wording in brief):
- A real packet whose name contains "manifest" is skipped as scaffolding (the design's own rule; two historical packets).
- The liveness source dates a commit in the committer's own time zone, so an evening commit stamped +0000 lands on the next day and a desk can read one day short of dark at the 7-day tie.
- Inbox subfolders other than `WALTER/` are treated as lanes and checked with the lane ACTION forms only; a subfolder named `Processed/` or `archive/` would be counted as backlog.
- The `due:` recogniser is strict (lower case, nothing after the date), which errs toward reporting.
- If the roster parsed only in part, the line could still read ✅ over the desks it did parse.
- Untested properties the reader's surviving mutants exposed: ACTION-first ordering among several desks, later delivery-log rows winning, outside-perimeter desks listed only when aged, oldest meaning the maximum age.
- "n item(s)" counts fresh items with aged ones.
- Each inbox file is read whole before its first 8,000 bytes are used.
- An ACTION line that says "none today" and then names later work on the same line is read as no ask; an ask written with ACTION in mid-line is not recognised (RAV's 10/31 packet): the design's declared weak leg.
