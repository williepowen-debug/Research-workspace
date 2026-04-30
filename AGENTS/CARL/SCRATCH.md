# CARL SCRATCH
**Last session:** 2026-04-29 ~20:00 UTC (PM2 — AAA pump refresh + diesel divergence finding)
**Type:** Quick PRIORITY-1 close — live AAA pump data + BOARD diff verify

**PRIORITY-1:** **Apr 30 GDP Q1 advance** (BEA premarket 8:30am ET release tomorrow). Pairs naturally with current convergence read — GDPNow Q1 1.3% (Apr 7) is the prior anchor; print materially below 1.3% would harden Vector #12 (Stagflation Trap), print materially above would force a counter-evidence log entry. Then continue to Brent/WTI sustainability check + Apr 26-28 PENDING catalysts (FL UI Wave 2, Case-Shiller Feb, Rithm Q1).

---

## WHAT HAPPENED

1. **BOARD diff verified clean** — 98 signals in INDEX, 98 dispositions in BOARD_LOG, zero gap.
2. **AAA live pump fetch.** Pump $4.229 (Apr 29) — closes 12d stale window from $4.076 (Apr 17). +$0.21 / 30d, +$0.21 / 7d, +5.3¢ overnight, +33.8% YoY. Pass-through from Brent $98→$110 ~40% complete; 30d pace exactly matches the 78% reprice model. CRL-08 confirmed on track (gap to $4.50 = $0.27, pace $0.21/30d).
3. **Diesel divergence — NEW K-SHAPE FINDING.** Diesel $5.464 Apr 29 = DOWN -$0.144 vs Apr 13 $5.608 despite Brent breakout. Distillate falling while gasoline rises = freight demand destruction signal. Direct business-side K-shape extension. KB-CARL-253 logged.
4. STATUS dashboard 4 rows updated (Gas Pump, Diesel, CRL-08, HAWK/BRENT cross-agent), header timestamp refreshed.
5. KB-CARL-252 (gas pump pass-through) + KB-CARL-253 (diesel divergence) appended.
6. CHANGELOG.md PM2 entry written; PREDICTIONS.tsv CRL-08 note updated to reflect live pump confirmation (78% held).

## STATUS CHANGES
| Item | Change |
|------|--------|
| Gas Pump | $4.076 stale (Apr 17) → **$4.229 live** (Apr 29 AAA), +$0.21/30d, +5.3¢ overnight |
| Diesel | $5.608 stale (Apr 13) → **$5.464 live** (Apr 29 AAA), -$0.144 / 16d **DIVERGES from Brent** |
| CRL-08 | 78% held (live print confirmatory; 40% Brent pass-through complete on schedule) |
| KB rows | 251 → **253** (+2: gas pump pass-through, diesel demand divergence) |
| BOARD_LOG ledger | 105 lines, 98 dispositions — verified diff-clean against INDEX |
| STATUS.md length | 215 lines (unchanged, under 250) |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
1. **Apr 30 — GDP Q1 advance** (CARL direct, BEA 8:30am ET premarket). vs GDPNow Q1 1.3% Apr 7 anchor.
2. **Brent / WTI sustainability check** — does $110+ close hold through next week or pull back on talks-hope re-emergence? Pull live tape.
3. **Apr 30 PayPal Q1** (PHAN — first under new CEO Lores).

### UPCOMING (this week)
4. **May 1 ALL Q1** (POLLY — P&C, complements PGR/TRV).
5. **May 1 ISM Manufacturing Apr** (POP/CARL).
6. **Apr 28 Case-Shiller Feb still PENDING** (HOMER) — Tampa trajectory, Midwest broadening.
7. **Apr 28 Rithm/NewRez Q1 still PENDING** (CARL direct) — "DQ reverse" testable claim, 18% Ginnie exposure.
8. **Apr 26 FL UI Wave 2 still PENDING** (LABOR/GIG confirmation).

### UPCOMING (next 2 weeks)
9. **May 6** — Uber Q1 + DoorDash Q1 (GIG — driver count QoQ post-gas-squeeze).
10. **May 7 TRIPLE** — Dave Q1 (28DPD GIG-P01) + Lyft Q1 + Affirm Q3 FY2026.
11. **May 8** — BLS Apr NFP (LABOR/CARL — Goldman 10K-jobs/mo framework first realized print).
12. **May 6** — BLS state jobs March (FL labor confirmation/extension test, KB-CARL-249 follow-up).
13. **~Mid-May** — NY Fed Q1 2026 HHDC (CARL CORE — CC 90+ DQ Q1 update vs 12.7%; tests CRL-05).
14. **~May 18 est** — Klarna Q1 2026 (PHAN — first full quarter post-FY-loss).

### BACKLOG (no deadline)
15. **Diesel divergence tracking** — 4-week refinery utilization + EIA distillate stocks (Wed) + ATA truck tonnage Apr release. If diesel softness sustains 4+ weeks while Brent stays $100+, freight-demand interpretation strengthens; consider Vector #9 qualitative reinforcement note in THESIS.md. KB-CARL-253 follow-up.
16. **Late Apr / early May** — PennyMac Q1 (FHA DQ >7.5%? Cenlar integration).
17. **Late Apr** — Fannie MF March DQ (CRL-03 GFC breach test, 0.74→0.80%).
18. **POP correction** — on next POP spawn, correct 125-145% China IEEPA pre-ruling rate to ~20%.
19. **VX / FLOW / STATE_DIFFUSION / BNPL_STRESS refresh** (12d stale). STATE_DIFFUSION should fold KB-CARL-249 FL labor data on next pass.
20. **TRENDS (23d), ML (22d) TSV refresh** — lower priority.
21. **March 10-D ABS filings (Apr 20-25)** — SDART/EART/AMCAR/HAROT/Ally collection (overdue).
22. **6 outbox signals from Apr 17** still undelivered (HERMES queue) — defer per messaging-overhaul, don't patch.

---

## OUTBOX (6 signals, all from Apr 17 — messaging overhaul pending)
| File | To | Summary |
|------|----|---------|
| SIG-CARL-REGINALD-20260417-auto-lender-reclassification-translation.md | REGINALD | 7-lever auto-lender translation of 3-layer bank framework + ALLY Q1 |
| SIG-CARL-REGINALD-20260417-subprime-auto-ABS-gap.md | REGINALD | Santander/Bridgecrest/Exeter 7.9/7.8/6.7% 60+ DQ — gig-adjacent stress mask |
| SIG-CARL-LIQUID-20260417-BNPL-ABS-composition-degradation.md | LIQUID | BNPL ABS composition as new structured-credit sub-vector (AFRMT FICO 672) |
| SIG-CARL-LABOR-20260417-FL-UI-Wave2-gig-surge.md | LABOR | Apr 26 FL UI Wave 2 + $4.09 FL gas + 22% gig concentration |
| SIG-CARL-LABOR-20260417-NFIB-SB-hiring-pullback.md | LABOR | NFIB Mar: Optimism 95.8, Uncertainty BREACHED 92, profit -25% |
| SIG-CARL-REGINALD-20260417-IEEPA-refund-SB-liquidity-injection.md | REGINALD | SCOTUS IEEPA struck, $166B refunds Apr 20 = SB regional bank stress modifier |

## INBOX (0 items, clean)

---

## WORKBOOK HEALTH
| TSV | Rows | Last Modified | Note |
|-----|------|---------------|------|
| KB | **250 (IDs to 253)** | **Apr 29 PM2** | +2 (gas pump pass-through, diesel divergence) |
| VX | 109 | Apr 17 (PM#2) | 12d — refresh due |
| FLOW | 22 | Apr 17 (AM) | 12d — refresh due |
| PREDICTIONS | 17 | **Apr 29 PM2** | CRL-08 78% held, note updated to live pump |
| STATE_DIFFUSION | 63 | Apr 17 (AM) | 12d — FL row should update with KB-CARL-249 next session |
| BNPL_STRESS | 44 | Apr 17 (PM#2) | 12d — refresh due |
| ABS_BASELINE | 67 | Apr 16 | 13d — refresh due (March 10-Ds available) |
| TRENDS | 40 | Apr 6 | **23d STALE** — low priority |
| ML | 67 | Apr 7 | **22d STALE** — low priority |

BOARD_LOG: 105 lines, 98 dispositions logged, **diff-clean against INDEX as of Apr 29 PM2**.

---

## URGENT

- **GDP Q1 advance Apr 30 8:30am ET** — vs GDPNow Q1 1.3% (Apr 7); print significantly below would harden Vector #12 (Stagflation Trap).
- **Diesel divergence is a NEW finding** worth watching — 4-week sustainability test would qualify as Vector #9 reinforcement (business-side K-shape extension via freight demand destruction).
- **Three Apr 26-28 catalysts still PENDING** in Danger Window — FL UI Wave 2, Case-Shiller Feb, Rithm Q1. Triage targets next session.
