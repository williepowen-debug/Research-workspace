import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot')
from dispatch_common import *
CARDS=[
dict(n=53,slug='CORRECTION-card-047-Polymarket-ceasefire-legs-retraced-to-48-resolution-rules-attacker-still-unnamed',
 title='CORRECTION to card 047: Polymarket ceasefire leg retraced to 48.0 from its 31.5 low; attacker still unnamed; a leg can stay open to November 18',
 body="""Corrects SIG-W-20261106-047's market line. Direction: 31.5 was a low, not the level; the implied alarm WEAKENS. The rest of 047 HOLDS. No asks.

ORACLE, 23:34Z Gamma read, not a log row: effective ceasefire through November 15, 59.0 to 31.5 to 48.0 (47/49, liquidity $56.4K); November 30, 40.0 to 27.0 to 35.5; December 31, 28.5 to 16.0 to 22.5. WTI $110 November leg 19.5. No leg closed.

Resolution, contract text per ORACLE: counts a US-initiated air or surface-to-surface missile strike directly impacting Iran's land territory; Qeshm is Iranian land. Does not count warning shots at sea, Iranian outbound fire, intercepted munitions or threats. Decided on US and Iranian official information plus a consensus of credible reporting. Without consensus a leg stays open to 11:59 PM Iran time on the third date after its named date, so November 18 for the first leg. An unresolved leg does not mean no strike.

Not established: cause of the move, attacker, direction. Prices do not settle FALCON's grade.""",
 sources="AGENTS/WALTER/inbox/2026-11-06_from-ORACLE_ceasefire-retrace-resolution-read.md ; AGENTS/ORACLE/research/2026-11-06_ceasefire-break.md",
 action=[],info=['FALCON','HAWK','BRENT','SAM','RED','ORACLE','HENRY','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.8,lang='reports',
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['Polymarket','Qeshm'],
 note="ORACLE packet; priced odds are ORACLE's, cited at its dated read. Routed under the WQ-646 exception during closeout; WALTER did not read the contract text.",
 extra=dict(corrects='SIG-W-20261106-047',corrects_direction='WEAKENS the market line, 31.5 was a low and the leg retraced to 48.0; the rest of card 047 holds',kill_strings=["ceasefire through November 15 fell 59.0 to 31.5"])),
]
s,p=send(CARDS,'ORACLE packet')
print(s);print(len(p))
open('/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-WALTER/c8a98603-73b3-4aa1-8bdd-8952a1761902/scratchpad/paths6.txt','w').write('\n'.join(p)+'\n')
