# OTTO PREDICTIONS — Archive

Post-mortems for resolved rows in [`PREDICTIONS.tsv`](PREDICTIONS.tsv). The TSV keeps the row + status for the calibration scoreboard; this file holds the *what fired, what went right/wrong, calibration lesson* per resolved prediction. Read at calibration-review pass, not at boot.

---

## Calibration Scoreboard (as of 2026-07-25, session 016)

| Status | Count | Notes |
|--------|-------|-------|
| **CONFIRMED (substance + window)** | 4 | OTTO-01, OTTO-08, OTTO-09, OTTO-27 |
| **CONFIRMED (substance, missed window)** | 1 | OTTO-26 — right on the PSEC dividend cut, missed the date by 2.5 months |
| **FALSIFIED outright** | 2 | **OTTO-05** (subprime BBB spread went the *opposite* way), **OTTO-28** (falsified-on-window) |
| **OPEN** | 11 | See TSV — incl. OTTO-30 at 12% and OTTO-31 at 12%, both near-falsified |

**Hit rate (substance):** **5/7 = 71%.** *(Was reported as 5/5 = 100% — that scoreboard was stale at Jun-9 and had not absorbed the two Jul-4 falsifications. Corrected 2026-07-25; the 100% figure was never right after Jul 4 and should not be cited from any prior copy.)*
**Hit rate (substance + window):** **4/7 = 57%.**

### ⚠ The dominant failure mode is measure-design, not directional error

Counting only "was OTTO right about the world" flatters the book. Sorted by *why* a claim failed:

| Claim | World moved as expected? | Failed on |
|---|---|---|
| OTTO-26 | ✅ yes (PSEC cut) | **date specificity** |
| OTTO-29 | ✅ yes (recovery ~3%) | **window** — $113M dispute pushes resolution past Sep 30 |
| OTTO-04 | ✅ yes on deep-subprime (EART 26-27.6% >25%) | **metric** — resolves on a blended index anchored down by Santander; *and* the index is now unobtainable (see 2026-09-01 decision row) |
| OTTO-30 | ❓ unknown | **instrument** — measured OTTO's own discovery latency; press-sampling missed TFIN 10mo, OBK 7mo |
| OTTO-07 | ❓ unknown | **instrument** — nominal ledger is a stub emitting `shelf_halts=0` by default; cannot falsify a "something halts" claim |
| OTTO-05 | ❌ **no** — spreads *tightened* | genuinely wrong. The one clean directional miss, and the most valuable row here |
| OTTO-28 | ✅ yes (bifurcation) | **window** — Ally Q2 postdates the resolve date |

**Five of seven problem rows failed on how the claim was written, not on what happened.** That is a fixable process defect, and it is more actionable than the headline hit rate. Corrective adopted 2026-07-25: **a claim must name its instrument in-row and carry a pre-registered re-check** — see `[[finding_discovery_instrument_defines_the_claim]]`. First application: **OTTO-33**.

**Do not read the 71% as "OTTO is well-calibrated on direction."** OTTO-05 is the only row where the world was cleanly tested and OTTO was wrong — the rest were never given a fair test.

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
