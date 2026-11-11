# FLG — NEXUS Brief

**Status:** 🔴 v1.0.5 — FLG's $2.8B non-accrual book carries a 5.5% specific reserve; both graded calls hit, but Q3 cures jumped to 56% of outflow, cause undisclosed

**Domain:** Flagstar Bank, N.A. (one entity since 10/2025) — NYC rent-regulated multi-family → CRE concentration → non-accrual formation → reserve adequacy → capital. Single name; cohort view = REGINALD.

**Thesis version:** v1.0.5 (`THESIS.md`)

**Recent change:** 11/11 catch-up — no change to any graded item: Q3 Call Report re-pulled, unamended (SR 07-1 322.11%); a December hike barely moves NII (+0.68% per +100bp short rates, issuer) and AOCI sits outside regulatory capital; the hike matters through refinancing (5Y 4.81 / 10Y 4.98 [11/10]), no rate relief for $12B of sub-3.9% resets through 2027 (INFERRED). Prior: v1.0.5 (11/07) — Q3 10-Q: FLG-02 and FLG-03 HIT, direction unchanged, "nothing is healing" withdrawn as a flat claim after Q3 cures $144M. Rail re-derived, no condition changed. The live signal is the reserve and the exit channel, not the 322.11% ratio.

**As of:** 2026-11-11 10:17 ET | STATUS commit: `fa9e28efe4` — event-driven desk; this brief stands until the next print or owner session.

---

## CROSS-DOMAIN

**SENDING:**
| To | Signal | Priority | Mechanism it triggers in recipient's domain |
|----|--------|----------|---------------------------------------------|
| REGINALD | Non-accrual roll-forward (13 filings): cure share 59.5% (2023H1) → 1.6% (2026H1); payoff/disposition 87.5%. Roll-forward is an FR Y-14Q item, non-public; the cohort base rate cannot be built | 🟠 | FLG's exit-channel dependence cannot be ranked against peers; matrix credit leg reads levels, not flows |
| REGINALD | SR 07-1 **322.11% at 9/30** (327.52% at 6/30; Call Report, total RBC basis, FLG pull 11/01): buyback lifted it ~+6.6pp, CRE run-off −3.61% more than offset. M3 +54% funded = +12% with unused lines; M3 line not disclosed in the 10-Q. Private-credit slice $1,069M → $2,139M: new lending better supported, ~$0.5B recode from C&I open | 🟡 | The path below 300% continues, slower. M3 step is composition, not hidden loss |
| NEXUS | M-05 / R10 inputs: FLG RED [10/23]. Coverage 30.85% (10-Q) is a series low; specific reserve 5.5% of non-accrual | 🔴 | Named-regional CRE level fire stays lit; recognition row = reserve, not provision |
| CREED | NYC rent-regulated multi-family is the issuer-named credit-cost driver; 2027 MF reset $8.4B incl. $2.9B ≥50% rent-regulated (call, 10/23, B2) | 🟡 | Volume of rent-regulated refinancings meeting the frozen-rent DSCR in 2027 |

**WAITING FOR:**
| From | Input | Expected by | Why it matters | How it changes my view |
|------|-------|-------------|----------------|------------------------|
| EDGAR (issuer) | FY2026 10-K | ~2027-03-01 (FY2025 filed 2/27) | Grades FLG-01; Q4 roll-forward; default full-year row | Q4 cures back under 10% of outflow → Q3 was a lump; second high quarter → repair read opens, cure cause still needed |
| FFIEC | Q4 Call Report Memo 10, 1763, J457 | ~2027-02-14 | Narrows the private-credit recode question | All rising again argues against recoding |
| NY Supreme Court, via press or filings only (docket read dropped by Will 11/10, WQ-477) | Kenilworth v. RGB merits ruling | Open — judge said "before the end of the year" | Freeze vacated = mechanism input reverses | Vacatur → lowers the 2027–28 DSCR stress; upheld → the 2028-Q2 fuse (T-11) stands |
| REGINALD | Cohort read on Q3 problem-loan / coverage pattern | Open — its 11/07 re-score | Whether FLG is an outlier or the cohort's leading edge | Cohort-wide → the stance is a sector call, not single-name |

---

## VIEW

- **Start from the specific reserve, not coverage.** $155M = 5.5% of non-accrual (9/30, 10-Q); $1,548M carries no allowance on management's collateral claim. Total ACL $869M flat in Q3 while non-accrual rose to $2,817M → coverage 30.85%. Flat hides MF + CRE reserve −$24M, C&I +$20M.
- **The book churns; Q3 changed the exit mix.** 9M gross formation $1,053M replaced 87.0% of outflow. H1 outflow 87.5% payoff, 1.6% cure; Q3 *derived* 29.7% payoff, **56.3% cure ($144M)**. Class and cause undisclosed; a cure after a rate cut is not a recovery (INFERRED). MF criticized + classified +$483M in Q3. The call says exits clear at 1–5% of the mark (B2) — loss vs carrying value, not vs par.
- **Capital went out while the reserve stayed flat.** ~$216M buyback in Q3 (derived), CET1 13.16% → 12.38%. Buybacks paused in Q4, resume in 2027 (call), which is the wall year.
- **The wall is 2027.** MF $8,519M (9/30) reprices or matures in 2027 into the freeze effective 10/1/26; the first borrower financials carrying most of a freeze year review at Q2-2028 (T-11).
- **Counterevidence:** concentration and the non-accrual LEVEL are improving (SR 07-1 down 12 straight quarters to 322.11% at 9/30; NAL rate 4.90% → 4.55%). The bank is shrinking MF (−3.56% in Q3) and growing C&I (+$2.0B in Q3); total loans up two quarters is mix shift.
- **Pipeline (Q3 Call Report):** MF 30–89 days past due $233M → $392M (+68%; Q1 $676M, n=3 — watch, not trend); bank net income $34.5M → $12.1M.

---

## CALIBRATION

- **Conviction:** direction-H · timing-L · level-M
- **Diverge from market by:** market trades the miss and the 2028 slip; this desk's claim is narrower — the reserve is thin against loans whose only exit is an outside refinance market the freeze is pricing against. No probability-vs-market figure held.
- **Cross-agent tensions known to me:** None active this cycle.
- **Uncertain about:** (1) what the $144M Q3 cure was — undisclosed; (2) who finances the buyers of exiting loans — undisclosed, 10-Q silent; (3) the par-basis loss at exit; (4) the freeze ruling (court, via Will).
- **Failure patterns:** proposing a kill form before base-rating it (K-3, six candidates retired); share-graded vintage test (KB-049) — see `workbook/PREDICTIONS.tsv` header and STATUS § SECOND PASS.
- **RED counter-frame:** deleveraging + 12.38% CET1 absorb the losses at 1–5% of marks. Response: that holds while the payoff channel works; the kill leg K-3 is **UNSET** (cure-share candidate retired 8/28), so no falsifier is held there — do not infer one.

---

## NEXT DECISION POINT

- **What:** grade FLG-01 (H2 formation < $600M; Q3 $273M, so Q4 < $327M) and read Q4 cures; next dated test of every rail leg.
- **When:** FY2026 10-K ~2027-03-01 (T-02).
- **What would falsify the trigger:** nothing grades before the filing; a slip is STUCK, never MISS.

---

## FORWARD CATALYSTS (next 2-4 weeks)

| Date | Event | Threshold / Signal |
|------|-------|---------------------|
| 🟡 by Dec 31 | Rent-freeze merits ruling (T-12) | Vacatur = mechanism input reverses |
