---
request_id: REQ-DEWEY-20260702-003
from: PROME (Will-directed batch 2026-07-02 — fleet-mined slate; WALTER logs + routes, see AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md)
to: DEWEY
created: 2026-07-02T04:00:00Z
state: NEW
flag_trigger: T3 (load-bearing-but-thin)
originating_evidence: "if dealer funding seizes first, the trigger never fires (dealers won't bid)" (PROME/cluster/2026-06-27_coverage_gap_analysis.md — the fleet's named #1 blind spot); funding-microstructure PRIMARY mandate scaffold staged (AGENTS/LIQUID/STATUS.md)
clusters: credit-recognition X1 / private-credit stress / funding plumbing
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (WALTER logs row at next boot, disposition QUEUED)
run_order: 3 of 13
deliver_by: ASAP — HY tagged 280-283 (6/26-29) then RECEDED to 275 [7/2], X1 not sustained; the CoreWeave single-name slide (7/4) makes the "stress real, index doesn't print" scenario live
---

# DEEP-RESEARCH PROMPT 07 — Funding-seizure pre-emption gate for the HY>280 X1 trigger

> **★ 7/4 REVISION (PROME):** the "5bp-from-280, about to fire" urgency has softened — HY tagged 280-283 (6/26-29) then RECEDED to 275 [7/2], X1 not sustained. But the CORE question is MORE live, not less: the 7/4 CoreWeave junk-bond slide (single-name AI-credit stress while the HY *index* recedes) is exactly the "stress is real but the index-level trigger never prints" scenario this prompt probes. Keep the four-episode calibration as written; ADD to the closing judgment a single-name/sector-dispersion angle: can a name- or sector-level funding-or-credit seizure (à la CoreWeave) pre-empt or bypass the HY>280 index print, and should the X1 conjunction include a dispersion / single-name gate alongside the funding-seizure gate?

**Decision question:** Is HY>280 X1 still a valid credit-recognition signal, or does the credit-bear entry need a calibrated funding-seizure (and/or single-name-dispersion) pre-emption gate — stress is real but the index never prints — before sizing?

**Materiality gate:**
- **(a) What a cheap verify can't answer:** the episode-level lead/lag calibration — which funding indicators broke before credit spreads, at what thresholds and lead times, with what false-positive rate. The in-repo Jan-26 SOFR research covers Sep-2019 mechanics + generic early-warning indicators only; no funding-vs-credit-spread lead/lag, no Mar-2020/UK-LDI/Mar-2023, no MMF/haircut/dealer-inventory calibration.
- **(b) Consequence:** defines tripwire rows (dealer inventory, haircuts, MMF flows) for LIQUID's Will-approved funding-plumbing PRIMARY mandate and redefines X1 so the bear can fire on funding seizure even if HY OAS never prints 280; re-routes credit-bear entry vehicle/timing.

## `/deep-research` prompt (paste-and-go)

> Across four stress episodes — Sep-2019 US repo spike, Mar-2020 dash-for-cash, Oct-2022 UK LDI/gilt crisis, Mar-2023 SVB/regional-bank run — which PUBLIC funding-microstructure indicators deteriorated BEFORE US credit spreads (HY OAS / IG OAS) repriced, and by how much? For each episode and each indicator family, establish: (1) the indicator's level/change at its break point, (2) lead time in days vs the credit-spread reprice, (3) whether it also fired in non-events (false-positive check, e.g. Sep-2024/Sep-2025/Dec-2025 quarter-end noise). IN-BOUNDS indicator families (public primaries only): NY Fed primary-dealer statistics (net positions and corporate-bond inventory, incl. failures-to-deliver), OFR Short-Term Funding Monitor (repo volumes, rates, haircut/margin data), SOFR distribution percentiles vs IORB, SEC N-MFP money-market-fund flows (prime-vs-govt shifts, weekly liquid assets), FICC sponsored-repo volumes, discount-window/SRF/central-bank-facility usage; for the UK leg, BoE gilt-market and LDI post-mortems as the cross-check on how fast collateral/margin spirals outrun spread markets. DELIVERABLE: a calibrated tripwire table (indicator, threshold, lead time, false-positive rate) usable as boot.py rows for LIQUID's funding-microstructure PRIMARY mandate, plus an explicit judgment: in a dealer-funding seizure, does HY OAS reliably print >280 late, never, or on time — i.e., does the X1 credit-recognition trigger need a funding-seizure pre-emption gate, and what should that gate's conjunction be? Close with current readings (as-of dates stamped) of each surviving tripwire from the primary sources. OUT-OF-BOUNDS: paid data (ICE sub-indices, Bloomberg), non-US credit spreads beyond the UK LDI cross-check, bank-specific fundamentals (REGINALD), BDC/private-credit fund mechanics (BROCK), re-litigating whether the credit bear thesis is right (only whether the trigger can print). TIMEFRAME: episode analysis 2019-2023 + false-positive windows 2024-2026; current readings as of latest available prints. NAMED ENTITIES/SERIES: NY Fed PD stats (e.g. PDPOSCSBND series), OFR STFM, SEC form N-MFP, FICC sponsored GC, BoE Financial Stability Reports/Bailey LDI testimony, Fed FEDS notes and BIS bulletins on the four episodes.

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260702-003; WALTER routes as a `research-output` signal (→ LIQUID action / PROME, NEXUS, REGINALD, HENRY info) and closes the ledger row.
