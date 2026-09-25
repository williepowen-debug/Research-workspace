# CE-R3-8: a declaration ADDED to the manifest after --mark-reviewed (hand edit) is honoured — REVIEWED is not bound to the declared set
from harness import *
f = Fx("ce8"); f.move(); f.freeze(None)        # ARGUS reviewed a manifest with NO declared moves
m = Path(f.repo) / A.REVIEW_FILE; d = json.loads(m.read_text()); d["consumed_moves"] = {DEST: ORIGIN}; m.write_text(json.dumps(d))
show("pair declared AFTER REVIEWED — ARGUS never saw it", f.verify())
f.done()
