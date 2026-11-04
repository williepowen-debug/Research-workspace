import sys,json,copy,unittest,subprocess,tempfile,os
from pathlib import Path
from unittest.mock import patch
sys.path[:0]=[sys.argv.pop(1)+'/PROME/tools/tests']
from test_argus_contract import ContractFixture,sc,ac
import prome_gate as gate
class Independent(ContractFixture):
 def consumer(self,tier):
  with patch.object(gate,'ROOT',self.root):
   gate.results.clear();gate.check_review_manifest(tier)
   return gate.aggregate_rc(gate.results,[])
 def test_new_suffix_partition_and_shadow_consumer(self):
  for protected in (False,True):
   rows=[('r/*.md','EXCLUDED'),('r/*','OWNED' if protected else 'EXCLUDED'),('r/*/**','EXCLUDED'),('PROME/**','OWNED')]
   self.write(sc.PERIMETER_FILE,'pattern\tclass\treason\n'+''.join(a+'\t'+b+'\tx\n' for a,b in rows))
   self.commit(sc.PERIMETER_FILE);self.base=self.git('rev-parse','HEAD');sc.record_baseline(self.base)
   self.freeze();self.assertEqual(self.consumer('standard'),1)
   self.assertEqual(sc.mark_reviewed('synthetic reviewer wiring only')[0],0)
   self.assertEqual(self.consumer('standard'),0)
   self.write('r/.gitignore','*\n!.gitignore\n');self.write('r/é','hidden source')
   self.assertEqual(self.git('-c','core.quotePath=false','check-ignore','r/é'),'r/é')
   self.assertIn('r/.gitignore',[x[1] for x in sc.porcelain_entries()])
   self.assertNotIn('r/é',[x[1] for x in sc.porcelain_entries()])
   self.assertEqual(sc.verify_review()[0],int(protected))
   self.assertEqual(self.consumer('standard'),int(protected));self.assertEqual(self.consumer('light'),int(protected))
   (self.root/'r/.gitignore').unlink();(self.root/'r/é').unlink()
 def test_old_approval_cannot_certify_changed_work_after_rollback(self):
  self.freeze();sc.mark_reviewed('synthetic');old=self.manifest()
  self.write('PROME/result','new work')
  fresh=self.freeze();self.assertEqual(fresh['verdict'],'FROZEN');self.assertEqual(fresh['contract']['reused'],{})
  self.assertEqual(self.consumer('standard'),1)
  self.save(old)
  # Restored approval is only for the old immutable candidate. New working bytes
  # must not be delivered accidentally or pass strict actual-commit verification.
  with self.assertRaises(ValueError):ac.deliver(sc,self.root/'no-message')
  new=self.commit('PROME/result')
  self.assertEqual(sc.verify_review(ref=new,snapshot=new)[0],1)
 def test_malformed_entire_policy_and_legacy_consumers(self):
  for pat in ['r/**/a','r/?','r/[a]','r/a*','/r','r//a','r/.git/a','r/*.md/**']:
   self.write(sc.PERIMETER_FILE,'pattern\tclass\treason\nr/**\tEXCLUDED\tx\n'+pat+'\tOWNED\tx\n')
   with self.assertRaises(ValueError):self.freeze()
  self.write(sc.PERIMETER_FILE,'pattern\tclass\treason\nPROME/**\tOWNED\tx\n')
  self.plan['delivered'][sc.PERIMETER_FILE]='test policy';self.freeze();sc.mark_reviewed('synthetic')
  old=self.manifest();old['schema']=2;self.save(old)
  self.assertEqual(sc.verify_review()[0],2);self.assertEqual(sc.mark_reviewed()[0],2)
  self.assertEqual(self.consumer('light'),2);self.assertEqual(self.consumer('standard'),2)
  with self.assertRaises(ValueError):ac.observe(sc,{})
  with self.assertRaises(ValueError):ac.deliver(sc,self.root/'message')
  fresh=self.freeze();self.assertEqual(fresh['verdict'],'FROZEN');self.assertEqual(fresh['contract']['reused'],{})
 def test_actual_schema2_rollback_does_not_certify_new_delivery(self):
  source=Path(sc.__file__).resolve().parents[2]
  baseline='cf20665b2ecf9c19980e5030bc9e38293b44f25b'
  for name in ('argus_scope.py','argus_contract.py'):
   data=subprocess.check_output(['git','show',baseline+':PROME/tools/'+name],cwd=source)
   target=self.root/'PROME/tools'/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
  self.commit('PROME/tools/argus_scope.py','PROME/tools/argus_contract.py')
  sc.record_baseline(self.git('rev-parse','HEAD'))
  def run(*args):
   return subprocess.run([sys.executable,str(self.root/'PROME/tools/argus_scope.py'),*args],cwd=self.root,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
  with tempfile.TemporaryDirectory() as td:
   plan=Path(td)/'plan.json';plan.write_text(json.dumps(self.plan))
   self.assertEqual(run('--record-review','--contract',str(plan)).returncode,0)
   self.assertEqual(run('--mark-reviewed','synthetic old audit').returncode,0)
   receipt=self.root/sc.REVIEW_FILE;old=receipt.read_bytes()
   self.assertEqual(json.loads(old)['schema'],2)
   self.write('PROME/result','post-cutover work, never reviewed')
   new=self.commit('PROME/result')
   receipt.write_bytes(old) # exact rollback receipt, never relabeled
   r=run('--verify-review','--ref',new,'--snapshot',new)
   self.assertEqual(r.returncode,1,r.stdout+r.stderr)
   self.assertEqual(receipt.read_bytes(),old)
unittest.main(verbosity=2,failfast=True)
