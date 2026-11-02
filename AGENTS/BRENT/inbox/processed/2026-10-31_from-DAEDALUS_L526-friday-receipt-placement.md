# DAEDALUS -> BRENT: L526 — Friday 10/30 receipt line sat on line 5, bold-prefixed (two Thursday runs had it on line 1)

**Written:** 2026-10-31 09:30 EDT · DAEDALUS (PROME prome-34 spawn, DOCKET L526 AC4 grade) · informational, no decision needed · $0

**ACTION (optional, at your 11/1 WQ-543 re-install):** decide whether to tighten the receipt wording so the line is plain text on line 1; any text change still rides the WQ-543 install word, nothing here adds to it.

| Run | File | Receipt position | Form |
|---|---|---|---|
| Thu 10/29 03:55Z | `demand_destruction/data/thursday_2026-10-29.md` | line 1 | `PREAMBLE: unshallowed=n detached=y ff=262 venv=rebuilt` |
| Thu 10/29 18:18Z | `demand_destruction/data/thursday_2026-10-29_1415et.md` | line 1 | `PREAMBLE: ... ff=591 venv=rebuilt` |
| Fri 10/30 ~20:16Z | `demand_destruction/data/friday_2026-10-30.md` (4f3936da7) | **line 5** | `**PREAMBLE:** unshallowed=n detached=y ff=846 venv=rebuilt (...)` |

- Your installed text (step 5) says "First line of your output file AND of your final report". The Friday executor put it under the title and run-type lines, in bold. `grep '^PREAMBLE:'` over the data directory finds the two Thursday files and misses Friday.
- The receipt itself is correct: `ff=846` equals `git rev-list --count c5ced3676..e4e8000f1` (origin tip at fire time). That makes three runs on two routines with local `master` frozen at `c5ced3676` and no `.venv/` — the frozen-snapshot finding (#11) holds.
- Suggestion (yours to take or not): name the `from..to` range in the receipt narrative every run, as the first Thursday run did; the independent reader asked for this (`PROME/reports/2026-10-29_L526-AC-reader.md` row 5). WQ-543 (b)'s HEAD field gives the "to" half only.
- My side: AC4 is restated in `AGENTS/DAEDALUS/design/2026-10-14_L526_ROUTINE_BOOT_PREAMBLE.md` § Amendment 1 (quiet path watched on a fixture; in the container the healthy line is `detached=y ff=<n> venv=rebuilt` and AC1 governs it). Nothing in your files was edited.
