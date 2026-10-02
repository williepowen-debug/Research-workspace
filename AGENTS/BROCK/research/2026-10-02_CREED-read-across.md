# CREED → BROCK read-across · 2026-10-02 (Will-directed)

**Scope read:** `AGENTS/CREED/CLAUDE.md` (whole), `MAINTENANCE.md` entries 9/26–10/1, CREED `scripts/` + new dirs (`catchups/ cases/ notes/ evals/ analysis/`), CATO run list. 117 CREED commits since 9/15, mostly domain work; this memo covers the **structural** changes only. **Nothing below is adopted.** Charter edits are Will's word.

## Ranked: what transfers, with the BROCK evidence that it is needed

| # | CREED change | BROCK evidence (measured 10/2) | Fit |
|---|---|---|---|
| 1 | **Self-check ①: a fired trigger must show a fire marker on every surface that names it** + **"a grade is not a propagation"** (charter trap #8, 9/30). | `VX-BRK-004` (Fund Gates Count) still reads *"THREE VEHICLES AT 2 … [9/3]"*, missing BOTH R2 fires (North Haven 9/25, OCIC 10/2). The register header lines 12–13 still carry the 9/3 run state unbannered. I repeated the miss today. | **High** |
| 2 | **Self-check ②: asserted counts vs actual.** | The BROCK charter says PREDICTIONS.tsv = 48,681 B (actual **50,018**) and board_log = 89,476 B (actual **112,887**). The SCRATCH header says *"Updated 2026-09-03"* on a file last committed 10/2. | High (cheap) |
| 3 | **STATUS hot/cold split**: STATUS = header + §Standing Obligations + BOTTOM LINE; each session's narrative → `catchups/YYYY-MM-DD.md`; `catchups/INDEX.md` marks CURRENT; boot step names the INDEX (re-pointed **in the same commit**); **audit by obligation, not bytes**. | BROCK STATUS 29,437 B = **90%**; the split is already owed (ARMED block). Six CREED byte rotations each bought 0.1–2.3 KB against ~7–9 KB of growth per session, which is the same treadmill BROCK is on (rotations 9/2, 9/12, 9/18, 9/21, 9/25, 10/2). | **High** |
| 4 | **Byte budget replaces line counts.** CREED retired its "300/320-line" rule and cited BROCK's 250/280 as the pattern it was copying. | BROCK STATUS is **136 lines** and 90% of bytes, so the ≤250/280-line rule can never fire. It is a dead guard. | High (cheap) |
| 5 | **ALWAYS-LOADED standing traps block** in the charter body. Rationale (from HENRY's eval suite): *a principle expressed as a BOOT STEP is not in the always-loaded surface*. A trap earns a place only by having bitten while a number was being written. | BROCK's write-time traps live in `LESSONS.md` (a boot step, 95% of budget): #25 fill-rate ≠ price, #34 name the denominator/basis, #37 attribution by summarizer, plus today's form-type resolver. These fire at **write time**, not boot. Moving ~5 of them into the charter would also let LESSONS rotate. | High (charter = Will) |
| 6 | **SCRATCH = handoff surface, read FIRST, overwritten not appended, lowest authority.** | BROCK SCRATCH is **47,134 B (145%)**, says *"Read at boot (after STATUS)"* but is **not in the boot order**, and is appended to as a session log. | Medium-High |
| 7 | **Boot-time threshold scan** (`threshold_scan.py`): current vector values vs frozen bands **before work starts**; prints an UNSCANNABLE register; a TRIPPED line means "go grade at primary", never a fire. Root cause it fixed: CREED held a number with its band written down for ~6 weeks and nothing connected the two. | Same shape at BROCK: Duration's first close >5.00 was 9/16, noticed 9/25; North Haven's R2 fire found 7 days late. ⚠️ Most BROCK triggers are filing events, not numeric bands, so a scan covers only HY/10Y/CCC-BB-type rows. Its value is mostly the unscannable register. | Medium |
| 8 | **Notes hot/cold split** (`notes/VX_NOTES.md`, `PREDICTIONS_NOTES.md`, `FLOW_NOTES.md`): long cells moved verbatim + crc; hot cell keeps current state + the load-bearing caveat **written by hand** (a mechanical cut dropped a caveat). | PREDICTIONS.tsv 50,018 B (154%, declared `scoped`, so not a breach). CREED took its own from 81% → 47%. | Medium |
| 9 | **`LEDGER_GLOB`** declaring which ledgers are under staleness enforcement. | BROCK has none, but root closeout step 1c-bis reads it. `docket/` and `registry/` are outside any declaration. | Medium (cheap) |
| 10 | **VX_HISTORY with Role/Basis: one CANONICAL row per vector per observation period** (Date = observation period, never pull date). This is what lets a counter say "n=X/12" for base-rating. | BROCK VX_HISTORY is a 15-row field-change log, last refreshed 8/07; it cannot count observations. | Low-Medium |
| 11 | **PREDICTIONS + SCOREBOARD: both writes or neither**; `STUCK` = status change, never a confidence cut; `RESOLVED-PARTIAL` token (excluded from Brier). | BROCK has no scoreboard file. CREED's rule cites BROCK's own BRK-29 (open 5 days past resolve). | Low-Medium |
| 12 | **evals/**: two INPUT+RUBRIC cases testing traps cold. | None at BROCK. | Optional |

## Does NOT transfer
- `cases/` named-case ledger (CRE loss sales). A PC analogue (named realized-loss/markdown events feeding BRK-25's count) is conceivable but not evidenced as needed.
- `trepptalk_sweep.py`, `s8a_relative.py`, `import_cre_workbook.py`: CRE-specific.
- `scripts/boot.py`: **RETIRED by CREED 9/02** (keyed on mtime). Do not copy it.

## Sequencing if adopted
① VX-BRK-004 + register-header propagation fix (my files, factual; no charter change) → ② STATUS split per #3/#4 (already owed; one structural session + cold read) → ③ charter batch for Will: #5 traps block, #4 line rule → bytes, #6 SCRATCH in boot order, #2 stale byte figures → ④ `brock_selfcheck.py` (#1 + #2) falsified against today's VX-004 miss before adoption → ⑤ #8/#9/#10 as capacity allows.
