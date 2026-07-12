# WATT — SCRATCH (next-session pickup)

**2026-07-12 — SECOND SESSION (first real post-build session; domain sweep run).**

Both P3 and P4 gaps from birth are closed — all four core channels now carry WATT-owned, sourced-and-dated reads (see STATUS/THESIS/workbook). Headline find: a free EIA wholesale-price file (`eia.gov/electricity/wholesale`, no key, biweekly) gives a usable PJM price proxy and it caught a real **$574.04/MWh Orange-band spike on 7/1** that the postings-only P1 read had completely missed. Full writeup: `reports/2026-07-12_domain-sweep.md`.

**▶ PICK UP HERE (next session, in priority order):**
1. **Run `boot.py`** first — confirm power_watch + staleness + predictions-due all green. Resolve WATT-03 (due 8/2), WATT-04 (due 7/23), WATT-05 (due 7/20) when their dates pass.
2. **Instrument upgrade (proposed 7/12, not yet built)** — wire the EIA ICE wholesale-price file into `power_watch.py` as an automatic P1 LMP-proxy + P4 spark-spread leg. It's `openpyxl`-parseable, biweekly, free. This was a manual pull this session; automating it is the single highest-value next build (closes the founding P1/P4 honest-wall permanently, no PJM_API_KEY needed).
3. **Calibrate the P4 heat-rate assumption** — currently a flat 7.0 MMBtu/MWh guess. Pull actual PJM gas-fleet heat rates (EIA-923, `facility-fuel` or `electric-power-operational-data` routes) for a real number instead of an ASSUMPTION-tier constant.
4. **Reconcile the P3 32GW (PJM-own) vs 55GW (Wood Mackenzie/utility-self-reported) divergence** — a 23GW/70% gap nobody has explained yet. Route to REGINALD/HENRY if it looks like utility over-commitment relative to PJM's own planning number (credit/FCF-timing angle).
5. **PJM_API_KEY** — still open (Will-gated); wires the *official* granular LMP once registered (the EIA proxy is daily-aggregate/biweekly-lag, not real-time).
6. Check whether the 7/1 LMP-proxy spike gets independently corroborated by AEOLUS (C3 heat-dome detection for that date) — worth a quick cross-check next session, not urgent.

**Open dependencies (not WATT's to do):** Will → PJM_API_KEY registration (~5min); PROME → route the P3 32GW-vs-55GW divergence + P4/P1 NEXUS_BRIEF findings to BRENT/HENRY if not auto-consumed.
