"""Bounded pinned review and CATO-authored proposed contract repair.
All owner mutations are isolated; the shared implementation is unchanged.
Proposal checks are author tests, not independent certification.
"""
import contextlib,io,json,os,subprocess,sys,tarfile,tempfile
from pathlib import Path
from unittest.mock import patch
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];REV='d1783bc3ff06ce2cfd36251c47518f1c21f789c2'
with tempfile.TemporaryDirectory(prefix='cato-hans-finish-') as td:
 repo=Path(td)
 with tarfile.open(fileobj=io.BytesIO(subprocess.check_output(['git','archive',REV,'AGENTS/HANS','scripts'],cwd=ROOT))) as arc:arc.extractall(repo,filter='data')
 for p in ROOT.iterdir():
  if p.name not in ('AGENTS','scripts'):(repo/p.name).symlink_to(p,target_is_directory=p.is_dir())
 for p in (ROOT/'AGENTS').iterdir():
  if p.name!='HANS':(repo/'AGENTS'/p.name).symlink_to(p,target_is_directory=p.is_dir())
 hans=repo/'AGENTS/HANS';sys.path.insert(0,str(hans/'scripts'))
 import fetch_eu as fe,closeout_check as cc
 print('PIN',REV)
 suite=subprocess.run([sys.executable,'-B',str(hans/'scripts/test_hans.py')],cwd=repo,capture_output=True,text=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
 print('OWNER SUITE',suite.returncode);print('\n'.join((suite.stdout+suite.stderr).splitlines()[-4:]));assert suite.returncode==0
 def norm(mode):
  def reply(req,**kw):
   day=req.full_url.split('date=')[1];row={'full':'85.0','gasDayStart':day}
   if mode=='same-row':row['gasDayStart']='2024-09-17'
   if mode=='no-date':row.pop('gasDayStart')
   if mode=='wrong-year':row['gasDayStart']=str(int(day[:4])+1)+day[4:]
   if mode=='wrong-day':row['gasDayStart']=day[:8]+'16'
   return io.BytesIO(json.dumps({'data':[row]}).encode())
  with patch.object(fe,'_agsi_key',lambda:'offline-fixture'),patch.object(fe.urllib.request,'urlopen',reply):return fe.agsi_norm('2026-09-17')
 for mode in ['same-row','no-date','wrong-year','wrong-day','valid']:
  result=norm(mode);assert (result[0] is None)==(mode!='valid');print('NORM',mode,result)
 def run_one(step,child):
  with patch.object(cc,'STEPS',[step]),patch.object(cc,'run',lambda *a:child),contextlib.redirect_stdout(io.StringIO()) as out:result=cc.main()
  return result,out.getvalue()
 for step in [s for s in cc.STEPS if 'consumer' in s[0]]:
  for rc,out in [(1,'SELF mode: ERROR - nothing scanned, 0 files'),(0,'CONSUMER CHECK\nERROR: nothing scanned')]:
   got,text=run_one(step,(rc,out));assert got==1;print('REPAIRED exact error',step[0],'rc',rc,'runner',got)
  real=cc.run(step[1],step[2]);got,text=run_one(step,real);assert got==0,(step[0],real)
  print('PASS real completed consumer',step[0],'child rc',real[0],'runner',got)
 # Actual cross-agent tool prints header then separator BEFORE it reads the ledger.
 cross=next(s for s in cc.STEPS if 'consumer CROSS' in s[0])
 real=cc.run(cross[1],cross[2]);ls=real[1].splitlines();header=next(i for i,l in enumerate(ls) if 'CONSUMER CHECK' in l)
 startup='\n'.join(ls[:header+2])
 child=cc.run([sys.executable,'-c','print('+repr(startup)+'); raise SystemExit(1)'],repo)
 got,text=run_one(cross,child);assert got==0
 print('OPEN real startup prefix then exit 1; no scan performed:');print(repr(child));print(text)
 selfstep=next(s for s in cc.STEPS if 'consumer --SELF' in s[0])
 # A separator before an error is not terminal. re.M makes $ match the internal newline.
 child=cc.run([sys.executable,'-c',"print('SELF mode: fixture\\n==========\\nERROR: nothing scanned'); raise SystemExit(1)"],repo)
 got,text=run_one(selfstep,child);assert got==0
 print('OPEN separator followed by error/exit 1:');print(repr(child));print(text)
 print('DONE. Storage correspondence closed for tested cases; runner completion remains open. No owner writes.')
 # CATO-authored proposal, tested only in this isolated copy; not an owner repair.
 import re,difflib
 contract=(r'CONSUMER CHECK[\s\S]*(?:^  (?:✓ clean —|🟠 \d+ CANDIDATE\(s\), zero certified-stale\.|🔴 \d+ stale (?:consumer )?reference\(s\))[^\n]*\n={10,}\s*\Z|^  ✓ ledger has no superseded values to check\.\s*\Z)')
 def proposed(rc,out):return rc==0 and cc._ok(rc,out,contract)
 for step in [s for s in cc.STEPS if 'consumer' in s[0]]:
  real=cc.run(step[1],step[2]);assert proposed(*real);print('PROPOSAL PASS actual completion',step[0])
 for name,rc,out in [('opening banner rc1',1,startup),('opening banner rc0',0,startup),('error after banner rc1',1,'CONSUMER CHECK\nSELF mode\n==========\nERROR: nothing scanned'),('error after banner rc0',0,'CONSUMER CHECK\nSELF mode\n==========\nERROR: nothing scanned'),('missing ledger',0,'CONSUMER CHECK\n==========\n  ⚠️ no ledger rows at fixture')]:
  assert not proposed(rc,out);print('PROPOSAL PASS rejects',name)
 for summary in ['  ✓ clean — every consumer is current or has it flagged superseded.','  ✓ clean — no surface under AGENTS/HANS/ carries the superseded value unqualified.','  🟠 2 CANDIDATE(s), zero certified-stale. A 🟠 is a prompt to LOOK.','  🔴 2 stale consumer reference(s). Send each owner a packet.','  🔴 2 stale reference(s) on YOUR OWN surfaces. You are the owner.']:
  complete='CONSUMER CHECK\n'+'='*66+'\nSELF mode: fixture\n'+summary+'\n'+'='*66
  assert proposed(0,complete)
  assert not proposed(1,complete)
  assert not proposed(0,complete+'\nERROR: nothing scanned')
 print('PROPOSAL PASS clean/candidate/stale terminal variants; nonzero and post-verdict error rejected')
 assert proposed(0,'CONSUMER CHECK\n==========\n  ✓ ledger has no superseded values to check.')
 print('PROPOSAL PASS legitimate no-superseded-values completion')
 old=(hans/'scripts/closeout_check.py').read_text()
 insert='# Non-strict consumers complete with rc=0. Require their terminal verdict,\n# not the opening banner; \\Z anchors to the end even when re.M is enabled.\n_CONSUMER_COMPLETE = '+repr(contract)+'\n\n'
 new=old.replace('STEPS = [',insert+'STEPS = [')
 for step in [s for s in cc.STEPS if 'consumer' in s[0]]:
  before='(0, 1, 2), r"'+step[4]+'"'
  assert before in new
  new=new.replace(before,'(0,), _CONSUMER_COMPLETE')
 Path('/tmp/cato-hans-consumer-contract-proposal.patch').write_text(''.join(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True),fromfile='a/AGENTS/HANS/scripts/closeout_check.py',tofile='b/AGENTS/HANS/scripts/closeout_check.py')))
 compile(new,'proposed_closeout_check.py','exec')
 print('PROPOSAL compiles; patch saved separately, NOT applied to shared HANS.')
