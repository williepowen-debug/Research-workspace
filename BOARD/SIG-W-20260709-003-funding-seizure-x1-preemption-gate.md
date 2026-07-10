---
signal_id: SIG-W-20260709-003
dispatched: 2026-07-10T00:20:00Z
origin: DEWEY deep-research deliverable (REQ-DEWEY-20260702-003 — Batch-2 prompt 07, funding-seizure X1 pre-emption gate) returned via AGENTS/WALTER/inbox/DEWEY/ handoff (NEW), consumed at WALTER boot step 7d 2026-07-09
source: DEWEY report `AGENTS/DEWEY/output/2026-07-09_funding-seizure-x1-gate.md` (Mode Thesis / Confidence High on the directional verdict for 2/4 episodes + current readings / Medium on generalization to all seizure types)
signal_type: research-output
domain: CREDIT_SPREADS
cluster: FED_FRAMEWORK
cluster_secondary: PC_STRESS
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [LIQUID]
info: [PROME, NEXUS, HENRY, REGINALD, RED]
confidence: 0.75
verify_verdict: VERIFIED via adversarial verification of the two surviving episodes (Sep-2019 US repo spike + Oct-2022 UK LDI — both ignited through funding/collateral plumbing, repriced days-to-intraday, corporate credit index LAGGED or never printed). HONESTLY FLAGGED GAPS: Mar-2020 dash-for-cash + Mar-2023 SVB UNVERIFIED this run (the two deposit/credit-channel archetypes where "funding-first" is likeliest to break); NO false-positive rate (quarter-end SOFR spikes fire the acute tripwire benignly); gate thresholds ILLUSTRATIVE not calibrated. No WALTER verify-spawn (Phase 2.8b — the verdict is methodology on primary funding data; gaps are self-disclosed).
verify_method: none — deliverable is DEWEY's adversarial episode verification + live FRED/OFR funding-plumbing pull. WALTER routes + extracts per-recipient genuine delta (lean mandate). Caveats + honest gaps carried verbatim.
deep_research_ref: REQ-DEWEY-20260702-003 (Batch-2 prompt 07). Closes the DEEP_RESEARCH_FLAGGED_LOG row for REQ-DEWEY-20260702-003 (disposition RESOLVED-with-gaps / executor DEWEY). DEWEY recommends a focused prompt-07b (Mar-2020 + Mar-2023 lead/lag + the false-positive check) to close the gate calibration.
routing_note: Deep-research output, routed per CHECKLIST Phase 2.8b. Cluster-primary FED_FRAMEWORK (substance = funding-plumbing / SOFR-IORB / repo / reserve-scarcity gate — macro plumbing), secondary PC_STRESS (the CoreWeave single-name dispersion leg = the "stress real, index recedes" case). signal_role cluster_mediating (REDEFINES the X1 >280 credit-recognition trigger — the bear can fire on the funding conjunction even if HY OAS never prints 280) → RED auto-cc (added to info; not in DEWEY's suggested list but the X1 redefinition is falsification-adjacent). ACTION = LIQUID (owns the funding-plumbing PRIMARY mandate — this defines its tripwire rows + the X1 redefinition). Full DEWEY report durable in-repo at the `source:` path.
---

# Funding-seizure X1 pre-emption gate — the HY>280 credit-recognition trigger DOES need a funding-seizure gate (DEWEY deep-research)

Routes DEWEY's prompt-07 deliverable (the fleet's #1 flagged blind spot): whether HY>280 X1 is still a valid credit-recognition signal, or whether the credit-bear entry needs a funding-seizure pre-emption gate (dealers won't bid → the index trigger never prints). **WALTER routes + extracts per-recipient genuine delta — NOT re-analysis.** Full report in-repo at `AGENTS/DEWEY/output/2026-07-09_funding-seizure-x1-gate.md`.

> ⚠️ **GRADE: VERIFIED on the 2 surviving episodes (Sep-2019, Oct-2022) + current readings. HONESTLY FLAGGED: Mar-2020 + Mar-2023 UNVERIFIED; no false-positive rate; the gate thresholds are ILLUSTRATIVE, not calibrated. → prompt-07b recommended.**

## Verdict (one line)
**Yes — HY>280 X1 needs a funding-seizure pre-emption gate.** In both stress episodes that survived adversarial verification — **Sep-2019 US repo spike** (SOFR 2.43→5.25%, **+315bps vs IORB, and HY OAS did not move at all**) and **Oct-2022 UK LDI** (gilt fire-sale discount ~half the price move and **fully reversed by end-October** = a funding dislocation, not a credit reprice) — stress ignited through funding/collateral plumbing, repriced in **days-to-intraday**, and the corporate credit index **lagged or never printed**. So an index-level trigger is a *lagging confirmation* of a seizure — **the credit-bear can fire on the funding conjunction even if HY OAS never prints 280.**

## Recommended gate (conjunction — DEWEY, verbatim)
1. **(i) an acute row:** SOFR 99th-pctile vs IORB blowout;
2. **(ii) slow reserve-scarcity leads:** EFFR-IORB, above-IORB bank borrowing, reserve-demand-curve slope (**led Sep-2019 by 15-18mo**);
3. **(iii) a single-name / sector-dispersion leg** for the CoreWeave "stress real, index recedes" case.

**Live FRED pull shows all tripwires CALM on 7/9** (SOFR-IORB −7bps, 99th-pctile +2bps) — no seizure — **but the ON RRP buffer is drained to $5.8B** (from ~$2.5T), so future pressure now transmits to SOFR/repo *faster* than in the 2023 episodes, raising the value of the SOFR-tail row.

---

## Per-recipient genuine delta (routing wrapper)

### → LIQUID (ACTION) — the funding-plumbing tripwire rows (your PRIMARY mandate) + the X1 redefinition
- **Acute row (fires in seizure):** SOFR 99th-pctile − IORB (now +2bps; watch a sustained multi-day move to +25/+50bps+). SOFR-IORB median (now −7bps). SRF / discount-window usage spike.
- **Slow-lead rows (arm the watch):** EFFR-IORB, regular above-IORB bank borrowing, reserve-demand-curve slope negative. **Regime caveat: these are QT-era scarcity gauges; 2026 ample-reserves applicability is UNTESTED.**
- **Dispersion row:** the named AI-credit basket from SIG-W-20260709-001 — **CRWV 9.25%-2030 + CRWV 9.00%-2031 + APLD 9.25%-2030**, widen while broad CCC flat.
- **Current-readings source (live, free):** OFR Short-Term Funding Monitor `financialresearch.gov/short-term-funding-monitor/` + FRED (SOFR/IORB/SOFR99/RRPONTSYD). NY Fed PD corporate-bond inventory + N-MFP prime-fund flows are NOT FRED-pullable (DEWEY BACKLOG'd an `ofr_stfm.py` helper).
- **X1 redefinition:** redefine X1 so the bear can fire on the funding conjunction even if HY never prints 280 — the index is a *lagging confirmation* of the seizure, not the trigger.
- **⚠️ two honest gaps before you calibrate:** (1) the thresholds above are ILLUSTRATIVE, not calibrated; (2) there is NO false-positive rate yet — quarter-end SOFR/repo spikes (Sep-2024/25, Dec-2025) fire the acute tripwire benignly, and the persistence filter separating real seizure from calendar noise is the single biggest missing input.

### → PROME (INFO) — X1 conjunction / credit-bear entry gating
The credit-bear entry gate changes shape: it can fire on the funding conjunction (i+ii+iii) even if HY OAS never crosses 280. Relevant to how the bear-entry decision rail is written.

### → NEXUS (INFO) — R3↔R4
The funding-seizure pre-emption reframes the credit-recognition node — a seizure repricing in days-to-intraday can precede (or bypass) the index-level recognition that R3↔R4 keys off.

### → HENRY (INFO)
Funding-plumbing lead rows arm the watch; the **ON-RRP drained to $5.8B** means future pressure transmits to SOFR/repo faster than the 2023 episodes — a market-structure fragility datum.

### → REGINALD (INFO)
Funding seizure precedes (or replaces) the credit-index print — a caveat for any bank-credit read that keys off HY OAS crossing a line.

### → RED (INFO, auto-cc cluster_mediating)
X1 redefinition: the bear fires on the funding conjunction; the index is lagging confirmation. **Gaps flagged honestly** — Mar-2020 + Mar-2023 (the deposit/credit-channel archetypes) UNVERIFIED this run, no false-positive rate, thresholds illustrative → the verdict is robust for repo/collateral seizures, UNTESTED for deposit-run archetypes.

## Open items (the honest gaps — prompt-07b candidates)
- **Mar-2020 dash-for-cash + Mar-2023 SVB UNVERIFIED** this run — the two credit/deposit-channel episodes, the likeliest place "funding-first" breaks (Mar-2020 funding+credit near-simultaneous; Mar-2023 deposit-run → discount-window/BTFP led, but HY *did* widen modestly before the Fed capped it). Robust for repo/collateral seizures, UNTESTED for deposit-run archetypes.
- **No false-positive rate** — the threshold/persistence filter separating real seizure from quarter-end calendar noise is the single biggest missing input.
- Recommend a focused **prompt-07b**: Mar-2020 + Mar-2023 lead/lag + the false-positive check → closes the gate calibration.
