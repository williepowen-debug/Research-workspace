import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=7,slug='new-UKMTO-tanker-strike-north-of-Qatar-IRGC-mine-claims-no-neutral-confirmation',
 title='UKMTO reports a tanker struck north of Qatar; Iranian mine and fire claims remain unconfirmed; no deal or reopening',
 action=['FALCON','BRENT'],info=['HAWK','SAM','NEXUS','RED','PROME'],precedence='IMMEDIATE',signal_type='catalyst',confidence=0.7,
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['UKMTO','IRGC','Hormuz','Madinat-ash-Shamal','Qatar','Oman','South-Korea','Brent'],
 body='''NEW, relayed, UKMTO primary 403: tanker struck by two unidentified projectiles, event 11/4 23:20Z (03:20 Gulf time 11/5), 50 NM N of Madinat ash Shamal, Qatar; crew and damage unconfirmed; no name, flag or attacker. Gulf, not Hormuz; absent from FALCON's list ending GRIT.

CLAIM-ONLY, night 11/4–11/5: IRGC via Fars says a tanker "striking a mine" on the southern route, a supertanker "massive fire" with no mechanism stated, and a tug that caught fire assisting. Iran's Navy via Tasnim says a tanker hit a mine east of Hormuz. No names or positions; the two may overlap. Do not merge the tug with SELAT STORM.

ANSWERS at sources reached: no neutrally confirmed mine detonation; no new confirmed sinking; no signed deal, reopening or public US acceptance. Araghchi–Albusaidi call: technical "progress", no text or date; mediated.

CORRECTED: India/China exemption is a lawmaker's remark; South Korea's mission is south of Oman, not yet approved. Oil up about 2.5% intraday; no source read ties it to these claims. BZF27 96.94, 09:34 ET, vendor, not a settle.

ACTION FALCON: ladder #2, census. ACTION BRENT: marks.''',
 sources='research/2026-11-05_morning/VERIFY-IRAN.md ; https://www.tasnimnews.com ; ABC live via AOL ; Asharq Al-Awsat 11/5',
 note='Rule 9 helper plus guards read in full pre-dispatch (ADD#26 five discriminators applied; ADD#7 and 7/27 Tasnim mine guards bind). Anchor full sweep 2026-11-05 01:44Z, this is a bounded check, clock unchanged. AP: most ships do not report attacks, so no UKMTO match is not proof of no fire. ukmto.org, centcom.mil 403. FALCON owns grades.',
 extra={'verify_research_verdict':'INDETERMINATE on mine and fire claims; CONFIRMED on UKMTO report via relays','kill_note':'ABC Hegseth stranglehold is March 13; EnergyNow Morgan Stanley peace deal is June 16; EnergyNow banks hike forecasts is September 11; Anadolu ceasefire wording is kill-on-sight'}),
dict(n=8,slug='European-dailies-TTF-85-OAT-fire-holds-gilts-inside-bands',
 title='European dailies: TTF about €85, far below the fired 100 line; France compound stays over its lines',
 action=['HANS'],info=['BRENT','BOND'],precedence='PRIORITY',signal_type='research',confidence=0.7,
 cluster='INFLATION_TRANSMISSION',domain='EUROPE_MACRO',entities=['TTF','HANS-T-07','HANS-T-08','HANS-T-10','HANS-T-05','OAT','Bund','BTP','EURUSD'],
 body='''Trading Economics screens, intraday November 5, not closes; named contract and official settle not read.

TTF about €85/MWh, down more than 18% on the week, lowest in over two weeks. Fired ladder HANS-T-07: L3 >100 fired October 28 with its settle disputed; €85 sits under L3 and over L2 >66. The row states no exit; HANS owns any state change. Reported reason: diplomacy hopes and the midterms, not established.

AGSI+ gas day November 3, latest: fill 74.07%, native five-year mean 89.842%, gap −15.772 pp. HANS-T-08 fire open, exit >−12 ×5 not met.

Bund 3.26% (−2 bp): T-05 watch >3.00 open, orange >3.75 not met. ECB AAA 3.340 [November 4] is a different basis.
OAT 4.74% (−8 bp), Trading Economics spread about 148 bp: T-10 compound still over >100 and >4.50; exit <90 and <4.40 not met; ideal-investisseur governing screen failed (404), so no governing grade.
BTP 4.34%, spread about 108 bp: T-09 not met. EURUSD about 1.125: T-11 not met.

ACTION HANS: named-contract TTF read and ladder state.''',
 sources='https://tradingeconomics.com/commodity/eu-natural-gas ; research/2026-11-05_morning/hans-observations.json ; https://tradingeconomics.com/germany/government-bond-yield ; https://tradingeconomics.com/france/government-bond-yield ; https://tradingeconomics.com/italy/government-bond-yield ; https://tradingeconomics.com/euro-area/currency',
 note='Step 6c HANS daily pull. HANS STATUS dated October 29, so these are WALTER screens awaiting owner grade. HANS-T-12 uninstrumented, no clean-board credit.'),
]
print(send(CARDS,'WALTER November 5 morning pass / Rule 9 helper / guards read')[0])
