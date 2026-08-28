# MI3 HIDDEN-CRE COHORT SCREEN — RE-RUN ON A UNIFORM BASIS, BOTH BASES REPORTED

**Date:** 2026-08-13 (Thu, markets open) · **Agent:** REGINALD (PROME-directed) · **Status:** ✅ RUN — supersedes the legacy v1 screen
**Instrument:** FFIEC CDR Public Web Service, **REST + JWT**, `RetrieveFacsimile` / SDF, bank-level `ID_RSSD` filers.
**Pull:** 14 banks × 4 quarters = **56 bank-quarters, 56/56 status `OK`**, zero pull failures, zero missing denominators.
**Reproducible:** `AGENTS/REGINALD/scripts/mi3_cohort_screen.py` · machine-readable → `AGENTS/REGINALD/workbook/MI3_COHORT.tsv`
**Cohort selection (stated, not implied):** every name the legacy v1 screen scored (OZK/WAL/EGBN/ZION/SSB) + my Convergence-Matrix watchlist (CFG/BKU/SBCF/AMTB/FLG) + the clean large-cap benchmarks (MTB/HBAN/VLY) + one NDFI-heavy control (CUBI). **Not** a population — a named cohort. `finding_ranked_head_sample_is_not_the_population`.

> ## 🔴 ADDENDUM 2026-08-28 — V1a DEFINITION REVISED, ALL v1a Q2-2026 LEVELS SUPERSEDED, RANKINGS UNVERIFIED
> **Ruling (REGINALD, cross-bank surface owner):** `v1a = MI3 ÷ (item 4 + item 9.a)` — item 9.b removed from the denominator. Triggered by wal-8a's 8/28 packet identifying an 18bp definition gap between two independent primary-source pulls that each self-passed against their own recipe (`finding_crosscheck_with_free_parameter_validates_nothing` at the definition layer). **Rationale, in order of weight:** (1) OZK's `RCONPV09 ≡ RCON2746` across 6 of 6 quarters proves MI3 IS a 9.a mirror at that name, not a distribution across 9.a and 9.b; (2) item 9.b is a heterogeneous residual catchall unrelated to the MI3 loan population; (3) cross-bank comparability requires a denominator matched to the numerator's residence, not a defensively-inclusive volume.
>
> **Consequence for THIS report's Q2-2026 v1a levels:** all 14 recompute UPWARD by each bank's own 9.b size. **WAL confirmed 8.99% → 9.17% (+18bp).** Other names recompute by unknown amounts pending 11/07 re-run. **The RANKING is UNVERIFIED, not just stale** — since every ratio moves by a bank-specific 9.b, the ordering ("WAL #3, EGBN #1, MTB #2") cannot be arithmetically recovered from the published table; it needs the re-run.
>
> ⛔ **Under this addendum:** do NOT cite Q2-2026 v1a LEVELS from this report without their basis named; do NOT cite Q2-2026 v1a RANKINGS at all until the 2026-11-07 re-run lands. All non-v1a-Q2-2026 findings in this report SURVIVE unaltered — v1 legacy screen (WAL 21.20%, falling; no name >20% on the uniform basis), the 37.6% single-cell defect at OZK, the up-cap-migration hypothesis refuted 0-of-14, the ranking inversion between legacy and uniform bases at the CONCEPTUAL level (not the specific ranking). WAL's 8/13 base-rate finding on step-prone-ness (17/154 = 11.0%) is untouched.
>
> **Followups at 2026-11-07 cohort refresh:** (a) apply v1a = 4+9.a in `scripts/mi3_cohort_screen.py` header + `workbook/MI3_COHORT.tsv`; (b) pull RC-R Tier-1 + RC-C labeled CRE at RSSD 3138146 (WAL) so `KB-WAL-007`'s 474% SR 07-1 breach claim can be re-verified (**currently on superseded input; DO NOT CITE as verified**); (c) NDFI trajectory at same RSSD to convert $122.5M NDFI nonaccrual from lead to finding across 4-6 quarters.

> ## ⚠️ SCOPE FENCE — V1a ≠ V1, carry this or the result is misread
> **MI3 (`RCON2746`) measures CRE / construction / land lending NOT secured by real estate.** The secured books — WAL's office book and $99M life-science credit, OZK's RESG — are a **different object** and are untouched by every number below. "Hidden-CRE screen fell" is one keystroke from "the CRE thesis fell," and the second is false.

---

## 0. INSTRUMENT RESOLUTION — the defect that would have silently dropped 6 of 14 banks

`"Item 4"` and `"item 9"` are **concepts**; the MDRM that carries them **depends on the filing form**:

| Form | Filers here | Item 4 (C&I) | Item 9 (NDFI + other) |
|---|---|---|---|
| FFIEC 041/051 (domestic-only) | OZK, WAL, EGBN, ZION, SSB, SBCF, BKU, CUBI | `RCON1766` **total printed** | `RCONJ454` + `RCONJ464` **totals printed** |
| FFIEC 031 (foreign offices) | CFG, MTB, HBAN, FLG, VLY, AMTB | **total NOT printed** → `RCFD1763`+`RCFD1764` (4.a+4.b) | 9.b total NOT printed → `RCFDJ454` + (`RCFD1545`+`RCFDJ451`) |

A naive `RCON1766` screen returns **`None` for all six 031 filers** — including CFG and MTB, my two clean benchmarks. Read carelessly that is "six banks have no hidden CRE," i.e. **a fabricated clean result**. The script resolves by fallback chain and **records the MDRM chain actually used per row** (`num_mdrm` / `denom_v1_mdrm` / `denom_v1a_mdrm` columns). `finding_registry_names_a_concept_tool_resolves_an_instrument`.

**Zero ≠ unknown ≠ not-applicable** (fleet audit convention, RULED 2026-08-12): SBCF and AMTB print **`RCON2746 = 0`, a reported zero present in the file** — not a gap. No missing part is ever coerced to 0; a chain with any absent leg returns `None` and the row is statused `NOT-REPORTED` / `DENOM-MISSING`, never scored.

---

## 1. ★ THE LEGACY SCREEN REPRODUCES 4-OF-5. THE OZK CELL IS A SINGLE-CELL DEFECT, NOT A SCREEN-LEVEL ONE.

Legacy screen vintage identified as **12/31/2025** — all four surviving cells reproduce to 2 decimals on the legacy recipe:

| Bank | Legacy v1 cell | My 12/31/2025 v1 | Verdict |
|---|---:|---:|---|
| WAL | 24.2% | **24.24%** | ✅ reproduces |
| EGBN | 23.7% | **23.68%** | ✅ reproduces |
| ZION | 1.8% | **1.75%** | ✅ reproduces |
| SSB | 0.9% | **0.91%** | ✅ reproduces |
| **OZK** | **37.6%** | **21.03%** | ❌ **does NOT reproduce** — and not at 6/30/2025 (51.59%), 3/31/2026 (12.81%) or 6/30/2026 (9.35%) either; WAL's 8/7 run separately found no match across **18 quarters** |

**⚠️ CORRECTION TO THE STANDING GUARD.** The kill-on-sight guard is **correct on the number** — 37.6% is invalid and must not be cited or propagated. But the guard's *rationale* ("screen-level item-9.a defect") is **not what the evidence says**. There are **two separate defects** and conflating them mis-scopes the repair:

- **(a) OZK cell — a single-cell data defect.** The other four cells reproduce exactly on the identical recipe at the identical vintage, so the recipe did not produce 37.6%; something in that one cell did. `finding_reconcile_mismatch_does_not_say_which_side_is_wrong` — I am not adjusting a number to close the gap, I am recording that the cell has no reproducible provenance and is dead.
- **(b) The v1 basis — a genuine screen-level defect, and it is the one that matters.** `RCON2746`'s own FFIEC label says its balance sits in **items 4 AND 9**, while v1 divides by item 4 only. The **item-9 share of the (item 4 + item 9) base varies from 5.5% to 65.8% across this cohort** — so v1 is **not cross-bank comparable**, and §3 shows it picks a different winner.

---

## 2. THE COHORT — Q2-2026, both bases, four quarters of trajectory

`v1` = `RCON2746 ÷ item 4` (legacy basis, kept for continuity). `v1a` = `RCON2746 ÷ (item 4 + item 9)` (uniform basis = the numerator's own stated parent).
Ranked by v1, Q2-2026. All figures $K→$M, source FFIEC CDR Call Report, pulled 2026-08-13.

| Bank | v1 Q2-25 | v1 Q4-25 | v1 Q1-26 | **v1 Q2-26** | **v1a Q2-26** | MI3 $M Q2-25 | MI3 $M Q2-26 | YoY $ | item-9 share of base |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **WAL** | 22.48 | 24.24 | 23.88 | **21.20** | **8.99** | 2,246 | 2,555 | **+14%** | 57.6% |
| CUBI | 17.07 | 15.41 | 14.36 | **17.41** | 5.96 | 503 | 569 | +13% | 65.8% |
| **MTB** | 13.06 | 13.75 | 15.04 | **14.45** | **9.69** | 4,276 | 4,947 | **+16%** | 32.9% |
| **EGBN** | 31.53 | 23.68 | 18.99 | **12.44** | **10.77** | 244 | 153 | **−38%** | 13.4% |
| **OZK** | 51.59 | 21.03 | 12.81 | **9.35** | 5.46 | 1,202 | 430 | **−64%** | 41.6% |
| CFG | 8.59 | 8.44 | 8.06 | 7.62 | 4.20 | 2,223 | 2,136 | −4% | 44.9% |
| VLY | 6.15 | 7.03 | 6.39 | 6.39 | 4.69 | 522 | 539 | +3% | 26.6% |
| **BKU** | 1.71 | 3.46 | 3.23 | **5.05** | 3.29 | 81 | 237 | **+193%** | 34.9% |
| **HBAN** | 2.83 | 4.10 | 4.33 | **4.13** | 3.06 | 1,105 | 2,207 | **+100%** | 25.9% |
| FLG | 5.52 | 3.87 | 3.92 | 3.65 | 2.83 | 519 | 441 | −15% | 22.5% |
| ZION | 2.82 | 1.75 | 2.14 | 2.03 | 1.70 | 401 | 311 | −23% | 16.0% |
| SSB | 0.84 | 0.91 | 0.95 | 1.04 | 0.87 | 55 | 74 | +36% | 16.6% |
| AMTB | 0.00 | 0.00 | 0.00 | **0.00** | 0.00 | 0 | 0 | *n/a (reported zero both ends)* | 5.5% |
| SBCF | 0.00 | 0.00 | 0.00 | **0.00** | 0.00 | 0 | 0 | *n/a (reported zero both ends)* | 12.2% |

---

## 3. ★ THE BASIS CHOICE PICKS A DIFFERENT TOP NAME — the rank inverts

`finding_normalization_choice_picks_opposite_winners`. **The disagreement IS the finding.**

| Rank | by **v1** (legacy) | by **v1a** (uniform) |
|---|---|---|
| 1 | **WAL 21.20%** | **EGBN 10.77%** |
| 2 | CUBI 17.41% | MTB 9.69% |
| 3 | MTB 14.45% | **WAL 8.99%** |
| 4 | **EGBN 12.44%** | CUBI 5.96% |
| 5 | OZK 9.35% | OZK 5.46% |

**WAL is #1 on v1 and #3 on v1a. EGBN is #4 on v1 and #1 on v1a.** Mechanism is arithmetic, not credit: WAL's item-9 book is **57.6%** of its base (a $16.4B NDFI book) while EGBN's is **13.4%**, so dividing by item 4 alone inflates WAL ~2.4× relative to EGBN. **Any cross-bank statement about "who has the most hidden CRE" is a statement about the denominator until the basis is named.** Report both; the uniform basis governs cross-bank claims, the legacy basis only for continuity against a v1-vintage record.

---

## 4. ★ THE SUBSTANTIVE FINDING: THE >20% FLAG IS NOW ESSENTIALLY EMPTY, AND THE BOOK IS MIGRATING UP-CAP

1. **The legacy screen's own `>20%` flag catches exactly ONE name at Q2-2026 — WAL at 21.20%, and it is falling** (24.24 → 23.88 → 21.20). **On the uniform v1a basis it catches NOBODY** — cohort maximum is EGBN 10.77%. The "hidden-CRE cohort" as a cross-bank *screen* has emptied out.
2. **The two names the thesis was built on are the two collapsing fastest.** OZK MI3 dollars **−64% YoY** ($1,202M → $430M); EGBN **−38%** ($244M → $153M). Both are real dollar declines, not denominator effects — though OZK's C&I item-4 book also nearly doubled ($2.33B → $4.60B) so the ratio falls twice as fast as the dollars.
3. **★ And it is showing up at the large diversified banks instead: HBAN MI3 dollars +100% YoY ($1.1B → $2.2B), BKU +193% ($81M → $237M), MTB +16% ($4.28B → $4.95B), WAL +14%.** MTB carries the **largest absolute MI3 book in the cohort at $4.95B** — larger than WAL's $2.55B — while sitting on my watchlist as a *clean benchmark*. **A concentration screen keyed on the RATIO never sees this**: MTB's ratio is unremarkable because its C&I book is huge. `finding_cohort_too_small_to_move_the_index` in reverse — the dollars went where the ratio can't flag them.
4. **`finding_rising_stock_flat_inflow_means_slower_outflow` does not apply here — this is the opposite.** OZK's stock is *draining*, and the 8/10 record already names where to: bucket migration into RC-C item 9.a plus the **first-ever debt-on-debt charge-offs ($42.4M YTD Q2-26)**. The ~$490M debt-on-debt book finding survives this re-run intact; only the ratio table is superseded.

## 5. WHAT THIS DOES AND DOES NOT GRADE

| Object | Disposition |
|---|---|
| Legacy v1 cohort ratio table (37.6 / 24.2 / 23.7 / 1.8 / 0.9) | **SUPERSEDED** by §2. The OZK cell is **DEAD** (no reproducible provenance). |
| "OZK is the most hidden-CRE-concentrated bank in the cohort" | **RETRACTED.** OZK ranks **5th on both bases** at Q2-2026 and is the fastest faller. |
| "WAL 24.2% and growing fastest in cohort" | **RETRACTED** (WAL's own 8/7 run: 6-quarter two-endpoint artifact). WAL is #1 on v1 but PLATEAUED-then-falling, and #3 on the uniform basis. |
| Bucket-migration / relabeling mechanism (the *original discovery*) | **STANDS.** It is a mechanism finding, not a ratio finding — `finding_claim_outlives_its_discredited_instrument`. Instrument for it = the item-4 → item-9.a migration, now measurable per-bank in `MI3_COHORT.tsv`. |
| Secured office books (WAL office, OZK RESG), classified balances, the $99M life-science credit, the pending appraisal | **UNTOUCHED.** V1a ≠ V1. |
| NEXUS's "no valid cross-bank hidden-CRE number fleet-wide" hold | **RELEASED** — §2 is the valid cross-bank number, on a stated uniform basis, 56/56 rows sourced to primary. |

**Owed next (not done here):** a per-bank item-4 → item-9.a migration series (the mechanism instrument, §5 row 4), and whether MTB's $4.95B absolute book warrants a Matrix row. Both → ROADMAP.

---

## 6. ADDENDUM 2026-08-13 (2nd pass) — THE SCREEN IS NOW HARDENED, AND THE LEGACY FLAG IS RETIRED

*Added after PROME/Will's follow-up: the numbers above were right partly because the traps were caught by hand, in flight. That is not a control. Full record → `registry/NOTES.md` § "MI3 HIDDEN-CRE SCREEN — HARDENING + FLAG DISPOSITION".*

**Three fail-loud guards, and output is written only after all three pass** (`.tmp` + `os.replace`, so a trip leaves the previous good vintage rather than a half-written one):

| Guard | Catches | On failure |
|---|---|---|
| `coverage_guard` | a bank-quarter silently dropped | exit 2, **nothing written** |
| `schema_guard` | a blank in a scored cell — the class that renders an unresolved 031-filer as an implied **zero** (§0's fabricated clean result) | exit 2, **nothing written** |
| `repro_guard` | **the §1 defect class** — a published bank-quarter that stops reproducing vs the prior **committed** vintage | exit 2 unless DECLARED via `--accept-restatement "<why + source>"` |

**★ The §1 finding is now enforced rather than remembered: the next run cross-checks every overlapping cell and refuses to publish a silent restatement.** On this run **56/56 reproduced** — an independent second confirmation of every figure in §2. Real FFIEC amendments are still allowed through; they just cannot be silent.

**Standard output is now dual-basis AND dollars by construction.** Every row carries `v1_pct`, `v1a_pct`, `item9_share_of_base_pct`, `mi3_k`, `mi3_yoy_pct`; the script generates `workbook/MI3_COHORT_SUMMARY.md`, which ranks the cohort **three ways** (v1 · v1a · dollar level) and **auto-warns** when the bases disagree on the top name or when the largest absolute book is not the top ratio. §3 and §4.3 can no longer be missed by an analyst who simply didn't think to compute them.

**Guards are falsified, not assumed:** `scripts/mi3_guard_selftest.py` asserts each guard trips on the exact defect it exists for, that a declared restatement still passes, and that the live output yields no false positive — **8/8 at 2026-08-13.**

**★ RULING — the legacy `>20%` flag is RETIRED as a cross-bank screen** (owner-lane, dated, with reasons in `registry/NOTES.md`): its basis is non-comparable (it *is* the §3 defect) and it no longer discriminates (§4.1). It was never in `THRESHOLDS.tsv` — it lived inside the recipe, which is exactly how it outlived its validity with no publisher to announce it.

**★ RULING — no successor threshold registered, and the base rate is the reason.** Over the 56 scored bank-quarters, `v1a` >25% fires **0/56**; >20% 3.6%; >12% 7.1%; >10% 16.1%. But **EGBN's own 4-quarter spread is 12.69pp and OZK's is 16.37pp, while every other bank moves ≤2.15pp** — so **any cross-sectional level between ~12% and ~20% fires on two banks' own volatility and nothing else.** And n=56 is not 56 independent observations (12 of 14 banks move <2.2pp across a full year ⇒ effective n ≈ 14). **The promising successor is a within-bank CHANGE instrument, not a level — which is what the original classification-migration discovery was actually about — and it needs ≥12 quarters before it can be base-rated.** Any level, when it comes, goes to Will as a numbers proposal with its base rate attached, never straight into the registry.

**Cadence registered:** quarterly, ~45d after quarter-end; **2026Q3 run due 2026-11-07**, on CALENDAR — which is also where the read-path lives, so a lapsed window is visible rather than excavated. ⚠️ **The JWT expires 2026-11-05, two days before that run** (Will action).

⚠️ **Open question carried, not closed:** the cohort was selected under ratio-era priors, and the run found the dollars pooling at the names admitted as *clean benchmarks*. **Decide before the Q3 run**, so any re-cut lands on a quarter boundary with both cohorts reported once — re-cutting mid-instrument would silently change what every figure above means.

*— REGINALD, 2026-08-13. All figures FFIEC CDR Call Report, `RetrieveFacsimile`/SDF, pulled 2026-08-13; JWT expires 2026-11-05.*
