# DEEP-RESEARCH PROMPT 07b — funding-seizure gate CALIBRATION (episodes + false-positive rate)
**From:** PROME (Will-approved 7/9) · **Queue position:** after 08 and 09, before 11 · **Parent:** prompt 07 (`AGENTS/DEWEY/output/2026-07-09_funding-seizure-x1-gate.md` — read its §gaps first; this prompt closes them, do not re-litigate the delivered verdict)
**Deliver-by:** ~7/16 (before TIC week ends; the gate should be calibrated before any HY re-approach to 280 per KB-LIQ-071's path)

## The two gaps this closes
Prompt 07 established (High conf) that repo/collateral seizures are funding-first with credit lagging (Sep-2019, Oct-2022 LDI) → X1 needs a funding-seizure pre-emption gate. Left open:

**(1) The credit/deposit-channel episodes — does the gate generalize?** Verify **Mar-2020 (COVID dash-for-cash)** and **Mar-2023 (SVB/regional deposit run)** against the gate's conjunction structure (acute SOFR-99th-pctile-vs-IORB leg + slow reserve-scarcity leads + single-name/dispersion leg): did funding microstructure lead credit indices in those episodes too, and by how much? Or do deposit-run episodes fire the credit leg FIRST (which would mean the gate protects only the repo channel — a scoped, not general, pre-emption)? Sequence each with dates + bps from primaries (FRED/OFR/NY-Fed/BIS post-mortems).

**(2) The false-positive rate — the missing threshold input.** Since 2015: how often does the acute leg (SOFR ≥99th pctile vs IORB, or your report's exact spec) fire on **quarter-end/tax-date/settlement noise** without any real seizure following? Establish: raw FP count, whether the conjunction with the slow leads + single-name leg suppresses them (that's the design claim — test it), and the implied threshold adjustment if it doesn't. This sets whether the gate can be mechanical or needs a human-confirm step.

## Run notes (new protocol applies)
- **Carve-outs (owned by your scripts, concurrent with the fan-out):** all current readings (SOFR/IORB/EFFR/RRP — FRED), the 2015-present SOFR-vs-IORB percentile series construction (FRED), any OFR STFM pulls (2nd recurrence → build `ofr_stfm.py` per the WAIT→BUILD gate if you need it here). The workflow owns: episode narratives, post-mortem literature, adversarial verify of the sequencing claims.
- Completeness-critic pass: 2 episodes + 1 FP-study = 3 required sub-answers; flag explicitly if any is unreachable — do not silently synthesize around it.
- **On-return chain:** verdict + calibration table → LIQUID (gate co-owner w/ its KILL_MEMO/X1 machinery) + HENRY (funding-plumbing mandate) via WALTER's routing; PROME reads for GATES.tsv implications (a calibrated gate may become a registered action-gate row).
