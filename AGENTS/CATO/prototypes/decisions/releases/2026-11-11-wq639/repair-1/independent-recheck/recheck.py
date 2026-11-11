import sys,tempfile,unittest,json,subprocess,hashlib
from pathlib import Path
BASE=Path('/tmp/cato-wq639-independent-recheck');tempfile.tempdir=str(BASE)
MVP=BASE/'tree/AGENTS/CATO/prototypes/decisions/mvp';sys.path.insert(0,str(MVP))
from test_wq639 import CardTests
import author_card
from queue_store import QUEUE
class Recheck(unittest.TestCase):
 def setUp(self):
  self.f=CardTests();self.f.setUp();self.addCleanup(self.f.doCleanups)
 def prep(self,existing=True):
  f=self.f
  if existing:f.install_options()
  p=Path(f.tmp.name)/'prepared';p.mkdir()
  result=author_card.prepare(f.root,'901',f.spec(),replace_source=existing)
  (p/'source.md').write_text(result.pop('source'));(p/'card.patch').write_text(result.pop('patch'));(p/'manifest.json').write_text(json.dumps(result))
  return p,result['source_path']
 def state(self):
  f=self.f
  return ({str(p.relative_to(f.root)):p.read_bytes() for p in f.root.rglob('*') if p.is_file() and '.git' not in p.relative_to(f.root).parts},f.git('write-tree'),f.git('rev-parse','HEAD'),f.git('rev-parse','origin/master'))
 def refuse(self,p):
  before=self.state()
  with self.assertRaises(ValueError):author_card.apply_prepared(self.f.root,p)
  self.assertEqual(self.state(),before)
 def test_question_closure_pointer_and_row_removal_refuse(self):
  p,path=self.prep();f=self.f;original=f.repo.path(QUEUE).read_text()
  variants=[original.replace('A: one task','A: a much larger task'),original.replace('A: one task','CLOSED A: one task'),original.replace(path,'PROME/proposals/reassigned.md'),'\n'.join(x for x in original.split('\n') if not x.startswith('| 901 |'))]
  for i,text in enumerate(variants):
   with self.subTest(case=i):f.put(QUEUE,text);self.refuse(p)
 def test_source_edits_and_remote_append_refuse(self):
  p,path=self.prep();f=self.f;original=f.repo.path(path).read_text()
  for text in [original.replace('Only this task','Two tasks'),original+'\nOwner appended a qualification far outside the patch hunk.\n']:
   with self.subTest(text=text[-65:]):f.put(path,text);self.refuse(p)
 def test_queue_append_and_other_row_change_refuse(self):
  p,path=self.prep();f=self.f;original=f.repo.path(QUEUE).read_text()
  for text in [original+'\nIndependent owner appendix\n',original.replace('Upload the report','Upload a different report')]:
   with self.subTest(text=text[-40:]):f.put(QUEUE,text);self.refuse(p)
 def test_success_preserves_unrelated_staging_and_commits(self):
  p,path=self.prep();f=self.f
  f.put('unrelated.txt','Other owner draft\n');f.git('add','unrelated.txt')
  tree=f.git('write-tree');head=f.git('rev-parse','HEAD');remote=f.git('rev-parse','origin/master');queue=f.repo.path(QUEUE).read_bytes()
  author_card.apply_prepared(f.root,p)
  self.assertEqual(f.repo.path(QUEUE).read_bytes(),queue)
  self.assertEqual(f.repo.path(path).read_bytes(),(p/'source.md').read_bytes())
  self.assertEqual(f.git('write-tree'),tree);self.assertEqual(f.git('rev-parse','HEAD'),head);self.assertEqual(f.git('rev-parse','origin/master'),remote)
 def test_fresh_card_stale_and_unchanged_success(self):
  p,path=self.prep(False);f=self.f;original=f.repo.path(QUEUE).read_text()
  f.put(QUEUE,original.replace('Exact caveat','Changed operational note'));self.refuse(p)
  f.put(QUEUE,original);tree=f.git('write-tree');author_card.apply_prepared(f.root,p)
  self.assertIn(path,f.repo.path(QUEUE).read_text());self.assertEqual(f.repo.path(path).read_bytes(),(p/'source.md').read_bytes());self.assertEqual(f.git('write-tree'),tree)
 def test_new_source_collision_refuses(self):
  p,path=self.prep(False);self.f.put(path,'Other owner created this file\n');self.refuse(p)
 def test_changed_patch_refuses(self):
  p,path=self.prep();patch=p/'card.patch';patch.write_bytes(patch.read_bytes()+b'\n');self.refuse(p)
 def test_missing_source_refuses(self):
  p,path=self.prep();self.f.repo.path(path).rename(self.f.repo.path(path+'.saved'));self.refuse(p)
 def test_raw_replacement_patch_target_guard(self):
  p,path=self.prep();f=self.f;original=f.repo.path(QUEUE).read_text()
  f.put(QUEUE,original.replace('A: one task','A: TWO tasks'));before=self.state()
  result=subprocess.run(['git','apply',str(p/'card.patch')],cwd=f.root,capture_output=True)
  self.assertNotEqual(result.returncode,0);self.assertEqual(self.state(),before)
 def test_real_cli_prepare_apply(self):
  f=self.f;f.install_options();spec=Path(f.tmp.name)/'spec.json';spec.write_text(json.dumps(f.spec()));out=Path(f.tmp.name)/'cli'
  cmd=[sys.executable,str(MVP/'author_card.py'),'--root',str(f.root)]
  prep=subprocess.run(cmd+['--wq','901','--input',str(spec),'--output',str(out),'--replace-source'],capture_output=True,text=True)
  self.assertEqual(prep.returncode,0,prep.stderr)
  before=f.git('write-tree');apply=subprocess.run(cmd+['--apply',str(out)],capture_output=True,text=True)
  self.assertEqual(apply.returncode,0,apply.stderr);self.assertEqual(f.git('write-tree'),before)
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Recheck));sys.exit(not r.wasSuccessful())
