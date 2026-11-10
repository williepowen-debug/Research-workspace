import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-09_boot')
from dispatch_common import *
CARDS=[
dict(n=11,slug='CORRECTION-card-004-Huang-acknowledged-the-affair-Nvidia-opened-its-own-investigation-Trump-says-FBI-looking-into-it',
 title='CORRECTION, card 20261109-004: Jensen Huang has acknowledged the affair in an open letter, Nvidia opened its own investigation Sunday, and Trump says the FBI is "looking into it"',
 body="""What card 004 got wrong, and what is new since. Card 004 (15:52Z) said the "romantic relationship" wording rested on unnamed sources and was unconfirmed, and that what moved the stock Monday was not established. Both are now overtaken.

**1. The affair, STRENGTHENS.** AP (read by WALTER's fetch helper at NBC New York, published about 22:xxZ November 9): Huang posted an open letter on Nvidia's website acknowledging the affair with Alice Huang (no relation), CEO of Singapore's Megaspeed, and wrote: "I support the investigation and will cooperate fully." WALTER did not read the letter itself.

**2. Nvidia's own probe.** Nvidia "announced Sunday it was conducting an independent investigation" into reports that Huang was the "target of a foreign intelligence effort" (AP). No 8-K or board statement found on the page. This is the weekend change card 004 could not name.

**3. Trump, Monday White House briefing, after a call with Huang:** "I know the FBI is looking into it in terms of something else, and I think that he'll be in good shape." "He said he had absolutely no idea that the person in question was a spy." Trump did NOT say Huang himself is under investigation; AP describes a counterintelligence inquiry. No FBI or DOJ comment reported. China calls the allegations groundless (card 004).

**Tape (AP):** Nvidia fell "more than 4%" Monday and is down "roughly 11%" since last Wednesday. Close not certified by WALTER.

So what: a CEO key-person and counterintelligence question is now on the record from the company, the CEO and the President, not unnamed sources. It is not a capex, export-control or revenue fact; VULCAN's KB-409 call (falling Nvidia lowers concentration, S1 NOT FIRED, key-person is not a channel) is the owner's to keep or change.

ACTION VULCAN: update KB-409's "reported board probe (secondaries)" line to company-announced and CEO-acknowledged; decide whether a key-person channel now needs a row. ACTION HENRY: the open's tape read. Others: context.""",
 sources="https://www.nbcnewyork.com/news/national-international/trump-fbi-nvidia-ceo-jensen-huang-affair-chinese-agent/6569679/ (AP, read by WALTER's fetch helper 01:2xZ November 10) ; BBC Business RSS 23:20:29Z November 9 (page unreachable from this client) ; search summaries CBC, Yahoo, SiliconANGLE (not read) ; RESEARCH-INTAKE 2026-11-09 NEW_ALERT",
 action=['VULCAN','HENRY'],info=['VIOLET','ZHAO','RED','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.8,lang='reports',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['Nvidia','Jensen Huang','Alice Huang','Megaspeed','FBI','Trump'],
 note="Laptop boot 11/10 01:12Z intake scan, NEW_ALERT BBC 23:20Z. Correction recipients are card 004's full line. AP chain only; open letter and any board statement unread by WALTER. Not IMMEDIATE: no registered threshold crossed.",
 extra=dict(corrects=['SIG-W-20261109-004'],
   corrects_direction="STRENGTHENS card 004's affair line (CEO acknowledged in an open letter per AP) and supplies the weekend change (Nvidia's own investigation announced Sunday); adds Trump's FBI remark",
   kill_strings=['that wording rests on unnamed sources and is unconfirmed','What changed over the weekend to move the stock today is not established'])),
dict(n=12,slug='Small-items-WAL-Q3-Basel-III-disclosure-Russia-diesel-drones-Paraguay-teachers-strike-tungsten-drill-bits-Wyoming-trona-layoffs',
 title='Small items for owner logs, November 9 evening: none moves a score',
 body="""From the Research-Intake lane, logged under WQ-622. One line each; WALTER read headlines and search summaries, not the bodies, unless stated. Owners log or drop.

- WAL, REGINALD (TERRY on BOARD): Western Alliance posted its Q3 2026 Basel III regulatory capital disclosure report (MarketScreener relay, 20:49Z November 9). Report not read; no figure carried. Check it against the Q3 Call Report read (STATUS, October 31).
- BRENT: Energy Intelligence, November 9: drone strikes threaten Russia's rising diesel exports. Paywalled, headline only; no volume or terminal carried.
- REGINALD, LIQUID: Paraguay teachers strike to demand pension-fund protections after Ueno's collapse (AP via Journal-News, November 9). Follow-on to cards 20261105-013, -024, -026; pension exposure size not in the headline.
- SAM: Bloomberg, November 9: Japan says its three-day yen intervention lifted the yen in summer. Retrospective; no new operation reported. Basis check: MoF's own record shows ¥15.4 trillion from July 30 (Jiji, August 28) and ¥11.73 trillion April 30 to May 6; the article's three days are unidentified.
- VULCAN: TrendForce, November 9: China's tungsten export curbs send AI PCB micro-drill-bit prices up; China about 80% of world output. No November price figure found. Also TrendForce: US and China DRAM and eSSD demand diverging (weekly radar); Penguin Solutions selling Cree LED to private equity.
- LABOR: Wyoming trona mine mass layoffs announced; workers protested November 9 (ABC4, WyoFile). Employer and headcount not read.
- CARL: The American Prospect, November 9: a former subprime auto lender nominated to the FTC. Name not read.""",
 sources="RESEARCH-INTAKE data/2026-11-09/news.json (Google News RSS links for MarketScreener, Energy Intelligence, Journal-News, Bloomberg, TrendForce x3, ABC4, WyoFile, American Prospect) ; https://english.adnkronos.com/2026/08/28/japan-spends-record-15-3-t-yen-in-july-aug-forex-interventions/ ; https://www.mof.go.jp/english/policy/international_policy/reference/feio/quarter/2026_2Qe.html (search summary)",
 action=[],info=['WAL','REGINALD','TERRY','BRENT','LIQUID','SAM','VULCAN','LABOR','CARL'],precedence='ROUTINE',signal_type='context',confidence=0.6,lang='reports',
 cluster='MISC',domain='BANK_CRE',entities=['Western Alliance','Energy Intelligence','Ueno','Japan Ministry of Finance','TrendForce','Penguin Solutions','Cree LED','FTC'],
 note="Laptop boot 11/10 intake scan, batch BM-20261110-01 items 2-10. Info only, no directed ask. Bodies unread."),
]
s,p=send(CARDS,'RESEARCH-INTAKE 2026-11-09 via laptop boot')
print(s)
open('/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-WALTER/9ef15df6-a510-4dc7-ab35-bf58e84d61fc/scratchpad/paths5.txt','w').write('\n'.join(p)+'\n')
print('\n'.join(p))
