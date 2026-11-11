# Table checker: declared whole-read classes

Written before implementation, 2026-11-11 closeout. `reads: 2` in this distinct repair episode.

The Standard gate blocks because the checker opens `PROME/inbox/*.md` literally. READS already permits file classes; read_cap_check.py owns their expansion and distinguishes historically populated but currently empty classes from typos or unavailable history. Repair this existing consumer; do not remove the declared row or bypass the gate.

Acceptance:
- Scan every current file in a PROME whole-read class, including untracked packets; detect an over-celled member.
- Keep other readers and scoped rows outside this perimeter; concrete whole-read paths retain their current missing/unreadable rc 2 behavior.
- Reuse read_cap_check's class expansion and history discriminator. An empty class with committed history is explicitly reported empty, not a scanned file. A never-matched class or unavailable history returns UNKNOWN/rc 2.
- Preserve table parsing and explicit CLI file behavior. Overlapping concrete/class entries may be scanned twice; no member is silently excluded.

Neighbours: ordinary clean and defective members; overlap concrete plus class; wrong-owner/scoped rows; missing concrete, typo class and unavailable history; concurrent deletion after expansion remains rc 2. An arrival after enumeration is outside this single-pass snapshot; no atomic census is claimed.

Required result: original suite plus focused manifest-class tests, actual default checker, independent reader with its own counterexample, then full Standard gate. IMPLEMENTED/TESTED/INDEPENDENTLY VERIFIED remain pending; no new rule, threshold, watcher or manifest exclusion.

## Result

Independent read 1, 2026-11-11: fresh Codex gpt-6.1-sol helper `/root/table_reader`, ACCEPT, zero blocking findings. Ten independent counterexamples passed (actual nonrepository Git history, simulated timeout/zero history, historical-empty plus concrete count, multiple members/directory exclusion, PermissionError, missing concrete after a class, recursive and ? classes, explicit CLI); focused author tests rerun 7/7. Source limits: positive-history and timeout use subprocess fixtures; no atomic arrival census claimed. Explicit read-only closeout received.

IMPLEMENTED: uses existing read_cap_check class expansion/history policy. TESTED: original plus focused suite 33 passed; live default checker rc 0, six files scanned and empty historical inbox class explicitly named. INDEPENDENTLY VERIFIED: bounded counterexamples above. STILL UNRESOLVED: final Standard gate and delivery pending; no clean gate claim yet. Operational ARGUS delta review will inspect the added code/receipt in the final closeout candidate.

Independent read 2: operational ARGUS delta audit reviewed the code/tests/acceptance with no code finding; its one lifecycle-row finding was corrected and rechecked separately. Final Standard gate rc 0 and verified delivery 8ac7c902b39ffbf293c870889e2270c8e7cd95d5. STILL UNRESOLVED: no bounded repair blocker; inherited class-history/snapshot limitations remain. This paragraph records subsequent verification, not a new code edit.
