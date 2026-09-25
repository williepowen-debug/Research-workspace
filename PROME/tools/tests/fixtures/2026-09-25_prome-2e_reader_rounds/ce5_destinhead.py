# CE-R3-5: HEAD already contains DEST. (a) same bytes — index only deletes ORIGIN; (b) different bytes — ORIGIN deleted and
# DEST overwritten with ORIGIN's bytes (D + M). Neither is a move; both must block.
from harness import *
f = Fx("ce5")
commit(f.repo, "earlier consume", [write(f.repo, DEST, "OLD processed body\n")])
sh("git", "push", "-q", cwd=f.repo); A.record_baseline(sh("git", "rev-parse", "HEAD", cwd=f.repo).strip())
sh("git", "rm", "-q", ORIGIN, cwd=f.repo); write(f.repo, DEST, "packet body v1\n"); sh("git", "add", DEST, cwd=f.repo)
print("name-status -M100% --cached:", sh("git", "diff", "--name-status", "-M100%", "--cached", "--", ORIGIN, DEST, cwd=f.repo).strip().replace("\n", " | "))
f.freeze({DEST: ORIGIN})
show("(b) D ORIGIN + M DEST(=origin bytes) — must block", f.verify())
sh("git", "add", "PROME/SCRATCH.md", cwd=f.repo)
sh("git", "commit", "-q", "-m", "c", "--", "PROME/SCRATCH.md", ORIGIN, DEST, cwd=f.repo)
show("(b) --ref HEAD — must block", f.verify(ref="HEAD"))
# (b') with break detection would git call it a rename? show what -B does
print("with -B -M100%:", sh("git", "diff", "--name-status", "-B", "-M100%", "HEAD^", "HEAD", "--", ORIGIN, DEST, cwd=f.repo).strip().replace("\n", " | "))
f.done()
g = Fx("ce5a")
commit(g.repo, "earlier copy", [write(g.repo, DEST, "packet body v1\n")]); sh("git", "push", "-q", cwd=g.repo)
A.record_baseline(sh("git", "rev-parse", "HEAD", cwd=g.repo).strip())
sh("git", "rm", "-q", ORIGIN, cwd=g.repo); g.freeze({DEST: ORIGIN})
show("(a) DEST identical already in HEAD, only ORIGIN deleted — must block", g.verify())
g.done()
