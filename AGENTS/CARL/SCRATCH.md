# CARL SCRATCH
**Last session:** 2026-05-02 ~14:00–18:00 UTC (Will-driven workbook restructure THEN workbook hardening Item #1: schema audit + expansion)
**Type:** Workbook architecture — schema hardening, multi-item plan

**PRIORITY-1:** **Workbook hardening Item #2 — KB.tsv fix pass.** Migrate 44 `Status='DELEGATED TO HOMER'` rows to new `Delegated_To` column; fix 5 column-bleed rows (KB-215..219, `CONFIRMED` in Epistemic col); fix 5 column-count anomalies (KB-075/077/254-256, paste-with-trailing-tab); fix 2 empty-Status framework rows (KB-001/002); fix 1 terminal-state hygiene (KB-029); reclassify 27 stale-ACTIVE rows. ~84 of the 87 audit issues clear in this pass. ~45 min, context-heavy. Full audit at `workbook/AUDIT_2026-05-02.md`.

---

## WHAT HAPPENED

1. **Boot clean** — pulled, BOARD diff-clean (98/98), inbox empty, outbox holds 6 Apr 17 signals (deferred per messaging-overhaul).
2. **Will dropped** `User Input/Carl Workbook convo.md` — transcript of external-LLM audit of CARL's workbook. Flagged schema violations + ML.tsv legacy concern + recommended Delegated_To/Last_Refreshed/validator/INDEX additions.
3. **CARL response to external audit** — confirmed most flags, pushed back on framing of "logical inconsistency" / "ML.tsv duplication", agreed on architectural fixes, answered 4 direct questions + the orientation-sequence question.
4. **Full programmatic audit** (`/tmp/audit_kb.py` against SCHEMA.tsv): **87 issues** in KB.tsv across 8 categories. Bigger finding: 5 of 9 other workbook TSVs have severe row-level col-count drift (BNPL_STRESS 93%, TRENDS 90%, STATE_DIFFUSION 77%, ABS_BASELINE 51%; VX/FLOW clean) — non-KB TSVs have no formal schema in SCHEMA.tsv at all.
5. **Audit report written** to `workbook/AUDIT_2026-05-02.md` — 4 sections (top-line, KB row-by-row, other TSVs, architectural recommendations) + recommended sequencing (Items #1-6).
6. **Item #1 executed atomically:**
   - SCHEMA.tsv: 13 → 15 column definitions (`Last_Refreshed` Date-optional + `Delegated_To` sub-agent-name-optional)
   - KB.tsv header: 2 new column names appended
   - KB.tsv data: 260 rows expanded with empty trailing cells (`\t\t`)
   - CARL `CLAUDE.md`: KB.tsv description "13-column schema" → "15-column schema" with reference to AUDIT file
   - Audit re-run: 87 issues unchanged, **0 new violations introduced**
   - Backup: `/tmp/KB.tsv.bak_1777742976`
7. **ROADMAP updated** — added Workbook hardening as new OPEN THREAD with full Items #1-6 description; ML.tsv question marked resolved (scheduled in Item #4); added RECENTLY RESOLVED entry for today's work.
8. **Choice point:** Will elected to commit at the Item #1 checkpoint rather than continuing into Item #2 — schema decision is most consequential and worth peer-review before touching 84 rows.

## STATUS CHANGES
| Item | Change |
|------|--------|
| `workbook/SCHEMA.tsv` | 13 → **15 column definitions** (added `Last_Refreshed` + `Delegated_To`) |
| `workbook/KB.tsv` | header 13→15 cols; 260 data rows expanded with empty trailing cells |
| `CLAUDE.md` | KB.tsv reference: "13-column schema" → "15-column schema" + AUDIT file ref |
| `workbook/AUDIT_2026-05-02.md` | NEW — full programmatic audit, 87 issues, recommendations + sequencing |
| `ROADMAP.md` | +Workbook hardening OPEN THREAD; ML.tsv OPEN QUESTION resolved (→Item #4); +RECENTLY RESOLVED entry |
| KB.tsv issue count | 87 → 87 (Item #1 was non-data structural — issues clear in Item #2) |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **Workbook hardening Item #2** — KB.tsv fix pass. Largest single item by row count; ~84 of 87 audit issues clear. Suggest doing this in dedicated session given context cost. Source: `workbook/AUDIT_2026-05-02.md` §1 (full row lists per category).
2. **DAILY AAA pump refresh** — $4.50 breach watch, likely May 3-4. May 2 latest $4.433 (gap $0.067). Quick (~5 min). When breach holds 2+ weeks, mark CRL-08 CONFIRMED.
3. **Brent close monitoring** — sustainability test ($107+ vs collapse on Iran de-escalation). Iran WPR deadline May 1 expired without resolution.

### UPCOMING (this week)
4. **Workbook hardening Item #3** — promote `/tmp/audit_kb.py` → `workbook/tools/validate.py`; add to spawn protocol step 0.5 (between `git pull` and SCRATCH read). ~45 min.
5. **Workbook hardening Item #4** — archive ML.tsv → `archive/legacy_workbook/`; update CLAUDE.md to remove ML reference. Trivial (~10 min).
6. **May 5** — PayPal Q1 (PHAN spawn) — first under new CEO Lores. Apply masking framework decompose.
7. **May 6** — Uber Q1 + DoorDash Q1 (GIG) — driver count QoQ post-gas.
8. **May 6** — BLS state jobs March (FL labor extension test).
9. **May 7 TRIPLE** — Dave Q1 (28DPD GIG-P01) + Lyft Q1 + Affirm Q3 FY2026.
10. **May 7** — EIA weekly inventory print — distillate (KB-253 follow-up) + gasoline stocks.

### UPCOMING (next 2 weeks)
11. **May 8** — BLS Apr NFP — V16 Employment Structural Rot first realized print.
12. **~May 18** — Klarna Q1 2026 (PHAN — first full quarter post-FY-loss).
13. **~Mid-May** — NY Fed Q1 2026 HHDC — CARL CORE — CC 90+ DQ vs 12.7%; tests CRL-05.
14. **May 28** — BEA Q1 GDP second estimate — CRL-18 resolves.
15. **~May 30** — March monthly Core PCE — CRL-19 resolves.
16. **Workbook hardening Item #5** — extend SCHEMA.tsv to other workbook TSVs (BNPL_STRESS, STATE_DIFFUSION, ABS_BASELINE, TRENDS, VX, FLOW) + fix row-level drift. Big job; deferred.

### v2.5.1 HARDENING (queued, no fixed dates — same as May 1)
17. UMich triangulation — TIPS 5y5y / SPF / NY Fed 3yr against UMich 5-10Y 3.5%.
18. Foreclosure 2019 absolute baseline — ATTOM Q1 2019 REO completions.
19. Path C counterfactual — pull COF/SYF Q1'24/'25 ACL builds; promote provisional → firm OR downgrade.
20. Crying-wolf X-threshold operational doc.
21. Brier audit full prediction history — CRL-01 through CRL-21 + legacy.
22. CONTAINMENT prior-calibration audit — joint CARL-RED.
23. COF/SYF candor puzzle — RED handoff.
24. Trade Duration roll plan — FORGE/REGINALD coord on KRE/WAL Dec 2026 → Q1-Q2 2027.
25. RED-CARL interface protocol — handshake document.

### BACKLOG (no deadline)
26. **Workbook hardening Item #6** — workbook root `INDEX.md`. Low priority.
27. LABOR/GIG spawn for FL UI Wave 2 (KB-CARL-262 partial).
28. HOMER spawn for Case-Shiller Feb sub-market detail (KB-CARL-261 headline only).
29. Workbook content refresh — VX consumer rows / FLOW / STATE_DIFFUSION / BNPL_STRESS (15d stale; folds into Item #5).
30. ABS_BASELINE refresh — March 10-Ds (16d stale; EART terminal + AMCAR ~2mo + SDART ~7mo).
31. 6 outbox signals from Apr 17 — defer per messaging-overhaul.
32. Methodology preservation note — extract v2.5 calibration discipline from CHANGELOG into `thesis/METHODOLOGY.md` (external-LLM suggestion).

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

## WORKBOOK HEALTH (post Item #1)
| TSV | Rows | Cols | Last Modified | Note |
|-----|------|------|---------------|------|
| KB | 260 | **15** | **May 2 PM** | Item #1 expansion; 87 audit issues queued for Item #2 |
| VX | 111 | 11 | May 2 | GAS-01 refreshed; clean col-counts (0 drift) |
| FLOW | 24 | 9 | Apr 17 | 15d — refresh due; clean col-counts (0 drift) |
| PREDICTIONS | 21 | — | May 1 PM2 | (canonical in `thesis/PREDICTIONS.tsv`) |
| STATE_DIFFUSION | 62 | 12 | Apr 17 | 15d; **77% col-count drift** — Item #5 target |
| BNPL_STRESS | 59 | 13 | Apr 17 | 15d; **93% col-count drift** — Item #5 target |
| ABS_BASELINE | 72 | 12 | Apr 16 | 16d; **51% col-count drift** — Item #5 target |
| TRENDS | 39 | 7 | Apr 6 | 26d; **90% col-count drift** — Item #5 target |
| ML | 66 | 9 | Apr 7 | 25d; **legacy** — Item #4 target (archive) |
| SCHEMA | 15 | 7 | **May 2 PM** | Item #1 expansion |

**Audit artifact:** `workbook/AUDIT_2026-05-02.md` — full 87-issue report + Items #1-6 sequencing.

BOARD_LOG: 105 lines, 98 dispositions, **diff-clean against INDEX as of May 1**.

---

## URGENT

- **Workbook hardening Item #2** — biggest single item, ~84 issues clear in one pass. Context-heavy; do in dedicated session.
- **AAA pump $4.50 breach watch** — daily refresh; breach likely May 3-4.
- **Iran cluster still live** — WPR deadline May 1 expired without resolution; Brent at $107-110 sustained.
- **Q3 2026 = CRL-21 first checkpoint** — ALLY consumer auto NCO ≥+30bps QoQ for 2 consecutive quarters OR vintage projections diverge above FY2023 ≥+50bps. **POSITION-ACTION COMMITMENT** if fails: confidence -25-30pp + trim 25% + extend duration to Q2 2027+.
