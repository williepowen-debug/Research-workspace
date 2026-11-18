# HEARTBEAT 41st base: sources

Written 2026-11-18 by PROME prome-6e (context c25c5e82). Each line is a file PROME read for this base. "Head" means the packet was read from its top through its result table (about the first 2,300 to 3,600 bytes) in this context. "Figures" means the cited figures were matched in the packet by search and the rest came from PROME's own daily note of the day it was first read whole (`memory/2026-11-18.md`, written by an earlier context of this session).

## Market levels
- `dashboard.txt` in this directory: `FORGE/tools/market-data/dashboard.py`. One pull, stamped 2026-11-18 17:00:25 EST at its head.
- `fetch_prices.txt` in this directory: `FORGE/tools/market-data/fetch.py price` for ^GSPC, SPY, QQQ, SMH, RSP, NVDA, ^VIX, ^VIX3M, GLD, HYG, BZF27.NYM, JPY=X and KRE, 17:01 ET. Vendor quotes an hour after the close. The Brent figure is a last trade after the settle window, not a settle.
- Treasury par 10Y 5.07 [11/18] is HENRY's figure (its close packet); the 11/17 set (2Y 4.80, 10Y 5.10, 30Y 5.46, real 10Y 2.89) is BOND's. PROME did not read Treasury's file itself for this base.

## Owner returns, November 18 (PROME/inbox/processed/), head
- HENRY: `2026-11-18_from-HENRY_row9-not-fired-fred-confirms-close-items.md`, `2026-11-18_from-HENRY_morning-fred-map-wq697-edit-inbox.md`
- LIQUID: `2026-11-18_from-LIQUID_L1178-hy320-MET-1117-and-drain.md` (whole)
- TERRY: `2026-11-18_from-TERRY_close-reads-gld-credit-cal0006.md` (whole), `2026-11-18_from-TERRY_L1187-L1192-and-tradeability-reads.md`
- BOND: `2026-11-18_from-BOND_20y-clean-wq699-applied-domain-update.md`
- MIDAS: `2026-11-18_from-MIDAS_L819-L821-L1010-delivery.md`
- ZHAO: `2026-11-18_from-ZHAO_sep-tic-zha22-access-inbox.md`
- BRENT: `2026-11-18_from-BRENT_gulf-eia-crimea-delivery.md`, `2026-11-18_from-BRENT_wednesday-eia-gasoline-yoy-flag.md` (whole)
- REGINALD: `2026-11-18_from-REGINALD_board-to-date.md`
- FALCON: `2026-11-18_from-FALCON_weekly-gate-tk2-draft.md`; `2026-11-17_from-FALCON_card022-qeshm-strike-confirmed.md`
- VULCAN: `2026-11-17_from-VULCAN_cards-025-023-sec-probe-and-board-refusal.md`
- BROCK: `2026-11-18_from-BROCK_L1140-crmt-backstop9-empty-provisional-L1175-outcome-not-on-file.md`
- DEWEY: `2026-11-18_from-DEWEY_L517-plaza-hearing-result.md`
- RED: `2026-11-18_from-RED_S67-owed-work-done-ft06-4of5.md`
- ANVIL: `2026-11-18_from-ANVIL_reconcile-report.md` (headline only)

## Owner returns, November 18, figures
- SAM: `2026-11-18_from-SAM_domain-update-through-11-17.md`
- VIOLET: `2026-11-18_from-VIOLET_L1182-soq-30pct-row-met-wq678-stale-kb.md`
- FALCON: `2026-11-18_from-FALCON_card007-weekly-sweep-grade.md`; the Kuwait and Bahrain grade from the daily note (`2026-11-18_from-FALCON_live-kuwait-bahrain-grade.md` not re-opened)
- ORACLE: `2026-11-18_from-ORACLE_WQ704-delivered-L1173-market-vs-fleet-gaps.md`
- HANS: `2026-11-18_from-HANS_L1146-trilateral-read-fsr-t16-fired-inbox-drained.md`
- OSPREY: `2026-11-18_from-OSPREY_crimea-bridge-gate001-osp07-drain.md`
- SHADE: `2026-11-18_from-SHADE_L240-DLIC-Q3-and-L185-close.md`
- FERT: the GATES row GATE-FERT-G5 and the daily note
- From the daily note only, packet not re-opened: HAWK (not cited beyond the pointer), YURI (the trilateral meeting).

## Ledgers read
- `PROME/GATES.tsv` state cells for GATE-LIQ-069, GATE-LIQ-076, GATE-FALCON-001, GATE-BRK-R2, GATE-BRENT-COT-35B, GATE-HY-REKILL, GATE-TERRY-HYG-FOLLOW-01, GATE-FERT-G5 (read 2026-11-18 about 17:05 ET). ⚠️ The GATE-HY-REKILL and GATE-LIQ-069 cells still stand at the 11/13 and 11/12 owner grades; the memo cites LIQUID's 11/18 packet for the 11/17 cell.
- `PROME/state/CALENDAR.md`, regenerated 2026-11-18 16:59 ET, and the refresh gate's desk-catalyst line, for the near-term calendar.
- `PROME/WILL_QUEUE.md` row 720 (APPROVED A, 11/18 12:10 ET).

## Carried from the 40th base and its amendments, not re-read
- Nvidia's Q3 figures and the dead Nvidia card (Amendment 2; HENRY, VULCAN, TERRY packets of 11/17); the SoftBank leverage figures and 5Y CDS; claims 200,000 [wk 11/7]; United Fidelity; N-able; HEN-63; VX-BND-18; AEOLUS C5; the QQQ and ORCL card states; the positioning gate's 11/16 grade; HOMER and ISHM lines; the Kernel line; the cold-file pointers; every kill-on-sight item from "CPI caused the December repricing" to the end of the list.

## Not read at all for this base
- Returns filed 11/14 to 11/17 by CARL, CORAL, CRUISE, CYPHER, FLG, GIBBS, HOMER, ISHM (October industrial production), MARCO, OTTO, OZK, WAL, WATT, CREED and NEXUS, and the 11/17 packets of LIQUID, REGINALD, ZHAO and RED. They were consumed by earlier PROME sessions; none is cited here.
- No return filed 11/14 to 11/18, by the listing of `PROME/inbox/processed/`: AEOLUS and LABOR. Both have rows for Thu 11/19.
