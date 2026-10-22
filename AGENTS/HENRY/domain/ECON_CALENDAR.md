# Economic Release Calendar — HENRY's Watch

**Purpose:** Flag surprises vs consensus on release mornings. Translate to rate path → bank NIM → regional repricing.

**Action on release days:** log actual vs consensus vs prior in `STATUS.md` (Data Release Protocol, `CLAUDE.md`). Cross-agent threshold fires route as SIGNALS via WALTER.

**Window verified:** 2026-10-22 → 2026-11-25, rebuilt 2026-10-21 ~21:10 ET at the agency calendars (BLS October and November 2026 schedule lists, BEA news schedule, Census 2026 economic indicator calendar, Federal Reserve FOMC calendar). None of those pages carried a lapse-in-appropriations notice on 2026-10-21. **ISM dates are the standard pattern, NOT verified** (ismworld.org returned HTTP 503). Weekly claims are the standing Thursday pattern, not re-verified at DOL. **Rebuild this window before 2026-11-20**, or it is stale again. The Mar–Jul 2026 dated tables were removed in this rebuild; recover them with `git show c9cb177c9:AGENTS/HENRY/domain/ECON_CALENDAR.md` if you need history (that is the last commit before this rebuild).

**Standing context lives in `STATUS.md`, not here.** This file is the schedule only, so it cannot carry a stale regime read.

---

## NEXT 30 DAYS (all times ET)

| Date | Time | Release | Data for | Source | Why it matters to HENRY |
|------|------|---------|----------|--------|-------------------------|
| Thu Oct 22 | before open | **AAL Q3 results** (call 08:30) | Q3 | issuer | HEN-46 resolves (AAL adjusted EPS vs −$0.70 low end of guide) |
| Thu Oct 22 | 10:00 | LUV Q3 call | Q3 | issuer | HEN-46 context; results already printed 10/21 |
| Tue Oct 27 | 8:30 | Durable goods (advance) | Sep | Census | Capex orders; HEN-36 context |
| Tue Oct 27 | 10:00 | New home sales | Sep | Census | Rates transmission |
| **Tue–Wed Oct 27–28** | 14:00 Wed | **FOMC** (no SEP) | — | Fed | Rate decision; 10Y above 5% red line |
| **Thu Oct 29** | 8:30 | **GDP advance + Personal Income and Outlays (PCE)** | Q3 / Sep | BEA | Core PCE vs >0.3% hot line |
| **Fri Oct 30** | 8:30 | **Employment Cost Index** | Q3 | BLS | LABOR owns; last print on the current weighting basis |
| Mon Nov 2 | 10:00 | ISM Manufacturing | Oct | ISM (UNVERIFIED) | PMI <50/<48/<47; prices >75 red |
| Tue Nov 3 | 10:00 | JOLTS | Sep | BLS | LABOR owns |
| Wed Nov 4 | 8:30 | Trade balance | Sep | BEA | — |
| Wed Nov 4 | 10:00 | ISM Services | Oct | ISM (UNVERIFIED) | — |
| Thu Nov 5 | 8:30 | Productivity and Costs (prelim) | Q3 | BLS | Unit labor cost |
| **Fri Nov 6** | 8:30 | **Employment Situation (NFP)** | Oct | BLS | LABOR owns; HENRY logs market reaction |
| **Tue Nov 10** | 8:30 | **CPI** + Real Earnings | Oct | BLS | Headline vs core, energy share |
| Wed Nov 11 | — | Veterans Day, no BLS releases | — | BLS | — |
| **Fri Nov 13** | 8:30 | **PPI** | Oct | BLS | FD m/m >0.4/>0.5/>0.6 |
| Tue Nov 17 | 8:30 | Retail sales (advance) + Import/Export prices | Oct | Census / BLS | Consumer demand |
| Wed Nov 18 | 8:30 | Housing starts | Oct | Census | — |
| Fri Nov 20 | 10:00 | State employment | Oct | BLS | Florida read (CORAL/MARCO) |
| **Wed Nov 25** | 8:30 | **GDP second + corporate profits; Personal Income and Outlays (PCE)** | Q3 / Oct | BEA | Core PCE; profits |
| Wed Nov 25 | 8:30 / 10:00 | Durable goods; new home sales | Oct | Census | — |
| Thu Nov 26 | — | Thanksgiving, no releases | — | — | — |

**Beyond the window (verified):** FOMC **Dec 8–9 with SEP** (Fed). November CPI **Thu Dec 10** 8:30 (BLS December list). GDP third estimate **Dec 23** (BEA).

---

## Weekly (every Thursday 8:30 ET)
- **Initial jobless claims** — >250K sustained is LABOR's trigger. Pattern only; not re-verified at DOL 2026-10-21.

## ISM Release Pattern
- Manufacturing: 1st business day of month, 10:00 ET
- Services: 3rd business day of month, 10:00 ET

## Key Thresholds

| Indicator | Threshold | Implication |
|-----------|-----------|-------------|
| Core CPI MoM | >0.3% | Hot — rate cuts delayed |
| Core PCE MoM | >0.3% | Hot — Fed's own gauge |
| NFP | <100K | Labor cracking |
| ISM Mfg | <49 | Contraction confirmed |
| Claims | >250K sustained | LABOR trigger fired |
| ~~ECI QoQ~~ | ~~>1.2%~~ | **RETIRED 2026-08-06 as a dated record (Will-ruled 7/31, PROME rulings packet §3): cannot fire — private-wage q/q has sat in a 0.8-1.0 band for seven quarters (LABOR, BLS-primary). Any replacement is a NEW registration with base rates. BLS re-weights ECI from Dec-2026 data; 2026-10-30 is the last print on the current basis** |

The live STANDING bands (ISM, PPI, VIX, SPX, KRE, yields, HY/CCC) are in `STATUS.md` § ACTIVE THRESHOLDS; this table holds only the release-level surprise lines.
