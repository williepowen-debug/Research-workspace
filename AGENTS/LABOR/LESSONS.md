# LABOR — LESSONS

LABOR-specific mistake-patterns to avoid. Read at boot (B3); written at closeout (C5).
**Scope:** durable LABOR-domain learnings that are NOT transferable to other agents (those go to auto-memory). One lesson per entry. Newest at top.

---

## L-06 — Ratio-gauge thresholds (U-3) can be silently defeated by the DENOMINATOR; playbook grids need a supply-artifact branch
**Pattern:** The Jul-2 NFP playbook grid conditioned every branch on (headline NFP × U-3-up-or-flat). The tape printed the un-written cell: NFP +57K (<100K) **with U-3 FALLING to 4.2%** — because the labor force shrank 720K (participation −0.3pp) and mechanically suppressed the rate. T-06 ("NFP <100K + U-3 jump") could not fire on a genuinely weak print; LAB-02 (U-3 ≥4.7%) died not because labor demand held but because the *gauge* was structurally suppressed. Same trap forward: LAB-12 (U-3 ≥5.0%) and T-03/T-04 are all denominated in a rate whose denominator is now the fastest-moving part.
**Fix:** (1) Every U-3-conditioned threshold gets graded **JOINTLY with LFPR** — a participation-driven U-3 move counts as NO-SIGNAL, not as strength/weakness. (2) Print-reaction grids must carry an explicit third-axis branch for the denominator artifact (here: "NFP <100K + U-3 ↓ + LFPR ↓ = supply-shrink; grade on claims/hires instead"). (3) The pre-registered cross-domain signature (U-3↓ + wages↑ + LFPR↓ = supply shock, from the Jun-16 ICE cross-domain table) is what made the print gradable same-day — keep pre-registering discriminating signatures BEFORE the release. Promoted to auto-memory `[[finding_ratio_gauge_denominator_branch]]`.
**First seen:** NFP June 2026 (Jul 2 print).

## L-05 — Cross-domain signals can be scored on the WRONG SIDE of the convergence matrix
**Pattern:** The convergence matrix carried ICE enforcement (5🔴🔴) and H-2A bottleneck (4🔴) as bearish-employment convergence — +9 points of a 57/85. But those are MARCO labor-*supply* signals, and a migration-driven supply cut keeps unemployment *low* / wages *up* — the **opposite** of LABOR's demand-weakness (rising-claims/U-3) thesis. The instinct to "re-verify the stale carries" would have *confirmed* them (ICE had actually strengthened — funding signed into law Jun 10) and left the 9 mis-signed points in place. The defect was sign, not staleness.
**Fix:** For every cross-domain vector, write down which way it moves LABOR's headline metric (claims/U-3). If it moves it the wrong way or sideways, it's CONTEXT, not convergence — pull it into a separate cross-domain table, keep only the same-direction slice (here: ICE worksite-disruption → on-site layoffs, scored 2). Watch supply-vs-demand inversions specifically (a supply shock and a demand shock move quantity the same way but slack/price the opposite way). LABOR domain explicitly EXCLUDES migration-driven displacement (= MARCO) — so importing ICE/H-2A at full bearish weight was also scope creep. Promoted to auto-memory `[[finding_convergence_sign_check]]` (transferable to any agent with a convergence matrix).
**First seen:** Jun 16 2026 (Orc-prompted thesis-honesty pass; matrix 57/85 → 48/80).

## L-04 — Structured ledgers (VX/KB/FLOW) drift months behind the narrative STATUS
**Pattern:** STATUS.md gets refreshed every session, but the C3 workbook sync keeps getting deferred — so on Jun 14 the VX claims rows were still dated **Mar 9** (213K initial / 1.868M CC with dead DHS-shutdown caveats), and FLOW still read "Claims 209K / NFP +50K (Dec)." A query against the ledger returns confidently-wrong stale values with **no staleness signal** — the row just shows an old "Last Updated" date a reader may not check. Orc's framing: "this is how a ledger gap silently distorts a trajectory read later."
**Fix:** (1) When deferring full C3, still refresh the **load-bearing rows** (claims/NFP/U-3) — they're cheap and most-queried. (2) Do **not** blanket-stamp a too-recent `[STALE date]` — the rows carry *their own* (often much older) dates; a generous stamp overstates freshness. (3) Treat a 2+-cycle C3 deferral as a real debt, not a footnote. Transferable to any agent with a STATUS+workbook split (CARL/REGINALD/BROCK/HENRY) — candidate for auto-memory promotion.
**First seen:** Jun 14 2026 (Orc-flagged; partial fix = 2 claims rows refreshed, rest still owed).

## L-03 — DOGE/government YoY comps are base-effect-poisoned
**Pattern:** Challenger YTD job-cuts showed -43% YoY (and DOGE-specific -94% YoY) in mid-2026 — which reads as "layoffs improving" but is an artifact of the inflated 2025 DOGE base (284,827 federal cuts in 2025 vs ~16K in 2026).
**Fix:** For any DOGE/federal-workforce YoY series, anchor to a pre-DOGE baseline (or use level + MoM), not the 2025-comp YoY. The comp laps a structural one-off. See auto-memory `[[feedback_yoy_baseeffect_use_multiyear_stack]]`.
**First seen:** Challenger May 2026 (Jun 5 print).

## L-02 — Track the *revised* NFP series, not just the first print
**Pattern:** The May NFP print (Jun 5) revised March/April UP by a net +93K (April 115K→179K). The original prints understated; the revision flipped the thesis read and pushed March across the Kill-A 200K line. Reasoning off first-print NFP would have kept the bearish "realization-weak" read alive longer than the data justified.
**Fix:** At every NFP, re-read the revised back-months, not only the headline. Exit/Kill rules (Kill A: NFP ≥200K ×3) must be evaluated on the revised series. The first print is the noisiest data point in the release.
**First seen:** NFP May 2026 (Jun 5 print).

## L-01 — Company-tier revenue ≠ industry employment
**Pattern:** LAB-01 ("Temp YoY <-6%") was FALSIFIED because the call conflated staffing-firm revenue weakness (KELYA/RHI down double digits) with BLS CES temp-help *employment* — which was actually expanding (+7.9K MoM Apr; ASA +4.9% YoY). Company-level reads lag and don't equal the industry-level series.
**Fix:** Pull the canonical industry series (BLS CES `TEMPHELPS`, ASA index) for any employment prediction — not the company proxy. Match the prediction's measure to its canonical data source. See auto-memory `[[feedback_prediction_canonical_measure]]`.
**First seen:** LAB-01 resolution (Jun 2 2026).
