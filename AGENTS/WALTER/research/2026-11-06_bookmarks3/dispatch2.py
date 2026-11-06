import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks3')
from dispatch_common import *
CARDS=[
dict(n=34,slug='CORRECTION-Microsoft-Oracle-wind-down-is-part-of-a-larger-cloud-partnership-reassessment',
 title='CORRECTION to card 029: Reuters places the Oracle wind-down inside a larger reassessment of Microsoft\'s cloud partnerships; card 029 carried only the older-capacity framing',
 action=[],info=['VULCAN','LIQUID','BROCK','HENRY','RED','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.7,lang='reports',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['Microsoft','Oracle-Corp','KB-VULCAN-391'],
 body='''Omission caught by VULCAN, KB-VULCAN-391. WALTER verified it at the page.

Reuters, November 6, citing Bloomberg and people familiar: Microsoft is winding down the arrangement "as part of a larger reassessment of billions of dollars in cloud partnerships".

Card 029 left that out and said only that the capacity was older. Its facts stand: 2023 contract, no renewal, capacity being turned off, value unknown.

What weakens: WALTER's closing framing, "older capacity dropped, newer spec demanded", is one reading. The older-chip reason comes from relays of Bloomberg. A wider review could reach other providers. Its size and direction are unknown: Bloomberg's body is unread, and VULCAN's two searches found no second account.

Do not read card 029 as a contained older-chip event. VULCAN records no score move.''',
 sources='https://live.euronext.com/en/financial-news/microsoft-winding-down-oracle-deal-rent-ai-cloud-capacity-bloomberg-news-reports ; KB-VULCAN-391, VULCAN commit f0741982cc',
 note='VULCAN message. WALTER read the Reuters line through a helper and dropped it from the card.',
 extra=dict(corrects='SIG-W-20261106-029',corrects_direction='WEAKENS — older-capacity framing is one reading; a wider reassessment is reported, size and direction unknown',kill_strings=['NONE — framing correction, no literal phrase to kill'])),
]
s,p=send(CARDS,'WALTER VULCAN message')
print(s);print(len(p));open('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks3/paths2.txt','w').write('\n'.join(p)+'\n')
