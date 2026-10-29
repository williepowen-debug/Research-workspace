# POLLY STATUS
**Last real data refresh:** 2026-10-28 (Q3 2026 primaries for P&C, UNH/ELV, CA FAIR Plan, FL Citizens; bounded pass, Will-approved). POLLY remains in dossier-mode: spawn on demand. Handoff: `state_vectors/SV-POLLY-2026-10-28-01.md` (supersedes the 2026-08-10 SV's figures; its DOSSIER CARRY LIST framing still holds).

> VINTAGE MAP. Q3-2026 vintage (this pass): PGR, TRV, UNH, ELV, CA FAIR Plan, FL Citizens, Epiq bankruptcies (secondary). **Allstate Q3 combined ratio NOT available** (earnings not filed as of 2026-10-28; Q2 values kept and marked stale). NOT refreshed (Apr-2026 or earlier, `[STALE]`): auto CPI, uninsured motorist rate, homeowners premium growth, ACA enrollment, health deductibles, medical debt. Parent CARL STATUS.md carries any live figure for those; DOC owns healthcare cost/OOP.

**Phase:** unchanged: Phase 2-3 nationally; Phase 3-4 in CA. CA/FL divergence widened: CA FAIR Plan growth has nearly stalled at a record level; FL Citizens kept falling.

---

## Q3 2026 REFRESH - 2026-10-28

| Item | Prior | New (Q3-2026) | As-of / Source |
|---|---|---|---|
| Progressive combined ratio | 87.3% (Q2) | **88.7%** (9M 87.5%) | Q3 2026; PGR 8-K 2026-10-14 |
| Travelers consolidated CR | 83.6% (Q2) | **86.8%**; Personal Auto **87.1%** (Q2 82.8%) | Q3 2026; TRV 8-K 2026-10-16 |
| Allstate | auto 83.3 / P-C 86.6 (Q2) `[STALE - 2026-08-10]` | Q3 cat losses $1.65B; **combined ratio not yet reported** | ALL 8-K 2026-10-15 (monthly cat release only) |
| UNH medical care ratio | 86.7% (Q2) | **88.4%** (Q3-25 89.9%); UHC members 48.3M | Q3 2026; UNH 8-K 2026-10-13 |
| ELV benefit expense ratio | 89.7% (Q2) | **90.6%** (-70bps YoY); medical members 44.88M | Q3 2026; ELV 8-K 2026-10-21 |
| CA FAIR Plan policies | 696,562 (Jun) | **698,307**; exposure **$773B** | Sep 2026; cfpnet.com fetched 2026-10-28 |
| FL Citizens policies | 278,196 (Jul-31) | **254,836** (Sep-30) | citizensfla.com fetched 2026-10-28 |
| US bankruptcies (9M) | n/a | 469,719 (+11% YoY) | Jan-Sep 2026; Epiq AACER via ABF Journal 2026-10-09 (secondary) |

**Headline:** CA FAIR Plan added only 1,745 policies in Q3 (vs 12,174 in Q2); 750K by year-end (P02) is effectively out of reach. The 8/10 view that Citizens was nearing a floor was wrong: it fell another 23.4K Jul->Sep. Hurricane Isaias (Cat 2, FL Panhandle, 2026-10-09, NWS Mobile) is below the Cat 3+ trigger and is not yet in the Citizens count. Both health carriers now show YoY margin improvement with falling membership (UNH Medicaid 6.695M vs 7.46M a year earlier; ELV MA -15.5%): the Q2 UNH/ELV divergence closed. CRL-22 is CARL's call; figures only. Correction: the prior "336K Citizens in Mar-2026" was the Feb-28 count (Mar-31 = 321,957).

---

## THESIS

Insurance is both INDICATOR and AMPLIFIER of consumer stress. CA and FL are diverging: CA 698K FAIR Plan policies / $773B exposure with growth stalling (private market not returning); FL Citizens 255K and falling. National auto/HO carriers remain very profitable (PGR 88.7, TRV 86.8), though TRV auto margin thinned in Q3. **Thesis confidence: 76%** (unchanged from 8/10, no re-mark this pass) | VALIDATED WITH GEOGRAPHIC DIVERGENCE.

---

## SIGNAL DASHBOARD

| Vector | ID | Current | Threshold | Status | As-of |
|---|---|---|---|---|---|
| Auto Insurance CPI YoY | VX-POLLY-2.01 | 0.8% (Mar 2026) `[STALE - 2026-04-17]` | >8% | GREEN (stale) | 2026-04-17 |
| Uninsured Motorist Rate | VX-POLLY-2.03 | 15.4% (2023 IRC) `[STALE]` | >14% | YELLOW | 2026-04-09 |
| CA FAIR Plan | VX-POLLY-1.03 | **698,307; $773B** | Largest carrier | RED, growth stalling | Sep 2026 (cfpnet.com, 2026-10-28) |
| FL Citizens | VX-POLLY-1.03 | **254,836** | <400K | GREEN, declining | 2026-09-30 (citizensfla.com, 2026-10-28) |
| Homeowners premium growth | VX-POLLY-1.01 | 4% nat'l `[STALE - 2026-04-09]` | >8% | YELLOW | 2026-04-09 |
| Auto CR | VX-POLLY-2.02 | **PGR 88.7 / TRV auto 87.1** (Q3); ALL Q3 pending (Q2 83.3 `[STALE]`) | >100% | GREEN | Q3 2026 (8-Ks 10/14, 10/16) |
| P&C CR broader | VX-POLLY-4.01 | **TRV 86.8 / PGR 88.7** (Q3) | HO >102% | GREEN | Q3 2026 |
| ACA enrollment | VX-POLLY-3.03 | 23.1M `[STALE - Jan 2026]` | <22M | ORANGE (stale) | 2026-04-09 |
| Health uninsured | VX-POLLY-3.03 | 8% / 27.1M `[STALE]` | >9% | YELLOW | 2026-04-09 |
| Employer deductible | VX-POLLY-3.02 | $1,886 `[STALE - 2025 survey]` | >$2,000 | YELLOW | 2026-04-09 |
| Medical debt | VX-POLLY-3.04 | ~20% / $195B `[STALE]` (see DOC) | >20% | YELLOW | 2026-04-09 |
| UNH MCR | VX-POLLY-3.01 | **88.4%** Q3 (Q2 86.7%) | >88% | YELLOW | Q3 2026 (8-K 2026-10-13) |
| ELV BCR | VX-POLLY-3.01 | **90.6%** Q3 (-70bps YoY) | >88% | ORANGE | Q3 2026 (8-K 2026-10-21) |

---

## GEOGRAPHIC STATUS

| State | Status | Key metric | Note |
|---|---|---|---|
| CA | RED, growth stalling | FAIR Plan 698,307 / $773B (Sep 2026) | FY26 new business 195,929, -27% YoY; ~30% avg rate hike eff 2026-10-15 (approved, per 8/10 read) |
| FL | GREEN | Citizens 254,836 (2026-09-30) | Isaias Cat 2 landfall 2026-10-09; Oct count unpublished; season ends 11-30 |
| LA / TX | `[STALE - Apr-2026]` | not refreshed | |
| National | `[STALE - Apr-2026]` for CPI/uninsured/ACA | not refreshed | DOC/CARL own live health reads |

---

## PREDICTIONS (full notes in workbook/PREDICTIONS.tsv; confidences NOT re-marked; CARL scores as-made)

| ID | Prediction | Conf. | Window | Reachability after Q3 (2026-10-28) |
|---|---|---|---|---|
| P01 | Uninsured >9% by end-2027 | 70% | 2026-Q4 to 2027-Q4 | Not decidable; no new primary |
| P02 | CA FAIR Plan >750K by end-2026 | 55% | 2026-Q4 | EFFECTIVELY UNREACHABLE: needs +51.7K in Q4 vs +1.7K in Q3. Not mathematically fixed |
| P03 | Citizens <400K through season | 85% | 2026-Q4 | Practically unreachable breach (255K; Isaias Cat 2). Not fixed until Nov-30 |
| P04 | ACA enrollment <22M for 2027 | 75% | Jan 2027 | Not decidable |
| P05 | Auto CR <95% FY2026 (ALL/PGR) | 90% | 2026-Q4 | PGR 9M 87.5; needs ~117% Q4 to breach. Allstate Q3 unreported. Not fixed |
| P06 | Bankruptcies >600K in 2026 | 55% | 2026-Q4 | 469,719 through Sep; needs 130,282 in Q4 (9M avg 52.2K/mo). Likely, not fixed. Secondary source |
| P07 | CA private re-entry <50K | 60% | 2026-Q4 | No primary pulled; not decidable |
| P08 | Uninsured+underinsured auto >35% | 65% | 2027 | Not decidable |

None resolves before its window; no outcome is mathematically fixed.

---

## SEASONAL WATCH (as of 2026-10-28)

- Hurricane season ends 2026-11-30. Isaias (Cat 2, 105 mph, near Destin FL, 2026-10-09) is the first hurricane of the season per NWS Mobile/WebSearch summary (not verified at NHC); no Cat 3+ FL landfall found.
- CA wildfire season through Oct: Q3 count shows no spike. P02 swing factor is now only a bulk assignment or catastrophic fire.
- OBBBA 6-month redeterminations and work requirements begin Dec 30-31, 2026. ACA 2027 OE results Jan 2027 (tests P04).
- Allstate Q3 earnings, PGR 10-Q 2026-11-02 / call 2026-11-03: next primaries.

---

*Workbook detail in `workbook/`. Prior (2026-08-10) Q2 figures are in git history and the 2026-08-10 SV.*
