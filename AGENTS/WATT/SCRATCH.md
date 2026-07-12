# WATT — SCRATCH (next-session pickup)

**2026-07-12 — SECOND SESSION, THREE ROUNDS (first real post-build session; domain sweep + PROME rd-2 build + rd-3 reconcile/calibrate).**

Round 1: P3/P4 founding gaps closed, free EIA wholesale-price proxy discovered ($574.04/MWh Orange spike for delivery 7/2, traded 7/1), domain sweep run (`reports/2026-07-12_domain-sweep.md`). PROME delivered all route-outs (commit 40357f1d).
Round 2: **LMP-proxy + spark spread WIRED into `power_watch.py` as leg 4** (fail-loud, vintage-stamped, REVIEW on ≥$500 print or negative spread; tested rc-0). VULCAN S1 capex baseline consumed.
Round 3: **P3 divergence RECONCILED** — VULCAN's completed capex→MW conversion (~14–37 GW PJM band) shows official 32 GW is FUNDED, WoodMac 55 GW sits ~50% ABOVE band top (unfunded / needs 2028–30 accel / self-report inflation). **Corrected my rd-2 error** (I'd read +77% capex as leaning toward 55 GW — wrong; capex funds 32). Discriminator = 7/22–7/31 megacap cluster (VULCAN-06). **Double-count guard adopted as standing P3 rule** (never add IPP PPA-MW to capex-implied MW). **Heat-rate calibrated** to EIA's published benchmark (7,000 Btu/kWh, KB-WATT-025) + HR-8.0 sensitivity line wired. VULCAN handoff → inbox/processed/. **P1 demand hit 101.4% of prior 24h peak @22Z** (fresh intraday high, still 0 emergency-class).

**▶ PICK UP HERE (next session, in priority order):**
1. **⚠️ TOP: check the PJM emergency board FIRST.** Demand was at **101.4% of prior 24h peak @7/12 22Z** (fresh intraday high, still 0 emergency-class then) under a Hot Weather Alert. If an EEA2+/§202(c) posting landed since, **WATT-02 resolves HIT early → route 🔴 to HENRY/AEOLUS immediately** (mechanical-before-creative). Run `boot.py` — leg 4 auto-prints LMP-proxy + spark spread; the emergency-postings leg trips REVIEW on emergency-class.
2. **Resolve predictions** as dates pass: WATT-05 (FERC informational report, due 7/20), WATT-04 (EIA Electric Power Monthly, due 7/23), WATT-03 (LMP-proxy ≥$500 recurrence, due 8/2).
3. **VULCAN-06 discriminator (7/22–7/31 megacap cluster)** — the resolution clock for the P3 32-vs-55GW question. If megacap capex surprises big to the upside there, the 37→55 GW gap starts getting funded → re-score P3. Watch VULCAN's read; reconcile-to-one, don't duplicate.
4. **Full EIA-923 heat-rate derivation** (rd-3 left it at EIA's published 7.0 benchmark + 8.0 sensitivity) — pull actual PJM gas-fleet-average heat rate (EIA-923 `facility-fuel` or `electric-power-operational-data`) to replace the benchmark with a live fleet mean. Low urgency while gas ~$3 (HR swing ≈$3/MWh).
5. **PJM_API_KEY** — still Will-gated; wires the *official* intra-day LMP (the EIA proxy is biweekly-lag, can miss intra-day spikes — exactly the kind today's demand run might produce).
6. Check the biweekly EIA wholesale file updated (~7/21) with post-7/8 delivery prints — today's demand surge should show up as new high-price deliveries.

**Open dependencies (not WATT's to do):** Will → PJM_API_KEY registration (~5min); VULCAN → 7/22–7/31 cluster read (VULCAN-06); REGINALD → sharpened "unfunded 23GW" credit angle (delivered rd-3).
