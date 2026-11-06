import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks2')
from dispatch_common import *
CARDS=[
dict(n=27,slug='CORRECTION-Osprey-precedent-not-only-benign-FALCON-grades-not-established',
 title='CORRECTION to card 023: the benign precedent was one-sided; FALCON grades the Osprey NOT ESTABLISHED',
 action=[],info=['FALCON','BRENT','HAWK','RED','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.6,lang='reports',
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['CMV-22B','Oman','Fars','KB-FALCON-418'],
 body='''Card 023 cited only the August 25 Salalah squawk as precedent. FALCON adds the other side: a US Apache was lost off Oman June 8, tied by a US initial inquiry to an Iranian drone. Search text only, FALCON's read.

Also from FALCON: Fars via Entekhab, published 16:44 Tehran time November 6, reports the CMV-22B's 7700 off southern Oman with no attack claim. So the event has an Iranian report, and that report does not carry the attack claim. The Tasnim item stays unread by FALCON and WALTER.

FALCON's grade: NOT ESTABLISHED, KB-418.

Survives from 023: cause unknown; no wire, Navy or CENTCOM report found by WALTER; tracker image not authenticated.''',
 sources='https://entekhab.ir/fa/news/946729 ; FALCON message 11:35 ET',
 note='FALCON message. WALTER picked the one precedent found; a benign-only list tilted the card.',
 extra=dict(corrects='SIG-W-20261106-023',corrects_direction='WEAKENS — benign-only framing withdrawn; cause still unknown',kill_strings=[])),
]
s,p=send(CARDS,'WALTER FALCON message')
print(s);print(len(p));open('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks2/paths2.txt','w').write('\n'.join(p)+'\n')
