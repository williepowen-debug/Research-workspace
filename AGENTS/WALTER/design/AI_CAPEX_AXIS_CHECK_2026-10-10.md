# AI_INFRA_CAPEX — COHERENCE REVIEW, 2026-10-10

reviews_cluster: AI_INFRA_CAPEX

**Date:** 2026-10-10 · **Run by:** WALTER (`walter-66`) · **Trigger:** `walter_doctor cluster_review_overdue`: 118 signals, last review 40d ago (window 30d). Run on Will's "continue working on our owed or incomplete tasks".
**Authority:** `CLUSTER_TAXONOMY` v0.7 cadence trigger; the v0.6 bidirectional test is the instrument. Evaluation is WALTER's; changing structure is Will's (RULE 8).
**Precedent:** [`AI_CAPEX_AXIS_CHECK_2026-08-31.md`](AI_CAPEX_AXIS_CHECK_2026-08-31.md) · [`…07-27`](AI_CAPEX_AXIS_CHECK_2026-07-27.md) · [`…07-16`](AI_CAPEX_AXIS_CHECK_2026-07-16.md)

## 1. Verdict

> **KEEP the cluster. Limb (a) does NOT fire on the comparable method (5 populated angles, unchanged since 8/31). Limb (b) fires on obsolescence, which has had ZERO new signals since the last review. The one datum 8/31 counted there (`-0828-050`) sits inside both windows.**
>
> 🔑 **The finding is not the count. It is that the 8/31 remedy for obsolescence was never executed, and the domain moved without us.** The 8/31 review prescribed an intake collection rule for depreciation / useful-life news (its rec 1). The 9/8 catch-up deferred it on purpose ("obsolescence lane"). It has not shipped: `newsweep_config.py` carries zero such terms. On 10/10 a live 30-day Google-News sample for `GPU depreciation` returned **5 of 5 on-topic headlines**, including Michael Burry's 10/1 "GPU Depreciation & Useful Lives" post and the coverage that followed. The lane holds **0 hits in 12,276 headlines** (2026-06-29 → 10-09). **Empty in INTAKE, live in the DOMAIN**, the same shape as memory before July's fix.

## 2. Scope and method

**65 signals in the trailing 60-day window (2026-08-11 → 2026-10-10)** of 118 total. There is still no `axis:` field, so angles are a judgment read: one PRIMARY angle per signal, on its SUBJECT, not on keyword presence (a mention is not a declaration).

**How the read was done, stated so the counts can be audited:**
1. An Opus read-only subagent read all 65 (frontmatter, H1, first paragraph, more where ambiguous) and wrote one row per signal with a reason: `research/2026-10-10_aicapex60_angles.tsv` (65 rows, ID set = input list). It allowed an `OTHER` bucket.
2. ⚠️ **Method difference, made explicit:** the 7/16, 7/27 and 8/31 reviews filed every signal under one of the six named angles, with no OTHER bucket (8/31's counts summed to all 52). The subagent's strict reading produced 5 OTHER groups. To keep the series comparable, **WALTER folded each OTHER row to its nearest named angle** (§3 lists every fold) and reports the strict reading as a sensitivity (§4). Without this note, a jump from 5 to 8 populated angles would read as the cluster fragmenting. It did not.
3. WALTER spot-checked the subagent's least-sure calls and four of the folds at the signal's title and action line (`-0928-022`, `-0914-011`, `-0819-001`, `-0828-050`). The other rows rest on the subagent's reasons as written in the TSV.

## 3. The bidirectional test (comparable method)

| Angle | 60d (comparable) | Subagent strict | Folded in | vs 8/31 (52-signal window) |
|---|---:|---:|---|---|
| **financing** | **24** | 22 | `-0928-022` (forced sale; BROCK's ask is a GPU-financing anchor) · `-0914-007` (SoftBank; the OpenAI IPO was its cash-out route) | ~15 |
| **memory / input-cost** | **22** | 18 | `-0819-001`, `-0819-010`, `-0819-017` (the 8/19 memory-complex selloff; `-0819-001`'s own finding: "a semiconductor event") · `-0826-002` (Micron governance) | ~13 |
| **ROI / capex-guidance / FCF** | **8** | 5 | `-0828-034` + `-0903-011` (Bernstein double-ordering: "inflates the order book capex guidance is built on") · `-0914-011` (lab divergence asked against the capex frame) | ~11 |
| **power** | **8** | 8 | — | ~8 |
| **supply-chain / geopol-semis** | **2** | 2 | — (`-1003-007` Tencent/Oracle is one of the two; if it moves to ROI this angle drops below 2) | ~4 |
| **obsolescence** | **0** | 0 | — (`-0828-050` BCA filed under ROI: its ask is the EBIT-margin path under heavy D&A, not useful life; 8/31 counted it here, and it is in both windows) | 1 |
| *excluded: mis-clustered* | 1 | — | `-0929-010` Oracle layoffs → belongs in CONSUMER_STAGFLATION (its own `cluster_secondary`; action LABOR; AI borrowing is context) | — |

**Limb (a), dispersion (>5 populated?):** 5 populated (financing, memory, ROI, power, supply-chain). **Does NOT fire.** Same count as 8/31. ⚠️ Supply-chain sits at exactly 2 and hinges on one judgment call (`-1003-007`).

**Limb (b), concentration (any ORIGINAL angle <2?):** financing 24 · ROI 8 · input-cost 22 · **obsolescence 0. FIRES on obsolescence**, as it has at every review since July (7/27: 0 · 8/31: 1, the same `-0828-050` · 10/10: 0 new).

**Concentration, recorded beside the test:** financing + memory = 46 of 64 in-cluster signals (72%), up from ~54% on 8/31. The 8/31 broadening has partly reversed. This is not a limb of the test, but it is the direction to watch.

## 4. Sensitivity: the strict reading

On the subagent's strict reading, 8 angles have ≥2 signals, which would fire limb (a). It does not hold up as a dispersion finding:
- **"AI/semis equity repricing" (4)** is two events: the 8/19 memory rout (3 signals) plus one hedge-fund forced sale.
- **"Phantom demand / double-ordering" (2)** is one survey plus its own correction, and the survey was not found at a primary.
- **"Frontier-lab trajectory" (2)** is the only OTHER group with two independent items (the SoftBank/OpenAI IPO deferral and the DeepMind rumor). **One to watch, not an angle yet.**

## 5. Obsolescence: same diagnosis as 8/31, remedy still unexecuted

| Question | Answer (10/10) |
|---|---|
| **INTAKE:** depreciation / useful-life collection in `newsweep_config.py` | **ZERO** (grep for `useful life`, `depreciation`, `refresh cycle`, `obsolesc`: the only hit is "insurance impairment", unrelated). Deferred on purpose 9/8 (`PROME/inbox/processed/2026-09-08_from-WALTER_codex-owner-catchup-completion.md`: "Deliberately deferred: … obsolescence lane"). |
| **DOMAIN:** is the subject live? | **Yes.** Live 30-day Google-News sample, `GPU depreciation`: 5 of 5 on-topic (Burry's "GPU Depreciation & Useful Lives", 10/1; coverage of his "1960s computer leasing" comparison; a 9/16 piece on "the GPU depreciation debate behind this week's AI dip"; a GPU-resale-value piece; an analyst column). Same 30 days also carry NVIDIA's own defense blog, Reuters on Nvidia using its chips to finance the boom, and GPU-backed lending stories. Harness output: `research/2026-10-10_obsolescence_harness.txt`. |
| **On the BOARD?** | **No.** Zero BOARD signals Aug–Oct on GPU-backed loans, the leasing-bubble comparison, NVIDIA's useful-life defense, or insurers de-risking chip loans (grep, 10/10). WALTER sent a verify agent on these items the same session; any dispatch is recorded separately. |
| **Instrument:** a VULCAN threshold on useful life | **None** (no VULCAN registry). 8/31 rec 2 (VULCAN owes an instrument decision) is still open. |

## 6. Recommendations (WALTER proposes; structure is Will's)

1. **🔴 Re-raise the obsolescence intake rule to PROME (who lands lane changes), now with live evidence.** Candidate query: `"GPU depreciation"`, 5/5 on-topic in the live sample. The 8/31 candidates `useful life servers` and `depreciation schedule hyperscaler` returned 0 live hits, so drop them. ⚠️ A WATCH_FOR phrase alone is not enough: no current lane query fetches the subject, so the lane needs a fetch query, not only a matcher phrase (the 9/25 VULCAN lesson). Run the harness `--live` against any candidate before it lands.
2. **🟠 VULCAN instrument decision, still owed since 8/31:** a useful-life / depreciation threshold row, or a formal fold of obsolescence into ROI.
3. **🟡 The 5-axis re-cut** (`financing · ROI (incl. obsolescence) · memory/input-cost · power · supply-chain/geopol`), VULCAN-proposed 7/16 and still not adopted. Today's read supports it again: obsolescence has produced zero new signals in two review windows, and the fold would end limb (b)'s standing fire. Needs Will + VULCAN. **But record the tension:** folding obsolescence into ROI while intake cannot see the subject would hide the gap rather than close it. Do rec 1 first.
4. **🟡 `-0929-010` (Oracle layoffs):** propose re-filing to CONSUMER_STAGFLATION. Not done here; a cluster re-tag changes an INDEX section, so it goes through the normal lifecycle edit with the reason recorded.
5. **📌 Watch:** financing + memory concentration (72%); supply-chain at the 2-signal edge; the frontier-lab group at 2.

## 7. Limits

- Angle assignment is judgment, not measurement. The comparable counts depend on WALTER's nine folds and one exclusion (§3) and on the subagent's 55 unchanged calls, which WALTER did not re-read individually.
- "Empty in intake" is shown by lane-grep and lane-hit evidence. "Live in the domain" rests on one 30-day sample of one query. That is evidence of presence, not of volume.

## 8. Addendum 2026-10-10 ~15:05 ET: recommendation 1 LANDED

PROME landed four lane FETCH rows in RESEARCH-INTAKE at `5a3b083` (verified at the artifact by WALTER, `scripts/newsweep_config.py` lines ~273–301): `"GPU depreciation"` (WALTER live 5/5) · `"GPU collateral"` (PROME live 3 of 7, 0 FALSE) · `"GPU-backed loan"` (1 of 8) · `"residual value guarantee"` (1 of 8). One row per leg, agents VULCAN + BROCK, labels `gpu-obsolescence-1..4`, under WQ-348 C7. The 0-live-hit 8/31 candidates were not landed. **Next review: check whether the obsolescence angle now populates from these rows**, and say so if limb (a) fires because of them (8/31 rec 4). ⚠️ The FORGE mirror (`FORGE/tools/news-sweep/config.py`) did NOT take the rows (no ai-capex anchor block; PROME's L634 drift), although the `5a3b083` commit body says it did. The mirror is the known-dark legacy feed, so the lane is unaffected.
