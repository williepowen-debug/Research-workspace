# CE-R3-2: eol=crlf attribute — a GENUINE consumed move (what ships == origin bytes) is refused (false block)
from harness import *
def attrs(f):
    commit(f.repo, "attrs", [write(f.repo, ".gitattributes", "*.md text eol=crlf\n")])
f = Fx("ce2", pre_packet=attrs)
# ensure checkout form is CRLF on disk
sh("git", "rm", "-q", "--cached", ORIGIN, cwd=f.repo); os.remove(Path(f.repo)/ORIGIN); sh("git", "checkout", "HEAD", "--", ORIGIN, cwd=f.repo)
print("disk bytes:", (Path(f.repo)/ORIGIN).read_bytes())
f.move(); f.freeze({DEST: ORIGIN})
print("git diff --name-only DEST:", repr(sh("git", "diff", "--name-only", "--", DEST, cwd=f.repo)))
show("working-tree form, genuine move", f.verify())
sh("git", "add", "PROME/SCRATCH.md", cwd=f.repo)
sh("git", "commit", "-q", "-m", "PROME: consume", "--", "PROME/SCRATCH.md", ORIGIN, DEST, cwd=f.repo)
print("committed blob:", sh("git", "cat-file", "-p", f"HEAD:{DEST}", cwd=f.repo).encode())
show("--ref HEAD form (the step-10 production form)", f.verify(ref="HEAD"))
f.done()
