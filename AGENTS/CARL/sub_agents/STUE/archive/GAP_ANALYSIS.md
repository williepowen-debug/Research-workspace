# STUE GAP ANALYSIS
**Generated:** 2026-04-13
**Agent:** STUE (Student Loan Stress Monitor)
**Purpose:** Identify specific missing, stale, or TBD data that a human researcher can go retrieve.

---

## PRIORITY KEY
- **HIGH** — feeds an active prediction or imminent catalyst (Apr-Jul 2026 window)
- **MEDIUM** — enriches existing analysis or confirms an estimate
- **LOW** — nice to have, no active threshold dependency

---

## GAP 1 — Sweet v. McMahon Non-Exhibit C Compliance (CRITICAL / 2-DAY DEADLINE)

**WHAT:** Confirmation of whether DOE issued decisions or notices to non-Exhibit C post-class applicants before the Apr 15, 2026 court deadline. As of Apr 13, no public record exists that any notices were issued. If missed, automatic full relief (discharge + refunds + credit corrections) triggers for this cohort.

**WHERE:**
- PACER docket: N.D. Cal. Case No. 3:19-cv-03674-WHA (now reassigned from Judge Alsup). Search for any DOE filing dated Apr 13-15, 2026. URL: https://ecf.cand.uscourts.gov/
- Student Defense (studentdefense.org) or PPSL (projectonstudentdebt.org) — both track Sweet compliance and post public updates within hours of filings.
- tateesq.com (Student Loan Lawyer Tate) — has been publishing near-real-time Sweet updates; check for any Apr 13-15 post.
- Search: `"Sweet v McMahon" "April 15" site:studentdefense.org OR site:ppsl.org`

**WHY:** STATUS.md flags DOE compliance as "UNCONFIRMED" and the pattern from Jan 28 (DOE missed Exhibit C deadline → auto relief) creates high probability of repeat. This is the single most time-sensitive data gap. Resolution by Apr 15 determines whether a new 🔴🔴 signal goes to PROME. Feeds: TIMELINE.tsv (Apr 15 entry), KB-CARL-183 (proposed).

**PRIORITY: HIGH — 2-day deadline**

---

## GAP 2 — NY Fed Q1 2026 QHDC Release (90+ DQ Threshold Watch)

**WHAT:** Quarterly Report on Household Debt and Credit for Q1 2026 (January–March 2026 data). This is the primary source for the 90+ DQ rate by product and age cohort. Currently stuck at Q4 2025 (9.6%, 0.4pp from the 10% RED threshold defined in CRL-04). Q1 2026 will capture the first full quarter of post-forbearance credit reporting and is expected to show the 10% threshold breach.

**WHERE:**
- NY Fed QHDC page: https://www.newyorkfed.org/microeconomics/hhdc
- Direct report PDFs downloadable from that page. Release cadence: ~8 weeks after quarter end. Q1 2026 ends Mar 31 → expect release late May or early June 2026.
- The associated "Center for Microeconomic Data" blog posts (Liberty Street Economics) often release an advance chart with key metrics. Search: site:libertystreeteconomics.newyorkfed.org "household debt" 2026
- Supplementary data tables (Excel) at the same page include age-cohort breakdowns for 90+ DQ by loan type.

**WHY:** CRL-04 (97% conf) predicts 90+ DQ >10%; the next NY Fed read is the resolution date. VX-CARL-SL-02 current value is 9.6% from Q4 2025 — will be 6+ months stale by the time Q1 data releases. The age cohort breakdown (18-29 cohort at ~21%) will also confirm cascade hypothesis. Feeds: VX-CARL-SL-01, VX-CARL-SL-02, CRL-04.

**PRIORITY: HIGH — resolution read for active prediction**

---

## GAP 3 — FSA Data Center Q1 2026 Portfolio Update (Default Count vs. 10M+ Threshold)

**WHAT:** FSA Data Center quarterly data release for Q1 2026 (Jan–Mar 2026). Current default count is 9.2M (early Mar 2026, via ED press/Treasury Transfer announcement) but this was a spoken figure from an ED official — not the formal FSA portfolio update. The formal Q1 FSA update (~June 2026) will give: default count by repayment status, age, loan type, and servicer; active repayment 31+ DQ rate update; forbearance/IDR enrollment by plan type.

**WHERE:**
- FSA Data Center portal: https://fsapartners.ed.gov/data-center
- Navigate: "Portfolio Summary" → current quarter. Historical releases show Q4 data released ~Mar 13, 2026; Q1 2026 expected ~June 2026.
- Specific tables to pull: "Student Loan Portfolio Summary" (default count row), "Direct Loan Portfolio by Repayment Plan" (shows how many in each plan = critical for RAP enrollment tracking), and "Default Resolution" tables.
- Also check College Investor (thecollegeinvestor.com) and Protect Borrowers (protectborrowers.org) — both publish early summaries when FSA releases.

**WHY:** VX-CARL-SL-05 (Borrowers in Default) threshold is >10M for RED breach. 9.2M already in Mar 2026; +1.5M/90 days pace suggests 10M breach likely before formal release. Will also give first hard data on RAP enrollment rates — directly feeds CRL-13 (SAVE non-selection >35%). Feeds: VX-CARL-SL-05, VX-CARL-SL-06, CRL-13.

**PRIORITY: HIGH — active prediction resolution + threshold watch**

---

## GAP 4 — MOHELA State AG Investigation Enumeration

**WHAT:** SERVICER.tsv row for MOHELA State AG Investigations reads "Multiple states" with a note "States not fully enumerated — need web pull." The file is dated 2025 with no specific state list, count, or complaint type. This is an explicit flagged gap in the workbook.

**WHERE:**
- NAAG (National Association of Attorneys General): naag.org — search for MOHELA or student loan servicer actions
- Individual state AG press releases: Search `"MOHELA" site:ag.ca.gov OR site:ag.ny.gov OR site:oag.dc.gov OR site:ago.mo.gov` (Missouri is MOHELA's home state — Missouri AG is particularly relevant)
- CFPB enforcement database: https://www.consumerfinance.gov/enforcement/ — filter for student loan servicer actions
- Press search: `"MOHELA" "attorney general" 2025 2026` via Bing/Google News
- Protect Borrowers (protectborrowers.org/mohela) maintains a tracker of MOHELA legal actions

**WHY:** The Maldonado ruling (Mar 2026, CA violation) creates legal precedent for other states with similar Student Borrower Bill of Rights statutes (NY, IL, CO, DC, MD have similar laws). Knowing which AGs are active tells us whether MOHELA faces multi-state operational disruption before Jul 1. Feeds: VX-CARL-SL-07, SERVICER.tsv (fills flagged gap).

**PRIORITY: HIGH — MOHELA operational capacity is a direct input to CRL-14 (500K additional defaults)**

---

## GAP 5 — SAVE Non-Selection Rate: Oct 2023 Precedent Granularity

**WHAT:** CRL-13 (SAVE non-selection >35%, 70% confidence) is anchored to "Oct 2023 precedent (20-30% failed to resume)." The CLAUDE.md key thresholds table shows "SAVE Non-Selection Rate | TBD" for current value. The 30-45% estimate in STATUS.md is derived from that Oct 2023 precedent plus MOHELA failure multiplier, but the exact Oct 2023 non-resumption rate and its comparability to Jul 2026 conditions is not documented with a primary source.

**WHERE:**
- Federal Student Aid Press Room: https://studentaid.gov/announcements-events/press-releases — search for "on-ramp" or "2023 payment restart" or "return to repayment"
- TCF (Third Way's College Excellence Program or The Century Foundation — context-check which "TCF" is meant): thecenturyfoundation.org — published multiple reports on the Oct 2023 payment restart with exact non-resumption rates
- Specific search: `"return to repayment" 2023 "failed to resume" OR "non-resumption" site:studentaid.gov OR site:thecenturyfoundation.org`
- NASFAA (nasfaa.org) published granular tracking of 2023 return-to-repayment; they have a searchable archive
- NY Fed blog (Liberty Street Economics): published research on the 2023 restart and who did not resume — cite this for CRL-13's empirical base

**WHY:** CRL-13 is a 70% confidence prediction on a $0→$407/mo payment shock for 2-3.4M borrowers. The analytic foundation (Oct 2023 precedent rate) needs a primary-source citation. Without it, REGINALD cannot use STUE's non-selection estimate in its bank-level impact analysis. Also: current non-selection rate threshold in CLAUDE.md shows "TBD" — this gap prevents VX-CARL-SL-03 from having a measurable current value. Feeds: CRL-13, VX-CARL-SL-03.

**PRIORITY: HIGH — analytic foundation for active prediction**

---

## GAP 6 — AFT v. MOHELA Discovery: Case Docket for May 28 Conference Materials

**WHAT:** AFT/MOHELA case is in discovery phase with next status conference May 28, 2026. The case docket likely contains: the amended complaint (Jan 2026) with MOHELA's abandon rate data (>14%), any discovery scheduling orders, and potentially preliminary discovery findings. The abandon rate figure (>14% vs. 5% max for peers) is cited as coming from "AFT amended complaint / CFPB data" but the docket has not been pulled.

**WHERE:**
- Case: American Federation of Teachers v. MOHELA (confirm full case name and jurisdiction — likely D.C. or E.D. Mo.)
- PACER: https://pacer.gov — search for "American Federation of Teachers" AND "MOHELA" — look for the most recent amended complaint and any scheduling orders
- AFT press room: aft.org/press-release — AFT posts press releases on litigation developments
- Protect Borrowers (protectborrowers.org) tracks AFT litigation closely and often embeds docket links
- Search: `"AFT" "MOHELA" "discovery" 2026 site:aft.org OR site:protectborrowers.org`

**WHY:** May 28 conference is the next STUE catalyst in the dashboard. Discovery could surface new MOHELA failure metrics that update CRL-14. The specific abandon rate (>14%) underpins the operational failure prediction — if discovery produces servicer call log data, this number could be confirmed or revised significantly. Also: any preliminary injunction filing before May 28 would be a 🔴 signal. Feeds: VX-CARL-SL-07, SERVICER.tsv, CRL-14, CARL DANGER WINDOW.

**PRIORITY: HIGH — imminent catalyst with potential for threshold-level findings**

---

## GAP 7 — CFPB Student Loan Ombudsman Annual Report (2025 Edition)

**WHAT:** SERVICER.tsv cites "CFPB Ombudsman 2025" for MOHELA call wait times and CFPB ranking, but with date "2025" — no specific report date, report number, or URL. The CFPB Student Loan Ombudsman releases an annual report each fall covering complaint volume by servicer, issue type, and resolution rate. The 2025 report (covering Oct 2024–Sep 2025 activity) would have the most current servicer performance metrics.

**WHERE:**
- CFPB reports page: https://www.consumerfinance.gov/data-research/research-reports/ — filter by "student loan" or "ombudsman"
- Direct URL pattern: consumerfinance.gov/reports/student-loan-ombudsman-annual-report-[year]/
- The 2024 report (covering FY2024) was released Nov 2024. The 2025 report should be at the same URL with year updated.
- Specific data tables to pull: complaint volume by servicer (Table 1 or equivalent), top complaint categories, and wait time benchmarks by servicer

**WHY:** SERVICER.tsv has MOHELA's CFPB complaint count as "~3,000 (Jul 2022–Sep 2023)" — this is nearly 3 years old. The 2025 report would cover the post-forbearance restart period when MOHELA complaints were described as spiking. The wait time data (7x EdFinancial, 50x Aidvantage) also needs its source document pinned with a specific report date for use in REGINALD-facing analysis. Feeds: SERVICER.tsv (multiple MOHELA rows), VX-CARL-SL-07.

**PRIORITY: MEDIUM — source authentication for existing claims, not new data**

---

## GAP 8 — RAP Enrollment Mechanics: Per-Dependent Deduction Confirmation and Payment Floor

**WHAT:** STATUS.md and VX-CARL-SL-03 state RAP has "$50/mo per-dependent deduction" and "1-10% AGI" with "30-yr forgiveness" — but the payment floor ($10/mo minimum noted in SPAWN1_DATA_REFRESH.md), the exact income band breakpoints within the 1-10% range, and whether the $50/mo deduction applies per dependent per month or as a flat reduction need confirmation from the actual ED Mar 31 guidance text.

**WHERE:**
- ED.gov press releases: https://www.ed.gov/news/press-releases — search for "Repayment Assistance Plan" or "RAP" released Mar 31, 2026
- StudentAid.gov RAP detail page: https://studentaid.gov/manage-loans/repayment/plans/rap (may not exist yet — check)
- Working Families Tax Cuts Act text (statutory authority for RAP): Congress.gov — search for the bill, find the student loan provisions defining RAP payment structure
- NerdWallet or Student Loan Planner published detailed RAP breakdowns in Mar-Apr 2026 — search: `"Repayment Assistance Plan" income tiers 2026`

**WHY:** CRL-13's non-selection estimate (30-45%) depends partly on whether RAP is attractive enough to drive opt-in. If the per-dependent deduction substantially reduces payment for families (e.g., 3 dependents = $150/mo reduction), it might pull non-selection rates down — which would be partial invalidation of CRL-13. Getting the exact mechanics right also matters for the spending destruction estimate ($1.5-2.0B/mo) in STATUS.md. Feeds: CRL-13, VX-CARL-SL-03, TIMELINE.tsv Jul 1 entry.

**PRIORITY: MEDIUM — analytic precision for active prediction**

---

## GAP 9 — State-Level DQ: Current Post-Forbearance Rates (FL, TX, MD Priority States)

**WHAT:** STATE_DQ.tsv lists estimated current DQ rates for all 17 states using pre-forbearance CDR data plus structural assumptions. All "Est_Current_DQ" values are marked as estimates derived from "FSA CDR / STRUCTURAL" — there is no post-forbearance measured state-level DQ. The three CARL priority states (FL, TX, MD) are most urgent.

**WHERE:**
- FSA Data Center "Default by State" table: https://fsapartners.ed.gov/data-center — this table shows borrower counts by state and default status. It updates quarterly. Pull the Dec 2025 release for FL, TX, MD.
- Education Data Initiative (educationdata.org/student-loan-debt-by-state) — aggregates FSA data with state breakdowns; updated periodically
- Urban Institute (urban.org) — published post-forbearance state-level student loan stress analysis in 2025
- For MD specifically: The PSLF concentration in MD is unique. FSA Data Center has a PSLF table showing approved vs. denied applications by state — pull MD data to confirm the DOGE/PSLF destruction angle.
- Search: `FSA "default by state" 2026 OR 2025 filetype:xlsx` (FSA often posts Excel supplemental data)

**WHY:** FL (CARL V7 triple overlap), TX (2nd largest portfolio, border community subprime), and MD (DOGE double-hit + PSLF destruction) are the states most likely to produce the first regional stress signals. Current estimated ranges (FL: 16-20%, TX: 17-21%, MD: 15-20%) are structurally derived, not measured. Actual data could show these are underestimates. Feeds: STATE_DQ.tsv, CARL's regional stress thesis.

**PRIORITY: MEDIUM — enriches existing estimates with measured data**

---

## GAP 10 — FICO Spring 2026 Credit Insights: Primary Source Document

**WHAT:** VX-CARL-SL-08 and multiple KB entries cite "FICO Spring 2026 Credit Insights" for: national avg FICO at 714, -62 pts avg for DQ borrowers, Gen Z 14.4% with -50pt+ drops, and 7M+ new DQ reports in 2025. The report is cited as "released Mar/Apr 2026" but no URL, report date, or direct download link is recorded.

**WHERE:**
- FICO newsroom: https://www.fico.com/en/newsroom — search for "credit scores" or "Spring 2026" or "credit insights"
- FICO Scores blog: https://www.fico.com/blogs/credit-scoring — the Credit Insights report often has an accompanying blog post with the full breakdown
- Experian, Equifax, TransUnion also partner with FICO on annual/semi-annual score distribution reports — if the FICO direct source is paywalled, check Experian's annual "State of Credit" report (experian.com/blogs/ask-experian/state-of-credit/)
- Search: `"FICO" "Spring 2026" "credit insights" OR "average score" "714"` — this will surface the exact press release or report

**WHY:** This is the primary empirical source for the credit cascade confirmation. Multiple KB entries and VX vectors reference it with no URL. If the report is challenged or if numbers are cited in a future PROME/REGINALD cross-check, STUE needs to point to a primary document. The -62 pts average and 714 national average are load-bearing numbers in the cascade thesis. Feeds: VX-CARL-SL-04, VX-CARL-SL-08, KB-CARL-181 (proposed).

**PRIORITY: MEDIUM — source authentication for most-cited new data point**

---

## GAP 11 — Nelnet Credit Report Error Class Action: Case Name and Status

**WHAT:** SERVICER.tsv lists Nelnet with "Credit Report Errors — Balance duplication" dated Feb 2026, sourced to "Court filing/class action." No case name, court, or docket number is recorded. Nelnet is the second-largest servicer (~5.6M accounts). The balance duplication error (if similar in scale to MOHELA) represents a separate manufactured-DQ risk.

**WHERE:**
- PACER: https://pacer.gov — search for class action filings against "Nelnet" in 2026
- Law360 or Courtroom View Network (CVN) — monitor student loan servicer class actions
- Search: `"Nelnet" "class action" "balance" "credit report" 2026` — the same plaintiffs' law firms that filed against MOHELA (like Tycko & Zavareei) often file parallel actions against other servicers
- The Feb 18, 2026 MOHELA class action (doubled balances) may have named Nelnet as co-defendant — check that filing specifically

**WHY:** If the Nelnet errors approach MOHELA scale, VX-CARL-SL-07 (Servicer Failure) should expand beyond MOHELA. More importantly, combined servicer failures before Jul 1 would significantly raise the confidence on CRL-14 (>500K MOHELA-caused defaults). Feeds: SERVICER.tsv (Nelnet rows), VX-CARL-SL-07.

**PRIORITY: MEDIUM — scope assessment for servicer failure vector**

---

## GAP 12 — Treasury Transfer Phase 2 Timeline and Legal Challenges

**WHAT:** VX-CARL-SL-06 and TIMELINE.tsv show Phase 1 (defaulted borrowers, 9.2M) transferred Mar 19. Phase 2 (non-defaulted portfolio) and Phase 3 (FAFSA) are noted as "planned" with no dates. The legal challenge is noted as "5 Senate committee ranking members demand rescission" but no court filings, GAO review requests, or administrative law challenges are enumerated.

**WHERE:**
- Congressional letters: Senate HELP Committee and Senate Finance Committee — committee press rooms list formal letters sent to ED/Treasury. Search: `site:help.senate.gov OR site:finance.senate.gov "student loan" "Treasury" 2026`
- GAO: gao.gov — any open GAO review of Treasury transfer authority would be listed in their "active work" tracker
- Federal Register: federalregister.gov — any rulemaking or administrative order related to Treasury transfer. Search: "student loan" "Department of Treasury" 2026
- Higher Ed news: Inside Higher Ed (insidehighered.com) and Chronicle of Higher Education (chronicle.com) have tracked Treasury transfer extensively; both have published timelines

**WHY:** If Phase 2 is announced (non-defaulted borrowers transferred to Treasury), it would represent a major operational disruption for 30M+ borrowers coinciding with the Jul 1 SAVE transition. A legal injunction could pause collections restart. This is a key uncertainty in the Jul 2026 compound stress scenario. Feeds: VX-CARL-SL-06, TIMELINE.tsv (Phase 2 entry).

**PRIORITY: LOW — no imminent deadline, but Phase 2 announcement would be material**

---

## GAP 13 — MOHELA Accounts Serviced (Current Count Post-Transfer)

**WHAT:** SERVICER.tsv shows MOHELA servicing "~16.5M accounts" dated 2025. Phase 1 of the Treasury Transfer moved 9.2M defaulted borrowers to Treasury collections management. If any of those 9.2M were in MOHELA's portfolio, MOHELA's account count has changed. The operative count matters for Jul 1 operational capacity analysis.

**WHERE:**
- FSA Data Center "Portfolio by Servicer" table: https://fsapartners.ed.gov/data-center — this table shows loan balance and borrower count by servicer; updated quarterly
- ED press releases around Treasury Transfer Phase 1 (Mar 19, 2026) may have specified which servicers' defaulted accounts were transferred
- National Student Loan Data System (NSLDS): ED.gov — not public, but press accounts of the transfer may break down by servicer

**WHY:** MOHELA's operational burden for Jul 1 transition is a direct input to CRL-14. If its effective non-defaulted account count is significantly lower (e.g., 10-12M vs. 16.5M), the Jul 1 load is lower — but its operational track record remains disqualifying. More importantly: if MOHELA lost defaulted accounts to Treasury, its servicing revenue drops, potentially accelerating operational deterioration. Feeds: SERVICER.tsv, CRL-14.

**PRIORITY: LOW — refines existing estimate, not a threshold input**

---

## SUMMARY TABLE

| Gap | Metric | Priority | Why It's Time-Sensitive |
|-----|--------|----------|------------------------|
| GAP 1 | Sweet v. McMahon Apr 15 compliance | **HIGH** | 2-day deadline; auto relief if missed |
| GAP 2 | NY Fed Q1 2026 QHDC (90+ DQ) | **HIGH** | CRL-04 resolution read; 10% threshold watch |
| GAP 3 | FSA Q1 2026 portfolio update | **HIGH** | 10M default threshold + RAP enrollment data |
| GAP 4 | MOHELA State AG list | **HIGH** | Operational capacity for CRL-14 |
| GAP 5 | Oct 2023 non-resumption rate (primary source) | **HIGH** | CRL-13 analytic foundation |
| GAP 6 | AFT v. MOHELA discovery docket | **HIGH** | May 28 catalyst; abandon rate confirmation |
| GAP 7 | CFPB Ombudsman Annual Report 2025 | **MEDIUM** | Source authentication; complaint volume update |
| GAP 8 | RAP mechanics (ED Mar 31 guidance text) | **MEDIUM** | CRL-13 precision; spending destruction estimate |
| GAP 9 | State-level DQ: FL, TX, MD measured rates | **MEDIUM** | Replace structural estimates with FSA data |
| GAP 10 | FICO Spring 2026 Credit Insights URL | **MEDIUM** | Primary source authentication |
| GAP 11 | Nelnet class action case name/status | **MEDIUM** | Scope of servicer failure vector |
| GAP 12 | Treasury Transfer Phase 2 timeline + legal | **LOW** | Jul 2026 compound stress scenario |
| GAP 13 | MOHELA current account count post-transfer | **LOW** | Refines CRL-14 load estimate |

---

## STALE DATA FLAGS

The following are explicitly stale and should be replaced when the above gaps are filled:

| File | Row/Field | Current Value | Stale Since | Replacement Source |
|------|-----------|---------------|-------------|-------------------|
| SERVICER.tsv | MOHELA CFPB Complaints | ~3,000 (Jul 2022-Sep 2023) | Sep 2023 | CFPB Ombudsman Annual Report 2025 (GAP 7) |
| SERVICER.tsv | MOHELA State AG investigations | "Multiple states" (no enumeration) | 2025 | State AG press rooms + NAAG (GAP 4) |
| SERVICER.tsv | MOHELA Accounts Serviced | ~16.5M (2025) | Mar 2026 | FSA Portfolio by Servicer (GAP 13) |
| SERVICER.tsv | Most rows dated "2025" | Various | Dec 2025 or earlier | Per-gap sources above |
| STATE_DQ.tsv | Est_Current_DQ (all states) | Structural estimates | Pre-2026 | FSA Data Center by State table (GAP 9) |
| VX-CARL-SL-01 | 30+ DQ Rate (16.3%) | Q4 2025 | Mar 31 2026 | NY Fed Q1 2026 QHDC (GAP 2) |
| VX-CARL-SL-02 | 90+ DQ Rate (9.6%) | Q4 2025 | Mar 31 2026 | NY Fed Q1 2026 QHDC (GAP 2) |
| CLAUDE.md thresholds | SAVE Non-Selection Rate "TBD" | TBD | Never set | Oct 2023 precedent primary source (GAP 5) |

---

*STUE sub-agent of CARL. This file is for human researcher use — actionable sources only.*
