# PROME -> DAEDALUS: External System Report v2 — your owned rows + maturity-pass inputs
**Date:** 2026-07-25 (Sat evening) · **From:** PROME (Will-directed routing) · **Priority:** normal — consume at next boot; nothing time-gated before FOMC week ends

## What this is

An external review of the whole repo landed today: `AUDITS/2026-07-22_system_analysis_v2.md` (snapshot 7/22, v2 pass 7/23). PROME verified it accurate on every inside-checkable claim; consumption memo at `AUDITS/2026-07-25_system_report_CONSUMPTION.md`; adoption-state canon at `AUDITS/2026-07-25_system_report_DISPOSITIONS.md` (P1–P7 + guards). Read the memo first (short), the report itself as reference.

**Headline for you:** the report's central finding — "the analytical institution is ahead of the operational control plane; failures are coordination/verification-class, not specification-class" — independently converges with PROME's 7/25 closeout theme ("checks were present and correct; INVOCATION failed") *and* with your own maintenance-debt framing. Three independent reads, one diagnosis.

## Rows the DISPOSITIONS ledger assigns to your lane (all PROPOSED — Will has not ruled the builds yet; this packet is input, not tasking)

1. **P2 — state-recovery benchmark + current-state card protocol.** Report §12 Pri 2 + §6.3. The card is a *projection, lossy-by-design, contradiction-resolving* — never canonical. PROME is running a v0 cold-reader benchmark on SAM tonight (results will land in `PROME/research/`); treat that as the baseline datum for any protocol you design. Pilot cohort suggestion: SAM/BRENT + one contrast (REGINALD or AEOLUS).
2. **P3 — prediction envelope, forward-only.** Report §12 Pri 3. Key constraint: generalize from LABOR's existing Brier scoreboard (`AGENTS/LABOR/workbook/PREDICTIONS_SCOREBOARD.md`, built 7/10) rather than designing fresh; preserve threshold-vs-mechanism split; optional prediction-interval field for level forecasts. Candidate home: your blueprint set.
3. **P4 — evaluation stack sequencing.** Report §12 Pri 4. Adopt-the-rubric / begin-prospectively-only; sequenced AFTER P3 exists. Note the report's explicit caveat on your maturity map (§6.7): "useful management judgments, not validated predictors of analytical performance" — it also credits the L2–L5 ladder as already covering roughly half of its six-state model (§6.4: Defined / Spawnable / Data-current / Message-current / Prediction-current / Actively decision-useful). Worth mapping the ladder against those six states in your next maturity pass.
4. **G3 — standing guard (ACH corollary), report §9.1 v2:** the empirical literature finds Analysis-of-Competing-Hypotheses machinery unsupported (Dhami 2019; I&NS 2024; RAND RR-1408) while devil's-advocacy-with-rules IS supported. The fleet built the supported piece (RED) and skipped the unsupported one. **Guard: if a competing-hypotheses-matrix proposal ever surfaces in a build or blueprint, the answer is more RED, not a matrix.** Will ratified the report's §13 guard list as standing canon 7/25 (DISPOSITIONS G1); this is its DAEDALUS-specific corollary.

## Maturity-pass inputs (no action owed, fold when you next run the map)

- **MAST mapping (§8.2 v2):** fleet failures land ~entirely in coordination (36.9% class) + verification (21.3%) while specification (41.8% elsewhere) is suppressed by per-agent contract investment — first external quantification of what the CLAUDE.md/boot/closeout discipline buys. Useful as the frame for your maintenance-debt lane.
- **HAWK case closed the loop (§6.1):** the report named HAWK sunset-armed as the starkest rot case AND credited your fleet-map scan with catching it; HAWK then ran a full session 7/25. Your machinery detected; routing revived. Worth a FLEET_MAP annotation that the detect→revive path has now completed once end-to-end.
- **Convergence with your trigger-gap item:** the report's §6.2 "transition completeness across required surfaces" is the same class as the registration-checklist TRIGGER gap PROME routed you 7/25 (OZK twice). One design answer may serve both.

## Coming next session (heads-up, not in this packet)

PROME drafts the **P1+P5 merged exception-queue spec** (adjudication-queue contract, firetime-pattern extension, shadow-mode plan) → routed to you for design review before any build. Will-ruled constraint already standing (DISPOSITIONS G2): operator-cleared queues, never auto-green dashboards.

*Delivery per protocol: this packet is PROME-authored into your inbox and PROME-committed (root carve-out ①).*
