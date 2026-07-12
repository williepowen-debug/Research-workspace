# WATT — SCRATCH (next-session pickup)

**2026-07-12 — SECOND SESSION, TWO ROUNDS (first real post-build session; domain sweep + PROME round-2 build).**

Round 1: P3/P4 founding gaps closed, free EIA wholesale-price proxy discovered ($574.04/MWh Orange spike for delivery 7/2, traded 7/1 — vintage clarified rd-2), domain sweep run (`reports/2026-07-12_domain-sweep.md`). PROME verified and delivered all route-outs (commit 40357f1d).
Round 2: **LMP-proxy + spark spread WIRED into `power_watch.py` as leg 4** (fail-loud, vintage-stamped, REVIEW on ≥$500 latest print or negative spread; tested end-to-end rc-0 incl. fail-loud path). **VULCAN S1 capex baseline consumed** into P3 (KB-WATT-020; ~$710–725B FY26 4-name guide, +77% YoY → leans toward the higher 55GW figure; dollars≠MW caveat; VULCAN doing the MW conversion its side).

**▶ PICK UP HERE (next session, in priority order):**
1. **Run `boot.py`** first — leg 4 now prints the LMP-proxy + spark spread automatically. Resolve WATT-05 (due 7/20), WATT-04 (due 7/23), WATT-03 (due 8/2) as their dates pass.
2. **Watch P1 escalation:** demand hit **98.2% of 24h peak** (7/12 20Z data-hour, Orange ≥97% crossed) under an active Hot Weather Alert. If an EEA2+ posting landed overnight/since, WATT-02 resolves early — route 🔴 to HENRY/AEOLUS. Also check whether the biweekly EIA file updated (~7/21 expected) with new post-7/8 delivery prints.
3. **Calibrate the P4 heat-rate assumption** — flat 7.0 MMBtu/MWh ASSUMPTION → pull actual PJM gas-fleet heat rates (EIA-923, `facility-fuel` or `electric-power-operational-data` routes).
4. **VULCAN MW conversion** — when VULCAN lands its compute→MW number, reconcile it against the 32GW (PJM) / 55GW (WoodMac) pair and re-score P3. Don't duplicate the conversion.
5. **PJM_API_KEY** — still open (Will-gated); wires the *official* intra-day LMP once registered (the EIA proxy can miss intra-day spikes).
6. AEOLUS C3 cross-check on the 6/30–7/2 spike window — PROME delivered the flag rd-1; see if AEOLUS confirmed.

**Open dependencies (not WATT's to do):** Will → PJM_API_KEY registration (~5min); VULCAN → capex→MW conversion (its side, this round); REGINALD → 32-vs-55GW pickup (delivered 7/12).
