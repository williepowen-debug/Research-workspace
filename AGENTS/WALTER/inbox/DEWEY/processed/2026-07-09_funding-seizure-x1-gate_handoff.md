# DEWEY → WALTER handoff — Funding-seizure X1 pre-emption gate

**State:** NEW | **Date:** 2026-07-09 | **From:** DEWEY | **For:** WALTER (route as `research-output`)
**Report:** `AGENTS/DEWEY/output/2026-07-09_funding-seizure-x1-gate.md`
**Originating flag:** REQ-DEWEY-20260702-003 (Batch-2 prompt 07; WALTER ledger `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` — close row, disposition RESOLVED-with-gaps, executor DEWEY)
**Mode:** Thesis | **Confidence:** High (directional verdict on 2/4 episodes + current readings) / Medium (generalization to all seizure types)

## Routing suggestion (LIST only — not executed; cross-agent inbox writes are Will-authorized per digest §standing discipline)
- **ACTION → LIQUID** (owns the funding-plumbing PRIMARY mandate — this defines its tripwire rows + the X1 redefinition).
- **INFO → PROME** (X1 conjunction / credit-bear entry gating), **NEXUS** (R3↔R4), **HENRY, REGINALD**.

## One-paragraph summary (for the signal wrapper)
**The HY>280 X1 credit-recognition trigger DOES need a funding-seizure pre-emption gate.** In both stress episodes that survived adversarial verification — Sep-2019 US repo spike and Oct-2022 UK LDI — stress ignited through funding/collateral plumbing, repriced in **days-to-intraday**, and the corporate credit index **lagged or never printed** (Sep-2019 SOFR 2.43→5.25%, +315bps vs IORB, and **HY OAS did not move at all**; Oct-2022 gilt fire-sale discount was ~half the price move and *fully reversed* by end-October = a funding dislocation, not a credit reprice). So an index-level trigger is a *lagging confirmation* of a seizure — the credit-bear can fire on the funding conjunction even if HY OAS never prints 280. **Recommended gate = conjunction of (i) an acute row: SOFR 99th-pctile vs IORB blowout; (ii) slow reserve-scarcity leads: EFFR-IORB, above-IORB bank borrowing, reserve-demand-curve slope (led Sep-2019 by 15-18mo); (iii) a single-name/sector-dispersion leg for the CoreWeave "stress real, index recedes" case.** DEWEY's live FRED pull shows **all tripwires calm on 7/9** (SOFR-IORB −7bps, 99th-pctile +2bps) — no seizure — but flags that the **ON RRP buffer is drained to $5.8B** (from ~$2.5T), so future pressure now transmits to SOFR/repo faster than in the 2023 episodes, raising the value of the SOFR-tail row.

## Load-bearing points for LIQUID (tripwire rows for the funding-plumbing mandate)
- **Acute row (fires in seizure):** SOFR 99th-pctile − IORB (now +2bps; watch a sustained multi-day move to +25/+50bps+). SOFR-IORB median (now −7bps). SRF/discount-window usage spike.
- **Slow-lead rows (arm the watch):** EFFR-IORB, regular above-IORB bank borrowing, reserve-demand-curve slope negative. **Regime caveat: these are QT-era scarcity gauges; 2026 ample-reserves applicability is untested.**
- **Dispersion row:** DEWEY supplies the named AI-credit basket from prompt 18 — **CRWV 9.25%-2030 + 9.00%-2031 + APLD 9.25%-2030**, widen while broad CCC flat.
- **Current-readings source (live, free):** OFR Short-Term Funding Monitor `financialresearch.gov/short-term-funding-monitor/` + FRED (SOFR/IORB/SOFR99/RRPONTSYD). NY Fed PD corporate-bond inventory + N-MFP prime-fund flows are NOT FRED-pullable (DEWEY BACKLOG'd an `ofr_stfm.py` helper).

## Open items (the honest gaps — candidates for a prompt-07b follow-up)
- **Mar-2020 dash-for-cash + Mar-2023 SVB UNVERIFIED** this run — the two credit/deposit-channel episodes, the likeliest place "funding-first" breaks (Mar-2020 funding+credit near-simultaneous; Mar-2023 deposit-run → discount-window/BTFP led, but HY *did* widen modestly before the Fed capped it). The verdict is robust for repo/collateral seizures, UNTESTED for deposit-run archetypes.
- **No false-positive rate** — quarter-end SOFR/repo spikes (Sep-2024/25, Dec-2025) fire the acute tripwire benignly; the threshold/persistence filter separating real seizure from calendar noise is the single biggest missing input. **The gate thresholds above are illustrative, not calibrated.**
- Recommend a focused **prompt-07b**: Mar-2020 + Mar-2023 lead/lag + the false-positive check → closes the gate calibration.
