# C3 — Masking-duration base rates: how long can clean surfaces last, and what is the tell?
**Date:** 2026-08-12 | **Mode:** Thesis | **Confidence:** High (all series PRIMARY, reproducible) / Medium (the NOW-mapping, which rests on 8 quarters of one measure)
**Commission:** CARL DEEP-RESEARCH-PROMPT-C3, re-commissioned by PROME 2026-08-10 (window 8/8–8/14) | **Consumers:** CARL action (CRL-20 / CRL-21); RED info (counter-evidence leg)
**Engine:** primary-pull only, **Will-ruled 2026-08-12**. The `/deep-research` fan-out is **re-gated to user-invoked only** (Claude Code v2.1.219 — *"Claude no longer launches it on its own"*), so it is absent from the agent-launchable skills list **by design, not removed**; it remains available when Will types it. Will chose primary-pull-only with that option open. Coverage limits are stated in §Gaps, not papered over.

---

## Key Finding

**The masking framework's strongest-looking evidence is real but mostly mechanical, and the one measure that cannot be masked has been flat for eight quarters.** Bureau-wide credit-card 90+ delinquency rose **+199bps (11.13% → 13.12%)** over the exact six quarters in which bank-reported card charge-offs *fell* 80bps — a textbook masking signature. But decomposing the bureau stock into its flow shows the divergence is driven by **slower outflow, not faster deterioration**: the quarterly **flow into 90+ has been flat at 6.93–7.18% since 2024Q2**, while bank charge-off *dollars* fell 17% on flat balances. A delinquent-balance stock rises when banks charge off less, because the 180-day charge-off rule is the pipe that drains it. **In the GFC, the equivalent inflow measure did not plateau — it rose monotonically from 5.51% (2006Q1) to 10.96% (2009Q4).** Today's inflow is elevated (6.97% vs a 3.04% 2022 low) but *not accelerating*, which is what CRL-20 requires by Q1-2027.

**Net for CRL-20: this supports a cut, on CARL's pre-registered kill logic.** Two material qualifiers keep it from being a kill: the plateau sits *above* the early-GFC reading, and the aggregate Q2 bank data that would confirm it **publishes ~2.5 weeks from now** (§Timing).

---

## Evidence

### (1) The clean surface is 6 quarters old and it is not a ratio artifact

Bank-reported credit-card net charge-offs peaked **2024Q3 at 4.64%** and have fallen six consecutive quarters to **3.84% (2026Q1)** [PRIMARY: Federal Reserve, *Charge-Off and Delinquency Rates on Loans and Leases at Commercial Banks*, FRED `CORCCACBS`, last updated 2026-05-19, accessed 2026-08-12]. Card delinquency fell seven quarters, 3.22% → **2.92%** [`DRCCLACBS`]. Consumer-loan NCO fell six, 3.00% → **2.64%** [`CORCACBS`]. CARL's 0-of-4 Q2 issuer cluster is **not an issuer-selection fluke — it is consistent with an 18-month trend in the un-selected all-commercial-banks aggregate.**

Applying CARL's own denominator guard to the bank data (the guard that changed the meaning of the Q2 HHDC print):

| | 2024Q3 (peak) | 2026Q1 | change |
|---|---|---|---|
| Card NCO rate (annualized) | 4.64% | 3.84% | **−80bps (−17.2%)** |
| Avg bank card balances | $1,068.8B | $1,071.0B | **+0.2%** |
| **Implied quarterly NCO dollars** | **$12.40B** | **$10.28B** | **−17.1%** |

*Method: NCO$ = (`CORCCACBS`/400) × quarterly mean of `CCLACBM027SBOG`; the ×400 annualization is the Fed's own definition. Balances $B SA, H.8, last updated 2026-08-07.*

**The denominator explains ~1% of the rate move.** Unlike the bureau print, this improvement is a genuine reduction in realized dollar loss, not dilution by balance growth. That is a real fact and it cuts against masking.

### (2) The bank-vs-bureau divergence — the masking signature, measured

| quarter | Bureau CC 90+ | Bank CC DQ | Bank CC NCO |
|---|---|---|---|
| 2023Q1 | 8.24 | 2.47 | 2.88 |
| 2024Q3 | 11.13 | 3.20 | **4.64** ← bank peak |
| 2025Q1 | 12.31 | 3.06 | 4.46 |
| 2025Q4 | 12.70 | 2.94 | 4.07 |
| 2026Q1 | **13.12** | **2.92** | **3.84** |
| 2026Q2 | 12.92 | *not published* | *not published* |

[PRIMARY: NY Fed *Quarterly Report on Household Debt and Credit*, Aug-2026 release, underlying-data workbook p.12; FRED `DRCCLACBS`/`CORCCACBS`]

From the bank NCO peak (2024Q3) to 2026Q1: **bureau +199bps rising, bank DQ −28bps falling, bank NCO −80bps falling.** Six quarters, opposite directions. *(This independently reproduces CARL's Q2 figures exactly — 13.12% Q1, 12.92% Q2 — confirming that pull.)*

### (3) …and why it is mostly plumbing — the adversarial leg

The two measures are **stock vs flow across different perimeters**, and one structural rule links them. FFIEC's *Uniform Retail Credit Classification and Account Management Policy* requires open-end (credit-card) loans be **charged off at 180 days past due**, closed-end at 120 [PRIMARY: [OCC Bulletin 2000-20](https://www.occ.gov/news-issuances/bulletins/2000/bulletin-2000-20.html); [Federal Reserve FRRS](https://www.federalreserve.gov/frrs/guidance/uniform-retail-credit-classification-and-account-management-policy.htm)]. A charged-off balance **leaves the bank's book entirely** (numerator *and* denominator of bank DQ) but **stays in the bureau's 90+ bucket** while the furnisher reports it. So a rising bureau stock alongside falling bank metrics is **partly what the accounting produces mechanically** — and with charge-off dollars down 17%, the drain is running slower.

The test that separates the two readings is the **inflow**:

**Bureau quarterly flow into serious (90+) delinquency, credit cards** [PRIMARY: HHDC Aug-2026 workbook p.14]

| 23:Q1 | 23:Q3 | 24:Q1 | **24:Q2** | 24:Q4 | 25:Q2 | 25:Q4 | **26:Q2** |
|---|---|---|---|---|---|---|---|
| 4.57 | 5.78 | 6.86 | **7.18** | 7.18 | 6.93 | 7.13 | **6.97** |

**Eight quarters flat in a 6.93–7.18 band.** The stock kept rising; the inflow stopped rising in mid-2024. That is the signature of slower removal, not faster failure — and it is the reading that survives.

### (4) The tell taxonomy, ranked by measured lead time

Turn dates computed from the primary series (trough = local minimum followed by ≥2 consecutive rises and an eventual ≥40bps rise):

**GFC** — mortgage DQ troughed **2004Q4 (1.41%)** and rose continuously; card DQ troughed **2005Q4 (3.54%)**; card NCO bottomed **2006Q1 (3.18%)** and did not begin its sustained rise until **2007Q3**, reaching **10.54% by 2009Q4**. Mortgage DQ led headline card convergence by **~10 quarters**; card DQ led card NCO by **~6**.

**2001** — C&I and all-loan DQ turned **1999Q4**, card DQ **2000Q1**, card NCO **2000Q2 (4.10%)** → peak **7.78% (2002Q1)**. Lead ~2 quarters: a fast, shallow-lag episode.

**2015-16 energy** — C&I DQ turned **2014Q4 (0.72%)** and ran +88bps to 1.60% (2016Q2); card NCO rose only **+47bps** (3.02→3.49). *Extends, does not re-run, DEWEY 2026-07-10.*

| Rank | Tell | Typical lead | Status NOW |
|---|---|---|---|
| 1 | **Bureau inflow into 90+** (un-maskable by issuer choice) | rises monotonically through the whole build | ⚪ **FLAT 8 quarters** — not firing |
| 2 | Mortgage/collateralized DQ | ~10q (GFC) | 🟡 rising, but only **+19bps over 9q** (1.70→1.89) vs GFC's +88bps/10q |
| 3 | Delinquency turning while charge-offs still fall | ~6q (GFC) | 🔴 **absent** — both falling together |
| 4 | C&I / commercial DQ | 2–6q | ⚪ flat (1.33→1.34) |
| 5 | Provision/ACL build | *unmeasured this run* | — see §Gaps |

### (5) Mapping to NOW

The pre-GFC card surface stayed clean for a **long** time — NCO fell 2002Q1 (7.78%) to 2006Q1 (3.18%), then plateaued ~3.2–4.0% for five more quarters before converging. **Six quarters of clean is well inside the historical range for "masking still in progress"**, so *duration alone cannot kill CRL-20*. But in that episode the tells fired *during* the plateau: mortgage DQ up 88bps and card DQ up 59bps while card NCO made lows. **Today only the weakest of those is present, and the un-maskable one is flat.**

On the base rate the prompt asked for: I built it (troughs after ≥4 and ≥6 consecutive declines, 8-quarter forward window, complete windows only) and it yields **n=3–4 non-overlapping episodes in 40 years**, 67–75% reversing ≥50bps. **I am not resting anything on that number** — n is too small, and "does a credit series eventually rise" has free parameters (run length, threshold, horizon) and near-zero power to separate masking from ordinary cyclicality. The divergence/inflow decomposition replaces it as the load-bearing test. *(Recorded because a first pass of that same base rate, before I caught two defects — incomplete forward windows and mid-run trough detection — read 33% and pointed the opposite way.)*

---

## Counter-Evidence

**Against the cut (i.e. arguments that preserve CARL's framework):**
1. **Flat is flat at an elevated plateau.** 6.97% inflow vs the 2022Q1 low of 3.04%, and **above the 2006Q1 early-GFC reading of 5.51%**. A high plateau is not healing; a stock can keep building for years at constant inflow.
2. **Composition masking predicts exactly this.** If issuers tighten origination and shed the worst cohort, *both* bank DQ and NCO improve together and inflow stalls — the absence of divergence-within-bank-data is **consistent with**, not evidence against, the framework. This is the strongest defense and it is not refuted here.
3. **The stock divergence is still 199bps and only partly explained.** I show the mechanism can produce it; I have not quantified *how much* of it the mechanism produces. That decomposition needs charged-off-balance persistence data I do not have.
4. **Mortgage DQ is rising** — the earliest GFC tell, present today, and the only series in the set that is up.

**Against the framework:**
5. Bank charge-off **dollars** fell 17.1% on +0.2% balances — a real loss reduction, not a denominator artifact, and the opposite of what CARL found in the bureau print.
6. Q2 issuer prints were **0 of 4** (ALLY −40bps, COF −39bps + $662M release, SYF 5.43% under ceiling, AXP flat) and now reconcile with the aggregate rather than standing apart from it.

**Explicit negative:** I searched for a documented prior episode in which a "masking" bear narrative was *ex-post* shown to be wrong, and **could not confirm one to primary-source standard** in this session. The 2015-16 energy episode is the closest candidate in my own data (a leading C&I DQ tell that converted to only +47bps of card NCO), but I did not verify contemporaneous commentary characterizing it as masking. **Sub-answer 5's adversarial leg is therefore partially unmet** — flagged, not synthesized around.

---

## Source Quality Assessment

All quantitative claims are **[PRIMARY]** — Federal Reserve Call Report aggregates (FRED), Federal Reserve H.8, NY Fed HHDC underlying-data workbook, FFIEC/OCC policy. No secondary figures. The regulatory charge-off rule is doubly sourced (OCC + Federal Reserve FRRS). Every derived figure is reproducible from the recipe in §Reproduction.

**Weakest link:** the NOW-mapping rests on **eight quarters** of the inflow series. Eight observations is thin for a plateau-vs-pause call, and one more quarter of the same could look materially different.

---

## Gaps (completeness-critic pass — 5 required sub-answers + 1 addition)

| # | Sub-answer | Status |
|---|---|---|
| 1 | GFC vintage study | ⚠️ **PARTIAL** — aggregate lag structure measured precisely; **issuer/ABS vintage-level loss curves NOT pulled** (needs EDGAR/ABS-EE) |
| 2 | 2015-16 energy | ✅ measured, extends 7/10 report |
| 3 | Third analog (2001) | ✅ measured |
| 4 | Tell taxonomy | ⚠️ **PARTIAL** — **provision/ACL build UNMEASURED** (FDIC QBP not pulled); subordinate-tranche rating actions not pulled. Both were named in the prompt's tell list |
| 5 | Mapping to NOW + adversarial | ⚠️ **PARTIAL** — mapping complete; **the "find a benign ex-post episode" leg is unmet** (see Counter-Evidence) |
| 6 | Q2-2026 0-of-4 cluster as datapoint | ✅ incorporated (§1, §Counter-Evidence 6) |

**Three of six are partial. None is silently synthesized around.** The two highest-value follow-ons are the **ACL/provision tell** (FDIC QBP, cheap) and the **charged-off-balance persistence decomposition** (would convert Counter-Evidence #3 from an open question into a number).

---

## Timing — decision-relevant

The Fed's charge-off/delinquency release publishes **~60 days after quarter end**, so **Q2-2026 aggregates land ~late August 2026** (Q1 was released 2026-05-19). **The un-selected aggregate cross-check on CARL's 0-of-4 Q2 issuer cluster does not exist at any source today and is roughly 2.5 weeks out.** If CRL-20 is to be cut on this analysis, that print is the natural confirmation gate — and it arrives well before the Q1-2027 window.

---

## Reproduction

FRED (via `AGENTS/DEWEY/scripts/fred_pull.py SERIES --all --csv`): `CORCCACBS`, `DRCCLACBS`, `CORCACBS`, `DRCLACBS`, `CORBLACBS`, `DRBLACBS`, `CORALACBS`, `DRALACBS`, `DRSFRMACBS`, `DRCRELEXFACBS`, `CORCREXFACBS`, `CCLACBM027SBOG`.
HHDC: `curl -A "<browser UA>" https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/xls/HHD_C_Report_2026Q2.xlsx` → sheets `Page 12 Data` (90+ share by loan type) and `Page 14 Data` (flow into 90+). **Select columns by header name, not position** — the two sheets order loan types differently (p.12 is MORTGAGE-first, p.14 is AUTO-first).
NCO dollars = (`CORCCACBS`/400) × quarterly mean of `CCLACBM027SBOG` ($B).
⚠️ `fred.stlouisfed.org` and `newyorkfed.org` both **403 on WebFetch**; both yield to the API / `curl` with a browser UA.

---

## Process Report

**Searches run:** 2 WebSearch (FFIEC charge-off rule; Fed release schedule), 4 WebFetch (2 succeeded — Fed definitions + release page; 2 × 403 on FRED). Primary pulls: 12 FRED series full-history, 1 FRED metadata batch, 1 NY Fed xlsx (963KB).
**Data gaps:** FDIC QBP ACL series; issuer vintage loss curves; charged-off-balance persistence; contemporaneous "masking narrative" commentary for the adversarial leg.
**Source frustrations:** FRED **and** NY Fed both 403 `WebFetch` — the API and `curl+UA` both work, so a 403 here is a statement about one mirror, not the source. `openpyxl` is absent from system python but present in `.venv` — use `.venv/bin/python` for xlsx.
**Engine-premise error, caught at closeout (the 4th):** at engine-selection I told Will the fan-out was *"not installed / gone"* and offered options on that basis. **Wrong, and it is a repeat of my own 2026-07-28 correction** (`finding_skill_regated_not_removed`): the skill is **re-gated to user-invoked**, not removed, so "absent from my list" is the gating working correctly. Will's primary-pull-only ruling stands on its merits, but it was made against a premise I had already been corrected on once — the memory existed and I did not check it before propagating. *(Still unverified since 7/28, and worth one cheap test: whether the manual path actually fires on 2.1.220.)*

**Errors caught in-run (3):** ① base-rate v1 scored recent episodes against *incomplete* forward windows and could land mid-decline instead of on a true trough — fixing it **inverted** the result (33% → 67-75%); ② H.8 balances read as $M when the series is $B (1000× on every dollar figure); ③ HHDC column selected by position, which silently returned the **student-loan** column as "CC" — the two sheets order loan types differently. All three would have shipped a wrong load-bearing number.
**Confidence:** High on every figure (primary, reproducible). Medium on the NOW-mapping — 8 observations.
**If I had more time/tools:** pull FDIC QBP for the ACL tell; decompose the 199bps stock divergence into charge-off-timing vs genuine deterioration.
**Suggestions:** the base-rate harness (trough detection + complete-window guard) is reusable and currently dies with this session — a candidate for `scripts/` if a second commission needs it. Will-gated per the build gate; **not** promoted unilaterally.
