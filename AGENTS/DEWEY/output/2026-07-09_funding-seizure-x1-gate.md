# Funding-seizure pre-emption gate for the HY>280 X1 trigger
**Date:** 2026-07-09 | **Mode:** Thesis | **Confidence:** High (directional verdict, on 2 of 4 episodes) / Medium (generalization) / High (current readings — DEWEY primary)

> **Flag:** REQ-DEWEY-20260702-003 (Batch-2 prompt 07). **Freshness reframe:** the "5bp-from-280" urgency is fully gone — HY OAS **267bps [7/7]**, X1 **CLOSED both halves** (digest §6). But the core mechanics question is undiminished, and today's prompt-18 finding (CoreWeave = idiosyncratic single-name AI-credit stress while the index recedes) is the live instance of the exact "stress real, index never prints" scenario this gate is for.

## Key Finding
**YES — the HY>280 X1 credit-recognition trigger needs a funding-seizure pre-emption gate.** In both stress episodes that survived adversarial verification (Sep-2019 US repo spike, Oct-2022 UK LDI), stress ignited through *funding/collateral plumbing*, repriced in **days-to-intraday**, and the corporate credit index **lagged or never printed** (Sep-2019 produced *no* HY reprice at all). An index-level trigger is therefore a *lagging confirmation* of a funding seizure. The gate should be a **conjunction**: an acute row (SOFR/repo percentiles blowing out vs IORB) backed by slow reserve-scarcity leads (EFFR-IORB, above-IORB borrowing, reserve-demand-curve slope) — and, given CoreWeave, a **single-name/sector-dispersion leg** (a funding-driven dislocation can be ~half a price move while the blended index recedes). **Current state (DEWEY FRED pull): all tripwires calm — no seizure on 7/9.** Confidence is capped at Medium overall because **2 of 4 episodes (Mar-2020, Mar-2023) and the false-positive rate went unverified** — those are the credit/deposit-channel cases where "funding-first" is most likely to break.

## Evidence

### Episode calibration (verified)
**Sep-2019 US repo spike — funding-only, zero credit signal.** Reserve/collateral supply-demand mismatch ($78B UST settling 9/16 + Q3 tax date + reserves <$1.4tn), NOT a credit event. Terminal dislocation: **SOFR 2.43%→5.25% on 9/17, ~700bps intraday range, +315bps vs IORB, >300bps above target (~30× the prior week), EFFR broke its band to 2.3%** [PRIMARY: Fed FEDS 2021-028, OFR WP-23-04, BIS Q4-2019]. **HY OAS did not move.** Advance warning existed in plumbing: **EFFR-IORB began widening Mar-2018 (~18mo lead); banks borrowed above IORB from mid-2018 (~15mo); reserve-demand-curve slope negative by Jan-2019** [PRIMARY: Fed FEDS Notes 2025-01-31, 2024-07-11]. Mechanism: tri-party (gross) vs FICC (netted) balance-sheet math constrains dealer intermediation independent of credit fundamentals [PRIMARY: Fed FEDS 2021-028].

**Oct-2022 UK LDI/gilt — collateral doom-loop outran markets by days.** After the 9/23 mini-budget, **30yr gilt yields +>100bps in 4 days (~140bps/3 days)**, forcing BoE intervention within ~5 days (9/28). Chain ran funding-first: falling gilts → LDI margin calls → forced fire-sales into thin markets → further declines [PRIMARY: BoE WP "Anatomy of the 2022 gilt crisis," BIS WP 1233, IMF, Chicago Fed]. Quantifiably a *funding* event not a *credit* one: forced-selling gilt discount **~6.87% (diff-in-diff) at the 9/27 peak = ~half the total price decline, fully reversed by end-October** (the signature of a transient funding dislocation, not fundamental repricing); LDI held ~28% of the gilt market [PRIMARY: BIS WP 1233, Pinter/Siriwardane/Walker]. **This is the direct analog to the CoreWeave concern: a real funding-driven dislocation ~half the move while the credit-fundamental signal is essentially absent.**

### Current readings — DEWEY primary pass (fills the workflow's unmet leg 3)
All pulled live from FRED 7/9/2026 [PRIMARY: FRED]; the workflow returned *no* verified current readings, so this leg is entirely DEWEY:

| Tripwire | Current | As-of | Read |
|---|---|---|---|
| **SOFR − IORB** | 3.58 − 3.65 = **−7bps** | 7/8 | soft, *below* floor — zero pressure (Sep-2019 hit +315bps) |
| **SOFR 99th pctile − IORB** | 3.67 − 3.65 = **+2bps** | 7/8 | tail barely elevated; the tail prints stress FIRST |
| SOFR volume | $3,158B | 7/8 | robust, no volume collapse |
| EFFR − IORB | 3.62 − 3.65 = −3bps | 7/8 | soft |
| **ON RRP (RRPONTSYD)** | **$5.8B** | 7/9 | drained from ~$2.5T 2023 peak |
| Total reserves | $3,078B | May | still ample |

**DEWEY structural point the episode literature predates: the RRP buffer is gone.** In 2022-23 the ~$2.5T ON RRP was a shock absorber — pressure hit RRP before SOFR. At **$5.8B it's essentially drained**, so future funding pressure transmits to SOFR/repo *faster* than in the calibration episodes. **This raises the value of the SOFR-tail (99th-pctile-vs-IORB) row** as the acute tripwire — reserves are now the marginal front line.

## The gate design (deliverable)
A **conjunction**, so a genuine seizure fires before/instead of the index:
1. **Acute row (fires in the seizure):** SOFR 99th-pctile − IORB blows out (calm now +2bps; a sustained multi-day move to +25/+50bps+ is the acute print), with SOFR-IORB median > +10bps and/or SRF/discount-window usage spiking. *The RRP-drained regime means this fires faster than 2023.*
2. **Slow-lead backing (arms the watch):** EFFR-IORB widening, regular above-IORB bank borrowing, reserve-demand-curve slope turning negative — the reserve-scarcity complex that led Sep-2019 by 15-18mo. **Regime caveat:** these are QT-era scarcity gauges; their 2026 (non-QT/ample) applicability is a regime-conditional assumption, not tested here.
3. **Dispersion leg (the CoreWeave case):** share of HY issuers above an OAS threshold, or single-name/index basis — captures "stress real, index recedes." *Prompt-18 supplies the named basket (CRWV 9.25%-2030 / 9.00%-2031 + APLD 9.25%-2030) as the AI-credit dispersion probe.*

**Answer to the decision question:** in a dealer-funding seizure, HY OAS prints **late or never** → X1 as a *sole* index gate is insufficient; the bear can fire on the funding/dispersion conjunction even if HY OAS never prints 280. This validates LIQUID's funding-plumbing PRIMARY mandate and adds the dispersion row.

## Counter-Evidence
- **The verdict generalizes from only 2 of 4 episodes.** No verified claims for **Mar-2020 dash-for-cash** or **Mar-2023 SVB** — precisely the credit/deposit-channel cases. In Mar-2020 funding *and* credit broke near-simultaneously (dash-for-cash hit everything at once — shorter or no funding lead); in Mar-2023 the SVB deposit run showed up in discount-window/BTFP usage (~$150B+ window draw) and FHLB advances, and HY *did* widen modestly before the Fed capped it fast. So "funding leads, credit lags cleanly" is well-supported for **repo/collateral seizures** but **untested for deposit-run/dash-for-cash archetypes** — where an index gate might not lag as badly. *(These characterizations are general Fed-record knowledge, not verified in this run — flagged as the open gap, not a DEWEY claim.)*
- **No false-positive rate established.** Quarter-end SOFR/repo spikes (Sep-2024, Sep-2025, Dec-2025) are common and benign; zero surviving claims tested how often the acute tripwire fires *without* a stress event. **This is the single biggest missing input before any threshold is set** — the +25/+50bps figures above are illustrative, not calibrated.
- **UK LDI is a sovereign-gilt/LDI event, not a US corporate-credit seizure** — a strong speed/mechanism analog, but transfer to HY OAS is by analogy.
- **The current all-calm reading could itself be a false comfort** if the RRP-drained regime means the first signal is a sudden SOFR-tail jump with little warning (the slow-lead gauges may be muted in ample reserves).

## Source Quality Assessment
High on the two verified episodes (all Fed/OFR/BIS/BoE/IMF primaries) and on current readings (FRED primary, DEWEY-pulled). The gaps are real and material: half the requested episodes and the entire false-positive calibration are unmet. One refuted claim (a specific "tri-party ~3.06%, 30× prior week" framing, 0-3) does not undercut the confirmed magnitude figures (+315bps vs IORB, ~30× prior week) from the merged Sep-2019 finding — it was a number-nuance refutation, not a reversal.

## References
- Sep-2019: Fed FEDS 2021-028 `federalreserve.gov/econres/feds/files/2021028pap.pdf`; OFR WP-23-04 `financialresearch.gov/working-papers/files/OFRwp-23-04_...pdf`; Fed FEDS Notes 2025-01-31 (ample-reserves indicators) + 2024-07-11 (fed funds dynamics); BIS Q4-2019 `bis.org/publ/qtrpdf/r_qt1912v.htm`
- Oct-2022 UK LDI: BoE "Anatomy of the 2022 gilt market crisis" WP; BIS WP 1233 (Pinter/Siriwardane/Walker, Dec 2024); IMF SIP 2023-049; Chicago Fed Letter 480
- Current readings: FRED SOFR / IORB / SOFR99 / EFFR / RRPONTSYD / TOTRESNS, accessed 7/9/2026
- OFR Short-Term Funding Monitor (named tripwire source, live): `financialresearch.gov/short-term-funding-monitor/`

## Process Report
- **Searches run:** 1 `/deep-research` workflow (105 agents; 6 angles; verified claims survived for **only 2 of 4 episodes**) + DEWEY FRED primary pass (6 funding-microstructure series, current readings).
- **What worked:** the Fed/OFR/BIS/BoE post-mortem literature is rich and primary — the Sep-2019 and UK-LDI mechanics + lead times came back clean and unanimous. My FRED pass fully supplied the "current readings" deliverable the workflow missed, and surfaced the RRP-drained structural point the episode papers predate.
- **Data gaps:** (1) **Mar-2020 + Mar-2023 unverified** — the two credit/deposit-channel episodes, the likeliest place the funding-first verdict breaks; (2) **no false-positive rate** — quarter-end noise vs real seizure, the key threshold input; (3) NY Fed primary-dealer corporate-bond inventory / FTD series and N-MFP prime-vs-govt flows named in scope but not returned as current readings (NY Fed PD stats aren't on FRED — need the NY Fed markets API/OFR STFM directly).
- **Source frustrations:** OFR STFM + NY Fed PD-stats datasets exist as primaries but aren't FRED-pullable; a helper is warranted (BACKLOG). Two transient SSL timeouts on FRED mid-pull (retried clean).
- **Confidence:** High on the directional verdict for repo/collateral seizures + current readings; Medium on generalization (2 of 4 episodes); the gate thresholds are illustrative pending the false-positive calibration.
- **If I had more time/tools:** run a focused follow-up on Mar-2020 + Mar-2023 (the untested episodes) and the false-positive check against Sep-2024/25 + Dec-2025 quarter-ends — that closes the gate calibration. Pull NY Fed PD corporate-bond inventory + N-MFP prime-fund flows directly for the dealer-inventory + MMF tripwire rows.
- **Suggestions:** BACKLOG a `scripts/ofr_stfm.py` / NY-Fed-markets helper (repo volumes/rates/haircuts, PD positions) — these are the funding-microstructure primaries FRED doesn't carry and they'll recur on every LIQUID funding-plumbing run. A Mar-2020/Mar-2023 + false-positive follow-up is the natural prompt-07b.
