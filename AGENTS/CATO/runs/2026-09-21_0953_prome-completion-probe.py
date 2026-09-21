"""Read-only completion-pass checks pinned to ecbb42ee4."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[3]
def load(name,path):
    sp=importlib.util.spec_from_file_location(name,ROOT/path)
    m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
def git(*args):
    return subprocess.check_output(["git",*args],cwd=ROOT)
m=load("cato_prome_completion_verify","PROME/tools/argus_scope.py")
d=json.loads(git("show","ecbb42ee4:PROME/state/argus_review.json"))
assert d==json.loads((ROOT/m.REVIEW_FILE).read_text()), "Live receipt changed; do not silently use a new one"
# The baseline was advanced after delivery. Restore its historical value in memory only.
m._current_baseline_sha=lambda:d["baseline"]
paths=git("diff-tree","--no-commit-id","--name-only","-r","ecbb42ee4").decode().splitlines()
rc,lines=m.verify_review(paths=paths,ref="ecbb42ee4")
print("Historical verifier",rc,lines)
for p in paths:
    if p not in m.RECEIPT_PATHS:
        print("COMMIT HASH MATCH",p,m._committed_content_id(p,"ecbb42ee4")==d["paths"].get(p))
s=load("cato_prome_completion_spawn","PROME/tools/spawn_list.py")
rows=git("show","ecbb42ee4:PROME/DOCKET.tsv").decode().splitlines()
for n in [312,347]:
    c=rows[n-1].split("\t");print(n,"excluded",s.covered(c[3],c[5]))
r=subprocess.run([sys.executable,"PROME/tools/orch_closeout.py"],cwd=ROOT,capture_output=True,text=True)
print("ORCH RC",r.returncode)
for line in r.stdout.splitlines():
    if "2026-09-21 ARGUS" in line or "2026-09-20 ANVIL" in line:print(line)
for f,needle in [("PROME/HANDOFF.md","record at the next DOCKET pass"),
                 ("PROME/HANDBOOK.md","next boot, no word needed (L424"),
                 ("PROME/artifacts/handbook.html","next boot, no word needed (L424")]:
    print("STALE COMPLETED-WORK INSTRUCTION",f,needle in git("show",f"ecbb42ee4:{f}").decode())
