import importlib.util, sys, unittest
sys.path.insert(0, '/home/willi/Research-workspace/PROME/tools'); sys.path.insert(0, '/home/willi/Research-workspace/PROME/tools/tests')
spec = importlib.util.spec_from_file_location('argus_contract', sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
sys.modules['argus_contract'] = m
import test_argus_contract as T
assert T.ac is m
suite = unittest.defaultTestLoader.loadTestsFromTestCase(T.PerimeterPinTests)
r = unittest.TextTestRunner(verbosity=0).run(suite)
print('FAILED:', sorted(t.id().split('.')[-1] for t, _ in r.failures + r.errors))
