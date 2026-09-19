"""Pinned read-only correction checks; passes and remaining text are separate outputs."""
import csv,io,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
REV='7edb949a3008b58e2aa6359bd0413228ec735e62'
BASE='c0092ebad'
def git(*a):return subprocess.check_output(['git','-C',str(ROOT),*a],text=True)
def read(p,r=REV):return git('show',r+':'+p)
def rows(p,r=REV):return list(csv.DictReader(io.StringIO(read(p,r)),delimiter='\t'))
def check(label,ok):
 print(('PASS' if ok else 'FAIL')+': '+label)
 assert ok,label
print('PIN',REV)
brief='AGENTS/ZHAO/NEXUS_BRIEF.md';status='AGENTS/ZHAO/STATUS.md'
bl=read(brief).splitlines();st=read(status).splitlines()
check('original brief line 19 marked SUPERSEDED before old text',bl[18].index('SUPERSEDED')<bl[18].index('ZHAO carried two lapse clocks'))
check('LIQUID ask re-pointed', 'RE-POINTED' in bl[68] and 'July:' in bl[68])
check('SOFR and vector 8 carry corrected at own text', 'RESOLVED 2026-09-18' in bl[97] and 'RESOLVED 2026-09-17' in bl[97])
scommit=git('log','-1','--format=%H',REV,'--',status).strip();bcommit=git('log','-1','--format=%H',REV,'--',brief).strip()
check('brief follows STATUS',subprocess.run(['git','-C',str(ROOT),'merge-base','--is-ancestor',scommit,bcommit]).returncode==0)
print('STATUS / brief commits',scommit,bcommit)
check('prediction ledger unchanged',read('AGENTS/ZHAO/workbook/PREDICTIONS.tsv')==read('AGENTS/ZHAO/workbook/PREDICTIONS.tsv',BASE))
kb={r['ID']:r for r in rows('AGENTS/ZHAO/workbook/KB.tsv')}
check('KB-177 through 180 present',all('KB-ZHAO-'+str(n) in kb for n in range(177,181)))
check('KB-180 marks inference as ASSUMPTION',kb['KB-ZHAO-180']['Epistemic']=='ASSUMPTION')
for n in [156,166,174,175,176]:
 check('parent KB-'+str(n)+' has correction marker', 'CORRECT' in kb['KB-ZHAO-'+str(n)]['Notes'].upper())
for p in ['AGENTS/ZHAO/workbook/KB.tsv','AGENTS/ZHAO/workbook/FLOW.tsv','AGENTS/ZHAO/docket/CATALYSTS.tsv']:
 data=list(csv.reader(io.StringIO(read(p)),delimiter='\t'));check('TSV widths '+p,all(len(x)==len(data[0]) for x in data[1:] if x))
print('BIS catalyst rows:')
for r in rows('AGENTS/ZHAO/docket/CATALYSTS.tsv'):
 if 'Affiliates' in str(r):print(r)
print('Remaining active brief passages (not the corrected historical bullet):')
for n in [16,17,18,92]:print(brief+':'+str(n),bl[n-1])
print('Remaining STATUS passages:')
for n in [17,168,178]:print(status+':'+str(n),st[n-1])
oldkb={r['ID']:r for r in rows('AGENTS/ZHAO/workbook/KB.tsv',BASE)}
print('KB-173 wholly unchanged:',kb['KB-ZHAO-173']==oldkb['KB-ZHAO-173'],'status',kb['KB-ZHAO-173']['Status'])
p='PROME/inbox/2026-09-19_from-ZHAO_CORRECTED-battery-decision.md';decision=read(p)
print('Corrected decision:')
print(decision)
print('No 3E901.a entry in new matrix:', '3E901.a' not in decision)
print('Original closeout memo unchanged:',read('PROME/inbox/2026-09-19_from-ZHAO_session-closeout.md')==read('PROME/inbox/2026-09-19_from-ZHAO_session-closeout.md',BASE))
newpacket=read('AGENTS/ZHAO/outbox/2026-09-19b_to-VULCAN-HAWK-HENRY_CORRECTION-2-dates-and-scope.md')
for owner in ['VULCAN','HAWK','HENRY']:
 result=subprocess.run(['git','-C',str(ROOT),'grep','-l','-F','CORRECTION #2. My correction packet',REV,'--','AGENTS/'+owner],capture_output=True,text=True)
 print(owner,'replacement heading found in recipient tree:',result.returncode==0,'grep rc',result.returncode)
 assert result.returncode in [0,1]
print('Outbox route is explicitly pending:', 'Proposed route: PROME' in newpacket)
print('RESULT: checked repairs exist; residuals above remain. No shared owner file written.')
