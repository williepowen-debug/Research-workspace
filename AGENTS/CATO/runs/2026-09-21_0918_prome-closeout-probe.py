"""Read-only probes for PROME closeout 251ef4949; no live state changes."""
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
REF = "251ef4949"
def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)
def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

a = module("cato_argus_receipt_probe", "PROME/tools/argus_scope.py")
manifest = json.loads(git("show", f"{REF}:PROME/state/argus_review.json"))
current = json.loads((ROOT / a.REVIEW_FILE).read_text())
assert current == manifest, "Manifest changed: use the pinned receipt, do not silently rebase this probe"
paths = git("diff-tree", "--no-commit-id", "--name-only", "-r", REF).decode().splitlines()
# Preserve historical baseline in process memory ONLY: the live baseline was advanced after delivery.
a._current_baseline_sha = lambda: manifest["baseline"]
rc, lines = a.verify_review(paths=paths, ref=REF)
print("PINNED DELIVERY VERIFIER RC", rc)
for line in lines: print(line)
for path in paths:
    if path in a.RECEIPT_PATHS: continue
    print("ACTUAL COMMIT PATH MATCH", path, a._committed_content_id(path, REF) == manifest["paths"].get(path))
print("The reported mismatch is outside PROME's nine-path commit; it remains a nonzero gate result.")

s = module("cato_spawn_cover_probe", "PROME/tools/spawn_list.py")
rows = git("show", f"{REF}:PROME/DOCKET.tsv").decode().splitlines()
for n in (312, 347):
    cells = rows[n-1].split("\t")
    print("BROCK ROW", n, "state", s.state_kind(cells[3]), "due", cells[0],
          "covered/excluded", s.covered(cells[3], cells[5] if len(cells)>5 else ""))
    print("STATE", cells[3])
    print("EXISTING SLATE FORM EXCLUDED", s.covered("PENDING · COVERED: PROME desktop boot slate — BROCK L0 spawn (SLATED)", ""))

arc = git("show", f"{REF}:PROME/archive/SCRATCH_ROTATED_2026-09-21.md")
block = arc.split(b"\n\n", 1)[1]
parent = git("show", f"{REF}^:PROME/SCRATCH.md")
print("ARCHIVE BLOCK IS EXACT PARENT SUBSTRING", block in parent)
for f in ("PROME/artifacts/decision_deck.html", "PROME/artifacts/decision_reference.html"):
    data = git("show", f"{REF}:{f}").decode()
    print("LOCAL DECK", f, {str(n): f'data-wq="{n}"' in data for n in (272,273,274)})
