# Owner-unconsumed boot line (S1): desks dark 7 days or more that hold inbox items 7 days or older

Written before the edit, 2026-11-16 12:38 ET (session prome-6f). DOCKET line 730. Authority: WQ-401 RULED APPROVE 2026-10-15 (the build; the hit set keys on dark at PROME's boot, reading (b)); WQ-577 "577 Yes." 2026-10-31 (kept as ONE advisory boot line, nothing more); Will in PROME's chat 2026-11-16 12:29 ET, "Okay go with this", on PROME's stated order of work. Design: `AGENTS/NEXUS/research/2026-10-08_S1_owner-unconsumed-line_DESIGN.md` (definitions §2, acceptance cases §5). `reads: 0`.

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
- A8. A desk with no item prints nothing. A DORMANT desk prints tagged and is never an ACTION candidate. A SPECIAL desk prints tagged.
- A9. A desk with a self-commit inside 7 days is not named, however old its items.
- A10. Scaffolding (`README*`, dotfiles, `*MANIFEST*.md`) is skipped and counted as skipped; a file with no date in its name is counted in the desk's item count and never sets the oldest age.
- A11. A directory under `AGENTS/` that is not on the roster's ACTIVE, TIER-2, DORMANT or SPECIAL lists is never a hit; if it holds aged items it is named once as outside the perimeter.
- A12. A git failure for a desk reads UNKNOWN for that desk, named on the line; it is never dark and never clean. If every desk is UNKNOWN the line is not ✅.
- A13. Item age: a file in the `WALTER/` lane takes its date and its ACTION or INFO role from WALTER's delivery log when the log has its path; otherwise from the file name (`YYYY-MM-DD` prefix or `SIG-W-YYYYMMDD`) and, for the role, its `action:` front matter naming the desk. A top-level packet is ACTION-typed when a line in its first 4,000 bytes starts with `**ACTION`, `ACTION:`, `## ACTION` or `## Requested action`.
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
| INDEPENDENTLY VERIFIED | NOT YET. An independent reader is owed before this is called fixed. |
| STILL UNRESOLVED | The scope cuts listed above (the WQ-221 check still uses its own, weaker liveness source). The ACTION recogniser for top-level packets is a four-form match over free text, the design's own declared weak leg: a packet that asks for work in other words is counted as backlog and not as ACTION. |

What the line printed on today's tree (2026-11-16 12:41 ET): RAV [SPECIAL] 6 items, oldest 104 days, dark 103 days, 2 ACTION · BARON [DORMANT] 1 item, oldest 96 days, dark 277 days · outside the roster perimeter with aged items: YEYOU 4 · searched 44 desks, 191 items, 14 scaffolding files skipped, 0 excluded by a due date. No ordinary desk qualifies today: the five desks holding unread packets since 11/11 are 5 days in, under the 7-day line on both clocks.
