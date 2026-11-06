# LIQUID handoff for November 6, 2026

Written Thursday November 5, 16:4x ET, session `liquid-9d`, ahead of Will's move to the laptop. LIQUID has no SCRATCH file; this is that surface, and STATUS §3 points here. Delete nothing here; mark steps done in STATUS. Scratchpad scripts and background watchers do not carry over, so every step below stands alone. The closing session pushes before the switch; the laptop session pulls first and confirms it has this file.

Limits unchanged from Will's 09:42 ET word: no trades; no change to a level, operator, instrument or consequence on a gate, kill rule, band or frozen letter; keep observation date and basis on every number; market signals through WALTER; commit own paths by exact pathspec; one packet to `PROME/inbox/`.

**Done 2026-11-06 by 10:30 ET:** SOFR, GSBD, November 5 ICE print, L4, tier rule, two peer answers, funding sweep. MAIN 10-Q not filed at 10:12 ET. W1 about 15:30 ET still open. Record: `REPORT.md` §15.

## State going in

HY 332, CCC 1,297, BB 199, B 351, IG 91, BBB 113 [November 4, first-published]. 069 2-of-2 FIRED unchanged, L1 and L4 NOT FIRED [November 4]. 076 NOT MET 1 of 3, window October 23→November 5. 079 NOT ARMED, +12 bp [November 4]. HY-REKILL 0 of 2. 072 NOT FIRED. Detail: `REPORT.md` §14.5 to §14.8 in this directory.

## Steps, in order

| When (ET) | Step | How | Then |
|---|---|---|---|
| 08:00 | SOFR as-of November 5 | `.venv/bin/python3 AGENTS/LIQUID/scripts/boot.py`; SOFR99−IORB date-matched; exclusions in `workbook/GATE079_CALENDAR_EXCLUDED.tsv` | 079 row, STATUS §2. Fires only at +30 or more, non-calendar, twice |
| 09:00 | GSBD Q3 | Call 09:00 ET. EDGAR CIK 1572694, `scripts/sec_contact.sec_ua()` for the SEC User-Agent. No 8-K at 16:38 ET November 5. Read regular dividend, NAV, FV/Cost, GSBD M3 | `workbook/BDC_MARK_CONVERGENCE_MONITOR.md`. A fresh regular cut is the only route left to CONFIRM. Packet to BROCK |
| any | MAIN 10-Q | EDGAR CIK 1396440. Release already read: NAV $34.22, FV 117% of cost rounded | Replace the rounded figure with exact FV/Cost |
| late morning | November 5 ICE print | First-published, from `FORGE/tools/market-data/fetch.py`: `fred_fetch_vintage('BAMLH0A0HYM2', limit=5, basis='first-published', observation_start='2026-11-01')`; then `.venv/bin/python3 AGENTS/LIQUID/scripts/transmission_check.py`. ICE rows reach FRED by late morning T+1 (KB-LIQ-151) | Next three rows |
| on print | Grade L4 | `.venv/bin/python3 AGENTS/LIQUID/scripts/gate069_legs.py`. Stock half on raw closes: IREN 18.03, −16.95% from 21.71, line 18.45; NBIS 120.37, APLD 14.17 missed. HY 337 or wider fires. Use the CLI verdict, not this table. Vendor closes, official close unchecked | Fire: WALTER card, VULCAN and VIOLET, PROME. Not fired: STATUS §2 only |
| on print | Tier rule | `REPORT.md` §14.5. Rule likely prints BROADENS on the 15-session clause even on a flat day, so report the d/d clause separately. REVERSES needs CCC ≤1,288 and B ≤347. HY 357 is WALTER's +25 bp routing net, not a LIQUID gate | STATUS §1 and §2 |
| on print | Two peer answers | VIOLET: the dated print only; "credit flat" stays VIOLET's judgment, no numeric definition. BROCK: ladder row 10 (VIX +3 without HY widening) | Direct packets, self-committed |
| on print | **Will's funding sweep** (word 15:40 ET November 5, one-off, no new monitor) | Same list as `REPORT.md` §14.6: SRF and RRP, SOFR99−IORB, bill auctions, 10Y/5Y/3M, gold, DXY, USD/JPY, MOVE, PFF, PGX, AT1.L, Fed swap lines, commercial paper, OFR stress index; plus bank stocks and bond funds. Compare against §14.7 closes where they exist, §14.6 14:14 ET tape otherwise, and mark which | New `REPORT.md` section. State the blind spots: cross-currency basis, swap spreads, prime-brokerage margin, repo haircuts, Treasury bid-ask |
| about 15:30 | W1 as-of November 3 | `.venv/bin/python3 AGENTS/LIQUID/scripts/cftc_tff_rates.py`, CME full-name key "SOFR-3M - CHICAGO MERCANTILE EXCHANGE". Lines: net ≤−2,950,000 or weekly cover >+300,000 | A hit pairs with W3 witnesses still in the window (October 26–29, November 4). Confirm the window before calling 2 of 3 |

## PROME and Will

PROME's Nov 5 HY addendum goes to `PROME/inbox/` after the print, doorbell PROME's live session (find it with the available channel, the name will differ on the laptop). Four DOCKET rows for LIQ-08 to LIQ-11 are PROME's; ledger is `workbook/PREDICTIONS.tsv` at 60cadb1f2. Will reads only his chat, so the sweep result goes to him in plain words with dates and basis, including the blind spots.

## Not closed tonight

NEXUS_BRIEF refresh (still says BROADENS and withheld). MEMORY.md is at 32,521 B against the 32,550 B cap and needs rotation before any note is added. Both belong to the closeout.
