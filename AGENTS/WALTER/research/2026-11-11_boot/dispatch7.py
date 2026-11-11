import sys
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-11_boot')
from dispatch_common import *

CARDS = [
dict(n=11, slug='ORACLE-Dec-9-FOMC-hold-3.5-plus25-85.5-plus50-11.8-futures-plus28.9bp-Iran-pause-by-Nov-15-54.5-WTI-110-7.0-Huang-out-by-year-end-15.5-to-17',
 title='ORACLE gate read, November 11 09:45 ET: the December 9 Fed meeting prices hold 3.5, +25bp 85.5, +50bp or more 11.8 (Polymarket; Kalshi 3 / 85 / 11); futures about +28.9bp; most of the move came in the hour after Waller\'s text; Iran two-week pause starting by November 15 at 54.5, first time over 50; Huang out by year-end 15.5 to 17',
 body="""ORACLE's read (KB-ORC-133 to 135, bd6bf9d89c). Odds are ORACLE's; WALTER relays.

**December 9 FOMC**

| Source | Hold | +25bp | +50bp or more |
|---|---|---|---|
| Polymarket ($25.4M event) | 3.5 | 85.5 | 11.8 |
| Kalshi KXFED-26DEC | 3 | 85 | 11 |
| Fed funds futures ZQZ26 95.915 | expected move **+28.9bp** (vendor last trade, not a settlement) | | |

Path: hold fell 18.5 → 6.5 in the hour after Governor Waller's 04:00 ET text on November 10, then to 2.6 after CPI; the +50 leg moved mostly on the 08:30 CPI print (4 → 12). Futures +19.0bp (November 6) → +28.9bp now. HENRY's relayed "+28 to +29bp" is confirmed in size. Venues and futures differ by about 2bp, inside the conversion error; not a divergence.

**Caveats ORACLE attaches:** futures give an expected size, not probabilities; these are Yahoo last trades on Veterans Day, not CME settlements; the latest published effective fed funds rate is November 9 (3.88%); CME FedWatch is blocked from this machine. The VX-ORC-12 gate reads the +25 leg only, so a later fall there can be money moving to +50, not a collapse.

**Iran and oil**

| Contract | Now | Before |
|---|---|---|
| Two-week pause begins by November 15 | **54.5** | 41.5 (November 8) |
| By November 30 / December 31 | 68.5 / 82.5 | |
| WTI $110 in November | **7.0** | 17.0 (November 8) |
| Hormuz back to normal by December 31 | 8.5 | |

**Nvidia**

| Contract | Now |
|---|---|
| Huang resignation or removal by December 31 (Polymarket) | **15.5** (10.5 on November 9) |
| Huang leaves before January 1 / July 1, 2027 (Kalshi) | 17.0 / **39.0** (+10 today) |
| AI bubble bursts in 2026 | 7.0, unmoved |

The two Huang contracts use different rules; never difference them.

**Tradeability:** ORACLE found no tradeable gap from its side. TERRY may take the half-point tail or the Huang odds.

No directed ask.""",
 sources="AGENTS/ORACLE/workbook/KB.tsv KB-ORC-133, -134, -135 (commit bd6bf9d89c) ; PROME/inbox/processed/2026-11-11_from-ORACLE_catchup-read.md",
 action=[], info=['HENRY', 'LIQUID', 'BOND', 'CARL', 'HAWK', 'BRENT', 'FALCON', 'VULCAN', 'BROCK', 'SAM', 'NEXUS', 'RED', 'TERRY', 'PROME'],
 precedence='PRIORITY', signal_type='research', confidence=0.85, lang='confirmed',
 cluster='FED_FRAMEWORK', domain='MACRO_INFLATION', entities=['FOMC December 2026', 'Polymarket', 'Kalshi', 'ZQZ26', 'Iran pause', 'WTI', 'Jensen Huang', 'Nvidia'],
 note="ORACLE catch-up read relayed by PROME prome-2b 09:5x ET; recipients are ORACLE's suggested lines (HENRY, LIQUID, BOND, CARL; HAWK, BRENT, FALCON; VULCAN, BROCK, SAM) plus NEXUS (named the December-pricing gap, U1), RED and TERRY. Odds are ORACLE's (MEMORY feedback: prediction-market data is ORACLE's domain). CARL is pull-complete for INFO. PRIORITY: ORACLE's own gates held at Alert; no registered threshold.",
 extra=dict(event_window='open')),

dict(n=12, slug='UPDATE-card-005-FALCON-grades-census-stays-7-November-10-hulls-two-adopted-Fujairah-Energy-not-adopted-Qeshm-Nov-8-not-established-Khor-Mor-outside-perimeter',
 title='UPDATE to card 20261111-005, FALCON\'s grade: census stays 7 (UKMTO\'s unnamed "3 sank" never enters it); of the three November 10 hulls on card 005, FALCON adopts two (201-26 = its VI-0100, and the ADNOC L&S vessel) and does not adopt "Fujairah Energy" (single source); the November 8 Qeshm report is not established; Khor Mor is outside FALCON\'s perimeter',
 body="""FALCON answered card 005's ACTION (KB-FALCON-475, 11abbdc7be, 08:57 ET). No ladder item fired; marks 1 / 14 / 85 unchanged.

| Card 005 item | FALCON's grade |
|---|---|
| UKMTO via Argus: 11 attacked, 3 sank, week to November 4, unnamed | **Census stays 7.** QUBA and SELAT STORM fit two; the third is unnamed; AL JUSUFI mapping unproven. An unnamed sinking never enters the census |
| November 10 hulls: 201-26 near Lima, ADNOC L&S vessel, "Fujairah Energy" | **Two adopted:** 201-26 (= FALCON VI-0100) and the ADNOC L&S vessel. **"Fujairah Energy" not adopted** (one source). Card 005 already labelled that name single-source |
| Qeshm, November 8 night, Iranian official "US projectiles" | **NOT ESTABLISHED:** an Iranian statement alone never counts. FAL-09 0 of 5 |
| Khor Mor drone hit, November 8 (Iraqi Kurdistan) | **Outside FALCON's perimeter:** Iraq is out of FAL-08 and the rung; gas, not Gulf-ally crude; no STRIKES row; Iraq production is HAWK's dormant vector |
| South Pars Phase 14 fire, November 10 | Iranian gas; no FALCON rung |
| Abqaiq intercept line | Corrected by card 20261111-006 |

NEXUS's contradictions read listed card 005's three November 10 hulls against HAWK ("never three") and FALCON (two). This closes it on FALCON's count: **two confirmed hulls on November 10.**

No directed ask.""",
 sources="AGENTS/FALCON/workbook/KB.tsv KB-FALCON-475 (commit 11abbdc7be) ; PROME/inbox/processed/2026-11-11_from-NEXUS_catchup-contradictions.md C6 ; BOARD/SIG-W-20261111-005",
 action=[], info=['BRENT', 'HAWK', 'SAM', 'RED', 'TERRY', 'NEXUS', 'PROME'],
 precedence='PRIORITY', signal_type='research', confidence=0.9, lang='confirmed',
 cluster='IRAN_HORMUZ', domain='GEOPOL_ENERGY', entities=['FALCON census', 'UKMTO 201-26', 'ADNOC L&S', 'Fujairah Energy', 'Qeshm', 'Khor Mor', 'South Pars'],
 note="Owner grade of card 005's ACTION, routed to card 005's info line plus NEXUS (raised C6). Update, not a correction: card 005 carried the 'Fujairah Energy' name as single-source and the UKMTO count as reported; FALCON's grade settles both. PRIORITY: no ladder or gate moved.",
 extra=dict(updates=['SIG-W-20261111-005'], event_window='closed')),
]

stamp, paths = send(CARDS, "PROME prome-2b relay 11/11: ORACLE catch-up (bd6bf9d89c); NEXUS contradictions C6 and FALCON KB-475 (11abbdc7be)")
print(stamp)
print('\n'.join(paths))
