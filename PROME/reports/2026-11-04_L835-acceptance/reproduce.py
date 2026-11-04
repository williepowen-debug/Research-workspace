"""Reproduce in disposable directories; does not execute source in candidate checkout.
Usage: python3 reproduce.py /home/willi/l835-phase2
Writes replay logs alongside this script; no source/receipt/install mutation.
"""
from pathlib import Path
import sys,tempfile,subprocess,tarfile,io,os,hashlib,json
src=Path(sys.argv[1]);out=Path(__file__).resolve().parent
candidate='5a2edeec2c7414c612478d59e32883bb527cef40';baseline='cf20665b2ecf9c19980e5030bc9e38293b44f25b'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=src,text=True).strip()==candidate
scratch=Path(tempfile.mkdtemp(prefix='l835-acceptance-replay-'))
def extract(sha,paths,dest):
 raw=subprocess.check_output(['git','archive',sha,*paths],cwd=src)
 with tarfile.open(fileobj=io.BytesIO(raw)) as t:t.extractall(dest,filter='data')
extract(candidate,['PROME','scripts','.claude','CLAUDE.md','AGENTS.md'],scratch)
subprocess.run(['git','init','-q',str(scratch)],check=True)
subprocess.run(['git','-C',str(scratch),'fetch','-q',str(src),baseline],check=True)
env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':'PROME/tools:PROME/tools/tests'}
def run(label,args,cwd=scratch):
 with (out/('replay-'+label+'.log')).open('w') as f:
  r=subprocess.run(args,cwd=cwd,env=env,stdout=f,stderr=subprocess.STDOUT)
 print(label,r.returncode,flush=True)
 if r.returncode:raise SystemExit('STOP: inspect replay log; no further tests run')
run('policy',[sys.executable,str(out/'independent_policy.py'),str(scratch)])
run('integration',[sys.executable,str(out/'independent_integration.py'),str(scratch)])
modules='test_argus_policy test_argus_contract test_argus_scope test_argus_scope_evidence test_argus_wq583 test_l835_phase2 test_review_mechanism_WQ240b test_closeout_simplification_WQ240 test_external_findings_2026_09_13 test_boot_charter_coverage test_parity_gate_L294_F3'.split()
run('regressions',[sys.executable,'-W','error::ResourceWarning','-m','unittest','-f','-v',*modules])
old=Path(tempfile.mkdtemp(prefix='l835-historical-replay-'))
extract(baseline,['PROME/tools/argus_scope.py','PROME/state/AUDIT_PERIMETER.tsv','PROME/tools/tests/test_argus_r100_consumed_move_WQ289.py'],old)
run('historical',[sys.executable,'-W','error::ResourceWarning','-m','unittest','-f','-v','PROME.tools.tests.test_argus_r100_consumed_move_WQ289'],old)
print('Temporary repositories retained:',scratch,old)
