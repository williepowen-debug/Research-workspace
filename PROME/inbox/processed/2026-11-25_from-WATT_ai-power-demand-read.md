# From WATT to PROME, 2026-11-25 11:48 ET: does AI power demand crack? (C9 commission, prome-77 11:35 ET)

**Runtime:** Claude Code, in-process subagent spawned by PROME; model Opus 5.5 (claude-opus-5-5); session id not exposed (UNKNOWN). **Boot reads (bounded reader, each to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/WATT/CLAUDE.md` 4; then SCRATCH, STATUS, CLOSEOUT whole; `boot.py` rc 2 (DM2 401, EIA timeouts on first try, EIA-930 re-fetched fine); corrections check rc 1 then 0 after five receipts. No pull (foreign dirty tree, HOMER and other desks' staged files untouched).

## Answer, for Will

**No crack in the record; this is equity repricing.** Over the three chip-led down days (November 20, 24, 25; Wednesday intraday at 11:40 ET) the data-centre power and equipment names fell 10 to 21%: GE Vernova −17.6%, Vertiv −21.3%, NRG −16.3%, Quanta −15.2%, Eaton −14.9%, Constellation −13.4%, Talen −13.4%, Vistra −12.9%, Caterpillar −10.2%, against the S&P 500 (SPY) −6.8%, the chip ETF (SMH) −23.1%, the utilities ETF (XLU) −0.6%, and NextEra, Southern and Duke up 0.8 to 2.9% (fetch.py 11:39:45 ET). They trade as AI beta, about half to nine tenths of the chip move, both ways (Monday's rebound was +6 to +12%). Meanwhile the contracted record grew at the last prints: AEP signed 15 GW more in the third quarter and counts 84 GW contracted by 2031, only on executed agreements (release October 28); Dominion's pipeline is 54.9 GW, +13% since December, 12.2 GW of it under signed service agreements (secondaries); PJM's own consultant (Charles River Associates, November 2) puts PJM data-centre demand at 30 GW by 2030 and says about 11.5 GW of it cannot be served at normal reliability: supply, not demand, is the limit. I found no named November cancellation, utility forecast cut or queue-withdrawal wave. ⚠️ **Caveats that change how much weight this carries:** the newest hard prints are a month old; Dominion and Exelon numbers are secondary reads; the search was bounded; and PJM's price feed has been dark to this desk since November 16, so live grid stress is unknown (that blinds prices, not the demand record). The one real cut on the record is Exelon's July cut (18 to 11 GW high-probability), from local opposition and vetting, unchanged in October.

Full tables, sources and limits: `AGENTS/WATT/research/2026-11-25_ai-power-demand-read.md` (KB-WATT-225 to 227).

## Item 1: established / reported / not found (summary)

| Grade | Lines |
|---|---|
| ESTABLISHED | AEP Q3 release (+15 GW, 84 GW by 2031, $100B plan); CRA review on PJM's site (30 GW by 2030; ~11.5 GW unservable at 1-in-10; low-adoption −19 GW by 2047); EIA-930 PJM 107,114 MW at 14Z today (demand half of P1 met, not a stress reading per KB222); no emergency posting on the board 11:36 ET; October US electrical equipment orders +0.4% (ISHM's read) |
| REPORTED | Dominion 54.9 GW / 12.2 GW ESA; Exelon 11 GW unchanged at Q3; ING's ~$500M data-centre loan sale short of bids and GPU lenders cutting advance rates (financing tail, not load); Market Monitor and advocates asking to delay the December auction (no postponement found; PJM's November 3 and 9 filings assume it runs) |
| UNVERIFIED | Alibaba 'may cut' its 20 GW plan (one X account); SoftBank write-off load direction (KB209) |
| NOT FOUND | named November US cancellation ≥ any size on the record; utility load-forecast cut; hyperscaler lease walk-away; queue-withdrawal wave; PJM final 2027 large-load adjustments (LAS December 18, nothing posted); new ERCOT large-load total after June's 474.7 GW |

## Item 2: the other desks' reads, weighed

- **ISHM:** BEA's +41.7% information-processing investment says the spending is real and accelerating; the Fed's +4.5% equipment-output revision says much of the gear is imported or price. For power: demand-side positive, supply-side caution (thin domestic equipment capacity fits the long transformer and turbine waits). Neither is a crack.
- **Section 301 (VULCAN PROVISIONAL, ZHAO):** proposed, not in force (comments January 5, hearing January 25). WATT sizing, ASSUMPTION grade: tariffed electrical items about $2-3M per MW of IT load, imported share unknown (30-60% tested), 15-20% duty ⇒ **about $0.1-0.3M per MW, 1-3% of non-IT build cost, 0.2-0.6% of all-in cost**, roughly two to six months of a site's PJM wholesale energy bill once (at the Market Monitor's $74.98/MWh January-September average). Too small to move a site decision on its own. Most large transformers are utility-side, so the cost lands in rate base: the WATT-08 who-pays question and CARL's bill channel. **Cannot size:** import shares by HTS line and country, Section 232 stacking (one secondary says 25% already applies, unverified), final rates, and the lead-time effect, which is the bigger lever (transformers about 128 weeks already).

## Item 3: own rows (graded only what the written rules grade today)

Nothing due today (`boot.py` predictions-due: none). No level, operator, instrument or consequence changed. Composite 14/20 unchanged (P1 3, P2 5, P3 4, P4 2); P3's upgrade trigger is IPP guidance raised or active queue > 2× peak, and AEP is a utility, so no move.
**What the PJM key refusal (WILL_QUEUE 695) hides:** the 5-minute and hourly price tape from November 14 11:00 EPT to now (eleven days, including the November 17-19 and 24-25 cold mornings: P1 UNKNOWN, not quiet); **WATT-13's resolver (DM2 forced outages), due first boot on or after December 2: it cannot be graded without the key** and stays OPEN with resolver data UNKNOWN (no substitute source, per your instruction); WATT-16's verified-tape grade December 18 (retention at least 49 days measured, so the window survives if the key returns by about early January); the same-vintage spark spread (the ICE proxy reads +$54.58/MWh at heat rate 7 for delivery today, a different product). The weekly coverage due November 21 was missed (desk dark, key refused). No work-around attempted.

## Item 4: inbox and the two older questions

- **Inbox:** 0 top-level, 14 WALTER cards, all dispositioned (card 017 first: WATT holds no row on the November 27 China export clock; the NEXUS brief line now carries January 27, 2027), board_log rows written, files moved to processed (d8086814d2). Five named corrections receipted (COR-20261117-02, -20 APPLIED at KB-WATT-224, COR-20261120-10, COR-20261123-13, COR-20261124-21).
- **WQ-735 honest-client-name packet:** NOT in WATT's inbox, never sent here (WATT is not among the twenty recipients). One-line reply: **WATT has no WQ-735 packet to action; but `AGENTS/WATT/power_watch.py` sends a Chrome User-Agent string to emergencyprocedures.pjm.com and to EIA's wholesale-price xlsx, so it looks missed by the 63-script census; not switched here, because WQ-735's test-first condition is yours.** Send the packet and WATT switches at its next session.
- **D:L1168 (can the forecast scorer read WATT's archive as it stands):** yes. Running `forecast_report.py`'s own reader (`read_all(load_bucket())`) today returns all ten resolved WATT rows from `workbook/PREDICTIONS_ARCHIVE.tsv` despite its `#` comment lines and lower-case headers (WATT-01, -02, -04, -05, -07, -12 HIT; -03, -06, -10, -11 MISS, each with a resolved date) and the seven open live rows. They count in the hit/miss tally but carry no readable probability (p = None): rows made before WQ-715 stated a tier, not a number, so they cannot enter a Brier score unless an owner-stated probability existed at the time, which it did not. WATT-14 to 17 read 0.88 / 0.45 / 0.55 / 0.45. One observation, not a defect while the rows are open: the reader parses a 'resolved' date of 2026-10-20 for open WATT-08 and -09 from the interim text in their resolution cells; it matters only if a timing check ever uses an open row's resolved date.

## Item 5: forward view (outlooks, unregistered, unscored)

Expectation: no crack shows in primary data before year-end; the names keep trading as AI beta until a hard print. Alternative that matters: if it comes, it shows first at the financing tail (neoclouds, standalone developers, GPU-backed loans) as withdrawn large-load requests, long before signed hyperscaler load.

| Signal of a real crack | When | Odds |
|---|---|---|
| Named cancellation or deferral of a US site of 1 GW or more | any day; Q4 prints late January | about 30% by January 31 |
| A utility cuts SIGNED load (not pipeline) | Q4 prints February | about 15% by February 28 |
| PJM's final 2027 large-load adjustments below the 2026 forecast's 2030 data-centre figure | LAS December 18; forecast January | about 40%, but a vetting cut is not a demand crack: read the reason |
| ERCOT Batch Zero shortfall led by withdrawals | December 10 | about 20% |
| GE Vernova backlog plus slots falls below 122 GW | late January | about 10% |
| 2029/30 auction clears below the cap | December 22 | 12% (WATT-14, registered) |

**TERRY:** tradeability packet sent unasked, no card asked (`AGENTS/TERRY/inbox/2026-11-25_from-WATT_power-selloff-is-equity-not-demand.md`, fa5a3deea4). TERRY was not live at your 11:35 preflight; no doorbell (no ACTION item). **WALTER:** no new signal to route (all items here are analysis of cards already on the board).

## Commits

d8086814d2 research, KB, board log, receipts, cards · fa5a3deea4 TERRY packet · 806f5cbae8 STATUS and SCRATCH · c8b94a9500 NEXUS brief (pin 806f5cbae8, pin check OK) · this packet and the closeout receipt follow. Not pushed (PROME pushes).

## COMPLETION — WATT — 2026-11-25
STATUS: ✅ DONE
CHANGED: AGENTS/WATT/research/2026-11-25_ai-power-demand-read.md, workbook/KB.tsv (KB225-227), board_log.tsv, registry/corrections_receipts.tsv, inbox/WALTER/processed/ (14), STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, two archives, reports/2026-11-25_c9-ai-demand-closeout-receipt.md; AGENTS/TERRY/inbox/2026-11-25_from-WATT_power-selloff-is-equity-not-demand.md; this packet
RESULT: No crack in the physical or contracted record; the Nov 20/24/25 fall (power and equipment names -10 to -21% vs SPY -6.8%, XLU -0.6%) is equity repricing. AEP +15 GW signed Q3 (84 GW by 2031); CRA for PJM says supply, not demand, binds by 2030; no named November cancellation found (bounded). Section 301 power-equipment cost ~$0.1-0.3M/MW (ASSUMPTION); inbox 14 of 14; composite 14/20 unchanged.
GAPS: PJM DM2 key refused (tape Nov 14 11:00 to now UNKNOWN; WATT-13 ungradeable Dec 2 without it); newest hard prints a month old; Dominion/Exelon secondary; tariff import shares and lead-time effect unsized; weekly coverage Nov 21 missed.
WILL_NEEDS: None new (PJM key stays WILL_QUEUE 695).
FOLLOW-UP: PROME: WQ-735 packet for power_watch.py's two browser-UA sources. WATT: WATT-09 Nov 30; WATT-13 first boot on/after Dec 2 (key-dependent); ERCOT Dec 10; PJM LAS Dec 18; WATT-16 Dec 18; BRA Dec 22 (WATT-14/15 by Dec 31); WATT-17 Dec 31.
