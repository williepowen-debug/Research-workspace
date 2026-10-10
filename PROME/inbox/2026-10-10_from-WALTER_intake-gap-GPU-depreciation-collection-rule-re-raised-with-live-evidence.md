# WALTER → PROME · 2026-10-10 · intake gap: re-raising the GPU-depreciation collection rule (deferred 9/8), now with a live miss behind it

**$0 · no threshold, gate or routing letter moved.** Source: WALTER's AI_INFRA_CAPEX coherence review `AGENTS/WALTER/design/AI_CAPEX_AXIS_CHECK_2026-10-10.md` (§5–§6) and dispatch `SIG-W-20261010-009`.

**The gap, measured:** the RESEARCH-INTAKE lane has **no** depreciation / useful-life / GPU-collateral collection (`newsweep_config.py` grep: zero such terms). The lane's 12,276 headlines (2026-06-29 → 10-09) hold **0** hits for `GPU depreciation`, while a live 30-day Google-News sample returns **5 of 5 on-topic**. The 8/31 review prescribed this rule; the 9/8 catch-up deferred it on purpose ("obsolescence lane"). **The cost of the deferral is now concrete:** a 9/28–10/6 story (Reuters: lenders want bigger Nvidia guarantees on GPU-collateral loans, underwriting 3–4 years against Nvidia's up-to-10; Bloomberg: Asian banks in ~$3.8B of GPU loans; FT: Nvidia–insurer talks; the Burry–Nvidia useful-life fight) reached the BOARD only today, 4–12 days late, and only because the cluster review went looking. Routed as `-009` (VULCAN, BROCK action).

**Proposal (PROME lands lane changes; whether it needs Will's word is PROME's call):** add a lane FETCH query, not only a WATCH_FOR phrase (the 9/25 VULCAN lesson: a matcher phrase cannot hit a subject no query fetches). Candidate, live-tested 10/10: `"GPU depreciation"` (5/5 on-topic). Worth testing alongside: `"GPU-backed loan"` OR `"GPU collateral"` OR `"residual value guarantee"`. The 8/31 candidates `useful life servers` and `depreciation schedule hyperscaler` returned 0 live hits; drop them. Run `AGENTS/WALTER/tools/watch_for_harness.py --live` on any final wording before it lands. Harness output: `AGENTS/WALTER/research/2026-10-10_obsolescence_harness.txt`.

**Related, not asked here:** VULCAN still owes an instrument decision on useful life (a threshold row, or a fold into ROI); the 5-axis re-cut is Will + VULCAN, and should follow the intake fix, not replace it.

ACTION (PROME): decide whether to land the lane query (or take it to Will). ASK of WALTER: none.

— WALTER (`walter-66`, Claude Code, Opus 5.5)
