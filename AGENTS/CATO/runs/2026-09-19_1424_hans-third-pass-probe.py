"""Pinned offline behavioral review; all mutations are in an isolated HANS copy.
Root scripts are pinned; other ancillary files and Git history are shared read-only.
Assertions describe verified repairs AND explicitly labelled residuals.
"""
import contextlib,csv,io,json,os,subprocess,sys,tarfile,tempfile,importlib
from pathlib import Path
from unittest.mock import patch
from datetime import date
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
REV='c7d02d780'
with tempfile.TemporaryDirectory(prefix='cato-hans-third-') as tmp:
 repo=Path(tmp)
 data=subprocess.check_output(['git','archive',REV,'AGENTS/HANS','scripts'],cwd=ROOT)
 with tarfile.open(fileobj=io.BytesIO(data)) as arc: arc.extractall(repo,filter='data')
 for child in ROOT.iterdir():
  if child.name not in ('AGENTS','scripts'): (repo/child.name).symlink_to(child,target_is_directory=child.is_dir())
 for child in (ROOT/'AGENTS').iterdir():
  if child.name!='HANS': (repo/'AGENTS'/child.name).symlink_to(child,target_is_directory=child.is_dir())
 hans=repo/'AGENTS/HANS';sys.path.insert(0,str(hans/'scripts'))
 import doc_audit as da,fetch_eu as fe,closeout_check as cc
 print('PIN',REV,'DATE',date.today(),'ANCILLARY HEAD',subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip())
 suite=subprocess.run([sys.executable,'-B',str(hans/'scripts/test_hans.py')],cwd=repo,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True)
 print('OWNER SUITE',suite.returncode,'\n','\n'.join((suite.stdout+suite.stderr).splitlines()[-6:]));assert suite.returncode==0
 assert da.audit()==[];print('CONTROL audit has no blocking findings')
 values={2021:71.26,2022:85.67,2023:93.87,2024:93.38,2025:81.09}
 def norm(mode='valid',value=None):
  def reply(req,**kw):
   day=req.full_url.split('date=')[1];y=int(day[:4]);row={'gasDayStart':day,'full':values[y] if value is None else value}
   if mode=='wrong-date':row['gasDayStart']='2020-01-01'
   if mode=='no-date':row.pop('gasDayStart')
   return io.BytesIO(json.dumps({'data':[] if mode=='four-years' and y==2023 else [row]}).encode())
  with patch.object(fe,'_agsi_key',lambda:'offline'),patch.object(fe.urllib.request,'urlopen',reply):return fe.agsi_norm('2026-09-17')
 assert abs(norm()[0]-85.054)<1e-9
 for mode,value,closed in [('four-years',None,True),('valid','NaN',True),('valid','inf',True),('valid',101,True),('wrong-date',None,False),('no-date',None,False)]:
  got=norm(mode,value);assert (got[0] is None)==closed;print('STORAGE norm',mode,value,got)
 def current(day,fill):
  with patch.object(fe,'_agsi_key',lambda:'offline'),patch.object(fe.urllib.request,'urlopen',lambda *a,**k:io.BytesIO(json.dumps({'data':[{'gasDayStart':day,'full':fill}]}).encode())):return fe.agsi_eu()
 for d,v,reject in [('2026-09-17','NaN',True),('2026-09-17',101,True),('2099-01-01',69.06,True),('1999-01-01',69.06,True),('2025-09-17',69.06,False),('2026-09-17',True,False)]:
  got=current(d,v);assert (got[0] is None)==reject;print('STORAGE current',d,repr(v),got)
 def render(st,normfun):
  with patch.object(fe,'ecb',lambda *a,**k:[('2026-09-18',2.5)]),patch.object(fe,'agsi_eu',lambda:(st,None)),patch.object(fe,'agsi_norm',normfun),patch.object(fe,'boe',lambda *a:('18 Sep 2026',3.75)),contextlib.redirect_stdout(io.StringIO()) as out:result=fe.main()
  return result,out.getvalue()
 badnorm=norm('wrong-date',50)
 result,out=render(('2026-09-17',69.06,None),lambda day:badnorm)
 assert not result['failures'] and '🟢 GAP TO 5-YR NORM +19.06pp' in out
 print('OPEN R1 wrong dates produce green +19.06pp, failures=[]; parsed norm',badnorm)
 for name,body,expect in [('future','01 Jan 2099,5.51',None),('12-day-old','07 Sep 2026,5.24',None),('9-day-old','10 Sep 2026,5.24',('10 Sep 2026',5.24)),('shuffled','18 Sep 2026,5.51\n07 Sep 2026,5.24',('18 Sep 2026',5.51))]:
  with patch.object(fe.urllib.request,'urlopen',lambda *a,**k:io.BytesIO(('DATE,IUDMNPY\n'+body+'\n').encode())):got=fe.boe('IUDMNPY')
  assert got==expect;print('BoE',name,got)
 # Legal valid step results for every other step; one failed child at a time.
 def runner(child,label_fragment):
  def fake(cmd,cwd):
   step=next(s for s in cc.STEPS if s[1]==cmd)
   return child if label_fragment in step[0] else (0,step[4] or 'orphan complete')
  with patch.object(cc,'run',fake),contextlib.redirect_stdout(io.StringIO()) as o:rc=cc.main()
  return rc,next(l.strip() for l in o.getvalue().splitlines() if 'MECHANICAL:' in l)
 for name,child in [('traceback',cc.run([sys.executable,'-c','raise RuntimeError("fixture")'],repo)),('missing script',cc.run([sys.executable,str(repo/'absent.py')],repo)),('argparse',cc.run([sys.executable,str(repo/'scripts/consumer_check.py'),'--bad-option'],repo)),('signal',(-15,'')),('timeout',(None,'TIMEOUT')),('empty-success',(0,''))]:
  for label in ['consumer CROSS','consumer --SELF','ledger nudge']:
   got=runner(child,label);assert got[0]==1
  print('REPAIRED runner',name,'child rc',child[0],'rejected by all three targeted steps')
 for label,marker in [('consumer CROSS','CONSUMER CHECK'),('consumer --SELF','SELF mode'),('ledger nudge','HANS')]:
  code='print('+repr(marker)+'); raise SystemExit(1)'
  child=cc.run([sys.executable,'-c',code],repo);got=runner(child,label);assert got[0]==0
  print('OPEN R2 early exit after marker',repr(marker),'child',child,'runner',got)
 # Real root consumer missing-directory failure already contains the accepted marker.
 real=cc.run([sys.executable,str(repo/'scripts/consumer_check.py'),'--agent','CATO_NO_SUCH_AGENT','--self','--from-ledger'],repo)
 got=runner(real,'consumer --SELF');assert real[0]==2 and got[0]==0
 print('OPEN R2 REAL missing self directory',real,'runner',got)
 good=runner((1,'nudge: [HANS] STATUS moving without ledgers — 1 ledger(s) behind'),'ledger nudge');assert good[0]==0;print('REPAIRED runner legitimate rc1 nudge retained')
 status=hans/'STATUS.md';orig=status.read_text();line_no=len(orig.splitlines())+2
 def prose(line):
  try:
   status.write_text(orig+'\n'+line+'\n');a,b=da._audit_full();return [(c,m) for c,m in a+b if c.startswith('C9-') and f'STATUS.md:{line_no} ' in m]
  finally:status.write_text(orig)
 cases=[('EU storage gap is -19.7pp; policy was unchanged today.',True),('The current BoE Bank Rate is 4.50%.',True),('EU storage gap is -19.7 percentage points.',True),('EU storage gap is -19.7pp; unrelated figure is -15.99.',False),('As of 2026-09-19, the current EU storage gap is -19.7pp.',False),('The gap is -19.7 percentage points.',False),('EU storage gap was -19.7pp; it is now -15.99pp.',False),('France OAT warning is >4.50%.',False)]
 for line,detect in cases:
  got=prose(line);assert bool(got)==detect,(line,got);print('C9',repr(line),'detected',bool(got))
 for rel,ident,key,detect in [('workbook/ML.tsv','ML-HANS-001','Entry_ID',True),('workbook/ML.tsv','ML-HANS-004','Entry_ID',True),('workbook/PREDICTIONS.tsv','HNS-07','Pred_ID',True),('workbook/FLOW.tsv','FLOW-HANS-1','Flow_ID',True),('registry/HANS_T_FIRED_LOG.tsv','HANS-F-001','fire_id',False)]:
  p=hans/rel;s=p.read_text();row=next(l for l in s.splitlines() if l.startswith(ident+'\t'))
  try:
   p.write_text(s.rstrip('\n')+'\n'+row+'\n');hit=any(c=='C12-ID-DUPLICATE' for c,m in da.audit());assert hit==detect;print('C12 duplicate',ident,'detected',hit)
  finally:p.write_text(s)
 # Freeze file accurately represents the original accepted counts (not today's extras).
 from collections import Counter
 baseline=subprocess.check_output(['git','show','3cad378f0:AGENTS/HANS/workbook/ML.tsv'],cwd=ROOT,text=True)
 counts=Counter(r['Entry_ID'] for r in csv.DictReader(io.StringIO(baseline),delimiter='\t'))
 frozen={l.split('\t')[0]:int(l.split('\t')[1]) for l in (hans/'registry/ML_LEGACY_DUP_IDS.txt').read_text().splitlines() if l and not l.startswith('#')}
 assert frozen=={k:v for k,v in counts.items() if v>1};print('REPAIRED R5 frozen counts match original 95 collision groups')
 # C0 claims only source presence, but its test deletes a comment, not behavior.
 srcpath=hans/'scripts/doc_audit.py';src=srcpath.read_text();start=src.index('    # ---- C14:');end=src.index('    # ---- C12:',start)
 try:
  status.write_text(orig+'\n## SESSION 99 — fixture\n')
  assert any(c=='C14-REGROWTH' or c.startswith('C14') for c,m in da.audit())
  srcpath.write_text(src[:start]+src[start:].splitlines()[0]+'\n'+src[end:]);importlib.reload(da)
  findings,notes=da._audit_full();assert not any(c.startswith(('C0-CHECK-MISSING','C14')) for c,m in findings)
  print('LIMIT C0 with C14 implementation removed but heading retained:',[x for x in notes if x[0].startswith('C0')],'no C14/C0 failure')
 finally:srcpath.write_text(src);status.write_text(orig);importlib.reload(da)
 print('R6 current STATUS unresolved strings:',{s:(s in orig) for s in ['13 checks','86 tests','see §SESSION 4','so the credit channel is ** Q3']})
 print('DONE isolated probes; no shared owner files written')
