import ast
import hashlib
import json
from pathlib import Path
import subprocess
import types
from datetime import date

ROOT = Path('/home/willi/Research-workspace')
REL = 'AGENTS/BRENT/scripts/eia_weekly.py'
path = ROOT / REL
before = subprocess.check_output(['git', 'show', '044e5ff2f760d92326e320b0b5536ecd2e23325d:' + REL], cwd=ROOT, text=True)
after = (Path(__file__).parent / 'reviewed_eia_weekly.py').read_text()

def reader(text):
    # Execute only imports needed by the parser, functions and constant assignments;
    # exclude FORGE import/.env loading and main execution.
    tree = ast.parse(text)
    safe = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.Assign)):
            safe.append(node)
    obj = types.ModuleType('isolated_eia')
    ns = obj.__dict__
    ns['__file__'] = str(path)
    ns['HAVE_FORGE'] = False
    ns['_forge'] = None
    exec(compile(ast.Module(body=safe, type_ignores=[]), str(path), 'exec'), ns)
    return obj

old, new = reader(before), reader(after)
result = {'head': subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
          'script_sha256': hashlib.sha256(after.encode()).hexdigest(), 'cases': []}
for filename in ['eia_2026-04-29.md','eia_2026-09-02.md','eia_2026-09-30.md']:
    text = (new.EIA_DATA_DIR / filename).read_text()
    a, b = old.extract_metrics(text), new.extract_metrics(text)
    result['cases'].append({'file':filename,'old':a,'new':b,
        'lost_keys':sorted(set(a)-set(b)), 'coverage_new': new.coverage(b,today=date(2026,10,4))})
text = (new.EIA_DATA_DIR / 'eia_2026-09-30.md').read_text()
rows = text.splitlines()
for i, row in enumerate(rows):
    if row.startswith('| **Gasoline product supplied, 4-wk avg**'):
        rows[i] = '| **Gasoline product supplied, 4-wk avg** | **8.721M b/d** | — | **+2.0% WoW** | UNKNOWN YoY |'
probe = new.extract_metrics('\n'.join(rows))
result['missing_yoy_probe'] = {'gas_yoy_latest':probe.get('gas_yoy_latest'),
    'coverage':new.coverage(probe,today=date(2026,10,4)), 'expected':'YoY missing; do not substitute WoW'}
print(json.dumps(result, indent=2))
