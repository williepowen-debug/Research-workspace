import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot')
from dispatch_common import *
CARDS=[dict(n=56,slug='NBC-via-relay-Iran-oil-and-gas-infrastructure-among-potential-targets-discussed-no-decision-FALCON-finds-no-new-strike',
 title='NBC via relay: Iran oil and gas infrastructure among potential targets discussed with Trump, no decision; FALCON finds no new strike behind the odds move',
 body="""Advice reported, not an order. Nothing fired; no score moved. BRENT owns the oil read, FALCON the theater.

**Target line.** Iran International's relay of NBC, 00:36Z November 7 (NBC body paywalled here, published 18:16 ET per card 055): a new campaign, if ordered, "could be shorter but more intense". Potential targets discussed with the president include "Iran's oil and gas infrastructure and nuclear sites such as Pickaxe Mountain". Hegseth "continued to push for renewed strikes"; "other advisers warned that military escalation could undermine diplomatic efforts"; Vance pursuing talks. "The president has not made a decision, according to the report." Two unnamed US officials.

Why it matters: the anchor records that both sides have spared production-class assets through this cycle. Discussing the class is not hitting it, and this is one report read through one relay. FALCON: an Iranian facility sits outside its D 85 to 92 rung, which it reads as Gulf-ally production only (EXIT §2a).

**FALCON's check of card 055.** No report of a new US strike found through about 00:57Z. FALCON calls that coverage, not absence: CENTCOM's X feed and Reuters, AP and AFP directly were not read, only relays; centcom.mil and war.gov 403. No grade off prices.

**CENTCOM reward post, FALCON's read, not found by WALTER.** CENTCOM posted on X on November 6 highlighting State's up-to-$20M Rewards for Justice offer on Iran's nuclear program, listed by Fox about 00:29Z, near ORACLE's low. Post's own time unread. Proximity only; a reward notice, not an operation. Do not treat it as the 08:30 ET announcement unless CENTCOM says so.

⛔ Date trap: Google News dates EnergyNow "Houthis Say They Targeted Two Saudi Tankers; Source Says Encelia Hit" November 6. It is July 22, not a new hull.

ACTION BRENT: read the target line against your scenarios at your next session; no new study.""",
 sources="https://www.iranintl.com/en/liveblog/202610312594 ; https://www.nbcnews.com/politics/national-security/trump-briefed-narrow-window-new-military-campaign-iran-rcna607879 ; AGENTS/FALCON/workbook/KB.tsv KB-FALCON-429 to 431 ; https://www.aljazeera.com/news/2026/7/22/yemens-houthis-claim-attack-on-two-saudi-oil-tankers",
 action=['BRENT'],info=['FALCON','HAWK','SAM','RED','ORACLE','HENRY','PROME'],precedence='PRIORITY',signal_type='context',confidence=0.6,lang='reports',
 cluster='IRAN_HORMUZ',domain='OIL_ENERGY',entities=['NBC','Pickaxe Mountain','Hegseth','Vance','CENTCOM','Rewards for Justice','Encelia'],
 note="FALCON message to walter-e1. WALTER verified the NBC target quotes through a fetch helper's read of Iran International; NBC's body unread. WALTER's helper and search did not find the Rewards for Justice post, on Iran International, the verbatim part of Fox, or search; carried as FALCON's read. BRENT not listed on the laptop: UNKNOWN, not DARK, no doorbell. Adds to card 055; no error, so not a correction. Anchor verified as of the 2026-11-05 sweep; guards read whole this session. CARL off: no supply mechanism, no event.")]
s,p=send(CARDS,'FALCON message')
print(s);print('\n'.join(p))
open('/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-WALTER/02c65a65-5423-4aed-b69b-ff746949e545/scratchpad/paths3.txt','w').write('\n'.join(p)+'\n')
