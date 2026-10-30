# Prose-Remedy Census #2 — step 2 classification, desks A–M

**Started:** 2026-10-30 11:31 EDT (from `date`) · **Classifier:** non-owner subagent for DAEDALUS (read-only; this file is its one write) · **HEAD:** c1ad5137f
**Input:** `runs/2026-10-30_PROSE_REMEDY_CENSUS_02/2026-10-30_PROSE_REMEDY_CENSUS_02_CANDIDATES.tsv` rows with desk A–M (74 rows, 20 desks) · **Playbook:** `sweeps/PROSE_REMEDY_SWEEP.md` §2 tokens · **Prior run:** `runs/2026-10-08_PROSE_REMEDY_CENSUS_01_A-M.md`.

## §0 Summary (74 candidate rows · 20 desks · all read)

| Desk | Candidates | PROSE-REMEDY | BUILT | DIAGNOSIS-ONLY | DECLINED | FALSE | Step-1 FP rate (FALSE/cand.) | Desk verdict |
|---|---|---|---|---|---|---|---|---|
| AEOLUS | 13 | 0 | 1 | 0 | 0 | 12 | 12/13 = 92% | `CLEAN (13)` |
| BOND | 2 | 1 | 1 | 0 | 0 | 0 | 0/2 = 0% | PROSE-REMEDY (1: STATUS line cap 108, LOW) |
| BRENT | 1 | 0 | 0 | 0 | 0 | 1 | 1/1 = 100% | `CLEAN (1)` |
| BROCK | 5 | 0 | 2 | 0 | 0 | 3 | 3/5 = 60% | `CLEAN (5)` |
| CARL | 3 | 2 (1 distinct) | 0 | 0 | 0 | 1 | 1/3 = 33% | PROSE-REMEDY (1: STATUS line cap 156, LOW) |
| CORAL | 3 | 3 (1 distinct) | 0 | 0 | 0 | 0 | 0/3 = 0% | PROSE-REMEDY (1: STATUS line cap 73, LOW) |
| CREED | 2 | 0 | 1 | 0 | 0 | 1 | 1/2 = 50% | `CLEAN (2)` |
| CRUISE | 2 | 1 | 1 | 0 | 0 | 0 | 0/2 = 0% | PROSE-REMEDY (1: STATUS line cap 38, LOW) |
| DEWEY | 2 | 0 | 1 | 0 | 0 | 1 | 1/2 = 50% | `CLEAN (2)` |
| FALCON | 1 | 0 | 1 | 0 | 0 | 0 | 0/1 = 0% | `CLEAN (1)` — BUILT row is a stale twin of the fixed :96 |
| FERT | 3 | 1 | 0 | 0 | 0 | 2 | 2/3 = 67% | PROSE-REMEDY (1: STATUS line cap 36, LOW; byte leg unwired, STATUS 74%) |
| FLG | 3 | 1 | 0 | 0 | 0 | 2 | 2/3 = 67% | PROSE-REMEDY (1: line cap 23, LOW; byte constant drifted 32,000 vs 32,550) |
| GIBBS | 2 | 0 | 0 | 0 | 0 | 2 | 2/2 = 100% | `CLEAN (2)` |
| HANS | 7 | 0 | 3 | 0 | 0 | 4 | 4/7 = 57% | `CLEAN (7)` — its line cap is code (`doc_audit.py:517`) |
| HENRY | 7 | 3 (2 distinct) | 2 | 0 | 0 | 2 | 2/7 = 29% | PROSE-REMEDY (2: STATUS line cap 161 · MEMORY line cap 128; both LOW) |
| HOMER | 3 | 0 | 1 | 0 | 0 | 2 | 2/3 = 67% | `CLEAN (3)` |
| ISHM | 2 | 1 | 1 | 0 | 0 | 0 | 0/2 = 0% | PROSE-REMEDY (1: line cap 6, LOW) |
| LABOR | 7 | 4 (3 distinct) | 1 | 0 | 0 | 2 | 2/7 = 29% | PROSE-REMEDY (3, none LOW: B5b unconsumed-card list 53 · B5 calendar event-set twin 77 · C2-0 stale-confidence row selection 50) |
| LIQUID | 3 | 1 | 0 | 0 | 0 | 2 | 2/3 = 67% | PROSE-REMEDY (1: line cap 159, LOW — while STATUS bytes are at 92%, rotate-tier, unwired) |
| MARCO | 3 | 0 | 2 | 0 | 0 | 1 | 1/3 = 33% | `CLEAN (3)` — 1 stale twin, 1 stale "worth adding" clause (run #1 ask unexecuted) |
| **Total** | **74** | **18 rows = 13 distinct** (10 LOW line caps · 3 LABOR not-LOW) | **18** | **0** | **0** | **38** | **38/74 = 51%** | 10 desks with PROSE-REMEDY · 10 `CLEAN` · 0 NOT READ |

Row arithmetic: 18 + 18 + 0 + 0 + 38 = 74.
**By form:** form 1 (script + token) 13 rows → BUILT 8, FALSE 4, PROSE-REMEDY 1 (FP 31%). Form 2 (charter comparison) 61 rows → FALSE 34, BUILT 10, PROSE-REMEDY 17 (FP 56%). **Form 2's false positives are almost all signal/escalation-table rows** (26 of 34; the other 8 are ruling history, retired-rule quotes, a prediction row and judgment rules): the v2 generator's R4 keeps unit-bearing thresholds (`≤ 153 cm`, `≥60%`) by design, and in A–M charters most of those live in signal tables, not boot/closeout steps. Scoping form 2 to boot/closeout sections (or excluding markdown table rows whose last cell is a routing target) would remove most of them; that is a step-1 refinement for DAEDALUS, needing the playbook's fleet before/after diff.
**The 13 distinct remedies, by class:** ① STATUS/MEMORY line caps with no counter ×10, all LOW (BOND, CARL, CORAL, CRUISE, FERT, FLG, HENRY ×2, ISHM, LIQUID). Two of these desks carry a live byte-side issue the line cap cannot see: LIQUID STATUS 30,018 B = 92% (rotate-tier, `read_cap_check` not named in its charter) and FERT STATUS 74% with the tool not named. ② LABOR boot/closeout comparisons ×3, not LOW: unconsumed grading cards (B5b), STATUS calendar vs CATALYSTS.tsv event set (B5), stale-high-confidence row selection (C2-0).
**Ordering class (run #1's main finding) is closed in this half:** the shared `scripts/brief_pin_check.py` exists (`d67d4b431`, 2026-10-08); CARL, FALCON, LABOR and MARCO now name it at the step, and the three A10-wording lines still present (AEOLUS :82, HENRY :54, HOMER :230) are `BUILT` (all three `OK-SAME-COMMIT` on 2026-10-30). Those three still quote the superseded A10 timestamp form; that is wording drift for the owners, not an uncomputed remedy.

## Classification rules applied (read before the tables)

- **Form-2 signal-table rows.** Playbook §1 form 2 is scoped to "a `CLAUDE.md` boot or closeout step written as a comparison". A row of a desk's signal/escalation/kill table (e.g. "U-3 ≥5.0% → HENRY 🔴") is a domain signal definition, not a boot/closeout step and not a remedy, so it is `FALSE` for this census whatever code grades it. Where I checked whether a desk script grades the level, the evidence column says so, for information only.
- **NEXUS-brief ordering rows (Amendment 10).** Since run #1 the shared repo-root check exists: `scripts/brief_pin_check.py` (`d67d4b431`, 2026-10-08). It grades the amendment-11 hash pin (rc 1 on STALE-PIN) and, for an UNPINNED brief, reports the amendment-10 "brief commit at or after STATUS" fallback (`:91`, ADVISORY). Its docstring (`:9-10`) records the schema rule that it is run by the reader (NEXUS), not added as a desk closeout step. These rows are `BUILT`; the desk line describes a check that now exists elsewhere.
- **STATUS/MEMORY line caps ("under 250 lines").** Still uncomputed: root `scripts/read_cap_check.py` checks bytes, and its own `:12` records that line caps pass clean over over-cap files; no desk script found counting lines (per-desk searches below). Classified as in run #1: `PROSE-REMEDY` by the letter, **LOW** (the byte budget is the computed binding constraint).
- **Session counting basis.** Distinct commit dates touching `AGENTS/<DESK>/` from the date the clause entered the file (`git log -S`, oldest hit) to HEAD — a proxy for sessions, as in run #1. Every PROSE-REMEDY count here clears ≥2 by a wide margin.

## §1 Per desk, per row

### AEOLUS — 13 candidates · 1 BUILT · 12 FALSE · `CLEAN (13)`

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| AEOLUS | CLAUDE.md:82 | `BUILT` | "ORDERING (NEXUS schema Amendment 10 …): the brief fold is the session's LAST write-back … Checkable form: the brief's commit timestamp ≥ your last STATUS commit timestamp." | Computed by repo-root `scripts/brief_pin_check.py` (A11 pin, rc 1 on STALE-PIN; A10 fallback `:91`). Run read-only 2026-10-30: `AEOLUS OK-SAME-COMMIT f1585b60a`, rc 0. Line still cites the superseded A10 timestamp form; not wired at the desk step (by schema design, `:9-10`). | n/a |
| AEOLUS | CLAUDE.md:156 | `FALSE` | "ACE vs normal — 1991-2020 Atlantic normal = 122.6 … ≥110% \| ≥130% \| ≥150% + landfall \| C1 → CORAL/REGINALD" | Signal-table row (C1 escalation bands), not a boot/closeout step. | — |
| AEOLUS | CLAUDE.md:159 | `FALSE` | "C2 — South Africa corn (LEAD El Niño band) · USDA PSD … vs trailing 5-yr mean (16,421 kt …) \| ≤−15% (13,958 kt)" | Signal-table row (C2 band, registered 2026-10-10). | — |
| AEOLUS | CLAUDE.md:160 | `FALSE` | "C2 — Australia wheat (second leg) · USDA PSD vs trailing 5-yr mean … \| ≤−15% \| ≤−30% \| ≤−40%" | Signal-table row. | — |
| AEOLUS | CLAUDE.md:161 | `FALSE` | "C3 — WINTER heating demand · NOAA CPC daily population-weighted HDD … \| ≥0% \| ≥+10% \| ≥+20%" | Signal-table row. | — |
| AEOLUS | CLAUDE.md:164 | `FALSE` | "Reinsurer cat-loss tally (Gallagher Re/Munich Re, YTD vs 10-yr avg) \| ≥110% \| ≥130% \| ≥150%" | Signal-table row. | — |
| AEOLUS | CLAUDE.md:165 | `FALSE` | "Panama Canal daily transits — oceangoing transits, daily average (baseline RE-BASED 8/21 to 35.86/day …) \| ≤32 \| ≤27 \| ≤22" | Signal-table row. | — |
| AEOLUS | CLAUDE.md:166 | `FALSE` | "🔴 Panama — READ THE ROW ABOVE WITH THIS GUARD (added 8/21). Transits are a WEAK Panama instrument …" | Interpretive guard on a signal row (retraction text), no check specified. | — |
| AEOLUS | CLAUDE.md:172 | `FALSE` | "C6 Colorado River implementation milestone (RE-KEYED 2026-10-10 …) … unexecuted with Jan 1, 2027 ≤60 days out" | Signal-table row (event gate). | — |
| AEOLUS | CLAUDE.md:189 | `FALSE` | "Superseded, preserved verbatim: \"fires when BOTH, on 10 consecutive days.\" It fired 8/18 on an 11-day run …" | A retired rule quoted as history. (Adjacent :190 is a diagnosis — "no guard of mine compares the charter against STATUS" — not a candidate, noted only.) | — |
| AEOLUS | CLAUDE.md:197 | `FALSE` | "A \| Kaub (km 546.2 — the binding shoal) \| daily mean ≤ 25 cm \| WSV NNW … set 2018-10-22" | Signal-table row (Rhine leg threshold). | — |
| AEOLUS | CLAUDE.md:198 | `FALSE` | "B \| Duisburg-Ruhrort (km 780.8 …) \| daily mean ≤ 153 cm \| WSV NNW, set 2018-10-23" | Signal-table row. | — |
| AEOLUS | CLAUDE.md:349 | `FALSE` | "seismic/ is deliberately exempt from the #1 guard … Promotion to a core channel (C7) requires ≥3 trigger fires in ~6 months …" | Governance criterion for a DAEDALUS/Will review, not a boot/closeout comparison. | — |

### BOND — 2 candidates · 1 PROSE-REMEDY (LOW) · 1 BUILT

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| BOND | CLAUDE.md:28 | `BUILT` | "Run `python3 monitors/docket_check.py`, THEN read `docket/CATALYSTS.tsv` … derives coverage from the issuer (TreasuryDirect `upcoming`) … keys on CUSIP" | The step is code: `AGENTS/BOND/monitors/docket_check.py:107` `TD_UPCOMING = …/securities/upcoming`, `:130` `_CUSIP` regex. Not stale; matched on its own tokens ("no boot step … can surface a row"). | n/a |
| BOND | CLAUDE.md:49 | `PROSE-REMEDY (108)` LOW | "Compress. STATUS.md should stay under 250 lines. If it's growing, archive old research to `domain/sources/`." | Searched `AGENTS/BOND/monitors/*.py` (BOND has no `scripts/`) for `250`, `splitlines`, `wc`: only unrelated hits (`grade_auction.py:193` row limit, `assertion_check.py:440` radius, `closeout_run.py:170` parses STATUS text, no count). Root `read_cap_check.py` counts bytes only. STATUS now 100 lines (passes). | intro `505184019` 2026-03-27; 108 commit-days |

### BRENT — 1 candidate · 1 FALSE · `CLEAN (1)`

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| BRENT | SCRATCH.md:12 | `FALSE` | "Fixes (Will-requested): `thresholds.py` GASREGW keyless EIA-workbook fallback (falsified …) … RF-013 Ufa downgrade candidate on Reuters 4/03, capacity re-key owed." | A done-fixes receipt; the one "owed" is a data re-key in INCIDENTS (a ledger edit judged on a Reuters read), not a computation. One session old (2026-10-29 block). | — |

### BROCK — 5 candidates · 2 BUILT · 3 FALSE · `CLEAN (5)`

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| BROCK | CLAUDE.md:60 | `BUILT` | "Budget is BYTES, not lines: `scripts/read_cap_check.py --agent BROCK`; keep STATUS under 70% of budget; never raise the budget. … the retired rule was \"≤250 lines …\"" | Computed by repo-root `scripts/read_cap_check.py` (named on the line). The line cap was retired here 2026-10-02 in favour of the computed byte budget — this is the remedy the line-cap rows below lack. | n/a |
| BROCK | CLAUDE.md:70 | `BUILT` | "11b. Memory-index check … `python3 \"$(git rev-parse --show-toplevel)/scripts/memory_index_check.py\" --strict --slug <the memory you wrote>`" | `scripts/memory_index_check.py` exists and is the named step. No uncomputed remedy. | n/a |
| BROCK | CLAUDE.md:30 | `FALSE` | "Before registering any threshold, run two tests. Inversion: … Panel depth: can the panel I hold reach N at all?" | Registration discipline (judgment tests), not a computed comparison. | — |
| BROCK | CLAUDE.md:170 | `FALSE` | "Major private credit fund reports default rate declining 2 consecutive quarters" | Thesis-kill criterion (signal list). | — |
| BROCK | CLAUDE.md:179 | `FALSE` | "BCRED redemptions fall below 2% for 2 consecutive quarters → gate thesis dead" | Position-exit criterion (signal list). | — |

### CARL — 3 candidates · 2 PROSE-REMEDY rows (1 distinct, LOW) · 1 FALSE

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| CARL | CLAUDE.md:157 | `PROSE-REMEDY (156)` LOW | "STATUS.md stays under 250 lines. Archive to `domain/sources/`." | Searched `AGENTS/CARL/scripts/*.py` (20 scripts incl. `boot.py`, `consistency_check.py`) for `250`, `wc -l`, line-count `len(…splitlines)`: only `consistency_check.py:131`, a comment about the 54,250 B byte cap. No line counter. STATUS 118 lines (passes). | intro `3e6a0ed98` 2026-03-02; 156 commit-days |
| CARL | CLAUDE.md:256 | `PROSE-REMEDY (150)` LOW — same remedy as :157 | "`STATUS.md` \| Live state — dashboard, K-shape, convergence mirror. Primary memory. ≤250 lines." | Same search as :157. (Adjacent :255 "MEMORY.md … Cap 100 lines" is the same class, not a candidate, noted only.) | intro `9e30a573c` 2026-03-09; 150 commit-days |
| CARL | CLAUDE.md:206 | `FALSE` | "~~CC 90+ DQ >13.74%~~ ⛔ RETIRED 2026-09-10 … Replacement: CC serious-delinquency FLOW ≥7.50% (CRL-30)" | Signal-routing table row. | — |

### CORAL — 3 candidates · 3 PROSE-REMEDY rows (1 distinct, LOW)

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| CORAL | CLAUDE.md:59 | `PROSE-REMEDY (73)` LOW | "11. `STATUS.md` — update signal status, dashboards … Keep under 250 lines; archive overflow to `workbook/` or `archive/`." | `AGENTS/CORAL/scripts/boot.py:38-47` has `STALE_LIMITS` (age in hours per file, e.g. `\"STATUS.md\": 48`), not a line count; no `250`/`wc -l`/line-length test in `scripts/boot.py` or `tools/bkcy`. STATUS 139 lines (passes). | intro `f276f7532` 2026-06-19; 73 commit-days |
| CORAL | CLAUDE.md:133 | `PROSE-REMEDY (73)` LOW — same remedy | "STATUS.md stays under 250 lines. Detail → `sources/`, `research/`, or `workbook/`." | As :59. | same |
| CORAL | CLAUDE.md:220 | `PROSE-REMEDY (73)` LOW — same remedy | "`STATUS.md` \| Live dashboard — signal status, condo/insurance/market indicators … Primary snapshot. ≤250 lines." | As :59. | same |

### CREED — 2 candidates · 1 BUILT · 1 FALSE · `CLEAN (2)`

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| CREED | CLAUDE.md:155 | `BUILT` | "`STATUS.md` stays the HOT file … must stay under the fleet read budget: check with `scripts/read_cap_check.py --agent CREED` … Never raise the budget." | Computed by repo-root `scripts/read_cap_check.py` (named on the line). The former 320-line trigger was retired 2026-09-30 (`:156`). | n/a |
| CREED | MAINTENANCE.md:22 | `FALSE` | "SCRATCH \"owed out\" (DAEDALUS SEC-UA helper, PROME MACHINE_LOCAL SEC-UA row) CLOSED unsent: a working declared-UA pattern exists (DEWEY `edgar_fetch.py`)." | A closed item in a changelog entry. | — |

### CRUISE — 2 candidates · 1 PROSE-REMEDY (LOW) · 1 BUILT

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| CRUISE | CLAUDE.md:47 | `BUILT` | "3d. Ledger staleness check: `python3 … scripts/ledger_staleness.py CRUISE` — every workbook ledger must be … FROZEN … or LIVE …" | Computed by repo-root `scripts/ledger_staleness.py` (named on the line); "owed this session" is the disposition of its output. | n/a |
| CRUISE | CLAUDE.md:74 | `PROSE-REMEDY (38)` LOW | "Compress. STATUS.md should stay under 250 lines. If it's growing, archive old research to `domain/sources/`." | CRUISE has no `scripts/` or `tools/` directory (checked `AGENTS/CRUISE/`); root `read_cap_check.py` counts bytes only. STATUS 117 lines (passes). | intro `d9744d9ed` 2026-03-20; 38 commit-days |

### DEWEY — 2 candidates · 1 BUILT · 1 FALSE · `CLEAN (2)`

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| DEWEY | CLAUDE.md:180 | `BUILT` | "Quote `path#key` values with spaces; repeat `--artifact` as needed. Review dates ≥ today; no semicolons, tabs or line breaks …" | Computed by the receipt writer, repo-root `scripts/corrections_boot_check.py:301-302` (`if d < today: die2("receipt refused: --review … is before today …")`). The line documents the writer's refusals. | n/a |
| DEWEY | CLAUDE.md:235 | `FALSE` | "Slate-building method … mining agents' SELF-flagged gaps … adversarially verify each candidate on four tests — already-answered? · cheap-verify (doesn't need a research run)? …" | Research method (judgment); matched on "needs a … run". | — |

### FALCON — 1 candidate · 1 BUILT · `CLEAN (1)`

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| FALCON | CLAUDE.md:143 | `BUILT` (stale twin) | "STATUS.md stays under 250 lines. Archive overflow to `domain/sources/` if it grows (dir doesn't exist yet at spinout …)" | The owner disposed run #1's line-cap ask at the closeout step: `CLAUDE.md:96` now reads "Size check by instrument, never by a remembered number: `… scripts/read_cap_check.py --agent FALCON`" (`4d06ed3a0` 2026-10-09). :143 is the surviving OUTPUT-RULES twin of the retired rule — a correction beside an instruction (two live instructions), not an uncomputed remedy. No FALCON script counts lines (`scripts/`: 4 watchers + `warrisk_row_staleness.py`). STATUS 65 lines / 10,912 B. | n/a (twin since `3fb46ebdf` 2026-07-12) |

### FERT — 3 candidates · 1 PROSE-REMEDY (LOW) · 2 FALSE

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| FERT | CLAUDE.md:164 | `PROSE-REMEDY (36)` LOW | "STATUS.md ≤250 lines, REWRITTEN not prepended (blueprint R3); ends with BOTTOM LINE (2-4 sentences, updated every session)." | FERT has no `scripts/` or `tools/` (checked `AGENTS/FERT/`); root `read_cap_check.py` counts bytes only and FERT's CLAUDE.md does not name it. STATUS 120 lines (line leg passes) / **24,230 B = 74.4% of the 32,550 B budget, 182 B under the 75% rotation trigger** — the live risk is the byte leg, which the step does not invoke. Root `read_cap_check.py --agent FERT` run read-only 2026-10-30: `rc=1 … manifest_defects=1 … rotation_due=1` (surface not isolated by this pass; owner's to read). | intro `595ac2306` 2026-08-16; 36 commit-days |
| FERT | CLAUDE.md:113 | `FALSE` | "Registered (Will ruling 2026-08-17 …): GATE-FERT-G5 (DTN retail DAP or MAP > $1,000/ton) and GATE-FERT-G3 … G4 (CPI food-at-home ≥+0.4% m/m ×2) was declined as specced" | Gate registry prose (letters canonical in `PROME/GATES.tsv`), not a boot/closeout step. | — |
| FERT | CLAUDE.md:144 | `FALSE` | "Transmission state change (food-at-home ≥+0.4% m/m, or ERS revises 2027 FAH upward citing inputs) \| CARL, HENRY \| 🔴" | Signal-routing table row. | — |

### FLG — 3 candidates · 1 PROSE-REMEDY (LOW) · 2 FALSE

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| FLG | CLAUDE.md:172 | `PROSE-REMEDY (23)` LOW | "STATUS.md ≤250 lines and ≤32,000 B, REWRITTEN not prepended (blueprint R3). At ≥75% of the byte budget (24,000 B), rotate the oldest history blocks verbatim …" | Line leg: FLG `scripts/` holds only `extract_filings.py` (no `250`/`wc -l`/line-count hit); root tool counts bytes only. Byte leg: computed by root `scripts/read_cap_check.py`, but FLG's CLAUDE.md never names it and carries a hand constant (32,000 B / 24,000 B) that differs from the fleet budget (32,550 B / 24,412 B). STATUS 151 lines / 21,860 B (passes both). | intro `416628c68` 2026-08-20; 23 commit-days |
| FLG | CLAUDE.md:149 | `FALSE` | "ACL/nonaccrual coverage moves ≥10pp in a quarter, either direction \| REGINALD, PROME \| 🔴" | Signal-routing table row. | — |
| FLG | CLAUDE.md:151 | `FALSE` | "Deleveraging stalls or reverses (loans QoQ turns positive ≥2 quarters) — the counter-thesis firing \| REGINALD, RED \| 🟠" | Signal-routing table row. | — |

### GIBBS — 2 candidates · 2 FALSE · `CLEAN (2)`

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| GIBBS | CLAUDE.md:14 | `FALSE` | "Critical semantics: the perimeter is a NAMED LIST, not an asset line. \"Above $250B\" is NOT the Fed's Category III test (12 CFR 252.5(d): ≥$250B four-quarter average …" | A read-the-list instruction; explicitly forbids computing membership from a size. | — |
| GIBBS | CLAUDE.md:138 | `FALSE` | "A read tagged `INDUSTRY-WIDE` on ≥2 items in one quarter \| REGINALD, PROME, NEXUS \| P1" | Signal-routing table row. | — |

### HANS — 7 candidates · 3 BUILT · 4 FALSE · `CLEAN (7)`

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| HANS | CLAUDE.md:94 | `BUILT` | "STATUS.md stays under 250 lines." | `AGENTS/HANS/scripts/doc_audit.py:103` `STATUS_LINE_CAP, STATUS_BYTE_BUDGET = 250, 32_550`; `:517-518` `if nl > STATUS_LINE_CAP: bad('C6-LINES', …)`; selftest `test_hans.py:614`. Run at RULE #1b (`CLAUDE.md:19`). The only A–M desk whose line cap is code. STATUS 139 lines / 22,772 B. | n/a |
| HANS | CLAUDE.md:21 | `BUILT` | "RULE #1c — BEFORE MINTING A STATUS TOKEN, READ THE PREAMBLE … AND MATCH STATUS CELLS BY PREFIX, NEVER BY EXACT MEMBERSHIP." | The matching half is code: `scripts/boot.py:82` `.startswith(DEAD_PREFIXES)`, `:94` `startswith(LIVE_KNOWN)`; `scripts/doc_audit.py:82` comment "PREFIX, never exact membership", `:387`, `:419`. The read half is a reading instruction. | n/a |
| HANS | CLAUDE.md:25 | `BUILT` | "RULE #2 — BEFORE SHIPPING AN EMPIRICAL FINDING, RUN `scripts/finding_check.py`'s `gate()` … It does NOT catch construct validity … which still needs a human question." | `scripts/finding_check.py:135` `def gate(claim, about, varied, …)`. The construct-validity limit is declared as judgment on the line, not a remedy owed. | n/a |
| HANS | CLAUDE.md:160 | `FALSE` | "EA core HICP \| ≥2.5 watch / ≥3.0 orange / ≥3.5 red, sustain 2" | Signal-band table row (`CLAUDE.md:148`: "this table carries bands only"). | — |
| HANS | CLAUDE.md:161 | `FALSE` | "UK core CPI \| ≥3.0 watch / ≥3.5 orange / ≥4.0 red, sustain 2" | Signal-band table row. | — |
| HANS | CLAUDE.md:162 | `FALSE` | "ECB Deposit Rate \| hike to ≥2.75% \| (The old \"emergency CUT\" trigger is RETIRED — wrong sign. …)" | Signal-band table row. | — |
| HANS | CLAUDE.md:166 | `FALSE` | "EU storage gap to 5-yr norm \| >15pp below norm (signed ≤−15) orange · >25pp red" | Signal-band table row. | — |

### HENRY — 7 candidates · 3 PROSE-REMEDY rows (2 distinct, LOW) · 2 BUILT · 2 FALSE

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| HENRY | CLAUDE.md:112 | `PROSE-REMEDY (161)` LOW | "STATUS.md stays under 250 lines." | HENRY `scripts/` = `boot.py`, `credit_monitor.py`, `gamma_flip.py`; grep for `250`, `wc -l`, line-count `len(…splitlines/readlines)`: no hit. Root tool counts bytes only. STATUS **178 lines** (passes; highest of the line-cap desks here). | intro `3e6a0ed98` 2026-03-02; 161 commit-days |
| HENRY | CLAUDE.md:229 | `PROSE-REMEDY (158)` LOW — same remedy as :112 | "`STATUS.md` \| Live state — market levels, macro data, vol regime. Primary memory. ≤250 lines." | As :112. | intro `ccec05569` 2026-03-05; 158 commit-days |
| HENRY | CLAUDE.md:233 | `PROSE-REMEDY (128)` LOW | "`MEMORY.md` \| … Boot step 3. Write before finishing. ≤100 lines; check `wc -l AGENTS/HENRY/MEMORY.md` from the repository root." | Partly disposed since run #1: the count is now a named command (`7d59ea301` 2026-10-19), but the ≤100 comparison is still by eye — no script compares and fails. Same search as :112. MEMORY 70 lines (passes). | intro `b293d676f` 2026-04-17; 128 commit-days |
| HENRY | CLAUDE.md:54 | `BUILT` | "NEXUS_BRIEF fold = the session's LAST write-back … (checkable: brief commit timestamp ≥ last STATUS commit timestamp). NEXUS schema Amendment 10 …" | Repo-root `scripts/brief_pin_check.py` (A11 pin + A10 fallback `:91`). Run read-only 2026-10-30: `HENRY OK-SAME-COMMIT 5ca6fec69`, rc 0. Line still cites the superseded A10 form. | n/a |
| HENRY | CLAUDE.md:66 | `BUILT` | "Boot step (f) lists `inbox/` filenames only … flags a packet if … (a) a date inside the next 14 days … or (e) it has sat ≥10 days unread." | Unchanged since run #1 He2: `scripts/boot.py:452` `INBOX_WINDOW_DAYS = 14`, `:453` `INBOX_STALE_DAYS = 10`, `:485` `def triage_names`. | n/a |
| HENRY | MAINTENANCE.md:124 | `FALSE` | "Boot-impact: boot.py is now a mandatory boot step. Still owed to Will: post-change eval re-run (guardrails 02/03 must hold …) + the case-03 baseline …" | Unchanged since run #1 He1 (then :108): discharged by the later entry `MAINTENANCE.md:111` "POST-WIRING EVAL RE-RUN (01+02) + CASE-03 FIRST BASELINE — 3/3 PASS". | — |
| HENRY | CLAUDE.md:170 | `FALSE` | "USD/JPY \| velocity, not level: \|Δ\| ≥2%/day either direction = escalate \| Carry — SAM owns the call …" | Signal table row. | — |

### HOMER — 3 candidates · 1 BUILT · 2 FALSE · `CLEAN (3)`

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| HOMER | CLAUDE.md:230 | `BUILT` | "ORDERING RULE — the brief fold is the session's LAST write-back … Checkable form: the brief's commit timestamp ≥ the session's last STATUS commit timestamp." | Repo-root `scripts/brief_pin_check.py` (A11 pin + A10 fallback `:91`). Run read-only 2026-10-30: `HOMER OK-SAME-COMMIT 055a9ab6f`, rc 0. Line still cites the superseded A10 form. | n/a |
| HOMER | CLAUDE.md:108 | `FALSE` | "RUNG CENSUS (2026-08-23, Will-directed; ZERO LEVELS MOVED — a labelling rule, not a retune). Test every RUNG … has this level been crossed by EVERY observation I hold?" | A dated census with its results recorded on :109-111 (and two rows re-armed 9/29), in the threshold section, not a boot/closeout step. The reporting rule beside it (:113, highest UNCROSSED rung) is code: `AGENTS/HOMER/tools/threshold_scan.py:9-10`, `:62-75`. The "pinned by every observation" test itself is not coded (grep `pinned`/`every observation` over `tools/*.py`: none) — noted for DAEDALUS as a design question, not counted. | — |
| HOMER | CLAUDE.md:291 | `FALSE` | "CRL-23: FY27 builder GM compression (DHI Q1 FY27 ≤17.5% OR PHM Q1 FY27 ≤22.0% AND tariff ≥10% sustained) — OPEN at CARL …" | A prediction row owned by CARL. | — |

### ISHM — 2 candidates · 1 PROSE-REMEDY (LOW) · 1 BUILT

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| ISHM | CLAUDE.md:264 | `PROSE-REMEDY (6)` LOW | "≤250 lines and under the 32,550 B read budget, REWRITTEN not prepended;" | Byte leg computed (root `read_cap_check.py`, named at `:266`). Line leg: ISHM `boot.py` (desk root) and `scripts/test_boot.py` searched for `250`, `wc -l`, line-count `len(…)`: none. STATUS 69 lines / 11,561 B. New desk (clause entered 2026-10-23). | intro `080fbc7d6` 2026-10-23; 6 commit-days |
| ISHM | CLAUDE.md:265 | `BUILT` | "at ≥75% (24,412 B), rotate the oldest history blocks verbatim, crc-at-rotation, contiguous-only into `archive/STATUS_ARCHIVE_<date>.md` until under 70%;" | Repo-root `scripts/read_cap_check.py:70` `ROTATE_AT = 0.75`, start/stop thresholds `:751-757`; named on `CLAUDE.md:266`. The rotation itself is a manual act on the tool's flag. | n/a |

### LABOR — 7 candidates · 4 PROSE-REMEDY rows (3 distinct, none LOW) · 1 BUILT · 2 FALSE

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| LABOR | CLAUDE.md:24 | `PROSE-REMEDY (53)` | "1b. Unconsumed dated-artifact check (B5b, floor version — 10 seconds): `ls docket/GRADING_CARD_*.md …`. Any card dated ≤ today whose grade is not already written into `STATUS.md` is owed work" | Specified: card filename date ≤ today AND card still at `docket/` top level (graded cards are `git mv`'d to `docket/graded/`, :65) ⇒ unconsumed; failure direction stated (7/30 and 7/29 cards went unconsumed). Searched `AGENTS/LABOR/scripts/*.py` for `GRADING_CARD`, `graded`: `card_required_check.py` checks the INVERSE (card that should exist but does not; its own docstring `:5-14` says "Neither can substitute for the other"); `catalyst_countdown.py:87-101` flags past-due unpruned CATALYSTS rows as UNGRADED — a proxy that misses a card whose catalyst row was pruned or never docketed. No code lists top-level cards dated ≤ today. Today's top-level cards are all dated 11/03–11/06 (none due). | intro `9146266e3` 2026-07-31; 53 commit-days |
| LABOR | CLAUDE.md:65 | `PROSE-REMEDY (53)` — same remedy as :24 | "`docket/` top level = LIVE cards only. `docket/graded/` = consumed cards … For each card whose date is ≤ today, ask one question: has it been GRADED?" | As :24 (the convention that makes the check computable; the question is still asked by hand). | intro `a9706a8b6` 2026-07-31; 53 commit-days |
| LABOR | CLAUDE.md:52 | `PROSE-REMEDY (77)` | "B5. Catalyst calendar reconciliation. Source of truth is `docket/CATALYSTS.tsv` …; the STATUS MONITORING CALENDAR is its human twin and must not diverge in event set." | The "≤ today and not yet resolved" leg is code (`catalyst_countdown.py:87-101` PAST DUE block). The event-set equality between STATUS calendar and CATALYSTS.tsv is not: grep `diverg`, `MONITORING CALENDAR`, `event set` over `scripts/*.py`: none. | intro `9e51e1cad` 2026-06-08; 77 commit-days |
| LABOR | CLAUDE.md:87 | `PROSE-REMEDY (50)` | "C2-0. STALE-HIGH-CONFIDENCE SWEEP … run §C gates #3, #5, #12 and #13 over every OPEN row ≥60% confidence whose confidence has not moved in 60+ days." | The gates are judgment; the row SELECTION (OPEN, Confidence ≥60%, last confidence change ≥60 days ago) is a pure computation and is not coded: `scripts/predictions_due.py` selects by Timeframe only (`:195-230`); grep `60 days`/`has not moved`/`stale.high` over LABOR and root `scripts/*.py`: none. | intro `f5525d857` 2026-08-05; 50 commit-days |
| LABOR | CLAUDE.md:83 | `BUILT` | "C2a. FROZEN GRADING CARD — write one BEFORE any multi-loaded or quarterly gauge print … A card is owed when a print is multi-loaded (≥2 live tests ride it) or is a quarterly …" | `AGENTS/LABOR/scripts/card_required_check.py` (derives card-owing rows from CATALYSTS.tsv via `CARD:<stem>` tokens or declared patterns, rc 1 when a required card is missing in its freeze window; wired as boot leg `scripts/boot.py:51`). "Multi-loaded" is classified by the row token, a judgment the desk enters. | n/a |
| LABOR | CLAUDE.md:192 | `FALSE` | "U-3 ≥5.0% (grade JOINTLY with LFPR — L-06) \| T-04 \| HENRY (structural bid break), REGINALD \| 🔴" | Signal-routing table row. | — |
| LABOR | CLAUDE.md:265 | `FALSE` | "WARN Lead Time \| WARN→claims r=0.78 at 6-week lag … Cohort-to-base ratio ≥~10% of weekly claims (≥~20K) required for national visibility (L-08)" | Indicator-reference table row (method note). | — |

### LIQUID — 3 candidates · 1 PROSE-REMEDY (LOW, with a live byte breach beside it) · 2 FALSE

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| LIQUID | CLAUDE.md:101 | `PROSE-REMEDY (159)` LOW | "STATUS.md stays under 250 lines." | LIQUID `scripts/*.py` (13 files) grep for `250`/`wc -l`/line-count: only `boot.py:333` (a 250bp spread band) and `sofr_dispersion.py:41` (a 250-session window). No line counter. STATUS 112 lines (passes). **The binding constraint is breached:** root `read_cap_check.py --agent LIQUID` run read-only 2026-10-30 reports `STATUS.md 30,018 B 92% of budget rotate-tier`, `rotation_due=1`; LIQUID's CLAUDE.md never names `read_cap_check` (grep: 0 hits). The uncomputed line cap is the wrong instrument for the live risk (same shape as run #1 HAWK H2). | intro `3e6a0ed98` 2026-03-02; 159 commit-days |
| LIQUID | CLAUDE.md:84 | `FALSE` | "BROCK RULED IT 2026-09-09 … A PRO-RATED TENDER IS NOT A GATE … a `>=2 vehicles gated simultaneously` trigger tripped 7-fold on day one" | Ruling history; matched on the quoted retired trigger. | — |
| LIQUID | CLAUDE.md:146 | `FALSE` | "~~Second private credit fund gate~~ RETIRED-AND-REPOINTED 2026-09-12 … BROCK's `GATE-BRK-R2` … ≥3 consecutive sub-100% satisfaction quarters" | Signal-routing table row (repointed to BROCK). | — |

### MARCO — 3 candidates · 2 BUILT · 1 FALSE · `CLEAN (3)`

| Desk | file:line | Token | Surface fragment (≤160 chars) | Evidence | Carry |
|---|---|---|---|---|---|
| MARCO | MAINTENANCE.md:108 | `BUILT` | "✅ T2-D … Class lesson: an append-only docket edit needs a dedup pass against existing rows, and a `date+event` uniqueness check is one line — worth adding to `catalyst_countdown.py`" | Unchanged since run #1 M1 (then :88): `AGENTS/MARCO/scripts/catalyst_countdown.py:90` `LIKELY DUPLICATE` warning (`572cad695` 2026-07-31). Run #1's H-1 ask (delete the "worth adding" clause) not yet executed. | n/a |
| MARCO | CLAUDE.md:158 | `BUILT` (stale twin) | "STATUS.md stays under 250 lines. Archive to `domain/sources/`." | Owner disposed run #1 M2 at the closeout step: `CLAUDE.md:51` now reads "Size: run `python3 scripts/read_cap_check.py --agent MARCO`" (`693f39170` 2026-10-10). :158 is the surviving OUTPUT-RULES twin. No MARCO script counts lines (`ml_to_kb.py:93` `max_len=250` is a string truncation). Note: root tool run read-only 2026-10-30 reports MARCO `rotation_due=1` (STATUS 25,065 B = 77%). | n/a (twin since `3e6a0ed98` 2026-03-02) |
| MARCO | CLAUDE.md:190 | `FALSE` | "MIA negative YoY, 2 consecutive months — on MIA's OWN airport-reported count (capacity caveat — item 3) \| REGINALD, CARL \| 🟠" | Signal-routing table row. | — |

## §2 Rows that changed verdict since run #1 (2026-10-08, A–M)

Run #1 A–M had 27 rows on 11 desks. Each was re-checked at the cited surface on 2026-10-30. Rows that are not candidates in run #2 are listed too, with the reason they dropped out, so a fix is not mistaken for a generator miss.

| Run #1 row | Run #1 token | Now | Why (evidence) |
|---|---|---|---|
| CARL CLAUDE.md:110 (Amendment-10 ordering) | PROSE-REMEDY (43) | resolved — not a candidate | Step 14b now names `brief_pin_check.py`; the "≥ timestamp" sentence is gone. The shared root check was built `d67d4b431` 2026-10-08. |
| FALCON CLAUDE.md:102 (ordering) | PROSE-REMEDY (48) | resolved — not a candidate | Closeout 14 now names `brief_pin_check.py`. |
| LABOR CLAUDE.md:81 (ordering) | PROSE-REMEDY (33) | resolved — not a candidate | C1 now names `brief_pin_check.py`. |
| MARCO CLAUDE.md:56 (ordering) | PROSE-REMEDY (32) | resolved — not a candidate | Closeout 11 now names `brief_pin_check.py`. |
| FALCON CLAUDE.md:96 (STATUS line cap) | PROSE-REMEDY (68) LOW | resolved at the step; twin :143 now `BUILT` (stale twin) | :96 "Size check by instrument … `read_cap_check.py --agent FALCON`" (`4d06ed3a0` 2026-10-09). The OUTPUT-RULES duplicate at :143 still says "under 250 lines". |
| MARCO CLAUDE.md:51 (STATUS line cap) | PROSE-REMEDY (88) LOW | resolved at the step; twin :158 now `BUILT` (stale twin) | :51 "Size: run `python3 scripts/read_cap_check.py --agent MARCO`" (`693f39170` 2026-10-10). Duplicate at :158 survives. |
| HENRY CLAUDE.md:233 (MEMORY ≤100 lines) | PROSE-REMEDY (108) LOW | **unchanged token**, PROSE-REMEDY (128) LOW | Partly disposed: the line now names `wc -l` (`7d59ea301` 2026-10-19), but the comparison is still by eye. |
| HENRY CLAUDE.md:230 (LESSONS ≤32,550 B) | BUILT (unwired at the step) | resolved — wired, not a candidate | The row now names `python3 scripts/read_cap_check.py --agent HENRY`. |
| HENRY CLAUDE.md:66 (inbox triage) | BUILT | BUILT (unchanged) | `scripts/boot.py:452-453`, `:485`. |
| HENRY MAINTENANCE.md:108 → now :124 | FALSE | FALSE (unchanged) | Still discharged by the entry at :111. |
| LABOR CLAUDE.md:88 (as-made) | BUILT (unwired) | resolved — wired, not a candidate | C2 now names `asmade_audit`. |
| HANS STATUS.md:122 ("see owed #15") | BUILT (H-1) | resolved — not a candidate | The stale caveat is gone from STATUS (grep: 0 hits). |
| MARCO MAINTENANCE.md:88 → now :108 | BUILT (H-1) | BUILT (unchanged) | `catalyst_countdown.py:90` still computes it; the "worth adding" clause is still in the ✅ block. Run #1's delete ask was not executed. |
| HAWK CLAUDE.md:68 (≤120 lines) | PROSE-REMEDY (69) LOW | resolved — owner re-scoped, not a candidate | Closeout 10 (:63) runs `read_cap_check.py --agent HAWK`; :85 declares "≤120 lines is a thinness heuristic". This is effectively a written decline. |
| MIDAS SCRATCH.md:31/43/61 (`cot_metals.py` boot leg) | PROSE-REMEDY (3) | now BUILT, not a candidate | `AGENTS/MIDAS/boot.py:67` `COT_METALS_VINTAGES` ledger, `:245` `cot_metals_vintage_leg`. |
| MIDAS CLAUDE.md:230 (LESSONS hook ≤~170 chars) | PROSE-REMEDY (24) LOW | resolved — DECLINED-BY-DESIGN in substance, not a candidate | :234 now reads "~170 chars is an ADVISORY brevity target, not an enforced cap". |
| CREED STATUS.md:3, LAST_COMPLETION.md:90; CARL STATUS.md:107; FLG STATUS.md:152; LIQUID STATUS.md:14, :73 | DECLINED / FALSE | not candidates | Removed by step-1 v2 (R1–R3) or rotated off the surface. Nothing to re-flag; CREED's decline stands. |

**New in run #2, not seen in run #1:** the line-cap rows at BOND, CARL, CORAL, CRUISE, FERT, FLG, HENRY :112/:229, ISHM and LIQUID. Run #1's A–M input did not carry these desks' output-rules lines. The perimeter and generator differ: v2 R6 roster perimeter, R4 keeps unit-bearing thresholds. These are not regressions. Also new: LABOR :24/:65/:52/:87 (v2 removed LABOR :68 but kept these) and the three A10-wording ordering lines.

## §3 Step-3 sentence and limits

**0 rows typed by this run (classification only); premise-verified at the source for 0 of 0.** Nothing here is fixed. Owners type, under H-6.

1. **Session counts are commit-day proxies** (method in the rules section). Every PROSE-REMEDY count clears ≥2. ISHM's is the smallest at 6. Exact session ages are not certified.
2. **"No code computes it" was searched, not proven.** Searched: the desk's `scripts/` and `tools/`, desk-root `*.py` (ISHM, MIDAS), BOND `monitors/`, and repo-root `scripts/*.py`. Hooks, CI, `PROME/tools/` and `~/Research-Intake` were not searched.
3. **BUILT means the code exists and was read; it was not verified to work.** Two tools were run read-only. `brief_pin_check.py` ran for AEOLUS, HENRY and HOMER (rc 0). `read_cap_check.py --agent` ran for LIQUID, MARCO and FERT, and only its result lines were read. No guard was falsified per CHECK_STANDARD §3.
4. **The signal-table rule is this classifier's reading of playbook §1 form 2** ("a `CLAUDE.md` boot or closeout step"). If DAEDALUS rules that signal-table thresholds are in scope, 26 FALSE rows need re-reading for whether a desk script grades each level. Most have one (e.g. HANS `registry/THRESHOLDS.tsv`, HOMER `tools/threshold_scan.py`). That was not checked row by row.
5. **The line-cap rows are classified by the letter and marked LOW**, as in run #1. Five owners (BROCK, CREED, FALCON and MARCO at the step, HAWK) have already resolved theirs by moving to the computed byte budget. That suggests the fleet remedy is a charter edit (name `read_cap_check.py` at the step, or declare the line count a heuristic) rather than a line counter. Only HANS typed the counter (`doc_audit.py:517`). If DAEDALUS rules that a line cap the byte budget outranks is not an H-4 remedy, 14 rows (10 distinct) become FALSE: 4 PROSE-REMEDY rows / 3 distinct remain (all LABOR), and FALSE becomes 52 (70%).
6. **Off-list notes, not counted:** AEOLUS CLAUDE.md:190 is a self-reported missing check: "no guard of mine compares the charter against STATUS". It is a diagnosis. CARL CLAUDE.md:255 ("MEMORY.md … Cap 100 lines") is the same class as the line caps, but it is not a candidate. HOMER's "pinned by every observation" rung test (:108) is not coded.
7. Read-only throughout. The only write is this file. Nothing was staged or committed, no messages were sent and no subagents were used.

**Closed:** 2026-10-30 11:38 EDT (from `date`)
