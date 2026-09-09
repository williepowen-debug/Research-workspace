## NEXT RUN HINTS

*FASTOW writes at end-of-run; BRENT may pre-edit between runs. What the next-spawn-of-FASTOW should know that isn't obvious from the read-set.*

- **(Run 3) META-REVIEW disposition:** Run 2 produced 9 propose-only meta-review findings (PENDING § Run 2 META-REVIEW). Read PENDING first — if BRENT has marked items ✅ RESOLVED with spec edits applied, those mechanics are now in FASTOW.md; re-read spec. If still pending, behave per current spec but expect re-discovery of the same patterns.
- **OPEC+ Jun 7 outcome ingestion (carryover from Run 1 hints).** By Run 3 the Vienna outcome will be known. If BRENT renamed the row to `— FIRED [outcome]`, start 1-week retention clock from Jun 7; eligible to prune Jun 14+. Active OPEC+ row currently still `— TODAY` with PENDING outcome.
- **OPEC MOMR Jun 11 — verify post-release.** Run 2 revised to Jun 11 10:00 source-locked. If Run 3 fires post-Jun-11, the event should be `— FIRED` (or the rename did happen and 1-week retention starts Jun 11+).
- **Pre-fire monitor rolling watch.** Next cadence-derived rows entering 7-day window after Run 2:
  - EIA STEO (July) Jul 8 — fires for pre-fire check at Jul 1 (current text: "Customary Tue early-month; verify against EIA schedule (Tue Jul 7 also possible)").
  - OPEC MOMR (July) Jul 11 — fires Jul 4 (current text: "Best-estimate date").
  - US CPI (June print) Jul 15 — fires Jul 8 (current text: "Verify against BLS schedule").
  All three are excellent monitor-validation candidates.
- **Modeled-date check carry-forward:**
  - SPR 350M floor — Jun 10 EIA WPSR (Wed) resolves the floor-touch directionally. If throttled, row resolves (rename to FIRED-throttle); if drain-through, the date model is moot and row should be removed (catalyst was the EIA print itself, the modeled floor is just the level).
  - Cushing 20M floor — currently 2026-07-01. Each EIA Wed print updates the projection. If Jun 10 EIA shows Cushing draw re-accelerating, push date earlier; if continued deceleration, push later.
- **STATUS↔TSV parity ESCALATION (Finding #1) is a recurring item until BRENT resolves the TRUTH MODEL ambiguity.** Next run will re-flag if untouched. Suggest BRENT pin the resolution in CALIBRATION or FASTOW.md before Run 3 to clear noise.
- **Monthly baseline-audit trigger next fires Jul 1+.** Read CALIBRATION first (light-convention for weekly classes is in place; expect ~5-7 monthly additions instead of ~28).
- **Sub-agent propagation gap reminder** (per auto-memory `[[feedback_subagent_propagation_gap]]`): BRENT must read this FASTOW_MEMORY at each BRENT closeout to catch FASTOW's PENDING delta. The PENDING table won't auto-propagate to CATALYSTS.tsv — BRENT applies.
- **Cost budget Run 3:** ~3-5 min if monthly-trigger doesn't fire. If BRENT applies any of the 9 META-REVIEW findings as spec edits before Run 3, budget may shift (e.g., schema migration to add cadence-derived tier would require a one-time pass to retag rows).
