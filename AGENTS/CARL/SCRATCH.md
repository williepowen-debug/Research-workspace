# CARL SCRATCH
**Last session:** 2026-05-02 ~14:00-17:00 UTC (Will-driven workbook restructure session — boot + AAA pump check + 3-phase workbook cleanup to "TSVs only" compliance)
**Type:** Maintenance + daily monitoring — workbook 31 → 9 files

**PRIORITY-1:** **AAA pump $4.50 breach watch — likely May 3-4.** May 2 = $4.433 (+4.1¢ overnight, pace decelerated from May 1's +9.2¢ — partial Saturday calendar effect). Gap to threshold $0.067 (was $0.108 May 1). At today's pace breach in ~1.6 days; at weekly pace also May 4-5. Daily AAA check is ~5min work. CRL-08 stays 92% (reprice to 95%+ deferred until threshold-cross + 2-week sustainability test).

---

## WHAT HAPPENED

1. **Boot clean** — pulled, BOARD diff-clean (98/98), inbox empty, outbox holds 6 Apr 17 signals (deferred per messaging-overhaul).
2. **Two thesis-thoughts files archived** — Will dropped v2.5 r1/r2 review docs in thesis/; moved to `archive/reviews/2026-05-01_v2.5_r1_review.md` + `..._r2_review.md`. Content fully integrated into canonical thesis yesterday.
3. **AAA pump check May 2** — $4.433 (+4.1¢ overnight, +34.7¢ WoW, +35.2¢ MoM, +39.4% YoY). Gap to $4.50 = $0.067. Diesel $5.627 (+16.3¢ vs Apr 29) — diesel divergence narrowing. KB-CARL-264 added; VX-CARL-GAS-01 + STATUS gas row updated. **Data caveat:** AAA top-state list returned East-Coast-only (CA/WA/OR/NV missing) — fetch parse anomaly, headline corroborated by internal consistency.
4. **Workbook audit** — 31 files, only 9 canonical TSVs per CLAUDE.md. 70% sediment (deprecated TSVs, prose MDs, misfiled archives, Excel predecessor).
5. **Phase 1A trash (2 files)** — `ML_old_9col.tsv` (true duplicate of ML.tsv with supersession notes added), `CARL_MLFLFLOWVX_S6.xlsx` (91KB Excel predecessor). Used `gio trash`.
6. **Phase 1B archive/snapshots (3 files)** — `VX_HISTORY.tsv` (Jan-Feb 2026 first-read snapshot), `CARL_ML_S2_ADDITIONS.tsv` (FOUNDING entries: NICK/POLLY/PHANTOM/Beneath-the-Ice-synthesis ML-CARL-01), `CARL_ML_MARCO_TRANSFER_FOOD.tsv` (Jan 22 MARCO domain transfer record). Spot-checked content first — 3 of 5 originally proposed for trash were actually founding/historical material; revised proposal to ARCHIVE not delete.
7. **Phase 1C archive/status (2 files)** — `STATUS_archive_20260325.md` + `STATUS_archive_mar1_mar15.md` (misfiled, belonged in archive/).
8. **Phase 2 Tier 3 cluster disposition (14 files):**
   - **Cluster A (5 files) → `domain/sources/ABS/`:** ABS_TRACKING_FRAMEWORK, ABS_BASELINE_PROTOCOL, ABS_IMPLEMENTATION_SUMMARY, ABS_QUICK_REFERENCE, SDART_ABS_BASELINE_2026-03-11
   - **Cluster B (1 file) → `domain/sources/`:** STATE_STRESS_FRAMEWORK
   - **Cluster C (2 files) → `archive/trade_analyses/`:** CONSUMER_FINANCE_TRADE_ANALYSIS_2026-02-16, HOMEBUILDER_TRADE_ANALYSIS_2026-02-16
   - **Cluster D (6 files) → `archive/founding_synthesis/`:** ML-CARL-01..06 (incl. BENEATH_THE_ICE_SYNTHESIS — origin of thesis name; METRIC_ARTIFACTS_AND_MASKING — origin of v2.5 cross-industry data masking framework)
   - **Cluster E (1 file) → `domain/sources/`:** ML-CR-18_PHANTOM_DEBT_ANALYSIS (PHAN reference)
9. **Atomic path edits:**
   - `domain/sources/ABS/README.md` — 4 path refs fixed (was pointing to nonexistent `domain/workbook/`)
   - `sub_agents/PHAN/CLAUDE.md` — ML-CR-18 path updated `workbook/` → `domain/sources/`
10. **Verification** — sweep for `workbook/<moved-file>` broken refs returned ZERO. Workbook now exactly 9 canonical TSVs (KB, VX, FLOW, ABS_BASELINE, BNPL_STRESS, STATE_DIFFUSION, SCHEMA, TRENDS, ML).
11. **ROADMAP updated** — 2 new RECENTLY RESOLVED rows (restructure + AAA pump), 1 OPEN QUESTION refreshed (TRENDS/ML retirement decision surfaced).

## STATUS CHANGES
| Item | Change |
|------|--------|
| Workbook | **31 → 9 files** (full CLAUDE.md "TSVs only" compliance) |
| AAA pump | $4.392 May 1 → **$4.433 May 2** (+4.1¢ overnight) |
| Gap to $4.50 | $0.108 → **$0.067** (breach now likely May 3-4) |
| Diesel | $5.464 Apr 29 → **$5.627 May 2** (+16.3¢) — divergence narrowing |
| KB | 263 → **264** rows (+KB-CARL-264 May 2 pump) |
| VX-CARL-GAS-01 | refreshed May 2 |
| STATUS gas pump row | refreshed May 2 with caveat note |
| `domain/sources/ABS/README.md` | 4 broken `domain/workbook/` paths fixed |
| `sub_agents/PHAN/CLAUDE.md` | ML-CR-18 path fixed |
| `archive/` tree | created (5 subdirs: reviews/, snapshots/, status/, trade_analyses/, founding_synthesis/) |
| `domain/sources/` | +7 files (5 in ABS/, 2 at top-level) |
| ROADMAP | +2 RECENTLY RESOLVED + 1 OPEN QUESTION refresh |

---

## NEXT SESSION SHOULD

### IMMEDIATE (next 24-48hrs)
1. **DAILY AAA pump refresh** — $4.50 breach likely May 3-4. When breach holds 2+ weeks, mark CRL-08 CONFIRMED.
2. **Brent close monitoring** — sustainability test ($107+ vs collapse on Iran de-escalation). Iran WPR deadline May 1 expired without resolution.
3. **Diesel divergence sustainability** — May 2 +16.3¢ catching up to crude. If trend continues through May 7 EIA inventory print, KB-CARL-253 freight-demand thread weakening confirmed.

### UPCOMING (this week)
4. **May 5** — PayPal Q1 (PHAN spawn) — first under new CEO Lores. Apply masking framework decompose.
5. **May 6** — Uber Q1 + DoorDash Q1 (GIG) — driver count QoQ post-gas.
6. **May 6** — BLS state jobs March (FL labor extension test).
7. **May 7 TRIPLE** — Dave Q1 (28DPD GIG-P01) + Lyft Q1 + Affirm Q3 FY2026.
8. **May 7** — EIA weekly inventory print — distillate (KB-253 follow-up) + gasoline stocks.

### UPCOMING (next 2 weeks)
9. **May 8** — BLS Apr NFP — V16 Employment Structural Rot first realized print.
10. **~May 18** — Klarna Q1 2026 (PHAN — first full quarter post-FY-loss).
11. **~Mid-May** — NY Fed Q1 2026 HHDC — CARL CORE — CC 90+ DQ vs 12.7%; tests CRL-05.
12. **May 28** — BEA Q1 GDP second estimate — CRL-18 resolves.
13. **~May 30** — March monthly Core PCE — CRL-19 resolves.

### v2.5.1 HARDENING (queued, no fixed dates — same as May 1)
14. UMich triangulation — verify TIPS 5y5y / SPF / NY Fed 3yr against UMich 5-10Y 3.5%.
15. Foreclosure 2019 absolute baseline — ATTOM Q1 2019 REO completions.
16. Path C counterfactual — pull COF/SYF Q1'24/'25 ACL builds; promote provisional → firm OR downgrade.
17. Crying-wolf X-threshold operational doc.
18. Brier audit full prediction history — CRL-01 through CRL-21 + legacy.
19. CONTAINMENT prior-calibration audit — joint CARL-RED.
20. COF/SYF candor puzzle — RED handoff.
21. Trade Duration roll plan — FORGE/REGINALD coord on KRE/WAL Dec 2026 → Q1-Q2 2027.
22. RED-CARL interface protocol — handshake document.

### NEW SURFACED (May 2)
23. **ML.tsv retirement decision** — CLAUDE.md calls it "legacy data log." Its ancestors (ML_old_9col, ML synthesis MDs, S2_ADDITIONS) are now archived. Question: fully retire to archive/ or keep refreshing? Surfaced during workbook restructure. Low priority.
24. **2 broken paths in ABS README left alone** (`domain/workbook/VX.tsv`, `domain/workbook/FL.tsv` — FL.tsv doesn't exist anymore). Out of scope this pass; flag if next ABS-touching session.

### BACKLOG (no deadline)
25. LABOR/GIG spawn for FL UI Wave 2 (KB-CARL-262 partial).
26. HOMER spawn for Case-Shiller Feb sub-market detail (KB-CARL-261 headline only).
27. Workbook content refresh — VX consumer rows / FLOW / STATE_DIFFUSION / BNPL_STRESS (15d stale).
28. ABS_BASELINE refresh — March 10-Ds (16d stale; EART terminal + AMCAR ~2mo + SDART ~7mo).
29. 6 outbox signals from Apr 17 — defer per messaging-overhaul.

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

## WORKBOOK HEALTH (after restructure)
| TSV | Rows | Last Modified | Note |
|-----|------|---------------|------|
| KB | **264** | **May 2** | +1 today (KB-CARL-264 AAA pump May 2) |
| VX | 112 | **May 2** | GAS-01 refreshed |
| FLOW | 22 | Apr 17 | 15d — refresh due |
| PREDICTIONS | 21 | May 1 PM2 | (canonical in `thesis/PREDICTIONS.tsv`) |
| STATE_DIFFUSION | 63 | Apr 17 | 15d — fold KB-CARL-249 on next pass |
| BNPL_STRESS | 44 | Apr 17 | 15d — refresh due |
| ABS_BASELINE | 67 | Apr 16 | 16d — March 10-Ds available |
| TRENDS | 40 | Apr 6 | 26d STALE — low priority OR retire? |
| ML | 67 | Apr 7 | 25d STALE — CLAUDE.md calls "legacy"; **retirement decision queued** |
| SCHEMA | 14 | Mar 17 | static (column defs) |

**Workbook contains EXACTLY the 9 canonical TSVs per CLAUDE.md.** No prose, no archives, no deprecated files. Full compliance achieved.

BOARD_LOG: 105 lines, 98 dispositions, **diff-clean against INDEX as of May 1** (no new BOARD signals May 2).

---

## URGENT

- **AAA pump $4.50 breach watch** — daily refresh; breach likely May 3-4.
- **Iran cluster still live** — WPR deadline May 1 expired without resolution; Brent at $107-110 sustained.
- **v2.5.1 hardening queue (9 items)** — sequencing matters: data items 1-3 before Brier audit (item 5).
- **Q3 2026 = CRL-21 first checkpoint** — ALLY consumer auto NCO ≥+30bps QoQ for 2 consecutive quarters OR vintage projections diverge above FY2023 ≥+50bps. **POSITION-ACTION COMMITMENT** if fails: confidence -25-30pp + trim 25% + extend duration to Q2 2027+.
