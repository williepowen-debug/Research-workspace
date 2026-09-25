# CE-R3-1: `git replace` makes an UNPUSHED local edit read as "bytes on origin"
from harness import *
f = Fx("ce1")
# PROME edits the packet locally and commits (never pushed): HEAD:ORIGIN = Y, origin:ORIGIN = X
write(f.repo, ORIGIN, "packet body LOCAL EDIT\n"); commit(f.repo, "PROME: local edit", [ORIGIN])
f.move(); f.freeze({DEST: ORIGIN})
show("control (no replace) — must block", f.verify())
X = sh("git", "rev-parse", f"origin/master:{ORIGIN}", cwd=f.repo).strip()
Y = sh("git", "rev-parse", f":{DEST}", cwd=f.repo).strip()
sh("git", "replace", X, Y, cwd=f.repo)
print("replace X->Y:", X[:9], "->", Y[:9])
show("with git replace — must STILL block", f.verify())
print("ls-remote truth:", sh("git", "ls-remote", "origin", "refs/heads/master", cwd=f.repo).strip()[:12])
print("true origin blob bytes (no-replace):", repr(sh("git", "--no-replace-objects", "cat-file", "-p", X, cwd=f.repo)))
f.done()
