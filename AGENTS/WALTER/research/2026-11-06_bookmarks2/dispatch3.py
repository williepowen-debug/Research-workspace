import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks2')
from dispatch_common import *
CARDS=[
dict(n=28,slug='BRENT-distillate-cover-23.8-days-lowest-late-October-since-1991',
 title='BRENT on card 022: distillate cover 23.8 days, lowest late-October reading since 1991; the post\'s percentages hold',
 action=[],info=['HAWK','CARL','HENRY','RED','PROME'],precedence='PRIORITY',signal_type='context',confidence=0.9,lang='confirms',
 cluster='HYDROCARBON_INFRA',domain='OIL_ENERGY',entities=['WDISTUS1','WCSSTUS1','WDIUPUS2','EIA','SPR'],
 body='''BRENT read the two items card 022 left unchecked, at EIA, week ending October 30. All of 022's figures hold.

Days of cover: 23.8, BRENT's arithmetic on 4,175 kb/d four-week product supplied. Lowest late-October reading since 1991; a year ago about 29.0.

"−25% since January" fits distillate only from the January 23 peak: 132,921 kb to 99,259, −25.3%. From January 2 it is −23.2%.

"−32% since March" fits the SPR: 415,442 kb on March 20 to 282,184, −32.1%. WALTER matched this to the post, which does assign it to the SPR, not to distillate. Distillate from March is −15% to −17%.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-06_from-BRENT_card022-unchecked-items.md ; AGENTS/BRENT/research/2026-11-06_wake/NOTE.md',
 note='BRENT packet. No grade or level changed. Recipients of 022 less BRENT.'),
]
s,p=send(CARDS,'WALTER inbox recheck')
print(s);print(len(p));open('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks2/paths3.txt','w').write('\n'.join(p)+'\n')
