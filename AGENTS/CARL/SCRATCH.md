# CARL SCRATCH
**Last session:** 2026-05-04 ~01:30 UTC (PM6)
**Type:** Grocery squeeze thread Light Mechanical Refresh — supply-side mechanism confirmed at primary-survey level

**PRIORITY-1:** **AAA pump Mon May 4 refresh — first weekday post-Brent-pullback.** Brent -5.12% Friday May 2 close ($108.17) should transmit to pump softening Mon-Wed at 3-4d lag (KB-CARL-259 acute-regime). Two scenarios: (a) softening confirmed → CRL-08 timing widens beyond Tue May 5; (b) Brent re-fires → breach Tue/Wed, 2-week sustainability clock starts. Plus: HY OAS still stale 23d — needs alternative fetch path (FRED + 4 secondaries blocked PM4).

---

## WHAT HAPPENED (PM6 work — grocery squeeze refresh)

1. **Will introduced new theme question:** rising grocery prices via farm bankruptcies + fertilizer trouble. Asked what we already have.
2. **KB inventory scan** surfaced existing thread: KB-076/080/110 fertilizer chain; KB-101 Russia AN; KB-120/121 USDA Plantings; KB-251 farm bankruptcies +46% YoY; VX-CARL-FOOD-01/02; CRL-10. Conclusion: significant coverage exists but stale 36+ days.
3. **Plan-mode pre-execution** with Will. Two paths offered (Light vs Heavy). Will chose Light + 2 small additions: (a) prior-price anchor for fertilizer, (b) Mar CPI Food at Home pull-forward test.
4. **Open Qs answered:** wheat/corn/soy only; try CPI this session; binary news scan for Russia/Gulf.
5. **Fetches (4 of 9 captured, ~45% success):**
   - ✅ Wheat $624.50 +23.18% YTD; Corn $468.25 +6.36% YTD; Soy $1,187.75 +15.26% YTD (tradingeconomics May 3)
   - ✅ Urea $585/T May 1 (-14.91% MoM, +24.40% YoY) — triangulated $475 baseline → $690s peak → $585 May 1
   - ✅ **AFBF Farm Bureau Fertilizer Survey Apr 14 (5,700+ farmers Apr 3-11)** — primary-source, BIG: 70% can't afford full fertilizer; urea +47% Feb→Mar peak (largest monthly recorded); ~60% worsening finances; pre-booking Midwest 67% / NE 30% / W 31% / S 19%
   - ✅ Food CPI 2.7% Mar 2026 (DECEL from Feb 3.1%) — pull-forward DISPROVEN; lag intact
   - ❌ USDA Crop Progress / WASDE (page-only / timeout)
   - ❌ DAP / NH3 specific (DTN/AgWeb 403/404)
   - ❌ US Drought Monitor (data tables blocked)
   - ❌ Russia AN / Gulf fertilizer news scan (all sources blocked — leave SUSPENDED ⚠️UNVERIFIED)
   - ❌ BLS Food at Home decomposition (cpi.t02.htm 403 — defer to May 13 Apr CPI release)
6. **Pull-forward test disposition (per Will Q2):** Mar Food CPI 2.7% DECELERATED from Feb 3.1% — therefore NO pull-forward; CRL-10 timeline holds with original Q4 2026 timeframe. Supply-side mechanism stronger than prior modeling (AFBF 70%-can't-afford finding) but consumer transmission still on lag.
7. **Synthesis: supply-side mechanism FULLY LOADED.** (a) Input shock peaked late Mar, partially retracing; (b) 70% behavioral can't-afford = under-application + crop mix shift; (c) plantings LOCKED for 2026/27 (wheat 107-yr low, corn -3.5%); (d) 2026/27 harvest output reduced from BOTH acres-down AND yield-per-acre-down; (e) wheat futures +23% YTD = market pricing 6-9mo forward tightness; (f) realized food CPI 2.7% Mar = transmission window Q3-Q4 2026 / Q1 2027 still intact.
8. **KB additions (3, Python append, schema-clean 15-col):**
   - KB-CARL-275: AFBF Survey Apr 14 (5,700 farmers, 70% can't afford, urea +47% peak)
   - KB-CARL-276: Fert/grain May 3 refresh (urea $585, wheat futures +23% YTD, triangulated price path)
   - KB-CARL-277: Mar Food CPI 2.7% lag confirmation
9. **VX updates (3 in place):** FOOD-01 (urea $585 + behavioral note), FOOD-02 (transmission lag confirmed Q3-Q4), AG-01 (AFBF forward signal note).
10. **STATUS edits:** +3 new rows (AFBF Survey, CBOT Wheat Futures, Food CPI Headline); +4 row refreshes (Urea cash $585, Russia AN ⚠️UNVERIFIED, Wheat/Corn "locked in"); 239→242 lines.
11. **CRL-10 disposition:** holds 70% confidence; timeline Q4 2026 INTACT; supply-side evidence strengthened (AFBF survey was not in original modeling).
12. **Commit + push pending.**

## STATUS CHANGES
| Item | Change |
|------|--------|
| `workbook/KB.tsv` | 271 → 274 (+KB-275 AFBF / +KB-276 Fert+Grain / +KB-277 Food CPI lag) |
| `workbook/VX.tsv` | 3 in-place: FOOD-01 ($585 + AFBF behavioral), FOOD-02 (lag confirmed), AG-01 (forward signal) |
| `STATUS.md` | +3 new rows, +4 refreshes; 239 → 242 lines |
| Vector #5 / #8 / #12 | Reinforced via grocery squeeze thread — supply-side fully loaded, transmission pending |
| CRL-10 | Holds 70%; timeline INTACT; supply-side stronger than modeled |
| Russia AN | Status unverified post-Mar 24 — flag ⚠️ |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **AAA pump Mon May 4 refresh** — first weekday post-Brent-pullback; CRL-08 timing.
2. **HY OAS refresh** — alternative fetch path (FRED API, abs_monitor.py, Yahoo HYG ETF proxy).
3. **Brent close monitoring Mon May 4** — peace-proposal repricing hold or Hormuz re-fire?

### UPCOMING (this week)
4. **May 5** — PayPal Q1 (PHAN spawn).
5. **May 6** — Uber Q1 + DoorDash Q1; BLS state jobs March.
6. **May 7 TRIPLE** — Dave Q1 + Lyft Q1 + Affirm Q3 FY2026.
7. **May 7** — EIA weekly inventory (distillate / DSL-01).
8. **May 8** — BLS Apr NFP (V16 first realized print).

### UPCOMING (next 2 weeks)
9. **May 13** — BLS Apr CPI — first full Iran-shock + tariff month; **NEW: extract Food at Home decomposition** (deferred from PM6).
10. **~May 18** — Klarna Q1 (PHAN).
11. **~Mid-May** — NY Fed Q1 HHDC — **CRL-05 test**.
12. **May 28** — BEA GDP Q1 second estimate (CRL-18) + AFT/MOHELA conference.

### UPCOMING (next 6+ weeks)
13. **Jun 16-17** — **FOMC + SEP** — first dot-plot post Iran-shock; KB-274. V12 hawkish/dovish surprise window.

### v2.5.1 HARDENING (8 PENDING_VERIFY items)
14-22. UMich triangulation / Foreclosure 2019 baseline / Path C COF/SYF counterfactual / Crying-wolf X-thresholds / **Brier audit (now n=2 direction-right/magnitude-low pattern: CRL-01 + CRL-19)** / CONTAINMENT prior calibration / COF/SYF candor puzzle / Trade Duration roll plan / RED-CARL interface.

### Grocery squeeze backlog (PM6 byproduct)
23. **DAP / NH3 / UAN specific prices** — find DTN/AgWeb-alternative fetch path; or use World Bank Pink Sheet monthly.
24. **USDA Crop Progress weekly extraction** — Cornell library blocked, NASS page-only; need PDF / CSV fetch path.
25. **US Drought Monitor data extraction** — droughtmonitor.unl.edu data tables blocked.
26. **Russia AN + Gulf fertilizer news scan** — Reuters/Bloomberg/Argus all blocked; need alternate intel path.
27. **BLS Food at Home decomposition** — defer to May 13 Apr CPI release.
28. **Heavy grocery squeeze session** — cattle/hogs/eggs/milk + grocery retail margins (WMT/KR/ACI) + ag labor (ICE/H-2A) + tariff-on-food + Farm Credit System DQ + land values.

### BACKLOG (no deadline)
29. HY OAS refresh path.
30. VX-CARL-FOMC-RATE vector (deferred per Will — STATUS-only).
31. Workbook hardening Item #3 (validator promotion).
32. Sub-agent workbook standardization (POP KB.tsv).
33. Workbook hardening Item #6 (root INDEX.md).
34. Supply-event sub-vector class.
35. Orphan-Claim Audit Byproduct.
36. LABOR/GIG spawn for FL UI Wave 2.
37. HOMER spawn for Case-Shiller Feb sub-market detail.
38. Workbook content refresh — VX consumer / FLOW / STATE_DIFFUSION / BNPL_STRESS (16-17d).
39. ABS_BASELINE refresh — March 10-Ds (17d).
40. POLLY refresh — 24d stale.
41. MARCO refresh ask.
42. 6 outbox signals from Apr 17 (deferred per messaging-overhaul).

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

## WORKBOOK HEALTH (post May 4 PM6 refresh)
| TSV | Rows | Cols | Last Modified | Note |
|-----|------|------|---------------|------|
| KB | **274** | 15 | **May 4 PM6** | +KB-CARL-275 (AFBF survey) + KB-CARL-276 (Fert/grain refresh) + KB-CARL-277 (Mar Food CPI lag); 0 dangling KB→VX refs preserved; 0 enum / hygiene / col-count violations |
| VX | 121 | 11 | **May 4 PM6** | 3 in-place updates: FOOD-01 ($585 + AFBF behavioral), FOOD-02 (lag confirmed), AG-01 (forward signal) |
| SCHEMA | 15 | 7 | May 2 PM | Unchanged |
| PREDICTIONS | 24 | 10 | May 3 PM4 | Unchanged this session |
| THESIS.md | — | — | May 3 AM | Unchanged this session |
| CHANGELOG.md | — | — | May 3 PM4 | Unchanged this session |
| ROADMAP.md | — | — | **May 4 PM6** | PM6 RECENTLY RESOLVED entry + timestamp |
| STATUS.md | — | — | **May 4 PM6** | 242 lines (was 239); +3 new rows + 4 refreshes |
| HOMER/KB | 65 | 12 | May 2 PM3 | Unchanged |
| FLOW | 24 | 9 | Apr 17 | 17d — refresh due |
| STATE_DIFFUSION | 62 | 12 | Apr 17 | 17d |
| BNPL_STRESS | 59 | 13 | Apr 17 | 17d |
| ABS_BASELINE | 72 | 12 | Apr 16 | 18d |
| TRENDS | 39 | 7 | Apr 6 | 28d |

**BOARD_LOG:** synced 0 gap (verified PM2 boot, unchanged through PM6).

---

## URGENT

- **AAA pump Mon May 4** — first weekday post-Brent-pullback. Disposition for CRL-08 timing.
- **HY OAS stale 23d** — FRED + 4 secondaries blocked PM4. Try alt path: FRED API key, abs_monitor.py, Yahoo HYG ETF proxy, ICE BofA via Bloomberg-proxy.
- **Russia AN ⚠️UNVERIFIED** — single news scan failed PM6. Retry alt sources (S&P Global Platts, ICIS, Argus alt-URL).

## SESSION FINDINGS WORTH CARRYING (informational, not urgent)

- **CRL-10 supply-side STRONGER than modeled** — AFBF 70%-can't-afford behavioral signal not in original modeling; Q4 2026 timeline INTACT.
- **Brier calibration n=2 pattern** — CRL-01 + CRL-19 both direction-right/magnitude-low; v2.5.1 hardening item #5 should examine systematic-over-magnitude question.
- **Vector #12 framing shift** — locked-passive → locked + hawkish-leaning (FOMC Apr 28-29 4-dissent pattern).
- **Wheat futures +23% YTD** = market pricing locked-in 2026/27 supply tightness 6-9mo ahead.
