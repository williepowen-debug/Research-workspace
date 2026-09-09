# FFB-RESEARCH portfolio preparation

Status: PLANNED — Will requested inclusion in planned work on September 9, 2026. Owner: PROME for portfolio framing and coordination. Timing: undated, after urgent broker/owner follow-ups; revisit at the next portfolio-work session.

## Objective

Present FFB-RESEARCH as a distinct companion to PROME: a structured NFL/fantasy research pipeline that turns reporting into traceable decisions. PROME demonstrates cross-domain coordination; this project demonstrates evidence intake, reconciliation and a concrete decision workflow.

## Planned deliverables

1. **Portfolio introduction / README opening:** lead with the user problem, sample output and architecture. Preserve contributor startup instructions further down. Working description: “Designed and built an AI-assisted NFL research pipeline with source provenance, temporal validation, evidence reconciliation and automated quality checks.”
2. **One illustrated case study:** trace original reporting → observations → synthesis → priority/ledger disposition → matchup decision. Candidate: the September 9 NE/SEA run. Re-verify the selected evidence and distinguish the recorded pregame decision from any later outcome.
3. **Contribution statement:** document Will's design and research-method choices, AI implementation assistance, and the verification/review process. Confirm attribution from actual work history.
4. **Small outcome evaluation:** select a bounded question, a simple baseline and a metric before collecting results—such as forecast accuracy, missed actionable signals or research time. Separate structural validation from research effectiveness; report the sample size and limitations.

## Starting evidence

Repo: `/home/willi/FFB-RESEARCH`. Read-only inspection on September 9 at local revision `50e0bec`: 15 regression tests passed; repository validation passed for 523 records and 10 schemas; generated catalog was current. These checks do not establish predictive accuracy or independently verify every source claim.

Entry points: `README.md`, `INTELLIGENCE_PIPELINE.md`, `scripts/validate_intelligence.py`, `.github/workflows/validate.yml`, `intelligence/2026/runs/20260909T210706Z/handoff.md`, and `weekly/2026/week-01/usage-tracking.md` in that repo.

## Pickup / completion

First choose the intended portfolio audience and case-study format, then inspect current FFB repo state and its local instructions before implementation. The current task records planned work only; no FFB files were changed or portfolio material published. Complete when the introduction, case study and contribution statement are reviewable and the bounded evaluation has a documented result or an explicitly pending collection window. Do not describe a planned evaluation as delivered evidence.
