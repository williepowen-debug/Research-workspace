# CE-R3-7: P6 "origin/master unresolvable => exemption withheld". No remote named `origin` — but git fetch treats the word
# `origin` as a PATH when no such remote exists. An untracked nested repo at ./origin holding the unpushed packet certifies it.
from harness import *
f = Fx("ce7")
pk = "2026-09-25_from-LOCAL_unpushed.md"; o, d = f"PROME/inbox/{pk}", f"PROME/inbox/processed/{pk}"
commit(f.repo, "LOCAL -> PROME", [write(f.repo, o, "local only\n")])        # never pushed
sh("git", "remote", "remove", "origin", cwd=f.repo)
sh("git", "clone", "-q", f.repo, str(Path(f.repo) / "origin"), cwd=f.repo)  # nested repo at ./origin (untracked)
(Path(f.repo)/".git/info/exclude").write_text("origin/\n")
f.move(o, d); f.freeze({d: o})
show("no remote named origin; ./origin is a local clone — must block", f.verify(("PROME/SCRATCH.md", o, d)))
f.done()
