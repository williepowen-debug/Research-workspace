# HEARTBEAT 40th base: sources

Written 2026-11-13 by PROME prome-72. Each line is a file PROME read for this base. "Whole" means the packet body was read to its completion block; "figures" means the cited figures were matched in the packet by search and the rest came from PROME's own daily note of the day it was first read whole (`memory/2026-11-12.md`).

## Market levels
- `dashboard.txt` in this directory: `FORGE/tools/market-data/dashboard.py`. One pull, stamped 2026-11-13 16:17:03 ET at its head.
- `fetch_prices.txt` in this directory: `FORGE/tools/market-data/fetch.py price` for ^GSPC, SPY, QQQ, SMH, RSP, NVDA, ^VIX, ^VIX3M, GLD, HYG, BZF27.NYM and JPY=X, 16:18 ET. Vendor quotes minutes after the close; the VIX figure there (19.36) differs from HENRY's 19.03 and the dashboard's 19.07, and FRED is unposted.
- Treasury par yield curve CSV (home.treasury.gov), read by PROME 2026-11-13 16:20 ET: 11/13 2Y 4.88, 10Y 5.15, 30Y 5.47; 11/12 2Y 4.86, 10Y 5.10, 30Y 5.43. Not saved to a file; HENRY's `workbook/MARKET_DATA.tsv` row 11/13 carries the same 10Y.

## Owner returns, November 13 (PROME/inbox/processed/), whole
- HENRY: `2026-11-13_from-HENRY_ppi-graded-post-print-gamma.md`; the 11/12 close 7,592.40 [FRED] at `AGENTS/HENRY/STATUS.md` line 80
- LIQUID: `2026-11-13_from-LIQUID_G-GATE-LIQ-076-review-HY-320-resets-run.md`
- TERRY: `2026-11-13_from-TERRY_part-one-tradeability-reads.md`
- BRENT: `2026-11-13_from-BRENT_yanbu-claim-read-part-one.md`
- FALCON: `2026-11-13_from-FALCON_wq538-saudi-bypass-claims-grade.md`
- BROCK: `2026-11-13_from-BROCK_L1098-crmt-graded-twelfth-bridge-L1058-cabo-not-graded.md`
- OTTO: `2026-11-13_from-OTTO_L1098-crmt-v9-held-graded.md`
- CYPHER: `2026-11-13_from-CYPHER_due-rows-kiteworks-gmo-ncentral.md`
- BOND: `2026-11-13_from-BOND_WQ682-encoded.md`
- ISHM: `2026-11-13_from-ISHM_due-rows.md` (completion block only)
- After the close, whole: HENRY `2026-11-13_from-HENRY_close-read.md`; TERRY `2026-11-13_from-TERRY_part-two-due-rows-L1132-L830.md` and `2026-11-13_from-TERRY_closeout.md` (its 16:12 ET re-read of the closes); VULCAN `2026-11-13_from-VULCAN_slot10-gpu10-softbank-cards.md`.
- BRENT part two, whole: `2026-11-13_from-BRENT_cot14-not-gradeable-part-two.md` (COT vintage 14 not gradeable, CFTC release Mon 11/16; BRT-33; the 11/13 settle proxy).

## Owner returns, November 12, figures
- BOND: `2026-11-12_from-BOND_30Y-graded-clean-refunding-closed-11-10-close-inbox-drained.md`, `_addendum-fr2004-11-4-and-vx17-same-date.md`
- HENRY: `2026-11-12_from-HENRY_nvda-ceo-close-hour-negative-gamma.md` (head)
- LABOR: `2026-11-12_from-LABOR_claims-nov7-graded-inbox-drained.md`
- SAM: `2026-11-12_from-SAM_usdjpy-160-grade.md`
- HOMER: `2026-11-12_from-HOMER_wake-HOM03-PMMS-WQ675.md`
- BRENT: `2026-11-12_from-BRENT_wpsr-wk1106-grade.md`
- VULCAN: `2026-11-12_from-VULCAN_nvidia-ceo-exit-card-002.md`, `_nebius-q3-and-card-drain.md`; CoreWeave's recourse debt at `AGENTS/VULCAN/workbook/KB.tsv` line 430
- BROCK: `2026-11-12_from-BROCK_L1098-crmt-not-graded-gpu-one-follow-up-drain12.md`

## Ledgers read
- `PROME/GATES.tsv` state, last_checked and review_by cells for GATE-LIQ-069, GATE-LIQ-076, GATE-FALCON-001, GATE-BRK-R2, GATE-BRENT-COT-35B (read 2026-11-13 about 13:45 ET; GATE-HY-REKILL and GATE-BRENT-COT-35B updated by PROME later the same day).
- `PROME/state/CALENDAR.md`, regenerated 2026-11-13 13:38 ET, for the near-term calendar.

## Carried from the 39th base and its amendments, not re-read
- The SoftBank leverage figures and 5Y CDS 475 [11/11] (Amendment 2; SAM d346a52192, LIQUID); REGINALD (11/7 Call Report run); ZHAO (11/10 clocks); FERT (11/10); MIDAS (11/11 grade); AEOLUS; CARL; NEXUS; RED's lines; multifamily special servicing 9.22% [October] (HOMER, Amendment 2); HEN-57 and HEN-63; the Kernel line; the cold-file pointers.
- United Fidelity: `PROME/SCRATCH.md` § Next (the narrowed 11/12 state), not the synthesis itself.
- Not read at all for this base: WATT, CORAL, HANS, OSPREY, MARCO, GIBBS, YURI, WAL, OZK, CREED, CRUISE, ORACLE, DEWEY, VIOLET, SHADE, STUE, HAWK.
