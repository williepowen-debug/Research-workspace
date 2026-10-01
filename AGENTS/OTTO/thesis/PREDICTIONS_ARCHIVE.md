# OTTO PREDICTIONS — Archive

Post-mortems for resolved rows in [`PREDICTIONS.tsv`](PREDICTIONS.tsv). The TSV keeps the row + status for the calibration scoreboard; this file holds the *what fired, what went right/wrong, calibration lesson* per resolved prediction. Read at calibration-review pass, not at boot.

---

## Calibration Scoreboard (as of 2026-07-25, session 016)

> ⚠️ **The counts in this table are as of 7/25.** Ledger at 2026-09-30 after s026 (Status column of `PREDICTIONS.tsv`): **5 CONFIRMED · 7 FALSIFIED · 1 NEEDS_VERIFY (OTTO-10) · 7 OPEN.** *(s025 read 5 · 8 · 7; OTTO-10 moved FALSIFIED → NEEDS_VERIFY on CATO RC2.)* The 9/30 set is in § *9/30 resolve set* below; OTTO-30 (resolved 8/14) has its grade in its TSV row.

| Status | Count | Notes |
|--------|-------|-------|
| **CONFIRMED (substance + window)** | 4 | OTTO-01, OTTO-08, OTTO-09, OTTO-27 |
| **CONFIRMED (substance, missed window/metric)** | 2 | OTTO-26 (right on the PSEC cut, date off 2.5mo); **OTTO-04** (deep-subprime substance confirmed, blended-index metric missed *and* unobtainable) |
| **FALSIFIED outright** | 2 | **OTTO-05** (subprime BBB spread went the *opposite* way), **OTTO-28** (falsified-on-window) |
| **OPEN** | 11 | See TSV — incl. OTTO-30 at 12% and OTTO-31 at 12%, both near-falsified |

**Hit rate (substance):** **6/8 = 75%** — *but see the credit note below; OTTO-04 should arguably not be counted at all.* *(Was reported as 5/5 = 100% — that scoreboard was stale at Jun-9 and had not absorbed the two Jul-4 falsifications. Corrected 2026-07-25; the 100% figure was never right after Jul 4 and should not be cited from any prior copy.)*
**Hit rate (substance + window):** **4/8 = 50%.**

### ⚠ OTTO-04 credit note (2026-07-25) — read before citing the hit rate

**OTTO-04 is counted above as substance-confirmed, and that is generous.** Will directed re-basing it onto the deep-subprime 10-D tranche. The *metric* re-base is right and is now OTTO's canonical measure. But the prediction was made **2026-02-23**, and on the re-based metric **EART 2022-3 was already 25.90%** (10-D filed 2026-01-28) with 2022-2 crossing days later — **the re-based claim was true-at-creation and has zero forecasting content.**

Scoring it CONFIRMED would launder a likely-miss into a hit — the OTTO-30 known-unknown trap, inverted. **No calibration credit was taken.** The genuinely forward replacement is **OTTO-34** (EART 2022-3 ≥29.0% on the Dec-2026 filing, 60%, deliberately near-coin-flip).

**The transferable rule: when you re-base an open prediction's metric, check whether the new metric was already satisfied at the original Made_Date. If it was, the prediction is not re-based — it is retired, and a fresh forward claim replaces it.**

### ⚠ The dominant failure mode is measure-design, not directional error

Counting only "was OTTO right about the world" flatters the book. Sorted by *why* a claim failed:

| Claim | World moved as expected? | Failed on |
|---|---|---|
| OTTO-26 | ✅ yes (PSEC cut) | **date specificity** |
| OTTO-29 | ✅ yes (recovery ~3%) | **window** — $113M dispute pushes resolution past Sep 30 |
| OTTO-04 | ✅ yes on deep-subprime (EART 26-27.6% >25%) | **metric** — resolved on a blended index anchored down by Santander *and* now unobtainable. Re-based 2026-07-25; retired rather than re-scored because the new metric was true-at-creation |
| OTTO-30 | ❓ unknown | **instrument** — measured OTTO's own discovery latency; press-sampling missed TFIN 10mo, OBK 7mo |
| OTTO-07 | ❓ unknown | **instrument** — nominal ledger is a stub emitting `shelf_halts=0` by default; cannot falsify a "something halts" claim |
| OTTO-05 | ❌ **no** — spreads *tightened* | genuinely wrong. The one clean directional miss, and the most valuable row here |
| OTTO-28 | ✅ yes (bifurcation) | **window** — Ally Q2 postdates the resolve date |

**Five of the seven problem rows failed on how the claim was written, not on what happened.** That is a fixable process defect, and it is more actionable than the headline hit rate. Corrective adopted 2026-07-25: **a claim must name its instrument in-row and carry a pre-registered re-check** — see `[[finding_discovery_instrument_defines_the_claim]]`. First application: **OTTO-33**.

**Do not read the 75% as "OTTO is well-calibrated on direction."** OTTO-05 is the only row where the world was cleanly tested and OTTO was wrong — the rest were never given a fair test.

---

## 9/30 resolve set — OTTO-06 · OTTO-10 · OTTO-29 · OTTO-32, scored at AS-MADE (resolved 2026-09-30, s025)

### ⛔ s026 correction (2026-09-30, CATO RC2 `433084d2b`): read this before the s025 table

CATO's finding was that three negative grades went further than the evidence recorded for them. **OTTO checked it against its own record, and it was TRUE for all three.** The scoring arithmetic was correct throughout. What failed was evidence sufficiency. **No outcome flipped, no as-made probability moved, and no term changed.**

| Row | Grade after s026 | Evidence | Calibration | As-made | Brier |
|---|---|---|---|---|---|
| OTTO-06 | ❌ FALSIFIED on the 9/28 instrument | VERIFIED: EART 10-Ds through the Aug collection month. CPS/ACA/CACC not checked | **NOT eligible.** On the 2/23 terms the result sits in the 15–18% dead zone; the clause that resolved it was written after the July data, and it decided the outcome | 70% | 0.4900, shown, not counted |
| OTTO-10 | **NEEDS_VERIFY** (s025 FALSIFIED held, not withdrawn) | Equifax through **May 2026** (Jul and Aug editions found; s025's 404s were guessed URLs). The claim runs through **Q3**, so Jun–Sep are not covered | Not eligible until covered; at the covering edition, eligible only if all four readings agree | 65% | 0.4225 staged, not counted |
| OTTO-29 | ❌ FALSIFIED-on-window / ✅ substance | **VERIFIED** on the claims agent's full docket (Verita, 1,448 entries, no distribution order, no final report) and the trustee's Dkt 1113 (final report projected 9/30/2030) | Eligible: event defined in the 4/15 seed row; window scored on the letter (Will's convention) | 75% | 0.5625 |
| OTTO-32 | ✅ CONFIRMED | VERIFIED Dkt 3748 | Eligible: the 8/27 resolver re-key did not decide the outcome (ruling 8/24 and entry 9/1 both CONFIRM) | 85% | 0.0225 |
| **Verified + eligible** | **1 of 2** | | | | **mean 0.2925** |
| *As graded s025, all four* | *1 of 4* | | | | *mean 0.3744: arithmetic correct, superseded as a verified figure* |

⚠️ **Before citing 0.2925.**
- **n=2 is not a calibration statistic.**
- **It reads better than 0.3744 only because two misses left the set on evidence grounds. No outcome changed.**
- **Verification is asymmetric.** A hit can be proven by one document, while a miss proven by absence needs complete coverage. A filter on evidence sufficiency therefore removes misses faster than hits, and every row set aside tonight is a miss.
- **0.2925 is unrelated to the "0.2927 at the walked cells" figure in the s025 table below.** The digits are a coincidence.

**The rule applied to every row (one rule, stated once):** a specification written after the claim was made (an instrument, a perimeter, a resolving clause or a granularity reading) counts for calibration only if it did not decide the outcome. If it did decide it, the observation is kept and not counted. Under that rule OTTO-32 passes, OTTO-06 fails, and OTTO-10 is tested when its covering edition lands.

**Lessons, s026:**
- **A 404 on a guessed URL is a search result, not a missing edition.** `-jul-2026.pdf` 404'd and `-july-2026.pdf` was there. Vary the URL before recording an absence.
- **A negative grade needs evidence for the whole claim period.** Data through March cannot certify "stays above 14% through Q3". The monthly prints show why: the May monthly balance share fell to 13.1%, 0.1pp above the line.
- **For a large Ch.7, the free complete docket is the claims agent's, not RECAP.** Verita's server omits its TLS intermediate; add the Go Daddy G2 intermediate from the certificate's AIA URL to the CA bundle. That verifies the chain. Do not skip verification.

### As first graded (s025), kept as recorded


| Row | Grade | As-made | Brier | Walked cell (not used) |
|---|---|---|---|---|
| OTTO-06 | ❌ FALSIFIED | 70% | 0.4900 | 70% |
| OTTO-10 | ❌ FALSIFIED | 65% | 0.4225 | 20% |
| OTTO-29 | ❌ FALSIFIED-on-window / ✅ substance | 75% | 0.5625 | 80% |
| OTTO-32 | ✅ CONFIRMED | 85% | 0.0225 | 97% |
| **Set** | 1 of 4 | | **mean 0.3744** | mean 0.2927 at the walked cells |

**Full evidence per row is in each TSV Result cell; this is the lesson layer only.**

- **OTTO-06: an instrument written late leaves a dead zone.** The row as made on 2/23 read "exceeds 18%" with the invalidation "stays <15%". EART 2022-2 printed 15.33% (Jan) and 15.22% (Aug), which lands between the two lines, so neither side resolves it. The 9/28 instrument line ("FALSIFIED otherwise") closed the gap, but it was written after the July data were visible. The grade stands on the letter, because "exceeds 18%" did not happen. **Rule: the confirm line and the invalidation line must be the same number, or the row must say what the gap resolves to.**
- **OTTO-10: the world moved against the claim, and the instrument hid it for seven months.** The subprime share ROSE on both Equifax bases, to 19.1% of accounts and 15.9% of balances. The "16.5→14.7" series that justified the 8/14 walk-down to 20% came from a synthesis document, and no Equifax table contains it. The walk-down would have cut this row's Brier from 0.4225 to 0.0400 for a reason that does not exist. **The as-made convention is what caught it.**
- **OTTO-29: the substance was right, and a hard catalyst date was the weak link again.** OTTO-26 had the same failure shape. The recovery is about 3% and the notes trade under 10¢, but no distribution had happened by 9/30 because the $113M dispute holds everything. Scored on the letter; no substance credit taken.
- **OTTO-32: the only hit, now VERIFIED.** On 9/28 the entry was INFERRED from two secondary sources. On 9/30 OTTO read Dkt 3748 itself (clerk stamp ENTERED 2026-09-01). Kroll and the CourtListener docket page still returned 403, and the RECAP search API was the route that worked. **Rule: when the docket page is blocked, try the search API before settling for secondaries.**

---

## OTTO-05 — Subprime BBB ABS spread >250bps by Jun 30 ❌ FALSIFIED (substance AND window)

**Resolved:** 2026-07-04 (s014 catch-up sweep). **Confidence at close:** had been carried at 70%.

**What happened:** the spread moved **the opposite way**. EART 2026-3 Class D (BBB/Baa3) settled ~Jun 24 at **+140bps** `[CONF SEC FWP/IFR]`, versus +190bps in March — a 50bp *tightening* against a predicted blowout to +250. The deal was **upsized to $1.2bn** and Exeter earned its **first-ever AAA** from S&P/Moody's.

**Why it was wrong:** OTTO bundled two separate claims into one conviction — *fraud is being discovered across the auto ecosystem* (true, still compounding) and *therefore subprime ABS funding will seize* (false). The primary market never stopped functioning; the fraud cases were idiosyncratic collapses, not a repricing of the asset class. Investor demand for subprime paper strengthened throughout the period OTTO expected it to break.

**Calibration lesson:** **this is the model row for the two-leg discipline.** Idiosyncratic fraud discovery and systemic funding transmission are separate bets with separate evidence and must be metered separately — see `[[finding_decouple_idiosyncratic_from_systemic_leg]]`. Banked as honest disconfirming evidence: the systemic-funding leg is **DISCONFIRMED**, and OTTO says so in STATUS rather than quietly re-dating the claim. It has stayed disconfirmed through every subsequent check (Jul 25: zero new bank names in a complete EDGAR sweep; Ally's 5th straight improving quarter).

**Worth preserving:** the *fraud* leg kept producing during the same window that the *systemic* leg died — a third collateral class (TFIN floorplan) and a federal indictment charging both OTTO mechanisms. Being wrong about transmission did not make OTTO wrong about the fraud.

---

## OTTO-28 — Ally discloses Carvana-specific DQ/NCO by Jun 30 ❌ FALSIFIED on window (substance ✅ directionally)

**Resolved:** 2026-07-04. **Confidence at close:** 55%.

**What happened:** the resolve date was set to **Jun 30**, but Ally's Q2 earnings did not print until **Jul 21** — the disclosure OTTO was predicting could not physically occur inside the window. Q1 (the only print inside the window) contained no Carvana-specific break-out.

**Why it was wrong:** a **calendar error at creation**, not an analytical one. The claim was written without checking when the disclosing event would actually happen. Ally has never broken out Carvana-sourced loans separately in any quarter, so the substance was likely false too — but the window guaranteed failure before the substance was ever tested.

**What the data showed instead — and it mattered more than the prediction:** Ally's credit is *improving*, and has kept improving. Q1: retail NCO 1.97% (−15bps YoY), 30+ DQ 4.60% (−17bps YoY, 4th straight quarter). Q2 (Jul 21): NCO **1.57%** (−18bps), 30+ DQ **4.80%** (−8bps), **5th straight**. Prime/near-prime improving while deep-subprime bleeds is exactly the bifurcation the Invisible Exit predicts.

**Calibration lesson:** **verify the disclosing event's date before setting the resolve date.** A prediction about a company disclosure inherits that company's reporting calendar; setting a resolve date earlier than the next scheduled print is an automatic loss. Pairs with the OTTO-26 date-specificity lesson — two of OTTO's seven resolved rows failed on calendar mechanics that a 30-second check would have caught. Note the asymmetry: the *falsified* prediction produced OTTO's most durable supporting evidence for the Secondary thesis.

---

---

## Failure patterns to watch for in new predictions

1. **Date-specificity at low confidence is the weakest link.** A <50%-confidence prediction with a hard date pinned to a single earnings release will probably miss the date even when the substance call is right (OTTO-26). When confidence is low, prefer a *window* over a *date*.
2. **Extrapolation off adjacent benchmarks can be wrong by a wide margin.** Subprime BBB extrapolated off A-rated +30bps came in 10-45bps below the primary-source FWP print (OTTO-05 mid-life recal 62→48%). When primary-source data exists, lean on it.
3. **Forward-discovery vs known-unknown blur.** A prediction whose *spirit* is forward-discovery ("X surfaces by Y date") can be mechanically satisfied by a known-unknown that predates the prediction window. State the spirit in the Notes column up front (OTTO-30 Origin Bancorp case).
4. **Litigation-allegation weighting ≤40% pending corporate-side confirmation.** Treating a Jan plaintiff complaint as load-bearing structural fact will get corporate-denied (OTTO-31, dropped 60→30% on M&T denial). Default to ≤40% conviction on `[ALLEG]` until `[CONF]` corroboration.

---

## OTTO-01 — 4th fraud case confirmed ✅ CONFIRMED

| Field | Value |
|-------|-------|
| **Confidence at write** | 75% |
| **Made** | 2026-02-23 |
| **Resolved** | 2026-02-26 (3 days later) |
| **Resolve_Date** | 2026-06-30 |
| **Outcome** | MFS UK confirmed — double-pledging £2B+ (Barclays + Atlas SP/Apollo) |
| **Invalidation** | No 4th case by Jun 30 2026 |

**Post-mortem.** The prediction resolved 4 months ahead of the Resolve_Date — the fastest substance confirmation in the OTTO ledger. The 75% confidence was well-calibrated for the question as posed: 4 confirmed cases had already surfaced when OTTO opened the prediction (Tricolor, First Brands, PrimaLend, + the Carvana-alleged case being tracked), and the *pattern* prediction was that one more would surface in the standard 6-month forward window.

**Calibration lesson:** when the pattern is mechanically over-determined (4 archetypes, 5+ years of latent fraud, 2022-vintage maturation), 75% may have been *under*-confident for a 6-month window. A 6-month forward case-discovery rate of 1+ has been the running rate for 9 of the last 12 months. Future similar predictions might write 85%.

---

## OTTO-08 — BDC redemptions trigger at least one fund gate ✅ CONFIRMED

| Field | Value |
|-------|-------|
| **Confidence at write** | 50% |
| **Made** | 2026-02-23 |
| **Resolved** | 2026-03 (MS North Haven gate) |
| **Resolve_Date** | 2026-12-31 |
| **Outcome** | MS North Haven gated 10.9% requests, 5% cap, 45.8% fulfilled. Blue Owl OTIC permanently gated. |
| **Invalidation** | No BDC fund gate triggered by H2 2026 close |

**Post-mortem.** Resolved 9 months ahead of the Resolve_Date. 50% was meaningfully under-confident given the structural pressure already visible at write-time (BCRED 7.9% redemption rate in Q4 2025, retail BDC AUM ~40% of total, dim outlook for H1 2026 vintage performance). The gate event was a *when*, not an *if*.

**Calibration lesson:** distinguish *probability the event happens at all* from *probability it happens within the resolve window*. For a Dec-31 resolve window on a stress mechanism that was already mechanically warming, 50% was the wrong number. Future similar predictions should anchor confidence on the time-discounted, not the point, probability.

---

## OTTO-09 — Additional BDC marks down auto/First Brands >10% ✅ CONFIRMED

| Field | Value |
|-------|-------|
| **Confidence at write** | 65% |
| **Made** | 2026-02-23 |
| **Resolved** | 2026-02 (within 2 weeks of write) |
| **Resolve_Date** | 2026-06-30 |
| **Outcome** | First Brands debt 13-16¢ senior / 0.375-0.625¢ second-lien = 80-99%+ markdowns (Feb 2026). 15 BDCs hold $237M exposure (Oaktree, FSK, PSEC, +12). |
| **Invalidation** | BDC marks stay <10% decline |

**Post-mortem.** Resolved essentially at write-time. The 10% threshold was set far too conservative — at write-time, First Brands debt was already trading at distressed levels. The threshold should have been 50% or "to recovery-implied levels" to have been a meaningful forward test.

**Calibration lesson:** check threshold-vs-current-state before publishing a prediction. If the threshold is already nearly satisfied by spot data, the prediction has no forward content. (Threshold-vs-mechanism lesson from auto-memory `[[finding_threshold_vs_mechanism]]` applies here in inverse: the threshold was *too low*, so the prediction was a trivial confirmation rather than a meaningful test of the mechanism.)

---

## OTTO-27 — FSK dividend coverage falls below 1.0x ✅ CONFIRMED

| Field | Value |
|-------|-------|
| **Confidence at write** | 50% |
| **Made** | 2026-02-23 |
| **Resolved** | 2026-Q1 (FSK cut $0.70 → $0.48; Q1 NII guide $0.44 vs new $0.48 div = 0.92x) |
| **Resolve_Date** | 2026-03-31 |
| **Outcome** | Coverage 0.92x — confirmed below 1.0x |
| **Invalidation** | Coverage stays >1.0x through Q1 |

**Post-mortem.** Resolved cleanly within the window. 50% confidence was reasonable at write — coverage was running 0.9-1.0x already and a cut was *possible* but not yet announced. The bigger move was the simultaneous *dividend cut* + *guidance miss* combo, which the prediction didn't directly capture but is the more informative signal for the broader thesis (NII compression at the BDC level).

**Calibration lesson:** when a binary threshold prediction resolves cleanly, the *adjacent richer signal* (here, the cut itself + the guidance) is often the more useful data point for the broader thesis. Predictions are crisp tests; the texture around the resolution is the actual learning. Notes column should capture both.

---

## OTTO-26 — PSEC dividend cut at Feb 20 earnings ❌ FALSIFIED on date (✅ substance)

| Field | Value |
|-------|-------|
| **Confidence at write** | 40% |
| **Made** | 2026-02-23 |
| **Resolved** | 2026-05-07 (Q3 FY26 earnings 8-K, accession 0001287032-26-000165) |
| **Resolve_Date** | 2026-02-28 |
| **Outcome** | PSEC cut $0.045 → $0.035 (~22% cut) — substance confirmed, but on May 7 not Feb 20 |
| **Invalidation** | PSEC maintains $0.06 monthly dividend |

**Post-mortem.** **The most informative resolution in the ledger.** OTTO predicted PSEC would cut at the Feb 20 earnings. PSEC *held* the dividend at Feb 20 and cut 2.5 months later at the May 7 Q3 print. The directional substance was correct (NII compression forcing a cut on a 6-month horizon), but the date specificity was wrong.

**Calibration lesson — the formal rule:** **Date-specific Resolve_Dates at <50% confidence are the weakest link.** When confidence is low, prefer a window over a date. The pattern: "X happens at Y specific earnings" requires getting both (a) the substance call right AND (b) the timing within the management's discretion right — and (b) is uncorrelated noise unless OTTO has specific intelligence on management intent. Future similar predictions:
- If <50% conviction → use a window (e.g., "by Q2 2026 earnings") not a date.
- If date-specific → confidence should be ≥60% before pinning.
- Notes column should explicitly call out "substance vs timing" decomposition at write-time.

This lesson is auto-memory-grade and has been promoted to auto-memory as `[[finding_date_specificity_weakest_link]]`.

---

*OTTO PREDICTIONS_ARCHIVE.md v1.0 | 2026-06-09 | Seeded with 5 resolved rows. Update on each new resolution.*
