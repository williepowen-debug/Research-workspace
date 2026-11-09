# 2026-11-10 lookup: CoreWeave Q3 and TSMC October, pre-stated before either print

**Written:** 2026-11-09 11:18 ET (by `date`), before either print. PROME commission 2026-11-09 (Will 11:14 ET). Nothing here changes a registered criterion; it restates `workbook/PREDICTIONS.tsv` VULCAN-188 and VULCAN-191 as tables and adds pre-stated handling for ambiguous wordings. Where the rows and this sheet disagree, the rows win.

## A. TSMC October revenue (VULCAN-188, resolves by 11/16, P = 0.60)

**Where:** EDGAR CIK 0001046179, 6-K with `tsm-revenue<YYYYMMDD>.htm` (month from reportDate). Last year's October 6-K filed 2025-11-10. Run from root: `.venv/bin/python AGENTS/VULCAN/tools/tsmc_watch.py`. Grade `rev_ntd_mn` for revenue_month 2026-10-31 as first published, NT$ million.

| October revenue (NT$mn) | VULCAN-188 | Monthly YoY vs Oct-2025 367,473 | S4 band (monthly legs) |
|---|---|---|---|
| ≥ 570,630 | **TRUE** | ≥ +55.3% | no stress |
| 559,330 to < 570,630 | **NO-VERDICT** | +52.2% to +55.3% | no stress |
| 374,823 to < 559,330 | **FALSE** | +2.0% to +52.2% | no stress |
| 367,473 to 374,822 | FALSE | 0 to +2% | **orange (flat)** |
| < 367,473 | FALSE | < 0 | **red (decline)** |

Arithmetic, frozen at registration: Q4 guide midpoint US$53.3B × 31.8 NT$/US$ ÷ 3 = NT$564,980mn; TRUE line +1%, FALSE line −1%. September was 511,857; TRUE needs October m/m ≥ +11.5%, NO-VERDICT starts at +9.3%.

**Separate fact, not graded by VULCAN-188 — the cumulative:** Jan–Sep 2026 cumulative YoY +41.1% (3,898,727 vs 2,762,964). The tool compares TSMC's stated Jan–Oct YoY with the stored 41.1. October below **NT$518,320mn** makes it tick down (stated YTD below 41.10%). ⚠️ One tick-down is **not** yellow: the tool needs a run of 2 consecutive months (`DECEL_MIN_RUN`, current run 0), so October alone cannot set S4 yellow; it would print `no-stress(cum ticked down … run=1 <2mo)`. Cite the cumulative, not the monthly.

**If FALSE:** record that the quarter started below the guide's pace; read November and December before any S4 demand claim. A slow first month is not a decline. **If TRUE:** same restraint. No score moves on this row either way. No 6-K by 11/16 ⇒ leave OPEN and date the slip.

## B. CoreWeave Q3 (VULCAN-191, resolves by 11/16, P = 0.35, contrarian)

**When:** Tuesday 11/10, call 5:00 PM ET (issuer-confirmed). Guidance is given on the call only; the press release will not carry it.
**Grade on:** issuer-posted transcript or deck if one exists, else two independent relays that agree. **Series:** management's stated FY2026 capital expenditure range, US$ billions, midpoint.
**Baseline confirmed 11/9** by two agreeing relays [KB-412]: $35–39B, midpoint $37.0B (raised from $31–35B at Q2, 8/11). Same relays: Q3 capex guide $11.5–13.5B.

| Stated FY2026 range | Midpoint | VULCAN-191 |
|---|---|---|
| e.g. $33–38B, $34–38B, $32–36B | < 36.5 | **TRUE** (a cut) |
| e.g. $35–38B, $35–39B, $36–38B | 36.5 to < 37.5 | **NO-VERDICT** |
| e.g. $36–39B, $37–40B | ≥ 37.5 | **FALSE** |
| no FY2026 figure stated | — | **VOID** |

**Pre-stated handling of wordings, so tomorrow is a lookup:**
1. A single figure ("about $36B") is its own midpoint.
2. "Toward the low end of $35–39B" with no new range restates the old range: grade 37.0, NO-VERDICT, and record the language as a disagreement beside the grade, never as the grade.
3. A range given on a new basis (e.g. excluding or including customer-funded or financed equipment) is graded as stated; the basis change is recorded beside it. Do not convert it.
4. A FY2027 figure with no FY2026 restatement: VOID for this row; log the 2027 figure separately.
5. The reason is recorded, not graded: late sites, funding, or better purchasing all grade the same.

**If TRUE:** read the stated reason, packet BROCK and LIQUID. A developer capex cut is not the S1 hyperscaler branch and no S5 letter keys on it. **If FALSE:** the delay reading has no support at this print; the weak-link read continues on funding and backlog.

**Context reads at the same print (not graded by VULCAN-191), from the CATALYSTS row:** backlog (6/30: $104.2B, relay), Q3 actual capex vs the $11.5–13.5B guide (below the range is a delay hint, context only), DDTL draws and margins, delay discounts or the accepted-capacity share (DDTL 4.0 clause (c)), customer concentration and Microsoft's share of revenue, expiry of older contracts, any non-renewal or oversight language [KB-400], funding gap, any new financing.

**What could move a VULCAN score from this print (each needs its letter, not the mood):**
- **S5:** a CoreWeave new issue PULLED or flexed ≥ +150bp vs talk; a developer failing to post mandated collateral. Earnings language alone does not.
- **S3:** a named contracted build losing FIRM grid capacity (WATT co-owns). A delay is not a removal.
- **VULCAN-13 (grades 11/15, developer form, WQ-608 A):** leg (b) a like-for-like facility priced ≥ 50bp wider than its own predecessor, or leg (c) tighter covenants than the predecessor, filing-primary. The 10-Q (window typical 11/12, latest 11/13) is the likelier primary than the call.
- **S1:** nothing at CoreWeave; S1's capex branch is the hyperscalers'.

## C. Other 11/10 clocks (ZHAO owns; read separately, never one "11/10 cliff")

- **BIS Affiliates Rule:** stay extension published 11/9, 91 FR 70789 (FR Doc. 2026-22793) [KB-411]. Does not widen 11/10; next window 2027-01-10 to 01-11. The 11/10 CATALYSTS row is swept.
- **MOFCOM:** ~~not re-suspended as of 11/8 per ZHAO~~ (struck 2026-11-09 12:59 ET): re-suspended 11/9 by MOFCOM-GAC 公告2026年第58号, from 11/11 to 2027-01-10, same six 2025 announcements (ZHAO A1) [KB-413]. Nothing reactivates; ZHAO grades ZHA-19 and ZHA-20 on their own letters.
- **USTR s.301 ship fees:** ~~OPEN~~ (struck 2026-11-09): FR Doc. 2026-22867 suspends them through 11:59 p.m. ET 2027-01-09, on public inspection 11/9, publishes 11/10 [KB-413]. Not on S4's letter.
