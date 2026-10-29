# FERT vs mature peers — structure comparison (2026-10-28 22:53 ET, Will-directed)

**Scope:** files and folders only. This is a FERT self-comparison, **not a maturity grade**; DAEDALUS owns grading (`AGENTS/DAEDALUS/FLEET_MAP.tsv`). Peers chosen from FLEET_MAP: BRENT (L5/M, commodity sibling), LABOR (L5/H), HANS (L5/H), CARL (L4/H, FERT's downstream consumer). FERT = L4/M (scored 2026-10-21).

## Measured side by side (read 2026-10-28)

| | FERT | BRENT | LABOR | HANS | CARL |
|---|---|---|---|---|---|
| Level / conf | L4/M | L5/M | L5/H | L5/H | L4/H |
| Directory size | 12M | 190M | 3.9M | 3.2M | 46M |
| Commits, last 30 days | 53 | 365 | 117 | 109 | 194 |
| CLAUDE.md | 20.6 KB | 22.9 KB | 54.1 KB | 24.9 KB | 48.5 KB |
| STATUS.md | 25.8 KB | 22.8 KB | 24.5 KB | 22.1 KB | 24.0 KB |
| KB rows | 109 | 153 | 226 | 148 | 573 |
| Predictions OPEN / total | **0 / 12** | 2 / 31 | 4 / 19 | 5 / 11 | (book, 7 closed) |
| Python scripts | 1 (boot.py) | 12 | 10 | 8 | 16 |
| Tests | none | none found | none found | test_hans.py | 2 test files |
| Calendar / docket | workbook/TRIGGERS.tsv | docket/CATALYSTS.tsv | docket/ + 5 pre-print GRADING_CARDs | thesis/ pre-registration | docket/CATALYSTS + CALENDAR |
| Thesis folder | none (EXIT_PROTOCOL + STATUS vectors) | thesis/ | — | thesis/KILL_TREE | thesis/ |
| Lessons / calibration file | none (post-mortems in PREDICTIONS rows) | LESSONS.md + lessons_check.py | LESSONS.md + PREDICTIONS_SCOREBOARD.md | ML.tsv | brier_audit.py |
| Closeout runner | none (manual) | — | — | scripts/closeout_check.py | — |
| NEXUS_BRIEF.md | none — **by ruling** | yes | yes | none (utility class) | yes |

## Where FERT matches or leads

- **Blueprint required minimums met:** mechanized predictions-due + triggers-due + ledger staleness in one boot (§5 REQUIRED); dated kill rail with channel-kill vs thesis-kill and bidirectional flip (§4); 5-pt score + Independence column (§2); If_Falsified_Action column on every prediction (§5); R1 corrections leg; read cap (25.8 KB of 32.55 KB).
- **Unique discipline:** benchmark + unit + date on every price cell, and an exclusions register naming blind spots. No peer has an equivalent of either.
- **Lean and tidy:** smallest CLAUDE.md of the set; archives in `archive/` (14 files) rather than BRENT's 30+ STATUS archives sitting inside `workbook/`.
- **10/26 buildout gave it peer-grade data layers:** `data/` (5 dated tables), `companies/CF/` (operating history + Q3 prep), `workbook/SUPPLY_EVENTS.tsv`, `DATA_ROUTES.md`, `README.md` index.

## Leaner by design — not gaps

| Absent | Why it is correct |
|---|---|
| NEXUS_BRIEF.md | NEXUS `BRIEFS_MAP.md` line 23 (Will-directed 10/24): FERT has no brief duty; no standing brief proposed |
| Fetch/data scripts | TRIGGERS.tsv header convention (DAEDALUS ⑰ 8/28, accepted 9/2): no standing fetch scripts by design |
| docket/CATALYSTS.tsv | TRIGGERS.tsv is the local form of the same function for an event-driven desk |
| Commit volume | Event-driven class; wakes on named triggers |

## Real gaps vs peers (candidate work — none executed)

| # | Gap | Peer model | Cost | Why it matters |
|---|---|---|---|---|
| 1 | **No pre-registered grading card for the 11/03–11/05 earnings cluster** (Mosaic Q3, CF Q3) | LABOR `docket/GRADING_CARD_*` per print; blueprint §5 print-grading contract (frozen card, two-stage print+call) | ~1 session before 11/03 | The two most informative primaries of the quarter land in 6 days; `companies/CF/Q3_PREP.md` is preparation, not a frozen card |
| 2 | **Zero OPEN predictions** — no calibration loop running | Peers carry 2–5 OPEN | Base-rate first (charter rule) | DAEDALUS: not a maturity failure. STATUS already flags it to PROME |
| 3 | **No calibration scoreboard / lessons file** | LABOR PREDICTIONS_SCOREBOARD + LESSONS.md; BRENT lessons_check.py | Small | 12 resolved rows (5 HIT / 5 MISS / 2 VOID, mostly the March charter) with post-mortems scattered in row Notes |
| 4 | **No closeout runner** | HANS `closeout_check.py` (built after a step went silently unrun) | Small script | FERT's 10/28 closeout logged a SKIPPED step by hand; DAEDALUS's named next upgrade is "L5 clean-closeout measurement" |
| 5 | **boot.py has no tests** | HANS/CARL test files | Small | A guard is only trusted after it is falsified (`finding_test_the_guard_not_just_the_guarded`) |
| 6 | **Closeout claim check skips FERT's own ledgers** — root step 1e names CATALYSTS.tsv/CALENDAR.md, which FERT lacks; TRIGGERS.tsv, GATE_GRADES.md, PREDICTIONS.tsv, KB.tsv are not in the recipe | — | One-line recipe change | Ran 10/28 22:53: all 4 clean. Gap is in the recipe, not the data |

**DAEDALUS's own L5 ask for FERT** (FLEET_MAP, 10/21): an independently read clean closeout. Gaps 4 and 6 bear directly on that; gap 1 is the time-sensitive one.
