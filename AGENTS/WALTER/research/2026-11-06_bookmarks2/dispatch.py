import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks2')
from dispatch_common import *
CARDS=[
dict(n=22,slug='US-distillate-stocks-99.3M-lowest-since-May-2003-SPR-282.2M-lowest-since-1982',
 title='US distillate stocks 99.3M barrels, lowest since May 2003; SPR 282.2M, lowest since October 1982 [w/e Oct 30]',
 action=['BRENT'],info=['HAWK','CARL','HENRY','RED','PROME'],precedence='PRIORITY',signal_type='context',confidence=0.95,lang='confirms',
 cluster='HYDROCARBON_INFRA',domain='OIL_ENERGY',entities=['WDISTUS1','WCSSTUS1','WCESTUS1','EIA','SPR'],
 body='''EIA weekly series, week ending October 30, read through the fleet tool November 6.

Distillate 99.259M barrels, −3.565M. WALTER checked the series back to 2001: the last reading at or under this is May 2, 2003, 97.303M. The post's "lowest since May 2003" holds.

SPR 282.184M, −0.399M. Last at or under this: October 15, 1982, 280.802M. Holds.

Commercial crude 409.760M, −0.865M.

The post's "−25% since January" and "−32% since March" were not checked. EIA's days-of-supply was not read.

Weekly stocks posted November 4; no BOARD card carried them until Will's bookmark.

BRENT: read against your distillate lines.''',
 sources='EIA series WDISTUS1, WCSSTUS1, WCESTUS1 via FORGE fetch.py, pulled 2026-11-06 ; X post 2118536096623571052',
 note='Bookmark 3. Primary figures checked; two-day gap on the board. Crack and days-of-supply context is BRENT\'s.'),
dict(n=23,slug='US-Navy-CMV-22B-squawked-7700-over-Oman-cause-unknown-Tasnim-attack-claim-unconfirmed',
 title='US Navy CMV-22B squawked emergency over Oman November 6; cause unknown, Tasnim attack claim unconfirmed',
 action=['FALCON'],info=['BRENT','HAWK','RED','PROME'],precedence='IMMEDIATE',signal_type='context',confidence=0.35,lang='alleges',
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['CMV-22B','RUDY72','Oman','Tasnim'],
 body='''A Flightradar24 screenshot on Mario Nawfal's X post shows RUDY72, CMV-22B, registration 169450, United States Navy, squawk 7700, at 12:55 UTC November 6, about 9,950 feet and 100 knots, near Mirbat, Oman. The tracker image was read; its authenticity was not tested.

CLAIM-ONLY: the post says unconfirmed Tasnim reports claim the aircraft came under attack off Oman. Original Tasnim item not reached.

7700 is a general emergency code. It says nothing about cause. An OSINT page records a CMV-22B squawking 7700 near Salalah on August 25, so this has a benign precedent.

Searched three ways, no wire, Navy or CENTCOM report found. Separately, Iranian claims of firing on US ships have been denied by CENTCOM before.

Not established: hostile action, damage, landing, crew state. Not a vessel; the FLASH bypass for a US naval vessel does not apply on this evidence.

FALCON: yours to grade. WALTER has not moved any ladder item.''',
 sources='X post 2118711752980386075 with tracker image ; https://www.osint613.com/location/arabian-sea ; https://www.jpost.com/middle-east/iran-news/article-898491',
 note='Bookmark 11. Decays fast, so routed at low confidence with the limits written in. Guard corpus: anchor inventory visited, POTUS, ADD#22 and ADD#26 considered, not the whole file. FALCON live.',
 extra=dict(narrative_channel='tasnim',anchor_unverified_as_of='2026-11-05')),
dict(n=24,slug='Samlyn-exited-non-financials-weeks-before-selloff-Walleye-blown-up-rumor-unsupported',
 title='Samlyn exited non-financial stocks weeks before the selloff and cuts analysts; "Walleye blown up" remains an unsupported rumor',
 action=['HENRY'],info=['VIOLET','LIQUID','RED'],precedence='PRIORITY',signal_type='context',confidence=0.7,lang='reports',
 cluster='POSITIONING_VALUATION',domain='MARKET_VOL',entities=['Samlyn-Capital','Walleye','ORCL'],
 body='''Adds to card 008.

Samlyn: Bloomberg November 6, headline and repost read, full text not, plus Hedgeweek. $7B fund, Rob Pohly. It sold industrials, tech and retail exposure weeks ago, before this selloff, to focus on global financials, and is dismissing senior analysts outside that sector. Not returning capital. Down about 5% this year through October, people familiar. No statement from the firm.

So this is a planned pivot, not forced selling. The "sold off nearly all its stocks" post reads worse than the facts.

⛔ Walleye "has blown up": a rumor from one X account, November 5. No outlet reports it. Reported fact stays card 008: −5.9% in October, cutting one unit, returning some capital.

⛔ "Oracle positions liquidated in dark pool", "many more hedge funds blew up", "hundreds of billions in realized losses": one unsourced post. Not carried.

HENRY: positioning context only.''',
 sources='https://www.bloomberg.com/news/articles/2026-11-06/hedge-fund-samlyn-dumps-all-stocks-but-financials-cuts-staff ; https://hedgeweek.com/news/samlyn-capital-cuts-staff-and-exits-most-equity-sectors-in-financials-pivot',
 note='Bookmarks 1, 2, 4. Searched Walleye rumor, no report found; a negative on one pass, stated as unsupported, not false.',
 extra=dict(kill_strings=['Walleye has blown up'])),
dict(n=25,slug='Europe-second-wave-flight-bomb-threats-hoaxes-20-to-27-flights-no-explosives',
 title='Europe: second wave of flight bomb threats, 20 to 27 flights November 5, hoaxes so far, no explosives found',
 action=['HANS'],info=['HAWK','YURI','RED','PROME'],precedence='PRIORITY',signal_type='context',confidence=0.75,lang='reports',
 cluster='MISC',domain='GEOPOL_NON_ENERGY',entities=['Europe-airlines','Bulgaria','Hungary','Finnair'],
 body='''Second wave in a week, Thursday November 5 into Friday. Counts differ: at least 20 flights (CBS), at least 27 (CBC). Al Jazeera: at least 17 disrupted by midday GMT Friday, a count less certain than Thursday's. First wave November 2–3.

Fighter escorts: Bulgaria's air force three airliners, Italy a Finnair flight, Hungary scrambled three times.

No explosives found. UK Transport Secretary: "malicious hoax threats". Czech police rate credibility low. An airport official told AP one email came from a self-described anti-feminist group. EU: not yet clear the alerts are connected. One outlet on the first wave noted a hybrid-warfare angle under review; not established.

No market channel found. Logged under WQ-622.

HANS: read at your lane, including any airline or insurance effect.''',
 sources='https://www.cnn.com/2026/11/05/world/live-news/plane-flights-bomb-threats-europe-intl ; https://www.aljazeera.com/news/2026/11/6/hoax-or-bomb-threats-what-we-know-about-flight-disruptions-across-europe ; https://www.cbsnews.com/news/europe-flights-airlines-hoax-bomb-threats/ ; https://www.cbc.ca/news/world/europe-bomb-threats-czechia-poland-france-9.7410169',
 note='Bookmark 5. Search snippets, pages not opened. HAWK and YURI on the hybrid question.'),
dict(n=26,slug='Small-items-AI-commitments-map-Columbus-office-vacancy-shinkin-branch-count',
 title='Small items for owner logs, November 6 midday: none moves a score',
 action=[],info=['VULCAN','BROCK','CREED','REGINALD','CYPHER'],precedence='ROUTINE',signal_type='context',confidence=0.55,lang='reports',
 cluster='MISC',domain='AI_CAPEX',entities=['Nvidia','Oracle','Meta','Google','Columbus-OH','Shinkin-Central-Bank'],
 body='''From Will's bookmarks, logged under WQ-622.

- VULCAN, BROCK: ZeroHedge "expanded AI capital web", dated October 30, extends Morgan Stanley's map. Off-balance-sheet labels: Google $1,059B, Meta $866B, Microsoft $594B, Nvidia $531B, Amazon $453B, Oracle $322B, Broadcom $202B. Compiled by ZeroHedge, not checked at filings; definitions unread. Linked URL not reached.
- CREED, REGINALD: Columbus, Ohio office vacancy per Colliers via Business First: Chase Tower 71%, Key Bank Building 65%, 250 High 58%, 65 East State 53%, Fifth Third Center 48%, 80 East Rich 48%, Continental Plaza 43%. Date of the data not stated; no loan event, so no case.
- CYPHER: a later post puts the shinkin outage at 3,430 branches and says Shinkin Central Bank apologized and blamed equipment. Card 005 said no branch count was printed in what it read; this one is unconfirmed, and a search found no copy.

Not routed: two market-statistics posts. One says QQQ last closed under its 200-day in March; HENRY's grade says April 7, and HENRY governs.''',
 sources='X posts 2118723435857690805, 2118509607710765292, 2118738525776474542 ; AGENTS/WALTER/research/2026-11-06_bookmarks2/BOOKMARK-REVIEW.md',
 note='Bookmarks 6, 9, 10. Info only, no directed ask. Co-op names kept off the BOARD per CYPHER guardrail.'),
]
s,p=send(CARDS,'WALTER bookmarks at Will request')
print(s);print(len(p));open('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks2/paths.txt','w').write('\n'.join(p)+'\n')
