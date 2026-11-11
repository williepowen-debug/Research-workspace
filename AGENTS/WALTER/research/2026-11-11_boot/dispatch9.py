import sys, csv, glob
from pathlib import Path
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-11_boot')
from dispatch_common import *

CARDS = [
dict(n=14, slug='CORRECTION-card-004-SEC-FY2026-1.1B-is-total-monetary-relief-752M-disgorgement-plus-343M-penalties-not-penalties-lowest-since-2008-unchecked',
 title='CORRECTION, card 20261111-004: the SEC\'s FY2026 "$1.1B" is total monetary relief ordered ($1.095B = $752M disgorgement and prejudgment interest + $343M civil penalties), not "penalties"; "lowest since 2008" is unchecked',
 body="""**What was wrong.** Card 004's SEC line relayed a post saying the SEC "obtained orders for penalties totaling $1.1 billion, the lowest tally since 2008". WALTER did not open the release.

**At the primary** (SEC press release 2026-113, November 10, read by BROCK, KB-BRK-482):

| Item | FY2026 (to September 30) |
|---|---|
| Enforcement actions | 348 (235 standalone, 113 follow-on) |
| **Monetary relief ordered** | **$1.095B** |
| of which disgorgement and prejudgment interest | $752M |
| of which **civil penalties** | **$343M** |

**What holds:** the $1.1B total, rounded. **What changes:** penalties are $343M, about a third of it. "Lowest since 2008" was not checked by BROCK or WALTER; treat it as the poster's claim. BROCK notes the release names private-fund fraud (pre-IPO share funds) and adviser "fraudulent valuations and mismarking" as categories, but no private-credit fund or BDC valuation case.

No directed ask.""",
 sources="SEC press release 2026-113 https://www.sec.gov/newsroom/press-releases/2026-113-sec-announces-enforcement-annual-results-fiscal-year-2026 (read by BROCK) ; AGENTS/BROCK/workbook/KB.tsv KB-BRK-482 ; PROME/inbox/processed/2026-11-11_from-BROCK_catchup-hiking-fed-read.md ; BOARD/SIG-W-20261111-004",
 action=[], info=['RED', 'VIOLET', 'HENRY', 'VULCAN', 'LIQUID', 'SAM', 'BROCK', 'CORAL', 'AEOLUS', 'CYPHER', 'PROME'],
 precedence='ROUTINE', signal_type='correction', confidence=0.9, lang='confirmed',
 cluster='MISC', domain='PRIVATE_CREDIT', entities=['SEC', 'SEC enforcement FY2026', 'press release 2026-113'],
 note="Correction-class: card 004 relayed a 'penalties' total that is total monetary relief. Recipients are card 004's full line. R1 row COR-20261111-14, banner on card 004 and the INDEX marker in the same commit. ROUTINE: context line, no score or threshold.",
 extra=dict(corrects=['SIG-W-20261111-004'], corrects_direction="WEAKENS card 004's SEC line: $1.1B is total monetary relief, civil penalties are $343M; 'lowest since 2008' unchecked; the rest of card 004 holds", kill_strings=['penalties totaling $1.1 billion'], event_window='closed')),

dict(n=15, slug='ZHAO-a-December-hike-does-not-make-China-a-forced-Treasury-seller-PBOC-resisting-appreciation-USDCNY-6.6612-Japan-at-159.38-is-the-live-Asian-seller',
 title='ZHAO: a priced December hike does not make China a forced seller of Treasuries (the PBOC is resisting yuan appreciation, USD/CNY 6.6612 with the fix set weaker than spot); the live Asian forced-official-seller risk is Japan, USD/JPY 159.38, 0.62 yen under the 160 line where MOF sold ¥15.4T in July and August',
 body="""ZHAO's read (KB-ZHAO-265 to 267; outbox note 711dcd8f28), November 11:

| Item | ZHAO's figure and read |
|---|---|
| China forced-sale channel | currency defence, and it is **shut**: USD/CNY 6.6612 (from 6.6727 on 11/10) while DXY rose 102.23 → 102.93; the CFETS fix 6.7191 is set about 0.7 to 0.9% weaker than spot, so the PBOC is **resisting appreciation**, not defending the yuan |
| China Treasury flows | six-month net −$71.5B (TIC, August) is not defence-driven; a hike does not mechanically add to it |
| Valuation, not flow | +12bp on the 10-year (11/06 → 11/10) cuts China's reported LEVEL by roughly $3.5B to $4B on price in the November data (ESTIMATE; 5 to 6 year duration ASSUMED). It touches the $650B level line, not September flows (ZHA-22, 11/18) |
| Japan | USD/JPY 159.38 (SAM, 11/11) is 0.62 yen under 160, where Japan's MOF sold ¥15.4T on July 30 to August 3. If Asia supplies forced official selling this quarter, it comes from Tokyo, not Beijing |
| Hong Kong | a hike HIBOR does not follow widens the carry gap from −128.5bp to about −154bp; USD/HKD 7.8455; no HKMA activity through 11/11 |

BOND's soft indirect shares at the refunding auctions are consistent with this, but they are not a foreign-official measure (ZHAO).

**Owners:** LIQUID owns the Treasury-market consequence, SAM the yen. ZHAO makes no ask; the 160 line is SAM's call.""",
 sources="AGENTS/ZHAO/outbox/2026-11-11_to-LIQUID-SAM_hawkish-fed-china-not-a-forced-seller.md (commit 711dcd8f28) ; AGENTS/ZHAO/workbook/KB.tsv KB-ZHAO-265, -266, -267",
 action=[], info=['LIQUID', 'SAM', 'BOND', 'HENRY', 'RED', 'PROME'],
 precedence='PRIORITY', signal_type='research', confidence=0.8, lang='reports',
 cluster='ASIA_CHINA', domain='UST_FOREIGN', entities=['PBOC', 'USD/CNY', 'CFETS fix', 'TIC', 'Japan MOF', 'USD/JPY', 'HKMA', 'HIBOR'],
 note="ZHAO outbox signal handed to WALTER for routing by PROME prome-2b (ZHAO does not deliver). UST_FOREIGN row: owner ZHAO; ZHAO named LIQUID and SAM; BOND (backup, auction composition) and HENRY, RED info. Figures are ZHAO's as labelled; WALTER did not re-pull. PRIORITY: composition read before ZHA-22 on 11/18; no threshold.",
 extra=dict(event_window='open')),
]

stamp, paths = send(CARDS, "PROME prome-2b relay 11/11 10:2x ET: BROCK KB-BRK-482 (SEC primary) and ZHAO outbox 711dcd8f28")
board = [p for p in paths if p.startswith('BOARD/SIG-W-20261111-014')][0]
with (W / 'registry/CORRECTIONS.tsv').open('a') as f:
    csv.writer(f, delimiter='\t', lineterminator='\n').writerow([
        'COR-20261111-14', '2026-11-11', 'WALTER', 'RED,VIOLET,HENRY,VULCAN,LIQUID,SAM,BROCK,CORAL,AEOLUS,CYPHER,PROME', board, '2026-11-25', 'LIVE',
        "-1111-004 said SEC FY2026 penalties totaled $1.1B; IS total monetary relief $1.095B = $752M disgorgement + $343M civil penalties (SEC 2026-113 via BROCK KB-BRK-482); lowest-since-2008 unchecked",
        'WEAKEN'])
p = Path(glob.glob(str(ROOT / 'BOARD/SIG-W-20261111-004-*.md'))[0]); s = p.read_text(); i = s.index('\n---\n', 4) + 5
p.write_text(s[:i] + "> **Correction, November 11 — SIG-W-20261111-014:** The SEC line's \"penalties totaling $1.1 billion\" is total monetary relief ordered: $1.095B = $752M disgorgement and prejudgment interest + $343M civil penalties (SEC release 2026-113, via BROCK). \"Lowest since 2008\" is unchecked. The rest of this card holds.\n" + s[i:])
print(stamp)
print('\n'.join(paths))
