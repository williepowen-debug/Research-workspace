from pathlib import Path
from datetime import datetime,timezone
import csv,json
R=Path('/home/willi/Research-workspace'); D=R/'AGENTS/WALTER/research/2026-10-19_afternoon';paths=[]
cards=[dict(n='013',slug='china-q3-gdp-45-domestic-investment-still-weak',title='China Q3 GDP accelerates to4.5%; investment/property remain weak',domain='ASIA_CONTAGION',cluster='ASIA_CHINA',priority='PRIORITY',action=['ZHAO'],info=['SAM','RED','HENRY','LIQUID','BRENT','PROME','CARL'],entities=['China','NBS'],body='''[NBS October19 release](https://www.stats.gov.cn/english/PressRelease/202610/t20261019_1965619.html),10:00Beijing=October18 22:00ET, reports preliminary Q3 realGDP+4.5%y/y versusQ2+4.3%; q/q+1.2%,nine-month+4.6%. September retail+1.1%y/y versusAugust+0.4%,industrial output+5.5%. Nine-month fixed investment−7.2%,private−10.4%,property−20.6%; new-property sales value−13.9%. GDP is constant-price; activity measures have their own nominal/comparable bases and periods.

The faster headline is counterevidence to a simple acceleration-down narrative; it does not establish broad domestic-demand or property recovery. ZHAO ACTION: integrate this existing scheduled macro release into current China/property/transmission work; no threshold or vector grade imposed. Other recipients INFO.

Rule9 helperCONFIRMED; NBS substantive text recovered through web-search response, direct-open failed. WALTER separately recovered the primary result; no independent national-accounts audit. Release timestamp belongs to Beijing, notMondayUSmorning. No trade/newstudy/launch.'''),dict(n='014',slug='france-monday-bond-selloff-after-known-unrest',title='France Monday borrowing-cost rise follows already-routed weekend unrest',domain='EUROPE_MACRO',cluster='MISC',priority='IMMEDIATE',action=['HANS','BOND'],info=['LIQUID','REGINALD','CARL','RED','PROME'],entities=['France','Germany','OAT','Bund'],body='''Monday market follow-through to already-routed unrest(1018-004), not a new protest discovery. [ReutersOctober19](https://www.investing.com/news/economy-news/french-markets-tumble-as-riots-add-to-political-crisis-4958015) reports INTRADAY OAT10Y4.90%(+13bp),Bund3.45%(+4bp),spread146bp. Displayed11:19update timezone unspecified.

[HANS governing screen](https://www.ideal-investisseur.fr/en/markets/oat-bund-spread.html),October19row:OAT4.85%,Bund3.43%,spread142.3bp versus137.4October16(+4.9bp). Bond-fixing/final-close timestamp unverified;sitewideCACclose is not bond fixing. Do not merge the intraday146 with daily142.3 or derive precise spread from rounded yield legs.

This is continued sovereign stress, not a newHANS-T-10fire:existingOPEN state/exit0-of-5 retained;both quoted legs remain above fire rails, not exit evidence. No US-funding transmission, government collapse or dated censure vote established.

HANS/BOND ACTION: carry Monday market follow-through/basis distinction in existing sovereign coverage;BOND takes time-critical interpretation. OthersINFO. Rule9CONFIRMED/CORRECTED-FRAMING;Reutersbody from search response/direct-openfailed,governingscreen directlyread. No launch,threshold,trade or external send.''')]
for c in cards:
 now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ');sid='SIG-W-20261019-'+c['n'];bp='BOARD/'+sid+'-'+c['slug']+'.md'
 header={'to':c['action'],'action':c['action'],'info':c['info'],'from':'WALTER','date':'2026-10-19','timestamp':now,'dispatched':now,'signal_id':sid,'domain':c['domain'],'signal_type':'data-point','cluster':c['cluster'],'precedence':c['priority'],'confidence':0.92,'entities':c['entities'],'source':'Public source refresh plus Rule9 verification; references and retrieval limits in body','dispatch_note':'Existing domain work only; source dates and bases preserved.','event_window':'closed'}
 if 'CARL' in c['info']:header.update(consumer_transmission='counter_evidence' if c['n']=='013' else 'none',consumer_lens='mixed')
 def y(v):return '['+', '.join(v)+']' if isinstance(v,list) else str(v)
 with (R/bp).open('x') as f:f.write('---\n'+'\n'.join(k+': '+y(v) for k,v in header.items())+'\n---\n\n# '+sid+' — '+c['title']+'\n\n'+c['body']+'\n')
 paths.append(bp)
 def app(p,row):
  with (R/p).open('a') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow(row)
 app('AGENTS/WALTER/routed/route_log.tsv',[now,sid,'Public sources / Rule9 helper',c['title'],c['priority'],','.join(c['action']),','.join(c['info']),'0.92'])
 for who in c['action']+c['info']:
  role='ACTION' if who in c['action'] else 'INFO'
  if who in ['PROME','TERRY'] or (who in ['CARL','RED'] and role=='INFO'):continue
  hp=f'AGENTS/{who}/inbox/WALTER/{sid}.md';(R/hp).parent.mkdir(parents=True,exist_ok=True)
  with (R/hp).open('x') as f:f.write(f'# {sid} — {c["title"]}\nBOARD: /{bp}\nPriority: {c["priority"]}\nRole: {role}\nFrom: WALTER\nDate: 2026-10-19\n\n## Kernel\n{c["body"]}\n\n## Why you got this\nExisting domain and transmission routing.\n\n## Requested action\n'+('Integrate the dated evidence in existing authorized domain work; no new study or launch.' if role=='ACTION' else 'INFO only; no directed work.')+'\n\n## Confidence / caveats\n0.92;source/retrieval/basis limits above travel with the figures. Publication and consumption separate.\n')
  app('AGENTS/WALTER/routed/delivery_log.tsv',[now,sid,who,role,'CODEX',c['priority'],hp,'written_not_delivered_pending_push','Foreign dirty tree; no verified independent-session relay; consumption UNKNOWN'])
  paths.append(hp)
(D/'news-route-paths.json').write_text(json.dumps(paths,indent=2)+'\n');print('\n'.join(paths))
