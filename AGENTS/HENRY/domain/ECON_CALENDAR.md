# Economic Release Calendar — HENRY's Watch

**Purpose:** Flag surprises vs consensus on release mornings. Translate to rate path → bank NIM → regional repricing.

**Action on release days:** log actual vs consensus vs prior in `STATUS.md` (Data Release Protocol, `CLAUDE.md`). Cross-agent threshold fires route as SIGNALS via WALTER.

**Window verified:** 2026-11-19 → 2026-12-23, rebuilt 2026-11-19 ~12:3x ET (prome-36 second touch, during the hold). **Read today at the agency:** BEA news schedule (page last modified 11/19/26) and the Federal Reserve FOMC calendar (last update 11/18/26). **Not readable today:** bls.gov returned HTTP 403 to this box on its November and December schedule lists (a block; not evaded, per root Data Hygiene), so the BLS dates below are the 10/21 reads at the BLS page, labelled; the Census list view showed only January 2027 onward, so Census rows for this window are the 10/21 read or marked UNVERIFIED. ISM dates are its business-day pattern only. **Rebuild before 2026-12-21**, or it is stale again. Prior window (2026-10-22 → 11-25, rebuilt 10/21) and its rows: `git log -p -- AGENTS/HENRY/domain/ECON_CALENDAR.md`.

**Standing context lives in `STATUS.md`, not here.** This file is the schedule only, so it cannot carry a stale regime read.

---

## NEXT ~30 DAYS (all times ET)

| Date | Time | Release | Data for | Source (basis) | Why it matters to HENRY |
|------|------|---------|----------|--------|-------------------------|
| Thu Nov 19 | 8:30 | Initial claims; Philadelphia Fed (printed: claims 203K; Philly 6.3) | Nov | DOL / Philadelphia Fed (printed) | LABOR / ISHM grade |
| Fri Nov 20 | — | **Monthly options expiry (SPX/SPY third Friday)** | — | calendar | About 40% of the ≤35d short dealer gamma at 7,204 rolls off (12:17 ET map) |
| Fri Nov 20 | 8:30 | BEA: Activities of US multinational enterprises, 2024 | 2024 | BEA (read 11/19) | — |
| Fri Nov 20 | 10:00 | State employment | Oct | BLS (read 10/21) | Florida read (CORAL/MARCO) |
| Fri Nov 20 | 10:00 | U. Michigan consumer sentiment, final | Nov | UMich 2026 release-date PDF (read 11/11) | Inflation expectations; CARL owns the consumer read |
| **Wed Nov 25** | 8:30 | **GDP second estimate + corporate profits, Q3** | Q3 | BEA (read 11/19) | Profits |
| **Wed Nov 25** | 8:30 | **Personal Income and Outlays (PCE)** | Oct | BEA (read 11/19) | Core PCE vs >0.3% hot line |
| Wed Nov 25 | 8:30 / 10:00 | Durable goods (advance); new home sales | Oct | Census (read 10/21; not re-read 11/19) | Capex orders; rates transmission |
| Thu Nov 26 | — | Thanksgiving, markets and agencies closed | — | — | — |
| Fri Nov 27 | — | US equity early close (13:00 ET) | — | NYSE holiday schedule (pattern) | Thin tape |
| Tue Dec 1 | 10:00 | ISM Manufacturing | Nov | ISM pattern (1st business day; not read) | ISHM grades; prices >75 red |
| Wed Dec 2 | 8:30 | BEA: GDP and personal income by county, 2025 | 2025 | BEA (read 11/19) | — |
| Thu Dec 3 | 10:00 | ISM Services | Nov | ISM pattern (3rd business day; not read) | Prices vs demand |
| **Fri Dec 4** | 8:30 | **Employment Situation (payrolls)** | Nov | BLS (read 10/21; 403 on 11/19) | LABOR owns; HENRY logs the market reaction |
| Fri Dec 4 | 10:00 | U. Michigan sentiment, preliminary | Dec | UMich PDF (read 11/11) | Inflation expectations |
| Tue Dec 8 | 8:30 | Trade balance | Oct | BEA (read 11/19) | — |
| **Tue–Wed Dec 8–9** | 14:00 Wed | **FOMC with projections** | — | Fed calendar (read 11/19) | HEN-63 (hike, 0.70) resolves 12/9 |
| **Thu Dec 10** | 8:30 | **CPI** | Nov | BLS (read 10/21; 403 on 11/19) | Headline vs core, energy share |
| Thu Dec 10 | 8:30 | BEA: real PCE and real personal income by state, 2025 | 2025 | BEA (read 11/19) | — |
| **Tue Dec 15** | 8:30 | **PPI** | Nov | BLS (read 10/21; 403 on 11/19) | FD m/m >0.4/>0.5/>0.6 |
| Fri Dec 18 | 8:30 | International transactions, Q3 | Q3 | BEA (read 11/19) | — |
| Fri Dec 18 | 10:00 | U. Michigan sentiment, final | Dec | UMich PDF (read 11/11) | Inflation expectations |
| Fri Dec 18 | — | Quarterly options expiry (third Friday) | — | calendar | Larger gamma roll-off than a monthly |
| **Wed Dec 23** | 8:30 | **GDP third estimate + profits, Q3; Personal Income and Outlays (PCE)** | Q3 / Nov | BEA (read 11/19) | Core PCE |
| — | — | Retail sales, housing starts, JOLTS, import prices for November/October | — | **UNVERIFIED this rebuild** (Census list view and bls.gov unreadable 11/19) | Confirm dates before citing |

**University of Michigan consumer sentiment, 10:00 ET, added 2026-11-11 (WALTER packet a34c796f9d: the 11/6 preliminary went uncarded about 8 hours because it was not listed here).** Dates read 11/11 13:4x ET from UMich's own release-date PDFs (data.sca.isr.umich.edu, survey-info page, "2026 Release Dates" docid 79628 and "2027 Release Dates" docid 81621); 10:00 ET from the sca.isr.umich.edu next-release note. Beyond this window: **2026: Dec 4 (Fri) December preliminary · Dec 18, 2026 (Fri) December final · 2027: Jan 8 prelim, Jan 22 final, Feb 12 prelim, Feb 26 final, Mar 12 prelim, Mar 25 final (a THURSDAY, flagged in UMich's PDF).** UMich notes November and December interviewing runs off its normal pattern for holidays. CARL owns the consumer read; HENRY reads the inflation-expectations leg for the rate path.

**Senior Loan Officer Survey (SLOOS), quarterly, 2:00 PM ET, added 2026-11-05 (WALTER 031: the October survey posted 11/2 and went unrouted because it was not listed here).** Next: January 2027 survey, **ESTIMATED Mon Feb 1, 2027**, the Monday after the Jan 26–27 FOMC. The Fed has not published this date; its 2027 monthly calendar pages returned 404 on 11/5. The pattern held on all four 2026 releases (Feb 2, May 4, Aug 3, Nov 2, read at the Fed's calendar, survey pages and FOMC page 11/5). Confirm at the Fed's February 2027 calendar when it posts. REGINALD and LIQUID hold the read; HENRY reads the equity consequence.

**Beyond the window:** FOMC 2027: Jan 26–27, Mar 16–17, Apr 27–28, Jun 8–9, Jul 27–28, Sep 14–15, Oct 26–27, Nov 16–17 (Fed calendar, read 11/19; tentative until confirmed at the preceding meeting). Census January 2027 rows (read 11/19): construction Jan 4; trade Jan 7; retail sales (December) Jan 15; housing starts Jan 20; durable goods and new home sales Jan 27.

*Disposition 2026-10-21, PROME closeout flag on "Dec 23": the date is a real release date outside the 30-day window, now verified at the BEA page. It was first written from a search summary and labelled "(verified)" before the BEA page had been read for December; the label was premature, the date was right. The BLS December dates were the same case and are now read at the BLS page too.*

---

## Weekly (every Thursday 8:30 ET)
- **Initial jobless claims** — >250K sustained is LABOR's trigger. Pattern only; not re-verified at DOL 2026-10-21.

## ISM Release Pattern
- Manufacturing: 1st business day of month, 10:00 ET
- Services: 3rd business day of month, 10:00 ET

## Key Thresholds

| Indicator | Threshold | Implication |
|-----------|-----------|-------------|
| Core CPI MoM | >0.3% | Hot — rate cuts delayed |
| Core PCE MoM | >0.3% | Hot — Fed's own gauge |
| NFP | <100K | Labor cracking |
| ISM Mfg | see `STATUS.md` bands | ISHM owns the <47 trigger (WQ-507 A) |
| Claims | >250K sustained | LABOR trigger fired |
| ~~ECI QoQ~~ | ~~>1.2%~~ | **RETIRED 2026-08-06 as a dated record (Will-ruled 7/31, PROME rulings packet §3): cannot fire — private-wage q/q has sat in a 0.8-1.0 band for seven quarters (LABOR, BLS-primary). Any replacement is a NEW registration with base rates. BLS re-weights ECI from Dec-2026 data; 2026-10-30 is the last print on the current basis** |

The live STANDING bands (ISM, PPI, VIX, SPX, KRE, yields, HY/CCC) are in `STATUS.md` § ACTIVE THRESHOLDS; this table holds only the release-level surprise lines.
