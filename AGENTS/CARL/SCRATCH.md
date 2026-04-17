# CARL SCRATCH
**Last session:** 2026-04-17 ~13:00 UTC (context compacted + closed after workbook audit)
**Type:** Apr 15 data processing + SYF pre-brief + **FULL WORKBOOK AUDIT** (VX/FLOW/PREDICTIONS/STATE_DIFFUSION/CHANGELOG/THESIS all synced to v2.4)

**PRIORITY-1:** Pull ALLY Q1 actuals (call closed ~10:15 AM ET Apr 17) — auto NCO, retail DQ, originations mix, credit tightening language. Feeds payment hierarchy thesis test (prime/near-prime auto = next domino after subprime breached). Check Quartr/IR site.

---

## WHAT HAPPENED
1. **Booted despite HENRY/REGINALD uncommitted files** — did not pull, flagged to Will. Read boot files from local state.
2. **Spawned STUE + HOMER in parallel** for Apr 15 data refresh (Sonnet, ~$0.06 combined).
3. **Sweet v. McMahon Apr 15 deadline MISSED** — DOE did not comply. Auto Full Relief triggered for ~170K non-Exhibit C borrowers. Combined with Exhibit C (missed Jan 28 ~170K), total pipeline ~271K. Second consecutive Sweet deadline miss. Notices required by Jun 15.
4. **FICO Spring 2026** — SL 90+ DQ ~9.8% (up 25% from 7.9% Apr 2025). 6.1M new DQ Feb-Apr. Avg score drop **-69 pts** (was -62). CRL-04 near-confirmed; breach likely Q2.
5. **SAVE judicially dead** — 8th Cir Mar 10 reversed + entered final judgment. Dual-dead (legislative + judicial). Jul 1 locked.
6. **NAHB HMI Apr = 34** (-4pts from 38, 7-mo low, 24th consec month <50). Future Sales 42 (-7pts). Tariff shock: +$10,900/home. Breaches CARL <40 RED threshold.
7. **ATTOM Q1 = PIPELINE CONVERTING** — Q1 filings 118,727 (+26% YoY); **Q1 REO 14,020 (+45% YoY)**. March monthly +18% MoM. FL Q1 REO +108% YoY (greatest nationally). Regime change from accumulation.
8. **STATUS.md refreshed** — 7 sections updated, 2 new rows (MBA Apps, NAHB HMI), predictions CRL-04 upgraded.
9. **7 KB entries added** (KB-CARL-215 through 221): Sweet outcome×2, SAVE judicial death, FICO 9.8%, MOHELA discovery, NAHB HMI, ATTOM Q1.
10. **FULL WORKBOOK AUDIT (session close)** — Will caught that VX/FLOW/PREDICTIONS/THESIS weren't updated. Executed 6-step fix list:
    - **VX.tsv:** BLDR-01 (HMI 38→34 ORANGE→RED), HSG-01 (6.37→6.30% + MBA -3% YoY), SL-02 (9.6→9.8%), 6.06 (FL +190→+108% Q1 REO), **new HSG-05** (REO quarterly completions vector)
    - **FLOW.tsv:** new **FLOW-CARL-12.04** Path C Activation (Pipeline Conversion → Bank Loss Realization) ACTIVATING-RED, 6-12mo speed
    - **PREDICTIONS.tsv:** CRL-04 97→98% OPEN-NEAR CONFIRMED, CRL-06 70→78% with Q1 ATTOM data (bonus)
    - **STATE_DIFFUSION.tsv:** FL row refreshed to +108% Q1 REO YoY w/ judicial state completion wave detail
    - **CHANGELOG.md:** new v2.4 entry "Foreclosure Pipeline Converting + Credit Cascade Executing"
    - **THESIS.md:** Vector #10 upgraded 🔴 4 → 🔴🔴 5 (canonical), convergence 57/60 → **58/60**
11. **STATUS.md dashboard mirror** synced to 58/60 + Vector #10 upgrade.

## STATUS CHANGES (incl. audit)
| Item | Change |
|------|--------|
| Convergence | 57/60 → **58/60 CRITICAL** |
| Vector #10 (Foreclosure) | 🔴 4 → 🔴🔴 5 (pipeline CONVERTING) |
| THESIS version | v2.3 → **v2.4** |
| SL 90+ DQ | 9.6% → **~9.8% FICO Spring 2026** |
| Sweet Auto-Relief | not tracked → **🔴 FIRED ~271K pipeline** |
| PMMS 30yr | 6.37% → **6.30%** (3rd consec wk easing) |
| NAHB HMI | not tracked → **34 RED** (new row) |
| Q1 Foreclosures | Q4 58,140 → **Q1 118,727 +26% YoY, REO +45% YoY** |
| FL Foreclosures | Q4 +190% filings → **Q1 REO +108% YoY** |
| CRL-04 | 9.6% 97% → **~9.8% 98% OPEN-NEAR CONFIRMED** |
| CRL-06 | 70% → **78%** (possibly confirmed at starts level) |
| KB entries | 214 → **221** (+7) |
| VX entries | added HSG-05 (REO completions) |
| FLOW entries | added 12.04 (Path C Activation) |

---

## NEXT SESSION SHOULD

### IMMEDIATE (today 4/17 post-ALLY / Mon 4/21)
1. **Pull ALLY Q1 actuals** — call closed ~10:15 AM ET today. Check auto NCO, 30+/60+ DQ, originations, credit tightening language, deposit trends. Post-call transcript on Quartr.
2. **Check REGINALD outbox** for OZK earnings signals (Apr 16) after their commit clears
3. **Commit CARL files** — pending HENRY/REGINALD commit resolution. Run `git status` first to verify others' dirs are clean.
4. **Finalize SYF Q1 Mon Apr 21 prep** — cross-ref EARNINGS_WATCH_Q1.md Apr 17 addendum + ABS structural findings. CRL-12 NCO >6% test.
5. **Cross-refs to REGINALD** — FL Q1 REO +108% (CRE-adjacent Path C), PMMS -53bps YoY (NIM/MBS), NAHB tariff shock (builder loan mix). Outbox signal candidate.

### UPCOMING (this week)
6. **Apr 21 Mon** — SYF Q1 (CRL-12 NCO >6% test), COF Q1, DHI Q2
7. **Apr 23 Wed** — PHM Q1, AXP Q1
8. **Apr 25 Fri** — UMich Apr Final (47.6 confirmed?)
9. **Apr 26** — FL UI Wave 2 peak

### UPCOMING (next 2 weeks)
10. **Apr 28** — Case-Shiller Feb, Rithm/NewRez Q1 (testable "DQ reverse" claim)
11. **Late Apr** — Fannie MF March DQ (GFC breach test, 0.74 → 0.80%)
12. **Late Apr / early May** — PennyMac Q1 (FHA DQ >7.5%?)
13. **May 28** — AFT/MOHELA status conference (discovery)

### BACKLOG (no deadline)
14. **March 10-D ABS filings** (~Apr 20-25) — SDART/EART/AMCAR/HAROT/Ally March collection data
15. **BNPL_STRESS refresh** (16 days stale) — spawn PHAN
16. **STATE_DIFFUSION refresh** — FL row updated this session; other states still 16 days stale
17. **Cross-agent outbox signal:** FL Q1 REO +108% YoY → REGINALD + MARCO (not yet drafted)

---

## OUTBOX (0 signals)
Last delivered: SIG-CARL-REGINALD-20260413-nonbank-servicer-warehouse.md (Apr 14)
**Draft candidate:** FL Q1 REO +108% + Path C activation → REGINALD (warehouse/MBS exposure) + MARCO (FL migration amplification).

## INBOX (1 item processed)
| File | From | Summary |
|------|------|---------|
| SV-HOMER-2026-04-17-01.md | HOMER | NAHB/MBA/PMMS/ATTOM — INTEGRATED, can archive |

---

## WORKBOOK HEALTH
| TSV | Rows | Last Modified | Note |
|-----|------|---------------|------|
| KB | 221 | **Apr 17** | +7 (Sweet, FICO, SAVE, MOHELA, NAHB, ATTOM) |
| VX | 103 | **Apr 17** | +1 (HSG-05 REO completions) + 4 updates |
| FLOW | 22 | **Apr 17** | +1 (12.04 Path C activation) |
| PREDICTIONS | 18 | **Apr 17** | CRL-04 + CRL-06 updated |
| STATE_DIFFUSION | 63 | **Apr 17** | FL row refreshed (other states still stale) |
| ABS_BASELINE | 67 | Apr 16 | OK |
| BNPL_STRESS | 44 | Apr 1 | **16 days stale — spawn PHAN** |
| TRENDS | 40 | Apr 6 | 11 days stale |
| ML | 67 | Apr 7 | 10 days stale |

---

## URGENT
- **ALLY Q1 actuals** — call closed ~10:15 AM ET. Prime/near-prime auto = next domino after subprime breach. Retail auto NCO >2.0% or 30+ DQ rising sharply = payment hierarchy cascade activates.
- **SYF Mon Apr 21** — CRL-12 NCO >6% test. Second HY OAS complacency test. Cross-ref ABS trust-level cure collapse.
- **Pipeline CONVERTING not just accumulating** — Q1 REO +45% YoY is a regime change. Path C (housing→banks) transmission probability UP. THESIS v2.4 58/60 reflects this.
- **Git commit still pending** — CARL files ready but blocked on HENRY/REGINALD. Check next session boot.
