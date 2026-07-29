## 2026-07-17 ~11:00 AM ET — To: PROME (from BRENT) — COT SESSION, PHASE 1 (pre-print)

**Signal:** Pre-print prep DONE. Grade is frozen + mechanized; the print lands ~3:30 PM ET (report-date 7/14). Four load-bearing pre-print findings below, then the grade template. Phase-2 (the actual grade) follows this memo after 3:30.
**Priority:** 🟠 (pre-print; the 🔴 is the grade itself, post-3:30)

---

### THE FROZEN GRADE (quoted back from `setups/2026-07-17_COT-grade-and-FAL02-prereg.md`, verified against the CFTC primary)

**Primary metric:** WoW change in MM GROSS SHORTS, `WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE` (CFTC disaggregated futures-only), off the **7/7 base = 129,072 short / 193,113 long**.
✅ **Baseline VERIFIED against the CFTC primary API today** (dataset 72hh-3qpy): the 7/7 row returns short **129,072** / long **193,113** — exact match to the pre-reg. No drift.

| Verdict | ΔShorts (7/7→7/14) | Short level | Re-entry read for the ~$80-82 arm |
|---|---|---|---|
| **(b) COILED** | **≥ −7,000** (flat/building) | ≥ ~122,000 | Fuel INTACT, unwind still AHEAD → re-entry conviction **HIGHEST** |
| **(a) SQUEEZE IGNITING** | **−25,000 < Δ < −7,000** | ~104,000–122,000 | Fuel BURNING NOW → re-entry **MODERATE** (dip may not come) |
| **(c) FUEL SPENT** | **≤ −25,000** | ≤ ~104,000 | Accelerant CONSUMED → re-entry **DOWNGRADED** absent a fresh kinetic leg |

**Mechanized:** built `scripts/cot_grade.py` — pulls the CFTC primary, self-checks the frozen anchor, refuses to grade unless report-date = 7/14 (exits 3 if stale — no grading last week's data), prints the verdict. Tested pre-print: correctly refuses (newest row still 7/7). At 3:30 I run it and transcribe.

---

### FOUR PRE-PRINT FINDINGS

**1. ⚠️ DENOMINATOR RULING (FALCON ask) — resolved from PortWatch's own 924-row history, not inherited.** Canonical surface written: `domain/HORMUZ_TRANSIT_BASELINE.md`.
- **88 (PortWatch) = CORRECT** — 50th percentile of the pre-crisis daily `n_total` distribution (2025-01→2026-02; mean 89.9, median 87). Keep it.
- **97 (Strait Monitor) = stale vintage** — it's the CY2024 mean; traffic drifted down ~5% into 2025. Reject for 2026 work.
- **~140 = REJECT, category error** — it is the **98th percentile of daily prints** (a peak day), NOT an average. Using it understates the transit ratio ~37% (10/88=11% vs 10/140=7%). **Provenance answered: a peak mis-cited as a baseline. Kill it fleet-wide.**
- **BONUS — the magnitude series FALCON thought didn't exist DOES:** the same PortWatch layer publishes **`capacity_tanker` (tanker DWT/day)**. Pre-crisis mean 2,330,676 DWT/day. The 7/9-12 window ran **2.0% / 2.4% / 7.2% / 2.5%** of that = **at/below the March crisis trough (1.7%)** — so the oil-relevant tonnage collapse in-window IS at crisis-extreme even though the all-vessel hull count (11%) is not. Cite tanker DWT and the "11% understates / collapse overstates" tension disappears.
- **⚠️ AND the ≤18/day fresh-leg bar is miscalibrated:** it fires on **86.6% of all crisis days** (Mar-Jul). March ran 30 consecutive sub-18 at a *lower* mean than the "sustained" 5-day 7/8-12 run I cited at re-arm. Near-zero discriminating power. Proposed replacement (FALCON owns the call): grade off tanker-DWT ≤5% of pre-crisis mean. **This does NOT retract the 7/16 re-arm** — that stood on ≥3 independent legs, transit being only one — but the transit leg was weaker than it read.

**2. ICE Brent COT leg (corroborator) — the +22K spring-fuel build STALLED.**
- **Report 7/7 IS published** [engine.online, pub 7/14]: MM net long ~55,000 lots, **−547 WoW** (8th straight week of net-long reduction). Gross-long −367; derived gross-short ΔS ≈ **+180** (≈flat). The **~+22,000 gross-short build into 6/30 did NOT continue** into 7/7. Corroborated directionally by Saxo ("Brent broadly unchanged; selling concentrated in WTI").
- **⚠️ Level unconfirmed** — engine.online printed no gross-short *level* this week; +180 is arithmetic inference. **Report 7/14 not yet published** (expected later today; re-check PM).
- **Two vintage traps caught & rejected:** a GoldFix "231,218 gross short / net 114,128" number is a **6/22 (mid-June) vintage** search-fused into "July"; an InvestMacro "net −24,649" figure is **NYMEX Brent Last Day**, not ICE Europe Brent — wrong contract. Neither enters the 7/7 row.

**3. ENERGY-HY OAS RE-DERIVED FRESH (was 8d stale) → hand to LIQUID.**
- The **June-30 vintage IS out.** Extracted from Fidelity 931730.PDF, ICE BofA HY Corporate Sectors table: **Energy HY OAS = 183 bps [CONF, as-of 6/30/2026]** — up ~+19bp from the stale 164 [5/31], but still the **tightest HY sector** and *below* broad HY OAS **271bps [FRED BAMLH0A0HYM2, 7/15]**.
- **Read:** credit has NOT repriced the Hormuz closure as solvency risk — the >400bp stress line is remote. This is the LAGGING credit tell, and it's benign — consistent with FALCON's "risk premium, not lost barrels." ⚠️ **Caveat: the 6/30 vintage PRE-DATES the 7/11-12 closure.** The July print (~mid-Aug) is the first post-closure energy-credit read. **→ LIQUID: watch it; 183→>250 would be the first crack.**

**4. OWN-RECORD FIX — the 7/13 settle mislabel (per FALCON's correction, independently re-pulled).**
- FALCON is right, and I verified it against Yahoo BZ=F daily OHLC: **zero Brent settles ever exceeded $85; high-water settle = $84.95 (7/15).** My 7/16 re-arm carried "**settles 7/13 $78.85**" — that was a **Mon 7/13 intraday SPOT quote [TradingEconomics, +3.74% on day]** that leaked into a settlement-series table from `demand_destruction/data/monday_2026-07-13.md`. **The 7/13 settle was $83.30.**
- **Corrected series: 7/13 $83.30 / 7/14 $84.73 / 7/15 $84.95 / 7/16 $84.23 / 7/17 $86.88 live intraday.**
- **Fixed in:** STATUS.md (×2), TRADE.md, NEXUS_BRIEF.md, SCRATCH.md, and a correction note appended to the delivered `outbox/2026-07-16_to-PROME_rearm-adjudication.md`.
- **The LEVEL-leg PASS is UNCHANGED** — every settle >>$75 by $7-10 either way; only the label was wrong. **FALCON's separately-registered ">$85 held for 3+ sessions" threshold remains UNFIRED** (distinct test; earliest possible fire Tue 7/21 even if today settles >$85). I did not carry ">$85 held" into the grade framing.

---

### CONTEXT CONSUMED FOR THE GRADE (not graded here, informs the integration)
- **China June crude imports −41.3% YoY (7.12 mb/d, lowest since Oct-2016)** [ZHAO/PROME 7/16] — the main **non-de-escalation** path to my ~$80-82 pullback zone. ZHAO caution endorsed: attribution splits war-supply + structural-EV + inventory, not cyclical demand-destruction.
- **Four "supply events" this week, ZERO confirmed lost barrels** [FALCON + WALTER SIG-012/013/018] — Iraq resumed same-day, Russian Novorossiysk loadings +68% MoM, Belma was an unladen shadow-tanker. The decoupling broke on **risk premium**, which is reversible in a way destroyed capacity is not.
- TTF gas €55.11/MWh (+31.5% MoM, breached HANS's €50 crisis line) [HANS/PROME 7/16] = cross-commodity confirmation of the closure.

**Next:** Phase-2 memo after 3:30 PM — the mechanical verdict with actual print values + what it does to the $80-82 re-entry band. Deploy/re-entry stays a proposal to Will, never action. Live regime: HOLD FLAT, PASS-ON-CHASE (OVX ~61, Brent $86.9 green).
