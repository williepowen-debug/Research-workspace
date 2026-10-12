# WATT — Domain Sweep, 2026-07-12

**Applied:** `PROME/packets/DOMAIN_SWEEP_LENSES.md` (4 lenses) against WATT's full corpus — STATUS, THESIS, TRADE, workbook/*.tsv, inbox, SCRATCH, LESSONS, NEXUS_BRIEF. First sweep run on WATT (newborn 2026-07-10, this is session 2).

**Context:** this session also closed the two founding gaps (P3, P4 — no WATT-pulled data since birth) and discovered a free LMP-proxy data source. Several sweep items below were closed inline during the session rather than left as proposals; they're marked ✅ CLOSED THIS SESSION.

---

## Prioritized findings

| # | Item | Lens | Age | Evidence | Proposed action | H-M-L |
|---|---|---|---|---|---|---|
| 1 | P3 channel carried inherited-only read since birth (7/10) | UNFINISHED WORK | 2 days | STATUS.md pre-edit: "⚠️ inherited read only" | ✅ CLOSED — first WATT pull done this session (PJM's own 20-yr forecast + IPP Q1-26 guidance) | H |
| 2 | P4 channel carried no live read since birth (7/10) | UNFINISHED WORK | 2 days | STATUS.md pre-edit: "no live read" | ✅ CLOSED — spark-spread computed (baseline + spike-day) | H |
| 3 | 2 inbox items unconsumed | UNFINISHED WORK | 1-2 days | `inbox/2026-07-10_from-DAEDALUS...`, `inbox/PROME_ROUTING_2026-07-11.md` | ✅ CLOSED — both read, logged to KB (KB-WATT-018/019), moved to `inbox/processed/` | M |
| 4 | "LMP leg NOT wired" framed as a hard blocker on `PJM_API_KEY` in STATUS/SCRATCH/NEXUS_BRIEF | UNFINISHED WORK / MISSED CONNECTION | 2 days | THRESHOLDS + STATUS language, pre-edit | ✅ CLOSED — free EIA ICE wholesale-price proxy found and used; STATUS/THESIS/LESSONS updated to stop over-stating the blocker | H |
| 5 | 3 catalysts in the next 3 weeks (FERC informational-report deadline 7/20; EIA Electric Power Monthly release 7/23; EIA wholesale-file next update ~7/21) had no pre-registered gradable resolver | GAPS | new this session | FERC show-cause order (Orrick, pub 7/6, order 6/18); EIA release-schedule search | Registered WATT-03/04/05 in PREDICTIONS.tsv (see below) | H |
| 6 | P4 heat-rate assumption (7.0 MMBtu/MWh) is a flat constant, not calibrated to PJM's actual gas fleet | GAPS | new this session | THESIS.md P4 table | Proposed (not built): pull EIA-923 generator-level heat-rate data for PJM footprint | M |
| 7 | 124GW on-site gas generation datum (LIQUID board_log) is single-sourced, not independently verified | GAPS | routed 7/11 | KB-WATT-018, source = 1 LIQUID board_log row | Flagged; verify independently before building further analysis on it | M |
| 8 | P3: PJM's own 32GW/2030 data-center-load-growth number vs Wood Mackenzie's utility-self-reported 55GW/2030 — 23GW/70% gap | MISSED CONNECTIONS / FURTHER THREADS | new this session | KB-WATT-012/013 vs KB-WATT-014 | Proposed: reconcile or explicitly carry both, routed to REGINALD/HENRY as an unresolved credit/FCF-timing angle | M |
| 9 | P4 spark-spread finding (wide, healthy, no compression during heat stress) never routed to BRENT — BRENT is the named gas-leg partner per THESIS boundaries | MISSED CONNECTIONS | new this session | THESIS.md boundaries section: "BRENT owns Henry Hub; WATT owns power curve + spark-spread coupling" | ✅ CLOSED — written into NEXUS_BRIEF this closeout | M |
| 10 | P1's new LMP-proxy spike (6/30–7/2) brackets the 7/3 EEA2 posting — no cross-check with AEOLUS's C3 heat-dome detection for that window | MISSED CONNECTIONS | new this session | KB-WATT-008 vs KB-WATT-003 | Proposed: quick cross-check next session, flagged to AEOLUS via NEXUS_BRIEF | L |
| 11 | Instrument-layer upgrade: automate the EIA wholesale-price pull into `power_watch.py` (currently a manual, one-off pull) | FURTHER THREADS | new this session | this session's manual `openpyxl` pull | Proposed for next session — single highest-value build (permanently closes P1/P4 honest-walls, $0 cost, no gated key) | H |
| 12 | PREDICTIONS.tsv had only 2 rows (WATT-01, WATT-02), both far-dated (12/31, 9/7) — no near-term calibration cadence | GAPS | since birth | workbook/PREDICTIONS.tsv pre-edit | ✅ CLOSED — WATT-03/04/05 added with 7/20–8/2 resolve dates | M |

---

## TOP 3 most consequential

**1. The free EIA wholesale-price proxy (item 4/11).** WATT was built with a named, explicit honest-wall: "LMP leg NOT wired — needs PJM_API_KEY (Will-gated)." That framing was accurate but incomplete — a check of `eia.gov/electricity/wholesale` (biweekly ICE-sourced OTC trade data, no key, `PJM WH Real Time Peak` hub) turned up a genuine, if coarser, price proxy. Using it immediately surfaced a real finding the postings-only P1 read had missed entirely: PJM Western Hub RT Peak weighted-average price hit **$574.04/MWh on 2026-07-01** — Orange band (≥$500) — a 3-day escalation from $134 (6/29) that bracketed the known 7/3 EEA2 declaration, then fully retreated to $72 by 7/7. This is simultaneously a data-source win (closes 2 of 4 founding gaps in one pull) and a real finding (P1 already had its first confirmed price-stress event, one WATT didn't know about until this session).

**2. P3/P4 gap closure itself.** Both channels carried inherited or absent reads since WATT's birth two days ago. The channels-first #1 guard (an empty channel is a gap, not idle background) was WATT's own founding discipline; this session is the first time it's been honored in full. P3 now rests on PJM's own official 20-year forecast (32GW/2030 data-center-driven load growth) plus a clean Q1-2026 guidance check across all 4 named IPPs (VST/CEG/NRG/TLN — all reaffirmed or beat, none cut). P4 now has a real spark-spread computation showing the mechanism runs opposite to naive expectation: heat stress *widens* the spread rather than compressing it, because gas is PJM's marginal price-setter and captures the scarcity rent directly.

**3. The unreconciled P3 32GW-vs-55GW divergence.** PJM's own official load forecast attributes 32GW of 2024-2030 peak-load growth to data centers; Wood Mackenzie's analysis of utility self-reported commitments puts the PJM-footprint number at 55GW by 2030 (100GW by 2037) — a 23GW/70% gap between the grid operator's central planning number and what individual utilities say they've committed to serve. Nobody has explained this gap yet, and it's exactly the kind of over-commitment-vs-official-forecast tension that could matter to REGINALD's credit read or HENRY's FCF-timing model if utilities are contracting ahead of what PJM's own reliability planning assumes. Flagged, not resolved, this session.

---

## ROUTE-OUTS for PROME

- **BRENT** — P4 spark-spread first read (wide/healthy, no compression; mechanism refinement on the heat-stress↔spread relationship). Delivered via NEXUS_BRIEF this closeout — confirm BRENT consumes it next session.
- **HENRY** — P1's confirmed $574.04/MWh Orange-band spike (7/1, now retreated) + P3's clean IPP guidance check (all 4 reaffirmed/beat). Delivered via NEXUS_BRIEF.
- **REGINALD / HENRY** — the unreconciled 32GW (PJM-own) vs 55GW (WoodMac/utility-self-reported) P3 load-growth divergence — a possible utility-over-commitment credit/FCF angle nobody owns yet. Flagged via NEXUS_BRIEF, not yet a formal task packet — PROME's call whether it's worth a dedicated ask.
- **AEOLUS** — opportunity (not urgent) to cross-check WATT's new LMP-proxy spike window (6/30–7/2) against AEOLUS's own C3 heat-dome detection for the same dates, to test the shared-antecedent independence claim already in STATUS's convergence matrix.
- **PROME** — no file-hygiene or cross-agent conflict issues found this sweep; WATT's own corpus is small and clean (2-day-old agent). Nothing needs PROME-level arbitration this session.
