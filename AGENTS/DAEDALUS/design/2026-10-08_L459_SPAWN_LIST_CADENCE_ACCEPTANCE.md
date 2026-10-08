# L459 — acceptance conditions for the `spawn_list.py` cadence-reader repair (DAEDALUS, 2026-10-08)

**Row:** DOCKET L459 (due 2026-10-07; this is one day late). PROME owns `PROME/tools/spawn_list.py` and the fix. DAEDALUS owns the cadence design (`design/2026-09-08_DESK_CADENCE_SPEC.md`). WQ-229 requires acceptance conditions **before** the fix, and an independent reader after it. **Read at:** `spawn_list.py` HEAD `f2d5733de` (`read_cadence` l.205–230, `cadence_note` l.241–268, `Liveness` l.164–192); `PROME/ROSTER.md` cadence heading at l.200.

**Measured on the live ROSTER (read_cadence called directly, 10/8):** the cadence section bounds correctly today (65 lines, no inner level-3 heading). That holds only by layout: the heading is `### DESK CADENCE`, the code splits on the substring `"## DESK CADENCE"` and ends at the next `"\n## "`, so a future `###` table placed after it would be swallowed. The section yields 38 desks, 0 duplicates and **6 "bad" entries, which are the token-definition rows** (`DAILY` → "REVIEW HINT PAST ONE CALENDAR DAY", … `UNDECLARED`). That is F5 as it presents today: the token table is parsed as desks with unknown tokens. *(An earlier draft of this paragraph named the section boundary as the root of R2/F5 without testing it. The test refuted it, and the boundary is now a latent condition, case A-BOUND.)*

## Invariants (each must hold before and after the fix)
- **I1** Cadence is an annotation only. On the same DOCKET/GATES input, every row's `class`, the DARK set and the exit code are byte-identical with the ROSTER cadence section removed, present, or malformed (spec §3/§5/§6).
- **I2** No non-evaluable path prints a clean annotation. Every one prints `CANNOT-EVALUATE (<named cause>)`.
- **I3** Fixtures are frozen strings in the selftest, never the live ROSTER.

## Acceptance cases (fixture input → required annotation)

| Id | Defect | Fixture | Must print | Must NOT print |
|---|---|---|---|---|
| A-R2 | A later table re-names a declared desk; the declaration is lost as a "duplicate" | `### DESK CADENCE` table with `ALPHA` WEEKLY, then `### OTHER` table whose first column also lists `ALPHA` | ALPHA → `WEEKLY — …` | `duplicate ROSTER identity` |
| A-F5 | The token-definition table parses as desks | Cadence section that holds a token table (`\| Token \| Meaning \|`, rows `DAILY`, `WEEKLY`…) and a desk table; desk `BETA` absent from the desk table | BETA → `CANNOT-EVALUATE (desk absent from ROSTER cadence)`; `DAILY`/`WEEKLY` are never keys in the cadence map | any desk annotated off a token-table row |
| A-F5b | Undeclared default | Desk table row `GAMMA` `UNDECLARED` | `UNDECLARED — CANNOT-EVALUATE …` | `absent from ROSTER cadence` |
| A-F6 | Duplicate plus bad token: the second copy is kept and the duplicate is never named | `DELTA` WEEKLY, then `DELTA` `WEEKLYY` in the same table | DELTA → `CANNOT-EVALUATE (duplicate ROSTER identity)` | `unknown token`; any `WEEKLY — within/REVIEW` |
| A-F6b | Order reversed | `DELTA` `WEEKLYY`, then `DELTA` WEEKLY | the same duplicate annotation | as above |
| A-F7 | Bold or lower-case names silently dropped | Rows `**HANS**` WEEKLY and `hans` WEEKLY (separately) | HANS → `WEEKLY — …` for each; if both rows appear together → duplicate | `absent from ROSTER cadence` for HANS |
| A-F8 | A failed `git log` reads as "no qualifying owner commit" | WEEKLY desk; `Liveness` returns the `("!ERR", …)` sentinel | `CANNOT-EVALUATE (git log failed: <first stderr line>)` | `no qualifying owner commit` |
| A-F11 | Stale docstring l.38–44 says cadence is "NOT modelled in v1" and instructs the forbidden inference | Text check | Docstring describes the WQ-269 annotation and states it never changes class | the strings `NOT modelled in v1` and `When the column lands, DARK requires` |
| A-F12 | Dates come from committer-local time, not America/New_York | A commit with committer date `2026-10-08T23:30-07:00` (= 10/09 02:30 ET) and `--as-of 2026-10-09` | age computed from the **ET** date 2026-10-09 → `0d` | `1d` |
| A-BOUND | Latent: the section ends only at a level-2 heading | `### DESK CADENCE` desk table, then `### NEXT` table listing `ZETA` with token `WEEKLY` | ZETA → `CANNOT-EVALUATE (desk absent from ROSTER cadence)` | ZETA → `WEEKLY — …` |
| A-ROSTER | The live ROSTER parses with the fix | Live run, `--horizon 30` | zero annotations caused by a non-desk row; the set of `absent from ROSTER cadence` desks equals ACTIVE+TIER-2 desks missing from the cadence table, listed by name | — |

**Capable case required for each fixture:** run it on the pre-fix code and record that it fails as described (CHECK_STANDARD §3). A case that also passes on the old code proves nothing about the fix.

**Watched today, before any fix (live, `--tsv --horizon 30`):** 116 rows. Annotations: WEEKLY within cadence 45 · n/a 39 · ON-DEMAND 14 · EVENT-DRIVEN 10 · WEEKLY REVIEW HINT 6 · DAILY within cadence 1 · CANNOT-EVALUATE 1. The one CANNOT-EVALUATE is DOCKET L154, owner token `STUE` ("desk absent from ROSTER cadence"). That is an owner-cell parse (`owner_token`), not a cadence-table defect, and is outside L459. PROME should look at it separately.

**Out of scope here:** whether the WEEKLY boundary (exactly 7 days = within) is right. That is spec §4 and already ruled. Converting the single table into a literal ROSTER column is also out of scope; PROME's l.204 note offers it, and DAEDALUS does not ask for it.
