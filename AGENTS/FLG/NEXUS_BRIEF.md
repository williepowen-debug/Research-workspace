# FLG — NEXUS Brief

**Status:** 🔴 v1.0.3 — FLG's $2.8B non-accrual book carries a 5.8% specific reserve and exits only through an outside refinance market

**Domain:** Flagstar Bank, N.A. (one entity since 10/2025) — NYC rent-regulated multi-family → CRE concentration → non-accrual formation → reserve adequacy → capital. Single name; cohort view = REGINALD.

**Thesis version:** v1.0.3 (`THESIS.md`)

**Recent thesis pivot:** v1.0 → v1.0.3 (10/22) — corrections only. Most recent material view shift: concentration read as deterioration → **level-high, trajectory de-risking** (8/20). The live signal is the reserve and the exit channel, not the 327.5% ratio.

**As of:** 2026-10-28 22:5x ET | STATUS commit: `b57347b5b` — event-driven desk; this brief stands until the next print or owner session.

---

## CROSS-DOMAIN

**SENDING:**
| To | Signal | Priority | Mechanism it triggers in recipient's domain |
|----|--------|----------|---------------------------------------------|
| REGINALD | Non-accrual roll-forward (13 filings): cure share 59.5% (2023H1) → 1.6% (2026H1); payoff/disposition 87.5%. Roll-forward is an FR Y-14Q item, non-public; the cohort base rate cannot be built | 🟠 | FLG's exit-channel dependence cannot be ranked against peers; matrix credit leg reads levels, not flows |
| REGINALD | SR 07-1 at 327.5% (2026Q2, total RBC basis) carries ~11pp of merger basis at 2025Q4; Q3 buyback pushes the ratio ~+7pp (ESTIMATE; Call Report ~11/14 grades) | 🟡 | The path below 300% slows. The −143pp headline is not all de-risking |
| NEXUS | M-05 / R10 inputs: FLG RED [10/23]. Coverage 30.85% (Q3 release, derived) is a series low; specific reserve 5.8% of non-accrual | 🔴 | Named-regional CRE level fire stays lit; recognition row = reserve, not provision |
| CREED | NYC rent-regulated multi-family is the issuer-named credit-cost driver; 2027 MF reset $8.4B incl. $2.9B ≥50% rent-regulated (call, 10/23, B2) | 🟡 | Volume of rent-regulated refinancings meeting the frozen-rent DSCR in 2027 |

**WAITING FOR:**
| From | Input | Expected by | Why it matters | How it changes my view |
|------|-------|-------------|----------------|------------------------|
| EDGAR (issuer) | Q3-2026 10-Q | Mon Nov 9 (observed +37d lag; [EST]) | Grades FLG-02 and FLG-03; carries non-accrual roll-forward, FDM tables, maturity table | Formation > outflow or cure share < 2% again → stance holds; new specific reserve build → coverage leg softens |
| FFIEC CDR | Q3-2026 Call Report, RSSD 694904 | Sat Nov 14 (+45d rule) | SR 07-1 recompute; closes the MDRM MIRROR residual | Ratio vs 300% line; buyback effect measured, not estimated |
| NY Supreme Court (Will's browser via PROME) | Kenilworth v. RGB merits ruling | Open — judge said "before the end of the year" | Freeze vacated = mechanism input reverses | Vacatur → lowers the 2027–28 DSCR stress; upheld → the 2028-Q2 fuse (T-11) stands |
| REGINALD | Cohort read on Q3 problem-loan / coverage pattern | Open — its 11/07 re-score | Whether FLG is an outlier or the cohort's leading edge | Cohort-wide → the stance is a sector call, not single-name |

---

## VIEW

- **Start from the specific reserve, not coverage.** $163M = 5.8% of non-accrual (6/30, 10-Q); $1,571M carries no allowance on management's collateral claim. Total ACL $869M flat in Q3 while non-accrual rose to $2,817M → coverage 30.85% (derived).
- **The book churns, it does not drain.** H1-2026 gross formation $780M replaced 81.7% of outflow; 87.5% of outflow left by payoff/disposition, 1.6% by cure (n=13 filings). The call says exits clear at 1–5% of the mark (B2) — loss vs carrying value, not vs par.
- **Capital went out while the reserve stayed flat.** ~$216M buyback in Q3 (derived), CET1 13.16% → 12.38%. Buybacks paused in Q4, resume in 2027 (call), which is the wall year.
- **The wall is 2027.** MF $8,503M (31.6% of the book) reprices or matures in 2027 into the freeze effective 10/2026; the first borrower financials carrying most of a freeze year review at Q2-2028 (T-11).
- **Counterevidence:** concentration and the non-accrual LEVEL are improving (SR 07-1 down 11 straight quarters; NAL rate 4.90% → 4.55%). The bank is shrinking MF and growing C&I (+$2.0B in Q3).

---

## CALIBRATION

- **Conviction:** direction-H · timing-L · level-M
- **Diverge from market by:** market trades the miss and the 2028 slip; this desk's claim is narrower — the reserve is thin against loans whose only exit is an outside refinance market the freeze is pricing against. No probability-vs-market figure held.
- **Cross-agent tensions known to me:** None active this cycle.
- **Uncertain about:** (1) who finances the buyers of exiting loans — undisclosed, call silent (issuer / 10-Q); (2) the par-basis loss at exit (10-Q); (3) the freeze ruling (court, via Will).
- **Failure patterns:** proposing a kill form before base-rating it (K-3, six candidates retired); share-graded vintage test (KB-049) — see `workbook/PREDICTIONS.tsv` header and STATUS § SECOND PASS.
- **RED counter-frame:** deleveraging + 12.38% CET1 absorb the losses at 1–5% of marks. Response: that holds while the payoff channel works; the kill leg K-3 is **UNSET** (cure-share candidate retired 8/28), so no falsifier is held there — do not infer one.

---

## NEXT DECISION POINT

- **What:** grade FLG-02 (coverage at 9/30 < 31.04%, 10-Q basis, 65%) and FLG-03 (MF HFI at 9/30 < $26,931M, 88%); both PREVIEW HIT from the release. Re-derive the EXIT_PROTOCOL in both directions and fold KB-071..097 into THESIS.
- **When:** Q3 10-Q, check Mon Nov 9 (T-02).
- **What would falsify the trigger:** a specific reserve build that lifts coverage on the 10-Q basis to ≥31.04% (FLG-02 MISS); FLG-02 grades on the 10-Q basis only — the Call Report basis flips it.

---

## FORWARD CATALYSTS (next 2-4 weeks)

| Date | Event | Threshold / Signal |
|------|-------|---------------------|
| 🔴 ~Nov 6–9 | Q3 10-Q (see NEXT DECISION) | FLG-02, FLG-03; roll-forward formation vs outflow; FDM subsequent defaults (T-13, deadline Nov 13) |
| 🟠 ~Nov 14 | Q3 Call Report | SR 07-1 vs 300%; ≥10pp coverage move or 300% cross → REGINALD + PROME 🔴 |
| 🟡 by Dec 31 | Rent-freeze merits ruling (T-12) | Vacatur = mechanism input reverses |
