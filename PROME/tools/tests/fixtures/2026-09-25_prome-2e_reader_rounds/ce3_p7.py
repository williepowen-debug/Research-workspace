# CE-R3-3: P7 — does the manifest-only form (paths=None: --mark-reviewed, prome_gate) now fetch / change output?
from harness import *
f = Fx("ce3")
f.move()
calls = []
real = A._fetch_origin_sha
def spy():
    calls.append(1); return real()
with patch.object(A, "_fetch_origin_sha", spy):
    f.freeze(None); base = f.verify(paths=None); n0 = len(calls)
    f.freeze({DEST: ORIGIN}); n1 = len(calls)            # includes mark_reviewed
    after = f.verify(paths=None); n2 = len(calls)
print("fetch calls: undeclared paths=None:", n0, "| record+mark_reviewed with declaration:", n1 - n0, "| paths=None verify with declaration:", n2 - n1)
show("paths=None, undeclared", base); show("paths=None, declared, remote OK", after)
sh("git", "remote", "set-url", "origin", str(f.tmp / "gone.git"), cwd=f.repo)   # network down
show("paths=None, declared, remote UNREACHABLE", f.verify(paths=None))
rc, msg = A.mark_reviewed("fx2"); print("mark_reviewed with remote unreachable:", rc, msg[:120])
f.done()
