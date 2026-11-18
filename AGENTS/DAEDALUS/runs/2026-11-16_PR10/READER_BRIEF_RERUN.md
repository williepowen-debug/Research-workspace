# Production Review #10 — reader brief (re-run after the 11/16 restart)

**Written:** 2026-11-18 10:4x ET by DAEDALUS. Reconstructed from the structure of the surviving reader files (`reader_A.md`, `reader_E.md`) and `sweeps/PRODUCTION_REVIEW.md` step 2; the 11/16 brief text itself was not saved (disclosed). Lost cohorts B, C, D, F re-run; C and D (9 and 10 desks) split in half to keep each report whole.

**Pinned cutoff (new):** `208bd704ea` (PROME closeout 11/17 evening). **Period:** 2026-11-02 00:00 to cutoff. Readers A and E used cutoff `916e683f5d` (11/16 20:58 ET); the difference is disclosed at assembly.

| File | Cohort |
|---|---|
| reader_B.md | TERRY, RED, NEXUS, HENRY, LABOR, CARL |
| reader_C1.md | REGINALD, LIQUID, BROCK, GIBBS, OZK |
| reader_C2.md | WAL, FLG, CREED, SHADE |
| reader_D1.md | VIOLET, BRENT, SAM, BOND, ZHAO |
| reader_D2.md | HANS, VULCAN, WATT, MIDAS, FERT |
| reader_F.md | OTTO, CORAL, MARCO, AEOLUS, HOMER, CRUISE |

## Rules for the reader

- **Read-only** against the repository. Do not edit, stage, commit, pull or stash anything. Your ONLY write is your own report file at `AGENTS/DAEDALUS/runs/2026-11-16_PR10/reader_<X>.md`. Other desks may be live and committing; read at the cutoff with `git show 208bd704ea:<path>` when the working tree differs.
- Ladder: `AGENTS/DAEDALUS/OPERATIONS.md` § MATURITY LADDER (floor L0–L2; class ceilings L3–L5; reading A = trade leg, reading B = any current-judgment section passes L1; mechanical-QC leg N/A). Enumerate EVERY ladder leg with a per-leg verdict; a skipped leg is NOT-ADJUDICATED.
- Each desk's current row: `grep -P '^<NAME>\t' AGENTS/DAEDALUS/FLEET_MAP.tsv` (read the header line for column names). Its profile: `AGENTS/DAEDALUS/profiles/<NAME>.md` (the **Staleness:** line names its trigger).
- Read the desk's STATUS delta and key commits in the period (`git log --after='2026-11-02 00:00' 208bd704ea -- AGENTS/<NAME>/`). Grade content, not filenames. Do not over-grade mechanically; say "confirm-read owed" where you did not do a full read.
- **REACHABILITY:** for every Next_upgrade leg and Conf gate, ask whether the desk can do it in its own tree and whether the trigger can fire at the right time. A gate keyed to a retired instrument, another desk's work, or a date with no occurrence precondition gets re-cut, not carried.
- A Gaps/Next_upgrade cell states what is TRUE NOW; history goes elsewhere. Write normal spaced words.
- Cite every claim with `path:line` or a commit hash. Take figures from commands, never from memory.
- GIBBS only: carry Will's WQ-692 ruling (GIBBS stays; premise widened) — `git show 73649fee80`.

## Report format (per desk, as in `reader_A.md`)

`## <NAME> (<Class>, map L<n> / <Cf>, last scored <date>)` then:
- (a) Commits in period: count + structural events table (date · event · evidence)
- (b) Current Gaps / Next_upgrade claims: table (# · claim · verdict STILL-TRUE / OVERTAKEN / RESOLVED / STALE FORM · evidence)
- (c) Proposed replacement cells: Gaps, Next_upgrade (and any other cell that is wrong), as exact text
- (d) Grade verdict — RETAIN / RAISE / LOWER L<n> / <Cf>: per-leg table (leg · verdict · basis)
- (e) Profile trigger: date-age and content trigger, FIRED or not, and whether a bounded delta can carry it
- (f) Cross-agent observations (things another desk or PROME should act on)

End with `## Not read / limits` (a table of what you did not read or run) and a final line `END OF REPORT`.
