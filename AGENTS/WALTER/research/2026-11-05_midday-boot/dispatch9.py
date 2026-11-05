import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[dict(n=42,slug='CORRECTION-data-center-100B-is-pre-vote-ballot-count-may-share-one-base',source='VULCAN',
 title='CORRECTION to card 034: the $100B figure is pre-vote, and the NYT and Bloomberg counts may share one base',
 action=[],info=['VULCAN','WATT','HENRY','RED','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.8,lang='confirms',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['Bisnow','Ballotpedia','Bloomberg'],
 body='''VULCAN caught both.

1. Card 034 read "over $100B of projects at risk" as post-vote context. Bisnow's piece is dated November 2, before the vote: "at least $100B of proposed projects in the crosshairs", from a Bloomberg analysis of Ballotpedia data. It is not a total after the results. Do not relay it as projects lost or blocked.

2. Card 034 said the 40-of-41 figure was firmed up by two wordings. Too strong: Bloomberg's Ballotpedia analysis also underlies Bisnow's "more than 40", so NYT and Bloomberg may share one base. Treat it as one count, reported, not independently confirmed. No Ballotpedia post-vote table was read.

Unchanged: the OpenAI pledge comes from the Bloomberg and NYT emails on 034's Sources line, not the Bisnow URL. Apple's budget cap stands as reported. No ask.''',
 sources='AGENTS/VULCAN KB-VULCAN-367/368 ; https://www.bisnow.com/news/national/data-center-community-relations/openai-plans-data-center-rebrand-to-make-projects-palatable-to-voters ; BOARD/SIG-W-20261105-034-Data-center-backlash-update-NYT-and-Bloomberg-carry-ballot-result-Apple-trims-AI-budgets.md',
 note='Owner-caught; Bisnow date is VULCAN\'s read.',
 extra=dict(corrects='SIG-W-20261105-034',corrects_direction='WEAKENS "firms up" — $100B predates the vote; counts may share one Ballotpedia base',kill_strings=['over $100B of projects at risk']))]
print(send(CARDS,'WALTER afternoon / VULCAN correction')[0])
