# consistency_check.py — build spec

**Owner:** CARL · **Created:** 2026-07-10 (Will-greenlit B4) · **Status:** PLAN (Phase 0)
**Origin:** ROADMAP "Closeout hardening — Phase 3" thread (L16/L20) + DAEDALUS docket #4 (the L5 gate).

## Purpose
Mechanize the **value-mirror-drift** class: catch, at boot + closeout, when a canonical value and its mirror disagree. This is the class the manual step-15 check misses (it only tests rows edited that session; pre-existing drift stays silent — Jun-8 found 7 accumulated STATUS↔PREDICTIONS deltas).

## Scope — what it DOES and does NOT catch
**Catches (structured value-mirror drift):** prediction conf/status drift, score-total drift across surfaces, per-vector score drift, catalyst-set drift.
**Does NOT catch (out of scope — different class, needs discipline/grep):**
- *Free-text number staleness* (e.g. "CMBS 7.71%" left behind after the row updated to 7.23%). → guarded by the closeout habit "grep a changed figure's other occurrences" ([[finding_seeded_selfsweep_secondary_surface_rot]]).
- *Narrative disposition drift* (e.g. V5 "surfaced, not executed" vs "held" across STATUS sections). → discipline; optional fuzzy heuristic later (Phase 6).

Setting this expectation explicitly so a clean run is not mistaken for "everything is consistent."

## Checks (3 live mirror pairs)

### Check A — Predictions mirror
- **Canonical:** `thesis/PREDICTIONS.tsv` (cols: Pred_ID, …, Confidence, Timeframe, Status, …).
- **Mirror:** `STATUS.md` → "## PREDICTIONS" → the **Open** table (ID | Prediction | Conf | Timeframe | Current) and the **Resolved** table.
- **Rules:**
  - Every TSV `Status=OPEN` Pred_ID must appear in STATUS Open table (and vice versa) — **hard flag** on presence mismatch.
  - A TSV Pred_ID with `Status≠OPEN` (MISSED/CONFIRMED/MIXED) must NOT be in STATUS Open table — **hard flag** (stale-open).
  - **Confidence:** numeric extract from both, compare — **hard flag** on mismatch (this is the exact drift class).
  - **Timeframe:** normalized string compare (strip markdown/whitespace/lowercase) — **soft/warn** (timeframes carry annotations; warn, don't fail).

### Check B — Score/matrix mirror
- **Canonical:** `thesis/THESIS.md` histogram table (Score | Vectors | Count | Sum) + total.
- **Mirror:** `STATUS.md` "## CONVERGENCE MATRIX" histogram table + total.
- **Rules:**
  - **Score total** (`N/70`) identical across: STATUS header (L2), STATUS Overall line, STATUS matrix total, STATUS bottom line, THESIS total, NEXUS_BRIEF status line — **hard flag** on any disagreement (this replaces the dropped VX check (iv)).
  - **Histogram self-consistency:** `Σ(score × count) == stated total` in each file — **hard flag**.
  - **Per-vector assignment:** the vector→score mapping from the STATUS histogram == THESIS histogram (parse the "Vectors" cell, e.g. "V1, V2, …") — **hard flag** on any vector at a different score.
  - *(Parse the histogram, not the prose matrix — the matrix "Current" column is narrative; the histogram is the structured surface.)*

### Check C — Catalyst set mirror
- **Canonical:** `docket/CATALYSTS.tsv` (date, event, …).
- **Mirror:** `docket/CALENDAR.md` markdown tables (| Date | Event | Test | Pri |).
- **Rules:** normalize each side to a set of `(month, day, event-head)` (ISO date vs "~Jul 15"; event-head = first ~4 words, lowercased). Compare sets — **flag** missing/extra rows either direction. Date/event fuzzy → **soft/warn** on near-misses, **hard flag** on a fully-missing event.

## Output + behavior
- **Warn-and-surface, exit 0** (do NOT hard-block boot). Print a `CONSISTENCY` section: `✅ clean` or a `⚠️ N drift(s)` list, one line per finding: `CHECK-x | <what> | canonical=<a> mirror=<b>`.
- Hard flags vs soft warns visually distinct. Summary line: `N hard, M soft`.
- cwd-proof (resolve paths from `git rev-parse --show-toplevel`, like the other CARL scripts).

## Wiring (Phase 4)
- **boot.py:** add as a BOOT_SEQUENCE step (durable home per PAT-041; survives SCRATCH rewrites). Non-slow.
- **CLAUDE.md:** closeout **step 15** points at it (replaces the manual mirror-check prose); boot **step 7d-sibling** surfaces it.

## Acceptance tests (per phase — seed a known drift, confirm flag, then confirm clean)
- A: temporarily change one STATUS Open-table Conf → run → must flag CHECK-A conf drift → revert → clean.
- B: temporarily change STATUS matrix total to 52/70 → must flag CHECK-B score drift → revert → clean.
- C: delete one CALENDAR row → must flag CHECK-C missing catalyst → revert → clean.

## Phase plan (incremental — each phase leaves a working, tested script)
- **Phase 0 (done):** this spec, committed.
- **Phase 1:** scaffold + markdown-table parse helper + **Check A** + acceptance test A.
- **Phase 2:** **Check B** (score cross-surface + histogram) + acceptance test B.
- **Phase 3:** **Check C** (catalyst set) + acceptance test C.
- **Phase 4:** wire into boot.py + CLAUDE.md; full clean run.
- **Phase 5 (B5):** STATUS trim 266→<250, **verified clean by this checker** (archive superseded lead-block/danger-window blocks to `archive/`).
- **Phase 6 (optional):** free-text figure cross-occurrence heuristic (warn-only).

## Technical risk
Main risk = markdown-table parsing of hand-maintained STATUS tables (irregular whitespace, `**bold**`, annotations). Mitigate: tolerant parser (split on `|`, strip markdown, skip separator rows), and prefer the most-structured surface (histogram over prose matrix; TSV over markdown where a pair exists).

---

# PHASE 4 — AS BUILT (2026-07-24, Will-directed)

**Status: BUILT, acceptance-tested, wired into `boot.py`.** Note this is *not* the
Phase 4 the original plan described (that was "wire boot.py + closeout step 15").
Boot wiring is included here, but the substance is two **new checks** that the
original 6-phase plan did not anticipate, because the failure class they cover had
not been observed yet.

## Why Phase 4 exists

Two coherence bugs on 2026-07-24, **neither catchable by any single-file review**:

**Bug 1 — instrument mismatch.** A vector downgrade was armed against an instrument
that does not publish the series the vector's own trigger names. V2 (Subprime Auto
60+) resolves on the **Fitch ATR** monthly index; it was armed against the **NY Fed
HHDC**, which publishes only a *blended* auto series and no subprime series at all.
The vector definition lived in `THESIS.md`; the arming happened in `STATUS.md`.
Neither file was internally wrong.

**Bug 2 — cross-ledger monotonicity.** `POP-P06` (SBA 7(a) default **>5%** by
Q4-2026) sat at **50%** while `CRL-15` (**>6.5%**, same series, same date) sat at
**65%**. Impossible: >5% is strictly implied by >6.5%, so P(>5%) ≥ P(>6.5%). Each
ledger was internally consistent; the violation exists only in the *pair*, and the
parent/sub-agent split guarantees nobody reads both at once.

## Schema change

`thesis/PREDICTIONS.tsv` gains an 11th column, **`Instrument`** (and sub-agent
ledgers may adopt it):

    <source> :: <series> :: <op><value>
    e.g.  SBA :: 7(a) default rate :: >6.5%

`qualitative` is accepted as the threshold clause where no numeric bar exists.
Documented in `workbook/SCHEMA.tsv`.

## Check D — instrument declaration
- **HARD** — `Status=OPEN` with a blank `Instrument`. The prediction does not
  record what would resolve it. This is the bug-1 class.
- **SOFT** — malformed (not 3 `::` parts), or a threshold clause that won't parse
  as `<op><value>` (Check E will skip it).
- Resolved rows are exempt from the HARD rule; declaring them is audit hygiene.

## Check E — cross-ledger threshold monotonicity
Groups CARL's ledger **and every `sub_agents/*/workbook/PREDICTIONS.tsv` carrying
an `Instrument` column** by `(source, series)`. Within a group, for rows with the
same operator direction:
- `>` / `>=` — a **higher** threshold is stricter → its confidence must be **≤**
  that of any lower threshold.
- `<` / `<=` — a **lower** threshold is stricter → same rule inverted.

**HARD** when the two rows share a normalized timeframe; **SOFT** when timeframes
differ (the implication may not hold across horizons — a human decides).

**Coverage gaps are reported, not skipped.** A sub-agent ledger without an
`Instrument` column emits a SOFT finding naming it. *An unscanned ledger must never
read as a clean one* — that is the same silence that produced both bugs.

## Acceptance test (run 2026-07-24, PASSED)
Reseeded the real bug — `CRL-15` back to 65%, `POP-P06` back to 50% — and Check E
produced:

    🔴 HARD CARL/CRL-15  MONOTONICITY: CARL/CRL-15 (>6.5) at 65% EXCEEDS
                         POP/POP-P06 (>5) at 50% on 'sba :: 7(a) default rate'
                         — the stricter threshold cannot be more likely (same timeframe)

Check A independently caught the same seed as confidence drift against the STATUS
mirror. Reverted; suite returns to 0 hard.

## Boot wiring + the `--warn-only` contract
`boot.py` runs it last, with `--quiet --warn-only`.

`--warn-only` forces **exit 0** while still printing every finding, plus a
🔴-prefixed summary line (🔴 is in boot's `KEY_MARKERS`, so it survives collapsed
mode). Rationale: boot renders a non-zero exit as **FAIL**, and *"the checker found
drift"* and *"the checker crashed"* must not look identical in the boot summary —
the first is information, the second is breakage. **Closeout runs it WITHOUT
`--warn-only`**, where exit 1 is the gate before commit.

## Coverage closure + coverage evidence (same day, Will-directed)

**All four remaining sub-agent ledgers now carry `Instrument`.** DOC (10), GIG (8),
PHAN (7), POLLY (8) declared — **66 instrument-declared rows across 6 ledgers, zero
coverage gaps.**

One declaration is worth calling out as a discipline point: **GIG-P08 ("gas $4+
triggers visible driver-count decline QoQ") declares the driver-count series, not
the gas series.** The gas level is the *condition*; the *resolving* series is driver
count. Declaring gas there would have created a spurious Check E group against
CRL-08/CRL-26 and compared two things that are not nested thresholds on one measure.
**Instrument = what resolves the prediction, not what appears in its sentence.**

**Coverage evidence added to the report.** A positive control after the closure found
52 comparable rows across 51 distinct series but **only 1 multi-threshold group** —
i.e. a "clean" Check E was asserting almost nothing, and nothing in the output said
so. `check_e` now returns `stats` and the report prints:

    coverage: 52/66 rows comparable (12 qualitative, 2 no-confidence) across 51 distinct series
    1 pair(s) compared across 1 multi-threshold series: sba :: 7(a) default rate (2)

and, when nothing groups at all:

    ⚠️  0 pairs actually compared — NO series has 2+ numeric thresholds, so Check E
        asserted nothing this run. 'Clean' here means 'nothing to compare', not
        'verified consistent'.

Both branches tested. This is the false-zero guard: *a check that compared nothing
must not read the same as a check that compared everything and found no violation.*
The acceptance test was re-run after the refactor and still reproduces the original
bug.

## Known gaps (honest)
- **Check E is thin by construction right now: 1 comparison pair.** It catches the
  class, and it will catch the *next* pair automatically — but it is not currently
  auditing much, and the coverage line says so on every run rather than letting a
  green tick imply breadth.
- Check E compares thresholds only within a `(source, series)` string match; two
  rows describing the same series with different wording will not group. The
  `Instrument` strings are therefore a small controlled vocabulary in practice —
  worth a periodic eyeball.
- Checks B (THESIS↔STATUS score) and C (CATALYSTS↔CALENDAR) remain unbuilt.

---

# CHECK B — AS BUILT (2026-07-24, Will-directed)

**Status: BUILT, five acceptance tests passed, wired into `boot.py`.** Built ahead of
need on purpose: **three vector candidates are armed and all resolve within three
weeks** (V5 3→4 ~8/3, V1/V2 ~8/15, V12 un-fire at FOMC 7/28-29). The next score move
mutates the THESIS matrix, the STATUS mirror, the histogram, the Overall line and the
BOTTOM LINE at once. A score check has to exist *before* that, not after.

## What it verifies

| # | Rule | Sev |
|---|---|---|
| **B1** | Per-vector score agrees THESIS matrix ↔ STATUS mirror (canonical = THESIS) | HARD |
| **B2** | No vector present in one matrix and missing from the other | HARD |
| **B3** | Histogram bucket membership matches the STATUS matrix score; no vector in two buckets | HARD |
| **B4** | Histogram arithmetic: `count == len(vectors)`, `sum == score × count`, bucket sums == stated total, denominator == `vectors × 5` | HARD |
| **B5** | Current-score **assertion sites** agree with the histogram total | HARD |

**Section bounding matters.** The matrix is located by its header (`| # | Vector |`),
not by row shape — `THESIS.md` contains other tables whose rows share the
`| <int> | …` form, and a naive row grep silently mixes them in.

## B5 and the false-positive that shaped it

The first implementation compared **every** `\d\d/70` in STATUS against the histogram
total, and immediately produced a false positive: STATUS legitimately carries prior
scores as history (`Net 52→51`, `recalibrated 58/60 → 53/70`, `52/70 held`).

**That was fixed rather than suppressed, because a checker that cries wolf gets
ignored — which is worse than no checker.** B5 now matches only the phrasings that
*assert* the live score:

    Convergence\s+\**(\d+)/70      -> Overall line + BOTTOM LINE
    Total:\s*\**(\d+)/70           -> the total line under the histogram

3 assertion sites currently agree. History mentions are ignored by construction, and
the report states how many sites were actually compared (same coverage-evidence
principle as Check E).

## Acceptance tests (all run 2026-07-24, all PASSED)

Each failure mode seeded into a live copy, caught, then reverted:

1. **B1** — set V5 to 4 in the STATUS mirror only (*the exact move armed for ~8/3*) →
   caught the THESIS↔STATUS drift **and** the resulting histogram mismatch.
2. **B3** — removed V5 from its histogram bucket → caught the absent vector, the
   count mismatch, the wrong total, **and** the now-wrong denominator.
3. **B4** — changed a bucket sum 28 → 29 → `sum says 29 but 7 vectors x 4 = 28`.
4. **B5** — set the Overall line to 52/70 → current-score drift caught, history
   mentions correctly ignored.
5. **B2** — deleted V7 from the STATUS mirror → caught as missing from the mirror and
   as present-in-histogram-but-absent-from-matrix.

Files verified byte-identical to their backups afterward.

## Check C — NOT built, and the reasoning

`CATALYSTS.tsv` ↔ `CALENDAR.md` event-set comparison was **declined** on
cost/value grounds, recorded here so the decision isn't silently revisited:

- **Low value.** `docket_countdown.py` reads the **TSV**, and that is what boot
  surfaces. CALENDAR drifting degrades a *human-readable twin* — a documentation
  problem, not a decision problem. Neither the ELV-date error nor any other docket
  failure this cycle would have been caught by C (that was wrong *content*, correctly
  mirrored).
- **Higher build cost than it looks.** The TSV holds ISO dates; CALENDAR holds prose
  (`~Aug 3`, `**Jul 28-29**`). Matching them means date-prose normalization, which is
  fiddly and fragile — a flaky check on a low-value surface is a net negative.

**Revisit if CALENDAR drift ever actually bites.**
