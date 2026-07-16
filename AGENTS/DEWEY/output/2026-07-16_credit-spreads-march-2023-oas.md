# CREDIT SPREADS, MARCH 2023 — ICE BofA HY & IG OAS, DAILY
**Date:** 2026-07-16 | **Mode:** Cold (data hunt) | **Confidence:** High

## Key Finding

Credit spreads **did** widen in March 2023, and they were **already widening on Mar 9–10, concurrent with SVB's run and failure — not only after it.** HY OAS bottomed **Mar 6 at 397bps**, ticked up **Mar 8 (+11 → 409)**, then **Mar 9 (+18 → 427)** and **Mar 10 (+34 → 461)**. But the **single largest day was Mar 13 (+42 → 503)**, the first session *after* the failure. Peak **522bps on Mar 24**; IG peaked earlier, **164bps on Mar 15**.

**Full daily history was recovered at [PRIMARY] quality** despite FRED's rolling-3yr truncation — see *Retrieval* below. The prior BACKLOG ruling that no free source exists is **refuted**.

## Retrieval — the truncation workaround (reusable)

FRED's free ICE BofA (`BAML*`) series are truncated to a rolling ~3yr window (earliest obs **2023-07-17**). Verified 2026-07-16 that this is a **licensing cut across the whole family**, not a per-series issue:

| Path | Result |
|---|---|
| FRED API | ❌ truncated at 2023-07-17 |
| `fredgraph.csv?cosd=2023-02-01` | ❌ **truncated too** — the hoped-for workaround FAILS |
| `fredgraph.csv` + `vintage_date` (ALFRED) | ❌ truncated |
| Live `fred.stlouisfed.org/data/<ID>.txt` | ❌ HTTP 000 (blocked/dead) |
| **Wayback snapshot of `/data/<ID>.txt`** | ✅ **FULL HISTORY 1996-12-31 → 2023-12-11** |

Uniform truncation confirmed across `BAMLH0A0HYM2`, `BAMLC0A0CM`, `BAMLH0A0HYM2EY`, `BAMLHYH0A0HYM2TRIV`, `BAMLCC0A0CMTRIV`, `BAMLC0A4CBBB`, `BAMLH0A3HYC` — **all** first-obs `2023-07-17`.

**Working sources** (both re-pulled and verified independently by DEWEY, not just by the sub-agent):
- HY: `https://web.archive.org/web/20231212182755id_/https://fred.stlouisfed.org/data/BAMLH0A0HYM2.txt` — [PRIMARY] Ice Data Indices, LLC via FRED
- IG: `https://web.archive.org/web/20240623204207id_/https://fred.stlouisfed.org/data/BAMLC0A0CM.txt` — [PRIMARY]

Header confirms provenance: `Source: Ice Data Indices, LLC` · `Date Range: 1996-12-31 to 2023-12-11` · `Units: Percent` (×100 → bps).

⚠️ **Caveats:** the *live* `/data/` endpoint is dead — only the **archived** copy works, so this is a history-recovery path, not a live-data path. Use `curl --compressed` + the `id_` raw modifier. Use the **CDX index API** to enumerate snapshots; `archive.org/wayback/available` returns **false negatives** (claimed zero snapshots for URLs with five).

## Evidence — HY OAS (BAMLH0A0HYM2), bps, daily close

| Date | bps | Δ | Event anchor |
|---|---|---|---|
| 2023-03-01 | 417 | | |
| 2023-03-02 | 418 | +1 | |
| 2023-03-03 | 405 | −13 | |
| **2023-03-06** | **397** | −8 | **March trough — tightening into the crisis week** |
| 2023-03-07 | 398 | +1 | |
| 2023-03-08 | 409 | **+11** | **first widening tick** |
| 2023-03-09 | 427 | +18 | SVB deposit run / stock collapse |
| 2023-03-10 | 461 | **+34** | **SVB closed by regulators** |
| 2023-03-13 | 503 | **+42** | **largest single day** — first session after failure |
| 2023-03-14 | 474 | −29 | |
| 2023-03-15 | 520 | +46 | Credit Suisse AT1 stress |
| 2023-03-16 | 493 | −27 | |
| 2023-03-17 | 517 | +24 | |
| 2023-03-20 | 515 | −2 | |
| 2023-03-21 | 485 | −30 | |
| 2023-03-22 | 500 | +15 | |
| 2023-03-23 | 510 | +10 | |
| **2023-03-24** | **522** | +12 | **PEAK (close basis)** |
| 2023-03-27 | 503 | −19 | |
| 2023-03-28 | 501 | −2 | |
| 2023-03-29 | 483 | −18 | |
| 2023-03-30 | 474 | −9 | |
| 2023-03-31 | 458 | −16 | month-end |

**Retrace:** Apr 3 458 · Apr 5–6 484 (secondary bump) · **Apr 18 437 (April trough)** · Apr 28 450 · Apr 30 453 · May 1 445 · **May 4 495 (May high — regional-bank round 2)** · May 31 469.

**Feb baseline:** Feb 27 421 · Feb 28 422.

## Evidence — IG / US Corporate OAS (BAMLC0A0CM), bps, daily close

| Date | bps | Δ |
|---|---|---|
| 2023-03-01 | 129 | |
| 2023-03-03 | 125 | −2 |
| **2023-03-06** | **124** | −1 (trough) |
| 2023-03-08 | 127 | +2 |
| 2023-03-09 | 130 | +3 |
| 2023-03-10 | 137 | +7 |
| 2023-03-13 | 151 | +14 |
| 2023-03-14 | 150 | −1 |
| **2023-03-15** | **164** | +14 — **PEAK** |
| 2023-03-16 | 161 | −3 |
| 2023-03-17 | 162 | +1 |
| 2023-03-20 | 162 | 0 |
| 2023-03-24 | 154 | |
| 2023-03-31 | 145 | month-end |

**Retrace:** Apr 18–19 137 (April trough) · Apr 30 141 · May 4 151 · May 31 142.

## The lead/lag verdict — dates pinned

| Question | Answer |
|---|---|
| Was HY OAS widening **before** SVB failed (Mar 10)? | **Yes, but only barely and only from Mar 8.** Trough Mar 6 (397). Mar 8 +11, Mar 9 +18. |
| Was it widening on Mar 9–10? | **Yes — decisively.** +18 then +34. By Mar 10 close it was 461, already +64bps off the Mar 6 low. |
| Did the bulk come after? | **The single biggest day was Mar 13 (+42), after the failure.** But Mar 6→Mar 13 = +106bps total, of which **+64 (60%) landed Mar 8–10, before that session.** |
| Peak-to-trough | **HY: +125bps** (Mar 6 397 → Mar 24 522). **IG: +40bps** (Mar 6 124 → Mar 15 164). |
| Do HY and IG peak together? | **No.** IG peaked **Mar 15 (164)**; HY peaked **Mar 24 (522)**. HY's Mar 15 print (520) is within 2bps of its Mar 24 max — "mid-March peak" is defensible for HY within noise, but the maximum is Mar 24. |

**Read for the lead/lag thesis:** credit was **coincident-to-slightly-lagging**, not leading. It was *tightening* (397, a local low) as late as Mar 6 — three days before the run — so it gave **no advance warning**. It moved in step with the equity/funding event on Mar 9–10 and took its largest step the session after. **Nothing here supports credit leading funding stress; it modestly supports credit lagging it.**

⚠️ Sequencing caveat: these are **daily closes**. Mar 9-vs-Mar 10 ordering at intraday resolution needs a terminal. Also, the Mar 8 +11bps tick coincides with Silvergate's announced wind-down (same session) — I did **not** independently source that event date, so do not attribute Mar 8 to SVB anticipation without verifying it. `[UNVERIFIED]` as an attribution.

## Secondary — KRE regional-bank ETF drawdown

[PRIMARY] Yahoo Finance OHLC via `yfinance`, retrieved 2026-07-16. **The ~-28% claim is basis-dependent — it is NOT reachable Mar 8→Mar 15 on a close-to-close basis:**

| Basis | Mar 8 close (57.70) → | Mar 6 close (59.93) → |
|---|---|---|
| Mar 15 **close** (44.64) | **−22.6%** | −25.5% |
| Mar 13 **close** (44.45) | −23.0% | −25.8% |
| Mar 15 **intraday low** (42.77) | −25.9% | **−28.6%** |
| Mar 13 **intraday low** (41.92) | **−27.3%** | **−30.1%** |

The claimed **~−28%** matches only **close→intraday-low** framings. The defensible headline for "Mar 8–15": **−22.6% close-to-close**, or **−27.3% peak-close-to-trough-low** if you extend to the Mar 13 low. State the basis.

## Secondary — MOVE index

⚠️ **Do not cite the date.** `^MOVE` via Yahoo shows **198.71 as the Mar 16 open**, but the series carries the **sparse-index date-shift signature** (every Open == prior Close; Mar 15 O=H=L=C=169.65 — a carry-forward stub). This is the known `[[finding_yahoo_sparse_index_date_shift]]` failure mode. The **~198 magnitude corroborates**, but the **Mar 15 date does not** — the print lands Mar 16 in this feed and is likely shifted. **Needs a non-Yahoo source (ICE/BBG) before citing a date.** `[UNVERIFIED]` on date, `[UNVERIFIED]` on level pending a second source.

## Counter-Evidence

- **Against "credit didn't warn":** HY OAS at 397–422bps through early March was **not** a complacent level — it was already ~100bps above the 2021 lows, i.e. credit carried standing risk premium. The *absence of a March-specific move* is not the absence of a signal.
- **Against the Mar 24 peak:** the Mar 24 print (522) is only 2bps above Mar 15 (520), inside daily noise, and Mar 24 has a plausible separate driver (Deutsche Bank CDS stress). A reader could legitimately call this a twin-peaked episode rather than a single Mar-24 max.
- **Against reading Mar 8's +11 as anticipation:** it is one day, 11bps, and confounded by Silvergate. Not a signal.
- **Index-mechanical caveat:** HY OAS is an index of surviving constituents; month-end rebalance (Mar 31) can shift the level independent of repricing. The Mar 31 458 print straddles a rebalance.
- **What would disprove the lead/lag read:** intraday Mar 9 data showing HY OAS moving *before* the equity/deposit break, or CDX HY (more liquid, faster) leading cash OAS. **CDX HY was not checked — that is the strongest untested counter-path**, since synthetic credit typically moves first and cash-index OAS is a laggy measure by construction. A "credit lagged" verdict built only on cash OAS may be measuring the instrument, not the market.

## Source Quality Assessment

**High** for the HY/IG OAS tables: these are the index owner's own values (Ice Data Indices, LLC), recovered verbatim from FRED's own data-dump file, re-pulled and confirmed independently by DEWEY. The sub-agent additionally cross-checked seven archived FRED *series pages* (a separate endpoint, separate crawl dates) against the data file — all matched exactly.

**Medium** for KRE (Yahoo close/adjusted data is reliable but unaudited; a corporate-action adjustment would shift levels — ratios are robust).

**Low** for MOVE — see the flag above.

**Gap:** the Fed FSR May 2023 was fetched and parsed (213,910 chars) but contains **no usable March-2023 spread levels** — its corporate-bond section is written report-over-report ("spreads were moderately lower, on net, since November") and the March episode appears only via *bid-ask* liquidity commentary, not OAS levels. Its figure 1.11 sources the ICE H0A0 index but the values live in the chart, not the text. **The FSR is not a substitute source for this question** — worth recording, as it was source #2 on the hunt list.

## References

- ICE BofA US High Yield Index OAS (BAMLH0A0HYM2), Ice Data Indices LLC via FRED, full history file — https://web.archive.org/web/20231212182755id_/https://fred.stlouisfed.org/data/BAMLH0A0HYM2.txt (accessed 2026-07-16)
- ICE BofA US Corporate Index OAS (BAMLC0A0CM), same lineage — https://web.archive.org/web/20240623204207id_/https://fred.stlouisfed.org/data/BAMLC0A0CM.txt (accessed 2026-07-16)
- Federal Reserve, *Financial Stability Report*, May 2023 — https://www.federalreserve.gov/publications/files/financial-stability-report-20230508.pdf (accessed 2026-07-16; **no March OAS levels stated**)
- KRE / ^MOVE OHLC — Yahoo Finance via `yfinance`, accessed 2026-07-16

## Process Report

**Searches run:** FRED API/CSV/ALFRED/live-txt probes (5 variants × 7 series); one delegated web/archive hunt; Fed FSR PDF fetch + parse; yfinance pulls.
**What worked:** the Wayback `/data/<ID>.txt` path — full 27-year history at index-owner quality. The task's suggested `fredgraph.csv` workaround **failed** (also truncated) — reporting that is itself the answer to a sub-question asked.
**Data gaps:** CDX HY (the best counter-test, untested); intraday Mar 9–10 sequencing; MOVE date confirmation; GCF/DVP repo (see the standing `ofr_stfm.py` BACKLOG row).
**Source frustrations:** `archive.org/wayback/available` **false negatives** — it reported zero snapshots for a URL with five; only the CDX index API surfaced them. Nearly killed the winning path at step one. Gzip without `--compressed` masquerades as an empty/blocked page.
**Confidence:** High on HY/IG. Medium on KRE (basis-sensitive). Low on MOVE.
**If I had more time:** CDX HY 5yr for the lead/lag counter-test; a terminal for intraday.
