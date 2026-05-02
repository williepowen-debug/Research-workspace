# CARL SCRATCH
**Last session:** 2026-05-01 ~10:00-21:00 UTC (Will-driven thesis v2.5 promotion — 3 revisions with 2 rounds of external review feedback + architectural realignment with RED + canonical promotion sequenced in 3 chunks)
**Type:** Thesis-level promotion session — v2.4.1 → v2.5 canonical

**PRIORITY-1:** **AAA pump $4.50 threshold breach watch (likely May 2-5).** Pump $4.392 May 1 (+9.2¢ overnight pace), gap to threshold $0.108. CRL-08 currently 92%. Daily AAA refresh required. If breach holds 2+ weeks, mark CRL-08 CONFIRMED. Daily check is ~5min work; v2.5.1 hardening work is the secondary track.

---

## WHAT HAPPENED

1. **Boot + state-of-CARL triage** — pulled clean, read all boot files, BOARD diff-clean (98/98), produced 5-most-significant list per Will request.
2. **Phase 0 Read** — read THESIS.md (v2.4.1, 58/60), CHANGELOG (full version trail), red_team/* (SOFT_LANDING <5%, CONTAINMENT 15-20%), spot-checked KB-CARL-222 through 262.
3. **Phase 1 Counter-test of data-masking generalization** — confirmed framework is real (already operational at KB-225, applied to ALLY/SYF/COF/AFRM/Rithm). 5+ industry mechanisms, same META-pattern. Counter-hypothesis test: SOFT_LANDING fails on cohort decomposition; CONTAINMENT is a timing-difference (falsifiable Q1 2027).
4. **Phase 2 Drafted v2.5 r1** (commit c0e06744) — initial draft, 12-vector matrix, 58/60 → 54/60.
5. **Phase 2 r2** (commit 36c1e5f3) — 13 reviewer critiques addressed: matrix expanded to 14 vectors, score rescaled, V8/V9 merge, HY OAS reframe, energy stickiness, TTM hurdle, intermediate falsification, puzzles section, fast early-warning kill. 54/70 (74%).
6. **Will surfaces RED agent** — review's "selection bias" critique dissolves under multi-agent architecture. Several r2 design choices were architecturally confused.
7. **Phase 2 r3** (commit 036c7247) — architectural realignment: V15 removed (RED domain), V16 Employment added (was missing), Counter-Evidence section stripped, Puzzles trimmed to thesis-internal only, V2 strict-def 5→4, CRL-21 operational thresholds + position-action commitment, Path C provisional/firm operational table, Trade Duration Implications section added, honest conviction reframe (60% calibration + 40% conviction reduction). 53/70 (76%).
8. **handoff_RED/ folder created** (commit 3d0bdf75) — git mv'd red_team/* (preserves history); README.md explains transitional staging; CARL CLAUDE.md updated.
9. **handoff_RED/COUNTER_EVIDENCE_FROM_THESIS.md** added — Counter-Evidence section content staged for RED.
10. **Phase 3 canonical promotion (3 chunks):**
    - **Chunk 1 (commit 1faf70ce):** THESIS.md (v2.4.1 → v2.5), CHANGELOG (audit entry), PREDICTIONS.tsv (+CRL-20, +CRL-21), draft file deleted.
    - **Chunk 2 (commit ca003039):** STATUS.md convergence mirror updated, predictions table refreshed, KB-CARL-263 added.
    - **Chunk 3 (this session end):** ROADMAP updated with v2.5.1 hardening thread + RECENTLY RESOLVED entry, SCRATCH rewritten.

## STATUS CHANGES
| Item | Change |
|------|--------|
| THESIS.md | v2.4.1 (Apr 17) → **v2.5** (May 1) — full promotion |
| Convergence score | 58/60 (97%) → **53/70 (76%)** — recalibrated and architecturally aligned |
| Convergence matrix | 12 vectors → **14 vectors** (V8+V9 merged; V13 Federal Fiscal Capacity, V14 Upper-Decile Wealth Stress, V16 Employment Structural Rot added; V15 Refi-Window dropped to RED) |
| Score 5-definition | Tightened to "fully fired, no further upside in mechanism." Currently **0 vectors at 5** |
| V2 Subprime Auto | 5 → **4** (strict-def: EART terminal but AMCAR/SDART have cushion) |
| V4 Student Loan 90+ | 5 → **4** (rescaled — room to escalate) |
| V5 Gas Squeeze | 5 → **4** (rescaled — $4.50/$5+ still possible) |
| V6 UI Exhaustion | 5 → **4** (mechanism unverified) |
| V8 K-Shape Converging | 5+5 → **4** (merged + magnitude caveat) |
| V10 Foreclosure | 5 → **4** (rescaled, base-effect caveat) |
| V11 SB Bankruptcy | 4 → **3** (rescaled) |
| V12 Stagflation Trap | 5 → **4** (rescaled, TTM not crossed) |
| Path C status | ACTIVATING-RED → **ACTIVE-RED (PROVISIONAL)** pending COF/SYF Q1'24/'25 counterfactual |
| Cross-Industry Data Masking | KB-225 framework → **thesis-level methodology** with intermediate Q3'26 + outer Q1'27 falsification windows |
| HY OAS | Counter-evidence → **masking-thesis confirmation** (reclassified) |
| Counter-Evidence section | Stripped from THESIS, **staged at handoff_RED/COUNTER_EVIDENCE_FROM_THESIS.md** |
| red_team/ folder | Moved to **handoff_RED/** (git mv, history preserved) |
| Puzzles section | 5 puzzles → **3 thesis-internal** (counter-narrative routed to RED) |
| CARL CLAUDE.md | red_team/ row replaced with handoff_RED/ pointer |
| PREDICTIONS | 19 → **21** (+CRL-20 75% Q1 2027 outer, +CRL-21 60% Q3 2026 intermediate w/ position-action) |
| KB | 262 → **263** rows (+KB-CARL-263 v2.5 thesis statement) |

---

## NEXT SESSION SHOULD

### IMMEDIATE (next 24-48hrs)
1. **DAILY AAA pump refresh** — track $4.50 breach (likely May 2-5). When breach holds 2+ weeks, mark CRL-08 CONFIRMED.
2. **Brent close monitoring** — sustainability test ($107+ vs collapse on Iran peace). Iran cluster live: WPR deadline May 1 + peace proposal in mediation.
3. **EIA inventory print Wed May 7** — distillate (KB-253 follow-up) + gasoline stocks.

### UPCOMING (this week)
4. **May 5 — PayPal Q1** (PHAN spawn) — first under new CEO Lores. Apply masking framework decompose.
5. **May 6** — Uber Q1 + DoorDash Q1 (GIG) — driver count QoQ post-gas.
6. **May 6** — BLS state jobs March (FL labor extension test).
7. **May 7 TRIPLE** — Dave Q1 (28DPD GIG-P01) + Lyft Q1 + Affirm Q3 FY2026.

### UPCOMING (next 2 weeks)
8. **May 8** — BLS Apr NFP — V16 Employment Structural Rot first realized print.
9. **~May 18** — Klarna Q1 2026 (PHAN — first full quarter post-FY-loss).
10. **~Mid-May** — NY Fed Q1 2026 HHDC — CARL CORE — CC 90+ DQ vs 12.7%; tests CRL-05.
11. **May 28** — BEA Q1 GDP second estimate — CRL-18 resolves.
12. **~May 30** — March monthly Core PCE — CRL-19 resolves.

### v2.5.1 HARDENING (queued, no fixed dates)
13. **UMich triangulation** — verify TIPS 5y5y / SPF / NY Fed 3yr against UMich 5-10Y 3.5%.
14. **Foreclosure 2019 absolute baseline** — ATTOM Q1 2019 REO completions for non-pandemic comparison.
15. **Path C counterfactual** — pull COF/SYF Q1'24/'25 ACL builds from 10-Q filings; promote provisional → firm OR downgrade to ACTIVATING-RED.
16. **Crying-wolf X-threshold operational doc** — refine 20bps credit / 50bps non-credit placeholders.
17. **Brier audit full prediction history** — CRL-01 through CRL-21 + legacy.
18. **CONTAINMENT prior-calibration audit** — joint CARL-RED.
19. **COF/SYF candor puzzle** — RED handoff.
20. **Trade Duration roll plan** — FORGE/REGINALD coord on KRE/WAL Dec 2026 → Q1-Q2 2027.
21. **RED-CARL interface protocol** — handshake document.

### BACKLOG (no deadline)
22. **LABOR/GIG spawn** for FL UI Wave 2 (KB-CARL-262 partial).
23. **HOMER spawn** for Case-Shiller Feb sub-market detail (KB-CARL-261 headline only).
24. **Workbook stale refresh** — VX consumer rows / FLOW / STATE_DIFFUSION / BNPL_STRESS (14d stale).
25. **ABS_BASELINE refresh** — March 10-Ds (15d stale; EART terminal + AMCAR ~2mo + SDART ~7mo).
26. **6 outbox signals from Apr 17** — defer per messaging-overhaul.

---

## OUTBOX (6 signals, all from Apr 17 — messaging overhaul pending)
| File | To | Summary |
|------|----|---------|
| SIG-CARL-REGINALD-20260417-auto-lender-reclassification-translation.md | REGINALD | 7-lever auto-lender translation of 3-layer bank framework + ALLY Q1 |
| SIG-CARL-REGINALD-20260417-subprime-auto-ABS-gap.md | REGINALD | Santander/Bridgecrest/Exeter 7.9/7.8/6.7% 60+ DQ |
| SIG-CARL-LIQUID-20260417-BNPL-ABS-composition-degradation.md | LIQUID | BNPL ABS composition new structured-credit sub-vector |
| SIG-CARL-LABOR-20260417-FL-UI-Wave2-gig-surge.md | LABOR | Apr 26 FL UI Wave 2 + $4.09 FL gas + 22% gig concentration |
| SIG-CARL-LABOR-20260417-NFIB-SB-hiring-pullback.md | LABOR | NFIB Mar: Optimism 95.8, Uncertainty BREACHED 92, profit -25% |
| SIG-CARL-REGINALD-20260417-IEEPA-refund-SB-liquidity-injection.md | REGINALD | SCOTUS IEEPA struck, $166B refunds Apr 20 = SB regional bank stress modifier |

## INBOX (0 items, clean)

## HANDOFF_RED (4 files staged, awaiting RED pickup)
| File | Notes |
|------|-------|
| COUNTER_LOG.md | Running counter-evidence log (was red_team/) |
| SOFT_LANDING.md | Competing hypothesis <5% (was red_team/) |
| CONTAINMENT.md | Competing hypothesis 15-20% (was red_team/) |
| COUNTER_EVIDENCE_FROM_THESIS.md | Stripped Counter-Evidence section + disposition rules + HY OAS reclassification note |

---

## WORKBOOK HEALTH
| TSV | Rows | Last Modified | Note |
|-----|------|---------------|------|
| KB | **263 (IDs to 263)** | **May 1 PM2** | +1 today (KB-CARL-263 v2.5 thesis statement) |
| VX | 112 | May 1 | Fresh on macro side |
| FLOW | 22 | Apr 17 | 14d — refresh due |
| PREDICTIONS | **21** | **May 1 PM2** | +CRL-20 (Q1'27 outer 75%), +CRL-21 (Q3'26 intermediate 60% + position-action) |
| STATE_DIFFUSION | 63 | Apr 17 | 14d — fold KB-CARL-249 on next pass |
| BNPL_STRESS | 44 | Apr 17 | 14d — refresh due |
| ABS_BASELINE | 67 | Apr 16 | 15d — March 10-Ds available |
| TRENDS | 40 | Apr 6 | 25d STALE — low priority |
| ML | 67 | Apr 7 | 24d STALE — low priority |

BOARD_LOG: 105 lines, 98 dispositions, **diff-clean against INDEX as of May 1**.

---

## URGENT

- **AAA pump $4.50 breach watch** — daily refresh (likely May 2-5).
- **Iran cluster live** — WPR deadline May 1 today, peace proposal in Pakistani mediation.
- **v2.5.1 hardening queue (9 items)** — sequencing matters: data items 1-3 before Brier audit (item 5).
- **Q3 2026 = CRL-21 first checkpoint** — ALLY consumer auto NCO ≥+30bps QoQ for 2 consecutive quarters OR vintage projections diverge above FY2023 ≥+50bps. **POSITION-ACTION COMMITMENT** if fails: confidence -25-30pp + trim 25% + extend duration to Q2 2027+.
