# CARL SCRATCH
**Last session:** 2026-05-03 ~19:00 UTC (PM2)
**Type:** Boot review + STATUS hygiene + boot-protocol cleanup + KB-266/267 logged

**PRIORITY-1:** **AAA pump refresh — $4.50 breach probable.** May 2 latest $4.433 / gap $0.067. Sunday May 3 not refreshed this session (work was hygiene, not data). At weekly pace breach was forecast May 4-5 — likely ALREADY breached when next session boots. Disposition: confirm threshold cross + start 2-week sustainability test for CRL-08 CONFIRMED. If sustained 2+ weeks, consider Vector #5 thesis upgrade.

---

## WHAT HAPPENED

1. **Boot per spawn protocol** — read SCRATCH/STATUS/SCHEMA/TEAM/ROADMAP. Skipped step 3c BOARD diff (no movement since Apr 29 disposition pass).
2. **Boot file review** — Will asked for content audit of STATUS + boot sequence. Identified: (a) STATUS header bloat (~3 paragraphs of dense narrative), (b) staleness in dashboard rows, (c) Notes columns grown into mini-essays, (d) BOARD diff (step 3c) routinely skipped because nothing changes between sessions, (e) SCRATCH carried stale "~40 INDEX entries" claim that was already 0 (verified diff). Awkward step numbering 3b/3c/3d/8b cosmetic-but-vestigial.
3. **Boot-protocol fixes (CLAUDE.md):**
   - Step 3c BOARD diff made conditional with grep snippet — skip when INDEX hasn't moved since last `Date_Logged`. Self-suppressing rule replaces broken "always do it but routinely skipped."
   - Spawn protocol step numbering renumbered 3/3b/3c/3d/4/5/6/7/8/8b/9 → 3/4/5/6/7/8/9/10/11/12/13. FILES table ROADMAP refs updated (step 6 / step 12).
4. **STATUS content review** (with KB cross-verification) — confirmed all 25+ recent KB rows backing STATUS narrative exist; flagged 2 stale STATUS-only counter-signals (auto + homeowners insurance CPI) needing fresh data before delete/keep decision.
5. **Quick web fetch** (Will approved) — BLS Mar 2026 CPI insurance components + ALL Q1 2026 (released today). Auto CPI 0.8% YoY (confirms KB-CARL-233); tenants 7.4% YoY (new); ALL Q1 CR 82.0 turnaround + homeowners profit flip + POLLY-P05 confirmed.
6. **KB additions** (Python append, schema-clean):
   - KB-CARL-266: ALL Q1 2026 (CR 82.0, homeowners flip, POLLY-P05 confirmed)
   - KB-CARL-267: BLS Mar 2026 CPI insurance (motor 0.8% YoY, tenants 7.4% YoY)
7. **STATUS edits 1-16:**
   - Header 3-paragraph blob → 2 lines + CHANGELOG pointer
   - THESIS section v2.1 → v2.5.1 refresh; **counter-signals line DELETED** (architecturally — counter-evidence lives in handoff_RED/COUNTER_LOG.md per v2.5 stripping); +masking framework + K-shape Selection sibling refs
   - Q1 NIPA 5 rows → 2 (consolidated)
   - Notes-column trims: gas pump, diesel, Iran cluster, Brent, WTI, Qatar LNG, ALLY Q1, SYF, COF, DHI, PHM, Case-Shiller, Sweet, UMich, Non-Bank Servicer
   - **NEW Insurance/Healthcare section** between Housing and Macro: UNH/ELV moved out of MACRO + ALL Q1 (KB-266) + Auto/Tenants CPI (KB-267) + CA FAIR Plan (from KB-233) — 6 rows total
   - Danger Window 8 resolved rows → 1 "Recently fired (last 30d)" digest + chronological reorder + Apr 28 Rithm dedupe
   - PREDICTIONS +CRL-22 (insurer MLR 60%) +CRL-23 (FY27 builder GM 70%) mirror from PREDICTIONS.tsv
   - EXIT RULES "Next catalysts" forward-looking only; added missing (May 8 NFP, May 13 CPI, NY Fed Q1 HHDC)
8. **SCRATCH inline correction** — "~40 INDEX entries" stale claim → "INDEX↔BOARD-LOG synced 0 gap, verified May 3 PM2 boot. Per CLAUDE.md 3c, skip BOARD diff next session unless INDEX mtime advances."
9. **Commit + push** (34b0ede8) — CARL: STATUS hygiene pass + boot-protocol cleanup + KB-266/267.

## STATUS CHANGES
| Item | Change |
|------|--------|
| `CLAUDE.md` | Step 3c BOARD diff made conditional + spawn protocol step renumber 3b/c/d→4/5/6, 8b→12 + FILES table refs |
| `SCRATCH.md` | BOARD-LOG line corrected (this session, then re-written for next handoff) |
| `STATUS.md` | 16 edits, 105 lines touched, +52/-53. New Insurance/Healthcare section (6 rows). 239 → 237 lines but major character-count reduction within rows |
| `workbook/KB.tsv` | 261 → 263 (+KB-CARL-266 ALL Q1 + KB-CARL-267 BLS Mar CPI insurance) |
| THESIS counter-signals line | DELETED — counter-evidence lives in handoff_RED/COUNTER_LOG.md (per v2.5 architectural decision May 1) |
| BOARD diff cadence | Was: routinely skipped boot-mandatory rule. Now: conditional self-suppressing rule. Aligned with practice. |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **AAA pump refresh** — $4.50 breach probable by now. If breach confirmed, start 2-week sustainability watch for CRL-08 CONFIRMED.
2. **Brent close monitoring** — Iran cluster still live; sustainability test ($107+ vs collapse on de-escalation).

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

### v2.5.1 HARDENING (8 PENDING_VERIFY items, item #10 ✅ DONE last session)
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
33. **POLLY refresh** — 24d stale; ALL Q1 + BLS CPI captured this session as drive-by, but full POLLY pass overdue.
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

## WORKBOOK HEALTH (post hygiene pass)
| TSV | Rows | Cols | Last Modified | Note |
|-----|------|------|---------------|------|
| KB | **263** | 15 | **May 3 PM2** | +KB-CARL-266 (ALL Q1) + KB-CARL-267 (BLS Mar CPI insurance) via Python append; 0 dangling KB→VX refs preserved; 0 enum / hygiene / col-count violations |
| VX | 120 | 11 | May 3 AM | Unchanged this session |
| SCHEMA | 15 | 7 | May 2 PM | Unchanged this session |
| PREDICTIONS | 24 | 10 | May 3 AM | Unchanged this session (CRL-22/23 mirror added to STATUS only) |
| THESIS.md | — | — | May 3 AM | Unchanged this session |
| CHANGELOG.md | — | — | May 3 AM | Unchanged this session |
| ROADMAP.md | — | — | **May 3 PM2** | Refreshed end-of-session for STATUS hygiene + boot-protocol cleanup resolutions |
| STATUS.md | — | — | **May 3 PM2** | 239 → 237 lines; 16 edits; new Insurance/Healthcare section; counter-signals DELETED |
| HOMER/KB | 65 | 12 | May 2 PM3 | Unchanged this session |
| FLOW | 24 | 9 | Apr 17 | 16d — refresh due |
| STATE_DIFFUSION | 62 | 12 | Apr 17 | 16d |
| BNPL_STRESS | 59 | 13 | Apr 17 | 16d |
| ABS_BASELINE | 72 | 12 | Apr 16 | 17d |
| TRENDS | 39 | 7 | Apr 6 | 27d |

**Audit artifact:** `workbook/AUDIT_2026-05-02.md` — full audit + Items #1 / #2a / #2d / #2.5 resolution logs.

**BOARD_LOG:** 105 lines, 98 dispositions. INDEX↔BOARD-LOG synced 0 gap (verified May 3 PM2 boot). Per new CLAUDE.md 3c, skip BOARD diff next session unless INDEX mtime advances.

---

## URGENT

- **AAA pump $4.50 breach watch** — gap was $0.067 May 2; almost certainly breached by next session.
- **Iran cluster still live** — Brent $107-110 sustained; WPR May-1 deadline expired.
- **STATUS Brent/WTI rows show May 1 data** — need refresh on next session.
