# CARL SCRATCH
**Last session:** 2026-05-02 PM4 → 2026-05-03 (Item #2.5 two-session execution: planning yesterday PM, S1+S2 today)
**Type:** Workbook hardening — Item #2.5 KB→VX reference integrity (full execute)

**PRIORITY-1:** **DAILY AAA pump refresh — $4.50 breach watch.** May 2 latest $4.433 / gap $0.067 to CRL-08 threshold. Likely breach May 3-4. When breach holds 2+ weeks, mark CRL-08 CONFIRMED + consider Vector #5 thesis upgrade.

---

## WHAT HAPPENED (Item #2.5 full execution)

1. **S1 — Verification & disposition firming.** Re-validated count (43 IDs / 59 edges, exact match plan). KB-105/106/153 reviewer-flag check passed (multitoken bucket). Verify-by-reading on all 43 IDs (~55 KB rows read). Produced `workbook/ITEM_2.5_DISPOSITIONS.md` (review-ready, zero TSV mutations, 6 open questions surfaced).
2. **WORKBOOK DISCIPLINE rule codified to CLAUDE.md** (S1.0) — new section after OUTPUT RULES. Verify-by-reading-target rule + threshold-uncertainty `[FLAG]` convention + conservative ref-cleanup default. Standalone commit pending.
3. **Will reviewed dispositions:** Q1 (WEALTH-01 anchor) accepted Prime CC NCO (AXP/DFS proxy) with proposed Green/Yellow/Orange/Red bands. Q5 (supply-event sub-vector class) accepted as desired but deferred. Q2/Q3/Q4/Q6 default-resolved per dispositions doc.
4. **S2 — Apply pass via `/tmp/fix_kb_2.5.py`.** 9 VX CREATEs + 5 REDIRECTs + 46 ref-blanks across 44 unique KB rows + 1 VX dedupe (NFP MACRO-05 → MACRO-09) + 1 SCHEMA description fix.
5. **Verify-by-reading shifted plan in 4 places:** WEALTH-01 anchor changed (KB-091 watch-list anchor instead of KB-237/111 — neither fit prime-NCO threshold), K-01 trimmed (KB-091/157 dropped on threshold-fit verification), KB-099 → ABS-12 (same metric), KB-101 → REMOVE not REDIRECT-FOOD-01 (supply event ≠ price metric).
6. **Bug caught in apply:** KB-CARL-007 missed in initial REMOVE list (original enumeration showed `[2]: 007, 034` but only 034 was in dispositions). Patched in-flight before final verification. Re-run enumeration confirmed 0 dangling.
7. **Documentation:** AUDIT log Item #2.5 entry added. ROADMAP updated (Workbook hardening thread updated; 2 new INVESTIGATIONS BACKLOG entries: supply-event sub-vector class + Orphan-Claim Audit Byproduct; Item #2.5 entry in RECENTLY RESOLVED).

## STATUS CHANGES
| Item | Change |
|------|--------|
| `workbook/KB.tsv` | 46 ref mutations across 44 unique rows (38 ref-blanks + 5 REDIRECTs + 1 missed-row patch). Row count unchanged at 260. |
| `workbook/VX.tsv` | **+9 CREATEs** (CC-01, SAV-01, AG-01, DSL-01, K-01, WEALTH-01, FL-01, ABS-AUTO-CACC, ABS-AUTO-SPREAD). NFP MACRO-05 renamed → MACRO-09. PPI keeps MACRO-05. **Total VX rows 110 → 120.** |
| `workbook/SCHEMA.tsv` | Delegated_To description corrected (Status preserved, not SUPERSEDED — matches Item #2a executed rule). |
| `AGENTS/CARL/CLAUDE.md` | **WORKBOOK DISCIPLINE section added** (between OUTPUT RULES and DOMAIN SCOPE). Standalone commit pending. |
| `workbook/ITEM_2.5_DISPOSITIONS.md` | Created (S1 deliverable, audit-trail of decisions). |
| Dangling KB→VX refs | **59 edges / 43 IDs → 0 edges / 0 IDs.** |
| `workbook/AUDIT_2026-05-02.md` | Item #2.5 resolution log entry added. |
| `ROADMAP.md` | Workbook hardening thread updated. 2 new INVESTIGATIONS BACKLOG entries. Item #2.5 in RECENTLY RESOLVED. |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **DAILY AAA pump refresh** — $4.50 breach watch. Gap $0.067 May 2; likely breach May 3-4. When breach holds 2+ weeks, mark CRL-08 CONFIRMED.
2. **Brent close monitoring** — Iran cluster still live; sustainability test ($107+ vs collapse on de-escalation).
3. **WEALTH-01 anchor refresh** — Q2'26 AXP/DFS not until July. No-op until then unless Q1 numbers can be back-pulled now (low priority).

### UPCOMING (this week)
4. **Workbook hardening Item #3** — promote `/tmp/audit_kb.py` → `workbook/tools/validate.py`; add `#`-line skip + KB→VX ref integrity check + dynamic enum from SCHEMA.tsv. Add to spawn protocol step 0.5. ~45 min.
5. **Workbook hardening Item #4** — archive ML.tsv → `archive/legacy_workbook/`; update CLAUDE.md to remove ML reference. Trivial (~10 min).
6. **May 5** — PayPal Q1 (PHAN spawn) — first under new CEO Lores.
7. **May 6** — Uber Q1 + DoorDash Q1 (GIG) — driver count QoQ post-gas.
8. **May 6** — BLS state jobs March (FL labor extension test — feeds FL-01 vector).
9. **May 7 TRIPLE** — Dave Q1 (28DPD GIG-P01) + Lyft Q1 + Affirm Q3 FY2026.
10. **May 7** — EIA weekly inventory print — distillate (KB-253 + DSL-01 follow-up).

### UPCOMING (next 2 weeks)
11. **May 8** — BLS Apr NFP — V16 Employment Structural Rot first realized print.
12. **~May 18** — Klarna Q1 2026 (PHAN — first full quarter post-FY-loss).
13. **~Mid-May** — NY Fed Q1 2026 HHDC — CARL CORE — CC 90+ DQ vs 12.7%; tests CRL-05 + feeds CC-01 vector.
14. **May 28** — BEA Q1 GDP second estimate — CRL-18 resolves.
15. **~May 30** — March monthly Core PCE — CRL-19 resolves.
16. **Sub-agent workbook standardization** — decide whether POP gets a KB.tsv mirroring HOMER's 12-col schema (drives KB-169, KB-251 + future AG-01-domain rows).

### v2.5.1 HARDENING (queued, no fixed dates — same as May 1)
17. UMich triangulation (TIPS 5y5y / SPF / NY Fed 3yr against UMich 5-10Y 3.5%).
18. Foreclosure 2019 absolute baseline (ATTOM Q1 2019 REO completions).
19. Path C counterfactual (COF/SYF Q1'24/'25 ACL builds).
20. Crying-wolf X-threshold operational doc.
21. Brier audit full prediction history.
22. CONTAINMENT prior-calibration audit (joint CARL-RED).
23. COF/SYF candor puzzle (RED handoff).
24. Trade Duration roll plan (FORGE/REGINALD coord on KRE/WAL Dec 2026 → Q1-Q2 2027).
25. RED-CARL interface protocol.

### BACKLOG (no deadline)
26. **Workbook hardening Item #6** — workbook root `INDEX.md`. Low priority.
27. **Supply-event sub-vector class** (NEW from #2.5 / Q5) — investigate whether supply shocks (Russia AN, Qatar LNG, Hormuz, China nitrogen halts) get a class of vectors with binary/event threshold structure.
28. **Orphan-Claim Audit Byproduct** (NEW from #2.5 / Q6) — 7 KB rows surfaced where Status looks dependent on now-blanked dangling linkage (KB-013, 022, 017, 101, 102 + 2 already STALE).
29. LABOR/GIG spawn for FL UI Wave 2 (KB-CARL-262 partial).
30. HOMER spawn for Case-Shiller Feb sub-market detail (KB-CARL-261 headline only).
31. Workbook content refresh — VX consumer rows / FLOW / STATE_DIFFUSION / BNPL_STRESS (16d stale).
32. ABS_BASELINE refresh — March 10-Ds (17d stale).
33. 6 outbox signals from Apr 17 — defer per messaging-overhaul.

---

## OUTBOX (6 Apr 17 signals deferred per messaging-overhaul; no new signals this session)
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
| COUNTER_LOG.md | Running counter-evidence log |
| SOFT_LANDING.md | Competing hypothesis <5% |
| CONTAINMENT.md | Competing hypothesis 15-20% |
| COUNTER_EVIDENCE_FROM_THESIS.md | Stripped Counter-Evidence section + disposition rules + HY OAS reclassification note |

---

## WORKBOOK HEALTH (post Item #2.5)
| TSV | Rows | Cols | Last Modified | Note |
|-----|------|------|---------------|------|
| KB | 260 | 15 | **May 3** | Item #2.5 46 ref mutations / 44 rows; **0 dangling KB→VX refs** (was 59 edges / 43 IDs); 0 enum / hygiene / col-count violations |
| VX | **120** | 11 | **May 3** | +9 CREATEs (CC-01, SAV-01, AG-01, DSL-01, K-01, WEALTH-01, FL-01, ABS-AUTO-CACC, ABS-AUTO-SPREAD); MACRO-05 NFP → MACRO-09; PPI keeps MACRO-05 |
| SCHEMA | 15 | 7 | **May 3** | Delegated_To description corrected (Status preserved, not SUPERSEDED) |
| HOMER/KB | 65 | 12 | May 2 PM3 | Unchanged this session |
| FLOW | 24 | 9 | Apr 17 | 16d — refresh due |
| PREDICTIONS | 21 | — | May 1 PM2 | (canonical in `thesis/PREDICTIONS.tsv`) |
| STATE_DIFFUSION | 62 | 12 | Apr 17 | 16d |
| BNPL_STRESS | 59 | 13 | Apr 17 | 16d |
| ABS_BASELINE | 72 | 12 | Apr 16 | 17d |
| TRENDS | 39 | 7 | Apr 6 | 27d |
| ML | 66 | 9 | Apr 7 | 26d; **legacy** — Item #4 target (archive) |

**Audit artifact:** `workbook/AUDIT_2026-05-02.md` — full audit + Items #1 / #2a / #2d / #2.5 resolution logs + Items #3 / #4 + sub-agent workbook standardization queued.

BOARD_LOG: 105 lines, 98 dispositions. SCRATCH May 2 PM3 noted ~40 INDEX entries not in BOARD_LOG were mostly grep noise; deferred for triage.

---

## URGENT

- **AAA pump $4.50 breach watch** — gap $0.067; breach likely May 3-4.
- **Iran cluster still live** — Brent $107-110 sustained; WPR May-1 deadline expired.
- **Workbook hardening Item #3** — natural next step (validator promotion); short / contained.
