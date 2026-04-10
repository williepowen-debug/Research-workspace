# CARL Sub-Agent Team

**Updated:** 2026-04-09

---

## ROSTER

| Agent | Domain | Status | Last Refresh | Next Catalyst | Stale? |
|-------|--------|--------|-------------|---------------|--------|
| **STUE** | Student loans (DQ, default, SAVE/RAP, servicers) | 🟢 BUILT | **Apr 10** | Sweet v McMahon Apr 15 (5 days), SAVE transition Jul 1, SAVE end Sep 30 | ✅ Current |
| **HOMER** | Housing (foreclosures, MF DQ, builders, state-level) | 🟢 BUILT | Apr 7 | MBA Q1 NDS (~May), Fannie MF monthly | ⚠️ 2 days |
| **GIG** | Gig economy (oversupply, Dave 28DPD, gas squeeze, AV) | 🟢 BUILT | **Apr 9** | Dave Q1 earnings May 7-12 | ✅ Current |
| **PHAN** | Phantom debt / BNPL ($400B+ invisible, stacking, fintech cockroaches) | 🟢 BUILT | **Apr 9** | Affirm Q3 FY2026 ~May, CFPB 1033 ON HOLD | ✅ Current |
| **POLLY** | Insurance (P&C, FAIR plans, health, FL/CA, auto) | 🟢 BUILT | **Apr 9** | FL hurricane season Jun 1, ACA subsidy cliff | ✅ Current |
| **POP** | Small business (Ch.11, closures, owner guarantees, tariff transmission) | 🟢 BUILT | **Apr 9** | Tariff impact Apr-Oct peak; NFIB monthly; Census BFS monthly | ✅ Current |
| **DOC** | Healthcare costs (medical debt, OOP, care avoidance, GLP-1 cost shock) | 🟢 BUILT | **Apr 9** | CPI Mar data Apr 10, ACA enrollment May, KFF survey fall | ✅ Current |
| **META** | Methodology & architecture research | ⚪ SPECIAL | Apr 6 | N/A — not a monitoring agent | — |

**Team readiness:** 7/7 monitoring agents built. All operational.

---

## UPCOMING CATALYSTS (next 30 days)

| Date | Catalyst | Agent(s) | Spawn Type |
|------|----------|----------|------------|
| Apr 14 | JPM Q1 earnings — consumer credit commentary | CARL direct | EARNINGS WATCH |
| Apr 15 | Sweet v. McMahon non-Exhibit C notices deadline | STUE | DATA REFRESH |
| Apr 21 | SYF Q1 earnings — NCO >6%? CRL-12 test | CARL direct | EARNINGS WATCH |
| Apr 26 | FL UI Wave 2 peak | GIG, HOMER | DATA REFRESH |
| Apr 30 | ~~CFPB 1033 deadline~~ — **ON HOLD** (judge enjoined, CFPB reconsidering) | PHAN | MONITOR |
| May 7-12 | Dave Q1 earnings — 28DPD with gas squeeze | GIG | EARNINGS WATCH |
| ~May | Uber/Lyft Q1 — driver counts, gas impact | GIG | EARNINGS WATCH |
| ~May | MBA Q1 NDS — foreclosure pipeline update | HOMER | DATA REFRESH |
| ~May | Fannie MF DQ March/April — GFC breach test | HOMER | DATA REFRESH |
| Apr 10 | CPI March — medical care component | DOC | DATA REFRESH |
| ~Apr | NFIB Small Business Optimism March | POP | DATA REFRESH |
| ~May | Affirm Q3 FY2026 earnings | PHAN | EARNINGS WATCH |
| Jun 1 | FL hurricane season begins | POLLY, HOMER | MONITOR |
| ~May | KFF employer survey / ACA enrollment data | POLLY, DOC | DATA REFRESH |

---

## BUILDOUT STATUS

All 7 monitoring agents built as of Apr 9. No further buildouts needed.

| Agent | Built | Notes |
|-------|-------|-------|
| STUE | Apr 6 | Student loans — operational |
| HOMER | Apr 7 | Housing — operational |
| GIG | Apr 9 | Gig economy — full buildout with 3 domain TSVs |
| PHAN | Apr 9 | Phantom debt — full buildout with 3 domain TSVs |
| POLLY | Apr 9 | Insurance — full buildout with CARRIER + STATE_MARKET TSVs |
| POP | Apr 9 | Small business — full buildout with SECTOR + TARIFF TSVs |
| DOC | Apr 9 | Healthcare — full buildout with COST_DRIVER + COVERAGE TSVs |

---

## REFRESH RULES

- **Current:** Refreshed within last 3 trading days. No action needed.
- **Stale (3-7 days):** Refresh on next session if no higher priority.
- **Very stale (>7 days):** Mandatory refresh. Data unreliable.
- **Dormant:** Not operational. Cannot be spawned until built out.

**At session start, check this table. Spawn any BUILT agent that is stale AND has an upcoming catalyst.**
