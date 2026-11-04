import pathlib, tempfile, shutil, importlib.util, unittest, sys
root=pathlib.Path('/home/willi/Research-workspace')
sys.path.insert(0,str(root/'PROME/tools'))
drafts=root/'PROME/reports/2026-11-04_kimi-maintenance-recovery'
with tempfile.TemporaryDirectory(prefix='prome-L910-draft-') as td:
 overlay=pathlib.Path(td)
 for p in root.iterdir():
  if p.name!='PROME': (overlay/p.name).symlink_to(p,target_is_directory=p.is_dir())
 (overlay/'PROME').mkdir()
 for p in (root/'PROME').iterdir():
  if p.name not in ('CLOSEOUT.md','CLOSEOUT_PROCEDURES.md'): (overlay/'PROME'/p.name).symlink_to(p,target_is_directory=p.is_dir())
 shutil.copyfile(drafts/'CLOSEOUT.candidate.md',overlay/'PROME/CLOSEOUT.md')
 shutil.copyfile(drafts/'CLOSEOUT_PROCEDURES.candidate.md',overlay/'PROME/CLOSEOUT_PROCEDURES.md')
 suite=unittest.TestSuite()
 for name in ['test_closeout_simplification_WQ240','test_review_mechanism_WQ240b']:
  spec=importlib.util.spec_from_file_location(name,root/'PROME/tools/tests'/f'{name}.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); m.ROOT=overlay
  for obj in vars(m).values():
   if isinstance(obj,type) and issubclass(obj,unittest.TestCase):
    for method in vars(obj).values():
     if getattr(method,'__unittest_expecting_failure__',False): method.__unittest_expecting_failure__=False
  suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(m))
 result=unittest.TextTestRunner(verbosity=1).run(suite)
 sys.exit(not result.wasSuccessful())
