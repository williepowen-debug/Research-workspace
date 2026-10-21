# LABOR → PROME: four grading cards frozen + three approved fixes (Will 09:38 ET)

**Written 2026-10-21 09:50 ET** by LABOR (PROME-spawned, af287aee). Nothing graded. D:L719, BD-35/BD-23, T-07, BD-26, LAB-11 and the charter trim were left alone, as instructed.

| Card | Print (VERIFIED at the issuer's calendar, 10/21) | Legs (instrument · document · basis named in §1 of each) | Checker | Commit |
|---|---|---|---|---|
| `AGENTS/LABOR/docket/GRADING_CARD_20261030_ECI.md` | Fri 10/30 08:30 (BLS ECI schedule) | E1 civilian comp 12-mo NSA (≥3.6 / 3.5 / ≤3.4) · composition conjunction (AHE-accelerating column unreachable: AHE fell 3.5 → 3.0) · wedge `w = 3.0 − ECI private wages` + which-side-closed implication line | 0 defects | `36e6064d2` |
| `…/GRADING_CARD_20261103_JOLTS.md` | Tue 11/3 10:00 (BLS Nov calendar) | NET = hires − total separations from printed levels, Aug rev × Sep P × Sep hires rate: 8 cells for LEG C + v4 · layoffs rate ≥1.2 · T-10 · openings record-only | 0 defects | `379a9e509` |
| `…/GRADING_CARD_20261105_Challenger.md` | Thu 11/5 05:30 EST (Challenger calendar) | cuts `X` · exact AI share `s` · exact tech YTD `g` from printed levels (UNGRADED if absent) · v5 6-cell cross-product | 0 defects | `c69fedbd8` |
| `…/GRADING_CARD_20261106_NFP.md` | Fri 11/6 08:30 (BLS empsit schedule) | LEG A `X ≥ max(150, 300 − (A' + S'))` · LEG B Oct EPOP ≥58.9 · LEG C from the 11/3 card · v2 8-cell cross-product · T-03/T-04 ≤58.6 · T-06 · U-3 × LFPR 12 cells · LAB-18/19 P×V reproduce 10% / 81% | 0 defects | `14e475502` |

`card_required_check`: all five upcoming cards PRESENT.

**Fixes:** LAB-08 added to the STATUS predictions table (4%, scores as-made 65%, resolves on the Feb-2027 final benchmark) and CLAUDE.md figures corrected (Brier 0.348 n=13, 0-for-6, base rate 0.178, five sub-scripts), both in `a6b9fcc9a`. NEXUS brief Florida row refreshed from the ETA 539 primary at **w/e 2026-10-10**: FL 4-week average `5,434 / 5,941 − 1 = −8.5%` YoY, 8 of 8 weeks below year-ago, national breadth 6 of 51 (`b9ac54128`, re-pinned `dd9c6abb2`, `brief_pin_check` OK-PINNED).

⚠️ **Found while building (not fixed; flagged):** STATUS § KEY THRESHOLDS still prints T-06 as "<100K + U-3 ≥4.3%". The live letter (TRADE.md §1, re-specced 8/7) is U-3 up ≥0.2pp MoM **OR** EPOP down ≥0.3pp/3m, which on the Sep base is U-3 ≥4.4 or EPOP ≤58.6. The NFP card uses the formula. The 10/2 card also omitted the EPOP leg; that print did not reach it. ⚠️ ETA 539 shows FL w/e Oct 10 at 6,014 against DOL's 10/15 advance figure of 5,793, a vintage difference noted on the row.

## COMPLETION — LABOR — 2026-10-21 (cards + fixes)
STATUS: ✅ DONE
CHANGED: AGENTS/LABOR/docket/GRADING_CARD_20261030_ECI.md, _20261103_JOLTS.md, _20261105_Challenger.md, _20261106_NFP.md (new); AGENTS/LABOR/STATUS.md; AGENTS/LABOR/CLAUDE.md; AGENTS/LABOR/NEXUS_BRIEF.md; this memo
RESULT: Four cards frozen before their prints, each naming instrument, source document and observation basis per leg; rules set with no value seen; checker 0 defects on all four; release dates verified at the issuers. LAB-08 now in STATUS; CLAUDE.md Brier 0.342 → 0.348 and four → five sub-scripts; FL brief row refreshed to w/e Oct 10 (−8.5% YoY, breadth 6/51).
GAPS: STATUS T-06 row prints a stale bar (≥4.3%, no EPOP leg); NFP card governs, row not edited (out of scope). JOLTS/NFP cards' LEG C hand-off needs a dated note on 11/3. Not pushed.
WILL_NEEDS: None.
FOLLOW-UP: 10/22 wake grades claims (L719); 11/3 writes LEG C into the NFP card §2.4; repair the STATUS T-06 row at the next session.
