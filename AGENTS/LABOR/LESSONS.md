# LABOR — LESSONS

LABOR-specific mistake-patterns to avoid. Read at boot (B3); written at closeout (C5).
**Scope:** durable LABOR-domain learnings that are NOT transferable to other agents (those go to auto-memory). One lesson per entry. Newest at top.

---

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
