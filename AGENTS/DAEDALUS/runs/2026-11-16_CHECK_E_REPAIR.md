# TERRY ledger_sweep check E — ISO-seconds repair, November 16

**Authority:** PROME packet `inbox/2026-11-16_from-PROME_terry-ledger-sweep-check-E-iso-seconds.md` (13:49 ET, on Will's 13:45 ET word to start PROME's examination list; idea row `PROME/ideas/list.tsv:87`) and PROME prome-c4's 20:56 ET message relaying Will's instruction for tonight. Cross-desk edit guards: permission = PROME's ask; idle = TERRY not among live sessions (ListAgents 2026-11-16 ~21:00 ET), last TERRY-path commit f90fcbcd48 19:19 ET, no dirty TERRY files before the edit.

## Defect, reproduced

`check_future_stamps` used `\b([01]?\d|2[0-3]):([0-5]\d)\b`. There is no word boundary between the ISO "T" and the hour, so in `2026-11-16T20:22:46` the regex matched the MINUTES:SECONDS pair and read 22:46. Reproduced before the edit at a pinned clock of 20:30: a stamp written at 20:22 printed `FUTURE-DATED STAMP … reads 22:46`, which blocks a clean closeout.

## Change (one file, `AGENTS/TERRY/scripts/ledger_sweep.py`)

| Element | Before | After |
|---|---|---|
| `TIME_RE` | `\b(H):(MM)\b` | `(?:(?<=\dT)|(?<![\w:]))(H):(MM)(?!\w)`: may start after `<digit>T`, never after a word character or `:` |
| Zone handling | none | `ZONE_AFTER_RE`: an ISO stamp with `Z` or `±hh:mm` after the time is skipped, only when the time follows an ISO `T` |
| Selftests | 119 pass lines | 126 pass lines: 8 new check E cases |

SHA256 before `bd6840b46e2f036fc28d97fc020454e8f03258c3c7c5a0ea44d8112f049aa162`, after `76b57c4c61ab6a3443198415fdaf729b14d4e315fb33662026392a19f4b70c07`.

## Evidence

| Test | Result |
|---|---|
| `--selftest` at the repo root, after | rc 0, 0 FAIL, live run `✅ CLEAN (A–H)` over 155 surfaces (same as before) |
| Mutant 1: old `TIME_RE` restored | 3 discriminating new tests FAIL |
| Mutant 2: zone skip disabled | 2 zone tests FAIL |
| Mutant 3: zone skip without the `T` guard | range test FAILS |
| Control: unmodified copy run outside the repo | fails only the location-dependent "surface parsing to ZERO rows" test, so that failure in the mutants is environmental |

**Independent review** (Opus reader, 46 old-versus-new inputs, verdict ACCEPT-WITH-RESIDUE): the fix is the intended change. It found one new false negative: `Tue **12:20-12:45 ET**` went silent because `-12:45` read as a zone offset. Fixed by the `T` guard plus a selftest. Re-running the reviewer's comparison afterwards: every range row is the same as the old code; all remaining differences are INTENDED (ISO with seconds read as HH:MM; ISO without seconds now caught; explicit-zone ISO skipped). Only importer: `PROME/reports/2026-10-14_TERRY-acceptance/review_checks.py`, which does not use `TIME_RE` or check E.

## Residue, stated

- Local-offset ISO stamps (TERRY's `board_log.tsv` form `…T13:45:58-05:00`) are skipped, so check E does not cover them. The old code never checked them correctly either. Comparing them would need offset conversion and a date-crossing rule. This is a scope change, not done here.
- Check E stays "structured stamps only", per its own header. A clean E is not proof that there is no clock skew.

REVIEW: required (code change to a closeout-blocking check). Independent reader ACCEPT-WITH-RESIDUE; its one regression is repaired and re-verified at the hash above.
