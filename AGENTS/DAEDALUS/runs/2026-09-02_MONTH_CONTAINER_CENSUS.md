# Month-named rolling containers — fleet census (detection-only) — 2026-09-02

**Trigger:** PROME routing 9/2 ~10:3x ET off MIDAS's self-flag (`analysis/LESSONS_ARCHIVE_2026-08.md` holds September lessons because MIDAS `CLAUDE.md` closeout step 4 names that path). **Method:** two read-only greps over `AGENTS/` + `PROME/`: (A) instruction files naming a `*_2026-0M.md` archive path; (B) files named for one month whose block headers carry the next month. Then the population of month-only-named files, classified rolling vs. closed. **Nothing edited outside my dir.**

## Root cause is MINE (PAT-050)
`BLUEPRINTS/STATUS_TWO_STATE_PILOT.md:46` prescribes the rotation target as **`status_archive/STATUS_ARCHIVE_<YYYY-MM>.md`**. A month in a filename asserts a CLOSED range; a rotation instruction that names it makes it a ROLLING target. The two cannot both hold past the month boundary, and nothing in the pilot said what happens on the 1st. The three pilot seats (WATT · HENRY · CARL) and MIDAS (8/27 split) adopted the form. My own `CLAUDE.md:156` uses `STATUS_ARCHIVE_<date>.md` (day-dated, closed) — a different convention from the one I handed the fleet.

## Confirmed instances (month container holding next-month bodies)
| File | Size | Next-month content | Instruction that aims writes at it |
|---|---|---|---|
| `AGENTS/CARL/status_archive/STATUS_ARCHIVE_2026-08.md` | 202,417 B | ROTATION #2 and #3 blocks dated 2026-09-01 (lines 207–232) | `CARL/STATUS.md:5` archive pointer (no CLAUDE.md step; rotation done live per the pilot) |
| `AGENTS/MIDAS/analysis/STATUS_ARCHIVE_2026-08.md` | 85,381 B | three rotations dated 2026-09-02 (lines 297–322) | `MIDAS/STATUS.md:86` pointer |
| `AGENTS/MIDAS/analysis/LESSONS_ARCHIVE_2026-08.md` | 87,243 B | L-45, L-46 dated 2026-09-02 | **`MIDAS/CLAUDE.md:51` closeout step 4 names the path** (the only instruction-file hit) + `LESSONS.md:3` index pointer |

## At risk (month-named, still the live rotation target, no next-month body yet)
`AGENTS/HENRY/status_archive/STATUS_ARCHIVE_2026-08.md` (81,689 B) · `AGENTS/WATT/status_archive/STATUS_ARCHIVE_2026-08.md` · `AGENTS/DAEDALUS/archive/EVOLUTION_ARCHIVE_2026-08.md` (mine — rotations 8/23, 8/28; next rotation would land September) · `AGENTS/CARL/archive/ROADMAP_ARCHIVE_2026-09.md` (born 9/1, same form, rolls into trouble 10/1) · `AGENTS/MIDAS/analysis/SCRATCH_ARCHIVE_2026-08.md` (declares a closed window 7/12→8/23 — fine as long as nothing appends).

## Not in class (dated snapshots, nothing writes to them)
VULCAN `archive/*_2026-07.md` (CLAUDE.md row 251 describes a closed pre-Aug range) · HANS `research/*_2026-06.md` · MARCO `baselines/*_2026-02.md` · BOND/LIQUID `*_PREREG_2026-07.md` · HENRY/LABOR/CARL-STUE source docs · SAM `ML_ARCHIVE_2026-01.tsv`. List (B) also returned ~25 dated proposals/handoffs mentioning September dates in their bodies — forward references, not rolled blocks; excluded.

## Fix-form (READ_CAP rule 4: owners choose HOW, never WHETHER)
The month in the filename must mean what it says. Two compliant forms:
- **(a) Name by content, split by size** — `STATUS_ARCHIVE.md` (no date) receives rotations; when IT approaches the read cap it is closed with a banner stating its actual range and a fresh `STATUS_ARCHIVE.md` opens. The cap governs the split, which is the axis the cap is about (PAT-086).
- **(b) Keep month names, mechanize the roll** — a boot/closeout check that refuses a rotation into a file whose month ≠ the block's month (the ritual "remember to roll on the 1st" is PAT-055 and will decay).
For the three confirmed files: **do not rename** (pointers on ≥6 surfaces; PAT-091). Add a header banner `RANGE: 2026-08-17 → <open>` stating the true range, and re-point the writing instruction at the successor per (a) or (b). Owner's call.

## Dispositions
- Pilot line 46 amended by me (own file) — form (a) default, (b) permitted, "a date in a filename asserts a closed range."
- CARL · HENRY · WATT · PROME notified (packets, carve-out ①). MIDAS already self-flagged and holds PROME's owner-side instruction.
- Sweep leg: **Staleness #5 (~9/22)** gains "month-named container check" (grep B above) — registered on the STATUS board; playbook edit at the run.
- PATTERNS: PAT-091 extended (a date-bearing path in an instruction is a dated carry item) with the PAT-050 self-inclusion note.
