# CARL SCRATCH
**Last session:** 2026-05-03 ~22:00 UTC (PM3)
**Type:** AAA pump refresh + Iran cluster update — CRL-08 disposition NEAR-BREACH NOT-YET

**PRIORITY-1:** **AAA pump Mon May 4 refresh — first weekday post-Brent-pullback.** Brent -5.12% Friday May 2 close ($108.17) should transmit to pump softening Mon-Wed at 3-4d lag (per KB-CARL-259 acute-regime model). Two scenarios: (a) softening confirmed → pump stabilizes $4.44-4.49 short of clean breach, CRL-08 timing widens beyond Tue May 5; (b) Brent re-firms + Memorial Day premium loads → breach Tue/Wed, 2-week sustainability clock starts. Decisive disposition for CRL-08 lands this week.

---

## WHAT HAPPENED

1. **Boot per spawn protocol** — git pull clean; read SCRATCH/STATUS/SCHEMA/TEAM/ROADMAP. Skipped BOARD diff per new conditional rule (INDEX mtime Apr 29 11:47 < BOARD_LOG last disposition Apr 29 19:51, 0 gap holds).
2. **Will requested readout of remaining work** — answered with breakdown: immediate (AAA + Iran), this week (May 5-8 catalysts), next 2 weeks (May 13-30), v2.5.1 hardening 8 items, workbook hardening Item #3 + sub-agent standardization, backlog.
3. **Plan-mode outline approved** — most-urgent first: AAA pump + Iran/Brent refresh.
4. **Live data fetch:** AAA pump $4.446 + diesel $5.642 (gasprices.aaa.com); Brent $108.17 + WTI $101.94 May 2 close (Investing.com); Iran cluster news May 1-3 (oilprice.com aggregation — Reuters/CNBC fetches failed).
5. **CRL-08 disposition NEAR-BREACH NOT-YET:** gap to $4.50 = $0.054, deceleration trio +9.2/+4.1/+1.3¢ (partial weekend), Brent -5% Fri counter-pressure. Held 92% per workbook discipline (no reprice without close ≥$4.50 + 2-week sustainability).
6. **KB additions** (Python append, schema-clean, 15-col):
   - KB-CARL-268: AAA pump May 3 (A1 — state list complete this fetch, May 2 parse anomaly resolved)
   - KB-CARL-269: Brent path May 2-3 (A2 — primary sources blocked, synthesized via Investing.com + oilprice.com)
7. **VX-CARL-GAS-01 updated:** Current_Value $4.433 → $4.446, Last_Updated → May 3, Source → KB-CARL-268, Notes refreshed (deceleration trio + state-list-complete + Brent counter-pressure + disposition).
8. **STATUS edits (8):** Updated timestamp; Gas Pump row (May 3 AAA + state list + NEAR-BREACH framing); Diesel row (single-digit moves both, distillate gap further compressing); Brent row (May 2 close $108.17 -5.12% on peace proposal); WTI row (spread WIDENED $6.23 mechanism finding); Iran Cluster row (bidirectional firing — peace proposal + Hormuz escort); DANGER WINDOW NOW row (May 3 disposition); Vector #5 row (NEAR-BREACH); CRL-08 prediction row (deceleration trio + counter-pressure context).
9. **ROADMAP update:** CRL-08 thread refreshed; PM3 RECENTLY RESOLVED entry added.
10. **Commit + push pending.**

## STATUS CHANGES
| Item | Change |
|------|--------|
| `workbook/KB.tsv` | 264 → 266 (+KB-CARL-268 AAA May 3 + KB-CARL-269 Brent May 2-3) |
| `workbook/VX.tsv` | VX-CARL-GAS-01 $4.433 → $4.446, May 2 → May 3, KB ref 264 → 268 |
| `STATUS.md` | 8 edits (Updated, Gas Pump, Diesel, Brent, WTI, Iran Cluster, DANGER WINDOW NOW, Vector #5, CRL-08 prediction); 237 lines (unchanged) |
| `ROADMAP.md` | CRL-08 thread last-touched May 1 → May 3 + PM3 RECENTLY RESOLVED entry |
| CRL-08 confidence | 92% HELD (NEAR-BREACH NOT-YET; reprice deferred until breach + 2-week sustainability) |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **AAA pump Mon May 4 refresh** — first weekday post-Brent-pullback; resolves whether 3-4d transmit lag softens pump or breach lands Tue/Wed.
2. **Brent close monitoring** — Sunday futures open + Mon May 4 cash close (does the peace-proposal repricing hold or does Hormuz escort blockade re-fire it?).

### UPCOMING (this week)
3. **May 5** — PayPal Q1 (PHAN spawn) — first under new CEO Lores.
4. **May 6** — Uber Q1 + DoorDash Q1 (GIG) — driver count QoQ post-gas.
5. **May 6** — BLS state jobs March (FL labor extension test — feeds FL-01 vector).
6. **May 7 TRIPLE** — Dave Q1 (28DPD GIG-P01) + Lyft Q1 + Affirm Q3 FY2026.
7. **May 7** — EIA weekly inventory print — distillate (KB-253 + DSL-01 follow-up).
8. **May 8** — BLS Apr NFP — V16 Employment Structural Rot first realized print.

### UPCOMING (next 2 weeks)
9. **May 13** — BLS Apr CPI — first print covering Iran-oil-shock + tariff pass-through full month; CRL-19 bridge confirms/disconfirms via core PCE proxy.
10. **~May 18** — Klarna Q1 2026 (PHAN — first full quarter post-FY-loss).
11. **~Mid-May** — NY Fed Q1 2026 HHDC — **CARL CORE — CC 90+ DQ vs 12.7%; tests CRL-05 + feeds CC-01 vector.**
12. **May 28** — BEA Q1 GDP second estimate — CRL-18 resolves.
13. **May 28** — AFT/MOHELA status conference (STUE).
14. **~May 30** — March monthly Core PCE — CRL-19 resolves.

### v2.5.1 HARDENING (8 PENDING_VERIFY items, item #10 ✅ DONE May 3 PM)
15. UMich triangulation (TIPS 5y5y / SPF / NY Fed 3yr against UMich 5-10Y 3.5%).
16. Foreclosure 2019 absolute baseline (ATTOM Q1 2019 REO completions).
17. Path C counterfactual (COF/SYF Q1'24/'25 ACL builds).
18. Crying-wolf X-threshold operational doc.
19. Brier audit full prediction history.
20. CONTAINMENT prior-calibration audit (joint CARL-RED).
21. COF/SYF candor puzzle (RED handoff).
22. Trade Duration roll plan (FORGE/REGINALD coord on KRE/WAL Dec 2026 → Q1-Q2 2027).
23. RED-CARL interface protocol.

### BACKLOG (no deadline)
24. **Workbook hardening Item #3** — promote `/tmp/audit_kb.py` → `workbook/tools/validate.py`; add `#`-line skip + KB→VX ref integrity check + dynamic enum from SCHEMA.tsv. Add to spawn protocol step 0.5. ~45 min.
25. **Sub-agent workbook standardization** — POP KB.tsv mirroring HOMER's 12-col schema (drives KB-169, KB-251 + future AG-01).
26. **Workbook hardening Item #6** — workbook root `INDEX.md`. Low priority.
27. **Supply-event sub-vector class** — Russia AN, Qatar LNG, Hormuz, China nitrogen halts as a class with binary/event threshold structure (Will accepted, deferred from Item #2.5).
28. **Orphan-Claim Audit Byproduct** — 7 KB rows where Status looks dependent on now-blanked dangling linkage (KB-013, 022, 017, 101, 102 + 2 already STALE).
29. LABOR/GIG spawn for FL UI Wave 2 (KB-CARL-262 partial).
30. HOMER spawn for Case-Shiller Feb sub-market detail (KB-CARL-261 headline only).
31. Workbook content refresh — VX consumer rows / FLOW / STATE_DIFFUSION / BNPL_STRESS (16-17d stale).
32. ABS_BASELINE refresh — March 10-Ds (17d stale).
33. **POLLY refresh** — 24d stale; ALL Q1 + BLS CPI captured PM2 as drive-by, full POLLY pass overdue.
34. 6 outbox signals from Apr 17 — defer per messaging-overhaul.

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

## WORKBOOK HEALTH (post May 3 PM3 refresh)
| TSV | Rows | Cols | Last Modified | Note |
|-----|------|------|---------------|------|
| KB | **266** | 15 | **May 3 PM3** | +KB-CARL-268 (AAA May 3) + KB-CARL-269 (Brent May 2-3) via Python append; 0 dangling KB→VX refs preserved; 0 enum / hygiene / col-count violations |
| VX | 120 | 11 | **May 3 PM3** | VX-CARL-GAS-01 row updated (Current_Value $4.433 → $4.446) |
| SCHEMA | 15 | 7 | May 2 PM | Unchanged |
| PREDICTIONS | 24 | 10 | May 3 AM | Unchanged this session (CRL-08 reprice deferred per discipline; Notes update only in STATUS) |
| THESIS.md | — | — | May 3 AM | Unchanged this session |
| CHANGELOG.md | — | — | May 3 AM | Unchanged this session |
| ROADMAP.md | — | — | **May 3 PM3** | CRL-08 thread last-touched May 1 → May 3 + PM3 RECENTLY RESOLVED entry |
| STATUS.md | — | — | **May 3 PM3** | 237 lines (unchanged); 8 edits (Updated, gas, diesel, Brent, WTI, Iran, DW NOW, V5, CRL-08) |
| HOMER/KB | 65 | 12 | May 2 PM3 | Unchanged this session |
| FLOW | 24 | 9 | Apr 17 | 16d — refresh due |
| STATE_DIFFUSION | 62 | 12 | Apr 17 | 16d |
| BNPL_STRESS | 59 | 13 | Apr 17 | 16d |
| ABS_BASELINE | 72 | 12 | Apr 16 | 17d |
| TRENDS | 39 | 7 | Apr 6 | 27d |

**Audit artifact:** `workbook/AUDIT_2026-05-02.md` — full audit + Items #1 / #2a / #2d / #2.5 resolution logs.

**BOARD_LOG:** 105 lines, 98 dispositions. INDEX↔BOARD-LOG synced 0 gap (verified May 3 PM2 boot, unchanged PM3). Per CLAUDE.md 3c, skip BOARD diff next session unless INDEX mtime advances.

---

## URGENT

- **AAA pump Mon May 4 refresh** — first weekday post-Brent-pullback; resolves CRL-08 timing distribution.
- **Iran cluster bidirectional** — peace proposal vs Hormuz escort blockade firing simultaneously; Brent path Mon close decisive.
- **CRL-08 2-week sustainability clock** — starts on first close ≥$4.50; not yet running.
