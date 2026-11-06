import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot')
from dispatch_common import *
CARDS=[
dict(n=20,slug='CORRECTION-UKMTO-197-26-incident-November-5-not-November-6-Velos-Sapphire-IMO-one-fatality',
 title='CORRECTION to card 018: the waterline explosion was November 5, a time-late UKMTO report; IMO lists Velos Sapphire as one fatality',
 action=[],info=['FALCON','BRENT','HAWK','SAM','RED','PROME'],precedence='IMMEDIATE',signal_type='correction',confidence=0.85,lang='confirms',
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['UKMTO-197-26','Velos-Sapphire','IMO'],
 body='''FALCON caught two errors in card 018.

1. Date. Card 018 said the explosion was November 6. UKMTO Warning 197-26 is a time-late report: incident 2200 UTC November 5, 16 NM east of Khasab, posted November 6. There is no separate November 6 event on this evidence. CBS itself says Thursday. Source: Siasat embedding the post text, WANA, TASS, CBS; ukmto.org not read by WALTER.

2. Status. Card 018 said "IMO listed one missing". IMO's table as at November 6 reads VELOS SAPPHIRE "One seafarer fatality", FALCON's own fetch 11:11 ET.

Also from FALCON. The undated CENTCOM mine line traces to about October 28, "all internationally recognized shipping lanes" cleared, Shafaq relay, primary unread; AFP's "all mines" is a compression. ⛔ Al Jazeera's "3 tankers reported hit" is one UKMTO report plus two IRGC claims.

Survives from 018: no confirmed mine, sinking, Yanbu hit, signed text or US answer found; IRGC mine claims CLAIM-ONLY; Najran and Mecca-region intercepts per CBS. FALCON: no mark moved.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-06_from-FALCON_card018-corrections.md ; imo.org incidents table per FALCON',
 note='FALCON packet. WALTER took the CBS blog stamp as the event date; ADD#26 discriminator one missed it. Recipients of 018. Filed with the anchor note fixed in the same commit.',
 extra=dict(corrects='SIG-W-20261106-018',corrects_direction='NEUTRAL — event date and casualty status; fact pattern unchanged',kill_strings=['3 tankers reported hit','IMO listed one missing'])),
]
s,p=send(CARDS,'WALTER inbox recheck')
print(s);print(len(p));open('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot/paths7.txt','w').write('\n'.join(p)+'\n')
