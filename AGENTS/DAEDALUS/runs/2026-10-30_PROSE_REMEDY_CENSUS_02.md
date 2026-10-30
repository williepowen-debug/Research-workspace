# Prose-Remedy Census #2 — 2026-10-30 (due 10/29, 1d late)

**Perimeter:** ROSTER ACTIVE + TIER-2 + SPECIAL charters and their STATUS/SCRATCH/CANARY_MAP/MAINTENANCE/LAST_COMPLETION (DAEDALUS included). **Step 1:** `scripts/prose_remedy_candidates.py` (selftest 21/21) at HEAD c1ad5137f → 165 candidate rows, `2026-10-30_PROSE_REMEDY_CENSUS_02/…_CANDIDATES.tsv`. **Step 2:** two non-owner Opus classifiers, every row opened at its line, every BUILT/PROSE-REMEDY checked against code: `…_A-M.md` (74 rows, 20 desks) and `…_N-Z.md` (91 rows, 18 desks). 0 rows NOT READ. DAEDALUS spot-checked the LABOR rows and the brief-pin claim at the artifacts (both hold).

## Result

| | A–M | N–Z | Total |
|---|---|---|---|
| Candidates | 74 | 91 | 165 |
| PROSE-REMEDY rows (distinct) | 18 (13) | 14 (12) | 32 (25) |
| of which LOW, distinct (unenforced STATUS line cap the byte budget dominates) | 10 | 5 | 15 |
| BUILT | 18 | 26 | 44 |
| DIAGNOSIS-ONLY / DECLINED | 0 / 0 | 2 / 7 | 2 / 7 |
| FALSE (step-1 FP rate) | 38 (51%) | 42 (46%) | 80 (48%) |

Run #1 → #2: the Amendment-10 brief-ordering class is CLOSED fleet-wide by the shared `scripts/brief_pin_check.py` (CARL, FALCON, LABOR, MARCO, NEXUS, OTTO now name it); 8 of run #1's 12 N–Z remedies are BUILT.

## Non-LOW remedies and dispositions

| Desk | Surface line | Carry (sessions) | Disposition |
|---|---|---|---|
| LABOR | `CLAUDE.md:24` + `:65` B5b unconsumed grading-card list (filename date ≤ today AND still at `docket/` top level) | 53 | packet |
| LABOR | `CLAUDE.md:52` B5 STATUS calendar vs `docket/CATALYSTS.tsv` event-set equality | 77 | packet |
| LABOR | `CLAUDE.md:87` C2-0 row selection (OPEN, confidence ≥60%, unmoved ≥60d) | 50 | packet |
| NEXUS | `CLAUDE.md:155` Will-facing page ≤6 KB, lead ≤150 words | 14 | packet |
| ORACLE | `MAINTENANCE.md:230` `polymarket.py pull` reports a RESOLVED market as PINNED BUT NOT FOUND (`scripts/polymarket.py:478-481`) | 10 | packet |
| ORACLE | `CLAUDE.md:65` STATUS under 250 lines — NOT dominated (≈118 B/line, bytes bind near 276 lines), nothing counts it | 27 | same packet |
| RED | `CLAUDE.md:68` CALENDAR.md event set == `docket/CATALYSTS.tsv` | 35 | packet |
| RED | `CLAUDE.md:162` hypothesis table ≥4 scenarios, each 2–60% | 43 | packet |
| PROME | `CLAUDE.md:51` WQ-206 aged-ACTION check | 47 | no packet — Will-approved build already DOCKET L730 (PENDING) |
| SAM | `MAINTENANCE.md:616` KOYOMI runway tripwire | 23 | no packet — the owner gated it on Will deciding the KOYOMI pattern; recorded only |

**Fleet-level (to PROME, not per desk):** 15 distinct items across 14 desks are a "STATUS under 250 lines" cap that nothing counts and the byte budget already dominates. Five owners already resolved theirs by moving to the computed byte budget. Recommendation: one charter-pattern edit at each desk's next touch, naming `scripts/read_cap_check.py --agent <NAME>` at the step or declaring the line count a heuristic. Building a line counter is not recommended. REGINALD and ZHAO already wrote that bytes bind; classed DECLINED-BY-DESIGN (weak).

## Step-3 sentence

0 rows typed by this run; premise-verified at the source for 0 of 0. The census proves which remedies are written and unbuilt, not that any remedy is right.

## Step-1 refinement owed (not applied this run)

**Recall miss:** RED `MAINTENANCE.md:880` ("Nothing compares `boot.py`'s METRIC_MAP source against each row's `instrument_basis`", run #1 item A5, still unbuilt) is absent from the candidate list. Cause, verified 10/30: `V1` and `V2` in `prose_remedy_candidates.py` compile without `re.I`, so a capitalized, sentence-initial token never matches. The fix (case-insensitive tokens) widens the population, so per playbook §5 it ships only with a fleet before/after diff, at run #3. **Precision:** 26 A–M FALSE rows are signal/threshold table cells; scoping form 2 to boot/closeout step lines would cut most of them, also at run #3 with a diff.

**Side observations (reader N–Z, not counted, not chased):** `ledger_staleness.py` prints no row for ORACLE `HISTORY.tsv`; WATT `power_watch.py` near-peak cutoff 95% matches neither charter band (90% / 97%); LIQUID STATUS at 92% of byte budget and its charter never calls `read_cap_check.py` (reader A–M).
