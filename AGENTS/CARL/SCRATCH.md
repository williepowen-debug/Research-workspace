# CARL SCRATCH
**Last session:** 2026-04-02 ~20:45 UTC
**Type:** Boot audit + system improvements + data refresh + NFP prep + predictions maintenance

**PRIORITY-1:** NFP March releases TOMORROW Apr 3 8:30am ET (Good Friday, markets closed). Scenario framework ready at `domain/sources/NFP_MAR2026_FRAMEWORK.md`. Consensus +57K. Gap risk Monday Apr 6.

---

## WHAT HAPPENED
1. **Boot process audit** — Identified 8 improvements. Restructured SCRATCH.md, date-tagged STATUS.md, formalized SCRATCH template in CLAUDE.md.
2. **Data accuracy audit** — Verified all dashboard values against live sources. Fixed 7 stale/incorrect values (mortgage 6.86→6.46, diesel 5.10→5.51, subprime auto 7.1→6.9, GDPNow 2.0→1.6, Fannie date Jan→Feb, JOLTS refs 0.94→0.91, Liberation Day removed as 1yr stale).
3. **Inbox cleared (2 items)** — Gas behavioral signal → KB-CARL-141. PROME check-in → response drafted to outbox.
4. **Fresh data pulls** — Gas $4.08, diesel $5.51, Brent $107-112, GDPNow collapsed to 1.6%, HY OAS tightened to 316bps (counter-signal), mortgage 6.46% confirmed.
5. **New KB + VX entries** — KB-CARL-141 (gas breakpoint), KB-CARL-142 (GDPNow collapse), KB-CARL-143 (HY OAS complacency). VX-CARL-MACRO-01 (GDPNow, RED), VX-CARL-MACRO-02 (HY OAS, ORANGE).
6. **NFP framework built** — 4-band scenario matrix, detail watch list, market structure notes, post-print action plan. Consensus +57K but strip Kaiser (+25-30K) and organic is ~+27-32K.
7. **Predictions maintenance** — Reconciled STATUS↔TSV numbering mismatch. CRL-08 timeline extended (Apr 5→May). CRL-02 noted 6.9% vs 7.1%. CRL-03 updated with Feb trajectory. Added CRL-12 (SYF FY NCO >6.0%, 77% conf).

## STATUS CHANGES
| Item | Change |
|------|--------|
| 30-yr Mortgage | 6.86% → **6.46%** 🔴→🟠 |
| Diesel | $5.10 → **$5.51** |
| Gas | → **$4.08** |
| Subprime Auto 60+ DQ | 7.1% → **6.9%** |
| GDPNow Q1 | 2.0% → **1.6%** 🟠→🔴 |
| HY OAS | 328bps → **316bps** 🔴→🟠 (counter-signal) |
| Fannie MF DQ date | Jan → **Feb 2026** |
| JOLTS refs | 0.94 → **0.91** throughout |
| KB entries | +3 (141-143). Total: 143 |
| VX entries | +2 (MACRO-01, MACRO-02). Total: 83 |
| Predictions | +1 (CRL-12). CRL-08 extended. Numbering reconciled. Total: 12 |
| Inbox | Cleared (was 2) |
| Outbox | +1 PROME check-in response. Total: 6 awaiting HERMES |
| CLAUDE.md | SCRATCH template formalized, stale data fixed |
| NFP framework | NEW: `domain/sources/NFP_MAR2026_FRAMEWORK.md` |

---

## NEXT SESSION SHOULD

### IMMEDIATE (24hrs)
1. **NFP Mar releases Apr 3 8:30am ET** — Read `domain/sources/NFP_MAR2026_FRAMEWORK.md`. Classify scenario (1-4). Update STATUS. Log KB-CARL-144. If Scenario 3/4: draft signals to LABOR + PROME (+ REGINALD if Scenario 4).
2. **Check Feb NFP revision** — if downward, compute new 3-month avg.
3. **Monday Apr 6 gap open** — First market reaction. Options pricing +/-2.1%.

### UPCOMING (this week)
4. **Savings rate Feb drops Apr 9** — If fell while retail rose → consumers spending down savings.
5. **UMich prelim April ~Apr 11** — Sub-50 = deep recession signal. Currently 53.3.
6. **CRL-08 ($4.50 gas)** — $4.08 now, $0.42 gap. Extended to May. Monitor Brent.

### UPCOMING (next 2 weeks)
7. **JPM earnings Apr 14** — First Phase 1 financial. See `EARNINGS_WATCH_Q1.md`.
8. **CPI March mid-April** — Food CPI acceleration? Gas passthrough?
9. **SYF earnings Apr 21** — CRITICAL. CRL-12 first test. NCO >6%? Guidance cut?
10. **CFPB 1033 deadline Apr 30** — BNPL phantom debt visibility shock.

### BACKLOG (no deadline)
11. State Diffusion exact numbers — NY Fed interactive pull.
12. ABS CC trust EDGAR pulls (DCMT + COMET 10-D).
13. Google Trends baseline (sell plasma, pawn shop, eviction help).
14. SLOOS / Credit Tightening VX vector.
15. Sub-agents DOC, NICK, POLLY, POP refresh.

---

## OUTBOX (6 signals, awaiting HERMES)
| File | To | Summary |
|------|----|---------|
| SIG-CARL-LABOR-20260329-jolts-inversion.md | LABOR | 🔴 JOLTS 0.94 inverted — request re-employment probability |
| SIG-CARL-LABOR-20260331-jolts-feb-deepening.md | LABOR | 🔴 JOLTS 0.91, hires COVID-low — UI hole revision needed |
| SIG-CARL-PROME-20260329-jolts-inversion.md | PROME | 🔴 JOLTS inversion — request convergence upgrade |
| SIG-CARL-REGINALD-20260327-fl-pincer.md | REGINALD | 🔴 FL three-sided pincer — request bank exposure assessment |
| SIG-CARL-REGINALD-20260331-syf-canary.md | REGINALD | 🟠 SYF NCO 5.8% — request regional bank cross-ref |
| SIG-CARL-PROME-20260402-checkin-response.md | PROME | Normal: DQ updates, thresholds, LABOR context, Q1 positioning |

## INBOX (0 items)
Cleared.

---

## WORKBOOK HEALTH
| TSV | Rows | Last Modified | Note |
|-----|------|---------------|------|
| KB | 143 | Apr 2 | Current |
| VX | 83 | Apr 2 | Current |
| FLOW | 18 | Mar 27 | 6 days old — refresh next session |
| PREDICTIONS | 12 | Apr 2 | Current |
| ABS_BASELINE | 53 | Mar 17 | 16 days old — stale |
| BNPL_STRESS | 43 | Apr 1 | Current |
| STATE_DIFFUSION | 62 | Apr 1 | Current |
| TRENDS | 28 | Mar 17 | 16 days old — stale |

---

## URGENT
- NFP Mar Apr 3 8:30am ET — Good Friday, markets closed, 67-hour gap to Monday. Framework ready.
- GDPNow collapsed to 1.6% — stagflation trap deepening. NFP will push it further.
- 6 outbox signals awaiting HERMES delivery (2 to LABOR, 2 to PROME, 2 to REGINALD)
