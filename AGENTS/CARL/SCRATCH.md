# CARL SCRATCH
**Last session:** 2026-05-03 ~23:30 UTC (PM4)
**Type:** STATUS staleness audit Cluster 1 — direct CARL data refresh + CRL-19 RESOLVED

**PRIORITY-1:** **Cluster 2 + Cluster 3 — Cross-agent stale fixup + FOMC May 6-7 to DANGER WINDOW.** Cluster 1 done. Cluster 2 = sync HAWK/BRENT row to today's data (or remove duplication w/ Macro Brent), refresh FOMC for May 6-7 meeting (3 days out), age-out Mar 24 FL UI Wave 1 from "Recently Fired" (40d old). Cluster 3 = add FOMC May 6-7 to DANGER WINDOW. Plus **HY OAS refresh** — FRED + 4 secondaries all blocked May 3; need fetch path resolution (try FRED API key / abs_monitor.py / dedicated tool).

---

## WHAT HAPPENED

1. **Boot per spawn protocol** — git pull clean; read SCRATCH/STATUS/SCHEMA/TEAM/ROADMAP. Skipped BOARD diff per conditional rule.
2. **Will requested readout** — answered with breakdown: immediate, this week (May 5-8), next 2 weeks, v2.5.1 hardening, workbook hardening, backlog.
3. **Plan-mode AAA + Iran (PM3)** — Approved, executed.
4. **PM3 work:** Live data AAA $4.446 + Brent $108.17 + Iran cluster bidirectional. KB-268/269 + VX-CARL-GAS-01. STATUS gas/diesel/Brent/WTI/Iran rows. CRL-08 NEAR-BREACH NOT-YET. Commit 7df5c0ba.
5. **STATUS staleness audit (this session)** — Will asked to look for stale rows. Identified 3 clusters: direct CARL refresh / cross-agent stale fixup / FOMC missing.
6. **Cluster 1 executed:** 5 web fetches (Freddie PMMS / MBA via tradingeconomics / BEA Mar PCE / Census Mar Retail / CB Apr); HY OAS BLOCKED (FRED + 4 secondaries 403/404).
7. **CRL-19 RESOLVED direction-correct/magnitude-light:** predicted Mar Core PCE 3.3-3.5%, actual 3.2% (10bps below floor; +20bps accel vs predicted +30-50bps). Strict-def MISSED. Same pattern as CRL-01 — calibration warning.
8. **KB additions** (Python append, schema-clean, 15-col):
   - KB-CARL-270: BEA Mar 2026 PCE (full mechanism — Real DPI -0.1% / PCE +0.9% / Core PCE 3.2% / Savings 3.6%)
   - KB-CARL-271: Census Mar Retail (+1.7% headline / +15.5% gas record / +0.7% control group)
   - KB-CARL-272: Mortgage Apr 30 (PMMS reversal + MBA contract +2bps)
   - KB-CARL-273: CB Apr (92.8 / 72.2 / 4 consec months <80)
9. **VX updates (5 rows in place):** HSG-01 (mortgage), SENT-02 (CB), SAV-01 (savings), 6.10 (retail control), MACRO-07 (Notes bridge resolved).
10. **STATUS edits (9):** Updated timestamp + 30-Yr Mortgage + MBA Purchase Apps + HY OAS (marked PENDING REFRESH) + Savings Rate + Core PCE Monthly + CB Expectations + Retail Sales + Real Consumer Spending + Real DPI + Retail Control Group + CRL-19 moved Open→Resolved.
11. **PREDICTIONS.tsv:** CRL-19 OPEN → MIXED + Date_Resolved 2026-05-03 + Outcome populated.
12. **CHANGELOG.md:** PM3 CRL-19 resolution entry added.
13. **Commit + push pending.**

## STATUS CHANGES
| Item | Change |
|------|--------|
| `workbook/KB.tsv` | 266 → 270 (+KB-270 BEA Mar / +KB-271 Census / +KB-272 Mortgage / +KB-273 CB Apr) |
| `workbook/VX.tsv` | 5 rows updated in place: HSG-01 mortgage Apr 30, SENT-02 CB Apr 72.2, SAV-01 savings 3.6%, 6.10 retail control 0.7%, MACRO-07 Notes bridge resolved |
| `STATUS.md` | 9 row edits + Updated timestamp + CRL-19 moved to Resolved; 237 lines (unchanged) |
| `thesis/PREDICTIONS.tsv` | CRL-19 OPEN → MIXED, Date_Resolved 2026-05-03 |
| `thesis/CHANGELOG.md` | New PM3 CRL-19 resolution entry |
| `ROADMAP.md` | PM4 RECENTLY RESOLVED entry + timestamp |
| Vector #12 | UNCHANGED — bridge HOLDS (3.2% monthly consistent w/ 4.3% Q1 NIPA via base-effect math). Calibration warning, not thesis warning. |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **Cluster 2 + Cluster 3 — Cross-agent stale fixup + FOMC.** HAWK/BRENT row sync, MARCO refresh ask, FOMC May 6-7, age-out >30d "Recently Fired" items, add FOMC May 6-7 to DANGER WINDOW.
2. **HY OAS refresh** — FRED direct + secondaries blocked. Try alternative paths: FRED API key, abs_monitor.py, dedicated fetch tool.
3. **AAA pump Mon May 4 refresh** — first weekday post-Brent-pullback; resolves CRL-08 timing.

### UPCOMING (this week)
4. **May 5** — PayPal Q1 (PHAN spawn) — first under new CEO Lores.
5. **May 6** — Uber Q1 + DoorDash Q1 (GIG) — driver count QoQ.
6. **May 6** — BLS state jobs March (FL labor).
7. **May 6-7** — **FOMC meeting** (currently NOT in DANGER WINDOW — fix in Cluster 3).
8. **May 7 TRIPLE** — Dave Q1 + Lyft Q1 + Affirm Q3 FY2026.
9. **May 7** — EIA weekly inventory (distillate / DSL-01).
10. **May 8** — BLS Apr NFP — V16 first realized print.

### UPCOMING (next 2 weeks)
11. **May 13** — BLS Apr CPI — first full Iran-shock + tariff month.
12. **~May 18** — Klarna Q1 (PHAN).
13. **~Mid-May** — NY Fed Q1 HHDC — **CARL CORE — CC 90+ DQ vs 12.7% / CRL-05 test**.
14. **May 28** — BEA GDP Q1 second estimate (CRL-18 resolves) + AFT/MOHELA conference.

### v2.5.1 HARDENING (8 PENDING_VERIFY items)
15-23. UMich triangulation / Foreclosure 2019 baseline / Path C COF/SYF counterfactual / Crying-wolf X-thresholds / Brier audit / CONTAINMENT prior calibration / COF/SYF candor puzzle / Trade Duration roll plan / RED-CARL interface.

### BACKLOG (no deadline)
24. **HY OAS refresh path** — fetch tooling.
25. Workbook hardening Item #3 (validator promotion).
26. Sub-agent workbook standardization (POP KB.tsv).
27. Workbook hardening Item #6 (root INDEX.md).
28. Supply-event sub-vector class.
29. Orphan-Claim Audit Byproduct.
30. LABOR/GIG spawn for FL UI Wave 2.
31. HOMER spawn for Case-Shiller Feb sub-market detail.
32. Workbook content refresh — VX consumer / FLOW / STATE_DIFFUSION / BNPL_STRESS (16-17d stale).
33. ABS_BASELINE refresh — March 10-Ds (17d).
34. **POLLY refresh** — 24d stale.
35. 6 outbox signals from Apr 17 (deferred per messaging-overhaul).

### CRL-19 calibration follow-up
36. **Brier audit pattern check:** CRL-01 + CRL-19 both direction-right/magnitude-low. Two data points = pattern of magnitude over-confidence? v2.5.1 hardening item #5 (Brier audit full prediction history) may want this question framed: are CARL predictions systematically over-magnitude, or is it sampling artifact at n=2?

---

## OUTBOX (6 Apr 17 signals deferred per messaging-overhaul; no new this session)
| File | To | Summary |
|------|----|---------|
| SIG-CARL-REGINALD-20260417-auto-lender-reclassification-translation.md | REGINALD | 7-lever auto-lender translation of 3-layer bank framework + ALLY Q1 |
| SIG-CARL-REGINALD-20260417-subprime-auto-ABS-gap.md | REGINALD | Santander/Bridgecrest/Exeter 7.9/7.8/6.7% 60+ DQ |
| SIG-CARL-LIQUID-20260417-BNPL-ABS-composition-degradation.md | LIQUID | BNPL ABS composition new structured-credit sub-vector |
| SIG-CARL-LABOR-20260417-FL-UI-Wave2-gig-surge.md | LABOR | Apr 26 FL UI Wave 2 + $4.09 FL gas + 22% gig concentration |
| SIG-CARL-LABOR-20260417-NFIB-SB-hiring-pullback.md | LABOR | NFIB Mar: Optimism 95.8, Uncertainty BREACHED 92, profit -25% |
| SIG-CARL-REGINALD-20260417-IEEPA-refund-SB-liquidity-injection.md | REGINALD | SCOTUS IEEPA struck, $166B refunds Apr 20 = SB regional bank stress modifier |

## INBOX (0 items, clean)

## HANDOFF_RED (4 files staged, awaiting RED pickup — unchanged this session)
| File | Notes |
|------|-------|
| COUNTER_LOG.md | Running counter-evidence log |
| SOFT_LANDING.md | Competing hypothesis <5% |
| CONTAINMENT.md | Competing hypothesis 15-20% |
| COUNTER_EVIDENCE_FROM_THESIS.md | Stripped Counter-Evidence section + disposition rules + HY OAS reclassification note |

---

## WORKBOOK HEALTH (post May 3 PM4 refresh)
| TSV | Rows | Cols | Last Modified | Note |
|-----|------|------|---------------|------|
| KB | **270** | 15 | **May 3 PM4** | +KB-270/271/272/273 (BEA Mar / Census Mar / Mortgage / CB Apr); 0 dangling KB→VX refs preserved; 0 enum / hygiene / col-count violations |
| VX | 121 | 11 | **May 3 PM4** | 5 rows updated in place: HSG-01, SENT-02, SAV-01, 6.10, MACRO-07 Notes |
| SCHEMA | 15 | 7 | May 2 PM | Unchanged |
| PREDICTIONS | 24 | 10 | **May 3 PM4** | CRL-19 OPEN → MIXED |
| THESIS.md | — | — | May 3 AM | Unchanged |
| CHANGELOG.md | — | — | **May 3 PM4** | +CRL-19 resolution entry |
| ROADMAP.md | — | — | **May 3 PM4** | PM4 RECENTLY RESOLVED entry |
| STATUS.md | — | — | **May 3 PM4** | 237 lines (unchanged); 9 row edits |
| HOMER/KB | 65 | 12 | May 2 PM3 | Unchanged |
| FLOW | 24 | 9 | Apr 17 | 16d — refresh due |
| STATE_DIFFUSION | 62 | 12 | Apr 17 | 16d |
| BNPL_STRESS | 59 | 13 | Apr 17 | 16d |
| ABS_BASELINE | 72 | 12 | Apr 16 | 17d |
| TRENDS | 39 | 7 | Apr 6 | 27d |

**Audit artifact:** `workbook/AUDIT_2026-05-02.md` — Items #1 / #2a / #2d / #2.5 resolution logs.

**BOARD_LOG:** synced 0 gap (verified PM2 boot, unchanged through PM4). Skip BOARD diff next session unless INDEX advances.

---

## URGENT

- **Cluster 2 + 3 outstanding** — Cross-agent stale rows + FOMC May 6-7 missing from DANGER WINDOW.
- **HY OAS still stale 23d** — FRED + 4 secondaries blocked May 3; needs alternative fetch path.
- **AAA pump Mon May 4** — first weekday post-Brent-pullback; resolves CRL-08 timing distribution.
- **CRL-19 resolved MIXED** — 2nd direction-correct/magnitude-low (CRL-01 pattern); calibration question for v2.5.1 Brier audit.
