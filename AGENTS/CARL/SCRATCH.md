# CARL SCRATCH
**Last session:** 2026-05-02 PM4 ~22:00–23:30 UTC (Item #2.5 planning session — multi-agent peer review caught material errors in initial draft; full plan written to `workbook/ITEM_2.5_PLAN.md` for fresh-context execution)
**Type:** Workbook architecture — Item #2.5 planning + agent peer review integration

**PRIORITY-1:** **Execute `workbook/ITEM_2.5_PLAN.md` Session 1 — verification & disposition firming.** Self-contained plan; read it cold. Produces `workbook/ITEM_2.5_DISPOSITIONS.md` for Will review (zero TSV mutations in S1). Approval gate before Session 2 (apply pass). Live count revalidated in plan: **43 dangling VX IDs / 59 edges** across 4 naming generations. Methodology rule (verify-by-reading-target before bundling/redirecting) codifies during S1 step 1.0. ~60 min S1 + 45 min S2.

---

## WHAT HAPPENED (PM4 planning session)

1. **Will requested Item #2.5 plan-out before execution** (context-heavy — fresh window better).
2. **Initial plan drafted** with 6 CREATE / 4 REDIRECT / ~17 REMOVE rough categories, count "47 edges / 34 IDs" (regex artifact — terminal-digit-only pattern missed multitoken + decimal generations).
3. **External agent peer review** (`User Input/Two responses.md`) caught material errors:
   - Real count is **43 IDs / 59 edges** (re-verified live)
   - K-01 collapse risks topical-umbrella failure (KB-154 plasma + KB-111 retail flows can't share threshold) — same 2d failure mode
   - 3 REDIRECTs (RV-01, FF-01, AUTO-01) are topical-adjacency not vector-identity → likely REMOVE
   - 3 missed ABS-AUTO refs (KB-105/106/153 multitoken pattern)
   - SAV-01 should be 7th CREATE (KB-098 live STATUS metric)
   - MACRO-05 duplicate in VX.tsv folds into 2.5
   - Methodology rule (verify-by-reading-target) belongs in CLAUDE.md
4. **Re-validated live state** with comprehensive regex: 43 dangling IDs across 4 naming generations (1 DECIMAL + 1 OTHER + 34 STANDARD + 7 MULTITOKEN).
5. **Two-session plan written** to `workbook/ITEM_2.5_PLAN.md` (self-contained; agent feedback summarized in Appendix B; enumeration script in Appendix A).
6. **No TSV mutations this session.** Pure planning.

## PM4 OPENS (carry forward; plan supersedes ad-hoc tracking)
- Session 1 of plan to be executed in fresh context
- Methodology rule edit to CARL CLAUDE.md is S1 step 1.0
- Approval gate after Session 1 — Will reviews `ITEM_2.5_DISPOSITIONS.md` before S2

## WHAT HAPPENED (PM3 — historical context, retain for audit)

1. **Boot clean** — pulled (clean), BOARD diff surfaced ~40 INDEX entries not in BOARD_LOG (mostly grep noise from truncated narrative refs; SCRATCH said diff-clean as of May 1, real new signals look minor — flagged for triage but not done).
2. **Will requested Item #2d execution.** Initial plan: 32 stale-ACTIVE reclassifications via 8-cluster pass (A Iran/Oil, B Gas Pump, C GDPNow, D UMich, E Sweet, F HOMER, G HY OAS, H Singletons).
3. **Scope expansion #1 — misplacement audit.** Will caught KB-CARL-173 (OZK NCO data) as misplaced (REGINALD/OZK domain, not CARL). Expanded to broader scan of `Group=BANKING` + `Vectors=→PEER`. Found 4 confirmed misplacements (KB-172, 173, 203, 239) + 3 sub-agent-domain rows (KB-169 SBA, 202 servicer, 251 farm). KB-178 (JPM CC DQ) verified to STAY — fact is consumer-credit-card data even though source is a bank.
4. **Scope expansion #2 — REGINALD outbox handover.** Will requested misplaced rows be packaged for REGINALD delivery rather than just deleted. Wrote `outbox/SIG-CARL-REGINALD-20260502-misplaced-banking-rows-handover.md` for 3 REGINALD-domain rows (KB-172/173/203). KB-239 excluded (already routed via WALTER to RED per its own Notes — no new outbox needed).
5. **Scope expansion #3 — sub-agent physical move.** Will asked if POP/HOMER rows could move to their workbooks. Discovery: HOMER has KB.tsv with `CARL_ID` provenance column (designed for migration); POP only has ML.tsv (different 17-col schema, lossy translation). Decided: move only KB-CARL-202 → HOMER (Path A); leave KB-169, 251 in CARL with `Delegated_To=POP` until POP gets a KB.tsv (deferred).
6. **SUPERSEDED-by-pointer verification.** Initial cluster plan marked 22 rows SUPERSEDED. Verification by reading each proposed canonical-replacement row revealed only 7 actually carry forward the load-bearing content. **14 downgraded to STALE** — point-in-time historical with no canonical successor in KB.tsv. Lesson: cluster-pattern alone is unreliable for SUPERSEDED dispositions; verification step is required.
7. **Apply pass executed.** Script `/tmp/fix_kb_2d.py` with DISPOSITIONS dict (8 action types). 38 mutations across 38 unique rows. Bug caught in verification: Python list-by-reference passed KB-CARL-202's blanked Stale_By to KB-HMR-065 in HOMER; restored to 2026-05-15. Bonus catches: 2 pre-existing CONFIRMED-with-Stale_By hygiene violations (KB-001 future-dated 2026-03-15, KB-063 past-dated 2026-03-24) — out of original 2d scope but same §1.5 rule. Blanked.
8. **AUDIT log + ROADMAP updated** — Item #2d resolution log entry with per-cluster breakdown + lessons learned + sub-agent workbook architecture finding queued for next session.
9. **One-time direct delivery to REGINALD inbox** — Will authorized direct cross-agent write since no other Claude Code agents were active (HERMES still down per messaging-overhaul). Copied outbox signal → `AGENTS/REGINALD/inbox/`; moved CARL source → `outbox/delivered/`. Single commit (`50b87eb9`) with `CARL→REGINALD:` prefix for cross-boundary auditability. Cross-agent inbox writes saved as global memory note (`feedback_cross_agent_inbox_writes.md`) — exception is per-instance authorization only, do not generalize.

## STATUS CHANGES
| Item | Change |
|------|--------|
| `workbook/KB.tsv` | 38 row mutations (no row count change). Status distribution 260 ACTIVE / 7 CONFIRMED / 3 SUPERSEDED / 0 STALE → **217 ACTIVE / 9 CONFIRMED / 15 SUPERSEDED / 19 STALE.** |
| `workbook/KB.tsv` | Stale-ACTIVE: **32 → 0.** Terminal-state-with-Stale_By: **3 → 0.** Delegated_To: 44 HOMER → **44 HOMER + 2 POP.** All enums clean. |
| `sub_agents/HOMER/workbook/KB.tsv` | **64 → 65 rows** (KB-HMR-065 added with CARL_ID=KB-CARL-202 back-link, Stale_By 2026-05-15 preserved). |
| `outbox/delivered/SIG-CARL-REGINALD-20260502-misplaced-banking-rows-handover.md` | **DELIVERED** to REGINALD inbox via one-time direct write (commit `50b87eb9`). Source moved to delivered/ for audit trail. |
| `workbook/AUDIT_2026-05-02.md` | Item #2d resolution log entry added (per-cluster breakdown + bug + bonus catches + 3 backlog findings). 87 issues → **~4 remaining** (deliberate ID gaps only). |
| `ROADMAP.md` | Workbook hardening OPEN THREAD updated (Item #2d done; #2.5 / #3 / #4 + sub-agent workbook standardization remain OPEN). RECENTLY RESOLVED entry added. |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **Execute `workbook/ITEM_2.5_PLAN.md` Session 1** — verification & disposition firming. Self-contained plan; reads cold. Produces `workbook/ITEM_2.5_DISPOSITIONS.md` for Will review. Zero TSV mutations in S1. Approval gate before S2. Live count: 43 dangling IDs / 59 edges across 4 naming generations. ~60 min.
2. **DAILY AAA pump refresh** — $4.50 breach watch. May 2 latest $4.433 (gap $0.067). Likely breach May 3-4. When breach holds 2+ weeks, mark CRL-08 CONFIRMED.
3. **Brent close monitoring** — sustainability test ($107+ vs collapse on Iran de-escalation). Iran WPR May-1 deadline expired without resolution.

### UPCOMING (this week)
4. **Workbook hardening Item #3** — promote `/tmp/audit_kb.py` → `workbook/tools/validate.py`; add `#`-line skip + ref integrity check (KB→VX) + dynamic enum from SCHEMA.tsv. Add to spawn protocol step 0.5. ~45 min.
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
16. **Sub-agent workbook standardization (NEW from #2d)** — decide whether POP gets a KB.tsv mirroring HOMER's 12-col schema; if yes, migrate 44 existing HOMER-delegated rows + the 2 new POP-delegated rows physically.

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
29. Workbook content refresh — VX consumer rows / FLOW / STATE_DIFFUSION / BNPL_STRESS (15d stale).
30. ABS_BASELINE refresh — March 10-Ds (16d stale; EART terminal + AMCAR ~2mo + SDART ~7mo).
31. 6 outbox signals from Apr 17 — defer per messaging-overhaul.
32. Methodology preservation note — extract v2.5 calibration discipline from CHANGELOG into `thesis/METHODOLOGY.md` (external-LLM suggestion).

---

## OUTBOX (6 Apr 17 signals deferred per messaging-overhaul; May 2 signal already delivered)
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

## WORKBOOK HEALTH (post Item #2d)
| TSV | Rows | Cols | Last Modified | Note |
|-----|------|------|---------------|------|
| KB | 260 | 15 | **May 2 PM3** | Item #2d 38 mutations; **0 stale-ACTIVE, 0 enum violations, 0 hygiene violations**; AUDIT scope ~4 remaining (deliberate ID gaps only) |
| HOMER/KB | **65** | 12 | **May 2 PM3** | +1 row (KB-HMR-065 from KB-CARL-202 migration) |
| VX | 111 | 11 | May 2 | GAS-01 refreshed; clean col-counts (0 drift); **43 dangling KB→VX refs queued for Item #2.5** |
| FLOW | 24 | 9 | Apr 17 | 15d — refresh due; clean col-counts |
| PREDICTIONS | 21 | — | May 1 PM2 | (canonical in `thesis/PREDICTIONS.tsv`) |
| STATE_DIFFUSION | 62 | 12 | Apr 17 | 15d; non-KB drift artifactual per Convo 2 |
| BNPL_STRESS | 59 | 13 | Apr 17 | 15d; non-KB drift artifactual per Convo 2 |
| ABS_BASELINE | 72 | 12 | Apr 16 | 16d |
| TRENDS | 39 | 7 | Apr 6 | 26d |
| ML | 66 | 9 | Apr 7 | 25d; **legacy** — Item #4 target (archive) |
| SCHEMA | 15 | 7 | May 2 | Item #1 expansion (15 cols defined) |

**Audit artifact:** `workbook/AUDIT_2026-05-02.md` — full audit + Items #1 / #2a / #2d resolution logs + Items #2.5 / #3 / #4 + sub-agent workbook standardization queued.

BOARD_LOG: 105 lines, 98 dispositions. SCRATCH said diff-clean as of May 1; today's BOARD diff surfaced ~40 INDEX entries not in BOARD_LOG but mostly grep noise (truncated narrative refs from disposition entries) — real new signals look minor, deferred for triage.

---

## URGENT

- **Workbook hardening Item #2.5** — 43 dangling KB→VX refs. Context-heavy; dedicated session.
- **AAA pump $4.50 breach watch** — gap $0.067; breach likely May 3-4.
- **Iran cluster still live** — WPR deadline May 1 expired without resolution; Brent at $107-110 sustained.
