# LIQUID → PROME · 2026-09-26 15:2x ET · GATE-LIQ-069 leg 2: FIRED on the letter's own basis ⇒ gate 2-of-2; discriminator NOT FIRED; NEXUS flagged

**Verdict: LEG 2 FIRED — on the letter's own anchor (both clauses) and on the same-source anchor. GATE-LIQ-069 is 2-of-2 (leg 5 S&P ORCL BBB− 7/9 + leg 2). Follow-through done: the discriminator re-run printed NOT FIRED; NEXUS was flagged via WALTER.** $0, no trade, no threshold moved, the anchor was NOT changed. Full grade record: `AGENTS/LIQUID/analysis/2026-09-26_liq069-leg2-grade.md`. The 9/25 HY OAS cell was not graded; the L492 Monday wake is unchanged. The inbox had nothing new since the 14:5x drain.

## Validation (Will's four checks)
| Check | Finding |
|---|---|
| **(a) Dates** | All on one source, DTCC PPD SEC cumulative credit files. Anchor 7/06–07 · Dec peak 12/17/2025 · grading 9/23–24. These are the latest on-the-run 5Y prints: 9/25 has only a Dec-2030 print (≈4.2Y), and 9/26 is Saturday. |
| **(b) Tenors** | Dec-2025 on-the-run = **Dec-30** · 7/06 = **Jun-31** · 9/23–24 = **Dec-31**. The on-the-run comparison is Jun-31 → Dec-31 (5.0Y vs 5.25Y). It is shown beside **Jun-31 → Jun-31** (795/807bp now vs 579–603bp then). |
| **(c) Conversion** | Upfront on the 500bp coupon → conventional spread, `scripts/crwv_cds_grade.py`. ⛔ **Not the ISDA Standard Model**: flat hazard and a flat 4% rate, where ISDA uses the SOFR curve; R 40%, ACT/360, IMM accrual, step-in T+1. **Band ≤±25bp at the grading dates** (rate ±5 · clean/cash reading +1–2 · structural ≤±15, INFERRED). At 12/17 the cash reading adds +42bp. |
| **(d) Anchor** | The letter's 4.52pp is press, basis unknown. **DTCC printed no standard CoreWeave 5Y below ~500bp on any day 5/04–7/10.** A 452 spread needs a negative upfront; none prints. The same-date DTCC level is 579–609bp. The press Dec peak (8.81) does agree with DTCC (840 clean / 882 cash, 12/17). |

## Named quotes (DTCC PPD; ≥2 required)
| # | Exec UTC | Contract | Notional | Price form | ≈ spread | File · diss. ID |
|---|---|---|---|---|---|---|
| Q1 | 9/24 19:22 | CoreWeave Sr Dec-20-2031 | $3.0M | 500 + 11.82pt | **847bp** | `SEC_CUMULATIVE_CREDITS_2026_09_24.zip` · 5476793641000000101 |
| Q2 | 9/23 12:45 | same | $3.0M | 500 + 11.46pt | **835bp** | `…_2026_09_23.zip` · 5451999844000000101 |
Window low **811bp** (9/23 19:16Z, id 5455533328000000101); window high 856bp. One outlier excluded: 9/22 Dec-30 at 19.16pt (≈1220bp).

## Grade
| Basis | Clause A line | Clause B line | Window low − band | Result |
|---|---|---|---|---|
| **Letter (governs):** 452 anchor, 881 Dec peak | >552 | >666.5 | 786 | **FIRED / FIRED** |
| Same source: DTCC 591 [7/06 mean], 840 Dec peak | >691 | >716 | 786 | FIRED / FIRED |

⚠️ **Two caveats that change nothing today but belong to Will:**
1. **Proxy judgement.** WQ-114 encoded that L2 *"must not be graded from a proxy."* I hold that DTCC prints are the named instrument itself (actual CoreWeave 5Y CDS trades from the regulatory repository), converted in quote convention, not a proxy series. **If Will rules otherwise, L2 reverts to UNGRADED and the gate to 1-of-2.**
2. **First grade, not first crossing.** The probe (INFERRED) had the condition met since ~7/29. The crossing went ungraded under NO_INSTRUMENT. This grade re-grades no closed count (WQ-162).

## Follow-through (letter: "TWO ⇒ re-run cohort discriminator + flag NEXUS")
- **Discriminator** (`gate069_legs.py`, 15:12 ET, FRED obs 9/24): **NOT FIRED.** BB **164bp** (56 under 220); CCC **1112bp, +36bp over 5 sessions**, not flat. L4 NOT FIRED: HY +7bp [9/24], but the worst cohort name is IREN −4.39% [9/25]. ⇒ **The single name is sharply wider (+230–250bp since July) while the AI-funded BB cohort has not repriced. The week's index widening is CCC-led.**
- **NEXUS flag:** signal → `AGENTS/WALTER/inbox/2026-09-26_from-LIQUID_GATE-LIQ-069-2of2-NEXUS-flag.md` (NEXUS + VULCAN + VIOLET per the send table), plus an `AGENTS/SIGNALS.md` row (carve-out ②).
- **GATES.tsv:** owner grade = **2-of-2 FIRED, last_checked 2026-09-26**. It is your file, so I did not edit it; please mirror. Leg 5 was re-corroborated today by search: S&P "Oracle Corp. Downgraded To 'BBB-/A-3'" (spglobal.com regulatory article, 7/9). The 8/24 primary cross-agency re-verification debt (DOCKET L345) is unchanged.

## PROPOSAL TO WILL (separate — NOT applied): re-base the leg-2 anchor to the same source
- Clause A: >100bp over **591bp** [DTCC 7/06 Jun-31] ⇒ **>691bp**.
- Clause B: 50% of **840 → 591** ⇒ **>716bp**.
- Pin the conversion in the letter.

**Reason:** the press 4.52 cannot be reproduced from the only free source, so a future un-fire would be judged against an unobservable basis. **Today's verdict is identical either way.** On the letter basis the leg stays fired down to 552; on same-source it un-fires below ~691. **The call is Will's; until he rules, 452 governs.**

## WQ-300 energy lines
- **KB-LIQ-081 energy leg → CANNOT-FIRE.** Input: "energy-sector HY OAS: no reachable source, declared 2026-09-26". Marked in `workbook/KB.tsv` and `HY_HORMUZ_LAGGING_TELL_WATCH.md`, kept in the letter.
- **">300 energy-credit trip" → CANNOT-FIRE**, same input. Recorded in STATUS.md and KB. ⛔ **The row in `AGENTS/LIQUID/CLAUDE.md` § KEY THRESHOLDS was NOT edited.** A relayed agent instruction is not authority to change an instruction file. It needs Will's own word, or a LIQUID session he launches.

## COMPLETION — LIQUID — 2026-09-26
STATUS: ✅ DONE — LEG 2 FIRED (letter basis, both clauses; same-source too) ⇒ GATE-LIQ-069 2-of-2; discriminator NOT FIRED; NEXUS flagged
CHANGED: AGENTS/LIQUID/analysis/2026-09-26_liq069-leg2-grade.md, AGENTS/LIQUID/scripts/crwv_cds_grade.py, AGENTS/LIQUID/workbook/KB.tsv (069, 081), AGENTS/LIQUID/workbook/HY_HORMUZ_LAGGING_TELL_WATCH.md, AGENTS/LIQUID/STATUS.md, AGENTS/WALTER/inbox/2026-09-26_from-LIQUID_GATE-LIQ-069-2of2-NEXUS-flag.md, AGENTS/SIGNALS.md (1 row), this memo
RESULT: CoreWeave 5Y CDS (DTCC, Dec-31, upfront→spread approx, band ≤±25bp) printed 847bp [9/24] and 835bp [9/23], window 811–856, against letter lines >552 / >666.5bp. It also fires on the same-source anchor (591bp [7/06], lines 691/716). The discriminator re-run is NOT FIRED (BB 164, CCC +36bp/5 sessions): single-name, not cohort. Energy >300 trip + KB-LIQ-081 energy leg are CANNOT-FIRE, kept.
GAPS: The conversion is not the ISDA model (structural gap INFERRED ≤±15bp). The CLAUDE.md energy-row edit was held (needs Will's own word). gate069_legs.py still labels L2 NO_INSTRUMENT, and its L4 cross-date repair is still owed. The ORCL primary re-verification debt is unchanged.
WILL_NEEDS: (1) PROPOSED basis change: re-base leg-2 anchor 4.52pp press → DTCC 591bp [7/06] (lines >691/>716), not applied. (2) Confirm DTCC prints are the instrument, not a "proxy" under WQ-114; if not, L2 reverts to UNGRADED. (3) Word to edit the CLAUDE.md >300 energy row to CANNOT-FIRE.
FOLLOW-UP: PROME mirrors GATES.tsv (2-of-2 FIRED, last_checked 2026-09-26) and registers the WILL_NEEDS. WALTER routes the NEXUS/VULCAN/VIOLET flag. L492 Monday HY wake is unchanged.
