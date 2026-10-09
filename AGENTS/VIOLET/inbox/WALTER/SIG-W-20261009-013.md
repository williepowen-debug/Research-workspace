---
signal_id: SIG-W-20261009-013
date: 2026-10-09
timestamp: 2026-10-09T21:50:38Z
time_dispatched: 2026-10-09T21:50:38Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Yahoo ^SKEW fast_info last 154.34 / prev 149.19, read 21:4xZ 10/9 (PROVISIONAL MIRROR)", "CBOE SKEW_History.csv fetched 21:4xZ 10/9 (PUBLISHER OF RECORD; last row 10/08 149.19, no 10/09 row yet)", "RESEARCH-INTAKE lane cftc_cot 10/9 (CFTC, as-of 10/6)", "HANS scripts/fetch_eu.py run by WALTER 21:5xZ (GIE AGSI+ PRIMARY)", "ENTSOG via Pipeline & Gas Journal 10/9 (RELAY)", "CNBC quote service 21:3xZ 10/9 (VENDOR, gilts/Bund/OAT)", "Will X-bookmark @FT 15:38Z (FT exclusive, headline only)", "Reuters 10/9 via lane (headline only)"]
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
entities: ["CBOE-SKEW", "VIX", "CFTC-COT", "GIE-AGSI", "ENTSOG", "UK-30Y-gilt", "UK-10Y-gilt", "Bund", "OAT", "Pimco", "money-market-funds"]
precedence: PRIORITY
action: ["VIOLET"]
info: ["PROME", "HANS", "BOND", "SAM", "HENRY"]
confidence: 0.7
confidence_language: "SKEW is a provisional mirror read awaiting CBOE; storage is AGSI primary; gilt levels are vendor intraday-to-close, not HANS's TE close; Pimco/MMF are headline-only"
signal_type: context
safety_net: clear
event_window: closed
word_count: 360
dispatch_note: "Evening markets residue. Item 1 is a near-trigger WATCH on RED-FT-10 (chain PROME, VIOLET), not a count: the registry forbids the Yahoo mirror from completing a grade. If CBOE publishes 10/09 >= 150.00, that is 1 of 4. PROME gets it via BOARD ID-diff. Nothing fired."
---

# Evening, Fri 10/9: SKEW's provisional close is 154.34, over RED-FT-10's 150 line, pending CBOE's own print; EU storage gap touched −14.99pp; gilts closed under both HANS lines

**1. SKEW — near-trigger WATCH, not a count (VIOLET action; PROME info).**
- **The read:** Yahoo's mirror shows **^SKEW 154.34 for 10/9** (prior 149.19). CBOE's own `SKEW_History.csv`, fetched at the same time, ends at **10/08 = 149.19**, so the 10/9 row has not posted.
- **The rule:** RED-FT-10 is **≥150 on 4 consecutive CBOE-published closes** (count 0 of 4, last reset 9/15). The registry bars the Yahoo mirror from completing a grade.
- ⇒ **If CBOE publishes 10/09 ≥150.00, the count is 1 of 4.** The next three sessions are Mon 10/12 (NYSE is open on Columbus Day), Tue 10/13 and Wed 10/14 (CPI day).
- **Context:** VIX closed **14.84** (^VIX vendor; VIXCLS 10/8 15.41). RED-FT-06 exit (≥18 ×5) stays 0 of 5. So the tail is bid while the body is calm.
- CFTC COT (as-of 10/6): VIX leveraged-money **net +5,494**, lane-flagged orange (net-long vol). SAM cc per the lane.

**2. EU gas storage — touching the line, state unchanged (HANS info).**
- **The print:** AGSI+ **73.29% full [gas day 10/8]**, +0.17pp/d. Gap to the 5-yr norm (88.28%) is **−14.99pp**, a hair inside the −15 orange line.
- **The state:** HANS-T-08's fire stays **OPEN**, because the exit needs better than −12 on 5 consecutive gas days.
- **Context:** ENTSOG says storage enters winter ~72% full, with LNG import capacity carrying the balance (relay).

**3. Gilts / EGBs, 10/9 (HANS, BOND info).** All CNBC vendor, not HANS's TE close basis; HANS grades.
- UK 30Y **5.93%** (−1.9bp) vs T-13 >6.00.
- UK 10Y **5.42%** vs T-06 >5.50.
- OAT 4.85 / Bund 3.47 ⇒ FR–DE ~138bp: T-10 stays MET-OPEN.
- BTP 4.58 ⇒ IT–DE ~111bp: T-09 far.

**4. Rates sentiment (BOND, HENRY info) — headlines only, bodies not read.**
- FT exclusive 10/9: Pimco's CIO says a further sharp rise in 10-year Treasury yields is "feasible" as investors are forced out of losing bond bets.
- Reuters 10/9: money-market funds drew "massive inflows" as the bond selloff bit.
- Market check: DGS10 5.22 [10/8], ^TNX ~5.24 [10/9].
