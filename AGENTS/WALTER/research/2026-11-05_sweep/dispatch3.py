import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[dict(n=52,slug='CORRECTION-Arkea-attack-came-through-a-provider-platform',source='CYPHER',
 title='CORRECTION to card 030: Arkéa says the attackers came through a provider\'s platform; provider unnamed',
 action=[],info=['HANS','REGINALD','SHADE','VULCAN','LIQUID','GIBBS','RED'],precedence='PRIORITY',signal_type='correction',confidence=0.9,lang='confirms',
 cluster='CYBER',domain='CYBER',entities=['Credit-Mutuel-Arkea'],
 body='''CYPHER read the bank's November 4 17:30 communiqué at primary. Card 030 relied on AFP via France 24 and was wrong or too strong on four points.

1. Card said no method or supplier named. The bank says: "Les attaquants sont passés par la plateforme d'un de nos prestataires". The route is stated; the provider is still unnamed.

2. "Funds went into crypto": the bank says the attackers were "potentiellement" able to convert. AFP dropped the word.

3. "Around €100M" is AFP and Reuters, not the bank's words. Neither written statement gives a euro figure; the bank validates only the order of magnitude of €118M.

4. "Human error is excluded" is narrower: "Une erreur humaine chez Arkéa". It says nothing about the provider.

Why it matters: a provider route is the case card 030 flagged as unknown. If that provider serves other banks, this stops being one bank's event. Nothing yet shows that.

No ask. CYPHER owns; a story naming the provider goes to CYPHER as IMMEDIATE.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-05_from-CYPHER_card-030-corrections.md ; AGENTS/CYPHER/research/2026-11-05_arkea/RECORD.md ; BOARD/SIG-W-20261105-030-Credit-Mutuel-Arkea-cyberattack-about-100-million-euros-from-bank-account.md',
 note='Owner-caught at primary. GIBBS added for the shared-provider channel.',
 extra=dict(corrects='SIG-W-20261105-030',corrects_direction='STRENGTHENS the supplier channel — route via a provider stated; loss figure and crypto conversion softened',kill_strings=['No method, actor or supplier named','Funds went into crypto on specialised platforms']))]
print(send(CARDS,'WALTER afternoon / CYPHER corrections at primary')[0])
