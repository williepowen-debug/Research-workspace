# INSIDERS STATUS
**Updated:** 2026-07-06 (fresh pull via FDIC securities-filings API — 16 new Form 4s since Apr 12)

> ⚠️ **VINTAGE FLAG (2026-08-28 integrity sweep) — this file is PRE-Q2-PRINT and has not been refreshed against it.** Everything below is **Q1-2026-based**; the Q2 print (7/21-22) and the Q2 Call Report (8/7) are **not** reflected. Q2 moved the relevant aggregates materially: classified+criticized **$1,215M→$1,282M**, RESG commitments **$27.8B→$25.7B**, NPA **$446M/1.07%→$589M/1.41%**, OREO **+93%**, NCO **0.56%→0.69%**. **Do not cite figures below as current** — root `STATUS.md` is canonical. *(Flagged, not rewritten: a refresh is real analytical work, not a stamp. This banner is the honest state; silently carrying Q1 figures under a current-looking header is what it replaces — [[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]].)*


## Assessment: 🔴 FULL CONVERGENCE (Score 13) — Maximum bearish signal; **pattern ESCALATING at 7/6 pull**

> ⏰ **Score vintage: 2026-07-06 — 53 days old at the 8/28 sweep.** The FDIC EFR (cert #110) re-pull owed since 7/6 has **not** been run, so "ESCALATING" describes the trajectory *as of early July*, not today. Within the charter's quarterly minimum; the **pre-Q3 window opens ~Oct**. ⚠️ **An unrun pull is no evidence in either direction** — do not read the absence of new filings here as "no insider activity since July."

## Current State
- **🆕 CRO Majumdar sold AGAIN (May 20): 827 @ $48.07 ≈ 24% of remaining** — 2nd discretionary sale in 3 months (Feb 24: 419 = 10.78%); cumulative ~32% lighter since Feb, with the Q2 print + IQHQ maturity inside 90 days. Upgraded from single event to **active de-risking pattern.**
- **🆕 Kenny grant-flip #3 (May 22):** sold 1,500 @ $47.81 = 71% of his 5/18 annual grant (2,113) within 4 days (2024: 86%/7d; 2025: 38%/5wk)
- **🆕 Helen W. Brown (officer, Jun 12):** 401(k) intra-plan transfer OUT of OZK stock — 4,317 @ $52.12, discretionary (16b-3(f)), executed at the June high two weeks before the 7/2 −5.7% drop
- **🆕 Dir. East sold 1,000 (Apr 28)** — ~0.7% of holdings, low signal. **May 18 batch of 12 × 2,113-share grants = routine annual comp** (post-annual-meeting), not signal.
- CFO staged $944K out across two tranches (Oct 2024 + Jan 2025) — before deterioration was public
- Director Whipple exited $5.2M at $51.50 — near the top
- CEO Gleason: ZERO Form 4 filings going back to Jul 2023. Not buying, not selling. Frozen. (Re-confirmed 7/6.)
- **Zero insider buying continues through Jul 6, 2026** — no open-market purchase by any insider on record
- Corporate buybacks occurring ($200M fresh authorization 6/30) but that's shareholder money, not personal conviction
- Institutional: Wellington Mgmt -43%, D.E. Shaw -26%, AQR -20%, Wasatch -6.6% (13F as of 12/31/25; fundamental/credit shops selling, quant/index adding)

## Key Pattern
CRO reduced personal exposure in the same quarter the bank reported ACL cuts + noncurrent doubling — **and did it a second time in May 2026, into the pre-Q2/IQHQ window.** The person assessing credit risk keeps getting lighter while the risk escalates. CFO was already out before the numbers went bad.

## No Departures Identified
Monitoring FDIC EFR for any executive exits, role changes, or board additions pre-earnings. Four new reporting insiders in ~12 months (Kerley, Munn Aug 2025; Majumdar Mar 2025; Fabrega May 2025).

## Data Source Fix (Apr 12; upgraded Jul 6)
**OZK files Form 4 with FDIC, not SEC EDGAR.** Dissolved holding company in 2017. Standard insider tracking tools (OpenInsider, Fintel, etc.) show "no data" for OZK because they scrape EDGAR. Authoritative source: FDIC securities filings — old efr.fdic.gov URL now redirects to **`securitiesfilings.fdicconnect.fdic.gov`**, whose JSON API is fully scriptable: `/api/instdiscl/cert/110` (all Form 3/4/5 records + per-filing transaction lines via `/api/instdiscl/{id}`), `/api/instflng/cert/110` (all company filings — 8-K/10-Q/10-K), and `/api/instflng/{id}/attachment/{n}` (**downloads the actual PDFs**, bypassing the 403'd IR page). See MEMORY Findings 7/6.

## What Changed Last
- **Jul 6:** Fresh pull via API — 16 new Form 4s Apr 12→Jul 6. CRO 2nd sale (827 @ $48.07, 5/20); Kenny grant-flip #3 (1,500 @ $47.81, 5/22); Brown 401(k) exit at $52.12 (6/12); East 1,000 (4/28); 12× annual grants (5/18). Zero buys; Gleason still frozen. Also via filings endpoint: **Q1 2026 10-Q retrieved → `../raw/Q1_2026_10Q.pdf` (UNREAD — queued for Q2 prep)**; no 8-K since May 19 (further confirms no hidden catalyst behind the 7/2 drop). Assessment escalated: CRO single-event → active pattern.
- **Apr 12:** FDIC EFR pull (cert #110) — full Form 4 history reviewed. 18 filings in 2026 YTD, all sells/grants/comp events. Zero purchases. Dir. Kenny full transaction history traced: net seller despite $170K+ in free stock grants. Gleason confirmed zero filings back to Jul 2023. Institutional ownership analysis added (13F Dec 31 2025): Wellington -43%, smart money divergence. Data source gap (FDIC vs EDGAR) identified and documented.
- Mar 24: Created SELLING.md, DEPARTURES.md, TIMELINE.md. Migrated from research/INSIDER_ACTIVITY_COMPILED.md. Timeline overlay reveals CRO gap and CFO window patterns.

## Next
- **Watch the pre-Q2 window:** closes ~Jul 7 (14d before Jul 21 print). Any buying before the print = counter-signal; more selling = pattern confirmation. Re-pull after Jul 21.
- Monitor for 8-K Item 5.02 filings (officer departures) — none since Aug 2025
- Pending: Wellington N-PORT (2026 monthly holdings) — would show if Wellington continued selling; next 13F (Q2) ~mid-Aug
- Pending: identify Helen W. Brown's officer title (proxy) — sizes the 401(k)-exit signal

---

*Detail → `SELLING.md`, `TIMELINE.md` | KB refs → KB-OZK-037 through 041, 093*
