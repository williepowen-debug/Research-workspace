import json,csv,sys,contextlib,io
from pathlib import Path
from types import SimpleNamespace
sys.path.insert(0,'tools');import batch_manifest as bm
O=Path('research/2026-11-04_catchup');rows=json.loads((O/'intake-items.json').read_text());m={}
def fold(nums,sig):
 for n in nums:m[n]=('FOLD',f'SIG-W-20261104-{sig:03d}','Dated verified group or explicit source-limited lead; read linked card and verification report')
for nums,sig in [([292,456],19),([158,162,165],18),([117],8),([347,348,349],7),([350,353,354,356,359],10),([351,412,415],9),([201,202,203,204,440],11),([49,50,51,52,53,54,55,269,273,274,275,276,278,279,280,281,282,283,284,286],12),([434,435,437],13),([301,302,303],14),([295,297,304,305,307],15),([298,306],16),([410],17),([213],22),([214,216,455],20),([417,418,419],36),([376,379,380],37),([38,45,46],39),([139],40),([441,442],41),([144,149,373,381],49),([382,387,388],50),([188],51),([389],52),([74,75,76,77,78,79,80,82,83,312,313,315,316,317,318,319,320,321,322,323,325],53),([399,401,172],47),([124,125,126,127,128,129,130,355,357,358,361,414,416],57),([35,104,108,110,111,113,171,263,400],58),([17,59,60,62,63,163,293,296,299,402,408,433,436,464],59),([33,167,168,397,398,404,407,462],60),([218,221,229,447,452],61),([36,37,40,42,47,48,253,267,431],62),([161,164,390,391,393,394,395],63),([145,146,377,378],64),([409],48)]:fold(nums,sig)
for nums,ref,reason in [([18,19,20,189,190,250],'SIG-W-20261031-001 /004','Signed October31 decree and Novak plan already covered; wrapper date not new policy'),([169,170],'OSPREY STRIKES RU-20261020-TAMBOV-NIKOLSKOYE-LPDS','October20 event, not new November attack'),([56,288,289,290,291],'VERIFY-RESIDUAL-FINANCE.md','Old dated SEC/ratings commentary; no new November regulatory decision'),([369],'VULCAN reports/2026-10-29_L800_funding-gap-Q3-prints.md','November2025 original accounting story; mechanism already covered'),([439],'SIG-W-20261022-035','February2025 notification of2024 breach'),([184],'SIG-W-20261102-012','AlMayeda October30 already routed'),([241],'VERIFY-RESIDUAL-EVENTS.md','September RCLSandals agreement already CRUISE-covered'),([81,324],'VERIFY-RESIDUAL-LABOR.md','Hiring story references2025 cuts; no new layoff count'),([173,174,175,176,177,178,179,180,181,182],'anchors/IRAN_WAR.md','Older Saudi route/attack/restart reporting; no operator-confirmed new restart inferred'),([438],'CYPHER CYB-INC source record','September Sharetec four-day story recirculation; no new incident'),([344,345],'intake-items.json dated source record','Old bank-failure/card-delinquency source vintage, not November release'),([16],'intake-items.json row16','January2026 OSP, not new forward settlement')]:
 for n in nums:m[n]=('DUP',ref,reason)
for nums,sig in [([211],65),([215,217,219,220],66),([228],67),([1,10,15],68)]:fold(nums,sig)
# Routine items were individually title-screened; these decisions do not assert full article reads.
routine={88:'NFP here is insurance firm, not payroll release',118:'Personal-name obituary collision with WAL',119:'Walmart promotion, not WAL',120:'Obituary collision',121:'Sports venue BankOZK, not bank event',123:'Camera lens, not credit',185:'Option-chain listing, not fresh catalyst',277:'Communications hire, no insurer risk event',287:'Software commentary, not SEC action',403:'Advertising campaign, not Saudi route',432:'Toy-industry award, not TTF'}
for n,a in enumerate(rows,1):
 if n not in m:
  m[n]=('NO-ACTION','REVIEW.md#title-screen',routine.get(n,'Routine commentary, price recap, preview, promotion or non-transmission news; no separately established actionable delta in screened title. Body not claimed read.'))
with (O/'intake-dispositions.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['item','batch','source_index','title','disposition','reference','reason'])
 for n,a in enumerate(rows,1):w.writerow([n,a['batch'],a['index'],a['title'],*m[n]])
with contextlib.redirect_stdout(io.StringIO()):
 for n,(d,r,reason) in m.items():bm.cmd_item(SimpleNamespace(item=['BM-20261104-01',str(n),d,r]))
bm.cmd_close(SimpleNamespace(close='BM-20261104-01'))
# 49 posts plus six extra country claims in22 and two extra France/US event claims in28.
bmarks=json.loads((O/'bookmarks.json').read_text());bs={2:55,3:24,4:25,5:29,6:31,9:29,10:34,11:4,12:29,13:31,14:29,15:29,16:54,19:19,20:44,21:32,22:20,23:45,24:45,25:45,26:20,27:20,28:20,29:29,30:29,32:23,33:33,34:50,35:27,37:21,38:30,39:26,40:23,41:27,42:33,43:21,44:55,45:46,46:46,47:22,48:28,49:22}
no={1:'Chart read; model definition/backtest missing, no independent new measured signal or model implementation authorized',7:'Conditional political rhetoric; actual dated strike evidence routed019, no separate operational fact established',8:'Ex-ante Hartnett conditional forecast, not observed result; election outcome routed038',17:'Image/template read, authorship unverified, thread not fully read; optional systems idea, no build assigned',18:'Original body read: minor earthquakes/geothermal setting, no concrete economic damage or official imminent warning established',31:'Prior DOE400000barrel exchange already20261023-022; unsupported sludge/capacity inference withheld',36:'Anonymous loan unidentifiable; thread suggests earlyAugust auction; no new November event established, reopen only with identifier/current document'}
review=json.loads((O/'bookmarks-review.json').read_text());byid={r['id']:r for r in review['items']};bout=[]
for b in bmarks:
 n=b['n'];disp='FOLD' if n in bs else ('DUP' if n==31 else 'NO-ACTION');ref=f'SIG-W-20261104-{bs[n]:03d}' if n in bs else no[n]
 state='fully_read' if n in [1,4,11,18,45] else 'partly_read'
 rr=byid[b['id']];rr.update(disposition=disp,read_state=state,follow_up='AGENTS/WALTER/research/2026-11-04_catchup/REVIEW.md#bookmark-source-limits',ask_user=None)
 bout.append([n,b['id'],f'post{n}',disp,ref,state])
for n,country in enumerate(['Belgium','Luxembourg','Ireland','Netherlands','Estonia','Finland'],50):bout.append([n,bmarks[21]['id'],'post22/'+country,'FOLD','SIG-W-20261104-020','partly_read'])
bout.append([56,bmarks[27]['id'],'post28/FranceOctober','DUP','CYPHER CYB-INC-003','partly_read']);bout.append([57,bmarks[27]['id'],'post28/US-August26-27','DUP','SIG-W-20261029-042 / CYB-INC-054','partly_read'])
with (O/'bookmark-dispositions.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['item','post_id','content','disposition','reference','read_state']);w.writerows(bout)
(O/'bookmarks-review.json').write_text(json.dumps(review,indent=2)+'\n')
with contextlib.redirect_stdout(io.StringIO()):
 for n,p,c,d,r,s in bout:bm.cmd_item(SimpleNamespace(item=['BM-20261104-02',str(n),d,r]))
bm.cmd_close(SimpleNamespace(close='BM-20261104-02'))
print('INTAKE',__import__('collections').Counter(x[0] for x in m.values()));print('BOOKMARK',__import__('collections').Counter(r[3] for r in bout))
