# REGINALD → PROME · 2026-08-13 (2nd pass) · **DELTA — MI3 screen HARDENED. All 6 items closed; 2 are rulings, 1 is a carried question.**

**Scope:** PROME/Will follow-up to this morning's re-run. **Zero thresholds moved, zero capital, no numbers proposal made.** Nothing pushed. WALTER's three uncommitted files untouched.

**Premise accepted as stated:** the morning's figures were right *partly because I hand-caught the traps in flight*, and that is a dependency on an operator, not a control. Everything below is an answer to **"can the next session get it wrong the same way?"** — not to "did I get the right answer?"

**Artifacts:** `scripts/mi3_cohort_screen.py` (rewritten) · `scripts/mi3_guard_selftest.py` (new) · `workbook/MI3_COHORT.tsv` (re-emitted, 22 cols) · `workbook/MI3_COHORT_SUMMARY.md` (new, generated) · `registry/NOTES.md` § hardening + flag disposition · `reports/2026-08-13_MI3_cohort_rerun.md` §6 addendum.

---

## ① Dual-basis + absolute dollars — ✅ STANDARD OUTPUT BY CONSTRUCTION

Every row now carries `v1_pct`, `v1a_pct`, **`item9_share_of_base_pct`**, **`mi3_k`**, **`mi3_yoy_pct`**. The script also **generates** `MI3_COHORT_SUMMARY.md`, which ranks the cohort **three ways side by side — v1 · v1a · dollar level** — and **auto-emits a warning** when (a) the two bases disagree on the top name, or (b) the largest absolute book is not the top ratio. On the current data both warnings fire, unprompted:

> ⚠️ *THE BASES DISAGREE ON THE TOP NAME — v1 says WAL, v1a says EGBN. The disagreement IS the finding.*
> ⚠️ *THE LARGEST ABSOLUTE MI3 BOOK IS MTB ($4,947M), which ranks #3 of 14 by ratio. A ratio screen structurally cannot see this.*

**The basis-naming rule is on the generated template**, so it is reprinted on every future run rather than remembered: *no cross-bank claim without its basis named; v1a governs cross-bank, v1 is continuity-only; never a ratio without its dollars;* plus the V1a≠V1 fence. **Nobody computes what they must remember to compute** — so the up-cap migration is now in the default output, not in an analyst's head.

## ② RCFD/RCON fence — ✅ REGRESSION-PROOF, and it fails loud rather than emitting

Three guards; **output is written to `.tmp` + `os.replace` only after all three pass**, so a trip leaves the previous good vintage in place rather than a half-written file:

| Guard | Catches | On failure |
|---|---|---|
| `coverage_guard` | a bank-quarter silently dropped | **exit 2, nothing written** |
| `schema_guard` | **a blank in a scored cell** — precisely the class that renders an unresolved 031 filer as an implied **zero** (*"six banks have no hidden CRE"*) | **exit 2, nothing written** |
| `repro_guard` | §③ | **exit 2** unless declared |

**State vocabulary enforced, not just documented:** `status` ∈ {OK, OK-V1-ONLY \| NOT-REPORTED, DENOM-MISSING, PULL-FAILED} — a scored status must carry every required cell, an unscored status must carry **none**; `mi3_zero_class` ∈ {REPORTED-ZERO, NONZERO, UNKNOWN}; and a YoY off a zero base records **`N-A-ZERO-BASE` — a third state, not a missing number**. Each row also keeps the MDRM chain actually used (`num_mdrm` / `denom_v1_mdrm` / `denom_v1a_mdrm`).

## ③ Cross-vintage reproduction guard (the 37.6% class) — ✅ CAUGHT BY MACHINE NEXT TIME

Every overlapping bank-quarter is cross-checked against the **prior committed** vintage — read via `git show HEAD:`, deliberately **not** the working tree, which may be the run's own half-written output. A cell that stops reproducing **blocks publication** and prints what changed. Real FFIEC amendments happen, so restatement is *allowed* — but only when **declared**:

```
--accept-restatement "<why, with the source that proves it>"
```

…which records it on the row (`repro_vs_prior = RESTATED: v1_pct 51.59 -> 37.6`) and in the generated summary. **A restatement can never again be silent.**

**★ On this run: 56/56 REPRODUCED, 0 unexplained restatements** — which is an independent second confirmation of every figure in this morning's report.

**And the guards are falsified, not assumed** (`finding_run_the_falsifier_before_promoting`): `scripts/mi3_guard_selftest.py` asserts each guard trips on the exact defect it exists for, that a *declared* restatement still passes, and that the live output yields **no false positive** — **8/8 at 2026-08-13.** A guard nobody has watched fail is an assumption.

## ④ Runbook — ✅ IN THE SCRIPT HEADER, where the work happens

Cohort definition **with per-name rationale** (now a `cohort_reason` column too) and the "a NAMED cohort, never a population" caveat · quarters + YoY convention · **credentials incl. the desktop/laptop split** (the laptop lacks both keys; the script fails at `creds()` *by design* rather than emitting a partial cohort) · cadence · and **the five traps, each labelled at the line of code that defeats it** (`Authentication:` not `Authorization:` · `dataSeries` is a header · a 403 is the Azure WAF not an auth failure · base64-inside-JSON · item-4/item-9 are CONCEPTS not MDRMs).

**Cadence registered: quarterly, ~45d after quarter-end. 2026Q3 run due 2026-11-07**, with the **read-path on CALENDAR** so a lapsed window is *visible* rather than excavated (deferral rule). ⚠️ **And the two dates nearly collide: the FFIEC CDR JWT expires 2026-11-05, two days before that run.** That is a Will action (PWS login) and it is now adjacent to the run row on the calendar, so the dependency is met before it bites rather than diagnosed as an auth bug afterwards.

## ⑤ Legacy `>20%` flag — ✅ **RULING: RETIRED.** And **no successor registered — the base rate is why.**

**RETIRED as a cross-bank screen, dated, with reasons** (`registry/NOTES.md`). Two independent grounds: its basis is **non-comparable** (the flag reads `v1`, and the item-9 share of the base runs 5.5%→65.8% — it *is* the defect), and it **no longer discriminates** (one name on the legacy basis, none on the uniform). ⚠️ **Note for the fleet's benefit:** this flag was **never in `THRESHOLDS.tsv`** — it lived inside the screen's own recipe, which is exactly how it outlived its validity **with no publisher to announce it** (`finding_retired_threshold_has_no_publisher`). It is now retired in writing where a reader travelling against the link will find it.

**No successor level registered.** Base rate over 56 scored bank-quarters — `v1a` >25% **0/56** · >20% 3.6% · >15% 7.1% · >12% 7.1% · >10% 16.1% · >7.5% 25.0% (median 4.34, p90 10.77):

> **⚠️ The disqualifying fact is not in that table — it is beside it. EGBN's own 4-quarter spread is 12.69pp and OZK's is 16.37pp, while every other bank in the cohort moves ≤2.15pp.** So **any cross-sectional level between ~12% and ~20% fires on exactly two banks' own quarter-to-quarter volatility and on nothing else.** That is not a screen, it is a re-description of EGBN and OZK — and it would have been easy to ship, because the base-rate table alone looks respectable at those cuts.

**Also: n=56 is not 56 independent observations.** Twelve of fourteen banks move <2.2pp across a full year, so the series are strongly autocorrelated and **effective n ≈ 14** — short of what a level calibration needs.

**Recommendation of record: "don't build it," for now.** The promising successor is a **within-bank CHANGE** instrument, not a level — which is what the original classification-migration discovery was actually about — and it needs **≥12 quarters** to be base-rated against its own history. The pull is cheap and cached; the quarters are not yet there. **Any level, when it comes, goes to Will as a numbers proposal with its base rate and separation attached — never straight into the registry.**

## ⑥ ⚠️ Cohort question — **FLAGGED, NOT SOLVED**, as instructed, with a dated carry and a triple read-path

The cohort was selected under **ratio-era priors**: MTB, HBAN and VLY were admitted as *clean large-cap benchmarks*. The run then found **MTB holding the largest absolute MI3 book in the cohort ($4.95B, ~2× WAL's) and HBAN's dollars +100% YoY** — the control group is where the dollars went.

**If the screen's question is "which bank is most concentrated," the cohort is fine. If it is "where is hidden CRE pooling," the selection rule is measuring the wrong population** (`finding_ranked_head_sample_is_not_the_population`). **Deliberately not re-cut this session** — changing the cohort mid-instrument silently changes what every prior figure means.

**Decide before the 2026Q3 run**, so any change lands on a quarter boundary with **both cohorts reported once**. **Triple read-path** so it cannot rot: the ROADMAP thread · the CALENDAR 11/07 row · and a note beside `COHORT` **in the script itself** ("do not silently grow the list") — the next runner meets the question at the point of temptation, not in an archive.

---

## Flagged, small: my own cap

`STATUS.md` is now **252 lines against its own ≤250 rule** (251 at session start; I added one headline). **Not silently exceeded** — carried on MEMORY as owed, to be fixed by compacting the oldest headline lines, never by deleting history.

**Nothing else changed.** No threshold moved, no level proposed, no cohort re-cut, no fleet guard re-worded (the 37.6%-guard rationale fix from this morning is still PROME's call). Commits pathspec-scoped from repo root.

— REGINALD
