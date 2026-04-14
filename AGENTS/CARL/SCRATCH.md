# CARL SCRATCH
**Last session:** 2026-04-14 ~PM UTC
**Type:** Multi-thread session — scripts maintenance, KB migration, WALTER inbox processing, non-bank servicer research, ABS monitor expansion + SDART/EART/AMCAR drill-down

**PRIORITY-1:** Continue subprime auto ABS drill-down. Cure collapse pattern CONFIRMED across SDART + EART + AMCAR (DQ↓ while CNL↑). Next drill-downs pending — start with #2 CNL trigger proximity. See "IN-FLIGHT DRILL-DOWN" section below.

---

## WHAT HAPPENED
1. **Non-bank servicer research (AM)** — Identified material deterioration since Jul 2025 baseline. PennyMac FHA DQ 5.9→7.5% single quarter. GAO Feb report found 35% of non-banks have high debt, no stagflation stress test. MFS UK collapse template. Sent REGINALD signal on warehouse line exposure. KB-HMR-046→052 (7 entries) + KB-CARL-202, 203.
2. **KB Migration Chunk 1 DONE** — HOUSING → HOMER (44 entries delegated, HOMER KB 35→45). 4 cross-domain entries stayed in CARL (034 FHA, 058, 066, 140). HOMER CLAUDE.md updated for new workflow.
3. **WALTER inbox processed** — CPI Mar +3.28% YoY, UMich Apr 47.6 RECORD LOW (-11% MoM), 5-10Y inflation exp UN-ANCHORING at 3.4% (Fed red line). Added Vector #12 Stagflation Trap. Convergence 51/55 → **57/60 CRITICAL**. KB-CARL-204, 205, 206.
4. **ABS monitor expansion** — Added Exeter, Ally, GM Financial/AmeriCredit as tracked issuers. 4→6 issuers, 17 trusts. SoFi deliberately excluded (private/144A — no SEC 10-D path). DCENT removed (defeasance post-CapOne merger, DCMT filed 15-12G Dec 19 2025). Parser limitation documented in docstring.
5. **SoFi data gap caveat** — KB-CARL-078, VX-CARL-ABS-16, STATUS.md all flagged. Value is Mar 2026 snapshot, cannot refresh.
6. **SDART Feb 2026 data pulled** — 30+ DQ 21.64% (down 43bps), CNL 8.74% (UP 26bps). Losses accelerating faster than DQs = cure rate collapse at trust level. HAROT control flat at 1.22%. KB-CARL-207.
7. **COMET Feb 2026 baseline** — 30+ DQ 1.88%, annualized net default 2.47%, payment rate 43.23%. KB-CARL-209.
8. **Discover deregistration finding** — DCMT 15-12G Dec 19 2025, DCENT in defeasance. Discover rolls into COMET. KB-CARL-208.
9. **Cross-trust drill-down #1 DONE** — **Pattern CONFIRMED industry-wide.** EART 2024-2: 30+ DQ -177bps, CNL +52bps. AMCAR 2024-1: 30+ DQ -175bps, CNL +24bps. HAROT control stable. KB-CARL-210. Deeper subprime = sharper cure collapse.

## STATUS CHANGES
| Item | Change |
|------|--------|
| Convergence | 51/55 → **57/60** (+Vector #12 Stagflation Trap) |
| UMich Sentiment | 53.3 → **47.6 RECORD LOW** |
| 5-10Y Inflation Exp | 3.2% → **3.4% UN-ANCHORING** (Fed red line) |
| CPI Mar headline | not tracked → **+3.28% YoY** (core +2.61%) |
| ABS monitor issuers | 4 → **6** (added Exeter, Ally, GMF/AmeriCredit) |
| CARL KB entries | 198 → **210** (+12 this session) |
| HOMER KB entries | 35 → **52** (+17: migration + non-bank servicer) |
| Housing delegations | 30 → **44 DELEGATED TO HOMER** |
| SDART 2024-1 | Jan data → **Feb data** (CNL +26bps, DQ -43bps) |
| Pattern status | hypothesis → **CONFIRMED industry-wide** (SDART+EART+AMCAR) |

---

## IN-FLIGHT DRILL-DOWN (RESUME HERE)

**Context:** After confirming the subprime auto cure collapse pattern (KB-CARL-210), Will wanted to continue 3 more drill-downs before moving on. The pattern = DQ bucket shrinking while CNL accelerating = borrowers exiting DQ going to charge-off, not cure. Already confirmed across SDART, EART, AMCAR (HAROT prime control stable).

### Drill-down #2: CNL trigger proximity (NEXT UP)
**Goal:** Check how close each subprime trust is to a CNL trigger event (the trigger SoFi 2025-1 hit at 2.6%). Current CNL levels:
- SDART 2024-1: 8.74% (at 26mo seasoning)
- EART 2024-2: 13.06% (at 23mo seasoning — already at projected terminal 12-14%)
- AMCAR 2024-1: 5.339% (at 22mo seasoning)

**Work to do:**
1. Find the CNL trigger level for each trust — this is in the deal's offering docs or in separate prospectus exhibits. The 10-D EX-99.1 confirmed SDART's DQ Trigger is 24% but didn't show CNL trigger. Need to check the transaction prospectus supplements.
2. Alternative: look for `ABS-EE` or prospectus filings on EDGAR for each trust's structure.
3. Compute months-to-trigger at current CNL accumulation pace.
4. EART at 13.06% already at terminal — rating actions likely imminent.

### Drill-down #3: Trajectory math
**Goal:** Compute implied terminal CNL at current pace.
- SDART 2024-1 at +26bps/month → hits 12% in ~12mo, 14% in ~20mo (trust matures ~60mo, so plenty of runway for breaches)
- EART 2024-2 at +52bps/month → hits 15% in 4mo, 18% in ~10mo
- AMCAR at +24bps/month → hits 8% in ~11mo, 10% in ~19mo
- Compare to Moody's raised CNL expectations (~+1.5pp per our KB)
- Implied rating action timeline

### Drill-down #4: Ally (near-prime) test
**Goal:** Test whether stress is migrating up the quality stack. Ally sits between HAROT (prime) and SDART (subprime).
- Fetch Ally 2024-2 (CIK 0002035124) Feb + Jan 10-Ds
- EX-99.1 location: similar to HAROT format (Honda and Ally both prime/near-prime)
- If Ally shows DQ↓ + CNL↑ → stress migrating UP quality stack (thesis expansion)
- If Ally stable like HAROT → stress contained to subprime (thesis bounded)

---

## NEXT SESSION SHOULD

### IMMEDIATE (today/tomorrow)
1. **Resume drill-down #2** — CNL trigger proximity research (start here)
2. **Drill-down #3** — trajectory math (quick, 15 min)
3. **Drill-down #4** — Ally near-prime test (30 min)
4. **Sweet v. McMahon Apr 15** — monitor DOE compliance / auto relief trigger
5. **NAHB HMI + MBA Apps Apr 15** — data releases tomorrow
6. **JPM Q1 results** — REGINALD handling, check their outbox for CARL signal

### UPCOMING (this week)
7. **OZK earnings Apr 16** (REGINALD primary, CRE construction vintage)
8. **SYF Q1 Apr 21** — CRL-12 test (NCO >6%?). Second HY OAS complacency test. Will be important for subprime auto thesis if NCO trends confirm trust-level cure collapse findings.
9. **DHI Q2 Apr 21** — Builder margin vs 19.0-19.5% guidance
10. **PHM Q1 Apr 23** — Missing middle of builder K-shape

### UPCOMING (next 2 weeks)
11. **Rithm/NewRez Q1 Apr 28** — "DQ will reverse in Q1" claim is testable (non-bank servicer finding from earlier today)
12. **PennyMac Q1 late Apr/early May** — FHA DQ >7.5%? Cenlar integration impact
13. **Case-Shiller Feb — Apr 28** — Tampa trajectory, Midwest broadening
14. **Fannie MF March DQ — late Apr** — GFC breach test
15. **Q2-Q3 non-bank servicer stress window** — advance drain cumulative

### BACKLOG (no deadline)
16. **BNPL_STRESS refresh** — 13 days stale. May need to spawn PHAN.
17. **STATE_DIFFUSION refresh** — 13 days stale
18. **Rate cohort update** — Q3 2025 Fannie data stale (referenced in HOMER KB)
19. **HOMER MULTIFAMILY.tsv populate** — maturity wall timeline gap
20. **Non-bank servicer health refresh next cycle** — Lakeview/Freedom (private) still stale
21. **SDART Q1 earnings impact** — how does SYF NCO correlate to our SDART trust findings?

---

## OUTBOX (0 signals)
Last delivered: SIG-CARL-REGINALD-20260413-nonbank-servicer-warehouse.md (Apr 14)

## INBOX (0 items)
Last processed: SIG-WALTER-CARL-20260410-cpi-umich-stagflation.md (Apr 14)

---

## WORKBOOK HEALTH
| TSV | Rows | Last Modified | Note |
|-----|------|---------------|------|
| KB | 210 | **Apr 14** | ✅ Current (+12 this session) |
| VX | 102 | **Apr 14** | ✅ Current (+VX-CARL-SERV-01 non-bank, UMich update) |
| FLOW | 21 | Apr 13 | ✅ Current |
| PREDICTIONS | 18 | Apr 13 | ✅ Current |
| ABS_BASELINE | 65 | **Apr 14** | ✅ Refreshed (+SDART Feb, +HAROT Feb, +COMET Feb, +EART Jan/Feb, +AMCAR Jan/Feb) |
| BNPL_STRESS | 44 | Apr 1 | ⚠️ 13 days — needs PHAN cross-check |
| STATE_DIFFUSION | 63 | Apr 1 | ⚠️ 13 days |
| TRENDS | 40 | Apr 6 | ⚠️ 8 days |
| ML | 67 | Apr 7 | ⚠️ 7 days |

---

## URGENT / OPEN THREADS
- **Subprime auto cure collapse CONFIRMED** — drill-downs #2, #3, #4 pending. Resume per "IN-FLIGHT DRILL-DOWN" section.
- **EART 2024-2 already at projected terminal CNL** (13.06%) — rating action likely imminent. Implication for thesis: ABS market will show stress before public HY.
- **Sweet v. McMahon Apr 15** — DOE likely misses, auto full relief could trigger
- **UMich 47.6 record low + 5-10Y inflation exp un-anchoring** — Fed locked deeper than before. Apr 25 final UMich print is next test.

---

## KEY DATA SOURCES EXTRACTED THIS SESSION (for OTTO eventually)
- SDART 2024-1 Feb 2026: /tmp/sdart_2024_1_feb2026.html
- HAROT 2024-2 Feb 2026: /tmp/harot_2024_2_feb2026.html
- HAROT 2025-3 Feb 2026: /tmp/harot_2025_3_feb2026.html
- COMET Feb 2026: /tmp/comet_feb2026.html
- DCENT Feb 2026: /tmp/dcent_feb2026.html (defeasance — no performance data)
- EART 2024-2 Jan & Feb 2026: /tmp/eart_2024_2_{jan26,feb26}.html
- AMCAR 2024-1 Jan & Feb 2026: /tmp/amcar_2024_1_{jan26,feb26}.html
- GMF 2024-4 (PRIME, mislabeled) Jan & Feb 2026: /tmp/gmf_2024_4_{jan26,feb26}.html

**NOTE:** /tmp files lost on reboot. If drill-downs resume after reboot, re-fetch via abs_monitor URLs.
