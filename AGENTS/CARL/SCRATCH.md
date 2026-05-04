# CARL SCRATCH
**Last session:** 2026-05-04 ~02:00 UTC (PM7)
**Type:** Workbook hardening pass — VX P1 (Status canonicalization + Delegated_To split + tombstone drops) + KB→VX dangle cleanup + SCHEMA Option A (Vectors-col formal multi-level expansion) + P4 (VX dedup) + closeout (CHANGELOG/ROADMAP/STATUS/SCRATCH)

**PRIORITY-1:** **AAA pump Mon May 4 refresh — first weekday post-Brent-pullback.** Brent -5.12% Friday May 2 close ($108.17) should transmit to pump softening Mon-Wed at 3-4d lag (KB-CARL-259 acute-regime). Two scenarios: (a) softening confirmed → CRL-08 timing widens beyond Tue May 5; (b) Brent re-fires → breach Tue/Wed, 2-week sustainability clock starts. Plus: HY OAS still stale 23d — needs alternative fetch path (FRED + 4 secondaries blocked PM4).

---

## WHAT HAPPENED (PM7 work — workbook hardening)

1. **Will requested VX.tsv audit** — produced 9-issue audit (schema, status enum overload, ID convention bifurcation, 23-row staleness, 10 PENDING orphans, 3 dups, V13 convergence-matrix coverage gap, threshold/status mismatch, 6 ID oddballs).
2. **Plan-mode P1 approval:** mirror KB Item #2a fix on VX. Added Delegated_To col (11→12); migrated 9 DELEGATED-TO-HOMER rows to threshold-color Status + Delegated_To=HOMER (per band-match + WORKBOOK DISCIPLINE [FLAG] for ambiguous 6.08 categorical + 2.02 range top); normalized 3 RED-BREACHED→RED + 1 YELLOW-borderline→YELLOW; updated 3 KB rows (KB-055/060/059) to remove tombstone refs BEFORE dropping 3 CONSOLIDATED VX tombstones (1.06/6.01/ABS-15) per discipline.
3. **Dangle cleanup byproduct:** post-P1 verify surfaced 5 pre-existing KB→VX dangles from PM4/PM5 sessions. Verified-by-reading-target before each rewrite. KB-271 RETAIL→6.10, KB-272 MORTG-RATE→HSG-01, KB-273 CB-EXPECT→SENT-02; KB-272 MBA-PURCH + KB-274 FOMC-RATE-PROXY blanked (no VX target exists).
4. **Will requested explanation of off-spec vs canonical refs.** Surfaced that 95 of 118 "off-spec" entries (Vector_N + CRL-NN) are doing real semantic work at thesis-vector + prediction levels respectively that pure VX-IDs can't replace. 3-level abstraction explained. Will chose **Option A — formalize multi-level system in SCHEMA**.
5. **SCHEMA.tsv expansion:** Vectors col `allowed_values` now formally recognizes `VX-{AGT}-NN, Vector_N, CRL-NN, FLOW-{AGT}-N.NN, {SUBAGT}-PNN, BRT-NN, →AGENT or empty`. Description expanded with KB-NNN restriction (DerivedFrom only).
6. **Truly-broken ref fixes (9 entries across 7 KB rows):** KB-031 (`STATE_DIFFUSION.tsv` filename dropped), KB-232/233/234 (5× `VX→AGENT` typos → `→AGENT`), KB-264/268 (KB-CARL-253 moved Vectors→DerivedFrom), KB-271 (`K-SHAPE` redundant tag dropped).
7. **P4 verification + execution:** verified-by-reading both dup pairs. Pair 1 (BNPL Late Rate) confirmed true dup — dropped 1.03 (stale orphan, 0 KB refs). Pair 2 (Medical) verification revealed NOT a clean dup — different metrics ($88-140B range w/ phantom debt vs $88B narrow CFPB) disagreeing on Status. Per WORKBOOK DISCIPLINE rule, chose Will-approved Option A: rename to expose distinction + cross-ref Notes. MED-01 → "Medical Collections (CFPB narrow)"; 1.08 → "Medical Debt Total (incl. phantom estimate)".
8. **Commit + push:** 3b47901f fast-forward clean. BRENT (3 changes incl. inbox-move) + SAM (1 change) concurrent uncommitted work untouched. Origin had not moved during session; no rebase needed.
9. **Closeout pass (this session cont.):** CHANGELOG PM7 entry + ROADMAP RECENTLY RESOLVED PM7 entry + ROADMAP timestamp + STATUS timestamp + this SCRATCH rewrite. Pending: closeout commit.

## STATUS CHANGES
| Item | Change |
|------|--------|
| `workbook/VX.tsv` | 120 → 116 rows; 11 → 12 cols (added Delegated_To); 9 status-enum off-spec → canonical; 3 tombstones removed; 1 dup dropped; 2 medical rows renamed |
| `workbook/KB.tsv` | 273 rows unchanged; 16 Vectors-col edits across 14 unique rows (3 P1 ref-rewrites + 4 dangle rewrites + 7 Option A truly-broken fixes); 2 rows moved KB-NNN refs Vectors→DerivedFrom |
| `workbook/SCHEMA.tsv` | Vectors col `allowed_values` formalized to multi-level ref system; description expanded |
| `ROADMAP.md` | +2 backlog adds (MBA Apps VX vector decision; CARL Status enum hardening); PM7 RECENTLY RESOLVED entry; timestamp |
| `thesis/CHANGELOG.md` | +PM7 entry (structural workbook work) |
| `STATUS.md` | timestamp bump only (signal data unchanged) |
| **Final integrity** | 0 col-count anomalies / 0 dangling KB→VX / 0 off-spec Vectors-col entries / Status enum {RED 42, ORANGE 36, GREEN 15, YELLOW 14, PENDING 10} / Delegated_To {empty 107, HOMER 9} |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **AAA pump Mon May 4 refresh** — first weekday post-Brent-pullback; CRL-08 timing.
2. **HY OAS refresh** — alternative fetch path (FRED API key, abs_monitor.py, Yahoo HYG ETF proxy, ICE BofA via Bloomberg-proxy).
3. **Brent close monitoring Mon May 4** — peace-proposal repricing hold or Hormuz re-fire?

### UPCOMING (this week)
4. **May 5** — PayPal Q1 (PHAN spawn).
5. **May 6** — Uber Q1 + DoorDash Q1; BLS state jobs March.
6. **May 7 TRIPLE** — Dave Q1 + Lyft Q1 + Affirm Q3 FY2026.
7. **May 7** — EIA weekly inventory (distillate / DSL-01).
8. **May 8** — BLS Apr NFP (V16 first realized print).

### UPCOMING (next 2 weeks)
9. **May 13** — BLS Apr CPI — first full Iran-shock + tariff month; **Food at Home decomposition** extract (deferred from PM6).
10. **~May 18** — Klarna Q1 (PHAN).
11. **~Mid-May** — NY Fed Q1 HHDC — **CRL-05 test**.
12. **May 28** — BEA GDP Q1 second estimate (CRL-18) + AFT/MOHELA conference.

### UPCOMING (next 6+ weeks)
13. **Jun 16-17** — **FOMC + SEP** — first dot-plot post Iran-shock; KB-274. V12 hawkish/dovish surprise window.

### v2.5.1 HARDENING (8 PENDING_VERIFY items)
14-22. UMich triangulation / Foreclosure 2019 baseline / Path C COF/SYF counterfactual / Crying-wolf X-thresholds / **Brier audit (now n=2 direction-right/magnitude-low pattern: CRL-01 + CRL-19)** / CONTAINMENT prior calibration / COF/SYF candor puzzle / Trade Duration roll plan / RED-CARL interface.

### Workbook hardening (PM7 byproduct)
23. **P2 — legacy ID retirement** (VX-CARL-1.01 vs CC-01 collision; broader 1.NN/6.NN ID convention sunset) — backlog item.
24. **MBA Apps VX vector decision** — KB-272 covers but no VX vector tracks. Create VX-CARL-MBA-APPS or accept informational-only.
25. **VX Status enum hardening (Item #5 sibling)** — VX schema not formal in SCHEMA.tsv; pairs with Item #3 validator promotion.
26. **Workbook hardening Item #3** (validator promotion) — `/tmp/audit_kb.py` → `workbook/tools/validate.py`; now feasible to add ref integrity check + VX schema check + dynamic enum from SCHEMA.
27. **Sub-agent workbook standardization** — POP KB.tsv decision (Item #2d follow-up; HOMER-style 12-col schema?).
28. **STUE/CLAUDE.md stale `VX-CARL-1.06: CONSOLIDATED` line** — flagged for Will, sub-agent doc edit.

### Grocery squeeze backlog (PM6 byproduct)
29. **DAP / NH3 / UAN specific prices** — find DTN/AgWeb-alternative fetch path; or use World Bank Pink Sheet monthly.
30. **USDA Crop Progress weekly extraction** — Cornell library blocked, NASS page-only; need PDF / CSV fetch path.
31. **US Drought Monitor data extraction** — droughtmonitor.unl.edu data tables blocked.
32. **Russia AN + Gulf fertilizer news scan** — Reuters/Bloomberg/Argus all blocked; need alternate intel path.
33. **BLS Food at Home decomposition** — defer to May 13 Apr CPI release.
34. **Heavy grocery squeeze session** — cattle/hogs/eggs/milk + grocery retail margins (WMT/KR/ACI) + ag labor (ICE/H-2A) + tariff-on-food + Farm Credit System DQ + land values.

### BACKLOG (no deadline)
35. HY OAS refresh path.
36. Workbook hardening Item #6 (root INDEX.md).
37. Supply-event sub-vector class.
38. Orphan-Claim Audit Byproduct.
39. LABOR/GIG spawn for FL UI Wave 2.
40. HOMER spawn for Case-Shiller Feb sub-market detail.
41. Workbook content refresh — VX consumer / FLOW / STATE_DIFFUSION / BNPL_STRESS (17-18d).
42. ABS_BASELINE refresh — March 10-Ds (18d).
43. POLLY refresh — 25d stale.
44. MARCO refresh ask.
45. 6 outbox signals from Apr 17 (deferred per messaging-overhaul).

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

## WORKBOOK HEALTH (post May 4 PM7 hardening)
| TSV | Rows | Cols | Last Modified | Note |
|-----|------|------|---------------|------|
| KB | 273 | 15 | **May 4 PM7** | 16 Vectors-col edits across 14 unique rows; 2 KB-NNN refs moved Vectors→DerivedFrom. 0 dangling KB→VX, all 521 refs SCHEMA-recognized. |
| VX | **116** | **12** | **May 4 PM7** | Was 120×11. +Delegated_To col; 9 DELEGATED migrations; 3 RED-BREACHED→RED; 1 YELLOW-borderline→YELLOW; 3 tombstones dropped; 1 dup dropped; 2 medical renamed. Status enum clean {RED 42 / ORANGE 36 / GREEN 15 / YELLOW 14 / PENDING 10}. |
| SCHEMA | 15 | 7 | **May 4 PM7** | Vectors-col allowed_values formalized to multi-level ref system. |
| PREDICTIONS | 24 | 10 | May 3 PM4 | Unchanged this session |
| THESIS.md | — | — | May 3 AM | Unchanged this session |
| CHANGELOG.md | — | — | **May 4 PM7** | +PM7 entry |
| ROADMAP.md | — | — | **May 4 PM7** | PM7 RECENTLY RESOLVED entry + 2 backlog adds + timestamp |
| STATUS.md | — | — | **May 4 PM7** | timestamp bump only (signal data unchanged) |
| HOMER/KB | 65 | 12 | May 2 PM3 | Unchanged |
| FLOW | 24 | 9 | Apr 17 | 18d — refresh due |
| STATE_DIFFUSION | 62 | 12 | Apr 17 | 18d |
| BNPL_STRESS | 59 | 13 | Apr 17 | 18d |
| ABS_BASELINE | 72 | 12 | Apr 16 | 19d |
| TRENDS | 39 | 7 | Apr 6 | 29d |

**BOARD_LOG:** synced 0 gap (verified PM2 boot, unchanged through PM7).

---

## URGENT

- **AAA pump Mon May 4** — first weekday post-Brent-pullback. Disposition for CRL-08 timing.
- **HY OAS stale 23d** — FRED + 4 secondaries blocked PM4. Try alt path: FRED API key, abs_monitor.py, Yahoo HYG ETF proxy, ICE BofA via Bloomberg-proxy.
- **Russia AN ⚠️UNVERIFIED** — single news scan failed PM6. Retry alt sources (S&P Global Platts, ICIS, Argus alt-URL).

## SESSION FINDINGS WORTH CARRYING (informational, not urgent)

- **Multi-level ref system formalized** — KB Vectors col now legitimately holds VX-IDs (specific measurement) + Vector_N (thesis mechanism) + CRL-NN (prediction) + FLOW-IDs (transmission) + →AGENT (cross-agent). Future Brier audits + thesis reviews + prediction-resolution queries can run cleanly.
- **WORKBOOK DISCIPLINE rule validated again** — Pair 2 Medical "obvious dup" was NOT a dup; verify-by-reading caught the band-disagreement that pattern-matching missed. Same lesson as Item #2d.
- **CARL/STUE doc drift** — STUE/CLAUDE.md still references VX-CARL-1.06 (now-dropped tombstone). Sub-agent doc — flagged not edited per Critical Rule #2.
