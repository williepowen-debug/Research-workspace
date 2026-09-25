# CE-R3-4: packet only on a NON-master remote branch, with origin/master shadowed by a local branch AND a tag,
# and refs/remotes/origin/master pre-poisoned to point at the local commit; no fetch refspec configured.
from harness import *
f = Fx("ce4")
pk = "2026-09-25_from-SIDE_feature.md"; o, d = f"PROME/inbox/{pk}", f"PROME/inbox/processed/{pk}"
commit(f.repo, "SIDE -> PROME", [write(f.repo, o, "side body\n")])
sh("git", "push", "-q", "origin", "HEAD:refs/heads/feature", cwd=f.repo)          # on origin, but NOT on master
sh("git", "branch", "origin/master", "HEAD", cwd=f.repo)
sh("git", "tag", "origin/master", "HEAD", cwd=f.repo)
sh("git", "update-ref", "refs/remotes/origin/master", "HEAD", cwd=f.repo)        # poisoned tracking ref
sh("git", "config", "--unset-all", "remote.origin.fetch", cwd=f.repo)
print("ambiguous short name resolves to:", sh("git", "rev-parse", "origin/master", cwd=f.repo, check=False).strip()[:12] or "(error)")
f.move(o, d); f.freeze({d: o})
show("working-tree form — must block", f.verify(("PROME/SCRATCH.md", o, d)))
sh("git", "add", "PROME/SCRATCH.md", cwd=f.repo)
sh("git", "commit", "-q", "-m", "PROME: consume", "--", "PROME/SCRATCH.md", o, d, cwd=f.repo)
show("--ref HEAD — must block", f.verify(("PROME/SCRATCH.md", o, d), ref="HEAD"))
print("tracking ref after verify:", sh("git", "rev-parse", "refs/remotes/origin/master", cwd=f.repo).strip()[:12],
      "| bare master:", sh("git", "rev-parse", "master", cwd=f.bare).strip()[:12])
f.done()
