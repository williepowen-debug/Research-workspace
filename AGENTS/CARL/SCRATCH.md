# CARL SCRATCH
**Last session:** 2026-05-04 ~00:30 UTC (PM5)
**Type:** STATUS staleness audit Clusters 2+3 — Cross-Agent dedup + FOMC refresh + DANGER WINDOW rebuild

**PRIORITY-1:** **AAA pump Mon May 4 refresh — first weekday post-Brent-pullback.** Brent -5.12% Friday May 2 close ($108.17) should transmit to pump softening Mon-Wed at 3-4d lag (KB-CARL-259 acute-regime model). Two scenarios: (a) softening confirmed → pump stabilizes $4.44-4.49 short of clean breach, CRL-08 timing widens beyond Tue May 5; (b) Brent re-firms → breach Tue/Wed, 2-week sustainability clock starts. Decisive disposition for CRL-08 lands this week. Plus: HY OAS still stale 23d — needs alternative fetch path.

---

## WHAT HAPPENED

1. **Boot per spawn protocol** (PM4 boot earlier today).
2. **PM4 work:** Cluster 1 staleness refresh — KB-270/271/272/273 + 5 VX rows + 9 STATUS rows + CRL-19 RESOLVED MIXED. Commit 711efcb3.
3. **Cluster 2+3 plan-mode** — Will requested planning with sources / decisions / open questions before execution.
4. **Plan recon:** Read HAWK/BRENT/MARCO STATUS files (HAWK 13d stale, BRENT 3d, MARCO 10d, no AGENTS/WAR/ — that row was BOARD-aggregated). Surfaced 3 of 4 cross-agent rows duplicative w/ Macro section. Plan + decisions presented.
5. **Decisions per Will:** drop HAWK/BRENT + WAR rows; web-fetch FOMC; hold MARCO mirror; age out >30d Recently Fired; no VX-CARL-FOMC-RATE creation (STATUS-only).
6. **FOMC web fetch** (Federal Reserve calendar + tradingeconomics): **Course-correction surfaced** — initial plan assumed FOMC May 6-7 imminent; verified NO May meeting. Last meeting Apr 28-29 (held 3.50-3.75%, 3rd consec); **4 dissents most since Oct 1992** (Miran -25bps + 3 hawkish-leaning objections); Fed signaling openness to **HIKES** if inflation persists; next Jun 16-17 with SEP (first dot-plot post Iran-shock).
7. **Cluster 2 STATUS edits:**
   - Removed HAWK/BRENT row (duplicative with Macro Brent/WTI/Gas/Iran rows)
   - Removed WAR row (duplicative with Macro Iran Cluster Resolution row)
   - Refreshed FOMC row Mar 19 → Apr 28-29 with 4-dissent narrative + Jun 16-17 SEP
   - LABOR row left alone (Apr 3, still current)
   - MARCO row left alone (no mirror per decision)
8. **Cluster 3 STATUS edits:**
   - Added Jun 16-17 FOMC + SEP row to DANGER WINDOW
   - Added May 6-8 (Uber/DoorDash/Dave/Lyft/Affirm/NFP) row
   - Added May 13 (BLS Apr CPI) row
   - Added Mid-May (NY Fed Q1 HHDC / CRL-05 test) row
   - Aged out Mar 24 FL UI Wave 1 from "Recently fired (last 30d)" (40d)
   - Added Apr 28-29 FOMC + Apr 30 BEA Mar + May 3 CRL-19 to "Recently fired"
9. **Workbook:** +KB-CARL-274 (FOMC Apr 28-29 + Jun 16-17 preview, A2 due to non-direct fetch).
10. **Vector #12 (Stagflation Trap / Fed Locked) REINFORCED:** was 'locked-passive', now 'locked + hawkish-leaning'. Path C bad news compounds — mortgage easing reversed, Fed not cutting, no rate relief.
11. **Updated timestamp:** May 3 ~23:30 UTC → May 4 ~00:30 UTC.
12. **Commit + push pending.**

## STATUS CHANGES
| Item | Change |
|------|--------|
| `STATUS.md` Cross-Agent Links section | 4 rows → 2 rows (removed HAWK/BRENT, WAR; refreshed FOMC; left LABOR + MARCO) |
| `STATUS.md` DANGER WINDOW | +4 forward catalysts (May 6-8, May 13, Mid-May, Jun 16-17 SEP); aged out Mar 24; +3 fired items (Apr 28-29 FOMC, Apr 30 BEA, May 3 CRL-19) |
| `STATUS.md` line count | 237 → 239 (+2 net) |
| `workbook/KB.tsv` | 270 → 271 (+KB-CARL-274 FOMC Apr 28-29) |
| Vector #12 framing | locked-passive → locked + hawkish-leaning (Apr 28-29 dissent pattern) |
| FOMC narrative | Mar 19 hold w/ 1 cut priced → Apr 28-29 hold w/ 4 dissents most since 1992 + openness to hikes if inflation persists |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **AAA pump Mon May 4 refresh** — first weekday post-Brent-pullback; resolves CRL-08 timing distribution.
2. **HY OAS refresh** — FRED + 4 secondaries blocked May 3; try FRED API key, abs_monitor.py, or Yahoo HYG ETF as proxy.
3. **Brent close monitoring Mon May 4** — does Iran peace-proposal repricing hold or does Hormuz escort blockade re-fire?

### UPCOMING (this week)
4. **May 5** — PayPal Q1 (PHAN spawn) — first under new CEO Lores.
5. **May 6** — Uber Q1 + DoorDash Q1 (GIG); BLS state jobs March (FL labor).
6. **May 7 TRIPLE** — Dave Q1 + Lyft Q1 + Affirm Q3 FY2026.
7. **May 7** — EIA weekly inventory (distillate / DSL-01).
8. **May 8** — BLS Apr NFP — V16 first realized print.

### UPCOMING (next 2 weeks)
9. **May 13** — BLS Apr CPI — first full Iran-shock + tariff month.
10. **~May 18** — Klarna Q1 (PHAN).
11. **~Mid-May** — NY Fed Q1 HHDC — **CARL CORE — CC 90+ DQ vs 12.7% / CRL-05 test**.
12. **May 28** — BEA GDP Q1 second estimate (CRL-18 resolves) + AFT/MOHELA conference.

### UPCOMING (next 6+ weeks)
13. **Jun 16-17** — **FOMC + SEP** — first dot-plot post Iran-shock + UMich un-anchoring; 4-dissent April pattern carries forward; KB-274. Hawkish surprise → V12 to 5/5; dovish surprise → V12 partial relief.

### v2.5.1 HARDENING (8 PENDING_VERIFY items)
14-22. UMich triangulation / Foreclosure 2019 baseline / Path C COF/SYF counterfactual / Crying-wolf X-thresholds / Brier audit / CONTAINMENT prior calibration / COF/SYF candor puzzle / Trade Duration roll plan / RED-CARL interface.

### CRL-19 calibration follow-up
23. Brier audit pattern check: CRL-01 + CRL-19 both direction-right/magnitude-low (n=2). Frame for v2.5.1 hardening item #5.

### BACKLOG (no deadline)
24. **HY OAS refresh path** — fetch tooling.
25. **VX-CARL-FOMC-RATE vector** — currently STATUS-only; consider creating to track Fed stance via dissent count + market-implied path (deferred per Will decision Cluster 2+3).
26. Workbook hardening Item #3 (validator promotion).
27. Sub-agent workbook standardization (POP KB.tsv).
28. Workbook hardening Item #6 (root INDEX.md).
29. Supply-event sub-vector class.
30. Orphan-Claim Audit Byproduct.
31. LABOR/GIG spawn for FL UI Wave 2.
32. HOMER spawn for Case-Shiller Feb sub-market detail.
33. Workbook content refresh — VX consumer / FLOW / STATE_DIFFUSION / BNPL_STRESS (16-17d stale).
34. ABS_BASELINE refresh — March 10-Ds (17d).
35. **POLLY refresh** — 24d stale.
36. **MARCO refresh ask** — Will decided to hold off mirror this session; if MARCO STATUS Apr 23 information becomes stale-blocking for STATUS, surface to Will.
37. 6 outbox signals from Apr 17 (deferred per messaging-overhaul).

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

## WORKBOOK HEALTH (post May 4 PM5 refresh)
| TSV | Rows | Cols | Last Modified | Note |
|-----|------|------|---------------|------|
| KB | **271** | 15 | **May 4 PM5** | +KB-CARL-274 (FOMC Apr 28-29 + Jun 16-17 preview); 0 dangling KB→VX refs preserved; 0 enum / hygiene / col-count violations |
| VX | 121 | 11 | May 3 PM4 | Unchanged this session (FOMC rate not added per Will decision — STATUS-only) |
| SCHEMA | 15 | 7 | May 2 PM | Unchanged |
| PREDICTIONS | 24 | 10 | May 3 PM4 | Unchanged this session |
| THESIS.md | — | — | May 3 AM | Unchanged this session |
| CHANGELOG.md | — | — | May 3 PM4 | Unchanged this session |
| ROADMAP.md | — | — | **May 4 PM5** | PM5 RECENTLY RESOLVED entry + timestamp |
| STATUS.md | — | — | **May 4 PM5** | 239 lines (was 237); 5 row edits + 2 row removes + 4 row adds in DANGER WINDOW + Cross-Agent Links |
| HOMER/KB | 65 | 12 | May 2 PM3 | Unchanged |
| FLOW | 24 | 9 | Apr 17 | 17d — refresh due |
| STATE_DIFFUSION | 62 | 12 | Apr 17 | 17d |
| BNPL_STRESS | 59 | 13 | Apr 17 | 17d |
| ABS_BASELINE | 72 | 12 | Apr 16 | 18d |
| TRENDS | 39 | 7 | Apr 6 | 28d |

**Audit artifact:** `workbook/AUDIT_2026-05-02.md` — Items #1 / #2a / #2d / #2.5 resolution logs.

**BOARD_LOG:** synced 0 gap (verified PM2 boot, unchanged through PM5). Skip BOARD diff next session unless INDEX advances.

---

## URGENT

- **AAA pump Mon May 4** — first weekday post-Brent-pullback; CRL-08 timing distribution disposition.
- **HY OAS still stale 23d** — FRED + 4 secondaries blocked; needs alt fetch path.
- **FOMC Vector #12 reinforced** — locked + hawkish-leaning; Jun 16-17 SEP highest-leverage near-term V12 catalyst.
- **CRL-19 calibration warning** — 2nd direction-right/magnitude-low (CRL-01 pattern); flag for v2.5.1 Brier audit.
