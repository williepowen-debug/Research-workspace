# WATT — STATUS

**Last Updated:** 2026-07-12 (first real session — DAEDALUS-build follow-through: P3/P4 gaps closed, LMP-proxy discovered, domain sweep run) · **Status:** 🟠 monitoring, elevated (structural capacity 🔴; P1 shows a confirmed-but-retreated Orange-band price spike; P3/P4 now WATT-owned)
**Class:** Market-agent (grid stress → power price → power cost) · **Spawnable by:** PROME or Will · **Maturity:** L2 (all 4 core channels now carry WATT-pulled live reads; DAEDALUS FLEET_MAP)

> **Second session, 2026-07-12.** All P1–P4 channels now carry a WATT-owned, sourced-and-dated live read — the #1 guard's founding gap is closed. Headline finding: a free, no-key EIA source (`eia.gov/electricity/wholesale`, biweekly ICE OTC data) gives a usable PJM wholesale-price proxy — and it shows a **$574.04/MWh Orange-band spike on 2026-07-01** that the postings-only P1 read never caught. Full session detail: `reports/2026-07-12_domain-sweep.md`.

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **P1** | Stress → price | **3 🟠** | elevated, evidence building (confirmed spike, now retreated) | shares heat-dome antecedent w/ P4 | PJM demand 116,909 MW = **93.6%** of 24h peak (124,911 MW @7-11 22Z); 2 postings (1 Hot Weather Alert #105381 7/11, 1 routine local warning #105380 7/9), 0 emergency-class [power_watch, 7/12 19Z]. **LMP-proxy** (EIA ICE wholesale, PJM WH RT Peak wtd-avg): **$574.04/MWh on 7/1** (Orange, ≥$500) — 3-day run 6/29 $134→6/30 $361→7/1 $574→7/2 $366→7/3 $79, now back to $72.38 (7/7, latest available, biweekly lag) [eia.gov/electricity/wholesale] | EEA2+ posting OR RT LMP >$1,000 sustained 2+ intervals → 5 |
| **P2** | Structural capacity cost | **4 🔴** | confirmed short | independent (auction structure) | 26/27 BRA at **$329.17 cap**; 27/28 at **$333.44 cap**, **6,623 MW short** of reliability req (uncapped sim ~$530) [PJM BRA] | 28/29 BRA (~Dec-26) clears at cap again → 5 |
| **P3** | Data-center demand leg | **3 🟠** | confirmed via first pull — matches inherited estimate, no escalation yet | couples to HEN-36 AI-capex | PJM's own 20-yr forecast [PJM Inside Lines, pub 2026-01-14]: summer peak 2027 160,451 MW → 2046 >253,000 MW (3.6%/yr next 10yr); current PJM capacity ~182,000 MW. DC attribution [PJM via DCD, pub 2025-08-12]: **32 GW total peak-load growth 2024–2030, 30 GW (94%) from data centers**. Cross-check (higher, utility-self-reported): **Wood Mackenzie [via White & Case, pub 2026-03-11]: 55 GW by 2030, 100 GW by 2037** — a 23 GW / 70% gap above PJM's own official number, unreconciled (flagged below). IPP guidance (Q1-2026, reported May 2026), all reaffirmed/strong, none cut: VST record Q1 EBITDA $1,494M, FY26 guide $6.8–7.6B held (+ 3,800MW AWS nuclear PPA, 2,609MW Meta PPA, both excluded from guidance = unpriced upside); CEG FY26 EPS guide $11–12 held; NRG FY26 EBITDA guide $5.33–5.83B; TLN FY26 EBITDA $1,750–2,050M held (+1,920MW Amazon PPA @ Susquehanna) [SEC 8-Ks / investor releases, May 2026] | queue > 2× peak load OR IPP load-growth guide **raised** (not just reaffirmed) → 4 |
| **P4** | Gas → power coupling | **2 🟡** | first live read — spread wide/healthy, NO compression | shares heat-dome antecedent w/ P1 | Spark spread (Power − 7.0 MMBtu/MWh × Henry Hub; **heat-rate = ASSUMPTION-tier, not yet PJM-fleet-calibrated**): baseline 7/7 **+$49.53/MWh** (Power $72.38 vs HH $3.265); spike-day 7/1 **+$551.50/MWh** (Power $574.04 vs HH $3.220) [EIA wholesale + yfinance NG=F, 2026-07-12 pull]. Heat-stress regime **widens** the spread (gas is marginal price-setter, captures full scarcity rent) — it does not compress it; compression risk is a different (oversupply/high-renewable-curtailment) regime | spread compresses 50% or goes negative, sustained 3+ sessions → 3 |

**Composite: 12/20** *(P1 3 + P2 4 + P3 3 + P4 2, up from 10/20). P2 still carries the thesis; P1 upgraded on confirmed (if retreated) price evidence; P3/P4 de-gapped — no longer provisional.*

**Independence note:** P1 and P4 share a heat-dome antecedent (a hot spell drives both demand-spike and gas-burn) — count the shared root once in any composite-stress call. P2 (auction structure) and P3 (buildout) are the two independent structural roots.

---

## LIVE CHANNEL READS (sourced + dated)

- **P1 — Stress → price** [power_watch.py, 2026-07-12 19Z]: PJM demand **116,909 MW = 93.6%** of the 24h peak (124,911 MW @7-11 22Z, up from 88.9% on 7/11). Emergency board: **2 postings** — Hot Weather Alert (PJM-RTO #105381, 7/11 08:03 EPT) + Post Contingency Local Load Relief Warning (DOM #105380, 7/9 12:40 EPT), **0 emergency-class**. Retail backdrop [EIA, 2026-04, ~2mo lag, unchanged]: industrial **8.66¢/kWh**, residential **18.83¢/kWh**. **Official PJM LMP still NOT wired** (needs `PJM_API_KEY`, Will-gated) — **but a free proxy now exists**: EIA's public ICE-sourced wholesale price file (`eia.gov/electricity/wholesale`, biweekly, `PJM WH Real Time Peak` hub) shows a real **$574.04/MWh spike on 7/1** (Orange band), retreating to $72.38 by 7/7 (latest available). This is the session's headline instrument-layer finding — see LESSONS L-04.
- **P2 — Structural capacity cost** [PJM BRA]: unchanged, the loud, high-conviction leg. 2026/27 base residual auction cleared at the **$329.17/MW-day cap**; 2027/28 at the **$333.44 cap AGAIN** (uncapped simulation ~$530), and 27/28 cleared **6,623 MW short** of the reliability requirement — driver is data-center load. Structural pass-through to retail/industrial bills is in train (ComEd/BGE/Dominion territory).
- **P3 — Data-center demand leg** ✅ GAP CLOSED (first WATT pull, 2026-07-12): PJM's own 20-yr forecast confirms structural growth (32 GW total / 30 GW data-center-driven peak-load growth by 2030, per PJM's own numbers); WoodMac's utility-self-reported 55 GW/2030 figure runs materially hotter — unreconciled divergence, flagged as a FURTHER THREAD. All 4 IPP names (VST/CEG/NRG/TLN) reaffirmed or beat FY26 guidance in Q1-2026 reporting, with new hyperscaler PPAs (VST: 3,800MW AWS + 2,609MW Meta; TLN: 1,920MW Amazon) sitting **outside** guidance = unpriced upside. Full detail + citations in convergence matrix row above and `reports/2026-07-12_domain-sweep.md`.
- **P4 — Gas → power coupling** ✅ GAP CLOSED (first WATT pull, 2026-07-12): spark spread computed from the new EIA wholesale proxy × Henry Hub (yfinance NG=F). Baseline (7/7) +$49.53/MWh; spike-day (7/1) +$551.50/MWh — **wide and healthy both days, no compression signal**. Key mechanism refinement: the heat-stress regime that drives P1 **widens** the spread (gas captures scarcity rent as marginal unit) rather than compressing it — compression is a distinct (oversupply/curtailment) regime the thesis hasn't tested yet. Heat-rate assumption (7.0 MMBtu/MWh) is ASSUMPTION-tier, not yet calibrated to the actual PJM gas fleet — flagged as a FURTHER THREAD.

**Inherited event context (from HENRY provisional, 7/3–7/10):** PJM **EEA2 on 7/3** (KB-AEO-018) — the one realized emergency event; set the **DOE §202(c) precedent** (PJM can curtail ≥50 MW data centers). The new LMP-proxy shows the price spike (6/30–7/2, peak $574 on 7/1) essentially bracketing the EEA2 declaration — first quantitative confirmation that the posting-based read and the price-based read move together, as expected. The structural tape (P2) is what makes this a thesis rather than a one-off.

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| P1 | EEA2+ posting OR RT LMP >$1,000 sustained 2+ intervals | LMP-proxy peaked $574.04 (Orange, 7/1) then retreated to $72.38 (7/7); demand 93.6% peak [7/12], 0 emergency-class posting now | NOT-FIRED (1 prior EEA2: 7/3; 1 confirmed Orange-band price print: 7/1 — below the $1,000 Red bar, single-day not sustained) |
| P2 | BRA clears at cap AND short of reliability req | 26/27 + 27/28 BOTH at cap; 27/28 short | **FIRED** (structural, 2 consecutive) |
| P3 | interconnection queue > 2× system peak load | first pull: PJM's own forecast confirms structural growth (32GW/2030, 94% DC-driven) but not yet at the 2x-queue trigger level; IPP guidance reaffirmed, not raised | NOT-FIRED (confirmed-but-not-escalated) |
| P4 | spark spread negative (gas-fired uneconomic) sustained 3+ sessions | first pull: +$49.53/MWh baseline, +$551.50/MWh spike-day — wide positive both days | NOT-FIRED (opposite signal: spread widening, not compressing) |

**Fired-count: 1 of 4** (P2 structural). **Thesis-kill vs channel-kill:** a mild summer kills P1's live read for the season — it does NOT kill the thesis, which migrates to P2 (structural capacity) and P3 (buildout). The thesis dies only if the 28/29 BRA clears well below cap AND data-center queues drain — testable ~Dec-2026.

**Cleanest bidirectional flip (BRENT discipline):** the 28/29 BRA clear (~Dec-2026). Clears at cap again → thesis confirmed structural; clears materially below cap with queues draining → structural leg falsified.

---

## OPEN ON WATT (next session)

1. **Instrument upgrade (proposed, not built this session — triage-first):** wire the free EIA ICE wholesale-price file (`eia.gov/electricity/wholesale/xls/ice_electric-YYYY.xlsx`, `PJM WH Real Time Peak` row, biweekly, `openpyxl`-parseable) into `power_watch.py` as a P1 LMP-proxy leg + auto-computed P4 spark spread. Permanently closes the honest-wall noted at birth, at $0 cost and no gated key.
2. **Calibrate the P4 heat-rate assumption** — currently a flat 7.0 MMBtu/MWh (efficient-CCGT) ASSUMPTION; pull actual PJM gas-fleet heat rates (EIA-923) for a real number.
3. **Reconcile PJM's own 32GW/2030 data-center forecast vs Wood Mackenzie's utility-self-reported 55GW/2030** — a 23GW/70% gap, unrouted, possibly REGINALD/HENRY-relevant (utility over-commitment vs PJM's central planning number).
4. **PJM_API_KEY** — still open (Will-gated); once registered, wires the *official* LMP leg (finer-grained than the biweekly proxy).
5. **Resolve WATT-03/04/05** at next boot (see PREDICTIONS.tsv — resolve dates 7/20, 7/23, 8/2).

---

## BOTTOM LINE

**WATT's second session (2026-07-12) closed the founding gap** — all four core channels now carry a WATT-owned, sourced-and-dated live read, not inherited/placeholder ones. The biggest find: a free EIA wholesale-price file gives a usable PJM price proxy with no gated key, and it shows a real **$574.04/MWh Orange-band spike on 7/1** that the postings-only P1 read had completely missed (STATUS previously called P1 "quiet" for that whole window). P2 (structural capacity, 🔴) still carries the thesis unchanged. P3 confirms structural data-center-driven load growth via PJM's own forecast, with all four IPP names holding strong FY26 guidance. P4's first read shows a **wide, healthy** spark spread — heat stress widens it, doesn't compress it, a mechanism refinement worth carrying forward. Next: propose (don't yet build) the instrument upgrade that would make the LMP-proxy + spark-spread reads automatic at every boot.
