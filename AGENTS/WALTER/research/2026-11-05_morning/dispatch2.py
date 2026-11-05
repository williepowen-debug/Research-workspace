import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=5,slug='AI-rotation-deepens-QQQ-down-3-Kospi-down-5-no-capex-cut',
 title='AI selling deepens globally after the midterms: QQQ down 3%, Kospi down 5%; no capex cut or enacted measure found',
 action=['VULCAN','HENRY'],info=['VIOLET','WATT','ZHAO','RED','PROME'],precedence='IMMEDIATE',signal_type='pattern-match',confidence=0.8,
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['QQQ','SMH','NVDA','MU','AVGO','CRWV','TSLA','Samsung','SK-Hynix','Kospi','Microsoft','Nscale','Texas'],
 body='''Vendor intraday 09:54 ET, not closes, against November 4 closes: S&P 7,581.82 (−1.39%), QQQ 669.30 (−3.27%), SMH 473.22 (−6.16%), MU −9.50%, NVDA −4.57%, AVGO −4.83%, CRWV −8.26%, TSLA −9.65%, VIX 18.01 (+8.43%). KRE +1.24%, HYG −0.15%: bank and credit proxies are not joining so far.

Asia November 5: Kospi −5.28% to 5,383.80 with a sell sidecar; SK Hynix −9.46%; Samsung −7.57%; Taiex −3.2%; TSMC −0.88% (Korean and Taiwan press via helper).

Cause is REPORTED, not established. Nothing enacted. The hard leg is Texas: governor-elect Hinojosa's promised moratorium, office January 19, on top of Abbott's August pause; Wells Fargo puts Texas at 27% of planned gigawatts, UBS about 30% of 2028 additions at risk (estimates). Goldman calls a national moratorium unlikely. Selling predates the vote. Microsoft declined an option to expand its Nscale Texas deal months ago (Reuters, one source; contract stands). "Microsoft cuts $5B" is a re-dated October 28 item: KILL. AMD data center +97% cuts the other way. No margin or forced-sale report found; TSLA cause INDETERMINATE.

ACTION VULCAN: read against gate S1. ACTION HENRY: index mechanics.''',
 sources='research/2026-11-05_morning/VERIFY-AI-TAPE.md ; research/2026-11-05_morning/tape-1455Z.json ; https://www.cnbc.com/',
 note='Rule 9 helper verdict CORRECTED-FRAMING on the sweep-threatens-data-centers claim, so RED on the info line. Reuters, Bloomberg and FT originals not reached. HENRY live this hour; VULCAN STATUS dated October 30. Copy list trimmed under WQ-556 C: LIQUID and SAM omitted, no credit or carry leg shown. Rotation is a label, not a finding.',
 extra={'verify_research_verdict':'CORRECTED-FRAMING','kill_note':'Microsoft cuts $5B is the October 28 capex trim re-dated'}),
dict(n=6,slug='DEWEY-card-peer-check-Capital-One-move-not-shared-Citi-unread',source='DEWEY',
 title='DEWEY peer check: Capital One modified-card jump not shared by five issuers read; Citi unread',
 action=[],info=['CARL','REGINALD','GIBBS','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.85,
 cluster='CONSUMER_STAGFLATION',domain='CONSUMER_CREDIT',entities=['COF','SYF','BFH','JPM','BAC','AXP','C'],
 body='''Follow-on to card 20261104-080. Report AGENTS/DEWEY/output/2026-11-04_card-modified-cohort-peer-check.md, commission Will's go in the DEWEY window November 4 20:59 ET; no WALTER flag.

Delinquent share of each rolling 12-month modified group, June to September 2026: Capital One domestic card 17.2% to 25.2%; Synchrony 22.9% to 23.7%; Bread 18.8% flat; JPMorgan retained card 11.3% to 11.6%; Bank of America card and other consumer 14.4% to 14.2%; American Express card 8.4% flat. On issuers read the move points to Capital One specifically; cause UNKNOWN. JPMorgan's group +74.1% on the year with its share flat, reason UNKNOWN.

Spot-check at primary, WALTER, American Express Q3 10-Q Table 2.7: card rows sum to 3,042 current, 202 and 76 past due, 3,320 total; matches DEWEY. Other loans correctly excluded.

Do not relay as "only Capital One" without naming Citi as unread, a Capital One credit break, hidden delinquency, or JPMorgan stress. Do not rank issuers on delinquent share; perimeters differ. CARL consumed DEWEY's packet in 0e11b4958, thesis NOT YET.''',
 sources='AGENTS/DEWEY/output/2026-11-04_card-modified-cohort-peer-check.md ; https://www.sec.gov/Archives/edgar/data/4962/000000496226000409/axp-20260930.htm',
 note='Research-output per CHECKLIST 2.8b; quality gate figure checked. Delivered copy to CARL already exists from DEWEY; no ACTION line. Verify verdict VERIFIED-PRIMARY on the one figure spot-checked, not the whole report.',
 extra={'verify_verdict':'VERIFIED-PRIMARY'}),
]
print(send(CARDS,'WALTER November 5 morning pass / Rule 9 helper / DEWEY return')[0])
