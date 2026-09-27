# OZK catch-up sweep — Sun 2026-09-27 (window 9/24 → 9/27)

**Scope:** news and filings since the 9/24 session. **Result: nothing OZK-specific moved; zero grades, thresholds, weights or conviction moved.** Clock: `date` = Sun Sep 27 16:41 EDT 2026.

## Instruments run

| Leg | Result | Source / basis |
|---|---|---|
| FDIC company filings (cert 110) | **rc 0 QUIET** — 182 filings returned, schema + coverage OK, none after id 11981 | `scripts/flng_watch.py`, 9/27 16:41 ET. No 8-K, no Q3-date notice, no sub-note redemption notice **returned** (never "confirmed") |
| FDIC insider forms (cert 110) | Newest = **8/14/26** (Hicks, Wolfe Form 4s). **Nothing filed 8/15 → 9/27** | `/api/instdiscl/cert/110`, sorted by `disclPubDate` |
| Price | **OZK $46.89** (+0.62%) · **KRE $71.55** (+0.86%) — **Fri 9/25 close**, not live (weekend) | FORGE `fetch.py`, asof 2026-09-25 |
| Short interest | **16,512,969 sh @ 9/15/26** (was 16,209,608 @ 8/31), **DTC 17.6** (was 16.0); ≈16.3% of float on the 6/30 float basis (derived) | Nasdaq SI API (FINRA) |
| Analyst tape | No new action after **9/8** (MS → UW, PT $56). Last 8: MS UW $56 (9/8) · RJ MP (9/1) · Citi Sell $40 (8/17) · WFC EW $56 (8/10) · UBS Neutral $51 · KBW MP $52 (7/28) · TD Cowen Hold $52 (7/24) · Piper OW $61 (7/22) | stockanalysis.com ratings page, read 9/27 |
| Q3 earnings date | **Not announced as of 9/27.** Aggregators guess 10/15 (estimate only) | web search; FLNG quiet |
| IQHQ / RaDD | Nothing new. A search summary returned the "two-year extension → 2028" line again — **the known vintage trap (5th sighting)**: its source is Bisnow 3/19/26 restating the 2024 extension; primary maturity = Aug 2026 (Q1'26 transcript) | Bisnow 3/19/26, fetched |
| Spur Ph I → Apollo | Second outlet confirms: The Real Deal **9/17/26** — 580 Dubuque Ave, 330K SF, never occupied, $275M Apollo construction loan (Nov 2022), deed-in-lieu to an Apollo affiliate. **Still one outlet (TRD) as the primary; the other hits are re-reports** | therealdeal.com 2026/09/17 |
| Bluerock BPRE | Sept distribution $0.1371/sh; **market price $11.91 (9/3) vs NAV ≈ $22.5 → ~47% discount** (DERIVED from the release's 7.3%-on-NAV vs 13.8%-on-market rates; ⚠️ corrected 9/27 PM — the "38%" first written here was Bisnow's **Dec 18 2025** listing-day figure, a vintage error); net assets ~$3.2B @ 8/31 (was $3.6B at listing). No IQHQ mark disclosed. Webinar **10/6** | bluerock.com, PR Newswire, Bisnow |
| Aimco v. IQHQ (Del. Ch.) | No ruling found **as of 9/27** (web only; docket pull still owed, TODO C3) | Bisnow, Hoodline (Apr 2026) |
| Campus at Horton (TODO C1) | **UNKNOWN — not discharged.** 3 queries found no lease announcement since the Aug 2025 AB credit bid. The only live listing (Cushman, Bldg 200, **204,842 SF, whole building "Available"**) is undated and still names **Stockdale** (the pre-foreclosure owner) → likely a stale page, so it cannot show vacancy *today*. Needs SD Business Journal / Bisnow SD / CoStar (403 to scripts) | cushmanwakefield.com listing; bisnow 8/2025 |

## Reads

- **Tape:** OZK **−4.5%** since 8/31 ($49.08 → $46.89) vs KRE ≈ **−2.2%** (≈$73.15 → $71.55; 8/31 KRE back-derived from 9/24 STATUS). The 9/24→9/25 bounce was sector-wide (cohort +0.6 to +1.8%). The gap is still the 9/8 MS day plus beta. <$45 band now **4.0% away**; P/TBV **≈0.97×** ($48.41 Q2 TBV).
- **Short interest:** still rising into the Q3 print — the crowded short keeps building (DTC 17.6 is near the 8/14 19.4 high).
- **Pre-print quiet is normal:** FLNG quiet + no insider forms is the expected state ~3 weeks before the print. Insider blackout starts ~early Oct.

## Forward (unchanged)
~9/30 Q3 date · **10/1 sub-notes reprice** (read Fri 10/2: flng_watch rc 0 = SCHEDULED-UNCONTRADICTED) · 10/6 BPRE webinar · ~mid/late Oct Q3 call (RaDD "~92-day" report-back).
